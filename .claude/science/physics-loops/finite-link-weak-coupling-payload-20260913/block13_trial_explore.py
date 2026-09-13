from pathlib import Path
from itertools import product
from collections import defaultdict
import numpy as np,json
P=Path(__file__).resolve().parent
# Cube: positively oriented x/y/z links within [0,1]^3, with outward faces.
verts=list(product(range(2),repeat=3));edges=[]
for x in verts:
 for i in range(3):
  if x[i]==0:
   y=list(x);y[i]=1;edges.append((x,tuple(y)))
ei={e:j for j,e in enumerate(edges)};D=np.zeros((8,12),int)
for j,(x,y) in enumerate(edges):D[verts.index(x),j]=1;D[verts.index(y),j]=-1
B=np.zeros((12,6),int);faces=[]
for normal in range(3):
 ij=[i for i in range(3) if i!=normal]
 for side in [0,1]:
  x=[0,0,0];x[normal]=side;i,j=ij
  v0=tuple(x);xx=x.copy();xx[i]=1;v1=tuple(xx);xx[j]=1;v2=tuple(xx);xx[i]=0;v3=tuple(xx)
  sign=(1 if side else -1)*(1 if normal!=1 else -1)
  face=len(faces);faces.append((normal,side))
  for a,b in [(v0,v1),(v1,v2),(v2,v3),(v3,v0)]:
   if (a,b) in ei:B[ei[(a,b)],face]=sign
   else:B[ei[(b,a)],face]=-sign
assert np.max(abs(D@B))==0 and np.max(abs(B.sum(axis=1)))==0
records=[]
for M in [0,1,2]:
 kappa=np.pi/(2*M+2);amplitudes=defaultdict(float)
 for n in product(range(-M,M+1),repeat=6):
  value=float(np.prod(np.cos(kappa*np.array(n))));key=tuple(B@np.array(n));amplitudes[key]+=value
 norm=sum(a*a for a in amplitudes.values());ws=[]
 for j in range(6):
  shift=B[:,j];value=sum(a*amplitudes.get(tuple(np.array(e)-shift),0) for e,a in amplitudes.items())/norm;ws.append(float(value))
  assert value>=np.cos(kappa)-1e-12
  for e,a in amplitudes.items():
   left=amplitudes.get(tuple(np.array(e)-shift),0)+amplitudes.get(tuple(np.array(e)+shift),0)
   assert left>=2*np.cos(kappa)*a-1e-11
 e2=sum(a*a*np.dot(e,e) for e,a in amplitudes.items())/norm
 records.append(dict(M=M,auxiliary_count=(2*M+1)**6,physical_count=len(amplitudes),norm=norm,product_norm=(M+1)**6,plaquette_expectations=ws,lower_bound=float(np.cos(kappa)),electric_sum_square=float(e2),maximum_link_flux=int(max(max(abs(v) for v in e) for e in amplitudes))))
result=dict(incidence=B.tolist(),records=records);(P/'BLOCK13_TRIAL_EXPLORATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(records,indent=2))
