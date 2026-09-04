import numpy as np, itertools, sys; sys.path.insert(0,".")
from bridge_geom import *
L=6; S0=edge_s(L,0.0,1,[0,0,0,0]); g=geometry(S0,L)
cnt=np.zeros(NT,dtype=int)
for p in range(24):
    for m in range(10): cnt[TC[p,m]]+=1
th=2*np.pi-g['dfc'][:,0]
print("class  count  theta_sum/pi   key")
for t in range(NT):
    print(f"{t:4d} {cnt[t]:6d} {th[t]/np.pi:12.6f}   {TKEY[t]}")
