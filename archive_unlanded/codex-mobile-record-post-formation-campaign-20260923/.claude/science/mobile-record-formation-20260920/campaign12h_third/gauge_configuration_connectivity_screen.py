#!/usr/bin/env python3
"""Exhaustive basis connectivity for a specified finite boundary-flux model.

Exploration, not an all-volume or unmonitored quantum conclusion.
Matter is fixed by Gauss: q=-B m, m=1 for a flipped negative link from
the initially uniform positive electric field. Outside links stay fixed.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, deque
import hashlib, itertools, json

HERE = Path(__file__).resolve().parent


def geometry(shape):
    vertices = list(itertools.product(*(range(n) for n in shape)))
    index = {x:i for i,x in enumerate(vertices)}
    edges = []
    for a,x in enumerate(vertices):
        for d,n in enumerate(shape):
            if x[d]+1 < n:
                y = list(x); y[d] += 1
                edges.append((a,index[tuple(y)],d))
    lookup = {(a,d):e for e,(a,b,d) in enumerate(edges)}
    faces = []
    for a,x in enumerate(vertices):
        for d,f in itertools.combinations(range(len(shape)),2):
            if x[d]+1>=shape[d] or x[f]+1>=shape[f]: continue
            yd=list(x); yd[d]+=1; yf=list(x); yf[f]+=1
            b=index[tuple(yd)]; c=index[tuple(yf)]
            faces.append([(lookup[a,d],1),(lookup[b,f],1),
                          (lookup[c,d],-1),(lookup[a,f],-1)])
    return vertices,edges,faces


def inventory(shape):
    vertices,edges,faces=geometry(shape); V=len(vertices); E=len(edges)
    charge={}
    for mask in range(1<<E):
        q=[0]*V
        for e,(a,b,_) in enumerate(edges):
            if mask>>e&1: q[a]-=1; q[b]+=1
        if all(abs(x)<=1 for x in q): charge[mask]=tuple(q)
    births={}; hops={}; fields={}; cycles={}
    for mask,q in charge.items():
        births[mask]=[]; hops[mask]=set(); fields[mask]=set(); cycles[mask]=set()
        for e,(a,b,_) in enumerate(edges):
            new=mask^(1<<e)
            if q[a]==q[b]==0:
                assert new in charge
                assert sum(x!=0 for x in charge[new])==sum(x!=0 for x in q)+2
                births[mask].append((e,new))
            elif (q[a]==0)!=(q[b]==0) and new in charge:
                qnew=charge[new]
                if (qnew[a],qnew[b])==(q[b],q[a]): hops[mask].add(new)
        for face in faces:
            flip=sum(1<<e for e,_ in face); new=mask^flip
            if new in charge and charge[new]==q: fields[mask].add(new)
            for sense in (1,-1):
                oriented=face if sense==1 else [(e,-s) for e,s in reversed(face)]
                sites=[edges[e][0 if s==1 else 1] for e,s in oriented]
                if not all(q[a]!=0 for a in sites): continue
                if not all(1-2*((mask>>e)&1)==s*q[a] for (e,s),a in zip(oriented,sites)): continue
                target=list(q)
                for i,a in enumerate(sites): target[sites[(i+1)%4]]=q[a]
                assert new in charge and charge[new]==tuple(target)
                cycles[mask].add(new)
    for adjacency in (hops,fields,cycles):
        for u,vs in adjacency.items():
            for v in vs:
                assert u in adjacency[v]
                assert Counter(charge[u])==Counter(charge[v])
    return vertices,edges,faces,charge,births,hops,fields,cycles


def analyze(shape):
    vertices,edges,faces,charge,births,hops,fields,cycles=inventory(shape)
    V=len(vertices)
    results=[]
    for name,use_field,use_cycle in [('hop_only',False,False),
                                    ('hop_and_field_loops',True,False),
                                    ('hop_field_and_record_cycles',True,True)]:
        adjacency={u:hops[u]|(fields[u] if use_field else set())|
                   (cycles[u] if use_cycle else set()) for u in charge}
        component={}; groups=[]
        for start in charge:
            if start in component: continue
            i=len(groups); group=[]; queue=[start]; component[start]=i
            for u in queue:
                group.append(u)
                for v in adjacency[u]:
                    if v not in component: component[v]=i; queue.append(v)
            groups.append(group)
        bad=[]
        for i,g in enumerate(groups):
            n=sum(q!=0 for q in charge[g[0]])
            if n<V and not any(births[u] for u in g): bad.append(i)
        reached={0}; parent={}; queue=deque([0])
        while queue:
            u=queue.popleft()
            transitions=[('H',v) for v in adjacency[u]]+[('birth',v) for _,v in births[u]]
            for kind,v in transitions:
                if v not in reached:
                    reached.add(v); parent[v]=(u,kind); queue.append(v)
        reachable_bad=[i for i in bad if any(u in reached for u in groups[i])]
        witness=None
        if reachable_bad:
            i=reachable_bad[0]; u=next(u for u in groups[i] if u in reached)
            trace=[]; end=u
            while u:
                old,kind=parent[u]; trace.append(dict(kind=kind,input_mask=old,output_mask=u)); u=old
            trace.reverse()
            witness=dict(component_masks=groups[i],final_mask=end,final_charge=charge[end],
                         holes=[vertices[a] for a,q in enumerate(charge[end]) if q==0],
                         support_path_from_empty=trace)
        results.append(dict(model=name,components=len(groups),bad_nonfull_components=len(bad),
                            reachable_basis_states_from_empty=len(reached),
                            reachable_bad_components=len(reachable_bad),
                            bad_component_histogram=dict(Counter(
                                (sum(q==0 for q in charge[groups[i][0]]),len(groups[i])) for i in bad)),
                            witness=witness))
    # JSON cannot encode pair keys.
    for row in results:
        row['bad_component_histogram']={str(k):v for k,v in row['bad_component_histogram'].items()}
    return dict(shape=shape,vertices=vertices,oriented_edges=edges,plaquettes=faces,
                boundary='All external fields fixed at +1/2; outside matter absent; outside hopping/birth omitted.',
                full_link_basis=1<<len(edges),physical_basis_size=len(charge),
                physical_basis_by_record_count=dict(Counter(sum(q!=0 for q in v) for v in charge.values())),
                results=results)


if __name__=='__main__':
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope='Exact finite support graphs. Interpretation as quantum completion requires a separately justified monitoring/irreducibility theorem.',
                cases=[analyze((2,2,2)),analyze((2,2,3))])
    encoded=json.dumps(result,indent=2)+'\n'
    (HERE/'GAUGE_CONFIGURATION_CONNECTIVITY_SCREEN_RESULTS.json').write_text(encoded)
    print(encoded,end='')
