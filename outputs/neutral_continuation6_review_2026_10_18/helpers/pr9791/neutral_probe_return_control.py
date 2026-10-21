import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['VECLIB_MAXIMUM_THREADS']='1'
import sys,json,math,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from numba import njit
from neutral_four_layer_geometry import geometry,makeorbits,diagonal
from scipy.sparse.linalg import LinearOperator,eigsh
R=5;_,_,edges,flips=geometry(R,True);rot,ref,_,_=geometry(R,True);ids,reps,sizes=makeorbits((R-1)**2,rot,ref)
@njit
def coefficient_apply(v,d,flips):
 out=d*v
 for f in flips:
  for j in range(len(v)):out[j]-=4*v[j^f]
 return out
dim=1<<((R-1)**2);d=diagonal(np.arange(dim,dtype=np.int64),edges)
op=LinearOperator((dim,dim),matvec=lambda v:coefficient_apply(v,d,flips),dtype=float)
ev,u=eigsh(op,k=1,which='SA',v0=np.ones(dim),tol=2e-12);g=u[:,0]
assert np.linalg.norm(coefficient_apply(g,d,flips)-ev[0]*g)<1e-8

neighbors=np.zeros((R*R,4),np.int64);masks=np.zeros_like(neighbors)
for x in range(R):
 for y in range(R):
  i=x*R+y
  for k,(dx,dy) in enumerate([(1,0),(-1,0),(0,1),(0,-1)]):
   xx=(x+dx)%R;yy=(y+dy)%R;neighbors[i,k]=xx*R+yy
   if dy and x<R-1:
    for b in [y,yy]:
     if b<R-1:masks[i,k]^=1<<(x*(R-1)+b)
@njit
def T(v,neighbors,masks):
 out=np.zeros_like(v)
 for i in range(len(neighbors)):
  for k in range(4):
   j=neighbors[i,k];m=masks[i,k]
   for s in range(v.shape[1]):out[i,s]-=v[j,s^m]
 return out
v=np.zeros((R*R,dim));v[0]=g
w=v.copy()
for _ in range(4):w=T(w,neighbors,masks)
states=np.arange(dim);B=sum(g[states^flips[x*R+y]] for x,y in [(0,0),(R-1,0),(0,R-1),(R-1,R-1)])
assert np.linalg.norm(w[0]-28*g-2*B)<1e-10
q=B-g*(g@B);rows=[]
for tau in [.1,.2,.4]:
 term=v.astype(complex);psi=term.copy()
 for n in range(1,25):term=(-1j*tau/n)*T(term,neighbors,masks);psi+=term
 ret=psi[0];inel=ret-g*np.vdot(g,ret)
 err=np.linalg.norm(inel-tau**4*q/12)
 rows.append(dict(tau=tau,inelastic_return_probability=float(np.vdot(inel,inel).real),leading_probability=float(tau**8*np.dot(q,q)/144),amplitude_error=float(err),error_div_tau6=float(err/tau**6),series_tail_bound=float(math.exp(4*tau)*(4*tau)**25/math.factorial(25))))
print(json.dumps(dict(R=R,dimension=R*R*dim,loop_identity_residual=float(np.linalg.norm(w[0]-28*g-2*B)),local_loop_variance=float(q@q),time_controls=rows,scope='Prepared heavy defect over vacuum coefficient ground, leading N2 hopping; not dressed matter ground or universal coupling'),indent=2))
