#!/usr/bin/env python3
"""Finite character and covariant-carrier controls; not a substitute for Schur's lemma."""
from pathlib import Path
from itertools import permutations, product
import hashlib, json
import numpy as np
import sympy as s
from scipy.spatial.transform import Rotation

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,condition,detail=None):
    assert bool(condition),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)

perms=list(permutations(range(4)))
pairings=[frozenset((frozenset((0,1)),frozenset((2,3)))),
          frozenset((frozenset((0,2)),frozenset((1,3)))),
          frozenset((frozenset((0,3)),frozenset((1,2))))]
characters=[]
classes={}
for p in perms:
    parity=(-1)**sum(p[a]>p[b] for a in range(4) for b in range(a+1,4))
    standard=sum(p[i]==i for i in range(4))-1
    E=sum(frozenset(frozenset(p[i] for i in pair) for pair in pairing)==pairing for pairing in pairings)-1
    row=[1,parity,E,parity*standard,standard]
    characters.append(row)
    used=set(); cycles=[]
    for i in range(4):
        if i in used:continue
        q=i;length=0
        while q not in used:used.add(q);length+=1;q=p[q]
        cycles.append(length)
    key=tuple(sorted(cycles,reverse=True));classes.setdefault(key,[]).append(row)
characters=s.Matrix(characters)
check('all_S4_character_inner_products',characters.T*characters==24*s.eye(5))
check('complete_dimension_square_sum',sum(q*q for q in [1,1,2,3,3])==24)
expected={(1,1,1,1):(1,[1,1,2,3,3]),(2,1,1):(6,[1,-1,0,-1,1]),
          (2,2):(3,[1,1,2,-1,-1]),(3,1):(8,[1,1,-1,0,0]),(4,):(6,[1,-1,0,1,-1])}
check('class_table_from_actual_permutations',all(len(classes[k])==n and all(q==row for q in classes[k]) for k,(n,row) in expected.items()))
# Dimension2 remainders: E, 1+1, 1+sign, sign+sign.
remainder_transposition=[0,2,0,-2]
check('only_two_trivial_remainder_has_nonnegative_Ad_character',
      [i for i,value in enumerate(remainder_transposition) if -1+value>=0]==[1])

sigma=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
eye=np.eye(2);zero=np.zeros((2,2))
def spin(v):return np.einsum('i,ijk->jk',v,sigma)
def block(a,b):return np.block([[a,zero],[zero,b]])
features=[(sign*np.eye(3)[i],np.zeros(3)) for i in range(3) for sign in (-1,1)]
features += [(np.zeros(3),np.array(signs)) for signs in product((-1,1),repeat=3)]
lookup={tuple(np.r_[e,b].astype(int)):a for a,(e,b) in enumerate(features)}
j=.7
states=[block((eye+spin(e))/2,zero) if a<6 else block(zero,(eye+spin(b)/np.sqrt(3))/2) for a,(e,b) in enumerate(features)]
effects=[block((eye+j*spin(e))/14,eye/14) if a<6 else block(eye/14,(eye+j*np.sqrt(3)*spin(b)/4)/14) for a,(e,b) in enumerate(features)]
worst=0.;rotations=0
for p in permutations(range(3)):
    parity=(-1)**sum(p[a]>p[b] for a in range(3) for b in range(a+1,3))
    for signs in product((-1,1),repeat=3):
        if parity*np.prod(signs)!=1:continue
        Q=np.zeros((3,3),int)
        for col in range(3):Q[p[col],col]=signs[col]
        quaternion=Rotation.from_matrix(Q).as_quat()
        u=quaternion[3]*eye-1j*spin(quaternion[:3])
        U=block(u,u)
        for a,(e,b) in enumerate(features):
            mapped=lookup[tuple(np.r_[Q@e,Q@b].astype(int))]
            for objects in (states,effects):
                worst=max(worst,float(np.max(abs(U@objects[a]@U.conj().T-objects[mapped]))))
        rotations+=1
check('four_dimensional_states_and_effects_covariant_under_all_proper_cubic_rotations',rotations==24 and worst<3e-14,dict(rotations=rotations,maximum_residual=worst))

report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Finite S4 character table and all24 positive carrier covariance checks. The projective-commutant argument remains a proof obligation for independent review.')
(HERE/'FOURTEEN_LABEL_CUBIC_CARRIER_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
