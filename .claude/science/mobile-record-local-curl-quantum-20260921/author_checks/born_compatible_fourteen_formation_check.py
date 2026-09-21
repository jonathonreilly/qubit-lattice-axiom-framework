#!/usr/bin/env python3
"""Primary full-species algebra and time-ordered finite-mode controls."""
from pathlib import Path
from itertools import product, permutations
import hashlib, json
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
from scipy.linalg import expm

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,condition,detail=None):
    assert bool(condition),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
def clean(m):return m.applyfunc(s.simplify)
unit=[s.eye(3)[:,i] for i in range(3)];zero=s.zeros(3,1)
features=[(sign*unit[i],zero) for i in range(3) for sign in (-1,1)]
features += [(zero,s.Matrix(signs)) for signs in product((-1,1),repeat=3)]
rays=[e if a<6 else b/s.sqrt(3) for a,(e,b) in enumerate(features)]
S=s.Matrix.hstack(*rays).T;T=S*S.T
check('Born_Gram_rank_and_isotropic_frame',T.rank()==3 and S.T*S==s.Rational(14,3)*s.eye(3) and S.T*s.ones(14,1)==s.zeros(3,1))
beta,j,gamma,rho=s.symbols('beta j gamma rho',real=True)
p=s.Matrix(s.symbols('p0:14',real=True));vac=1-sum(p)
raw=sum((p[a]*rays[a] for a in range(14)),zero)
birth=s.Matrix([beta*vac*(1+j*rays[a].dot(raw))**6 for a in range(14)])
background={q:rho/14 for q in p}
check('uniform_fourteen_trajectory',clean(birth.subs(background)-beta*(1-rho)*s.ones(14,1))==s.zeros(14,1))
moment=[]
for a,(e,b) in enumerate(features):
    isA=int(a<6);isB=1-isA
    moment.append([1,4*isA-3*isB,*list(2*e),*list(b),e[0]**2-e[2]**2,e[1]**2-e[2]**2,b[0]*b[1],b[0]*b[2],b[1]*b[2],b[0]*b[1]*b[2]])
M=s.Matrix(moment).T;inverse=M.inv()
reaction=clean(M*birth.jacobian(p).subs(background)*inverse)
h=beta*j*(1-rho)
expected=s.zeros(14);expected[0,0]=-14*beta
expected[2:5,2:5]=12*h*s.eye(3);expected[2:5,5:8]=8*s.sqrt(3)*h*s.eye(3)
expected[5:8,2:5]=8*s.sqrt(3)*h*s.eye(3);expected[5:8,5:8]=16*h*s.eye(3)
check('entire_fourteen_species_reaction_Jacobian',reaction==expected)
k=s.Matrix(s.symbols('kx ky kz',real=True));C=s.Matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])
speed=2*gamma*rho/7
flux=s.Matrix(14,14,lambda a,b:gamma*rho*s.Rational(1,14)*k.dot(features[a][0].cross(features[b][1])+features[b][0].cross(features[a][1])))
full=clean(reaction-s.I*M*flux*inverse)
target=expected.copy();target[2:5,5:8]+=s.I*speed*C;target[5:8,2:5]-=s.I*speed*C
check('entire_fourteen_species_flux_and_reaction',full==target)
R=4*h*s.Matrix([[3,2*s.sqrt(3)],[2*s.sqrt(3),4]])
O=s.Matrix([[s.sqrt(3),2],[-2,s.sqrt(3)]])/s.sqrt(7)
check('driven_and_undriven_vector_rotation',clean(O*R*O.T)==s.diag(28*h,0) and O.det()==1)
omega,z=s.symbols('omega z',real=True)
helicity=R+s.Matrix([[0,omega],[-omega,0]])
check('frozen_transverse_characteristic_polynomial',s.factor((z*s.eye(2)-helicity).det()-(z*z-28*h*z+omega**2))==0)
check('noncommuting_gain_and_wave_blocks',R*s.Matrix([[0,1],[-1,0]])-s.Matrix([[0,1],[-1,0]])*R!=s.zeros(2))

