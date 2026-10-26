from t8 import *
import time
c=np.load('example_c.npy'); Es,gs=eval(open('example_vals.txt').read().replace('np.float64',''))
Mz=Mof(c); Mall=build_M_all(Mz)
for L in (6,8):
    for K in ((0,0,0),(0,0,0.1)):
        t=time.time()
        H=box_H(L,K,{r:gs*Mall[r] for r in POS})
        w=spl.eigsh(H,k=8,sigma=Es+0.02,which='LM',return_eigenvectors=False)
        w=np.sort(w.real)
        print('L',L,'K',K,'levels near E*',np.round(w,6),'time',round(time.time()-t,1),flush=True)
