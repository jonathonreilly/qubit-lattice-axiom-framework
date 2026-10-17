from diraclib import *
import itertools
rng=np.random.default_rng(11)
X=np.tensordot(rng.normal(size=len(Xb)),Xb,1); X/=np.abs(X).max()
Hbase=H0(-1.0,0.2)+0.05*X
bl=blocks_from(Hbase); EN=np.linalg.eigvalsh(Hk(bl,kst))[0]
ev0,V0=np.linalg.eigh(Hbase); idx=np.where(np.abs(ev0-EN)<1e-6)[0]; P4=V0[:,idx]
def w1(R):
    p=[C.DIRS.index(C.rot_dir(R,d)) for d in C.DIRS]; s=1
    for i in range(6):
        while p[i]!=i:
            j=p[i]; p[i],p[j]=p[j],p[i]; s=-s
    return 0 if s==1 else 1
W1=[w1(R) for R in C.ROTS]
tsign=[(-1.0)**sum(t) for t in TV]
def sym(Xm, Qmom, a2):
    Y=np.zeros_like(Xm)
    for (P,s),t in zip(trans,TV): Y+=((-1.0)**sum(t) if Qmom else 1.0)*conj(Xm,P,s)
    Z=np.zeros_like(Xm)
    for (P,s),w in zip(rots,W1): Z+=((-1.0)**w if a2 else 1.0)*conj(Y,P,s)
    return Z
res={}
for Qmom in (True,False):
  for kind in ('real','imag'):
    vals=[]
    for trial in range(4):
        A=rng.normal(size=(12,12)); A=(A+A.T) if kind=='real' else (A-A.T)
        S=np.zeros((nV,nV),complex); S[np.ix_(loc0,loc0)]=(1 if kind=='real' else 1j)*A
        M=sym(S,Qmom,True); M=(M+M.conj().T)/2
        if np.abs(M).max()<1e-10: vals.append(None); continue
        M/=np.abs(M).max()
        w=np.linalg.eigvalsh(P4.conj().T@M@P4); vals.append(np.round(w,4))
    res[(Qmom,kind)]=vals
    print(f'A2 on-site term, momentum {"Q" if Qmom else "0"}, {kind}: projected 4x4 eigenvalues', vals)
