import os
for x in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[x]='1'
import resource,time,json,hashlib,datetime,itertools
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(3,3));start=time.process_time();p=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929');assert not any((runtime/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'));assert datetime.datetime.now(datetime.timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
import numpy as np
with np.load(p/'PRE_ARRAYS.npz') as z:
 states=z['states'];F=z['F12'];res=z['residual_num'];B=z['B12'];U=z['upper_num'];G2=z['G2'];C=z['core'];Annz=len(z['A12']);X=z['Xnum']
 axial={(2*s if j==i else 0 for j in range(3)) for i in () for s in ()} # unused; explicit predicate below
 def adjacent(a,b):
  d=np.abs(a-b);return int(d.sum())==2 and (int(d.max()) in (1,2))
 def matched(S):
  return any(adjacent(S[a],S[b]) and adjacent(S[c],S[d]) for (a,b),(c,d) in (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))))
 active=np.flatnonzero(np.any(F!=0,axis=1));rr=np.flatnonzero(np.any(res!=0,axis=1));pF=sum(matched(states[i]) for i in active);pR=sum(matched(states[i]) for i in rr)
 m=np.array([1,-1,0,0,0,1,0,0,0,0,0,0,0,0,0],dtype=np.int64)
 result={'primary_status':'Mathematical assertions completed; resource envelope failed, disclosed separately. This step only extracts saved evidence.','core_dimension':len(C),'complete_source_orbits':len(active),'source_P_orbits':pF,'source_Q_orbits':len(active)-pF,'core_to_all_nonzero_entries':Annz,'all_boundary_source_orbits':len(states),'residual_orbits':len(rr),'residual_P_orbits':pR,'residual_Q_orbits':len(rr)-pR,'bare_matrix_denominator':12,'bare_matrix_numerator':B.tolist(),'raw_metric':G2.tolist(),'trial_denominator':1920,'raw_upper_matrix_denominator':12*1920**2,'raw_upper_matrix_numerator':U.tolist(),'normalized_E_threshold_upper_fraction':[int(m@U@m),2*12*1920**2],'source_direct_rows_checked_before_resource_assertion':15,'all_225_old_bare_entries_matched_before_resource_assertion':True,'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'array_sha256':hashlib.sha256((p/'PRE_ARRAYS.npz').read_bytes()).hexdigest()}
 assert result['cpu_seconds']<3 and result['peak_rss_bytes']<80*1024**2
 (p/'PRE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ('complete_source_orbits','source_P_orbits','source_Q_orbits','core_to_all_nonzero_entries','residual_orbits','normalized_E_threshold_upper_fraction','cpu_seconds','peak_rss_bytes')},indent=2))
