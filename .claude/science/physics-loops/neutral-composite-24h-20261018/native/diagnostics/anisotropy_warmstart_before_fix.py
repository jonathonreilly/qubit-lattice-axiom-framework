"""Finite exact plane-sector native tube versus weak-rung ratio; no bulk phase claim."""
from pathlib import Path
import numpy as np,json,time
from scipy.sparse.linalg import LinearOperator,eigsh
from compass_sector_basis import basis
from compass_sector_solve import apply
from neutral_extra_sector import reducer
P=Path(__file__).resolve().parent;rows=[]
for L in [4,6,8]:
 d=basis((2,2,L));st=[]
 for axis in [0,1]:
  mask=sum(1<<i for i,x in enumerate(d['sites']) if x[axis]==0)
  # L even, each Y plane has2L sites and phase i^(2L)=+1.
  st.append(d['reduce_term'](mask,mask if axis==1 else 0,1))
 R=reducer(len(d['free']),st,[1,1]);terms=np.array([R['reduce'](x) for x in d['terms']],np.int64);f,z,c=terms.T.copy();axes=np.array([a for i,j,a in d['bonds']]);dim=R['dimension'];v=np.random.default_rng(1818+L).normal(size=dim)
 idx={x:i for i,x in enumerate(d['sites'])};ct=[]
 for zz in range(1,L-1):
  for x in range(2):
   for y in range(2):
    mask=(1<<idx[x,y,zz-1])|(1<<idx[x,y,zz+1]);ct.append(R['reduce'](d['reduce_term'](0,mask,1)))
 cf,cz,cc=np.array(ct,np.int64).T.copy()
 for lam in [1.,.7,.5,.35,.2,.1]:
  start=time.monotonic();coeff=c*np.where(axes==2,lam,1.);calls=0
  def mv(a):
   global calls
   calls+=1
   if time.monotonic()-start>1200:raise TimeoutError('owned finite probe exceeded1200s, no science inference')
   return apply(a,f,z,coeff)
  H=LinearOperator((dim,dim),matvec=mv,dtype=float)
  e,u=eigsh(H,k=4,which='SA',tol=1e-11,ncv=32,v0=v,maxiter=3000);ix=np.argsort(e);e=e[ix];u=u[:,ix];v=u[:,0]
  residuals=[float(np.linalg.norm(mv(u[:,j])-e[j]*u[:,j])) for j in range(4)];assert max(residuals)<1e-7
  src=apply(v,cf,cz,cc)/np.sqrt(L-2);src-=v*(v@src);weight=float(src@src);overlaps=(u.T@src)**2
  row=dict(L=L,lambda_z=lam,dimension=dim,energy=float(e[0]),gaps=(e-e[0]).tolist(),gaps_over_t=((e-e[0])/(lam**2/np.sqrt(2))).tolist(),residuals=residuals,source_weight=weight,mode_source_weights=overlaps.tolist(),seconds=time.monotonic()-start,calls=calls)
  rows.append(row);(P/'neutral_tube_anisotropy.json').write_text(json.dumps(dict(rows=rows,scope='Selected positive rung/individualX/Yplane sector, finite open2x2xL; diagnostic anisotropy, no ground-sector survey or bulk phase proof'),indent=2)+'\n');print(row,flush=True)
