"""T30 block D refinement + SM matching.  Not a repo result.
D: for fixed content n (real) and start alpha_UV, ln(M_Pl/Lambda) where alpha reaches marker alpha_c.
   Find n_c (edge of the conformal window in this perturbative model) and the n-width giving Lambda in [1e-21,1e-19] M_Pl.
S: where does the Standard-Model MSbar coupling (2-loop, n_f=5 below m_t, 6 above) equal the framework's lattice couplings?
"""
import math, sys
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
sys.path.insert(0, '.')
def bs(n): return (11-2*n/3, 102-38*n/3, 2857/2-5033*n/18+325*n*n/54)
def efolds(n, loops, a0, amark, tmax=600.0):
    b0,b1,b2 = bs(n)
    def f(t,y):
        a=y[0]/(4*math.pi); s=b0*a**2
        if loops>=2: s+=b1*a**3
        if loops>=3: s+=b2*a**4
        return [4*math.pi*(-2*s)]
    ev=lambda t,y: y[0]-amark
    ev.terminal=True; ev.direction=1
    sol=solve_ivp(f,[0,-tmax],[a0],events=[ev],rtol=1e-11,atol=1e-14,max_step=0.5)
    if sol.status==1: return -sol.t_events[0][0]
    return float('inf')
out=[]
def P(s):
    print(s); out.append(s)
A_LM=0.09066783601728631; A_B=1/(4*math.pi)
for a0name,a0 in (("alpha_LM",A_LM),("alpha_bare",A_B)):
  for amark in (1.0, 0.785):
    for loops in (2,3):
        lo,hi=6.0,16.0
        for _ in range(60):
            mid=0.5*(lo+hi)
            if efolds(mid,loops,a0,amark)<1e8: lo=mid
            else: hi=mid
        nc=lo
        # n giving 43.7 and 48.4 efolds
        def nfor(E):
            return brentq(lambda n: min(efolds(n,loops,a0,amark),1e4)-E, nc-1.0 if nc>7 else 6.0, nc-1e-12, xtol=1e-14)
        try:
            n1=nfor(43.7); n2=nfor(48.4); nm=nfor(46.0)
            P("start %-10s marker %.3f %d-loop: n_c=%.6f ; Lambda in [1e-21,1e-19]M_Pl for n in [%.6f, %.6f] i.e. n_c-n in [%.2e, %.2e], width %.2e ; e-folds at n_c-0.01: %.1f, n_c-0.1: %.1f" %
              (a0name,amark,loops,nc,n2,n1,nc-n1,nc-n2,n1-n2,efolds(nc-0.01,loops,a0,amark),efolds(nc-0.1,loops,a0,amark)))
        except Exception as e:
            P("start %s marker %.3f %d-loop: n_c=%.6f ; window solve failed %s" % (a0name,amark,loops,nc,e))

# ---- S. SM matching
P("\n== S. Standard-Model MSbar alpha_s(mu), 2-loop, nf=5 (M_Z..m_t) and nf=6 (above), alpha_s(M_Z)=0.1180")
MZ=91.1876; MT=172.5
def run(a0, mu0, mu1, n, loops=2):
    b0,b1,b2=bs(n)
    def f(t,y):
        a=y[0]/(4*math.pi); s=b0*a**2+b1*a**3+(b2*a**4 if loops>=3 else 0)
        return [4*math.pi*(-2*s)]
    sol=solve_ivp(f,[math.log(mu0),math.log(mu1)],[a0],rtol=1e-11,atol=1e-14)
    return sol.y[0][-1]
def alpha_sm(mu, loops=2):
    if mu<=MT: return run(0.1180, MZ, mu, 5, loops)
    a=run(0.1180, MZ, MT, 5, loops)
    return run(a, MT, mu, 6, loops)
for mu in (91.19, 246.28, 500, 1000, 2000, 5000, 1e4, 1e6, 1.2209e19):
    P("mu=%10.3e GeV  alpha_s=%.4f" % (mu, alpha_sm(mu)))
for name,val in (("alpha_s(v)_repo=alpha_bare/u0^2",0.10330381612226712),("alpha_LM",A_LM),("alpha_bare",A_B)):
    mu=math.exp(brentq(lambda t: alpha_sm(math.exp(t))-val, math.log(150), math.log(1e9)))
    P("SM coupling equals %s = %.4f at mu = %.3g GeV" % (name,val,mu))
P("SM at M_Pl: alpha_s(M_Pl)=%.4f => beta_lat = 6/g^2 = %.1f (lattice beta=6 would need alpha=%.4f)" % (alpha_sm(1.2209e19), 6/(4*math.pi*alpha_sm(1.2209e19)), 6/(4*math.pi*6)))
# 3-loop fixed point for n=16 and required precision on alpha_UV in transmutation
def fp(n,loops):
    b0,b1,b2=bs(n)
    g=lambda a: b0+b1*a+(b2*a*a if loops>=3 else 0)
    return brentq(g,1e-6,0.3)*0+ (brentq(g,1e-6,0.05) if loops>=3 else -b0/b1)*4*math.pi
P("n=16 fixed point alpha*: 2-loop %.4f ; 3-loop %.4f" % (fp(16,2), fp(16,3)))
open('t30_window_output.txt','w').write("\n".join(out)+"\n")
