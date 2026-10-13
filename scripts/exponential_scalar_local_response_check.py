#!/usr/bin/env python3
"""Exact local-response identities and raw action derivatives for the note.

No observational data, cosmological fit or history runner is read. The
handwritten domain and operator arguments remain essential to the result.
"""
import json
import sys
import mpmath as mp
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md",
)
COUPLING_DENOMINATOR = 3
NEWTON_LINEAR_COEFFICIENT = 0
DENSITY_FEEDBACK_SIGN = -1
BALL_SOURCE_SIGN = 1
VACUUM_MASS_NUMERATOR = 4
CHECKS = []


def check(name, ok, **detail):
    CHECKS.append(dict(name=name, passed=bool(ok), **detail))


def identity(name, value):
    residue = sp.factor(sp.cancel(sp.trigsimp(value)))
    check(name, residue == 0, residue=str(residue))


def near(name, actual, expected, tolerance):
    error = abs(actual - expected) / max(mp.mpf(1), abs(expected))
    check(name, mp.isfinite(error) and error <= mp.mpf(tolerance),
          scaled_error=mp.nstr(error, 12), tolerance=tolerance)


def exact():
    k, E = sp.symbols('k E', positive=True)
    chi, w, b = sp.symbols('chi w b', real=True)
    a = (1-k)*(1+3*k)/4
    s = (1+k)/(k*(1-3*k))
    d = 1-3*a
    F, J = 1+s*E, 1+d*s*E
    C, Ku = (1+s)*E/F, J/F**2
    # d/du = 2 sqrt(a) E d/dE. This is the exact derivative of log sqrt(C).
    ab = sp.sqrt(a)*E*sp.diff(sp.log(C), E)
    raw_g = sp.cancel(ab**2/Ku)
    raw_beta = -a*d*s*E*F/J**2
    Em = (1+chi/s)/(1-chi)
    gm = k*(1-chi)/(1-COUPLING_DENOMINATOR*k*chi)
    betam = -(1+k+k*(1-3*k)*chi)/(1-3*k*chi)**2
    etam = (1-k*chi)*(1+3*k*chi)/(1-3*k*chi)**2
    B = 4*k**2*(1-3*k)/(1+k)**2
    Rm = 1-B*chi**2/(1-3*k*chi)+NEWTON_LINEAR_COEFFICIENT*k*chi
    chiu = 2*sp.sqrt(a)*(s+chi)*(1-chi)/(1+s)
    chiE = s*(E-1)/F
    identities = {
        'coupling_from_A_and_K': raw_g-a/J,
        'inverse_field_map': chiE.subs(E, Em)-chi,
        'coupling_chi': raw_g.subs(E, Em)-gm,
        'coupling_monotonic_derivative': sp.diff(gm, chi)+k*(1-3*k)/(1-3*k*chi)**2,
        'vacuum_beta': raw_beta.subs(E, 1)+(1+k),
        'beta_chi': raw_beta.subs(E, Em)-betam,
        'density_feedback': betam+gm-DENSITY_FEEDBACK_SIGN*etam,
        'density_sign_change': etam.subs(chi, -1/(3*k)),
        'density_sign_change_field': Em.subs(chi, -1/(3*k))-2*k/(1+k),
        'eta_monotonic': sp.diff(etam, chi)-8*k/(1-3*k*chi)**3,
        'Newton_strength_cancellation': (C*(1+raw_g)/(1+k)).subs(E, Em)-Rm,
        'Newton_strength_derivative': sp.diff(Rm, chi)+B*chi*(2-3*k*chi)/(1-3*k*chi)**2,
        'Newton_vacuum_derivative': sp.diff(Rm, chi).subs(chi, 0),
        'chi_u': (2*sp.sqrt(a)*E*sp.diff(chiE, E)).subs(E, Em)-chiu,
        'vacuum_energy_floor': sp.Rational(3, 2)*s**2*(E-1)**2/F**2-sp.Rational(3, 2)*chiE**2,
        'observational_inversion': gm.subs(chi, (k-b)/(k*(1-3*b)))-b,
        'trapped_minimum': gm.subs(chi, w)-k*(1-w)/(1-3*k*w),
        'trapped_maximum': gm.subs(chi, -w)-k*(1+w)/(1+3*k*w),
        'weak_limit_Newton_second_order': sp.limit((Rm-1)/k**2, k, 0)+4*chi**2,
        'weak_limit_coupling_first_order': sp.limit(gm/k, k, 0)-(1-chi),
    }
    for name, value in identities.items():
        identity('exact.'+name, value)
    # Generalized eta, not only the previously checked vacuum eta=1 case.
    z, r, eta = sp.symbols('z r eta', positive=True)
    interior = (1-sp.sin(z*r)/(z*r*sp.cos(z)))/eta
    exterior = -(sp.tan(z)/z-1)/(eta*r)
    identity('ball.ODE', sp.diff(interior, r, 2)+2*sp.diff(interior, r)/r+z**2*interior-BALL_SOURCE_SIGN*z**2/eta)
    identity('ball.field_match', interior.subs(r, 1)-exterior.subs(r, 1))
    identity('ball.derivative_match', sp.diff(interior, r).subs(r, 1)-sp.diff(exterior, r).subs(r, 1))
    identity('ball.center_regular', sp.limit(sp.diff(interior, r), r, 0))
    identity('ball.charge_series', sp.series(3*(sp.tan(z)-z)/z**3, z, 0, 6).removeO()-(1+2*z**2/5+17*z**4/105))
    # Algebraic negative controls, not damaged full-script runs.
    for name, residual in {
        'wrong_Newton_linear_term': Rm-(1-k*chi),
        'wrong_density_sign': 2*etam,
        'wrong_coupling_denominator': gm-k*(1-chi)/(1-2*k*chi),
        'wrong_inversion': gm.subs(chi, (k-b)/k)-b,
    }.items():
        val = residual.subs({k:sp.Rational(1, 100), chi:sp.Rational(1, 3), b:sp.Rational(1, 79999)})
        check('algebraic_negative_control.'+name, sp.cancel(val) != 0, residue=str(sp.cancel(val)))
    return {'g':str(gm), 'beta':str(betam), 'eta':str(etam), 'Newton_ratio':str(Rm), 'chi_u':str(chiu)}


