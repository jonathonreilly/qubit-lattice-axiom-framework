#!/usr/bin/env python3
"""A fixed rational covariant encoding of all fourteen probabilities on two pairs."""
from pathlib import Path
from itertools import product,permutations
import datetime,hashlib,json
import sympy as s
from sympy.polys.matrices import DomainMatrix
HERE=Path(__file__).resolve().parent
group=[]
for sigma in permutations(range(3)):
 character=(-1)**sum(sigma[i]>sigma[j] for i in range(3) for j in range(i+1,3))
 for signs in product((-1,1),repeat=3):
  R=s.zeros(3)
  for i in range(3):R[i,sigma[i]]=signs[i]
  if R.det()==1:
   U=s.diag(1,R);group.append((R,s.kronecker_product(U,U),character))
assert len(group)==24
origins=[s.Matrix([1,0,0]),s.ones(3,1)]
labels=[s.eye(3)[:,i]*z for i in range(3) for z in (1,-1)]+[s.Matrix(b) for b in product((-1,1),repeat=3)]
vectors=[s.Matrix([(7*i*i+3*i+5)%17-8 for i in range(16)]),s.Matrix([(11*i*i*i+4*i+1)%19-9 for i in range(16)])]
seeds=[];denominators=[];stabilizer_counts=[]
for origin,v in zip(origins,vectors):
 stabilizer=[U for R,U,c in group if R*origin==origin]
 seed=s.eye(16)+sum((U*v*v.T*U.T for U in stabilizer),s.zeros(16))
 seeds.append(seed);denominators.append(int(s.trace(seed)));stabilizer_counts.append(len(stabilizer))
 assert seed==seed.T
assert stabilizer_counts==[4,3]
states=[];integers=[]
for a,label in enumerate(labels):
 orbit=int(a>=6);origin=origins[orbit]
 rotations=[U for R,U,c in group if R*origin==label]
 matrices=[U*seeds[orbit]*U.T for U in rotations]
 assert matrices and all(M==matrices[0] for M in matrices)
 integers.append(matrices[0]);states.append(matrices[0]/denominators[orbit])
lookup={tuple(label):a for a,label in enumerate(labels)}
for R,U,c in group:
 for a,label in enumerate(labels):
  target=lookup[tuple(R*label)]
  assert states[target]==U*states[a]*U.T
  assert s.trace(states[a])==1
columns=s.Matrix.hstack(*[s.Matrix(list(M)) for M in integers])
rank=DomainMatrix.from_Matrix(columns).convert_to(s.QQ).rank()
affine=s.Matrix.hstack(*[s.Matrix(list(states[a]-states[0])) for a in range(1,14)])
affine_rank=DomainMatrix.from_Matrix(affine).convert_to(s.QQ).rank()
assert rank==14 and affine_rank==13
# Exact character computation: operator alternating sector exists, although the Hilbert sector does not.
operator_mult=sum(c*s.trace(U)**2 for R,U,c in group)/24
hilbert_mult=sum(c*s.trace(U) for R,U,c in group)/24
assert operator_mult==7 and hilbert_mult==0
cubic=sum((s.prod(labels[a])*states[a] for a in range(6,14)),s.zeros(16))
assert cubic!=s.zeros(16)
for R,U,c in group:assert U*cubic*U.T==c*cubic
out=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),dimension=16,physical_pairs=2,proper_rotations=24,
 stabilizers=stabilizer_counts,seed_vectors=[[int(x) for x in v] for v in vectors],trace_denominators=denominators,
 rational_state_column_rank=rank,affine_probability_rank=affine_rank,operator_alternating_multiplicity=str(operator_mult),
 hilbert_alternating_multiplicity=str(hilbert_mult),cubic_operator_nonzero=True,covariance_equalities=336,
 strict_positivity='Each state is a conjugate of I plus a sum of vv^T terms, divided by its positive trace.',
 minimum_eigenvalue_lower_bounds=[str(s.Rational(1,z)) for z in denominators],
 cubic_operator_frobenius_square=str(s.trace(cubic.T*cubic)),sources=[])
for name in [Path(__file__).name,'DIMER_TWO_PAIR_FAITHFUL_COVARIANT_ENCODING.md']:
 p=HERE/name;out['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(HERE/'DIMER_TWO_PAIR_FAITHFUL_ENCODING_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
