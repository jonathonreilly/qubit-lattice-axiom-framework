from itertools import product
from collections import defaultdict
from pathlib import Path
import json

def check(Ly,Lz):
 vertices=list(product(range(4),range(Ly),range(Lz)));idx={v:i for i,v in enumerate(vertices)};edges=set()
 for v in vertices:
  for a,n in enumerate((4,Ly,Lz)):
   w=list(v);w[a]=(w[a]+1)%n;edges.add(tuple(sorted((idx[v],idx[tuple(w)]))))
 plane=sum(1<<i for i,v in enumerate(vertices) if v[0] in(0,2))
 def H(f):
  out=defaultdict(int)
  for S,c in f.items():
   for a,b in edges:
    if ((S>>a)^(S>>b))&1:out[S]+=2*c;out[S^(1<<a)^(1<<b)]-=2*c
  return {s:c for s,c in out.items() if c}
 def V(z1,z2,stagger=True):
  out=defaultdict(int)
  for y in range(Ly):
   for x1,x2 in product((1,3),repeat=2):
    S=(1<<idx[x1,y,z1])|(1<<idx[x2,(y+2)%Ly,z2]);c=(-1 if x1==3 else 1)*(-1 if x2==3 else 1)
    if stagger:c*=(-1)**y
    out[S]+=c
  return {s:c for s,c in out.items() if c}
 cols=[V(a,b) for a,b in product(range(Lz),repeat=2)]
 for i,v in enumerate(cols):
  assert sum(c*c for c in v.values())==4*Ly
  for u in cols[:i]:assert sum(c*u.get(s,0) for s,c in v.items())==0
 for z1,z2 in product(range(Lz),repeat=2):
  target=defaultdict(int)
  for s,c in V(z1,z2).items():target[s]+=24*c
  for step in(-1,1):
   for w in(V((z1+step)%Lz,z2),V(z1,(z2+step)%Lz)):
    for s,c in w.items():target[s]-=2*c
  target={s:c for s,c in target.items() if c}
  assert H(V(z1,z2))==target,(Ly,Lz,z1,z2)
  assert all(not s&plane for s in target)
 # Wrong phase has an initially dark boundary but its next full-H image exits this prescribed code.
 bad=V(0,0,False);hb=H(bad)
 assert any(hb.get(s,0) for s in hb if s not in bad)
 # Compare against same claimed effective equation to ensure selected transverse phase is load-bearing.
 wrong_target=defaultdict(int)
 for s,c in bad.items():wrong_target[s]+=24*c
 for step in(-1,1):
  for w in(V(step%Lz,0,False),V(0,step%Lz,False)):
   for s,c in w.items():wrong_target[s]-=2*c
 wrong_target={s:c for s,c in wrong_target.items() if c}
 assert hb!=wrong_target
 # Adjacent mirror singlets: first action has no plane excitation, second does.
 adjacent={}
 for x1,x2 in product((1,3),repeat=2):
  S=(1<<idx[x1,0,0])|(1<<idx[x2,1,0])
  adjacent[S]=(-1 if x1==3 else 1)*(-1 if x2==3 else 1)
 first=H(adjacent);second=H(first)
 assert sum(c*c for S,c in first.items() if S&plane)==0
 second_leak=sum(c*c for S,c in second.items() if S&plane)/4
 assert second_leak==256
 return {'adjacent_second_action_leak_squared':second_leak,'shape':[4,Ly,Lz],'edges':len(edges),'independent_columns':len(cols),'integer_intertwining_verified':True,'unstaggered_control_rejected':True}
result={'method':'independently written full-spin exchange action and exact encoded target comparison','fixtures':[check(6,3),check(8,4),check(10,3)]}
Path(__file__).with_name('root_two_particle_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
