"""S3: flavour-blind dressing families shared between the two quark sectors (power tilt; additive shift)."""
from common import *
from scipy.optimize import brentq
g = load_runner(); PARS, _RG = g["PARS"], g["_RG"]
R = _RG(PARS['aS'], PARS['mc'], PARS['mb'], PARS['mt'])
# quark masses at 2 GeV (MSbar): light as quoted; c,b,t run to 2 GeV (formal extrapolation for t)
up2 = np.array([PARS['mu'], PARS['mc']*R.factor(PARS['mc'],2.0), PARS['mt']*R.factor(PARS['mt'],2.0)])
dn2 = np.array([PARS['md'], PARS['ms'], PARS['mb']*R.factor(PARS['mb'],2.0)])
print("masses at 2 GeV [GeV]  up:", up2, " down:", dn2)
print("r at 2 GeV: up %.5f down %.5f  (should equal common-scale values)" % (rf(up2), rf(dn2)))
lep = M_LEP_POLE/1000
def tilt(m, eta): return np.asarray(m)**(1+eta)
def solve_all(fun, m, lo, hi, n=4000):
    xs = np.linspace(lo, hi, n); vals = np.array([fun(m, x)-0.5 for x in xs]); roots=[]
    for i in range(n-1):
        if vals[i]*vals[i+1] < 0: roots.append(brentq(lambda x: fun(m,x)-0.5, xs[i], xs[i+1]))
    return roots
rt = lambda m, e: rf(tilt(m, e))
print("\n(a) power tilt m -> m^(1+eta): roots of r=1/2")
for name, m in (("down", dn2), ("up", up2)):
    print("  %s: eta roots:" % name, ["%.4f" % x for x in solve_all(rt, m, -0.95, 3.0)])
print("  leptons: r(eta) at eta=0: %.6f ; d r/d eta = %.4f" % (rf(lep), (rt(lep,1e-4)-rt(lep,-1e-4))/2e-4))
print("  => lepton tolerance |eta| < %.1e for |r-1/2| < 1e-5" % (1e-5/abs((rt(lep,1e-4)-rt(lep,-1e-4))/2e-4)))
ra = lambda m, D: rf(np.asarray(m)+D)
print("\n(b) additive shift m -> m + Delta [GeV, at 2 GeV]: roots of r=1/2")
for name, m in (("down", dn2), ("up", up2)):
    print("  %s: Delta roots [GeV]:" % name, ["%.4g" % x for x in solve_all(ra, m, 1e-6, 500.0, 200000)][:4])
d_roots = solve_all(ra, dn2, 1e-6, 500.0, 200000); u_roots = solve_all(ra, up2, 1e-6, 500.0, 200000)
# ratio to the second-generation mass (the natural comparison unit for a constituent-like offset)
if d_roots and u_roots:
    print("  Delta_d/m_s = %.3g ; Delta_u/m_c = %.3g ; Delta_u/Delta_d = %.3g" % (d_roots[0]/dn2[1], u_roots[0]/up2[1], u_roots[0]/d_roots[0]))
print("  reference: constituent-mass scale from chiral symmetry breaking ~0.3 GeV; QCD dressing exponent 2 alpha_s/pi ~ 0.08-0.2 for alpha_s 0.12-0.3")
