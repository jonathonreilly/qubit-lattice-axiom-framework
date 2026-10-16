"""Part 2e: bosonic class (class 0, permutation action; class 1 is phase-gauge equivalent).
Commutant = Bose-Mesner algebra of the cube = span of the isotypic projectors for A1+A2+T1+T2.
Two-layer walk W = G uBt G^dag uA, uA = sum_r e^{i a_r} P_r, uBt = sum_r e^{i b_r} P_r.
First-order splitting of each k=0 level, isotropy over directions. NUMERICAL (floating point)."""
import numpy as np
from walks import *
from part2_cone import dirs
X = [np.diag([v[j] - 0.5 for v in corners]) for j in range(3)]
u = np.array([v - 0.5 for v in corners])
f_A1 = np.ones(8) / np.sqrt(8)
f_A2 = np.array([(-1) ** v.sum() for v in corners]) / np.sqrt(8)
f_T1 = [u[:, j] / np.sqrt(2) for j in range(3)]
f_T2 = [u[:, (j + 1) % 3] * u[:, (j + 2) % 3] * 4 / np.sqrt(8) * 2 for j in range(3)]
f_T2 = [f / np.linalg.norm(f) for f in f_T2]
Ps = {"A1": np.outer(f_A1, f_A1), "A2": np.outer(f_A2, f_A2),
      "T1": sum(np.outer(f, f) for f in f_T1), "T2": sum(np.outer(f, f) for f in f_T2)}
assert np.allclose(sum(Ps.values()), np.eye(8))
D = class_D(0)
for P in Ps.values():
    assert all(np.allclose(d @ P, P @ d) for d in D.values())
rng = np.random.default_rng(7)
for t in range(3):
    a = rng.uniform(0, 2 * np.pi, 4); b = rng.uniform(0, 2 * np.pi, 4)
    uA = sum(np.exp(1j * a[i]) * P for i, P in enumerate(Ps.values()))
    uB = sum(np.exp(1j * b[i]) * P for i, P in enumerate(Ps.values()))
    A = two_layer(uA, uB)
    print(f"trial {t}: covariance {covariance_defect(A, D):.1e} unitarity {unitarity_defect(A):.1e}")
    for name, P in Ps.items():
        lam = np.exp(1j * (a[list(Ps).index(name)] + b[list(Ps).index(name)]))
        w, V = np.linalg.eigh(P); Vp = V[:, w > 0.5]
        hs = [(1j / lam) * Vp.conj().T @ (1j * (X[j] @ uB - uB @ X[j]) @ uA) @ Vp for j in range(3)]
        sp = np.array([np.sort(np.linalg.eigvalsh(sum(n[j] * hs[j] for j in range(3)))) for n in dirs(200)])
        print(f"  {name}: omega0={-np.angle(lam):+.4f}, velocities(100)={np.round(np.linalg.eigvalsh(hs[0]),5)},"
              f" spread over directions {np.round(sp.max(0)-sp.min(0),8)}")
