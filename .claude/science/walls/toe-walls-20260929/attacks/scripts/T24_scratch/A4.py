"""T24 test A4: explicit two-node symbol, its nodes and which symmetries it breaks."""
import itertools, json
import numpy as np
rng = np.random.default_rng(4)
def d2(K):
    K = np.atleast_2d(K)
    return np.stack([np.sin(K[:, 0]), np.sin(K[:, 1]), 2 - np.cos(K[:, 0]) - np.cos(K[:, 1]) - np.cos(K[:, 2])], axis=1)
def jac(k):
    return np.array([[np.cos(k[0]), 0, 0], [0, np.cos(k[1]), 0], [np.sin(k[0]), np.sin(k[1]), np.sin(k[2])]])
g = np.linspace(-np.pi, np.pi, 33)[:-1] + 0.01
K = np.array(list(itertools.product(g, g, g)))
nodes = []
for it in range(60):
    d = d2(K)
    J = np.array([jac(k) for k in K])
    det = np.linalg.det(J)
    ok = np.abs(det) > 1e-10
    step = np.zeros_like(K)
    step[ok] = np.linalg.solve(J[ok], d[ok][..., None])[..., 0]
    nrm = np.linalg.norm(step, axis=1)
    K = K - step * np.minimum(1.0, 0.5 / np.maximum(nrm, 1e-12))[:, None]
d = d2(K)
good = np.linalg.norm(d, axis=1) < 1e-9
for k in K[good]:
    kk = (k + np.pi) % (2 * np.pi) - np.pi
    if not any(np.linalg.norm((kk - k2 + np.pi) % (2*np.pi) - np.pi) < 1e-5 for k2, _ in nodes):
        nodes.append((kk, int(np.sign(np.linalg.det(jac(kk))))))
print("A4 nodes:", [(np.round(k, 4).tolist(), c) for k, c in nodes])
Kt = rng.uniform(-np.pi, np.pi, size=(200, 3))
theta = np.abs(d2(-Kt) + d2(Kt)).max()
sgn = np.array([1, -1, -1])
C2x = np.abs(d2(Kt * sgn) - d2(Kt) * sgn).max()
sgz = np.array([-1, -1, 1])
C2z = np.abs(d2(Kt * sgz) - d2(Kt) * sgz).max()
C4 = 0
for k in Kt:
    kr = np.array([-k[1], k[0], k[2]]); dk = d2(k)[0]
    C4 = max(C4, np.abs(d2(kr)[0] - np.array([-dk[1], dk[0], dk[2]])).max())
print(f"Theta (d odd) violation {theta:.3f}; C2x violation {C2x:.3f}; C2z violation {C2z:.1e}; C4z violation {C4:.1e}")
json.dump(dict(nodes=[(np.round(k, 4).tolist(), c) for k, c in nodes], theta=float(theta), C2x=float(C2x), C2z=float(C2z), C4z=float(C4)), open("A4_results.json", "w"))
