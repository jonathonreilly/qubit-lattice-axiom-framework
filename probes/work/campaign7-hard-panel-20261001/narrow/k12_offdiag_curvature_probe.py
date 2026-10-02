"""Scratch probe: off-diagonal species curvature K_ij = -Re Tr[G P_i G P_j], G = (D+J)^-1,
4D staggered (eta^0 spatial + eta_t = (-1)^(x1+x2+x3)), L_s = 4, L_t = 4 temporal APBC.
(i) spatial periodic, P_n = projector on the plain-translation joint-character sector of corner n;
(ii) spatial APBC, P_n = projector on plane waves whose nearest corner label is n."""
import os; os.environ["OPENBLAS_NUM_THREADS"] = "1"
import itertools, numpy as np
Ls, Lt = 4, 4
X = np.array([(a, b, c, t) for t in range(Lt) for c in range(Ls) for b in range(Ls) for a in range(Ls)])
N = len(X)
def idx(x): return x[0] % Ls + Ls * (x[1] % Ls) + Ls**2 * (x[2] % Ls) + Ls**3 * (x[3] % Lt)
def T(mu, apbc):
    t = np.zeros((N, N))
    L = Lt if mu == 3 else Ls
    for i, x in enumerate(X):
        y = x.copy(); y[mu] += 1; s = 1.0
        if y[mu] == L:
            y[mu] = 0; s = -1.0 if apbc else 1.0
        t[i, idx(y)] = s
    return t
eta = [np.ones(N), (-1.0) ** X[:, 0], (-1.0) ** (X[:, 0] + X[:, 1]), (-1.0) ** (X[:, 0] + X[:, 1] + X[:, 2])]
def D(spatial_apbc):
    Ts = [T(m, spatial_apbc) for m in range(3)] + [T(3, True)]
    m = sum(eta[mu][:, None] * Ts[mu] for mu in range(4)) * 0.5
    return m - m.T
def label_projectors(spatial_apbc):
    ks = [(2 * m + 1) * np.pi / Ls for m in range(Ls)] if spatial_apbc else [2 * np.pi * m / Ls for m in range(Ls)]
    P = {}
    for kv in itertools.product(ks, repeat=3):
        if spatial_apbc:
            n = tuple(int(np.cos(k) < 0) for k in kv)          # nearest corner 0 or pi
        else:
            if not all(np.isclose(np.sin(k), 0) for k in kv): continue
            n = tuple(int(np.isclose(k, np.pi)) for k in kv)
        ps = np.exp(1j * (X[:, :3] @ np.array(kv))) / np.sqrt(Ls**3)
        P.setdefault(n, np.zeros((N, N), complex))
        P[n] += np.outer(ps, ps.conj())   # spatial plane wave (x) identity on time
    return P
masses = {(1, 0, 0): 0.3, (0, 1, 0): 0.5, (0, 0, 1): 0.7}
for apbc in (False, True):
    d = D(apbc); P = label_projectors(apbc)
    J = 0.4 * np.eye(N, dtype=complex)
    for n, m in masses.items(): J += (m - 0.4) * P[n]
    G = np.linalg.inv(d + J)
    K = lambda a, b: -np.real(np.trace(G @ P[a] @ G @ P[b]))
    hw1 = list(masses)
    off = [K(hw1[i], hw1[j]) for i in range(3) for j in range(3) if i != j]
    leak = np.linalg.norm(P[hw1[0]] @ d @ P[hw1[1]])
    print(f"spatial {'APBC' if apbc else 'periodic'}: |P_100 D P_010| = {leak:.3e};  K_ij (i!=j) = {np.round(off, 6)}")
