#!/usr/bin/env python3
"""Independent exact controls for the supplied fifteen-state exchange.

No primary code is imported. Local rates use integer tensor numerators;
complete four-cycle forward equations use integer transition arrays.
Symbolic field matrices are assembled from species-space tensor Hessians.
"""
from pathlib import Path
from itertools import product, permutations
from fractions import Fraction as F
import json
import platform
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
checks=[]
def check(name, okay, details=None):
    if not okay: raise AssertionError((name,details))
    checks.append(dict(name=name,passed=True,details=details))

electric=[(0,0,0)]
magnetic=[(0,0,0)]
names=['vacancy']
for axis in range(3):
    for sign in (1,-1):
        z=[0,0,0];z[axis]=sign
        electric.append(tuple(z));magnetic.append((0,0,0));names.append(f'A{axis+1}:{sign:+d}')
for sigma in product((-1,1),repeat=3):
    electric.append((0,0,0));magnetic.append(sigma);names.append('B'+str(sigma))
e=np.array(electric,dtype=np.int64);b=np.array(magnetic,dtype=np.int64)
tensor2=(np.cross(e[:,None,:],b[None,:,:])+np.cross(e[None,:,:],b[:,None,:])).transpose(2,0,1)
states=np.array(list(product(range(15),repeat=4)),dtype=np.int64)
size=len(states);l,a,c,r=states.T
drive2=np.stack([tensor2[i,l,a]+tensor2[i,a,r]-tensor2[i,l,c]-tensor2[i,c,r] for i in range(3)])
check('sharp_tensor_and_drive_bounds',np.max(np.abs(tensor2))==1 and np.max(np.abs(drive2))==4,
      dict(gamma=1,max_abs_S='1/2',max_abs_h=2,local_words=size))
witness=states[np.argmax(drive2[2])]
check('sharp_bound_witness',drive2[2].max()==4,dict(axis=3,labels=[names[z] for z in witness],h=2))
for i in range(3):
    swapped=tensor2[i,l,c]+tensor2[i,c,r]-tensor2[i,l,a]-tensor2[i,a,r]
    assert np.array_equal(swapped,-drive2[i])
    balance=np.zeros(size,dtype=np.int64)
    for x in range(4):
        ll,aa,bb,rr=(states[:,(x+d)%4] for d in (-1,0,1,2))
        balance+=tensor2[i,ll,aa]+tensor2[i,aa,rr]-tensor2[i,ll,bb]-tensor2[i,bb,rr]
    assert np.max(np.abs(balance))==0
check('endpoint_antisymmetry_and_complete_cycle_balance',True,dict(axes=3,configurations_per_axis=size))
check('both_fixed_positive_floors',np.min(4+2*np.maximum(drive2,0))==4
      and np.max(4+2*np.maximum(drive2,0))==12
      and np.min(8+drive2)==4 and np.max(8+drive2)==12,
      dict(gamma=1,kappa=1,K=2,rate_range=[1,3]))

lookup={(tuple(e[z]),tuple(b[z])):z for z in range(15)}
rotations=0
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        R=np.zeros((3,3),dtype=np.int64)
        for old in range(3): R[perm[old],old]=signs[old]
        if round(np.linalg.det(R))!=1: continue
        labels=np.array([lookup[(tuple(R@e[z]),tuple(R@b[z]))] for z in range(15)])
        transformed=tensor2[:,labels[:,None],labels[None,:]]
        assert np.array_equal(transformed,np.einsum('ij,jab->iab',R,tensor2))
        rotations+=1
check('proper_cubic_tensor_covariance',rotations==24,dict(rotations=rotations,pairs_per_rotation=225))

def cross(x,y):
    return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
weights=np.arange(1,16,dtype=np.int64);den=int(sum(weights))
prob=[F(int(w),den) for w in weights]
E=[sum(prob[z]*int(e[z,i]) for z in range(15)) for i in range(3)]
B=[sum(prob[z]*int(b[z,i]) for z in range(15)) for i in range(3)]
P=cross(E,B)
mass=np.prod(weights[states],axis=1)
exact_currents=[]
for i in range(3):
    target=[prob[z]*(cross(e[z],B)[i]+cross(E,b[z])[i]-2*P[i]) for z in range(15)]
    for variant,rate4 in [('positive_part',4+2*np.maximum(drive2[i],0)),('linear',8+drive2[i])]:
        raw=np.zeros(15,dtype=np.int64)
        np.add.at(raw,a,mass*rate4);np.add.at(raw,c,-mass*rate4)
        actual=[F(int(value),4*den**4) for value in raw]
        assert actual==target and sum(actual)==0
        exact_currents.append(dict(axis=i+1,variant=variant,current=[str(x) for x in actual]))
