"""T58 follow-up (added after the first run; NOT pre-registered as a pass/fail test, reported as exploratory):
 (a) max over the imported coupling g_weak of eta/eta_obs on the one-flavour chain;
 (b) sign of sin(dCP) on gamma=+1/2 restricted to the NuFit-5.3 3-sigma angle box (data-compatible basin).
"""
import math, sys
import numpy as np
sys.dont_write_bytecode = True
exec(open('t58_chain_test.py').read().split('res = {}')[0])   # reuse the chain definitions only
from scipy import optimize
# (a)
gs = np.exp(np.linspace(math.log(0.02), math.log(30), 60))
vals = [chain({"g_weak": g})["eta"] for g in gs]
i = int(np.argmax(vals))
r = optimize.minimize_scalar(lambda lg: -chain({"g_weak": math.exp(lg)})["eta"], bracket=(math.log(gs[max(i-1,0)]), math.log(gs[i]), math.log(gs[min(i+1,len(gs)-1)])))
gbest = math.exp(r.x); print(f"(a) max_g eta/eta_obs = {-r.fun:.4f} at g_weak = {gbest:.4f} (base 0.653; K there = {chain({'g_weak':gbest})['K']:.3f})")
# (b)
GAMMA=0.5; E1=math.sqrt(8/3); E2=math.sqrt(8)/3
T_M=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=complex); T_D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]],dtype=complex); T_Q=np.array([[0,1,1],[1,0,1],[1,1,0]],dtype=complex)
HB=np.array([[0,E1,-E1-1j*GAMMA],[E1,0,-E2],[-E1+1j*GAMMA,-E2,0]],dtype=complex); PERM=(2,1,0)
B3={'s12':(0.275,0.345),'s13':(0.02029,0.02391),'s23':(0.430,0.596)}
rng=np.random.default_rng(7); lo=np.array([-1.5,0.0,0.0]); hi=np.array([3.5,2.6,3.0])
inb=[]; ch=0
for _ in range(400000):
    m,d,q=lo+(hi-lo)*rng.random(3)
    if q+d-math.sqrt(8/3)<0: continue
    ch+=1
    Hh=HB+m*T_M+d*T_D+q*T_Q
    w,V=np.linalg.eigh(Hh); o=np.argsort(w.real); V=V[:,o]; P=V[list(PERM),:]
    s13=abs(P[0,2])**2; c13=1-s13; s12=abs(P[0,1])**2/c13; s23=abs(P[1,2])**2/c13
    if not (B3['s12'][0]<=s12<=B3['s12'][1] and B3['s13'][0]<=s13<=B3['s13'][1] and B3['s23'][0]<=s23<=B3['s23'][1]): continue
    J=(P[0,0]*np.conj(P[0,1])*np.conj(P[1,0])*P[1,1]).imag
    den=math.sqrt(s12*(1-s12)*s23*(1-s23)*s13*c13*c13)
    inb.append((J/den,s23))
inb=np.array(inb); print(f"(b) chamber samples {ch}; inside NuFit-5.3 3sigma box: {len(inb)}")
if len(inb):
    print(f"    sin(dCP)<0: {np.sum(inb[:,0]<0)}, >0: {np.sum(inb[:,0]>0)}; s23^2>0.5 with sin<0: {np.sum((inb[:,0]<0)&(inb[:,1]>0.5))}, s23^2<0.5 with sin>0: {np.sum((inb[:,0]>0)&(inb[:,1]<0.5))}")
    print(f"    sin(dCP) range in box: [{inb[:,0].min():+.3f}, {inb[:,0].max():+.3f}]")
