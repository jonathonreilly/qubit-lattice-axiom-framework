#!/usr/bin/env python3
"""Fresh primitive cube paths and finite QFI/conserving-swap checks; no repo imports."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import json
import numpy as np
A=(0,3,5,6);B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if (a^b).bit_count()==1)
OMEGA=(tuple(int(v in A) for v in range(8)),(0,)*12)
transitions=[]
def clean(v):return {k:x for k,x in v.items() if x}
def apply(v,operation):
 out=defaultdict(Fraction)
 for state,c in v.items():
  for new,weight in operation(state):out[new]+=c*weight
 return clean(out)
def hops(state,inward=False,center=None):
 q,E=state
 for e,(a,b) in enumerate(EDGES):
  if center is not None and a!=center:continue
  source,target=(b,a) if inward else (a,b)
  if not q[source] or q[target]:continue
  s=q[source];step=s if inward else -s
  qq=list(q);ee=list(E);qq[target]=s;qq[source]=0;ee[e]+=step
  transitions.append((E[e],step))
  yield (tuple(qq),tuple(ee)),Fraction(1)
def F(v):return apply(v,lambda x:hops(x))
def Ft(v):return apply(v,lambda x:hops(x,True))
def mark(v,signs):
 def op(state):
  q,E=state
  if q[0] or q[1]:return
  for s in signs:
   qq=list(q);ee=list(E);qq[0]=s;qq[1]=-s;ee[0]+=s
   transitions.append((E[0],s))
   yield (tuple(qq),tuple(ee)),Fraction(1)
 return apply(v,op)
def n2(v):return sum(x*x for x in v.values())
def D(state):
 q,E=state
 return sum(E[e]*(E[e]-q[a]) for e,(a,b) in enumerate(EDGES) if q[b]==0)
omega={OMEGA:Fraction(1)}
M=Ft(F(omega));assert M=={OMEGA:Fraction(12)}
Z=F(F(omega));H4={state:-x/2 for state,x in Ft(Ft(Z)).items()}
assert len(H4)==13 and H4[OMEGA]==-84
assert sorted(x for state,x in H4.items() if state!=OMEGA)==[-2]*12
mean=H4[OMEGA];var=n2(H4)-mean*mean
assert var==48
mark_rows=[]
for label,signs in [('plus',(1,)),('minus',(-1,)),('coherent',(1,-1))]:
 BB=mark(F(omega),signs)
 RR={state:-c for state,c in apply(BB,lambda x:hops(x,center=0)).items()}
 assert all(D(state)==0 for state in BB)
 b,r=n2(BB),n2(RR)
 assert (b,r)=={'plus':(2,4),'minus':(2,2),'coherent':(4,6)}[label]
 mark_rows.append({'mark':label,'b':str(b),'r':str(r),'ell':str(r/b),'leading_QFI_apparatus_over_alpha2_delta2_epsilon_minus4':str(4*r)})
assert all(E*(E+step)==0 for E,step in transitions)
# Hence every displayed path has exactly unit actual normalized spin amplitude, any S>=1.

def projector(v):return np.outer(v,v.conj())
def qfi(rho,H):
 eig,V=np.linalg.eigh((rho+rho.conj().T)/2);HH=V.conj().T@H@V
 value=0.
 for i,x in enumerate(eig):
  for j,y in enumerate(eig):
   if x+y>1e-13:value+=2*(x-y)**2/(x+y)*abs(HH[i,j])**2
 return float(value)
def variance(rho,H):return float(np.trace(rho@H@H).real-np.trace(rho@H).real**2)
def trnorm(X):return float(np.linalg.svd(X,compute_uv=False).sum())
def close(a,b,scale=1.):assert abs(a-b)<=2e-10*max(scale,abs(a),abs(b))
zero=projector(np.array([1.,0.]));success=zero;failure=projector(np.array([0.,1.]))
U=np.zeros((8,8))
for s in range(2):
 for a in range(2):
  for f in range(2):U[(a*2+s)*2+f,(s*2+a)*2+f]=1.
toy=[]
for eps in (.25,.125,.0625):
 p=eps**2;w=eps**2;gap=eps**-4;H=np.diag([0.,gap])
 phi=np.array([np.sqrt(1-w),np.sqrt(w)]);pure=projector(phi);deph=np.diag(np.diag(pure))
 H_A=np.kron(H,np.eye(2));Htot=np.kron(H,np.eye(4))+np.kron(np.eye(2),H_A)
 assert np.linalg.norm(U@Htot-Htot@U)==0
 target=p*pure;Fphi=qfi(pure,H);close(Fphi,4*w*(1-w)*gap**2)
 per=[]
 for mu in (0.,.25,.75,1.):
  conditional=(1-mu)*pure+mu*deph
  apparatus=p*np.kron(conditional,success)+(1-p)*np.kron(zero,failure)
  joint_out=U@np.kron(zero,apparatus)@U.T
  selected=np.zeros((2,2),complex)
  for s in range(2):
   for t in range(2):
    for a in range(2):selected[s,t]+=joint_out[(s*2+a)*2,(t*2+a)*2]
  assert trnorm(selected-p*conditional)<1e-14
  FA=qfi(apparatus,H_A);expected=p*(1-mu)**2*Fphi;close(FA,expected)
  eta=trnorm(selected-target);close(eta,2*mu*p*np.sqrt(w*(1-w)))
  # Centered spectral radius M=gap/2, so 2M=gap.
  numerator=max(0.,p*np.sqrt(Fphi)-gap*eta)
  exact_q_lower=numerator**2/p
  trace_only_lower=numerator**2/(p+eta)
  close(FA,exact_q_lower);assert FA+1e-8>=trace_only_lower
  mean_A=float(np.trace(apparatus@H_A).real);var_A=variance(apparatus,H_A)
  close(mean_A,1.);close(var_A,eps**-4-1)
  close(trnorm(H@conditional-conditional@H)**2,qfi(conditional,H))
  per.append({'dephasing_fraction':mu,'apparatus_QFI':FA,'apparatus_variance':var_A,'apparatus_mean':mean_A,'selected_probability':float(np.trace(selected).real),'subnormalized_trace_error':eta,'error_over_epsilon_cubed':eta/eps**3,'robust_lower_using_actual_probability':exact_q_lower,'robust_lower_using_probability_tolerance':trace_only_lower})
 assert per[0]['apparatus_QFI']<Fphi # an unweighted postselection requirement would be false
 assert per[-1]['apparatus_QFI']==0. and per[-1]['apparatus_variance']>0.
 toy.append({'epsilon':eps,'gap':gap,'target_conditional_QFI':Fphi,'cases':per})
# Input coherence cannot be omitted from the budget: identity + stationary coin flag.
psi=projector(np.array([1.,1.])/np.sqrt(2));H=np.diag([0.,1.]);p=.25
assert qfi(psi,H)>0 and p*qfi(psi,H)>0
input_example={'input_QFI':qfi(psi,H),'apparatus_QFI':0.,'selected_probability':p,'selected_weighted_QFI':p*qfi(psi,H),'mechanism':'Identity system operation and stationary zero-energy classical success flag; target equals the supplied input.'}
# Additivity and commutator lower bound on unrelated mixed finite examples.
rng=np.random.default_rng(20260924)
X=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));rho=X@X.conj().T;rho/=np.trace(rho)
H3=np.diag([-3.,0.,5.]);Y=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));sigma=Y@Y.conj().T;sigma/=np.trace(sigma);H2=np.diag([1.,4.])
close(qfi(np.kron(rho,sigma),np.kron(H3,np.eye(2))+np.kron(np.eye(3),H2)),qfi(rho,H3)+qfi(sigma,H2))
assert trnorm(H3@rho-rho@H3)**2<=qfi(rho,H3)+1e-12
assert qfi(rho,H3)<=4*variance(rho,H3)+1e-12
result={'cube_input':{'M_Omega_coefficient':12,'H4_Omega_coefficient':-84,'off_diagonal_words':12,'off_diagonal_coefficient':-2,'H4_variance':48,'input_QFI_limit_over_delta_squared':192,'all_traversed_edges_have_unit_actual_spin_amplitude_for_S_ge_1':True},'cube_first_marks':mark_rows,'conservative_swap_toys':toy,'input_coherence_subtraction_example':input_example,'independent_mixed_checks':'QFI additivity, commutator lower bound and QFI<=4 variance verified on fixed random mixed states.','scope':'Exact primitive path integers and finite floating matrix controls; asymptotic and arbitrary-apparatus conclusions require PRE proofs.'}
Path('COHERENCE_CHECK_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
print('All listed checks completed without assertion failure.')
