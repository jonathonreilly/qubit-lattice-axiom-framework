from fractions import Fraction as F
from itertools import product
import json

def check(b):
 es=[('x',(0,0,0),(1,0,0)),('y',(1,0,0),(1,1,0)),('x',(0,1,0),(1,1,0)),('y',(0,0,0),(0,1,0))]
 bonds=list(es)
 if b not in bonds:bonds.append(b)
 target=[1]*4+([2] if len(bonds)==5 else [])
 if len(bonds)==4:target[bonds.index(b)]+=2
 sites=sorted(set(p for _,a,c in bonds for p in (a,c))); idx={p:i for i,p in enumerate(sites)}
 bs=[(a,(1<<idx[p])|(1<<idx[q]),idx[p],idx[q]) for a,p,q in bonds]
 def en(s):
  flipped={sites[i] for i in range(len(sites)) if s>>i&1};return 2*sum(((x,y,(z+dz)%6) not in flipped) for x,y,z in flipped for dz in (-1,1))
 def apply(v,j):
  a,mask,i,k=bs[j];out={}
  for s,c in v.items():
   amp=-1 if a=='x' else 1-2*(((s>>i)^(s>>k))&1)
   out[s^mask]=out.get(s^mask,F(0))+amp*c
  return out
 zero=tuple(0 for _ in target);psi={zero:{0:F(1)}};ener={zero:F(0)}
 alphas=sorted(product(*(range(t+1) for t in target)),key=sum)
 for al in alphas[1:]:
  rhs={}
  for j in range(len(target)):
   if al[j]:
    prev=list(al);prev[j]-=1
    for s,v in apply(psi[tuple(prev)],j).items():rhs[s]=rhs.get(s,F(0))+v
  ener[al]=rhs.get(0,F(0))
  for beta,e in list(ener.items()):
   if not e or beta==al or any(b>a for a,b in zip(al,beta)):continue
   rem=tuple(a-b for a,b in zip(al,beta))
   for s,v in psi[rem].items():rhs[s]=rhs.get(s,F(0))-e*v
  psi[al]={s:-v/F(en(s)) for s,v in rhs.items() if s and v}
 return ener[tuple(target)]
rows=[]
for z in (0,1,5,2):
 bs=set()
 for x,y in product(range(2),repeat=2):
  for axis,dx,dy in [('x',1,0),('y',0,1)]:
   for shift in (0,-1):
    p=(x+shift*dx,y+shift*dy,z);q=(p[0]+dx,p[1]+dy,z);bs.add((axis,p,q))
 subtotal=F(0)
 for b in sorted(bs):
  v=check(b);subtotal+=v;rows.append({'bond':b,'coefficient':str(v)})
 print(z,str(subtotal),flush=True)
