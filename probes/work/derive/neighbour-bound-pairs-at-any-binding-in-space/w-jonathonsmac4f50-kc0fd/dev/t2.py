from dev_engine import *
import time
Mz=np.eye(4,dtype=complex); Mall=build_M_all(Mz)
g=30.0; V=Vmat(g,Mall)
t=time.time()
roots=find_levels(V,24,+1,nscan=20)
print(time.time()-t)
import collections
grp=collections.defaultdict(list)
for j,r in roots: grp[round(r,7)].append(j)
for r,js in sorted(grp.items()): print(r,len(js))
