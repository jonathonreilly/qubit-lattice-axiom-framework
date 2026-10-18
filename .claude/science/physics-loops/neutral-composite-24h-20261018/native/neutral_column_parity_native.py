import os
os.environ['NUMBA_NUM_THREADS']='4'
import numpy as np,json,time
from numba import njit,prange
from scipy.sparse.linalg import LinearOperator,eigsh
from pathlib import Path
@njit(parallel=True)
def apply(v,diag,dest,amp,lam):
 out=diag*v
 for s in prange(len(v)):
  for j in range(dest.shape[0]):out[s]+=lam*amp[j,s]*v[dest[j,s]]
 return out
rows=[]
for L in [5,6]:
 for parity in [0,1]:
  colors=[s for s in range(16) if s.bit_count()%2==parity];lookup={s:i for i,s in enumerate(colors)}
  n=8**L;ids=np.arange(n);digits=np.array([(ids//8**j)%8 for j in range(L)]);phys=np.array(colors)[digits]
  diag=np.zeros(n)
  for j in range(L-1):diag-=sum(1-2*(((phys[j]^phys[j+1])>>a)&1) for a in range(4))
  Cdiag=sum(sum(1-2*(((phys[j]^phys[j+2])>>a)&1) for a in range(4)) for j in range(L-2))
  dest=[];amp=[]
  for j in range(L):
   for a,b,kind in [(0,1,'X'),(2,3,'X'),(0,2,'Y'),(1,3,'Y')]:
    target=np.array([lookup[c^(1<<a)^(1<<b)] for c in colors])[digits[j]]
    dest.append(ids+(target-digits[j])*8**j)
    amp.append(np.full(n,-1.) if kind=='X' else (1-2*((phys[j]>>a)&1))*(1-2*((phys[j]>>b)&1)))
  dest=np.array(dest,dtype=np.int32);amp=np.array(amp,dtype=float)
  for lam in [.1,.2]:
   t=time.time();H=LinearOperator((n,n),matvec=lambda v:apply(v,diag,dest,amp,lam),dtype=float)
   e,u=eigsh(H,k=16,which='SA',tol=2e-12,ncv=64,v0=np.random.default_rng(118+parity).normal(size=n))
   order=np.argsort(e);e=e[order];u=u[:,order];res=[np.linalg.norm(H@u[:,i]-e[i]*u[:,i]) for i in range(8)]
   assert e[8]-e[7]>1 and max(res)<1e-8
   r=dict(L=L,parity=parity,lambda_perp=lam,band_mean=float(np.mean(e[:8])),ground=float(e[0]),band=list(e[:8]),readout_band_mean=float(np.mean(np.sum(Cdiag[:,None]*u[:,:8]**2,axis=0))),residuals=list(res),seconds=time.time()-t);rows.append(r);print(json.dumps(r),flush=True)
   Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
