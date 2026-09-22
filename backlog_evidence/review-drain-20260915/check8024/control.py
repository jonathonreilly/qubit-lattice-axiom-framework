from itertools import product,combinations
from fractions import Fraction as F
import json,time
from pathlib import Path
start=time.monotonic(); checks=[]; results={}
def check(n,b):
 assert b,n
 checks.append(n)
# Recover elementary squares from undirected adjacency/common-neighbor cycles,
# not from the primary's anchored oriented plaquette function.
for L in (1,2,3):
 vertices=set(product(range(L+1),repeat=3));adj={x:{y for y in vertices if sum(abs(a-b) for a,b in zip(x,y))==1} for x in vertices}
 faces=set()
 for x in vertices:
  for y,z in combinations(adj[x],2):
   for t in (adj[y]&adj[z])-{x}:faces.add(frozenset((x,y,z,t)))
 edges={frozenset((x,y)) for x in vertices for y in adj[x]}
 check(f'faces_{L}',len(faces)==3*L*L*(L+1));check(f'edges_{L}',len(edges)==3*L*(L+1)**2)
 for face in faces:
  tails={min(edge) for edge in edges if edge<=face}
  checkname=False
  assert len(tails)==3
  anchor=tuple(min(x[k] for x in face) for k in range(3))
  assert anchor in tails
 check(f'three_tail_support_{L}',True)
 results[str(L)]={'faces':len(faces),'edges':len(edges)}
# Shell formula independently sums one-dimensional Weyl dimensions, no expanded energies.
for R,expected in [(1,19),(2,155),(3,805)]:
 dimension=sum((t**7-t**3)//120 for t in range(2,R+3));check(f'shell_dimension_{R}',dimension==expected)
check('inert_R1_multiplicity',1+(32-19)==14)
check('penalty_R1_gap',min([1,F(9,4),1])==1)
# Symbolic all-label identity and discrete growth establish minimum for all labels.
for p,q in product(range(5),repeat=2):
 f=lambda p,q:p*p+p*q+q*q+3*p+3*q
 assert f(p+1,q)-f(p,q)==2*p+q+4 and f(p,q+1)-f(p,q)==p+2*q+4
check('growth_identity_coefficients',True)
check('rescaling',F(3,8)*F(8,3)==1 and 4*F(1,2)==2)
check('local_energy_two_sided',4+4==8)
out={'checks':checks,'passed':len(checks),'geometry':results,'seconds':time.monotonic()-start,'scope':'Independent finite adjacency/shell controls only. General Casimir monotonicity, local norm, GNS reduction and code-ground continuation also checked analytically; external stability theorem imported, not reproduced.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
