from e7 import *
OFF,Sm=d4cone();C=CA(OFF,Sm)
d=np.array([.3,-.5,.6,.55]);d/=np.linalg.norm(d)
def Lmat(Tl,Tr,q,be):
    out=np.zeros((len(Tl),len(Tr)),complex)
    for i,a in enumerate(Tl):
        for j,b in enumerate(Tr):
            a2=a/2;b2=b/2
            out[i,j]=(be/1)*1j*( (q@np.diag(a2))*np.trace(b2) - np.trace(a2)*(q@np.diag(b2)) )
    return out
for kap in (0,1/24):
  be=4/3 if kap==0 else 2
  for t in (.02,.01,.005):
    q=t*d;K,Tl,Tr,w,wm,g1,g2=Kc(C,q+0j,kap)
    D=K-F0(Tl,Tr,-4,be);L=Lmat(Tl,Tr,q,be)
    print(kap,t,'|D|',np.linalg.norm(D),'|L|',np.linalg.norm(L),'|D-L|/|L|',np.linalg.norm(D-L)/np.linalg.norm(L))
# beta(kappa)
for kap in (0,1/48,1/36,1/24,1/16,1/12):
    q=.01*d;K,Tl,Tr,w,wm,g1,g2=Kc(C,q+0j,kap)
    X=np.array([[np.sum((a/2)*(b/2)),np.sum(wm*np.diag(a/2))*np.sum(w*np.diag(b/2))] for a in Tl for b in Tr])
    co=np.linalg.lstsq(X,K.ravel(),rcond=None)[0]
    print('kappa',kap,co,'pred beta',2-(2/3)*(1-24*kap)**2)
# source fit residual (T basis, lstsq) reproduction
for kap in (0,1/24):
  for t in (.02,.01):
    q=t*d;K,Tl,Tr,w,wm,g1,g2=Kc(C,q+0j,kap)
    X=np.array([[np.sum((a/2)*(b/2)),np.trace(a/2)*np.trace(b/2)] for a in Tl for b in Tr])
    co=np.linalg.lstsq(X,K.ravel(),rcond=None)[0];print(kap,t,'fit res',np.linalg.norm(X@co-K.ravel())/np.linalg.norm(K.ravel()))
