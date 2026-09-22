#!/usr/bin/env python3
"""Author checks of new smooth-time proof steps; no simulation of a PDE limit."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as F
import hashlib,json,math,importlib.util
import numpy as np
import sympy as s
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('flux',ROOT/'dimer_nonlinear_flux_check.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def block_controls():
 gs=np.array([[-2,0,0],[-1,1,0],[-1,0,1]],dtype=int);assert round(np.linalg.det(gs))==-2
 routes=[gs[0],gs[1],gs[2],gs[0]-gs[1],gs[0]-gs[2]];rows=[]
 for ell in [2,3,4,5,6]:
  N=8*ell+2;coords=list(product(range(ell),repeat=3));B={tuple(np.array(r)@gs) for r in coords};mod={tuple(np.array(b)%N) for b in B}
  assert len(B)==len(mod)==ell**3 and all(sum(b)%2==0 for b in B)
  diff={tuple((np.array(r)@gs)%N) for r in product(range(-ell+1,ell),repeat=3)}
  assert len(diff)==(2*ell-1)**3 and len(diff)<=8*ell**3
  edges=[]
  for x in coords:
   for j in range(3):
    y=list(x);y[j]+=1
    if y[j]<ell:edges.append((x,tuple(y)))
  assert len(edges)==3*(ell-1)*ell**2
  interior=[]
  for a in routes:
   count=sum(all(tuple(np.array(b)+d*a) in B for d in [-1,0,1,2]) for b in B)
   assert ell**3-count<=9*ell**2
   interior.append(count)
  rows.append(dict(ell=ell,N=N,block_sites=ell**3,overlap_colors_bound=8*ell**3,actual_difference_count=len(diff),bare_internal_edges=len(edges),five_internal_stencil_counts=interior))
 return rows

def sector_controls():
 sites=list(product(range(2),repeat=3));ix={x:i for i,x in enumerate(sites)};edges=[]
 for x in sites:
  for j in range(3):
   y=list(x);y[j]^=1
   if ix[x]<ix[tuple(y)]:edges.append((ix[x],ix[tuple(y)]))
 rows=[]
 for count in [1,2,3,4]:
  states=[tuple(int(i in pos) for i in range(8)) for pos in combinations(range(8),count)];ind={x:i for i,x in enumerate(states)};dim=len(states);L=np.zeros((dim,dim),dtype=int)
  for col,state in enumerate(states):
   for a,b in edges:
    out=list(state);out[a],out[b]=out[b],out[a];j=ind[tuple(out)]
    if j!=col:L[j,col]-=1;L[col,col]+=1
  assert s.Matrix(L).to_DM().rank()==dim-1
  evals=np.linalg.eigvalsh(L);gap=float(evals[1]);assert gap>0
  c=np.array([1+i%7 for i in range(dim)],dtype=np.int64);den=int(c@c)
  variance=F(1)-F(int(c.sum())**2,dim*den);dirichlet=F(int(c@L@c),den)
  assert float(variance)<=float(dirichlet)/gap+1e-13
  values=[F(st[0]*st[3])-F(sum(t[0]*t[3] for t in states),dim) for st in states];M=max(abs(v) for v in values)
  expected=sum(F(int(z*z),den)*v for z,v in zip(c,values))
  assert expected**2<=4*M*M*variance
  # The unweighted stationary entropy derivative obeys the scalar bound.
  rho=dim*c.astype(float)**2/den;entropy_derivative=float((-L@rho)@np.log(rho)/dim)
  assert entropy_derivative<=-2*float(dirichlet)+1e-13
  rows.append(dict(particle_count=count,sector_dimension=dim,exact_connected_rank=dim-1,numerical_gap=gap,exact_variance=str(variance),exact_Dirichlet=str(dirichlet),centered_pairing=str(expected),entropy_derivative=entropy_derivative))
 return rows

def algebra_controls():
 rows=[]
 for seed in range(4):
  weights=[2+(i+3*seed)**2%13 for i in range(14)];p=s.Matrix([s.Rational(w,sum(weights)) for w in weights]);H=s.diag(*[1/x for x in p])
  grads=[old.T*s.Matrix([s.Rational(((i+seed+j)%5)-2,101) for i in range(13)]) for j in range(3)]
  Js=[old.jac(p,old.Kmatrix(s.eye(3)[:,j])) for j in range(3)]
  pt=-sum((J*g for J,g in zip(Js,grads)),s.zeros(14,1))
  cancellation=H*pt+sum((J.T*H*g for J,g in zip(Js,grads)),s.zeros(14,1))
  assert old.T.T*cancellation==s.zeros(13,1) and (p.T*H*pt)[0]==0
  rows.append(dict(seed=seed,exact_tangent_entropy_cancellation=True,ambient_constant=str(cancellation[0])))
 draw=[]
 for m in [4,5,8,14,17,64,125,1000]:
  tv=1-F(math.prod(range(m-3,m+1)),m**4);assert tv<=F(6,m)
  draw.append(dict(m=m,exact_index_coupling_failure=str(tv),four_draw_bound=str(F(6,m))))
 alpha=F(1,224);assert 2*alpha*8==F(1,14)
 # Bernoulli centered log MGF has value and slope zero at the origin;
 # its second derivative is tilted_p*(1-tilted_p)<=1/4. Integrating
 # twice proves the t^2/8 bound for all real t, then Chernoff gives (15).
 z=s.symbols('z',real=True);assert s.expand(F(1,4)-z*(1-z))==s.expand((z-s.Rational(1,2))**2)
 mgf=[]
 for probability in [.001,.1,.5,.9,.999]:
  for t in [-10,-2,-.1,.1,2,10]:
   actual=np.logaddexp(math.log1p(-probability)-t*probability,math.log(probability)+t*(1-probability))
   assert actual<=t*t/8+1e-14
   mgf.append(dict(p=probability,t=t,log_centered_MGF=float(actual),bound=t*t/8))
 return dict(tangent_cancellations=rows,without_replacement_coupling=draw,holder_alpha=str(alpha),integrated_Hoeffding_exponential_bound=29,Bernoulli_checks=mgf)

def main():
 result=dict(sources=[],blocks=block_controls(),fixed_sector=sector_controls(),entropy_algebra=algebra_controls(),
  scope='Exact finite block geometry, exact connectivity ranks and conditional Cauchy calculations, finite numerical gap/entropy controls, exact tangent cancellation and coupling arithmetic. The full all-volume theorem is a proof, not inferred from these checks.')
 for f in ['DIMER_SMOOTH_NONLINEAR_EULER_LIMIT.md','DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md','DIMER_NONLINEAR_INITIAL_DRIFT.md','dimer_nonlinear_flux_check.py',Path(__file__).name]:
  p=ROOT/f;result['sources'].append(dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
 out=ROOT/'dimer_smooth_nonlinear_checks';out.mkdir(exist_ok=True);(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print('three_control_groups_complete',flush=True)
if __name__=='__main__':main()

