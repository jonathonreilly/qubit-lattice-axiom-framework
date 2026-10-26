from t22 import *
import itertools
res=[]
t=time.time()
for a in (-0.5,0.0,0.25,0.5,0.75,1.0,1.5):
    for b in (-0.5,0.0,0.25,0.5,0.75,1.0,1.5):
        M=proj(UU)+proj(DD)+a*proj(S)+b*proj(T0)
        rows=scanM(M,tabs)
        # only isolated: gap>0.3 and null==3 exact (need level info): use all rows
        sel=[r for r in rows if r[6]>0.3]
        mx=max([r[3] for r in sel],default=None)
        res.append((a,b,mx))
        print(a,b,None if mx is None else round(mx,3),flush=True)
print(time.time()-t)
