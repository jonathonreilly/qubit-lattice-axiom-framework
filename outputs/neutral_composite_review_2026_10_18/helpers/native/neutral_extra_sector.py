"""Exact signed-orbit reduction for two independent commuting Pauli flips."""
import itertools,numpy as np

def mul(a,b):
 f,z,c=a;g,w,d=b
 return f^g,z^w,c*d*(-1)**((z&g).bit_count())
def reducer(n,stabs,signs):
 assert len(stabs)==2
 for t in stabs:assert mul(t,t)==(0,0,1)
 assert mul(*stabs)==mul(*stabs[::-1])
 groups=[((0,0,1),1), (stabs[0],signs[0]),(stabs[1],signs[1]),(mul(*stabs),signs[0]*signs[1])]
 piv=next((a,b) for a,b in itertools.combinations(range(n),2) if len({((t[0]>>a)&1,(t[0]>>b)&1) for t,s in groups})==4)
 free=[i for i in range(n) if i not in piv]
 def compress(x):return sum(((x>>f)&1)<<i for i,f in enumerate(free))
 def expand(x):return sum(((x>>i)&1)<<f for i,f in enumerate(free))
 def reduce(t):
  f,z,c=t
  for st in stabs:assert mul(t,st)==mul(st,t)
  (g,w,d),sign=next((t,s) for t,s in groups if all(((t[0]^f)>>p)&1==0 for p in piv))
  cf=f^g
  return compress(cf),compress(z^w),c*d*sign*(-1)**((z&g).bit_count())
 def vector(j):
  r=expand(j);return {r^f:sign*c*(-1)**((z&r).bit_count()) for (f,z,c),sign in groups}
 return dict(reduce=reduce,vector=vector,expand=expand,free=free,dimension=1<<len(free),pivots=piv)