def quantities(k, u):
    a=(1-k)*(1+3*k)/4; al=mp.sqrt(a); s=(1+k)/(k*(1-3*k))
    E=mp.exp(2*al*u); F=1+s*E; J=1+(1-3*a)*s*E
    C=(1+s)*E/F; chi=s*(E-1)/F; g=a/J
    beta=-a*(1-3*a)*s*E*F/J**2
    eta=(1-k*chi)*(1+3*k*chi)/(1-3*k*chi)**2
    B=4*k*k*(1-3*k)/(1+k)**2
    delta_R=-B*chi*chi/(1-3*k*chi)
    return dict(a=a,al=al,s=s,E=E,F=F,J=J,C=C,Ku=J/F**2,
                chi=chi,g=g,beta=beta,eta=eta,delta_R=delta_R,R=1+delta_R,
                ab=al/F,chi_u=2*al*(s+chi)*(1-chi)/(1+s),B=B)


def high_precision(protocol):
    rows=[]
    for ks in protocol['derivative_k']:
        k=mp.mpf(ks)
        for us in protocol['derivative_u']:
            u=mp.mpf(us); q=quantities(k,u)
            # Actual numerical differentiation of A and K, not the closed beta.
            A=lambda v:mp.sqrt(quantities(k,v)['C'])
            K=lambda v:quantities(k,v)['Ku']
            alpha=lambda v:mp.diff(lambda w:mp.log(A(w)),v)/mp.sqrt(K(v))
            beta=mp.diff(alpha,u)/mp.sqrt(K(u))
            tag=f'high_precision.k{ks}.u{us}'
            near(tag+'.alpha',alpha(u),mp.sqrt(q['g']),'1e-60')
            near(tag+'.beta',beta,q['beta'],'1e-60')
            near(tag+'.density_feedback',beta+alpha(u)**2,-q['eta'],'1e-60')
            near(tag+'.Newton',q['C']*(1+q['g'])/(1+k),q['R'],'1e-60')
            direct_derivative=mp.diff(lambda v:mp.log(quantities(k,v)['C']*(1+quantities(k,v)['g'])/(1+k)),u)
            factor=-q['B']*q['chi']*(2-3*k*q['chi'])/(1-3*k*q['chi'])**2
            near(tag+'.Newton_derivative',direct_derivative,factor*q['chi_u']/q['R'],'1e-60')
            check(tag+'.positive_G',0<q['R']<=1)
            if abs(q['chi'])<1:
                check(tag+'.trapped_negative_feedback',q['eta']>0)
            rows.append({'k':ks,'u':us,**{n:mp.nstr(q[n],35) for n in ['chi','g','eta','delta_R']}})
    return rows


