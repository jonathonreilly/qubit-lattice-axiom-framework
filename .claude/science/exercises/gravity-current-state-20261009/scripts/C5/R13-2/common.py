# R13-2 common: orthonormal 6-component symmetric-tensor basis, cubic group rep, N-type symbols (as R12-5 s2 / R11-2).
import numpy as np, itertools
idx=[(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
Bs=[]
for (i,j) in idx:
    M=np.zeros((3,3))
    if i==j: M[i,i]=1
    else: M[i,j]=M[j,i]=1/np.sqrt(2)
    Bs.append(M)
def vec(M): return np.array([np.sum(M*b) for b in Bs])
def mat(v): return sum(c*b for c,b in zip(v,Bs))
eps=np.zeros((3,3,3))
for a,b,c in [(0,1,2),(1,2,0),(2,0,1)]: eps[a,b,c]=1; eps[a,c,b]=-1
def Vmap(q): return np.column_stack([vec(0.5*(np.outer(q,e)+np.outer(e,q))) for e in np.eye(3)])  # sym grad: alpha -> h
def Svec(q): return vec(np.dot(q,q)*np.eye(3)-np.outer(q,q))
def Rmap(q): return np.column_stack([vec(np.einsum('iab,jcd,a,c,bd->ij',eps,eps,q,q,b)) for b in Bs])
trv=vec(np.eye(3))
def KN(lam=0.5): return np.eye(6)-lam*np.outer(trv,trv)   # E:E - lam (trE)^2
# cubic group O_h: 48 signed permutation matrices
G48=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        R=np.zeros((3,3))
        for i in range(3): R[i,p[i]]=s[i]
        G48.append(R)
def D6(R): return np.column_stack([vec(R@b@R.T) for b in Bs])
D48=[D6(R) for R in G48]
# C4v sectors at k || z (orthonormal vectors in the 6-basis)
xx,yy,zz,xy,yz,xz=np.eye(6)
SECT={'B1(TT xx-yy)':[ (xx-yy)/np.sqrt(2)], 'B2(TT xy)':[xy], 'E(vector xz,yz)':[xz,yz], 'A1(scalar zz, xx+yy)':[zz,(xx+yy)/np.sqrt(2)]}
def omegas(H):
    n=H.shape[0]//2; J=np.block([[np.zeros((n,n)),np.eye(n)],[-np.eye(n),np.zeros((n,n))]])
    ev=np.linalg.eigvals(J@H); w=np.sort(np.abs(ev.imag)); return w[::2]  # one per +-pair (approx)
def sector_omegas(H,vecs):
    P=np.array(vecs).T; Z=np.zeros_like(P); Pf=np.block([[P,Z],[Z,P]])
    return omegas(Pf.T@H@Pf)
