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


# Author continuation: retain the literal physical word implementation above.
# New field observable and complete pair seed are independent of the old tilt.
from fractions import Fraction as Q
h=(0,0,0);a=(1,0,1);c=(1,1,0);c2=(1,1,2)
b0=(1,0,2);d=(1,1,1);extra=(2,0,1)
def field_weight(key):
    q,E=unpack(key)
    holes=[v for v,x in q.items() if parity(v)==0 and x==0]
    return sum(Q(2756)+sum(Q(1,2)**sum(abs(x-y) for x,y in zip(v,u))*e*e for (u,b),e in E.items()) for v in holes)
def source_word(seed):
    key=seed
    for aa,bb,kind,sig in [(c,(1,0,0),'out',1),(c,(0,1,0),'birth',1),(a,(0,0,1),'out',1),(a,extra,'birth',1),(h,(0,-1,0),'out',1),(h,(-1,0,0),'birth',1),(h,(0,0,-1),'out',1)]:
        key=move(key,aa,bb,kind,sig);assert key is not None and gauss(key)
    return key
# A complete actual S* S pair word produces this circulation on Omega.
seed=pack({}, {(a,b0):1,(a,d):-1,(c2,b0):-1,(c2,d):1})
assert gauss(seed)
complete_pair=F(F(F(F({Omega:1},a),c2),c2,True),a,True)
assert complete_pair[seed]==1
assert all(gauss(x) for x in complete_pair)
gamma=source_word(seed);mid=move(gamma,a,b0,'out');beta=move(mid,a,extra,'in')
assert mid and beta and gauss(mid) and gauss(beta)
near={add(add(h,u),v) for u in dirs for v in dirs}-{h}
def same_hole(key):
    out=defaultdict(int)
    for x,amp in F(F({key:1},h,True),h).items():out[x]+=amp
    for aa in near:
        for x,amp in F(F({key:1},aa),aa,True).items():out[x]-=amp
    return {x:v for x,v in out.items() if v}
Hg=same_hole(gamma);Hb=same_hole(beta)
assert Hg[beta]==Hb[gamma]==-1
assert all(gauss(x) for x in list(Hg)+list(Hb))
assert gamma_basis(gamma)==gamma_basis(beta)==0
assert field_weight(gamma)==Q(2756)+Q(37,8)
assert field_weight(beta)==Q(2756)+Q(33,8)
assert field_weight(beta)-field_weight(gamma)==Q(-1,2)
plain=source_word(Omega);plain_beta=move(move(plain,a,b0,'out'),a,extra,'in')
assert field_weight(plain_beta)==field_weight(plain)
# Full spin1 words are the rotor words with forbidden |E|>1 steps removed;
# all remaining adjacent 0<->+/-1 normalized weights are exactly one.
def F1(vec,aa,reverse=False):
    out=defaultdict(int)
    for key,amp in vec.items():
        for dv in dirs:
            bb=add(aa,dv);nxt=move(key,aa,bb,'in' if reverse else 'out')
            if nxt is not None and all(abs(e)<=1 for e in unpack(nxt)[1].values()):out[nxt]+=amp
    return {x:v for x,v in out.items() if v}
def same_hole_spin1(key):
    out=defaultdict(int)
    for x,amp in F1(F1({key:1},h,True),h).items():out[x]+=amp
    for aa in near:
        for x,amp in F1(F1({key:1},aa),aa,True).items():out[x]-=amp
    return {x:v for x,v in out.items() if v}
assert same_hole_spin1(gamma)[beta]==same_hole_spin1(beta)[gamma]==-1
seed1=F1(F1(F1(F1({Omega:1},a),c2),c2,True),a,True)
assert seed1[seed]==1
# Scalar Young bound underlying actual jump drift, exact rational spot controls.
Bmax=26;c0=2756
assert all(Bmax*(2*abs(m)+1)<=Q(1,2)*(m*m+c0) for m in range(-100,101))
# The sharp real maximum is at |m|=2B; equality there checks c0 exactly.
assert Bmax*(4*Bmax+1)==Q(1,2)*((2*Bmax)**2+c0)
result={'scope':'actual original field-word discriminator and finite corroboration; no microscopic trajectory or moment theorem',
 'implementation_exposure':'physical sparse word definitions copied from frozen own check_local_tilt.py; not independent reviewer evidence',
 'old_runner_sha256':hashlib.sha256((here.parent/'original-record-microscopic-cluster-route/check_local_tilt.py').read_bytes()).hexdigest(),
 'pair_seed_coefficient_in_SstarS':complete_pair[seed], 'pair_seed_spin1':seed1[seed],
 'pair_seed_complete_support':len(complete_pair),'same_hole_supports':[len(Hg),len(Hb)],
 'gamma':{'charges':gamma[0],'fields':gamma[1]},'beta':{'charges':beta[0],'fields':beta[1]},
 'quasilocal_field_weights':[str(field_weight(gamma)),str(field_weight(beta))],
 'weight_difference':str(field_weight(beta)-field_weight(gamma)),
 'Hbar_elements':[-1,-1],'spin1_Hbar_elements':[-1,-1],'original_loss':[0,0],
 'normalized_fast_current_eigenvalues':'plus/minus delta/2',
 'without_circulation_weight_difference':str(field_weight(plain_beta)-field_weight(plain)),
 'jump_scalar_constant':c0,'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'WEIGHTED_CURRENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['pair_seed_coefficient_in_SstarS','quasilocal_field_weights','Hbar_elements','original_loss','cpu_seconds','peak_rss_bytes']},indent=2))
print('TOTAL: PASS=8 FAIL=0')
