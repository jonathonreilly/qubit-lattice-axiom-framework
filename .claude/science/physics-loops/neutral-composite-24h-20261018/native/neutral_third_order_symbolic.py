from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import random,json
import sys
R=int(sys.argv[1]) if len(sys.argv)>1 else 6;L=4;N=R*R
bonds=[];masks={}
for x,y,z in product(range(R),range(R),range(L)):
 i=x*R+y
 for axis,j in [('x',((x+1)%R)*R+y),('y',x*R+(y+1)%R)]:
  b=(axis,4*i+z,4*j+z);m=(1<<b[1])^(1<<b[2]);bonds.append(b);masks[m]=b
@lru_cache(None)
def wall(s):
 return sum(((q:=((s>>(4*c))&15))^((q<<1|q>>3)&15)).bit_count() for c in range(N))
def phase(s,b):
 return -1 if b[0]=='x' else (1-2*((s>>b[1])&1))*(1-2*((s>>b[2])&1))
def neighbors(s):
 return [(s^(1<<b[1])^(1<<b[2]),phase(s,b)) for b in bonds]
@lru_cache(None)
def C(a,b):
 nb=dict(neighbors(b));out=F(0)
 for q,v in neighbors(a):
  n=wall(q)
  if n!=2 and q in nb:out+=F(v*nb[q],(4-2*n)**2)
 return out
def third(a,b):
 na=[(q,v,4-2*wall(q)) for q,v in neighbors(a) if wall(q)!=2]
 nb=[(q,v,4-2*wall(q)) for q,v in neighbors(b) if wall(q)!=2]
 raw=F(0)
 for q,v,d in na:
  for r,w,e in nb:
   bond=masks.get(q^r)
   if bond:raw+=F(v*w*phase(q,bond),d*e)
 fold=F(0)
 for p,v in neighbors(a):
  if wall(p)==2:fold+=F(v,2)*C(p,b)
 for p,v in neighbors(b):
  if wall(p)==2:fold+=F(v,2)*C(a,p)
 return raw-fold,raw,fold

from collections import defaultdict

def phaseword(s,b):
 return (phase(s,b),0 if b[0]=='x' else (1<<(b[1]//4))^(1<<(b[2]//4)))
def nwords(s):
 return [(s^(1<<b[1])^(1<<b[2]),*phaseword(s,b)) for b in bonds]
def cw(a,b):
 nb={q:(v,m) for q,v,m in nwords(b)};out=defaultdict(F)
 for q,v,m in nwords(a):
  n=wall(q)
  if n!=2 and q in nb:
   w,k=nb[q];out[m^k]+=F(v*w,(4-2*n)**2)
 return {m:v for m,v in out.items() if v}
def dw(a,b):
 na=[(q,v,m,4-2*wall(q)) for q,v,m in nwords(a) if wall(q)!=2]
 nb=[(q,v,m,4-2*wall(q)) for q,v,m in nwords(b) if wall(q)!=2]
 raw=defaultdict(F);fold=defaultdict(F)
 for q,v,m,d in na:
  for r,w,k,e in nb:
   bond=masks.get(q^r)
   if bond:
    u,l=phaseword(q,bond);raw[m^k^l]+=F(v*w*u,d*e)
 for p,v,m in nwords(a):
  if wall(p)==2:
   for k,w in cw(p,b).items():fold[m^k]+=F(v,2)*w
 for p,v,m in nwords(b):
  if wall(p)==2:
   for k,w in cw(a,p).items():fold[m^k]+=F(v,2)*w
 keys=raw.keys()|fold.keys();out={k:raw[k]-fold[k] for k in keys if raw[k]!=fold[k]}
 return out,{k:v for k,v in raw.items() if v},{k:v for k,v in fold.items() if v}
rows=[]
for axis,j in [('x',R),('y',1)]:
 a=1;b=1<<(4*j)
 for changed in [False,True]:
  target=b^(15^(15<<(4*j))) if changed else b
  value,raw,fold=dw(a,target)
  mask=0 if axis=='x' else 1^(1<<j)
  expected=F(-1,4) if changed and axis=='x' else F(1,4) if changed else F(1,8)
  assert value=={mask:expected},(axis,changed,value)
  rows.append(dict(axis=axis,background_changed=changed,result={str(k):str(v) for k,v in value.items()},raw={str(k):str(v) for k,v in raw.items()},fold={str(k):str(v) for k,v in fold.items()}))
print(json.dumps(dict(status='pass',all_background_symbolic=True,rows=rows),indent=2))
