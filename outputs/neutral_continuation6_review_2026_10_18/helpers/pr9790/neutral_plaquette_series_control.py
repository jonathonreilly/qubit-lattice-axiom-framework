import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['VECLIB_MAXIMUM_THREADS']='1'
import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from scipy.sparse.linalg import LinearOperator,eigsh
from neutral_four_layer_geometry import geometry,diagonal
from numba import njit
@njit
def H(v,d,f,t):
 out=d*v
 for a in f:
  for j in range(len(v)):out[j]-=4*t*v[j^a]
 return out
R=5;_,_,edges,f=geometry(R,True);states=np.arange(1<<16,dtype=np.int64);d=diagonal(states,edges)
rows=[]
for t in [.05,.1,.2,.4,.7,1.]:
 op=LinearOperator((len(d),len(d)),matvec=lambda v:H(v,d,f,t),dtype=float)
 ev,u=eigsh(op,k=2,which='SA',v0=np.ones(len(d)),tol=1e-12)
 g=u[:,0];ground_residual=float(np.linalg.norm(H(g,d,f,t)-ev[0]*g));assert ground_residual<1e-7, ('ground residual',t,ground_residual);E=-d/5;q=-3*(E-g@(E*g))*g;norm=np.linalg.norm(q)
 # project source Krylov and obtain lowest visible line
 B=[];v=q/norm
 for k in range(35):
  B.append(v);w=H(v,d,f,t)-ev[0]*v
  for _ in range(2):
   for z in B:w-=np.dot(z,w)*z
  wnorm=np.linalg.norm(w)
  if wnorm<1e-10:break
  v=w/wnorm
 B=np.array(B).T;HB=np.column_stack([H(z,d,f,t)-ev[0]*z for z in B.T]);T=B.T@HB;ee,uu=np.linalg.eigh((T+T.T)/2)
 wt=norm**2*uu[0]**2;i=np.flatnonzero(wt>1e-8)[0];z=B@uu[:,i];res=np.linalg.norm(H(z,d,f,t)-(ev[0]+ee[i])*z)
 assert np.isfinite(ee[i]) and np.isfinite(res) and norm>0 and wt[i]>0, (t,ee[i],res,norm,wt[i])
 row=dict(ground_residual=ground_residual,u=t,gap=float(ee[i]),gap_series=80-29/24*16/5*t*t,weight=float(wt[i]),total_weight=float(norm**2),weight_series=25*5.76*t*t,residual=float(res));rows.append(row)
assert len(rows)==6 and [r['u'] for r in rows]==[.05,.1,.2,.4,.7,1.]
# A finite two-fixture trend, not a uniform remainder theorem or a u=1 approximation certificate.
e0=abs(rows[0]['gap']-rows[0]['gap_series']);e1=abs(rows[1]['gap']-rows[1]['gap_series'])
assert e0>0 and .5<(e1/e0)/8<2, ('finite cubic error ratio',e0,e1)
print(json.dumps(dict(controls=rows,scope="Auxiliary u convergence control; physical u1 not controlled by truncation")))
