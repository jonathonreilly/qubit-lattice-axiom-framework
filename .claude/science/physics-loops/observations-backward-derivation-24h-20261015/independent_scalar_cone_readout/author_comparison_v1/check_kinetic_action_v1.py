"""Root controls of a general kinetic action and its conditional scalar readout.

Exact constructed mathematics; no empirical arrays or canonical-action inference.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = []
import hashlib
import json
from pathlib import Path
import sys
import time
import sympy as s

start = time.monotonic()
checks = {}
details = {}

def equal(name, expr):
    residual = s.factor(s.cancel(s.expand(expr)))
    checks[name] = bool(residual == 0)
    if residual != 0:
        details[name] = str(residual)

def check(name, condition):
    checks[name] = bool(condition)

eps, q, vt, vz, p0, p1, p2, p3 = s.symbols('eps q vt vz p0 p1 p2 p3', real=True)
dX = eps*q*vt + eps**2*(vt**2-vz**2)/2
lag = p0+p1*dX+p2*dX**2/2+p3*dX**3/6
quad = s.expand(lag).coeff(eps, 2)
equal('quadratic_time_coefficient', s.diff(quad,vt,2)-(p1+q*q*p2))
equal('quadratic_space_coefficient', s.diff(quad,vz,2)+p1)
equal('mixed_principal_coefficient', s.diff(quad,vt,vz))
D = p1+q*q*p2
G = s.diag(-D,p1,p1,p1)
omega,k = s.symbols('omega k', positive=True)
covector = s.Matrix([-omega,0,0,k])
equal('rest_frame_principal_symbol', (covector.T*G*covector)[0]-(-D*omega**2+p1*k**2))
X,j,A = s.symbols('X j A', positive=True)
equal('field_relabeling_sound_ratio', (j*j*p1)/(j*j*p1+2*(X/j**2)*j**4*p2)-p1/(p1+2*X*p2))
equal('conformal_clock_ruler_ratio', ((A*omega)**2/(A*k)**2)-omega**2/k**2)
check('principal_wrong_sign_mutation_detected', s.simplify(p1/(p1-2*X*p2)-p1/(p1+2*X*p2)) != 0)
equal('tensor_light_cone_does_not_depend_on_kinetic_coefficients', s.diff(-omega**2+k**2,p2))

# Derive R_0i0j from the linearized Riemann tensor, not an imported ratio.
t,x,y,z = s.symbols('t x y z',real=True)
Phi,Psi = s.symbols('Phi Psi')
plane = s.exp(s.I*(k*z-omega*t)); coords=[t,x,y,z]
h=s.diag(-2*Psi*plane,-2*Phi*plane,-2*Phi*plane,-2*Phi*plane)
def R(a,b,c,d):
    return (s.diff(h[a,d],coords[b],coords[c])+s.diff(h[b,c],coords[a],coords[d])
            -s.diff(h[a,c],coords[b],coords[d])-s.diff(h[b,d],coords[a],coords[c]))/2
RT=s.simplify(R(0,1,0,1)/plane); RL=s.simplify(R(0,3,0,3)/plane)
equal('transverse_tidal_component',RT+omega**2*Phi)
equal('longitudinal_tidal_component',RL+omega**2*Phi+k**2*Psi)
U,J=s.symbols('U J')
rt=RT.subs({Phi:U-J,Psi:U+J});rl=RL.subs({Phi:U-J,Psi:U+J})
Jread=((1+k*k/(omega*omega))*rt-rl)/(2*k*k)
equal('tidal_slip_cancels_common_potential',Jread-J)
equal('tidal_slip_no_common_potential_dependence',s.diff(Jread,U))
naive=s.cancel(rl/rt-(1-k*k/(omega*omega)))
check('naive_pure_conformal_ratio_fails_with_common_potential',naive!=0)
equal('naive_ratio_recovers_declared_zero_potential_limit',naive.subs(U,0))
details['naive_ratio_discrepancy']=str(naive)
details['finite_common_potential_control']={
    'U':3,'J':5,'omega_squared':13,'k_squared':4,
    'RT':str(rt.subs({U:3,J:5,omega:s.sqrt(13),k:2})),
    'RL':str(rl.subs({U:3,J:5,omega:s.sqrt(13),k:2})),
    'reconstructed_J':str(s.simplify(Jread.subs({U:3,J:5,omega:s.sqrt(13),k:2})))}

c,mu,K1,K2=s.symbols('c mu K1 K2',positive=True)
W1=c*K1+mu;W2=c*K2+mu
equal('two_squared_wavenumbers_cancel_common_mass_squared',(W2-W1)/(K2-K1)-c)
check('one_frequency_phase_ratio_does_not_cancel_mass',s.simplify(W1/K1-c)!=0)
disp=s.sqrt(c*k*k+mu)
check('massive_group_speed_not_principal_speed',s.simplify(s.diff(disp,k)**2-c)!=0)
noise1=s.Rational(1,10);noise2=-s.Rational(1,20)
inferred=((s.Rational(3,5)*9+7+noise2)-(s.Rational(3,5)*4+7+noise1))/5
equal('finite_dispersion_error_bound_saturated',abs(inferred-s.Rational(3,5))-(abs(noise1)+abs(noise2))/5)
details['finite_dispersion_control']={'true_cs_squared':'3/5','fitted_slope':str(inferred),'certified_error':'3/100'}

# Open-domain and finite-accuracy controls. These do not supply an open-domain observation.
phi,lam=s.symbols('phi lam',real=True)
canonical=(1+phi*phi)*X-phi**4
equal('affine_kinetic_form_has_zero_second_X_derivative',s.diff(canonical,X,2))
equal('positive_K_canonical_coordinate_change',s.diff(canonical,X)/(1+phi*phi)-1)
noncanon=X+lam*X*X
cs=s.diff(noncanon,X)/(s.diff(noncanon,X)+2*X*s.diff(noncanon,X,2))
equal('zero_gradient_luminality_countercontrol',cs.subs(X,0)-1)
check('zero_gradient_does_not_force_canonical',s.diff(noncanon,X,2)!=0)
delta=s.Rational(1,10);power=delta/(2*(1-delta))
equal('finite_accuracy_derivative_bound_saturates',1/(1+2*power)-(1-delta))
equal('integrated_kinetic_ratio_bound_saturates',s.log(4**power)-power*s.log(4))

# Finite-history alternatives: exact jets and the full Einstein reference solution.
aa,bb,yy,kap=s.symbols('aa bb yy kap',positive=True)
deformation=lam*(X-aa*yy)**3*(X-bb*yy)**3
dphi=lambda f:-kap*yy*s.diff(f,yy)
jets={'value':deformation,'X':s.diff(deformation,X),'phi':dphi(deformation),
      'XX':s.diff(deformation,X,2),'Xphi':dphi(s.diff(deformation,X)),
      'phiphi':dphi(dphi(deformation))}
for curve,name in [(aa,'a'),(bb,'b')]:
    for jet,value in jets.items():
        equal('curve_'+name+'_zero_jet_'+jet,value.subs(X,curve*yy))
third=s.factor(s.diff(deformation,X,3).subs(X,aa*yy))
equal('transverse_cubic_interaction_survives',third-6*lam*(aa-bb)**3*yy**3)
nonlinear=X+deformation
px=s.diff(nonlinear,X);pxx=s.diff(nonlinear,X,2)
point={aa:1,bb:2,yy:1,X:s.Rational(3,2),lam:s.Rational(1,100)}
check('off_curve_positive_kinetic',px.subs(point)>0)
check('off_curve_positive_hyperbolicity',(px+2*X*pxx).subs(point)>0)
equal('off_curve_scalar_speed_differs', (px/(px+2*X*pxx)).subs(point)-s.Rational(800,809))
details['off_curve_cs_squared']='800/809'
M,t0,T=s.symbols('M t0 T',positive=True);ph0=s.symbols('ph0',real=True)
velocity=s.sqrt(s.Rational(2,3))*M/T;xx=velocity**2/2;H=1/(3*T)
equal('full_Einstein_Friedmann',3*M*M*H*H-xx)
equal('full_Einstein_Raychaudhuri',-2*M*M*s.diff(H,T)-2*xx)
equal('full_Einstein_scalar',s.diff(velocity,T)+3*H*velocity)
ph=s.sqrt(s.Rational(2,3))*M*s.log(T/t0)+ph0
C=M*M*s.exp(s.sqrt(6)*ph0/M)/(3*t0*t0)
equal('full_Einstein_state_curve',xx-C*s.exp(-s.sqrt(6)*ph/M))

deltaX=eps*q*vt+eps**2*(vt*vt-vz*vz)/2
cubic=s.expand(lam*deltaX**3).coeff(eps,3)
equal('local_deformation_cubic_action',cubic-lam*q**3*vt**3)
vtt=s.symbols('vtt')
equal('local_nonlinear_Euler_contribution',s.diff(s.diff(cubic,vt),vt)*vtt-6*lam*q**3*vt*vtt)
details['scope']='General pure-P conformal class; symbolic principal/plane controls and constructed alternatives. No measured scalar, no empirical fit, no global stability or unique action.'
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'software':{'python':sys.version.split()[0],'sympy':s.__version__},
        'checks':checks,'passed':sum(checks.values()),'failed':sum(not v for v in checks.values()),
        'details':details,'elapsed_seconds':time.monotonic()-start}
print(json.dumps(result,indent=2))
raise SystemExit(bool(result['failed']))
