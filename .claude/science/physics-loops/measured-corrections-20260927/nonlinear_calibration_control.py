"""Independent full finite-S control of toy calibration-tangent signs."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import least_squares
from exact_schur_square import spectrum
K0=1.;d0=31.607246;n=np.arange(-100,101,dtype=float)
e=eigh_tridiagonal(4*n*n-4*d0,np.full(200,-2*d0),select='i',select_range=(0,6),tol=1e-12)[0];target=e[1:]-e[0]
for S in (50,100,200,500):
    def residual(z):return np.array(spectrum(S,*np.exp(z),count=3)['gaps'])-target[:2]
    fit=least_squares(residual,np.log([K0,d0]),xtol=1e-11,gtol=1e-9,ftol=1e-11)
    K,d=np.exp(fit.x);r=spectrum(S,K,d);diff=np.array(r['gaps'])-target
    print(json.dumps(dict(S=S,K=K,delta=d,calibration_error=max(abs(diff[:2])),higher_gap_differences=diff[2:].tolist(),higher_differences_over_original_x=(diff[2:]/(d0/(S*(S+1)))).tolist())),flush=True)
