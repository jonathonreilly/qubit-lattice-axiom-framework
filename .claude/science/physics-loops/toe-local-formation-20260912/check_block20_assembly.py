"""Exact small code/fuel comparator for the conditional assembly identities.

This realizes the cycle anticommutation algebra on a separate two-level
factor; it is not a second literal native spatial embedding. That embedding
and its code identities are the pinned input of the written assembly proof.
"""
from pathlib import Path
import hashlib,json,time
import sympy as s
HERE=Path(__file__).resolve().parent
AUDIT_TIMEOUT_SEC=180

def run():
 start=time.monotonic();checks=[]
 def eq(name,a,b):
  d=a-b
  assert all(s.simplify(x)==0 for x in d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0,name
  checks.append(name)
 I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
 zero=s.diag(1,0);one=s.diag(0,1);lower=s.Matrix([[0,1],[0,0]])
 kron=s.kronecker_product
 eye=s.eye(4);S=kron(I,Z);R=kron(I,X);B=kron(Z,I);H=kron(X,I)
 P=kron(I,zero);eta=s.Rational(4,5);kappa=s.Rational(3,5);gamma=s.Rational(3,2)
 U=(3*eye+B*R*S)/s.sqrt(10)
 K={z:(eye+z*R)*U/2 for z in (1,-1)}
 eq('full_pulse_unitary',U.H*U,eye)
 eq('complete_full_physical_instrument',sum((k.H*k for k in K.values()),s.zeros(4)),eye)
 L={z:s.sqrt(gamma)*kron(k,lower) for z,k in K.items()}
 fuel=kron(eye,one);fullH=kron(H,I);fullP=kron(P,I)
 loss=sum((l.H*l for l in L.values()),s.zeros(8))
 eq('full_fuel_loss_identity',loss,gamma*fuel)
 dualH=sum((l.H*fullH*l for l in L.values()),s.zeros(8))-(loss*fullH+fullH*loss)/2
 target=-gamma*(1-eta)*kron(H,one)
 eq('compressed_mean_energy_generator',fullP*dualH*fullP,fullP*target*fullP)
 assert dualH!=target,'full_carrier_cross_term_must_not_be_discarded'
 checks.append('full_carrier_cross_term_retained')
 rho=(I+X/2+Y/3+Z/7)/2
 state=kron(rho,zero,one)
 eq('mean_energy_rate_on_ready_state',s.trace(state*dualH),-s.Rational(3,20))
 eq('matter_independent_total_jump_rate',s.trace(state*loss),gamma)
 for z,l in L.items():
  eq('native_mark_rate_'+str(z),s.trace(l*state*l.H),gamma*(1+z*kappa/s.Integer(7))/2)
  eq('fuel_absorbs_after_jump_'+str(z),fuel*l,s.zeros(8))
  eq('physical_Record_after_jump_'+str(z),kron(R,I)*l,z*l)
  for w,other in L.items():eq('no_second_jump_'+str((z,w)),other*l,s.zeros(8))
 eq('Record_retention_under_dwell',kron(R,I)*fullH,fullH*kron(R,I))
 q=s.Rational(1,5)
 M0=kron(eye,zero+s.sqrt(1-q)*one)
 M=[M0]+[s.sqrt(q)*kron(k,lower) for k in K.values()]
 eq('finite_collision_completeness',sum((m.H*m for m in M),s.zeros(8)),s.eye(8))
 eq('finite_collision_fuel_probability',s.trace(sum((m*state*m.H for m in M),s.zeros(8))*fuel),1-q)
 out=sum((m*state*m.H for m in M),s.zeros(8))
 eq('finite_collision_mean_energy',s.trace((out-state)*fullH),-q*(1-eta)/2)
 return {'status':'pass','checks':checks,'total_pass':len(checks),'total_fail':0,'seconds':time.monotonic()-start,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
 result=run();(HERE/'BLOCK20_ASSEMBLY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2));print(f"TOTAL: PASS={result['total_pass']} FAIL=0")
