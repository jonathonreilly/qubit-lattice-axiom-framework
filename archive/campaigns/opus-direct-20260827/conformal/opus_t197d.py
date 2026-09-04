"""T197d - the Cl(6)/M_8 block structure, with generators that ACTUALLY generate."""
import numpy as np, itertools
from scipy.linalg import expm
s=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
def clifford(d):
    if d<=2: return [s[0],s[1]][:d]
    if d==3: return [s[0],s[1],s[2]]
    G=clifford(d-2); n=G[0].shape[0]
    out=[np.kron(g,s[2]) for g in G]
    out.append(np.kron(np.eye(n),s[0])); out.append(np.kron(np.eye(n),s[1]))
    return out
G6=clifford(6)
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]; I8={r:i for i,r in enumerate(R8)}
def cubic():
    R=[]
    for p in itertools.permutations(range(3)):
        for sg in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3))
            for i,q in enumerate(p): M[i,q]=sg[i]
            if abs(np.linalg.det(M)-1)<1e-9: R.append(M)
    return R
ROT=cubic()
def closure(gs):
    seen=[np.eye(3)]; fr=[np.eye(3)]
    for _ in range(12):
        nw=[]
        for X in fr:
            for Y in gs:
                Z=X@Y
                if not any(np.allclose(Z,W) for W in seen): seen.append(Z); nw.append(Z)
        fr=nw
        if not nw: break
    return len(seen)
g1=g2=None
for i in range(len(ROT)):
    for j in range(i+1,len(ROT)):
        if closure([ROT[i],ROT[j]])==24: g1,g2=ROT[i],ROT[j]; break
    if g1 is not None: break
print(f"T197d  CONTROL generators close to {closure([g1,g2])} of 24")
def spin_rep(R,G):
    ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    if abs(ang)<1e-9: return np.eye(G[0].shape[0],dtype=complex)
    if abs(ang-np.pi)<1e-9:
        w,v=np.linalg.eigh((R+np.eye(3))/2); ax=v[:,np.argmax(w)]
    else:
        ax=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]])/(2*np.sin(ang))
    ax=ax/np.linalg.norm(ax)
    S=[0.25*(G[(i+1)%3]@G[(i+2)%3]-G[(i+2)%3]@G[(i+1)%3]) for i in range(3)]
    return expm(-ang*sum(ax[i]*S[i] for i in range(3)))
def corner_perm(R):
    P=np.zeros((8,8))
    for r in R8:
        v=np.array(r)*2-1; w=R@v
        P[I8[tuple(((w+1)/2).astype(int))],I8[r]]=1.0
    return P
def parts(a,sg):
    Mi=np.zeros((8,8),dtype=complex); Mc=np.zeros((8,8),dtype=complex)
    for r in R8:
        t=list(r)
        if sg>0:
            if r[a]==0: t[a]=1; Mi[I8[tuple(t)],I8[r]]+=1
            else:       t[a]=0; Mc[I8[tuple(t)],I8[r]]+=1
        else:
            if r[a]==1: t[a]=0; Mi[I8[tuple(t)],I8[r]]+=1
            else:       t[a]=1; Mc[I8[tuple(t)],I8[r]]+=1
    return Mi,Mc
N=64
Gm=[]
for mu in range(3):
    Pi,Pc=parts(mu,1); Mi,Mc=parts(mu,-1)
    Gm.append(np.kron(1j*Pc+1j*Mc,G6[mu])/2.0)
L=[np.kron(corner_perm(R),spin_rep(R,G6)) for R in (g1,g2)]
M=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in Gm+L])
U,sv,Vt=np.linalg.svd(M,full_matrices=False)
d=int(np.sum(sv<=max(M.shape)*np.finfo(float).eps*sv.max()))
B=[Vt[len(Vt)-d+i].conj().reshape(N,N) for i in range(d)]
C=np.vstack([np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B])
U2,s2,V2=np.linalg.svd(C,full_matrices=False)
kc=int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
cen=[sum(V2[len(V2)-kc+i].conj()[j]*B[j] for j in range(len(B))) for i in range(kc)]
print(f"   internal symmetry dim = {d},  centre = {kc}")
rng=np.random.default_rng(3)
Z=sum(rng.normal()*(0.5*(Zc+Zc.conj().T)) for Zc in cen)
w,V=np.linalg.eigh(Z)
grp={}
for i,x in enumerate(np.round(w,6)): grp.setdefault(x,[]).append(i)
Ps=[V[:,ix]@V[:,ix].conj().T for ix in grp.values()]
sizes=[np.linalg.matrix_rank(np.array([(P@X@P).ravel() for X in B]),tol=1e-8) for P in Ps]
ms=[int(round(np.sqrt(x))) for x in sizes]
print(f"   block dims = {sorted(sizes,reverse=True)}  sum {sum(sizes)} (must be {d})")
print(f"   m_i = {sorted(ms,reverse=True)};  largest u({max(ms)})")
print()
print(f"   SM needs m >= 5:  {'M_8(C) SUFFICES -- R128 too pessimistic' if max(ms)>=5 else 'M_8(C) fails; R128 M_12 stands'}")
