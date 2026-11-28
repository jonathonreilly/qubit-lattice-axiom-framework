#!/usr/bin/env python3
"""A scaled Taylor action; diagnostic only unless its controls pass."""
import guard
import os
for key in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS","BLIS_NUM_THREADS"):
    os.environ[key]="1"
import math
import numpy as np

def taylor(X,b,x):
    shift=6*b
    term=math.exp(-shift)*x
    result=term.copy()
    weight=math.exp(-shift)
    k=0
    while True:
        k+=1
        term=(b/k)*(X@term)
        result+=term
        weight*=shift/k
        if k>shift and weight<1e-20:break
        if k>400:raise RuntimeError('Taylor degree limit')
    return result

if __name__=='__main__':
    from cube import *
    from scipy.sparse import eye
    import sys
    dest=Path(sys.argv[1]);checks=[]
    for sector in (0,1,2,4,5,6):
      X=load_npz(dest/f'sector{sector}.npz')
      for b in (2.4,4.):
        x=np.sin(np.arange(X.shape[0])+.5);x/=np.linalg.norm(x)
        V=b*X-6*b*eye(X.shape[0],format='csr')
        ref=expm_multiply(V,x,traceA=float(V.diagonal().sum()))
        y=taylor(X,b,x)
        rel=float(np.linalg.norm(y-ref)/np.linalg.norm(ref))
        print(sector,b,rel,flush=True);checks.append(rel)
    assert max(checks)<2e-12,max(checks)
    print('ALL CONTROLS PASS',max(checks))