check('direct_biased_product_currents_both_rates',True,
      dict(E=[str(x) for x in E],B=[str(x) for x in B],potential=[str(x) for x in P],cases=exact_currents))

p=sp.Matrix([sp.Rational(x.numerator,x.denominator) for x in prob[1:]])
C=sp.diag(*p)-p*p.T
one=sp.ones(14,1)
for i in range(3):
    Hess=sp.Matrix(tensor2[i,1:,1:].tolist())
    gradient=Hess*p;potential=(p.T*gradient)[0]/2
    J=C*gradient
    jac=sp.diag(*[x-2*potential for x in gradient])+sp.diag(*p)*(Hess-2*one*gradient.T)
    assert jac*C==(jac*C).T
    assert list(J)==[sp.Rational(x.numerator,x.denominator) for x in
        [prob[z]*(cross(e[z],B)[i]+cross(E,b[z])[i]-2*P[i]) for z in range(1,15)]]
check('chemical_potential_current_and_entropy_at_biased_product',True)

# Field basis: rho_A,rho_B,E(3),B(3),two A axis imbalances,
# three B pair characters and the B triple character.
rows=[]
rows.append([int(z<=6) for z in range(1,15)])
rows.append([int(z>=7) for z in range(1,15)])
rows += [[int(e[z,i]) for z in range(1,15)] for i in range(3)]
rows += [[int(b[z,i]) for z in range(1,15)] for i in range(3)]
rows += [[sp.Rational(int(e[z,i]**2),1)-sp.Rational(int(z<=6),3) for z in range(1,15)] for i in range(2)]
rows += [[int(b[z,i]*b[z,j]) for z in range(1,15)] for i,j in ((0,1),(0,2),(1,2))]
rows += [[int(np.prod(b[z])) for z in range(1,15)]]
T=sp.Matrix(rows)
check('fourteen_field_basis_is_complete',T.rank()==14)
rA,rB,gamma,kx,ky,kz,z=sp.symbols('rho_A rho_B gamma kx ky kz z',real=True)
ks=(kx,ky,kz)
crossK=sp.Matrix([[0,-kz,ky],[kz,0,-kx],[-ky,kx,0]])
HessK=sum((gamma*ks[i]*sp.Matrix(tensor2[i,1:,1:].tolist()) for i in range(3)),sp.zeros(14))
piso=sp.Matrix([rA/6]*6+[rB/8]*8)
check('isotropic_potential_gradient_vanishes',HessK*piso==sp.zeros(14,1))
A=(T*sp.diag(*piso)*HessK*T.inv()).applyfunc(sp.simplify)
expected=sp.zeros(14)
expected[2:5,5:8]=-gamma*rA*crossK/3
expected[5:8,2:5]=gamma*rB*crossK
check('complete_curl_signs_and_eight_spectator_fields',A==expected)
speed2=gamma**2*rA*rB/3
poly=A.charpoly(z)
check('full_fourteen_mode_spectrum',sp.factor(poly.as_expr()-poly.gen**10*(poly.gen**2-speed2*(kx*kx+ky*ky+kz*kz))**2)==0,
      dict(propagating_modes=4,zero_speed_modes=10,speed_squared='gamma^2 rho_A rho_B / 3'))
Cfield=(T*(sp.diag(*piso)-piso*piso.T)*T.T).applyfunc(sp.simplify)
check('field_covariance_normalizations',Cfield[2:5,2:5]==rA*sp.eye(3)/3
      and Cfield[5:8,5:8]==rB*sp.eye(3) and Cfield[2:5,5:8]==sp.zeros(3)
      and (A*Cfield-(A*Cfield).T).applyfunc(sp.simplify)==sp.zeros(14))

