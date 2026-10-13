"""R19-13: rigorous lower bound for Wilson-Dirac plane insertion (any operation on the slab of radius R).
Per transverse q (complex 4-component chain, number-conserving H):
   dE_q >= gap_q * D_T^2,  D_T >= || G_old(bR,bL) - G_new(bR,bL) ||_op,
using O = c_bL^dag X c_bR + h.c. with ||O|| = ||X||_1 (trace norm), so max |Delta<O>|/2 = ||Delta G||_op.
Old separation d = 2R+1, new d+1.  gap_q = min_k E(k,q).  P_-(k) = (1 - h(k)/E(k))/2 (h^2 = E^2 for Wilson-Dirac).
q-points with |q| < QMIN are dropped (keeps a lower bound; avoids k-sum resolution error there).
Usage: python r1913_dirac_lb.py m  -> r1913_dirac_lb_m{m}.out
"""
import sys, numpy as np
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
al = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]
be = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)
r = 1.0
m = float(sys.argv[1])
NK = 2 ** 14; QMIN = 5e-3
k = 2 * np.pi * (np.arange(NK) + 0.5) / NK
Rs = [1, 2, 4, 8, 16, 32, 64]
NQ = 70; p = 3.0
t = (np.arange(NQ) + 0.5) / NQ
qv = np.pi * t ** p; wv = p * t ** (p - 1) / NQ          # weights for (1/pi) int_0^pi dq
tot = {R: 0.0 for R in Rs}; wsum = 0.0
for i in range(NQ):
    for j in range(i + 1):
        qy, qz = qv[i], qv[j]
        w = wv[i] * wv[j] * (1 if i == j else 2); wsum += w
        if np.hypot(qy, qz) < QMIN:
            continue
        mu = m + r * (2 - np.cos(qy) - np.cos(qz))
        Mk = mu + r * (1 - np.cos(k))
        E = np.sqrt(np.sin(k) ** 2 + np.sin(qy) ** 2 + np.sin(qz) ** 2 + Mk ** 2)
        gap = E.min()
        # h(k)/E = (alpha_x sin k + alpha_y sin qy + alpha_z sin qz + beta Mk)/E
        cx = np.sin(k) / E; cy = np.sin(qy) / E; cz = np.sin(qz) / E; cb = Mk / E
        for R in Rs:
            d = 2 * R + 1
            def G(n):
                ph = np.exp(1j * k * n) / NK
                return 0.5 * (ph.sum() * np.eye(4) - (al[0] * (ph * cx).sum() + al[1] * (ph * cy).sum()
                                                      + al[2] * (ph * cz).sum() + be * (ph * cb).sum()))
            dG = G(d) - G(d + 1)
            sv = np.linalg.svd(dG, compute_uv=False)[0]
            tot[R] += w * gap * sv * sv
with open('r1913_dirac_lb_m%g.out' % m, 'w') as fo:
    fo.write('# Wilson-Dirac m=%g: rigorous lower bound per inserted site (BZ average), any slab operation; weight sum %.8f\n' % (m, wsum))
    for R in Rs:
        fo.write('R=%d  LB=%.6e\n' % (R, tot[R]))
    Rv = np.array(Rs, float); Lv = np.array([tot[R] for R in Rs])
    for a_, b_ in zip(Rs[:-1], Rs[1:]):
        fo.write('local exponent %d-%d: %.3f\n' % (a_, b_, -np.log(tot[b_] / tot[a_]) / np.log(b_ / a_)))
print(open('r1913_dirac_lb_m%g.out' % m).read())
