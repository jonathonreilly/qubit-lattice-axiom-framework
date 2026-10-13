"""R18-9 (b): checks at a root (argv[1] = root .npy: b_s, b_f, r, a, fr, b_g, fw, m).
(i) mu_T2 at the Dirac law by three evaluators: R16-13's dfam GL (archived), R17-13's lib13 forms P and I (archived, independent GL build);
(ii) Dirac UD rows at four GL resolutions; (iii) scalar quadrature n = 2^14 vs 2^16; (iv) whole-zone v_max of every edge;
(v) stencil weights and second moment."""
import sys, os, time, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch13'))
import lib9 as L
import lib13
import dfam
from content3 import D1q
from content4 import scalw
from photon import photonGw
z = np.load(sys.argv[1]); bs, bf, r, a, fr, bg, fw, m = z; t0 = time.time()
print('root: scalar G_w(%.10f, fr=%.4f); Dirac D1(%.10f, %.10f); photon gGw(%.6f, fw=%.4f); a = %.10f; m = %g' % (bs, fr, bf, r, bg, fw, a, m))
law = D1q(bf, r)
print('(i) mu_T2 per field: dfam GL(3,8) %+.3e  GL(6,12) %+.3e | lib13 P(8,16) %+.3e  P(12,24) %+.3e  I(12,24) %+.3e' % (
    dfam.evaluate(law, m, 3, 8)['muT2'], dfam.evaluate(law, m, 6, 12)['muT2'],
    lib13.muT2(lib13.D1law(bf, r), m, 8, 16), lib13.muT2(lib13.D1law(bf, r), m, 12, 24), lib13.muT2(lib13.D1law(bf, r), m, 12, 24, form='I')))
pp = lib13.muT2_parts(lib13.D1law(bf, r), m, 8, 16); print('    parts (KK, KM, MM):', pp)
print('    d mu_T2/d b_f = %+.4e, d mu_T2/d r = %+.4e (per field)' % ((L.muT2(bf+1e-5, r, m) - L.muT2(bf-1e-5, r, m))/2e-5, (L.muT2(bf, r+1e-5, m) - L.muT2(bf, r-1e-5, m))/2e-5))
for q in ((3, 8), (4, 10), (5, 12), (6, 16)):
    F = L.dirac(bf, r, m=m, q=q); print('(ii) Dirac UD GL%s: T %+.9e E %+.9e muE %+.9e muT2 %+.2e' % (q, *F))
s1, Ls = scalw(bs, fr, m, vert='U'); s2, _ = scalw(bs, fr, m, vert='U', n=1 << 16, nu=3000)
print('(iii) scalar n=2^14: %s ; 2^16/nu3000 minus 2^14: %s' % (s1[:3], (s2 - s1)[:3]))
print('(iv) v_max: scalar edge %.6f ; Dirac sampled %.6f (Lemma V1: r = %.6f <= 1/sqrt3 = %.6f) ; ' % (Ls.vmax(m), dfam.vmax_sample(law, m, 161), r, 1/np.sqrt(3)), end='')
ph = photonGw(bg, fw*(np.pi - bg)); k = np.linspace(0, np.pi, 200001); dp = ph.dpr(k)
print("photon d' in [%.6f, %.6f] => |grad omega| <= 1" % (dp.min(), dp.max()))
print('(v) stencil: weight %.6f at z+-1/2, %.6f at z+-3/2; P(0) = 1; lam = 1/4 + 2a = %+.6f' % (1 - a, a, 0.25 + 2*a))
print('%.0fs' % (time.time() - t0))