def vacuum_and_monotonicity():
    k,nu = sp.symbols('k nu',positive=True)
    u,x,y,t = sp.symbols('u x y t',real=True)
    a=(1-k)*(1+3*k)/4;al=sp.sqrt(a);s=(1+k)/(k*(1-3*k))
    E=sp.exp(2*al*u);F=1+s*E;J=1+(1-3*a)*s*E;D=1+2*(1+k)*(x*x+y*y)/3
    K=[J/F**2,(1+s)*4*k/(9*F*D),(1+s)*k/(3*F*D)]
    U=sp.Rational(3,2)+sp.Rational(3,2)*s*(E-1)**2/F**2+k*x*x*sp.exp(-(1-k)*u/al)/2+k*y*y*sp.exp(-(1+k)*u/al)/3+nu*(1+s)*u*u/(2*F**2)
    zero={u:0,x:0,y:0};fields=[u,x,y]
    expected=[VACUUM_MASS_NUMERATOR*(3*(1+k)+nu)/(1-3*k),sp.Rational(9,4),sp.Integer(2)]
    for i,field in enumerate(fields):
        identity('vacuum.gradient.'+str(i),sp.diff(U,field).subs(zero))
        identity('vacuum.mass.'+str(i),(sp.diff(U,field,2)/K[i]).subs(zero)-expected[i])
        for j in range(i):
            identity('vacuum.off_diagonal.'+str(i)+'.'+str(j),sp.diff(U,field,fields[j]).subs(zero))
    Et=sp.exp(t);Ft=1+s*Et
    Uline=sp.Rational(3,2)+sp.Rational(3,2)*s*(Et-1)**2/Ft**2+nu*(1+s)*t*t/(8*a*Ft**2)
    G=12*a*(Et-1)+nu*t*(1-t)+nu*t/(s*Et)
    identity('potential.monotonic_sign_factor',sp.diff(Uline,t)*4*a*Ft**3/(s*Et*(1+s))-G)
    bound=(12*a+nu)*t+(6*a-nu)*t*t+nu*t/(s*Et)
    identity('potential.monotonic_positive_remainder',G-bound-12*a*(sp.exp(t)-1-t-t*t/2))


def run_checks():
    CHECKS.clear()
    mp.mp.dps=80
    algebra=exact()
    derivatives=high_precision({'derivative_k':['0.000001','0.00001','0.01','0.32'],
                               'derivative_u':['-2','-0.5','0','0.5','2','10']})
    vacuum_and_monotonicity()
    return {'scope':'Conditional exact coupling/energy/local-operator identities and action derivatives. No finite-distance astronomical matching or empirical test.',
            'exact':algebra,'high_precision':derivatives,'checks':CHECKS,
            'counts':{'passed':sum(q['passed'] for q in CHECKS),'failed':sum(not q['passed'] for q in CHECKS)}}


if __name__=='__main__':
    result=run_checks()
    print(json.dumps(result,indent=2))
    sys.exit(bool(result['counts']['failed']))
