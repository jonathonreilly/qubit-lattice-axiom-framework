#!/usr/bin/env python3
"""Exact selected ORIGINAL rotor words; not a simulation of their probabilities."""
import json
from itertools import product


def check(L,b,r,dark):
    assert L>=8 and L%4==0 and r>=1
    n=L**3//2
    assert 1<=b<=n//4 and (not dark or b>=4)
    def add(v,d): return tuple((v[i]+d[i])%L for i in range(3))
    def axis(i,s): return tuple(s if j==i else 0 for j in range(3))
    def isA(v): return sum(v)%2==0
    qs={v:1 for v in product(range(L),repeat=3) if isA(v)}
    fields={}; div={}; endpoint_checks=0; primitive_hops=0; births=0
    def setq(v,q):
        if q: qs[v]=q
        else: qs.pop(v,None)
    def increment(a,z,k):
        nonlocal endpoint_checks
        assert isA(a) and not isA(z)
        assert sum(min((a[i]-z[i])%L,(z[i]-a[i])%L) for i in range(3))==1
        edge=(a,z); fields[edge]=fields.get(edge,0)+k
        if fields[edge]==0: del fields[edge]
        div[a]=div.get(a,0)+k; div[z]=div.get(z,0)-k
        for v in (a,z):
            assert div.get(v,0)==qs.get(v,0)-int(isA(v))
            endpoint_checks+=1
    def out(a,z):
        nonlocal primitive_hops
        q=qs.get(a,0); assert q in (-1,1) and qs.get(z,0)==0
        setq(a,0);setq(z,q);increment(a,z,-q);primitive_hops+=1
    def inward(a,z):
        nonlocal primitive_hops
        q=qs.get(z,0);assert q in (-1,1) and qs.get(a,0)==0
        setq(z,0);setq(a,q);increment(a,z,q);primitive_hops+=1
    def jplus(a,z):
        assert qs.get(a,0)==qs.get(z,0)==0
        setq(a,1);setq(z,-1);increment(a,z,1)
    def ordinary(a,old,marked):
        nonlocal births
        out(a,old);jplus(a,marked);births+=1
    a0=(0,0,0)
    ordinary(a0,(1,0,0),(0,1,0))
    grid=[v for v in product(range(L),repeat=3) if v[1]%4==0 and (v[0]+v[2])%2==0 and v!=a0]
    if dark:
        aminus,aplus,az=(4,0,0),(4,4,0),(4,2,L-2)
        for a in (aminus,aplus): ordinary(a,add(a,axis(1,-1)),add(a,axis(1,1)))
        ordinary(az,add(az,axis(2,-1)),add(az,axis(2,1)))
        extra=[v for v in grid if v not in (aminus,aplus)][:b-4]
    else: extra=grid[:b-1]
    for a in extra: ordinary(a,add(a,axis(1,-1)),add(a,axis(1,1)))
    assert births==b and sum(abs(e) for e in fields.values())==2*b
    prep_q=qs.copy(); prep_E=fields.copy()
    m=r*L//4
    for step in range(m):
        x=(4*step+1)%L
        start=(x,0,0);a=((x+1)%L,0,0);d=((x+2)%L,0,0)
        c=((x+3)%L,0,0);end=((x+4)%L,0,0)
        assert qs.get(start)==1 and d!=end
        assert sum(min((a[i]-c[i])%L,(c[i]-a[i])%L) for i in range(3))==2
        out(a,d);out(c,end);inward(c,d);inward(a,start)
    assert qs==prep_q
    cycle={}
    for x in range(0,L,2):
        a=(x,0,0);cycle[(a,((x+1)%L,0,0))]=-1;cycle[(a,((x-1)%L,0,0))]=1
    for edge in set(fields)|set(prep_E)|set(cycle):
        assert fields.get(edge,0)-prep_E.get(edge,0)==r*cycle.get(edge,0)
    c0=(4,2,0);old=add(c0,axis(0,1));marked=add(c0,axis(2,1));last=add(c0,axis(0,-1))
    out(c0,old);jplus(c0,marked);out(c0,last) # B^+=-F j F: overall minus is analytic.
    Aholes=sum(qs.get(v,0)==0 for v in product(range(L),repeat=3) if isA(v))
    NB=sum(1 for v,q in qs.items() if not isA(v))
    minus=sum(q==-1 for q in qs.values())
    G=2*sum(qs.get(add(c0,axis(i,s)),0)==0 for i in range(3) for s in (-1,1))
    flux=0
    for (a,z),E in fields.items():
        if a[1:]==z[1:] and {a[0],z[0]}=={0,L-1}:
            local_dx=1 if (z[0]-a[0])%L==1 else -1
            flux-=local_dx*E
    assert Aholes==1 and NB==2*b+3 and minus==b+1 and sum(qs.values())==n
    assert sum(abs(E) for E in fields.values())==2*b+3+r*L
    assert max(abs(E) for E in fields.values())==r+1 and flux==r
    assert G==(0 if dark else 6)
    for v in product(range(L),repeat=3): assert div.get(v,0)==qs.get(v,0)-int(isA(v))
    return {'L':L,'ordinary_births':b,'source_NB':NB,'source_G':G,'winding':r,
            'actual_pair_factors':m,'pair_word_coefficient_lower_bound':'2^m (analytic complete Q positivity)',
            'field_l1':sum(abs(E) for E in fields.values()),'field_max':max(abs(E) for E in fields.values()),
            'Gauss_endpoint_checks':endpoint_checks,'primitive_hops':primitive_hops,
            'scope':'selected exact legal original words only; complete-mark/no-event Taylor argument analytic, no probability or rank simulation'}


if __name__=='__main__':
    cases=[check(8,1,1,False),check(8,4,1,True),check(8,64,2,True),check(16,512,1,True)]
    print(json.dumps({'cases':cases},indent=2))
    print('TOTAL PASS=4 FAIL=0')
