"""T2 core: shared definitions.

Free real scalar on Z^4 (Euclidean; axis 0 = time; a_t = a_s).
Metric: G(eps) = diag(1, exp(eps X)), X traceless symmetric 3x3, |X|_F = 1 (volume preserving).
  X_E = diag(1,-1,0)/sqrt2  (E_g),   X_T = (e12+e21)/sqrt2  (T_2g).
Stiffness (per site):  kappa = d^2/deps^2 [ (1/2N) log det D_G ]  at eps = 0
                              = 1/2 < D''/D - (D'/D)^2 >_BZ,
with D' = dD_G/deps, D'' = d^2 D_G/deps^2 computed ANALYTICALLY (no finite differences).
(The brief's "-1/2 log det" is log Z; its second derivative is -kappa. Readings use |kappa|.)
BZ average on a midpoint grid q_j = 2 pi (j + 1/2)/L - pi (q = 0 never sampled, so m = 0 is allowed).
"""
import numpy as np

S2 = np.sqrt(2.0)
XE = np.zeros((3, 3)); XE[0, 0] = 1 / S2; XE[1, 1] = -1 / S2
XT = np.zeros((3, 3)); XT[0, 1] = XT[1, 0] = 1 / S2
CHANNELS = {"E_g": XE, "T_2g": XT}


def midgrid(L):
    return 2 * np.pi * (np.arange(L) + 0.5) / L - np.pi


def spatial_mesh(L):
    k = midgrid(L)
    return np.meshgrid(k, k, k, indexing="ij")


def V_matrix(k1, k2, k3):
    """Metric carrier of R2's 'minimal coupling' nn form: V_ii = 2-2cos k_i, V_ij = sin k_i sin k_j."""
    ks = (k1, k2, k3)
    V = [[None] * 3 for _ in range(3)]
    for i in range(3):
        V[i][i] = 2 - 2 * np.cos(ks[i])
        for j in range(i + 1, 3):
            V[i][j] = V[j][i] = np.sin(ks[i]) * np.sin(ks[j])
    return V


def contract(X, V):
    return sum(X[i, j] * V[i][j] for i in range(3) for j in range(3) if X[i, j] != 0)


def kappa_from_slices(gen, L):
    """gen(q0) yields (D, D1, D2) arrays over the spatial grid; returns 1/2 <D2/D - (D1/D)^2>."""
    acc = 0.0
    for q0 in midgrid(L):
        D, D1, D2 = gen(q0)
        acc += np.sum(D2 / D - (D1 / D) ** 2)
    return 0.5 * acc / L ** 4


def fit_power(x, y):
    x = np.log(np.asarray(x, float)); y = np.log(np.abs(np.asarray(y, float)))
    p, c = np.polyfit(x, y, 1)
    return -p, np.exp(c)
