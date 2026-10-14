#!/usr/local/bin/python3
"""Conditional scalar physical-past, calibration and slow-event checks; no empirical fit."""
from pathlib import Path
import json,hashlib,argparse
import sympy as S
import itertools
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/EXPONENTIAL_SCALAR_PHYSICAL_PAST_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_CURVATURE_LOOPHOLE_BOUNDED_THEOREM_NOTE_2026-10-14.md']

def check_turnaround():
    rows=[]
    def ck(n,b,d=None):rows.append({'name':n,'passed':bool(b),'detail':d})
    def zero(n,e):v=S.factor(S.simplify(e));ck(n,v==0,str(v))
    k,E=S.symbols('k E',positive=True);a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k));F=1+s*E;J=1+(1-3*a)*s*E
    K=J/F**2;b=S.sqrt(a)/F
    zero('action_coupling_norm',b*b/K-a/J)
    zero('action_strict_norm_domain',1-3*a-(1-3*k)**2/4)
    zero('action_J_gap',J-1-(1-3*a)*s*E)
    Q,V,rho=S.symbols('Q V rho',positive=True);v2,rm,sigma=S.symbols('v2 rm sigma',nonnegative=True);q=S.symbols('q',positive=True)
    # sigma=q|v|²-(b.v)² is a nonnegative Cauchy gap for an actual velocity.
    H2=q*v2-sigma;kap=(Q*v2+V+rho+rm)/(3*Q)-H2
    zero('stationary_curvature_gap',3*Q*kap-rho-(Q*(1-3*q)*v2+3*Q*sigma+V+rm))
    c=S.symbols('c',positive=True);qq=1/(3*(1+c));gap=S.factor((Q*(1-3*q)*v2+3*Q*sigma+V+rm).subs(q,qq));ck('stationary_strict_gap',gap.is_positive,str(gap))
    x=S.symbols('x',nonnegative=True)
    endpoint_lower=(1+x)**2/(3*qq)-x**2
    zero('endpoint_positive_polynomial',endpoint_lower-1-(c+2*(1+c)*x+c*x*x))
    ck('endpoint_incompatible_near_flat',S.expand(endpoint_lower-1).is_positive,str(S.expand(endpoint_lower-1)))
    # Dimensionful physical transformations and the positive-radiation product.
    AA,ZZ,kapf=S.symbols('A Z kapf',positive=True);C=AA**2;HJ2=ZZ**2/C;rhoJ=rho/C**2;dJ=kapf/ZZ**2;Frad=HJ2/(C*rhoJ/(3*Q));zero('physical_product',dJ*Frad-3*Q*kapf/rho)
    lam=S.symbols('lambda',positive=True);fb=S.symbols('fb',positive=True);rhob,kapb=S.symbols('rhob kapb',positive=True)
    zero('radiation_curvature_transport',(rhob/lam**4)/(3*Q*(kapb/lam**2))-rhob/(3*Q*kapb*lam**2))
    eta,ell=S.symbols('eta ell',positive=True);fb_nozero=1/(1+eta);l=1+ell
    ck('no_zero_case_product_strict',S.expand(l*l/fb_nozero-1).is_positive,str(S.expand(l*l/fb_nozero-1)))
    eta0=S.symbols('eta0',nonnegative=True);fb_lastzero=1/(2+eta0)
    ck('last_zero_case_product_stronger',S.expand(l*l/fb_lastzero-2).is_positive,str(S.expand(l*l/fb_lastzero-2)))
    enthalpy,hd=S.symbols('enthalpy hd',nonnegative=True);kap0=hd+(enthalpy+S.Rational(4,3)*rho)/(2*Q)
    zero('last_zero_nonnegative_raychaudhuri',3*Q*kap0-2*rho-3*Q*hd-S.Rational(3,2)*enthalpy)
    ck('last_zero_nonstrict_gap',(3*Q*hd+S.Rational(3,2)*enthalpy).is_nonnegative)
    # Standalone witnesses of lost algebraic premises, not complete cosmologies.
    # q=1/2 permits flat stationary data with positive V and radiation.
    flat_sub={Q:1,v2:1,V:S.Rational(1,10),rho:S.Rational(2,5),rm:0,q:S.Rational(1,2),sigma:0}
    zero('excluded_large_q_flat_witness',kap.subs(flat_sub))
    # Positive physical expansion can coincide with Einstein contraction if curvature is large.
    v0=S.Rational(3);b0=S.Rational(1,3);H0=-S.Rational(1,2);Z0=H0+b0*v0;kapx=(v0*v0+1+1)/3-H0*H0
    ck('large_curvature_counterwitness_E_contraction',H0<0 and Z0>0)
    zero('large_curvature_counterwitness_d',kapx/Z0**2-S.Rational(41,3))
    ck('large_curvature_counterwitness_outside_endpoint',kapx/Z0**2>1)
    # Strict and degenerate final zeros: chronology controls alone, not physical trajectories.
    t=S.symbols('t',real=True)
    chronology=[('cross',(t-1)**2*(t-2)),('degenerate_cross',(t-1)**2*(t-2)**3),('touch',(t-1)**2*(t-2)**2)]
    for name,H in chronology:
     roots=S.solve(H,t);last=max(roots);zero(name+'_last_zero',last-2);ck(name+'_right_derivative_nonnegative',S.diff(H,t).subs(t,last)>=0);ck(name+'_positive_final_H',H.subs(t,3)>0);ck(name+'_positive_final_log_radius',S.integrate(H,(t,last,3))>0)
    H=t+S.Rational(1,2);ck('zero_free_chronology',H.subs(t,0)>0 and S.diff(H,t)>0);ck('zero_free_positive_radius',S.integrate(H,(t,0,3))>0)
    # The exact closed constant-scalar solution is a physical example within the domain.
    for tau in [S.Rational(1,2),S.Rational(1),S.Rational(2)]:
     X=(3+S.sqrt(5)*S.cosh(2*tau))/2;HH=S.sqrt(5)*S.sinh(2*tau)/(2*X);rho0=3/X**2;kapv=3/X;dv=kapv/HH**2;fv=3*HH**2/rho0
     zero('closed_example_product_'+str(tau),dv*fv-3*X)
     ck('closed_example_obstruction_'+str(tau),3*X>2)
    # Threshold implication is purely algebraic; no epsilon or delta is an observed tolerance.
    eps,delta=S.symbols('eps delta',positive=True)
    for ev,dv in [(S.Rational(1,100),S.Rational(1,10)),(S.Rational(1,2),1),(S.Rational(1,4),2)]:ck('illustrative_threshold_'+str((ev,dv)),ev*(1+dv)<=1)
    return rows

