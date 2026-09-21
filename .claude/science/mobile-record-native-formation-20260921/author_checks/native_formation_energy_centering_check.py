#!/usr/bin/env python3
"""Exact additional source/energy controls and finite relative-walk identities."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s
from native_formation_centering_check import relative_generator

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,condition,detail=None):
    assert condition,(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail))
    print('PASS:',name,flush=True)

rho,beta,j,alpha,K=s.symbols('rho beta j alpha K',real=True)
R,G,Q=s.symbols('R G Q',real=True)
v=1-rho;lam=6*beta;mu=12*beta*j*v
a=2*alpha*rho*v;b=2*alpha*rho/3
# A Fourier pair with density R real and longitudinal vector iG. Arbitrary
# complex amplitudes split into two such real pairs with the same identity.
wr=1/(rho*v);wg=3/rho
energy=wr*R**2+wg*(G**2+Q**2)
actual=s.diff(energy,rho)*lam*v+s.diff(energy,R)*(-lam*R+a*K*G)+s.diff(energy,G)*(-b*K*R+mu*G)
expected=-(lam/rho)*wr*R**2+(2*mu-lam*v/rho)*wg*G**2-(lam*v/rho)*wg*Q**2
check('nonautonomous_entropy_energy_identity',s.factor(actual-expected)==0)
check('entropy_growth_coefficient_in_density_clock',s.factor((2*mu-lam*v/rho)/(lam*v)-(4*j-1/rho))==0)

vectors=[s.Matrix(x) for x in ((0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))]
p=[v]+[rho/6]*6
endpoint=beta*v*sum(vectors[aa][0]*sum(p[bb]*vectors[bb][0]*(1+j*vectors[aa].dot(vectors[bb])) for bb in range(7)) for aa in range(1,7))
check('exact_initial_adjacent_component_covariance',s.factor(2*endpoint-4*beta*j*rho*v/3)==0)

t,v0,kappa,A=s.symbols('t v0 kappa A',positive=True)
z=s.exp(-6*beta*t);vt=v0*z;rt=1-vt
D=(4*beta*A/kappa)*v0**2*z*((1-z)-v0*(1-z*z)/2)
check('closed_cubic_coefficient_solves_limit_ode',s.simplify(s.diff(D,t)+6*beta*D-24*beta**2*A*rt*vt**2/kappa)==0 and s.simplify(D.subs(t,0))==0)
g0=s.symbols('g0')
check('independent_Green_normalization_agrees',s.expand(90*g0-9-3*(15*(2*g0)-3))==0)

rows=[]
for side in (4,5,8):
    lap,source,pairs,lookup=relative_generator(side,3)
    first=int(2*pairs@(lap@source))
    assert int(pairs@source)==0
    assert first==(60 if side==4 else 54),(side,first)
    assert np.allclose(np.asarray(lap.sum(axis=1)),0)
    rows.append(dict(side=side,neighbor_pair_count=int(pairs.sum()),heat_reward_derivative=first))
check('exact_short_time_three_dimensional_geometry',True,rows)

report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Exact symbolic identities and integer relative-graph counts, not a fixed-coupling fluctuation theorem or a heat-kernel proof.')
(HERE/'NATIVE_FORMATION_ENERGY_CENTERING_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
