#!/usr/bin/env python3
"""Find and exactly verify optional birth-reachable frozen gauge states."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from gauge_record_orientation_screen import geometry,validate

HERE=Path(__file__).resolve().parent


def attempt(free_charges,no_faces):
    vertices,edges,B,faces=geometry(4);V,E=len(vertices),len(edges)
    holes={vertices.index((0,0,0)),vertices.index((1,1,1))}
    eligible=[e for e,(a,b,d) in enumerate(edges) if a not in holes and b not in holes]
    M=len(eligible);dim=E+V+M
    rows=[];lo=[];hi=[]
    def add(coeff,lower,upper):
        row=np.zeros(dim,dtype=np.int64)
        for j,c in coeff:row[j]+=c
        rows.append(row);lo.append(lower);hi.append(upper)
    for v in range(V):
        coeff=[(e,int(B[v,e])) for e in np.flatnonzero(B[v])]
        if v not in holes:coeff.append((E+v,-2))
        add(coeff,0 if v in holes else -1,0 if v in holes else -1)
    for e,(a,b,d) in enumerate(edges):
        if a in holes:
            assert b not in holes
            add([(e,1),(E+b,-1)],0,0)
        elif b in holes:
            add([(e,1),(E+a,1)],1,1)
    for v in range(V):
        coeff=[(E+V+j,1) for j,e in enumerate(eligible) if v in edges[e][:2]]
        add(coeff,0 if v in holes else 1,0 if v in holes else 1)
    for j,e in enumerate(eligible):
        a,b,d=edges[e];m=E+V+j
        # If selected as a final birth edge, q_a=2 bit-1, q_b=1-2 bit.
        add([(m,1),(E+a,1),(e,-1)],-np.inf,1)
        add([(m,1),(E+a,-1),(e,1)],-np.inf,1)
        add([(m,1),(E+b,1),(e,1)],-np.inf,2)
        add([(m,1),(E+b,-1),(e,-1)],-np.inf,0)
    if no_faces:
        for cycle in faces:add(cycle,-1,1)
    lower=np.zeros(dim);upper=np.ones(dim)
    for v in holes:upper[E+v]=0
    if not free_charges:
        for v,x in enumerate(vertices):
            if v not in holes:lower[E+v]=upper[E+v]=int(sum(x)%4<2)
    result=milp(c=np.zeros(dim),integrality=np.ones(dim),bounds=Bounds(lower,upper),
                constraints=LinearConstraint(np.array(rows),np.array(lo),np.array(hi)),
                options={'time_limit':30.0})
    out=dict(free_charges=free_charges,no_faces_required=no_faces,status=int(result.status),message=result.message)
    if result.x is None:return out
    bits=np.rint(result.x[:E]).astype(np.int64)
    charge=2*np.rint(result.x[E:E+V]).astype(np.int64)-1
    for v in holes:charge[v]=0
    selected=[eligible[j] for j in range(M) if result.x[E+V+j]>.5]
    assert len(selected)==31
    used=[]
    start=bits.copy()
    for e in selected:
        a,b,d=edges[e];used.extend((a,b))
        assert charge[a]==2*bits[e]-1 and charge[b]==1-2*bits[e]
        start[e]=1-start[e]
    assert len(set(used))==62 and set(used)==set(range(V))-holes
    assert np.array_equal(B@start,np.zeros(V,dtype=np.int64))
    # Reconstruct every birth rather than infer reachability from final constraints.
    now=start.copy();qnow=B@now
    for e in selected:
        a,b,d=edges[e];assert qnow[a]==qnow[b]==0
        before=qnow.copy();now[e]=1-now[e];qnow=B@now
        assert abs(qnow[a])==abs(qnow[b])==1 and qnow[a]==-qnow[b]
        assert all(qnow[v]==before[v] for v in range(V) if v not in (a,b))
    assert np.array_equal(now,bits) and np.array_equal(qnow,charge)
    cert=validate(vertices,edges,B,faces,bits,charge)
    assert not cert['available_birth_edges'] and not cert['available_hop_edges']
    if no_faces:assert not cert['flippable_plaquettes']
    rescues=[]
    for f in cert['flippable_plaquettes']:
        trial=bits.copy()
        for e,sign in faces[f]:trial[e]=1-trial[e]
        test=validate(vertices,edges,B,faces,trial,charge)
        if test['available_hop_edges']:rescues.append(dict(face=f,new_hop_edges=test['available_hop_edges']))
    out.update(bits=bits.tolist(),charge=charge.tolist(),birth_matching_edges=selected,
               all_vacant_initial_flux=start.tolist(),every_birth_checked_exactly=True,certificate=cert,
               single_face_rescues=rescues,max_integer_rounding_error=float(np.max(abs(result.x-np.rint(result.x)))))
    return out


def main():
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             geometry_source_sha256=hashlib.sha256((HERE/'gauge_record_orientation_screen.py').read_bytes()).hexdigest(),
             scope='Finite N4 supplied gauge model. MILP finds witnesses only; returned arrows and births checked exactly. Infeasible/time limits are not proofs.',attempts=[])
    for args in [(False,False),(False,True),(True,True)]:
        result=attempt(*args);out['attempts'].append(result)
        (HERE/'GAUGE_RECORD_REACHABLE_JAM_SCREEN_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in result.items() if k not in {'bits','charge','all_vacant_initial_flux'}}),flush=True)


if __name__=='__main__':main()
