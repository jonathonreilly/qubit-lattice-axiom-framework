#!/usr/bin/env python3
"""Exact small geometry/control job for the analytic coercivity proof.

Price: <100 MB,<30 s. 1D torus interval geometry L5..64; rational graph
resistances on at most27 vertices. No N=3 many-body space is constructed.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from collections import Counter
from datetime import datetime,timezone
import json,time,resource
OUT=Path(__file__).resolve().parent
runtime=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (runtime/'STOP_REQUESTED.json').exists()
assert datetime.now(timezone.utc).timestamp()<json.loads((runtime/'DEADLINE.json').read_text())['deadline_epoch']
start=time.monotonic()
CR=448;OVERLAP=27;VOLCONST=2048
B=2*CR*OVERLAP*VOLCONST
assert B==49545216 and 2*B==99090432

partition_cases=0;max_vertex_overlap=0;max_edge_overlap=0
for L in range(5,65):
    V=L**3
    for q in range(1,L+1):
        if 4*q**3>V:break
        inner=[];expanded=[]
        for j in range(q):
            lo=j*L//q;hi=(j+1)*L//q
            I=list(range(lo,hi));inner.append(I)
            if q==1:C=list(range(L))
            else:C=[(lo-1+t)%L for t in range(min(L,len(I)+2))]
            assert len(set(C))==len(C)
            assert set(I)|{(x+1)%L for x in I}|{(x-1)%L for x in I} <= set(C)
            expanded.append(C)
        assert sorted(x for I in inner for x in I)==list(range(L))
        vc=Counter(x for C in expanded for x in C)
        ec=Counter(tuple(sorted((C[j],C[j+1]))) for C in expanded for j in range(len(C)-1))
        assert max(vc.values())<=3 and max(ec.values())<=3
        max_vertex_overlap=max(max_vertex_overlap,max(vc.values()))
        max_edge_overlap=max(max_edge_overlap,max(ec.values()))
        sizes=[len(C) for C in expanded]
        assert max(sizes)<=2*min(sizes)
        # Worst N in the range selecting this q is the strongest volume test.
        Nhi=min(V,4*(q+1)**3-1)
        assert max(sizes)**3*Nhi<=VOLCONST*V
        assert 2*q**3<=F(Nhi,2)
        partition_cases+=1

# Integer-spectrum diagonal bound used pointwise before conditional amplitudes.
for m in range(19):
    D=(m-1)*(m-2)//2
    assert D>=0 and 1<=D+m
for nbox in range(100):
    assert nbox*int(nbox>=3)>=nbox-2
    if nbox>=3:
        for removed_inside in range(3):assert nbox-removed_inside>=1

# Orthogonal channel projectors, checked without square-root normalization.
def mm(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
projection_rows=[]
for n in [3,4]:
    P=[[F(1,n) for _ in range(n)] for _ in range(n)]
    Q=[[F(i==j)-P[i][j] for j in range(n)] for i in range(n)]
    assert mm(P,P)==P and mm(Q,Q)==Q
    assert all(not v for row in mm(P,Q) for v in row)
    projection_rows.append({'internal_words':n,'singlet_rank':1,'orthogonal_rank':n-1})

# The elementary shell estimate in the resistance proof has no trig rounding.
for r in range(1,101):assert (r+1)**3-r**3<=7*r*r
assert F(32)*F(7,4)*8==CR

def inverse(A):
    n=len(A);M=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=next(i for i in range(k,n) if M[i][k]);M[k],M[p]=M[p],M[k]
        v=M[k][k];M[k]=[x/v for x in M[k]]
        for i in range(n):
            if i==k or not M[i][k]:continue
            v=M[i][k];M[i]=[x-v*y for x,y in zip(M[i],M[k])]
    return [row[n:] for row in M]
resistance_rows=[]
for shape in [(2,2,2),(2,2,3),(2,3,3),(3,3,3)]:
    sites=list(product(*(range(s) for s in shape)));idx={x:i for i,x in enumerate(sites)};n=len(sites)
    A=[[F(0) for _ in sites] for _ in sites]
    for x in sites:
        for j in range(3):
            if x[j]+1>=shape[j]:continue
            y=list(x);y[j]+=1;a=idx[x];b=idx[tuple(y)]
            A[a][a]+=1;A[b][b]+=1;A[a][b]-=1;A[b][a]-=1
    inv=inverse([row[1:] for row in A[1:]])
    def G(a,b):return inv[a-1][b-1] if a and b else F(0)
    resistance=max(G(a,a)+G(b,b)-2*G(a,b) for a,b in combinations(range(n),2))
    assert 0<resistance<CR
    resistance_rows.append({'shape':shape,'vertices':n,'max_effective_resistance':str(resistance)})

# Lattice pair incidences underlying the five constant amplitudes in ker H.
kernel_geometry=[]
for L in [5,6]:
    sites=list(product(range(L),repeat=3));words=Counter();norms=[F(0)]*5
    def pos(x,i,s):return tuple((x[k]+(s if k==i else 0))%L for k in range(3))
    plane_sign={}
    for x in sites:
        for i in range(3):words[('O',tuple(sorted((pos(x,i,1),pos(x,i,-1)))))]+=1
        for i,j in combinations(range(3),2):
            for si,sj in product([-1,1],repeat=2):
                key=('T',tuple(sorted((pos(x,i,si),pos(x,j,sj)))))
                words[key]+=1
                if key in plane_sign:assert plane_sign[key]==si*sj
                else:plane_sign[key]=si*sj
    assert {v for (kind,p),v in words.items() if kind=='O'}=={1}
    assert {v for (kind,p),v in words.items() if kind=='T'}=={2}
    kernel_geometry.append({'L':L,'constant_opposite_amplitudes':3,'opposite_sum_constraint':1,'constant_plane_amplitudes':3,'two_particle_kernel_dimension':5})

result={'partition_cases':partition_cases,'L_range':[5,64],'maximum_1d_vertex_overlap':max_vertex_overlap,'maximum_1d_free_edge_overlap':max_edge_overlap,'3d_overlap_bound':OVERLAP,'expanded_volume_constant':VOLCONST,'pinned_resistance_constant':CR,'coercivity_denominator':2*B,'projectors':projection_rows,'exact_resistance_controls':resistance_rows,'constant_pair_geometry':kernel_geometry,'elapsed_s':time.monotonic()-start,'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'coverage':'Exact geometry controls; the all-volume Poincare and operator coercivity proofs are analytic, not inferred from these finite cases.'}
(OUT/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
