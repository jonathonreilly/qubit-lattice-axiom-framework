# R12-5 s2: Gaussian (small-field) spectra of ENERGETIC-constraint tensor models at generic lattice k.
#  H = 1/2 E.K.E + 1/2 h.B.h ;  hdot = K E, Edot = -B h  => omega^2 = eig(K B).
#  K = J*K_E + U * G^T G (vector penalty on E),  B = g*B_h + W * s s^T (scalar penalty on h)
#  N-type: K_E = E:E-(trE)^2/2 (weak), B_h = h:R (weak).   L-type: K_E = C^T C, B_h = R^T R (strong).
# Symbols as in R11-2 r112_symbols.py (midpoint q = 2 sin(k/2), orthonormal 6-comp tensor basis).
import numpy as np, sys
rng=np.random.default_rng(12)
idx=[(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
Bs=[]
for (i,j) in idx:
    M=np.zeros((3,3))
    if i==j: M[i,i]=1
    else: M[i,j]=M[j,i]=1/np.sqrt(2)
    Bs.append(M)
vec=lambda M: np.array([np.sum(M*b) for b in Bs])
eps=np.zeros((3,3,3))
for a,b,c in [(0,1,2),(1,2,0),(2,0,1)]: eps[a,b,c]=1; eps[a,c,b]=-1
def Vmap(q): return np.column_stack([vec(0.5*(np.outer(q,e)+np.outer(e,q))) for e in np.eye(3)])
def Svec(q): return vec(np.dot(q,q)*np.eye(3)-np.outer(q,q))
def Rmap(q): return np.column_stack([vec(np.einsum('iab,jcd,a,c,bd->ij',eps,eps,q,q,b)) for b in Bs])
def Cmap(q):
    cols=[]
    for b in Bs:
        Et=b-np.eye(3)*np.trace(b)/2; C=np.einsum('iab,a,bj->ij',eps,q,Et); cols.append(vec(0.5*(C+C.T)))
    return np.column_stack(cols)
trv=vec(np.eye(3)); KN=np.eye(6)-0.5*np.outer(trv,trv)
def PTT(q):
    A=np.hstack([Vmap(q),Svec(q)[:,None]]); Qo,_=np.linalg.qr(A); return np.eye(6)-Qo@Qo.T
out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); sys.stdout.flush(); out.append(s)
def spectrum(model,q,J=1,g=1,U=1,W=1):
    G=Vmap(q).T   # div: 3x6 (G E)
    s=Svec(q)
    if model=='N': KE,Bh=KN,-Rmap(q)
    else: KE,Bh=Cmap(q).T@Cmap(q),Rmap(q).T@Rmap(q)
    K=J*KE+U*G.T@G; B=g*Bh+W*np.outer(s,s)
    w2=np.linalg.eigvals(K@B)
    return K,B,w2
def classify(w2,tol=1e-12):
    re=w2.real; im=w2.imag
    return dict(neg=int(np.sum(re<-tol)), cplx=int(np.sum(np.abs(im)>tol)), zero=int(np.sum(np.abs(w2)<=tol)), pos=int(np.sum((re>tol)&(np.abs(im)<=tol))))
P("== A. energetic N-type (H_N + U|G|^2 + W S^2): spectrum classes at generic k, and min eig of K (kinetic) and B (potential)==")
for (U,W) in [(1,1),(10,10),(100,100),(1e4,1e4)]:
    agg={'neg':0,'cplx':0,'zero':0,'pos':0}; minK=[];minB=[]; ttlin=[]
    for t in range(200):
        k=rng.uniform(-np.pi,np.pi,3); q=2*np.sin(k/2)
        K,B,w2=spectrum('N',q,U=U,W=W)
        c=classify(w2/ (q@q)**0)  # raw
        for kk in agg: agg[kk]+=c[kk]
        minK.append(np.linalg.eigvalsh(K).min()); minB.append(np.linalg.eigvalsh(B).min())
    P(f"U=W={U:g}: over 200 random k x 6 eigenvalues of KB: {agg};  min eig K over k: {min(minK):.3f};  min eig B: {min(minB):.3f}")
P("   reading: K indefinite (det K<0 in scalar block, 09-14:262-270) => Gaussian H unbounded below at every finite U; TT block decoupled below")
d=rng.normal(size=3); d/=np.linalg.norm(d)
for model in ['N','L']:
    for (U,W) in [(1,1),(100,100)]:
        ks=[0.04,0.02,0.01,0.005]; tt=[]; others=[]
        for km in ks:
            q=2*np.sin(km*d/2); K,B,w2=spectrum(model,q,U=U,W=W)
            Pt=PTT(q); Uu,_,_=np.linalg.svd(Pt); T=Uu[:,:2]
            # TT block decoupling check
            off=np.linalg.norm((np.eye(6)-Pt)@K@Pt)+np.linalg.norm((np.eye(6)-Pt)@B@Pt)
            wtt=np.sqrt(np.abs(np.linalg.eigvals((T.T@K@T)@(T.T@B@T)).real)); tt.append(np.sort(wtt))
            others.append(classify(w2))
        tt=np.array(tt); p0=np.polyfit(np.log(ks),np.log(tt[:,0]),1)[0]; p1=np.polyfit(np.log(ks),np.log(tt[:,1]),1)[0]
        P(f"{model}-type, U=W={U}: TT exponents {p0:.3f},{p1:.3f}; TT leakage |(1-P)KP|+|(1-P)BP| at k=0.005: {off:.1e}; full-spectrum classes at k=0.005: {others[-1]}")
P("   reading: N-type energetic: TT linear but the non-TT sector has negative/complex omega^2 (unstable); L-type energetic: TT k^3, gauge directions omega^2=0 (free, not oscillators)")
open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
