#!/usr/bin/env python3
"""Enumerate all four-edge currents, then check dilute covariance coefficients.

The walk enumeration does not use the four-record template list. Floating
Fourier comparisons are numerical controls; graph constraints/counts are exact.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):
    assert bool(ok),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail))
    print('PASS:',name,flush=True)

N=7;V=N**3
steps=tuple(tuple(sign*int(axis==j) for j in range(3)) for axis in range(3) for sign in (-1,1))
add=lambda a,b,mult=1:tuple((a[j]+mult*b[j])%N for j in range(3))
loops=set();short_counts=Counter()
for start in product(range(N),repeat=3):
    for first in steps:
        one=add(start,first,2)
        for second in steps:
            two=add(one,second,2)
            if two==start:continue
            for third in steps:
                three=add(two,third,2)
                if three in (start,one):continue
                final=[step for step in steps if add(three,step,2)==start]
                for fourth in final:
                    vertices=(start,one,two,three)
                    directions=(first,second,third,fourth)
                    records=tuple(sorted((*add(vertex,step),*step) for vertex,step in zip(vertices,directions)))
                    assert len({row[:3] for row in records})==4
                    loops.add(records)
check('all_four_edge_signed_current_configurations',len(loops)==6*V,dict(side=N,configurations=len(loops),per_site=len(loops)//V))

label_counts=Counter();site_label_counts=Counter()
for loop in loops:
    charge=Counter();total=np.zeros(3,dtype=np.int64)
    for row in loop:
        point=row[:3];direction=row[3:]
        charge[add(point,direction,-1)]+=1
        charge[add(point,direction,1)]-=1
        total+=np.asarray(direction)
        label_counts[direction]+=1;site_label_counts[(point,direction)]+=1
    assert all(value==0 for value in charge.values())
    assert not np.any(total)
check('each_enumerated_configuration_is_Gauss_free_and_has_zero_total_vector',True)
check('isotropic_single_label_fugacity_coefficient',set(site_label_counts.values())=={4} and len(site_label_counts)==6*V,
      dict(per_site_per_axis_label=4,density_per_orbit=24,two_orbit_total=48))

# Compare the direct walk enumeration with the compact form-factor prediction.
numeric=[]
for mode in ((0,0,0),(1,0,0),(1,1,0),(1,1,1),(2,1,0)):
    k=2*np.pi*np.asarray(mode)/N;cov=np.zeros((3,3),dtype=np.complex128)
    for loop in loops:
        positions=np.array([row[:3] for row in loop]);features=np.array([row[3:] for row in loop])
        transform=np.sum(features*np.exp(-1j*(positions@k))[:,None],axis=0)
        cov+=np.outer(transform,transform.conj())/V
    sine=np.sin(k);target=8*(np.dot(sine,sine)*np.eye(3)-np.outer(sine,sine))
    error=float(np.max(np.abs(cov-target)))
    assert error<3e-12,(mode,error)
    numeric.append(dict(mode=mode,maximum_error=error))
check('enumerated_order_four_vector_covariance',True,numeric)

# Single-slot phase factor: vacancy plus exactly one of twelve labels.
ta=s.symbols('a1:4',real=True);tb=s.symbols('b1:4',real=True)
za,zb=s.symbols('zA zB',real=True,nonnegative=True)
factor=1+za*sum(s.exp(s.I*t)+s.exp(-s.I*t) for t in ta)+zb*sum(s.exp(s.I*t)+s.exp(-s.I*t) for t in tb)
target=1+2*za*sum(s.cos(t) for t in ta)+2*zb*sum(s.cos(t) for t in tb)
check('one_record_capacity_compact_phase_factor',s.simplify(s.expand_complex(factor)-target)==0)
minimum=s.simplify(target.subs({t:s.pi for t in (*ta,*tb)}))
check('positive_factor_sufficient_bound_and_explicit_sign_witness',minimum==1-6*(za+zb) and minimum.subs({za:s.Rational(1,10),zb:s.Rational(1,10)})<0)

result=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Finite-volume Taylor coefficient identities and one-site compact-phase algebra. No uniform cluster expansion, thermodynamic phase or Markov mixing claim.')
(HERE/'GAUSS_LOOP_FUGACITY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
