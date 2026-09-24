#!/usr/bin/env python3
"""Exact Riccati/canonical algebra and numerical full-cluster controls."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/block_expansion_check.py', 'scripts/mobile_compensation_finite_blocks_20260924.py')
import sys
sys.dont_write_bytecode=True
import json,platform
import numpy as np
import sympy as sp
from mobile_compensation_finite_blocks_20260924 import exact_blocks,numpy_matrix,ingredients,canonical_rotation

def strings(M):return [[str(v) for v in row] for row in M.tolist()]
def frob_squared(M):return str(sp.trace(M.H*M))
W,N,T,C,jumps=exact_blocks();dim=W.rows
ix,qx,A,Z,M,C0,C1,K2,K4,B=ingredients(W,T,C,jumps)
P=sp.diag(*[int(W[i,i]==0) for i in range(dim)])
assert C.H==C and W*C==C*W and N*C==C*N and N*T==T*N
assert T.H==T and all(T[i,j]==0 for i in range(dim) for j in range(dim) if abs(W[i,i]-W[j,j])!=1)
for j in jumps:assert W*j-j*W==-j and N*j-j*N==2*j and j*P==sp.zeros(dim)
Np=N.extract(ix,ix)
for b in B:assert Np*b-b*Np==2*b
assert C0*M!=M*C0 and C1!=sp.zeros(C1.rows)
# Graph map X:P->Q and exact order-three invariance.
Wq=W.extract(qx,qx);R=Wq.inv();Tq=T.extract(qx,qx);Cq=C.extract(qx,qx)
Af=T.extract(qx,ix)
X1=-R*Af;X2=-R*Tq*X1
X3=-R*(Tq*X2+Cq*X1-X1*C0-X1*Af.H*X1)
e=sp.Symbol('e');X=e*X1+e**2*X2+e**3*X3
res=e*Af+(Wq+e*Tq+e**2*Cq)*X-X*(e**2*C0)-e*X*Af.H*X
for order in [1,2,3]:assert res.applyfunc(lambda z:sp.expand(z).coeff(e,order))==sp.zeros(len(qx),len(ix))
assert X1.H*X1==M and Af.H*X2==sp.zeros(len(ix))
graph4=Af.H*X3
canonical4=graph4+(M*K2-K2*M)/2
assert canonical4==K4 and K4.H==K4
assert graph4!=graph4.H
# Scalar compensation cancels completely from the fourth-order addition.
scalar=sp.Rational(7,3)
assert A.H*(scalar*sp.eye(A.rows))*A-(M*(scalar*sp.eye(M.rows))+(scalar*sp.eye(M.rows))*M)/2==sp.zeros(M.rows)
Wn,Tn,Cn=map(numpy_matrix,[W,T,C]);K2n,K4n=map(numpy_matrix,[K2,K4])
Xi=np.diag([(-1)**int(W[i,i]) for i in range(dim)])
rows=[]
for eps in [1/8,1/16,1/32,1/64]:
 U,ht=canonical_rotation(Wn,Tn,Cn,eps);Um,hm=canonical_rotation(Wn,Tn,Cn,-eps)
 low=ht[np.ix_(ix,ix)]
 error=float(np.linalg.norm(low-eps**2*K2n-eps**4*K4n,2))
 coefficient=(low-eps**2*K2n)/eps**4
 parity=float(np.linalg.norm(Um-Xi@U@Xi,2))
 full_off=ht.copy()
 for i in range(dim):
  for j in range(dim):
   if W[i,i]==W[j,j]:full_off[i,j]=0
 assert parity<1e-12 and np.linalg.norm(full_off,2)<1e-12
 assert np.linalg.norm(U.conj().T@U-np.eye(dim),2)<1e-12
 rows.append({'epsilon':eps,'canonical_remainder_norm':error,'remainder_over_epsilon6':error/eps**6,
  'fourth_coefficient_error':float(np.linalg.norm(coefficient-K4n,2)),
  'wrong_graph_coefficient_error':float(np.linalg.norm(coefficient-numpy_matrix(graph4),2)),
  'wrong_omitted_C1_error':float(np.linalg.norm(coefficient-(K4n-numpy_matrix(A.H*C1*A)),2)),
  'global_rotated_remainder_times_epsilon_minus2':float(np.linalg.norm(ht-Wn,2))/eps**2,
  'parity_error':parity,'off_W_block_norm':float(np.linalg.norm(full_off,2))})
assert rows[-1]['fourth_coefficient_error']<rows[0]['fourth_coefficient_error']/40
assert rows[-1]['wrong_graph_coefficient_error']>1 and rows[-1]['wrong_omitted_C1_error']>1
# C2 first enters beyond the fourth coefficient, and scalar C only shifts H2.
controls=[]
for eps in [1/8,1/16,1/32]:
 U0,h0=canonical_rotation(Wn,Tn,np.zeros_like(Cn),eps)
 Cs=float(scalar)*np.eye(dim);Us,hs=canonical_rotation(Wn,Tn,Cs,eps)
 assert np.linalg.norm(hs[np.ix_(ix,ix)]-h0[np.ix_(ix,ix)]-eps**2*float(scalar)*np.eye(len(ix)),2)<1e-12
 Cexc=np.zeros_like(Cn);Cexc[4,4]=7
 _,hexc=canonical_rotation(Wn,Tn,Cexc,eps)
 delta=float(np.linalg.norm((hexc-h0)[np.ix_(ix,ix)],2))
 controls.append({'epsilon':eps,'scalar_rotation_error':float(np.linalg.norm(Us-U0,2)),
  'W2_only_compensation_low_block_change':delta,'W2_change_over_epsilon6':delta/eps**6})
print(json.dumps({'environment':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
 'W_diagonal':[str(W[i,i]) for i in range(dim)],'N_diagonal':[str(N[i,i]) for i in range(dim)],
 'T':strings(T),'C':strings(C),'jumps':[strings(j) for j in jumps],
 'P_indices':ix,'M':strings(M),'C0':strings(C0),'C1':strings(C1),'Z':strings(Z),
 'K2':strings(K2),'K4':strings(K4),'leading_effective_jumps':[strings(b) for b in B],
 'commutator_M_C0_frobenius_squared':frob_squared(M*C0-C0*M),
 'graph_fourth_antihermitian_frobenius_squared':frob_squared(graph4-graph4.H),
 'exact_Riccati_orders_1_to_3_zero':True,'canonical_fourth_formula_verified':True,
 'canonical_full_cluster_checks':rows,'scalar_and_excited_block_controls':controls},indent=2))
