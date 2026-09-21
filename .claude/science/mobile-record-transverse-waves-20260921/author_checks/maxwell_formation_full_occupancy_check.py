#!/usr/bin/env python3
"""Exact full-alphabet and birth-covariance controls for the transverse model.

These verify finite matrices and analytic Gaussian formulas. They do not
replace the finite-alphabet limit proofs or select a physical record menu.
"""
from pathlib import Path
from itertools import product
import hashlib,json
import sympy as s

HERE=Path(__file__).resolve().parent
records=[]
def check(name,condition,detail=None):
    assert bool(condition),(name,detail)
    records.append(dict(name=name,passed=True,detail=detail))
    print('PASS:',name,flush=True)
def zero(M):return all(s.expand(x)==0 for x in M)
def cross(x):return s.Matrix([[0,-x[2],x[1]],[x[2],0,-x[0]],[-x[1],x[0],0]])

# Fourteen occupied label vectors, written independently from the current runner.
axes=[s.Matrix(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
cubes=[s.Matrix(v) for v in product((-1,1),repeat=3)]
e=axes+[s.zeros(3,1) for _ in cubes]
b=[s.zeros(3,1) for _ in axes]+cubes
E=s.Matrix.hstack(*e);B=s.Matrix.hstack(*b)
indicator=s.Matrix([[1]*6+[0]*8])
quad=s.Matrix([[v[0]**2-v[1]**2 for v in e],[v[1]**2-v[2]**2 for v in e]])
bpair=s.Matrix([[v[0]*v[1] for v in b],[v[1]*v[2] for v in b],[v[2]*v[0] for v in b]])
btriple=s.Matrix([[v[0]*v[1]*v[2] for v in b]])
T=s.ones(1,14).col_join(indicator).col_join(E).col_join(B).col_join(quad).col_join(bpair).col_join(btriple)
check('complete_fourteen_label_moment_basis',T.shape==(14,14) and T.det()!=0,dict(determinant=str(T.det())))
Ti=T.inv();r,gamma,lam=s.symbols('r gamma lambda',real=True)
kx,ky,kz=s.symbols('kx ky kz',real=True);K=s.Matrix([kx,ky,kz]);CK=cross(K)
p=s.Matrix([r/6]*6+[(1-r)/8]*8)
# Exact derivative of all fourteen species currents at the zero-vector product.
D=s.zeros(14,14)
for a in range(14):
    for c in range(14):
        D[a,c]=gamma*p[a]*K.dot(e[a].cross(b[c])+e[c].cross(b[a]))
A=s.simplify(T*D*Ti)
check('fixed_occupancy_linear_current_has_zero_mass_row_and_column',zero(A[0,:]) and zero(A[:,0]))
A13=A[1:,1:]
expected=s.zeros(13,13)
expected[1:4,4:7]=-gamma*r*CK/3
expected[4:7,1:4]=gamma*(1-r)*CK
check('full_thirteen_field_linearization_retains_every_static_mode',zero(A13-expected))
char=s.factor(A13.charpoly(lam).as_expr())
target=lam**9*(lam**2-gamma**2*r*(1-r)*(kx*kx+ky*ky+kz*kz)/3)**2
# charpoly may create its own same-named dummy symbol; use its returned generator.
charpoly=A13.charpoly();target2=target.subs(lam,charpoly.gen)
check('full_occupancy_characteristic_polynomial',s.factor(charpoly.as_expr()-target2)==0,dict(polynomial=str(s.factor(charpoly.as_expr()))))
C=s.diag(*p)-p*p.T;Cm=s.simplify(T*C*T.T)
check('full_occupancy_entropy_symmetrizer',zero(A*Cm-Cm*A.T))
check('full_occupancy_vector_covariances',Cm[2:5,2:5]==r*s.eye(3)/3 and Cm[5:8,5:8]==(1-r)*s.eye(3) and zero(Cm[2:5,5:8]))
check('no_discarded_extra_wave_modes',s.factor(A13.subs({r:s.Rational(3,7),gamma:1,kx:1,ky:2,kz:2}).rank())==4)

# All fourteen occupied species are independent coordinates when vacancy exists.
pa=s.Matrix(s.symbols('p1:15',positive=True));beta,p0=s.symbols('beta p0',positive=True)
C14=s.diag(*pa)-pa*pa.T;pd=beta*p0*s.ones(14,1)
Cd=s.diag(*pd)-pd*pa.T-pa*pd.T
R=-beta*s.ones(14,14);Q=beta*p0*s.eye(14)
res=Cd-R*C14-C14*R.T-Q
# Probability normalization p0+sum pa=1 is the only substitution needed.
res=res.subs(pa[-1],1-p0-sum(pa[:-1]))
check('fourteen_species_birth_Lyapunov_identity',zero(res))
check('vector_reaction_zero_for_arbitrary_profile',E*s.ones(14,1)==s.zeros(3,1) and B*s.ones(14,1)==s.zeros(3,1))
check('vector_birth_noise',E*Q*E.T==2*beta*p0*s.eye(3) and B*Q*B.T==8*beta*p0*s.eye(3) and zero(E*Q*B.T))
check('equal_label_rescaling_has_equal_noise',4*E*Q*E.T==B*Q*B.T)

# Exact one-site birth semigroup, including the empty initial state.
t,v0=s.symbols('t v0',nonnegative=True)
pinit=s.Matrix(s.symbols('a1:15',nonnegative=True))
pnow=s.Matrix([v0*s.exp(-14*beta*t)]).col_join(pinit+s.ones(14,1)*v0*(1-s.exp(-14*beta*t))/14)
L=s.zeros(15,15)
for a in range(1,15):L[0,a]=beta
L[0,0]=-14*beta
check('exact_one_site_product_birth_trajectory',zero(pnow.diff(t)-L.T*pnow))
rho=1-v0*s.exp(-14*beta*t)
ra=s.Rational(3,7)*rho;rb=s.Rational(4,7)*rho
check('equal_label_late_transverse_speed',s.simplify(gamma**2*ra*rb/3-(2*gamma*rho/7)**2)==0)
qscalar=8*beta*v0*s.exp(-14*beta*t);covscalar=4*rho/7
check('equal_time_covariance_derivative_equals_birth_noise',s.simplify(s.diff(covscalar,t)-qscalar)==0)
check('finite_total_birth_noise',s.integrate(qscalar,(t,0,s.oo))==4*v0/7)

# Full vector propagator, including longitudinal directions and cross signs.
Kv=s.Matrix([1,2,2]);kmag=s.Integer(3);Ck=cross(Kv)
PL=Kv*Kv.T/kmag**2;PT=s.eye(3)-PL
th,ph=s.symbols('theta phi',real=True)
def prop(angle):
    H=PL+s.cos(angle)*PT;off=s.I*s.sin(angle)*Ck/kmag
    return H.row_join(off).col_join((-off).row_join(H))
P=prop(th);generator=s.zeros(3,3).row_join(s.I*Ck/kmag).col_join((-s.I*Ck/kmag).row_join(s.zeros(3,3)))
check('transverse_propagator_derivative_and_cross_sign',all(s.trigsimp(x)==0 for x in P.diff(th)-generator*P))
check('propagator_unitary_with_longitudinal_static_sector',all(s.trigsimp(x)==0 for x in P*P.conjugate().T-s.eye(6)))
check('propagator_composition',all(s.trigsimp(s.expand_trig(x))==0 for x in prop(th+ph)-P*prop(ph)))
st=s.symbols('s',nonnegative=True)
phase=2*gamma*kmag/7*((t-st)-v0*(s.exp(-14*beta*st)-s.exp(-14*beta*t))/(14*beta))
check('integrated_phase_derivative_and_zero_interval',s.simplify(s.diff(phase,t)-2*gamma*kmag*rho/7)==0 and s.simplify(phase.subs(t,st))==0)
check('empty_start_covariance_and_integrated_noise',covscalar.subs({v0:1,t:0})==0 and s.simplify(s.integrate(qscalar,(t,0,st)).subs(v0,1)-covscalar.subs({v0:1,t:st}))==0)
# A deliberately different orbit ratio produces a nonzero commutator.
def drift(ra,rb):
    return s.zeros(3,3).row_join(s.I*gamma*ra*Ck/3).col_join((-s.I*gamma*rb*Ck).row_join(s.zeros(3,3)))
D1=drift(s.Rational(1,5),s.Rational(1,3));D2=drift(s.Rational(1,4),s.Rational(2,5))
check('nonproportional_orbit_masses_require_time_ordering',not zero(D1*D2-D2*D1))
report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),sympy_version=s.__version__,checks=records,
            scope='Exact finite-label linearization, birth covariance and Gaussian propagator identities. Conditional finite-mode theorem applications still require their separate proof hypotheses. No native-birth fluctuation theorem or physical Maxwell identification.')
(HERE/'MAXWELL_FORMATION_FULL_OCCUPANCY_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
print('TOTAL:',len(records),'exact controls',flush=True)
