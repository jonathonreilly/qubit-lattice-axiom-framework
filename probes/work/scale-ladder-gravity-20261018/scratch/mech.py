import sys, numpy as np
sys.path.insert(0, 'scripts')
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R
Qe, Mh = R.regge(np.eye(4))
rng = np.random.default_rng(1)
for _ in range(5):
    p = rng.uniform(-2, 2, 4); L = np.sum(4*np.sin(p/2)**2)
    ev = np.sort(np.linalg.eigvalsh(0.5*(Qe(p)+Qe(p).conj().T)))
    print(f"phat^2={L:.5f}", "nonzero eig/phat^2:", np.array2string(ev[5:]/L, precision=5))
    # determinant-type invariant: product of nonzero eigenvalues / phat^(2m)
    nz = ev[5:]; print("   prod(nz)/phat^4 =", np.prod(nz)/L**2, "  prod/phat^20", np.prod(nz)/L**10)
