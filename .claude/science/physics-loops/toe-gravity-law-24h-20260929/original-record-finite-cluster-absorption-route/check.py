#!/usr/bin/env python3
"""Independent exact finite-cluster height and periodic-fiber controls.

No imported model builder; integers only. The proof, not these samples, covers
arbitrary configurations. Resource price: <=30 CPU s, expected <150 MB, BLAS1.
"""
import collections, datetime, hashlib, itertools, json, os, resource, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNTIME = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (RUNTIME/'STOP_REQUESTED.json').exists()
assert time.time() < json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
t0, c0 = time.monotonic(), time.process_time()
dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
zero=(0,0,0)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def parity(a): return sum(a)%2
def nb(a): return [add(a,d) for d in dirs]
near=sorted({add(d,e) for d in dirs for e in dirs}-{zero})
assert len(near)==18
def chi(x): return max(-5,min(5,x))
def phi(h,S): return sum(chi(h[0]-b[0]) for b in S)
def clean(v): return {s:n for s,n in v.items() if n}
def accumulate(out,v,f=1):
    for s,n in v.items(): out[s]+=f*n

# Exact infinite-lattice charges and A->B integer electric fields.
def pack(q,e): return (tuple(sorted((s,v) for s,v in q.items() if v != (1-parity(s)))), tuple(sorted((l,v) for l,v in e.items() if v)))
def unpack(st): return dict(st[0]),dict(st[1])
def charge(q,s): return q.get(s,1-parity(s))
def hop(st,a,b,dag=False):
    q,e=unpack(st); qa,qb=charge(q,a),charge(q,b)
    if (not dag and (qa==0 or qb!=0)) or (dag and (qa!=0 or qb==0)): return None
    value=qb if dag else qa
    q[a],q[b]=(value,0) if dag else (0,value)
    e[(a,b)]=e.get((a,b),0)+(value if dag else -value)
    return pack(q,e)
def local(v,a,dag=False):
    out=collections.defaultdict(int)
    for s,n in v.items():
        for b in nb(a):
            z=hop(s,a,b,dag)
            if z is not None: out[z]+=n
    return clean(out)
def occupation(st):
    q=dict(st[0]); holes=[s for s,v in q.items() if parity(s)==0 and v==0]
    assert len(holes)==1
    return holes[0],{s for s,v in q.items() if parity(s)==1 and v!=0}
def loss(st):
    h,S=occupation(st); return 2*sum(b not in S for b in nb(h))
def H(st):
    h,S=occupation(st); v={st:1}; out=collections.defaultdict(int)
    accumulate(out,local(local(v,h,True),h))
    for d in near:
        a=add(h,d)
        accumulate(out,local(local(v,a),a,True),-1)
        accumulate(out,local(local(v,h,True),a))
        accumulate(out,local(local(v,a),h,True),-1)
    return clean(out)
def gauss(st):
    q,e=unpack(st); divergence=collections.defaultdict(int)
    for (a,b),v in e.items(): divergence[a]+=v; divergence[b]-=v
    return all(divergence[s] == charge(q,s)-(1-parity(s)) for s in set(q)|set(divergence))
def physical(S):
    assert len(S)%2==1 and set(nb(zero))<=S
    q={zero:0}; e=collections.defaultdict(int)
    for i,b in enumerate(sorted(S)):
        s=-1 if i<(len(S)-1)//2 else 1
        q[b]=s; a=b
        for axis in range(3):
            while a[axis]:
                step=[0,0,0]; step[axis]=-1 if a[axis]>0 else 1
                c=add(a,step)
                if parity(a)==0: e[(a,c)]+=s
                else: e[(c,a)]-=s
                a=c
    ans=pack(q,e); assert gauss(ans); return ans

# Analytic local geometry, with breakpoint corroboration.
c=(2,0,0); other=[add(c,d) for d in near if add(c,d)!=zero]
assert sorted(set(x[0] for x in other))==[1,2,3,4]
star=set(nb(zero))
star_rises={d:phi((d,0,0),star)-phi(zero,star) for d in range(1,5)}
assert star_rises=={1:6,2:12,3:18,4:24}
assert all(chi(x+d)>=chi(x) for x in range(-20,21) for d in range(1,5))
assert all(abs(chi(x+d)-chi(x))<=2 for x in range(-20,21) for d in range(-2,3))
geometry={'other_hole_centers':other,'star_rises':star_rises}

