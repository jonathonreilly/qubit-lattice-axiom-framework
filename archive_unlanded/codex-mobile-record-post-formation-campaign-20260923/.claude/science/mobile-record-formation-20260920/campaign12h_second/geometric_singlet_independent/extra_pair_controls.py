#!/usr/bin/env python3
"""Small independent phase and antipodal-product controls; only own code imports."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from itertools import product,permutations
import json
import sympy as s
from quantum_core_check import physical_pair,singlet,pauli

OUT=Path(__file__).resolve().parent
phases=[s.I,-1,-s.I,-s.I]
common=s.prod(phases)
frames=[(s.Matrix([1,0]),s.Matrix([0,1])),
        (s.Matrix([s.Rational(3,5),4*s.I/5]),s.Matrix([4*s.I/5,s.Rational(3,5)]))]
rows=[]
for pairs in [[(0,1),(3,2)],[(0,2),(3,1)]]:
    plain=s.zeros(16,1);changed=s.zeros(16,1)
    for assignment in permutations(range(2)):
        for flips in product([0,1],repeat=2):
            vectors=[None]*4;rephased=[None]*4
            for key,flip,(black,white) in zip(assignment,flips,pairs):
                for site,sign in [(black,flip),(white,1-flip)]:
                    vectors[site]=frames[key][sign]
                    rephased[site]=phases[2*key+sign]*frames[key][sign]
            sign=(-1)**sum(flips)
            plain+=sign*s.kronecker_product(*reversed(vectors))
            changed+=sign*s.kronecker_product(*reversed(rephased))
    assert (changed-common*plain).applyfunc(s.simplify)==s.zeros(16,1)
    rows.append({'matching':pairs,'independently_rephased_record_vectors':4,'fiber_size':8,'common_phase':str(common)})
rho=s.zeros(4)
for axis in range(3):
    for sign in [-1,1]:
        n=s.zeros(3,1);n[axis]=sign;rho+=physical_pair(n)/6
expected=(s.eye(4)-sum((s.kronecker_product(x,x) for x in pauli),s.zeros(4))/3)/4
assert rho==expected and (singlet.H*rho*singlet)[0]==s.Rational(1,2)
assert rho.eigenvals()=={s.Rational(1,2):1,s.Rational(1,6):3}
result={'actual_individual_representative_phase_controls':rows,
        'six_axis_separable_product_mixture_spectrum':{'1/2':1,'1/6':3},
        'singlet_weight':'1/2','scope':'The six-axis mixture exactly realizes the uniform-sphere second-moment density. This is not a replacement for the tilted color ensemble.'}
target=OUT/'EXTRA_PAIR_RESULTS.json';assert not target.exists();target.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
