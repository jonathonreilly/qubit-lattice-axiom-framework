#!/usr/bin/env python3
"""Independent symbolic/analytic/Bessel checks; never imports the author runner."""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[name] = '1'
import datetime as dt
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import sys
import time
import traceback
import warnings

import mpmath as mp
import numpy as np
from scipy.integrate import quad
from scipy.special import jv
import sympy as s

OUT = Path(__file__).resolve().parent
PINS = OUT / 'SOURCE_PINS_v1.json'
SNAP = OUT / 'pinned_source'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def conservation():
    x, y, z, t = s.symbols('x y z t', real=True)
    coords = (x, y, z)
    alpha, mu, beta, G = s.symbols('alpha mu beta G', positive=True)
    u = [s.Function('u' + str(i))(*coords, t) for i in range(3)]
    ut = [s.diff(v, t) for v in u]
    grad = [[s.diff(v, q) for v in u] for q in coords]
    div = sum(grad[i][i] for i in range(3))
    kinetic = alpha * sum(v*v for v in ut)
    spatial = mu * sum(v*v for row in grad for v in row) + beta*div**2
    h = (kinetic + spatial)/(8*s.pi*G)
    lagrangian = (kinetic - spatial)/(8*s.pi*G)
    A = [[mu*grad[j][i] + (beta*div if i == j else 0)
          for i in range(3)] for j in range(3)]
    op = [alpha*s.diff(u[i], t, 2) - sum(s.diff(A[j][i], coords[j]) for j in range(3))
          for i in range(3)]
    flux = [-sum(ut[i]*A[j][i] for i in range(3))/(4*s.pi*G) for j in range(3)]
    balance = s.diff(h, t) + sum(s.diff(flux[j], coords[j]) for j in range(3))
    assert s.expand(balance - sum(ut[i]*op[i] for i in range(3))/(4*s.pi*G)) == 0
    # Full field momentum makes explicit why matter COM need not be exact at higher order.
    for i in range(3):
        momentum = -alpha*sum(ut[k]*grad[i][k] for k in range(3))/(4*s.pi*G)
        stress = [sum(A[j][k]*grad[i][k] for k in range(3))/(4*s.pi*G)
                  + (lagrangian if i == j else 0) for j in range(3)]
        residual = s.diff(momentum,t)+sum(s.diff(stress[j],coords[j]) for j in range(3))
        assert s.expand(residual + sum(op[k]*grad[i][k] for k in range(3))/(4*s.pi*G)) == 0
    return {'field_energy_identity': 'dh/dt+div(S)=sum(u_t dot operator)/(4*pi*G)=-rho*phi_t',
            'field_momentum_identity': 'dP_field/dt=+integral(rho grad(phi)); matter force cancels it',
            'matter_interaction_cancellation': '-J.grad(phi) + rho*phi_t + J.grad(phi) - rho*phi_t = 0',
            'static_half_counting': 'E_field=-1/2 integral(rho phi); H_static=T+1/2 integral(rho phi)',
            'symbolic_local_energy_residual': 0, 'symbolic_momentum_residuals': [0,0,0]}


