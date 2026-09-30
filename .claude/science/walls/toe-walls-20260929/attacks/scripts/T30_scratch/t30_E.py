"""Block E only (fast).  Frozen rung ratio alpha_LM vs running: rung k ratio = running alpha(mu_k)."""
import math
from scipy.integrate import solve_ivp
def bs(n): return (11-2*n/3, 102-38*n/3, 2857/2-5033*n/18+325*n*n/54)
def seg(a, t0, t1, n, loops, amax=1.0):
    b0,b1,b2=bs(n)
    def f(t,y):
        x=y[0]/(4*math.pi); s=b0*x**2
        if loops>=2: s+=b1*x**3
        if loops>=3: s+=b2*x**4
        return [4*math.pi*(-2*s)]
    ev=lambda t,y: y[0]-amax; ev.terminal=True; ev.direction=1
    sol=solve_ivp(f,[t0,t1],[a],events=[ev],rtol=1e-10,atol=1e-14,max_step=0.1)
    if sol.status==1: return amax, sol.t_events[0][0], True
    return sol.y[0][-1], t1, False
A_LM=0.09066783601728631
out=[]
def P(s): print(s); out.append(s)
P("E. rung k has ratio = running alpha(mu_k); 16 rungs; frozen value: span %.2f, v/M_Pl(no 7/8 factor) = %.2e" % (16*math.log(A_LM), A_LM**16))
for name,content in (("repo staircase n=16-k",lambda k:16-k),("constant n=16",lambda k:16),("constant n=15",lambda k:15)):
    for loops in (1,2,3):
        t=0.0; a=A_LM; al=[a]; msg="done"
        for k in range(16):
            if a>=1: msg="alpha>=1 at rung %d"%k; break
            dt=math.log(a)
            a2,t2,hit=seg(a,t,t+dt,content(k),loops)
            if hit: msg="pole inside rung %d at t=%.2f"%(k,t2); t=t2; break
            t+=dt; a=a2; al.append(a)
        P("%-22s %d-loop: %s; span t=%.2f -> ratio to frozen v/M_Pl = %.2e ; alpha_k every 3rd rung: %s" % (name,loops,msg,t,math.exp(t)/A_LM**16," ".join("%.3f"%x for x in al[::3])))
open('t30_E_output.txt','w').write("\n".join(out)+"\n")
