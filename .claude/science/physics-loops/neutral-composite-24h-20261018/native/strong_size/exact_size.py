from pathlib import Path
import sys,time,json
import numpy as np
from scipy.linalg import eigh
from scipy.sparse.linalg import eigsh,LinearOperator
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from compass_sector_basis import basis,dense_terms
from compass_sector_solve import apply

def main():
 rows=[]
 for L in [4,6,8]:
  start=time.monotonic();D=basis((2,2,L));terms=np.array(D['terms'],np.int64);dim=D['dimension'];H=lambda v:apply(v,*terms.T.copy());op=LinearOperator((dim,dim),matvec=H,dtype=float)
  if L==8 and (P/'stationary_2x2x8_plus.npz').exists():
   s=np.load(P/'stationary_2x2x8_plus.npz');g=s['vectors'][:,0].copy();e0=float(s['values'][0]);del s
  else:
   v=np.random.default_rng(733+L).normal(size=dim);E,V=eigsh(op,k=1,which='SA',tol=1e-12,v0=v,ncv=20);g=V[:,0];e0=float(E[0])
  res=float(np.linalg.norm(H(g)-e0*g));assert res<1e-8
  lengths=list(range(2,L-1,2));sources=[];means=[];diags=[]
  for ell in lengths:
   a=(L-ell)//2;mask=sum(1<<i for i,(x,y,z) in enumerate(D['sites']) if x==0 and a<=z<a+ell)
   t=np.array([D['reduce_term'](mask,0,1)],np.int64);u=apply(g,*t.T.copy());mu=float(g@u);s=u-mu*g;sources.append(s);means.append(mu)
   energy=float(u@H(u)-e0);diags.append(energy)
  V=np.array(sources).T;HV=np.array([H(s)-e0*s for s in sources]).T
  levels=[]
  for depth in [0,1]:
   B=V if depth==0 else np.column_stack((V,HV));G=B.T@B;sv,U=eigh(G);keep=sv>1e-10*max(sv)
   W=B@(U[:,keep]/np.sqrt(sv[keep]));HW=np.array([H(W[:,i])-e0*W[:,i] for i in range(W.shape[1])]).T
   T=W.T@HW;T=(T+T.T)/2;ev,c=eigh(T);Y=W@c;HY=HW@c
   rr=np.linalg.norm(HY-Y*ev[None,:],axis=0)
   overlap=V.T@Y;weights=overlap**2/np.diag(G[:len(lengths),:len(lengths)])[:,None]
   levels.append(dict(depth=depth,rank=int(sum(keep)),eigenvalues=ev.tolist(),residuals=rr.tolist(),probe_overlap_squared=weights.tolist()))
  row=dict(L=L,physical_qubits=4*L,dimension=dim,lambda_value=1,ground_energy=e0,ground_residual=res,lengths=lengths,raw_string_energy=diags,source_means=means,source_gram=(V.T@V).tolist(),ritz=levels,seconds=time.monotonic()-start)
  rows.append(row);(P/'strong_size/exact_size.json').write_text(json.dumps(dict(scope='Full native H, exact selected CSS sector on open thin grids; Ritz residuals are reported, not assumed eigenstates; no bulk or size optimum',rows=rows),indent=2)+'\n');print(dict(L=L,diagonal=diags,levels=[(x['eigenvalues'][:2],x['residuals'][:2]) for x in levels],seconds=row['seconds']),flush=True)
if __name__=='__main__':main()
