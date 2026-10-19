import json,numpy as np
from scipy.sparse.linalg import eigsh
from neutral_rect_model import sector
from neutral_translation_model import translation_tables,orbits,orbit_op
from collections import defaultdict
from neutral_rect_model import mult
def comm(a,b):
 d=defaultdict(float)
 for x in a:
  for y in b:
   u=mult(x,y);v=mult(y,x);d[u[:2]]+=u[2];d[v[:2]]-=v[2]
 return [(x,z,c) for (x,z),c in d.items() if c]
D=sector(3);T,R,C=translation_tables(D);data=orbits(D['dim'],T,R,C);ht=sum(D['H'],[]);H=orbit_op(ht,data)
E,V=eigsh(H,k=32,which='SA',tol=2e-12,ncv=72,v0=np.random.default_rng(61).normal(size=len(data[2])));g=V[:,0];S=orbit_op(D['S'],data);B=orbit_op([(x,z,c*(1 if a==2 else -.5)) for a,gg in enumerate(D['H']) for x,z,c in gg],data)
qt=[]
for a in D['H']:qt+=comm(a,comm(ht,a))
Q=orbit_op(qt,data);sources=[S@g,B@g,Q@g];rows=[]
for i,e in enumerate(E):
 rows.append(dict(index=i,gap=float(e-E[0]),residual=float(np.linalg.norm(H@V[:,i]-e*V[:,i])),S_weight=float((V[:,i]@sources[0])**2) if i else 0,B_weight=float((V[:,i]@sources[1])**2) if i else 0,Q_weight=float((V[:,i]@sources[2])**2) if i else 0))
print(json.dumps(rows,indent=2));open('/private/tmp/neutral_cube_low_spectrum.json','w').write(json.dumps(dict(ground=float(E[0]),rows=rows,scope='32 numerical low eigenpairs in selected zero-momentum plane sector'),indent=2)+'\n')
