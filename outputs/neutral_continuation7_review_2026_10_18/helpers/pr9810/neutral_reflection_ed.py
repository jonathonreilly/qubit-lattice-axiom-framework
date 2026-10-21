AUDIT_TIMEOUT_SEC=300
import numpy as np,json
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

def run(shape,lam):
 nx,ny,nz=shape;N=nx*ny*nz;dim=1<<N;states=np.arange(dim,dtype=np.int64)
 idx=lambda x,y,z:((x%nx)*ny+y%ny)*nz+z%nz
 diag=np.zeros(dim);rows=[];cols=[];vals=[]
 for x in range(nx):
  for y in range(ny):
   for z in range(nz):
    i=idx(x,y,z)
    for axis,dx,dy,dz in [('x',1,0,0),('y',0,1,0),('z',0,0,1)]:
     j=idx(x+dx,y+dy,z+dz);sgn=1-2*(((states>>i)^(states>>j))&1)
     if axis=='z':diag-=sgn
     else:
      rows.append(states^((1<<i)|(1<<j)));cols.append(states);vals.append(np.full(dim,-lam) if axis=='x' else lam*sgn)
 rows.append(states);cols.append(states);vals.append(diag)
 H=coo_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(dim,dim)).tocsr()
 planes=[]
 for axis,size in [('x',nx),('y',ny),('z',nz)]:
  for k in range(size):
   sites=[idx(x,y,z) for x in range(nx) for y in range(ny) for z in range(nz) if {'x':x,'y':y,'z':z}[axis]==k]
   mask=sum(1<<i for i in sites);sgn=np.ones(dim)
   for i in sites:sgn*=1-2*((states>>i)&1)
   if axis=='x':planes.append((states^mask,np.ones(dim)))
   elif axis=='y':planes.append((states^mask,(-1)**(len(sites)//2)*sgn))
   else:planes.append((states,sgn))
 rng=np.random.default_rng(313);v=rng.normal(size=dim)
 for dest,sgn in planes:v=(v+sgn*v[dest])/2
 v/=np.linalg.norm(v)
 e,a=eigsh(H,k=1,which='SA',v0=v,tol=1e-11);ef,_=eigsh(H,k=1,which='SA',v0=rng.normal(size=dim),tol=1e-11)
 a=a[:,0]
 return dict(shape=shape,lam=lam,sector_energy=float(e[0]),full_energy=float(ef[0]),difference=float(e[0]-ef[0]),residual=float(np.linalg.norm(H@a-e[0]*a)),plane_expectations=[float(a@(sgn*a[dest])) for dest,sgn in planes])
rows=[]
for shape in [(2,2,2),(2,2,4)]:
 for lam in [.2,.7,1.0]:
  r=run(shape,lam);rows.append(r)
print(json.dumps(rows,indent=2))
