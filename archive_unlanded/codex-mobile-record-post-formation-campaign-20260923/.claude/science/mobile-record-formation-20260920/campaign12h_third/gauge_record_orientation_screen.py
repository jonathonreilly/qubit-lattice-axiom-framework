#!/usr/bin/env python3
"""Exploratory integer certificate search; supplied spin-half gauge model.

MILP is used only to find finite arrow configurations. Every returned bit
configuration is then checked using integer arithmetic and actual move rules.
No infeasible/timeout status is promoted to an analytic obstruction.
"""
from pathlib import Path
from datetime import datetime,timezone
import itertools,json,hashlib
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint

HERE=Path(__file__).resolve().parent


def geometry(N):
    vertices=list(itertools.product(range(N),repeat=3));where={v:i for i,v in enumerate(vertices)}
    step=lambda x,d:tuple((x[a]+int(a==d))%N for a in range(3))
    edges=[(where[x],where[step(x,d)],d) for x in vertices for d in range(3)]
    lookup={(a,d):i for i,(a,b,d) in enumerate(edges)}
    B=np.zeros((len(vertices),len(edges)),dtype=np.int64)
    for e,(a,b,d) in enumerate(edges):B[a,e]=1;B[b,e]=-1
    faces=[]
    for x in vertices:
        for d,e in itertools.combinations(range(3),2):
            faces.append([(lookup[(where[x],d)],1),
                          (lookup[(where[step(x,d)],e)],1),
                          (lookup[(where[step(x,e)],d)],-1),
                          (lookup[(where[x],e)],-1)])
    return vertices,edges,B,faces


def validate(vertices,edges,B,faces,bits,charge):
    assert set(map(int,bits))<=set((0,1))
    assert np.array_equal(B@bits,charge)
    assert abs(charge).max()<=1 and sum(charge)==0
    births=[];moves=[];plaquettes=[]
    for e,(a,b,d) in enumerate(edges):
        change=1-2*int(bits[e])
        qa,qb=int(charge[a]),int(charge[b])
        ra,rb=qa+change,qb-change
        if qa==qb==0:
            assert ra==-rb and abs(ra)==1;births.append(e)
        if (qa==0)!=(qb==0) and abs(ra)+abs(rb)==1:
            assert sorted((qa,qb))==sorted((ra,rb));moves.append(e)
    for f,cycle in enumerate(faces):
        along=[int(bits[e]) if sign==1 else 1-int(bits[e]) for e,sign in cycle]
        if len(set(along))==1:plaquettes.append(f)
    return dict(vacancies=[vertices[i] for i,q in enumerate(charge) if q==0],
                available_birth_edges=births,available_hop_edges=moves,
                flippable_plaquettes=plaquettes,charge_counts={str(q):int(sum(charge==q)) for q in (-1,0,1)},
                Gauss_law_integer_residual_zero=True)


def attempt(no_plaquettes):
    N=4;vertices,edges,B,faces=geometry(N);where={v:i for i,v in enumerate(vertices)}
    charge=np.array([1 if sum(v)%4<2 else -1 for v in vertices],dtype=np.int64)
    holes=[where[(0,0,0)],where[(2,0,0)]]
    for v in holes:charge[v]=0
    lower=np.zeros(len(edges));upper=np.ones(len(edges))
    fixed=[]
    for e,(a,b,d) in enumerate(edges):
        if charge[a]==0 or charge[b]==0:
            assert not charge[a]==charge[b]==0
            # Flipping an edge changes q_a by 1-2 bit and q_b oppositely.
            # Choose its orientation so the vacancy's neighbor could not move.
            allowed=[]
            for bit in (0,1):
                change=1-2*bit;ra,rb=int(charge[a])+change,int(charge[b])-change
                if not(abs(ra)+abs(rb)==1):allowed.append(bit)
            assert len(allowed)==1
            lower[e]=upper[e]=allowed[0];fixed.append(e)
    mats=[B];lo=[charge];hi=[charge]
    if no_plaquettes:
        F=np.zeros((len(faces),len(edges)),dtype=np.int64)
        for f,cycle in enumerate(faces):
            for e,sign in cycle:F[f,e]=sign
        # Two oppositely traversed edges contribute a constant two.
        mats.append(F);lo.append(-np.ones(len(faces)));hi.append(np.ones(len(faces)))
    result=milp(c=np.zeros(len(edges)),integrality=np.ones(len(edges)),bounds=Bounds(lower,upper),
                constraints=LinearConstraint(np.vstack(mats),np.concatenate(lo),np.concatenate(hi)),
                options={'time_limit':30.0})
    out=dict(no_plaquettes_required=no_plaquettes,status=int(result.status),message=result.message,
             vertices=len(vertices),edges=len(edges),fixed_incident_hole_edges=fixed,
             charge=charge.tolist(),solver_only_discovery=True)
    if result.x is not None:
        bits=np.rint(result.x).astype(np.int64)
        out['max_rounding_error']=float(np.max(np.abs(result.x-bits)))
        out['bits']=bits.tolist();out['certificate']=validate(vertices,edges,B,faces,bits,charge)
        assert not out['certificate']['available_birth_edges']
        assert not out['certificate']['available_hop_edges']
        if no_plaquettes:assert not out['certificate']['flippable_plaquettes']
    return out


def main():
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             scope='Finite supplied spin-half link flux and charges -1,0,+1. No native model or photon-phase claim.',
             attempts=[])
    for value in (False,True):
        out['attempts'].append(attempt(value));print(json.dumps(out['attempts'][-1]),flush=True)
        (HERE/'GAUGE_RECORD_ORIENTATION_SCREEN_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
