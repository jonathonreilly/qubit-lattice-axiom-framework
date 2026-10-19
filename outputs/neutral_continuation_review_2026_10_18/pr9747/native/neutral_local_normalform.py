import numpy as np,json
from scipy.linalg import expm
from math import factorial

def model(nx=2,ny=2,nz=2):
 n=nx*ny*nz;dim=1<<n;states=np.arange(dim);H0=np.zeros(dim);V=np.zeros((dim,dim));idx=lambda x,y,z:(x*ny+y)*nz+z
 for x in range(nx):
  for y in range(ny):
   for z in range(nz):
    a=idx(x,y,z)
    if z+1<nz:
     b=idx(x,y,z+1);H0-=1-2*((states>>a ^ states>>b)&1)
    if x+1<nx:
     b=idx(x+1,y,z);V[states^((1<<a)|(1<<b)),states]-=1
    if y+1<ny:
     b=idx(x,y+1,z);V[states^((1<<a)|(1<<b)),states]+=1-2*((states>>a ^ states>>b)&1)
 return H0,V

def construct(H0,V,m):
 n=len(H0);h=[np.diag(H0),V]+[np.zeros((n,n)) for _ in range(m-1)];generators=[];den=H0[:,None]-H0[None,:];off=den!=0
 for k in range(1,m+1):
  S=np.zeros((n,n));S[off]=h[k][off]/den[off];assert np.linalg.norm(S+S.T)<1e-12
  generators.append(S);new=[np.zeros((n,n)) for _ in range(m+1)]
  for j in range(m+1):
   term=h[j].copy();new[j]+=term
   for r in range(1,(m-j)//k+1):
    term=(S@term-term@S)/r;new[j+r*k]+=term
  h=new
  assert np.linalg.norm(h[k][off])<1e-11
 return h,generators

def run():
 H0,V=model();rows=[]
 for m in [1,2,3,4]:
  h,gens=construct(H0,V,m);off=H0[:,None]!=H0[None,:]
  assert max(np.linalg.norm(q[off]) for q in h[1:])<1e-10
  for lam in [.02,.04,.08]:
   U=np.eye(len(H0))
   for k,S in enumerate(gens,1):U=expm(lam**k*S)@U
   transformed=U@(np.diag(H0)+lam*V)@U.T;D=sum(lam**j*q for j,q in enumerate(h));R=transformed-D
   error=np.linalg.norm(R,2);rows.append(dict(order=m,lam=lam,remainder_norm=float(error),scaled_remainder=float(error/lam**(m+1)),offblock_norm=float(np.linalg.norm(transformed*off,2)),unitarity=float(np.linalg.norm(U.T@U-np.eye(len(H0)),2))))
  scaled=[r['scaled_remainder'] for r in rows if r['order']==m];assert max(scaled)<2*min(scaled)
 return rows
if __name__=='__main__':
 rows=run();print(json.dumps(rows,indent=2));open('/private/tmp/neutral_local_normalform.json','w').write(json.dumps(rows,indent=2)+'\n')
