#!/usr/bin/env python3
"""Exact rational same-density/different-drift witness for one mixed encoding."""
from pathlib import Path
from itertools import product
import hashlib,json
import sympy as s
ROOT=Path(__file__).resolve().parent
R=s.Rational;I=s.I
labels=[(s.eye(3)[:,i]*z,s.zeros(3,1)) for i in range(3) for z in [1,-1]]+[(s.zeros(3,1),s.Matrix(b)) for b in product([-1,1],repeat=3)]
E=s.Matrix.hstack(*[v[0] for v in labels]);B=s.Matrix.hstack(*[v[1] for v in labels])
amplitude=R(1,8);zeta=R(1,28);la=R(1,8);lb=R(1,12);q=R(1,2);r=R(1,6);N=12;k0=R(11,10)
assert q+3*r==1 and max(la**2,3*lb**2)<q*r
states=[]
for e,b in labels:
 w=la*e+I*lb*b;rho=s.Matrix.vstack(s.Matrix.hstack(s.Matrix([[q]]),w.conjugate().T),s.Matrix.hstack(w,r*s.eye(3)));assert rho==rho.conjugate().T and s.trace(rho)==1;states.append(rho)
cos=[s.Integer(1),R(1,2),R(-1,2),s.Integer(-1),R(-1,2),R(1,2)]*2
laws=[]
for modified in [False,True]:
 rows=[]
 for x in range(N):
  p=s.ones(14,1)/14
  for a,(_,b) in enumerate(labels):p[a]+=b[2]*amplitude*cos[x]/8
  if modified:
   for a in [2,3]:p[a]+=zeta/2
   for a in [0,1]:p[a]-=zeta/2
  assert sum(p)==1 and min(p)>0
  rows.append(p)
 laws.append(rows)
for x in range(N):
 assert E*laws[0][x]==E*laws[1][x]==s.zeros(3,1) and B*laws[0][x]==B*laws[1][x]
 density=[sum((p[a]*states[a] for a in range(14)),s.zeros(4)) for p in [laws[0][x],laws[1][x]]]
 assert density[0]==density[1]
def current(p,x,delta):
 step=int(delta[0]-1)
 if delta==s.Matrix([1,0,0]):return s.zeros(14,1)
 S=s.Matrix(14,14,lambda a,b:delta.dot(labels[a][0].cross(labels[b][1])+labels[b][0].cross(labels[a][1])))/2
 pl,pu,pw,pr=[p[(x+j*step)%N] for j in [-1,0,1,2]]
 ss=S*(pl+pr);muu=pu.dot(ss);muw=pw.dot(ss)
 return k0*(pu-pw)/2+((pu+pw).multiply_elementwise(ss)-pu*muw-pw*muu)/4
drifts=[]
for law in laws:
 drift=s.zeros(14,1)
 for i,z in product(range(3),[1,-1]):
  delta=s.eye(3)[:,i]*z;step=int(delta[0]-1);drift+=current(law,1-step,delta)-current(law,1,delta)
 assert sum(drift)==0
 drifts.append((E*drift)[1])
assert drifts[0]==-3*R(1,7)*amplitude/4 and drifts[1]==-3*(R(1,7)+zeta)*amplitude/4
difference=drifts[1]-drifts[0];assert difference==R(-3,896) and 2*la*difference==R(-3,3584)
result=dict(N=N,same_pair_density_at_all_coordinates=True,full_product_equality='Exact consequence of each local equality, no full tensor matrix materialized.',minimum_probability=str(min(v for law in laws for p in law for v in p)),X2_drifts=[str(x) for x in drifts],X2_derivative_difference=str(difference),physical_A2_derivative_difference=str(2*la*difference),sources=[])
for f in ['DIMER_MIXED_ENCODING_INITIAL_DRIFT_AMBIGUITY.md',Path(__file__).name]:
 p=ROOT/f;result['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(ROOT/'DIMER_MIXED_ENCODING_INITIAL_DRIFT_AMBIGUITY_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

