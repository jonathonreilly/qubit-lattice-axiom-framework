from itertools import product
from collections import defaultdict
from pathlib import Path
import json

def add(out,vec,c=1):
 for b,v in vec.items():out[b]+=c*v

def fixture(Ly,Lz):
 shape=(4,Ly,Lz);sites=list(product(*(range(n) for n in shape)));idx={p:i for i,p in enumerate(sites)};edges=set()
 for p in sites:
  for axis in range(3):
   q=list(p);q[axis]=(q[axis]+1)%shape[axis];edges.add(tuple(sorted((idx[p],idx[tuple(q)]))))
 recmask=sum(1<<i for i,p in enumerate(sites) if p[0] in (0,2))
 def action(v):
  out=defaultdict(int)
  for b,c in v.items():
   for i,j in edges:
    if ((b>>i)&1)!=((b>>j)&1):
     out[b]-=2*c;out[b^(1<<i)^(1<<j)]+=2*c
  return {b:c for b,c in out.items() if c}
 def ss(a,b):
  out={}
  for x,signx in [(1,1),(3,-1)]:
   for xx,signxx in [(1,1),(3,-1)]:
    bits=(1<<idx[(x,*a)])|(1<<idx[(xx,*b)])
    out[bits]=signx*signxx
  return out
 def column(z,w):
  out=defaultdict(int)
  for y in range(Ly):add(out,ss((y,z),((y+2)%Ly,w)),(-1)**y)
  return {b:c for b,c in out.items() if c}
 B={(z,w):column(z,w) for z in range(Lz) for w in range(Lz)}
 for (z,w),v in B.items():
  assert sum(c*c for c in v.values())==4*Ly
  assert all(not(b&recmask) for b in v)
  rhs=defaultdict(int);add(rhs,v,-24)
  for zz,ww in [((z-1)%Lz,w),((z+1)%Lz,w),(z,(w-1)%Lz),(z,(w+1)%Lz)]:add(rhs,B[zz,ww],2)
  assert action(v)=={b:c for b,c in rhs.items() if c}
 keys=list(B)
 for i,k in enumerate(keys):
  for l in keys[i+1:]:assert sum(v*B[l].get(b,0) for b,v in B[k].items())==0
 # Nonstationarity: an image has support outside its original single column.
 assert any(action(B[0,0]).get(b,0) for b in B[1,0])
 # Initial boundary-dark product is NOT invariant: adjacent singlets excite records at second action.
 bad=ss((0,0),(1,0));hb=action(bad);hhb=action(hb)
 assert all(not(b&recmask) for b in hb)
 leak2=sum(c*c for b,c in hhb.items() if b&recmask)
 assert leak2>0
 return {'shape':shape,'vertices':len(sites),'edges':len(edges),'code_dimension':len(B),'column_norm_squared':4*Ly,'exact_full_spin_intertwining':True,'nonstationary_code':True,'adjacent_singlet_first_record_leakage':0,'adjacent_singlet_second_action_record_leakage_norm_squared_normalized':leak2/4}
results=[fixture(6,3),fixture(8,4),fixture(10,3)]
out={'method':'exact integer literal Pauli exchange and diagonal action, E0 subtracted only for computation, J=1','scope':'same-author controls; arbitrary-size statement rests on written proof','results':results}
Path(__file__).with_name('many_body_dark_result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
