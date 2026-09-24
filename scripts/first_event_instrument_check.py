"""Exact finite cube Gram and recovery controls for the conditional first mark.
The all-graph argument uses orthogonal destinations and unit rotor shifts;
this is a finite control, not a physical inverse of permanent formation.
"""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/first_event_instrument_check.py',)
from itertools import product
from pathlib import Path
import json
import sympy as s

def main():
 vertices=list(product((0,1),repeat=3));vi={x:i for i,x in enumerate(vertices)}
 edges=[]
 for x in vertices:
  for k in range(3):
   if x[k]==0:
    y=list(x);y[k]=1;edges.append((vi[x],vi[tuple(y)]))
 A={i for i,x in enumerate(vertices) if sum(x)%2==0};bg=tuple(int(i in A) for i in range(8))
 D=s.zeros(8,12)
 for e,(a,b) in enumerate(edges):D[a,e]=1;D[b,e]=-1
 cycles=D.nullspace();assert len(cycles)==5
 fields=[(0,)*12]+[tuple(int(sign*z) for z in c) for c in cycles for sign in (-1,1)]
 assert len(set(fields))==11 and all(D*s.Matrix(f)==s.zeros(8,1) for f in fields)
 rows=[]
 for e,(x,y) in enumerate(edges):
  a=x if x in A else y
  b=y if a==x else x
  neighbors=[(f,v if u==a else u,1 if u==a else -1) for f,(u,v) in enumerate(edges) if a in (u,v) and f!=e]
  assert len(neighbors)==2
  for kind in ('resolved_minus','resolved_plus','coherent'):
   signs=(-1,) if kind=='resolved_minus' else (1,) if kind=='resolved_plus' else (-1,1)
   outputs=[]
   for field in fields:
    col={}
    for hop,dest,orientation in neighbors:
     for charge in signs:
      q=list(bg);q[a]=0;q[dest]=1;q[x]=charge;q[y]=-charge
      ff=list(field);ff[hop]-=orientation;ff[e]+=charge
      state=(tuple(q),tuple(ff));assert state not in col
      assert D*s.Matrix(ff)+s.Matrix(bg)-s.Matrix(q)==s.zeros(8,1)
      assert sum(z!=0 for z in q)==6
      col[state]=1
    outputs.append(col)
   allout=sorted({state for col in outputs for state in col});oi={z:i for i,z in enumerate(allout)}
   B=s.zeros(len(allout),len(fields))
   for j,col in enumerate(outputs):
    for z,v in col.items():B[oi[z],j]=v
   coeff=2*len(signs)
   assert B.T*B==coeff*s.eye(11)
   # Recovery on the known image: normalized isometry adjoint recovers each
   # matrix unit, including coherences between different circulation inputs.
   for i in range(11):
    for j in range(11):
     X=s.zeros(11);X[i,j]=1
     assert B.T*(B*X*B.T)*B==coeff**2*X
   rows.append({'edge':e,'instrument':kind,'input_dimension':11,'output_dimension':len(allout),'Gram_coefficient':coeff,'matrix_units_checked':121})
 # Degree zero/one has no other destination and zero rate; do not divide by it.
 assert 2*0*(0-1)==0 and 2*1*(1-1)==0
 out={'status':'PASS','cube_edges':12,'controls':rows,'zero_rate_normalization':'No normalized mark law when total rate is zero','scope':'Exact finite circulation-basis Gram and logical image-recovery identities; no physical record-reversal operation asserted.'}
 Path(__file__).with_name('FIRST_EVENT_INSTRUMENT_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
 print('TOTAL: PASS=37 FAIL=0')
if __name__=='__main__':main()