# Preserve two failed naive extensions, without mislabeling either as darkness.
S={p for p in itertools.product(range(-3,4),repeat=3) if sum(map(abs,p)) in (1,3)}
S-= {tuple(3*v for v in d) for d in dirs}
S-= {p for p in itertools.product((-1,1),repeat=3) if p[0]*p[1]*p[2]==1}
assert len(S)==34
shield_counts=[len(set(nb(a))&S) for a in near]
assert set(shield_counts)=={5}
shield=S|{(15,0,0)}
L=8
def torusphi(h,S): return sum(chi((h[0]-b[0]+L//2)%L-L//2) for b in S)
badstar={tuple(x%L for x in b) for b in star}
badmask=badstar|{(5,0,0),(5,1,1),(5,2,0)}
badheight=[torusphi(zero,badmask),torusphi(c,badmask)]
assert badheight==[9,3]

mask7=star|{(7,0,0)}
mask11=star|set(nb((2,0,0))) # union has 11 for axial stars
assert len(mask11)==11
mask45={p for p in itertools.product(range(-3,4),repeat=3) if sum(map(abs,p)) in (1,3)}|{(15,0,0)}
masks=[mask7,mask11,shield,mask45]
reverse_results=[]
for S in masks:
    st=physical(S); b=(1,0,0)
    selected=hop(hop(st,zero,b,True),c,b)
    assert selected is not None and H(st).get(selected)==1
    row=H(selected)
    assert row.get(st)==1
    base=phi(zero,S); rises=[]; counts=collections.Counter()
    for x,coef in row.items():
        assert gauss(x)
        h,Sx=occupation(x); assert len(Sx)==len(S)
        if loss(x)==0 and x!=st:
            rise=phi(h,Sx)-base
            assert rise>=6,(len(S),h,rise)
            rises.append(rise)
            counts['same_hole' if h==c else 'hole_moving']+=1
    hs=H(st)
    reverse_results.append({'k':len(S),'output_words':len(hs),'reverse_words':len(row),'other_dark_counts':dict(counts),'height_rises':dict(collections.Counter(rises)),'deep_bright_G_at_least_4_outputs':sum(loss(x)>=4 for x in hs)})
assert reverse_results[2]['deep_bright_G_at_least_4_outputs']==0

# Exact zero-cycle-angle Dicke-vacancy intertwiner on an L8 torus.
# Charges remain in the proof; this is the exact invariant symmetric-charge
# subspace of this fiber, not a replacement for general field vectors.
sites=list(itertools.product(range(L),repeat=3)); A=[s for s in sites if not parity(s)]
def tnb(a): return [tuple(x%L for x in add(a,d)) for d in dirs]
def vp(v): return tuple(sorted(v))
def vlocal(vec,a,dag=False):
    out=collections.defaultdict(int)
    for holes,n in vec.items():
        holes=set(holes)
        for b in tnb(a):
            if (not dag and a not in holes and b in holes):
                out[vp((holes-{b})|{a})]+=n
            elif dag and a in holes and b not in holes:
                out[vp((holes-{a})|{b})]+=n
    return clean(out)
def vglobal(vec,dag=False):
    out=collections.defaultdict(int)
    for a in A: accumulate(out,vlocal(vec,a,dag))
    return clean(out)
def vC(vec):
    out=collections.defaultdict(int)
    for a in A:
        neighborhood={tuple(x%L for x in add(a,d)) for d in near}
        gated={s:n for s,n in vec.items() if not neighborhood.intersection(s)}
        accumulate(out,vlocal(vlocal(gated,a),a,True))
    return clean(out)
b0=(1,0,0)
v={vp((h,b0)):(1 if (h[0]//2+h[2])%2==0 else -1) for h in A if (h[1]+h[2])%L==4}
assert len(v)==32
assert all(h[0]%2==0 for holes in v for h in holes if h!=b0)
adj=collections.defaultdict(int)
for holes,n in v.items():
    h=next(x for x in holes if x!=b0)
    for b in tnb(h): adj[b]+=n
    assert b0 not in tnb(h)
assert not clean(adj)
f=vglobal(v); fd=vglobal(v,True); cv=vC(v)
ffdag=vglobal(fd); fdagf=vglobal(f,True)
hv=collections.defaultdict(int)
accumulate(hv,cv); accumulate(hv,ffdag); accumulate(hv,fdagf,-1)
assert not clean(hv)
assert cv==fdagf and not fd

# Finite combinatorial Dicke transport: each sign assignment is mapped once,
# with no normalization ratio, for any fixed number of minus signs.
dicke_checks=0
for n in range(2,9):
    for m in range(n+1):
        words=list(itertools.combinations(range(n),m))
        shifted=[tuple(sorted(99 if i==0 else i for i in word)) for word in words]
        assert len(set(shifted))==len(words)
        dicke_checks+=1

result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'geometry':geometry,'shield':{'k':35,'neighbor_occupied_counts':shield_counts},'failed_periodic_minimum_image_height':badheight,'physical_reverse_rows':reverse_results,'periodic_literal_fiber':{'L':L,'k':255,'initial_words':len(v),'F_words':len(f),'Fdag_words':len(fd),'C_words':len(cv),'FdagF_words':len(fdagf),'H_words':len(clean(hv)),'G_words':0,'dicke_combinatorial_cases':dicke_checks,'cycle_dimension':3*L**3-L**3+1},'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
