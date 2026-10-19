"""Test full Pauli support of interior rectangular X patches, retaining side walls."""
from pathlib import Path
import sys,json
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from compass_sector_basis import geometry
rows=[]
for Ny,Nz in [(6,8),(8,12),(12,16)]:
 sites,bonds=geometry((3,Ny,Nz))
 for w in range(2,Ny-1,2):
  for ell in range(2,Nz-1,2):
   S={i for i,(x,y,z) in enumerate(sites) if x==1 and 1<=y<1+w and 1<=z<1+ell}
   counts=[0,0,0]
   for i,j,a in bonds:
    if a!=0 and ((i in S)!=(j in S)):counts[a]+=1
   assert counts==[0,2*ell,2*w]
   rows.append(dict(shape=[3,Ny,Nz],width=w,length=ell,changed_XX=counts[0],changed_YY=counts[1],changed_ZZ=counts[2]))
(P/'strong_size/compact_patch_control.json').write_text(json.dumps(dict(cases=len(rows),all_pass=True,rows=rows),indent=2)+'\n')
print(len(rows),'compact patch support checks passed')
