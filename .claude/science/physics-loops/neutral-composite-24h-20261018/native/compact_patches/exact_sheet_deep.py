"""Native one-layer control: no XX bonds in this geometry, not a 3D certificate."""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh,LinearOperator
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parent))
from compass_sector_basis import basis
from compass_sector_solve import apply

def main():
 rows=[]
 for shape in [(1,4,4),(1,4,6)]:
  t0=time.monotonic();d=basis(shape);ts=np.array(d['terms'],np.int64);dim=d['dimension'];H=lambda v:apply(v,*ts.T.copy());op=LinearOperator((dim,dim),matvec=H,dtype=float)
  E,V=eigsh(op,k=4,which='SA',tol=1e-11,ncv=24,v0=np.random.default_rng(19000+dim).normal(size=dim));g=V[:,0];e=float(E[0]);gsub=V[:,E-E[0]<1e-8]
  labels=[];S=[];raw=[]
  for w in range(2,shape[1]-1,2):
   for ell in range(2,shape[2]-1,2):
    a=(shape[1]-w)//2;b=(shape[2]-ell)//2;mask=sum(1<<i for i,(x,y,z) in enumerate(d['sites']) if a<=y<a+w and b<=z<b+ell)
    term=np.array([d['reduce_term'](mask,0,1)],np.int64);v=apply(g,*term.T.copy());raw.append(float(v@H(v)-e));v-=gsub@(gsub.T@v);S.append(v);labels.append([w,ell])
  initial=np.column_stack(S);B=[];HB=[];front=S;levels=[]
  for depth in range(41):
   new=[]
   for v in front:
    v=v.copy()
    for repeat in range(2):
     v-=gsub@(gsub.T@v)
     for q in B:v-=q*float(q@v)
    norm=np.linalg.norm(v)
    if norm<1e-10:continue
    v/=norm;B.append(v);h=H(v)-e*v;HB.append(h);new.append(h)
   front=new
   if depth in [0,4,12,24,40]:
    BB=np.column_stack(B);HH=np.column_stack(HB);T=BB.T@HH;en,c=eigh((T+T.T)/2);Y=BB@c[:,:3];HY=HH@c[:,:3];rr=np.linalg.norm(HY-Y*en[:3],axis=0)
    levels.append(dict(depth=depth,rank=len(B),energies=en[:3].tolist(),residuals=rr.tolist(),probe_overlaps=((initial.T@Y)**2/np.sum(initial**2,axis=0)[:,None]).tolist()));print(shape,levels[-1],flush=True)
  row=dict(shape=shape,dimension=dim,ground_energy=e,ground_residual=float(np.linalg.norm(H(g)-e*g)),lowest_sector_energies=E.tolist(),projected_ground_rank=gsub.shape[1],patches=labels,raw=raw,levels=levels,seconds=time.monotonic()-t0);rows.append(row)
  (P/'exact_sheet_deep.json').write_text(json.dumps(dict(scope='Exact selected-sector one-layer native H control, no XX bonds; not a 3D stable-size result',rows=rows),indent=2)+'\n')
if __name__=='__main__':main()
