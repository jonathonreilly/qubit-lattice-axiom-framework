from pathlib import Path
import importlib.util
import numpy as np
from itertools import product
from scipy.linalg import eigvalsh
import json,time
path=Path(__file__).resolve().with_name('block8_principal_transfer_check.py')
spec=importlib.util.spec_from_file_location('check',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
f,d,states,basis=m.cube_geometry()
lifts=np.array(list(product([-1,0,1],repeat=12)),dtype=np.int8)
curl=lifts@f.T;energy=np.sum(lifts*lifts,axis=1)
powers=3**np.arange(6);keys=((states+1)%3)@powers
lookup=np.full(3**6,-1,dtype=int);lookup[keys]=np.arange(243)
rows=[]
for q,mu in [(.638,1.),(.9,1.),(.9,10.)]:
 start=time.monotonic();k=np.zeros((243,243));base=q**energy/(1+2*q)**12
 for j,b in enumerate(states):
  bp=m.principal(b+curl);targets=lookup[((bp+1)%3)@powers]
  mismatch=(bp-b-curl)//3
  assert min(targets)>=0
  weight=base*np.exp(-mu*np.sum(mismatch*mismatch,axis=1))
  k[:,j]=np.bincount(targets,weights=weight,minlength=243)
 vals=eigvalsh(k);result=dict(q=q,mu=mu,min_eigenvalue=float(vals[0]),five_smallest=vals[:5].tolist(),symmetry=float(np.max(np.abs(k-k.T))),max_row_sum=float(np.max(k.sum(axis=0))),seconds=time.monotonic()-start)
 rows.append(result);print(json.dumps(result),flush=True)
np.savez(path.parent/'BLOCK8_PRINCIPAL_CUBE_LAST_MATRIX.npz',kernel=k,states=states,F=f,D=d,q=q,mu=mu)
(path.parent/'BLOCK8_PRINCIPAL_CUBE_PROBE.json').write_text(json.dumps(rows,indent=2)+'\n')
