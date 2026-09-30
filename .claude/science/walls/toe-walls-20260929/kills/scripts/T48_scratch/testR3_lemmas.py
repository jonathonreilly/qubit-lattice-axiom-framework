"""R3 lemmas: (i) commutant of the S3 permutation rep on the hw=1 triplet is span{I,J}; (ii) Jarlskog identity |det[Hu,Hd]| = 2 |J| prod|dl_u| prod|dl_d|."""
import numpy as np, itertools
P=[np.array([[1.0 if j==p[i] else 0.0 for j in range(3)] for i in range(3)]) for p in itertools.permutations(range(3))]
# commutant dimension over C: solve [X,g]=0 for all g
rows=[]
for g in P:
    # vec(Xg - gX) = (g^T kron I - I kron g) vec(X)
    rows.append(np.kron(g.T,np.eye(3))-np.kron(np.eye(3),g))
A=np.vstack(rows); s=np.linalg.svd(A,compute_uv=False)
print("commutant complex dimension of S3 perm rep =", int(np.sum(s<1e-10)), "(expect 2 = span{I,J})")
# Hermitian commutant real dimension is also 2
rng=np.random.default_rng(0)
ratios=[]
for _ in range(2000):
    A_=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); Hu=A_+A_.conj().T
    B_=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); Hd=B_+B_.conj().T
    wu,Uu=np.linalg.eigh(Hu); wd,Ud=np.linalg.eigh(Hd)
    V=Uu.conj().T@Ud
    J=np.imag(V[0,0]*V[1,1]*np.conj(V[0,1])*np.conj(V[1,0]))
    dU=np.prod([wu[i]-wu[j] for i,j in ((0,1),(0,2),(1,2))]); dD=np.prod([wd[i]-wd[j] for i,j in ((0,1),(0,2),(1,2))])
    C=Hu@Hd-Hd@Hu
    ratios.append(abs(np.linalg.det(C))/(abs(J)*abs(dU)*abs(dD)))
print("Jarlskog commutator identity: |det[Hu,Hd]| / (|J| prod|dl_u| prod|dl_d|) min,max =",min(ratios),max(ratios))
