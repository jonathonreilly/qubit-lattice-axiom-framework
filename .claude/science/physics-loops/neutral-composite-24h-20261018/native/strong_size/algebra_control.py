"""Exact integer Pauli support check; no state or weak-coupling approximation."""
from pathlib import Path
import sys,json
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from compass_sector_basis import geometry
rows=[]
for L in range(4,33):
 for periodic in [False,True]:
  sites,bonds=geometry((2,2,L));idx={p:i for i,p in enumerate(sites)}
  if periodic:
   bonds += [(idx[x,y,L-1],idx[x,y,0],2) for x in range(2) for y in range(2)]
  for ell in range(2,L-1,2):
   a=(L-ell)//2;S={i for i,(x,y,z) in enumerate(sites) if x==0 and a<=z<a+ell}
   changed=[(i,j,k) for i,j,k in bonds if k!=0 and ((i in S) != (j in S))]
   expected={frozenset((idx[0,y,z],idx[0,y,z+1])) for y in range(2) for z in [a-1,a+ell-1]}
   assert len(changed)==4 and all(k==2 for i,j,k in changed)
   assert {frozenset((i,j)) for i,j,k in changed}==expected
   rows.append(dict(L=L,periodic_z=periodic,length=ell,changed_bonds=4))
(P/'strong_size/algebra_control.json').write_text(json.dumps(dict(cases=len(rows),all_pass=True,scope='Only specified full-transverse-width strings on thin grids',rows=rows),indent=2)+'\n')
print(len(rows),'exact support checks passed')
