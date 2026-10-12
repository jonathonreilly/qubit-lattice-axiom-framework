"""K1 checks: (1) U(1) Ward identity for the metric-coupled photon (M(h) shat = 0 for random constant h, exact);
(2) U(1) Ward identity of the fermion current, Pi_{mu nu}(q=0) = 0 (bubble + tadpole) with the same integrator;
(3) W(B4) covariance of the fermion h-bilinear: B(Rq) = rho(R)^T B(q) rho(R) for random signed permutations, on-grid q;
(4) even-ness B(q) = B(-q).   Usage: python ward_checks.py
"""
import numpy as np, itertools
import loop_fermion as lf
from photon_q0 import P6, sym
rng = np.random.default_rng(11)
# (1) photon gauge invariance with metric
def Mphoton(hv, p):
    g = np.eye(4) + sym(hv); gi = np.linalg.inv(g); sg = np.sqrt(np.linalg.det(g))
    sh = 2 * np.sin(p / 2); co = np.cos(p / 2)
    R = np.zeros((6, 4))
    for I, (m, n) in enumerate(P6):
        R[I, n] += sh[m]; R[I, m] -= sh[n]
    M = np.zeros((4, 4))
    for I, (m, n) in enumerate(P6):
        for J, (r, s) in enumerate(P6):
            C = np.prod([co[a] for a in set((m, n)) ^ set((r, s))]) if set((m, n)) ^ set((r, s)) else 1.0
            M += 2 * sg * (gi[m, r] * gi[n, s] - gi[m, s] * gi[n, r]) * C * np.outer(R[I], R[J])
    return M, sh
worst = 0
for t in range(200):
    M, sh = Mphoton(0.1 * rng.normal(size=10), rng.uniform(-np.pi, np.pi, 4))
    worst = max(worst, np.abs(M @ sh).max() / np.abs(M).max())
print(f"(1) photon: max |M(h) shat| / |M| over 200 random (h, p) = {worst:.1e}  (exact U(1) invariance with metric)")
# (2) fermion vector-current vacuum polarisation at q = 0
def pi_mn0(L, m):
    k = lf.grid(L)
    P = np.meshgrid(k, k, k, k, indexing="ij")
    a = np.array([np.sin(x).ravel() for x in P]); c = np.array([np.cos(x).ravel() for x in P])
    D = (a * a).sum(0) + m * m
    out = np.zeros((4, 4))
    for mu in range(4):
        for nu in range(4):
            # bubble: -1/2 int tr[S gamma_mu cos S gamma_nu cos] * (i)^2 ... ; written as 2 A^2 [I1 - int cos^2 (D - 2 a_mu^2)/D^2] for mu=nu
            tr = 4 * (m * m * (mu == nu) - (2 * a[mu] * a[nu] - (a * a).sum(0) * (mu == nu)))
            bub = -0.5 * np.mean(c[mu] * c[nu] * tr / D ** 2)
            tad = 0.5 * np.mean(4 * a[mu] ** 2 / D) * (mu == nu)
            out[mu, nu] = 2 * (bub + tad)
    return out
print(f"(2) fermion Pi_mu_nu(0) (per naive fermion, m=0.3, L=24): max |.| = {np.abs(pi_mn0(24, 0.3)).max():.1e};"
      f" separate pieces are O(1e-1)")
# (3) W(B4) covariance and (4) evenness of the h-bilinear
G = []
for perm in itertools.permutations(range(4)):
    for sg in itertools.product((1, -1), repeat=4):
        R = np.zeros((4, 4))
        for i, j in enumerate(perm):
            R[i, j] = sg[i]
        G.append(R)
def rho(R):
    M = np.zeros((10, 10))
    for kk in range(10):
        e = np.zeros(10); e[kk] = 1
        h = R @ sym(e) @ R.T
        M[:, kk] = [h[m, n] for (m, n) in lf.pairs]
    return M
L, m = 16, 0.4
q = 2 * np.pi / L * np.array([2., 1, 0, 3])
Bq, _ = lf.bilinear(q, L, m)
dev = 0
for R in [G[i] for i in rng.choice(384, 6, replace=False)]:
    BR, _ = lf.bilinear(R @ q, L, m)
    r = rho(R)
    # Gamma(h') with h' = R h R^T, q' = R q equals Gamma(h, q):  v'^T B(Rq) v' = v^T B(q) v,  v' = r v
    dev = max(dev, np.abs(r.T @ BR @ r - Bq).max() / np.abs(Bq).max())
Bm, _ = lf.bilinear(-q, L, m)
print(f"(3) W(B4) covariance of fermion bilinear: max rel dev over 6 random elements = {dev:.1e}")
print(f"(4) evenness: max |B(q) - B(-q)| / |B| = {np.abs(Bq - Bm).max() / np.abs(Bq).max():.1e}")
for L in (16, 24, 32, 40):
    P = pi_mn0(L, 0.3)
    print(f"(2b) fermion Pi_mu_nu(0), m=0.3, L={L}: max |.| = {np.abs(P).max():.2e}")
