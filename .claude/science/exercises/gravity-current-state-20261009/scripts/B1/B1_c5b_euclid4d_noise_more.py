"""B1 check c5: the finite-valency loophole of BHS. A 4D EUCLIDEAN Poisson point set (O(4)- and SL(4)-invariant
in law, finite valency: Christ-Friedberg-Lee-type random lattice). Free massive scalar with R3/K1's
proper-distance kernel (R = 1.8, w = (1-d^2/R^2)^4, pairs chosen by current proper distance), boson zero-point
functional, exact eigen-perturbation derivatives (reuses the packet's e23_core.derivs, which is dimension-agnostic).
Measures per-realization TT tadpole E' and stiffness E'' per site, and sd*sqrt(N) vs N (flat = white = S(0)>0).
4D TT-type directions: diag(1,-1,0,0)/sqrt2 (E-type) and off-diagonal (0,1) (T-type); in 4D Euclidean all 9
traceless directions are equivalent in law.
"""
import sys, time, numpy as np
sys.path.insert(0, '/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-current-state-20261009/scripts/E23')
import e23_core as C

h1 = np.diag([1., -1, 0, 0]) / np.sqrt(2)
h2 = np.zeros((4, 4)); h2[0, 1] = h2[1, 0] = 1 / np.sqrt(2)
h3 = np.diag([1., 1, -1, -1]) / 2.0
DIRS4 = [h1, h2, h3]
rng = np.random.default_rng(777)
fns = [C.boson_fns(1.0), C.boson_fns(0.04)]
print("L  N   nreal | m2=1: mean E''(dir1) sd*sqrtN E''(d1,d2,d3) sd*sqrtN E'(d1) | m2=0.04: sd*sqrtN E''(d1)")
for L, nreal in [(4, 200), (5, 120), (6, 80), (7, 40), (8, 14)]:
    rows = []
    t0 = time.time()
    for r in range(nreal):
        n = rng.poisson(L**4)
        X = rng.uniform(0, L, size=(n, 4))
        I, J, D = C.pairs_sparse(X, float(L), 'pd')
        out, lam = C.derivs(n, I, J, D, 'pd', fns, dirs=DIRS4)
        rows.append((n, out))
    Ns = np.array([r[0] for r in rows]); Nm = Ns.mean()
    E2 = np.array([r[1][0, :, 1] for r in rows]); E1 = np.array([r[1][0, :, 0] for r in rows])
    E2b = np.array([r[1][1, :, 1] for r in rows])
    sd2 = E2.std(axis=0, ddof=1) * np.sqrt(Nm); sd1 = E1.std(axis=0, ddof=1) * np.sqrt(Nm)
    print(f"{L}  {Nm:6.0f} {nreal:3d} | {E2[:,0].mean():+.4f}+-{E2[:,0].std(ddof=1)/np.sqrt(nreal):.4f}  "
          f"{sd2[0]:.3f} {sd2[1]:.3f} {sd2[2]:.3f}   {sd1[0]:.3f} | {E2b[:,0].std(ddof=1)*np.sqrt(Nm):.3f}"
          f"   ({time.time()-t0:.0f}s)", flush=True)
# (fit appended) -- pooled exponent of sd(E'') vs N over the printed rows is done by hand in the report
