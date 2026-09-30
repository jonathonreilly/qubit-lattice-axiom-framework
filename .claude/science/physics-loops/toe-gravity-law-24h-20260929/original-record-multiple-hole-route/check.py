#!/usr/bin/env python3
"""Actual multiple-hole C+[F,F*], overlapping gates, reverse rows and marks.

Elementary conventions match our earlier checked rotor controls; no old runner
is imported or executed. All coefficients and fields are exact integers.
"""
from pathlib import Path
import collections, datetime, hashlib, itertools, json, resource, time
P=Path(__file__).resolve().parent
R=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (R/'STOP_REQUESTED.json').exists()
assert time.time()<json.loads((R/'DEADLINE.json').read_text())['deadline_epoch']
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
t0,c0=time.monotonic(),time.process_time()
origin=(0,0,0)
dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def parity(x): return sum(x)%2
def nb(x): return [add(x,d) for d in dirs]
near=sorted({add(x,y) for x in dirs for y in dirs}-{origin})
def pack(q,e): return (tuple(sorted((x,v) for x,v in q.items() if v!=1-parity(x))),tuple(sorted((x,v) for x,v in e.items() if v)))
def charge(q,x): return q.get(x,1-parity(x))
def move(st,a,b,adj=False):
    q,e=dict(st[0]),dict(st[1]); qa,qb=charge(q,a),charge(q,b)
    if (not adj and (qa==0 or qb!=0)) or (adj and (qa!=0 or qb==0)): return None
    value=qb if adj else qa
    q[a],q[b]=(value,0) if adj else (0,value)
    e[(a,b)]=e.get((a,b),0)+(value if adj else -value)
    return pack(q,e)
def birth(st,a,b,s):
    q,e=dict(st[0]),dict(st[1])
    if charge(q,a)!=0 or charge(q,b)!=0: return None
    q[a],q[b]=s,-s; e[(a,b)]=e.get((a,b),0)+s
    return pack(q,e)
def fa(v,a,adj=False):
    out=collections.defaultdict(int)
    for st,n in v.items():
        for b in nb(a):
            y=move(st,a,b,adj)
            if y is not None: out[y]+=n
    return {x:n for x,n in out.items() if n}
def occupancy(st):
    return ({x for x,v in st[0] if not parity(x) and v==0},{x for x,v in st[0] if parity(x) and v!=0})
def loss(st):
    holes,S=occupancy(st); return 2*sum(b not in S for h in holes for b in nb(h))
def inc(out,v,c=1):
    for st,n in v.items(): out[st]+=c*n
def H(st,wrong_additive=False):
    holes,S=occupancy(st); out=collections.defaultdict(int); v={st:1}
    adjacent=collections.Counter(add(h,d) for h in holes for d in near)
    for h in holes: inc(out,fa(fa(v,h,True),h))
    for a,multiplicity in adjacent.items():
        if a not in holes: inc(out,fa(fa(v,a),a,True),-multiplicity if wrong_additive else -1)
    for h in holes:
        for d in near:
            a=add(h,d)
            if a not in holes:
                inc(out,fa(fa(v,h,True),a))
                inc(out,fa(fa(v,a),h,True),-1)
    return {x:n for x,n in out.items() if n}
def global_H(st,anchors):
    v={st:1}; out=collections.defaultdict(int); holes,S=occupancy(st)
    def F(vec,adj=False):
        ans=collections.defaultdict(int)
        for a in anchors: inc(ans,fa(vec,a,adj))
        return {x:n for x,n in ans.items() if n}
    inc(out,F(F(v,True)))
    inc(out,F(F(v),True),-1)
    for a in anchors:
        if all(add(a,d) not in holes for d in near): inc(out,fa(fa(v,a),a,True))
    return {x:n for x,n in out.items() if n}
def gauss(st):
    q,e=dict(st[0]),dict(st[1]); divergence=collections.defaultdict(int)
    for (a,b),v in e.items(): divergence[a]+=v; divergence[b]-=v
    return all(divergence[x]==charge(q,x)-(1-parity(x)) for x in set(q)|set(divergence))
def physical(holes,S):
    m,k=len(holes),len(S); assert k>=m and (k-m)%2==0
    q={h:0 for h in holes}
    for i,b in enumerate(sorted(S)): q[b]=-1 if i<(k-m)//2 else 1
    assert origin in holes
    e=collections.defaultdict(int)
    for x,value in q.items():
        delta=value-(1-parity(x)); a=x
        for axis in range(3):
            while a[axis]:
                d=[0,0,0]; d[axis]=-1 if a[axis]>0 else 1
                b=add(a,d)
                if not parity(a): e[(a,b)]+=delta
                else: e[(b,a)]-=delta
                a=b
    ans=pack(q,e); assert gauss(ans); return ans
