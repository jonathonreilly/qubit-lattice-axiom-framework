#!/usr/bin/env python3
"""Finite full-configuration controls for the proposed Gauss polymer proof.

These test the exact polymer mapping on three different overlap geometries,
including a branched balanced component, and control the analytic constants.
They do not replace the uniform cluster or thermodynamic-limit arguments.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json,math
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,condition,detail=None):
    assert bool(condition),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail))
    print('PASS:',name,flush=True)

def cycle_edges(vertices):
    edges=[]
    for a,b in zip(vertices,vertices[1:]+vertices[:1]):
        delta=tuple(b[i]-a[i] for i in range(3))
        assert sum(abs(v) for v in delta)==2 and sum(v!=0 for v in delta)==1
        axis=next(i for i in range(3) if delta[i])
        point=tuple((a[i]+b[i])//2 for i in range(3))
        edges.append((point,axis))
    return edges

first=[(0,0,0),(2,0,0),(2,2,0),(0,2,0)]
geometries={
    'shared_charge_edge':[first,[(0,0,0),(2,0,0),(2,0,2),(0,0,2)]],
    'shared_charge_vertex':[first,[(0,0,0),(-2,0,0),(-2,0,-2),(0,0,-2)]],
    'shared_physical_slot_distinct_axes':[first,[(1,-1,0),(1,1,0),(1,1,2),(1,-1,2)]],
}

def enumerate_shape(name,faces):
    edges=sorted(set(edge for face in faces for edge in cycle_edges(face)))
    endpoint=[]
    for point,axis in edges:
        endpoint.append((tuple(point[j]-int(j==axis) for j in range(3)),
                         tuple(point[j]+int(j==axis) for j in range(3))))
    vertices=sorted(set(p for ends in endpoint for p in ends))
    incidence=np.zeros((len(edges),len(vertices)),dtype=np.int16)
    for e,(a,b) in enumerate(endpoint):
        incidence[e,vertices.index(a)]=1;incidence[e,vertices.index(b)]=-1
    sites=sorted(set(p for p,i in edges))
    choices=[]
    for point in sites:
        at=[e for e,(p,i) in enumerate(edges) if p==point]
        choices.append([(None,0,0)]+[(e,species,sign) for e in at for species in (1,2) for sign in (-1,1)])
    valid=[];polynomial=Counter();assignments=0;batch=[]
    def consume(rows):
        nonlocal assignments
        assignments+=len(rows)
        a=np.zeros((len(rows),len(edges)),dtype=np.int16);b=a.copy()
        for r,row in enumerate(rows):
            for e,species,sign in row:
                if species==1:a[r,e]=sign
                elif species==2:b[r,e]=sign
        mask=np.all(a@incidence==0,axis=1)&np.all(b@incidence==0,axis=1)
        for r in np.flatnonzero(mask):
            configuration=tuple(sorted((e,species,sign) for e,species,sign in rows[r] if species))
            valid.append(configuration)
            polynomial[(np.count_nonzero(a[r]),np.count_nonzero(b[r]))]+=1
    for row in product(*choices):
        batch.append(row)
        if len(batch)==8192:consume(batch);batch=[]
    if batch:consume(batch)
    def components(configuration):
        remaining=set(configuration);answer=[]
        while remaining:
            seed=remaining.pop();component={seed};front=[seed]
            while front:
                e,species,sign=front.pop()
                adjacent={record for record in remaining if record[1]==species and set(endpoint[e])&set(endpoint[record[0]])}
                remaining-=adjacent;component|=adjacent;front.extend(adjacent)
            answer.append(tuple(sorted(component)))
        return tuple(sorted(answer))
    polymers=sorted({component for state in valid for component in components(state)})
    assert all(len(components(polymer))==1 for polymer in polymers)
    assert all(len(polymer)>=4 for polymer in polymers)
    def incompatibility(p,q,capacity=True,charge=True):
        if capacity and {edges[e][0] for e,_,_ in p}&{edges[e][0] for e,_,_ in q}:return True
        if charge and p[0][1]==q[0][1]:
            return bool({v for e,_,_ in p for v in endpoint[e]}&{v for e,_,_ in q for v in endpoint[e]})
        return False
    def collections(capacity=True,charge=True):
        ans=[]
        def recurse(start,selected):
            ans.append(tuple(selected))
            for j in range(start,len(polymers)):
                if all(not incompatibility(polymers[j],polymers[k],capacity,charge) for k in selected):
                    recurse(j+1,selected+[j])
        recurse(0,[]);return ans
    legal=collections();recovered=[]
    for family in legal:
        state=tuple(sorted(record for p in family for record in polymers[p]))
        assert components(state)==tuple(sorted(polymers[p] for p in family))
        recovered.append(state)
    assert len(recovered)==len(set(recovered)) and set(recovered)==set(valid)
    wrong_capacity=len(collections(capacity=False))
    wrong_components=len(collections(charge=False))
    return dict(shape=name,record_slots=len(sites),charge_edges=len(edges),assignments=assignments,
                valid_configurations=len(valid),polymers=len(polymers),compatible_collections=len(legal),
                partition_coefficients=[dict(nA=int(a),nB=int(b),coefficient=int(v)) for (a,b),v in sorted(polynomial.items())],
                without_capacity_collections=wrong_capacity,without_component_exclusion_collections=wrong_components,
                branched_balanced_polymers=sum(len(p)==8 for p in polymers))

outcomes=[]
for name,faces in geometries.items():
    result=enumerate_shape(name,faces);outcomes.append(result)
    check(name+'_full_configuration_polymer_bijection',True,result)
check('omitting_shared_midpoint_capacity_changes_partition',outcomes[2]['without_capacity_collections']>outcomes[2]['compatible_collections'])
check('omitting_same_species_vertex_exclusion_double_counts',outcomes[1]['without_component_exclusion_collections']>outcomes[1]['compatible_collections'] and outcomes[1]['branched_balanced_polymers']>0)

# Direct geometry of the anchor sets, with periodic indexing at two sizes.
for side in (7,9):
    origin=(0,0,0);axis=0
    ends=[tuple((sign*int(j==axis))%side for j in range(3)) for sign in (-1,1)]
    same_species=set()
    for vertex in ends:
        for j in range(3):
            for sign in (-1,1):
                midpoint=tuple((vertex[k]+sign*int(k==j))%side for k in range(3))
                same_species.add((midpoint,j,1))
    slot={(origin,j,species) for j in range(3) for species in (1,2)}
    assert len(same_species)==11 and len(slot)==6 and len(same_species|slot)==16
    assert len(same_species-{(origin,axis,1)})==10
check('edge_degree_and_incompatibility_anchor_counts',True,dict(edge_adjacency_degree=10,same_species_anchors=11,slot_anchors=6,union=16,bound_used=17))

q=s.symbols('q',positive=True)
bound=q**4/(100*(1-q))
check('uniform_enlarged_activity_KP_margin',bound.subs(q,s.Rational(1,2))==s.Rational(1,800) and 17*bound.subs(q,s.Rational(1,2))<1 and 6*bound.subs(q,s.Rational(1,2))<1,
      dict(z_star=1/(400*math.e**2),ordinary_margin='17/800',ghost_margin='6/800'))

k=s.Matrix(s.symbols('kx ky kz',real=True));a,b,c=s.symbols('a b c',real=True);k2=(k.T*k)[0]
tensor=s.Matrix(3,3,lambda i,j:a*k2+b*k[i]**2 if i==j else c*k[i]*k[j])
constraint=s.expand((tensor*k)[0])
equations=[constraint.coeff(k[0],3),constraint.coeff(k[0],1).coeff(k[1],2)]
solution=s.solve(equations,(b,c),dict=True)
check('cubic_quadratic_tensor_constrained_by_Gauss',solution==[{b:-a,c:-a}] and s.simplify(tensor.subs(solution[0])-a*(k2*s.eye(3)-k*k.T))==s.zeros(3))

# A nonzero constant covariance violates the leading analytic Gauss identity.
wrong=s.eye(3)
check('constant_covariance_negative_control',wrong*k!=s.zeros(3,1))
M=s.symbols('M',positive=True)
f=M*s.exp(-M/2)
check('spatial_weight_calculus',s.diff(f,M).subs(M,2)==0 and s.simplify(f.subs(M,2)-2/s.E)==0 and s.simplify(s.diff(f,M)/(s.exp(-M/2))-(1-M/2))==0)

report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Primary exact finite-configuration, combinatorial-constant and symbolic tensor controls. The general polymer/cluster proof and thermodynamic passage require separate mathematical reading.')
(HERE/'GAUSS_LOOP_POLYMER_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
