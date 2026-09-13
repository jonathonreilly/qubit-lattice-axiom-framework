"""Direct bit-action native carrier versus a separate one-particle calculation."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,time
import sympy as s
HERE=Path(__file__).resolve().parent
EDGES=[(0,1),(0,3),(1,2),(1,4),(2,5),(3,4),(4,5)]
PROTECTED=[(0,3),(1,4),(2,5),(3,4),(4,5)]
def run():
 start=time.monotonic();checks=[]
 def eq(name,a,b):
  d=a-b
  if isinstance(d,s.MatrixBase):ok=all(s.simplify(x)==0 for x in d.todok().values())
  else:ok=s.simplify(d)==0
  assert ok,name
  checks.append(name)
 def check(name,ok):
  assert bool(ok),name
  checks.append(name)
 n=128;I=s.eye(n).as_immutable().as_mutable().todok()
 I=s.SparseMatrix(n,n,I)
 def diag(mask):return s.SparseMatrix(n,n,{(b,b):(-1)**((b&mask).bit_count()) for b in range(n)})
 Z={e:diag(1<<j) for j,e in enumerate(EDGES)}
 B={v:diag(sum(1<<j for j,e in enumerate(EDGES) if v in e)) for v in range(6)}
 A={}
 for j,(v,w) in enumerate(EDGES):
  mask=0
  for endpoint,other in ((v,w),(w,v)):
   for k,e in enumerate(EDGES):
    if endpoint in e:
     neighbor=e[1] if e[0]==endpoint else e[0]
     if neighbor<other:mask^=1<<k
  a=s.SparseMatrix(n,n,{(b^(1<<j),b):(-1)**((b&mask).bit_count()) for b in range(n)})
  A[v,w]=a;A[w,v]=-a
 def cycle(vs):
  q=I
  for v,w in zip(vs,vs[1:]+vs[:1]):q=q*A[v,w]
  return s.I**len(vs)*q
 S1=cycle([0,1,4,3]);S2=cycle([1,2,5,4])
 P=(I+S1)*(I+S2)/4
 eq('two_cycles_commute',S1*S2,S2*S1)
 eq('incoming_code_projector',P*P,P)
 eq('incoming_code_dimension',s.trace(P),32)
 for j,(S,e) in enumerate(((S1,(0,1)),(S2,(1,2)))):
  eq('cycle_anticommutes_record_'+str(j),S*Z[e]+Z[e]*S,s.zeros(n))
  eq('cycle_involution_'+str(j),S*S,I)
 T={e:s.I*A[e]*(B[e[0]]-B[e[1]])/2 for e in PROTECTED}
 J=-A[1,4]*(I-B[1]*B[4])/2
 H=sum(T.values(),s.zeros(n)).as_immutable()
 N=sum(((I-B[v])/2 for v in range(6)),s.zeros(n))
 eq('current_continuity_sign',J,-s.I*(H*(I-B[1])/2-(I-B[1])*H/2))
 eq('incident_parity_commutator',H*B[1]-B[1]*H,T[1,4]*B[1]-B[1]*T[1,4])
 eq('incident_current_square',J*J,(I-B[1]*B[4])/2)
 for e,hop in T.items():
  eq('hop_norm_certificate_'+str(e),hop*hop,(I-B[e[0]]*B[e[1]])/2)
  eq('number_conservation_'+str(e),N*hop,hop*N)
 occ=(I-B[0])/2
 for v in (2,3,5):occ=occ*(I+B[v])/2
 rho=P*occ*(I-J)/2
 eq('prepared_state_trace',s.trace(rho),1)
 eq('prepared_state_pure',rho*rho,rho)
 eq('prepared_state_hermitian',rho.H,rho)
 eq('prepared_state_code',P*rho,rho)
 eq('prepared_state_number_two',N*rho,2*rho)
 eq('prepared_parity_mean',s.trace(rho*B[1]),0)
 eq('prepared_current_mean',s.trace(rho*J),-1)
 eq('prepared_mean_energy',s.trace(rho*H),0)
 h=s.zeros(6)
 for v,w in PROTECTED:h[v,w]=h[w,v]=1
 e1=s.eye(6)[:,1];e4=s.eye(6)[:,4];e0=s.eye(6)[:,0]
 eq('cyclic_fourth_polynomial',(h**4-4*h*h+s.eye(6))*e1,s.zeros(6,1))
 eq('cyclic_first_image',h*e1,e4)
 eq('cyclic_third_image',h**3*e1,e0+s.eye(6)[:,2]+3*e4)
 roots=[2+s.sqrt(3),2-s.sqrt(3)]
 weights=[(s.sqrt(3)-1)/(2*s.sqrt(3)),(s.sqrt(3)+1)/(2*s.sqrt(3))]
 eq('spectral_weights_sum',sum(weights),1)
 eq('spectral_second_moment',sum(w*l for w,l in zip(weights,roots)),1)
 for k in (0,1,2,3,4,5):
  eq('spectral_moment_'+str(k),sum(w*l**k for w,l in zip(weights,roots)),(e1.T*h**(2*k)*e1)[0])
 color=s.diag(-1,1,-1,1,-1,1)
 eq('bipartite_hopping',color*h*color,-h)
 branch={}
 for z in (1,-1):
  Q=(I+z*Z[0,1])/2
  W=Q*(3*I+B[1]*Z[0,1]*S1)
  raw=W*rho*W.H/10
  eq('first_probability_'+str(z),s.trace(raw),s.Rational(1,2))
  state=2*raw
  eq('first_branch_parity_'+str(z),s.trace(state*B[1]),z*s.Rational(3,5))
  eq('first_branch_current_'+str(z),s.trace(state*J),-s.Rational(4,5))
  eq('first_branch_energy_'+str(z),s.trace(state*H),0)
  eq('first_branch_number_'+str(z),N*state,2*state)
  eq('first_Record_locked_'+str(z),Z[0,1]*state,z*state)
  eq('second_cycle_survives_'+str(z),S2*state,state)
  r=s.Rational(1,2) if z==1 else s.Integer(2)
  v=r*e1+s.I*e4
  C=e0*e0.T+v*v.H/(1+r*r)
  eq('CAR_postfilter_projector_'+str(z),C*C,C)
  eq('CAR_postfilter_current_'+str(z),2*s.im(C[1,4]),-s.Rational(4,5))
  eq('CAR_real_bipartite_covariance_'+str(z),color*s.conjugate(C)*color,C)
  rho_deriv=state;C_deriv=C
  for k in range(4):
   eq('native_CAR_parity_derivative_'+str((z,k)),s.trace(rho_deriv*B[1]),(1 if k==0 else 0)-2*C_deriv[1,1])
   eq('native_CAR_current_derivative_'+str((z,k)),s.trace(rho_deriv*J),2*s.im(C_deriv[1,4]))
   rho_deriv=-s.I*(H*rho_deriv-rho_deriv*H)
   C_deriv=-s.I*(h*C_deriv-C_deriv*h)
  for w in (1,-1):
   Q2=(I+w*Z[1,2])/2
   W2=Q2*(3*I+B[1]*Z[1,2]*S2)
   raw2=W2*state*W2.H/10
   prob=s.trace(raw2)
   eq('zero_dwell_second_probability_'+str((z,w)),prob,(1+w*z*s.Rational(9,25))/2)
   eq('second_old_Record_retained_'+str((z,w)),Z[0,1]*raw2,z*raw2)
   eq('second_new_Record_locked_'+str((z,w)),Z[1,2]*raw2,w*raw2)
   eq('second_number_retained_'+str((z,w)),N*raw2,2*raw2)
   eq('second_energy_zero_'+str((z,w)),s.trace(H*raw2),0)
   eq('second_selective_current_'+str((z,w)),s.trace(J*raw2)/prob,-s.Rational(16,25)/(1+w*z*s.Rational(9,25)))
  # Actual adjacent native-control/relay-qubit copy; pointer is highest bit.
  ptr0=s.diag(1,0);ptrz=ptr0 if z==1 else s.diag(0,1)
  control_bit=1<<EDGES.index((0,1))
  V=s.SparseMatrix(256,256,{(b^(128 if b&control_bit else 0),b):1 for b in range(256)})
  before=s.kronecker_product(ptr0,state)
  eq('physical_NN_projector_copy_'+str(z),V*before*V.H,s.kronecker_product(ptrz,state))
  branch[z]=C
 # A rational enclosure challenges the nonzero-dwell analytical estimates.
 u=s.Rational(1,40);order=10
 U=sum(((-s.I*u)**k*h**k/s.factorial(k) for k in range(order+1)),s.zeros(6))
 x=3*u
 rem=x**(order+1)/(s.factorial(order+1)*(1-x))
 covariance_error=(2+rem)*rem
 rows={}
 for z,C in branch.items():
  Ct=U*C*U.H
  q=s.Rational(4,5)-s.Rational(3,5)*s.re(Ct[1,1])
  j=2*s.im(Ct[1,4])
  qerr=s.Rational(3,5)*covariance_error
  jerr=2*covariance_error
  check('nonzero_dwell_current_bound_'+str(z),j+jerr<=-s.Rational(11,20))
  check('nonzero_dwell_probability_interior_'+str(z),q-qerr>s.Rational(1,5) and q+qerr<s.Rational(4,5))
  rows[str(z)]={'q_center':str(q),'q_error':str(qerr),'q_float':float(q),'current_center':str(j),'current_error':str(jerr),'current_float':float(j)}
 qp=s.Rational(rows['1']['q_center']);qm=s.Rational(rows['-1']['q_center'])
 qe=s.Rational(rows['1']['q_error'])
 check('nonzero_dwell_branch_gap',qp-qm-2*qe>=s.Rational(33,100))
 eq('analytic_probability_gap_bound',s.Rational(3,10)*(s.Rational(6,5)-4*u),s.Rational(33,100))
 eq('analytic_first_current_bound',-s.Rational(4,5)+10*u,-s.Rational(11,20))
 eq('analytic_final_current_bound',s.Rational(4,5)*(-s.Rational(11,20))/s.Rational(8,5),-s.Rational(11,40))
 return {'status':'pass','checks':checks,'total_pass':len(checks),'total_fail':0,'seconds':time.monotonic()-start,'nonzero_dwell_enclosures':rows,'Taylor_order':order,'unitary_remainder_bound':str(rem),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(HERE/'BLOCK01_NATIVE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
