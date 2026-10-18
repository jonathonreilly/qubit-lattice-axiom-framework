import numpy as np, sys
sys.path.insert(0, '.')
from fifth import null5, p1_edge_stress, gauge, R, D15
U = np.ones(4)
q = np.array([0.3, -0.2, 0.25, 0.0])         # static momentum transfer
print("lowest non-gauge singular value of the Regge edge form at static q vs b:")
for b in (0.0, 1e-3, 3e-3, 1e-2, 3e-2, 0.1):
    Qe, _ = R.regge(np.eye(4) + b*np.outer(U, U))
    s = np.sort(np.linalg.svd(Qe(q), compute_uv=False)); print(f"  b={b:.0e}: sv5 = {s[4]:.3e}   sv6 = {s[5]:.3e}")
# conserved static metric source T_tt through the line map
Qe0, Mh0 = R.regge(np.eye(4)); f, _, _ = null5(q)
T = np.zeros(10); T[R.HC.index((3, 3))] = 1.0
J = Mh0(-q).T.conj().T @ T if False else np.conj(Mh0(q)) @ T     # edge source from metric source
print(f"static T_tt via line map: |f.J|/|J| = {abs(np.vdot(f, J))/np.linalg.norm(J):.3f}")
T2 = np.zeros(10); T2[R.HC.index((0, 1))] = 1.0; q2 = np.array([0, 0, 0.3, 0.0])   # conserved T_xy with q along z
J2 = np.conj(Mh0(q2)) @ T2; f2, _, _ = null5(q2)
print(f"conserved T_xy (q along z) via line map: |f.J|/|J| = {abs(np.vdot(f2, J2))/np.linalg.norm(J2):.3f}")
