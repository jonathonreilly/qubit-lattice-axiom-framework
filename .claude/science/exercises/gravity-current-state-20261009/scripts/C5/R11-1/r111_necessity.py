"""C5 R11-1 (a): checks for the necessity theorems (N*: measure pairing across statistics; S: species-level pairing).

Coefficient forms used (refereed or rechecked inputs):
  photon, complex scalar, band u (Theorem T', R10-1, refereed):      C = (q^2/32) < u'(k_y)^2 A(k_x) / eps^5 >
  photon, Clifford-flat fermion, 8 comp, v = S^2+W^2 (Theorem P, ref): C = -(q^2/8) < v'(k_y)^2 A_v(k_x) / E^5 >
  graviton TT (T_2g, q || z), complex scalar = 2 real, vertex |V|^2 (Theorem T, R9-9 ref): C = (2/32) < |V|^2(kx,ky) A(k_z)/eps^5 >
  graviton TT, Clifford-flat 8-comp fermion, vielbein vertex (R10-5 Theorem PT, unrefereed; rechecked there):
                                                                       C = - < S_x^2 S_y^2 A_v(k_z) / E^5 >
Laplace form: eps^-5 = Gamma(5/2)^-1 int dt t^{3/2} e^{-t eps^2}; with separable bands the t-integrand factorizes into
1D transforms F_A(t) = <A e^{-tu}>, F_w(t) = <w e^{-tu}>, F_1(t) = <e^{-tu}>.  Total mass of each species' measure = value at t=0.
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from r99_profiles_copy import profile
from r101_pairing_copy import make_box_curve, wilson_curve
from scipy.special import gamma
from scipy.integrate import quad

NK = 4096
k = (np.arange(NK) + 0.5) * 2 * np.pi / NK - np.pi

def scalar_band(name):
    u, up, upp = profile(name, k)
    return dict(u=u, up=up, A=upp / 2 - 1, w=u)          # w: TT vertex function (minimal metric M: |V|^2 = 4 w_x w_y)

def fermion_band(cur):
    S, W, Sp, Wp = cur['S'](k), cur['W'](k), cur['Sp'](k), cur['Wp'](k)
    v = S * S + W * W; vp = 2 * (S * Sp + W * Wp)
    h = 1e-4
    vpp = ((cur['S'](k + h) ** 2 + cur['W'](k + h) ** 2) - 2 * v + (cur['S'](k - h) ** 2 + cur['W'](k - h) ** 2)) / h ** 2
    return dict(u=v, up=vp, A=vpp / 2 - 1, w=S * S, unit=np.max(np.abs(Sp ** 2 + Wp ** 2 - 1)))

def F(t, band, key):
    wgt = {'A': band['A'], 'V': band['up'] ** 2, '1': 1.0, 'w': band['w']}[key]
    return np.mean(wgt * np.exp(-t * band['u']))

def C_photon(band, m, sign_norm):
    """(norm) <u'(ky)^2 A(kx)/eps^5> via the Laplace form (exact for separable bands)."""
    g = lambda t: t ** 1.5 * np.exp(-t * m * m) * F(t, band, 'A') * F(t, band, 'V') * F(t, band, '1')
    val = quad(g, 0, np.inf, limit=400)[0] / gamma(2.5)
    return sign_norm * val

def C_tt(band, m, sign_norm):
    """(norm) <w_x w_y A(kz)/eps^5> (vertex |V|^2 = 4 w_x w_y for bosons -> norm includes the 4)."""
    g = lambda t: t ** 1.5 * np.exp(-t * m * m) * F(t, band, 'A') * F(t, band, 'w') ** 2
    return sign_norm * quad(g, 0, np.inf, limit=400)[0] / gamma(2.5)

def direct3d_photon(band, m, N=96):
    kk = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    # re-evaluate on the coarse grid by interpolation of the fine-grid band (periodic, smooth)
    u = np.interp(kk, k, band['u']); up = np.interp(kk, k, band['up']); A = np.interp(kk, k, band['A'])
    e2 = m * m + u[:, None, None] + u[None, :, None] + u[None, None, :]
    return np.mean(A[:, None, None] * (up ** 2)[None, :, None] / e2 ** 2.5)

