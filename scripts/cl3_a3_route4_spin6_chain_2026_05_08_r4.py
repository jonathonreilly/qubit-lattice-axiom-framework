#!/usr/bin/env python3
"""Finite supplied Clifford/block/cyclic controls; no physical generation no-go."""
AUDIT_TIMEOUT_SEC = 120
import itertools
import numpy as np
I=np.eye(2); X=np.array([[0,1],[1,0]]); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1])
def kron(ms):
 a=np.ones((1,1))
 for m in ms:a=np.kron(a,m)
 return a
checks={}
def check(k,v): checks[k]=bool(v)
def eq(a,b):return np.linalg.norm(a-b)<1e-10
g=[kron([Z]*k+[p]+[I]*(2-k)) for k in range(3) for p in [X,Y]]; I8=np.eye(8)
check('all Clifford anticommutators',all(eq(a@b+b@a,2*I8 if i==j else 0*I8) for i,a in enumerate(g) for j,b in enumerate(g)))
mon=[]
for mask in range(64):
 m=I8.astype(complex)
 for j in range(6):
  if mask>>j&1:m=m@g[j]
 mon.append(m.reshape(-1))
check('64 monomials span M8',np.linalg.matrix_rank(np.stack(mon))==64)
omega=g[0]@g[1]@g[2]@g[3]@g[4]@g[5]; chir=-1j*omega
check('volume has order four not two',eq(omega@omega,-I8) and eq(np.linalg.matrix_power(omega,4),I8) and not eq(omega@omega,I8))
b=[g[i]@g[j]/2 for i in range(6) for j in range(i+1,6)]
check('volume commutes with every bivector',all(eq(omega@t,t@omega) for t in b))
ev,U=np.linalg.eigh(chir)
for sign in [-1,1]:
 V=U[:,np.isclose(ev,sign)]; bs=[V.conj().T@t@V for t in b]
 check('chirality dimension '+str(sign),V.shape==(8,4))
 check('su4 span '+str(sign),all(eq(t+t.conj().T,0*t) and abs(np.trace(t))<1e-10 for t in bs) and np.linalg.matrix_rank(np.stack([np.r_[t.real.ravel(),t.imag.ravel()] for t in bs]))==15)
# A simple spanning set of traceless Hermitian 3x3 matrices.
t=[]
for i in range(3):
 for j in range(i+1,3):
  m=np.zeros((3,3),complex);m[i,j]=m[j,i]=1;t.append(m)
  m=np.zeros((3,3),complex);m[i,j]=-1j;m[j,i]=1j;t.append(m)
t += [np.diag([1,-1,0]),np.diag([1,1,-2])]
def null_dim(gs):
 n=len(gs[0]);return n*n-np.linalg.matrix_rank(np.vstack([np.kron(np.eye(n),a)-np.kron(a.T,np.eye(n)) for a in gs]))
check('full su3 commutant scalar',null_dim(t)==1)
emb=[np.pad(a,((0,1),(0,1))) for a in t];Q=np.diag([1/3,1/3,1/3,-1])
check('su3 commutant on 3+1 has dimension two',null_dim(emb)==2)
check('Q commutes with chosen block',all(eq(Q@a,a@Q) for a in emb))
check('Q constant on three-block',eq(Q[:3,:3],np.eye(3)/3))
charges=sorted(Q[i,i]+Q[j,j] for i in range(4) for j in range(i+1,4))
check('exterior square charges',np.allclose(charges,[-2/3]*3+[2/3]*3))
C=np.array([[0,0,1],[1,0,0],[0,1,0]]);H=C+C.T
check('cyclic SU3 element',eq(C.T@C,np.eye(3)) and abs(np.linalg.det(C)-1)<1e-10)
check('cyclic commutant dimension three',null_dim([C])==3)
check('Hermitian nonscalar cyclic counterexample',eq(H,H.T) and eq(H@C,C@H) and not eq(H,np.eye(3)*np.trace(H)/3))
check('counterexample equal diagonals distinct eigenvalues',np.allclose(np.diag(H),0) and np.allclose(np.linalg.eigvalsh(H),[-1,-1,2]))
check('each cyclic commutant basis element has equal diagonals',all(np.allclose(np.diag(a),np.diag(a)[0]) for a in [np.eye(3),C,C@C]))
for k,v in checks.items():print(('PASS' if v else 'FAIL')+': '+k)
print('Finite matrix residual/rank checks only; supplied group, block and charge choices; physical identifications open.')
print('Resolution scope and limits (not physical bridge or no-go certificates):')
print('per_element: six supplied 8x8 Clifford matrices, their 36 anticommutators and 64 monomial-span rank; finite numerical residuals only.')
print('per_block: two supplied 4D chirality blocks and a chosen 3+1 embedding; no physical block selection derived.')
print('per_mode: six supplied Clifford generators, not a physical mode spectrum or generation count.')
print('per_site: no site-resolved dynamics or physical site assignment calculated.')
print('lattice_wide: no full-lattice embedding, continuum limit or universal physical exclusion tested.')
raise SystemExit(0 if all(checks.values()) else 1)
