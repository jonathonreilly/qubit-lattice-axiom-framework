#!/usr/local/bin/python3
"""Conditional flat physical-clock proof and published-input SI normalization."""
from pathlib import Path
import json,hashlib,argparse
import sympy as S
import mpmath as mp
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/EXPONENTIAL_SCALAR_PHYSICAL_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_PHYSICAL_PAST_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_THERMAL_BOUNCE_BOUNDED_THEOREM_NOTE_2026-10-14.md']

def check_clock():
    rows=[]
    def eq(name,expr):
        value=S.factor(S.simplify(expr)); rows.append(dict(name=name,passed=value==0,residual=str(value)))
    def ck(name,value,detail=None): rows.append(dict(name=name,passed=bool(value),detail=detail))

    Q,H,q,L,w,V,ro,rho=S.symbols('Q H q L w V rho_other rho_B',positive=True)
    # The equality follows from Friedmann; no independent H/w choice is inferred.
    rhoc=3*Q*H**2-Q*w-V-ro
    square=(3*q*H+2*L)**2/(3*q)+(4-3*q)*(w-L**2/q)/3+(4-3*q)*(V+ro)/(3*Q)
    eq('joint_Friedmann_coupling_square',(2*H+L)**2-(4-3*q)*rhoc/(3*Q)-square)
    gap=S.symbols('gap',nonnegative=True)
    qp=1/(3*(1+S.symbols('z',positive=True)))
    eq('positive_transverse_coefficient',4-3*qp-(3+S.symbols('z',positive=True)*4)/(1+S.symbols('z',positive=True)))
    ck('positive_joint_coefficients', S.factor(4-3*qp).is_positive)
    # Exact square saturation at a local constraint state is not a full solution.
    Lopt=-3*q*H/2; wopt=Lopt**2/q
    eq('local_square_minimizer',square.subs({L:Lopt,w:wopt,V:0,ro:0}))
    eq('local_minimizer_bath_density',rhoc.subs({L:Lopt,w:wopt,V:0,ro:0})-3*Q*H**2*(1-3*q/4))

    A,a,D,R=S.symbols('A a D R',positive=True)
    eq('Phi_physical_time_derivative',(A*a**2*L+2*A*a**2*H)/A-a**2*(2*H+L))
    eq('constant_duration_integrand',a**4*(4-3*q)*(D/(R*a**4))/(3*Q)-(4-3*q)*D/(3*Q*R))
    C,rj,a0=S.symbols('C rhoJ a0',positive=True)
    D0=C**2*rj*a0**4
    sharp=S.sqrt(C)*a0**2*S.sqrt(3*Q*R/((4-3*q)*D0))
    eq('physical_endpoint_density_conversion',sharp**2-3*Q*R/(C*rj*(4-3*q)))
    G,gamma,eta=S.symbols('G gamma eta',positive=True)
    qsub=gamma*C/(8*S.pi*G)
    eq('positive_gravity_calibration',sharp.subs(Q,qsub)**2-3*R*gamma/(8*S.pi*G*rj*(4-3*q)))
    eq('same_background_upper_coefficient',sharp.subs(Q,qsub).subs(gamma,S.Rational(4,3)*(1+eta))**2-R*(1+eta)/(2*S.pi*G*rj*(4-3*q)))
    eq('zero_coupling_radiation_normalization',sharp.subs(q,0)**2-3*Q*R/(4*C*rj))
    ck('candidate_uniform_domain',S.factor(1-3*qp).is_positive)

    c,x,xi=S.symbols('c x xi',positive=True)
    envelope=x**(2-c)/(2-c)
    eq('separate_envelope_integral',S.diff(envelope,x)-x**(1-c))
    eq('sharp_vs_separate_squared_denominators',(4-c**2)-(2-c)**2-2*c*(2-c))
    # A second independent algebraic route: optimize the energy-weighted clock.
    ell=S.symbols('ell',real=True)
    eq('weighted_clock_ratio_square',(2+ell)**2-(4-c**2)*(1-ell**2/c**2)-(2*ell+c**2)**2/c**2)
    eq('weighted_clock_optimal_log_slope',((2+ell)**2-(4-c**2)*(1-ell**2/c**2)).subs(ell,-c**2/2))

    examples=[]
    for kval in [S.Rational(1,100),S.Rational(1,10),S.Rational(1,5),S.Rational(3,10)]:
        qa=(1-kval)*(1+3*kval)/4; cv=S.sqrt(3*qa)
        ck('candidate_qmax_'+str(kval),0<qa<S.Rational(1,3))
        ck('candidate_clock_sign_'+str(kval),0<cv<1)
        ck('sharp_improves_separate_'+str(kval),S.sqrt(4-3*qa)>2-cv)
        for hv in [S.Rational(1),S.Rational(3,2)]:
            for frac in [-S.Rational(2,3),S.Rational(1,4)]:
                lv=frac*hv; ww=lv**2/qa+S.Rational(1,10); bath=3*hv**2-ww-S.Rational(1,20)
                if bath<=0:continue
                resid=(2*hv+lv)**2-(4-3*qa)*bath/3
                ck('positive_local_constraint_'+str((kval,hv,frac)),resid>=0 and 2*hv+lv>0)
        examples.append(dict(k=str(kval),qmax=str(qa),sharp_coefficient=str(S.N(1/S.sqrt(4-3*qa),20)),separate_coefficient=str(S.N(1/(2-cv),20))))

    # Exact homogeneous radiation+vacuum solution within candidate origin domain:
    # a^2=sinh(2Hv t), rho=3Q Hv^2/a^4, C=1, scalar velocity zero.
    t,hv=S.symbols('t Hv',positive=True)
    aa=S.sqrt(S.sinh(2*hv*t)); hh=hv*S.coth(2*hv*t); rr=3*Q*hv**2/S.sinh(2*hv*t)**2
    eq('origin_radiation_vacuum_Friedmann',3*Q*hh**2-3*Q*hv**2-rr)
    eq('origin_radiation_continuity',S.diff(rr,t)+4*hh*rr)
    eq('origin_Phi_derivative',S.diff(aa**2,t)-2*hv*S.cosh(2*hv*t))
    for tt in [S.Rational(1,10),S.Rational(1,2),S.Rational(2)]:
        # sinh(2t)>2t, analytic from derivative cosh-1; evaluated as a control.
        ck('origin_duration_below_floor_free_bound_'+str(tt),S.sinh(2*tt)>2*tt)
    z=S.symbols('z',positive=True)
    eq('sinh_gap_at_zero',(S.sinh(z)-z).subs(z,0))
    eq('sinh_gap_positive_derivative',S.diff(S.sinh(z)-z,z)-2*S.sinh(z/2)**2)
    ck('sinh_gap_derivative_positive',(2*S.sinh(z/2)**2).is_positive)

    # Prescribed de Sitter geometry with constant positive density fails the charge
    # premise. This is a bookkeeping probe, not an asserted full scalar solution.
    rho0=S.symbols('rho0',positive=True)
    eq('deSitter_nonconserved_positive_bath_charge',S.diff(rho0*S.exp(4*t),t)-4*rho0*S.exp(4*t))
    ck('deSitter_charge_bound_fails_in_past',S.limit(S.exp(4*t),t,-S.oo)==0)
    # Curved full-action constant-origin histories were established separately.
    # This script makes no assertion that algebraic q>=1/3 data solve the action.
    Hneg=-S.Rational(1); Llarge=S.Rational(6,5); qlarge=S.Rational(3,4); wlarge=Llarge**2/qlarge
    ck('large_q_kinematic_sign_counterexample',Hneg+Llarge>0 and 3*Hneg**2-wlarge>0)
    ck('large_q_outside_candidate_domain',qlarge>S.Rational(1,3))
    return {'checks':rows,'candidate_envelopes':examples}

