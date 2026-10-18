import numpy as np, sys
sys.path.insert(0, '.')
from fifth import null5, p1_edge_stress, gauge, R
rng = np.random.default_rng(9)
print("on-shell legs (lattice shell), momenta scaled by s; overlaps |f^dag J|, |J|, gauge component of J")
for t in range(3):
    n1, n2 = rng.standard_normal(3), rng.standard_normal(3)
    for s in (0.4, 0.2, 0.1, 0.05):
        k1s = s*n1/np.linalg.norm(n1); k2s = 0.7*s*n2/np.linalg.norm(n2)
        k1 = np.array([*k1s, R.lattice_kt(k1s)]); k2 = np.array([*k2s, R.lattice_kt(k2s)])
        q = k1 - k2; f, res, _ = null5(q); J = p1_edge_stress(k1, k2)
        G = gauge(q); Jg = G @ np.linalg.lstsq(G, J, rcond=None)[0]
        k1o = np.array([*k1s, 1.2*R.lattice_kt(k1s)]); Jo = p1_edge_stress(k1o, k2); fo, _, _ = null5(k1o - k2)
        print(f" t{t} s={s:.2f}: on |f.J|={abs(np.vdot(f, J)):.2e} |J|={np.linalg.norm(J):.2e} |J_gauge|={np.linalg.norm(Jg):.2e} | off |f.J|={abs(np.vdot(fo, Jo)):.2e}")
