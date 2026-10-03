"""A26 s3_span3d: 3D version of s1_span (supplied toy).  A10's 2x2x2 cell, KS signs eta=(1,(-1)^x,(-1)^(x+y)).
48 perturbations = 24 bond classes (axis a, parity, transverse position) x {real, imaginary}.
First-order cone deformation dH(K*+q) = C0 + sum_i q_i C_i.  Taste-singlet frame components: tr(A_a C_i)/8.
Question: with C0 = 0, which singlet frame matrices M_ia are reachable?  Trotter limit and Floquet (time-symmetric
blocks x, y, z) at th = 0.3."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import itertools
import numpy as np
from scipy.linalg import expm, logm, null_space

def idx(i, j, k):
    return 4 * i + 2 * j + k
AX = 3
CLASSES = []
for a in range(3):
    for par in 'eo':
        for t in itertools.product((0, 1), repeat=2):
            CLASSES.append((a, par, t))


def ks(a, s):
    return [1.0, (-1.0) ** s[0], (-1.0) ** (s[0] + s[1])][a]


def class_bond(cls, t_amp):
    a, par, tr = cls
    s = [0, 0, 0]
    others = [b for b in range(3) if b != a]
    s[others[0]], s[others[1]] = tr
    p = list(s); q = list(s); d = [0, 0, 0]
    if par == 'e':
        p[a], q[a] = 0, 1
    else:
        p[a], q[a] = 1, 0; d[a] = 1
    return idx(*p), idx(*q), d, t_amp * ks(a, p)


def gen(K, amps):
    H = np.zeros((8, 8), complex)
    for cls, t in amps.items():
        p, q, d, tt = class_bond(cls, t)
        ph = np.exp(1j * np.dot(K, d))
        H[p, q] += tt * ph; H[q, p] += np.conj(tt * ph)
    return H


def floquet(K, amps):
    U = np.eye(8, dtype=complex)
    for a in range(3):
        def L(par, f):
            return expm(-1j * gen(K, {c: f * t for c, t in amps.items() if c[0] == a and c[1] == par}))
        U = L('e', .5) @ L('o', 1.) @ L('e', .5) @ U
    return U


KS = np.array([np.pi] * 3)
base = lambda th: {c: th for c in CLASSES}
dq = 1e-6
H0 = lambda K: gen(K, base(1.0))
A = [(H0(KS + dq * np.eye(3)[i]) - H0(KS - dq * np.eye(3)[i])) / (2 * dq) for i in range(3)]
anti = max(np.abs(A[i] @ A[j] + A[j] @ A[i] - 2 * (i == j) * np.eye(8)).max() for i in range(3) for j in range(3))
print("3D Trotter cone: A_a anticommute, square to 1: max dev %.1e" % anti)


def first_order(mode, th, eps=1e-4, h=2e-3):
    out = []
    pert = [(c, u) for c in CLASSES for u in (1.0, -1j)]
    def HF(K, amps):
        return gen(K, amps) if mode == 'trotter' else 1j * logm(floquet(K, amps))
    for c, u in pert:
        def dH(K):
            ap = base(th); ap[c] = ap[c] + eps * u
            am = base(th); am[c] = am[c] - eps * u
            return (HF(K, ap) - HF(K, am)) / (2 * eps)
        C0 = dH(KS)
        Ci = []
        for i in range(3):
            e = np.eye(3)[i]
            Ci.append((8 * (dH(KS + h * e) - dH(KS - h * e)) - (dH(KS + 2 * h * e) - dH(KS - 2 * h * e))) / (12 * h))
        out.append((C0, Ci))
    return out


for mode, th in (('trotter', 1.0), ('floquet', 0.3)):
    out = first_order(mode, th)
    C0m = np.array([np.concatenate([o[0].real.ravel(), o[0].imag.ravel()]) for o in out])
    ns = null_space(C0m.T, rcond=1e-6)
    # singlet frame matrix M[i][a] = tr(A_a C_i)/8  (9 numbers)
    Fm = np.array([[np.real(np.trace(A[a] @ o[1][i])) / 8 for i in range(3) for a in range(3)] for o in out])
    Fn = ns.T @ Fm
    sv = np.linalg.svd(Fn, compute_uv=False)
    rk = int(np.sum(sv > 1e-5 * sv.max()))
    Q, _ = np.linalg.qr(Fn.T); Q = Q[:, :rk]
    def resid(M):
        v = np.array(M, float).ravel(); v /= np.linalg.norm(v)
        return np.linalg.norm(v - Q @ (Q.T @ v))
    cross_xy = np.zeros((3, 3)); cross_xy[0, 1] = cross_xy[1, 0] = 1
    plus = np.diag([1.0, -1.0, 0.0]); conf = np.eye(3)
    print("[%s th=%.2f] gap-free combos %d of 48; singlet-frame image rank %d; sv %s" % (
        mode, th, ns.shape[1], rk, np.array2string(sv, precision=3)))
    print("    residual outside image: cross shear (xy) %.3e ; plus shear %.3e ; conformal %.3e" % (
        resid(cross_xy), resid(plus), resid(conf)))
