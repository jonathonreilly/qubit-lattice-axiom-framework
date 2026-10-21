"""Exact finite-pattern geometry/path controls, not microscopic ED."""
AUDIT_TIMEOUT_SEC=300
from fractions import Fraction as F
from itertools import combinations,permutations
from collections import Counter
import json,math

def syndrome(cols):
 s=set()
 for x,y in cols:s^={(x,y),(x-1,y),(x,y-1),(x-1,y-1)}
 return s

def perimeter(s):return sum((x+dx,y+dy) not in s for x,y in s for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)))
def inverse(s):
 return {(x,y) for x in range(min(x for x,y in s)+1,max(x for x,y in s)+1) for y in range(min(y for x,y in s)+1,max(y for x,y in s)+1) if sum(a<x and b<y for a,b in s)%2}
def adjacent(e):
 (x,y),(u,v)=sorted(e)
 return {(x,y),(x,y-1)} if y==v else {(x,y),(x-1,y)}
def mark(c,e):return sum(-1 if p in syndrome(c) else 1 for p in adjacent(e))
L=10;Delta=F(L,16);a=F(25*L,18432);b=F(3*L,8192);g=F(12155,33554432);d=F(1076510135,10567230160896)
classes=Counter()
for xs in combinations(range(6),3):
 for ys in combinations(range(6),3):
  for perm in permutations(range(3)):
   s={(xs[i],ys[j]) for i in range(3) for j in range(3) if j!=perm[i]}
   assert perimeter(s)>=16
   if perimeter(s)==16:classes[len(inverse(s))]+=1
c={(0,0),(1,1)};edges=[{(x,y),(x+dx,y+dy)} for x in range(-4,5) for y in range(-4,5) for dx,dy in ((1,0),(0,1))]
q6=Counter();orders={}
for e in edges:
 f=c^e;s=syndrome(f);q=len(s);per=perimeter(s)
 for e2 in edges:
  dest=f^e2;t=syndrome(dest)
  if len(t)!=6 or perimeter(t)!=16:continue
  key=tuple(sorted(dest))
  if q==6:
   assert per>16
   q6[key]+=F(1,per-16)
  elif dest!=c:
   den=(6-q)*Delta/4;nextden=2*a*(6-q)+2*b*(16-per)
   if key not in orders:orders[key]=[F(0),F(0),F(0)]
   orders[key][0]+=g*g/den
   orders[key][1]-=g*g*nextden/den**2
   orders[key][2]+=g*d*(mark(c,e)+mark(f,e2))/den
A=-48*g*g*b/Delta**2+8*g*d/Delta;B=-32*g*g*b/Delta**2;K=A-B
rows=[]
for dest,v in orders.items():
 same=dest[1][0]-dest[0][0]==dest[1][1]-dest[0][1]
 onsite=dest==((0,1),(1,0))
 if onsite:assert v[0]==8*g*g/Delta
 else:assert v[0]==0 and sum(v[1:])==(A if same else B)
 rows.append(dict(destination=dest,order16=str(v[0]),order18_energy=str(v[1]),order18_detour=str(v[2])))
source=[]
for R in (6,8,12):
 op={}
 for x in range(R):
  for y in range(R):
   phase=-(-1)**(x+y)
   for axis in ('X','Y'):
    for cols,sg in [(((x,y),((x+1)%R,(y+1)%R)),1),((((x+1)%R,y),(x,(y+1)%R)),-1)]:
     op[(axis,tuple(sorted(cols)))]=phase*sg
 rotated={('Y' if axis=='X' else 'X',tuple(sorted(((-y)%R,x) for x,y in cols))):v for (axis,cols),v in op.items()}
 reflected={(axis,tuple(sorted(((-x)%R,y) for x,y in cols))):v for (axis,cols),v in op.items()}
 assert rotated==op and reflected==op
 counts=[]
 for cols in ({(0,0),(1,1)},{(1,0),(0,1)}):
  counts.append(L*sum(((x,y) in cols)!=((x,(y+1)%R) in cols) for x in range(R) for y in range(R)))
 assert counts==[40,40]
 # X/Y collapse to the same pattern; normalization sqrt2 R and averaging2 cancel.
 norm=F(sum(v*v for (axis,cols),v in op.items() if axis=='X'),2*R*R)
 assert norm==1
 source.append(dict(R=R,norm=str(norm),reversed_bonds=counts,exact_C4=True,exact_axial_reflection=True,weight_coefficient=str(-F(L,4))))
assert len(q6)==1 and q6[tuple(sorted(c))]==2
assert A>0 and B<0 and K>0
print(json.dumps(dict(minimum_counts=dict(classes),q6_return=str(q6[tuple(sorted(c))]),paths=rows,A=str(A),B=str(B),K=str(K),K_float=float(K),source=source)))
