import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key]='1'
import json,time,resource,signal,itertools,hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
DEADLINE=json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
start=time.monotonic(); cpu=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(30,30)); signal.alarm(40)
def guard():
    assert time.time()<DEADLINE, 'campaign deadline'
    assert not (RUNTIME/'STOP_REQUESTED.json').exists(), 'STOP requested'
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<150*1024**2, 'RSS cap'
guard()
e=[(1,0,0),(0,1,0),(0,0,1)]; z=(0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,k):return tuple(k*x for x in a)
def edge(a,b):return tuple(sorted((a,b)))
def row_shift(row,c):return {edge(add(a,c),add(b,c)):v for (a,b),v in row.items()}
d=[edge(scale(v,-1),v) for v in e]
q=[({d[0]:1,d[1]:-1},F(1,2),'E1'),({d[0]:1,d[1]:1,d[2]:-2},F(1,6),'E2')]
srows=[({x:1 for x in d},F(2,3))]
for i,j in itertools.combinations(range(3),2):
    v=[(edge(scale(e[i],s),scale(e[j],t)),s*t) for s,t in itertools.product([-1,1],repeat=2)]
    q.append((dict(v),F(1,4),f'T{i}{j}'))
    for (a,sa),(b,sb) in itertools.combinations(v,2):srows.append(({a:sa,b:-sb},F(1,4)))
refs=d+[edge(z,add(e[i],scale(e[j],s))) for i,j in itertools.combinations(range(3),2) for s in [-1,1]]
centers=list(itertools.product(range(-3,4),repeat=3))
rows=[]; originals=[]
for c in centers:
    for r,w in srows:rows.append((row_shift(r,c),w,'mu'))
    for r,w,name in q:
        rc=row_shift(r,c); originals.append((rc,-(2 if name.startswith('E') else 1)*w))
        for axis in e:
            rr=row_shift(r,add(c,axis))
            for b,v in rc.items():rr[b]=rr.get(b,0)-v
            rows.append((rr,w,'tau'))
outputs=[]
for idx,ref in enumerate(refs):
    guard(); km=defaultdict(F);kt=defaultdict(F); orig=defaultdict(F);orig[ref]=F(2)
    bound={'mu':F(0),'tau':F(0)}; max_delta=0
    for r,w,ch in rows:
        if ref not in r:continue
        bound[ch]+=w*abs(r[ref])*sum(map(abs,r.values()))
        k=km if ch=='mu' else kt
        for f,v in r.items():
            k[f]+=w*r[ref]*v
            max_delta=max(max_delta,abs(sum(p[0] for p in ref)-sum(p[0] for p in f)))
    for r,w in originals:
        if ref in r:
            for f,v in r.items():orig[f]+=w*r[ref]*v
    clean=lambda r:{k:v for k,v in r.items() if v}
    assert clean(km)==clean(orig)
    expected_mu=F(2 if idx<3 else 3)
    expected_tau=F([20,20,16][idx] if idx<3 else 24)
    assert bound=={'mu':expected_mu,'tau':expected_tau},(idx,bound)
    assert sum(map(abs,km.values()))<=expected_mu
    assert sum(map(abs,kt.values()))<=expected_tau
    assert max_delta<=6
    outputs.append({'orientation':idx,'mu_uncancelled':str(bound['mu']),'tau_uncancelled':str(bound['tau']),'mu_actual':str(sum(map(abs,km.values()))),'tau_actual':str(sum(map(abs,kt.values()))),'max_affine_x1_pair_difference':max_delta})
# Literal matrix L*L first, then independent pair-word double commutator.
fixtures=[('axial_S',srows[0]),('plane_difference_S',srows[1])]
for name in ['E1','T01']:
    r,w,_=next(x for x in q if x[2]==name)
    rr=row_shift(r,e[0])
    for b,v in r.items():rr[b]=rr.get(b,0)-v
    fixtures.append(('gradient_'+name,(rr,w)))
checks=[]
for name,(r,w) in fixtures:
    guard(); sites=sorted({x for ed in r for x in ed}); index={x:i for i,x in enumerate(sites)}
    words=[(sum(1<<index[x] for x in ed),v, sum((x[0]+2*x[1]-3*x[2]) for x in ed)) for ed,v in r.items()]
    diag=[sum((x[0]+2*x[1]-3*x[2]) for x,i in index.items() if (s>>i)&1) for s in range(1<<len(sites))]
    nonzero=0
    for s in range(1<<len(sites)):
        h=defaultdict(F)
        # Literal lowering output and its physical adjoint.
        low=defaultdict(F)
        for mask,v,_ in words:
            if s&mask==mask:low[s^mask]+=v
        for residual,amp in low.items():
            for mask,v,_ in words:
                if not residual&mask:h[residual|mask]+=w*v*amp
        direct={t:-(diag[t]-diag[s])**2*a for t,a in h.items()}
        current={t:(diag[s]-diag[t])*a for t,a in h.items()}
        rhs=defaultdict(F); crhs=defaultdict(F)
        for fm,fv,fw in words:
            if s&fm!=fm:continue
            residual=s^fm
            for em,ev,ew in words:
                if not residual&em:
                    t=residual|em
                    rhs[t]-=w*ev*fv*(ew-fw)**2
                    crhs[t]-=w*ev*fv*(ew-fw)
        assert clean(direct)==clean(rhs),(name,s)
        assert clean(current)==clean(crhs),(name,s,'current')
        nonzero+=len(clean(direct))
    checks.append({'fixture':name,'sites':len(sites),'basis_columns':1<<len(sites),'nonzero_double_commutator_entries':nonzero})
guard()
result={'status':'all assertions passed','edge_rows':outputs,'literal_controls':checks,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'wall_seconds':time.monotonic()-start,'cpu_seconds':time.process_time()-cpu,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'thread_limits':{k:os.environ[k] for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']},'deadline_epoch':DEADLINE}
(ROOT/'local_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
