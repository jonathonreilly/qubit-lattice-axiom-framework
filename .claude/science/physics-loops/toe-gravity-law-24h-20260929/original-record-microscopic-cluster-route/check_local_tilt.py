"""Exact sparse original cubic birth-word discriminator; integer arithmetic only."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from collections import defaultdict
from itertools import product
import hashlib,json,resource,time
start=time.process_time();here=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
import datetime
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not any((runtime/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'))
assert datetime.datetime.now(datetime.timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
neg=lambda a:tuple(-x for x in a)
axes=((1,0,0),(0,1,0),(0,0,1));dirs=axes+tuple(map(neg,axes))
def parity(v):return sum(v)%2
def default(v):return 1 if parity(v)==0 else 0
# A basis key contains only changed charges and nonzero A->B electric fields.
def pack(q,E):return (tuple(sorted((v,x) for v,x in q.items() if x!=default(v))),tuple(sorted((a,b,e) for (a,b),e in E.items() if e)))
def unpack(key):return dict(key[0]),{(a,b):e for a,b,e in key[1]}
def charge(q,v):return q.get(v,default(v))
Omega=pack({},{});a=(0,0,0)
def move(key,a,b,kind,sign=1):
    q,E=unpack(key);qa,qb=charge(q,a),charge(q,b)
    if kind=='out':
        if not qa or qb:return None
        q[a]=0;q[b]=qa;step=-qa
    elif kind=='in':
        if qa or not qb:return None
        q[a]=qb;q[b]=0;step=qb
    else:
        if qa or qb:return None
        q[a]=sign;q[b]=-sign;step=sign
    E[(a,b)]=E.get((a,b),0)+step
    return pack(q,E)
def F(vec,a,reverse=False):
    out=defaultdict(int)
    for key,amp in vec.items():
        for dv in dirs:
            v=move(key,a,add(a,dv),'in' if reverse else 'out')
            if v is not None:out[v]+=amp
    return {v:k for v,k in out.items() if k}
def J(vec,a,b,signs):
    out=defaultdict(int)
    for key,amp in vec.items():
        for sig in signs:
            v=move(key,a,b,'birth',sig)
            if v is not None:out[v]+=amp
    return {v:k for v,k in out.items() if k}
def B(vec,a,b,signs):return J(F(vec,a),a,b,signs)
def gauss(key):
    q,E=unpack(key);div=defaultdict(int)
    for (u,v),e in E.items():div[u]+=e;div[v]-=e
    sites=set(q)|set(div)
    return all(div[v]==charge(q,v)-(1 if parity(v)==0 else 0) for v in sites)
def gamma_basis(key):
    q,E=unpack(key);total=0
    for v,x in q.items():
        if parity(v)==0 and x==0:
            total+=2*sum(charge(q,add(v,dv))==0 for dv in dirs)
    return total

# Model representation reused from our frozen check_dark_cubic.py; this is an
# author continuation control, not an independent reconstruction.
c=(1,1,0);a=(1,0,1);h=(0,0,0);extra=(2,0,1);b0=(1,0,2)
key=Omega
source=[(c,(1,0,0),'out',1),(c,(0,1,0),'birth',1),(a,(0,0,1),'out',1),(a,extra,'birth',1),(h,(0,-1,0),'out',1),(h,(-1,0,0),'birth',1),(h,(0,0,-1),'out',1)]
for aa,bb,kind,sig in source:
    before=unpack(key)[1].get((aa,bb),0)
    key=move(key,aa,bb,kind,sig)
    assert key is not None and gauss(key)
    after=unpack(key)[1].get((aa,bb),0)
    assert {before,after} in ({0,1},{0,-1})
gamma=key
mid=move(gamma,a,b0,'out');beta=move(mid,a,extra,'in')
assert mid and beta and gauss(mid) and gauss(beta)
assert unpack(gamma)[1].get((a,b0),0)==0 and unpack(mid)[1][(a,b0)]==-1
assert unpack(mid)[1][(a,extra)]==1 and unpack(beta)[1].get((a,extra),0)==0
near={add(add(h,u),v) for u in dirs for v in dirs}-{h}
assert len(near)==18
def same_hole(key):
    out=defaultdict(int)
    for x,amp in F(F({key:1},h,True),h).items():out[x]+=amp
    for aa in near:
        for x,amp in F(F({key:1},aa),aa,True).items():out[x]-=amp
    return {x:v for x,v in out.items() if v}
Hg=same_hole(gamma);Hb=same_hole(beta)
assert Hg[beta]==Hb[gamma]==-1
assert all(gauss(x) for x in list(Hg)+list(Hb))
for state in (gamma,beta):
    q,E=unpack(state)
    assert gamma_basis(state)==0
    assert sum(parity(v)==0 and x==0 for v,x in q.items())==1
    assert sum(parity(v)==1 and x!=0 for v,x in q.items())==7
assert charge(unpack(gamma)[0],b0)==0 and charge(unpack(beta)[0],b0)==1
# Compensation gating is load bearing, not an adopted ungated model.
wrong=Hg.get(beta,0)+F(F({gamma:1},a),a,True).get(beta,0)
assert wrong==0
result={'scope':'Author exact sparse local-tilt discriminator, not independent checking or microscopic dynamics simulation.','source_builder_provenance':'Own previous original-record-microscopic-local-route/check_dark_cubic.py model representation, copied explicitly; source law unchanged.','gamma':{'charge_changes':gamma[0],'electric_fields':gamma[1]},'beta':{'charge_changes':beta[0],'electric_fields':beta[1]},'W':1,'N_B':7,'original_loss_at_both_endpoints':0,'H2_matrix_element_and_reverse':[-1,-1],'same_hole_output_sizes':[len(Hg),len(Hb)],'all_selected_spin_weights':'Exactly one for all integer S>=1; selected links traverse 0<->+/-1.','normalized_current_eigenvalues':'plus/minus 2*delta*sinh(theta/2)','mutation_ungated_compensation_matrix_element':wrong,'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'attempt_sha256':hashlib.sha256((here/'LOCAL_TILT_ATTEMPT.md').read_bytes()).hexdigest()}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'LOCAL_TILT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['original_loss_at_both_endpoints','H2_matrix_element_and_reverse','same_hole_output_sizes','cpu_seconds','peak_rss_bytes']},indent=2))
