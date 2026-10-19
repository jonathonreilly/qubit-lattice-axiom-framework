import sys,itertools,numpy as np
from collections import defaultdict
sys.path.insert(0,'/private/tmp')
from neutral_cube_model import sector
rng=np.random.default_rng(2718)
def applyword(s,o):
 x,z,p=o;return s^x,p*(-1)**((s&z).bit_count())
def orbit(s,gens):
 out={s:1.}
 for g in gens:
  nxt=dict(out)
  for a,c in out.items():
   b,p=applyword(a,g);nxt[b]=nxt.get(b,0)+c*p
  out=nxt
 norm=sum(c*c for c in out.values())**.5
 return {a:c/norm for a,c in out.items() if c}
for k in range(4):
 d=sector(3,tuple(a<k for a in range(3)))
 def W(j):
  s=d['offset']
  for i,v in enumerate(d['vectors']):
   if j>>i&1:s^=v
  return orbit(s,d['all_generators'][3:])
 for label,physical,logical in [('H',sum(d['physical_H'],[]),sum(d['H'],[])),('S',d['physical_S'],d['S'])]:
  err=0.
  for _ in range(8):
   j=int(rng.integers(d['dim']));left=defaultdict(float);right=defaultdict(float)
   for s,c in W(j).items():
    for o in physical:
     b,p=applyword(s,o);left[b]+=c*p
   for o in logical:
    b,p=applyword(j,o)
    for s,c in W(b).items():right[s]+=c*p
   err=max(err,max(abs(left[s]-right[s]) for s in left.keys()|right.keys()))
  print(k,label,err)
