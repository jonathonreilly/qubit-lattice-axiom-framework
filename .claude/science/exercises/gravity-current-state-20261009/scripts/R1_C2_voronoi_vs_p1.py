"""C2: in 3D, is the assembled P1 stiffness on the Delaunay complex equal to the Voronoi-dual
Laplacian w_ij = |Voronoi face ij| / |x_i - x_j| ?  Compare entrywise; report worst entries."""
import numpy as np
from scipy.spatial import Voronoi
from itertools import product
src = open("B_liquid_glass_crystal.py").read().split("which = sys.argv")[0]
ns = {}; exec(src, ns)

def voronoi_laplacian(Y, A):
    N, d = Y.shape
    shifts = np.array(list(product((-1, 0, 1), repeat=d)))
    P = np.concatenate([Y + s @ A for s in shifts]); idx = np.tile(np.arange(N), len(shifts))
    c0 = int(np.where((shifts == 0).all(1))[0][0]) * N
    vor = Voronoi(P)
    W = np.zeros((N, N))
    for (p, q), rv in zip(vor.ridge_points, vor.ridge_vertices):
        pc, qc = (c0 <= p < c0 + N), (c0 <= q < c0 + N)
        if not (pc or qc):
            continue
        if -1 in rv:
            continue
        V = vor.vertices[rv]
        # polygon area (planar polygon in 3D): fan triangulation around centroid, ordered as given
        c = V.mean(0); area = 0.5 * np.linalg.norm(sum(np.cross(V[k] - c, V[(k + 1) % len(V)] - c) for k in range(len(V))))
        w = area / np.linalg.norm(P[p] - P[q])
        if pc: W[idx[p], idx[q]] += w
        if qc: W[idx[q], idx[p]] += w
    W = 0.5 * (W + W.T) if False else W
    K = -W.copy(); np.fill_diagonal(K, 0); K[np.diag_indices(N)] = W.sum(1)
    return K, W

rng = np.random.default_rng(3)
N = 400; L = N ** (1/3); A0 = L * np.eye(3)
X = rng.uniform(0, L, size=(N, 3))
vid, voff = ns["periodic_delaunay"](X, A0)
Kp1 = ns["stiffness"](X, A0, vid, voff)
Kv, W = voronoi_laplacian(X, A0)
off = ~np.eye(N, dtype=bool)
print("asym of Voronoi W (should be 0):", np.abs(W - W.T).max())
d = np.abs(Kp1 - Kv)[off]
print("max |K_P1 - K_vor| offdiag:", d.max(), "  max |K_P1| offdiag:", np.abs(Kp1[off]).max(), " max W:", W.max())
print("negative P1 off-diagonal weights (K_ij>0):", int((Kp1[off] > 1e-9).sum()), " of nonzero:", int((np.abs(Kp1[off]) > 1e-9).sum()))
print("lam_max P1 / Voronoi:", np.linalg.eigvalsh(Kp1)[-1], np.linalg.eigvalsh(0.5*(Kv+Kv.T))[-1])
