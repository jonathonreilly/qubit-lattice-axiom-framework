"""C5 R9-9: INV control. TT pair vertex times a compact invariant-mass form factor f(s), s = (eps+eps')^2 - q^2,
f = 1 on s <= s1, 0 on s >= s2 (C^inf plateau), chosen so every pair on supp f has both legs inside the matter box
(|k_i| < B = 2) and the box dispersion there is exactly continuum.  Expectation (Kallen-Lehmann, proved in the report):
alpha + beta = 0 exactly (Lorentz-invariant paramagnetic part); the k^2 = 0 value Pi_para(0,0) is NOT zero.
Same grid-shift + Richardson alpha as r99_tt_selfenergy.py.  Profiles G (edge irrelevant on supp f) and NN (control: not box)."""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles import profile, sstep
def fplat(s, s1, s2):
    return sstep((s2 - s)/(s2 - s1))
for name, m, s1, s2 in [('G', 1.0, 9.0, 16.0), ('G', 0.3, 4.0, 9.0), ('NN', 1.0, 9.0, 16.0)]:
    for N in (96, 160):
        k = 2*np.pi*(np.arange(N) - N//2)/N
        u = profile(name, k)[0]
        ux, uy, uz = u[:, None, None], u[None, :, None], u[None, None, :]
        eps = np.sqrt(m*m + ux + uy + uz)
        dq = 2*np.pi/N
        out = []
        for vn, V2 in [('T2g', 4*ux*uy), ('Eg', (ux-uy)**2)]:
            V2b = np.broadcast_to(V2, eps.shape)
            def Pi(n, w2=0.0):
                epsp = np.roll(eps, n, axis=2); E = eps+epsp; q = n*dq
                f = fplat(E*E - q*q, s1, s2)
                return -0.25*np.mean(V2b*f*f/(eps*epsp)*E/(E*E - w2))
            P0 = Pi(0); alpha = (16*(Pi(1)-P0) - (Pi(2)-P0))/(12*dq*dq)
            hw = 1e-3; beta = (Pi(0, hw) - Pi(0, -hw))/(2*hw)       # d/d(w^2) at fixed q = 0 (f depends on s = E^2, not on w)
            # maximal |k_i| on supp f
            kmax = np.max(np.abs(k)[np.any(fplat(4*eps**2, s1, s2) > 0, axis=(1, 2))])
            out.append('%s: alpha=%+.6e beta=%+.6e alpha+beta=%+.2e  Pi_para(0,0)=%+.6e' % (vn, alpha, beta, alpha+beta, P0))
        print('[%s m=%.1f N=%d, f support s<=%.0f, max|k_x| on supp(q=0) = %.3f]  ' % (name, m, N, s2, kmax) + ' | '.join(out))
