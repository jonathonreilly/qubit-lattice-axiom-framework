"""Exact selected-sector 27-qubit periodic native cube: small-volume control only."""
from pathlib import Path
import sys,json,time
import numpy as np
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh,LinearOperator
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parent))
from compass_sector_basis import basis
from compass_sector_solve import apply

def main():
 start=time.monotonic();shape=(3,3,3);d=basis(shape);idx={p:i for i,p in enumerate(d['sites'])};ts=list(d['terms'])
 for a in range(3):
  for p,i in idx.items():
   if p[a]==2:
    q=list(p);q[a]=0;mask=(1<<i)|(1<<idx[tuple(q)])
    ts.append(d['reduce_term'](mask if a!=2 else 0,mask if a!=0 else 0,1 if a==1 else -1))
 ts=np.array(ts,np.int64);dim=d['dimension'];H=lambda v:apply(v,*ts.T.copy());op=LinearOperator((dim,dim),matvec=H,dtype=float)
 E,V=eigsh(op,k=2,which='SA',tol=1e-11,ncv=24,maxiter=1200,v0=np.random.default_rng(271910).normal(size=dim));g=V[:,0];e=float(E[0]);gsub=V[:,E-E[0]<1e-8]
 out=dict(shape=shape,physical_qubits=27,periodic_axes=[0,1,2],dimension=dim,ground_energy=e,lowest_energies=E.tolist(),ground_residual=float(np.linalg.norm(H(g)-e*g)),scope='Exact selected CSS sector, 3-site periodic cube; no large-volume or stable-size conclusion',levels=[])
 (P/'exact_periodic_cube.json').write_text(json.dumps(out,indent=2)+'\n');print('ground',out,flush=True)
 S=[];raw=[]
 for k in [1,2]:
  mask=sum(1<<i for i,(x,y,z) in enumerate(d['sites']) if x<k and y<2 and z<2);t=np.array([d['reduce_term'](mask,0,1)],np.int64);u=apply(g,*t.T.copy());raw.append(float(u@H(u)-e));u-=gsub@(gsub.T@u);S.append(u)
 out.update(patches=['1x2x2','2x2x2'],raw_energies=raw);initial=np.column_stack(S);B=[];HB=[];front=S
 for depth in range(9):
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
  if depth in [0,1,2,4,8]:
   BB=np.column_stack(B);HH=np.column_stack(HB);T=BB.T@HH;en,c=eigh((T+T.T)/2);Y=BB@c[:,:2];HY=HH@c[:,:2];rr=np.linalg.norm(HY-Y*en[:2],axis=0)
   out['levels'].append(dict(depth=depth,rank=len(B),energies=en[:2].tolist(),full_residuals=rr.tolist(),probe_overlaps=((initial.T@Y)**2/np.sum(initial**2,axis=0)[:,None]).tolist(),seconds=time.monotonic()-start));print(out['levels'][-1],flush=True)
   (P/'exact_periodic_cube.json').write_text(json.dumps(out,indent=2)+'\n');del BB,HH,Y,HY
if __name__=='__main__':main()
