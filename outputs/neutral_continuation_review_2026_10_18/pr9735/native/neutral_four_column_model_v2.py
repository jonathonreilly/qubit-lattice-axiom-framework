"""Full leading L4 column Hamiltonian in + subsystem-flip quotient, no four-defect restriction."""
import os
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1');os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np,json,sys,time
from numba import njit,prange
from scipy.sparse.linalg import LinearOperator,eigsh
from scipy.linalg import eigh_tridiagonal
@njit(parallel=True)
def mv(v,diag,masks,t):
 out=np.empty_like(v)
 for i in prange(len(v)):
  val=diag[i]*v[i]
  for m in masks:val-=t*v[i^m]
  out[i]=val
 return out

def setup(nx,ny):
 nb=(nx-1)*(ny-1);even=nx%2==0 and ny%2==0;dim=1<<(nb-int(even))
 def idx(x,y):return x*(ny-1)+y
 def pm(x,y):
  return sum(1<<idx(a,b) for a in (range(nx-1) if x==nx-1 else [x]) for b in (range(ny-1) if y==ny-1 else [y]))
 def site(x,y):
  return sum(1<<idx(a,b) for a,b in [((x-1)%nx,(y-1)%ny),((x-1)%nx,y%ny),(x%nx,(y-1)%ny),(x%nx,y%ny)] if a<nx-1 and b<ny-1)
 masks=np.array([site(x,y)^site((x+dx)%nx,(y+dy)%ny) for x in range(nx) for y in range(ny) for dx,dy in [(1,0),(0,1)]],dtype=np.int64)
 ids=np.arange(dim,dtype=np.int64)
 if even:
  paritymask=sum(1<<idx(a,b) for a in range(0,nx-1,2) for b in range(0,ny-1,2))
  # last independent bit is in paritymask; eliminate it in the + global-Z sector
  z=ids&paritymask;z^=z>>32;z^=z>>16;z^=z>>8;z^=z>>4;z^=z>>2;z^=z>>1
  ids|=(z&1)<<(nb-1)
  assert all((int(m)&paritymask).bit_count()%2==0 for m in masks)
  masks&=(1<<(nb-1))-1
 P=np.zeros(dim)
 for x in range(nx):
  for y in range(ny):
   z=ids&pm(x,y);z^=z>>32;z^=z>>16;z^=z>>8;z^=z>>4;z^=z>>2;z^=z>>1
   P+=1-2*(z&1)
 return -P,masks

def run(nx,ny,t=8/9,steps=64,mx=0,my=0):
 start=time.time();diag,masks=setup(nx,ny);d=len(diag);op=LinearOperator((d,d),matvec=lambda v:mv(v,diag,masks,t),dtype=np.float64)
 vals,vecs=eigsh(op,k=1,which='SA',tol=2e-12,v0=np.ones(d)/np.sqrt(d),ncv=16)
 o=np.argsort(vals);vals=vals[o];vecs=vecs[:,o];gs=vecs[:,0];E=vals[0];res=[np.linalg.norm(op@vecs[:,i]-vals[i]*vecs[:,i]) for i in range(len(vals))]
 np.savez('/private/tmp/neutral_four_column_gs_%dx%d.npz'%(nx,ny),ground=gs,energy=E)
 print('ground ready',nx,ny,E,res,flush=True)
 P=-diag;mean=float(np.dot(gs,P*gs));f=(P-mean)*gs/np.sqrt(nx*ny);norm=float(np.linalg.norm(f));v=f/norm;prev=np.zeros(d);beta=0;vs=[];aa=[];bb=[]
 for k in range(steps):
  vs.append(v.copy());w=op@v-E*v-beta*prev;a=float(v@w);aa.append(a);w-=a*v
  w-=gs*(gs@w)
  for q in vs:w-=q*(q@w)
  for q in vs:w-=q*(q@w)
  b=float(np.linalg.norm(w))
  if b<1e-12:break
  bb.append(b);prev=v;v=w/b;beta=b
 ev,u=eigh_tridiagonal(np.array(aa),np.array(bb[:len(aa)-1]));weights=norm**2*u[0]**2
 # Direct residual of low significant Ritz vectors; do not label unvalidated nodes poles.
 selected=[i for i in range(len(ev)) if weights[i]>norm**2*1e-5][:8];ritz=[]
 for j in selected:
  q=sum(u[k,j]*vs[k] for k in range(len(vs)));r=np.linalg.norm(op@q-(E+ev[j])*q)
  ritz.append(dict(index=j,gap=float(ev[j]),weight=float(weights[j]),residual=float(r)))
 result=dict(nx=nx,ny=ny,dimension=d,t_over_K=t,ground_energy=float(E),energy_per_column=float(E/(nx*ny)),low_gaps=(vals-E).tolist(),eigen_residuals=res,plaquette_mean_per_site=mean/(nx*ny),source_norm2=norm**2,source_mean=float(aa[0]),source_std=float(bb[0]),ritz=ritz,lanczos_steps=len(aa),elapsed=time.time()-start,scope='Full leading order-four coefficient model, selected + subsystem-flip sector; no exact microscopic or infinite-grid claim')
 np.savez('/private/tmp/neutral_four_column_gs_%dx%d.npz'%(nx,ny),ground=gs,energy=E);print(json.dumps(result,indent=2),flush=True);open('/private/tmp/neutral_four_column_%dx%d.json'%(nx,ny),'w').write(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),steps=int(sys.argv[3]) if len(sys.argv)>3 else 64)
