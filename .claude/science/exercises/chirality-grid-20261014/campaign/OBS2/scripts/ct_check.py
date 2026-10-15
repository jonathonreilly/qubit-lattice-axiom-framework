"""OBS-2: the cubic-invariant counterterm pair at the hw1 corners. H = (1+alpha) sum_a sigma_a sin p_a + beta sum_a sigma_a sin p_a (cos p_b + cos p_c).
Checks: (1) invariance under the 24 proper cubic rotations with spin lift; (2) corner velocities v_par, v_perp at e_x, e_y, e_z and the origin."""
import numpy as np, itertools
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex); SIG = [sx, sy, sz]
def H(p, al, be):
    out = np.zeros((2, 2), complex)
    for a in range(3):
        b, c = [x for x in range(3) if x != a]
        out += SIG[a] * np.sin(p[a]) * ((1 + al) + be * (np.cos(p[b]) + np.cos(p[c])))
    return out
def su2(R):   # spin lift of a proper rotation R (SO(3)) via axis-angle
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if abs(ang) < 1e-12: return np.eye(2)
    if abs(ang - np.pi) < 1e-9:
        n = np.sqrt(np.clip((np.diag(R) + 1) / 2, 0, None)); i = np.argmax(n)
        n = R[:, i] + np.eye(3)[:, i]; n /= np.linalg.norm(n)
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    return np.cos(ang / 2) * np.eye(2) - 1j * np.sin(ang / 2) * sum(n[a] * SIG[a] for a in range(3))
rots = [np.array(M) for perm in itertools.permutations(range(3)) for sg in itertools.product((1, -1), repeat=3)
        for M in [np.array([[sg[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)], float)] if np.linalg.det(M) > 0]
rng = np.random.default_rng(1); mx = 0
for R in rots:
    U = su2(R)
    for _ in range(5):
        p = rng.uniform(-np.pi, np.pi, 3)
        mx = max(mx, np.abs(U @ H(p, 0.1, 0.3) @ U.conj().T - H(R @ p, 0.1, 0.3)).max())
print(f"{len(rots)} proper rotations; max |U H(p) U^dag - H(Rp)| = {mx:.1e}")
dq = 1e-6
for name, e in (('e_x', [np.pi, 0, 0]), ('e_y', [0, np.pi, 0]), ('e_z', [0, 0, np.pi]), ('origin', [0, 0, 0])):
    e = np.array(e, float); v = []
    for a in range(3):
        d = np.zeros(3); d[a] = dq
        v.append(np.linalg.eigvalsh(H(e + d, 0.0, 0.05)).max() / dq)
    print(f"  alpha=0, beta=0.05 at {name}: |v| per axis = {np.round(v, 6)}  (expect par 1+2beta = 1.1 at hw1 axis, perp 1; origin 1+2beta isotropic)")
