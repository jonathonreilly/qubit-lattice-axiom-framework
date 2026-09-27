"""Exploratory exact low-spectrum Schur solve; no floating error certification."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq

def spectrum(S,K=1.,delta=1.,count=7):
    C=S*(S+1);x=delta/(K*C);n=np.arange(-S,S+1,dtype=float)
    a=1-n*(n-1)/C;b=1-n*(n+1)/C
    def f(E,j):
        lam=x*x*E/delta
        ra=(1-lam)*(2-lam)-4*x*a;rb=(1-lam)*(2-lam)-4*x*b
        if min(ra.min(),rb.min())<=0 or 1+4*x-2*lam<=0:raise ValueError('Outside positive Schur denominator/metric range')
        diagonal=4*K*n*n-4*delta*(a*a/ra+b*b/rb)
        off=-4*delta*b[:-1]**2/rb[:-1]
        eig=eigh_tridiagonal(diagonal,off,select='i',select_range=(j,j),tol=1e-12)[0][0]
        return eig-E*(1+4*x-lam)
    energies=[brentq(lambda E:f(E,j),-10*delta,4*K*(j+2)**2,xtol=1e-11) for j in range(count)]
    return dict(S=S,x=x,delta_over_K=delta/K,energies=energies,gaps=(np.array(energies[1:])-energies[0]).tolist(),root_residuals=[f(E,j) for j,E in enumerate(energies)])
if __name__=='__main__':
    for ratio in (1.,31.607246):
        for S in (20,50,120,250,500,1000):
            print(json.dumps(spectrum(S,delta=ratio)),flush=True)
