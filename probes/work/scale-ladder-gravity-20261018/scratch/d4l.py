import sys, numpy as np
sys.path.insert(0, '.')
from d4e import C, on_shell, stress
rng = np.random.default_rng(2); n1, n2 = rng.standard_normal(3), rng.standard_normal(3)
nt = len(C.types)
for s in (0.1, 0.05, 0.025):
    k1s, k2s = s*n1/np.linalg.norm(n1), 0.7*s*n2/np.linalg.norm(n2)
    k1, p1, _ = on_shell(k1s, 1j*s); k2, p2, _ = on_shell(k2s, 0.7j*s)
    out = []
    for kk2 in (k2, np.array([*k2s, 1.2*k2[3]])):
        J = stress(k1, p1, kk2, p2); q = k1 - kk2; G = C.gauge(q)
        Ga = sum(G[:, 4*t:4*t+4] for t in range(nt))      # acoustic: same xi on every vertex type (Bloch phases already in G)
        out.append((np.linalg.norm(Ga.T @ J), np.linalg.norm(G.T @ J), np.linalg.norm(J)))
    (a_on, g_on, j_on), (a_off, g_off, j_off) = out
    print(f"s={s}: acoustic on {a_on:.2e} off {a_off:.2e} | all displacements on {g_on:.2e} | |J| {j_on:.2e}")
