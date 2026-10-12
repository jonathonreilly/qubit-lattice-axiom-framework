"""Cross-check of the 4x4 partner-loop code (r131_electron_sqed.dE_partner) against R10-5's refereed 8x8 code
(r105_partner_loop.dE, copied logic) on a case where the two contents coincide: W = 0 curves (literal edge),
photino on the same curve as the electron, massless photino (8x8 Clifford module with W = 0 = two copies of the
4x4 Dirac module; g5 restricted identically).  Per y^2, chiral (P_L + P_R).
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r85_box_qed_copy import Law
import r131_electron_sqed as R
U = 16 * np.pi ** 2
law = Law(1.0, 2.0, 0.0, 1.0, 2.0, 0.1)

# 4x4 version with photino forced onto the electron curve, Wl = 0
def dE4(p, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    Sg = law.S(k)
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    El = np.sqrt(Sg[IX] ** 2 + Sg[IY] ** 2 + Sg[IZ] ** 2)
    eps = np.sqrt(law.S(p - k)[IX] ** 2 + law.S(-k)[IY] ** 2 + law.S(-k)[IZ] ** 2 + law.m ** 2)
    w, V = np.linalg.eigh(R.he(law, (p, 0, 0))); Pe = V[:, 2:] @ V[:, 2:].conj().T; Ep = w[-1]
    tot = 0.0
    for Y in (R.beta @ R.PL, R.beta @ R.PR):
        Xm = Y @ Pe @ Y.conj().T; trX = np.trace(Xm).real
        ta = [np.trace(R.alpha[j] @ Xm).real for j in range(3)]
        c = Sg[IX] * ta[0] + Sg[IY] * ta[1] + Sg[IZ] * ta[2]
        tp = 0.5 * (trX + c / El); tm = 0.5 * (trX - c / El)
        tot += np.mean(tp / (2 * eps * (Ep - El - eps)) + tm / (2 * eps * (Ep + El + eps)))
    return Ep, tot / 2

# 8x8 version: R10-5's matrices and formula (r105_partner_loop.py:24-61), curves (S, 0)
I2 = np.eye(2); X_ = np.array([[0, 1], [1, 0]], complex); Y_ = np.array([[0, -1j], [1j, 0]]); Z_ = np.diag([1., -1.]).astype(complex)
P = {'I': I2, 'X': X_, 'Y': Y_, 'Z': Z_}
mat = lambda s: np.kron(np.kron(P[s[0]], P[s[1]]), P[s[2]])
A = [mat(s) for s in ('IIY', 'IYX', 'XYZ')]; B = [mat(s) for s in ('YYZ', 'ZIZ', 'ZXX')]; B0 = mat('ZZX')
g5 = B[0] @ B[1] @ B[2] @ B0
PL8, PR8 = (np.eye(8) - g5) / 2, (np.eye(8) + g5) / 2
def dE8(p, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    Sg = law.S(k)
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    El = np.sqrt(Sg[IX] ** 2 + Sg[IY] ** 2 + Sg[IZ] ** 2)
    eps = np.sqrt(law.S(p - k)[IX] ** 2 + law.S(-k)[IY] ** 2 + law.S(-k)[IZ] ** 2 + law.m ** 2)
    H = law.m * B0 + float(law.S(np.array(p))) * A[0]
    w, V = np.linalg.eigh(H); Pe = V[:, 4:] @ V[:, 4:].conj().T; Ep = w[-1]
    tot = 0.0
    for Y in (B0 @ PL8, B0 @ PR8):
        Xm = Y @ Pe @ Y.conj().T; trX = np.trace(Xm).real
        ta = [np.trace(A[j] @ Xm).real for j in range(3)]
        c = Sg[IX] * ta[0] + Sg[IY] * ta[1] + Sg[IZ] * ta[2]
        tp = 0.5 * (trX + c / El); tm = 0.5 * (trX - c / El)
        tot += np.mean(tp / (2 * eps * (Ep - El - eps)) + tm / (2 * eps * (Ep + El + eps)))
    return Ep, tot / 4

def dc(f, N, h=0.02):
    E0, d0 = f(0.0, N); vals = []
    for hh in (h, 2 * h):
        Ep, d = f(hh, N); vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    return ((4 * vals[0] - vals[1]) / 3) / 2, d0

for N in (48, 64):
    a4, d4 = dc(dE4, N); a8, d8 = dc(dE8, N)
    print('N=%d  4x4: dc x16pi^2/y^2 = %+.6f  dE(0)=%+.6f | 8x8 (R10-5 logic): %+.6f  dE(0)=%+.6f | diff %.1e' % (
        N, U * a4, U * d4, U * a8, U * d8, abs(a4 - a8) * U))
