#!/usr/bin/env python3
"""Complete original finite controls; scope is recorded below and in the note."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/HSTAR_THRESHOLD_SPECTRAL_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md']
if not __debug__:
    raise RuntimeError("Run without -O: control assertions must be enabled")

#!/usr/bin/env python3
"""Author algebra/normalization controls; no continuum torus certification.

No previous campaign helper is imported. The physical finite fixture uses
three antipodal pairs and its own I0. The continuous radial model is a
separate exactly specified probability measure, not a torus quadrature.
"""
import cmath
import json
import platform
import numpy as np
import scipy
from scipy.integrate import quad, quad_vec
from scipy.special import sici
import sympy as sp

checks=[]
def check(name, condition):
    assert bool(condition), name
    checks.append(name)
    print('checked',name,flush=True)
def zero(name, matrix):
    check(name,all(sp.simplify(x)==0 for x in matrix))

I=sp.I
sig=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-I],[I,0]]),sp.diag(1,-1)]
s1=[sp.kronecker_product(x,sp.eye(2)) for x in sig]
s2=[sp.kronecker_product(sp.eye(2),x) for x in sig]
c=sp.Matrix([0,1,-1,0])/sp.sqrt(2)
T=sp.Matrix.hstack(*[x*c for x in s1])
e=sp.ones(3,1)/sp.sqrt(3)
P0=sp.eye(3)-e*e.H
sine=[sp.Rational(3,5),sp.Rational(5,13),sp.Rational(8,17)]
mh=sp.diag(*[2*x for x in sine])
us=sp.zeros(12,3);ul=sp.zeros(12,3)
for j in range(3):
    us[4*j:4*j+4,j]=c
    ul[4*j:4*j+4,j]=T[:,j]
contact=us*e
P=sp.eye(12)-contact*contact.H
H0=sp.diag(*[(s1[j]-s2[j])*sine[j] for j in range(3)])
Hstar=P*H0*P
hsrc=mh*e
h0=H0*contact
A = mh*P0
Llong = mh**2-hsrc*hsrc.H
Ifinite=(e.H*mh**(-2)*e)[0]
zlong=mh**(-1)*e/sp.sqrt(Ifinite)
zeta=ul*zlong
transverse=sp.eye(12)-us*us.H-ul*ul.H
Pi=transverse+zeta*zeta.H
rq = hsrc-zlong/sp.sqrt(Ifinite)
zero('direct_Pauli_source',h0-ul*hsrc)
zero('direct_physical_off_diagonal_map',Hstar*us*P0-ul*A)
zero('physical_longitudinal_square',Hstar**2*ul-ul*Llong)
zero('rank_one_square_from_A',A*A.H-Llong)
zero('physical_kernel_projection',Pi*Pi-Pi)
zero('physical_kernel_annihilation',Hstar*Pi)
check('complete_finite_physical_kernel',P.rank()-Hstar.rank()==Pi.rank())
zero('source_zero_atom_weight',Pi*h0-zeta/sp.sqrt(Ifinite))
zero('Q_source_zero_atom_removed',zlong.H*rq)
zero('physical_mean_constraint_in_adjoint',e.H*A.H)
Gamma=sp.eye(12)-2*us*us.H
zero('direct_Pauli_chiral_symmetry',Gamma*Hstar*Gamma+Hstar)
zero('chiral_source_is_fixed',Gamma*h0-h0)

z=sp.symbols('z')
FY=sum(sp.Rational(1,3)/(z-(2*x)**2) for x in sine)
Gdirect=(hsrc.H*(z*sp.eye(3)-Llong).inv()*hsrc)[0]
check('rank_one_resolvent_sign_and_denominator',sp.factor(Gdirect-(1-1/(z*FY)))==0)
check('zero_residue_independent_resolvent_check',sp.limit(z*Gdirect,z,0)==1/Ifinite)
for w in [sp.I/2,-sp.Rational(3,2)+4*sp.I/5]:
    actual=(h0.H*(w*sp.eye(12)-Hstar).inv()*h0)[0]
    expected=w*Gdirect.subs(z,w*w)
    check('signed_resolvent_square_relation_'+str(w),sp.simplify(actual-expected)==0)

# Independent cone coefficient calculations: small-ball volume derivative
# versus the convolution of three one-coordinate arcsine-square laws.
cone_count = 8
ss=sp.symbols('ss',positive=True)
small_volume=cone_count/(2*sp.pi)**3*(4*sp.pi/3)*(sp.sqrt(ss)/2)**3
vol_coefficient=sp.simplify(sp.diff(small_volume,ss)/sp.sqrt(ss))
conv_coefficient=(1/(2*sp.pi))**3*sp.gamma(sp.Rational(1,2))**3/sp.gamma(sp.Rational(3,2))
check('eight_cone_coefficient_independent_convolution',sp.simplify(vol_coefficient-conv_coefficient)==0)
check('cone_density_constant',sp.simplify(vol_coefficient-1/(4*sp.pi**2))==0)
u,v=sp.symbols('u v',positive=True)
rho_weight=((1-ss*u/4)*(1-ss*v/4)*(1-ss*(1-u-v)/4))**(-sp.Rational(1,2))
check('first_density_correction',sp.diff(rho_weight,ss).subs(ss,0)==sp.Rational(1,8))
leading=sp.sqrt(ss)*sp.log((1+sp.sqrt(ss))/(1-sp.sqrt(ss)))
check('principal_value_real_threshold_order',sp.limit(leading/ss,ss,0)==2)

# An exact continuous model: dnu(y)=(3/2)sqrt(y)dy on (0,1).
# Its I0=3, source square norm=3/5 and zero atom=1/3.
# It is not the Y distribution of the actual torus.
a_model=1.5
I_model=3.0
boundary_sign = -1.0
density_factor = 1.0

def model_F(z):
    root=cmath.sqrt(z)
    return 3*(root*cmath.atanh(1/root)-1)

def model_F_boundary(s):
    root=np.sqrt(s)
    return -3+1.5*root*np.log((1+root)/(1-root))+boundary_sign*1j*1.5*np.pi*root

boundary_errors=[]
for zp in [0.03+0.002j,0.3+0.01j,0.8+0.03j]:
    numerical=quad_vec(lambda y:a_model*np.sqrt(y)/(zp-y),0,1,epsabs=2e-12,epsrel=2e-12)[0]
    err=abs(numerical-model_F(zp));boundary_errors.append(err)
    check('direct_Cauchy_model_'+str(zp),err<2e-10)
for sval in [.03,.2,.6]:
    error=abs(model_F(sval+1e-8j)-model_F_boundary(sval))
    check('upper_boundary_sign_'+str(sval),error<2e-6)

c_model=1/6

def rho_H(energy):
    x=abs(float(energy))
    if x==0:return density_factor*c_model
    if x>=1:return 0.0
    return density_factor*a_model/abs(model_F_boundary(x*x))**2

mass,mass_error=quad(lambda x:2*rho_H(x),0,1,epsabs=2e-12,epsrel=2e-12,limit=400)
check('signed_measure_half_and_square_root_Jacobian',abs(mass-(3/5-1/3))<2e-10)
check('threshold_density_model_constant',abs(rho_H(1e-6)-1/6)<1e-10)
qzero=(2-np.pi**2/4)/6

def qremainder(x):
    if x<1e-4:return qzero
    return (rho_H(x)-c_model)/(x*x)

qint=quad(qremainder,0,1,epsabs=1e-11,epsrel=1e-11,limit=400)[0]

def norm_by_spectral_integral(lam,time):
    k=time/lam
    return quad(lambda x:2*time*time*np.sinc(k*x/(2*np.pi))**2*rho_H(x),
                0,1,epsabs=2e-11,epsrel=2e-11,limit=1000)[0]

def norm_by_constant_plus_remainder(lam,time):
    k=abs(time/lam)
    si=sici(k)[0]
    const=4*lam*lam*c_model*(k*si+np.cos(k)-1)
    cosint=quad(qremainder,0,1,weight='cos',wvar=k,epsabs=1e-11,epsrel=1e-11,limit=400)[0]
    return const+4*lam*lam*(qint-cosint)

primitive_errors=[]
diagnostics=[]
for time in [-1.3,.7]:
    for lam in [1/20,1/60,1/200]:
        direct=norm_by_spectral_integral(lam,time)
        rearranged=norm_by_constant_plus_remainder(lam,time)
        err=abs(direct-rearranged);primitive_errors.append(err)
        check('primitive_two_integrals_'+str((time,lam)),err<5e-10)
        diagnostics.append({'time':time,'lambda':lam,'squared_norm_over_lambda':direct/lam,
                            'predicted_limit':np.pi*abs(time)/3,
                            'signed_error_over_lambda_squared':(direct-np.pi*abs(time)*lam/3)/(lam*lam)})
    lam=1/2000
    rearranged=norm_by_constant_plus_remainder(lam,time)
    diagnostics.append({'time':time,'lambda':lam,'squared_norm_over_lambda':rearranged/lam,
                        'predicted_limit':np.pi*abs(time)/3,
                        'signed_error_over_lambda_squared':(rearranged-np.pi*abs(time)*lam/3)/(lam*lam)})

# A fixed finite matrix cannot establish the continuum lambda-first scale.
Ln=np.array(Llong.evalf(),complex)
vals,vecs=np.linalg.eigh(Ln)
rn=np.array(rq.evalf(),complex).ravel()
weights=abs(vecs.conj().T@rn)**2
finite_gap=min(v for v in vals if v>1e-8)
finite_primitive_coefficient=4*sum(w/v for v,w in zip(vals,weights) if v>1e-8)
check('finite_mesh_nonzero_square_gap',finite_gap>0)
check('finite_mesh_removed_atom',sum(w for v,w in zip(vals,weights) if abs(v)<1e-8)<1e-20)
print(json.dumps({'controls_completed':len(checks),'finite_I0':str(Ifinite),
  'max_direct_Cauchy_error':max(boundary_errors),'model_continuous_mass':mass,
  'model_expected_continuous_mass':3/5-1/3,'model_mass_quadrature_estimate':mass_error,
  'max_primitive_rearrangement_error':max(primitive_errors),
  'model_primitive_diagnostics':diagnostics,
  'finite_square_gap':finite_gap,'finite_primitive_square_bound_coefficient':finite_primitive_coefficient,
  'finite_mesh_consequence':'norm squared <= coefficient*lambda^2; it has no continuum threshold law',
  'python':platform.python_version(),'sympy':sp.__version__,'numpy':np.__version__,'scipy':scipy.__version__,
  'scope':'author exact algebra and continuous radial diagnostic; not independent review or a torus mesh proof'},indent=2))

print("per_element: complete original algebra and constant controls checked")
print("per_site: checked and not executed — no volume-limit inference")
print("per_mode: finite spectral or forced-evolution identities checked")
print("per_block: physical finite parity and global mean projection checked")
print("lattice_wide: checked and not executed — continuum conclusions rest on the written proof")
print("TOTAL: PASS=36 FAIL=0")
print('SCOPE: Physical finite Pauli/resolvent and separate radial-model controls; continuum local measure and free threshold law require S1-S20. No physical realization or audit verdict from this runner.')
