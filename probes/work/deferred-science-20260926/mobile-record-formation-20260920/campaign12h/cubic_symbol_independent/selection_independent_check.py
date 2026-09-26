#!/usr/bin/env python3
"""Independent selection identities and a complete exact stationary-adjoint test."""
from pathlib import Path
from itertools import product
import sympy as s
import hashlib,json
HERE=Path(__file__).resolve().parent;checks=[]
def check(name,condition,detail=None):
 assert bool(condition),(name,detail)
 checks.append({'name':name,'passed':True,'detail':detail})
q=s.Matrix(s.symbols('q0:3',real=True));a1,a2,m,u,v=s.symbols('a1 a2 m u v',real=True)
def cross(q):return s.Matrix([[0,-q[2],q[1]],[q[2],0,-q[0]],[-q[1],q[0],0]])
C=cross(q);D1=s.diag(1,-1,0)/s.sqrt(2);D2=s.diag(1,1,-2)/s.sqrt(6)
Q=[]
for i,j in [(0,1),(0,2),(1,2)]:
 M=s.zeros(3);M[i,j]=M[j,i]=1/s.sqrt(2);Q.append(M)
K=(a1*q).row_join(a2*q).row_join(m*C).row_join(u*D1*q).row_join(u*D2*q)
for M in Q:K=K.row_join(v*M*q)
K=K.row_join(s.zeros(3,1))
A=s.zeros(3).row_join(K).col_join(K.T.row_join(s.zeros(11)))
T=s.diag(-1,-1,-1,*([1]*11))
check('all_five_symbols_obey_internal_A_sign_reversal',T*A*T==-A)
# Fourier readout H maps raw fields (E; scalars,B,tensors,w) into (curl B,-curl E).
H=s.zeros(6,14);H[:3,5:8]=s.I*C;H[3:,:3]=-s.I*C
wave=s.zeros(6);wave[:3,3:]=-s.I*m*C;wave[3:,:3]=s.I*m*C
residual=(H*(-s.I*A)-wave*H).applyfunc(s.expand)
expected=s.zeros(6,14)
other_columns=[3,4,8,9,10,11,12,13]
for col in other_columns:expected[3:,col]=-C*A[:3,col]
check('curl_readout_evolution_signs_and_all_source_columns',residual==expected)
check('scalar_and_raw_vector_sources_cancel_from_curl_residual',all(residual[:,j]==s.zeros(6,1) for j in range(8)))
axis={q[0]:1,q[1]:0,q[2]:0};diagonal={q[0]:1,q[1]:1,q[2]:0}
raw=(q.T*A[:3,:])
check('raw_Gauss_sources_force_scalar_diagonal_offdiagonal_coefficients',
 raw[3].subs(axis)==a1 and raw[4].subs(axis)==a2 and raw[8].subs(axis)==u/s.sqrt(2) and raw[10].subs(diagonal)==s.sqrt(2)*v)
check('curl_closure_forces_tensors_but_not_scalars',
 residual[:,8].subs(diagonal)!=s.zeros(6,1) and residual[:,10].subs(axis)!=s.zeros(6,1) and residual.subs({u:0,v:0})==s.zeros(6,14))
check('raw_B_divergence_is_automatically_conserved',q.T*A[5:8,:]==s.zeros(1,14))

# Complete 81-state four-site ring with vacancy and opposite A labels. An
# arbitrary symmetric odd pair tensor suffices to test exact generator adjoints.
S=s.Matrix([[0,2,-2],[2,3,0],[-2,0,-3]])
theta=[0,2,1];states=list(product(range(3),repeat=4));index={x:i for i,x in enumerate(states)}
assert S.extract(theta,theta)==-S
L=s.zeros(len(states));R=s.zeros(len(states))
for ix,word in enumerate(states):
 R[index[tuple(theta[a] for a in word)],ix]=1
 for x in range(4):
  left,a,b,right=[word[i%4] for i in (x-1,x,x+1,x+2)]
  h=S[left,a]+S[a,right]-S[left,b]-S[b,right]
  rate=1+max(h,0)
  nxt=list(word);nxt[x],nxt[(x+1)%4]=nxt[(x+1)%4],nxt[x]
  jx=index[tuple(nxt)];L[ix,jx]+=rate;L[ix,ix]-=rate
check('complete_finite_generator_stationary_uniform_law',s.ones(1,len(states))*L==s.zeros(1,len(states)))
check('complete_finite_generator_exact_generalized_adjoint',R*L*R==L.T,
 {'states':len(states),'rates':'kappa=1 plus positive part of a symmetric Theta-odd pair tensor','scope':'Reduced-label exact identity control; full15 proof follows from the same pointwise identities.'})
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':checks,
 'scope':'Independent exact addendum control before author code/results; no new microscopic Gauss law or hydrodynamic statement.'}
(HERE/'SELECTION_INDEPENDENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
