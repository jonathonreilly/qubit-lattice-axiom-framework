"""State-independent native Pauli cut/fusion identities on compact patches."""
from pathlib import Path
import json,itertools
from native_mpo import geometry
P=Path(__file__).resolve().parent
sites,bonds=geometry((3,6,6));ix={p:i for i,p in enumerate(sites)}
def cut(S):return {k:2 for k,(i,j,a) in enumerate(bonds) if a in [1,2] and ((i in S)!=(j in S))}
rows=[]
for w in [1,2,3]:
 for ell in [1,2,3,4]:
  S={ix[1,y,z] for y in range(1,1+w) for z in range(1,1+ell)}
  assert len(cut(S))==2*(w+ell)
  for shift in [w,w+1]:
   if 1+shift+w>5:continue
   T={ix[1,y,z] for y in range(1+shift,1+shift+w) for z in range(1,1+ell)}
   assert not S&T
   lhs={k:cut(S|T).get(k,0)-cut(S).get(k,0)-cut(T).get(k,0) for k in range(len(bonds))}
   rhs={k:-4 if a in [1,2] and ((i in S and j in T) or (i in T and j in S)) else 0 for k,(i,j,a) in enumerate(bonds)}
   assert lhs==rhs
   rows.append(dict(w=w,ell=ell,shift=shift,shared_bonds=sum(v==-4 for v in rhs.values())))
(P/'fusion_control.json').write_text(json.dumps(dict(cases=len(rows),all_pass=True,scope='Exact operator identity, not relaxed bound-state or size selection',rows=rows),indent=2)+'\n');print(len(rows),'fusion identities passed')
