#!/usr/bin/env python3
"""Exact integer chain checks and explicit sufficient sparse-box constants.

The random finite currents are test objects, not samples from the Hamiltonian.
This does not validate the probability premise or a thermodynamic phase.
"""
AUDIT_TIMEOUT_SEC=120
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import time
import mpmath as mp


def add(dst,src,factor=1):
    for key,val in src.items():
        dst[key]+=factor*val
        if not dst[key]:del dst[key]


def shifted(x,mu,n=1):
    y=list(x);y[mu]+=n;return tuple(y)


def boundary(chain):
    out=defaultdict(int)
    for (x,axes),val in chain.items():
        for i,mu in enumerate(axes):
            face=axes[:i]+axes[i+1:]
            out[(shifted(x,mu),face)]+=(-1)**i*val
            out[(x,face)]-=(-1)**i*val
    return {k:v for k,v in out.items() if v}


def path(a,x):
    out=defaultdict(int);cursor=a
    assert all(x[i]>=a[i] for i in range(4))
    for mu in range(4):
        for _ in range(x[mu]-a[mu]):
            out[(cursor,(mu,))]+=1;cursor=shifted(cursor,mu)
    assert cursor==x
    return dict(out)


def edge_fill(a,x,mu):
    # Commute the appended mu-edge backwards through later coordinates.
    out=defaultdict(int);cursor=x
    for nu in range(3,mu,-1):
        for _ in range(x[nu]-a[nu]):
            cursor=shifted(cursor,nu,-1)
            out[(cursor,(mu,nu))]-=1
    return dict(out)


def edge_fill_checks():
    a=(-2,-1,0,2);rows=[];cases=0;maximum=0
    for displacement in product(range(4),repeat=4):
        x=tuple(a[i]+displacement[i] for i in range(4))
        for mu in range(4):
            q=edge_fill(a,x,mu);b=boundary(q)
            expected=defaultdict(int);add(expected,path(a,x))
            add(expected,{(x,(mu,)):1});add(expected,path(a,shifted(x,mu)),-1)
            assert b==dict(expected)
            area=sum(abs(v) for v in q.values())
            assert area==sum(displacement[nu] for nu in range(mu+1,4))
            maximum=max(maximum,area);cases+=1
    return dict(cases=cases,maximum_area=maximum,anchor=a)


def cycles_and_duality():
    # Currents arise as boundaries of independent signed plaquette chains;
    # the filling uses ONLY that resulting current and its bounding box.
    import random
    rng=random.Random(8161603);rows=[]
    for case in range(12):
        original=defaultdict(int)
        for _ in range(25):
            x=tuple(rng.randrange(-2,3) for _ in range(4))
            axes=tuple(sorted(rng.sample(range(4),2)))
            add(original,{(x,axes):rng.choice((-2,-1,1,2))})
        j=boundary(original)
        assert boundary(j)=={}
        vertices=set()
        for (x,(mu,)),val in j.items():
            vertices.update((x,shifted(x,mu)))
        a=tuple(min(x[i] for x in vertices) for i in range(4))
        q=defaultdict(int)
        for (x,(mu,)),val in j.items():add(q,edge_fill(a,x,mu),val)
        assert boundary(q)==j
        s=len(vertices)
        # This finite check permits disconnected currents and coefficients>3;
        # use the general box-diameter times total-current bound instead.
        diameter=max(max(x[i] for x in vertices)-a[i] for i in range(4))
        total=sum(abs(v) for v in j.values())
        assert sum(abs(v) for v in q.values())<=3*diameter*total
        rows.append(dict(case=case,current_edges=len(j),vertices=s,
                         current_l1=total,filled_l1=sum(abs(v) for v in q.values()),
                         general_bound=3*diameter*total))
    return rows


def cochain_d(values,k,lo,hi):
    out={}
    for x in product(range(lo,hi),repeat=4):
        for axes in combinations(range(4),k+1):
            val=0
            for i,mu in enumerate(axes):
                face=axes[:i]+axes[i+1:]
                val+=(-1)**i*(values.get((shifted(x,mu),face),0)-values.get((x,face),0))
            if val:out[(x,axes)]=val
    return out


def dual_chain_to_cochain(chain,k):
    # Primal k-face at x intersects dual (4-k)-face based at x-e_(complement)
    # with dual coordinates shifted by the common half-vector. Orient by
    # sign(axes,complement). Supports are finite here.
    out={}
    for (y,comp),value in chain.items():
        axes=tuple(i for i in range(4) if i not in comp)
        assert len(axes)==k
        x=y
        for mu in comp:x=shifted(x,mu)
        order=axes+comp
        sign=(-1)**sum(order[i]>order[j] for i in range(4) for j in range(i+1,4))
        out[(x,axes)]=sign*value
    return out