def mechanics_and_multipoles():
    G,N,D,m1,m2,a,z,Omega,t = s.symbols('G N D m1 m2 a z Omega t',positive=True)
    total=m1+m2; reduced=m1*m2/total
    r=s.sqrt(a*a+z*z)
    U=-G*m1*m2*((N+D)/r+(N-D)*z*z/r**3)/2
    kvertical=s.simplify(s.series(U,z,0,3).removeO().coeff(z,2)*2/reduced)
    om2=G*(N+D)*total/(2*a**3)
    assert s.simplify(kvertical-G*(3*D-N)*total/(2*a**3))==0
    assert s.simplify(s.diff(U,a).subs(z,0)/(a*reduced)-om2)==0
    orbit=s.Matrix([a*s.cos(Omega*t),a*s.sin(Omega*t),0])
    # Compute I from both mass locations, not by supplying a precomputed moment.
    x1=m2/total*orbit; x2=-m1/total*orbit
    dipole=s.simplify(m1*x1+m2*x2)
    moment=s.simplify(m1*x1*x1.T+m2*x2*x2.T)
    assert dipole==s.zeros(3,1)
    assert s.simplify(moment-reduced*orbit*orbit.T)==s.zeros(3)
    assert s.simplify(s.diff(s.trace(moment),t))==0
    third=s.simplify(moment.diff(t,3).subs(t,0))
    expected=s.Matrix([[0,-4,0],[-4,0,0],[0,0,0]])*reduced*a*a*Omega**3
    assert third==expected
    # Spherical monomial moments supply an independent angular-integration route.
    def sphere_even(i,j,k):
        df=lambda n:s.factorial2(n) if n>=0 else s.Integer(1)
        return 4*s.pi*df(2*i-1)*df(2*j-1)*df(2*k-1)/df(2*(i+j+k)+1)
    cross=sphere_even(1,1,0); three=sphere_even(1,1,1)
    angular=[s.simplify(64*(cross-three)),s.simplify(64*three)]
    assert angular==[512*s.pi/35,256*s.pi/105]
    coefficients=[s.simplify(v/(16*s.pi)) for v in angular]
    assert coefficients==[s.Rational(32,35),s.Rational(16,105)]
    # Finite-speed density expansion includes the Taylor 1/2, not a trace-free substitution.
    I=s.Function('I')(t); c, n=s.symbols('c n',positive=True)
    amplitude=-G/(c*c)*n*n*s.diff(I,t,2)/(2*c*c)
    assert s.simplify(amplitude+G*n*n*s.diff(I,t,2)/(2*c**4))==0
    Q=moment-s.eye(3)*s.trace(moment)/3
    Q3=s.simplify(Q.diff(t,3))
    Qnorm=s.trigsimp(sum(v*v for v in Q3))
    assert s.simplify(Qnorm-32*reduced**2*a**4*Omega**6)==0
    return {'vertical_frequency_squared':str(kvertical),'orbital_frequency_squared':str(om2),
            'dipole_exact_conservative':str(dipole),'moment_third_at_zero':str(third),
            'angular_contraction_integrals_over_mred2_a4_Omega6':[str(v) for v in angular],
            'power_coefficients':[str(v) for v in coefficients],
            'GR_comparator_quadrupole_norm':str(Qnorm),
            'period_balance':'dlog(P_orb)/dt = -3 P_rad/(2 |E_orbit|)',
            'tail_trace_not_discarded':True}


def retarded_middle_and_flux():
    tau, w = s.symbols('tau w',real=True,nonzero=True)
    primitive=s.exp(s.I*w*tau)*(tau/(s.I*w)+1/w**2)
    assert s.simplify(s.diff(primitive,tau)-tau*s.exp(s.I*w*tau))==0
    mp.mp.dps=65
    errors=[]
    for radius in (mp.mpf('2'),mp.mpf('5')):
        omega=mp.mpf('1.3'); cL=mp.mpf('1.2'); cT=mp.mpf('.7')
        low=radius/cL; high=radius/cT
        primitive_mp=lambda q:mp.exp(1j*omega*q)*(q/(1j*omega)+1/omega**2)
        direct=mp.quad(lambda q:q*mp.exp(1j*omega*q),[low,high])
        exact=primitive_mp(high)-primitive_mp(low)
        errors.append(str(abs(direct-exact)))
        assert abs(direct-exact)<mp.mpf('1e-60')
    # Projectors at a non-axis direction with both polarizations nonzero.
    direction=s.Matrix([s.Rational(1,3),s.Rational(2,3),s.Rational(2,3)])
    PL=direction*direction.T; PT=s.eye(3)-PL
    assert PT*PL==s.zeros(3) and PT*PT==PT and PL*PL==PL
    e=s.Matrix([1,0,0]); AT,AL,alpha,cT,cL=s.symbols('AT AL alpha cT cL',real=True,positive=True)
    velocity_T=AT*PT*e; velocity_L=AL*PL*e
    velocity=velocity_T+velocity_L
    traction=alpha*cT*velocity_T+alpha*cL*velocity_L
    assert s.expand(velocity.dot(traction)-alpha*(cT*velocity_T.dot(velocity_T)+cL*velocity_L.dot(velocity_L)))==0
    return {'primitive':str(primitive),'primitive_numeric_errors':errors,
            'fixed_frequency_middle_bound':'|middle scalar| <= (1/cL+1/cT)/(|omega| r^2) + 2/(omega^2 r^3)',
            'DC_middle_scalar':'(1/cT^2-1/cL^2)/(2r)',
            'fixed_frequency_and_large_wave_zone_required':True,
            'projector_cross_terms_exactly_zero':True,
            'flux':'alpha/(4*pi*G) [cT |u_t,T|^2 + cL |u_t,L|^2]',
            'quadrupole_power_mode_factor':'G/(16*pi*alpha*c_s^7)'}


