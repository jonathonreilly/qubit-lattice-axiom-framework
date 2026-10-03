#!/usr/bin/env python3
"""A22 task 3, sector version of heat.py (same model): half-filled sector basis, SWAP_b as index permutations.
usage: heat2.py L T theta1,theta2,...   [prints window-averaged heating fraction, t* where it first exceeds 0.5]"""
import sys, time, numpy as np
from itertools import combinations
from scipy.sparse.linalg import eigsh, LinearOperator

L = int(sys.argv[1]); T = int(sys.argv[2]); thetas = [float(x) for x in sys.argv[3].split(",")]
m = 0.3; import os; vs = float(os.environ.get("VSCALE", "1")); Jz = 0.5 * vs; J2 = 0.7 * vs
wo = 1 - 2 * m / np.pi
states = np.array(sorted(sum(1 << (L - 1 - s) for s in c) for c in combinations(range(L), L // 2)), dtype=np.int64)
D = states.size
bits = (states[:, None] >> (L - 1 - np.arange(L))[None, :]) & 1
Vdiag = (Jz * sum(bits[:, s] * bits[:, (s + 1) % L] for s in range(L)) +
         J2 * sum(bits[:, s] * bits[:, (s + 2) % L] for s in range(L))).astype(float)
bond_w = np.array([1.0 if s % 2 == 0 else wo for s in range(L)])
perms = []
for s in range(L):
    t = (s + 1) % L
    bs, bt = bits[:, s], bits[:, t]
    flipped = states ^ (((bs ^ bt) << (L - 1 - s)) | ((bs ^ bt) << (L - 1 - t)))
    perms.append(np.searchsorted(states, flipped))


def H0(psi):
    out = Vdiag * psi
    for s in range(L):
        out = out + bond_w[s] * psi[perms[s]]
    return out


def layer(psi, a, parity):
    c, sn = np.cos(a), np.sin(a)
    for s in range(parity, L, 2):
        psi = c * psi - 1j * sn * psi[perms[s]]
    return psi


op = LinearOperator((D, D), matvec=H0, dtype=complex)
Egs, vgs = eigsh(op, k=1, which="SA", v0=np.random.default_rng(0).normal(size=D) + 0j, tol=1e-10)
E_gs = Egs[0]
diagH = Vdiag + sum(bond_w[s] * (bits[:, s] == bits[:, (s + 1) % L]) for s in range(L))
E_inf = diagH.mean()
print(f"L={L} dim={D}; m={m} Jz={Jz} J2={J2}; E_gs/L={E_gs/L:.4f} E_inf/L={E_inf/L:.4f}")
for th in thetas:
    t0 = time.time()
    psi = vgs[:, 0].astype(complex)
    phV = np.exp(-1j * th * Vdiag)
    ts, es = [], []
    for t in range(1, T + 1):
        psi = layer(psi, th, 0); psi = layer(psi, th * wo, 1); psi = phV * psi
        if t % 5 == 0 or t < 20:
            ts.append(t); es.append((np.vdot(psi, H0(psi)).real - E_gs) / (E_inf - E_gs))
    ts = np.array(ts); es = np.array(es)
    wins = []; tt = 20
    while tt <= T:
        sel = (ts > tt / 2) & (ts <= tt); wins.append((tt, es[sel].mean())); tt *= 2
    tstar = next((tt for tt, e in wins if e > 0.5), None)
    # heating rate: least-squares slope of e(t) on [50, t_end], t_end = first time the 50-tick running mean exceeds 0.45
    rm = np.convolve(es, np.ones(10) / 10, mode="same")
    over = np.nonzero((ts > 100) & (rm > 0.45))[0]
    t_end = ts[over[0]] if over.size else ts[-1]
    sel = (ts >= 50) & (ts <= t_end)
    slope = np.polyfit(ts[sel], es[sel], 1)[0] if sel.sum() > 5 else float('nan')
    print(f"   rate fit on [50,{t_end}]: de/dt = {slope:.3e} per tick ; e(50..100) mean {es[(ts>=50)&(ts<=100)].mean():.3f}")
    print(f"theta={th:.4f} (1/theta={1/th:.3f}): " + "  ".join(f"{tt}:{e:.3f}" for tt, e in wins) +
          f"   | t*(>0.5) = {tstar}   [{time.time()-t0:.1f}s]")
    sys.stdout.flush()
