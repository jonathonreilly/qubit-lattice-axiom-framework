from t22 import *
import time
Es=float(np.load('ex_E.npy')[0]); gs=Es
a=0.25
M=proj(UU)+proj(DD)+a*proj(S)
Mall=build_M_all(M)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
V=gs*M24
N=72
r0=roots_near(Es,V,N,(0,0,0),width=0.05,npts=5); print('K=0 roots',r0,flush=True)
for K in ((0,0,0.05),(0,0,0.1),(0,0,0.2),(0.1,0,0)):
    t=time.time()
    rt=roots_near(Es,V,N,K,width=0.08,npts=7)
    tt=max(abs(x) for x in K)
    dd=[(r-Es)*2/tt**2 for r in rt]
    print('K',K,'roots',rt,'E-d2',np.round(dd,5),'E0*sum =',Es*sum(dd),'time',round(time.time()-t,1),flush=True)
for L in (6,8):
    for K in ((0,0,0),(0,0,0.1)):
        H=box_H(L,K,{r:gs*Mall[r] for r in POS})
        w=np.sort(spl.eigsh(H,k=8,sigma=Es+0.02,which='LM',return_eigenvectors=False).real)
        print('box L',L,'K',K,np.round(w,6),flush=True)
