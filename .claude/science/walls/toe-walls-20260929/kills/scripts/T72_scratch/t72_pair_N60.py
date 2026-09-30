import numpy as np
from t72_stag_pair_direct import direct_pair
from t72_stag_pairband import W_pair_band
for N in (30,60):
    for lam in (0.4,):
        Wd,E,*_=direct_pair(N,lam,1.0,1.0,0.0,True)
        Wb=W_pair_band(60,lam,1.0,1.0,0.0)[0]
        print(f"N={N} lam={lam}: W_direct={Wd:.5f}  W_band={Wb:.5f} ratio={Wd/Wb:.4f}", flush=True)