def check_calibration():
    rows=[]
    def ck(n,b,d=None):rows.append(dict(name=n,passed=bool(b),detail=d))
    def eq(n,x):y=S.factor(S.simplify(x));ck(n,y==0,str(y))
    k,E,nu,Q=S.symbols('k E nu Q',positive=True)
    a=(1-k)*(1+3*k)/4;s=(1+k)/(k*(1-3*k));F=1+s*E;J=1+(1-3*a)*s*E;C=(1+s)*E/F;q=a/J
    chi=S.symbols('chi',real=True);Ec=(1+chi/s)/(1-chi);B=4*k*k*(1-3*k)/(1+k)**2
    R=C*(1+q)/(1+k)
    eq('global_calibration_ceiling_identity',R.subs(E,Ec)-(1-B*chi*chi/(1-3*k*chi)))
    eq('chi_coupling_identity',q.subs(E,Ec)-k*(1-chi)/(1-3*k*chi))
    eq('maximum_at_origin',R.subs(E,1)-1)
    eq('positive_denominator_split',1-3*k*chi-((1-3*k)+3*k*(1-chi)))
    eq('finite_field_coupling_norm_gap',1-3*a-(1-3*k)**2/4)
    eq('coupling_monotone',S.diff(C,E)-(1+s)/(1+s*E)**2)
    # Independent Euler normalization of a constant-metric quadratic gradient.
    f1,f2,f3,b1,b2,b3=S.symbols('f1 f2 f3 b1 b2 b3',real=True)
    K=S.diag(4,9,16);grad=S.Matrix([f1,f2,f3]);bb=S.Matrix([b1,b2,b3]);L=-Q*(grad.T*K*grad)[0]
    for i in range(3):eq('gradient_Euler_coefficient_'+str(i),S.diff(L,grad[i])+2*Q*(K*grad)[i])
    Gstar=1/(8*S.pi*Q);eq('scalar_Poisson_normalization',4*S.pi*Gstar-1/(2*Q))
    # Stable frozen mass operator: orthogonal eigenbasis with positive spectral weights.
    O=S.Matrix([[S.Rational(3,5),-S.Rational(4,5),0],[S.Rational(4,5),S.Rational(3,5),0],[0,0,1]])
    eq('eigenbasis_orthogonality',sum((O.T*O-S.eye(3))[i,j]**2 for i in range(3) for j in range(3)))
    bvec=S.Matrix([S.Rational(1,3),S.Rational(1,5),S.Rational(1,7)]);white=S.diag(S.Rational(1,2),S.Rational(1,3),S.Rational(1,4))*bvec
    w=[(O[:,i].dot(white))**2 for i in range(3)];eq('spectral_weight_sum',sum(w)-(bvec.T*K.inv()*bvec)[0]);ck('weights_nonnegative',all(x>=0 for x in w))
    r,m=S.symbols('r m',positive=True)
    force=(1+m*r)*S.exp(-m*r)
    eq('force_from_Green_potential',-r*r*S.diff(S.exp(-m*r)/r,r)-force)
    eq('force_kernel_derivative',S.diff(force,r)+m*m*r*S.exp(-m*r))
    eq('force_massless_limit',S.limit(force,m,0)-1)
    eq('force_infinite_range_limit',S.limit(force,r,S.oo))
    for radius in [S.Rational(1,10),S.Rational(1),S.Rational(10)]:
     correction=sum(ww*(1+mm*radius)*S.exp(-mm*radius) for ww,mm in zip(w,[0,1,3]));ck('spectral_force_ceiling_'+str(radius),0<=float(correction)<=float(sum(w)))
    # Calibration inversion and conditional event threshold: all denominators positive.
    Gc,Gb,H2,rho,gamma=S.symbols('Gcal Gbare H2 rho gamma',positive=True)
    Fcal=H2/(8*S.pi*Gc*rho/3);Fbare=H2/(8*S.pi*Gb*rho/3)
    eq('calibration_divides_radiation_diagnostic',(Fcal/Fbare).subs(Gc,gamma*Gb)-1/gamma)
    et,eps,de,mm,cc=S.symbols('eta epsilon delta m cc',positive=True)
    upper=(1+et)*(1+k)/cc;crit=(1+et)*(1+k)*eps*(1+de)/mm
    eq('necessary_coupling_threshold',((mm/upper)-eps*(1+de)).subs(cc,crit))
    # An upper ceiling alone admits an invalid negative calibration; positivity must be separate.
    ck('negative_calibration_does_not_define_positive_diagnostic',Fcal.subs({Gc:-1,H2:1,rho:1})<0)
    # Reconstruct the actual potential at fixed C, then check its total derivative sign form.
    c,aa,ss,t=S.symbols('c aa ss t',positive=True);D=1+ss-ss*c;Einv=c/D;u=S.log(Einv)/(2*S.sqrt(aa));Finv=1+ss*Einv
    U_original=S.Rational(3,2)+S.Rational(3,2)*ss*(Einv-1)**2/Finv**2+nu*(1+ss)*u*u/(2*Finv**2)
    Ufloor=S.Rational(3,2)+S.Rational(3,2)*ss*(1-c)**2+nu*D**2*S.log(c/D)**2/(8*aa*(1+ss))
    eq('potential_coupling_inverse',((1+ss)*Einv/(1+ss*Einv))-c)
    eq('potential_energy_floor_identity',U_original-Ufloor)
    FF=1+ss*S.exp(t);Ut=S.Rational(3,2)+S.Rational(3,2)*ss*(S.exp(t)-1)**2/FF**2+nu*(1+ss)*t*t/(8*aa*FF**2)
    G=12*aa*(S.exp(t)-1)+nu*t*(1-t)+nu*t/(ss*S.exp(t));pref=ss*S.exp(t)*(1+ss)/(4*aa*FF**3)
    eq('total_potential_derivative_sign_factor',S.diff(Ut,t)-pref*G)
    z=S.symbols('z',positive=True)
    for i,term in enumerate([12*aa*(S.exp(t)-1),nu*t*(1-t),nu*t/(ss*S.exp(t))]):
     # At i=0 use f(0)=0 and f'(z)>0 for f=1-exp(-z); symbolic assumptions alone returned None.
     positive_gap=1-S.exp(-z)
     calculus=(positive_gap.subs(z,0)==0 and S.simplify(S.diff(positive_gap,z)-S.exp(-z))==0 and S.exp(-z).is_positive is True)
     sign_ok=calculus if i==0 else term.subs(t,-z).is_negative is True
     ck('negative_u_derivative_term_'+str(i),sign_ok,str(term.subs(t,-z)))
    eq('zero_coupling_log_squared_floor',S.limit(Ufloor/S.log(c)**2,c,0,dir='+')-nu*(1+ss)/(8*aa))
    # Exposed synthetic targets, not fitted values or histories.
    examples=[]
    for kval,nval,ep,mval in itertools.product([S.Rational(1,20),S.Rational(1,10),S.Rational(1,4)],[S.Rational(1,10),S.Rational(1),S.Rational(10)],[S.Rational(1,100),S.Rational(1,10)],[1,2]):
     av=a.subs(k,kval);sv=s.subs(k,kval);cv=(1+kval)*ep*S.Rational(11,10)/mval
     val=Ufloor.subs({c:cv,aa:av,ss:sv,nu:nval});val_half=Ufloor.subs({c:cv/2,aa:av,ss:sv,nu:nval});v=float(val.evalf(30));vh=float(val_half.evalf(30));ck('synthetic_floor_'+str((kval,nval,ep,mval)),0<cv<1 and vh>v>1.5)
     examples.append(dict(k=str(kval),nu=str(nval),epsilon=str(ep),delta='1/10',eta=0,m=mval,Ccrit=str(cv),U_floor=v,U_at_half_Ccrit=vh))
    return rows

