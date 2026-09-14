from pathlib import Path
import json,itertools
import numpy as np
from block5_tensor_check import incidence,operators
from scipy.linalg import null_space

def clock_alias_checks():
 G,S,T,sites=incidence(5);n=len(sites);dim=6*n
 assert np.max(abs(G).sum(axis=1))==6 and np.max(abs(S).sum(axis=1))==36
 rng=np.random.default_rng(9140535);rows=[]
 for N in [7,11,17,101]:
  # Principal representatives of exact stabilizer characters can acquire a
  # nonzero integer syndrome while retaining zero modular syndrome.
  beta=np.zeros(n,dtype=int);beta[0]=(N-1)//2
  m=S.T@beta;m=(m+N//2)%N-N//2
  assert np.max(abs(G@m))>0 and np.max(abs((G@m)%N))==0
  alpha=rng.integers(-N//2,N//2+1,3*n);r=G.T@alpha;r=(r+N//2)%N-N//2
  assert np.max(abs(S@r))>0 and np.max(abs((S@r)%N))==0
  rows.append({'N':N,'h_character_largest_integer_syndrome':int(np.max(abs(G@m))),'E_character_largest_integer_syndrome':int(np.max(abs(S@r))),'modular_syndromes_zero':True,'not_a_constructed_linear_phase':True})
 # Small bounded random words test the sufficient lifting bound directly.
 trials=[]
 for M in [1,2,3]:
  N=36*M+1
  for _ in range(20):
   m=rng.integers(-M,M+1,dim);r=rng.integers(-M,M+1,dim)
   gm=G@m;sr=S@r
   assert np.max(abs(gm))<N and np.max(abs(sr))<N
   assert bool(np.all(gm%N==0))==bool(np.all(gm==0))
   assert bool(np.all(sr%N==0))==bool(np.all(sr==0))
  trials.append({'M':M,'N':N,'words':20})
 return {'row_l1_norms':[6,36],'alias_witnesses':rows,'lifting_checks':trials}

def mixed_modes():
 rows=[]
 # Local invariant building blocks R(h), C(E), including mixed terms, with
 # positive quadratic form on the full 6+9 invariant-component vector.
 rng=np.random.default_rng(9140536);A=rng.normal(size=(15,15));W=A.T@A+np.eye(15)
 for direction in [np.array([0.,0.,1.]),np.array([1.,2.,-3.])/np.sqrt(14)]:
  scaled=[]
  for kscale in [.2,.1,.05,.025]:
   k=kscale*direction;R,G,S,C,K0=operators(k);TT=null_space(np.vstack([G,S]))
   # A single spatial derivative contributes i; retaining it makes the mixed
   # Hessian Hermitian and compatible with real fields at opposite momenta.
   D=np.block([[R@TT,np.zeros((6,2))],[np.zeros((9,2)),1j*C@TT]])
   H=D.conj().T@W@D;J=np.block([[np.zeros((2,2)),np.eye(2)],[-np.eye(2),np.zeros((2,2))]])
   assert np.max(abs(H-H.conj().T))<1e-13
   F=J@H;scale=np.diag([1.,1.,kscale,kscale])
   rescaled=np.linalg.solve(scale,F@scale)/kscale**3
   eig=np.linalg.eigvals(F);assert np.max(abs(eig.real))<1e-12
   scaled.append(np.sort(abs(eig.imag))/kscale**3)
   rows.append({'direction':direction.tolist(),'k':kscale,'frequency_over_k_cubed':scaled[-1].tolist(),'rescaled_operator_norm':float(np.linalg.norm(rescaled,2))})
  assert max(np.max(abs(scaled[0]-a)) for a in scaled[1:])<1e-10
 return rows

if __name__=='__main__':
 result={'compact_character_lift':clock_alias_checks(),'mixed_invariant_Hamiltonian_scaling':mixed_modes()}
 Path(__file__).with_name('BLOCK5_CLOCK_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
