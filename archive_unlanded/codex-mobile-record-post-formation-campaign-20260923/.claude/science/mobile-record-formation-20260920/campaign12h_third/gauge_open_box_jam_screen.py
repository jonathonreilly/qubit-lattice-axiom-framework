#!/usr/bin/env python3
"""Search and directly verify empty-accessible matching traps in open boxes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,itertools,json,sys
sys.dont_write_bytecode=True
from gauge_configuration_connectivity_screen import geometry

HERE=Path(__file__).resolve().parent


def screen(N):
    vertices,edges,faces=geometry((N,N,N));where={v:i for i,v in enumerate(vertices)}
    a=N//2-1;b=a+1;holes={where[(a,a,a)],where[(b,b,b)]};required={}
    for h in holes:
        for x,y,d in edges:
            if x==h:v,q=y,1
            elif y==h:v,q=x,-1
            else:continue
            assert v not in required or required[v]==q
            required[v]=q
    black=[i for i,x in enumerate(vertices) if sum(x)%2==0 and i not in holes]
    adj={x:[] for x in black}
    for e,(x,y,d) in enumerate(edges):
        if x in holes or y in holes:continue
        if required.get(x,-1)!=-1 or required.get(y,1)!=1:continue
        left,right=(x,y) if x in adj else (y,x)
        adj[left].append((right,e))
    match={}
    def augment(x,seen):
        for y,e in adj[x]:
            if y in seen:continue
            seen.add(y)
            if y not in match or augment(match[y][0],seen):
                match[y]=(x,e);return True
        return False
    for x in black:augment(x,set())
    chosen=sorted(e for x,e in match.values())
    out=dict(N=N,holes=[vertices[h] for h in sorted(holes)],matching_edges=len(chosen),
             needed_edges=(N**3-2)//2,matching_found=len(chosen)==(N**3-2)//2)
    if not out['matching_found']:return out
    q=[0]*len(vertices);mask=0
    for e in chosen:
        x,y,d=edges[e];assert q[x]==q[y]==0
        q[x]=-1;q[y]=1;mask|=1<<e
    assert all(q[v]==s for v,s in required.items())
    assert {v for v,x in enumerate(q) if x==0}==holes
    hop=[];birth=[];field=[]
    for e,(x,y,d) in enumerate(edges):
        delta=-(1-2*((mask>>e)&1))
        if q[x]==q[y]==0:birth.append(e)
        if (q[x]==0)!=(q[y]==0) and (q[x]+delta,q[y]-delta)==(q[y],q[x]):hop.append(e)
    for f,face in enumerate(faces):
        if len({(1-2*((mask>>e)&1))*s for e,s in face})==1:field.append(f)
    assert not hop and not birth and not field
    out.update(negative_edges=chosen,charge=q,ordinary_hops=hop,births=birth,field_plaquettes=field,
               exact_empty_birth_sequence=chosen,
               boundary='Fixed outside fields +1/2; no outside transitions; exact finite induced cubic box.')
    return out


if __name__=='__main__':
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             cases=[screen(N) for N in (4,6,8)])
    (HERE/'GAUGE_OPEN_BOX_JAM_SCREEN_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**out,'cases':[{k:v for k,v in c.items() if k not in {'negative_edges','charge','exact_empty_birth_sequence'}} for c in out['cases']]},indent=2))
