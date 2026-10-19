"""Direct finite native-H response; no continuum-width interpretation."""
from pathlib import Path
import sys,json,time,os
import numpy as np
from scipy.sparse.linalg import LinearOperator,eigsh
sys.path.insert(0,str(Path(__file__).resolve().parent))
from compass_sector_basis import basis
from compass_sector_solve import apply
from neutral_extra_sector import reducer
L=8;D=basis((2,2,L));idx={x:i for i,x in enumerate(D['sites'])};st=[]
for axis in [0,1]:
 mask=sum(1<<i for i,x in enumerate(D['sites']) if x[axis]==0)
 st.append(D['reduce_term'](mask,mask if axis==1 else 0,1))
R=reducer(len(D['free']),st,[1,1]);terms=list(D['terms']);axes=[a for i,j,a in D['bonds']]
for x in range(2):
 for y in range(2):
  mask=(1<<idx[x,y,L-1])|(1<<idx[x,y,0]);terms.append(D['reduce_term'](0,mask,-1));axes.append(2)
terms=np.array([R['reduce'](x) for x in terms],np.int64);f,z,c=terms.T.copy();axes=np.array(axes);dim=R['dimension']
ct=[]
for j in range(L):
 for x in range(2):
  for y in range(2):
   mask=(1<<idx[x,y,j])|(1<<idx[x,y,(j+2)%L]);ct.append(R['reduce'](D['reduce_term'](0,mask,1)))
cf,cz,cc=np.array(ct,np.int64).T.copy();rows=[]
E4,U4=np.linalg.eigh(np.array([[-73/192-1,-3*np.sqrt(2)/32],[-3*np.sqrt(2)/32,-13/96]]));predshift=E4[0];predZ=U4[0,0]**2
for lam in [.1,.2]:
 start=time.monotonic();coeff=c*np.where(axes==2,1.,lam);calls=0
 def mv(a):
  global calls
  calls+=1
  if time.monotonic()-start>1800:raise TimeoutError('bounded native probe, no scientific inference')
  return apply(a,f,z,coeff)
 H=LinearOperator((dim,dim),matvec=mv,dtype=float);v=np.random.default_rng(8123).normal(size=dim)
 e,g=eigsh(H,k=1,which='SA',v0=v,tol=1e-12,ncv=24,maxiter=3000);g=g[:,0];e0=e[0];gres=np.linalg.norm(mv(g)-e0*g)
 src=apply(g,cf,cz,cc)/np.sqrt(L);src-=g*np.dot(g,src);weight=np.dot(src,src)
 print(dict(stage='ground',lam=lam,energy=e0,residual=gres,weight=weight,seconds=time.monotonic()-start),flush=True)
 steps=256;Q=np.memmap('/private/tmp/neutral_native_periodic_lanczos.dat',dtype='float64',mode='w+',shape=(steps,dim));q=src/np.sqrt(weight);prev=np.zeros_like(q);b=0.;aa=[];bb=[]
 for k in range(steps):
  Q[k]=q;w=mv(q)-e0*q-b*prev;a=np.dot(q,w);w-=a*q;w-=g*np.dot(g,w);nb=np.linalg.norm(w);aa.append(a)
  if k%64==63:print(dict(stage='lanczos',lam=lam,steps=k+1,seconds=time.monotonic()-start),flush=True)
  if k<steps-1:bb.append(nb)
  prev,q=q,w/nb;b=nb
 T=np.diag(aa)+np.diag(bb,1)+np.diag(bb,-1);en,uu=np.linalg.eigh(T);target=8-2*lam**2+lam**4*predshift
 choices=np.argsort(abs(en-target))[:6];cand=[]
 for ind in choices:
  vv=np.zeros(dim)
  for k in range(steps):vv+=uu[k,ind]*Q[k]
  norm=np.linalg.norm(vv);vv/=norm;energy=float(vv@mv(vv)-e0);res=float(np.linalg.norm(mv(vv)-(energy+e0)*vv));wt=float((vv@src)**2)
  cand.append(dict(quadrature_node=float(en[ind]),energy=energy,residual=res,source_weight=wt,ritz_norm=float(norm),weight_over_lambda4=wt/lam**4))
 row=dict(L=L,lambda_perp=lam,dimension=dim,ground_energy=float(e0),ground_residual=float(gres),source_weight=float(weight),prediction_energy=float(target),prediction_shift=float(predshift),prediction_weight_coefficient=float(2*predZ),candidates=cand,seconds=time.monotonic()-start,calls=calls,scope='Selected symmetry sector, finite periodic32site full-H eigenvector tests; no continuum decay or physical scalar claim')
 rows.append(row);Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2));print(row,flush=True);del Q
os.unlink('/private/tmp/neutral_native_periodic_lanczos.dat')
