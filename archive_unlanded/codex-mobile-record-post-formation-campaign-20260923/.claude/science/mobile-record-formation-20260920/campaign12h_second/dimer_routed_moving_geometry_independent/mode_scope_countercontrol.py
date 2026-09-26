#!/usr/bin/env python3
"""Exact countercontrol to an unqualified arbitrary-product mode count."""
from pathlib import Path
from itertools import product
from hashlib import sha256
import json
import sympy as s

OUT=Path(__file__).resolve().parent
e=[s.Matrix([sgn if j==i else 0 for j in range(3)]) for i in range(3) for sgn in [1,-1]]+[s.zeros(3,1)]*8
b=[s.zeros(3,1)]*6+[s.Matrix(x) for x in product([-1,1],repeat=3)]
variables=s.symbols('p0:14');Q=s.Matrix([0,0,1])
X=sum((variables[a]*e[a] for a in range(14)),s.zeros(3,1))
Y=sum((variables[a]*b[a] for a in range(14)),s.zeros(3,1))
J=s.Matrix([variables[a]*Q.dot(e[a].cross(Y)+X.cross(b[a])-2*X.cross(Y)) for a in range(14)])
Jacobian=J.jacobian(variables)
tangent=s.zeros(14,13)
for i in range(13):tangent[i,i]=1;tangent[13,i]=-1
z=s.Symbol('z');rows=[]
for name in ['isotropic','asymmetric_A']:
    p=[s.Rational(1,14)]*14
    if name=='asymmetric_A':p[0]=s.Rational(3,28);p[1]=s.Rational(1,28)
    assert sum(p)==1 and all(x>0 for x in p)
    A=Jacobian.subs(dict(zip(variables,p)))
    reduced=(A*tangent)[:13,:]
    assert A*tangent==tangent*reduced
    C=s.diag(*p)-s.Matrix(p)*s.Matrix(p).T
    assert A*C==C*A.T
    char=s.factor(reduced.charpoly(z).as_expr());rank=reduced.rank()
    expected=s.expand(z**9*(49*z*z-4)**2/2401) if name=='isotropic' else s.expand(z**5*(14*z-1)**2*(14*z+1)**2*(196*z*z-17)*(1372*z*z-103)/10330523392)
    assert s.expand(char-expected)==0 and rank==(4 if name=='isotropic' else 8)
    rows.append({'case':name,'p':[str(x) for x in p],'rho_A':str(sum(p[:6])),'rho_B':str(sum(p[6:])),
                 'gamma':'1','direction_Q_without_2pi':[0,0,1],
                 'tangent_rank_nonzero_eigenvalues':rank,'zero_eigenvalue_multiplicity':13-rank,
                 'monic_characteristic_polynomial':str(char),'entropy_covariance_symmetry_exact':True})
result={'source_current':'Corrected routed note equation (5), differentiated symbolically on the full variables then restricted to the probability tangent.',
        'Fourier_scaling':'For the actual fixed mode Q=2pi e3, multiply every eigenvalue by 2pi; the mode counts are unchanged.',
        'finding':'F1: positive orbit masses alone do not imply four propagating and nine static modes. Require the orbit-isotropic probabilities for this specialization.',
        'does_not_refute':'The arbitrary fixed full-support p matrix-propagation theorem.', 'rows':rows}
(OUT/'MODE_SCOPE_COUNTERCONTROL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
