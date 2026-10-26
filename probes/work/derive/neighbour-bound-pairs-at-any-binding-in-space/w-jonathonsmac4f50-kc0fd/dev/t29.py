from t22 import *
import sys
for a in (0.25,0.75):
    M=proj(UU)+proj(DD)+a*proj(S)
    Mall=build_M_all(M)
    M24=np.zeros((24,24),complex)
    for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
    print('a=',a)
    for tab in tabs[::2]:
        gl=levels_tab(tab,M24)
        s=[]
        for g in gl:
            if abs(g-tab['E'])<1e-6:   # dark triplet E=g
                o=weights_tab(tab,g,M24)
                ev=np.linalg.eigvalsh(o['Wsum']); s.append((round(g,4),o['null'],round(ev.max(),4),round(o['gap'],3)))
        print(' E=%.4f'%tab['E'],s)
