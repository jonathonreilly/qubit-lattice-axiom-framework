"""Author original-mark magnetic energy-drift polynomial on the charged probe.

Disclosed reuse of the preceding root's Laurent representation/preparation.
New calculation includes recycling AND the real anticommutator form; it is
not conditional output energy minus an unconditional input mean.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json,time


def word_sum(*words):
    out=defaultdict(int)
    for w in words:
        for edge,n in w:out[edge]+=n
    return tuple(sorted((e,n) for e,n in out.items() if n))
def neg(w):return tuple((e,-n) for e,n in w)
def cross(left,right):
    l=defaultdict(list);r=defaultdict(list)
    for (q,w),a in left.items():
        if a:l[q].append((w,a))
    for (q,w),a in right.items():
        if a:r[q].append((w,a))
    out=defaultdict(int)
    for q,terms in l.items():
        for u,a in terms:
            for v,b in r.get(q,[]):out[word_sum(v,neg(u))]+=a*b
    return {w:a for w,a in out.items() if a}

def control(L,sigma):
    vertices=list(product(range(L),repeat=3));index={v:i for i,v in enumerate(vertices)}
    bits=[1<<i for i in range(len(vertices))];A=[i for i,v in enumerate(vertices) if sum(v)%2==0]
    def loc(v):return index[tuple(x%L for x in v)]
    def near(i):
        v=vertices[i];out=[]
        for mu in range(3):
            for s in (-1,1):
                x=list(v);x[mu]=(x[mu]+s)%L;out.append(index[tuple(x)])
        return out
    adj={i:near(i) for i in range(len(vertices))};mask=sum(bits[i] for i in A)
    a,d,h,c,e,b=map(loc,[(0,0,0),(1,1,0),(2,2,0),(1,0,0),(0,1,0),(-1,0,0)])
    blockers=list(map(loc,[(0,-1,0),(0,0,1),(0,0,-1)]))
    n=bits[d]|bits[h];p=(mask^n)|sum(bits[v] for v in blockers)
    raw={((p|bits[c],n),(((d,c),-1),)):1,((p|bits[e],n),(((d,e),-1),)):-1}
    pairs=set()
    for x in A:
        for y in adj[x]:
            for z in adj[y]:
                if x<z:pairs.add((x,z))
    mark_support={a,*adj[a]}
    active=[(x,z) for x,z in sorted(pairs) if mark_support&{x,z,*adj[x],*adj[z]}]
    def hop(vector,x,inward=False):
        out=defaultdict(int)
        for ((p,n),w),amp in vector.items():
            for y in adj[x]:
                src,dst=(y,x) if inward else (x,y)
                if not (p|n)&bits[src] or (p|n)&bits[dst]:continue
                charge=1 if p&bits[src] else -1
                q=(p^bits[src]^bits[dst],n) if charge==1 else (p,n^bits[src]^bits[dst])
                shift=charge if inward else -charge
                out[q,word_sum(w,(((x,y),shift),))]+=amp
        return {k:v for k,v in out.items() if v}
    def bare_creation(vector,adjoint=False):
        out=defaultdict(int)
        for ((p,n),w),amp in vector.items():
            if not adjoint:
                if (p|n)&(bits[a]|bits[b]):continue
                q=(p|bits[a],n|bits[b]) if sigma==1 else (p|bits[b],n|bits[a])
                shift=sigma
            else:
                pos,minus=(a,b) if sigma==1 else (b,a)
                if not p&bits[pos] or not n&bits[minus]:continue
                q=(p^bits[pos],n^bits[minus]);shift=-sigma
            out[q,word_sum(w,(((a,b),shift),))]+=amp
        return {k:v for k,v in out.items() if v}
    def B(vector):return bare_creation(hop(vector,a))
    def Bstar(vector):return hop(bare_creation(vector,True),a,True)
    bv=B(raw);mv=Bstar(bv)
    assert sum(cross(bv,bv).values())==0
    result=defaultdict(Fraction);rows=[]
    for x,z in active:
        sb=hop(hop(bv,x),z);sm=hop(hop(mv,x),z);sv=hop(hop(raw,x),z)
        gain=cross(sb,sb);anti=cross(sm,sv);local=defaultdict(Fraction)
        for w,amp in gain.items():local[w]-=amp
        for w,amp in anti.items():
            local[w]+=Fraction(amp,2);local[neg(w)]+=Fraction(amp,2)
        local={w:amp for w,amp in local.items() if amp}
        for w,amp in local.items():result[w]+=amp
        rows.append({'pair':[vertices[x],vertices[z]],'terms':len(local),'value_at_zero':str(sum(local.values()))})
    result={w:amp for w,amp in result.items() if amp}
    assert sum(result.values())==0
    for w,amp in result.items():
        assert result.get(neg(w))==amp
        div=defaultdict(int)
        for (x,y),n in w:div[x]+=n;div[y]-=n
        assert all(v==0 for v in div.values())
        assert sum(abs(n) for _,n in w)<=10
    words=[{'word':[[vertices[x],vertices[y],n]for (x,y),n in w],'coefficient':str(amp),'length':sum(abs(n)for _,n in w)}for w,amp in sorted(result.items())]
    return {'L':L,'sigma':sigma,'active_pairs':len(active),'all_pairs':len(pairs),'terms':len(words),
        'coefficient_sum':str(sum(result.values())),'absolute_coefficient_sum':str(sum(abs(x)for x in result.values())),
        'constant':str(result.get((),0)),'words':words,'pair_rows':rows}

if __name__=='__main__':
    tic=time.perf_counter();rows=[control(16,s)for s in (-1,1)]
    print(json.dumps({'scope':__doc__,'rows':rows,'elapsed_seconds':time.perf_counter()-tic},indent=2))
