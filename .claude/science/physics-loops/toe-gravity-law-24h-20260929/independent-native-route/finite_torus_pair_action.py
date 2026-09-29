"""Direct two-hard-core-particle action on an 8^3 physical-site torus.

All amplitudes are Gaussian integers (integer real/imaginary pairs).  Work with
12 H at mu=1,gE=2,gT=1, so no floating point or spectral fitting occurs.
This is an author cross-check, not an independent review.
"""
from itertools import product
from collections import defaultdict
from pathlib import Path
import json

L=8
SITES=list(product(range(L),repeat=3))
ZERO=(0,0)
PHASE=((1,0),(0,1),(-1,0),(0,-1))
def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def scale(k,a):return (k*a[0],k*a[1])
def shift(x,i,t):return tuple((x[j]+(t if j==i else 0))%L for j in range(3))
def pair(a,b):return tuple(sorted((a,b)))
def shell(x):
 d=[pair(shift(x,i,1),shift(x,i,-1)) for i in range(3)]
 cols=[{d[0]:1,d[1]:-1},{d[0]:1,d[1]:1,d[2]:-2}]
 for i,j in ((0,1),(0,2),(1,2)):
  cols.append({pair(shift(x,i,a),shift(x,j,b)):a*b for a,b in product((-1,1),repeat=2)})
 return cols

COLS=[(x,shell(x)) for x in SITES]
WEIGHTS=(12,4,3,3,3)
def h12(v):
 out={p:scale(24,a) for p,a in v.items()}
 for x,cols in COLS:
  for weight,col in zip(WEIGHTS,cols):
   overlap=ZERO
   for p,c in col.items():overlap=plus(overlap,scale(c,v.get(p,ZERO)))
   for p,c in col.items():out[p]=plus(out.get(p,ZERO),scale(-weight*c,overlap))
 return {p:a for p,a in out.items() if a!=ZERO}

results=[]
# k lists momenta in units pi/2, including all different T Gram values 0,1,2.
for k in ((0,0,0),(1,0,0),(1,1,0),(1,1,1),(2,0,0)):
 cos=[(1,0,-1,0)[ki%4] for ki in k]
 eig=(0,0,1-cos[0]*cos[1],1-cos[0]*cos[2],1-cos[1]*cos[2])
 gram=(2,6,4*(1+cos[0]*cos[1]),4*(1+cos[0]*cos[2]),4*(1+cos[1]*cos[2]))
 for a in range(5):
  v={}
  for x,cols in COLS:
   phase=PHASE[sum(ki*xi for ki,xi in zip(k,x))%4]
   for p,c in cols[a].items():v[p]=plus(v.get(p,ZERO),scale(c,phase))
  v={p:z for p,z in v.items() if z!=ZERO}
  norm=sum(z[0]*z[0]+z[1]*z[1] for z in v.values())
  assert norm==len(SITES)*gram[a],(k,a,norm,gram[a])
  actual=h12(v)
  expected={p:scale(12*eig[a],z) for p,z in v.items() if eig[a]!=0}
  assert actual==expected,(k,a,actual,expected)
  results.append({'q_in_pi_over_2':k,'channel':a,'norm_squared':norm,
                  'energy_mu_units':eig[a] if norm else None,
                  'null_operator_state':not bool(norm),'exact_action_verified':True})
output={'torus_side':L,'physical_qubits':len(SITES),'coefficient_domain':'Gaussian integers',
        'operator':'12H at mu=1,gE=2,gT=1; exact hard-core pair action',
        'cases':results,'all_pass':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'torus_side':L,'physical_qubits':len(SITES),'cases':len(results),
                  'null_cases':sum(x['null_operator_state'] for x in results),'all_pass':True},indent=2))
print('TOTAL: PASS=25 FAIL=0 (exact Gaussian-integer torus action and norms)')
