#!/usr/local/bin/python3
"""Conditional thermal-charge, finite-mass bounce and calibration controls."""
from pathlib import Path
import json,hashlib,argparse,math
import sympy as S
import numpy as np
from scipy.integrate import quad
from scipy.special import expit
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/EXPONENTIAL_SCALAR_THERMAL_BOUNCE_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_PHYSICAL_PAST_BOUNDED_THEOREM_NOTE_2026-10-14.md']

def check_trace_bridge():
    rows=[]
    def ck(n,b,d=None):rows.append(dict(name=n,passed=bool(b),detail=d))
    def eq(n,x):v=S.factor(S.simplify(x));ck(n,v==0,str(v))
    A,a,r,p=S.symbols('A a r p',positive=True);L,H,src=S.symbols('L H source',real=True)
    Z=H+L;HJ=Z/A;rdot=A*(src-3*HJ*(r+p));rhoE=A**4*r;pressE=A**4*p
    rEdot=4*L*rhoE+A**4*rdot
    rhs=L*(rhoE-3*pressE)+A**5*src
    eq('conformal_component_balance',rEdot+3*H*(rhoE+pressE)-rhs)
    eq('tracefree_scalar_exchange_vanishes',(L*(rhoE-3*pressE)).subs(p,r/3))
    DE=rhoE*a**4;DJ=r*(A*a)**4
    eq('radiation_charge_frame_invariant',DE-DJ)
    Ddot=(rEdot*a**4+4*H*rhoE*a**4).subs(p,r/3)
    eq('radiation_charge_Einstein_source',Ddot-a**4*A**5*src)
    eq('radiation_charge_physical_source',Ddot/A-(A*a)**4*src)
    eq('isolated_radiation_charge',Ddot.subs(src,0))
    rd,pd,rdJ,rpJ=S.symbols('rho_d p_d Qd Qr',real=True)
    eq('internal_sources_cancel',(A**5*rdJ+A**5*rpJ).subs(rdJ,-rpJ))
    # Two possible transfer laws solve the same total continuity identity.
    t,h,ga,r0,d0=S.symbols('t h Gamma r0 d0',positive=True)
    d=d0*S.exp(-(3*h+ga)*t);rsol=S.exp(-4*h*t)*(r0+ga*d0*(S.exp((h-ga)*t)-1)/(h-ga));J=ga*d
    for n,e in [('dust_transfer',S.diff(d,t)+3*h*d+J),('radiation_transfer',S.diff(rsol,t)+4*h*rsol-J),('total_continuity',S.diff(d+rsol,t)+3*h*(d+S.Rational(4,3)*rsol))]:eq(n,e)
    resonant=S.exp(-4*h*t)*(r0+h*d0*t)
    eq('resonant_transfer_limit',S.limit(rsol,ga,h)-resonant)
    eq('no_transfer_control',rsol.subs(ga,0)-r0*S.exp(-4*h*t))
    eq('same_initial_radiation_for_distinct_rates',rsol.subs(t,0)-r0)
    eq('same_initial_dust_for_distinct_rates',d.subs(t,0)-d0)
    # These prescribed-H solutions are continuity controls, not Einstein/scalar histories.
    fb,lam,zet,eps,delta,calS=S.symbols('fb lambda zeta epsilon delta entropy_ratio',positive=True)
    rhob,kapb,Q=S.symbols('rhob kapb Q',positive=True);rhof=zet*rhob/lam**4;kapf=kapb/lam**2
    product=3*Q*kapf/rhof
    eq('endpoint_charge_budget',product.subs(rhob,3*Q*kapb*fb)-lam**2/(fb*zet))
    threshold=lam**2/(fb*eps*(1+delta))
    eq('necessary_growth_threshold_saturates',(lam**2/(fb*zet)).subs(zet,threshold)-eps*(1+delta))
    # Thermodynamic endpoint identity from rho(T) and entropy(T), no chosen temperature scale.
    g,gs,ent,rad=S.symbols('g gs entropy radius',positive=True)
    TT=(45*ent/(2*S.pi**2*gs*rad**3))**S.Rational(1,3)
    D=S.pi**2*g*TT**4*rad**4/30
    coef=(S.pi**2/30)*(45/(2*S.pi**2))**S.Rational(4,3)
    eq('thermal_charge_entropy_identity',D-coef*g*ent**S.Rational(4,3)/gs**S.Rational(4,3))
    gb,gf,gsb,gsf,Sb,Sf=S.symbols('gb gf gsb gsf Sb Sf',positive=True)
    zthermal=gf/gb*(gsb/gsf)**S.Rational(4,3)*(Sf/Sb)**S.Rational(4,3)
    eq('thermal_endpoint_ratio',(D.subs({g:gf,gs:gsf,ent:Sf})/D.subs({g:gb,gs:gsb,ent:Sb}))-zthermal)
    zcommon=(gb/gf)**S.Rational(1,3)*(Sf/Sb)**S.Rational(4,3)
    eq('common_temperature_endpoint_reduction',zthermal.subs({gsb:gb,gsf:gf})-zcommon)
    smin=threshold**S.Rational(3,4)*(gf/gb)**S.Rational(1,4)
    eq('necessary_entropy_threshold',zcommon.subs(Sf,Sb*smin)-threshold)
    # Specified ideal electromagnetic bath; component identity prevents budget inflation.
    gstart=S.Rational(2)+S.Rational(7,8)*4;gend=S.Rational(2)
    zall=(gstart/gend)**S.Rational(1,3);zphot=(gstart/gend)**S.Rational(4,3)
    eq('electron_pair_spin_weight',gstart-S.Rational(11,2))
    eq('total_bath_charge_factor',zall-(S.Rational(11,4))**S.Rational(1,3))
    eq('photon_charge_factor',zphot-(S.Rational(11,4))**S.Rational(4,3))
    fph=(gend/gstart)*fb
    eq('same_component_budget_cancellation',fph*zphot-fb*zall)
    ck('larger_photon_factor_is_not_total_factor',zphot>zall>1)
    # Exposed illustrative threshold, not Planck/BBN observation.
    example={fb:S.Rational(1,4),lam:S.Rational(1),eps:S.Rational(1,100),delta:S.Rational(1,10)}
    needed=threshold.subs(example);ck('illustrative_adiabatic_pair_budget_insufficient',needed>zall)
    wrong=fb*zphot;correct=fb*zall;ck('mixed_component_budget_overstates_repair',wrong>correct)
    return {'checks':rows,'ideal_pair_total_factor':str(S.N(zall,20)),'ideal_pair_photon_factor':str(S.N(zphot,20)),'illustrative_required_growth':str(needed)}

