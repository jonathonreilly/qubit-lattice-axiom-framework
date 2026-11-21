# GUIDE: peeling (decoder-order integration) weights. Constraints beta-independent in (X2=X^2, Z).
import math
M1=4/(3*math.pi); M2=0.25; M3=8/(15*math.pi); M4=1/8; M5=32/(105*math.pi); M6=5/64
def Ks(a,Z):  # a = X^2
    return [5*M1*a*Z+10*M3*a**2*Z**3+M5*a**3*Z**5,
            a+6*M2*a**2*Z**2+M4*a**3*Z**4,
            3*M1*a**2*Z+M3*a**3*Z**3,
            a**2+M2*a**3*Z**2,
            M1*a**3*Z, a**3]
best=(0,None)
for i in range(1,4001):
    a=i/4000; lo,hi=0.0,5.0
    for _ in range(80):
        m=(lo+hi)/2
        if max(Ks(a,m))<=1: lo=m
        else: hi=m
    val=a*a*lo
    if val>best[0]: best=(val,(a,lo),Ks(a,lo))
print("max X^4 Z =",best[0],"at a=X^2,Z =",best[1],"Ks",[round(k,4) for k in best[2]])
print("rate R/q =",2/best[0])
for b in [1/6,0.2,2/9,0.25,0.27,0.28,0.3,1/3]:
    s=math.sinh(b)/2;c=math.cosh(b);q=s*c**8
    print(f"beta={b:.4f} q={q:.5f} R={2*q/best[0]:.4f}  deg2-only R={10*M1*q:.4f}")
