import sys, numpy as np
sys.path.insert(0, '.')
from d4e import C, on_shell, stress
rng = np.random.default_rng(2); n1, n2 = rng.standard_normal(3), rng.standard_normal(3)
for s in (0.1, 0.05):
    k1s, k2s = s*n1/np.linalg.norm(n1), 0.7*s*n2/np.linalg.norm(n2)
    k1, p1, _ = on_shell(k1s, 1j*s); k2, p2, _ = on_shell(k2s, 0.7j*s)
    k2o = np.array([*k2s, 1.2*k2[3]])
    for lab, kk2 in (('on', k2), ('off', k2o)):
        J = stress(k1, p1, kk2, p2); q = k1 - kk2
        vals = {nm: np.linalg.norm(Gm.T @ J) for nm, Gm in (('G(q)', C.gauge(q)), ('G(-q)', C.gauge(-q)), ('conjG(q)', np.conj(C.gauge(q))))}
        print(f"s={s} {lab}: " + "  ".join(f"{a} {b:.2e}" for a, b in vals.items()))
# Newtonian: gauge component of the line-map source and the gauge-invariant energy
k = np.array([0.02, 0, 0, 0.0]); Q = C.Q(k); M = C.line_map(k); G = C.gauge(k)
T = np.zeros(10); T[3] = 1.0; J = np.conj(M) @ T
print("static source: |G^dag J|/|J| =", np.linalg.norm(G.conj().T @ J)/np.linalg.norm(J), " per-type displacement overlaps:", np.round(np.abs(G.conj().T @ J).reshape(8, 4)[:, 3], 6))
