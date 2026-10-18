from itertools import permutations,product
from collections import defaultdict
from pathlib import Path
from math import factorial
import json

def clean(d):return {k:v for k,v in d.items() if v}
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def seed(n):
 # Ordered coordinate determinants, all z=0. No wavefunction interpolation.
 d={}
 for xp in permutations(range(1,n+1)):
  for yp in permutations(range(n)):
   for signs in product((-1,1),repeat=n):
    sites=tuple((xp[i]*signs[i],yp[i],0) for i in range(n))
    sign=parity(xp)*parity(yp)
    for s in signs:sign*=s
    d[sites]=sign
 return d

def free(f):
 o=defaultdict(int)
 for positions,c in f.items():
  o[positions]+=12*len(positions)*c
  for i in range(len(positions)):
   for axis,step in product(range(3),(-1,1)):
    p=list(positions);v=list(p[i]);v[axis]+=step;p[i]=tuple(v);o[tuple(p)]-=2*c
 return clean(o)
def physical(f):return {p:c for p,c in f.items() if tuple(sorted(p))==p and len(set(p))==len(p)}
def actual(f):
 o=defaultdict(int)
 for positions,c in f.items():
  for i in range(len(positions)):
   for axis,step in product(range(3),(-1,1)):
    p=list(positions);v=list(p[i]);v[axis]+=step;v=tuple(v)
    if v in positions:continue
    p[i]=v;o[positions]+=2*c;o[tuple(sorted(p))]-=2*c
 return clean(o)
def nodes(f):
 for p in f:
  assert all(v[0]!=0 for v in p)
  assert len(set(v[0] for v in p))==len(p)
  assert len(set(v[1] for v in p))==len(p)
rows=[]
for n in (1,2,3):
 f=seed(n);nodes(f);g=free(f);nodes(g);gg=free(g);nodes(gg)
 assert all(f.get(tuple(reversed(p)))==c for p,c in f.items())
 assert actual(physical(f))==physical(g)
 assert actual(actual(physical(f)))==physical(gg)
 assert len(physical(f))==2**n*factorial(n)
 rows.append({'n':n,'ordered_seed_terms':len(f),'physical_seed_terms':len(physical(f)),'physical_second_action_terms':len(physical(gg)),'exact_intertwining_two_actions':True})
result={'fixtures':rows,'method':'ordered coordinate determinants versus independent unordered hard-core full spin action on actual Z3; exact integers','scope':'n=1,2,3 finite-support witnesses, no finite-volume boundary'}
Path(__file__).with_name('infinite_n_root_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
