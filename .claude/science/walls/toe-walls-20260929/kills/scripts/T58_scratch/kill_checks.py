"""Kill-round checks on T58. Reuses the attacker's chain definitions (read-only exec of the top of t58_chain_test.py)."""
import math, sys
sys.dont_write_bytecode = True
exec(open('t58_chain_test.py').read().split('res = {}')[0])
from scipy import optimize

b = chain({})
print("base eta", b["eta"], "K", b["K"], "kappa", b["kappa"], "m3_eV", b["m3_light_eV"])

# K1: elasticity of eta wrt g_weak at FIXED light mass m3 = Y0^2 v^2/M1 (Mscale ~ g^4), the lane's T50 tie
def elast_fixed_m3(rel=0.01):
    def f(g):
        return chain({"g_weak": g, "Mscale": (g/0.653)**4})["eta"]
    up, dn = f(0.653*(1+rel)), f(0.653*(1-rel))
    return (math.log(up)-math.log(dn))/(math.log(1+rel)-math.log(1-rel))
print("K1 dln eta/dln g_weak at fixed m3 (Mscale ~ g^4):", elast_fixed_m3())
print("   m3 check at g=0.8, Mscale=(0.8/.653)^4:", chain({"g_weak":0.8,"Mscale":(0.8/0.653)**4})["m3_light_eV"])

# K2: Davidson-Ibarra ratio of the chain's eps (repo helper definition)
Y0 = 0.653**2/64
eps = abs(b["eps"]); m1=b["M1"]; m3g = Y0**2*V_EW**2/m1
epsDI = 3/(16*PI)*m1*m3g/V_EW**2
print("K2 |eps1|/eps_DI =", eps/epsDI, " eps1 =", eps, " eps_DI =", epsDI)
print("   raising gamma x5.30 gives eps/eps_DI =", 5.297*eps/epsDI)

# K3: dimension of tuning: does anything within the supplied one-flavour chain, with sheet bit fixed, give eta>=1?
# vary each of E1,E2,gamma within the lane's own (unbounded) formulas: no upper bound known; report factor needed only.
print("K3 eta with sign bit right but nothing else changed:", b["eta"])

# K4: chamber fraction dependence on sampling box (is 83% a property of an arbitrary box?)
import numpy as np
GAMMA=0.5; E1=math.sqrt(8/3); E2=math.sqrt(8)/3
T_M=np.array([[1,0,0],[0,0,1],[0,1,0]],dtype=complex); T_D=np.array([[0,-1,1],[-1,1,0],[1,0,-1]],dtype=complex); T_Q=np.array([[0,1,1],[1,0,1],[1,1,0]],dtype=complex)
HB=np.array([[0,E1,-E1-1j*GAMMA],[E1,0,-E2],[-E1+1j*GAMMA,-E2,0]],dtype=complex); PERM=(2,1,0)
def sind(m,d,q):
    H=HB+m*T_M+d*T_D+q*T_Q
    w,V=np.linalg.eigh(H); o=np.argsort(w.real); V=V[:,o]; P=V[list(PERM),:]
    s13=abs(P[0,2])**2; c13=1-s13; s12=abs(P[0,1])**2/c13; s23=abs(P[1,2])**2/c13
    J=(P[0,0]*np.conj(P[0,1])*np.conj(P[1,0])*P[1,1]).imag
    den=math.sqrt(max(s12*(1-s12)*s23*(1-s23)*s13*c13*c13,1e-300))
    return J/den
rng=np.random.default_rng(3)
for name,lo,hi in [("attack box",[-1.5,0,0],[3.5,2.6,3.0]),("half box",[-0.75,0,0],[1.75,1.3,1.5]),("big box",[-3,0,0],[6,5,6]),("m>0 box",[0,0,0],[3.5,2.6,3.0])]:
    lo=np.array(lo);hi=np.array(hi);n=neg=0
    for _ in range(20000):
        m,d,q=lo+(hi-lo)*rng.random(3)
        if q+d-math.sqrt(8/3)<0: continue
        n+=1; neg+= sind(m,d,q)<0
    print(f"K4 {name}: sin(dCP)<0 fraction at gamma=+1/2 = {neg/n:.3f} (n={n})")
