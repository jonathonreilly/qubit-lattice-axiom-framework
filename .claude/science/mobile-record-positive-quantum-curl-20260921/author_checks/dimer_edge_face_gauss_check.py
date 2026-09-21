#!/usr/bin/env python3
"""Incidence identities and physical finite-block Gauss-limit corroboration."""
from pathlib import Path
from itertools import product,permutations
import json,hashlib,math,time
import numpy as np
import sympy as sy
from scipy import sparse as sp
from scipy.sparse.linalg import expm_multiply

ROOT=Path(__file__).resolve().parent
def epsilon(i,j,k):
 return 0 if len({i,j,k})<3 else (1 if (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)] else -1)

def incidence(L):
 xs=list(product(range(L),repeat=3));ind={x:i for i,x in enumerate(xs)};V=len(xs);D=[]
 for j in range(3):
  d=np.zeros((V,V),dtype=np.int64)
  for x in xs:
   y=list(x);y[j]=(y[j]+1)%L;d[ind[x],ind[tuple(y)]]+=1;d[ind[x],ind[x]]-=1
  D.append(d)
 d0=np.vstack(D);d2=np.hstack(D)
 C=np.block([[sum((epsilon(i,j,k)*D[j] for j in range(3)),np.zeros((V,V),dtype=np.int64)) for k in range(3)] for i in range(3)])
 return xs,ind,D,d0,C,d2

def incidence_controls():
 rows=[]
 for L in [3,4]:
  xs,ind,D,d0,C,d2=incidence(L);V=len(xs)
  assert not np.any(C@d0) and not np.any(d2@C)
  lap=sum(d.T@d for d in D);vec=np.kron(np.eye(3,dtype=np.int64),lap)
  assert np.array_equal(C.T@C,vec-d0@d0.T)
  assert np.array_equal(C@C.T,vec-d2.T@d2)
  rankC=sy.Matrix(C).to_DM().rank();rankd0=sy.Matrix(d0).to_DM().rank()
  assert rankC==2*V-2 and rankd0==V-1
  evals=np.linalg.eigvalsh(C.T@C);expected=[];symbol_error=0.
  xyz=np.array(xs)
  for ns in product(range(L),repeat=3):
   k=2*np.pi*np.array(ns)/L;d=np.exp(1j*k)-1;lam=float(np.vdot(d,d).real)
   expected.extend([0.,lam,lam])
   S=np.array([[0,-d[2],d[1]],[d[2],0,-d[0]],[-d[1],d[0],0]])
   assert np.max(np.abs(S.conj().T@S-(lam*np.eye(3)-np.outer(d,d.conj()))))<2e-14
   phase=np.exp(1j*(xyz@k))/math.sqrt(V)
   for j in range(3):
    f=np.kron(np.eye(3)[:,j],phase);target=np.kron(S[:,j],phase)
    symbol_error=max(symbol_error,float(np.linalg.norm(C@f-target)))
  assert max(abs(np.sort(evals)-np.sort(expected)))<5e-13 and symbol_error<2e-13
  wrong=np.block([[np.zeros_like(C),C],[-C,np.zeros_like(C)]])
  right=np.block([[np.zeros_like(C),C.T],[-C,np.zeros_like(C)]])
  assert not np.any(right+right.T) and np.any(wrong+wrong.T)
  broken=C.copy();broken[0,0]+=1
  assert np.any(broken@d0) and np.any(d2@broken)
  rows.append(dict(L=L,vertices=V,edges=3*V,exact_rank_curl=rankC,exact_rank_gradient=rankd0,exact_kernel_dimension=3*V-rankC,nonzero_frequency_min=float(math.sqrt(min(x for x in expected if x>1e-10))),zero_frequency_wavevectors=1,Fourier_max_error=symbol_error,wrong_adjoint_energy_defect_frobenius=float(np.linalg.norm(wrong+wrong.T)),one_entry_incidence_mutation_rejected=True))
 return rows

