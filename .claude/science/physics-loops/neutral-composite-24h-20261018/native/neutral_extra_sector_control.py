import sys,json
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from compass_sector_basis import basis
from neutral_extra_sector import reducer
D=basis((3,3,3));st=[]
for y in [0,1]:
 m=sum(1<<i for i,x in enumerate(D['sites']) if x[1] in [y,y+1]);st.append(D['reduce_term'](m,m,-1))
rng=np.random.default_rng(18026);checks=0
for signs in [(1,1),(1,-1),(-1,1),(-1,-1)]:
 R=reducer(22,st,signs)
 for j in rng.integers(0,R['dimension'],size=50):
  j=int(j);v=R['vector'](j)
  for t in D['terms']:
   f,z,c=t;got={i^f:a*c*(-1)**((z&i).bit_count()) for i,a in v.items()}
   rf,rz,rc=R['reduce'](t);factor=rc*(-1)**((rz&j).bit_count());want={i:a*factor for i,a in R['vector'](j^rf).items()}
   assert got==want;checks+=1
out=dict(checks=checks,dimension=R['dimension'],stabilizers=st,pivots=R['pivots'])
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
