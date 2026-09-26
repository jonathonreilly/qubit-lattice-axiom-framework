#!/usr/bin/env python3
"""Exact representation projection and microscopic initial-drift control."""
from pathlib import Path
from itertools import product,permutations
import datetime,hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent
F=s.Rational
labels=[(s.eye(3)[:,i]*z,s.zeros(3,1)) for i in range(3) for z in (1,-1)]+[(s.zeros(3,1),s.Matrix(b)) for b in product((-1,1),repeat=3)]
E=s.Matrix.hstack(*[x[0] for x in labels]);B=s.Matrix.hstack(*[x[1] for x in labels])
Z=s.Matrix([[b[0]*b[1] for e,b in labels]])
chi=s.Matrix([[s.prod(b) for e,b in labels]])
q,r,la,lb,kap=F(1,2),F(1,6),F(1,16),F(1,48),F(1,96)
states=[];minor_rows=[]
for e,b in labels:
 w=la*e+s.I*lb*b
 block=r*s.eye(3)+(kap*(b*b.T-s.eye(3)) if b!=s.zeros(3,1) else s.zeros(3))
 rho=s.Matrix.vstack(s.Matrix.hstack(s.Matrix([[q]]),w.conjugate().T),s.Matrix.hstack(w,block))
 assert rho==rho.conjugate().T and s.trace(rho)==1
 minors=[rho[:j,:j].det() for j in range(1,5)]
 assert all(x>0 for x in minors)
 states.append(rho);minor_rows.append([str(x) for x in minors])
lookup={(tuple(e),tuple(b)):a for a,(e,b) in enumerate(labels)}
Pa=s.zeros(16);Pone=s.zeros(16);grouprows=[];covariance_checks=0
for sigma in permutations(range(3)):
 parity=(-1)**sum(sigma[i]>sigma[j] for i in range(3) for j in range(i+1,3))
 for signs in product((-1,1),repeat=3):
  R=s.zeros(3)
  for i in range(3):R[i,sigma[i]]=signs[i]
  if R.det()!=1:continue
  U=s.diag(1,R);superop=s.kronecker_product(U.conjugate(),U)
  Pa+=parity*superop/24;Pone+=superop/24
  for a,(e,b) in enumerate(labels):
   target=lookup[(tuple(R*e),tuple(R*b))]
   assert states[target]==U*states[a]*U.conjugate().T
   if b!=s.zeros(3,1):assert s.prod(R*b)==parity*s.prod(b)
   covariance_checks+=1
  grouprows.append(dict(matrix=[list(R.row(i)) for i in range(3)],character=parity,operator_character=str(s.trace(superop))))
assert len(grouprows)==24 and Pa==s.zeros(16)
assert Pone**2==Pone and Pone.rank()==2
assert sum((chi[0,a]*states[a] for a in range(14)),s.zeros(4))==s.zeros(4)
Q=s.zeros(4);Q[1,2]=Q[2,1]=1
assert all(s.trace(states[a]*Q)==2*kap*Z[a] for a in range(14))
A,eta,N,k0=F(1,28),F(1,16),12,F(11,10)
cos=[1,F(1,2),F(-1,2),-1,F(-1,2),F(1,2)]*2
laws=[]
for changed in (False,True):
 law=[]
 for x in range(N):
  p=s.ones(14,1)/14;p[2]+=A/2;p[3]-=A/2
  if changed:p+=eta*cos[x]*chi.T/8
  assert sum(p)==1 and min(p)>0
  assert E*p==s.Matrix([0,A,0]) and B*p==s.zeros(3,1) and Z*p==s.zeros(1,1)
  law.append(p)
 laws.append(law)
for x in range(N):
 densities=[sum((p[a]*states[a] for a in range(14)),s.zeros(4)) for p in (laws[0][x],laws[1][x])]
 assert densities[0]==densities[1]
def current(law,x,delta):
 step=int(delta[0]-1)
 if delta==s.Matrix([1,0,0]):return s.zeros(14,1)
 S=s.Matrix(14,14,lambda a,b:delta.dot(labels[a][0].cross(labels[b][1])+labels[b][0].cross(labels[a][1])))/2
 pl,pu,pw,pr=[law[(x+j*step)%N] for j in (-1,0,1,2)]
 v=S*(pl+pr)
 return k0*(pu-pw)/2+((pu+pw).multiply_elementwise(v)-pu*pw.dot(v)-pw*pu.dot(v))/4
derivatives=[];direction_rows=[]
for law in laws:
 drift=s.zeros(14,1);rows=[]
 for i,sign in product(range(3),(1,-1)):
  delta=s.eye(3)[:,i]*sign;step=int(delta[0]-1)
  contribution=current(law,1-step,delta)-current(law,1,delta)
  rows.append(dict(delta=list(delta),Z12_derivative=str((Z*contribution)[0])))
  drift+=contribution
 assert sum(drift)==0
 derivatives.append((Z*drift)[0]);direction_rows.append(rows)
assert derivatives==[0,F(3,3584)]
assert 2*kap*(derivatives[1]-derivatives[0])==F(1,57344)
out=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),proper_rotations=grouprows,
 alternating_operator_projection_all_256_entries_zero=True,trivial_operator_projection_rank=2,covariance_checks=covariance_checks,
 positive_state_leading_principal_minors=minor_rows,N=N,minimum_color_probability=str(min(p[a] for law in laws for p in law for a in range(14))),
 local_density_equality_all_coordinates=True,full_product_equality='Follows exactly from all local equalities; full tensor not materialized.',
 Z12_initial_derivatives=[str(x) for x in derivatives],physical_Q12_derivative_difference='1/57344',directional_derivatives=direction_rows,
 boundary='Specified U=1 plus vector, affine covariant pair encoding and a domain with the displayed preparations. Not a general no-go result.',sources=[])
for f in ['DIMER_PAIR_COVARIANCE_CUBIC_MOMENT.md',Path(__file__).name,'DIMER_NONLINEAR_INITIAL_DRIFT.md','DIMER_COVARIANT_QUANTUM_FLUCTUATION_ENCODING.md']:
 p=HERE/f;out['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(HERE/'DIMER_PAIR_COVARIANCE_CUBIC_RESULTS.json').write_text(json.dumps(out,indent=2,default=str)+'\n')
print('exact representation, covariance, positivity and drift controls complete')
