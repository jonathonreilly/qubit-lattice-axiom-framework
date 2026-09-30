#!/usr/bin/env python3
"""Exact finite controls only; no enumeration of full charge/fiber space."""
import os,sys,time,json,math,resource,hashlib
from pathlib import Path
from collections import defaultdict
START=time.monotonic(); CPU=time.process_time()
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
DEADLINE=json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
def guard():
    assert not (RUNTIME/'STOP_REQUESTED.json').exists(),'STOP_REQUESTED'
    assert time.time()<DEADLINE,'deadline'
    assert time.monotonic()-START<90,'wall cap'
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform!='darwin': rss*=1024
    assert rss<120*1024**2,('RSS cap',rss)
def add(v,w,c=1):
    for k,a in w.items():
        v[k]+=c*a
        if not v[k]: del v[k]
def fixture(L):
    guard(); m=L//2; N=L**3//2
    pts=[(x,y,z) for x in range(L) for y in range(L) for z in range(L)]
    A={x for x in pts if sum(x)%2==0}; B=set(pts)-A
    def shift(p,i,s):
        q=list(p);q[i]=(q[i]+s)%L;return tuple(q)
    def adj(p): return [shift(p,i,s) for i in range(3) for s in (-1,1)]
    def dist(a,b): return sum(min((x-y)%L,(y-x)%L) for x,y in zip(a,b))
    h=(0,m,0); v=(1,0,0); star=[(1,m,0),(L-1,m,0),(0,m-1,0)]
    pairs=[]
    for y in range(L):
        for z in range(L):
            p=(1-y-z)%2
            if (y,z)==(m,0):
                pairs += [((x,y,z),(x+2,y,z),(x+1,y,z)) for x in range(3,L-3,4)]
                continue
            for x in range(p,L,4):
                if z==0 and y<m and x==p: continue
                pairs.append(((x,y,z),((x+2)%L,y,z),((x+1)%L,y,z)))
    for y in range(m-1):
        if y%2==0: pairs.append(((3,y,0),(2,y+1,0),(2,y,0)))
        else: pairs.append(((0,y,0),(1,y+1,0),(1,y,0)))
    used=[b for pair in pairs for b in pair[:2]]
    assert len(pairs)==(N-4)//2
    assert len(set(used))==len(used) and set(used)==B-{v,*star}
    assert len({a for _,_,a in pairs})==len(pairs) and h not in {a for _,_,a in pairs}
    assert all(a in A and c in B and d in B and dist(a,c)==dist(a,d)==1 for c,d,a in pairs)
    q={x:1 if x in A else 0 for x in pts}; E=defaultdict(int); hops=marks=0
    def hop(a,b):
        nonlocal hops
        assert q[a] and not q[b] and dist(a,b)==1
        charge=q[a]; q[a]=0;q[b]=charge;E[a,b]-=charge;hops+=1
    def birth(a,b):
        nonlocal marks
        assert q[a]==q[b]==0 and dist(a,b)==1
        q[a]=1;q[b]=-1;E[a,b]+=1;marks+=1
    for c,d,a in pairs: hop(a,c);birth(a,d)
    assert all(q[a] for a in A) and {b for b in B if not q[b]}=={v,*star}
    hop(h,star[0]);birth(h,star[1]);hop(h,star[2])
    assert {a for a in A if not q[a]}=={h}
    assert {b for b in B if not q[b]}=={v}
    assert sum(c==-1 for c in q.values())==(N-2)//2
    div=defaultdict(int)
    for (a,b),e in E.items(): div[a]+=e;div[b]-=e
    assert all(div[x]==q[x]-(x in A) for x in pts)
    assert max(map(abs,E.values()))==1
    f={a:(-1)**(a[0]//2+a[2]) for a in A if (a[1]+a[2])%L==m}
    assert len(f)==L*L//2 and all(dist(a,v)>=5 for a in f)
    K=defaultdict(int)
    for a,c in f.items():
        for b in adj(a): K[b]+=c
    assert all(c==0 for c in K.values())
    state=lambda ah,bh:(tuple(sorted(ah)),tuple(sorted(bh)))
    psi={state({a},{v}):c for a,c in f.items()}
    def F(s,dag=False):
        ah,bh=map(set,s);out=defaultdict(int)
        if not dag:
            for b in bh:
                for a in adj(b):
                    if a not in ah: out[state(ah|{a},bh-{b})]+=1
        else:
            for a in ah:
                for b in adj(a):
                    if b not in bh: out[state(ah-{a},bh|{b})]+=1
        return out
    def C(s):
        ah,bh=map(set,s);out=defaultdict(int)
        for a in {a for b in bh for a in adj(b)}:
            if a in ah or any(dist(a,hole)==2 for hole in ah): continue
            for b in set(adj(a))&bh:
                for c in set(adj(a))-(bh-{b}): out[state(ah,(bh-{b})|{c})]+=1
        return out
    def apply(vv,op):
        out=defaultdict(int)
        for st,c in vv.items(): add(out,op(st),c)
        return out
    fd=apply(psi,lambda s:F(s,True)); assert not fd
    cv=apply(psi,C); ff=apply(apply(psi,F),lambda s:F(s,True))
    assert cv==ff and cv
    full=defaultdict(int);add(full,cv);add(full,apply(fd,F));add(full,ff,-1);assert not full
    guard()
    return {'L':L,'N':N,'ordinary_births':len(pairs),'actual_total_birth_marks':marks,'literal_hops':hops,'W':1,'N_B':N-1,'N_minus':(N-2)//2,'gauss_sites_checked':len(pts),'max_abs_E':1,'one_word_field_l1':sum(map(abs,E.values())),'hole_wave_support':len(f),'full_C_coefficients':len(cv),'full_FdagF_coefficients':len(ff),'H_residual_coefficients':0,'Fdag_residual_coefficients':0,'cycle_dimension':2*L**3+1,'scope':'One legal original word plus exact full canceled vacancy fiber. Full charge Dicke embedding and all-word positivity are analytic proofs, not enumerated here.'}
guard(); rows=[fixture(L) for L in (8,12,16)];guard()
rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
if sys.platform!='darwin': rss*=1024
out={'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'cases':rows,'cpu_seconds':time.process_time()-CPU,'wall_seconds':time.monotonic()-START,'peak_rss_bytes':rss,'threads':1,'failures':[],'science_scope':'Finite corroboration only; no asymptotic source/tail theorem inferred from tests.'}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