if __name__ == '__main__':
    bos = {n: scalar_band(n) for n in ['G', 'L', 'NN']}
    fer = {'Wilson': fermion_band(wilson_curve()), 'box0.5': fermion_band(make_box_curve(0.5, 1.2)),
           'box0.8': fermion_band(make_box_curve(0.8, 1.6))}
    for n, f in fer.items():
        bos['v[' + n + ']'] = dict(u=f['u'], up=f['up'], A=f['A'], w=f['w'])   # complex scalar on the fermion's curve v, TT vertex S^2
    print('== 1. Total masses (t = 0 values): every species has sign fixed by statistics (zone mean <A> = -1) ==')
    print('   boson (complex scalar): photon total = (1/32) <u_y^2>*<A> ; TT total (M vertex, w=u; or pairing vertex w=S^2) = (2/32)*4 <w>^2 <A>')
    for n, b in bos.items():
        print('   boson %-12s <A> = %+.10f   photon total = %+.5e   TT total = %+.5e   (both < 0)'
              % (n, np.mean(b['A']), np.mean(b['up'] ** 2) * np.mean(b['A']) / 32, 0.25 * np.mean(b['w']) ** 2 * np.mean(b['A'])))
    for n, f in fer.items():
        print('   fermion %-10s (8 comp) unit-speed err %.1e <A_v> = %+.10f   photon total = %+.5e   TT total = %+.5e   (both > 0)'
              % (n, f['unit'], np.mean(f['A']), -np.mean(f['up'] ** 2) * np.mean(f['A']) / 8, -np.mean(f['w']) ** 2 * np.mean(f['A'])))
    print('\n== 2. Laplace form vs direct 3D mean (check of the factorized representation), photon, scalar G, m = 0.3 ==')
    for n in ['G', 'L']:
        lap = C_photon(bos[n], 0.3, 1.0); d3 = direct3d_photon(bos[n], 0.3)
        print('   %s: Laplace %+.8e   direct N=96 %+.8e   rel diff %.1e' % (n, lap, d3, abs(lap - d3) / abs(d3)))
    print('\n== 3. Paired content (complex scalars on v, TT vertex S^2) vs unpaired content tuned to the t=0 total, photon and TT ==')
    ms = np.linspace(0.05, 1.5, 30)
    for fn in ['box0.8', 'Wilson']:
        f = fer[fn]; bp = bos['v[' + fn + ']']
        # paired: 4 complex scalars per 8-comp fermion (unit charges); TT: 4 complex scalars = 8 real, vertex S^2
        ph = np.array([4 * C_photon(bp, m, 1 / 32) + C_photon(f, m, -1 / 8) for m in ms])
        tt = np.array([4 * C_tt(bp, m, 2 * 4 / 32) + C_tt(f, m, -1.0) for m in ms])
        print('   PAIRED  (4 cplx scalars on v[%s] + 1 fermion): max |C_photon| over m in [0.05,1.5] = %.1e ; max |C_TT| = %.1e'
              % (fn, np.max(np.abs(ph)), np.max(np.abs(tt))))
    # unpaired: bosons on G (R8-2 gapped edge, box B = 2.0), fermion box0.8; boson multiplicity x chosen to null the t=0 total
    for bn, fn in [('G', 'box0.8'), ('v[box0.5]', 'box0.8'), ('L', 'Wilson')]:
        b, f = bos[bn], fer[fn]
        xg = (np.mean(f['up'] ** 2) / 8) / (np.mean(b['up'] ** 2) / 32)            # complex scalars per fermion (photon totals)
        ph = np.array([xg * C_photon(b, m, 1 / 32) + C_photon(f, m, -1 / 8) for m in ms])
        xt = np.mean(f['w']) ** 2 / (0.25 * np.mean(b['w']) ** 2)                   # TT totals (M vertex w = u for G, L)
        tt = np.array([xt * C_tt(b, m, 2 * 4 / 32) + C_tt(f, m, -1.0) for m in ms])
        zc = np.sum(np.sign(ph[1:]) != np.sign(ph[:-1])); zt = np.sum(np.sign(tt[1:]) != np.sign(tt[:-1]))
        print('   UNPAIRED bosons %-10s x_ph = %.4f x_tt = %.4f per fermion %s: C_photon(m) in [%+.2e, %+.2e] (%d sign changes), '
              'C_TT(m) in [%+.2e, %+.2e] (%d sign changes)' % (bn, xg, xt, fn, ph.min(), ph.max(), zc, tt.min(), tt.max(), zt))
        print('      C_photon at m = 0.05, 0.3, 1.0: %+.3e %+.3e %+.3e' % (ph[0], np.interp(0.3, ms, ph), np.interp(1.0, ms, ph)))
    print('\n== 4. Edge onset (A masked to exactly 0 on the box, removing finite-difference noise): -(1/t) ln|F_A(t)| -> u(face) = b^2 ==')
    for n, bx in [('G', 2.0), ('L', 2.0), ('v[box0.5]', 0.5), ('v[box0.8]', 0.8)]:
        b = bos[n]; Am = np.where(np.abs(k) <= bx, 0.0, b['A'])
        out = []
        for t in [2.0, 5.0, 10.0, 20.0]:
            FA = np.mean(Am * np.exp(-t * b['u']))
            out.append('t=%4.1f: %.3f (sign %+d)' % (t, -np.log(abs(FA)) / t, int(np.sign(FA))))
        print('   %-10s b^2 = %.3f | ' % (n, bx * bx) + ' ; '.join(out))
