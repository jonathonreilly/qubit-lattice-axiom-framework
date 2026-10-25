"""K2c-A/B (PREREG.md): K2b's greedy most-negative-direction search with a selectable crossing weight (hard = X3's measure,
tri = K2's Fejer, power reference) and margin-admissible pools (bulk plaquettes <= 0.55).
usage: python3 k2c_search.py MODE GEOM T K SEED WEIGHT [OP]   MODE search|gsearch  GEOM open|torus  WEIGHT hard|tri  OP O|DWF4"""
import numpy as np, sys, time
from k2c_lib import *

mode, gname, T, K, seed, weight = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
matched = mode.startswith('w'); bmode = mode[1:] if matched else mode     # V2: W-matched modes wsearch / wgsearch
OP = sys.argv[7] if len(sys.argv) > 7 else 'O'
s0 = 0.25
if gname == 'open':
    G = Geom(2, T, False, -1); qlo, qhi, q3 = (16, None), (32, None), (48, None)
else:
    G = Geom(2, T, True, 1); qlo, qhi, q3 = (6, 4), (8, 6), (10, 8)
rng = np.random.default_rng(seed); t00 = time.time()
print(f"# K2c {mode} op={OP} weight={weight} {gname} Lx={G.Lx} Lt={G.Lt} K={K} seed={seed} delta={DELTA} margin(bulk<= {DB}) quad lo={qlo} hi={qhi} third={q3}", flush=True)

WT0 = [None]
def match(u):
    """V2: shift to W(slice 1) = 0 (holonomy shift); torus: also W(slice T) = WT0 via x-link (T, 0); None if margin breaks."""
    v = {'x': u['x'] - 0.5 * u['x'][0].sum(), 't': u['t'].copy()}
    if G.torus:
        if WT0[0] is None: WT0[0] = v['x'][G.T - 1].sum()
        v['x'][G.T - 1, 0] += wrap(WT0[0] - v['x'][G.T - 1].sum())
        if not admissible(G, v, DB): return None
    return v
def rand_m():
    if not matched: return rand_half(rng, G, s0, DB)
    for _ in range(5000):
        v = match(rand_half(rng, G, s0, DB))
        if v is not None: return v
    raise RuntimeError('no matched config')
def pert_m(u, sig):
    for _ in range(200):
        v = perturb(rng, G, u, sig, DB)
        if v is None: continue
        if not matched: return v
        v = match(v)
        if v is not None: return v
    return None
U0 = [rand_m() for _ in range(8)]
P = Pool(G, qlo[0], qlo[1], OP, weight); PW = Pool(G, qlo[0], qlo[1], 'W', weight)
for u in U0:
    logs, g = P.row(u); P.add(u, logs, g)
    if bmode == 'gsearch': lw, _ = PW.row(u); PW.add(u, lw, np.inf)
a, b, _ = lam(normalized(P.L))
print(f"start k={len(P.U)}: lam_min {a:+.3e} min/max {a/b:+.3e} min|H| {P.gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)
step = 0
while len(P.U) < K:
    step += 1; cands = []
    for _ in range(4 if matched else 3): cands.append(('rand', rand_m()))
    for sig in ((0.02, 0.05, 0.1, 0.2) if matched else (0.02, 0.05, 0.1)):
        v = pert_m(P.U[rng.integers(len(P.U))], sig)
        if v is not None: cands.append((f'pert{sig}', v))
    if not matched:
        for _ in range(2): cands.append(('hol', holonomy_shift(rng, P.U[rng.integers(len(P.U))])))
    best = None
    for (tag, u) in cands:
        logs, g = P.row(u); Zb = normalized(P.bordered(logs)); a, b, _ = lam(Zb)
        if bmode == 'gsearch':
            lw, _ = PW.row(u); obj = gen_ratio(Zb, normalized(PW.bordered(lw)), 1e-6)
        else:
            lw = None; obj = a
        if best is None or obj < best[0]: best = (obj, a, b, tag, u, logs, g, lw)
    P.add(best[4], best[5], best[6])
    if bmode == 'gsearch': PW.add(best[4], best[7], np.inf)
    print(f"step {step}: k={len(P.U)} added {best[3]:8s} objective {best[0]:+.3e} lam_min {best[1]:+.3e} min/max {best[1]/best[2]:+.3e} min|H| {P.gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)

U = P.U; k = len(U)
fn = f"pool_K2c_{mode}_{weight}_{OP}_{gname}_Lt{G.Lt}_seed{seed}.npz"
np.savez(fn, ux=np.array([u['x'] for u in U]), ut=np.array([u['t'] for u in U]))
if matched:
    print(f"W-match check: max|W1| {max(abs(wrap(u['x'][0].sum())) for u in U):.1e}" + (f", max|W_T - W_T0| {max(abs(wrap(u['x'][G.T-1].sum() - WT0[0])) for u in U):.1e}" if G.torus else ""))
print(f"pool saved: {fn}; max bulk |plaquette| over pool {max(max_bulk(G, u) for u in U):.4f} (margin limit {DB})", flush=True)
res = {}
rs = np.random.default_rng(99); pairs = set()
while len(pairs) < min(24, k * (k - 1) // 2):
    a_ = int(rs.integers(k)); b_ = int(rs.integers(k))
    if a_ != b_: pairs.add((min(a_, b_), max(a_, b_)))
for op in ([OP, 'W', 'PG'] if OP != 'W' else ['W', 'PG']):
    Zlo, glo = (normalized(P.L), P.gmin) if op == OP else full_kernel(G, U, qlo[0], qlo[1], op, weight)
    Zhi, ghi = full_kernel(G, U, qhi[0], qhi[1], op, weight)
    q = np.abs(Zhi - Zlo).max(); qq3 = subset_change(G, U, Zhi, q3[0], q3[1], op, weight, sorted(pairs))
    E = k * max(q, qq3) + 1e-13; a, b, ev = lam(Zhi)
    res[op] = (Zhi, a, b, ev, q, qq3, E, min(glo, ghi))
    print(f"FINAL {op:3s} k={k}: lam_min {a:+.4e} min/max {a/b:+.4e} q {q:.1e} q3 {qq3:.1e} E {E:.1e} | certified-negative {a < -10*E} | PSD-within-error {a > -10*E}"
          f" | min|H| {min(glo, ghi):.3f} | lowest {np.array2string(ev[:4], precision=3)} max {ev[-1]:.3f} [{time.time()-t00:.0f}s]", flush=True)
Zo = res[OP][0]; Zw = res['W'][0]
try:
    print(f"   gen-ratio min ({OP} vs W, W range > 1e-8): {gen_ratio(Zo, Zw):+.3e}")
except Exception as ex:
    print("   gen-ratio failed", ex)
clean = res[OP][4] < 1e-6 and res[OP][7] > 0.1 and max(max_bulk(G, u) for u in U) <= DB + 1e-12
print(f"SUMMARY {gname} Lt={G.Lt} {mode} weight={weight} op={OP} seed={seed}: clean {clean} | {OP} lam_min {res[OP][1]:+.3e} (E {res[OP][6]:.1e}) cert-neg {res[OP][1] < -10*res[OP][6]}"
      f" | W lam_min {res['W'][1]:+.3e} cert-neg {res['W'][1] < -10*res['W'][6]} | PG lam_min {res['PG'][1]:+.3e} cert-neg {res['PG'][1] < -10*res['PG'][6]}")
print(f"done [{time.time()-t00:.0f}s]", flush=True)
