# GUIDE: Kraft optimum with improved branching penalties g4, g6 (kap=g4 c^-6, lam=g6 c^-12).
import math
def Ks(P,y,kap,lam):
    K1=5*P*y+10*kap*P**2*y**3+lam*P**3*y**5
    K2=P+6*kap*P**2*y**2+lam*P**3*y**4
    K3=3*kap*P**2*y+lam*P**3*y**3
    K4=kap*P**2+lam*P**3*y**2
    K5=lam*P**3*y
    K6=lam*P**3
    return [K1,K2,K3,K4,K5,K6]
def best(q,kap,lam,states):
    bestR=1e9;arg=None
    for i in range(1,800):
        P=i/800; lo,hi=0.0,2.0
        for _ in range(60):
            m=(lo+hi)/2
            if max(Ks(P,m,kap,lam)[:states])<=1: lo=m
            else: hi=m
        y=lo
        if y<=0: continue
        R=q/(P*P*y)
        if R<bestR: bestR=R;arg=(P,y)
    return bestR,arg
for b in [0.18,0.2,2/9,0.24,0.25]:
    s=math.sinh(b)/2;c=math.cosh(b);q=s*c**8
    for g4,g6 in [(2,5),(1.138,5),(1.138,1.707),(1,1)]:
        for st in [6,2]:
            R,arg=best(q,g4*c**-6,g6*c**-12,st)
            print(f"beta={b:.4f} g4={g4} g6={g6} st<={st}: R={R:.4f} R/q={R/q:.3f} P,y={arg[0]:.3f},{arg[1]:.4f}")
