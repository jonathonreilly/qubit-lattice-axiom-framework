"""A26 s1_span: which first-order cone deformations can nearest-neighbour, cell-periodic hop modulations produce?
(supplied toy).  16 perturbation directions = 8 bond classes (x-even row j, x-odd row j, y-even col i, y-odd col i)
x {real, imaginary} unit amplitude.  For each, the first-order change of the cone generator near K*:
   dH(K*+q) = C0 + qx Cx + qy Cy,
expanded in the spin-taste basis Gamma_alpha T_beta (alpha in 1,Ax,Ay,G3; beta in 1,T1,T2,T3; T_beta commute with Ax,Ay).
A metric (taste-singlet frame) perturbation needs C0 = 0 and Ci in span{Ax, Ay} x 1.
(a) Trotter limit: generators summed.  (b) actual time-symmetric Floquet cycle at dose th, via H_F = i log U.
"""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import itertools
import numpy as np
from scipy.linalg import expm, logm, null_space
from walk2d import bond_gen, site, KSTAR, I2, X, Y, Z, kr

CLASSES = [(ax, par, r) for ax in 'xy' for par in 'eo' for r in (0, 1)]


def class_bonds(K, cls, t):
    ax, par, r = cls
    if ax == 'x':
        return [(site(0, r), site(1, r), (0, 0), t)] if par == 'e' else [(site(1, r), site(0, r), (1, 0), t)]
    return [(site(r, 0), site(r, 1), (0, 0), t)] if par == 'e' else [(site(r, 1), site(r, 0), (0, 1), t)]


def base_amp(cls, th):
    ax, par, r = cls
    return th * (1.0 if ax == 'x' else (-1.0) ** r)          # KS sign on y bonds = (-1)^x, x = column r


def gen_sum(K, amps):
    H = np.zeros((4, 4), complex)
    for cls, t in amps.items():
        H += bond_gen(K, class_bonds(K, cls, t))
    return H


def floquet(K, amps):
    """time-symmetric blocks; amps = total angle per class (even classes split into two halves)"""
    def L(ax, par, f):
        H = np.zeros((4, 4), complex)
        for cls, t in amps.items():
            if cls[0] == ax and cls[1] == par:
                H += bond_gen(K, class_bonds(K, cls, f * t))
        return expm(-1j * H)
    Ux = L('x', 'e', .5) @ L('x', 'o', 1.) @ L('x', 'e', .5)
    Uy = L('y', 'e', .5) @ L('y', 'o', 1.) @ L('y', 'e', .5)
    return Uy @ Ux


th0 = 0.3
# spin matrices from the Trotter cone, normalised by th
dq = 1e-6
H0 = lambda K: gen_sum(K, {c: base_amp(c, 1.0) for c in CLASSES})
Ax = (H0(KSTAR + [dq, 0]) - H0(KSTAR - [dq, 0])) / (2 * dq)
Ay = (H0(KSTAR + [0, dq]) - H0(KSTAR - [0, dq])) / (2 * dq)
print("Trotter cone: Ax = %s-ish, |Ax - (-kron(Y,I))| = %.1e ; |Ay - (-kron(Z,Y))| = %.1e ; {Ax,Ay} = %.1e"
      % ("", np.abs(Ax + kr(Y, I2)).max(), np.abs(Ay + kr(Z, Y)).max(), np.abs(Ax @ Ay + Ay @ Ax).max()))
masses = {'Bx': kr(X, I2), 'By': kr(Z, X), 'eps': kr(Z, Z)}
for nm, M in masses.items():
    print("   mass %-3s anticommutes with Ax, Ay: %.1e %.1e" % (nm, np.abs(M @ Ax + Ax @ M).max(), np.abs(M @ Ay + Ay @ M).max()))
G3 = -1j * Ax @ Ay
T = {}
for b, nm in zip((1, 2, 3), ('Bx', 'By', 'eps')):
    Tb = G3 @ masses[nm]
    T[b] = Tb
    print("   T%d = G3 * %-3s : hermitian %.1e, square-1 %.1e, [T,Ax] %.1e, [T,Ay] %.1e" % (
        b, nm, np.abs(Tb - Tb.conj().T).max(), np.abs(Tb @ Tb - np.eye(4)).max(),
        np.abs(Tb @ Ax - Ax @ Tb).max(), np.abs(Tb @ Ay - Ay @ Tb).max()))
print("   T1 T2 = i T3 ? %.1e" % np.abs(T[1] @ T[2] - 1j * T[3]).max())
GAM = {'1': np.eye(4), 'Ax': Ax, 'Ay': Ay, 'G3': G3}
TAS = {'1': np.eye(4), 'T1': T[1], 'T2': T[2], 'T3': T[3]}
BASIS = [(g, t, GAM[g] @ TAS[t]) for g in GAM for t in TAS]
Bmat = np.array([B.reshape(-1) for _, _, B in BASIS])
print("   spin-taste basis orthogonality: max |tr(Bi Bj)/4 - delta| = %.1e"
      % np.abs(Bmat.conj() @ Bmat.T / 4 - np.eye(16)).max())
