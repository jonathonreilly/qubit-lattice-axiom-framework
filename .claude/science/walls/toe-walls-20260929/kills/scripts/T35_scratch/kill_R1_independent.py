"""KILL CHECK 4: independent 1-loop re-derivation of R1 with a self-written RGE (not the lane runner).
Gauge couplings at v from the lane (kEW=0), 1-loop SM RGEs (nf=6 constant), find y_t(M_Pl) from beta_lambda=0 at lambda=0 (analytic 1-loop),
run y_t down to v, read pole mass with K=1.0619 at mu* (self-consistent).  Compare to the attack's 1-loop entry (y_t(v)=0.9009, y_t(M_Pl)=0.38793)."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
PI=np.pi; k=1/(16*PI**2)
V=246.28281829; MPL=1.221e19
def rhs(t,y):
    g1,g2,g3,yt=y
    return [41/10*g1**3*k,-19/6*g2**3*k,-7*g3**3*k, yt*k*(4.5*yt**2-0.85*g1**2-2.25*g2**2-8*g3**2)]
def up(g,ytv):
    s=solve_ivp(rhs,[np.log(V),np.log(MPL)],[g[0],g[1],g[2],ytv],rtol=1e-11,atol=1e-13); return s.y[:,-1]
def blam(y):  # lambda=0, 1-loop, V = lambda |H|^4 normalisation used by the lane (checked in the attack's test A)
    g1,g2,g3,yt=y; gp2=3/5*g1**2
    return (-6*yt**4+3/8*(2*g2**4+(g2**2+gp2)**2))*k
def crit(g):
    return brentq(lambda z: blam(up(g,z)),0.6,1.2,xtol=1e-12)
g=[0.4644,0.6480,np.sqrt(4*PI*0.1033)]
z=crit(g); y=up(g,z)
print("1-loop critical y_t(v)=%.5f  y_t(M_Pl)=%.5f  g(M_Pl)=%s"%(z,y[3],np.round(y[:3],4)))
# analytic formula check
gp2=3/5*y[0]**2; y4=(2*y[1]**4+(y[1]**2+gp2)**2)/16
print("analytic y_t(M_Pl)=(2g2^4+(g2^2+g'^2)^2)/16)^(1/4)= %.5f"%(y4**0.25))
# pole mass, 1-loop y_t running down from v
def ytdown(mu):
    s=solve_ivp(rhs,[np.log(V),np.log(mu)],[g[0],g[1],g[2],z],rtol=1e-11,atol=1e-13); return s.y[3,-1]
mu=brentq(lambda m: ytdown(m)*V/np.sqrt(2)-m,120,240)
print("mu*=%.1f  m_MSbar=%.2f  pole(K=1.0619)=%.2f"%(mu,mu,1.0619*mu))
# sensitivity of y_t(v) to y_t(M_Pl) near R1 and Ward (the lane's QFP-insensitivity claim: 10% -> <0.5%)
def ytv_from_pl(g,ypl,gpl_from_up=True):
    yv=brentq(lambda zz: up(g,zz)[3]-ypl,0.3,1.3); return yv
for ypl in (0.3889,0.4358,0.4794):
    print("y_t(M_Pl)=%.4f -> y_t(v)=%.4f"%(ypl,ytv_from_pl(g,ypl)))
a=ytv_from_pl(g,0.4358); b=ytv_from_pl(g,0.4358*1.1)
print("10%% shift in y_t(M_Pl) -> %.2f%% shift in y_t(v)  (lane's YT_ZERO_IMPORT_CHAIN_NOTE.md:177 claims <0.5%%; June-16 note says 3.1%%)"%((b/a-1)*100))
