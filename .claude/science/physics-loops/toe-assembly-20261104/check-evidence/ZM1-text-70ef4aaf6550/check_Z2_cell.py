# Lemma Z2.0, Z2.1, Z2.2: tested from the statements. Controls perturb the statement.
import numpy as np, itertools
from scipy.linalg import expm
from check_common import *
rng=np.random.default_rng(1)
A,Z,Gm=AZG(); I=np.eye(8)
six=A+Gm
e=max(nrm(X@X-I) for X in six); e2=max(nrm(X-X.conj().T) for X in six)
e3=max(nrm(X@Y+Y@X) for a,X in enumerate(six) for b,Y in enumerate(six) if a<b)
print("Z2.0(1) involution/herm/anticomm residuals",e,e2,e3)
# control: without the eta signs the matchings commute instead
A0=[np.abs(a) for a in A]; print("  control (no signs) anticomm residual",nrm(A0[0]@A0[1]+A0[1]@A0[0]))
mx=0;mx3=0;mxD=0
for _ in range(200):
    K=rng.uniform(-np.pi,np.pi,3); eps=rng.uniform(0.01,1.56)
    Re=Rfib(K,'e'); Ro=Rfib(K,'o')
    Ro_f=sum(np.cos(K[j])*A[j]-np.sin(K[j])*Gm[j] for j in range(3))/np.sqrt(3)
    mx=max(mx,nrm(Re-sum(A)/np.sqrt(3)),nrm(Ro-Ro_f))
    D=Ro-Re; V=Vfib(K,eps)
    mx3=max(mx3,nrm(V-(I+1j*np.sin(eps)*D@expm(-1j*eps*Re))))
    mxD=max(mxD,abs(nrm(D)-2/np.sqrt(3)*np.sqrt(sum(np.sin(K/2)**2))))
print("Z2.0(2) max residual",mx," Z2.0(3) V formula",mx3," ||D|| formula",mxD)
K=np.array([.3,-.7,1.1]); Ro_bad=sum(np.cos(K[j])*A[j]+np.sin(K[j])*Gm[j] for j in range(3))/np.sqrt(3)
print("  control (+sin sign) residual",nrm(Rfib(K,'o')-Ro_bad))
# B10 premise as used: V+V* scalar, cos w = a chi - b
for mu,eps in [(0,0.7),(0.4,0.9)]:
    K=rng.uniform(-np.pi,np.pi,3); V=Vfib(K,eps,mu); a=(np.cos(mu)-np.cos(2*eps))/2;b=(-np.cos(2*eps)-np.cos(mu))/2
    print("  B10 use: ||V+V*-2(a chi-b)||",nrm(V+V.conj().T-2*(a*np.mean(np.cos(K))-b)*I))
# Z2.1
worst=0;worstC=0;wa=0;wn=0;wctl=0
for eps in [0.05,0.3,0.7,1.2,1.5,1.5607]:
    G,C=GC(eps); s=np.sin(eps); c=np.cos(eps); v=s/np.sqrt(3)
    wa=max(wa,max(nrm(G[j]@G[k]+G[k]@G[j]-2*(j==k)*I) for j in range(3) for k in range(3)),
           max(nrm(G[j]-G[j].conj().T) for j in range(3)),max(nrm(C[j]-C[j].conj().T) for j in range(3)),
           max(nrm(G[j]@C[k]+C[k]@G[j]) for j in range(3) for k in range(3)))
    wn=max(wn,max(abs(nrm(C[j])-s/(2*np.sqrt(3))*np.sqrt(c*c+2*s*s/3)) for j in range(3)))
    for _ in range(300):
        K=rng.normal(size=3); K*=rng.uniform(1e-2,1)/np.linalg.norm(K); k=np.linalg.norm(K)
        h=hfib(K,eps); h1=v*sum(K[j]*G[j] for j in range(3)); h2=sum(K[j]**2*C[j] for j in range(3))
        worst=max(worst,nrm(h-h1-h2)/k**3)
        # control: wrong C_j (drop the A_jA_k part) -> remainder/|K|^3 blows up at small K
    K=np.array([1,2,-1.5])*1e-2; k=np.linalg.norm(K)
    Cb=[s/(2*np.sqrt(3))*c*A[j] for j in range(3)]
    wctl=max(wctl,nrm(hfib(K,eps)-v*sum(K[j]*G[j] for j in range(3))-sum(K[j]**2*Cb[j] for j in range(3)))/k**3)
print("Z2.1(1),(3) algebra residual",wa," norm-formula residual",wn)
print("Z2.1(2) max ||r3||/|K|^3 over |K|<=1:",worst,"(claimed <=0.5)   control with wrong C_j at |K|~0.027:",wctl)
# Z2.2
w1=0;w2=0;w3=0
for eps in [0.05,0.7,1.5]:
    G,C=GC(eps); v=np.sin(eps)/np.sqrt(3)
    for _ in range(100):
        th=rng.uniform(-np.pi,np.pi,3)
        Y=Ytr(th,eps); h1=v*sum(th[j]*G[j] for j in range(3))
        w1=max(w1,nrm(Y-Y.conj().T),nrm(1j*(Y@h1-h1@Y)-sum(th[j]*np.sin(th[j])*C[j] for j in range(3))))
        w2=max(w2,nrm(Y)-0.25*sum(abs(np.sin(th))))
        Yl=1j/(2*v)*sum(th[j]*G[j]@C[j] for j in range(3))
        w1=max(w1,nrm(1j*(Yl@h1-h1@Yl)-sum(th[j]**2*C[j] for j in range(3))))
print("Z2.2(1) residual",w1," Z2.2(2) max(||Ytr||-(1/4)sum|sin|) (must be <=0):",w2)
# Z2.2(3): find sign lifts by brute force for two generators of O, then test covariance
def perm_mats():
    out=[]
    for p in itertools.permutations(range(3)):
        for sg in itertools.product((1,-1),repeat=3):
            Q=np.zeros((3,3),int)
            for j in range(3): Q[p[j],j]=sg[j]
            if round(np.linalg.det(Q))==1: out.append(Q)
    return out
c0=np.array([.5,.5,.5])
def lift(Q):
    Kt=np.array([.37,-1.1,.83]); found=[]
    P=np.zeros((8,8))
    for r in RES:
        g=tuple(int(round(x)) for x in Q@(np.array(r)-c0)+c0); P[IDX[g],IDX[r]]=1
    for sg in itertools.product((1,-1),repeat=7):
        S=P@np.diag((1,)+sg)
        if all(nrm(S@Rfib(Kt,T)@S.T-Rfib(Q@Kt,T))<1e-10 for T in 'eo'): found.append(S)
    return found
nl=[];wc=0;wctl=0
for Q in perm_mats():
    L=lift(Q); nl.append(len(L)); S=L[0]
    for eps in [0.3,1.1]:
        th=rng.uniform(-np.pi,np.pi,3)
        wc=max(wc,nrm(S@Ytr(th,eps)@S.T-Ytr(Q@th,eps)), nrm(S@Vfib(th,eps)@S.T-Vfib(Q@th,eps)))
        wctl=max(wctl,nrm(S@Ytr(th,eps)@S.T-Ytr(th,eps)))
print("Z2.2(3): sign lifts found per rotation (with s(000)=+1):",sorted(set(nl)),"count",len(nl)," covariance residual",wc," control (no Q on theta) max",wctl)