def bessel_power(q,eps, m1=.5,m2=.5, G=1.,alpha=1.,Omega=1., a=None):
    cT=1/math.sqrt(alpha*q); cL=1/math.sqrt(alpha)
    if a is None:a=eps*cT/Omega
    total=m1+m2; r1=m2/total*a; r2=m1/total*a
    powers=[]; odd=[]; errors=[]
    for mode,c in enumerate((cT,cL)):
        mode_power=0.;odd_power=0.;error=0.
        for harmonic in range(1,33):
            if m1==m2 and harmonic%2:continue
            omega=harmonic*Omega
            def integrand(z):
                transverse=math.sqrt(max(0.,1-z*z))
                amp=m1*jv(harmonic,omega*r1*transverse/c)+((-1)**harmonic)*m2*jv(harmonic,omega*r2*transverse/c)
                weight=(1-z*z) if mode==0 else z*z
                return weight*float(amp)**2
            val,err=quad(integrand,-1,1,epsabs=1e-120,epsrel=2e-12,limit=100)
            factor=G*omega**2/(alpha*c**3)
            mode_power+=factor*val;error+=factor*err
            if harmonic%2:odd_power+=factor*val
        powers.append(mode_power);odd.append(odd_power);errors.append(error)
    reduced=m1*m2/total
    leading=[G*reduced**2*a**4*Omega**6/alpha*32/(35*cT**7),
             G*reduced**2*a**4*Omega**6/alpha*16/(105*cL**7)]
    return np.array(powers),np.array(leading),odd,errors


def harmonic_checks(author):
    rows=[]
    for row in author['controls']:
        q=row['q'];eps=row['a_Omega_over_cT']
        actual,leading,odd,quaderr=bessel_power(q,eps)
        stored=np.array(row['exact_source_harmonic_power'])
        relative=np.abs(actual-stored)/actual
        assert np.max(relative)<2e-8
        assert np.allclose(leading,row['leading_power'],rtol=3e-14,atol=0)
        # Rigorous geometric bound for all missing n>=18 at equal antipodal masses.
        # |J_n(n eps sin(theta)/2)| <= [(3 eps/4)/(1-eps^2/16)]^n.
        epsilon=F(str(eps));b=3*epsilon/(4*(1-epsilon*epsilon/16));v=b*b;m=18
        tail_sum=v**m*(F(m*m)/(1-v)+F(2*m)*v/(1-v)**2+v*(1+v)/(1-v)**3)
        upper=2*(q**1.5+1)*float(tail_sum)
        coeff=(leading[0]*F(4,27)+leading[1]/(9*q))/sum(leading)
        deviation=float(sum(actual)/sum(leading)-1)
        rows.append({'q':q,'epsilon_T':eps,'bessel_power_1_to_32':actual.tolist(),
                     'relative_difference_from_author':relative.tolist(),
                     'adaptive_quadrature_error_estimates':quaderr,
                     'fractional_leading_correction':deviation,
                     'predicted_epsilon_squared_coefficient':float(coeff),
                     'harmonics_ge18_total_power_bound':upper,
                     'bound_over_leading':upper/sum(leading)})
    for q in sorted({r['q'] for r in rows}):
        sequence=[r for r in rows if r['q']==q]
        for previous,current in zip(sequence[:-1],sequence[1:]):
            ratio=abs(previous['fractional_leading_correction']/current['fractional_leading_correction'])
            assert 3.9<ratio<4.1
        last=sequence[-1]
        assert abs(-last['fractional_leading_correction']/last['epsilon_T']**2-last['predicted_epsilon_squared_coefficient'])<1e-4
    # Unequal masses: no leading density dipole, but higher odd harmonics survive.
    unequal=[]
    for eps in (.06,.03,.015):
        actual,leading,odd,error=bessel_power(2.,eps,.3,.7)
        unequal.append({'epsilon_T':eps,'total_power':float(sum(actual)),
                        'fractional_leading_correction':float(sum(actual)/sum(leading)-1),
                        'odd_harmonic_power_fraction':float(sum(odd)/sum(actual))})
    assert all(r['odd_harmonic_power_fraction']>0 for r in unequal)
    # One self-consistent slow circular input, unlike the author's prescribed harmonic controls.
    q=2.;eps=.03;cT=1/math.sqrt(q);Geq=(q+1)/2;total=1.;red=.21
    a=Geq*total/(eps*cT)**2;Omega=math.sqrt(Geq*total/a**3)
    assert math.isclose(a*Omega/cT,eps,rel_tol=2e-15)
    actual,leading,odd,error=bessel_power(q,eps,.3,.7,Omega=Omega,a=a)
    binding=Geq*.3*.7/(2*a)
    damping=float(sum(leading)*2*math.pi/(Omega*binding))
    assert damping<1e-5
    return {'equal_mass_rows':rows,'unequal_mass_controls':unequal,
            'self_consistent_slow_control':{'q':q,'a':a,'Omega':Omega,'epsilon_T':eps,
                'potential_compactness_GeqM_over_a_cT2':Geq*total/(a*cT*cT),
                'relative_binding_loss_per_orbit':damping,
                'point_multipole_only_no_internal_body_model':True},
            'coefficient_formula':'rho_h(n)=i^h [m1 J_h(h Omega r1 sin(theta)/c)+(-1)^h m2 J_h(h Omega r2 sin(theta)/c)] up to convention conjugation',
            'equal_mass_odd_harmonics_exactly_zero':True,
            'no_author_runner_import_or_execution':True}


