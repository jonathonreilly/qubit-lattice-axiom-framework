#!/usr/bin/env python3
"""Lane T check G: a strictly cubic-covariant finite-range step whose low-energy branches split at LINEAR order.

U_tot(k) = direct sum over the 6 orderings s of the three axis conveyors, U_s(k) = E(s1) E(s2) E(s3),
E(i) = exp(-i k_i sigma_i) (a two-component content set moved along axis i, + component forward, - component back).
Claim: U_tot(g k) = V_g U_tot(k) V_g^dag with k-INDEPENDENT V_g = (permutation of orderings) x W_g for all 24 proper
cubic rotations g (W_g the SU(2) lift of g). Even orderings have cos w = cx cy cz - sx sy sz, odd ones + sx sy sz,
so the low-energy cone splits as w = |k| +- |k|^2 n_x n_y n_z (linear order in |k|), opposite on the two classes,
which 90-degree rotations exchange (an internal A2 label).
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import numpy as np

rng = np.random.default_rng(11)
I2 = np.eye(2, dtype=complex)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]

O = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i, j in enumerate(perm):
            M[i, j] = signs[i]
        if round(np.linalg.det(M)) == 1:
            O.append(M)


def su2_lift(g):
    """W with W sigma_j W^dag = sum_i g_ij sigma_i."""
    th = np.arccos(np.clip((np.trace(g) - 1) / 2, -1, 1))
    if th < 1e-12:
        return I2.copy()
    if abs(th - np.pi) < 1e-9:
        # axis = eigenvector with eigenvalue 1
        w, v = np.linalg.eig(g)
        n = np.real(v[:, np.argmin(np.abs(w - 1))])
    else:
        n = np.array([g[2, 1] - g[1, 2], g[0, 2] - g[2, 0], g[1, 0] - g[0, 1]]) / (2 * np.sin(th))
    n = n / np.linalg.norm(n)
    for sgn in (1, -1):
        W = np.cos(th / 2) * I2 - 1j * sgn * np.sin(th / 2) * sum(n[i] * SIG[i] for i in range(3))
        ok = all(np.allclose(W @ SIG[j] @ W.conj().T, sum(g[i, j] * SIG[i] for i in range(3)), atol=1e-12) for j in range(3))
        if ok:
            return W
    raise RuntimeError("no lift")


def E(i, k):
    return np.cos(k[i]) * I2 - 1j * np.sin(k[i]) * SIG[i]


ORD = list(itertools.permutations(range(3)))


def Us(s, k):
    return E(s[0], k) @ E(s[1], k) @ E(s[2], k)


def Utot(k):
    Z = np.zeros((12, 12), complex)
    for a, s in enumerate(ORD):
        Z[2 * a:2 * a + 2, 2 * a:2 * a + 2] = Us(s, k)
    return Z


def parity(s):
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if s[i] > s[j])
    return (-1) ** inv


maxerr = 0.0
for g in O:
    W = su2_lift(g)
    pi = [int(np.argmax(np.abs(g[i]))) for i in range(3)]   # (g k)_i = s_i k_{pi(i)}
    # V_g: block a (ordering s) of the image is filled from block b with ordering pi(s)
    V = np.zeros((12, 12), complex)
    for a, s in enumerate(ORD):
        b = ORD.index(tuple(pi[x] for x in s))
        V[2 * a:2 * a + 2, 2 * b:2 * b + 2] = W
    for _ in range(20):
        k = rng.uniform(-np.pi, np.pi, 3)
        maxerr = max(maxerr, np.max(np.abs(Utot(g @ k) - V @ Utot(k) @ V.conj().T)))
print("strict covariance: max |U_tot(gk) - V_g U_tot(k) V_g^dag| over 24 rotations x 20 random k = %.1e" % maxerr)

err = 0.0
for _ in range(500):
    k = rng.uniform(-np.pi, np.pi, 3)
    c, s = np.cos(k), np.sin(k)
    for sgo in ORD:
        lam = np.linalg.eigvals(Us(sgo, k))
        cw = np.real(lam.sum()) / 2
        err = max(err, abs(cw - (c[0] * c[1] * c[2] - parity(sgo) * s[0] * s[1] * s[2])))
print("cos w = cx cy cz - parity(ordering) sx sy sz : max error %.1e" % err)

n = np.array([1.0, 2.0, 3.0]) / np.sqrt(14)
for kk in (1e-2, 5e-3):
    ph = np.angle(np.linalg.eigvals(Utot(kk * n)))
    pos = np.sort(ph[ph > 0])
    print("|k|=%.0e along (1,2,3): positive branches (w-|k|)/|k|^2 = %s  (n_x n_y n_z = %.5f)" % (
        kk, ", ".join("%+.4f" % ((p - kk) / kk ** 2) for p in pos), n[0] * n[1] * n[2]))
Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float)
print("90-degree rotation maps even orderings to:", sorted({parity(tuple(int(np.argmax(np.abs(Rz[i]))) for i in s)) for s in ORD if parity(s) == 1}))
print("per-tick neighbourhood of each U_s: the 8 body-diagonal neighbours (three nearest-neighbour axis layers per tick)")
