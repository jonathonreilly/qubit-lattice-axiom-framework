# GUIDE only: optimize the basic Kraft system (all states D=1..6) over P, y.
import math
def consts(b):
    s=math.sinh(b)/2; c=math.cosh(b)
    q=s*c**8; kap=2*c**-6; lam=5*c**-12
    return s,c,q,kap,lam
def Ks(P,y,kap,lam):
    K1=5*P*y+10*kap*P**2*y**3+lam*P**3*y**5
    K2=P+6*kap*P**2*y**2+lam*P**3*y**4
    K3=3*kap*P**2*y+lam*P**3*y**3
    K4=kap*P**2+lam*P**3*y**2
    K5=lam*P**3*y
    K6=lam*P**3
    return [K1,K2,K3,K4,K5,K6]
def best(b,states=6):
    s,c,q,kap,lam=consts(b)
    bestR=1e9;arg=None
    for i in range(1,400):
        P=i/400
        lo,hi=0.0,2.0
        # find max y with all Ks<=1 (monotone in y)
        for _ in range(60):
            m=(lo+hi)/2
            if max(Ks(P,m,kap,lam)[:states])<=1: lo=m
            else: hi=m
        y=lo
        if y<=0: continue
        R=q/(P*P*y)
        if R<bestR: bestR=R;arg=(P,y)
    return bestR,arg,q
for b in [0.1,0.15,0.18,0.2,2/9,0.25,0.27,0.3,1/3]:
    for st in [6,3,2]:
        R,arg,q=best(b,st)
        print(f"beta={b:.4f} states<= {st}: R={R:.4f} R/q={R/q:.3f} P,y={arg}")
