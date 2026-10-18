"""UV-1 A12s8 / A20s8 (PREREG §5): K2c-style greedy W-matched torus search under the PRIMARY weight at beta_g = 8,
objective = lam_min of the lo-level (n=4, nw=4) overlap kernel; 4 random + 4 perturbation candidates per step.
Saves the pool; the final multi-level evaluation is done by uv1_d1.py on the saved pool.
usage: python3 uv1_search.py T K SEED [ARM BETA]"""
import numpy as np, sys, time
from uv1_lib import *
from k2b_lib import admissible, perturb
from lat2d import rand_half

T, K, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
ARM = sys.argv[4] if len(sys.argv) > 4 else 'tri'; BETA = float(sys.argv[5]) if len(sys.argv) > 5 else 8.0
G = Geom(2, T, True, 1); rng = np.random.default_rng(seed); t00 = time.time(); Fs, Bs = G.crossing_mats()
KEY = (ARM, BETA); n, nw = 4, 4
print(f"# UV-1 search torus Lt={G.Lt} K={K} seed={seed} objective arm={ARM} beta={BETA} lo=(n {n}, nw {nw})", flush=True)
WT0 = [None]
def match(u):
    v = {'x': u['x'] - 0.5 * u['x'][0].sum(), 't': u['t'].copy()}
    if WT0[0] is None: WT0[0] = v['x'][G.T - 1].sum()
    v['x'][G.T - 1, 0] += wrap(WT0[0] - v['x'][G.T - 1].sum())
    return v if admissible(G, v, DB) else None
def rand_m():
    for _ in range(5000):
        v = match(rand_half(rng, G, 0.25, DB))
        if v is not None: return v
    raise RuntimeError('no matched config')
def pert_m(u, sig):
    for _ in range(200):
        v = perturb(rng, G, u, sig, DB)
        if v is None: continue
        v = match(v)
        if v is not None: return v
    return None
def row(Ucur, u):
    r = [entry_d1(G, a, u, n, nw, 'O', Fs, Bs) for a in Ucur] + [entry_d1(G, u, u, n, nw, 'O', Fs, Bs)]
    return np.array([x[0][KEY] for x in r], complex), min(x[1] for x in r)
def bordered(L, logs):
    k = L.shape[0]; M_ = np.full((k + 1, k + 1), -np.inf + 0j); M_[:k, :k] = L
    M_[:k, k] = logs[:k]; M_[k, :k] = np.conj(logs[:k]); M_[k, k] = logs[k].real; return M_
U = []; L = np.zeros((0, 0), complex); gmin = np.inf
for _ in range(8):
    u = rand_m(); lg, g = row(U, u); L = bordered(L, lg); U.append(u); gmin = min(gmin, g)
a, b, _ = lam(normalized(L)); print(f"start k=8: lam_min {a:+.3e} min/max {a/b:+.3e} min|H| {gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)
step = 0
while len(U) < K:
    step += 1; best = None
    cands = [('rand', rand_m()) for _ in range(4)]
    for sig in (0.02, 0.05, 0.1, 0.2):
        v = pert_m(U[rng.integers(len(U))], sig)
        if v is not None: cands.append((f'pert{sig}', v))
    for tag, u in cands:
        lg, g = row(U, u); Lb = bordered(L, lg); a, b, _ = lam(normalized(Lb))
        if best is None or a < best[0]: best = (a, b, tag, u, Lb, g)
    L = best[4]; U.append(best[3]); gmin = min(gmin, best[5])
    print(f"step {step}: k={len(U)} added {best[2]:8s} lam_min {best[0]:+.3e} min/max {best[0]/best[1]:+.3e} min|H| {gmin:.3f} [{time.time()-t00:.0f}s]", flush=True)
fn = f"pool_UV1_search_{ARM}_b{BETA:g}_torus_Lt{G.Lt}_seed{seed}.npz"
np.savez(fn, ux=np.array([u['x'] for u in U]), ut=np.array([u['t'] for u in U]))
print(f"pool saved: {fn}; W-match max|W1| {max(abs(wrap(u['x'][0].sum())) for u in U):.1e} max|W_T-W_T0| {max(abs(wrap(u['x'][G.T-1].sum()-WT0[0])) for u in U):.1e}; done [{time.time()-t00:.0f}s]", flush=True)