def check_general_trace():
    rows=[]
    def eq(name,expr):
     value=S.factor(S.expand(expr)); rows.append(dict(name=name,passed=value==0,residual=str(value)))
    A,a,r,p,H,L,Q=S.symbols('A a rho pressure H L Q',real=True,nonzero=True)
    Z=H+L; hj=Z/A; aj=A*a
    rjprime=Q-3*hj*(r+p)
    # Direct physical differentiation, no traceless or isolated component premise.
    djprime=aj**4*(rjprime+4*hj*r)
    expected=aj**4*(hj*(r-3*p)+Q)
    eq('general_physical_charge_equation',djprime-expected)
    # Independently differentiate the Einstein expression A^4 rho_J a_E^4.
    dedot=A**4*a**4*(4*L*r+A*rjprime+4*H*r)
    eq('charge_derivatives_proper_time_conversion',dedot-A*djprime)
    eq('general_Einstein_charge_trace_and_source',dedot-a**4*((H+L)*(A**4*r-3*A**4*p)+A**5*Q))
    eq('traceless_source_limit',djprime.subs(p,r/3)-aj**4*Q)
    eq('isolated_traceful_limit',djprime.subs(Q,0)-aj**4*hj*(r-3*p))
    eq('isolated_dust_charge_growth',djprime.subs({Q:0,p:0})-hj*r*aj**4)
    r1,r2,p1,p2,j=S.symbols('r1 r2 p1 p2 j',real=True)
    pair=djprime.subs({r:r1,p:p1,Q:j})+djprime.subs({r:r2,p:p2,Q:-j})
    eq('complete_bath_sources_cancel_but_trace_survives',pair-aj**4*hj*(r1+r2-3*(p1+p2)))
    # The conditional logarithmic budget retains a nonzero trace across a threshold.
    w=S.symbols('w',real=True)
    eq('isolated_logarithmic_charge_rate',djprime.subs({Q:0,p:w*r})/(hj*r*aj**4)-(1-3*w))
    return {'checks':rows}

