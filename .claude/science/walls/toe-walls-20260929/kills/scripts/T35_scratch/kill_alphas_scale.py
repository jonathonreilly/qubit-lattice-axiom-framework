"""KILL CHECK 1: is 0.1179 an alpha_s at v (246 GeV) or alpha_s(M_Z)?  Run alpha_s(M_Z)=0.1179 up to v (2-loop, nf=5 -> 6 at m_t=172.5)
and, independently, alpha_s(v)=0.1033 down to M_Z."""
import numpy as np
from scipy.integrate import solve_ivp
PI=np.pi
def beta(a,nf):
    b0=11-2*nf/3; b1=102-38*nf/3
    # d a/d ln mu = -2 a^2/(4pi) [b0 + b1 a/(4pi)]   (a = alpha_s)
    return -2*a**2/(4*PI)*(b0+b1*a/(4*PI))
def run(a0,mu0,mu1,mt=172.5):
    a=a0; mu=mu0
    segs=[]
    if mu1>mu0:
        pts=[(mu0,min(mu1,mt),5)] if mu0<mt else []
        if mu1>mt: pts.append((max(mu0,mt),mu1,6))
    else:
        pts=[]
        if mu0>mt: pts.append((mu0,max(mu1,mt),6))
        if mu1<mt: pts.append((min(mu0,mt),mu1,5))
    for lo,hi,nf in pts:
        s=solve_ivp(lambda t,y:[beta(y[0],nf)],[np.log(lo),np.log(hi)],[a],rtol=1e-10,atol=1e-12)
        a=s.y[0,-1]
    return a
MZ=91.1876; V=246.28
print("alpha_s(M_Z)=0.1179 run up to v : alpha_s(v) = %.4f"%run(0.1179,MZ,V))
print("alpha_s(v)=0.1033 run down to M_Z: alpha_s(M_Z) = %.4f"%run(0.1033,V,MZ))
print("alpha_s(v)=0.1179 run down to M_Z: alpha_s(M_Z) = %.4f  (what the 'observed' corner would imply)"%run(0.1179,V,MZ))
print("alpha_s(v)=0.0907 run down to M_Z: alpha_s(M_Z) = %.4f"%run(0.0907,V,MZ))
