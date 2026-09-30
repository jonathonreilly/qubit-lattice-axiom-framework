"""Independent exact actual-spin coefficient inequalities before proof exposure."""
import os
for x in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[x]='1'
from fractions import Fraction as F
from pathlib import Path
import resource,time,json,hashlib,itertools
resource.setrlimit(resource.RLIMIT_CPU,(5,5));t0=time.process_time();out=Path(__file__).resolve().parent
rt=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929');assert not any((rt/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'));assert time.time()<json.loads((rt/'DEADLINE.json').read_text())['deadline_epoch']
def w(S,m,s):
 return F(S*(S+1)-m*(m+s),S*(S+1)) if -S<=m<=S and -S<=m+s<=S else F(0)
def sqrt_error_leq(p,b):
 assert 0<=p<=1 and b>=0
 assert b>=1 or p>=(1-b)**2
single=same=different=loss=0;nontrivial=0
for S in range(1,17):
 C=S*(S+1);fields=range(-S-2,S+3)
 for m in fields:
  for sig in (-1,1):
   aa=w(S,m,sig);bd=F(abs(m)*(abs(m)+1),C);assert 1-aa<=bd;sqrt_error_leq(aa,bd);single+=1
  ell=2-w(S,m,1)-w(S,m,-1);assert 0<=ell<=F(2*m*m,C);loss+=1
  for s,t in itertools.product((-1,1),repeat=2):
   q=1+abs(m);p=w(S,m,s)*w(S,m+s,t);b=F(2*q*q,C);sqrt_error_leq(p,b);same+=1;nontrivial+=b<1
  for n in fields:
   for s,t in itertools.product((-1,1),repeat=2):
    q=1+abs(m)+abs(n);p=w(S,m,s)*w(S,n,t);b=F(2*q*q,C);sqrt_error_leq(p,b);different+=1;nontrivial+=b<1
 # Forbidden physical outward step demonstrates why an unweighted norm limit fails.
 assert w(S,S,1)==0
result={'spins':list(range(1,17)),'single_shift_and_compensation_checks':single,'exact_original_loss_checks':loss,'same_link_two_step_checks':same,'different_link_two_step_checks':different,'nontrivial_two_step_bounds_below_one':nontrivial,'physical_outward_boundary_zero_checked_each_spin':True,'new_author_proof_code_results_read':False,'cpu_seconds':time.process_time()-t0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2));assert result['cpu_seconds']<5 and result['peak_rss_bytes']<60*1024**2
(out/'PRE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
