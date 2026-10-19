"""Actual infinite-lattice C time derivatives in a block-product preparation."""
import itertools,json,sys
from pathlib import Path
import numpy as np
from compass_local_transport import word,shift,derivative
P=Path(__file__).resolve().parent

def run(shape,seed=0):
 psi=np.load(P/('cluster_'+'x'.join(map(str,shape))+'_seed'+str(seed)+'.npz'))['psi'];bits=np.arange(len(psi));sites=list(itertools.product(*(range(L) for L in shape)));idx={x:i for i,x in enumerate(sites)};cache={():1.}
 def local(w):
  w=tuple(sorted(w))
  if w not in cache:
   flip=0;phase=np.ones(len(psi),complex)
   for i,a in w:
    if a!=2:flip^=1<<i
    if a in [1,2]:phase*=1-2*((bits>>i)&1)
    if a==1:phase*=1j
   cache[w]=np.vdot(psi[bits^flip],phase*psi)
  return cache[w]
 def mean(w):
  blocks={}
  for *coords,a in w:
   b=tuple(coords[i]//shape[i] for i in range(3));p=tuple(coords[i]%shape[i] for i in range(3));blocks.setdefault(b,[]).append((idx[p],a))
  return np.prod([local(v) for v in blocks.values()])
 C={word([(shift((0,0,0),a,-1),a),(shift((0,0,0),a,1),a)]):1 for a in range(3)};ops=[C]
 for _ in range(2):ops.append(derivative(ops[-1]))
 rows=[]
 for x in sites:
  values=[]
  for order,A in enumerate(ops):
   val=sum(c*mean(tuple((*tuple(v[i]+x[i] for i in range(3)),v[3]) for v in w)) for w,c in A.items())
   assert abs(val.imag)<1e-7
   values.append(float(val.real)*(-1)**order) # H=-sum bonds
  rows.append(dict(site=list(x),C=values[0],dC_dt=values[1],d2C_dt2=values[2]))
 out=dict(shape=shape,seed=seed,average={k:float(np.mean([r[k] for r in rows])) for k in ['C','dC_dt','d2C_dt2']},rows=rows,cached_local_words=len(cache),scope='Initial exact full-H Heisenberg derivatives in supplied nonstationary cluster-product state, J=1; not equilibrium spectral response')
 (P/('cluster_acceleration_'+'x'.join(map(str,shape))+'.json')).write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='rows'},flush=True)
if __name__=='__main__':run(tuple(map(int,sys.argv[1].split('x'))) if len(sys.argv)>1 else (2,2,2))
