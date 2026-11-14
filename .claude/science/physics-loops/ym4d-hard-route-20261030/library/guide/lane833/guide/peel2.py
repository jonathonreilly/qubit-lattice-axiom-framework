# GUIDE: peeling with per-link neighbourhood c^(6-d) instead of c^8 per plaquette.
# weight w(sigma|D) = c^(6-d) * (sh*Y)^j * M_j * X^d, d=D+j; product = ubound * X^(4|S|) Y^(|S|-1) / sh
# Sum_S u (X^4 Y)^|S| <= sh*Y ; rate R = 1/(X^4 Y).
import math
M=[1,4/(3*math.pi),0.25,8/(15*math.pi),1/8,32/(105*math.pi),5/64]
from math import comb
def maxrate(b):
    sh=math.sinh(b); c=math.cosh(b)
    best=1e9
    for i in range(1,600):
        X2=i/300.0
        lo,hi=0.0,50.0
        for _ in range(70):
            Y=(lo+hi)/2; ok=True
            for D in range(1,7):
                tot=0.0
                for j in range(0,7-D):
                    d=D+j
                    if d%2: continue
                    tot+=comb(6-D,j)*c**(6-d)*(sh*Y)**j*M[j]*X2**(d/2)
                if tot>1: ok=False;break
            if ok: lo=Y
            else: hi=Y
        Y=lo
        if Y>0:
            R=1/(X2*X2*Y)
            best=min(best,R)
    return best
for b in [2/9,0.235,0.24,0.245,0.25]:
    print(f"beta={b:.4f} rate={maxrate(b):.4f}")
