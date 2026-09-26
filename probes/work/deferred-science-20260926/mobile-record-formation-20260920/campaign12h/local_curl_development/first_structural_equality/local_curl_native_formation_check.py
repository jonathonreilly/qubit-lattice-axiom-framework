#!/usr/bin/env python3
"""Primary algebra and finite-event controls for local curl/native formation.

The complete fourteen-dimensional Jacobian is checked, not just a selected
wave block. No stochastic native fluctuation limit is tested or asserted.
"""
from pathlib import Path
from itertools import product,permutations
import hashlib,json
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
beta,gamma,j,rho=s.symbols('beta gamma j rho',real=True)
unit=[s.eye(3)[:,i] for i in range(3)]
zero=s.zeros(3,1)
features=[(sign*unit[i],zero) for i in range(3) for sign in (-1,1)]
features += [(zero,s.Matrix(signs)) for signs in product((-1,1),repeat=3)]
checks=[]
def check(name,condition,detail=None):
    assert bool(condition),(name,detail)
    checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,flush=True)
def clean(matrix):return matrix.applyfunc(s.simplify)
def cross(k):
    return s.Matrix([[0,-k[2],k[1]],[k[2],0,-k[0]],[-k[1],k[0],0]])

T=s.Matrix(14,14,lambda a,b:features[a][0].dot(features[b][0])+features[a][1].dot(features[b][1])/4)
values=set(T)
check('all_pair_weight_brackets_and_positivity_bound',values=={-1,-s.Rational(3,4),-s.Rational(1,4),0,s.Rational(1,4),s.Rational(3,4),1})
p=s.Matrix(s.symbols('p0:14',real=True));v=1-sum(p)
X=sum((p[a]*features[a][0] for a in range(14)),zero)
Y=sum((p[a]*features[a][1] for a in range(14)),zero)
birth=s.Matrix([beta*v*(1+j*(features[a][0].dot(X)+features[a][1].dot(Y)/4))**6 for a in range(14)])
background={q:rho/14 for q in p}
check('full_uniform_reaction_trajectory',clean(birth.subs(background)-s.ones(14,1)*beta*(1-rho))==s.zeros(14,1))
moment=[]
for a,(e,b) in enumerate(features):
    isA=int(a<6);isB=1-isA
    moment.append([1,4*isA-3*isB,*list(2*e),*list(b),e[0]**2-e[2]**2,e[1]**2-e[2]**2,b[0]*b[1],b[0]*b[2],b[1]*b[2],b[0]*b[1]*b[2]])
M=s.Matrix(moment).T;inverse=M.inv()
check('fourteen_moments_reconstruct_all_occupied_probabilities',M*inverse==s.eye(14))
reaction=clean(M*birth.jacobian(p).subs(background)*inverse)
lam=12*beta*j*(1-rho)
expected=s.diag(-14*beta,0,*([lam]*6),*([0]*6))
check('complete_native_reaction_jacobian',reaction==expected)

k=s.Matrix(s.symbols('kx ky kz',real=True));C=cross(k);speed=2*gamma*rho/7
current_derivative=s.Matrix(14,14,lambda a,b:gamma*rho*s.Rational(1,14)*k.dot(features[a][0].cross(features[b][1])+features[b][0].cross(features[a][1])))
full=clean(reaction-s.I*M*current_derivative*inverse)
target=expected.copy();target[2:5,5:8]=s.I*speed*C;target[5:8,2:5]=-s.I*speed*C
check('all_fourteen_linear_flux_and_reaction_fields',full==target)
P=k.dot(k)*s.eye(3)-k*k.T
L=full[2:8,2:8];skew=L-lam*s.eye(6)
check('transverse_wave_and_longitudinal_reaction_structure',clean(skew**2+s.diag(speed**2*P,speed**2*P))==s.zeros(6) and clean(C*k)==s.zeros(3,1))
filter=s.zeros(6);filter[:3,3:]=s.I*C;filter[3:,:3]=-s.I*C
check('local_curl_field_evolution_intertwining',clean(filter*L-L*filter)==s.zeros(6) and clean(s.diag(k.T,k.T)*filter)==s.zeros(2,6))

