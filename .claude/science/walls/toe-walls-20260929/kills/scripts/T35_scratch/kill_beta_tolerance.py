"""KILL CHECK 6: the attack's 'route-specific spread 0.6%' allows lambda(M_Pl)=+-1e-3 and loop order but treats beta_lambda(M_Pl)=0 as exact.
Multiple-point criticality is an approximate principle (Froggatt-Nielsen quote m_t = 173 +- 5 GeV, ~3%; docs/YT_P1_..._2026-06-16.md sec.4).
Allow beta_lambda(M_Pl) = b (3-loop, lambda=0) and see the y_t(v) shift.  Scale for b: the individual 1-loop terms are 6 yt^4/(16 pi^2) ~ 8.7e-4."""
import numpy as np
from common import *
g0=gauge_at_v(0)
def yv_for_b(b,loop=3):
    f=lambda yt: beta_lam_at_pl(yt,g0,loop=loop,lam_pl=0.0)[0]-b
    return brentq(f,0.8,1.05,xtol=1e-10)
base=yv_for_b(0.0)
print("base y_t(v)=%.5f ; single-term scale 6 yt^4 k =%.2e"%(base, 6*0.3889**4/(16*PI**2)))
for b in (-1e-4,-3e-5,-1e-5,1e-5,3e-5,1e-4):
    z=yv_for_b(b); pole,m,mu=pole_from_yt_v(z,g0)
    print(f"beta_lambda(M_Pl)={b:+.0e} ({abs(b)/8.7e-4*100:.1f}% of one term): y_t(v)={z:.4f} ({(z/base-1)*100:+.2f}%), pole {pole:.1f} GeV")