def hodge_checks():
    cases=[]
    for comp in combinations(range(4),2):
        q={((0,0,0,0),comp):1};j=boundary(q)
        two=dual_chain_to_cochain(q,2);three=dual_chain_to_cochain(j,3)
        derivative=cochain_d(two,2,-2,4)
        # With this orientation convention: d(I_2 Q)=-I_3(boundary Q).
        assert derivative=={key:-val for key,val in three.items()}
        assert cochain_d(three,3,-2,4)=={}
        cases.append(dict(dual_face=comp,primal_2_terms=len(two),primal_3_terms=len(three)))
    return cases


def witness_geometry():
    L=4;membership=defaultdict(set);classes=set();counts=[]
    for x in product(range(L),repeat=3):
        events=[]
        for axes in combinations(range(3),2):
            normal=next(i for i in range(3) if i not in axes)
            for offset in (0,1):
                y=list(x);y[normal]=(y[normal]+offset)%L
                events.append(('magnetic',tuple(y),axes))
                classes.add(('magnetic',axes))
        for mu in range(3):
            transverse=[i for i in range(3) if i!=mu]
            for offsets in product((0,1),repeat=2):
                y=list(x)
                for nu,offset in zip(transverse,offsets):y[nu]=(y[nu]+offset)%L
                events.append(('oscillation',tuple(y),(mu,)))
                classes.add(('oscillation',(mu,)))
        assert len(set(events))==18
        counts.append(len(events))
        for event in events:membership[event].add(x)
    multiplicities={kind:sorted(set(len(cells) for event,cells in membership.items()
                                  if event[0]==kind)) for kind in ('magnetic','oscillation')}
    assert multiplicities=={'magnetic':[2],'oscillation':[4]}
    return dict(L=L,cells=L**3,witnesses_per_cell=sorted(set(counts)),
                orientation_classes=len(classes),multiplicities=multiplicities,
                maximum_cells_per_witness=max(len(cells) for cells in membership.values()))


def numerical_constants():
    mp.mp.dps=80
    C0=3*mp.pi**2/16+12*(mp.mpf(1)/3-2/mp.pi**2)
    cases=[(mp.pi/3,mp.pi/(3*16*mp.sqrt(2)*mp.sqrt(1-mp.cos(mp.pi/6))),mp.mpf('.003')),
           (mp.mpf('.1'),mp.mpf('.05'),mp.mpf('.0002')),
           (mp.mpf('.1'),mp.mpf('.05'),mp.mpf('.0001'))]
    rows=[]
    for alpha,T,g in cases:
        cb=1-mp.cos(alpha/2)
        qb=min(1,mp.exp(-T*cb/g**2)+16*mp.exp(-alpha**2/(512*g**2*T)))
        qe=min(1,4*mp.exp(-alpha**2/(8*g**2*T)))
        eb=min(1,mp.exp(C0*T)*qb**mp.mpf('.25'))
        ee=min(1,mp.exp(C0*T)*qe**mp.mpf('.25'))
        exponent=mp.mpf(1)/12
        geometry=witness_geometry()
        assert exponent==mp.mpf(1)/(geometry['orientation_classes']*geometry['maximum_cells_per_witness'])
        p=min(1,18*max(eb,ee)**exponent)
        lambdas=[]
        for c in (0,1):
            term=lambda s:4096*(s+1)**8*80**(2*s-2)*p**s*mp.exp(c*s)
            cutoff=120
            partial=mp.fsum(term(s) for s in range(1,cutoff+1))
            # Consecutive ratios decrease with s. This gives an analytic
            # geometric bound on the entire positive tail after cutoff.
            ratio=80**2*p*mp.exp(c)*(mp.mpf(cutoff+3)/(cutoff+2))**8
            assert ratio<1
            tail=term(cutoff+1)/(1-ratio)
            lambdas.append(dict(c=c,partial=str(partial),tail_upper=str(tail),
                                upper=str(partial+tail),sufficient=bool(partial+tail<1)))
        rows.append(dict(alpha=str(alpha),T=str(T),g=str(g),bad_cell_upper=str(p),
                         lambda_bounds=lambdas))
    assert rows[0]['lambda_bounds'][1]['sufficient']
    assert not rows[1]['lambda_bounds'][1]['sufficient']
    assert rows[2]['lambda_bounds'][1]['sufficient']
    return rows


def main():
    start=time.monotonic()
    out=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope=__doc__,edge_fill=edge_fill_checks(),current_fill=cycles_and_duality(),
             hodge=hodge_checks(),witness_geometry=witness_geometry(),constants=numerical_constants(),
             status='PERSONAL_CHECKS_COMPLETED')
    out['elapsed_seconds']=time.monotonic()-start
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__':main()