# Directly sum the birth at either endpoint of an initially independent pair.
U=[2*e for e,b in features];V=[b for e,b in features]
adjacent=[]
for observable in (U,V):
    endpoint=beta*(1-rho)*sum((rho*s.Rational(1,14)*observable[b][0]*sum(observable[a][0]*(1+j*T[a,b]) for a in range(14)) for b in range(14)),s.S.Zero)
    adjacent.append(s.factor(2*endpoint))
check('exact_initial_neighbor_covariance_with_both_birth_endpoints',all(s.factor(q-16*beta*j*rho*(1-rho)/7)==0 for q in adjacent))
gain=s.exp(6*j*(rho-s.Symbol('rho_start'))/7)
check('integrated_native_linear_gain',s.simplify(s.diff(gain,rho)*14*beta*(1-rho)-lam*gain)==0)

sx=s.Matrix(s.symbols('sx sy sz',real=True));curl=s.I*cross(sx)
check('exact_lattice_Gauss_and_curl_covariance',clean(sx.T*curl)==s.zeros(1,3) and clean(curl*curl.conjugate().T-(sx.dot(sx)*s.eye(3)-sx*sx.T))==s.zeros(3))
actions=0
for perm in permutations(range(3)):
    parity=(-1)**sum(perm[a]>perm[b] for a in range(3) for b in range(a+1,3))
    for signs in product((-1,1),repeat=3):
        Q=s.zeros(3)
        for col in range(3):Q[perm[col],col]=signs[col]
        determinant=parity*np.prod(signs)
        assert clean(cross(Q*k)*Q-determinant*Q*C)==s.zeros(3)
        assert clean(cross(Q*k)*(determinant*Q)-Q*C)==s.zeros(3)
        actions+=1
check('polar_axial_curl_readout_under_all_cubic_actions',actions==48)

N=7;rng=np.random.default_rng(20260921201)
table=np.array([[0]*6]+[[*map(int,2*e),*map(int,b)] for e,b in features],dtype=np.int64)
labels=rng.integers(0,15,size=(N,N,N));labels[0,0,0]=0
def difference(a,axis):return np.roll(a,-1,axis)-np.roll(a,1,axis)
def curl2(a):
    return np.stack([difference(a[...,2],1)-difference(a[...,1],2),
                     difference(a[...,0],2)-difference(a[...,2],0),
                     difference(a[...,1],0)-difference(a[...,0],1)],axis=-1)
def divergence2(a):return sum(difference(a[...,i],i) for i in range(3))
def audit(state):
    f=table[state];assert not np.any(divergence2(curl2(f[...,:3]))) and not np.any(divergence2(curl2(f[...,3:])))
audit(labels)
for newlabel in range(1,15):
    state=labels.copy();state[0,0,0]=newlabel;audit(state)
state=labels.copy();state[1,1,1],state[1,1,2]=state[1,1,2],state[1,1,1];audit(state)
check('finite_configuration_identity_after_all_birth_labels_and_whole_record_swap',True,dict(side=N,birth_labels=14))

probabilities=[s.factor((1+j*T[a,1])/sum(1+j*T[b,1] for b in range(14))) for a in range(14)]
check('nearest_neighbor_birth_law_is_nonconstant_for_nonzero_j',sum(probabilities)==1 and probabilities[1]==(1+j)/14 and probabilities[0]==(1-j)/14)

report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
            scope='Primary exact finite-event and full fourteen-field algebra. The general entropy proof and native fluctuation replacement are not certified by check counts; the latter is not claimed.')
(HERE/'LOCAL_CURL_NATIVE_FORMATION_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(checks),'PASS',flush=True)
