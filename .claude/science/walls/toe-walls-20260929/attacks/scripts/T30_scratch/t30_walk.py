"""T30 walking-bridge check: constant n (real) from M_Pl to v; which n puts alpha(v) at the repo target?  Not a repo result."""
import math
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
def bs(n): return (11-2*n/3, 102-38*n/3, 2857/2-5033*n/18+325*n*n/54)
def alpha_v(n, loops, a0, L=38.44):
    b0,b1,b2=bs(n)
    def f(t,y):
        a=y[0]/(4*math.pi); s=b0*a**2
        if loops>=2: s+=b1*a**3
        if loops>=3: s+=b2*a**4
        return [4*math.pi*(-2*s)]
    ev=lambda t,y: y[0]-3.0; ev.terminal=True
    sol=solve_ivp(f,[0,-L],[a0],events=[ev],rtol=1e-11,atol=1e-14,max_step=0.5)
    return float('inf') if sol.status==1 else sol.y[0][-1]
out=[]
def P(s): print(s); out.append(s)
A_LM=0.09066783601728631; A_B=1/(4*math.pi)
for a0name,a0 in (("alpha_LM",A_LM),("alpha_bare",A_B)):
    for loops in (1,2,3):
        row=" ".join("n=%.1f:%.4f"%(n,alpha_v(n,loops,a0)) for n in (14,14.5,15,15.5,16))
        P("%s %d-loop alpha(v): %s"%(a0name,loops,row))
        for tgt in (0.1033,0.1162):
            try:
                n=brentq(lambda n: alpha_v(n,loops,a0)-tgt, 12.0, 16.0, xtol=1e-6)
                # tolerance: n range for +-10% on target
                n_lo=brentq(lambda n: alpha_v(n,loops,a0)-tgt*1.1, 12.0, 16.0, xtol=1e-6)
                n_hi=brentq(lambda n: alpha_v(n,loops,a0)-tgt*0.9, 12.0, 16.0, xtol=1e-6)
                P("   target %.4f: constant n = %.3f (+-10%% in alpha(v) <-> n in [%.3f, %.3f])"%(tgt,n,n_lo,n_hi))
            except Exception as e:
                P("   target %.4f: no constant n in [12,16] (%s)"%(tgt,e))
# what the staggered doubler count would do: n=4 Dirac tastes (one 4D staggered field) instead of 16
for n in (4,8,16):
    b0,b1,b2=bs(n); P("n_Dirac=%d: b0=%.3f b1=%.2f  -> const-n 2-loop alpha(v) from alpha_LM: %s"%(n,b0,b1,("%.4f"%alpha_v(n,2,A_LM)) if alpha_v(n,2,A_LM)<10 else "pole"))
# SU(2) with 16 copies of SM fermions: one-loop b2 and Landau scale from alpha_2(M_Pl)=alpha_LM-like 0.0907
def su2_b(tastes): return 22/3 - tastes*3*4/3 - 1/6
for tastes in (1,4,16):
    b=su2_b(tastes)
    P("SU(2) with %d taste copies of the SM fermion content: b2=%.2f (AF lost if <0)"%(tastes,b))
open('t30_walk_output.txt','w').write("\n".join(out)+"\n")
