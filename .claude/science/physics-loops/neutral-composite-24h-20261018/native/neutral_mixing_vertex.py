import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad_vec
import json
R=7;n=R*R
T=np.zeros((n,n));idx=lambda x,y:(x%R)*R+y%R
for x in range(R):
 for y in range(R):
  i=idx(x,y)
  for dx,dy in [(1,0),(0,1)]:
   j=idx(x+dx,y+dy);T[i,j]=T[j,i]=-1
V=np.zeros_like(T)
for x in [2,3]:
 for y in [1,3]:
  i,j=idx(x,2),idx(x,y);V[i,j]=V[j,i]=2
Te=T+V
rows=[]
for c in [.1,.03,.01]:
 d=.07;h=c*d;theta=.5*np.arctan2(2*h,d);s=np.sin(theta);a=np.cos(theta)
 Q=np.kron(np.array([[a,-s],[s,a]]),np.eye(n))
 H=np.block([[T,-h*np.eye(n)],[-h*np.eye(n),Te+d*np.eye(n)]])
 rot=Q.T@H@Q
 err=np.max(np.abs(rot[n:,:n]-s*a*V))
 rows.append(dict(c=c,rotation_error=float(err),leading_relative_error=float(abs(s*a/c-1))))
tau=.23
lhs,err=quad_vec(lambda t:-1j*expm(-1j*(tau-t)*Te)@V@expm(-1j*t*T),0,tau,epsabs=1e-11,epsrel=1e-11)
rhs=expm(-1j*tau*Te)-expm(-1j*tau*T)
result=dict(rotation=rows,duhamel_error=float(np.max(np.abs(lhs-rhs))),quadrature_error=float(err),flux_return_trace4=float(np.trace(np.linalg.matrix_power(Te,4)-np.linalg.matrix_power(T,4))))
assert max(q['rotation_error'] for q in rows)<1e-13
assert result['duhamel_error']<1e-12
assert result['flux_return_trace4']==-64
print(json.dumps(result,indent=2))
