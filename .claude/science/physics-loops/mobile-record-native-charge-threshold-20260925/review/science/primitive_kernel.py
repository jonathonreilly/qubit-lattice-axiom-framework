"""Own flat Gram-column primitives. No I/O or author imports at import time."""
from collections import Counter
from functools import lru_cache
from itertools import combinations
STEPS=tuple(tuple(s if i==j else 0 for i in range(3)) for j in range(3) for s in (-1,1))
@lru_cache(None)
def neighbors(x,L=None):
 out={tuple((a+b)%L if L else a+b for a,b in zip(x,v)) for v in STEPS}
 return tuple(sorted(out))
@lru_cache(None)
def active_pairs(x,L=None):
 pairs=set()
 for a in neighbors(x,L):
  for b in neighbors(a,L):
   for c in neighbors(b,L):
    if a!=c:pairs.add(tuple(sorted((a,c))))
 return frozenset(pairs)
@lru_cache(None)
def add_kernel(pair,L=None):
 a,c=pair
 return Counter(tuple(sorted((u,v))) for u in neighbors(a,L) for v in neighbors(c,L) if u!=v)
def column(occupied,L=None):
 """Q_I minus vacuum, Q_I=-H4=2 sum pair Grams; X can be algebraic odd."""
 occupied=tuple(sorted(occupied));occ=set(occupied)
 relevant=set().union(*(active_pairs(x,L) for x in occupied))
 result=Counter();vacuum=0
 for pair in sorted(relevant):
  kernel=add_kernel(pair,L)
  vacuum+=2*sum(k*k for k in kernel.values())
  for addition,w in kernel.items():
   if occ.isdisjoint(addition):
    mid=occ.union(addition)
    for removal in combinations(sorted(mid),2):
     v=kernel.get(removal,0)
     if v:result[tuple(sorted(mid.difference(removal)))]+=2*w*v
 result[occupied]-=vacuum
 return {k:v for k,v in sorted(result.items()) if v}
def ordered_path_column(occupied,L=None):
 """Different bounded check: four ordered moves, without unordered kernel."""
 occupied=tuple(sorted(occupied));occ=set(occupied);result=Counter();vacuum=0
 for a,c in sorted(set().union(*(active_pairs(x,L) for x in occupied))):
  na,nc=neighbors(a,L),neighbors(c,L)
  # Empty input forward/return norm is counted by primitive ordered paths.
  vac=0
  for u in na:
   for v in nc:
    if u==v:continue
    for uu in na:
     for vv in nc:
      if uu!=vv and {u,v}=={uu,vv}:vac+=2
    if u in occ or v in occ:continue
    intermediate=occ|{u,v}
    for back_c in nc:
     if back_c not in intermediate:continue
     after_c=intermediate-{back_c}
     for back_a in na:
      if back_a in after_c:result[tuple(sorted(after_c-{back_a}))]+=2
  vacuum+=vac
 result[occupied]-=vacuum
 return {k:v for k,v in sorted(result.items()) if v}
def relative_type(x,y,L=None):
 d=tuple(b-a for a,b in zip(x,y))
 if L:d=tuple(min(v%L,(-v)%L) for v in d)
 return tuple(sorted(map(abs,d)))
def relative_column(occupied,L=None):
 out=Counter()
 for final,w in column(occupied,L).items():
  d=tuple((b-a)%L if L else b-a for a,b in zip(final[0],final[1]))
  opposite=tuple((-v)%L if L else -v for v in d)
  out[min(d,opposite)]+=w
 return {k:v for k,v in sorted(out.items()) if v}
