"""R17-9 (b): photon-class sign scan for both local vertices (VU, VM), C_sub laws (d' in [0,1], whole-zone v_max = 1 attained in the box),
N = 64 (G-type) / 96 (narrow G_w turns), plus R8-5's own photon R85(1,2,G=1) and 'plateau' laws d' = 1 -> lam -> 0.
Also the SF shear (2 x scalar formula on omega) and the 'two-scalar' comparator VS = 2 x U-scalar Xi on omega (not a Maxwell stress)."""
import numpy as np, time
from photon import *
from zz import mu_E, xi_all
from sublum import sstep
t0 = time.time()
def r85(c1=1.0, c2=2.0, G=1.0):
    # R8-5's photon: d = rho q + (1 - rho) G 2 sin(q/2), rho a C^inf plateau 1 on |q|<=c1, 0 beyond c2
    a = np.linspace(0, np.pi, 400001); rho = 1 - sstep((a - c1)/(c2 - c1))
    d = rho*a + (1 - rho)*G*2*np.sin(a/2); dp = np.gradient(d, a)
    return PhotonProfile(lambda x: np.interp(x, a, dp), 'R85(%.1f,%.1f,G=%.1f)' % (c1, c2, G))
def plateau(b, lam, w2):
    return PhotonProfile(lambda a: 1 - (1 - lam)*sstep((a - b)/0.3) - lam*sstep((a - (b + 0.3 + w2))/0.3), 'plat(b%.1f,lam%.2f,w%.1f)' % (b, lam, w2))
laws = [(photonNN(), 64), (r85(), 64)] + [(photonG(b), 64) for b in (0.1, 0.2, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.1)] + \
       [(photonGw(b, w), 96) for b in (0.3, 0.8, 1.2, 1.6, 2.4) for w in (0.25, 0.5, 1.0) if b + w <= np.pi] + \
       [(plateau(b, lam, w2), 64) for b in (0.5, 1.0) for lam in (0.1, 0.4, 0.7) for w2 in (0.5, 1.0)]
res = []
for law, N in laws:
    vu = [photon_xi(law, N, p)[0] for p in ('T2g', 'Eg')]
    vm = [photon_xi_VM(law, N, p)[0] for p in ('T2g', 'Eg')]
    g, f = law.samples(1 << 14); mu = 2*mu_E(g, f, 1e-3); xs = xi_all(g, f, 1e-3)
    res.append((*vu, *vm, mu))
    print('%-26s N=%d VU %+.4e %+.4e | VM %+.4e %+.4e | mu_E(SF) %+.4e | VS(2xU-scalar) %+.3e %+.3e | d\' in [%.3f, %.6f]' %
          (law.name, N, *vu, *vm, mu, 2*xs['U,T2g'], 2*xs['U,Eg'], law.mindp, law.maxdp), flush=True)
R = np.array(res)
print('MIN over %d photon laws: VU T2g %+.4e Eg %+.4e | VM T2g %+.4e Eg %+.4e | mu_E range [%+.4e, %+.4e]' % (len(R), R[:, 0].min(), R[:, 1].min(), R[:, 2].min(), R[:, 3].min(), R[:, 4].min(), R[:, 4].max()))
print('elapsed %.1fs' % (time.time()-t0))
