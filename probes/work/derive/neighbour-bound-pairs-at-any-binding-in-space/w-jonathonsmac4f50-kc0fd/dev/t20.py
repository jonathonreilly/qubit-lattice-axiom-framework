from t8 import *
import time
rng=np.random.default_rng(7)
cs=[]
for it in range(600):
    c=rng.normal(size=5); c/=np.linalg.norm(c); cs.append(c)
c=cs[312]
Mz=Mof(c); Mall=build_M_all(Mz)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
Npts=100
def Wtrip(E,gref=5.87):
    tab=make_tab(E,Npts)
    gl=levels_tab(tab,M24)
    cand=[]
    for g in gl:
        if abs(g-gref)<1.5:
            o=weights_tab(tab,g,M24)
            if o is not None and o['null']==3: cand.append((g,o))
    return cand[0]
from scipy.optimize import brentq
f=lambda E: np.linalg.eigvalsh(Wtrip(E)[1]['Wsum']).max()-3.0
for E in (3.53,3.5371,3.545):
    g,o=Wtrip(E); print(E,g,np.linalg.eigvalsh(o['Wsum']),f(E))
Es=brentq(f,3.5371,3.56,xtol=1e-12)
g,o=Wtrip(Es)
print('E*',repr(Es),'g*',repr(g))
np.save('example_c.npy',c)
open('example_vals.txt','w').write(repr((Es,g)))
