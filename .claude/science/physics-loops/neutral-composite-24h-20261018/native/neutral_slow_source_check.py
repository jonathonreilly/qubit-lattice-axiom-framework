import sys,json,math
from collections import defaultdict
from pathlib import Path
exec(Path(__file__).with_name('neutral_bulk_source_check.py').read_text().split('d=E(1);reps=[]')[0])

def first(v):
 out=defaultdict(float)
 for s,a in v.items():
  for m,t in edges:
   dest=s^m
   if energy(dest)!=8:out[dest]+=a*(-1 if t=='X' else (-1)**((s&m).bit_count()))
 return {s:a for s,a in out.items() if abs(a)>1e-13}
def bil(a,b):return sum(v*b.get(s,0)/(8-energy(s)) for s,v in a.items())
Ax=add((1/math.sqrt(2),orbit(2,0,2)),(1/math.sqrt(2),orbit(0,2,2)))
D=add((1/math.sqrt(2),orbit(1,1,2)),(1/math.sqrt(2),orbit(1,-1,2)))
d2=add((1/math.sqrt(2),orbit(2,0,1)),(-1/math.sqrt(2),orbit(0,2,1)))
fa,fd,fe,fb=map(first,[Ax,D,E(2),d2])
vals={'A_to_e':bil(fa,fe),'A_to_d2':bil(fa,fb),'D_to_e':bil(fd,fe),'D_to_d2':bil(fd,fb)}
assert max(abs(vals[k]-v) for k,v in [('A_to_e',-1),('A_to_d2',-1),('D_to_e',-2),('D_to_d2',0)])<1e-10
# Direct two-edge support from vacuum: no slow four-spin mask is an xor of two native edge masks.
masks={m for m,t in edges}
for target in list(Ax)+list(D):assert not any((target^m) in masks for m in masks)
vals['direct_second_order_source_support_absent']=True
Path(__file__).with_suffix('.json').write_text(json.dumps(vals,indent=2));print(vals)
