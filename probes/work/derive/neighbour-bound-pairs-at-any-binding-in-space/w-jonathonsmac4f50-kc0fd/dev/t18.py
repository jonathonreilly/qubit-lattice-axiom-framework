from t8 import *
up=np.array([1,0],complex); dn=np.array([0,1],complex)
UU=np.kron(up,up); DD=np.kron(dn,dn)
Ppm=np.outer(UU,UU.conj())+np.outer(DD,DD.conj())
Mall=build_M_all(Ppm)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
for tabs_ in [tabs[:10]]:
    for tab in tabs_:
        gl=levels_tab(tab,M24)
        s=[]
        for g in gl:
            o=weights_tab(tab,g,M24)
            if o is None: continue
            ev=np.linalg.eigvalsh(o['Wsum'])
            s.append((round(g,4),o['null'],round(ev.min(),3),round(ev.max(),3),round(o['gap'],3)))
        print('E-EC=%.4f'%(tab['E']-EC),s)
