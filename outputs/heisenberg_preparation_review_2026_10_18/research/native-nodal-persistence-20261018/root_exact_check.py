from itertools import product
from collections import defaultdict
import json
from pathlib import Path

def fixture(L):
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
rows=[fixture(L) for L in (4,6,8)]
result={'method':'exact integer full-spin SWAP action, independent of coordinate-Laplacian derivation','scope':'three finite torus fixtures; proof still needed for arbitrary sizes and common rotated record q','fixtures':rows}
Path(__file__).with_name('root_exact_result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
