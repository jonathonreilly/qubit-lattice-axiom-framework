#!/usr/bin/env python3
"""Literal finite controls; no imported native builder or many-body matrix."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
import sys,time,resource,hashlib,json,itertools
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
START=time.monotonic(); CPU=time.process_time()
ROOT=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
DEADLINE=json.loads((ROOT/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
def guard():
    assert not (ROOT/'STOP_REQUESTED.json').exists(),'STOP_REQUESTED'
    assert time.time()<DEADLINE,'deadline'
    assert time.monotonic()-START<90,'wall'
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin': rss*=1024
    assert rss<150*1024**2,('RSS',rss)
def plus(x,y): return tuple(a+b for a,b in zip(x,y))
def minus(x,y): return tuple(a-b for a,b in zip(x,y))
UNIT=((1,0,0),(0,1,0),(0,0,1))
NEG=tuple(tuple(-a for a in e) for e in UNIT)
NEIGH=UNIT+NEG
AX=[tuple(sorted((e,tuple(-a for a in e)))) for e in UNIT]
# Each template is an unnormalized literal Q with its squared denominator.
TEMPLATES=[(list(zip(AX,(1,-1,0))),2,2),(list(zip(AX,(1,1,-2))),6,2)]
for i in range(3):
    for j in range(i+1,3):
        words=[]
        for s,t in itertools.product((-1,1),repeat=2):
            words.append((tuple(sorted((tuple(s*a for a in UNIT[i]),tuple(t*a for a in UNIT[j])))),s*t))
        TEMPLATES.append((words,4,1))
def shiftpair(pair,c): return tuple(sorted(plus(p,c) for p in pair))
def terms(c):
    for words,den,g in TEMPLATES:
        for (po,ao),(pi,ai) in itertools.product(words,repeat=2):
            if not ao*ai: continue
            val=F(ao*ai,den)
            out,inp=shiftpair(po,c),shiftpair(pi,c)
            yield out,inp,(-g*val,F(0))
            for e in UNIT:
                co=plus(c,e); oo,ii=shiftpair(po,co),shiftpair(pi,co)
                yield oo,ii,(F(0),val)
                yield out,inp,(F(0),val)
                yield oo,inp,(F(0),-val)
                yield out,ii,(F(0),-val)
def ops(out,inp):
    return tuple(sorted((p,'n' if p in out and p in inp else '+' if p in out else '-') for p in set(out)|set(inp)))
def accumulate(d,key,val):
    old=d.get(key,(F(0),F(0))); new=tuple(a+b for a,b in zip(old,val))
    if any(new): d[key]=new
    elif key in d: del d[key]
guard()
line={(j,0,0) for j in range(4)}
target=(((1,0,0),'+'),((2,0,0),'-'),((3,0,0),'+'))
reverse=tuple((p,'-' if s=='+' else '+') for p,s in target)
line_terms={}; boundary={}; boundary_dagger={}; enumerated=0
# Any term containing (3,0,0) has a base center within this radius-two cube.
for offset in itertools.product(range(-2,3),repeat=3):
    c=plus((3,0,0),offset)
    for out,inp,val in terms(c):
        enumerated+=1; op=ops(out,inp)
        if {p for p,s in op}==line: accumulate(line_terms,op,val)
        ext=tuple((p,s) for p,s in op if p[0]>0)
        inside=tuple((p,s) for p,s in op if p[0]<=0)
        if ext==target: accumulate(boundary,inside,val)
        if ext==reverse: accumulate(boundary_dagger,inside,val)
    guard()
expected_forward=(((0,0,0),'-'),((1,0,0),'+'),((2,0,0),'-'),((3,0,0),'+'))
expected_backward=tuple((p,'+' if s=='-' else '-') for p,s in expected_forward)
assert line_terms=={expected_forward:(F(0),F(-2,3)),expected_backward:(F(0),F(-2,3))},line_terms
assert boundary=={(((0,0,0),'-'),):(F(0),F(-2,3))},boundary
assert boundary_dagger=={(((0,0,0),'+'),):(F(0),F(-2,3))},boundary_dagger
def transpose(m): return tuple(zip(*m))
def matmul(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
rotations=[('original',((F(0),F(1)),(F(0),F(0))),F(1)),
           ('rational_3_5_4_5',((F(12,25),F(9,25)),(F(-16,25),F(-12,25))),F(9,25)),
           ('balanced',((F(1,2),F(1,2)),(F(-1,2),F(-1,2))),F(1,2))]
rotation_results=[]
for name,b,t in rotations:
    matrices={'-':b,'+':transpose(b),'n':matmul(transpose(b),b)}
    n=(1,0,1,0);m=(0,1,0,1); got=F(0)
    for op,(mu,tau) in line_terms.items():
        value=tau
        for p,s in op: value*=matrices[s][m[p[0]]][n[p[0]]]
        got+=value
    want=-F(2,3)*(t**4+(1-t)**4)
    assert got==want,(name,got,want)
    assert abs(got)>=F(1,12)
    rotation_results.append({'basis':name,'tau_coefficient':str(got)})
assert rotation_results[-1]['tau_coefficient']=='-1/12'
# Control: the witness comes from mobility, not from the density term.
assert all(mu==0 for mu,tau in line_terms.values())
assert all(mu+0*tau==0 for mu,tau in line_terms.values())
DISP=set()
for a,b in itertools.permutations(NEIGH,2): DISP.add(minus(a,b))
assert len(DISP)==18
def apply_pair(state,out,inp):
    if not set(inp)<=state: return None
    remaining=state-set(inp)
    if remaining&set(out): return None
    return frozenset(remaining|set(out))
def literal_H(state,mu=F(7),tau=F(5)):
    state=frozenset(state); answer=defaultdict(F)
    answer[state]+=mu*len(state)
    for x in state:
        m=sum(plus(x,d) in state for d in DISP)
        answer[state]+=mu*m*(m-1)/2
    # Every nonzero annihilation is centered one unit from an occupied site.
    pair_centers={plus(x,e) for x in state for e in NEIGH}
    bases=pair_centers|{minus(c,e) for c in pair_centers for e in UNIT}
    for c in bases:
        for out,inp,(am,at) in terms(c):
            new=apply_pair(state,out,inp)
            if new is not None: answer[new]+=mu*am+tau*at
    return {k:v for k,v in answer.items() if v}
independent_cases=[]
for points in [[],[(0,0,0)],[(0,0,0),(3,0,0)],[(0,0,0),(3,0,0),(0,3,0),(0,0,3)]]:
    st=frozenset(points); got=literal_H(st)
    want={} if not st else {st:F(7)*len(st)}
    assert got==want,(points,got)
    independent_cases.append({'particles':len(st),'eigenvalue':str(F(7)*len(st))})
    guard()
pair=frozenset({(0,0,0),(2,0,0)})
outside=literal_H(pair)
assert outside!={pair:F(14)}
# Native pair moves have a genuine output outside the original word.
assert any(k!=pair for k in outside)
guard()
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform!='darwin': rss*=1024
output={'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'templates':len(TEMPLATES),'streamed_terms':enumerated,
        'four_site_catalog':[{ 'operators':str(k),'mu':str(v[0]),'tau':str(v[1])} for k,v in line_terms.items()],
        'boundary_remaining':str(boundary),'boundary_dagger_remaining':str(boundary_dagger),
        'rotated_matrix_elements':rotation_results,'tau_zero_witness':0,
        'independent_set_controls':independent_cases,'graph_pair_output_words':len(outside),
        'cpu_seconds':time.process_time()-CPU,'wall_seconds':time.monotonic()-START,'peak_rss_bytes':rss,
        'threads':1,'failures':[],
        'scope':'Literal local coefficients and finite-state controls only. No computation of arbitrary-support commutants or general Lindblad compatibility.'}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
print('TOTAL: PASS=4 FAIL=0')
