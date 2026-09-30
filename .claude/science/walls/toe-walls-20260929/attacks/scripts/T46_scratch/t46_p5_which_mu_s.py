"""T46 P5: at which light-quark scale mu_s does each candidate exponent 'match' the mixed ratio m_s(mu_s)/m_b(m_b)?"""
import numpy as np
from scipy.optimize import brentq
from qcdrun import QCD
q = QCD(); V = 0.103303816122/np.sqrt(6)
f = lambda mus, p: q.mass(0.0934, 2.0, mus)/4.18 - V**(1/p)
print("exponent   mu_s[GeV] at which m_s(mu_s)/m_b(m_b) = V^(1/p)   (pure conventional-scale reading)")
for name, p in (("3/4",3/4),("4/5",4/5),("5/6",5/6),("6/7",6/7),("7/8",7/8),("8/9",8/9)):
    try:
        mus = brentq(f, 0.6, 12.0, args=(p,))
        print(f"  {name:4s} p={p:.4f}   mu_s = {mus:6.3f} GeV")
    except Exception as e:
        print(f"  {name:4s} no root in [0.6,12] ({e})")
# GST-side and m_d/m_b on the RG surface
md_ms = 4.67/93.4
Rc = q.mass(0.0934,2.0,4.18)/4.18
print("\nm_d/m_s (both at 2 GeV, scale-blind): data %.5f  atlas alpha_s/2 = %.5f  (%+.1f%%)"%(md_ms, 0.103303816122/2, 100*(0.103303816122/2/md_ms-1)))
pred_db = (0.103303816122/2)*V**1.2
print("m_d/m_b: bridge prediction %.6f ; mixed-scale comparator 4.67/4180 = %.6f (%+.1f%%) ; RG-common comparator (m_d/m_s)*R_common = %.6f (%+.1f%%)"%(
    pred_db, 4.67/4180, 100*(pred_db/(4.67/4180)-1), md_ms*Rc, 100*(pred_db/(md_ms*Rc)-1)))
