from t8 import *
import time
c=np.load('example_c.npy'); Es,gs=eval(open('example_vals.txt').read().replace('np.float64',''))
Mz=Mof(c); Mall=build_M_all(Mz)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
V=gs*M24
N=72
print('E*',Es,'g*',gs)
r0=roots_near(Es,V,N,(0,0,0),width=0.03,npts=5)
print('K=0 roots',r0)
for K in ((0,0,0.1),(0,0,0.2),(0.1,0,0)):
    t=time.time()
    rt=roots_near(Es,V,N,K,width=0.03,npts=7)
    tt=max(abs(x) for x in K)
    dd=[(r-Es)*2/tt**2 for r in rt]
    print('K',K,'roots',rt,'E-d2',np.round(dd,5),'sum E0*E2 =',Es*sum(dd),'time',time.time()-t,flush=True)
