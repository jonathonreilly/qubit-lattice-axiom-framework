# S2: exact/numerical checks on small periodic lattices.
import itertools, numpy as np
rng=np.random.default_rng(7)
L=4; sites=list(itertools.product(range(L),repeat=3)); idx={s:i for i,s in enumerate(sites)}; N=len(sites)
O=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=np.zeros((3,3),int)
        for i in range(3): M[i,p[i]]=s[i]
        if round(np.linalg.det(M))==1: O.append(M)
# SU(2) lift of a rotation matrix (sign irrelevant under conjugation)
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);sig=[sx,sy,sz]
def lift(R):
    from scipy.linalg import logm, expm
    w,V=np.linalg.eig(R); ax=np.real(V[:,np.argmin(abs(w-1))]); ang=np.arccos(np.clip((np.trace(R)-1)/2,-1,1))
    if ang<1e-9: return np.eye(2)
    for sgn in [1,-1]:
        n=sgn*ax/np.linalg.norm(ax); U=np.cos(ang/2)*np.eye(2)-1j*np.sin(ang/2)*sum(n[i]*sig[i] for i in range(3))
        if np.allclose(sum(np.outer([np.real(np.trace(sig[a]@U@sig[b]@U.conj().T))/2 for b in range(3)],[1])[:,0]*0 for a in [0]) ,0): pass
        Rb=np.array([[np.real(np.trace(sig[a]@U@sig[b]@U.conj().T))/2 for b in range(3)] for a in range(3)])
        if np.allclose(Rb,R): return U
    raise RuntimeError
nint=2
def bloch(hops,k):
    return sum(np.exp(1j*np.dot(k,d))*T for d,T in hops.items())
# (i) random NN translation-invariant 2x2 hoppings, group-averaged over O with spinor action -> G-covariant carrier
H0={(0,0,0):rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))}
for j in range(3):
    e=tuple(int(x) for x in np.eye(3,dtype=int)[j]); T=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    H0[e]=T; H0[tuple(-x for x in e)]=T.conj().T
H0[(0,0,0)]=H0[(0,0,0)]+H0[(0,0,0)].conj().T
Hs={}
for R in O:
    U=lift(R)
    for d,T in H0.items():
        dd=tuple(int(x) for x in R@np.array(d)); Hs[dd]=Hs.get(dd,0)+U@T@U.conj().T/len(O)
X=[np.pi*np.eye(3)[i] for i in range(3)]; M=[np.pi*(np.ones(3)-np.eye(3)[i]) for i in range(3)]
G0=np.zeros(3); R0=np.pi*np.ones(3)
evX=[np.linalg.eigvalsh(bloch(Hs,k)) for k in X]
print("(i) G-covariant spin-1/2 NN carrier: eigenvalues at X1,X2,X3:",[e.round(10).tolist() for e in evX])
print("    six-fold X multiplet (3 arms x 2):",np.allclose(evX[0],evX[1]) and np.allclose(evX[1],evX[2]) and abs(evX[0][0]-evX[0][1])<1e-10)
# (ii) NN identities for an ARBITRARY (non-symmetric) NN translation-invariant n x n carrier
n=4; Hr={(0,0,0):None}; A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); Hr[(0,0,0)]=A+A.conj().T
for j in range(3):
    e=tuple(int(x) for x in np.eye(3,dtype=int)[j]); T=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); Hr[e]=T; Hr[tuple(-x for x in e)]=T.conj().T
h=lambda k: bloch(Hr,k)
def d2(k,j,eps=1e-4):
    e=np.eye(3)[j]*eps; return (h(k+e)-2*h(k)+h(k-e))/eps**2
ok1=all(np.allclose(h(X[i])+h(M[i]),h(G0)+h(R0)) for i in range(3))
ok2=all(np.allclose(h(X[i])-h(X[j]),2*(d2(G0,i)-d2(G0,j)),atol=1e-5) for i in range(3) for j in range(3))
print("(ii) sum rule H(X_i)+H(M_i)=H(Gamma)+H(R):",ok1,"; splitting identity H(X_i)-H(X_j)=2[d_i^2 H(Gamma)-d_j^2 H(Gamma)]:",ok2)
# (iii) on-site period-2 order at M3 on the L=4 lattice: corner-to-corner matrix elements
k_of=lambda c: np.pi*np.array(c)
corners=list(itertools.product([0,1],repeat=3))
phi=lambda c: np.array([np.exp(1j*np.dot(k_of(c),s)) for s in sites])/np.sqrt(N)
V=np.array([(-1)**(s[0]+s[1]) for s in sites])  # wavevector M3=(pi,pi,0)
pairs=[(a,b) for a in corners for b in corners if a<b and abs(np.vdot(phi(a),V*phi(b)))>1e-12]
print("(iii) corner pairs coupled by an M3 order:",pairs)
# (iv) residual-symmetry theorem: common residual H acting on V_L with distinct characters -> |CKM| permutation
C=np.roll(np.eye(3),1,axis=0)
def equiv(chars_L,chars_R,P_L,P_R):
    Mx=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    # project onto Hom_H(V_R,V_L) for H=<g>, g acting by P_L on V_L and P_R on V_R (order 3)
    return sum(np.linalg.matrix_power(P_L,k)@Mx@np.linalg.matrix_power(P_R,k).conj().T for k in range(3))/3
def ckm(Mu,Md):
    _,Uu=np.linalg.eigh(Mu@Mu.conj().T); _,Ud=np.linalg.eigh(Md@Md.conj().T); return np.abs(Uu.conj().T@Ud)
V1=ckm(equiv(0,0,C,C),equiv(0,0,C,C)); print("(iv) H=C3 (distinct characters on V_L): |V| =",V1.round(8).tolist())
I3=np.eye(3); w=np.exp(2j*np.pi/3)
# H acting on V_L by a single character: no constraint -> generic CKM, generic masses
V2=ckm(equiv(0,0,w*I3,w*I3),equiv(0,0,w*I3,w*I3)); print("     H acting by one character: |V| =",V2.round(3).tolist())
# eigenvalue freedom: H=C3-equivariant Hermitian matrices realise any spectrum: build F diag(m) F^dag
F=np.array([[w**(a*b) for b in range(3)] for a in range(3)])/np.sqrt(3); m=np.array([0.000511,0.10566,1.77686])
Hm=F@np.diag(m)@F.conj().T; print("     C3-invariant Hermitian with the lepton spectrum exists:",np.allclose(C@Hm@C.T,Hm),np.linalg.eigvalsh(Hm).round(6).tolist())