def check_finite_mass():
    rows = []
    def ck(name, passed, detail=None):
        rows.append(dict(name=name, passed=bool(passed), detail=detail))
    def eq(name, expr):
        value = S.factor(S.simplify(expr))
        ck(name, value == 0, str(value))

    rho, p, T, rhoT, H, a, Q, kap, kinetic, other, hd = S.symbols(
        'rho pressure T rhoT H a Q kappa kinetic other_enthalpy Hdot', positive=True)
    s = (rho+p)/T
    pT = s
    sT = (rhoT+pT)/T-(rho+p)/T**2
    eq('equilibrium_entropy_derivative', sT-rhoT/T)
    tdot = -3*H*(rho+p)/rhoT
    eq('isolation_implies_comoving_entropy', sT*tdot+3*H*s)
    dlogG = rhoT/rho-S.Rational(4,3)*sT/s
    eq('charge_monotonicity_identity', dlogG-rhoT*(3*p-rho)/(3*rho*(rho+p)))
    eq('physical_charge_trace_rate', dlogG*tdot-H*(rho-3*p)/rho)
    E, mom, mass = S.symbols('E momentum mass', positive=True)
    eq('massive_trace_integrand', (mom**2*E-mom**4/E-mass**2*mom**2/E).subs(E,S.sqrt(mom**2+mass**2)))
    w = S.symbols('w', nonnegative=True)
    kap_at_bounce = hd+kinetic+(rho*(1+w)+other)/(2*Q)
    margin = 3*Q*kap_at_bounce-rho*S.Rational(3,2)*(1+w)
    eq('strict_bounce_margin', margin-3*Q*(hd+kinetic)-S.Rational(3,2)*other)
    ck('strict_bounce_margin_positive', S.expand(margin).is_positive)
    fbcap = 2/(3*(1+w))
    eq('pressure_weakening_bound', S.Rational(2,3)-fbcap-2*w/(3*(1+w)))
    fb, lam, zeta, rb, kb = S.symbols('fb radius_ratio zeta rhob kappab', positive=True)
    eq('same_bath_endpoint_budget', (3*Q*(kb/lam**2)/(zeta*rb/lam**4)).subs(rb,3*Q*kb*fb)-lam**2/(fb*zeta))
    gb, gf, Sb, Sf = S.symbols('gb gf Sb Sf', positive=True)
    R = (S.Rational(11,4))**S.Rational(1,3)
    coefficient = S.Rational(3,2)/R
    eq('pair_bath_ratio_cube', R**3-S.Rational(11,4))
    eq('coarse_bounce_coefficient_cube', coefficient**3-S.Rational(27,22))
    ck('coefficient_strictly_above_one', S.Rational(27,22)>1)
    eq('photon_bath_initial_fraction_consistency', S.Rational(4,11)*(S.Rational(11,4))**S.Rational(4,3)-R)
    eps, delta, sigma = S.symbols('epsilon delta sigma', positive=True)
    sigcrit = (3*lam**2/(2*R*eps*(1+delta)))**S.Rational(3,4)
    eq('entropy_escape_threshold', (3*lam**2/(2*R*sigma**S.Rational(4,3))).subs(sigma,sigcrit)-eps*(1+delta))

    # Actual finite-mass phase-space integration. The endpoint range is proved in
    # the note; these numerical samples only check formula implementation.
    pi = math.pi
    def integral(fun):
        value, error = quad(fun, 0, np.inf, epsabs=2e-11, epsrel=2e-11, limit=300)
        return value, error
    def gas(x):
        def vals(y):
            e=math.hypot(y,x); f=float(expit(-e))
            return e,f
        rr, er = integral(lambda y:y*y*vals(y)[0]*vals(y)[1])
        pp, ep = integral(lambda y:y**4/vals(y)[0]*vals(y)[1])
        tr, et = integral(lambda y:x*x*y*y/vals(y)[0]*vals(y)[1])
        cv, ec = integral(lambda y:y*y*vals(y)[0]**2*vals(y)[1]*(1-vals(y)[1]))
        r=pi*pi/15+2*rr/pi**2
        pressure=pi*pi/45+2*pp/(3*pi**2)
        return dict(x=float(x),r=r,p=pressure,trace=2*tr/pi**2,
                    heat=4*pi*pi/15+2*cv/pi**2,
                    G=r/(r+pressure)**(4/3),w=pressure/r,
                    error_estimates=[er,ep,et,ec])

    grid=[gas(float(x)) for x in np.geomspace(1e-3,100,61)]
    def masslessG(g):
        rr=pi*pi*g/30
        return rr/(4*rr/3)**(4/3)
    Ghot=masslessG(5.5); Gcold=masslessG(2)
    for j,row in enumerate(grid):
        r,pressure,tr=row['r'],row['p'],row['trace']
        ck('finite_mass_trace_'+str(j),abs(r-3*pressure-tr)<2e-11*max(1,r),r-3*pressure-tr)
        ck('finite_mass_stress_domain_'+str(j),0<pressure<=r/3+3e-12 and tr>=0 and row['heat']>0)
        ck('finite_mass_charge_range_'+str(j),Ghot-3e-12<=row['G']<=Gcold+3e-12)
    ck('charge_monotone_in_m_over_T',all(b['G']>=a['G']-3e-12 for a,b in zip(grid,grid[1:])))
    ck('hot_endpoint_convergence',abs(grid[0]['G']/Ghot-1)<1e-6)
    ck('cold_endpoint_convergence',abs(grid[-1]['G']/Gcold-1)<1e-12)
    ck('endpoint_ratio_numerical',abs(Gcold/Ghot-float(R))<2e-15)

    alternate=[]
    for x in [0.001,0.03,0.3,1.0,3.0,10.0,100.0]:
        base=gas(x)
        # Independent energy-coordinate integral, e=x+z, dp/de=e/p.
        ir,er=integral(lambda z:(x+z)**2*math.sqrt(z*(z+2*x))*float(expit(-x-z)))
        ip,ep=integral(lambda z:(z*(z+2*x))**1.5*float(expit(-x-z)))
        ra=pi*pi/15+2*ir/pi**2; pa=pi*pi/45+2*ip/(3*pi**2)
        ck('energy_coordinate_rho_'+str(x),abs(ra-base['r'])<2e-10*max(1,abs(ra)))
        ck('energy_coordinate_pressure_'+str(x),abs(pa-base['p'])<2e-10*max(1,abs(pa)))
        # Differentiate dimensional rho(T),p(T) at fixed m=x and T=1.
        step=1e-4
        plus=gas(x/(1+step)); minus=gas(x/(1-step))
        dr=((1+step)**4*plus['r']-(1-step)**4*minus['r'])/(2*step)
        dp=((1+step)**4*plus['p']-(1-step)**4*minus['p'])/(2*step)
        ck('fixed_mass_heat_derivative_'+str(x),abs(dr/base['heat']-1)<3e-7,dr/base['heat']-1)
        ck('fixed_mass_pressure_entropy_'+str(x),abs(dp/(base['r']+base['p'])-1)<3e-7,dp/(base['r']+base['p'])-1)
        alternate.append(dict(x=x,r=ra,p=pa,quadrature_errors=[er,ep],rho_T_numeric=dr,p_T_numeric=dp))
    return {'checks':rows,'grid':grid,'alternate_quadrature':alternate,'R':str(S.N(R,25)),'bounce_coefficient':str(S.N(coefficient,25)),'analytic_endpoint_G':[Ghot,Gcold]}

