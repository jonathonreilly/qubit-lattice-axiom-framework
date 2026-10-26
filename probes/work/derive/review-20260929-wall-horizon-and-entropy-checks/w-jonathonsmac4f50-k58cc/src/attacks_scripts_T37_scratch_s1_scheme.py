"""S1: is the sector spread robust against the mass scheme?"""
from common import *
g = load_runner()
PARS, _RG, _dial_f, _sector_dials = g["PARS"], g["_RG"], g["_dial_f"], g["_sector_dials"]
print("leptons (pole):  Q=%.7f  r=%.7f  delta=%.5f (2/9=%.5f)" % (Qf(M_LEP_POLE), rf(M_LEP_POLE), delta_lep_convention(M_LEP_POLE), 2/9))
(Qu, ru, _), (Qd, rd, _) = _sector_dials(PARS, 162.5)
print("common-scale MSbar (mu=162.5): r_up=%.6f r_down=%.6f" % (ru, rd))
R = _RG(PARS['aS'], PARS['mc'], PARS['mb'], PARS['mt'])
# common-scale masses
up = np.array([PARS['mu']*R.factor(2.0,162.5), PARS['mc']*R.factor(PARS['mc'],162.5), PARS['mt']*R.factor(PARS['mt'],162.5)])
dn = np.array([PARS['md']*R.factor(2.0,162.5), PARS['ms']*R.factor(2.0,162.5), PARS['mb']*R.factor(PARS['mb'],162.5)])
print("common-scale masses [GeV] up:", up, " down:", dn)
print("  delta_up=%.4f delta_down=%.4f (lepton convention);  Q/3: lep %.4f down %.4f up %.4f" % (delta_lep_convention(up), delta_lep_convention(dn), Qf(M_LEP_POLE)/3, Qf(dn)/3, Qf(up)/3))
# mixed as-quoted
mixu = [PARS['mu'], PARS['mc'], PARS['mt']]; mixd = [PARS['md'], PARS['ms'], PARS['mb']]
print("mixed as quoted: r_up=%.4f r_down=%.4f" % (rf(mixu), rf(mixd)))
# one-loop pole factor on heavy entries only
pf = lambda m: 1 + 4*R.a_at(m)/3
print("pole factors c,b,t:", pf(PARS['mc']), pf(PARS['mb']), pf(PARS['mt']))
pu = [PARS['mu'], PARS['mc']*pf(PARS['mc']), PARS['mt']*pf(PARS['mt'])]
pd = [PARS['md'], PARS['ms'], PARS['mb']*pf(PARS['mb'])]
print("one-loop pole on c,b,t only (light = MSbar 2 GeV): r_up=%.4f r_down=%.4f" % (rf(pu), rf(pd)))
# all entries incl. light at alpha_s(2 GeV)~0.30 (formal)
a2 = 0.30/math.pi
pu2 = [PARS['mu']*(1+4*a2/3), pu[1], pu[2]]; pd2 = [PARS['md']*(1+4*a2/3), PARS['ms']*(1+4*a2/3), pd[2]]
print("formal one-loop pole incl. light quarks (alpha_s(2GeV)=0.30): r_up=%.4f r_down=%.4f" % (rf(pu2), rf(pd2)))
# envelope: independent factors in [0.85,1.15] on every entry (common-scale masses)
rng = np.random.default_rng(37)
def env(m0, lo=0.85, hi=1.15, n=200000):
    f = rng.uniform(lo, hi, size=(n,3)); mm = np.asarray(m0)[None,:]*f
    x = np.sqrt(mm); Q = mm.sum(1)/x.sum(1)**2; r = (3*Q-1)/2
    return r.min(), r.max()
# also the exact corner search (8 corners per triple is enough for monotone pieces; add random)
import itertools
def corners(m0, lo=0.85, hi=1.15):
    vals=[rf(np.asarray(m0)*np.array(c)) for c in itertools.product([lo,hi],repeat=3)]
    return min(vals), max(vals)
for name,m0 in (("up",up),("down",dn)):
    print("envelope [0.85,1.15]^3 %s: random (min,max)=%s  corners=%s" % (name, env(m0), corners(m0)))
for name,m0 in (("up",up),("down",dn)):
    print("envelope [0.70,1.30]^3 %s: corners=%s" % (name, corners(m0,0.70,1.30)))
# how large must a non-common factor be to bring r to 1/2?  scale only the heaviest entry by f
from scipy.optimize import brentq
for name,m0 in (("up",up),("down",dn)):
    m0=np.array(m0)
    f = brentq(lambda f: rf(m0*np.array([1,1,f]))-0.5, 0.005, 1.0)
    print("%s: factor on the heaviest mass alone needed for r=1/2: %.4f  (a %.0f%% cut)" % (name, f, 100*(1-f)))
    f2 = brentq(lambda f: rf(m0*np.array([1,f,1]))-0.5, 1.0, 400.0)
    print("%s: factor on the middle mass alone needed for r=1/2: %.3f" % (name, f2))
# lepton MSbar shift (one-loop QED, alpha fixed) = L08-W7
for alpha in (1/137.036, 1/127.9):
    for mu in (91187.6, 162.5e3):
        m = M_LEP_POLE*(1-(alpha/np.pi)*(1+0.75*np.log(mu**2/M_LEP_POLE**2)))
        print("lepton MSbar(mu=%g MeV, alpha=1/%.0f): Q-2/3=%+.3e  r=%.5f (pole r-1/2=%+.2e)" % (mu, 1/alpha, Qf(m)-2/3, rf(m), rf(M_LEP_POLE)-0.5))