def check_observed_normalization():
    mp.mp.dps=50
    inp={'role': 'published calibration/development inputs; no held-out empirical test and no parameter fitted', 'T_CMB_K': {'value': 2.72548, 'reported_uncertainty': 0.00057, 'source': 'https://arxiv.org/pdf/0911.1955', 'locator': 'Table2 p5 and conclusion p6; aggregate literature estimate, not exclusively one FIRAS measurement'}, 'G_SI': {'value': 6.6743e-11, 'standard_uncertainty': 1.5e-15, 'source': 'https://physics.nist.gov/cuu/Constants/Table/allascii.txt', 'locator': '2022 recommended Newtonian constant of gravitation'}, 'c_m_s': 299792458, 'h_J_s': 6.62607015e-34, 'kB_J_K': 1.380649e-23, 'SI_definitions': 'c, h and kB exact in SI; hbar=h/(2pi)', 'year_conversion': 'Julian year =365.25*86400 seconds by convention', 'protocol_frozen_at': '2026-10-14T12:19:14.052121+00:00', 'planned_calculation': 'rho_energy=pi^2(kB T)^4/(15 hbar^3 c^3); rho_mass=rho_energy/c^2; conditional universal same-background clock normalization tau_ref=1/sqrt(6pi G rho_mass); actual interval ceiling tau_ref sqrt(R(1+eta)) requires all clock theorem and calibration premises', 'uncertainty_handling': 'evaluate corners of published +/-uncertainty input rectangle only; this is not a simultaneous confidence bound, does not model source covariance, and says nothing about eta', 'limits': 'No empirical cosmic-age bound, no verified photon charge over an arbitrary past interval, no proof laboratory G is same-background coefficient, no Hv/k/nu calibration or fitted likelihood.'}
    c=mp.mpf(str(inp['c_m_s']));h=mp.mpf(str(inp['h_J_s']));kb=mp.mpf(str(inp['kB_J_K']));hb=h/(2*mp.pi)
    T=mp.mpf(str(inp['T_CMB_K']['value']));G=mp.mpf(str(inp['G_SI']['value']))
    uT=mp.mpf(str(inp['T_CMB_K']['reported_uncertainty']));uG=mp.mpf(str(inp['G_SI']['standard_uncertainty']))
    year=mp.mpf('365.25')*86400;gyr=year*10**9

    def calc(temp,gravity):
     energy=mp.pi**2*(kb*temp)**4/(15*hb**3*c**3)
     mass=energy/c**2
     tau=1/mp.sqrt(6*mp.pi*gravity*mass)
     return dict(T=temp,G=gravity,energy_density_J_m3=energy,mass_density_kg_m3=mass,tau_reference_s=tau,tau_reference_Gyr=tau/gyr)
    center=calc(T,G);corners=[calc(tt,gg) for tt in [T-uT,T+uT] for gg in [G-uG,G+uG]]
    checks=[]
    def ck(n,v):checks.append(dict(name=n,passed=bool(v)))
    sb=2*mp.pi**5*kb**4/(15*h**3*c**2)
    ck('blackbody_stefan_boltzmann_route',abs(4*sb*T**4/c/center['energy_density_J_m3']-1)<mp.mpf('1e-45'))
    ck('SI_mass_energy_conversion',abs(center['mass_density_kg_m3']*c**2/center['energy_density_J_m3']-1)<mp.mpf('1e-45'))
    ck('time_temperature_scaling',abs(calc(2*T,G)['tau_reference_s']*4/center['tau_reference_s']-1)<mp.mpf('1e-45'))
    ck('time_gravity_scaling',abs(calc(T,4*G)['tau_reference_s']*2/center['tau_reference_s']-1)<mp.mpf('1e-45'))
    ck('monotone_rectangle_upper',max(r['tau_reference_s'] for r in corners)==corners[0]['tau_reference_s'])
    ck('monotone_rectangle_lower',min(r['tau_reference_s'] for r in corners)==corners[-1]['tau_reference_s'])
    # Exponents in (mass,length,time,temperature) for explicitly dimensional inputs.
    import sympy as S
    L=S.Matrix([0,1,0,0]);Ti=S.Matrix([0,0,1,0]);M=S.Matrix([1,0,0,0]);Th=S.Matrix([0,0,0,1])
    dc=L-Ti;dh=M+2*L-Ti;dk=M+2*L-2*Ti-Th;dG=3*L-M-2*Ti
    energy_dim=4*(dk+Th)-3*dh-3*dc
    mass_dim=energy_dim-2*dc
    time_dim=-(dG+mass_dim)/2
    ck('energy_density_dimensions',energy_dim==M-L-2*Ti)
    ck('mass_density_dimensions',mass_dim==M-3*L)
    ck('clock_dimensions',time_dim==Ti)
    for q in [mp.mpf('.25'),mp.mpf('.30'),mp.mpf('0.333333333333')]:
     exact=mp.sqrt(3*(1+q)/(8*mp.pi*G*center['mass_density_kg_m3']*(4-3*q)))
     ck('q_envelope_'+str(q),exact<center['tau_reference_s'])
    def clean(v):
     if isinstance(v,dict):return {k:clean(x) for k,x in v.items()}
     if isinstance(v,list):return [clean(x) for x in v]
     if isinstance(v,mp.mpf):return mp.nstr(v,35)
     return v
    return {'checks':checks,'central':clean(center),'reported_uncertainty_rectangle':clean(corners)}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    checks=[];units={};outputs={}
    for name,fn in [('clock',check_clock),('observed_normalization',check_observed_normalization)]:
        result=fn();rows=result.pop('checks');outputs[name]=result
        units[name]={'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows)}
        checks.extend([{**row,'name':name+'::'+row['name']} for row in rows])
    result={'scope':'Conditional flat physical-clock mathematics and published-input normalization; no fitted age or verified environment.','passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'units':units,'checks':checks,'substantive_outputs':outputs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        p=Path(args.output);assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(bool(result['failed']))
