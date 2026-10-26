from t8 import *
import time
up=np.array([1,0],complex); dn=np.array([0,1],complex)
UU=np.kron(up,up); DD=np.kron(dn,dn)
Ppm=np.outer(UU,UU.conj())+np.outer(DD,DD.conj())
Mall=build_M_all(Ppm)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
out=[]
for dl,N in ((0.02,120),(0.01,140),(0.005,180),(0.0025,240)):
    t=time.time()
    tab=make_tab(EC+dl,N)
    gl=levels_tab(tab,M24)
    s=[]
    for g in gl:
        o=weights_tab(tab,g,M24)
        if o is None: continue
        ev=np.linalg.eigvalsh(o['Wsum'])
        s.append((round(g,6),o['null'],round(ev.min(),5),round(ev.max(),5),round(o['gap'],3)))
    print('dl',dl,'N',N,'time',round(time.time()-t,1),s,flush=True)
