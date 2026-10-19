import numpy as np,json,time
from numba import njit
from neutral_corrected_fast_host import host
@njit
def arm(z,lam,multiplier=1.):
 f=lam**3/16;N=int(np.ceil(multiplier*(8+abs(z.real)+3*lam)/f/2));h1=-2.;h2=-lam/4
 a=0j;b=0j;c=0j
 for m in range(N,0,-1):
  s00=h2*h2*a;s01=h2*(h1*a+h2*b);s11=h1*h1*a+2*h1*h2*b+h2*h2*c
  v1=f*(2*m)-2.5*lam;v2=f*(2*m+1)-2.5*lam
  aa=z-v1-s00;bb=-h1-s01;cc=z-v2-s11;det=aa*cc-bb*bb
  a=cc/det;b=-bb/det;c=aa/det
 return np.array([[a,b],[b,c]])
def resolvent(z,lam):
 G=host(z,lam);G=G+lam*np.outer(G[:,0],G[0,:])/(1-lam*G[0,0]);g=arm(z,lam)
 # coordinates host d,d2 and arm E2,E3, nonorthogonal Green submatrix before connection.
 W=np.array([[-2.,-lam/4],[-lam,0.]])
 R0=np.zeros((4,4),complex);R0[:2,:2]=G;R0[2:,2:]=g
 V=np.zeros((4,4));V[:2,2:]=W;V[2:,:2]=W.T
 return np.linalg.solve(np.eye(4)-R0@V,R0),G,g
if __name__=='__main__':
 rows=[]
 for lam in [.2,.1,.05,.025]:
  start=time.time();z=-6*lam-.06j*lam**3;R,G,g=resolvent(z,lam);gg=arm(z,lam,1.2);V=np.array([[0.,0.],[-1.,0.],[-1.,-2.],[0.,0.]])
  M=V.T@R@V;row=dict(lam=lam,g=[[[v.real,v.imag] for v in row] for row in g],M=[[[v.real,v.imag] for v in row] for row in M],tail_error=float(np.max(abs(g-gg))),seconds=time.time()-start)
  assert row['tail_error']<1e-9;rows.append(row);print(row,flush=True)
 open('/private/tmp/neutral_corrected_fast_boundary.json','w').write(json.dumps(rows,indent=2)+'\n')
