exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
import itertools
GROUP=[]
def sym(Xm, Qmom=False, inversion=False):
    Y=np.zeros_like(Xm)
    for (P,s),t in zip(trans,TV): Y+=((-1.0)**sum(t) if Qmom else 1.0)*conj(Xm,P,s)
    Z=np.zeros_like(Xm)
    for P,s in rots: Z+=conj(Y,P,s)
    if inversion:
        Z2=conj(Z,*invs[0]); Z=(Z+Z2)/2
    return Z
rng=np.random.default_rng(3)
# Weyl Hamiltonian model (C19): H0(-1,0.2) + 0.05 X with X a random conj-odd O x I invariant range<=1 term
nbr=[C.VID[(tuple(x%L for x in d),c)] for d in [(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)] for c in C.CORNERS]
A=np.zeros((nV,nV))
for i in loc0:
    for j in nbr:
        v,w=C.VERTS[i][0],C.VERTS[j][0]; dd=[abs(dmod(y-x)) for x,y in zip(v,w)]
        if i!=j and sum(dd)<=1: A[i,j]=rng.normal()
A=A-A.T; X=sym(1j*A,inversion=True); X/=np.abs(X).max()
Hb=H0(-1.0,0.2)+0.05*X
def Bloch(k):
    B=np.zeros((nV,12),complex)
    for a,(v,c) in enumerate(C.VERTS): B[a,CI[c]]=np.exp(1j*np.dot(k,v))/np.sqrt(L**3)
    return B
ex=np.array([np.pi,0,0])
pts={"k*":kst,"k*+pi ex":kst+ex}
Bf={nm:np.hstack([Bloch(k),Bloch(k+np.pi*np.ones(3))]) for nm,k in pts.items()}
# levels at nu=1 boundary: report lowest 4 folded levels
for trial in range(3):
    S0=np.zeros((nV,nV),complex)
    S0[np.ix_(loc0,nbr)]=rng.normal(size=(12,len(nbr)))+1j*rng.normal(size=(12,len(nbr)))
    Ms=sym(S0+S0.conj().T,Qmom=True,inversion=True); Ms/=np.abs(Ms).max()
    for eps in (0.0,0.05,0.1):
        out=[]
        for nm,B in Bf.items():
            e=np.linalg.eigvalsh(B.conj().T@(Hb+eps*Ms)@B); out.append((nm,np.round(e[:4],4)))
        print(f"trial {trial} eps {eps}:",out)
print("---- O-only (no inversion) staggered terms")
def folded_H(M,k,eps):
    B=np.hstack([Bloch(k),Bloch(k+np.pi*np.ones(3))]); return B.conj().T@(Hb+eps*M)@B
for trial in range(3):
    S0=np.zeros((nV,nV),complex)
    S0[np.ix_(loc0,nbr)]=rng.normal(size=(12,len(nbr)))+1j*rng.normal(size=(12,len(nbr)))
    Ms=sym(S0+S0.conj().T,Qmom=True,inversion=False); Ms/=np.abs(Ms).max()
    eps=0.05
    for nm,k in pts.items():
        e=np.linalg.eigvalsh(folded_H(Ms,k,eps))[:4]
        # dispersion near point: min gap between level 2 and 3 (indices 1,2) in a small sphere
        gaps=[]
        for d in DIRS[:20]:
            for r in (0.01,0.03,0.06):
                ee=np.linalg.eigvalsh(folded_H(Ms,k+r*d,eps)); gaps.append(ee[2]-ee[1])
        print(f"trial {trial} {nm}: levels {np.round(e,4)}  min(E3-E2) within r<=0.06: {min(gaps):.4f}")
