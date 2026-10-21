"""Full 16-physical-qubit check of open L4 column effective interaction/readout."""
import numpy as np,json
from scipy.sparse.linalg import LinearOperator,lobpcg
from scipy.linalg import svd
from numba import njit,prange
L=4;N=16;D=1<<N;ids=np.arange(D,dtype=np.int64)
def bit(x,y,z):return (2*x+y)*L+z
edges=[];diag=np.zeros(D);C=np.zeros(D)
for x in range(2):
 for y in range(2):
  for z in range(L-1):
   a,b=bit(x,y,z),bit(x,y,z+1);diag-=1-2*(((ids>>a)^(ids>>b))&1)
  for z in range(L-2):
   a,b=bit(x,y,z),bit(x,y,z+2);C+=1-2*(((ids>>a)^(ids>>b))&1)
for z in range(L):
 for y in range(2):edges.append((bit(0,y,z),bit(1,y,z),0))
 for x in range(2):edges.append((bit(x,0,z),bit(x,1,z),1))
edges=np.array(edges,dtype=np.int64)
@njit(parallel=True)
def action(v,lam):
 w=np.empty_like(v)
 for i in prange(D):
  a=diag[i]*v[i]
  for j,k,y in edges:
   coef=-lam if y==0 else lam*(1-2*(((i>>j)^(i>>k))&1))
   a+=coef*v[i^((1<<j)|(1<<k))]
  w[i]=a
 return w
aligned=np.array([sum(((1<<L)-1)<<(c*L) for c in range(4) if s>>c&1) for s in range(16)])
X=np.zeros((D,16));X[aligned,np.arange(16)]=1
P=np.diag([(-1)**s.bit_count() for s in range(16)]);T=np.zeros((16,16))
for i in range(16):
 for a,b in [(0,2),(1,3),(0,1),(2,3)]:T[i^((1<<a)|(1<<b)),i]+=1
he=-9/64*P-1/8*T;ce=-51/128*P-3/8*T
rows=[]
for lam in [.1,.2]:
 op=LinearOperator((D,D),matvec=lambda v:action(v.ravel(),lam),matmat=lambda v:np.column_stack([action(v[:,j],lam) for j in range(v.shape[1])]),dtype=float)
 e,V=lobpcg(op,X.copy(),largest=False,tol=1e-11,maxiter=160)
 res=np.linalg.norm(op@V-V*e,axis=0)
 A=V[aligned];U,s,Vh=svd(A);rot=Vh.T@U.T;Q=V@rot
 H=(rot.T*e)@rot;O=Q.T@(C[:,None]*Q)
 h=(H-np.trace(H)*np.eye(16)/16)/lam**4;c=(O-np.trace(O)*np.eye(16)/16)/lam**4
 row=dict(lam=lam,max_residual=float(max(res)),minimum_aligned_overlap=float(min(s)),H_coefficient_error=float(np.linalg.norm(h-he,2)),C_coefficient_error=float(np.linalg.norm(c-ce,2)),H_plaquette=float(np.trace(h@P)/16),H_pair=float(np.trace(h@T)/np.trace(T@T)),C_plaquette=float(np.trace(c@P)/16),C_pair=float(np.trace(c@T)/np.trace(T@T)));rows.append(row);print(row,flush=True)
 assert max(res)<1e-8 and min(s)>.95
open('/private/tmp/neutral_four_column_native.json','w').write(json.dumps(rows,indent=2)+'\n')
