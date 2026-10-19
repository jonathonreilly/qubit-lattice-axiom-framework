"""Exact binary rank controls for the open compass bond algebra."""
import itertools,json
from pathlib import Path

def rank(vs):
 piv={}
 for v in vs:
  while v:
   k=v.bit_length()-1
   if k in piv:v^=piv[k]
   else:piv[k]=v;break
 return len(piv),piv

def check(shape):
 sites=list(itertools.product(*(range(l) for l in shape)));idx={x:i for i,x in enumerate(sites)};n=len(sites);mask=(1<<n)-1
 def pauli(a,inds):
  b=sum(1<<i for i in inds)
  return b if a==0 else b|(b<<n) if a==1 else b<<n
 bonds=[]
 for x,i in idx.items():
  for a in range(3):
   y=list(x);y[a]+=1
   if y[a]<shape[a]:bonds.append(pauli(a,[i,idx[tuple(y)]]))
 planes=[pauli(a,[i for x,i in idx.items() if x[a]==k]) for a in range(3) for k in range(shape[a])]
 for b in bonds:
  for p in planes:assert (((b&mask)&(p>>n)).bit_count()+((b>>n)&(p&mask)).bit_count())%2==0
 rb,piv=rank(bonds);rp,_=rank(planes)
 assert rp==sum(shape)-1
 assert rb==2*n-rp
 # Central opposite-neighbor composite components, when available, reduce in bond span.
 count=0
 for x,i in idx.items():
  for a in range(3):
   if 0<x[a]<shape[a]-1:
    l=list(x);r=list(x);l[a]-=1;r[a]+=1;v=pauli(a,[idx[tuple(l)],idx[tuple(r)]])
    while v:
     k=v.bit_length()-1;assert k in piv;v^=piv[k]
    count+=1
 return dict(shape=shape,sites=n,bond_rank=rb,plane_rank=rp,neutral_dimension=2*n-rp,composite_checks=count)
rows=[check(s) for s in [(2,2,2),(3,2,2),(3,3,2),(3,3,3),(4,4,4),(5,4,3),(6,6,6),(10,10,10)]]
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n');print(rows)
