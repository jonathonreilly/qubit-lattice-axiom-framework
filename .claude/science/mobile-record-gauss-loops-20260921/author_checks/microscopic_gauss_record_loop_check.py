#!/usr/bin/env python3
"""Exact local charge impulses and immutable loop transport/formation controls."""
from pathlib import Path
from itertools import product,permutations
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):
    assert bool(ok),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail))
    print('PASS:',name,flush=True)
N=7
axes=np.array([(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)],dtype=np.int64)
unit=np.eye(3,dtype=np.int64)
def div2(field):
    return sum(np.roll(field[...,i],-1,axis=i)-np.roll(field[...,i],1,axis=i) for i in range(3))
def field(points,features):
    out=np.zeros((N,N,N,3),dtype=np.int64)
    for point,feature in zip(points,features):out[tuple(np.asarray(point)%N)]+=feature
    return out

# Direct finite arrays, independently from the Fourier formula used below.
origin=np.array((3,3,3));grams=[]
for direction in range(3):
    target=origin+unit[direction]
    matrix=np.column_stack([div2(field((origin,target),(u,-u))).ravel() for u in unit])
    gram=matrix.T@matrix
    assert np.array_equal(gram,4*np.eye(3,dtype=np.int64))
    grams.append(gram.tolist())
check('nearest_neighbor_swap_centered_charge_Gram',True,grams)

features_e=np.vstack((np.zeros((1,3),dtype=np.int64),axes,np.zeros((8,3),dtype=np.int64)))
features_b=np.vstack((np.zeros((7,3),dtype=np.int64),np.array(list(product((-1,1),repeat=3)),dtype=np.int64)))
count=0
for a in range(15):
    for b in range(15):
        if a==b:continue
        for direction in range(3):
            points=(origin,origin+unit[direction]);de=features_e[b]-features_e[a];db=features_b[b]-features_b[a]
            qe=div2(field(points,(de,-de)));qb=div2(field(points,(db,-db)))
            norm=int(np.sum(qe*qe)+np.sum(qb*qb))
            assert norm==4*int(de@de+db@db) and norm>0
            count+=1
check('all_distinct_original_labels_have_nonzero_local_swap_impulse',True,dict(ordered_swaps_and_directions=count))

# Coordinates relative to center: bottom, right, top, left in the xy plane.
center=np.array((3,3,3))
points=np.array((center-unit[1],center+unit[0],center+unit[1],center-unit[0]))
values=np.array((unit[0],unit[1],-unit[0],-unit[1]))
loop=field(points,values)
check('axis_record_loop_has_exact_zero_centered_divergence',not np.any(div2(loop)))
reverse=field(points,values[[2,3,0,1]])
check('opposite_site_permutation_reverses_loop_without_charge',np.array_equal(reverse,-loop) and not np.any(div2(reverse)))
single=values.copy();single[[0,2]]=single[[2,0]]
check('one_half_of_collective_reversal_has_charge',np.any(div2(field(points,single))))

translations=[]
for direction in list(unit)+list(-unit):
    moved=points+direction
    assert set(map(tuple,points)).isdisjoint(set(map(tuple,moved)))
    changed=field(moved,values)-loop
    assert not np.any(div2(changed))
    assert np.all(np.sum(np.abs(moved-points),axis=1)==1)
    translations.append(direction.tolist())
check('all_six_atomic_parallel_nearest_neighbor_translations_preserve_charge',True,translations)

# Persistent identities demonstrate departure followed by fresh formation.
sites={};labels={}
for record,(point,value) in enumerate(zip(points,values)):
    sites[tuple(point)]=record;labels[record]=('A',tuple(value))
original=dict(labels)
for point in points:del sites[tuple(point)]
for record,point in enumerate(points+unit[2]):sites[tuple(point)]=record
assert not any(tuple(point) in sites for point in points)
for record,(point,value) in enumerate(zip(points,values),start=4):
    assert tuple(point) not in sites
    sites[tuple(point)]=record;labels[record]=('B',tuple(value))
E=np.zeros((N,N,N,3),dtype=np.int64);B=E.copy()
for point,record in sites.items():
    kind,value=labels[record]
    (E if kind=='A' else B)[point]=value
check('move_old_loop_and_form_new_loop_with_unique_immutable_record_ids',
      len(sites)==len(set(sites.values()))==len(labels)==8 and all(labels[k]==v for k,v in original.items())
      and not np.any(div2(E)) and not np.any(div2(B)),
      dict(old_records=4,new_records=4,occupied_sites=8,new_alphabet='vacancy plus six A axis and six B axis labels'))

# Cubic covariance of the centered divergence and the complete template family.
actions=0
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        R=np.zeros((3,3),dtype=np.int64)
        for col in range(3):R[perm[col],col]=signs[col]
        determinant=round(np.linalg.det(R))
        relative=points-center
        pp=np.array([center+R@r for r in relative]);polar=np.array([R@v for v in values]);axial=determinant*polar
        assert len(set(map(tuple,pp)))==4
        assert not np.any(div2(field(pp,polar))) and not np.any(div2(field(pp,axial)))
        assert sorted(map(tuple,polar))==sorted(map(tuple,axial))
        actions+=1
check('polar_and_axial_loop_templates_under_all_signed_cubic_actions',actions==48)

# Fourier form factor: field uses exp(-i k.x), D_centered has symbol i sin(k).
u,v=s.symbols('u v',real=True)
form=s.Matrix([2*s.I*s.sin(v),-2*s.I*s.sin(u),0])
symbol=s.Matrix([s.sin(u),s.sin(v),0])
check('exact_transverse_loop_Fourier_form_factor',s.simplify(symbol.dot(form))==0)
norm=s.simplify(sum(s.conjugate(a)*a for a in form))
check('loop_low_frequency_weight_is_order_k_squared',norm==4*s.sin(u)**2+4*s.sin(v)**2)

# Aggregate all three planes and both circulations per vector species.
sx,sy,sz,bet=s.symbols('sx sy sz beta',real=True)
wave=s.Matrix([sx,sy,sz]);birth=s.zeros(3)
for i,j in ((0,1),(0,2),(1,2)):
    direction=s.zeros(3,1);direction[i]=wave[j];direction[j]=-wave[i]
    birth+=8*bet*direction*direction.T
check('exact_empty_start_loop_birth_covariance',all(s.expand(x)==0 for x in birth-8*bet*(wave.dot(wave)*s.eye(3)-wave*wave.T)))

# Event permutation weight, for arbitrary positive homogeneous label weights.
p0,px,nx,py,ny=s.symbols('p0 px nx py ny',positive=True)
before=p0**4*px*nx*py*ny;after=ny*py*nx*px*p0**4
check('homogeneous_product_weight_preserved_by_translation_and_reversal',s.expand(before-after)==0)

k1,k2,k3,rate=s.symbols('k1 k2 k3 rate',real=True)
plane=s.exp(s.I*k1)+s.exp(-s.I*k1)+s.exp(s.I*k2)+s.exp(-s.I*k2)+s.exp(s.I*k3)+s.exp(-s.I*k3)-6
expected=-2*rate*((1-s.cos(k1))+(1-s.cos(k2))+(1-s.cos(k3)))
check('isolated_symmetric_loop_translation_symbol_is_diffusive',s.simplify(s.expand_complex(rate*plane)-expected)==0)

result=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Primary exact local constructions and a one-isolated-loop calculation. No independent review, hydrodynamic theorem, microscopic gauge derivation or physical electromagnetism claimed.')
(HERE/'MICROSCOPIC_GAUSS_RECORD_LOOP_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
