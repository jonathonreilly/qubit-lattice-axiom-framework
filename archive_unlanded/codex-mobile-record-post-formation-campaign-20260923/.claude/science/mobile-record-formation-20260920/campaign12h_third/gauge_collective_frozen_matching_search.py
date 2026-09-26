#!/usr/bin/env python3
"""MILP discovery screen for a matching trap with occupied cycles also absent.

Solver infeasibility or timeout is not promoted to a general theorem.
Any candidate is verified directly with integer local rules afterward.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,itertools,json,sys
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,milp
from scipy.sparse import lil_matrix
sys.dont_write_bytecode=True
from gauge_collective_record_cycle_check import geometry,divergence,hops,cycles

HERE=Path(__file__).resolve().parent


def search(N,limit=40):
    vertices,edges,faces=geometry(N);V=len(vertices);E=len(edges)
    where={v:i for i,v in enumerate(vertices)}
    holes={where[(0,0,0)],where[(1,1,1)]}
    constraints=[]
    def add(items,lo,hi):constraints.append((dict(items),lo,hi))
    for v in range(V):
        incident={e:1 for e,(a,b,d) in enumerate(edges) if v in (a,b)}
        add(incident,0 if v in holes else 1,0 if v in holes else 1)
        incoming={e:-1 for e,(a,b,d) in enumerate(edges) if b==v}
        incoming[E+v]=1;add(incoming,0,0)
    for h in holes:
        for a,b,d in edges:
            if a==h:v,value=b,1
            elif b==h:v,value=a,0
            else:continue
            add({E+v:1},value,value)
    # A matching can intersect a square in zero edges, one edge or either
    # opposite pair. Enumerate those patterns and forbid each compatible
    # occupied forward/reverse circulation by an exact Boolean nogood.
    patterns=[bits for bits in itertools.product((0,1),repeat=4)
              if all(not(bits[i] and bits[(i+1)%4]) for i in range(4))]
    for face in faces:
        sites=[edges[e][0 if s==1 else 1] for e,s in face]
        if any(v in holes for v in sites):continue
        for bits in patterns:
            for sense in (1,-1):
                assignment={e:bit for (e,s),bit in zip(face,bits)}
                for i,((e,s),bit) in enumerate(zip(face,bits)):
                    if sense==1:v=sites[i];q=s*(1-2*bit)
                    else:v=sites[(i+1)%4];q=-s*(1-2*bit)
                    assignment[E+v]=(q+1)//2
                # sum_{a=0}x + sum_{a=1}(1-x)>=1.
                ones=sum(assignment.values())
                add({v:(1 if a==0 else -1) for v,a in assignment.items()},1-ones,np.inf)
    A=lil_matrix((len(constraints),E+V),dtype=float)
    for i,(row,lo,hi) in enumerate(constraints):
        for j,c in row.items():A[i,j]=c
    started=datetime.now(timezone.utc).isoformat()
    res=milp(np.zeros(E+V),integrality=np.ones(E+V),bounds=Bounds(0,1),
             constraints=LinearConstraint(A.tocsr(),[x[1] for x in constraints],[x[2] for x in constraints]),
             options={'time_limit':limit,'mip_rel_gap':0.0})
    out=dict(N=N,variables=E+V,constraints=len(constraints),started_utc=started,
             completed_utc=datetime.now(timezone.utc).isoformat(),
             time_limit_seconds=limit,solver_status=int(res.status),solver_message=res.message,
             scope='Only the specified minimal-flux matching sector and two fixed holes; no coherent dark-state or arbitrary-state exclusion.')
    if res.x is None:return out
    candidate=np.rint(res.x).astype(int)
    for row,lo,hi in constraints:
        value=sum(c*int(candidate[j]) for j,c in row.items())
        assert lo<=value<=hi
    bits=tuple(1-int(x) for x in candidate[:E])
    q=divergence(bits,edges,V);state=(bits,q)
    assert {v for v,x in enumerate(q) if not x}==holes
    assert all(abs(x)<=1 for x in q)
    hp=list(hops(state,edges));cy=list(cycles(state,edges,faces))
    births=[e for e,(a,b,d) in enumerate(edges) if q[a]==q[b]==0]
    fields=[i for i,face in enumerate(faces) if len({s*(2*bits[e]-1) for e,s in face})==1]
    assert not hp and not cy and not births and not fields
    out.update(direct_integer_verification=True,negative_edges=[e for e,b in enumerate(bits) if not b],
               charges=q,holes=[vertices[v] for v in sorted(holes)],
               hopping_count=len(hp),birth_count=len(births),field_loop_count=len(fields),record_cycle_count=len(cy))
    return out


if __name__=='__main__':
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             cases=[search(4),search(6)])
    encoded=json.dumps(out,indent=2)+'\n'
    (HERE/'GAUGE_COLLECTIVE_FROZEN_MATCHING_SEARCH_RESULTS.json').write_text(encoded)
    print(encoded,end='')
