"""Exact Laurent polynomial of J_-* H4 J_- minus the empty-B field block.

Personal new energy diagnostic. Reuses disclosed vertex/preparation and active-pair
logic of flat_matter_controls.py; implements link monomials and the pair norm
independently of that program's flat action. Not an independent scientific check.
"""
from collections import defaultdict
from itertools import product
from pathlib import Path
import json,time


def add_word(*words):
    out=defaultdict(int)
    for w in words:
        for e,n in w:out[e]+=n
    return tuple(sorted((e,n) for e,n in out.items() if n))


def negative(w):return tuple((e,-n) for e,n in w)


def control(side):
    assert side%2==0 and side>=6
    vertices=list(product(range(side),repeat=3));idx={v:i for i,v in enumerate(vertices)}
    bits=[1<<i for i in range(len(vertices))];A=[i for i,v in enumerate(vertices) if sum(v)%2==0]
    def loc(v):return idx[tuple(x%side for x in v)]
    def near(i):
        v=vertices[i];out=[]
        for mu in range(3):
            for s in (-1,1):
                x=list(v);x[mu]=(x[mu]+s)%side;out.append(idx[tuple(x)])
        return out
    adj={i:near(i) for i in range(len(vertices))};mask=sum(bits[i] for i in A)
    a,d,h,c,e=map(loc,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),(0,1,0)])
    blockers=list(map(loc,[(0,-1,0),(0,0,1),(0,0,-1)]))
    minus=bits[d]|bits[h];common=(mask^minus)|sum(bits[i] for i in blockers)
    initial=[(common|bits[x],minus) for x in (c,e)];empty=(mask,0)
    pairs=set()
    for x in A:
        for y in adj[x]:
            for z in adj[y]:
                if x<z:pairs.add((x,z))
    pairs=sorted(pairs)
    active=[]
    for x,z in pairs:
        near_mask=sum(bits[v] for v in set(adj[x])|set(adj[z]))
        if any(((p|n)&near_mask) or (n&(bits[x]|bits[z])) for p,n in initial):active.append((x,z))
    def forward(vector,x):
        out=defaultdict(int)
        for ((p,n),w),amp in vector.items():
            assert (p|n)&bits[x]
            charge=1 if p&bits[x] else -1
            for y in adj[x]:
                if (p|n)&bits[y]:continue
                q=(p^bits[x]^bits[y],n) if charge==1 else (p,n^bits[x]^bits[y])
                w2=add_word(w,(((x,y),-charge),))
                out[q,w2]+=amp
        return dict(out)
    def norm_poly(vec):
        by_matter=defaultdict(list)
        for (q,w),amp in vec.items():
            if amp:by_matter[q].append((w,amp))
        out=defaultdict(int)
        for terms in by_matter.values():
            for w,amp in terms:
                for w2,amp2 in terms:out[add_word(w,negative(w2))]+=amp*amp2
        return {w:a for w,a in out.items() if a}
    prep={(initial[0],(((d,c),-1),)):1,(initial[1],(((d,e),-1),)):-1}
    base={(empty,()):1};delta=defaultdict(int);pair_rows=[]
    for x,z in active:
        p=norm_poly(forward(forward(prep,x),z));b=norm_poly(forward(forward(base,x),z))
        local=defaultdict(int)
        for w,amp in p.items():local[w]-=amp # -2 H4 factor times preparation norm 1/2
        for w,amp in b.items():local[w]+=2*amp
        local={w:amp for w,amp in local.items() if amp}
        for w,amp in local.items():delta[w]+=amp
        pair_rows.append({'pair':[vertices[x],vertices[z]],'terms':len(local),'flat_excess':sum(local.values())})
    delta={w:amp for w,amp in delta.items() if amp}
    for w,amp in delta.items():
        assert delta.get(negative(w))==amp
        divergence=defaultdict(int)
        for (x,y),n in w:divergence[x]+=n;divergence[y]-=n
        assert all(n==0 for n in divergence.values())
        assert sum(abs(n) for _,n in w)<=6
    def describe(w):return [[vertices[x],vertices[y],n] for (x,y),n in w]
    rows=[{'word':describe(w),'coefficient':n,'length':sum(abs(a) for _,a in w)} for w,n in sorted(delta.items())]
    result={'side':side,'vertices':len(vertices),'all_pairs':len(pairs),'active_union':len(active),
            'terms':len(delta),'constant_coefficient':delta.get((),0),'flat_excess':sum(delta.values()),
            'absolute_coefficient_sum':sum(abs(x) for x in delta.values()),'words':rows,'pair_rows':pair_rows}
    assert result['flat_excess']==5140
    return result

if __name__=='__main__':
    started=time.perf_counter();rows=[control(side) for side in (8,16)]
    print(json.dumps({'scope':__doc__,'rows':rows,'elapsed_seconds':time.perf_counter()-started},indent=2))
