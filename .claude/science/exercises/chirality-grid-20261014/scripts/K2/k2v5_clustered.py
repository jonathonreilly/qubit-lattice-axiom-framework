"""Follow-up V5 (PREREG.md): clustered configuration sets on the torus (G3p) and open (G1p) Lt = 12 lattices."""
import numpy as np, sys, time
from lat2d import Geom, rand_half, kernel, mineig, logdet_batch, wrap
geom_name = sys.argv[1]; delta = 0.6; k = 8
G = {'G3p': Geom(2, 6, True, 1), 'G1p': Geom(2, 6, False, -1)}[geom_name]
n_lo, n_hi, nw_lo, nw_hi = (6, 8, 10, 16) if G.torus else (16, 32, None, None)
rng = np.random.default_rng(777)
def admissible(u):
    T, Lx = G.T, G.Lx
    for t in range(T - 1):
        for x in range(Lx):
            if abs(wrap(u['x'][t, x] + u['t'][t, (x + 1) % Lx] - u['x'][t + 1, x] - u['t'][t, x])) >= delta: return False
    return True
print(f"# V5 {geom_name}: clustered sets, base s=0.25, perturbation 0.05, delta={delta}, n=({n_lo},{n_hi}) nw=({nw_lo},{nw_hi})")
for rep in range(3):
    t0 = time.time(); base = rand_half(rng, G, 0.25, delta); U = []
    while len(U) < k:
        u = {'x': base['x'] + rng.normal(0, 0.05, base['x'].shape), 't': base['t'] + rng.normal(0, 0.05, base['t'].shape)}
        if admissible(u): U.append(u)
    out = {}
    for op in ['W', 'O']:
        Zl, gl, _ = kernel(G, U, delta, n_lo, 'tri', op, nw_lo); Zh, gh, _ = kernel(G, U, delta, n_hi, 'tri', op, nw_hi)
        out[op] = (mineig(Zh), np.abs(Zh - Zl).max(), min(gl, gh), np.linalg.eigvalsh(0.5 * (Zh + Zh.conj().T)))
    O, W = out['O'], out['W']; clean = O[1] < 1e-5 and O[2] > 0.1 and W[1] < 1e-5
    print(f"set {rep}: OVERLAP min/max {O[0]:+.3e} q {O[1]:.1e} min|H_W| {O[2]:.3f} | WILSON min/max {W[0]:+.3e} q {W[1]:.1e} | clean {clean} | {time.time()-t0:.0f}s")
    print(f"   overlap eigenvalues: {np.array2string(O[3], precision=3)}"); sys.stdout.flush()
print("done")
