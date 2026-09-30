"""Independent rebuild of the base x fibre embedding and the N_g=1 Fock census (kill check T54).
Different construction from the attack: colour SU(3) built on the symmetric triplet from an explicit
orthonormal basis, weak SU(2) on the last qubit, Y = 1/3 on Sym x C^2, -1 on Anti x C^2.
Fock space via explicit occupation-number basis (no Jordan-Wigner matrices), sparse."""
import itertools, numpy as np, scipy.sparse as sp
s=1/np.sqrt(2)
# base basis |b1 b2>: index 2*b1+b2 ; sym triplet = |00>, (|01>+|10>)/sqrt2, |11>; anti = (|01>-|10>)/sqrt2
E=np.zeros((4,4))
E[0,0]=1; E[1,1]=s; E[2,1]=s; E[3,2]=1; E[1,3]=s; E[2,3]=-s   # columns: sym1, sym2, sym3, anti
gm=[np.array(m,dtype=complex) for m in (
 [[0,1,0],[1,0,0],[0,0,0]],[[0,-1j,0],[1j,0,0],[0,0,0]],[[1,0,0],[0,-1,0],[0,0,0]],
 [[0,0,1],[0,0,0],[1,0,0]],[[0,0,-1j],[0,0,0],[1j,0,0]],[[0,0,0],[0,0,1],[0,1,0]],
 [[0,0,0],[0,0,-1j],[0,1j,0]],np.diag([1,1,-2])/np.sqrt(3))]
T=[]
for g in gm:
    M=np.zeros((4,4),complex); M[:3,:3]=g/2
    T.append(np.kron(E@M@E.conj().T,np.eye(2)))
sig=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
J=[np.kron(np.eye(4),x/2) for x in sig]
Psym=E@np.diag([1,1,1,0])@E.conj().T
Y=np.kron(Psym/3-(np.eye(4)-Psym),np.eye(2))
# checks
comm=max(np.abs(a@b-b@a).max() for a in T for b in J+[Y])
print("commutation colour vs weak/Y:",comm)
C3=sum(t@t for t in T); C2=sum(j@j for j in J)
print("colour Casimir eigenvalues:",np.round(np.linalg.eigvalsh(C3),4))
print("weak Casimir eigenvalues:",np.round(np.linalg.eigvalsh(C2),4))
print("Tr Y:",np.trace(Y).real)
# joint singlet count in single-particle space
S=sum(g.conj().T@g for g in T+J+[Y]); print("single-particle gauge singlets:",int((np.linalg.eigvalsh(S)<1e-9).sum()))
# Cl+(3) SU(2) alternative (CL3_SM_EMBEDDING_THEOREM): staggered Gammas
X=np.array([[0,1],[1,0]]);Z=np.diag([1,-1]);I2=np.eye(2)
G=[np.kron(np.kron(X,I2),I2),np.kron(np.kron(Z,X),I2),np.kron(np.kron(Z,Z),X)]
Jc=[0.5j*G[1]@G[2],0.5j*G[2]@G[0],0.5j*G[0]@G[1]]
print("Cl+(3) SU(2): Casimir eigenvalues",np.round(np.linalg.eigvalsh(sum(j@j for j in Jc)),4),
      " [J1,J2]-iJ3:",np.abs(Jc[0]@Jc[1]-Jc[1]@Jc[0]-1j*Jc[2]).max())
# Fock space, occupation basis, sparse one-body operators
n=8
def onebody(M):
    rows=[];cols=[];vals=[]
    dim=2**n
    for st in range(dim):
        occ=[(st>>i)&1 for i in range(n)]
        for j in range(n):
            if not occ[j]: continue
            for i in range(n):
                if abs(M[i,j])<1e-14: continue
                if i!=j and occ[i]: continue
                # c_i^dag c_j with fermion sign
                sgn=1
                sgn*=(-1)**sum(occ[:j])
                occ2=list(occ); occ2[j]=0
                sgn*=(-1)**sum(occ2[:i])
                occ2[i]=1
                st2=sum(b<<k for k,b in enumerate(occ2))
                rows.append(st2);cols.append(st);vals.append(M[i,j]*sgn)
    return sp.csr_matrix((vals,(rows,cols)),shape=(dim,dim),dtype=complex)
Tq=[onebody(t) for t in T]; Jq=[onebody(j) for j in J]; Yq=onebody(Y)
N=np.array([bin(s_).count('1') for s_ in range(2**n)])
C3q=sum(t@t for t in Tq); C2q=sum(j@j for j in Jq)
print("\nFull decomposition by particle number k: (C3, j(j+1), Y) -> number of states")
for k in range(n+1):
    idx=np.where(N==k)[0]
    H=(C3q+0.37*C2q+0.11*Yq)[idx][:,idx].toarray()
    w,v=np.linalg.eigh(H)
    C3k=C3q[idx][:,idx].toarray(); C2k=C2q[idx][:,idx].toarray(); Yk=Yq[idx][:,idx].toarray()
    cnt={}
    for c in range(len(idx)):
        x=v[:,c]
        key=(round(float((x.conj()@C3k@x).real),3)+0.0,round(float((x.conj()@C2k@x).real),3)+0.0,round(float((x.conj()@Yk@x).real),3)+0.0)
        cnt[key]=cnt.get(key,0)+1
    cs={kk:vv for kk,vv in cnt.items() if abs(kk[0])<1e-6}
    print(f" k={k}: colour-singlet (C3=0) states:",cs)
