"""Static susceptibilities in all on-site particle-hole channels (12x12 corner matrices) at Q = 0 and Q = (pi,pi,pi),
for the corner Weyl-pair model with the chemical potential at the node; leading channel classified by symmetry."""
import itertools, sys, numpy as np
from diraclib import *
def build(params):
    t1,t2,dX,xvec=params
    Hr=H0(t1,t2)+dX*np.tensordot(xvec,Xb,1)
    return blocks_from(Hr), Hr
# orthonormal Hermitian basis of 12x12: real symmetric (78) and imaginary antisymmetric (66)
basis=[];kinds=[]
for i in range(12):
    for j in range(i,12):
        M=np.zeros((12,12),complex)
        if i==j: M[i,i]=1
        else: M[i,j]=M[j,i]=1/np.sqrt(2)
        basis.append(M); kinds.append('real')
for i in range(12):
    for j in range(i+1,12):
        M=np.zeros((12,12),complex); M[i,j]=-1j/np.sqrt(2); M[j,i]=1j/np.sqrt(2); basis.append(M); kinds.append('imag')
Bm=np.array(basis)                      # (144,12,12)
# site-0 PSG matrices (corner space) for character analysis
def site_mat(k):
    P,s=rots[k]; M=np.zeros((12,12))
    for bi,j in enumerate(loc0):
        i=P[j]; ci=[x for x in range(12) if loc0[x]==i][0]; M[ci,bi]=(-1.0)**s[j]
    return M
SM=[site_mat(k) for k in range(24)]
def w1(R):
    p=[C.DIRS.index(C.rot_dir(R,d)) for d in C.DIRS]; s=1
    for i in range(6):
        while p[i]!=i:
            j=p[i]; p[i],p[j]=p[j],p[i]; s=-s
    return 0 if s==1 else 1
W1=[w1(R) for R in C.ROTS]
def chi_matrix(bl, mu, Qv, N=12, T=0.01):
    ks=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,N,endpoint=False),repeat=3)))+0.037
    chi=np.zeros((144,144),complex)
    for k in ks:
        e1,v1=np.linalg.eigh(Hk(bl,k)); e2,v2=np.linalg.eigh(Hk(bl,k+Qv))
        f1=1/(np.exp((e1-mu)/T)+1); f2=1/(np.exp((e2-mu)/T)+1)
        de=e2[None,:]-e1[:,None]; df=f1[:,None]-f2[None,:]
        with np.errstate(divide='ignore',invalid='ignore'):
            W=np.where(np.abs(de)>1e-9, df/de, (f1*(1-f1)/T)[:,None]*np.ones_like(de))
        Om=np.einsum('in,aij,jm->anm',v1.conj(),Bm,v2)     # <n k|O_a|m k+Q>
        chi+=np.einsum('anm,nm,bnm->ab',Om,W,Om.conj())
    chi/=len(ks)
    return (chi+chi.conj().T)/2
def classify(vec):
    M=np.tensordot(vec,Bm,1); M=(M+M.conj().T)/2
    re=np.linalg.norm(M.real); im=np.linalg.norm(M.imag)
    # O character: <M, R M R^T> averaged; for an irreducible channel the character sign pattern
    a1=np.mean([np.real(np.vdot(M,SM[k]@M@SM[k].T))/np.real(np.vdot(M,M)) for k in range(24)])
    a2=np.mean([(-1)**W1[k]*np.real(np.vdot(M,SM[k]@M@SM[k].T))/np.real(np.vdot(M,M)) for k in range(24)])
    tr=abs(np.trace(M))
    return dict(real=round(re,3),imag=round(im,3),A1_weight=round(a1,3),A2_weight=round(a2,3),trace=round(tr,3))
if __name__=='__main__':
    rng=np.random.default_rng(11); xv=rng.normal(size=len(Xb)); xv/=np.linalg.norm(xv)
    X=np.tensordot(xv,Xb,1); xv=xv/np.abs(X).max()
    bl,Hr=build((-1.0,0.2,0.05,xv))
    mu=np.linalg.eigvalsh(Hk(bl,kst))[0]
    for name,Qv in (('Q=0',np.zeros(3)),('Q=(pi,pi,pi)',Q)):
        chi=chi_matrix(bl,mu,Qv)
        # exclude the site-charge (identity) channel: repulsive Hartree
        Pid=np.eye(144); idv=np.zeros(144); idv[[i for i in range(144) if kinds[i]=='real' and np.allclose(Bm[i],np.diag(np.diag(Bm[i]))) and np.trace(Bm[i])!=0]]=1
        idv=np.array([np.trace(B).real for B in Bm])/np.sqrt(12); Pr=np.eye(144)-np.outer(idv,idv)
        w,V=np.linalg.eigh(Pr@chi@Pr)
        print(name,'largest susceptibilities',np.round(w[::-1][:6],4))
        for t in range(3):
            print('   eigvec',t,classify(V[:,-1-t]))
