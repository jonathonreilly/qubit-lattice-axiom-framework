"""R10-1 check 1: the Dirac-sea photon speed shift of R8-5's box QED (BQ) as an anomaly moment.

Identity (r101_dirac_symbolic.out; proved by symbolic algebra + integration by parts along k_x on the torus):
  dc_gamma = < R_D >,  R_D = a (E^2 x^2 - X^2)/(4E^5) - (a+b) * 0 ... written as
  R_D = a * x^2/(4E^3)  -  A * X^2/(4E^5)  -  c1 (h.h') X/(2E^5)  +  c2 X/(2E^3)
  with x = dh/dk_y (Ward-forced current vertex), X = x.h, E^2 = h.h, h' = dh/dk_x, h'' = d2h/dk_x2,
  a = |h'|^2 - 1, b = h.h'', A = a + b = Hess_xx(E^2/2) - 1, c1 = x.h', c2 = x.h''.
Compare with R8-5's directly computed dc_gamma (r85_shapes.out, r85_heavy_edge.out; referee-confirmed).
Every term vanishes where k_x is inside the fermion box and the k_y-vertex is continuum: the box contributes 0.
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r85_box_qed_copy import Law, deriv, kgrid1, photon

U = 16 * np.pi ** 2

def moment(law, N, chunk=16):
    k1 = kgrid1(N)
    KY, KZ = np.meshgrid(k1, k1, indexing='ij')
    Sy, Wy, Sz, Wz = law.S(KY), law.W(KY), law.S(KZ), law.W(KZ)
    xy, xb = deriv(law.S, KY), deriv(law.W, KY)       # x = (0, S'(ky), 0, W'(ky))
    acc = dict(a=0.0, A=0.0, mix=0.0, tot=0.0, a_only_edge=0.0)
    for i0 in range(0, N, chunk):
        kx = k1[i0:i0 + chunk][:, None, None]
        Sx, Wx = law.S(kx), law.W(kx)
        Sxp, Wxp = deriv(law.S, kx), deriv(law.W, kx)
        Sxpp, Wxpp = deriv(law.S, kx, 2), deriv(law.W, kx, 2)
        M = law.m + Wx + Wy[None] + Wz[None]
        E2 = Sx ** 2 + Sy[None] ** 2 + Sz[None] ** 2 + M ** 2
        E = np.sqrt(E2)
        x2 = (xy ** 2 + xb ** 2)[None] + 0 * E
        X = xy[None] * Sy[None] + xb[None] * M
        a = Sxp ** 2 + Wxp ** 2 - 1 + 0 * E
        b = Sx * Sxpp + M * Wxpp
        A = a + b
        hhp = Sx * Sxp + M * Wxp
        c1 = xb[None] * Wxp
        c2 = xb[None] * Wxpp
        ta = a * x2 / (4 * E ** 3)
        tA = -A * X ** 2 / (4 * E ** 5)
        tm = -c1 * hhp * X / (2 * E ** 5) + c2 * X / (2 * E ** 3)
        acc['a'] += ta.sum(); acc['A'] += tA.sum(); acc['mix'] += tm.sum()
    V = N ** 3
    out = {k: v / V * U for k, v in acc.items()}
    out['tot'] = out['a'] + out['A'] + out['mix']
    return out

if __name__ == '__main__':
    t0 = time.time()
    shapes = [  # (label, b1, b2, r, c1, c2, R8-5 dc_g*U at m=0.025,N=320 [r85_shapes.out])
        ('S1', 1.0, 2.0, 1.0, 1.0, 2.0, 2.3671),
        ('S2', 1.5, 2.5, 1.0, 1.5, 2.5, 5.3204),
        ('S3', 2.0, 3.0, 1.0, 2.0, 3.0, 15.1618),
        ('S4', 2.0, 3.0, 0.5, 2.0, 3.0, 20.0980),
        ('S5', 0.5, 1.5, 1.0, 0.5, 1.5, 1.5040),
        ('S7', 1.0, 3.0, 1.0, 1.0, 3.0, 2.7190),
        ('S8', 2.5, 3.1, 1.0, 2.5, 3.1, 65.5786),
        ('Wilson r=1 no box', None, None, 1.0, None, None, 0.8501),
    ]
    print('Dirac (BQ) photon speed shift: anomaly moment <R_D>*16pi^2 vs R8-5 direct dc_gamma*16pi^2')
    print('label | m | N | a-moment | A-moment | Wilson-mix | total moment | R8-5 direct (m=0.025) | direct here (r85 photon(), m, N=160)')
    for lab, b1, b2, r, c1, c2, ref in shapes:
        for m, N in [(0.025, 96), (0.025, 160)]:
            law = Law(b1, b2, r, c1, c2, m)
            mo = moment(law, N)
            line = '%-18s | %.3f | %3d | %+9.4f | %+9.4f | %+9.4f | %+9.4f | %+9.4f' % (
                lab, m, N, mo['a'], mo['A'], mo['mix'], mo['tot'], ref)
            if N == 160 and lab in ('S3', 'Wilson r=1 no box', 'S1'):
                ph = photon(law, 160)
                line += ' | %+9.4f' % (ph['dcg'] * U)
            print(line, flush=True)
    # naive (r=0, no box): the moment carries every doubler; compare to r85 photon() directly
    for m, N in [(0.2, 48), (0.1, 64)]:
        law = Law(None, None, 0.0, None, None, m, naive_photon=True)
        mo = moment(law, N)
        ph = photon(law, N)
        print('naive r=0 (F2 law)  | %.3f | %3d | a %+8.4f A %+8.4f mix %+8.4f | total %+9.4f | direct(r85 photon, same N) %+9.4f'
              % (m, N, mo['a'], mo['A'], mo['mix'], mo['tot'], ph['dcg'] * U))
    # heavy edge series (r85_heavy_edge.out: S3, m = 0.05: Delta photon term +15.0,+25.2,+70.4,+172.4,+367.6,+706.1)
    print('heavy-edge series S3, m=0.05, N=160: r, moment total (a, A, mix); R8-5 dc_g*U')
    for r, ref in [(1, 15.0), (2, 25.2), (4, 70.4), (8, 172.4), (16, 367.6), (32, 706.1)]:
        law = Law(2.0, 3.0, float(r), 2.0, 3.0, 0.05)
        mo = moment(law, 160)
        print('  r=%2d  total %+9.3f  (a %+9.3f, A %+9.3f, mix %+9.3f)   R8-5 %+7.1f' % (r, mo['tot'], mo['a'], mo['A'], mo['mix'], ref), flush=True)
    print('elapsed %.1fs' % (time.time() - t0))
