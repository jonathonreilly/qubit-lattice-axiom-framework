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


print(json.dumps({'scope':'Scoped execution of author prefix only, excluding all finite-history product controls','checks':checks,'details':details,'passed':sum(checks.values()),'failed':sum(not x for x in checks.values())},indent=2))
raise SystemExit(any(not x for x in checks.values()))
