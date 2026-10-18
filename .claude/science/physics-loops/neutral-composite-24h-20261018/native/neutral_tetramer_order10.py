from fractions import Fraction as F
from neutral_tetramer_geometry import count,syn
import json
def norm(S):
 x=min(x for x,y in S);y=min(y for x,y in S)
 return tuple(sorted((a-x,b-y) for a,b in S))
def orbit(S):
 out=set()
 for flip in [0,1]:
  for rot in range(4):
   A=set(S)
   if flip:A={(x,-y) for x,y in A}
   for _ in range(rot):A={(-y,x) for x,y in A}
   out.add(norm(A))
 return out
def per(S):return sum((x+dx,y+dy) not in S for x,y in S for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
def turns(S):
 corners={(x+dx,y+dy) for x,y in S for dx,dy in [(0,0),(1,0),(0,1),(1,1)]}
 return sum(sum((x-dx,y-dy) in S for dx,dy in [(0,0),(1,0),(0,1),(1,1)]) in [1,3] for x,y in corners)
A=syn({(0,0),(1,0),(4,0),(5,0)});B=syn({(0,0),(1,0),(0,3),(1,3)})
shapes={((0,0),)};allshapes=set()
for n in range(2,7):
 nex=set()
 for S in shapes:
  for x,y in S:
   for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:nex.add(norm(set(S)|{(x+dx,y+dy)}))
 shapes={s for s in nex if len(s)==n}
 allshapes|={min(orbit(s)) for s in shapes if per(set(s))==10}
rows=[];split=F(0)
for S in sorted(allshapes):
 m=turns(set(S));coef={4:F(-143,33554432),6:F(55,33554432),8:F(-35,33554432)}[m]
 ca=sum(count(A,p) for p in orbit(S));cb=sum(count(B,p) for p in orbit(S));difference=-2*coef*(cb-ca);split+=difference
 rows.append(dict(shape=S,turns=m,orientations=len(orbit(S)),countA=ca,countB=cb,BminusA=str(difference)))
extra=[]
for S in [{(0,0),(2,0)},{(0,0),(2,1)},{(0,0),(1,0),(2,1)}]:
 extra.append(dict(shape=sorted(S),orientations=len(orbit(S)),countA=sum(count(A,p) for p in orbit(S)),countB=sum(count(B,p) for p in orbit(S))))
delta=split-16*F(331,226492416)+8*F(75101,97844723712)
assert delta==F(949685,12230590464)
print(json.dumps(dict(primitive=rows,primitive_BminusA=str(split),other_new_invariants=extra,full_BminusA=str(delta)),indent=2))
