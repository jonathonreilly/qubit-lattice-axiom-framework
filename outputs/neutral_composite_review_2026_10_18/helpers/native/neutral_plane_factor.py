"""Exact binary dimensions of plane algebra and its neutral commutant."""
from pathlib import Path
import json,itertools

def echelon(vs):
 piv={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k in piv:v^=piv[k]
   else:piv[k]=v;break
 return list(piv.values())
rows=[]
for shape in [(2,2,2),(3,2,2),(3,3,2),(3,3,3),(4,4,4),(5,5,5),(10,10,10)]:
 sites=list(itertools.product(*(range(l) for l in shape)));n=len(sites);mask=(1<<n)-1;planes=[]
 for a in range(3):
  for k in range(shape[a]):
   v=sum(1<<i for i,x in enumerate(sites) if x[a]==k)
   planes.append(v if a==0 else v|(v<<n) if a==1 else v<<n)
 W=echelon(planes);d=len(W)
 gram=[sum(((((a&mask)&(b>>n)).bit_count()+((a>>n)&(b&mask)).bit_count())%2)<<j for j,b in enumerate(W)) for a in W]
 sr=len(echelon(gram));assert sr%2==0 and d==sum(shape)-1
 r=sr//2;z=d-2*r;m=n-z-r
 assert z+r+m==n and 2*n-d==z+2*m
 rows.append(dict(shape=shape,sites=n,plane_rank=d,symplectic_rank=sr,central_bits=z,protected_qubits=r,neutral_multiplicity_qubits=m))
assert next(x for x in rows if x['shape']==(3,3,3))['neutral_multiplicity_qubits']==20
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(rows=rows,scope='Exact algebra dimensions and neutral matrix factorization; protected-mediator exclusion deferred, no classification of every dynamical zero mode.'),indent=2)+'\n');print(rows)
