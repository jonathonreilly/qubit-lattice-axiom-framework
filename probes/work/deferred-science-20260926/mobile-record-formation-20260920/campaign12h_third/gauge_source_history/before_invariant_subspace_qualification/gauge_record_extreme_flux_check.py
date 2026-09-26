#!/usr/bin/env python3
"""Integer certificates of permanent pair birth from uniform link flux.

An augmenting-path matching search finds a witness; direct local checks, not
the search method, certify the result. No MILP feasibility claim is needed.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,itertools,json

HERE=Path(__file__).resolve().parent


def check(N):
    vertices=list(itertools.product(range(N),repeat=3));where={v:i for i,v in enumerate(vertices)}
    edges=[]
    for a,x in enumerate(vertices):
        for d in range(3):
            y=list(x);y[d]=(y[d]+1)%N;edges.append((a,where[tuple(y)],d))
    holes={where[(0,0,0)],where[(1,1,1)]};required={}
    for h in holes:
        for a,b,d in edges:
            if a==h:v,q=b,1
            elif b==h:v,q=a,-1
            else:continue
            assert v not in required or required[v]==q
            required[v]=q
    black=[a for a,x in enumerate(vertices) if sum(x)%2==0 and a not in holes]
    adj={a:[] for a in black}
    for e,(a,b,d) in enumerate(edges):
        if a in holes or b in holes:continue
        if required.get(a,-1)!=-1 or required.get(b,1)!=1:continue
        left,right=(a,b) if a in adj else (b,a)
        adj[left].append((right,e))
    match={}
    def augment(a,seen):
        for b,e in adj[a]:
            if b in seen:continue
            seen.add(b)
            if b not in match or augment(match[b][0],seen):match[b]=(a,e);return True
        return False
    for a in black:augment(a,set())
    chosen=sorted(e for a,e in match.values())
    assert len(chosen)==(len(vertices)-2)//2
    used=[v for e in chosen for v in edges[e][:2]]
    assert len(set(used))==len(used)==len(vertices)-2
    assert set(used)==set(range(len(vertices)))-holes
    bits=[1]*len(edges);charge=[0]*len(vertices)
    history=[]
    for e in chosen:
        a,b,d=edges[e]
        assert charge[a]==charge[b]==0 and bits[e]==1
        bits[e]=0;charge[a]-=1;charge[b]+=1;history.append((e,a,b))
    assert all(charge[v]==q for v,q in required.items())
    divergence=[0]*len(vertices)
    for bit,(a,b,d) in zip(bits,edges):
        divergence[a]+=bit;divergence[b]-=bit
    assert divergence==charge and sum(abs(q) for q in charge)==len(vertices)-2
    hop=[];birth=[]
    for e,(a,b,d) in enumerate(edges):
        change=1-2*bits[e];qa,qb=charge[a],charge[b]
        if qa==qb==0:birth.append(e)
        if (qa==0)!=(qb==0) and abs(qa+change)+abs(qb-change)==1:hop.append(e)
    assert not hop and not birth
    lookup={(a,d):e for e,(a,b,d) in enumerate(edges)};faces=[]
    for a,x in enumerate(vertices):
        for d,e in itertools.combinations(range(3),2):
            xd=list(x);xd[d]=(xd[d]+1)%N;xe=list(x);xe[e]=(xe[e]+1)%N
            face=[(lookup[(a,d)],1),(lookup[(where[tuple(xd)],e)],1),
                  (lookup[(where[tuple(xe)],d)],-1),(lookup[(a,e)],-1)]
            clockwise=[bits[j] if sign==1 else 1-bits[j] for j,sign in face]
            if len(set(clockwise))==1:faces.append(face)
    assert not faces
    return dict(N=N,vertices=len(vertices),edges=len(edges),vacancies=[vertices[h] for h in sorted(holes)],
                initial_flux='Every reference-positive oriented link has E=+1/2; all sites vacant.',
                final_negative_flux_edge_indices=chosen,final_charge=charge,
                birth_history=history,each_birth_verified=True,Gauss_law_exact=True,
                available_hop_edges=hop,available_birth_edges=birth,flippable_elementary_plaquettes=faces,
                negative_flux_count=len(chosen),record_count=len(vertices)-2,
                saturation='negative_flux_count = record_count/2')


def main():
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Exact finite certificates, not a size-uniform probability or native theory claim.',
             cases=[check(N) for N in (4,6,8)])
    (HERE/'GAUGE_RECORD_EXTREME_FLUX_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**out,'cases':[{k:v for k,v in row.items() if k not in {'final_charge','birth_history','final_negative_flux_edge_indices'}} for row in out['cases']]},indent=2))


if __name__=='__main__':main()
