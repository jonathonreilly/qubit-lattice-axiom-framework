#!/usr/bin/env python3
"""Remaining shared start/time budget, with mu0>=0 and mu1 signed."""
import sys
sys.dont_write_bytecode=True
import json,time,datetime
import numpy as np
from scipy.optimize import least_squares
import search as model
ROOT=model.ROOT
prior=json.loads((ROOT/'SEARCH.json').read_text())
remaining=60-prior['completed_starts'];available=max(0,180-prior['elapsed_seconds'])
seed=2026101604;rng=np.random.default_rng(seed);start=time.monotonic()
lower=np.array([.03,.08,.005,.005,.001,.001,0,0,0,.001,0,-4])
upper=np.array([.49,np.pi-.003,1.,1.,4.,4.,4.,4.,4.,4.,4.,4.])
rows=[];best=None
for i in range(remaining):
 if i==0:
  old=np.array(prior['best']['x'])
  x=old.copy();x[2],x[3]=old[3],old[2];x[5],x[9]=old[9],old[5]
  x[7],x[8]=old[8],old[7];x[10],x[11]=old[11],old[10]
 elif i%3==0 and best is not None:
  x=np.array(best['x'])+rng.normal(0,.1,12)*(upper-lower)
 else:
  x=lower+(upper-lower)*rng.random(12)
  x[1]=np.pi-np.exp(rng.uniform(np.log(.0031),np.log(1.4)))
  x[2:4]=rng.uniform(.3,1,2)
  x[4:6]=np.exp(rng.uniform(np.log(.02),np.log(4),2));x[9]=np.exp(rng.uniform(np.log(.02),np.log(4)))
  x[7:9]=rng.uniform(0,2,2);x[10]=rng.uniform(0,1);x[11]=rng.uniform(-1,1)
 x=np.maximum(lower+1e-10,np.minimum(upper-1e-10,x));n0=model.calls;ts=time.monotonic()
 try:
  sol=least_squares(model.residual,x,bounds=(lower,upper),max_nfev=500,ftol=2e-11,xtol=2e-11,gtol=2e-11)
  nc=model.calls-n0;row=model.describe(sol.x)
  row.update(index=prior['completed_starts']+i,lower=lower.tolist(),upper=upper.tolist(),initial=x.tolist(),
   nfev_reported=int(sol.nfev),actual_optimizer_residual_calls=nc,success=bool(sol.success),
   message=str(sol.message),elapsed_seconds=time.monotonic()-ts)
  if best is None or row['numerical_target_error']<best['numerical_target_error']:
   best=row;print(json.dumps({'new_best':row['index'],'error':row['numerical_target_error'],
    'phase_norm':row['phase_residual_norm'],'loads':row['added_incident_loads'],'x':row['x']}),flush=True)
 except Exception as e:
  row=dict(index=prior['completed_starts']+i,failure=repr(e),elapsed_seconds=time.monotonic()-ts)
 rows.append(row)
 result=dict(kind='bounded numerical discovery, mu0>=0; no certificate',seed=seed,
  original_starts=prior['completed_starts'],original_search_seconds=prior['elapsed_seconds'],
  max_new_starts=remaining,max_nfev_per_start=500,remaining_wall_checkpoint_seconds=available,
  total_shared_start_cap=60,total_shared_search_checkpoint_seconds=180,
  new_starts=len(rows),combined_starts=prior['completed_starts']+len(rows),
  elapsed_seconds=time.monotonic()-start,combined_search_seconds=prior['elapsed_seconds']+time.monotonic()-start,
  model_residual_calls=model.calls,best=best,rows=rows)
 (ROOT/'ALLOWED_SEARCH.json').write_text(json.dumps(result,indent=2)+'\n')
 if time.monotonic()-start>=available:break
 if best is not None and best['numerical_target_error']<1e-9:break
print(json.dumps({'combined_starts':result['combined_starts'],'combined_search_seconds':result['combined_search_seconds'],'best':best}),flush=True)
