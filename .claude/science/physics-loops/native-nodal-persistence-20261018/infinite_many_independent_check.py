from itertools import permutations,product
from collections import defaultdict
from math import factorial
from pathlib import Path
import json

def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def neighbors(v):
 for axis in range(3):
  for step in (-1,1):
   w=list(v);w[axis]+=step;yield tuple(w)
def seed(n):
 # Integer coefficients for product of x and y Slater determinants; all z=0.
 out={}
 for px,py,sgns in product(permutations(range(n)),permutations(range(n)),product((-1,1),repeat=n)):
  coords=tuple((sgns[k]*(px[k]+1),py[k],0) for k in range(n))
  out[coords]=sign(px)*sign(py)*(-1)**sum(s<0 for s in sgns)
 return out

def free(f):
 out=defaultdict(int)
 for coords,c in f.items():
  out[coords]+=12*len(coords)*c
  for i,v in enumerate(coords):
   for w in neighbors(v):
    dest=list(coords);dest[i]=w;out[tuple(dest)]-=2*c
 return {s:c for s,c in out.items() if c}
def physical(f):
 out=defaultdict(int)
 for config,c in f.items():
  occupied=set(config)
  for v in config:
   for w in neighbors(v):
    if w not in occupied:
     dest=tuple(sorted((occupied-{v})|{w}));out[config]+=2*c;out[dest]-=2*c
 return {s:c for s,c in out.items() if c}
def unordered(f):
 out={}
 for coords,c in f.items():
  assert len(set(coords))==len(coords)
  s=tuple(sorted(coords))
  assert s not in out or out[s]==c
  out[s]=c
 return out

def properties(f,n):
 for coords,c in f.items():
  assert all(v[0]!=0 for v in coords)
  assert len({v[0] for v in coords})==n and len({v[1] for v in coords})==n
  assert all(sum(abs(a-b) for a,b in zip(coords[i],coords[j]))!=1 for i in range(n) for j in range(i))
  # Individual x oddness and each coordinate's pair-exchange symmetry.
  for i in range(n):
   d=list(coords);v=list(d[i]);v[0]=-v[0];d[i]=tuple(v);assert f.get(tuple(d),0)==-c
  for i in range(n-1):
   for axis,expected in [(0,-c),(1,-c),(2,c)]:
    d=[list(v) for v in coords];d[i][axis],d[i+1][axis]=d[i+1][axis],d[i][axis]
    assert f.get(tuple(map(tuple,d)),0)==expected

results=[]
for n in (1,2,3):
 f=seed(n);p=unordered(f);normo=sum(c*c for c in f.values());normp=sum(c*c for c in p.values())
 assert normo==factorial(n)*normp
 assert normp==2**n*factorial(n)
 levels=[]
 for step in range(3):
  properties(f,n)
  assert unordered(f)==p
  levels.append({'power':step,'ordered_support':len(f),'physical_support':len(p)})
  if step<2:f,p=free(f),physical(p)
 # Nonzero motion changes z: original seed has all z=0.
 assert any(any(v[2]!=0 for v in coords) for coords in physical(unordered(seed(n))))
 results.append({'n':n,'ordered_seed_norm_squared':normo,'physical_integer_seed_norm_squared':normp,'checks':levels})
out={'method':'fresh independent exact integer ordered free action versus unordered full physical spin-exchange action on actual Z3, j=1; no finite torus','results':results,'scope':'finite-support controls through H^2; written proof carries all finite n and all times'}
Path(__file__).with_name('infinite_many_independent_result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
