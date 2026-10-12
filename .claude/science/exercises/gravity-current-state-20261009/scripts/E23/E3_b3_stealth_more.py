"""E3 (b3): more stealthy (chi = 0.30) realizations for the noise scaling: L = 6 (+60), 8 (+36), 10 (+24), 12 (8)."""
import numpy as np, sys, time
sys.argv = ['x', 'stealth', '0.3']
src = open('E3_b_hyperuniform.py').read().split('for Lb, nr in PLAN.items():')[0]
exec(src)
rng = np.random.default_rng(4321)
for Lb, nr in {6: 60, 8: 36, 10: 24, 12: 8}.items():
    t0 = time.time(); acc = []
    for _ in range(nr):
        X, chi_eff, K, fval = stealthy(Lb, 0.3)
        I, J, D = c.pairs_sparse(X, Lb, 'pd'); out, _ = c.derivs(len(X), I, J, D, 'pd', fns); acc.append(out)
    A = np.array(acc); np.save(f"E3_b3_stealth_L{Lb}.npy", A); print(f"L={Lb} done n={nr} [{time.time()-t0:.0f}s] last Phi/N={fval:.1e}", flush=True)
