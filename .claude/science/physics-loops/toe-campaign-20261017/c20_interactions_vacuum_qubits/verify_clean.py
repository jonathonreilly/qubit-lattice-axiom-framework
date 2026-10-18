import itertools, numpy as np
from diraclib import *
from scipy.optimize import minimize
import chi as CH
Xb2=np.load('Xbasis2.npy'); Rb2=np.load('Rbasis2.npy'); p=np.load('clean_params.npy')
ops=[H0(-1.0,0.0), H0(0.0,1.0)]+list(Rb2)+list(Xb2)
c=np.concatenate([[1.0],p])
Hr=np.tensordot(c,np.array(ops),1); Hr=(Hr+Hr.conj().T)/2
bl=blocks_from(Hr); f=lambda k: np.linalg.eigvalsh(Hk(bl,k))
eK,eM=f(kst),f(-kst); EN=eK[0]
print('node doublets: k* %s, -k* %s'%(np.round(eK[:3],5),np.round(eM[:3],5)))
dirs=np.random.default_rng(2).normal(size=(6,3)); dirs/=np.linalg.norm(dirs,axis=1)[:,None]
v=[(f(kst+1e-4*d)[1]-f(kst+1e-4*d)[0])/2e-4 for d in dirs]; print('Weyl velocity per direction',np.round(v,5))
G=np.array(list(itertools.product(np.linspace(-np.pi,np.pi,32,endpoint=False),repeat=3)))+0.011
E=np.array([f(k)[:3] for k in G])
def far(k): 
    return min(np.linalg.norm(((k-kk+np.pi)%(2*np.pi))-np.pi) for kk in (kst,-kst))>0.05
idx0=np.argsort(-E[:,0])[:40]; idx1=np.argsort(E[:,1])[:40]
mx=max(-minimize(lambda k:-f(k)[0],G[i],method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-14,maxiter=4000)).fun for i in idx0)
mn=min(minimize(lambda k:f(k)[1],G[i],method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-14,maxiter=4000)).fun for i in idx1)
mn2=E[:,2].min()
print('refined: max band0 - EN = %.3e ; min band1 - EN = %.3e ; min band2 - EN (grid) = %.4f'%(mx-EN,mn-EN,mn2-EN))
# pseudoscalar mass (A2 imaginary staggered, as in C19)
exec(open('../c19/dirac5.py').read().split("res={}")[0].split("def w1(R):")[0].split("Hbase=")[0].replace("from diraclib import *","").replace("import itertools",""))
def w1(R):
    pp=[C.DIRS.index(C.rot_dir(R,d)) for d in C.DIRS]; s=1
    for i in range(6):
        while pp[i]!=i:
            j=pp[i]; pp[i],pp[j]=pp[j],pp[i]; s=-s
    return 0 if s==1 else 1
W1=[w1(R) for R in C.ROTS]
def symA2(Xm):
    Y=np.zeros_like(Xm)
    for (P,s),t in zip(trans,TV): Y+=((-1.0)**sum(t))*conj(Xm,P,s)
    Z=np.zeros_like(Xm)
    for (P,s),w in zip(rots,W1): Z+=((-1.0)**w)*conj(Y,P,s)
    return Z
A_=np.random.default_rng(42).normal(size=(12,12)); A_=A_-A_.T
S=np.zeros((nV,nV),complex); S[np.ix_(loc0,loc0)]=1j*A_
Mm=symA2(S); Mm=(Mm+Mm.conj().T)/2; Mm/=np.abs(Mm).max(); blM=blocks_from(Mm)
def Hfold(k,m): return np.block([[Hk(bl,k),m*Hk(blM,k).conj().T],[m*Hk(blM,k),Hk(bl,k+Q)]])
Gf=G[::4]
for m in (0.005,0.01,0.02):
    ff=lambda k: np.linalg.eigvalsh(Hfold(k,m))
    e0=ff(kst); mD=(e0[2]-e0[1])/2
    Ef=np.array([ff(k)[:3] for k in Gf])
    i1=np.argsort(-Ef[:,1])[:20]; i2=np.argsort(Ef[:,2])[:20]
    top=max(-minimize(lambda k:-ff(k)[1],Gf[i],method='Nelder-Mead',options=dict(xatol=1e-9,maxiter=3000)).fun for i in i1)
    top=max(top,e0[1]); bot=min(minimize(lambda k:ff(k)[2],Gf[i],method='Nelder-Mead',options=dict(xatol=1e-9,maxiter=3000)).fun for i in i2); bot=min(bot,e0[2])
    print('m=%.3f: direct Dirac gap 2 m_D = %.5f ; global gap (refined) = %.5f'%(m,2*mD,bot-top))
np.save('clean_Hr.npy',Hr)
