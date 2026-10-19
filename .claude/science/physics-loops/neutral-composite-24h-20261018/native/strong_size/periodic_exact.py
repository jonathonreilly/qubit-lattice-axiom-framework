from pathlib import Path
import sys,json,time
import numpy as np
from scipy.sparse.linalg import eigsh,LinearOperator
P=Path(__file__).resolve().parents[1];sys.path.insert(0,str(P))
from compass_sector_basis import basis
from compass_sector_solve import apply
rows=[]
for L in [4,6,8]:
 t0=time.monotonic();d=basis((2,2,L));idx={p:i for i,p in enumerate(d['sites'])};ts=list(d['terms'])
 for x in range(2):
  for y in range(2):ts.append(d['reduce_term'](0,(1<<idx[x,y,0])|(1<<idx[x,y,L-1]),-1))
 ts=np.array(ts,dtype=np.int64);H=lambda v:apply(v,*ts.T.copy());op=LinearOperator((d['dimension'],)*2,matvec=H,dtype=float)
 en,v=eigsh(op,k=1,which='SA',tol=1e-11,ncv=20,v0=np.random.default_rng(98400+L).normal(size=d['dimension']));g=v[:,0];e=float(en[0]);raw=[]
 for ell in range(2,L//2+1,2):
  mask=sum(1<<i for i,(x,y,z) in enumerate(d['sites']) if x==0 and z<ell);term=np.array([d['reduce_term'](mask,0,1)],dtype=np.int64);u=apply(g,*term.T.copy());raw.append(dict(length=ell,energy=float(u@H(u)-e)))
 row=dict(L=L,energy=e,residual=float(np.linalg.norm(H(g)-e*g)),raw=raw,seconds=time.monotonic()-t0);rows.append(row);print(row,flush=True)
 (P/'strong_size/periodic_exact.json').write_text(json.dumps(rows,indent=2)+'\n')
