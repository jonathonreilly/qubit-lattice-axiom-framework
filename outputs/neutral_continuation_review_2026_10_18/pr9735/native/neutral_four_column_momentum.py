"""Finite source-resolved coefficient spectra; cosine source combines degenerate +/-q."""
from neutral_four_column_model_v2 import setup,mv
import numpy as np,json,sys,time
from scipy.sparse.linalg import LinearOperator,eigsh
from scipy.linalg import eigh_tridiagonal

def source_diag(nx,ny,mx,my):
 nb=(nx-1)*(ny-1);even=nx%2==0 and ny%2==0;d=1<<(nb-int(even));ids=np.arange(d,dtype=np.int64)
 def idx(a,b):return a*(ny-1)+b
 if even:
  mask=sum(1<<idx(a,b) for a in range(0,nx-1,2) for b in range(0,ny-1,2));z=ids&mask
  for shift in [32,16,8,4,2,1]:z^=z>>shift
  ids|=(z&1)<<(nb-1)
 out=np.zeros(d)
 for x in range(nx):
  for y in range(ny):
   mask=sum(1<<idx(a,b) for a in (range(nx-1) if x==nx-1 else [x]) for b in (range(ny-1) if y==ny-1 else [y]));z=ids&mask
   for shift in [32,16,8,4,2,1]:z^=z>>shift
   out+=(1-2*(z&1))*np.cos(2*np.pi*(mx*x/nx+my*y/ny))
 return out*np.sqrt((1 if (2*mx)%nx==0 and (2*my)%ny==0 else 2)/(nx*ny))

def run(nx,ny,ratio=8/9,steps=64):
 start=time.time();diag,masks=setup(nx,ny);d=len(diag);op=LinearOperator((d,d),matvec=lambda v:mv(v,diag,masks,ratio),dtype=np.float64)
 vals,vecs=eigsh(op,k=1,which='SA',tol=1e-12,v0=np.ones(d),ncv=16);E=vals[0];gs=vecs[:,0];gr=float(np.linalg.norm(op@gs-E*gs));rows=[]
 for mx,my in [(0,0),(1,0),(0,1),(1,1),(2,0)]:
  od=source_diag(nx,ny,mx,my);mean=float(gs@(od*gs));f=(od-mean)*gs;norm=float(np.linalg.norm(f));v=f/norm;old=np.zeros(d);b=0;aa=[];bb=[];vs=[]
  for k in range(steps):
   vs.append(v.copy());w=op@v-E*v-b*old;a=float(v@w);aa.append(a);w-=a*v;w-=gs*(gs@w)
   for _ in range(2):
    for q in vs:w-=q*(q@w)
   b=float(np.linalg.norm(w))
   if b<1e-12:break
   bb.append(b);old=v;v=w/b
  ev,u=eigh_tridiagonal(aa,bb[:len(aa)-1]);wts=norm**2*u[0]**2;j=next(j for j in range(len(ev)) if wts[j]>norm**2*1e-5)
  state=sum(u[k,j]*vs[k] for k in range(len(vs)));res=float(np.linalg.norm(op@state-(E+ev[j])*state))
  qx,qy=2*np.pi*mx/nx,2*np.pi*my/ny
  correction=-13/24-(np.cos(qx)+np.cos(qy)+np.cos(2*qx)+np.cos(2*qy))/8-(np.cos(2*qx)*np.cos(qy)+np.cos(qx)*np.cos(2*qy))/12
  row=dict(mx=mx,my=my,qx=qx,qy=qy,gap=float(ev[j]),weight=float(wts[j]),source_norm2=norm**2,residual=res,auxiliary_second_order_prediction=float(16*ratio+correction/ratio));rows.append(row);print(row,flush=True)
 out=dict(nx=nx,ny=ny,t_over_K=ratio,ground_energy=float(E),ground_residual=gr,rows=rows,elapsed=time.time()-start,scope='finite full leading coefficient model; strong-X prediction is auxiliary, uncontrolled at native ratio')
 open('/private/tmp/neutral_four_column_momentum_%dx%d_t%.4f.json'%(nx,ny,ratio),'w').write(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]) if len(sys.argv)>3 else 8/9)
