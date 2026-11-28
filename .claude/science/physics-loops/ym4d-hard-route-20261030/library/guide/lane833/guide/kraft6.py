# GUIDE: c=1 worst case with isolated-branching constants g4=(2/3)(1+2^-1/2), g6=1+2^-1/2.
import math
def Ks(P,y,kap,lam):
    return [5*P*y+10*kap*P**2*y**3+lam*P**3*y**5,
            P+6*kap*P**2*y**2+lam*P**3*y**4,
            3*kap*P**2*y+lam*P**3*y**3,
            kap*P**2+lam*P**3*y**2,
            lam*P**3*y, lam*P**3]
g4=(2/3)*(1+2**-0.5); g6=1+2**-0.5
for kap,lam,name in [(2,5,"finner"),(g4,g6,"iso")]:
    best=(0,None)
    for i in range(1,4000):
        P=i/4000; lo,hi=0.0,2.0
        for _ in range(60):
            m=(lo+hi)/2
            if max(Ks(P,m,kap,lam))<=1: lo=m
            else: hi=m
        if P*P*lo>best[0]: best=(P*P*lo,(P,lo),Ks(P,lo,kap,lam))
    print(name,"max P^2y=",best[0],"at",best[1],"Ks",[round(k,4) for k in best[2]])
    # endpoint where q(beta)=P^2 y
    lo,hi=0.0,1.0
    for _ in range(60):
        m=(lo+hi)/2; q=math.sinh(m)/2*math.cosh(m)**8
        if q<best[0]: lo=m
        else: hi=m
    print("  beta endpoint (q=P^2y):",lo)
# also with c-dependence at beta: kap=g4 c^-6 etc
for b in [0.2,2/9,0.23,0.235,0.24]:
    s=math.sinh(b)/2;c=math.cosh(b);q=s*c**8
    kap=g4*c**-6;lam=g6*c**-12
    best=(0,None)
    for i in range(1,2000):
        P=i/2000; lo,hi=0.0,2.0
        for _ in range(60):
            m=(lo+hi)/2
            if max(Ks(P,m,kap,lam))<=1: lo=m
            else: hi=m
        if P*P*lo>best[0]: best=(P*P*lo,(P,lo))
    print(f"iso beta={b:.4f}: R={q/best[0]:.4f}")
