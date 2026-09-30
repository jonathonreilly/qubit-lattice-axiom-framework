#!/usr/bin/env python3
"""Exact local no-event and original-mark prefix controls.

Uses the previously checked elementary charge/rotor conventions, implemented
here without importing or executing any older runner. All coefficients are
Gaussian integer pairs, not floating complex arithmetic. No dense carrier.
"""
from pathlib import Path
import collections, datetime, hashlib, itertools, json, resource, time
P=Path(__file__).resolve().parent
R=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (R/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((R/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0,c0=time.monotonic(),time.process_time()
directions=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
origin=(0,0,0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def parity(a): return sum(a)%2
def radius(a): return sum(abs(x) for x in a)
def neighbors(a): return [add(a,d) for d in directions]
other_A=sorted({add(x,y) for x in directions for y in directions}-{origin})
def pack(q,e): return (tuple(sorted((x,v) for x,v in q.items() if v!=1-parity(x))),tuple(sorted((x,v) for x,v in e.items() if v)))
def charge(q,x): return q.get(x,1-parity(x))
def move(st,a,b,adj=False):
    q,e=dict(st[0]),dict(st[1]); qa,qb=charge(q,a),charge(q,b)
    if (not adj and (qa==0 or qb!=0)) or (adj and (qa!=0 or qb==0)): return None
    s=qb if adj else qa
    q[a],q[b]=(s,0) if adj else (0,s)
    e[(a,b)]=e.get((a,b),0)+(s if adj else -s)
    return pack(q,e)
def birth(st,a,b,s):
    q,e=dict(st[0]),dict(st[1])
    if charge(q,a)!=0 or charge(q,b)!=0: return None
    q[a],q[b]=s,-s; e[(a,b)]=e.get((a,b),0)+s
    return pack(q,e)
def fa(v,a,adj=False):
    out=collections.defaultdict(int)
    for st,n in v.items():
        for b in neighbors(a):
            y=move(st,a,b,adj)
            if y is not None: out[y]+=n
    return {x:n for x,n in out.items() if n}
def hole(st):
    found=[x for x,v in st[0] if not parity(x) and v==0]
    assert len(found)==1; return found[0]
def loss(st):
    q=dict(st[0]); return 2*sum(charge(q,b)==0 for b in neighbors(hole(st)))
def H(st):
    h=hole(st); out=collections.defaultdict(int); v={st:1}
    def inc(v,c=1):
        for x,n in v.items(): out[x]+=c*n
    inc(fa(fa(v,h,True),h))
    for d in other_A:
        a=add(h,d)
        inc(fa(fa(v,a),a,True),-1)
        inc(fa(fa(v,h,True),a))
        inc(fa(fa(v,a),h,True),-1)
    return {x:n for x,n in out.items() if n}
def incpair(out,x,z):
    a,b=out.get(x,(0,0)); out[x]=(a+z[0],b+z[1])
def A(vec): # delta=kappa=1; -iH-G/2
    out={}
    for st,(re,im) in vec.items():
        for y,n in H(st).items(): incpair(out,y,(n*im,-n*re))
        d=loss(st)//2; incpair(out,st,(-d*re,-d*im))
    return {x:z for x,z in out.items() if z!=(0,0)}
def marks(vec,coherent):
    out={}
    for st,z in vec.items():
        a=hole(st)
        for b in neighbors(a):
            for s in (-1,1):
                y=birth(st,a,b,s)
                if y is not None:
                    label=(a,b) if coherent else (a,b,s)
                    incpair(out,(label,y),z)
    return {x:z for x,z in out.items() if z!=(0,0)}
def gauss(st):
    q,e=dict(st[0]),dict(st[1]); div=collections.defaultdict(int)
    for (a,b),v in e.items(): div[a]+=v; div[b]-=v
    return all(div[x]==charge(q,x)-(1-parity(x)) for x in set(div)|set(q))
def core(S):
    q={origin:0}; e=collections.defaultdict(int)
    for i,b in enumerate(sorted(S)):
        s=-1 if i<(len(S)-1)//2 else 1; q[b]=s; a=b
        for axis in range(3):
            while a[axis]:
                d=[0,0,0]; d[axis]=-1 if a[axis]>0 else 1
                z=add(a,d)
                if not parity(a): e[(a,z)]+=s
                else: e[(z,a)]-=s
                a=z
    st=pack(q,e); assert gauss(st); return st
def exterior(st):
    # Original + birth contribution j_(a,right,+) f_(a,left).
    a=(8,0,0); left=(7,0,0); right=(9,0,0)
    st=birth(move(st,a,left),a,right,1)
    q,e=dict(st[0]),dict(st[1])
    cycle=[(10,0,0),(11,0,0),(11,1,0),(10,1,0),(10,0,0)]
    for u,v in zip(cycle,cycle[1:]):
        edge=(u,v) if not parity(u) else (v,u)
        e[edge]=e.get(edge,0)+(19 if not parity(u) else -19)
    st=pack(q,e); assert gauss(st); return st
def strip(st):
    # Every possible changed near variable in the tested prefixes has x<7.
    return (tuple((x,v) for x,v in st[0] if x[0]<7),tuple((x,v) for x,v in st[1] if min(a[0] for a in x)<7))
def stripvec(v,marked=False):
    out={}
    for x,z in v.items():
        y=(x[0],strip(x[1])) if marked else strip(x)
        assert y not in out; out[y]=z
    return out
def norm2(v): return sum(a*a+b*b for a,b in v.values())

records=[]
for S,degree in [({(1,0,0)},2),(set(neighbors(origin))|{(1,1,1)},1)]:
    a=core(S); b=exterior(a); va={a:(1,0)}; vb={b:(1,0)}
    initial_radius=max([radius(x) for x,v in a[0]]+[radius(x) for edge,v in a[1] for x in edge])
    rows=[]
    for j in range(degree+1):
        assert stripvec(vb)==va
        max_hole=max(radius(hole(st)) for st in va)
        max_changed=max([radius(x) for st in va for x,v in st[0]]+[radius(x) for st in va for edge,v in st[1] for x in edge])
        assert max_hole<=2*j
        if j: assert max_changed<=initial_radius+2*j+1
        for st in list(va)+list(vb): assert gauss(st)
        jr=marks(va,False); jc=marks(va,True)
        assert stripvec(marks(vb,False),True)==jr
        assert stripvec(marks(vb,True),True)==jc
        weighted=sum(loss(st)*(z[0]*z[0]+z[1]*z[1]) for st,z in va.items())
        assert norm2(jr)==norm2(jc)==weighted
        rows.append({'degree':j,'near_words':len(va),'resolved_mark_words':len(jr),'coherent_mark_words':len(jc),'max_hole_distance':max_hole,'max_changed_cell_distance':max_changed,'Jnorm2_equals_Gform':weighted})
        if j<degree: va=A(va); vb=A(vb)
        assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<150*1024**2
    records.append({'core_k':len(S),'core_radius':initial_radius,'external_B':2,'external_cycle_flux':19,'exact_prefixes':rows})

# The B mask is not static, even at fixed hole center.
st=core({(1,0,0)})
reshuffled=move(move(st,origin,(1,0,0),True),origin,(0,1,0))
assert hole(reshuffled)==origin and H(st).get(reshuffled)==1
assert gauss(reshuffled)

# Local operator radius enumeration, independent of initial word sampling.
accessed=set(neighbors(origin))|{origin}
for a in other_A: accessed.add(a); accessed.update(neighbors(a))
assert max(map(radius,accessed))==3
assert max(map(radius,other_A))==2
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'prefix_comparisons':records,'actual_same_hole_B_reshuffle_coefficient':1,'local_access_radius':3,'maximum_hole_step':2,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(P/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
