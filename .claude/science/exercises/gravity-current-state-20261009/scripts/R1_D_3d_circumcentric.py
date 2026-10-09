"""
Check D (route 1, 3D): liquid vs glass vacuum TT modulus with the circumcentric (Voronoi-dual)
DEC Laplacian, which is continuous through Delaunay flips (P1 is not in 3D; see C2).
  w_ij = (signed circumcentric dual area of edge ij in the complex) / |e_ij|, unit masses,
  E = 1/2 sum sqrt(lambda).
  liquid: re-triangulate (Delaunay of strained points)  == Voronoi Laplacian of the strained points
  glass : frozen eps = 0 complex, circumcentric weights recomputed from strained geometry
PRE-STATED READING (same lines as check B)
  L  PASS iff |<G_liq>| <= 3 SE and <= 0.1 |<G_glass>|;  H1 PASS iff |<G_glass>| > 5 SE.
Self-test first: at eps = 0 the circumcentric weights must equal the Voronoi weights (C2).
"""
import numpy as np, sys
from itertools import product
src = open("B_liquid_glass_crystal.py").read().split("which = sys.argv")[0]
ns = {}; exec(src, ns)
periodic_delaunay, expm_sym = ns["periodic_delaunay"], ns["expm_sym"]

EVEN = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2), (1, 2, 0, 3), (1, 3, 2, 0), (2, 3, 0, 1)]

def tri_cc(a, b, c):
    u, v = b - a, c - a; w = np.cross(u, v)
    return a + (np.einsum("ti,ti->t", u, u)[:, None] * np.cross(v, w) + np.einsum("ti,ti->t", v, v)[:, None] * np.cross(w, u)) / (2 * np.einsum("ti,ti->t", w, w)[:, None])

def tet_cc(p):
    a = p[:, 0]; B = p[:, 1:] - a[:, None, :]
    rhs = 0.5 * np.einsum("tki,tki->tk", B, B)
    return a + np.linalg.solve(B, rhs[..., None])[..., 0]

def dec_laplacian(Y, A, vid, voff):
    N = len(Y)
    pos = Y[vid] + np.einsum("tvk,kl->tvl", voff, A)
    D = pos[:, 1:] - pos[:, :1]
    flip = np.linalg.det(D) < 0
    vid = vid.copy(); pos = pos.copy()
    vid[flip, 0], vid[flip, 1] = vid[flip, 1], vid[flip, 0].copy()
    pos[flip, 0], pos[flip, 1] = pos[flip, 1], pos[flip, 0].copy()
    cT = tet_cc(pos)
    W = np.zeros((N, N))
    for (i, j, k, l) in EVEN:
        xi, xj, xk, xl = pos[:, i], pos[:, j], pos[:, k], pos[:, l]
        e = xj - xi; le = np.linalg.norm(e, axis=1); n = e / le[:, None]
        m = 0.5 * (xi + xj)
        P = [m, tri_cc(xi, xj, xk), cT, tri_cc(xi, xj, xl)]
        area = 0.0
        for a in range(4):
            area = area + 0.5 * np.einsum("ti,ti->t", n, np.cross(P[a] - m, P[(a + 1) % 4] - m))
        w = area / le
        np.add.at(W, (vid[:, i], vid[:, j]), w)
        np.add.at(W, (vid[:, j], vid[:, i]), w)
    K = -W; K[np.diag_indices(N)] = 0; K[np.diag_indices(N)] = -K.sum(1)
    return K, W

def E_vac(K):
    lam = np.linalg.eigvalsh(K); return 0.5 * np.sqrt(np.clip(lam, 0, None)).sum(), lam[0]

if sys.argv[1:] == ["selftest"]:
    exec(open("C2_voronoi_vs_p1.py").read().split("rng = np.random")[0])
    rng = np.random.default_rng(3); N = 400; L = N ** (1/3); A0 = L * np.eye(3)
    X = rng.uniform(0, L, size=(N, 3)); vid, voff = periodic_delaunay(X, A0)
    K, W = dec_laplacian(X, A0, vid, voff); Kv, Wv = voronoi_laplacian(X, A0)
    print("selftest max|W_dec - W_vor| =", np.abs(W - Wv).max(), "  max W_vor =", Wv.max(),
          "  sign-flipped match:", np.abs(W + Wv).max())
    sys.exit()

rng = np.random.default_rng(20261009)
N, R = 1000, 12; L = N ** (1/3); A0 = L * np.eye(3)
epss = np.array([-0.06, -0.04, -0.02, 0.0, 0.02, 0.04, 0.06])
S3 = np.zeros((3, 3)); S3[0, 1] = S3[1, 0] = 1.0
chans = {"Eg": np.diag([1.0, -1.0, 0.0]), "T2g": S3}
res = {c: [] for c in chans}; lmin = []
for r in range(R):
    X = rng.uniform(0, L, size=(N, 3)); vid0, voff0 = periodic_delaunay(X, A0)
    for c, S in chans.items():
        Eg, El = [], []
        for e in epss:
            M = expm_sym(S, e); Y, A = X @ M.T, A0 @ M.T
            Kg, _ = dec_laplacian(Y, A, vid0, voff0)
            v, o = periodic_delaunay(Y, A); Kl, _ = dec_laplacian(Y, A, v, o)
            eg, lg = E_vac(Kg); el, ll = E_vac(Kl); lmin.append(min(lg, ll))
            Eg.append(eg / N); El.append(el / N)
        res[c].append((2 * np.polyfit(epss, Eg, 4)[-3], 2 * np.polyfit(epss, El, 4)[-3], El[3]))
    print(f"realization {r} done", flush=True)
for c, rows in res.items():
    a = np.array(rows); n = len(a); e0 = a[:, 2].mean()
    mg, sg = a[:, 0].mean(), a[:, 0].std(ddof=1) / np.sqrt(n)
    ml, sl = a[:, 1].mean(), a[:, 1].std(ddof=1) / np.sqrt(n)
    print(f"3D DEC {c:4s} e0/site={e0:.4f}  G_glass={mg:+.4f}+-{sg:.4f}  G_liquid={ml:+.4f}+-{sl:.4f}  (G/e0: {mg/e0:+.4f}, {ml/e0:+.4f})")
print("most negative eigenvalue seen (glass DEC can lose positivity):", min(lmin))
