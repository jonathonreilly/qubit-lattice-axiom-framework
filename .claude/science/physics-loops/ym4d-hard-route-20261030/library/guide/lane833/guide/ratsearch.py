# GUIDE: search simple rationals (P,y) feasible at c=1 for given (kap,lam) upper bounds; report best P^2 y.
from fractions import Fraction as F
def Ks(P,y,kap,lam):
    return [5*P*y+10*kap*P**2*y**3+lam*P**3*y**5,
            P+6*kap*P**2*y**2+lam*P**3*y**4,
            3*kap*P**2*y+lam*P**3*y**3,
            kap*P**2+lam*P**3*y**2,
            lam*P**3*y, lam*P**3]
for name,kap,lam in [("iso",F(239,210),F(239,140)),("finner",F(2),F(5))]:
    best=[]
    for dP in range(2,60):
        for nP in range(1,dP):
            P=F(nP,dP)
            for dy in range(2,60):
                for ny in range(1,dy):
                    y=F(ny,dy)
                    if P*P*y < (F(139,1000) if name=="iso" else F(97,1000)): continue
                    K=Ks(P,y,kap,lam)
                    if all(k<=1 for k in K):
                        best.append((P*P*y,P,y,[float(k) for k in K]))
    best.sort(key=lambda t:(-t[0], t[1].denominator+t[2].denominator))
    print(name)
    for b in best[:8]: print(float(b[0]),b[1],b[2],[round(k,4) for k in b[3]])
