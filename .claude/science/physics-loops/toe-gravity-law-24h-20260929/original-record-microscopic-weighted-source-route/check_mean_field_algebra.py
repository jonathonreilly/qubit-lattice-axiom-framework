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



# These physical word primitives are copied from our frozen earlier runner.
# The following control is new and retains ORIGINAL labels throughout.
def clean(v):return {k:a for k,a in v.items() if a}
def plus(*terms):
    r=defaultdict(int)
    for coeff,v in terms:
        for k,a in v.items():r[k]+=coeff*a
    return clean(r)
def step_op(v,aa,reverse=False,spin=False):
    r=defaultdict(int)
    for key,amp in v.items():
        for dv in dirs:
            nxt=move(key,aa,add(aa,dv),'in' if reverse else 'out')
            if nxt is not None and (not spin or all(abs(x)<=1 for x in unpack(nxt)[1].values())):r[nxt]+=amp
    return clean(r)
def birth_op(v,aa,bb,signs,spin=False):
    r=defaultdict(int)
    for key,amp in v.items():
        for sig in signs:
            nxt=move(key,aa,bb,'birth',sig)
            if nxt is not None and (not spin or all(abs(x)<=1 for x in unpack(nxt)[1].values())):r[nxt]+=amp
    return clean(r)
def near(aa):return {add(add(aa,u),v) for u in dirs for v in dirs}-{aa}
def fall(v,centers,reverse=False,spin=False):return plus(*[(1,step_op(v,x,reverse,spin))for x in centers])
def absfield(key):return sum(abs(x) for x in unpack(key)[1].values())
def holes(key):return [x for x,q in key[0] if parity(x)==0 and q==0]
def norm2(v):return sum(a*a for a in v.values())
def inner(v,w):return sum(a*w.get(k,0) for k,a in v.items())
def literal_h2(key,centers,spin):
    # The omitted electric compensation is diagonal and has zero V_E current.
    q,_=unpack(key);C=defaultdict(int)
    for aa in centers:
        gate=all(charge(q,c)!=0 for c in near(aa))
        if gate:
            for k,v in step_op(step_op({key:1},aa,False,spin),aa,True,spin).items():C[k]+=v
    ff=fall(fall({key:1},centers,True,spin),centers,False,spin)
    ff2=fall(fall({key:1},centers,False,spin),centers,True,spin)
    return plus((1,clean(C)),(1,ff),(-1,ff2))
def reduced_h2(key,spin):
    hh=holes(key);assert len(hh)==1;h=hh[0];cs=near(h)
    terms=[(1,step_op(step_op({key:1},h,True,spin),h,False,spin))]
    for aa in cs:
        terms.extend([(-1,step_op(step_op({key:1},aa,False,spin),aa,True,spin)),
         (1,step_op(step_op({key:1},h,True,spin),aa,False,spin)),
         (-1,step_op(step_op({key:1},aa,False,spin),h,True,spin))])
    return plus(*terms)
h=(0,0,0);aloop=(1,0,1);c2=(1,1,2);b0=(1,0,2);dd=(1,1,1)
seed=pack({}, {(aloop,b0):1,(aloop,dd):-1,(c2,b0):-1,(c2,dd):1})
one=move(Omega,h,(1,0,0),'out');ordinary=move(one,h,(0,1,0),'birth',1)
old_result=json.loads((here/'WEIGHTED_CURRENT_RESULTS.json').read_text())
def from_old(v):return pack({tuple(x):q for x,q in v['charges']},{(tuple(a),tuple(b)):e for a,b,e in v['fields']})
gamma=from_old(old_result['gamma']);beta=from_old(old_result['beta'])
seed_births={}
for dv in dirs:
    for signs in [(1,),(-1,),(-1,1)]:seed_births.update(birth_op(step_op({seed:1},aloop),aloop,add(aloop,dv),signs))
