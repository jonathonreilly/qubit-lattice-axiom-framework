"""Mixed local-energy/composite hierarchy, exact integer K=1 algebra.
E0=2e0/K is an integer Pauli sum. Divide mixed results by2 for e0 at K=1.
"""
from collections import defaultdict
from pathlib import Path
import json
from compass_local_transport import shift,word,derivative
P=Path(__file__).resolve().parent
def groups(A):
 g=defaultdict(list)
 for w,c in A.items():
  p=w[0][:3];key=tuple((*tuple(v[j]-p[j] for j in range(3)),v[3]) for v in w);g[key].append((p,c))
 return g
def cross(A,B):
 a=groups(A);b=groups(B);out=defaultdict(int)
 for k,rows in a.items():
  for x,c in rows:
   for y,d in b.get(k,[]):out[tuple(x[j]-y[j] for j in range(3))]+=c*d
 return {r:v for r,v in out.items() if v}
C={word([(shift((0,0,0),a,-1),a),(shift((0,0,0),a,1),a)]):1 for a in range(3)}
E={word([((0,0,0),a),(shift((0,0,0),a,s),a)]):1 for a in range(3) for s in [-1,1]}
rows=[]
for n in range(5):
 cr=cross(C,E)
 row=dict(order=n,composite_terms=len(C),energy_terms=len(E),overlaps=[dict(displacement=r,value=v) for r,v in sorted(cr.items())],sum_over_displacements=sum(cr.values()))
 assert sum(cr.values())==0
 rows.append(row);print(row,flush=True)
 (P/'compass_energy_bridge.json').write_text(json.dumps(dict(scope='Mixed HS correlations; not an inferred physical source coupling',rows=rows),indent=2)+'\n')
 if n<4:C=derivative(C);E=derivative(E)
