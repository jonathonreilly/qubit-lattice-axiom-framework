import numpy as np
from scipy.optimize import brentq
from t72_kappa_scan import W_of
for lam in (0.1,0.15,0.2,0.3,0.45,0.6):
    ks=np.linspace(-3,1,17)
    fs=[W_of(lam,k)[0]-1 for k in ks]
    roots=[]
    for a,b,fa,fb in zip(ks[:-1],ks[1:],fs[:-1],fs[1:]):
        if fa*fb<0:
            roots.append(round(brentq(lambda k:W_of(lam,k)[0]-1,a,b,xtol=1e-4),4))
    print(f"lam={lam}: W-1 on kappa grid [-3..1]:",np.round(fs,3).tolist()[:17:2],"roots:",roots,flush=True)
