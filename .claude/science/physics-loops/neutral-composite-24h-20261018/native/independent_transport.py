from collections import defaultdict
from itertools import product
from functools import lru_cache
from pathlib import Path
import json
coords=list(product(range(-5,6),repeat=3));idx={x:i for i,x in enumerate(coords)}
def pauli(points,a):
 mask=sum(1<<idx[p] for p in points)
 return (mask if a<2 else 0, mask if a>0 else 0)
@lru_cache(None)
def sites(w):
 m=w[0]|w[1];o=[]
 while m:
  b=m&-m;m-=b;o.append(b.bit_length()-1)
 return o
@lru_cache(None)
def incident(i):
 p=coords[i];out=set()
 for a in range(3):
  for sign in [-1,1]:
   q=list(p);q[a]+=sign;out.add(pauli((p,tuple(q)),a))
 return out

def D(A):
 out=defaultdict(int)
 for (x,z),c in A.items():
  bonds=set()
  for i in sites((x,z)):bonds.update(incident(i))
  for xx,zz in bonds:
   if ((xx&z).bit_count()+(zz&x).bit_count())%2==0:continue
   ox=xx^x;oz=zz^z
   phase=((xx&zz).bit_count()+(x&z).bit_count()-(ox&oz).bit_count()+2*(zz&x).bit_count())%4
   assert phase in(1,3)
   out[(ox,oz)]+=(-2 if phase==1 else 2)*c
 return {w:c for w,c in out.items() if c}

def corr(A):
 groups=defaultdict(list)
 for (x,z),c in A.items():
  pp=sites((x,z));anchor=coords[pp[0]];key=[]
  for i in pp:
   a=1 if ((x>>i)&1 and (z>>i)&1) else (0 if (x>>i)&1 else 2)
   key.append(tuple(coords[i][j]-anchor[j] for j in range(3))+(a,))
  groups[tuple(key)].append((anchor,c))
 out=defaultdict(int)
 for entries in groups.values():
  for p,c in entries:
   for q,d in entries:out[tuple(p[j]-q[j] for j in range(3))]+=c*d
 return {r:c for r,c in out.items() if c}
A={}
for a in range(3):
 p=[0,0,0];q=p.copy();p[a]=-1;q[a]=1;A[pauli((tuple(p),tuple(q)),a)]=1
rows=[]
for n in range(5):
 cr=corr(A)
 assert all((len(sites(w))-n)%2==0 for w in A)
 row={'n':n,'terms':len(A),'norm2':sum(c*c for c in A.values()),'correlations':{str(r):c for r,c in sorted(cr.items())}}
 rows.append(row);print(row,flush=True)
 if n<4:A=D(A)
Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
