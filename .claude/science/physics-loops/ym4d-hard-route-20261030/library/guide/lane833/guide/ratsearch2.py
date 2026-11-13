# GUIDE: simple fractions (small denominators) feasible at kap=239/210, lam=239/140 with P^2 y >= 0.1366
from fractions import Fraction as F
kap,lam=F(239,210),F(239,140)
def Ks(P,y):
    return [5*P*y+10*kap*P**2*y**3+lam*P**3*y**5, P+6*kap*P**2*y**2+lam*P**3*y**4,
            3*kap*P**2*y+lam*P**3*y**3, kap*P**2+lam*P**3*y**2, lam*P**3*y, lam*P**3]
res=[]
for dP in range(2,41):
    for nP in range(1,dP):
        P=F(nP,dP)
        if P.denominator!=dP: continue
        for dy in range(2,41):
            for ny in range(1,dy):
                y=F(ny,dy)
                if y.denominator!=dy: continue
                if P*P*y<F(1366,10000): continue
                K=Ks(P,y)
                if max(K)<=1: res.append((dP+dy,float(P*P*y),P,y,[round(float(k),5) for k in K]))
res.sort()
for r in res[:12]: print(r)
# rational upper bound for q(2/9)
x=F(2,9); s=(x/(1-x*x/6))/2; u=4*x*x; e=1+u+u*u/(2*(1-u/3)); q=s*e
print("q(2/9)<=",float(q), q)
