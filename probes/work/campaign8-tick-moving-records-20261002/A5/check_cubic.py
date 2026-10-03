#!/usr/bin/env python3
"""Lane T check E: which orders of grid dispersion survive proper cubic rotations (3D).

(1) Dimension of polynomials of degree d invariant under the 24 proper cubic rotations O (Reynolds averaging,
    evaluated at random points, numerical rank). Expected from (1+t^9)/((1-t^2)(1-t^4)(1-t^6)):
    d=1..9 -> 0,1,0,2,0,3,0,4,1  (no odd invariant below degree 9).
    Same for the 8-element stabilizer D4 of the zone points (pi,0,0)/(pi,pi,0): expected first odd degree 5.
(2) Fixed-order conveyor product U(k) = e^{-ik_x sx} e^{-ik_y sy} e^{-ik_z sz} (NOT cubic covariant):
    cos w = c_x c_y c_z - s_x s_y s_z  ->  w = |k| + k_x k_y k_z/|k| + ...  (linear-order, direction-dependent term).
(3) Two rotation-related copies, U(k) (+) U(R_z k): spectrum is an O-invariant set, Tr = 4 c_x c_y c_z has no odd terms,
    yet the two positive branches split at linear order: w_pm = |k| +- |k|^2 n_x n_y n_z.
"""
import os
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import itertools
import numpy as np

rng = np.random.default_rng(7)

# proper cubic rotations: signed permutation matrices with det +1
O = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3))
        for i, j in enumerate(perm):
            M[i, j] = signs[i]
        if round(np.linalg.det(M)) == 1:
            O.append(M)
assert len(O) == 24
D4 = [M for M in O if abs(abs(M[0, 0]) - 1) < 1e-12]   # maps x-axis to +-x-axis
assert len(D4) == 8


def inv_dims(G, dmax=9, npts=400):
    P = rng.normal(size=(npts, 3))
    out = []
    for d in range(1, dmax + 1):
        mons = [(a, b, d - a - b) for a in range(d + 1) for b in range(d + 1 - a)]
        rows = []
        for (a, b, c) in mons:
            val = np.zeros(npts)
            for g in G:
                Q = P @ g.T
                val += Q[:, 0] ** a * Q[:, 1] ** b * Q[:, 2] ** c
            rows.append(val / len(G))
        A = np.array(rows)
        sv = np.linalg.svd(A, compute_uv=False)
        out.append(int(np.sum(sv > 1e-9 * sv[0])) if sv[0] > 1e-12 else 0)
    return out


print("== (1) invariant polynomial dimensions, degrees 1..9")
print("   O  (24 proper rotations):", inv_dims(O), " expected [0, 1, 0, 2, 0, 3, 0, 4, 1]")
print("   D4 (stabilizer of (pi,0,0)):", inv_dims(D4), " first odd degree expected 5")
# the degree-9 invariant
J = lambda v: v[..., 0] * v[..., 1] * v[..., 2] * (v[..., 0] ** 2 - v[..., 1] ** 2) * (v[..., 1] ** 2 - v[..., 2] ** 2) * (v[..., 2] ** 2 - v[..., 0] ** 2)
P = rng.normal(size=(50, 3))
print("   max |J(gv) - J(v)| over O, 50 random v: %.1e" % max(np.max(np.abs(J(P @ g.T) - J(P))) for g in O))

sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)


def ex(a, s):
    return np.cos(a) * np.eye(2) - 1j * np.sin(a) * s


def Uprod(k):
    return ex(k[0], sx) @ ex(k[1], sy) @ ex(k[2], sz)


print("\n== (2) fixed-order conveyor product")
err = 0.0
for _ in range(2000):
    k = rng.uniform(-np.pi, np.pi, 3)
    lam = np.linalg.eigvals(Uprod(k))
    cw = np.real(lam[0] + lam[1]) / 2
    c, s = np.cos(k), np.sin(k)
    err = max(err, abs(cw - (c[0] * c[1] * c[2] - s[0] * s[1] * s[2])), abs(np.prod(lam) - 1))
print("   max |cos w - (cx cy cz - sx sy sz)|, |det-1| over 2000 random k: %.1e" % err)
for n in (np.array([1, 1, 1]) / np.sqrt(3), np.array([1, 1, -1]) / np.sqrt(3), np.array([1, 2, 3]) / np.sqrt(14), np.array([1, 0, 0])):
    row = []
    for kk in (1e-2, 5e-3, 2.5e-3):
        lam = np.linalg.eigvals(Uprod(kk * n))
        w = np.max(np.abs(np.angle(lam)))
        row.append((w - kk) / kk ** 2)
    print("   n=%s  (w-|k|)/|k|^2 at |k|=1e-2,5e-3,2.5e-3: %s   -> n_x n_y n_z = %+.5f" % (
        np.round(n, 3), ", ".join("%+.5f" % r for r in row), n[0] * n[1] * n[2]))
Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float)
k = rng.uniform(-0.05, 0.05, 3)
w1 = np.max(np.abs(np.angle(np.linalg.eigvals(Uprod(k)))))
w2 = np.max(np.abs(np.angle(np.linalg.eigvals(Uprod(Rz @ k)))))
print("   90-degree rotation flips the linear-order term: w(k)-|k| = %+.3e, w(R_z k)-|k| = %+.3e" % (w1 - np.linalg.norm(k), w2 - np.linalg.norm(k)))

print("\n== (3) two rotation-related copies U(k) (+) U(R_z k)")


def Upair(k):
    Z = np.zeros((4, 4), complex)
    Z[:2, :2] = Uprod(k)
    Z[2:, 2:] = Uprod(Rz @ k)
    return Z


errset, errtr = 0.0, 0.0
for _ in range(300):
    k = rng.uniform(-np.pi, np.pi, 3)
    base = np.sort(np.mod(np.angle(np.linalg.eigvals(Upair(k))), 2 * np.pi))
    for g in O:
        other = np.sort(np.mod(np.angle(np.linalg.eigvals(Upair(g @ k))), 2 * np.pi))
        d = np.abs(base - other)
        d = np.minimum(d, 2 * np.pi - d)
        errset = max(errset, d.max())
    c = np.cos(k)
    errtr = max(errtr, abs(np.trace(Upair(k)) - 4 * c[0] * c[1] * c[2]))
print("   spectrum O-invariant as a set: max mismatch %.1e over 300 k x 24 rotations;  |Tr - 4 cx cy cz| max %.1e" % (errset, errtr))
n = np.array([1, 2, 3]) / np.sqrt(14)
for kk in (1e-2, 5e-3):
    ph = np.angle(np.linalg.eigvals(Upair(kk * n)))
    pos = np.sort(ph[ph > 0])
    print("   |k|=%.0e  positive branches (w-|k|)/|k|^2 = %+.5f, %+.5f   (+-n_x n_y n_z = +-%.5f)" % (
        kk, (pos[0] - kk) / kk ** 2, (pos[1] - kk) / kk ** 2, n[0] * n[1] * n[2]))
