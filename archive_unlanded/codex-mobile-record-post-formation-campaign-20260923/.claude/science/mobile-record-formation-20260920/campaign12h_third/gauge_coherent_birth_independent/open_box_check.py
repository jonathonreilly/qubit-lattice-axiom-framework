#!/usr/bin/env python3
"""Exhaustive integer physical-basis / vacancy-hop component check."""
from collections import Counter
from itertools import product
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent


def box(lengths):
    vertices=list(product(*(range(n) for n in lengths)))
    index={v:i for i,v in enumerate(vertices)}
    edges=[]
    for x in vertices:
        for axis in range(3):
            if x[axis]+1<lengths[axis]:
                y=list(x);y[axis]+=1
                edges.append((index[x],index[tuple(y)]))
    return vertices,edges


def enumerate_physical(vertices,edges):
    # Relative to every internal and exterior reference link being positive,
    # flipping an internal bit 1->0 contributes -1 at its tail, +1 at its head.
    q=[0]*len(vertices)
    for x,y in edges:q[x]-=1;q[y]+=1
    bad=sum(abs(v)>1 for v in q)
    records={}
    previous=0
    for step in range(1<<len(edges)):
        mask=step^(step>>1)
        if step:
            edge=(step & -step).bit_length()-1
            x,y=edges[edge]
            delta=1 if mask & (1<<edge) else -1
            bad-=int(abs(q[x])>1)+int(abs(q[y])>1)
            q[x]+=delta;q[y]-=delta
            bad+=int(abs(q[x])>1)+int(abs(q[y])>1)
            assert mask^previous == 1<<edge
        if not bad:
            assert sum(q)==0
            records[mask]=tuple(q)
        previous=mask
    return records


def analyze(lengths):
    started=time.monotonic()
    vertices,edges=box(lengths)
    states=enumerate_physical(vertices,edges)
    masks=sorted(states);index={b:i for i,b in enumerate(masks)}
    parent=list(range(len(masks)));sizes=[1]*len(masks)
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]];a=parent[a]
        return a
    def merge(a,b):
        a,b=find(a),find(b)
        if a==b:return
        if sizes[a]<sizes[b]:a,b=b,a
        parent[b]=a;sizes[a]+=sizes[b]
    direct_crosschecks=0
    hop_edges=0;birth_arcs=0;max_hazard=0
    hazards={}
    for mask in masks:
        q=states[mask];hazard=0
        if len(edges)<=12 or mask%97==0:
            direct=[0]*len(vertices)
            for e,(x,y) in enumerate(edges):
                if not mask&(1<<e):direct[x]-=1;direct[y]+=1
            assert tuple(direct)==q;direct_crosschecks+=1
        for e,(x,y) in enumerate(edges):
            delta=1-2*int(bool(mask&(1<<e)))
            other=mask^(1<<e)
            if q[x]==q[y]==0:
                assert other in states
                target=states[other]
                assert sum(v==0 for v in target)==sum(v==0 for v in q)-2
                hazard+=1;birth_arcs+=1
            elif (q[x]==0) != (q[y]==0):
                if (q[x]+delta,q[y]-delta)==(q[y],q[x]):
                    assert other in states
                    expected=list(q);expected[x],expected[y]=expected[y],expected[x]
                    assert states[other]==tuple(expected)
                    if mask<other:
                        merge(index[mask],index[other]);hop_edges+=1
        hazards[mask]=hazard;max_hazard=max(max_hazard,hazard)
    components={}
    for mask in masks:
        r=find(index[mask])
        row=components.setdefault(r,dict(holes=states[mask].count(0),size=0,
            active_configurations=0,max_hazard=0,representative=mask))
        assert states[mask].count(0)==row['holes'] and row['holes']%2==0
        row['size']+=1;row['active_configurations']+=int(hazards[mask]>0)
        row['max_hazard']=max(row['max_hazard'],hazards[mask])
    assert sum(r['size'] for r in components.values())==len(states)
    nonfull=[r for r in components.values() if r['holes']>=2]
    misses=[r for r in nonfull if r['active_configurations']==0]
    hist=Counter((r['holes'],r['size'],r['active_configurations'],r['max_hazard']) for r in components.values())
    return dict(lengths=lengths,vertices=len(vertices),edges=len(edges),
        bit_strings_exhaustively_scanned=1<<len(edges),physical_basis_states=len(states),
        independent_direct_charge_crosschecks=direct_crosschecks,
        undirected_hop_edges=hop_edges,directed_birth_arcs=birth_arcs,
        total_components=len(components),nonfull_components=len(nonfull),
        every_nonfull_hop_component_contains_positive_loss=not misses,
        maximum_vacant_edge_count=max_hazard,
        component_histogram=[dict(holes=k[0],size=k[1],active_configurations=k[2],max_hazard=k[3],multiplicity=v) for k,v in sorted(hist.items())],
        failing_components=misses,
        runtime_seconds=time.monotonic()-started)


if __name__=='__main__':
    result={'method':'All link bit strings; exact integer Gauss charges with frozen positive exterior; complete legal vacancy-hop graph.',
            'cases':[analyze((2,2,2)),analyze((2,2,3))]}
    (HERE/'OPEN_BOX_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
