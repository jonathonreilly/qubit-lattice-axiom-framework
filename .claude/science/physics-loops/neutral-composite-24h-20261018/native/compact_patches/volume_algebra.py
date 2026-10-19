from pathlib import Path
import json
from native_mpo import geometry
sites,bonds=geometry((4,6,8));idx={p:i for i,p in enumerate(sites)}
rows=[]
for k in [1,2]:
 for w in [2,4]:
  for ell in [2,4,6]:
   S={i for i,(x,y,z) in enumerate(sites) if 1<=x<1+k and 1<=y<1+w and 1<=z<1+ell}
   cuts=[sum(a==b and ((i in S)!=(j in S)) for i,j,a in bonds) for b in [1,2]]
   assert cuts==[2*k*ell,2*k*w]
   rows.append(dict(thickness=k,width=w,length=ell,changed_YY=cuts[0],changed_ZZ=cuts[1]))
# Adjacent parallel planes have no shared y/z bonds, so the diagonal fusion difference vanishes.
S={idx[1,y,z] for y in [1,2] for z in [1,2]};T={idx[2,y,z] for y in [1,2] for z in [1,2]}
assert sum(a in [1,2] and ((i in S and j in T) or (i in T and j in S)) for i,j,a in bonds)==0
out=dict(cases=len(rows),all_pass=True,x_face_fusion_contribution=0,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
