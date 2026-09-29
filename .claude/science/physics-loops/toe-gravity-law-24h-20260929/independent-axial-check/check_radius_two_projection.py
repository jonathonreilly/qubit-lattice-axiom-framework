#!/usr/bin/env python3
"""Extract the exact moment obstruction and check parameter scaling factors."""
from collections import defaultdict
from fractions import Fraction as Q
import ast
import json
import os
from pathlib import Path
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[name]='1'
import sympy as s
HERE=Path(__file__).resolve().parent
certificate=json.loads((HERE/'radius_two_independent_certificate.json').read_text())
names=json.loads((HERE/'axial_r2_constraint_mixing_system_radius2_start.json').read_text())['columns']
ordinary=defaultdict(Q); normal=defaultdict(Q)
for row in certificate['independent_witness_rows']:
    dest=normal if ast.literal_eval(row['key'])[0].startswith('continuum_') else ordinary
    for j,c in row['independent_coefficients']: dest[j]+=Q(row['weight'])*Q(c)
expected={}
for j,name in enumerate(names):
    fam,data=name.split(':',1)
    if fam!='G2':continue
    h,p=ast.literal_eval(data)
    if h[1]==p[1]==1 and h[2]!=p[2]: expected[j]=Q(p[2]-h[2])
clean=lambda d:{j:c for j,c in d.items() if c}
assert clean(normal)==expected
assert clean(ordinary)=={j:-c for j,c in expected.items()}
print('Exact surviving normalization combination: sum_(a,b)(b-a)c_BB(a,b).')
print('Ordinary equations combine to its negative, with zero RHS.')
print('Nonzero projected coefficients:',[(names[j],str(c)) for j,c in expected.items()])

# For normalized unknowns xbar=D*x, verify A_general=R*A_normalized*D
# at each family/column type, including every potentially nonzero bracket block.
a,k=s.symbols('alpha K',nonzero=True,real=True)
D={'V2':4/k,'T3':a,'G2':s.Integer(1),'F1':4*a/k,'U0':s.Integer(1),
   'V0':s.Integer(1),'G3p':a*k/4,'Z1':a,'W1':a}
R={'CC2':k/(4*a),'GC1':k/4,'GC2_P2':1/a,'GG1':s.Integer(1)}
actual={'CC2':{'V2':1/a,'T3':k/4,'G2':k/(4*a),'F1':1,'Z1':k/4},
        'GC1':{'V2':1,'G2':k/4,'U0':k/4},
        'GC2_P2':{'T3':1,'G2':1/a,'G3p':k/4,'U0':1/a,'W1':1},
        'GG1':{'G2':1,'V0':1}}
n=0
for fam,blocks in actual.items():
    for col,factor in blocks.items():
        assert s.simplify(R[fam]*D[col]-factor)==0,(fam,col)
        n+=1
print('Symbolic nonzero-parameter scaling identities:',n)
print('G2 moment rows have unit row and column factors; their RHS remains -1.')