# Fully occupied model: use its own thirteen independent probabilities,
# with the last B label as reference. No vacancy entropy inverse is used.
pfull=piso.subs(rB,1-rA);q=pfull[:13,0]
C13=sp.diag(*q)-q*q.T
D=sp.Matrix.vstack(sp.eye(13),-sp.ones(1,13))
reduced_Hess=D.T*HessK*D
keep=[i for i in range(14) if i!=1]
T13=T[keep,:]*D
A13=(T13*C13*reduced_Hess*T13.inv()).applyfunc(sp.simplify)
expected13=expected[keep,keep].subs(rB,1-rA)
check('full_occupancy_independent_coordinate_derivation',A13==expected13 and T13.rank()==13)
poly13=A13.charpoly(z)
check('full_occupancy_thirteen_mode_spectrum',
      sp.factor(poly13.as_expr()-poly13.gen**9*(poly13.gen**2-gamma**2*rA*(1-rA)*(kx*kx+ky*ky+kz*kz)/3)**2)==0,
      dict(propagating_modes=4,zero_speed_modes=9))
check('full_occupancy_entropy_metric_is_nonsingular',
      C13.subs(rA,sp.Rational(3,7)).det()==sp.Rational(1,14)**14,
      dict(equal_label_speed_at_abs_gamma_1='2/7'))

beta,v,rho=sp.symbols('beta vacancy rho',real=True)
R=-beta*sp.ones(14)
Rfield=(T*R*T.inv()).applyfunc(sp.simplify)
expectedR=sp.zeros(14);expectedR[:2,:2]=sp.Matrix([[-6*beta,-6*beta],[-8*beta,-8*beta]])
check('uniform_birth_all_field_reaction',Rfield==expectedR)
noise=T*T.T
check('formation_noise_all_vector_components',noise[2:5,2:5]==2*sp.eye(3)
      and noise[5:8,5:8]==8*sp.eye(3) and noise[2:5,5:8]==sp.zeros(3)
      and noise.rank()==14)
TM=T[2:8,:].copy();TM[3:6,:]=TM[3:6,:]/2
peq=sp.ones(14,1)*rho/14
check('equal_label_Maxwell_covariance_and_noise',
      (TM*(sp.diag(*peq)-peq*peq.T)*TM.T).applyfunc(sp.simplify)==rho*sp.eye(6)/7
      and TM*TM.T==2*sp.eye(6))
Aeq=A.subs({rA:3*rho/7,rB:4*rho/7})
rescale=sp.diag(1,1,1,sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,2))
check('equal_label_common_curl_coefficient',
      (rescale*Aeq[2:8,2:8]*rescale.inv()).applyfunc(sp.simplify)
      ==sp.BlockMatrix([[sp.zeros(3),-2*gamma*rho*crossK/7],[2*gamma*rho*crossK/7,sp.zeros(3)]]).as_explicit())
later={rA:sp.Rational(89,280),rB:sp.Rational(57,140),gamma:1,kx:1,ky:2,kz:-1}
earlier={rA:sp.Rational(1,5),rB:sp.Rational(1,4),gamma:1,kx:1,ky:2,kz:-1}
A0=A.subs(earlier);A1=A.subs(later)
check('unequal_orbits_need_time_ordering',A0*A1!=A1*A0)

# Complete fifteen-state four-cycle generator with N=4 acceleration and
# beta=1/3. Q3 stores three times each actual macroscopic rate.
ids=np.arange(size,dtype=np.int64)
powers=np.array([15**3,15**2,15,1],dtype=np.int64)
exchange=[];birth=[]
for x in range(4):
    y=(x+1)%4
    ll,aa,bb,rr=(states[:,(x+d)%4] for d in (-1,0,1,2))
    h2=tensor2[0,ll,aa]+tensor2[0,aa,rr]-tensor2[0,ll,bb]-tensor2[0,bb,rr]
    c4=4+2*np.maximum(h2,0)
    dest=ids+(states[:,y]-states[:,x])*powers[x]+(states[:,x]-states[:,y])*powers[y]
    exchange.append((ids,dest,3*c4))
    vacant=ids[states[:,x]==0]
    for label in range(1,15): birth.append((vacant,vacant+label*powers[x],np.ones(len(vacant),dtype=np.int64)))
