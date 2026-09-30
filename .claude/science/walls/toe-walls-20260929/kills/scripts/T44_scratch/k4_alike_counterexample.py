"""Counterexample to 'a coupling that treats up and down alike cannot mix them':
same law g(t)=K1 + t K2 for both sectors, only the sector strength t differs.  Also the S3-commutant check."""
import numpy as np
rng=np.random.default_rng(3)
def herm(n=3):
    X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); return X+X.conj().T
K1,K2=herm(),herm()
g=lambda t:K1+t*K2
_,Uu=np.linalg.eigh(g(0.1)); _,Ud=np.linalg.eigh(g(0.5))
print("same law g(t)=K1+tK2, t_u=0.1, t_d=0.5: |V| =\n",np.round(np.abs(Uu.conj().T@Ud),3))
# with K1,K2 both S3-equivariant (in span{1,J}) they commute -> permutation
J=np.ones((3,3)); I=np.eye(3)
K1e=0.7*I+0.3*J; K2e=-0.2*I+1.1*J
_,Uu=np.linalg.eigh(K1e+0.1*K2e); _,Ud=np.linalg.eigh(K1e+0.5*K2e)
print("S3-equivariant K1,K2 (span{1,J}): |V| =\n",np.round(np.abs(Uu.conj().T@Ud),3))
# S3 commutant dimension on C^3 permutation rep
import itertools
perms=[np.eye(3)[list(p)] for p in itertools.permutations(range(3))]
# solve X P = P X for all P: dimension of commutant
rows=[]
for P in perms:
    rows.append(np.kron(np.eye(3),P)-np.kron(P.T,np.eye(3)))
A=np.vstack(rows); s=np.linalg.svd(A,compute_uv=False); print("dim commutant of S3 perm rep on C^3 =",int(np.sum(s<1e-10)))