def calibration(author):
    q,cE,cL,G,D,alpha=s.symbols('q cE cL G D alpha',positive=True)
    cT=cL/s.sqrt(q)
    power=G/alpha*(s.Rational(32,35)/cT**7+s.Rational(16,105)/cL**7)
    comparator=s.Rational(32,5)*G*D*(q+1)/(2*cE**5)
    ratio=s.simplify((power/comparator).subs(alpha,1/(D*cL*cL)))
    expected=(cE/cL)**5*(6*q**s.Rational(7,2)+1)/(21*(q+1))
    assert s.simplify(ratio-expected)==0
    normalized=ratio.subs(cE,cL)
    assert normalized.subs(q,1)==s.Rational(1,6)
    derivative=s.simplify(s.diff(normalized,q))
    numerator=15*q**s.Rational(7,2)+21*q**s.Rational(5,2)-1
    assert s.simplify(derivative-numerator/(21*(q+1)**2))==0
    # Independent rational bisection; no floating root finder.
    polynomial=lambda x:6*x**7-21*x*x-20
    low,high=F(1),F(3,2)
    for _ in range(120):
        middle=(low+high)/2
        if polynomial(middle)<0:low=middle
        else:high=middle
    assert polynomial(low)<0<polynomial(high)
    alo,ahi=map(F,author['calibration_example']['sqrt_q_bracket'])
    assert alo<low<high<ahi
    assert high*high<3
    estimate=float((low+high)/2)**2
    assert math.isclose(estimate,author['calibration_example']['q_approx'],rel_tol=3e-15)
    return {'ratio':str(ratio),'derivative':str(derivative),
            'monotonicity_reason':'For q>=1, derivative numerator >=15+21-1=35>0.',
            'sqrt_q_exact_bracket':[str(low),str(high)],
            'q_exact_bracket':[str(low*low),str(high*high)],'q_approx':estimate,
            'cT_over_cL':1/math.sqrt(estimate),
            'polar_to_equatorial_static_ratio':2*estimate/(estimate+1),
            'vertical_to_orbital_frequency_squared':(3-estimate)/(estimate+1),
            'unique_root_greater_than_one_and_less_than_three':True}


def main():
    started=time.monotonic()
    pins=json.loads(PINS.read_text())
    for row in pins['sources']:
        assert sha(row['source'])==sha(row['snapshot'])==row['sha256']
    author=json.loads((SNAP/'evidence_v1/RESULTS.json').read_text())
    for name,digest in author['source_sha256'].items():assert sha(SNAP/name)==digest
    result={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'checker_sha256':sha(__file__),
            'source_pins_sha256':sha(PINS),'author_results_sha256':sha(SNAP/'evidence_v1/RESULTS.json'),
            'no_author_runner_execution':True,'checks':{},'raw_failures':[]}
    checks=[('energy_and_momentum',conservation),('mechanics_multipoles_and_spherical_moments',mechanics_and_multipoles),
            ('middle_term_and_positive_flux',retarded_middle_and_flux),
            ('independent_Bessel_source_harmonics',lambda:harmonic_checks(author)),
            ('calibration_polynomial',lambda:calibration(author))]
    for name,function in checks:
        try:
            with warnings.catch_warnings(record=True) as captured:
                warnings.simplefilter('always')
                detail=function()
            result['checks'][name]={'passed':True,'detail':detail,'warnings':[str(w.message) for w in captured]}
        except Exception:
            failure={'check':name,'traceback':traceback.format_exc()}
            result['raw_failures'].append(failure)
            result['checks'][name]={'passed':False}
    for row in pins['sources']:
        assert sha(row['source'])==sha(row['snapshot'])==row['sha256']
    result['pass_count']=sum(row['passed'] for row in result['checks'].values())
    result['fail_count']=len(result['raw_failures'])
    result['elapsed_seconds']=time.monotonic()-started
    result['limits']='Symbolic identities plus floating Bessel/quadrature controls, with an analytic harmonic-tail bound; no empirical test, finite-body self-force calculation or relativistic matter bridge.'
    target=OUT/'CHECKS_v1.json'
    with target.open('x') as handle:json.dump(result,handle,indent=2);handle.write('\n')
    print(json.dumps(result,indent=2))
    return 1 if result['raw_failures'] else 0


if __name__=='__main__':
    sys.exit(main())
