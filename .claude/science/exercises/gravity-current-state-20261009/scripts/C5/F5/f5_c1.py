"""F5 (b)(iv) structural cross-check: the vacuum's mass slope of the E_g shear row on the R18-9 root's Dirac edge,
d mu_E/dm = d^2_t e_m (e = -2<E o Phi_t>, per field), which is the coefficient R19-21's Higgs/matter channel multiplies by
the matter-induced mass shift (R19-11's c1 = +1.06932e-2 per field on the 0+ root, r1921_history.py:4).  The rule (which only
re-sets m_c(h)) leaves this coefficient untouched.  GL octant grid as f5_nn; argv: n hmax mph"""
import numpy as np, time, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from f5_lib import *
t00 = time.time()
n, hm, mph = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])
for lab, rt in (('R18-9 root', ROOT),):
    br = mkbreaks(rt[0], CPH, mph); x, w = panels(br, n, hm)
    X, Y, Z = x[:, None, None], x[None, :, None], x[None, None, :]
    WW = w[:, None, None]*w[None, :, None]*w[None, None, :]
    def evac(t, m, h=H_EG, nrk=4):
        Fm = Ferm(*rt, mflow=m); tot = 0.0
        for i0 in range(0, len(x), 8):
            sl = slice(i0, i0 + 8)
            a, b, c = flow3(Fm, h, X, Y, Z[:, :, sl], t, nrk)
            M = m + Fm.W(a) + Fm.W(b) + Fm.W(c)
            tot += float((WW[:, :, sl]*np.sqrt(Fm.s(a)**2 + Fm.s(b)**2 + Fm.s(c)**2 + M*M)).sum())
        return -2*tot
    def mu(m, dt=0.01):
        e0 = evac(0.0, m); h1 = (evac(dt, m) - 2*e0 + evac(-dt, m))/dt**2; h2 = (evac(2*dt, m) - 2*e0 + evac(-2*dt, m))/(4*dt*dt)
        return (4*h1 - h2)/3
    vals = {m: mu(m) for m in (0.0, 0.005, 0.01, 0.015)}
    print('%s: mu_E per Dirac field: m=0 %+.7e, 0.005 %+.7e, 0.01 %+.7e, 0.015 %+.7e' % ((lab,) + tuple(vals[m] for m in (0.0, 0.005, 0.01, 0.015))), flush=True)
    print('   d mu_E/dm at 0.01 (central) %+.5e ; [mu(0.005)-mu(0)]/0.005 %+.5e   (R19-11 0+ root fit c1 +1.06932e-2, c2 +6.6e-3)  [%.0f s]'
          % ((vals[0.015] - vals[0.005])/0.01, (vals[0.005] - vals[0.0])/0.005, time.time() - t00), flush=True)
