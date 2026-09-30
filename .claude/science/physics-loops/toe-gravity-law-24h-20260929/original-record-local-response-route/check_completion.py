#!/usr/bin/env python3
"""Integer Gauss completions preserving regional boundary-sector coherence."""
from pathlib import Path
import collections, datetime, hashlib, itertools, json, resource, time
P=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (RUNTIME/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0,c0=time.monotonic(),time.process_time()
L,R=32,3
dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def parity(x): return sum(x)%2
def nb(x): return [tuple((a+b)%L for a,b in zip(x,d)) for d in dirs]
def rad(x): return sum(min(t,L-t) for t in x)
sites=list(itertools.product(range(L),repeat=3))
D={x for x in sites if rad(x)<=R}; outside=set(sites)-D
boundary={x for x in D if any(y not in D for y in nb(x))}
def tree(vertices,root):
    parent={root:None}; queue=collections.deque([root])
    while queue:
        x=queue.popleft()
        for y in nb(x):
            if y in vertices and y not in parent: parent[y]=x; queue.append(y)
    assert len(parent)==len(vertices)
    return parent
inside_tree=tree(D,(3,0,0)); outside_tree=tree(outside,(16,0,0))
def addflow(e,x,y,v):
    edge=(x,y) if not parity(x) else (y,x)
    e[edge]=e.get(edge,0)+(v if not parity(x) else -v)
def route(e,x,parents,v):
    while parents[x] is not None:
        y=parents[x]; addflow(e,x,y,v); x=y
def div(e):
    d=collections.defaultdict(int)
    for (a,b),v in e.items(): d[a]+=v; d[b]-=v
    return d
def normalize(e): return {x:v for x,v in e.items() if v}
def defects(q,e):
    d=div(e)
    return {x:q.get(x,1-parity(x))-(1-parity(x))-d[x] for x in boundary}
chosen_B=sorted(x for x in D if parity(x))
ext_B=sorted(x for x in outside if x[0]==L//2 and parity(x))
cases=[([],0),([1],0),([-1],0),([1,1],0),([1,-1],0),([1,1,1],0),([1,1,-1],0),([1,1,1],1),([-1,-1,-1],0),([1,1,1,1,-1,-1,-1],0)]
records=[]
for signs,minusA in cases:
    q={(0,0,0):0}
    if minusA: q[(2,0,0)]=-1
    for x,v in zip(chosen_B,signs): q[x]=v
    e={}
    for x in D:
        delta=q.get(x,1-parity(x))-(1-parity(x))
        if delta: route(e,x,inside_tree,delta)
    # Large opposing boundary flux. This is not a zero-electric buffer.
    route(e,(0,3,0),inside_tree,100003)
    e=normalize(e)
    d=defects(q,e); Q=sum(d.values())
    assert Q==sum(q.get(x,1-parity(x))-(1-parity(x)) for x in D)
    assert all(div(e)[x]==q.get(x,1-parity(x))-(1-parity(x)) for x in D-boundary)
    K=len(signs)+abs(Q); assert K<=7 and L>=4*K
    eq=dict(e); qfull=dict(q); cross={}
    for x,value in d.items():
        if value:
            y=next(y for y in nb(x) if y in outside)
            addflow(eq,x,y,value); addflow(cross,x,y,value)
    for x in ext_B[:abs(Q)]: qfull[x]=-1 if Q>0 else 1
    dcross=div(cross)
    target={x:qfull.get(x,1-parity(x))-(1-parity(x))-dcross[x] for x in outside}
    assert sum(target.values())==0
    for x,value in target.items():
        if value: route(eq,x,outside_tree,value)
    eq=normalize(eq); divergence=div(eq)
    assert all(divergence[x]==qfull.get(x,1-parity(x))-(1-parity(x)) for x in sites)
    assert sum(parity(x) and v!=0 for x,v in qfull.items())==K
    assert K%2==1
    assert sum(not parity(x) and v==0 for x,v in qfull.items())==1
    assert {l:v for l,v in eq.items() if all(x in D for x in l)}==e
    # A second, orthogonal internal loop word has exactly the same d and
    # therefore precisely the same exterior completion, preserving coherence.
    e2=dict(e)
    loop=[(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,0)]
    for x,y in zip(loop,loop[1:]): addflow(e2,x,y,17)
    e2=normalize(e2)
    assert e2!=e and defects(q,e2)==d
    eq2={l:v for l,v in eq.items() if not all(x in D for x in l)}
    eq2.update(e2); div2=div(eq2)
    assert all(div2[x]==qfull.get(x,1-parity(x))-(1-parity(x)) for x in sites)
    ext1=tuple(sorted((l,v) for l,v in eq.items() if not all(x in D for x in l)))
    ext2=tuple(sorted((l,v) for l,v in eq2.items() if not all(x in D for x in l)))
    assert ext1==ext2
    records.append({'local_B':len(signs),'local_A_minus':minusA,'Q_D':Q,'reference_global_B':K,'nonzero_boundary_defects':sum(v!=0 for v in d.values()),'maximum_boundary_defect':max(map(abs,d.values())),'reference_nonzero_links':len(eq),'within_sector_offdiagonal_multiplier':1})
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'L':L,'R':R,'regional_sites':len(D),'connected_exterior_sites':len(outside_tree),'gauss_complete_words':2*len(cases),'cases':records,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(P/'COMPLETION_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
