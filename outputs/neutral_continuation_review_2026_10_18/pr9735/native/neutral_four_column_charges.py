"""Full leading column Hamiltonian in X-spin row/column-charge sectors."""
import numpy as np,json,sys,time
from scipy.sparse.linalg import LinearOperator,eigsh
from neutral_four_column_model_v2 import mv

def setup(nx,ny,sites=()):
 r=np.zeros(nx,dtype=int);c=np.zeros(ny,dtype=int)
 for x,y in sites:r[x]^=1;c[y]^=1
 assert int(r.sum())%2==int(c.sum())%2
 nb=(nx-1)*(ny-1);even=nx%2==0 and ny%2==0;d=1<<(nb-int(even));ids=np.arange(d,dtype=np.int64)
 def idx(x,y):return x*(ny-1)+y
 def spin(x,y):
  if x<nx-1 and y<ny-1:return 1<<idx(x,y),0
  if x<nx-1:return sum(1<<idx(x,b) for b in range(ny-1)),int(r[x])
  if y<ny-1:return sum(1<<idx(a,y) for a in range(nx-1)),int(c[y])
  return (1<<nb)-1,int(r[-1])^int(sum(c[:-1])%2)
 diag=np.zeros(d)
 for x in range(nx):
  for y in range(ny):
   a,ca=spin(x,y)
   for dx,dy in [(1,0),(0,1)]:
    b,cb=spin((x+dx)%nx,(y+dy)%ny);z=ids&(a^b)
    for shift in [32,16,8,4,2,1]:z^=z>>shift
    diag-=1-2*((z&1)^(ca^cb))
 masks=[]
 for x in range(nx):
  for y in range(ny):
   m=sum(1<<idx(a,b) for a,b in [(x,y),((x+1)%nx,y),(x,(y+1)%ny),((x+1)%nx,(y+1)%ny)] if a<nx-1 and b<ny-1)
   if even and m>>(nb-1):m^=(1<<nb)-1
   masks.append(m)
 return diag,np.array(masks,dtype=np.int64)

def run(nx,ny):
 ratio=8/9;rows=[];gs0=None;E0=None;P0=None;start=time.time()
 for label,sites in [('vacuum',[]),('single',[(nx-1,ny-1)]),('vertical_dipole',[(nx-2,ny-1),(nx-1,ny-1)]),('separated_vertical',[(nx-3,ny-1),(nx-1,ny-1)]),('horizontal_dipole',[(nx-1,ny-2),(nx-1,ny-1)])]:
  diag,masks=setup(nx,ny,sites);d=len(diag);op=LinearOperator((d,d),matvec=lambda v:mv(v,ratio*diag,masks,1.),dtype=np.float64)
  vals,vecs=eigsh(op,k=1,which='SA',tol=2e-12,v0=np.ones(d),ncv=20);E=vals[0];v=vecs[:,0];res=np.linalg.norm(op@v-E*v)
  Pmean=float(ratio*np.dot(v,diag*v)-E)
  if E0 is None:E0=E;gs0=v.copy();P0=Pmean
  deltaP=Pmean-P0
  ccharge=3*(9/64)*(E-E0)+(3/128)*deltaP
  # Chosen sites lie on last row/column, so they change affine charge boundary only; free coordinates unchanged.
  overlap=float(abs(gs0@v)**2)
  row=dict(sector=label,sites=sites,energy=float(E),gap=float(E-E0),residual=float(res),source_overlap2=overlap,plaquette_mean=Pmean,plaquette_difference=deltaP,native_readout_charge_over_lambda4=float(ccharge),native_readout_charge_over_mass_Jz=float(3+deltaP/(6*(E-E0))) if E!=E0 else None);rows.append(row);print(row,flush=True)
 out=dict(nx=nx,ny=ny,dimension=d,rows=rows,elapsed=time.time()-start,scope='Selected subsystem-charge sectors of leading coefficient model; no full native pole or particle statistics identification')
 open('/private/tmp/neutral_four_column_charges_%dx%d.json'%(nx,ny),'w').write(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]))