def rotation_controls():
 L=3;xs,ind,D,d0,C,d2=incidence(L);V=len(xs);count=0
 for perm in permutations(range(3)):
  for signs in product([-1,1],repeat=3):
   R=np.zeros((3,3),dtype=int)
   for j in range(3):R[perm[j],j]=signs[j]
   if round(np.linalg.det(R))!=1:continue
   RE=np.zeros((3*V,3*V),dtype=int);RF=RE.copy();R0=np.zeros((V,V),dtype=int);R3=R0.copy()
   for x in xs:
    y=R@x;R0[ind[tuple(y%L)],ind[x]]=1
    cube=y+sum((min(0,signs[j])*np.eye(3,dtype=int)[perm[j]] for j in range(3)),np.zeros(3,dtype=int));R3[ind[tuple(cube%L)],ind[x]]=1
    for i in range(3):
     edge=y+min(0,signs[i])*np.eye(3,dtype=int)[perm[i]]
     RE[perm[i]*V+ind[tuple(edge%L)],i*V+ind[x]]=signs[i]
     face=y+sum((min(0,signs[j])*np.eye(3,dtype=int)[perm[j]] for j in range(3) if j!=i),np.zeros(3,dtype=int))
     RF[perm[i]*V+ind[tuple(face%L)],i*V+ind[x]]=signs[i]
   assert np.array_equal(RE.T@RE,np.eye(3*V)) and np.array_equal(RF.T@RF,np.eye(3*V))
   assert np.array_equal(d0@R0,RE@d0) and np.array_equal(C@RE,RF@C) and np.array_equal(d2@RF,R3@d2)
   count+=1
 assert count==24
 return dict(L=L,proper_rotations=count,exact_edge_face_chain_maps=3*count,negative_axis_basepoint_shifts_included=True)

def spin_controls():
 rows=[]
 for K in [1,2,3,4]:
  states=list(product([0,1],repeat=K));ix={x:i for i,x in enumerate(states)};U=sy.zeros(2**K,K+1);a=sy.zeros(2**K)
  for col,x in enumerate(states):
   n=sum(x);U[col,n]=1/sy.sqrt(math.comb(K,n))
   for i in range(K):
    if x[i]:
     y=list(x);y[i]=0;a[ix[tuple(y)],col]+=1/sy.sqrt(K)
  exact=sy.zeros(K+1)
  for m in range(1,K+1):exact[m-1,m]=sy.sqrt(sy.Rational(m*(K-m+1),K))
  assert sy.simplify(U.T*a*U-exact)==sy.zeros(K+1) and sy.simplify(a*U-U*exact)==sy.zeros(2**K,K+1)
  Q=(exact+exact.T)/sy.sqrt(2);P=sy.I*(exact.T-exact)/sy.sqrt(2)
  assert sy.simplify((Q*P-P*Q)/sy.I-sy.diag(*[1-sy.Rational(2*m,K) for m in range(K+1)]))==sy.zeros(K+1)
  assert max(abs(x) for x in Q.eigenvals())==sy.sqrt(sy.Rational(K,2))
  rows.append(dict(K=K,qubits_in_two_level_subspaces=2*K,physical_pair_product_dimension=2**K,symmetric_dimension=K+1,exact_quadrature_norm=str(sy.sqrt(sy.Rational(K,2)))))
 # A two-link incidence motif, not a three-dimensional lattice surrogate.
 X=sy.Matrix([[0,1],[1,0]])/sy.sqrt(2);Y=sy.Matrix([[0,-sy.I],[sy.I,0]])/sy.sqrt(2)
 q1=sy.kronecker_product(X,sy.eye(2));q2=sy.kronecker_product(sy.eye(2),X);p1=sy.kronecker_product(Y,sy.eye(2));p2=sy.kronecker_product(sy.eye(2),Y)
 H=(p1*p1+p2*p2+(q1-q2)**2)/2;G=-(p1+p2)/sy.sqrt(2);comm=sy.simplify(G*H-H*G)
 assert comm!=sy.zeros(4)
 return dict(rows=rows,two_link_K1_finite_Gauss_commutator_squared_Frobenius=str(sy.trace(comm.H*comm)),scope='The motif only checks cutoff algebra; it does not replace the full cubical incidence controls.')

def norm(z):return math.sqrt(math.fsum(float(x) for x in np.abs(z).reshape(-1)**2))

def squeezed_projection(K,eps):
 U=np.array([[1,1],[-1,1]])/math.sqrt(2);A=U@np.diag([math.sqrt(2),eps**2])@U.T
 Z=(np.eye(2)-A)@np.linalg.inv(np.eye(2)+A);coeff=np.zeros((K+1,K+1));coeff[0,0]=np.linalg.det(np.eye(2)-Z@Z)**.25
 for total in range(1,2*K+1):
  for a in range(max(0,total-K),min(K,total)+1):
   b=total-a
   if a:
    coeff[a,b]=((Z[0,0]*math.sqrt(a-1)*coeff[a-2,b] if a>=2 else 0)+(Z[0,1]*math.sqrt(b)*coeff[a-1,b-1] if b else 0))/math.sqrt(a)
   elif b>=2:coeff[a,b]=Z[1,1]*math.sqrt((b-1)/b)*coeff[a,b-2]
 return coeff.reshape(-1),A

