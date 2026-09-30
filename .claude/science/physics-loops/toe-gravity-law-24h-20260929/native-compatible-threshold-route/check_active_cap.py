#!/usr/bin/env python3
"""One literal full-carrier fixture with an active cell number cutoff."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import itertools,json,math,resource,time,hashlib
from pathlib import Path
start=time.monotonic(); cpu=time.process_time()
p=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
S=frozenset((1+10*i+shift,1+10*j,1+10*k) for i,j,k in itertools.product(range(3),repeat=3) for shift in (0,2))
def distance(x,y):return max(abs(a-b) for a,b in zip(x,y))
def graph(x,y):
    d=sorted(abs(a-b) for a,b in zip(x,y))
    return d in ([0,0,2],[0,1,1])
def selected(R):
    return [frozenset((x,y)) for x,y in itertools.combinations(S,2) if graph(x,y) and all(min(distance(z,x),distance(z,y))>R for z in S-{x,y})]
small=selected(2); big=selected(40)
ell=40; M=math.ceil(8*ell**3/40**3); K=2*M
n=len(small); nb=len(big); B= len(S)-2*nb
loss=n if n>K else 0
assert len(S)==54 and n==27 and nb==0 and K==16
assert loss==27 and loss<=2*(n-nb)<=B
out={'physical_particles':len(S),'small_radius':2,'large_radius':40,'ell':ell,'M':M,'K':K,'selected_small':n,'selected_large':nb,'lost_selected_pairs':loss,'B_large':B,'cutoff_active':True,'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert out['peak_rss_bytes']<50*1024*1024
(p/'active_cap.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
