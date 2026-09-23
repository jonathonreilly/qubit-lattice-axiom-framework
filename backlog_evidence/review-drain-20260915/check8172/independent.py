from fractions import Fraction as F
from itertools import product,combinations
from collections import Counter
import json,time,sys
start=time.monotonic()
axes=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def law(p,ns):
 w=[]
 for v in axes:
  counts=Counter(sum(a*b for a,b in zip(v,n)) for n in ns)
  w.append(p**counts[1]*F(2)**counts[0])
 z=sum(w);return [v/z for v in w]
def sens(p):
 worst=F(0);arg=None
 for b,c in product(axes,repeat=2):
  ks=[law(p,[a,b,c]) for a in axes]
  for i,j in combinations(range(6),2):
   # TV via positive subset mass, not half absolute sum
   d=sum(max(F(0),v-w) for v,w in zip(ks[i],ks[j]))
   if d>worst:worst,arg=d,(i,j,b,c)
 return str(3*worst),arg
r={'python':sys.version,'sensitivity':{str(p):sens(p) for p in [F(1,10),F(1),F(2),F(37,10),F(19,5)]}}
# Deviations computed from actual majority triples; no closed-form implementation.
for p in [285717,285718]:
 ds=[1-law(F(p),ns)[0] for ns in [[axes[0]]*3,[axes[0],axes[0],axes[1]],[axes[0],axes[0],axes[2]]]]
 r[str(p)]={'deviations':list(map(str,ds)),'threshold':max(ds)<=F(7,10**6)}
def region(I):
 D=sum(max(i[k] for i in I) for k in range(3));T=D+1
 Fwd=set()
 for i in I:
  for a in range(T+1):
   for b in range(T-a+1):Fwd.add((i[0]+a,i[1]+b,i[2]+T-a-b))
 U=set()
 for x in Fwd:
  for s in range(1,T+1):
   n=T-s
   for a in range(n+1):
    for b in range(n-a+1):U.add((x[0]-a,x[1]-b,x[2]-n+a+b))
 return D,U
r['regions']=[]
for I in [[(0,0,0)],[(100,-100,0)],[(0,0,0),(1,0,-1),(0,1,-1)],[(100,-100,0),(101,-100,-1),(100,-99,-1)]]:
 D,U=region(I);B=2*D+1
 clipped={y for y in U if -3*B-3<=y[0]<=B and -3*B-3<=y[1]<=B and y[2]<=B}
 r['regions'].append({'I':I,'D':D,'true_count':len(U),'original_box_count':len(clipped),'bound':18*(D+1)**3})
# Independently count forward paths by exhaustive strings (through t=8).
r['walk']=[]
import math
for t in range(9):
 C=Counter(tuple(s.count(k) for k in range(3)) for s in product(range(3),repeat=t))
 assert sum(C.values())==3**t
 assert all(n==math.factorial(t)//math.prod(math.factorial(x) for x in c) for c,n in C.items())
 r['walk'].append({'t':t,'paths':sum(C.values()),'sites':len(C)})
r['elapsed_seconds']=time.monotonic()-start
print(json.dumps(r,indent=2))