def check_calibration():
    rows=[]
    def eq(n,e):
     v=S.factor(S.simplify(e));rows.append(dict(name=n,passed=v==0,residual=str(v)))
    def ck(n,b,d=None):rows.append(dict(name=n,passed=bool(b),detail=d))
    R,sigma,gamma,lam,eta,L,C,Q,Gcal=S.symbols('R sigma gamma radius_ratio eta L C Q Gcal',positive=True)
    k,q=S.symbols('k q',positive=True)
    fb=S.symbols('fb',positive=True)
    Gbare=C/(8*S.pi*Q);Fbare=S.symbols('Fbare',positive=True)
    eq('measured_normalization_conversion',Fbare*Gbare/Gcal-Fbare/(Gcal/Gbare))
    charge=R*sigma**S.Rational(4,3)
    bare=3*lam**2/(2*charge)
    measured=bare/gamma
    eq('same_background_principal_ceiling',measured.subs(gamma,S.Rational(4,3)*(1+eta))-9*lam**2/(8*R*sigma**S.Rational(4,3)*(1+eta)))
    threshold=S.Rational(8,9)*R*sigma**S.Rational(4,3)*(1+eta)*L
    eq('radius_budget_boundary',measured.subs(gamma,S.Rational(4,3)*(1+eta)).subs(lam,S.sqrt(threshold))-L)
    Ccrit=2*R*sigma**S.Rational(4,3)*(1+eta)*(1+k)*L/(3*lam**2)
    local=measured.subs(gamma,(1+eta)*(1+k)/C)
    eq('arbitrary_background_C_budget',local-3*C*lam**2/(2*R*sigma**S.Rational(4,3)*(1+eta)*(1+k)))
    eq('Ccrit_boundary',local.subs(C,Ccrit)-L)
    eq('Ccrit_positive_slack',local.subs(C,Ccrit+S.Symbol('h',positive=True))-L-3*S.Symbol('h',positive=True)*lam**2/(2*R*sigma**S.Rational(4,3)*(1+eta)*(1+k)))
    Rpair=S.Rational(11,4)**S.Rational(1,3)
    coef=S.Rational(9,8)/Rpair
    eq('calibrated_coefficient_cube',coef**3-S.Rational(729,1408))
    ck('measured_coefficient_below_one',S.Rational(729,1408)<1)
    ck('bare_coefficient_above_one',S.Rational(27,22)>1)
    # Positive explicit corners are exposed algebra controls, not real observations.
    examples=[]
    for kv,ev,sv,lv,nv in [(S.Rational(1,5),S.Rational(0),S.Rational(1),S.Rational(1,100),S.Rational(1)),(S.Rational(1,10),S.Rational(1,20),S.Rational(3,2),S.Rational(1,10),S.Rational(2)),(S.Rational(3,10),S.Rational(1,5),S.Rational(2),S.Rational(1),S.Rational(1))]:
     vals={k:kv,eta:ev,sigma:sv,L:lv,lam:nv,R:Rpair}
     cc=Ccrit.subs(vals);ccf=float(cc);examples.append(dict(k=str(kv),eta=str(ev),sigma=str(sv),target=str(lv),radius_ratio=str(nv),Ccrit=str(S.N(cc,20)),negative_u_floor_applies=ccf<1))
     eq('corner_Ccrit_saturation_'+str(len(examples)),local.subs(C,Ccrit).subs(vals)-lv)
    # The calibration dependency supplies U0 monotonicity on0<C<1. These
    # controls only check substitution and domain gates, not a new proof of it.
    a,ss,nu=S.symbols('a s nu',positive=True)
    U0=S.Rational(3,2)+S.Rational(3,2)*ss*(1-C)**2+nu*(1+ss-ss*C)**2*S.log(C/(1+ss-ss*C))**2/(8*a*(1+ss))
    eq('potential_origin_floor',U0.subs(C,1)-S.Rational(3,2))
    ck('domain_floor_not_claimed_above_one',not (0<S.Rational(5,4)<1))
    return {'checks':rows,'same_background_pair_coefficient':str(S.N(coef,25)),'synthetic_examples':examples}

