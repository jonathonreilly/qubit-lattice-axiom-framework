AUDIT_TIMEOUT_SEC=120 # Executed only under the enforced owning primary aggregate timer.
"""Exact finite full-spin controls; general proofs are in the source note."""
from itertools import product
from collections import defaultdict
import json
from pathlib import Path

def one_particle_fixture(L):
 xyz=list(product(range(L),range(3),range(3)));idx={v:i for i,v in enumerate(xyz)}
 edges=set()
 for v in xyz:
  for a,n in enumerate((L,3,3)):
   w=list(v);w[a]=(w[a]+1)%n
   edges.add(tuple(sorted((idx[v],idx[tuple(w)]))))
 def reflect(mask):
  return sum(1<<idx[((-x)%L,y,z)] for i,(x,y,z) in enumerate(xyz) if mask>>i&1)
 def H(vector):
  # Full spin exchange H=sum_e 2(I-SWAP_e), exact integer arithmetic.
  out=defaultdict(int)
  for mask,c in vector.items():
   for i,j in edges:
    if ((mask>>i)^(mask>>j))&1:
     out[mask]+=2*c;out[mask^(1<<i)^(1<<j)]-=2*c
  return {m:c for m,c in out.items() if c}
 def V(v):
  m=1<<idx[v];return {m:1,reflect(m):-1}
 plane=sum(1<<i for i,v in enumerate(xyz) if v[0] in (0,L//2))
 tested=0
 for v in xyz:
  if not 0<v[0]<L//2:continue
  actual=H(V(v));expected=defaultdict(int)
  for m,c in V(v).items():expected[m]+=12*c
  for a,n in enumerate((L,3,3)):
   for step in (-1,1):
    w=list(v);w[a]=(w[a]+step)%n;w=tuple(w)
    if not 0<w[0]<L//2:continue
    for m,c in V(w).items():expected[m]-=2*c
  expected={m:c for m,c in expected.items() if c}
  assert actual==expected,(L,v)
  assert all(not m&plane for m in actual)
  tested+=1
 u=idx[(1,0,0)];v=idx[(1,1,0)];m=(1<<u)|(1<<v);two={m:1,reflect(m):-1}
 assert all(not m&plane for m in two)
 leakage={m:c for m,c in H(two).items() if m&plane}
 assert leakage
 return {'shape':[L,3,3],'sites':len(xyz),'edges':len(edges),'one_excitation_columns_checked':tested,'normalized_two_excitation_leakage_square':sum(c*c for c in leakage.values())/2,'two_excitation_nonzero_leaked_configurations':len(leakage),'vacuum_H_zero':H({0:1})=={}}

from itertools import product
from collections import defaultdict
from pathlib import Path
import json

def two_particle_fixture(Ly,Lz):
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
