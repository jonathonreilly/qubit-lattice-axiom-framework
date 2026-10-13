"""R19-9 (a): cubic covariance of the glued exact photon stress under proper rotations R (signed permutations, det +1):
M^{mu nu}(R k1, R k2) = Lam^mu_a Lam^nu_b Rt M^{ab}(k1, k2) Rt^T, Lam = diag(1, R), Rt = blockdiag(R, R) (B is a pseudovector:
proper rotations only, as the axioms supply). True-position Fourier transforms (rotated frame) make R act without extra phases."""
import numpy as np, lib199 as L
rng = np.random.default_rng(11); r = 0.1
Rs = {'C4z': np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1.]]), 'C3(111)': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.]]),
      'C2(110)': np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1.]])}
for name, R in Rs.items():
    Lam = np.eye(4); Lam[1:, 1:] = R; Rt = np.kron(np.eye(2), R); mx = 0.0
    for t in range(300):
        if t % 2: k1, k2 = rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3)
        else:
            v1, v2 = rng.normal(size=3), rng.normal(size=3); k1 = v1/np.linalg.norm(v1)*2*r*rng.uniform(); k2 = v2/np.linalg.norm(v2)*2*r*rng.uniform()
        A = L.glued(R @ k1, R @ k2, r); B = np.einsum('ma,nb,xy,abyz,wz->mnxw', Lam, Lam, Rt, L.glued(k1, k2, r), Rt)
        mx = max(mx, np.abs(A - B).max())
    print(f'{name}: max |M(Rk1,Rk2) - R.M(k1,k2)| over 300 pairs (half in the corner region) = {mx:.2e}')
