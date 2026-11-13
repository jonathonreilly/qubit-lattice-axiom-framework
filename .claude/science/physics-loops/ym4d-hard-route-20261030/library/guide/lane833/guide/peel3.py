# GUIDE: per-link peeling scheme in variables a=X^2, V=sh*Y. Rate R = sh/(a^2 V). Find optimum at beta and test rationals.
import math
from fractions import Fraction as F
M1=4/(3*math.pi); M2=0.25; M3=8/(15*math.pi); M4=1/8; M5=32/(105*math.pi)
def Ks(a,V,c2,c4):
    return [5*c4*M1*a*V+10*c2*M3*a**2*V**3+M5*a**3*V**5,
            c4*a+6*c2*M2*a**2*V**2+M4*a**3*V**4,
            3*c2*M1*a**2*V+M3*a**3*V**3,
            c2*a**2+M2*a**3*V**2,
            M1*a**3*V, a**3]
for b in [0.24,0.245]:
    sh=math.sinh(b); c=math.cosh(b); c2=c*c; c4=c2*c2
    best=(1e9,None)
    for i in range(1,2000):
        a=i/2000; lo,hi=0.0,10.0
        for _ in range(70):
            V=(lo+hi)/2
            if max(Ks(a,V,c2,c4))<=1: lo=V
            else: hi=V
        V=lo
        if V>0 and sh/(a*a*V)<best[0]: best=(sh/(a*a*V),(a,V))
    a,V=best[1]
    print(f"beta={b}: best rate {best[0]:.4f} at a={a:.4f} V={V:.4f}, Ks={[round(k,4) for k in Ks(a,V,c2,c4)]}")
# candidate rationals at beta=0.24 using upper bounds c2<=1.0587, c4<=1.1208, sh<=0.24232
c2u=1.0587; c4u=1.1208; shu=0.24232
for a,V in [(0.66,0.565),(0.65,0.57),(2/3,0.56),(0.66,0.56),(0.65,0.565),(13/20,4/7),(0.64,0.58),(0.645,0.575)]:
    K=Ks(a,V,c2u,c4u)
    print(a,V,"rate<=",round(shu/(a*a*V),4),[round(k,4) for k in K],max(K)<=1)
