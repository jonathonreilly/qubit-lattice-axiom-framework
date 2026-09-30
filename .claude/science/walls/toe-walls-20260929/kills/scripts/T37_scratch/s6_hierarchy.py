"""S6: the dial r is the top-two hierarchy in Koide coordinates."""
from common import *
from scipy.optimize import brentq
g = load_runner(); PARS, _RG = g["PARS"], g["_RG"]
R = _RG(PARS['aS'], PARS['mc'], PARS['mb'], PARS['mt'])
dn = np.array([PARS['md']*R.factor(2.0,162.5), PARS['ms']*R.factor(2.0,162.5), PARS['mb']*R.factor(PARS['mb'],162.5)])
up = np.array([PARS['mu']*R.factor(2.0,162.5), PARS['mc']*R.factor(PARS['mc'],162.5), PARS['mt']*R.factor(PARS['mt'],162.5)])
lep = M_LEP_POLE
def r2(m2, m3):   # two-generation truncation x1 -> 0
    return rf(np.array([0.0, m2, m3])) if False else (3*((m2+m3)/(np.sqrt(m2)+np.sqrt(m3))**2)-1)/2
print("sector   r_full   r_trunc(x1=0)   |diff|   m3/m2    m2/m1")
rows = {}
for name, m in (("lepton", lep), ("down", dn), ("up", up)):
    rows[name] = (rf(m), r2(m[1], m[2]), m[2]/m[1], m[1]/m[0])
    print("%-7s %8.4f %10.4f %13.4f %9.2f %9.1f" % (name, rows[name][0], rows[name][1], abs(rows[name][0]-rows[name][1]), rows[name][2], rows[name][3]))
print("\nx1 = 0 inversion: m3/m2 needed for a given r:")
for r in (0.5, 0.6211, 0.8310):
    rho = brentq(lambda p: (3*(1+p*p)/(1+p)**2 - 1)/2 - r, 1.0001, 1e4)
    print("  r=%.4f  -> m3/m2 = %.2f (x3/x2 = %.3f)" % (r, rho*rho, rho))
print("\nsensitivity: r vs log10(m3/m2) at x1=0 (monotone):")
for l in (0.5, 1.0, 1.2, 1.5, 1.7, 2.0, 2.5, 3.0):
    print("  m3/m2=10^%.1f: r=%.4f" % (l, r2(1.0, 10**l)))
# Jacobian: what fraction of dr is from x1/x3? partial derivatives at each sector
for name, m in (("lepton", lep), ("down", dn), ("up", up)):
    base = rf(m); out=[]
    for i in range(3):
        mm = m.copy(); mm[i]*=1.01; out.append((rf(mm)-base)/0.01)
    print("%-7s dr/dln m_i (per unit ln m): m1 %.4f  m2 %.4f  m3 %.4f" % (name, *out))
