"""A1: exact re-verification of certificates. A2: feasibility boundaries of the two counting recursions."""
from fractions import Fraction as Fr
import math

def d123(p,q,r):
    p,q,r=map(Fr,(p,q,r))
    d1=1-p**3/(p**3+q**3+4*r**3)
    d2=1-p*p*q/(p*q*(p+q)+4*r**3)
    d3=1-p*p/(p*p+q*q+r*(p+q)+2*r*r)
    return d1,d2,d3

def eps(p,q,r):
    d1,d2,d3=d123(p,q,r)
    return d1,max(d2,d3)

# ---------- A1: block 30 T4 certificates (exact) ----------
rows=[((4165,1,2),Fr(99,1000),Fr(56694252249173,500000000000),Fr(3279872914431,10**12),Fr(168429466648591,10**12)),
      ((2085,1,1),Fr(49,500),Fr(88632394933177,10**12),Fr(3254100818939,10**12),Fr(131311435970231,10**12)),
      ((8330,2,4),Fr(99,1000),Fr(56694252249173,500000000000),Fr(3279872914431,10**12),Fr(168429466648591,10**12)),
      ((6247,1,3),Fr(99,1000),Fr(24445325573453,250000000000),Fr(3264868815393,10**12),Fr(9064364177089,62500000000))]
print("A1 block-30 T4 rational certificates")
for (pqr,t,D,U,F) in rows:
    e1,e2=eps(*pqr)
    x=t+e2/t**2; y=e1/t**3
    rD=(1+x*U)**2*(1+3*x*D)*(1+y*F)**6
    rU=(1+x*U)**3*(1+y*F)**6
    rF=(1+x*U)**3*(1+3*x*D)*(1+y*F)**5
    Rb=(1+x*U)**3*(1+3*x*D)*(1+y*F)**6
    ok = (rD<=D and rU<=U and rF<=F and D>=1 and U>=1 and F>=1 and e1*Rb<Fr(1,10**7))
    print(pqr,"t",t,"dominates:",rD<=D,rU<=U,rF<=F,"e1*Rbar=%.4e"%float(e1*Rb),"ok",ok)

# (84,1,2) refinement-history certificate
sig=Fr(161,5000); Zb=Fr(5119922891,10**9)
def H1_ok(pqr,sig,Zb):
    e1,e2=eps(*pqr)
    c=6*e1/sig; mu=sig*(2+e2/sig)**3
    return (c*Zb<1) and (Zb>=1+mu*Zb/(1-c*Zb)**3), float(e1*Zb), float(mu), float(c*Zb)
print("A1 refinement-history certificate (H2 table rows)")
for pqr,sg,Z in [((84,1,2),Fr(161,5000),Fr(5119922891,10**9)),((44,1,1),Fr(313,10000),Fr(230312929,5*10**7)),
                 ((168,2,4),Fr(161,5000),Fr(5119922891,10**9)),((125,1,3),Fr(13,400),Fr(655476451,125*10**6))]:
    print(pqr,H1_ok(pqr,sg,Z))
print("(83,1,2) with the same (sigma,Zbar):",H1_ok((83,1,2),sig,Zb))

# ---------- A2: feasibility boundaries (float) ----------
def H1_feasible(p,q=1.0,r=2.0):
    e1,e2=[float(v) for v in eps(Fr(p).limit_denominator(10**9),q,r)]
    best=None
    # scan sigma in (0,1]
    for k in range(1,4000):
        sg=1.0*math.exp(-k*0.004)           # sigma from 1 down
        c=6*e1/sg; mu=sg*(2+e2/sg)**3
        if mu>=1: continue
        # min over Z of f(Z)-Z on [1,1/c)
        lo,hi=1.0,(1/c)*(1-1e-12)
        # f convex increasing; minimise g(Z)=1+mu Z/(1-cZ)^3 - Z by ternary search
        a,b=lo,hi
        g=lambda Z:1+mu*Z/(1-c*Z)**3-Z
        for _ in range(200):
            m1=a+(b-a)/3; m2=b-(b-a)/3
            if g(m1)<g(m2): b=m2
            else: a=m1
        Z=(a+b)/2
        if Z<lo: Z=lo
        if g(Z)<=0:
            return True,sg,Z
    return False,None,None

def bisect(feas,lo,hi,tol=1e-3):
    assert not feas(lo) and feas(hi)
    while hi-lo>tol:
        m=(lo+hi)/2
        if feas(m): hi=m
        else: lo=m
    return hi

pH1=bisect(lambda p:H1_feasible(p)[0],20.0,200.0)
print("A2 refinement-history recursion H1 feasible from p = %.3f on (p,1,2); at p=84: %s"%(pH1,H1_feasible(84.0)))
print("   ceiling mu>=27*eps2 => eps2<1/27: p >=", bisect(lambda p: float(eps(Fr(p).limit_denominator(10**9),1,2)[1])<1/27,20.,100.))

def tree_feasible(p,q=1.0,r=2.0,cbud=2):
    """block 30 recursion; scan t; iterate from (1,1,1) and test boundedness."""
    e1,e2=[float(v) for v in eps(Fr(p).limit_denominator(10**9),q,r)]
    for k in range(0,600):
        t=math.exp(-k*0.01)
        x=t+e2/t**2; y=e1/t**3
        D=U=F=1.0
        okb=True
        for it in range(4000):
            nD=(1+x*U)**2*(1+3*x*D)*(1+y*F)**6
            nU=(1+x*U)**3*(1+y*F)**6
            nF=(1+x*U)**3*(1+3*x*D)*(1+y*F)**5
            if max(nD,nU,nF)>1e8: okb=False;break
            if abs(nD-D)+abs(nU-U)+abs(nF-F)<1e-13: D,U,F=nD,nU,nF;break
            D,U,F=nD,nU,nF
        else:
            okb=False
        if okb: return True,t,(D,U,F)
    return False,None,None
pT=bisect(lambda p:tree_feasible(p)[0],1000.0,20000.0,tol=0.5)
print("A2 block-30 tree recursion (budget c=2) bounded iteration from p = %.1f on (p,1,2); at 4165: %s"%(pT,tree_feasible(4165.0)[:2]))
