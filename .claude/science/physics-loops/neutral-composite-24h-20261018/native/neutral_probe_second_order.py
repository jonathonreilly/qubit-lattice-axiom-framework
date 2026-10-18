from fractions import Fraction as F
from collections import defaultdict
import random,json
R=6;L=4;N=R*R
rng=random.Random(1821)
bonds=[]
for x in range(R):
 for y in range(R):
  for z in range(L):
   i=x*R+y
   for axis,j in [('x',((x+1)%R)*R+y),('y',x*R+(y+1)%R)]:bonds.append((axis,4*i+z,4*j+z))
def wall(s):
 total=0
 for c in range(N):
  q=(s>>(4*c))&15;total+=(q^((q<<1|q>>3)&15)).bit_count()
 return total
def act(s,b):
 axis,i,j=b;v=-1 if axis=='x' else (1-2*((s>>i)&1))*(1-2*((s>>j)&1))
 return s^(1<<i)^(1<<j),v
out=[]
for run in range(3):
 bg=[1]*N if run==0 else [rng.choice([-1,1]) for i in range(N)]
 aligned=sum(15<<(4*i) for i,s in enumerate(bg) if s<0);i=0;z=0;initial=aligned^(1<<(4*i+z));row=defaultdict(F)
 for b in bonds:
  mid,a=act(initial,b);nm=wall(mid)
  if nm==2:continue
  for c in bonds:
   final,aa=act(mid,c)
   if wall(final)==2:row[final]+=F(a*aa,4-2*nm)
 row[initial]+=F(len(bonds),8)
 row={s:c for s,c in row.items() if c}
 # D=Tx-Ty, including physical background sign. Check R2=-D²/8.
 def step(j):
  x,y=divmod(j,R)
  return [(((x+1)%R)*R+y,-1),(((x-1)%R)*R+y,-1),(x*R+(y+1)%R,bg[j]*bg[x*R+(y+1)%R]),(x*R+(y-1)%R,bg[j]*bg[x*R+(y-1)%R])]
 expected=defaultdict(F)
 for j,a in step(i):
  for k,aa in step(j):expected[aligned^(1<<(4*k+z))]-=F(a*aa,8)
 expected={s:c for s,c in expected.items() if c};assert row==expected,(row,expected)
 out.append(dict(run=run,outputs=len(row),diagonal=str(row[initial]),coefficients=sorted(map(str,row.values()))))
print(json.dumps(dict(exact_controls=out,identity='R2 relative vacuum = -(Tx-Ty)^2/8',scope='Second-order native N2 singleton block; no added interaction')))
