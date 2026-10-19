"""Stationary finite open-grid selected-sector benchmark, full native H."""
import json,time,sys,os
from pathlib import Path
import numpy as np
from numba import njit,prange,set_num_threads
from scipy.sparse.linalg import LinearOperator,eigsh
from compass_sector_basis import basis,dense_terms
P=Path(__file__).resolve().parent
set_num_threads(min(4,os.cpu_count() or 1))
@njit(parallel=True)
def apply(v,flips,zs,coefs):
 out=np.empty_like(v)
 for i in prange(len(v)):
  value=0.
  for t in range(len(flips)):
   j=i^flips[t];w=j&zs[t]
   w^=w>>32;w^=w>>16;w^=w>>8;w^=w>>4
   odd=(0x6996>>(w&15))&1
   value+=coefs[t]*(1-2*odd)*v[j]
  out[i]=value
 return out

def main():
 shape=tuple(map(int,sys.argv[1].split('x'))) if len(sys.argv)>1 else (3,3,3)
 d=basis(shape);terms=np.array(d['terms'],dtype=np.int64);f,z,c=terms.T.copy();dim=d['dimension'];start=time.monotonic();calls=0
 # Independent-of-ARPACK implementation control against small dense matrix.
 small=basis((2,2,2));st=np.array(small['terms'],dtype=np.int64);test=np.random.default_rng(188).normal(size=32)
 assert np.max(abs(apply(test,*st.T.copy())-dense_terms(small['terms'],32)@test))<1e-12
 def mv(v):
  nonlocal calls
  if time.monotonic()-start>1800:raise TimeoutError('owned stationary benchmark reached1800s; no science conclusion')
  calls+=1
  return apply(v,f,z,c)
 op=LinearOperator((dim,dim),matvec=mv,dtype=float);v=np.random.default_rng(181).normal(size=dim);v/=np.linalg.norm(v)
 tick=time.monotonic();op@v;print(json.dumps(dict(shape=shape,dimension=dim,terms=len(terms),matvec_seconds=time.monotonic()-tick)),flush=True)
 values,vectors=eigsh(op,k=4,which='SA',v0=v,tol=2e-10,ncv=20,maxiter=1000)
 order=np.argsort(values);values=values[order];vectors=vectors[:,order]
 residuals=[float(np.linalg.norm(op@vectors[:,i]-values[i]*vectors[:,i])) for i in range(4)]
 assert max(residuals)<1e-6
 tag='x'.join(map(str,shape));np.savez_compressed(P/('stationary_'+tag+'_plus.npz'),values=values,vectors=vectors)
 out=dict(shape=shape,sector='all selected Z planes and adjacent X-plane pairs +1',dimension=dim,energies=values.tolist(),residuals=residuals,calls=calls,elapsed_seconds=time.monotonic()-start,scope='Numerical low eigenpairs of one exact invariant sector; no global ground, thermodynamic pole or physical preparation identification')
 (P/('stationary_'+tag+'_plus.json')).write_text(json.dumps(out,indent=2)+'\n');print(out,flush=True)
if __name__=='__main__':main()
