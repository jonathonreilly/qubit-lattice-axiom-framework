#!/usr/bin/env python3
from pathlib import Path
from itertools import product,combinations,permutations
from fractions import Fraction as F
from collections import defaultdict
import json,hashlib,platform
import sympy as sp
import numpy as np

HERE=Path(__file__).resolve().parent
V=[(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
lookup={v:i for i,v in enumerate(V)}
columns=[(i,a,b) for i in range(3) for a,b in combinations(range(7),2)]
idx={c:n for n,c in enumerate(columns)}
def h(i,a,b):
    row=[0]*len(columns)
    if a!=b:row[idx[(i,min(a,b),max(a,b))]]=1 if a<b else -1
    return sp.Matrix(1,len(columns),row)
cycles=[]
for i in range(3):
    for a,b,c in combinations(range(7),3):cycles.append(h(i,a,b)+h(i,b,c)+h(i,c,a))
cycle_matrix=sp.Matrix.vstack(*cycles)
cycle_rank=cycle_matrix.rank();assert cycle_rank==45
rotations=[]
for perm in permutations(range(3)):
    for signs in product([-1,1],repeat=3):
        R=np.zeros((3,3),dtype=int)
        for i in range(3):R[perm[i],i]=signs[i]
        if round(np.linalg.det(R))==1:rotations.append(R)
assert len(rotations)==24
rows=list(cycles)
for R in rotations:
    states=[lookup[tuple(R@np.array(v))] for v in V]
    for i in range(3):
        direction=R[:,i];j=int(np.flatnonzero(direction)[0]);sign=int(direction[j])
        for a,b in combinations(range(7),2):rows.append(sign*h(j,states[a],states[b])-h(i,a,b))
M=sp.Matrix.vstack(*rows)
null=M.nullspace();assert len(null)==1
wanted=sp.Matrix([V[a][i]-V[b][i] for i,a,b in columns])
assert M*wanted==sp.zeros(M.rows,1)
ratio=next(null[0][k]/wanted[k] for k in range(len(columns)) if wanted[k]!=0)
assert null[0]==ratio*wanted

# Full three-site periodic color generators: each count is conserved.
states=list(product(range(7),repeat=3))
menus=[]
for drift in [F(-2,3),F(0),F(1),F(7,4)]:
    for symmetric_scale in [F(0),F(2,5)]:
        rate={}
        for a,b in product(range(7),repeat=2):
            antisym=drift*(V[a][0]-V[b][0])
            # Extra color-dependent symmetric rate, which does not affect
            # invariance or currents; this control need not be cubic covariant.
            rate[a,b]=max(antisym,F(0))+symmetric_scale*(1+(a+b)%3)
        balance=defaultdict(F)
        for s in states:
            for x in range(3):
                y=(x+1)%3;t=list(s);t[x],t[y]=t[y],t[x];t=tuple(t)
                if t!=s:balance[t]+=rate[s[x],s[y]];balance[s]-=rate[s[x],s[y]]
        assert all(balance[s]==0 for s in states)
        p=[F(k,28) for k in range(1,8)]
        g=sum(p[b]*V[b][0] for b in range(7))
        for a in range(7):
            actual=sum(p[a]*p[b]*(rate[a,b]-rate[b,a]) for b in range(7))
            assert actual==drift*p[a]*(V[a][0]-g)
        menus.append({'drift':str(drift),'symmetric_scale':str(symmetric_scale),'states':len(states)})
# Oriented color cycle has nonzero circulation; uniform products fail.
cycle_rate={(a,b):F(int((a,b) in {(1,2),(2,3),(3,1)})) for a,b in product(range(7),repeat=2)}
s=(1,2,3);outgoing=incoming=F(0)
for x in range(3):
    y=(x+1)%3
    outgoing+=cycle_rate[s[x],s[y]];incoming+=cycle_rate[s[y],s[x]]
assert outgoing==3 and incoming==0
result={'antisymmetric_coordinates':len(columns),'three_color_cycle_constraints':len(cycles),'cycle_rank':cycle_rank,'cycle_nullity':len(columns)-cycle_rank,'proper_cubic_rotations':len(rotations),'total_constraints':M.rows,'combined_rank':len(columns)-len(null),'combined_nullity':len(null),'basis_exactly_velocity_difference':True,'stationarity_menus':menus,'nonzero_cycle_stationarity_counterexample':{'configuration':[1,2,3],'incoming':str(incoming),'outgoing':str(outgoing)},'status':'primary algebraic classification checked; independent scrutiny pending','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'versions':{'python':platform.python_version(),'sympy':sp.__version__}}
text=json.dumps(result,indent=2)+'\n';(HERE/'PAIR_EXCHANGE_CLASSIFICATION_RESULTS.json').write_text(text);print(text,end='')
