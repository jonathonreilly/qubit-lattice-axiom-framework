#!/usr/bin/env python3
"""Exact source from local SOS defects; disclosed reuse of polynomial geometry."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import resource,signal,time,json,hashlib
from pathlib import Path
from collections import defaultdict
from itertools import combinations
resource.setrlimit(resource.RLIMIT_CPU,(60,61));signal.alarm(120)
t0,c0=time.monotonic(),time.process_time();out=Path(__file__).resolve().parent;pack=out.parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
 assert not(runtime/'STOP_REQUESTED.json').exists()
 assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
 assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<180*1024**2
guard()
import numpy as np
src=pack/'native-interaction-route/compute_quartic.py';ns={'__file__':str(src)}
exec(compile(src.read_text().split('d0=[defects')[0],str(src),'exec'),ns)
zero,unit,add,sub,types,planes,defects,four,D=[ns[k] for k in ('zero','unit','add','sub','types','planes','defects','four','D')]
canonical=lambda S:tuple(sorted(sub(x,min(S)) for x in S))
d0=[defects(zero,t) for t in types];neighbors=[tuple(s*x for x in e) for e in unit for s in (-1,1)]
dnear=[[defects(e,t) for t in types] for e in neighbors]
keys=set().union(*(set(d) for d in d0),*(set(d) for ds in dnear for d in ds));zero15=np.zeros(15,dtype=np.int64)
Fm=defaultdict(lambda:np.zeros(15,dtype=np.int64));Ft=defaultdict(lambda:np.zeros(15,dtype=np.int64))
for r in keys:
 ps=np.array([d.get(r,(0,)*15) for d in d0],dtype=np.int64)
 lap=6*ps-sum((np.array([d.get(r,(0,)*15) for d in ds],dtype=np.int64) for ds in dnear),np.zeros((15,15),dtype=np.int64))
 cm=np.zeros((15,15),dtype=np.int64);ct=np.zeros((15,15),dtype=np.int64)
 cm[:3]=8*sum(ps[:3]);ct[:3]=12*lap[:3]-4*sum(lap[:3])
 for ids in planes:
  cm[ids]=3*(4*ps[ids]-sum(ps[ids]));ct[ids]=3*sum(lap[ids])
 for i,(a,b,sg) in enumerate(types):
  if a in r or b in r:continue
  S=canonical((a,b)+r);Fm[S]+=sg*cm[i];Ft[S]+=sg*ct[i]
for trio in combinations(D,3):
 S=canonical((zero,)+trio);Fm[S]+=12*np.array(four((zero,)+trio),dtype=np.int64)
keys=sorted(S for S in set(Fm)|set(Ft) if np.any(Fm.get(S,zero15)) or np.any(Ft.get(S,zero15)))
FM=np.array([Fm.get(S,zero15) for S in keys]);FT=np.array([Ft.get(S,zero15) for S in keys]);PHI=np.array([four(S) for S in keys],dtype=np.int64)
raw=json.loads((pack/'native-interaction-route/quartic.json').read_text())
assert np.array_equal(PHI.T@FM,raw['energy_mu_matrix_numerator'])
assert np.array_equal(PHI.T@FT,raw['energy_tau_matrix_numerator'])
core=np.load(out/'CORE_TRIAL.npz');fi={S:i for i,S in enumerate(keys)}
assert all(np.array_equal(FM[fi[S]]+FT[fi[S]],row) if S in fi else not np.any(row) for SS,row in zip(core['core'],core['F12']) for S in [tuple(map(tuple,SS.tolist()))])
# Validate full support by the SOS construction; core row comparison is an
# independent algebraic expression within this author route, not independent review.
np.savez_compressed(out/'COMPLETE_SOURCE.npz',shapes=np.array(keys,dtype=np.int16),mu_source12=FM,tau_source12=FT)
result={'source_shape_count':len(keys),'residual_pair_keys':len(keys),'mu_nonzero_rows':int(np.any(FM,axis=1).sum()),'tau_nonzero_rows':int(np.any(FT,axis=1).sum()),'max_coordinate_span':max(max(max(x[k] for x in S)-min(x[k] for x in S) for k in range(3)) for S in keys),'checks':['all225 mu bare-energy coefficients','all225 tau bare-energy coefficients','all1487x15 direct-row core source coefficients'],'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'reused_geometry_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
guard();(out/'SOURCE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
