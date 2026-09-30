#!/usr/bin/env python3
"""Exact source-word control; no dynamics simulation or Hilbert enumeration."""
import os,time,resource,signal,json,hashlib
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
START=time.monotonic(); CPU=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5)); signal.alarm(30)
HERE=Path(__file__).resolve().parent
GUARD=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
    deadline=json.loads((GUARD/'DEADLINE.json').read_text())['deadline_epoch']
    assert time.time()<deadline
    assert not any((GUARD/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'))
    assert all(os.environ.get(k)=='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'))
guard()
L=8
sites=[(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
A=[v for v in sites if sum(v)%2==0]; B=[v for v in sites if sum(v)%2]
def add(v,i,s):
    w=list(v);w[i]=(w[i]+s)%L;return tuple(w)
NB={v:[add(v,i,s) for i in range(3) for s in (-1,1)] for v in sites}
EDGES=[(a,b) for a in A for b in NB[a]]
N=len(A)
rows=[]
for S in (1,2,4,8):
    q={v:int(v in A) for v in sites}; E={e:0 for e in EDGES}
    C=S*(S+1); gauss_checks=0; min_weight=Fraction(1); steps=[]
    def check():
        global gauss_checks
        for v in sites:
            div=sum(E[(v,b)] for b in NB[v]) if v in A else -sum(E[(a,v)] for a in NB[v])
            assert div==q[v]-int(v in A),(S,v,div,q[v])
        assert max(abs(x) for x in E.values())<=S
        gauss_checks+=1
    def shift(a,b,d,kind):
        global min_weight
        e=E[(a,b)]; e2=e+d
        assert abs(e)<=S and abs(e2)<=S
        weight=1-Fraction(e*(e+d),C)
        assert weight>0
        min_weight=min(min_weight,weight); E[(a,b)]=e2
        steps.append({'kind':kind,'a':a,'b':b,'shift':d,'input_E':e,'weight_squared':str(weight)})
    def out(a,b):
        assert q[a] in (-1,1) and q[b]==0
        charge=q[a];q[a]=0;q[b]=charge;shift(a,b,-charge,'outward');check()
    def inward(b,a):
        assert q[b] in (-1,1) and q[a]==0
        charge=q[b];q[b]=0;q[a]=charge;shift(a,b,charge,'inward');check()
    def birth(a,b,sigma):
        assert q[a]==q[b]==0
        q[a]=sigma;q[b]=-sigma;shift(a,b,sigma,'original_birth');check()
    check()
    a,b,c,d=(0,0,0),(1,0,0),(1,1,0),(0,1,0)
    m=S-1
    for unused in range(m):
        out(a,b);out(c,d);inward(b,c);inward(d,a)
    for y in range(L):
        for z in range(L):
            p=1-((y+z)%2)
            for k in (0,2):
                b1=(p+2*k,y,z);b2=(p+2*k+2,y,z);center=(p+2*k+1,y,z)
                out(center,b1);birth(center,b2,1)
    assert all(q[v]!=0 for v in sites)
    assert sum(q.values())==N
    births=sum(x['kind']=='original_birth' for x in steps)
    assert births==N//2==128
    # Literal hard-core supports: all actual outward, inward and birth words vanish.
    out_count=sum(q[a]!=0 and q[b]==0 for a,b in EDGES)
    in_count=sum(q[a]==0 and q[b]!=0 for a,b in EDGES)
    birth_count=sum(q[a]==0 and q[b]==0 for a,b in EDGES)
    D_full=sum(e*(e-q[a]) for (a,b),e in E.items() if q[a]!=0 and q[b]==0)
    assert out_count==in_count==birth_count==D_full==0
    Q2=sum(e*e for e in E.values())
    assert Q2==N+4*m*m+2*m
    assert gauss_checks==257+4*m
    assert min_weight==Fraction(2,S+1)
    rows.append({'S':S,'m':m,'Q2':Q2,'expected_Q2':N+4*m*m+2*m,'births':births,
                 'gauss_checks':gauss_checks,'max_abs_E':max(abs(e) for e in E.values()),
                 'min_selected_spin_weight_squared':str(min_weight),'W':0,'D_full':D_full,
                 'nonzero_primitive_hop_or_birth_words':0,'H_action_zero':True,
                 'word_steps':steps,'final_nonzero_fields':[{'a':a,'b':b,'E':e} for (a,b),e in E.items() if e],
                 'final_negative_B':[v for v in B if q[v]==-1]})
increment_rows=[]
for S in (1,2,4,8):
    for e in range(-S,S+1):
        for sigma in (-1,1):
            e2=e+sigma
            if abs(e2)>S:continue
            w=1-Fraction(e*(e+sigma),S*(S+1))
            assert w>0
            increment=e2*e2-e*e
            assert increment==2*sigma*e2-1
            assert abs(increment)<=2*abs(e2)+1
            increment_rows.append({'S':S,'input_E':e,'sigma':sigma,'output_E':e2,'increment':increment,'weight_squared':str(w)})
guard()
cpu=time.process_time()-CPU; wall=time.monotonic()-START;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert cpu<5 and wall<30 and rss<100*1024*1024,(cpu,wall,rss)
result={'role':'exact physical word and original increment controls; no Omega probability or dynamics claim',
        'utc':datetime.now(timezone.utc).isoformat(),'budget':{'cpu_seconds':5,'wall_seconds':30,'rss_bytes':100*1024*1024,'rss_guard':'observed peak checked at return'},
        'actual':{'cpu_seconds':cpu,'wall_seconds':wall,'rss_bytes':rss},
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'expectations_sha256':hashlib.sha256((HERE/'CONTROL_EXPECTATIONS.md').read_bytes()).hexdigest(),
        'filled_rows':rows,'increment_rows':increment_rows,'gauss_checks':sum(r['gauss_checks'] for r in rows)}
(HERE/'FILLED_FLUX_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print('filled-source words:',len(rows),'Gauss checks:',result['gauss_checks'])
print('original increment rows:',len(increment_rows))
print('CPU',cpu,'wall',wall,'peak RSS bytes',rss)
print('TOTAL: PASS=3 FAIL=0')
