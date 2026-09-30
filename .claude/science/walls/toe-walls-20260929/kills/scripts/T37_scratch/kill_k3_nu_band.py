"""K3: robustness of the S5 neutrino kill. (i) attack's IO mass assignment has the wrong splitting (heaviest m^2 = m3^2+d32+d21 instead of m3^2+d32);
(ii) alternative dictionaries: seesaw with degenerate M_R (Dirac mass ~ sqrt(m_nu)); (iii) how interpolating charge laws behave at Q=0."""
from common import *
d21, d31_no, d32_io = 7.42e-5, 2.515e-3, 2.498e-3
m0 = np.concatenate([[0.0], np.logspace(-6, np.log10(0.3), 4000)])
def NO(m1): return np.sqrt(np.array([m1**2, m1**2+d21, m1**2+d31_no]))
def IO_attack(m3): return np.sqrt(np.array([m3**2, m3**2+d32_io, m3**2+d32_io+d21]))
def IO_fixed(m3): return np.sqrt(np.array([m3**2, m3**2+d32_io-d21, m3**2+d32_io]))   # m3 < m1 < m2
for name,f in (("NO",NO),("IO attack",IO_attack),("IO corrected",IO_fixed)):
    vals=np.array([rf(f(x)) for x in m0]); print("%-13s direct sqrt(m) dictionary: r in [%.4f, %.4f]" % (name, vals.min(), vals.max()))
    vals=np.array([rf(np.sqrt(f(x))) for x in m0]); print("%-13s seesaw (M_R degenerate, m_D ~ sqrt(m_nu)): r in [%.4f, %.4f]" % (name, vals.min(), vals.max()))
    vals=np.array([rf(f(x)**2) for x in m0]); print("%-13s inverse (m_D ~ m_nu^2) [control]: r in [%.4f, %.4f]" % (name, vals.min(), vals.max()))
print("\nany interpolating charge law: r(e,Q=-1)=0.5, r(d,-1/3)=0.621, r(nu,0)=?, r(u,2/3)=0.831")
print("  linear interpolation between d and u at Q=0: %.3f ; convex/concave quadratic through (e,d,u): " % (0.621+(0.831-0.621)*(1/3)/1.0), end="")
Q=np.array([-1,-1/3,2/3]); y=np.array([0.5,0.62109,0.83097]); c=np.polyfit(Q,y,2); print("%.3f" % np.polyval(c,0.0))
print("  band max (direct dictionary) 0.3785 -> the kill applies to any charge law monotone-or-quadratic through the three charged sectors;")
print("  a law reaching <=0.38 at Q=0 must dip by >0.24 below the value at Q=-1/3 and rise by >0.45 by Q=2/3 (non-smooth); no test for a 4-parameter law.")