def check_joint_entropy(prior):
    rows=[]
    def ck(name, passed, detail=None): rows.append(dict(name=name,passed=bool(passed),detail=detail))
    def eq(name, expr):
     v=S.factor(S.simplify(expr));ck(name,v==0,str(v))
    f,E,x,y=S.symbols('f E x y',positive=True)
    hf=-f*S.log(f)-(1-f)*S.log(1-f)
    eq('entropy_occupation_derivative',S.diff(hf,f)-S.log((1-f)/f))
    fd=1/(S.exp(E)+1)
    eq('fermi_occupation_energy_derivative',S.diff(fd,E)+fd*(1-fd))
    eq('entropy_energy_derivative',S.diff(E*fd+S.log(1+S.exp(-E)),E)+E*fd*(1-fd))
    eq('entropy_mass_derivative',(-E*f*(1-f)*x/E)-(-x*f*(1-f)))
    Eof=S.sqrt(y*y+x*x); ell=S.log(1+S.exp(-Eof))
    eq('entropy_pressure_integration_by_parts',S.diff(y**3*ell,y)-3*y*y*ell+y**4/(Eof*(S.exp(Eof)+1)))
    r,p,gf,sigma,eta,gamma,lam,k,C,Ltar=S.symbols('r p Gf sigma eta gamma lam k C Ltar',positive=True)
    h=r+p;w=p/r;G=r/h**S.Rational(4,3)
    Gibbs=(1+w)*G
    eq('joint_pressure_entropy_identity',Gibbs-h**(-S.Rational(1,3)))
    fbcap=2/(3*(1+w));zeta=sigma**S.Rational(4,3)*gf/G
    jointcap=S.Rational(2,3)*sigma**S.Rational(4,3)*gf*h**S.Rational(1,3)
    eq('joint_fraction_charge_cap',fbcap*zeta-jointcap)
    R=S.Rational(11,4)**S.Rational(1,3)
    hhot=11*S.pi**2/45;hcold=4*S.pi**2/45
    Ghot=S.Rational(3,4)*hhot**(-S.Rational(1,3));Gcold=S.Rational(3,4)*hcold**(-S.Rational(1,3))
    eq('endpoint_ratio_cube',(Gcold/Ghot)**3-S.Rational(11,4))
    eq('joint_cap_at_hot_and_cold',jointcap.subs({gf:Gcold,p:hhot-r})-R*sigma**S.Rational(4,3)/2)
    bare=2*lam**2/(R*sigma**S.Rational(4,3))
    measured=bare*3/(4*(1+eta))
    eq('improved_bare_coefficient_cube',(2/R)**3-S.Rational(32,11))
    eq('measured_coefficient_cube',(3/(2*R))**3-S.Rational(27,22))
    ck('measured_unit_obstruction',S.Rational(27,22)>1)
    converted=bare/gamma
    eq('calibration_divides_product',converted*gamma-bare)
    eq('same_background_cap',measured-3*lam**2/(2*R*sigma**S.Rational(4,3)*(1+eta)))
    q,slack=S.symbols('q slack',nonnegative=True)
    # Exact positive remainder at a fixed q<1/3, preserving strict bounce slack.
    B=S.symbols('B',positive=True)
    rem=(B+slack)/((1+eta)*(1+q))-3*B/(4*(1+eta))
    eq('same_background_strict_remainder',rem-(B*(1-3*q)+4*slack)/(4*(1+eta)*(1+q)))
    lamcrit=2*R*sigma**S.Rational(4,3)*(1+eta)*Ltar/3
    eq('radius_threshold_boundary',measured.subs(lam**2,lamcrit)-Ltar)
    sigcrit=(3*lam**2/(2*R*(1+eta)*Ltar))**S.Rational(3,4)
    eq('entropy_threshold_boundary',measured.subs(sigma,sigcrit)-Ltar)
    Ccrit=R*sigma**S.Rational(4,3)*(1+eta)*(1+k)*Ltar/(2*lam**2)
    eq('different_background_threshold',converted.subs(gamma,(1+eta)*(1+k)/C).subs(C,Ccrit)-Ltar)
    ck('joint_stronger_than_coarse',S.Rational(2)>S.Rational(3,2))

    # Previously exposed finite-mass data: postprocessing, not new independent runs.
    grid=prior['grid'];gh,gc=prior['analytic_endpoint_G'];ratio=float(R)
    post=[]
    for j,a in enumerate(grid):
     hh=a['r']+a['p'];gg=a['G'];ww=a['w']
     tight=1.5*(1+ww)*gg/gc
     ck('entropy_hot_cap_'+str(j),float(hcold)-2e-11<=hh<=float(hhot)+2e-11,hh)
     ck('joint_lower_coefficient_'+str(j),tight>=2/ratio-2e-11,tight)
     ck('gibbs_cube_'+str(j),abs(((1+ww)*gg)**3*hh-1)<3e-14)
     # Compare every final endpoint against this bounce value, with no T ordering.
     endpoints=[(2/(3*(1+ww)))*v['G']/gg for v in grid]
     ck('all_final_temperature_caps_'+str(j),max(endpoints)<=ratio/2+2e-11,max(endpoints))
     post.append(dict(x=a['x'],h=hh,minimum_bare_coefficient=tight,max_fraction_charge_cap=max(endpoints)))

    # Fresh entropy integrals in occupation form, separate from saved stress integrals.
    pi=math.pi
    fresh=[]
    def integ(fn):return quad(fn,0,np.inf,epsabs=2e-12,epsrel=2e-12,limit=300)
    def entropy(xx):
     def kernel(yy):
      ee=math.hypot(xx,yy);ff=float(expit(-ee))
      return yy*yy*(ee*ff+float(np.logaddexp(0,-ee)))
     ss,err=integ(kernel)
     return 4*pi*pi/45+2*ss/pi**2,err
    for j in [0,10,20,30,40,50,60]:
     a=grid[j];xx=a['x'];hh,er=entropy(xx)
     ck('fresh_entropy_matches_stress_'+str(j),abs(hh-a['r']-a['p'])<3e-11,hh-a['r']-a['p'])
     fresh.append(dict(x=xx,h=hh,error_estimate=er))
    for xx in [.01,.1,.5,1.,3.,10.]:
     der,er=integ(lambda yy:yy*yy*float(expit(-math.hypot(xx,yy)))*(1-float(expit(-math.hypot(xx,yy)))))
     exact=-2*xx*der/pi**2;step=1e-4*max(.1,xx)
     num=(entropy(xx+step)[0]-entropy(xx-step)[0])/(2*step)
     ck('entropy_mass_derivative_numeric_'+str(xx),exact<0 and abs(num-exact)<3e-8*max(1,abs(exact)),dict(exact_integral=exact,centered=num,error_estimate=er))
    return {'checks':rows,'postprocessing':post,'fresh_entropy_integrals':fresh,'constants':dict(R=str(S.N(R,25)),bare=str(S.N(2/R,25)),same_background=str(S.N(3/(2*R),25)),unit_target_eta_ceiling=str(S.N(3/(2*R)-1,25)))}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    checks=[];units={};outputs={}
    for name,fn in [('trace_bridge',check_trace_bridge),('general_trace',check_general_trace),('finite_mass',check_finite_mass),('calibration',check_calibration),('joint_entropy',lambda:check_joint_entropy(outputs['finite_mass']))]:
        result=fn();rows=result.pop('checks');outputs[name]=result
        units[name]={'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows)}
        checks.extend([{**row,'name':name+'::'+row['name']} for row in rows])
    result={'scope':'Conditional ideal matter and supplied action, synthetic quadrature and calibration controls; no observational likelihood.','passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'units':units,'checks':checks,'substantive_outputs':outputs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        p=Path(args.output);assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(bool(result['failed']))
