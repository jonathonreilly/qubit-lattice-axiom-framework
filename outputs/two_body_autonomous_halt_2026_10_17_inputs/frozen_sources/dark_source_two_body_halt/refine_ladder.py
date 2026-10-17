#!/usr/bin/env python3
"""Refine a saved numerical lead, allowing signed clock onsite energies.

A negative mu*n is represented physically as |mu|*(I-n), with an explicitly
retained scalar |mu| I; this script reports phases after that scalar shift.
"""
import json,time
import numpy as np
from scipy.optimize import least_squares
import probe_ladder as model
from probe import OUT
start=time.monotonic()
previous=json.loads((OUT/'ladder_optimization.json').read_text())
lower=np.array(previous['lower']);upper=np.array(previous['upper'])
lower[-2:]=[-10,-10]
x=np.array(previous['best']['x'])
sol=least_squares(model.residual,x,bounds=(lower,upper),max_nfev=12000,
  ftol=1e-14,xtol=1e-14,gtol=1e-14,verbose=0)
r,info=model.reflection(sol.x,True)
record=dict(kind='numerical refinement, not an exact certificate',
 parent='ladder_optimization.json',max_nfev=12000,lower=lower.tolist(),upper=upper.tolist(),
 x=sol.x.tolist(),residual=sol.fun.tolist(),norm=float(np.linalg.norm(sol.fun)),
 nfev=sol.nfev,success=bool(sol.success),message=sol.message,
 physical_scalar_reserve=float(sum(max(0,-a) for a in sol.x[-2:])),
 r_real=r.real.tolist(),r_imag=r.imag.tolist(),channels=info,elapsed_seconds=time.monotonic()-start)
(OUT/'ladder_refinement.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