def motif_dynamics():
 rows=[];uT=np.array([1,-1])/math.sqrt(2);uZ=np.array([1,1])/math.sqrt(2);omega=math.sqrt(2);ET=omega/2
 for K in [4,8,16,32,64,128]:
  eps=K**(-1/6);coef,A=squeezed_projection(K,eps);alpha=norm(coef);phi=coef/alpha
  values=np.array([math.sqrt(n*(1-(n-1)/K)) for n in range(1,K+1)])
  low=sp.diags(values,1,shape=(K+1,K+1),format='csr');q=(low+low.T)/math.sqrt(2);p=1j*(low.T-low)/math.sqrt(2);eye=sp.eye(K+1,format='csr')
  qs=[sp.kron(q,eye,format='csr'),sp.kron(eye,q,format='csr')];ps=[sp.kron(p,eye,format='csr'),sp.kron(eye,p,format='csr')]
  B=qs[0]-qs[1];G=-(ps[0]+ps[1])/math.sqrt(2);H=(ps[0]@ps[0]+ps[1]@ps[1]+B@B)/2
  initial_energy=float(np.vdot(phi,H@phi).real)
  tests=[(np.array([.4,-.2]),.3),(np.array([.5,.5]),0.)]
  for t in [0.,.5,1.25]:
   state=phi.astype(complex) if t==0 else expm_multiply(-1j*t*H,phi,traceA=-1j*t*H.diagonal().sum())
   assert abs(norm(state)-1)<1e-11
   energy=float(np.vdot(state,H@state).real);assert abs(energy-initial_energy)<1e-10
   gauss=norm(G@state)**2
   values_out=[]
   for e,b in tests:
    Op=-e[0]*ps[0]-e[1]*ps[1]+b*B;actual=np.vdot(state,expm_multiply(1j*Op,state,traceA=0.))
    # Reduced transverse vacuum is stationary; longitudinal P is free and constant.
    varT=(float(np.dot(e,uT))**2*omega+2*b*b/omega)/2
    target=math.exp(-varT/2);canonical=target*math.exp(-eps*eps*float(np.dot(e,uZ))**2/4)
    values_out.append(dict(e=e.tolist(),b=b,finite_real=float(actual.real),finite_imag=float(actual.imag),reduced_target=target,canonical_squeezed_target=canonical,error_to_reduced=float(abs(actual-target)),error_to_squeezed=float(abs(actual-canonical))))
   rows.append(dict(K=K,physical_dimension=(K+1)**2,epsilon=eps,time=t,projection_missing_probability=max(0.,1-alpha**2),energy=energy,reduced_energy=ET,energy_error=abs(energy-ET),energy_error_over_K_minus_third=abs(energy-ET)*K**(1/3),Gauss_mean_square=gauss,Gauss_over_K_minus_sixth=gauss*K**(1/6),canonical_Gauss_mean_square=eps*eps/2,Weyl_values=values_out))
  print('two_link_K_complete',K,flush=True)
 return dict(rows=rows,scope='Exact finite-spin two-link motif with one transverse oscillator and one squeezed null coordinate. Full 3D convergence is proved analytically, not inferred from this small motif. Ratios are corroboration, not fitted exponents or universal constants.')

def main():
 result={'status':'completed author corroboration; conditional proofs require separate review','sources':[]}
 for name in ['DIMER_EDGE_FACE_GAUSS_QUANTUM_LIMIT.md','DIMER_EDGE_FACE_ENERGY_AND_GAUSS_MOMENT_ADDENDUM.md',Path(__file__).name]:
  p=ROOT/name;result['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 for name,fn in [('incidence',incidence_controls),('rotations',rotation_controls),('finite_qubit_algebra',spin_controls),('squeezed_motif',motif_dynamics)]:
  result[name]=fn();print(name+' complete',flush=True)
 out=ROOT/'dimer_edge_face_gauss_checks';out.mkdir(exist_ok=True);(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print('all_four_control_groups_complete',flush=True)

if __name__=='__main__':main()
