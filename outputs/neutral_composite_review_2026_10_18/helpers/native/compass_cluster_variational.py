"""Cluster-product variational search with exact boundary variance identity.
No dynamical decoupling, convergence-to-ground or physical state assumption.
"""
import itertools,json,sys
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix,csr_matrix
from scipy.sparse.linalg import eigsh
P=Path(__file__).resolve().parent

def run(shape,seed,maxiter=120):
 sites=list(itertools.product(*(range(L) for L in shape)));idx={x:i for i,x in enumerate(sites)};n=len(sites);dim=1<<n;bits=np.arange(dim);ops={}
 for i in range(n):
  z=1-2*((bits>>i)&1)
  for a in range(3):
   target=bits if a==2 else bits^(1<<i); val=z if a==2 else (np.ones(dim) if a==0 else 1j*z)
   ops[i,a]=coo_matrix((val,(target,bits)),shape=(dim,dim)).tocsr()
 H=csr_matrix((dim,dim),dtype=complex);faces=[[] for _ in range(3)]
 for x,i in idx.items():
  for a,L in enumerate(shape):
   y=list(x)
   if x[a]<L-1:
    y[a]+=1;H-=ops[i,a]@ops[idx[tuple(y)],a]
   else:
    y[a]=0;faces[a].append((i,idx[tuple(y)]))
 rng=np.random.default_rng(seed);m=np.zeros((n,3))
 if seed==0:m[:,2]=.9
 elif seed==1:m[:]=rng.normal(size=(n,3))*.1
 psi=rng.normal(size=dim)+1j*rng.normal(size=dim);psi/=np.linalg.norm(psi)
 history=[]
 for it in range(maxiter):
  heff=H.copy()
  for a,face in enumerate(faces):
   for i,j in face:heff-=m[j,a]*ops[i,a]+m[i,a]*ops[j,a]
  ev,u=eigsh(heff,k=1,which='SA',v0=psi,tol=1e-11);psi=u[:,0]
  new=np.array([[np.vdot(psi,ops[i,a]@psi).real for a in range(3)] for i in range(n)])
  err=np.max(abs(new-m));E=np.vdot(psi,H@psi).real-sum(new[i,a]*new[j,a] for a,face in enumerate(faces) for i,j in face)
  history.append(dict(iteration=it,energy_per_site=float(E/n),self_consistency=float(err)))
  m=.5*(m+new)
  if err<2e-9:break
 # Rebuild from actual moments, so variance identity holds even if iteration stopped.
 m=new;heff=H.copy()
 for a,face in enumerate(faces):
  for i,j in face:heff-=m[j,a]*ops[i,a]+m[i,a]*ops[j,a]
 hp=heff@psi;res=hp-psi*np.vdot(psi,hp);localvar=np.vdot(res,res).real
 boundary=[]
 for a,face in enumerate(faces):
  upper=np.array([ops[i,a]@psi-m[i,a]*psi for i,j in face]);lower=np.array([ops[j,a]@psi-m[j,a]*psi for i,j in face])
  gu=upper.conj()@upper.T;gl=lower.conj()@lower.T
  boundary.append(float(np.sum(gu*gl).real))
 out=dict(shape=shape,seed=seed,iterations=len(history),converged=bool(err<2e-9),energy_per_site=float(E/n),local_residual_per_site=float(localvar/n),boundary_variance_per_site=[x/n for x in boundary],full_variance_per_site=float((localvar+sum(boundary))/n),moments=m.tolist(),history=history,scope='Supplied cluster-product trial, J=1; variational search not guaranteed global optimum; full variance retained')
 np.savez_compressed(P/('cluster_'+'x'.join(map(str,shape))+'_seed'+str(seed)+'.npz'),psi=psi)
 return out
if __name__=='__main__':
 shape=tuple(map(int,sys.argv[1].split('x'))) if len(sys.argv)>1 else (2,2,2)
 rows=[]
 for seed in ([int(sys.argv[2])] if len(sys.argv)>2 else [0,1,2]):
  out=run(shape,seed);rows.append(out);print({k:v for k,v in out.items() if k not in ['history','moments']},flush=True)
  (P/('cluster_'+'x'.join(map(str,shape))+'.json')).write_text(json.dumps(rows,indent=2)+'\n')