sigma=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
def spin(v):return sum((v[i]*sigma[i] for i in range(3)),s.zeros(2))
states=[(s.eye(2)+spin(v))/2 for v in rays]
effects=[(s.eye(2)+j*spin(v))/14 for v in rays]
check('all196_single_qubit_marked_probabilities',all(s.simplify(s.trace(effects[a]*states[b])-(1+j*T[a,b])/14)==0 for a in range(14) for b in range(14)))
SWAP=s.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
second=sum((s.kronecker_product(q,q) for q in states),s.zeros(4))/14
check('fourteen_ray_second_moment_for_fidelity',clean(second-(s.eye(4)+SWAP)/6)==s.zeros(4))
# Factorized rate probabilities are checked over every two-parent input pair.
Js=s.Rational(1,2)
joint=0
for a in range(14):
    effect=s.kronecker_product(14*effects[a].subs(j,Js),14*effects[a].subs(j,Js))
    for b,c in product(range(14),repeat=2):
        value=s.trace(effect*s.kronecker_product(states[b],states[c]))
        assert s.simplify(value-(1+Js*T[a,b])*(1+Js*T[a,c]))==0
        joint+=1
check('all_two_parent_marked_rate_probabilities',True,dict(probabilities=joint))

# The specified improper action is e->Qe and b->det(Q)Qb.
Q=s.diag(-1,1,1);exampleA=unit[0];exampleB=s.ones(3,1)
before=exampleA.dot(exampleB)/s.sqrt(3)
after=(Q*exampleA).dot(-Q*exampleB)/s.sqrt(3)
check('explicit_full_parity_failure_of_cross_orbit_weight',s.simplify(after+before)==0 and before!=0)
gain=s.exp(2*j*(rho-s.Symbol('rho_start')))
check('integrated_norm_gain_comparison',s.simplify(s.diff(gain,rho)*14*beta*(1-rho)-28*h*gain)==0)

# Direct time ordering for the 6x6 fundamental matrix; this is a finite ODE
# check, not a Monte Carlo experiment or a native stochastic CLT.
wave=np.array([2*np.pi,0,0]);K=np.linalg.norm(wave)
Cn=np.array([[0,-wave[2],wave[1]],[wave[2],0,-wave[0]],[-wave[1],wave[0],0]])
J=np.block([[np.zeros((3,3)),1j*Cn],[-1j*Cn,np.zeros((3,3))]])
bval=.3;gval=.7;r0=.2;cinf=2*gval/7;Linf=cinf*J
ode=[]
for js in (-.8,0,.8):
    def derivative(t,y):
        density=1-(1-r0)*np.exp(-14*bval*t);hh=bval*js*(1-density)
        Rn=4*hh*np.array([[3,2*np.sqrt(3)],[2*np.sqrt(3),4]])
        L=cinf*density*J+np.kron(Rn,np.eye(3))
        return (L@y.reshape(6,6)).ravel()
    times=np.linspace(0,6,121)
    sol=solve_ivp(derivative,(0,6),np.eye(6,dtype=complex).ravel(),t_eval=times,
                  method='DOP853',rtol=2e-11,atol=2e-12)
    assert sol.success
    violations=[]
    for t,flat in zip(sol.t,sol.y.T):
        density=1-(1-r0)*np.exp(-14*bval*t);factor=np.exp(2*js*(density-r0))
        singular=np.linalg.svd(flat.reshape(6,6),compute_uv=False)
        violations.extend([max(singular)-max(1,factor),min(1,factor)-min(singular)])
    Phi3=sol.y[:,60].reshape(6,6);Phi6=sol.y[:,-1].reshape(6,6)
    Z3=expm(-Linf*3)@Phi3;Z6=expm(-Linf*6)@Phi6
    diff=np.linalg.norm(Z6-Z3,ord=2)
    tail=np.exp(2*abs(js)*(1-r0))*(1-r0)*np.exp(-14*bval*3)*(2*abs(js)+abs(cinf)*K/(14*bval))
    assert max(violations)<2e-9 and diff<tail+2e-10
    exact_residual=None
    if js==0:
        integrated_c=cinf*(6-(1-r0)*(1-np.exp(-14*bval*6))/(14*bval))
        exact_residual=float(np.linalg.norm(Phi6-expm(integrated_c*J),ord=2))
        assert exact_residual<2e-9
    ode.append(dict(j=js,norm_comparison_violation=float(max(violations)),late_interaction_picture_difference=float(diff),
                    rigorous_tail_bound=float(tail),j0_integrated_phase_residual=exact_residual))
check('time_ordered_six_field_ODE_gain_and_late_wave_controls',True,ode)

report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Primary exact fourteen-field and quantum-event controls plus finite numerical time-ordered ODE checks. No repeated quantum waiting law, immutable physical parent, native stochastic fluctuation theorem or physical EM identification.')
(HERE/'BORN_COMPATIBLE_FOURTEEN_FORMATION_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
