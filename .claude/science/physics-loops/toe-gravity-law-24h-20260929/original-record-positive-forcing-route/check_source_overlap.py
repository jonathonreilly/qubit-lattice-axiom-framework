#!/usr/bin/env python3
"""Literal physical rotor source B=-F_a j F_a, no imported action builder."""
import collections
import datetime
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import time

HERE = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def guard():
    assert not (RUNTIME/'STOP_REQUESTED.json').exists(), 'STOP requested'
    assert time.time() < json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch'], 'deadline'

guard()
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
signal.alarm(60)
started_cpu, started_wall = time.process_time(), time.monotonic()
L = 8
a = (0, 0, 0)
c = (2, 2, 0)
neighbors = [(1,0,0),(7,0,0),(0,1,0),(0,7,0),(0,0,1),(0,0,7)]

def parity(x): return sum(x) % 2
def qref(x): return 1-parity(x)
def pack(q, e):
    return tuple(sorted((x,v) for x,v in q.items() if v != qref(x))), tuple(sorted((x,v) for x,v in e.items() if v))
def edge_delta(x, y, oriented_value):
    for d in range(3):
        if all(x[j] == y[j] for j in range(3) if j != d):
            if (x[d]+1) % L == y[d]: return (x,d), oriented_value
            if (y[d]+1) % L == x[d]: return (y,d), -oriented_value
    raise AssertionError('not nearest neighbors')
def shifted(state, updates, link_change):
    q, e = map(dict, state)
    q.update(updates)
    edge, de = link_change
    e[edge] = e.get(edge,0)+de
    return pack(q,e)
def qget(state,x): return dict(state[0]).get(x,qref(x))
def divergence(e):
    out = collections.Counter()
    for (x,d), value in e.items():
        y=list(x); y[d]=(y[d]+1)%L; y=tuple(y)
        out[x]+=value; out[y]-=value
    return {x:v for x,v in out.items() if v}
def gauss(state):
    required = {x:v-qref(x) for x,v in state[0]}
    assert divergence(dict(state[1])) == required
def F(state):
    qa=qget(state,a)
    if not qa: return []
    return [shifted(state,{a:0,b:qa},edge_delta(a,b,-qa))
            for b in neighbors if qget(state,b)==0]
def j(state, sign):
    b=neighbors[0]
    if qget(state,a) or qget(state,b): return []
    return [shifted(state,{a:sign,b:-sign},edge_delta(a,b,sign))]
def source(state, signs):
    answer=collections.Counter(); all_words=[state]; paths=[]
    for first in F(state):
        for sign in signs:
            for second in j(first,sign):
                for final in F(second):
                    answer[final]-=1
                    paths.append((state,first,second,final))
                    all_words.extend((first,second,final))
    for word in all_words: gauss(word)
    return dict(answer), paths, all_words

# Build one physical common output using a tree flow, then reverse exact source paths.
qgamma={a:0,c:-1,neighbors[0]:-1}
qgamma.update({neighbors[i]:1 for i in (1,2,3,4)})
charge={x:v-qref(x) for x,v in qgamma.items() if v!=qref(x)}
assert sum(charge.values())==0
egamma=collections.Counter()
for x,r in charge.items():
    if x==a: continue
    current=list(a)
    for d in range(3):
        while current[d]!=x[d]:
            old=tuple(current); current[d]+=1; nxt=tuple(current)
            edge,de=edge_delta(old,nxt,-r); egamma[edge]+=de
gamma=pack(qgamma,egamma); gauss(gamma)

def input_word(occupied, added):
    q={c:-1}; q.update({neighbors[i]:1 for i in occupied})
    e=dict(egamma)
    for i in added:
        edge,de=edge_delta(a,neighbors[i],-1); e[edge]=e.get(edge,0)-de
    edge,de=edge_delta(a,neighbors[0],1); e[edge]=e.get(edge,0)-de
    word=pack(q,e); gauss(word); return word

alpha=input_word((1,2),(3,4))
beta=input_word((1,3),(2,4))
assert alpha!=beta
rows={}
all_paths=[]
for name, signs in [('resolved_plus',(1,)), ('coherent_edge',(1,-1))]:
    aa,pa,wa=source(alpha,signs); bb,pb,wb=source(beta,signs)
    common=set(aa)&set(bb)
    overlap=sum(aa[x]*bb[x] for x in common)
    assert aa[gamma]==bb[gamma]==-2
    assert overlap>=4
    rows[name]={'alpha_output_words':len(aa),'beta_output_words':len(bb),
                'common_output_words':len(common),'exact_rotor_overlap':overlap,
                'gamma_amplitudes':[aa[gamma],bb[gamma]],
                'path_counts':[len(pa),len(pb)],
                'gauss_words_checked':len(wa)+len(wb)}
    all_paths += pa+pb

# Every literal spin path remains legal at this finite S, with strictly positive weights.
maxfield=max(abs(v) for path in all_paths for word in path for _,v in word[1])
spin=maxfield+2; casimir=spin*(spin+1)
min_numerator=casimir
for path in all_paths:
    for old,new in zip(path,path[1:]):
        oe,ne=dict(old[1]),dict(new[1])
        changed=[edge for edge in oe.keys()|ne.keys() if oe.get(edge,0)!=ne.get(edge,0)]
        assert len(changed)==1
        edge=changed[0]; m=oe.get(edge,0); de=ne.get(edge,0)-m
        assert abs(de)==1
        numerator=casimir-m*(m+de)
        assert numerator>0
        min_numerator=min(min_numerator,numerator)
guard()
elapsed=time.process_time()-started_cpu
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
# macOS ru_maxrss is bytes.
assert rss <100*1024*1024
result={'status':'completed literal source control; no probabilistic preparation claim',
        'L':L,'fixture':{'a':a,'other_negative_A':c,'neighbor_order':neighbors,
                       'alpha':alpha,'beta':beta,'common_output':gamma},
        'instruments':rows,'finite_spin_positive_path_check':{
            'S':spin,'max_abs_field':maxfield,'minimum_squared_edge_weight':[min_numerator,casimir]},
        'cpu_seconds':elapsed,'wall_seconds':time.monotonic()-started_wall,
        'peak_rss_bytes':rss,'threads':{key:os.environ.get(key) for key in
            ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
        'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(HERE/'SOURCE_OVERLAP_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='fixture'},indent=2))
