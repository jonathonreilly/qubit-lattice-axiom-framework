#!/usr/bin/env python3
"""Full Lindblad controls, including the large off-block loss source."""
import sys
sys.dont_write_bytecode=True
import json
import numpy as np
import scipy.linalg as la
from finite_blocks import exact_blocks,numpy_matrix,ingredients,canonical_rotation

def lindblad(H,jumps):
 d=len(H);I=np.eye(d);L=-1j*(np.kron(I,H)-np.kron(H.T,I))
 for j in jumps:
  loss=j.conj().T@j
  L+=np.kron(j.conj(),j)-.5*(np.kron(I,loss)+np.kron(loss.T,I))
 return L

def vec(M):return M.reshape(-1,order='F')
def matrix(v,d):return v.reshape((d,d),order='F')
def tr_norm(M):return float(np.sum(la.svdvals(M)))
def norm(M):return float(la.svdvals(M)[0])
W0,N0,T0,C0,j0=exact_blocks()
ix,qx,A,Z,M,Cp,C1,K2,K4,B=ingredients(W0,T0,C0,j0)
W,T,C=map(numpy_matrix,[W0,T0,C0]);jumps=list(map(numpy_matrix,j0));b=list(map(numpy_matrix,B))
k2,k4=map(numpy_matrix,[K2,K4]);d=len(W);r=len(ix);w=np.real(np.diag(W))
embedding=np.zeros((d*d,r*r),complex)
for j in range(r):
 for i in range(r):embedding[ix[i]+d*ix[j],i+r*j]=1
E0=lambda X:matrix(embedding@vec(X),d)
delta=.7;kappa=.4
weights=vec(w[:,None]-w[None,:]);A0=-1j*delta*weights
mask=vec((w[:,None]==0)^(w[None,:]==0))
assert all(A0[mask]!=0)
hermitian_basis=[]
for i in range(r):
 X=np.zeros((r,r),complex);X[i,i]=1;hermitian_basis.append(X)
 for j in range(i):
  X=np.zeros((r,r),complex);X[i,j]=X[j,i]=1;hermitian_basis.append(X)
  Y=np.zeros((r,r),complex);Y[i,j]=1j;Y[j,i]=-1j;hermitian_basis.append(Y)
psi=np.zeros(r,complex);psi[:2]=[1,1j];psi/=np.linalg.norm(psi)
phi=np.array([1,1j,.5,-1j/3,.25]);phi/=np.linalg.norm(phi)
initial=[np.outer(v,v.conj()) for v in [psi,phi]]
residual_rows=[];density_rows=[]
for eps in [1/8,1/16,1/32,1/64]:
 U,ht=canonical_rotation(W,T,C,eps);jt=[U.conj().T@j@U for j in jumps]
 G=lindblad(delta*ht/eps**4,[np.sqrt(kappa)*j/eps for j in jt])
 Hp=delta*(k2/eps**2+k4);Lp=lindblad(Hp,[np.sqrt(kappa)*j for j in b])
 R=G@embedding-embedding@Lp
 Roff=R*mask[:,None];Rdiag=R*(~mask)[:,None]
 F=np.zeros_like(R);F[mask,:]=-eps**4*Roff[mask,:]/A0[mask,None]
 residual=G@(embedding+F)-(embedding+F)@Lp
 rest=G-np.diag(A0)/eps**4
 expanded=Rdiag+rest@F-F@Lp
 cancellation=norm(residual-expanded)
 assert cancellation<2e-7
 hp_error=max(norm(matrix(F@vec(X),d)-matrix(F@vec(X),d).conj().T) for X in hermitian_basis)
 assert hp_error<1e-12
 low_jump_error=max(norm(jt[k][np.ix_(ix,ix)]/eps-b[k]) for k in range(len(b)))
 leakage_jump=max(norm(jt[k][np.ix_(qx,ix)]) for k in range(len(b)))
 corr_density=E0(initial[0])+matrix(F@vec(initial[0]),d)
 residual_rows.append({'epsilon':eps,'off_discrepancy_HS_norm':norm(Roff),'epsilon_times_off_discrepancy':eps*norm(Roff),
 'diagonal_discrepancy_HS_norm':norm(Rdiag),'diagonal_discrepancy_over_epsilon':norm(Rdiag)/eps,
 'corrector_HS_norm':norm(F),'corrector_over_epsilon3':norm(F)/eps**3,
 'corrected_residual_HS_norm':norm(residual),'corrected_residual_over_epsilon':norm(residual)/eps,
 'rest_generator_norm_times_epsilon2':norm(rest)*eps**2,'target_generator_norm_times_epsilon2':norm(Lp)*eps**2,
 'residual_identity_error':cancellation,'corrector_hermiticity_error':hp_error,
 'effective_jump_error':low_jump_error,'excited_jump_leakage_over_epsilon2':leakage_jump/eps**2,
 'corrected_embedding_minimum_eigenvalue':float(np.min(la.eigvalsh(corr_density)))})
 # Physical undressed initial density, ordinary compact times, full generator.
 Hfull=delta*(W+eps*T+eps**2*C)/eps**4
 Lfull=lindblad(Hfull,[np.sqrt(kappa)*j/eps for j in jumps])
 for time in [.0,.03,.12,.35]:
  full_prop=la.expm(time*Lfull);target_prop=la.expm(time*Lp)
  for number,rho in enumerate(initial):
   exact=matrix(full_prop@vec(E0(rho)),d)
   target=E0(matrix(target_prop@vec(rho),r))
   error=tr_norm(exact-target);trace_error=abs(np.trace(exact)-1)
   hermitian_error=norm(exact-exact.conj().T)
   assert trace_error<2e-8 and hermitian_error<2e-8
   density_rows.append({'epsilon':eps,'time':time,'initial_state':number,'trace_distance_norm':error,
      'trace_error_over_epsilon':error/eps,'exact_density_trace_error':float(trace_error),
      'exact_density_minimum_eigenvalue':float(np.min(la.eigvalsh((exact+exact.conj().T)/2)))})
assert residual_rows[-1]['off_discrepancy_HS_norm']>4*residual_rows[0]['off_discrepancy_HS_norm']
assert max(row['corrected_residual_over_epsilon'] for row in residual_rows)<100
assert max(row['trace_error_over_epsilon'] for row in density_rows)<20
print(json.dumps({'delta':delta,'kappa':kappa,'full_Hilbert_dimension':d,'P_dimension':r,
 'residual_norm_convention':'Euclidean induced norm of vectorized matrices (Hilbert--Schmidt), a finite control only; the proof uses dimension-free trace-norm estimates.',
 'initial_state_0':'Pure N=0 superposition of the first two P states with relative phase i.',
 'initial_state_1':'Pure P superposition across N=0,2,4 with amplitudes proportional to (1,i,1/2,-i/3,1/4).',
 'residual_controls':residual_rows,'density_controls':density_rows,
 'maximum_trace_error_over_epsilon':max(row['trace_error_over_epsilon'] for row in density_rows),
 'proof_limit':'These floating finite-block comparisons corroborate the analytic estimate; no interval certificate or spin/volume-uniform numerical assertion.'},indent=2))