def check_slow_past():
    rows=[]
    def ck(n,b,d=None):rows.append(dict(name=n,passed=bool(b),detail=d))
    def eq(n,e):v=S.factor(S.simplify(e));ck(n,v==0,str(v))
    q,Q,C,Cmax,a,Hv,rho,V=S.symbols('q Q C Cmax a Hv rho V',positive=True)
    L,Z=S.symbols('L Z',real=True);wp,rm=S.symbols('wp rm',nonnegative=True)
    w=L*L/q+wp;H=Z-L
    completed=wp+(1-3*q)/q*(L+3*q*Z/(1-3*q))**2-3*Z*Z/(1-3*q)
    eq('kinetic_square_completion',w-3*H*H-completed)
    kap=(Q*w+V+rho+rm)/(3*Q)-H*H
    eq('slow_event_curvature_gap',3*Q*kap-rho-(V+rm+Q*completed))
    # Exact minimum over the velocity component; orthogonal motion increases the gap.
    Lmin=-3*q*Z/(1-3*q)
    eq('stationary_velocity_minimum',S.diff(completed,L).subs(L,Lmin))
    eq('velocity_minimum_value',completed.subs(L,Lmin)-(wp-3*Z*Z/(1-3*q)))
    qq,slack=S.symbols('qq slack',positive=True);qpos=1/(3*(1+qq))
    ck('positive_completed_square_coefficient',S.factor(((1-3*q)/q).subs(q,qpos)).is_positive)
    VV=3*Q*Z*Z/(1-3*q)+slack
    eq('strict_slow_gap_exact_certificate',VV+rm+Q*completed-(slack+rm+Q*wp+Q*(1-3*q)/q*(L+3*q*Z/(1-3*q))**2))
    ck('strict_slow_gap_positive_remainder',(slack+rm+Q*wp).is_positive is True)
    # Derive q(C) from the actual field-dependent action, not a free q selector.
    k,E=S.symbols('k E',positive=True);aa=(1-k)*(1+3*k)/4;ss=(1+k)/(k*(1-3*k));FF=1+ss*E;JJ=1+(1-3*aa)*ss*E;CC=(1+ss)*E/FF;CM=(1+ss)/ss
    qqC=a*(1-C/Cmax)/(1-3*a*C/Cmax);eq('action_norm_as_coupling',qqC.subs({a:aa,C:CC,Cmax:CM})-aa/JJ)
    ratio=(1-3*a)/(C*(1-3*a*C/Cmax))
    eq('norm_to_physical_clock_ratio',(1-3*qqC)/C-ratio)
    cap=Cmax/(12*a)
    eq('quadratic_completion_for_denominator',cap-C*(1-3*a*C/Cmax)-3*a/Cmax*(C-Cmax/(6*a))**2)
    Cstar=Cmax/(6*a)
    eq('ratio_minimum_point_derivative',S.diff(ratio,C).subs(C,Cstar))
    eq('ratio_at_minimum',ratio.subs(C,Cstar)-12*a*(1-3*a)/Cmax)
    eq('positive_margin_k',1-3*aa-(1-3*k)**2/4)
    z=S.symbols('z',positive=True);ap=S.Rational(1,4)+z/(12*(1+z))
    ck('minimizer_inside_Cmax',S.factor(6*ap-1).is_positive)
    ck('positive_uniform_margin',S.factor(1-3*ap).is_positive)
    # Full expression equality proving nonnegative excess; positivity in stated domain.
    eq('ratio_minus_uniform_floor',ratio-12*a*(1-3*a)/Cmax-((1-3*a)*(Cmax-6*a*C)**2/(Cmax*C*(Cmax-3*a*C))))
    hj=S.symbols('HJ',real=True);hstar2=Hv*Hv*12*a*(1-3*a)/Cmax
    eq("threshold_is_exact_coupling_minimum",hstar2/Hv**2-ratio.subs(C,Cstar))
    # Sufficient trigger from V>=3QHv² and C: compare squared quantities exactly.
    rr,ee=S.symbols('rr ee',positive=True)
    trigger_margin=(1-3*q)*Hv*Hv-C*hj*hj
    # Let ratio=hstar²/Hv²+rr and HJ²=hstar²-ee, yielding positive C(Hv²rr+ee).
    eq('strict_trigger_margin',trigger_margin.subs(q,(1-C*(hstar2/Hv**2+rr))/3).subs(hj*hj,hstar2-ee)-C*(Hv*Hv*rr+ee))
    # Proper-time integral and conservation signs, using exact kinematic controls.
    h,T,af,amin,rhof,rhomax=S.symbols('h T af amin rhof rhomax',positive=True)
    at=af*S.exp(-h*T);rho_t=rhof*S.exp(4*h*T)
    eq('proper_time_radius_derivative',-S.diff(S.log(at),T)-h)
    eq('physical_radiation_charge',rho_t*at**4-rhof*af**4)
    eq('radius_duration_boundary',at.subs(T,S.log(af/amin)/h)-amin)
    eq('density_duration_boundary',rho_t.subs(T,S.log(rhomax/rhof)/(4*h))-rhomax)
    # A positive excess H increases growth and preserves the one-sided bounds.
    beta=S.symbols('beta',positive=True);at_excess=af*S.exp(-h*T-beta*(1-S.exp(-T)))
    eq('excess_rate_derivative',-S.diff(S.log(at_excess),T)-(h+beta*S.exp(-T)))
    eq('excess_zero_at_origin',(1-S.exp(-T)).subs(T,0))
    ck('excess_gap_derivative_positive',S.diff(1-S.exp(-T),T).is_positive)
    # Exact critical emergent history: slow past exists but fails future target.
    t=S.symbols('t',real=True);X=1+S.exp(2*t);HH=S.exp(2*t)/X;kapx=2/X;rhox=3/X**2
    for name,expr in [('critical_constraint',3*(HH**2+kapx)-(3+rhox)),('critical_raychaudhuri',S.diff(HH,t)-(kapx-S.Rational(2,3)*rhox)),('critical_radiation',S.diff(rhox,t)+4*HH*rhox)]:eq(name,expr)
    eq('critical_physical_rate_past_zero',S.limit(HH,t,-S.oo))
    eq('critical_past_radius_positive',S.limit(X,t,-S.oo)-1)
    product=kapx/HH**2*3*HH**2/rhox;eq('critical_target_failure_product',product-2*X)
    # No fitted parameters: fixed rational controls across supplied k and coupling intervals.
    for kval,cfrac in itertools.product([S.Rational(1,100),S.Rational(1,10),S.Rational(1,4),S.Rational(3,10)],[S.Rational(1,100),S.Rational(1,4),S.Rational(1,2),S.Rational(3,4),S.Rational(99,100)]):
     av=aa.subs(k,kval);cm=CM.subs(k,kval);cv=cm*cfrac;rat=ratio.subs({a:av,Cmax:cm,C:cv});low=12*av*(1-3*av)/cm
     ck('uniform_bound_'+str((kval,cfrac)),rat>=low>0)
    # Every premature large-magnitude stationary replacement violates a needed inequality.
    qv=S.Rational(1,4);Zv=S.Rational(1);Lv=Lmin.subs({q:qv,Z:Zv});wv=Lv*Lv/qv;kapv=(wv+1+1)/3-(Zv-Lv)**2
    ck('outside_slow_condition_curvature_can_be_negative',kapv<0)
    return rows

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    allrows=[];counts={}
    for name,fn in [('turnaround',check_turnaround),('calibration',check_calibration),('slow_past',check_slow_past)]:
        rows=fn();counts[name]={'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows)}
        allrows.extend([{**x,'name':name+'::'+x['name']} for x in rows])
    result={'scope':'Conditional supplied-action theorems and exposed synthetic controls, not an observational likelihood.','passed':sum(x['passed'] for x in allrows),'failed':sum(not x['passed'] for x in allrows),'units':counts,'checks':allrows,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        p=Path(args.output);assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(1 if result['failed'] else 0)