def phi(st):
    holes,S=occupancy(st); h=max(x[0] for x in holes)
    return sum(max(-5,min(5,h-b[0])) for b in S)

# Literal finite-sum expression, including all neighbors of every input hole.
# Terms at further A centers commute/cancel exactly; two remote anchors are
# nevertheless retained here to check that their contributions cancel too.
holes={origin,(1,1,0)}; S=set().union(*(set(nb(h)) for h in holes))
assert len(S)==10
st=physical(holes,S)
anchors=holes|{add(h,d) for h in holes for d in near}|{(10,0,0),(12,0,0)}
literal=global_H(st,sorted(anchors)); correct=H(st); wrong=H(st,True)
assert literal==correct
difference={x:wrong.get(x,0)-correct.get(x,0) for x in set(wrong)|set(correct)}
difference={x:n for x,n in difference.items() if n}
assert difference
literal_info={'m':2,'k':10,'A_anchors':len(anchors),'actual_output_words':len(correct),'wrong_additive_difference_words':len(difference),'wrong_additive_difference_squared_norm':sum(n*n for n in difference.values())}

ball5={x for x in itertools.product(range(-5,6),repeat=3) if sum(map(abs,x)) in (1,3,5)}
assert len(ball5)==146
specs=[
    (holes,S),
    ({origin,(0,2,0)},set(nb(origin))|set(nb((0,2,0)))|{(9,0,0)}),
    ({origin,(0,0,2)},ball5),
    ({origin,(1,1,0),(0,0,2)},ball5|{(17,0,0)}),
    ({origin,(1,1,0),(0,0,2),(0,2,0)},ball5),
]
rows=[]; gauss_checks=0; mark_checks=0
for holes,S in specs:
    st=physical(holes,S); assert loss(st)==0
    h=max(holes); b=add(h,(1,0,0)); c=add(h,(2,0,0))
    assert c not in holes
    beta=move(move(st,h,b,True),c,b)
    assert move(move(beta,c,b,True),h,b)==st
    hb=H(beta); hs=H(st)
    assert hs.get(beta)==hb.get(st)==1
    categories=collections.Counter(); rises=collections.Counter()
    for y,n in hb.items():
        assert gauss(y); gauss_checks+=1
        Z,Sy=occupancy(y); assert len(Z)==len(holes) and len(Sy)==len(S)
        if y!=st and loss(y)==0:
            rise=phi(y)-phi(st); assert rise>=6
            categories['same_mask' if Z==occupancy(beta)[0] else ('retains_selected_output_hole' if c in Z else 'moves_selected_output_hole')]+=1
            rises[rise]+=1
    spectral_rise=phi(beta)-phi(st) if loss(beta)==0 else None
    if spectral_rise is not None: assert spectral_rise>=12
    # Actual original outputs from a representative bright word, both signs.
    bright=next((y for y in hs if loss(y)>0),None)
    if bright is not None:
        Z,_=occupancy(bright)
        for a in Z:
            for bb in nb(a):
                for sign in (-1,1):
                    y=birth(bright,a,bb,sign)
                    if y is not None:
                        zz,ss=occupancy(y)
                        assert len(zz)==len(holes)-1 and len(ss)==len(S)+1 and gauss(y)
                        mark_checks+=1
    rows.append({'m':len(holes),'k':len(S),'input_words':len(hs),'reverse_words':len(hb),'selected_hole':h,'output_hole':c,'other_dark_categories':dict(categories),'height_rises':dict(rises),'spectral_height_rise':spectral_rise})
    assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<150*1024**2

# An actual finite original-mark word, without replacing the cascade law.
state=physical({origin,(4,0,0)},{(1,0,0),(5,0,0)})
cascade=[{'W':len(occupancy(state)[0]),'NB':len(occupancy(state)[1])}]
for a,b,s in [(origin,(-1,0,0),1),((4,0,0),(3,0,0),-1)]:
    state=birth(state,a,b,s); assert state is not None and gauss(state)
    cascade.append({'W':len(occupancy(state)[0]),'NB':len(occupancy(state)[1])})
assert cascade==[{'W':2,'NB':2},{'W':1,'NB':3},{'W':0,'NB':4}]
assert H(state)=={} and loss(state)==0

out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'literal_full_gate_check':literal_info,'reverse_rows':rows,'gauss_reverse_words_checked':gauss_checks,'actual_original_mark_outputs_checked':mark_checks,'actual_two_mark_grade_word':cascade,'cpu_seconds':time.process_time()-c0,'wall_seconds':time.monotonic()-t0,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
(P/'RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
