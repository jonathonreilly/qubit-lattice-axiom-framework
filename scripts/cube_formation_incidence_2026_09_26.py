"""Independent simultaneous incidence construction, originally frozen blind.

Adapted only to return data without writing source copies or result files.
It shares the stated primitive model, not the primary four-hop implementation.
"""
from collections import Counter, deque
from itertools import combinations, product
AUDIT_TIMEOUT_SEC = 120
A = tuple(v for v in range(8) if v.bit_count() % 2 == 0)
B = tuple(v for v in range(8) if v not in A)
EDGES = tuple((a,b) for a in A for b in B if a ^ b in (1,2,4))
EI = {e:i for i,e in enumerate(EDGES)}
NB = {a:tuple(b for aa,b in EDGES if aa==a) for a in A}
PAIRS = tuple(combinations(A,2))
MARKS = tuple((a,b,sig) for a,b in EDGES for sig in (-1,1))
OMEGA = (tuple(1 if v in A else 0 for v in range(8)), (0,)*len(EDGES))

def gauss(s):
    q, e = s
    div = [0]*8
    for f,(a,b) in zip(e, EDGES):
        div[a] += f
        div[b] -= f
    return tuple(div) == tuple(q[v]-(v in A) for v in range(8))

def d_cost(s):
    q, e = s
    assert all(q[a] for a in A)
    return sum(f*(f-q[a]) for f,(a,b) in zip(e,EDGES) if q[b]==0)

def change(s, qs, es):
    q,e = map(list,s)
    for v,value in qs.items(): q[v]=value
    for edge,delta in es.items(): e[EI[edge]] += delta
    ans=(tuple(q),tuple(e))
    assert gauss(ans)
    return ans

def s_outputs(s,pair):
    q,e=s
    a,c=pair
    assert q[a] and q[c]
    out=Counter()
    for b,d in product(NB[a],NB[c]):
        if b==d or q[b] or q[d]: continue
        y=change(s,{a:0,c:0,b:q[a],d:q[c]},
                 {(a,b):-q[a],(c,d):-q[c]})
        out[y]+=1
    return out

def s_preimages(y,pair):
    """All incidence columns of this row, obtained by destination matching.

    This is a two-hole incidence inverse, not an ordered four-hop H4 walk.
    One simultaneous destination assignment specifies each preimage exactly.
    The complete integer field is retained and the only filter is D=0.
    """
    q,e=y
    a,c=pair
    assert q[a]==q[c]==0 and all(q[b] for b in B)
    out=Counter()
    for b,d in product(NB[a],NB[c]):
        if b==d: continue
        x=change(y,{a:q[b],c:q[d],b:0,d:0},
                 {(a,b):q[b],(c,d):q[d]})
        if d_cost(x)==0:
            out[x]+=1
    return out

def j_outputs(s,mark):
    q,e=s
    a,b,sig=mark
    out=Counter()
    if q[b]: return out
    for dest in NB[a]:
        if dest==b or q[dest]: continue
        y=change(s,{a:sig,b:-sig,dest:q[a]},
                 {(a,b):sig,(a,dest):-q[a]})
        out[y]+=1
    return out

def j_preimages(y,mark):
    q,e=y
    a,b,sig=mark
    out=Counter()
    if q[a]!=sig or q[b]!=-sig: return out
    for dest in NB[a]:
        if dest==b or not q[dest]: continue
        x=change(y,{a:q[dest],b:0,dest:0},
                 {(a,b):-sig,(a,dest):q[dest]})
        if d_cost(x)==0:
            out[x]+=1
    return out

def gram(rows):
    g=Counter()
    for row in rows.values():
        for i,ci in row.items():
            for j,cj in row.items(): g[i,j]+=ci*cj
    return g

def reconstruct():
    seeds=set().union(*(set(j_outputs(OMEGA,m)) for m in MARKS))
    todo=deque(sorted(seeds)); states=[]; seen=set(seeds); sr={}; jr={}
    while todo:
        x=todo.popleft(); states.append(x)
        for pair in PAIRS:
            for y in s_outputs(x,pair):
                if (pair,y) in sr: continue
                row=s_preimages(y,pair); sr[pair,y]=row
                for z,c in row.items():
                    assert s_outputs(z,pair)[y]==c
                    if z not in seen: seen.add(z); todo.append(z)
        for mark in MARKS:
            for y in j_outputs(x,mark):
                if (mark,y) in jr: continue
                row=j_preimages(y,mark); jr[mark,y]=row
                for z,c in row.items():
                    assert j_outputs(z,mark)[y]==c
                    if z not in seen: seen.add(z); todo.append(z)
        if len(seen)>10000:
            raise RuntimeError('Incidence resource guard: closure unestablished')
    # Verify every column against all rows after queue exhaustion.
    for x in states:
        for pair in PAIRS:
            for y,c in s_outputs(x,pair).items(): assert sr[pair,y][x]==c
        for mark in MARKS:
            for y,c in j_outputs(x,mark).items(): assert jr[mark,y][x]==c
    return set(states), {k:-2*v for k,v in gram(sr).items()}, gram(jr), jr