loopbirth=next(iter(seed_births));inputs=[Omega,seed,one,ordinary,loopbirth,gamma,beta]
assert all(gauss(k) for k in inputs+list(seed_births))
comm_cases=block_cases=0;boundary_differences=[]
for spin in [False,True]:
 for aa in [h,aloop]:
  centers=near(aa)|{aa,add(aa,(6,0,0))}
  for key in inputs:
   for dv in dirs:
    for signs in [(1,),(-1,),(-1,1)]:
     bb=add(aa,dv);v={key:1}
     b=birth_op(step_op(v,aa,False,spin),aa,bb,signs,spin)
     d=step_op(birth_op(v,aa,bb,signs,spin),aa,False,spin)
     full=plus((1,birth_op(fall(v,centers,False,spin),aa,bb,signs,spin)),(-1,fall(birth_op(v,aa,bb,signs,spin),centers,False,spin)))
     assert full==plus((1,b),(-1,d));comm_cases+=1
     assert not inner(b,d)
     assert all(charge(unpack(k)[0],aa)!=0 for k in b)
     assert all(charge(unpack(k)[0],aa)==0 for k in d)
     assert all(gauss(k) for k in full);block_cases+=1
for dv in dirs:
 for signs in [(1,),(-1,),(-1,1)]:
  bb=add(aloop,dv)
  r=birth_op(step_op({seed:1},aloop),aloop,bb,signs)
  s=birth_op(step_op({seed:1},aloop,False,True),aloop,bb,signs,True)
  if norm2(r)!=norm2(s):boundary_differences.append({'direction':dv,'original_signs':signs,'rotor_norm2':norm2(r),'spin1_norm2':norm2(s)})
assert boundary_differences
rows=[]
for spin in [False,True]:
 for key in [one,gamma,beta]:
  hh=holes(key)[0];literal=literal_h2(key,near(hh)|{hh},spin);reduced=reduced_h2(key,spin)
  assert literal==reduced
  assert all(gauss(k) for k in literal)
  row=sum(abs(v)*abs(absfield(k)-absfield(key)) for k,v in literal.items())
  assert row<=1512
  assert all(abs(absfield(k)-absfield(key))<=2 for k in literal)
  rows.append({'spin1':spin,'input_fields':absfield(key),'support':len(literal),'absolute_current_row':row})
for spin in [False,True]:
 for key in [Omega,ordinary,loopbirth]:
  assert not literal_h2(key,near(h)|near(aloop)|{h,aloop},spin)
# Actual failure control: omitting compensation leaves a nonzero W0 field current.
uncancelled=[]
for key in list(seed_births):
 for aa in [h,aloop,c2]:
  v=step_op(step_op({key:1},aa),aa,True)
  r=sum(abs(vv)*abs(absfield(k)-absfield(key))for k,vv in v.items())
  if r:uncancelled.append({'center':aa,'row':r,'input_fields':absfield(key)})
assert uncancelled
# Direct occupied/hole coherent input, without measuring the A occupancy.
for signs in [(1,),(-1,),(-1,1)]:
 v={Omega:1,one:1};bb=(0,1,0)
 b=birth_op(step_op(v,h),h,bb,signs);d=step_op(birth_op(v,h,bb,signs),h)
 assert inner(b,d)==0 and norm2(plus((1,b),(-1,d)))==norm2(b)+norm2(d)
result={'scope':'author exact sparse original mean-block/current corroboration; no trajectory, asymptotic calibration or independent review',
 'implementation_exposure':'physical word prefix copied from own frozen check_weighted_current.py; new full neighboring commutators and literal/reduced D2 assembly',
 'copied_runner_sha256':hashlib.sha256((here/'check_weighted_current.py').read_bytes()).hexdigest(),
 'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'neighbor_commutator_cases':comm_cases,'occupancy_block_cases':block_cases,
 'boundary_differences':boundary_differences,'full_D2_rows':rows,
 'W0_compensation_cases':6,'omit_compensation_nonzero_controls':uncancelled[:6],
 'cpu_seconds':time.process_time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['cpu_seconds']<30 and result['peak_rss_bytes']<150*1024**2
(here/'MEAN_FIELD_ALGEBRA_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k]for k in ['neighbor_commutator_cases','occupancy_block_cases','full_D2_rows','cpu_seconds','peak_rss_bytes']},indent=2))
print('TOTAL: PASS=7 FAIL=0')
