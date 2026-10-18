"""Memory-bounded20site native calculation; separate matrix-free implementation."""
from pathlib import Path
import json,numpy as np
from scipy.sparse.linalg import LinearOperator
import compass_scalar as base

def mf(shape,terms):
 n=int(np.prod(shape));size=1<<n;states=np.arange(size,dtype=np.int64);combined={}
 for i,j,a,c in terms:
  if i==j:key=(0,0)
  elif a==0:key=((1<<i)|(1<<j),0)
  elif a==1:key=((1<<i)|(1<<j),(1<<i)|(1<<j));c=-c
  else:key=(0,(1<<i)|(1<<j))
  combined[key]=combined.get(key,0)+c
 combined={k:v for k,v in combined.items() if abs(v)>1e-14};dtype=np.result_type(*combined.values())
 def mv(v):
  v=np.asarray(v).reshape(-1);out=np.zeros(size,dtype=np.result_type(v.dtype,dtype))
  for (flip,zmask),coef in combined.items():
   sign=np.ones(size,dtype=np.int8)
   for bit in range(n):
    if zmask>>bit&1:sign*=1-2*((states>>bit)&1).astype(np.int8)
   out+=coef*sign*v[states^flip]
  return out
 return LinearOperator((size,size),matvec=mv,dtype=dtype)
if __name__=='__main__':
 # Different assembly path tested before the larger solve.
 shape=(2,2,2);rng=np.random.default_rng(31);terms=[(0,1,0,.7),(1,3,1,-.4),(3,6,2,1.2),(4,4,0,2.)];v=rng.normal(size=256)+1j*rng.normal(size=256)
 assert np.linalg.norm(mf(shape,terms)@v-base.operator(shape,terms)@v)<1e-12
 base.operator=mf
 result=base.run((5,2,2))
 Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'20site thin torus; matrix-free supplied native compass Hamiltonian, finite-state diagnostic','row':result},indent=2)+'\n')
