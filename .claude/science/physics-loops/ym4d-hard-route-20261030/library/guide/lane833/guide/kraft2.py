# GUIDE: sensitivity of the Kraft optimum to the branching constants kap, lam.
import math
from kraft1 import Ks
def best(q,kap,lam,states):
    bestR=1e9;arg=None
    for i in range(1,400):
        P=i/400; lo,hi=0.0,2.0
        for _ in range(60):
            m=(lo+hi)/2
            if max(Ks(P,m,kap,lam)[:states])<=1: lo=m
            else: hi=m
        y=lo
        if y<=0: continue
        R=q/(P*P*y)
        if R<bestR: bestR=R;arg=(P,y)
    return bestR,arg
for b in [2/9,0.25]:
    s=math.sinh(b)/2;c=math.cosh(b);q=s*c**8
    for name,kap,lam in [("finner",2*c**-6,5*c**-12),("nopen",c**-6,c**-12),("nobranch",0,0)]:
        for st in [6,2]:
            R,arg=best(q,kap,lam,st)
            print(f"beta={b:.4f} {name} states<={st}: R/q={R/q:.3f} R={R:.4f} 1/q={1/q:.3f}")
