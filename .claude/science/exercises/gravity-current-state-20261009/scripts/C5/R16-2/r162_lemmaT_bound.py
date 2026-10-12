"""R16-2 Lemma T' (integration by parts, photon-monotone form). For fixed q_perp, w(q) = 1/(d(q)^2 W), W^2 = d(q)^2 + D',
D' = d_y^2 + d_z^2 + lam^2. If d is nondecreasing on [0, pi] then w' <= 0 on (0, pi], and for an odd symbol S with S = q on
[0,b], S(pi) = 0 and S(q) <= q on [b, pi]:
   int_b^pi (S' - 1) w dq = -pi w(pi) + int_b^pi (q - S) w' dq <= -pi w(pi) < 0.
Hence Dirac tadpole (m -> 0): dc_tad = (1/2) <(S'-1) w>  <=  -(1/2) <w(pi)>_perp   (x16pi^2 printed).
Scalar (u even, u = q^2 on [0,b], u'(pi) = 0, u'/2 <= q on [b,pi]): int_b^pi A w = -pi w(pi) + int (q - u'/2) w' <= -pi w(pi),
   so dc_seagull = (1/4) <A w> <= -(1/4) <w(pi)>_perp.
Axis subluminality at m -> 0 gives S <= q (Dirac, Wilson or not: |(W,s)| <= k) and u'/2 <= sqrt(u) <= q (scalar).
Checks: photon monotonicity of d; the bound vs the measured tadpole/seagull (runner columns) for the tested laws."""
import numpy as np, sys
sys.path.insert(0, '.')
from r162_laws import D1Law, GScal, photon_d
from r85_box_qed_copy import kgrid1, Law
from sublum import SymS
U = 16*np.pi**2
def wpi_mean(d, N, lam):
    q = kgrid1(N); QY, QZ = np.meshgrid(q, q, indexing='ij')
    Dp = d(QY)**2 + d(QZ)**2 + lam**2; dpi = float(d(np.array(np.pi)))
    return np.mean(1/(dpi**2*np.sqrt(dpi**2 + Dp)))
def tad_closed(S_prime, d, N, lam):
    q = kgrid1(N); QX, QY, QZ = np.meshgrid(q, q, q, indexing='ij')
    W = np.sqrt(d(QX)**2 + d(QY)**2 + d(QZ)**2 + lam**2)
    return np.mean((S_prime(QX) - 1)/(d(QX)**2*W))/2*U
qq = np.linspace(0, np.pi, 100001)
for (c1, c2) in [(None, None), (1.0, 2.0), (2.0, 3.0), (0.5, 1.5), (1.4, 1.6), (2.5, 3.1), (2.8, 3.1)]:
    d = photon_d(c1, c2); dd = np.diff(d(qq)); mono = dd.min() >= -1e-12
    lam = 0.05; N = 128; wp = wpi_mean(d, N, lam)
    print('photon (%s,%s): d nondecreasing on [0,pi]: %s (min step %.2e) | Dirac bound -(1/2)<w(pi)>U = %+8.4f | scalar bound -(1/4)<w(pi)>U = %+8.4f'
          % (c1, c2, mono, dd.min(), -0.5*wp*U, -0.25*wp*U))
    # measured tadpoles (m -> 0 S-part) on D1 symbols and literal BQ, and scalar seagulls
    out = []
    for b in (1.0, 1.4):
        A = SymS(b); out.append(('D1 S(%.1f)' % b, tad_closed(A.ds, d, N, lam), -0.5*wp*U))
    for (b1, b2) in [(1.0, 2.0), (0.5, 1.5), (2.5, 3.1)]:
        L = Law(b1, b2, 0.0, None, None, 0.1)
        Sp = lambda k, L=L: (L.S(k + 1e-5) - L.S(k - 1e-5))/2e-5
        out.append(('LIT(%.1f,%.1f)' % (b1, b2), tad_closed(Sp, d, N, lam), -0.5*wp*U))
    for b in (0.6, 1.4, 2.6):
        G = GScal(b, c1, c2, 0.1)
        Aq = lambda k, G=G: G.upp(k)/2 - 1
        q = kgrid1(N); QX, QY, QZ = np.meshgrid(q, q, q, indexing='ij')
        W = np.sqrt(d(QX)**2 + d(QY)**2 + d(QZ)**2 + lam**2)
        out.append(('G(%.1f) seagull' % b, np.mean(Aq(QX)/(2*d(QX)**2*W))/2*U, -0.25*wp*U))
    print('   ' + ' | '.join('%s %+8.4f (<= %+7.4f: %s)' % (n, v, bd, v <= bd + 1e-9) for n, v, bd in out))
