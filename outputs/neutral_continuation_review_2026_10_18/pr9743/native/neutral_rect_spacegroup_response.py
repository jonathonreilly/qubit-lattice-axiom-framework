import numpy as np,json,time
from pathlib import Path
from neutral_rect_model import sector
from neutral_spacegroup_model import orbit_op
p=Path('/private/tmp/neutral_rect_spacegroup_data');D=sector((3,3,4));data=tuple(np.load(p/(x+'.npy'),mmap_mode='r') for x in ['labels','signs','reps','sizes'])+(0,);meta=json.loads((p/'low.json').read_text());V=np.load(p/'low_vectors.npy');g=V[:,0];E0=meta['rows'][0]['energy'];H=orbit_op(sum(D['H'],[]),data);Hs=[orbit_op(x,data) for x in D['H']];S=orbit_op(D['S'],data);terms=[]
for x in range(3):
 for y in range(3):
  for z in range(4):terms.append(D['project']((0,(1<<(12*x+4*y+z))^(1<<(12*x+4*y+(z+2)%4)),1)))
C=orbit_op(terms,data);sources=dict(plaquette=S@g,directional=Hs[2]@g-(Hs[0]@g+Hs[1]@g)/2,original_Cz=C@g)
from collections import defaultdict
from neutral_rect_model import mult
def comm(a,b):
 d=defaultdict(float)
 for x in a:
  for y in b:
   u=mult(x,y);v=mult(y,x);d[u[:2]]+=u[2];d[v[:2]]-=v[2]
 return [(x,z,c) for (x,z),c in d.items() if c]
ht=sum(D['H'],[]);qt=[]
for a in D['H']:qt+=comm(a,comm(ht,a))
qsrc=orbit_op(qt,data)@g
sources['native_Q']=qsrc;rows=[]
for name,src in sources.items():
 mean=g@src;src-=g*mean;variance=src@src;weights=(V.T@src)**2;weights[0]=0
 row=dict(source=name,mean=float(mean),variance=float(variance),captured_low_weight=float(weights.sum()),lines=[dict(gap=erow['gap'],weight=float(weights[i]),residual=erow['residual']) for i,erow in enumerate(meta['rows']) if i and weights[i]>1e-9]);rows.append(row);print(row,flush=True)
out=dict(rows=rows,scope='Exact36siteHamiltonian selected symmetrysector,20numerical loweigenpairs; sourceoperatorsgiven/diagnostic notempiricalmapping; shapeanisotropic')
(p/'response.json').write_text(json.dumps(out,indent=2)+'\n')
