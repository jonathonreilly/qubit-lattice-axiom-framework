#!/usr/bin/env python3
"""Literal exact small control; no imported campaign or author assembly."""
import os,sys,time,resource,json,hashlib,itertools
from pathlib import Path
from fractions import Fraction
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
import signal
signal.alarm(15)
t0=time.monotonic(); cpu0=time.process_time()
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
deadline=json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
assert time.time()<deadline and not (runtime/'STOP_REQUESTED.json').exists()
assert all(os.environ.get(x)=='1' for x in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'])
L=5
basis=[tuple(int(i==j) for i in range(3)) for j in range(3)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
scale=lambda c,a:tuple(c*x for x in a)
sub=lambda a,b:add(a,scale(-1,b))
planes=list(itertools.combinations(range(3),2))
dirs=[scale(2,e) for e in basis]+[add(basis[i],scale(s,basis[j])) for i,j in planes for s in (1,-1)]
sites=set(itertools.product(range(L),repeat=3))
def orient(a,b):
    d=sub(b,a)
    if d in dirs:return dirs.index(d),a
    return dirs.index(scale(-1,d)),b
edges={(d,x):(x,add(x,v)) for d,v in enumerate(dirs) for x in sites if add(x,v) in sites}
for d in range(9):
    anchors={x for e,x in edges if e==d}
    seen={next(iter(anchors))}; todo=list(seen)
    while todo:
        x=todo.pop()
        for e in basis:
            for sign in (-1,1):
                y=add(x,scale(sign,e))
                if y in anchors and y not in seen:seen.add(y);todo.append(y)
    assert seen==anchors

def reduced(terms):
    row=[0]*9
    for c,a,b in terms:
        d,x=orient(a,b);assert (d,x) in edges;row[d]+=c
    return tuple(row)
rows=set(); actual_rows=0
for x in sites:
    axial=[(1,add(x,e),sub(x,e)) for e in basis]
    if all(a in sites and b in sites for c,a,b in axial):rows.add(reduced(axial));actual_rows+=1
    for i,j in planes:
        v=[(s*t,add(x,scale(s,basis[i])),add(x,scale(t,basis[j]))) for s,t in itertools.product((-1,1),repeat=2)]
        if all(a in sites and b in sites for c,a,b in v):
            for a,b in itertools.combinations(v,2):
                rows.add(reduced([a,(-b[0],b[1],b[2])]))
                actual_rows+=1

def rank(vectors):
    mat=[[Fraction(v) for v in row] for row in vectors];r=0
    for col in range(9):
        pivot=next((i for i in range(r,len(mat)) if mat[i][col]),None)
        if pivot is None:continue
        mat[r],mat[pivot]=mat[pivot],mat[r]
        c=mat[r][col];mat[r]=[v/c for v in mat[r]]
        for i in range(len(mat)):
            if i!=r and mat[i][col]:
                c=mat[i][col];mat[i]=[a-c*b for a,b in zip(mat[i],mat[r])]
        r+=1
    return r
assert rank(rows)==4
soft=[(1,-1,0,0,0,0,0,0,0),(1,1,-2,0,0,0,0,0,0)]
for j in (3,5,7):
    v=[0]*9;v[j]=-1;v[j+1]=1;soft.append(tuple(v))
assert all(sum(a*b for a,b in zip(row,v))==0 for row in rows for v in soft)
pin_hist={}; minimum_rank=9; corners=[]
for y in sorted(sites):
    pins={d for (d,x),(a,b) in edges.items() if y in (a,b)}
    unit=[tuple(int(i==d) for i in range(9)) for d in sorted(pins)]
    actual_rank=rank(list(rows)+unit);minimum_rank=min(minimum_rank,actual_rank)
    assert actual_rank==9
    pin_hist[len(pins)]=pin_hist.get(len(pins),0)+1
    if all(c in (0,L-1) for c in y):corners.append({'y':y,'types':sorted(pins),'rank':actual_rank})
G=set(dirs)|{scale(-1,d) for d in dirs}
boundary={x for x in sites if any(add(x,d) not in sites for d in G)}
assert len(boundary)==L**3-(L-4)**3
assert all(len([x for d,x in edges if d==j])==((L-2)*L*L if j<3 else (L-1)**2*L) for j in range(9))
result={'status':'all exact assertions passed','scope':'literal finite fixture only; general pinned-kernel proof remains analytic','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'L':L,'physical_vertices':len(sites),'forward_edges':len(edges),'actual_complete_S_rows':actual_rows,'distinct_constant_S_rows':len(rows),'constant_S_rank':4,'soft_dimension':5,'site_pin_cases':len(sites),'minimum_total_rank':minimum_rank,'pin_type_count_histogram':pin_hist,'corners':corners,'boundary_sites':len(boundary),'cpu_seconds':time.process_time()-cpu0,'wall_seconds':time.monotonic()-t0,'rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
assert result['rss_bytes']<=60*1024**2
print(json.dumps(result,indent=2))
