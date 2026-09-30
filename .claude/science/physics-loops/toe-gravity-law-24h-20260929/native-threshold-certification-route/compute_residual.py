#!/usr/bin/env python3
"""Compute actual compact residual and exact global-norm trial improvement."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import resource,signal,time,json
from pathlib import Path
from collections import defaultdict
resource.setrlimit(resource.RLIMIT_CPU,(60,61));signal.alarm(120)
t0,c0=time.monotonic(),time.process_time();out=Path(__file__).resolve().parent;pack=out.parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert not(runtime/'STOP_REQUESTED.json').exists()
 assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
 assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<256*1024**2
guard()
import numpy as np
source=pack/'native-scattering-route/check_matching.py';ns={};exec(compile(source.read_text().split('# All abstract graphs')[0],str(source),'exec'),ns)
canonical,action12=[ns[k] for k in ('canonical','action12')]
c=np.load(out/'CORE_TRIAL.npz');s=np.load(out/'COMPLETE_SOURCE.npz');scale=int(c['scale'])
R={tuple(map(tuple,S.tolist())):scale*(m+t) for S,m,t in zip(s['shapes'],s['mu_source12'],s['tau_source12'])}
for i,(SS,x) in enumerate(zip(c['core'],c['X_numerator'])):
 S=tuple(map(tuple,SS.tolist()));row=defaultdict(int)
 for z,(a,b) in action12(S).items():row[canonical(z)]+=a+b
 for z,v in row.items():
  if v:
   if z not in R:R[z]=np.zeros(15,dtype=np.int64)
   R[z]+=v*x
 if i%50==0:guard()
keys=sorted(S for S,r in R.items() if np.any(r));RM=np.array([R[S] for S in keys],dtype=np.int64)
# Object arithmetic avoids silently overflowing the exact Gram certificate.
RO=RM.astype(object);gram=RO.T@RO;del RO
old=json.loads((out/'CORE_RESULTS.json').read_text());Q=np.array([[int(a) for a in row] for row in old['upper_pulse_matrix_numerator']],dtype=object)
# H_N4 <= 160 at the supplied benchmark, so chi-r/160 improves at least
# <r,r>/160. New bound denominator is 160*144*scale^2.
den=160*144*scale**2;new=1920*Q-gram
from fractions import Fraction
mon=[tuple(x) for x in old['monomial_order']];pe=np.zeros(15,dtype=object)
pe[mon.index((0,0))]=1;pe[mon.index((0,1))]=-1;pe[mon.index((1,1))]=1
E=Fraction(int(pe@new@pe),2*den);T=Fraction(int(new[mon.index((2,2)),mon.index((2,2))]),2*den)
np.savez_compressed(out/'RESIDUAL.npz',shapes=np.array(keys,dtype=np.int16),numerator=RM,denominator=12*scale)
result={'scope':'Exact residual and operator-norm-controlled compact-trial upper bound, not full threshold form or lower estimate.','residual_rows':len(keys),'residual_denominator':12*scale,'residual_gram_numerator':[[str(int(x)) for x in row] for row in gram],'improved_upper_pulse_matrix_denominator':den,'improved_upper_pulse_matrix_numerator':[[str(int(x)) for x in row] for row in new],'exact_normalized_coherent_threshold_upper':{'E1':str(E),'T12':str(T)},'coherent_upper_float_display':{'E1':float(E),'T12':float(T)},'operator_norm_bound':160,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
guard();(out/'RESIDUAL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if 'matrix_numerator' not in k and 'gram_numerator' not in k},indent=2))