labels = ["%s.%s" % (g, t) for g, t, _ in BASIS]


def coeffs(C):
    return np.real(Bmat.conj() @ C.reshape(-1) / 4)


# Pauli dictionary used in the report: which spin-taste element is each simple bond operator?
for nm, op in (("X_y (unsigned real y-hop)", kr(I2, X)), ("Y_y (unsigned imag y-hop)", kr(I2, Y)),
               ("Z_y X_x ((-1)^y real x-hop)", kr(X, Z)), ("Z_y Y_x ((-1)^y imag x-hop)", kr(Y, Z)),
               ("X_x Y_y (in-cell diagonal)", kr(X, Y))):
    c = coeffs(op)
    k = np.argmax(np.abs(c))
    print("   %-30s = %+.3f %s   (residual %.1e)" % (nm, c[k], labels[k], np.sqrt(max(0, np.sum(c ** 2) - c[k] ** 2))))


def first_order(mode, th, eps=1e-4, dq=2e-3):
    """return arrays C0, Cx, Cy (16 x 16: perturbation k x basis coefficient)"""
    base = {c: base_amp(c, th) for c in CLASSES}
    pert = [(c, u) for c in CLASSES for u in (1.0, -1j)]
    def HF(K, amps):
        if mode == 'trotter':
            return gen_sum(K, amps)
        return 1j * logm(floquet(K, amps))
    out = []
    for c, u in pert:
        def dH(K):
            ap = dict(base); ap[c] = ap[c] + eps * u
            am = dict(base); am[c] = am[c] - eps * u
            return (HF(K, ap) - HF(K, am)) / (2 * eps)
        C0 = dH(KSTAR)
        d4 = lambda e: (8 * (dH(KSTAR + dq * e) - dH(KSTAR - dq * e)) - (dH(KSTAR + 2 * dq * e) - dH(KSTAR - 2 * dq * e))) / (12 * dq)
        Cx = d4(np.array([1.0, 0.0]))
        Cy = d4(np.array([0.0, 1.0]))
        out.append((coeffs(C0), coeffs(Cx), coeffs(Cy)))
    C0 = np.array([o[0] for o in out]); Cx = np.array([o[1] for o in out]); Cy = np.array([o[2] for o in out])
    return C0, Cx, Cy, [("%s%s%d" % c) + ("re" if u == 1.0 else "im") for c, u in pert]


ix = {l: i for i, l in enumerate(labels)}
for mode, th in (('trotter', 1.0), ('floquet', 0.1), ('floquet', th0), ('floquet', 0.6), ('floquet', 1.0)):
    C0, Cx, Cy, names = first_order(mode, th)
    ns = null_space(C0.T, rcond=1e-6)                      # combinations with no constant (gap/shift) part at K*
    # frame map: coefficients of (Ax.1, Ay.1) in Cx and Cy
    F = np.column_stack([Cx[:, ix['Ax.1']], Cx[:, ix['Ay.1']], Cy[:, ix['Ax.1']], Cy[:, ix['Ay.1']]])
    Fn = ns.T @ F                                          # achievable taste-singlet frame perturbations
    sv = np.linalg.svd(Fn, compute_uv=False)
    target = np.array([0, 1, 1, 0.]) / np.sqrt(2)          # symmetric off-diagonal frame (cross shear)
    plus = np.array([1, 0, 0, -1.]) / np.sqrt(2)           # plus shear
    Q, _ = np.linalg.qr(Fn.T)
    rk = int(np.sum(sv > 1e-5 * sv.max()))
    Q = Q[:, :rk]
    res_t = np.linalg.norm(target - Q @ (Q.T @ target))
    res_p = np.linalg.norm(plus - Q @ (Q.T @ plus))
    # taste-graded cross shear: (Ay.T3 in Cx, Ax.T3 in Cy)
    G = np.column_stack([Cx[:, ix['Ay.T3']], Cy[:, ix['Ax.T3']]])
    Gn = ns.T @ G
    sg = np.linalg.svd(Gn, compute_uv=False)
    print("[%s th=%.2f] gap-free combinations: %d of 16; taste-singlet frame image rank %d, sv %s"
          % (mode, th, ns.shape[1], rk, np.array2string(sv, precision=4)))
    print("      residual of CROSS shear (Ay in Cx = Ax in Cy) outside image: %.3e ; of PLUS shear: %.3e"
          % (res_t, res_p))
    print("      taste-graded cross shear (Ay.T3 in Cx, Ax.T3 in Cy) image sv: %s" % np.array2string(sg, precision=4))
    if mode == 'trotter':
        # list which components each single imaginary/real class produces at linear order (nonzero coefficients)
        for k, nm in enumerate(names):
            parts = []
            for C, tag in ((C0, '0'), (Cx, 'qx'), (Cy, 'qy')):
                for j in np.nonzero(np.abs(C[k]) > 1e-6)[0]:
                    parts.append("%s:%+.2f %s" % (tag, C[k][j], labels[j]))
            print("      %-8s %s" % (nm, "; ".join(parts)))
