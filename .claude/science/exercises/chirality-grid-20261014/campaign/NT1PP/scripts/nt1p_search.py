"""NT-1' pool P-A: K2c wsearch rule (W-matched greedy most-negative search) on the vector-like O (m = 0.05) kernel, hard
weight delta = 0.6, Lx = 4 open, antiperiodic x, margin 0.55, LOW quadrature Duffy n = 3.  usage: python3 nt1p_search.py T K seed"""
import numpy as np, sys, time
import k2c_lib
from k2c_lib import Pool, normalized, lam, perturb, admissible, max_bulk, DB
from lat2d import Geom, rand_half

T, K, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
G = Geom(4, T, False, -1); Lx = 4; rng = np.random.default_rng(seed); t00 = time.time(); s0 = 0.25; n = 3
print(f"# NT-1' P-A wsearch op=O weight=hard Lx=4 Lt={2*T} K={K} seed={seed} delta={k2c_lib.DELTA} margin {DB} n={n}", flush=True)
def match(u): return {'x': u['x'] - u['x'][0].sum() / Lx, 't': u['t'].copy()}
def rand_m(): return match(rand_half(rng, G, s0, DB))
def pert_m(u, sig):
    v = perturb(rng, G, u, sig, DB)
    return None if v is None else match(v)
P = Pool(G, n, None, 'O', 'hard')
for _ in range(8):
    u = rand_m(); logs, g = P.row(u); P.add(u, logs, g)
a, b, _ = lam(normalized(P.L)); print(f"start k=8: lam_min {a:+.3e} min/max {a/b:+.3e} min|H| {P.gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)
step = 0
while len(P.U) < K:
    step += 1; cands = [('rand', rand_m()) for _ in range(4)]
    for sig in (0.02, 0.05, 0.1, 0.2):
        v = pert_m(P.U[rng.integers(len(P.U))], sig)
        if v is not None: cands.append((f'pert{sig}', v))
    best = None
    for (tag, u) in cands:
        logs, g = P.row(u); a, b, _ = lam(normalized(P.bordered(logs)))
        if best is None or a < best[0]: best = (a, b, tag, u, logs, g)
    P.add(best[3], best[4], best[5])
    print(f"step {step}: k={len(P.U)} added {best[2]:8s} lam_min {best[0]:+.3e} min/max {best[0]/best[1]:+.3e} min|H| {P.gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)
fn = f"pool_NT1P_PA_wsearchO_Lx4_Lt{2*T}_seed{seed}.npz"
np.savez(fn, ux=np.array([u['x'] for u in P.U]), ut=np.array([u['t'] for u in P.U]))
print(f"saved {fn}; max|W1| {max(abs(u['x'][0].sum()) for u in P.U):.1e}; max bulk plaquette {max(max_bulk(G, u) for u in P.U):.4f} [{time.time()-t00:.0f}s]")
