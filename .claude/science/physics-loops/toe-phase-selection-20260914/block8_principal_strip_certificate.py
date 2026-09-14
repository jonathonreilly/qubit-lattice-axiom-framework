#!/usr/bin/env python3
"""Exact rational witness for the three-square principal temporal kernel.
Author exploration; no claim about a periodic infinite-volume phase.
"""
from itertools import product
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.linalg import eigh
import json

n=3;e=3*n+1
f=np.zeros((n,e),dtype=int)
for j in range(n):
    f[j,j]=1;f[j,j+1]=-1;f[j,n+1+2*j]=1;f[j,n+2+2*j]=-1
lifts=np.array(list(product([-1,0,1],repeat=e)),dtype=np.int8)
curl=lifts@f.T;energy=np.sum(lifts*lifts,axis=1)
states=np.array(list(product([-1,0,1],repeat=n)))
power=3**np.arange(n);lookup=np.zeros(3**n,dtype=int)
lookup[((states+1)%3)@power]=np.arange(3**n)
q=Fraction(9,10);r=Fraction(1,2)
counts=np.zeros((27,27,e+1,4*n+1),dtype=np.int64)
for j,b in enumerate(states):
    bp=(b+curl+1)%3-1;mismatch=(bp-b-curl)//3
    target=lookup[((bp+1)%3)@power];penalty=np.sum(mismatch*mismatch,axis=1)
    np.add.at(counts[:,j],(target,energy,penalty),1)
assert np.max(np.abs(counts-counts.transpose(1,0,2,3)))==0
weights=np.array([[float(q**k*r**s/(1+2*q)**e) for s in range(4*n+1)] for k in range(e+1)])
k=np.einsum('ijab,ab->ij',counts,weights)
vals,vecs=eigh(k)
v=vecs[:,0]
v=v/max(abs(v))
candidates=[]
for scale in [1,2,3,4,5,10,20,100]:
    w=np.rint(scale*v).astype(int)
    form=float(w@k@w)
    if form<0:
        candidates.append((scale,w,form));break
assert candidates
scale,w,form=candidates[0]
# Integer aggregation followed by Fraction arithmetic: no eigenvalue sign test
# is used for the final witness. The numerical search only chose this w.
hist=np.einsum('i,j,ijab->ab',w,w,counts,dtype=np.int64)
exact=sum((int(hist[a,b])*q**a*r**b/(1+2*q)**e for a in range(e+1) for b in range(4*n+1)),Fraction(0))
assert exact<0
assert abs(float(exact)-form)<1e-14
result=dict(scope='3 adjacent spatial squares with free boundary; gauge-invariant flux space; principal temporal Wilson kernel',E=e,P=n,physical_dimension=27,q=str(q),exp_minus_mu=str(r),F=f.tolist(),states=states.tolist(),integer_witness=w.tolist(),witness_norm_squared=int(w@w),exact_quadratic_form=str(exact),exact_rayleigh_quotient=str(exact/int(w@w)),numeric_quadratic_form=float(exact),minimum_float_eigenvalue=float(vals[0]),coefficient_histogram=hist.tolist(),proof='Each histogram coefficient is an exact sum of w[bprime]*w[b] over all 3^10 principal lifts, grouped by lift norm squared and mismatch norm squared. Negative exact rational quadratic form disproves positive semidefiniteness of this finite physical principal kernel only.')
path=Path(__file__).resolve().with_name('BLOCK8_PRINCIPAL_STRIP_CERTIFICATE.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:value for key,value in result.items() if key not in ['coefficient_histogram','states']},indent=2))
