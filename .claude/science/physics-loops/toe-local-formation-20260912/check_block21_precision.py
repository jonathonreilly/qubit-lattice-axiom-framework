"""Exact two-sector comparator for the written complete-instrument distance.
This does not implement a physical controller or a new native carrier.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
HERE=Path(__file__).resolve().parent
def run():
 start=time.monotonic();checks=[]
 def eq(name,a,b):
  d=a-b
  assert all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0,name
  checks.append(name)
 I=s.eye(2); B=s.diag(1,-1); psi=s.Matrix([1,1])/s.sqrt(2);rho=psi*psi.H
 angles=[(s.Integer(1),s.Integer(0)),(3/s.sqrt(10),1/s.sqrt(10)),(s.sqrt(3)/2,s.Rational(1,2)),(1/s.sqrt(2),1/s.sqrt(2))]
 for j,(c,d) in enumerate(angles):
  F={z:(c*I+z*d*B)/s.sqrt(2) for z in (1,-1)}
  eq('complete_'+str(j),sum((f.H*f for f in F.values()),s.zeros(2)),I)
  for k,(a,b) in enumerate(angles[:j]):
   G={z:(a*I+z*b*B)/s.sqrt(2) for z in (1,-1)}
   overlap=s.simplify(c*a+d*b)
   eq('coherent_overlap_'+str((j,k)),sum((F[z].H*G[z] for z in F),s.zeros(2)),overlap*I)
   for z in F:
    eq('balanced_outcome_'+str((j,k,z)),s.trace(F[z]*rho*F[z].H),s.Rational(1,2))
    delta=F[z]*rho*F[z].H-G[z]*rho*G[z].H
    eq('flagged_block_traceless_'+str((j,k,z)),s.trace(delta),0)
    eq('flagged_block_singular_values_'+str((j,k,z)),delta*delta,(1-overlap**2)*I/4)
 # Contrasts3/5 and1: full instrument distance squared equals2*(contrast error).
 c,d=angles[1];a,b=angles[-1]
 eq('projective_endpoint_square_root_error',4*(1-(c*a+d*b)**2),2*(1-2*c*d))
 # For the balanced input, outcome distributions coincide although poststates differ.
 F={z:(c*I+z*d*B)/s.sqrt(2) for z in (1,-1)}
 for z,f in F.items():
  eq('zero_outcome_TV_but_nonzero_instrument_'+str(z),s.trace(f*rho*f.H),s.Rational(1,2))
 assert s.simplify(4*(1-c*c))>0
 checks.append('probability_only_comparison_misses_positive_distance')
 return {'status':'pass','checks':checks,'total_pass':len(checks),'total_fail':0,'seconds':time.monotonic()-start,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 r=run();(HERE/'BLOCK21_INSTRUMENT_PRECISION_CHECKS.json').write_text(json.dumps(r,indent=2)+'\n')
 print(json.dumps(r,indent=2))
