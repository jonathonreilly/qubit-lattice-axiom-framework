#!/usr/bin/env python3
"""Actual rotor word control of sparse-dark rows; no earlier runner import."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import collections,datetime,hashlib,itertools,json,resource,time
from pathlib import Path
here=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert all(not(runtime/x).exists() for x in ('STOP_REQUESTED','STOP_REQUESTED.json'))
assert time.time()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
c0=time.process_time();w0=time.monotonic()
dirs=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
z=(0,0,0)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def parity(a):return sum(a)%2
def norm(a):return sum(map(abs,a))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def nb(a):return tuple(add(a,d) for d in dirs)
near=tuple(sorted({add(d,e) for d in dirs for e in dirs}-{z}))
star=set(nb(z));outer=tuple(sorted(p for p in itertools.product(range(-3,4),repeat=3) if norm(p)==3))
assert len(outer)==38 and len(near)==18
axis_centers=tuple(tuple(2*x for x in d) for d in dirs)
axis_outer=tuple(set(nb(c))-{d} for c,d in zip(axis_centers,dirs))
assert all(not(a&b) for a,b in itertools.combinations(axis_outer,2))
geom=collections.Counter()
for n in range(4):
    for extra in itertools.combinations(outer,n):
        occ=star|set(extra)
        clean=[i for i,s in enumerate(axis_outer) if not(s&occ)]
        assert len(clean)>=6-n
        assert all(not(set(nb(a))<=occ) for a in near)
        geom[n,len(clean)]+=1
assert sum(geom.values())==9178
# Exactly one occupied neighbor at selected c geometrically permits only
# the opposite axial dark center; every diagonal candidate needs a second.
sole_neighbor_tests=[]
for c,b in zip(axis_centers,dirs):
    candidates=[a for a in nb(b) if a!=c]
    assert z in candidates
    for a in candidates:
        overlap=set(nb(a))&set(nb(c))
        assert overlap=={b} if a==z else len(overlap)==2
    sole_neighbor_tests.append(len(candidates))

def base(v):return 1-parity(v)
def pack(q,E):return(tuple(sorted((v,a) for v,a in q.items() if a!=base(v))),tuple(sorted((e,a) for e,a in E.items() if a)))
def unpack(s):return dict(s[0]),dict(s[1])
def charge(q,v):return q.get(v,base(v))
def hop(s,a,b,reverse=False):
    q,E=unpack(s);qa,qb=charge(q,a),charge(q,b)
    if reverse:
        if qa or not qb:return None
        q[a],q[b],step=qb,0,qb
    else:
        if not qa or qb:return None
        q[a],q[b],step=0,qa,-qa
    E[a,b]=E.get((a,b),0)+step
    return pack(q,E)
def F(vec,a,reverse=False):
    out=collections.defaultdict(int)
    for s,n in vec.items():
        for b in nb(a):
            t=hop(s,a,b,reverse)
            if t is not None:out[t]+=n
    return {s:n for s,n in out.items() if n}
def addvec(out,v,scale=1):
    for s,n in v.items():out[s]+=scale*n

def info(s):
    q,_=unpack(s);holes=[v for v,a in q.items() if not parity(v) and a==0]
    assert len(holes)==1
    h=holes[0];occupied={v for v,a in q.items() if parity(v) and a}
    g=2*sum(b not in occupied for b in nb(h))
    n3=sum(norm(sub(b,h))<=3 for b in occupied)
    return h,occupied,g,n3

def H(s):
    h,_,_,_=info(s);v={s:1};out=collections.defaultdict(int)
    addvec(out,F(F(v,h,True),h))
    for off in near:
        a=add(h,off)
        # Actual occupied-A gate: Q_a=0 exactly for these eighteen centers.
        assert a!=h and norm(sub(a,h))==2
        addvec(out,F(F(v,a),a,True),-1)
        addvec(out,F(F(v,h,True),a))
        addvec(out,F(F(v,a),h,True),-1)
    return {t:n for t,n in out.items() if n}

def gauss(s):
    q,E=unpack(s);div=collections.defaultdict(int)
    for(a,b),m in E.items():div[a]+=m;div[b]-=m
    return all(div[v]==charge(q,v)-base(v) for v in set(q)|set(div))

def physical(S,minus_a=None):
    assert len(S)%2==1
    q={z:0}
    if minus_a is not None:q[minus_a]=-1
    nminus=(len(S)-1-2*(minus_a is not None))//2
    for i,b in enumerate(sorted(S)):q[b]=-1 if i<nminus else 1
    E=collections.defaultdict(int)
    for v,x in q.items():
        demand=x-base(v)
        if v==z:continue
        p=v
        for ax in range(3):
            while p[ax]:
                step=tuple((-1 if p[ax]>0 else 1) if j==ax else 0 for j in range(3))
                t=add(p,step)
                if parity(p):E[t,p]-=demand
                else:E[p,t]+=demand
                p=t
    ans=pack(q,E);assert gauss(ans)
    return ans

def select(s):
    h,S,g,n3=info(s);assert g==0 and n3<=9
    for d in dirs:
        c=add(h,tuple(2*x for x in d));b=add(h,d)
        if set(nb(c))&S=={b}:
            mid=hop(s,h,b,True);out=hop(mid,c,b)
            assert out is not None and info(out)[2]==10
            return out,d
    raise AssertionError('no clean axis')

far={p for p in itertools.product(range(8,13),range(-2,3),range(-2,3)) if parity(p)}
assert len(far)==62
extras=[(),((3,0,0),),((3,0,0),(0,3,0)),((3,0,0),(0,3,0),(0,0,3)),((2,1,0),(1,2,0),(1,1,1))]
controls=[];images=set()
for j,extra in enumerate(extras):
    occ=star|set(extra)|far
    if len(occ)%2==0:occ.add((17,0,0))
    st=physical(occ,(2,0,0) if j==4 else None)
    output,d=select(st);v=H(st);row=H(output)
    assert v.get(output)==1 and row.get(st)==1
    assert output not in images;images.add(output)
    dark=[(t,n) for t,n in row.items() if info(t)[2]==0]
    assert dark==[(st,1)] or dict(dark)=={st:1}
    assert all(gauss(t) for t in v) and all(gauss(t) for t in row)
    darkout=[t for t in v if info(t)[2]==0]
    assert all(info(t)[0]==z and info(t)[3]==6+len(extra) for t in darkout)
    # Distinct divergence-free internal circulation: same selection, different
    # exact charge/field output, and still a unique reverse dark input.
    q,E=unpack(st)
    a=z;b=(1,0,0);aa=(1,1,0);bb=(0,1,0)
    for edge,sign in (((a,b),1),((aa,b),-1),((aa,bb),1),((a,bb),-1)):
        E[edge]=E.get(edge,0)+4*sign
    shifted=pack(q,E);assert gauss(shifted)
    shiftedout,dd=select(shifted);rr=H(shiftedout)
    assert dd==d and shiftedout!=output
    assert {t:n for t,n in rr.items() if info(t)[2]==0}=={shifted:1}
    controls.append({'local_N3':6+len(extra),'global_NB':len(occ),'selected_direction':d,'original_H_words':len(v),'selected_reverse_words':len(row),'dark_H_words':len(darkout),'unique_original_dark_inverse':True,'field_loop_coherence_injective':True,'A_minus_case':j==4})
    del v,row,rr
# A literal negative same-hole word merges an initially disconnected occupied
# component. No static B mask/component is a conserved observable.
occ=star|{(2,1,0),(5,0,0),(15,0,0)}
st=physical(occ);a=(2,0,0);src=(2,1,0);dst=(3,0,0)
mid=hop(st,a,dst);merged=hop(mid,a,src,True)
assert merged is not None and H(st).get(merged)==-1
assert gauss(merged) and info(merged)[0]==z and info(merged)[2]==0 and info(merged)[3]==7

def component(S,start):
    seen={start};todo=[start]
    while todo:
        p=todo.pop()
        for q in S-seen:
            if norm(sub(p,q))==2:seen.add(q);todo.append(q)
    return seen
before=component(occ,(1,0,0));after=component(info(merged)[1],(1,0,0))
assert (5,0,0) not in before and (5,0,0) in after
result={'geometry_masks':sum(geom.values()),'clean_axes_distribution':{f'outer{n}_clean{c}':v for(n,c),v in sorted(geom.items())},'sole_neighbor_candidates_checked':sole_neighbor_tests,'actual_physical_controls':controls,'static_component_counterexample':{'original_coefficient':-1,'original_term':'-F_(2,0,0)* F_(2,0,0)','occupied_B_move':{'from':src,'to':dst},'component_before':len(before),'component_after':len(after),'local_N3_before_after':7,'hole_fixed_and_original_G_zero':True},'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-w0,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
assert result['cpu_seconds']<25 and result['peak_rss_bytes']<130*1024**2
(here/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
