# Referee independent check (own closed-form 2-loop; no ODE; no rgcommon import)
import math
from scipy.optimize import brentq
MPL=1.2209e19; V=246.22; LN10=math.log(10)
def b(nf): return 11-2*nf/3, 102-38*nf/3
def L2(mu2_over_lam2_log=None, a=None, nf=0):
    b0,b1=b(nf)
    return 1/(b0*a)+(b1/b0**2)*math.log(b0*a/(1+b1*a/b0))   # ln(mu^2/Lam^2)
def a_at(lnmu2lam2, nf):
    f=lambda x: L2(a=x,nf=nf)-lnmu2lam2
    return brentq(f,1e-6,0.05,xtol=1e-16)
def lam_over_mcut(g2, nf_top, nf_low=None, kappa=1.0):
    a=g2/(16*math.pi**2)
    if nf_low is None or kappa==1.0:
        return math.exp(-0.5*L2(a=a,nf=nf_top))
    # run nf_top from Mcut down to kappa*Mcut (Lambda invariant), identity match
    lnl= L2(a=a,nf=nf_top)          # ln(Mcut^2/L^2)
    ak = a_at(lnl+2*math.log(kappa), nf_top)
    return kappa*math.exp(-0.5*L2(a=ak,nf=nf_low))
def edge(target, bcell, nf_top, nf_low=None, kappa=1.0):
    t = target*bcell   # Lambda/Mcut
    return brentq(lambda g2: lam_over_mcut(g2,nf_top,nf_low,kappa)-t, 0.05, 0.9, xtol=1e-12)
T=V/MPL
print("T_v =",T)
for name,args in [("A pure",(0,)),("B nf6",(6,)),("C k=0.1",(12,6,0.1)),("C k=0.3",(12,6,0.3))]:
    for bc in (1,35):
        e=[edge(x,bc,*args) for x in (2e-16,T,2e-18)]
        print(f"{name:8s} b={bc:2d} g2 edges {e[0]:.4f} centre {e[1]:.4f} {e[2]:.4f}")
# pure-gauge Wilson bare 2-loop: Lambda_L = Lambda_MS/28.809
for lab,r in (("MSbar",1.0),("Wilson",28.809),("HK",28.809/1.819)):
    e=[brentq(lambda g2: lam_over_mcut(g2,0)-x/r,0.05,0.9) for x in (2e-16,2e-18)]
    print(lab,"pure g2",[round(z,4) for z in e],"beta",[round(6/z,1) for z in e])
# C1 best case one loop X2' k=0.1 (nf=12 above, 6 below)
a=1/(16*math.pi**2); inv=1/a-3*2*math.log(10)
dec=1+ (inv/7)/2/LN10
print("C1 one-loop X2' k=0.1 decades",dec, " short of 15.70:",15.70-dec)
# 2-loop version of C1
print("C1 two-loop X2' k=0.1 decades",-math.log10(lam_over_mcut(1.0,12,6,0.1)), " nf6 2loop", -math.log10(lam_over_mcut(1.0,6)), " pure 2loop", -math.log10(lam_over_mcut(1.0,0)))
# non-perturbative: Sommer
for r0a in (5.0057,5.368):
    Lam=0.602/r0a
    print(f"r0/a={r0a}: Lambda_MS a={Lam:.4f} ({-math.log10(Lam):.2f} dec); sqrt(sigma)a={math.sqrt(1.65-math.pi/12)/r0a:.4f}; alpha_MS(1/a) 2loop={16*math.pi**2*a_at(2*math.log(1/Lam),0)/(4*math.pi):.4f}")
# R4(i) one loop Wilson-bare -> MSbar at 1/a
inv_alpha= 4*math.pi - (11/(2*math.pi))*math.log(28.809)
print("alpha_MS(1/a) one-loop from g0^2=1:",1/inv_alpha)
# C5
for nf in (0,6):
    b0=b(nf)[0]; print("nf",nf,"g2 at b=5,35:",[round(1/(1-b0*math.log(x)/(8*math.pi**2)),3) for x in (5,35)],
     "ln ratio to reach 0.3606:", (1/0.3606-1)*8*math.pi**2/b0)
# observed alpha_s(M_Pl) = 1/52.98
print("obs alpha(MPl)=",1/52.98)