src=np.concatenate([x[0] for x in exchange+birth]);dst=np.concatenate([x[1] for x in exchange+birth]);q3=np.concatenate([x[2] for x in exchange+birth])
population=(states==1).sum(axis=1)
du=population[dst]-population[src]
Gu3=np.zeros(size,dtype=np.int64);Gam3=np.zeros(size,dtype=np.int64)
np.add.at(Gu3,src,q3*du);np.add.at(Gam3,src,q3*du*du)
complete=[]
for label,w in [('interior_equal',[14]+[1]*14),('interior_biased',[14]+list(range(1,15))),
                ('empty',[1]+[0]*14),('fully_occupied',[0]+[1]*14)]:
    w=np.array(w,dtype=np.int64);total=int(sum(w));m=np.prod(w[states],axis=1)
    forward=np.zeros(size,dtype=np.int64)
    np.add.at(forward,dst,m[src]*q3);np.add.at(forward,src,-m[src]*q3)
    derivative=np.zeros(size,dtype=np.int64)
    for x in range(4):
        other=np.prod(w[states[:,[i for i in range(4) if i!=x]]],axis=1)
        derivative+=w[0]*np.where(states[:,x]==0,-14,1)*other
    assert np.array_equal(forward,derivative)
    energy_left=int(np.dot(derivative,population**2))
    energy_right=int(np.dot(m,2*population*Gu3+Gam3))
    assert energy_left==energy_right
    stale=F(-int(np.dot(m,population*Gu3)),3*total**4)
    bracket=F(int(np.dot(m,Gam3)),3*total**4)
    pp=sp.Matrix([sp.Rational(int(a),total) for a in w[1:]])
    vv=sp.Rational(int(w[0]),total);cov=sp.diag(*pp)-pp*pp.T;react=-sp.ones(14)/3
    cdot=vv*(sp.eye(14)-sp.ones(14,1)*pp.T-pp*sp.ones(1,14))/3
    assert cdot==react*cov+cov*react.T+vv*sp.eye(14)/3
    if label=='empty': assert bracket==sp.Rational(4,3) and stale==0
    if label.startswith('interior'): assert stale<0
    complete.append(dict(case=label,forward_equation_max_integer_residual=0,
        evolving_energy_integer_residual=0,incorrect_stationary_energy=str(stale),
        actual_count_bracket=str(bracket),birth_covariance_identity=True))
check('complete_cycle_forward_energy_and_birth_covariance',True,
      dict(states=size,transition_array_entries=len(src),cases=complete))

# Configuration Fourier sign, independently from the symbolic curl algebra.
phre=np.array([1,0,-1,0]);phim=np.array([0,-1,0,1])
features=np.concatenate((e,b),axis=1)
Ure=np.einsum('x,sxf->sf',phre,features[states]);Uim=np.einsum('x,sxf->sf',phim,features[states])
dr=np.zeros_like(Ure);di=np.zeros_like(Uim);jr=np.zeros_like(Ure);ji=np.zeros_like(Uim)
for x,(ss,dd,rr) in enumerate(exchange):
    dr+=rr[:,None]*(Ure[dd]-Ure[ss]);di+=rr[:,None]*(Uim[dd]-Uim[ss])
    delta=features[states[:,x]]-features[states[:,(x+1)%4]]
    jr+=(rr//3)[:,None]*phre[x]*delta;ji+=(rr//3)[:,None]*phim[x]*delta
check('complete_configuration_Fourier_orientation',np.array_equal(dr,3*(-jr+ji)) and np.array_equal(di,3*(-jr-ji)),
      dict(configurations=size,features=6,phase='exp(-i pi x/2)'))
empty_half=sp.ones(14,1)/28
empty_cov=sp.diag(*empty_half)-empty_half*empty_half.T
check('empty_initial_state_requires_formation_noise',sp.trace(empty_cov)==sp.Rational(27,56),
      dict(initial_field='identically zero',at_vacancy_half_trace_covariance='27/56'))

result=dict(scope='Independent pre-source exact finite and symbolic controls; no stochastic simulation or primary code.',
    environment=dict(python=platform.python_version(),numpy=np.__version__,sympy=sp.__version__),
    count=len(checks),checks=checks,
    limitations=['The complete finite generator is a directional four-cycle control; the three-dimensional limits rest on the reconstructed proofs.',
                 'No finite-N fluctuation limit is inferred from a spectrum alone.',
                 'No physical electromagnetism, qubit realization or parity extension is certified by these checks.'])
text=json.dumps(result,indent=2)+'\n'
(HERE/'RESULTS.json').write_text(text);print(text,end='')
