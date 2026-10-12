"""
Check A (route 2, ledger rows S6/H2): does equilibrium relaxation ("self-tuning")
remove the vacuum's static traceless-strain (TT) modulus on the fixed Z^3 grid?

Model (supplied): one band of free fermions on Z^3, nearest-neighbour hops on axes,
range-2 face hops for the off-diagonal metric, coupled to a uniform volume-preserving
metric g = M^T M, M = exp(eps*S), S traceless symmetric:
    E(k; g) = sum_i g^{ii} 2(1 - cos k_i) + sum_{i != j} g^{ij} sin k_i sin k_j
IR limit: E -> k.g^{-1}.k (covariant).  Fixed particle number per site nu.

Relaxed   : the sea re-forms at each eps (lowest nu*N levels)   -> "liquid in k-space"
Frozen    : the occupied set is held at its eps = 0 shape        -> "crystal in k-space"
Filled band (nu = 1) is the frozen case automatically.

Continuum predictions (derived before running, see report):
    Eg channel: G_frozen / e0 -> 8/3,   G_relaxed / e0 -> -(2/21) k_F^2   (k_F = (6 pi^2 nu)^(1/3))
PRE-STATED READING
    PASS for "self-tuning kills the modulus": G_relaxed/e0 -> 0 faster than any power of k_F,
                                              or exactly 0 at finite nu.
    FAIL: G_relaxed/e0 ~ c k_F^2 with c != 0 (relaxation kills only the continuum part).
"""
import numpy as np

def band(kx, ky, kz, Ginv):
    c = [2 * (1 - np.cos(k)) for k in (kx, ky, kz)]
    s = [np.sin(k) for k in (kx, ky, kz)]
    E = Ginv[0, 0] * c[0] + Ginv[1, 1] * c[1] + Ginv[2, 2] * c[2]
    E = E + 2 * Ginv[0, 1] * s[0] * s[1] + 2 * Ginv[0, 2] * s[0] * s[2] + 2 * Ginv[1, 2] * s[1] * s[2]
    return E

def ginv(eps, S):
    w, V = np.linalg.eigh(S)
    M = V @ np.diag(np.exp(eps * w)) @ V.T          # M = exp(eps S), det M = 1
    g = M.T @ M
    return np.linalg.inv(g)

n = 160
k = 2 * np.pi * (np.arange(n) + 0.5) / n - np.pi
KX, KY, KZ = np.meshgrid(k, k, k, indexing="ij")
KX, KY, KZ = KX.ravel(), KY.ravel(), KZ.ravel()
N = KX.size

S_Eg = np.diag([1.0, -1.0, 0.0])
S_T2g = np.zeros((3, 3)); S_T2g[0, 1] = S_T2g[1, 0] = 1.0
epss = np.linspace(-0.06, 0.06, 13)

print(f"k-grid {n}^3 = {N} states")
print(f"{'chan':5s} {'nu':>8s} {'kF':>7s} {'e0':>10s} {'Gfroz/e0':>10s} {'Grel/e0':>11s} {'Grel/(e0 kF^2)':>15s} {'pred':>8s}")
for name, S in (("Eg", S_Eg), ("T2g", S_T2g)):
    E0 = band(KX, KY, KZ, ginv(0.0, S))
    order0 = np.argsort(E0)
    for nu in (0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.25):
        Nocc = int(round(nu * N))
        occ0 = order0[:Nocc]
        erel, efro = [], []
        for e in epss:
            E = band(KX, KY, KZ, ginv(e, S))
            erel.append(np.partition(E, Nocc)[:Nocc].sum() / N)
            efro.append(E[occ0].sum() / N)
        prel = np.polyfit(epss, erel, 4); pfro = np.polyfit(epss, efro, 4)
        Grel, Gfro = 2 * prel[-3], 2 * pfro[-3]
        e0 = E0[occ0].sum() / N
        kF = (6 * np.pi ** 2 * nu) ** (1 / 3)
        pred = -2 / 21 if name == "Eg" else float("nan")
        print(f"{name:5s} {nu:8.3f} {kF:7.3f} {e0:10.3e} {Gfro/e0:10.4f} {Grel/e0:11.3e} {Grel/(e0*kF**2):15.4f} {pred:8.4f}")
