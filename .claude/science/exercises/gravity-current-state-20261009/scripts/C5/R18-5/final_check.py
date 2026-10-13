"""R18-5: final record at the stepped root (smroot_C160.npy): per-species parts (photon N=160, Dirac GL(5,12)),
scalar quadrature convergence, whole-zone v_max of every edge, and the stencil weights."""
import numpy as np, time
import dfam
from content3 import D1q
from content4 import scalw
from smud_lib import dirac, phot, NS, ND, NV
from photon import photonGw
t0 = time.time(); z = np.load('smroot_C160.npy'); bg, fwg, bf, r, bs, frs, a = z; wg = fwg*(np.pi-bg); ws = frs*(np.pi-bs)
print('photon gammaGw(b=%.9f, w=%.9f) [VWa, a=%.9f: weights (1-a, a) = (%.6f, %.6f) at z+-1/2, z+-3/2; lam = %.6f]' % (bg, wg, a, 1-a, a, 0.25+2*a))
print('Dirac D1(b=%.9f, r=%.9f) [UD]  scalar G_w(b=%.9f, w=%.9f) [U]  m = 0.01' % (bf, r, bs, ws))
s1, L = scalw(bs, frs, 0.01, vert='U'); s2, _ = scalw(bs, frs, 0.01, vert='U', n=1 << 16, nu=3000)
print('scalar per real (T2g, Eg, muE): n=2^14 %s | n=2^16,nu=3000 diff %s' % (s1[:3], (s2 - s1)[:3]))
print('scalar edge vmax(m=0.01) = %.6f' % L.vmax(0.01))
F = dirac(bf, r, q=(5, 12)); V = phot(bg, wg, 160, 'VWa', a)
print('per Dirac field (UD): Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e mu_T2 %+.6e' % tuple(F))
print('per vector (VWa, N=160): Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e' % tuple(V[:3]))
print('per real scalar (U): Xi_T2g %+.6e Xi_Eg %+.6e mu_E %+.6e' % tuple(s1[:3]))
t = NS*s1 + ND*F + NV*V
print('TOTAL (4 + 22.5 + 12): Xi_T2g %+.3e Xi_Eg %+.3e mu_E %+.3e | mu_T2 %+.4e' % tuple(t))
print('contributions T2g: scal %+.4e dirac %+.4e vec %+.4e' % (NS*s1[0], ND*F[0], NV*V[0]))
print('contributions Eg : scal %+.4e dirac %+.4e vec %+.4e' % (NS*s1[1], ND*F[1], NV*V[1]))
print('contributions muE: scal %+.4e dirac %+.4e vec %+.4e' % (NS*s1[2], ND*F[2], NV*V[2]))
law = D1q(bf, r); print('Dirac edge sampled vmax = %.6f (n=161); Lemma V1 bound 1 since r = %.6f < 1/sqrt3 = %.6f' % (dfam.vmax_sample(law, 0.01, 161), r, 1/np.sqrt(3)))
ph = photonGw(bg, wg); k = np.linspace(0, np.pi, 200001); dp = ph.dpr(k)
print('photon d\' range [%.6f, %.6f] (class d\' in [0,1] => |grad omega| <= 1; = 1 inside the box)' % (dp.min(), dp.max()))
print('%.0fs' % (time.time() - t0))
