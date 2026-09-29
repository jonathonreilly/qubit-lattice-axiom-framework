"""Exact full-original-first-mark energy calculation on cubic integer rotors.
Gram-path implementation of q/E words and the supplied F and j moves.
No one-pair Hamiltonian projection or substituted birth observable is used.
All arithmetic integers or Fraction; infinite-lattice locality reduction.
"""
AUDIT_TIMEOUT_SEC = 180

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

DIRS = tuple(tuple(s if i == j else 0 for i in range(3)) for j in range(3) for s in (-1, 1))
ORIGIN = (0,0,0)
OMEGA = ((), ())
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def even(a): return sum(a)%2 == 0
def nb(a): return tuple(add(a,d) for d in DIRS)
def default(a): return int(even(a))
def canonical(q,e):
    return (tuple(sorted((v,x) for v,x in q.items() if x != default(v))),
            tuple(sorted((ab,x) for ab,x in e.items() if x)))
def unpack(s): return dict(s[0]), dict(s[1])
def charge(q,v): return q.get(v,default(v))
def F(s,a):
    q,e = unpack(s); v = charge(q,a)
    if not v: return []
    ans=[]
    for b in nb(a):
        if charge(q,b): continue
        q2,e2=q.copy(),e.copy(); q2[a]=0; q2[b]=v
        e2[a,b]=e2.get((a,b),0)-v
        ans.append(canonical(q2,e2))
    return ans

def J(s,a,b,sigma):
    q,e=unpack(s)
    if charge(q,a) or charge(q,b): return None
    q[a]=sigma; q[b]=-sigma; e[a,b]=e.get((a,b),0)+sigma
    return canonical(q,e)

def birth(a,b,sigmas):
    out=Counter()
    for sigma in sigmas:
        for t in F(OMEGA,a):
            y=J(t,a,b,sigma)
            if y is not None: out[y]+=1
    return out

def gauss(s):
    q,e=unpack(s); div=Counter()
    for (a,b),v in e.items(): div[a]+=v; div[b]-=v
    return all(div[v] == charge(q,v)-default(v) for v in set(q)|set(div))

def D(s):
    q,e=unpack(s)
    return sum(v*(v-charge(q,a)) for (a,b),v in e.items() if charge(q,b)==0)

def partners(a):
    return {c for b in nb(a) for c in nb(b)}-{a}

def candidate_pairs(vec,halo=0):
    vertices={v for s in vec for v,c in s[0]}|{v for s in vec for ab,c in s[1] for v in ab}
    active={a for v in vertices for a in ((v,) if even(v) else nb(v))}
    for _ in range(halo): active |= {c for a in active for c in partners(a)}
    return sorted({tuple(sorted((a,c))) for a in active for c in partners(a)})

def apply_pair(vec,a,c):
    out=Counter()
    for s,v in vec.items():
        for u in F(s,a):
            for t in F(u,c): out[t]+=v
    return out

def norm2(vec): return sum(v*v for v in vec.values())

def energy_change(vec,halo=0):
    norm=norm2(vec); total=0; rows=[]
    assert all(gauss(s) and D(s)==0 for s in vec)
    for a,c in candidate_pairs(vec,halo):
        out=apply_pair(vec,a,c)
        vacuum_count=36-len(set(nb(a))&set(nb(c)))
        excess=norm2(out)-norm*vacuum_count
        total-=2*excess
        if excess: rows.append({'a':a,'c':c,'S_norm2':norm2(out),'vacuum_count':vacuum_count,'norm_excess':excess})
    return Fraction(total,norm),rows


def shift_difference(e,f):
    z=Counter(dict(e))
    for k,v in f:z[k]-=v
    return tuple(sorted((k,v) for k,v in z.items() if v))

def gram_laurent(vec):
    groups=defaultdict(list)
    for (q,e),v in vec.items():groups[q].append((e,v))
    out=Counter()
    for group in groups.values():
        for e,u in group:
            for f,v in group:out[shift_difference(e,f)]+=u*v
    return out

def work_laurent(vec,halo=0):
    n=norm2(vec);out=Counter()
    for a,c in candidate_pairs(vec,halo):
        for z,v in gram_laurent(apply_pair(vec,a,c)).items():out[z]-=Fraction(2*v,n)
        for z,v in gram_laurent(apply_pair({OMEGA:1},a,c)).items():out[z]+=2*v
    return {z:v for z,v in out.items() if v}
