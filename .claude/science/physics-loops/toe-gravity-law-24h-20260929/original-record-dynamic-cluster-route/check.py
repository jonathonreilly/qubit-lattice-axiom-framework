#!/usr/bin/env python3
"""Literal local source, regional charge, and exact series controls; no imported builder."""
import os
for key in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import datetime,hashlib,itertools,json,math,resource,time
from collections import defaultdict
from pathlib import Path
START=time.monotonic(); CPU=time.process_time()
ROOT=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
DEADLINE=json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
def guard():
    assert not (RUNTIME/'STOP_REQUESTED.json').exists(), 'STOP_REQUESTED'
    assert time.time()<DEADLINE, 'campaign deadline'
    assert time.monotonic()-START<30, 'wall price'
    assert time.process_time()-CPU<10, 'CPU price'
guard()
resource.setrlimit(resource.RLIMIT_CPU,(10,11))
# State is occupied A charge, six B charges, six oriented A->B link fields.
def F(state):
    qa,bs,es=state
    if qa==0:return []
    out=[]
    for edge in range(6):
        if bs[edge]:continue
        qb=list(bs); ee=list(es);qb[edge]=qa;ee[edge]-=qa
        out.append((0,tuple(qb),tuple(ee)))
    return out
def jump(state,edge,sign):
    qa,bs,es=state
    if qa or bs[edge]:return None
    qb=list(bs);ee=list(es);qb[edge]=-sign;ee[edge]+=sign
    return sign,tuple(qb),tuple(ee)
def source(state,edge,signs):
    out=defaultdict(int)
    for s1 in F(state):
        for sign in signs:
            s2=jump(s1,edge,sign)
            if s2 is None:continue
            for s3 in F(s2):out[s3]-=1
    return {s:c for s,c in out.items() if c}
def residual(state):
    qa,bs,es=state
    return (sum(es)-qa+1,)+tuple(-e-q for e,q in zip(es,bs))
def counts(state,other_negative_A=0):
    qa,bs,_=state
    nb=sum(q!=0 for q in bs)
    minus=(qa==-1)+sum(q==-1 for q in bs)+other_negative_A
    w=(qa==0)
    q=nb-2*minus-w
    return nb,minus,w,q,nb+abs(q)
columns=outputs=coherent_collisions=negative_A_columns=0
max_abs=0;vacuum_norms={}
for qa in (-1,1):
    for bs in itertools.product((-1,0,1),repeat=6):
        state=(qa,bs,(0,)*6)
        for kind in ('resolved','coherent'):
            specs=[(e,(s,)) for e in range(6) for s in (-1,1)] if kind=='resolved' else [(e,(-1,1)) for e in range(6)]
            nrm=0
            for edge,signs in specs:
                columns+=1;negative_A_columns+=(qa==-1)
                out=source(state,edge,signs)
                nrm+=sum(c*c for c in out.values())
                for final,c in out.items():
                    outputs+=1;max_abs=max(max_abs,abs(c));coherent_collisions+=(abs(c)>1)
                    assert residual(final)==residual(state)
                    for spectator_minus in (0,1,3,7):
                        before=counts(state,spectator_minus);after=counts(final,spectator_minus)
                        assert after[0]==before[0]+3
                        assert after[1]==before[1]+1
                        assert after[2]==before[2]+1
                        assert after[3]==before[3]
                        assert after[4]==before[4]+3
            if qa==1 and not any(bs):vacuum_norms[kind]=nrm
        guard()
assert vacuum_norms=={'resolved':360,'coherent':360}
# All number sectors permitted by <=r whole dissipator factors.
grading_cases=0;sharp_witness=[]
for r in range(21):
    for nb in range(2*r+1):
        for minus in range(r+1):
            cap=nb+abs(nb-2*minus)
            assert cap<=4*r
            for Kcap in range(3,84):
                r0=(Kcap-3)//4+1
                if r<r0: assert cap+3<=Kcap
                grading_cases+=1
    sharp_witness.append({'r':r,'nb':2*r,'minus_in_region':0,'cap':4*r})
series_identities=0
for q in range(1,15):
    for n in range(21):
        for r in range(n+1):
            assert math.comb(q+n-1,n)*math.comb(n,r)==math.comb(q+r-1,r)*math.comb(q+n-1,n-r)
            series_identities+=1
guard()
result={'status':'all asserted controls completed','scope':'Local ambient-star identities preserve Gauss residual; restriction to every physical completion follows. Only bare-Omega source fixture has zero residual in this isolated star. No full dynamic-response simulation.',
'columns':columns,'negative_A_columns':negative_A_columns,'output_coefficients':outputs,'colliding_path_coefficients':coherent_collisions,'max_abs_coefficient':max_abs,'vacuum_stack_norm_squared':vacuum_norms,
'grading_cases':grading_cases,'sharp_number_sector_witnesses':sharp_witness,'exact_binomial_identities':series_identities,
'cpu_seconds':time.process_time()-CPU,'wall_seconds':time.monotonic()-START,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='sharp_number_sector_witnesses'},indent=2))
