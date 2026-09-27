"""Central-difference toy calibration check, independent of author HF derivatives."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import json,numpy as np
from scipy.linalg import eigh_tridiagonal
n=np.arange(-70,71,dtype=float)
def gaps(K,d,t=0):
    diagonal=4*K*n*n-4*d+t*(8*d-8*K*n*n)
    off=np.full(len(n)-1,-2*d)+t*(4*d+4*K*n[:-1]*(n[:-1]+1))
    e=eigh_tridiagonal(diagonal,off,select='i',select_range=(0,6),tol=1e-13)[0]
    return e[1:]-e[0]
rows=[]
for h in (1e-4,3e-5,1e-5):
    K=1.;d=31.607246
    J=np.column_stack(((gaps(K+h,d)-gaps(K-h,d))/(2*h),(gaps(K,d+h)-gaps(K,d-h))/(2*h)))
    raw=(gaps(K,d,h)-gaps(K,d,-h))/(2*h)
    dp=np.linalg.solve(J[:2],-raw[:2]);corrected=raw+J@dp
    rows.append(dict(step=h,adjustment=dp.tolist(),raw=raw.tolist(),corrected=corrected.tolist()))
print(json.dumps(rows,indent=2))
