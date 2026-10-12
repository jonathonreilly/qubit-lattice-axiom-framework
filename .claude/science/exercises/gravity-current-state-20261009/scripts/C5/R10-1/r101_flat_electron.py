"""R10-1 check 5: electron self-energy speed shift for the Clifford-flat box law (what pairing of the photon leaves).

R8-5's fermion() (r85_box_qed.py:120-170, referee-confirmed) adapted to the Clifford-flat 8-component law
h = sum_j [S(k_j) alpha_j + W(k_j) beta_j] + m beta_0 (separate beta_j): the x-hop's Wilson part lies along beta_x,
so the beta component used in the alpha_x projection is n_{beta_x} = W(k_x)/E, and E^2 = m^2 + sum_j (S_j^2 + W_j^2).
Photon: R8-5 box symbol d (plateau c1, c2).  Validation: with flat=False the code reduces to R8-5's own fermion().
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r85_box_qed_copy import Law, kgrid1, deriv, fermion, photon
from r101_pairing import make_box_curve, wilson_curve
def flat_moments(cur, m, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W, Sp, Wp = cur['S'](k), cur['W'](k), cur['Sp'](k), cur['Wp'](k)
    h = 1e-4
    v = S ** 2 + W ** 2
    vpp = ((cur['S'](k + h) ** 2 + cur['W'](k + h) ** 2) - 2 * v + (cur['S'](k - h) ** 2 + cur['W'](k - h) ** 2)) / h ** 2
    A = vpp / 2 - 1
    X = S * Sp + W * Wp                      # x.h for the y-axis curve
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    E = np.sqrt(m * m + v[IX] + v[IY] + v[IZ])
    XD = -np.mean(A[IX] * X[IY] ** 2 / (4 * E ** 5))
    XS = np.mean(A[IX] * X[IY] ** 2 / (8 * E ** 5))
    return XD, XS, A


U = 16 * np.pi ** 2

class FlatLaw:
    def __init__(self, cur, c1, c2, m):
        self.cur, self.m = cur, m
        self.ph = Law(None, None, 0.0, c1, c2, m)
    def S(self, k): return self.cur['S'](k)
    def W(self, k): return self.cur['W'](k)
    def d(self, q): return self.ph.d(q)

def fermion_flat(law, N, lam, hp=(1e-3, 2e-3), chunk=16):
    q1 = kgrid1(N)
    QY, QZ = np.meshgrid(q1, q1, indexing='ij')
    dqy2, dqz2 = law.d(QY) ** 2, law.d(QZ) ** 2
    Sy, Wy, Sz, Wz = law.S(-QY), law.W(-QY), law.S(-QZ), law.W(-QZ)
    W0 = law.W(np.array(0.0))
    dly = (0 - Sy, W0 - Wy); dlz = (0 - Sz, W0 - Wz)
    A_id = 0.0; tadd = 0.0
    sun = {p: 0.0 for p in [s * h for h in hp for s in (+1, -1)]}
    S0p = deriv(law.S, np.array(0.0))
    for i0 in range(0, N, chunk):
        qx = q1[i0:i0 + chunk][:, None, None]
        dqx2 = law.d(qx) ** 2
        Om = np.sqrt(dqx2 + dqy2[None] + dqz2[None] + lam ** 2)
        tadd += np.sum((deriv(law.S, qx) - S0p) / (2 * Om * dqx2) + 0 * Om)
        for p in list(sun.keys()) + [0.0]:
            kx = p - qx
            Sx, Wx = law.S(kx), law.W(kx)
            E = np.sqrt(Sx ** 2 + Wx ** 2 + Sy[None] ** 2 + Wy[None] ** 2 + Sz[None] ** 2 + Wz[None] ** 2 + law.m ** 2 + 0 * Om)
            nax, nbx = Sx / E, Wx / E
            dxa = law.S(np.array(p)) - Sx; dxb = law.W(np.array(p)) - Wx
            if p == 0.0:
                s2 = (dxa ** 2 + dxb ** 2) / dqx2 + (dly[0] ** 2 + dly[1] ** 2)[None] / dqy2[None] \
                     + (dlz[0] ** 2 + dlz[1] ** 2)[None] / dqz2[None]
                A_id += np.sum((s2 - 1) / (2 * Om * (Om + E) ** 2))
                continue
            dn_x = dxa * nax + dxb * nbx
            comp = (2 * dn_x * dxa - (dxa ** 2 + dxb ** 2) * nax) / dqx2
            comp += (-(dly[0] ** 2 + dly[1] ** 2)[None] * nax) / dqy2[None]
            comp += (-(dlz[0] ** 2 + dlz[1] ** 2)[None] * nax) / dqz2[None]
            comp -= nax
            sun[p] += np.sum(-comp / (2 * Om * (Om + E)))
    V = N ** 3
    A_id /= V; tadd /= V
    for p in sun: sun[p] /= V
    h1, h2 = hp
    D1 = (sun[h1] - sun[-h1]) / (2 * h1); D2 = (sun[h2] - sun[-h2]) / (2 * h2)
    B = (4 * D1 - D2) / 3 + tadd
    return dict(A_id=A_id, B=B, dce=B - A_id)

if __name__ == '__main__':
    t0 = time.time()
    # validation of the adapted code path: Wilson circle with SHARED beta is R8-5's r=1 no-box law; flat differs.
    print('electron speed shift dc_e x16pi^2 (Feynman gauge, R8-5 method), photon moment from pairing formulas')
    for lab, cur, c1, c2 in [('Wilson circle, flat, no photon box', wilson_curve(), None, None),
                             ('box curve b1=0.8 b2=1.6, flat, photon box (0.8,1.6)', make_box_curve(0.8, 1.6), 0.8, 1.6)]:
        for m, N in [(0.05, 96), (0.05, 160)]:
            law = FlatLaw(cur, c1, c2, m)
            fe = fermion_flat(law, N, m)
            XD, XS, _ = flat_moments(cur, m, 128)
            print('  %-52s m=%.2f N=%3d | dc_e %+8.4f | dc_gamma(Dirac 4comp) %+7.4f, +2 scalars -> %+.1e | Delta(no partners) %+8.4f'
                  % (lab, m, N, fe['dce'] * U, XD * U, (XD + 2 * XS) * U, (fe['dce'] - XD) * U), flush=True)
    # control: R8-5's own fermion() on its r=1 no-box law (shared beta), for the record
    fe = fermion(Law(None, None, 1.0, None, None, 0.05, naive_photon=True), 96, 0.05)
    print('  control R8-5 fermion(), Wilson r=1 shared beta, naive photon, m=0.05 N=96: dc_e %+8.4f (r85_shapes.out: -21.41 at N=224)' % (fe['dce'] * U))
    print('elapsed %.1fs' % (time.time() - t0))
