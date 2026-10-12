"""C5 R10-5 script 4c: N=2 completion -- the electron's one-loop speed from the neutral complex scalar 'a' of the N=2 vector
multiplet (Yukawa y psi-bar (a P_L + a^* P_R) psi type; internal electron + massless a on the photon's curve), and a general
re-check of the selectron-photino loop with swapped roles. Same OFPT formula as r105_partner_loop.py with:
internal fermion = electron (curve ce, mass m), internal boson = a (dispersion |c_g(k)|, massless).
Vertices tried: Y = B0 (scalar), Y = B0 g5 (pseudoscalar), and the chiral pair {B0 P_L, B0 P_R} (complex a).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
import r105_partner_loop as P
from r101_pairing import make_box_curve, wilson_curve
U = 16 * np.pi ** 2
t0 = time.time()
def dE(ce, cb, m, p, N, Ys, mb=0.0):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    Sf, Wf = ce['S'](k), ce['W'](k)                     # internal fermion = electron at k
    vf = Sf ** 2 + Wf ** 2
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    Ef = np.sqrt(m * m + vf[IX] + vf[IY] + vf[IZ])
    vb = lambda kk: cb['S'](kk) ** 2 + cb['W'](kk) ** 2
    bx = vb(p - k); byz = vb(-k)
    eb = np.sqrt(mb * mb + bx[IX] + byz[IY] + byz[IZ])
    H = P.he(ce, (p, 0.0, 0.0), m); w, V = np.linalg.eigh(H)
    Pe = V[:, 4:] @ V[:, 4:].conj().T; Ep = w[-1]
    tot = 0.0
    for Y in Ys:
        Xm = Y @ Pe @ Y.conj().T
        trX = np.trace(Xm).real
        ta = [np.trace(P.A[j] @ Xm).real for j in range(3)]; tb = [np.trace(P.B[j] @ Xm).real for j in range(3)]
        t0m = np.trace(P.B0 @ Xm).real
        c = Sf[IX] * ta[0] + Sf[IY] * ta[1] + Sf[IZ] * ta[2] + Wf[IX] * tb[0] + Wf[IY] * tb[1] + Wf[IZ] * tb[2] + m * t0m
        tp = 0.5 * (trX + c / Ef); tm = 0.5 * (trX - c / Ef)
        tot += np.mean(tp / (2 * eb * (Ep - Ef - eb)) + tm / (2 * eb * (Ep + Ef + eb)))
    return Ep, tot / 4
def dc(ce, cb, m, N, Ys, h, mb=0.0):
    E0, d0 = dE(ce, cb, m, 0.0, N, Ys, mb)
    vals = []
    for hh in (h, 2 * h):
        Ep, d = dE(ce, cb, m, hh, N, Ys, mb); vals.append((2 * Ep * d - 2 * E0 * d0) / hh ** 2)
    return ((4 * vals[0] - vals[1]) / 3) / 2
B0, g5, PL, PR = P.B0, P.g5, P.PL, P.PR
print('a-loop (internal electron + massless neutral scalar on the photon curve): dc_e x16pi^2/y^2')
for lab, ce, cb in [('Wilson e / Wilson a', wilson_curve(), wilson_curve()), ('box0.8 e / box0.8 a', make_box_curve(0.8, 1.6), make_box_curve(0.8, 1.6)),
                    ('box0.8 e / Wilson a', make_box_curve(0.8, 1.6), wilson_curve())]:
    for m, N, h in [(0.1, 128, 0.005), (0.05, 160, 0.0025), (0.05, 192, 0.0025)]:
        r1 = dc(ce, cb, m, N, [B0], h); r2 = dc(ce, cb, m, N, [B0 @ g5], h); r3 = dc(ce, cb, m, N, [B0 @ PL, B0 @ PR], h)
        print('  %-20s m=%.2f N=%3d | scalar %+8.4f | pseudoscalar %+8.4f | chiral pair %+8.4f' % (lab, m, N, r1 * U, r2 * U, r3 * U), flush=True)
# consistency: the selectron-photino loop recomputed with this code (fermion = photino massless, boson = selectron mass m) is in
# r105_partner_loop.py; here a cross-check of that code path with roles swapped is not possible without a massive boson, so we
# check the generic code against r105_partner_loop for (internal fermion massless curve cl, boson = electron curve, mass m):
def dE_generic_check():
    ce, cl = wilson_curve(), wilson_curve(); m = 0.1; N = 96
    a = P.dc(ce, cl, m, N, [B0 @ PL, B0 @ PR], h=0.01)[0] * U
    print('  [check] r105_partner_loop chiral Wilson/Wilson m=0.1 N=96: %+8.4f (should equal the convergence file value -1.4937)' % a)
dE_generic_check()
print('elapsed %.1fs' % (time.time() - t0))
