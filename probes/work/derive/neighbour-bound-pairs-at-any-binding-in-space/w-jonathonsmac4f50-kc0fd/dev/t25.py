from t8 import *
from scipy.optimize import brentq
rng=np.random.default_rng(7)
cs=[]
for it in range(600):
    c=rng.normal(size=5); c/=np.linalg.norm(c); cs.append(c)
it=161
c=cs[it]; Mz=Mof(c); Mall=build_M_all(Mz)
M24=np.zeros((24,24),complex)
for i,r in enumerate(POS): M24[4*i:4*i+4,4*i:4*i+4]=Mall[r]
def Wtrip(E,gref):
    tab=make_tab(E,48)
    gl=levels_tab(tab,M24)
    cand=[]
    for g in gl:
        if abs(g-gref)<0.6:
            o=weights_tab(tab,g,M24)
            if o is not None and o['null']==3: cand.append((g,o))
    return cand[0]
f=lambda E: np.linalg.eigvalsh(Wtrip(E,9.2)[1]['Wsum']).max()-3.0
for E in (5.5,5.6,5.7,5.8,5.9,6.0):
    g,o=Wtrip(E,9.2+ (E-5.6)*2.3); print(E,g,np.linalg.eigvalsh(o['Wsum']),flush=True)
