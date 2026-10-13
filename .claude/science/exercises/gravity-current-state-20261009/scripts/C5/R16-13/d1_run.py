"""R16-13: Dirac D1(1.4, r) graviton-cone shift (both polarizations) and strain shear masses, per 4-comp Dirac field.
Shift method (independent of the identity) at m=0.3; A-form at all masses; strain mu^F = -4 mu^s[E]."""
import numpy as np, time, sys
from dirac import D1, dirac_xi, strain_mu
from aform import d1_aform
t0 = time.time()
for r in (0.30, 0.5773):
    law = D1(1.4, r)
    print('== D1(1.4, r=%.4f): W_pi = %.4f' % (r, law.Wpi), flush=True)
    for N in (96, 144):
        for pol in ('T2g', 'Eg'):
            rr = dirac_xi(law, 0.3, N, pol=pol, Nc=4, kind='D1')
            print('  shift-method m=0.3 N=%d %s: alpha %+.6e beta %+.6e Xi_F %+.6e' % (N, pol, rr['alpha'], rr['beta'], rr['Xi']), flush=True)
    for m in (0.3, 0.1, 0.03, 0.01):
        for N in (96, 144, 192):
            o = d1_aform(law, m, N)
            muE, muT = strain_mu(law, m, N, kind='D1')
            print('  A-form m=%.2f N=%d: Xi_F T2g %+.6e (a %+.3e, s %+.3e) | Eg %+.6e (a %+.3e, s %+.3e) | mu_E^F %+.6e  mu_T2^F %+.6e' % (
                m, N, o['T2g'][0], o['T2g'][1], o['T2g'][2], o['Eg'][0], o['Eg'][1], o['Eg'][2], -4*muE, -4*muT), flush=True)
print('elapsed %.1fs' % (time.time()-t0))
