import numpy as np
from scipy.optimize import brentq
from t72_kappa_scan import W_of
print("kappa*(lam): nn/contact ratio at which W_pair=1 (timed, m=beta=1, ring 48). Bracket found from grid.")
for lam,(a,b) in ((0.2,(-1.5,-1.0)),(0.3,(-1.5,-1.0)),(0.45,(-1.1,-0.6))):
    f=lambda k: W_of(lam,k)[0]-1
    fa,fb=f(a),f(b)
    if fa*fb<0:
        k=brentq(f,a,b,xtol=1e-4); W,E0=W_of(lam,k)
        print(f"lam={lam:4.2f}: kappa*={k:8.4f}  W={W:.5f}  B={2-E0:.4f}")
    else:
        print(f"lam={lam}: bracket fails f(a)={fa:.3f} f(b)={fb:.3f}")
