# GUIDE: worst case c=1 (kap=2, lam=5): maximize P^2 y subject to K_D<=1 for all D.
from fractions import Fraction as F
from kraft3 import Ks
import math
best=(0,None)
for i in range(1,2000):
    P=i/2000; lo,hi=0.0,2.0
    for _ in range(60):
        m=(lo+hi)/2
        if max(Ks(P,m,2.0,5.0))<=1: lo=m
        else: hi=m
    if P*P*lo>best[0]: best=(P*P*lo,(P,lo))
print("max P^2 y at c=1:",best)
# check a rational candidate
for P,y in [(F(3,5),F(7,25)),(F(29,50),F(7,25)),(F(117,200),F(57,200)),(F(58,100),F(29,100))]:
    K=[5*P*y+10*2*P**2*y**3+5*P**3*y**5, P+6*2*P**2*y**2+5*P**3*y**4, 3*2*P**2*y+5*P**3*y**3, 2*P**2+5*P**3*y**2, 5*P**3*y, 5*P**3]
    print(P,y,"P^2y=",float(P*P*y),[float(k) for k in K], all(k<=1 for k in K))
# q at candidate endpoints
for b in [1/6,0.17,0.175]:
    s=math.sinh(b)/2;c=math.cosh(b);print(b,"q=",s*c**8)
