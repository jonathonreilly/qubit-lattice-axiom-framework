"""All symmetry sectors modulo exact global-Z-sign equivalence; numerical lows."""
import itertools,json,time
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator,eigsh
from compass_sector_basis import basis
from compass_sector_solve import apply
P=Path(__file__).resolve().parent;rows=[];start=time.monotonic();best=1e10
for number,bits in enumerate(itertools.product([0,1],repeat=4)):
 zsign=[0,*bits[:2]];xsign=list(bits[2:]);d=basis((3,3,3),zsign,xsign);terms=np.array(d['terms'],np.int64);calls=[0]
 def mv(v):
  if time.monotonic()-start>2400:raise TimeoutError('survey local2400s limit; partial rows preserved, no scientific conclusion')
  calls[0]+=1;return apply(v,*terms.T.copy())
 op=LinearOperator((d['dimension'],d['dimension']),matvec=mv,dtype=float)
 seed=7100+number;v=np.random.default_rng(seed).normal(size=d['dimension']);v/=np.linalg.norm(v)
 ev,u=eigsh(op,k=1,which='SA',v0=v,tol=1e-10,ncv=16,maxiter=800);g=u[:,0];res=np.linalg.norm(op@g-ev[0]*g)
 assert res<1e-6
 row=dict(zsign=zsign,xsign=xsign,energy=float(ev[0]),residual=float(res),calls=calls[0],seed=seed,elapsed_total=time.monotonic()-start);rows.append(row)
 if ev[0]<best-1e-8:
  best=ev[0];np.savez_compressed(P/'stationary_survey_best.npz',vector=g,energy=ev[0],zsign=zsign,xsign=xsign)
 (P/'stationary_sector_survey.json').write_text(json.dumps(dict(rows=rows,complete=len(rows)==16,equivalence='one X-plane flips all3 Z-plane signs while preserving X-pair signs and H; first Zsign fixed0',scope='Numerically lowest Ritz values; no interval certification of global lower spectral edge, no state-selection or bulk inference'),indent=2)+'\n');print(row,flush=True)
