#!/usr/bin/env python3
"""A19 Monte Carlo quantum trajectories: record tracks of a registered Dirac mover (supplied toy).

usage: mc_grid.py CUT [m K0 T B]   CUT in {site, cell, g1, g4, g16, g64, b32, b128, su}
  site : sharp single-site cut (w = delta)            cell : sharp cut onto the 2-site cell (A5 two-component site)
  gS   : Gaussian (unsharp) cut, std S sites          bS   : sharp cut onto aligned blocks of S sites
  su   : sharp single-site cut, single-use sites (one record per site; no-record update reshapes)
Prints, per registration rate g: E[Y(t)]/t at checkpoints (inertia: = v0), Var Y(t), LS slope stats,
first/second-half slope correlation, residual about own line, final momentum (mean K, sd K, + band weight),
and for sharp site cuts the record-parity direction correlation vs the exact value.
"""
import sys, time
import numpy as np
from core1d import step, packet, vgroup, momentum_stats, Registrar, track_metrics
from exact_sharp import sharp_stats

cut = sys.argv[1]
m = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
K0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
T = int(sys.argv[4]) if len(sys.argv) > 4 else 600
B = int(sys.argv[5]) if len(sys.argv) > 5 else 200
gs = [float(x) for x in sys.argv[6].split(",")] if len(sys.argv) > 6 else [0.01, 0.03, 0.1, 0.3, 1.0]
M = 2048
w0 = 20.0
j0 = 700
v0 = vgroup(K0, m)
chk = [T // 8, T // 4, T // 2, T]

if cut == "site":
    kw = dict(kind="gauss", sig=0.0)
elif cut == "cell":
    kw = dict(kind="block", s=2)
elif cut == "su":
    kw = dict(kind="gauss", sig=0.0, single_use=True)
elif cut.startswith("g"):
    kw = dict(kind="gauss", sig=float(cut[1:]))
elif cut.startswith("b"):
    kw = dict(kind="block", s=int(cut[1:]))
else:
    raise SystemExit("bad cut")

print(f"cut={cut} {kw}  m={m} K0={K0} v0=v(K0)={v0:.5f} cells/tick  T={T} B={B} M={M} cells  packet w0={w0}")
print("cols: g | E[Y(t)]/t at t=" + ",".join(map(str, chk)) + " | sd Y(t) | slope mean, sd, rmse vs v0 | "
      "half-slopes s1,s2, corr12, same-sign | resid | <#reg> | final K mean, sd, plus-band wt")
t0 = time.time()
for g in gs:
    rng = np.random.default_rng(12345 + int(1000 * g))
    a0, b0 = packet(M, m, K0, w0, j0)
    a = np.repeat(a0[None], B, axis=0)
    b = np.repeat(b0[None], B, axis=0)
    reg = Registrar(B, M, g, rng=rng, x0_cells=j0 + 0.25, **kw)
    for t in range(1, T + 1):
        a, b = step(a, b, m)
        a, b = reg.apply(a, b, t)
    met = track_metrics(reg.tracks, T, v0, chk)
    Km, Kv, plus = momentum_stats(a, b, m)
    line = (f"g={g:<5} | " + " ".join(f"{x:+.4f}" for x in met["meanY_over_t"]) + " | "
            + " ".join(f"{np.sqrt(x):7.2f}" for x in met["varY"]) + " | "
            + f"{met['slope_mean']:+.4f} {met['slope_sd']:.4f} {met['slope_rmse_v0']:.4f} | "
            + f"{met['s1_mean']:+.4f} {met['s2_mean']:+.4f} {met['corr12']:+.3f} {met['samesign12']:.3f} | "
            + f"{met['resid_rms']:7.2f} | {reg.count.mean():6.1f} | "
            + f"{np.mean(Km):+.4f} {np.sqrt(np.mean(Kv) + np.var(Km)):.4f} {np.mean(plus):.4f}")
    print(line)
    if cut in ("site", "su"):
        # direction (sublattice) correlation of consecutive records vs exact r(g, m)
        prods, cdy, dy2 = [], [], []
        for tr in reg.tracks:
            ys = np.array([p[1] for p in tr[1:]])
            if ys.size >= 2:
                c = np.where(np.isclose(ys % 1.0, 0.0), 1.0, -1.0)   # integer cell = right sublattice
                prods.extend(list(c[1:] * c[:-1]))
                d = np.diff(ys)
                cdy.extend(list(c[:-1] * d))
                dy2.extend(list(d ** 2))
        prods, cdy, dy2 = map(np.array, (prods, cdy, dy2))
        ex = sharp_stats(m, g)
        print(f"      parity corr r_MC = {prods.mean():+.4f} +- {prods.std()/np.sqrt(max(prods.size,1)):.4f} "
              f"(n={prods.size}) vs exact r = {ex['r']:+.4f};  exact D_track = {ex['D']:.3f} vs Var Y(T)/T = {met['varY'][-1]/T:.3f}")
        print(f"      per segment: mu_MC = {cdy.mean():.4f} +- {cdy.std()/np.sqrt(cdy.size):.4f} vs exact {ex['mu']:.4f}; "
              f"M2_MC = {dy2.mean():.3f} +- {dy2.std()/np.sqrt(dy2.size):.3f} vs exact {ex['M2']:.3f}")
    sys.stdout.flush()
print(f"elapsed {time.time() - t0:.1f} s")
