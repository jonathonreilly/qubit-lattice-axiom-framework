#!/usr/local/bin/python3
"""Conditional action/scale inverse mathematics; no empirical fit."""
from pathlib import Path
import json,hashlib,argparse
import sympy as s
import mpmath as mp
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/EXPONENTIAL_SCALAR_ACTION_SCALE_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md']

def check_inverse():
    checks=[]
    def zero(name,expr):
        z=s.factor(s.cancel(s.together(expr)))
        checks.append({'name':name,'pass':z==0,'residual':str(z)})
    def nonzero(name,expr):
        z=s.factor(s.cancel(s.together(expr)))
        checks.append({'name':name,'pass':z!=0,'deliberate_defect':str(z)})
    def condition(name,value,detail=None):
        checks.append({'name':name,'pass':bool(value),'detail':detail})
    # Differentiate Friedmann value and check compatibility independently of U.
    H,V,W,rho,pressure,Q,Hv,T,av=s.symbols('H V W rho pressure Q Hv T av',real=True,nonzero=True)
    Hdot=-V-(rho+pressure)/(2*Q)
    rhodot=-3*H*(rho+pressure)+av*(rho-3*pressure)
    Udot=(6*H*Hdot-2*W-rhodot/Q)/(2*Hv**2)
    grad_contract=-(W+3*H*V+av*(rho-3*pressure)/(2*Q))/Hv**2
    zero('first_jet_compatibility',Udot-grad_contract)
    wrong_rhodot=-3*H*(rho+pressure)-av*(rho-3*pressure)
    nonzero('wrong_fluid_exchange_sign',(6*H*Hdot-2*W-wrong_rhodot/Q)/(2*Hv**2)-grad_contract)
    # Curved exact rolling example in flat target metric, C=1, Q=Hv=1.
    x,y,z,t=s.symbols('x y z t',real=True)
    coords=s.Matrix([x,y,z]); curve=s.Matrix([t,t**2,t**3]); vel=curve.diff(t); acc=vel.diff(t)
    Hx=10-x-s.Rational(4,3)*x**3-s.Rational(9,5)*x**5
    Ht=Hx.subs(x,t); speed=vel.dot(vel)
    Ucurve=(3*Hx**2-(1+4*x**2+9*x**4))/2
    g=s.Matrix([-s.diff(curve[i],t,2)-3*Ht*vel[i] for i in range(3)])
    f=s.Matrix([y-x**2,z-x**3]); B=s.Matrix([[2,1],[1,3]])
    U0=Ucurve+g[1].subs(t,x)*f[0]+g[2].subs(t,x)*f[1]
    dU=(f.T*B*f)[0]/2
    sub={x:t,y:t**2,z:t**3}
    grad0=s.Matrix([s.diff(U0,c) for c in coords]); gradD=s.Matrix([s.diff(dU,c) for c in coords])
    zero('rolling_raychaudhuri',s.diff(Ht,t)+speed)
    for i in range(3):
        zero('rolling_scalar_U0_'+str(i),(acc+3*Ht*vel+grad0.subs(sub))[i])
        zero('rolling_scalar_U1_'+str(i),(acc+3*Ht*vel+(grad0+gradD).subs(sub))[i])
    zero('rolling_Friedmann_U0',3*Ht**2-speed-2*U0.subs(sub))
    zero('rolling_Friedmann_U1',3*Ht**2-speed-2*(U0+dU).subs(sub))
    zero('deformation_value',dU.subs(sub))
    for i in range(3): zero('deformation_gradient_'+str(i),gradD.subs(sub)[i])
    hess=s.hessian(dU,coords).subs(sub)
    Df=f.jacobian(coords).subs(sub)
    for i in range(3):
        for j in range(3): zero('normal_Hessian_'+str(i)+str(j),(hess-Df.T*B*Df)[i,j])
    for i in range(3):zero('Hessian_tangent_kernel_'+str(i),(hess*vel)[i])
    condition('positive_definite_B',B[0,0]>0 and B.det()>0,{'principal_minors':[str(B[0,0]),str(B.det())]})
    condition('normal_rank',Df.rank()==2,str(Df))
    # A change with only zero value, not zero gradient, changes the history.
    wrong=f[0]
    nonzero('missing_square_changes_scalar_equation',s.diff(wrong,y).subs(sub))
    nonzero('Hessian_changes',hess[1,1])
    # Covariant Hessian identity is valid for arbitrary connection because dD=0.
    connections=s.symbols('G0:27')
    for a in range(3):
     for b in range(3):
        corr=sum(connections[9*c+3*a+b]*gradD[c].subs(sub) for c in range(3))
        zero('connection_correction_'+str(a)+str(b),corr)
    # Supplied scalar action: vary only nu, keeping K,C fixed.
    k,nu,dnu=s.symbols('k nu dnu',positive=True)
    a=(1-k)*(1+3*k)/4; alpha=s.sqrt(a); ss=(1+k)/(k*(1-3*k)); F=1+ss*s.exp(2*alpha*x); J=1+(1-3*a)*ss*s.exp(2*alpha*x)
    Ku=J/F**2
    DeltaNu=dnu*(1+ss)*x**2/(2*F**2)
    zero('nu_deformation_vacuum_value',DeltaNu.subs(x,0))
    zero('nu_deformation_vacuum_gradient',s.diff(DeltaNu,x).subs(x,0))
    zero('nu_mass_shift',s.diff(DeltaNu,x,2).subs(x,0)/Ku.subs(x,0)-4*dnu/(1-3*k))
    C=(1+ss)*s.exp(2*alpha*x)/F
    zero('vacuum_coupling',((s.diff(C,x)/(2*C))**2/Ku).subs(x,0)-k)
    # Static transfer inversion: use squared q variables to avoid fake branch choices.
    q1,q2,q3,M=s.symbols('q1 q2 q3 M',positive=True)
    h=lambda q:k*q/(q+M)
    x1,x2=1/q1,1/q2; y1,y2=1/h(q1),1/h(q2)
    c1=(y1-y2)/(x1-x2); c0=(x1*y2-x2*y1)/(x1-x2)
    zero('transfer_intercept',c0-1/k);zero('transfer_slope',c1-M/k)
    zero('k_inversion',1/c0-k);zero('mass_inversion',c1/c0-M)
    zero('third_scale_prediction',1/h(q3)-c0-c1/q3)
    jac=s.Matrix([h(q1),h(q2)]).jacobian(s.Matrix([k,M])).det()
    zero('identifiability_determinant',jac-k*q1*q2*(q2-q1)/((q1+M)**2*(q2+M)**2))
    nonzero('wrong_mass_intercept',c1*c0-M)
    nonzero('swapped_potential_force',k*s.exp(-x)*(1+x)-k*s.exp(-x))
    # Exact rational synthetic controls: verification only, not empirical examples.
    examples=[]
    for kval,mval in [(s.Rational(1,100000),s.Rational(1,7)),(s.Rational(1,100),s.Rational(5,2)),(s.Rational(8,25),s.Rational(1,1000))]:
     qs=[s.Rational(1,4),s.Rational(2,1),s.Rational(13,3)]
     hs=[kval*q/(q+mval) for q in qs]
     slope=(1/hs[0]-1/hs[1])/(1/qs[0]-1/qs[1])
     intercept=(1/qs[0]/hs[1]-1/qs[1]/hs[0])/(1/qs[0]-1/qs[1])
     zero('synthetic_k_'+str(kval),1/intercept-kval)
     zero('synthetic_mass_'+str(kval),slope/intercept-mval)
     zero('synthetic_prediction_'+str(kval),1/hs[2]-intercept-slope/qs[2])
     examples.append({'k':str(kval),'mu_squared':str(mval),'q_squared':[str(q) for q in qs],'h':[str(v) for v in hs]})
    # Two supplied hypotheses can fit one scalar readout; no extra observation.
    qobs=s.Rational(3,2);hobs=s.Rational(1,1000)
    m1=qobs*(s.Rational(1,100)/hobs-1);m2=qobs*(s.Rational(1,50)/hobs-1)
    zero('one_scale_family_first',s.Rational(1,100)*qobs/(qobs+m1)-hobs)
    zero('one_scale_family_second',s.Rational(1,50)*qobs/(qobs+m2)-hobs)
    condition('distinct_mass_same_readout',m1!=m2 and m1>0 and m2>0,{'mass1':str(m1),'mass2':str(m2)})

    return {'checks':checks,'synthetic_examples':examples,'rolling_example':{'curve':[str(c) for c in curve],'H':str(Ht),'base_potential':str(s.factor(U0)),'deformation':str(dU),'Hessian_on_curve':str(hess)}}

def check_readout():
    checks=[]
    def exact(name,e):
     e=s.factor(s.cancel(s.trigsimp(s.simplify(e))));checks.append({'name':name,'passed':e==0,'residual':str(e)})
    def control(name,ok,detail):checks.append({'name':name,'passed':bool(ok),'detail':detail})
    r,b,z,mu,m,k,c,x,r1,r2,R,rp=s.symbols('r b z mu m k c x r1 r2 R rp',positive=True)
    Phi=m*(1+k*s.exp(-mu*r))/r;Psi=m*(1-k*s.exp(-mu*r))/r
    F=lambda x:(1+x)*s.exp(-x)
    exact('Weyl_potential',(Phi+Psi)/2-m/r)
    exact('radial_acceleration',-s.diff(Phi,r)-m*(1+k*F(mu*r))/r**2)
    primitive=2*m*z/(b*s.sqrt(b*b+z*z))
    exact('deflection_integrand',s.diff(primitive,z)-2*m*b/(b*b+z*z)**s.Rational(3,2))
    exact('deflection_total',s.limit(primitive,z,s.oo)-s.limit(primitive,z,-s.oo)-4*m/b)
    acc=c*c*m*(1+k*F(mu*r))/r**2;theta=4*m/b
    exact('mass_normalization_cancellation',4*r*r*acc/(c*c*b*theta)-1-k*F(mu*r))
    L=s.log(1+mu*r1)-s.log(1+mu*r2)+mu*(r2-r1)
    exact('ratio_log_derivative',s.diff(L,mu)-mu*(r2*r2/(1+mu*r2)-r1*r1/(1+mu*r1)))
    exact('radius_monotonicity',s.diff(r*r/(1+mu*r),r)-r*(2+mu*r)/(1+mu*r)**2)
    exact('zero_mass_ratio',L.subs(mu,0))
    exact('force_series',s.series(F(x),x,0,4).removeO()-(1-x*x/2+x**3/3))
    exact('ratio_series',s.series(L,mu,0,4).removeO()-(mu**2*(r2*r2-r1*r1)/2-mu**3*(r2**3-r1**3)/3))
    # Exterior angular Green integral after replacing separation variable.
    angular=(s.exp(-mu*(r-rp))-s.exp(-mu*(r+rp)))/(mu*r*rp)
    exact('external_spherical_Yukawa_kernel',angular-2*s.exp(-mu*r)*s.sinh(mu*rp)/(mu*r*rp))
    ball=3*(x*s.cosh(x)-s.sinh(x))/x**3
    exact('uniform_ball_radial_integral',s.diff(mu*rp*s.cosh(mu*rp)-s.sinh(mu*rp),rp)-mu**2*rp*s.sinh(mu*rp))
    exact('uniform_ball_small_mass',s.series(ball,x,0,6).removeO()-(1+x*x/10+x**4/280))
    charge=s.symbols('charge',positive=True)
    exact('finite_body_ratio_cancellation',(k*charge*F(mu*r1))/(k*charge*F(mu*r2))-F(mu*r1)/F(mu*r2))
    # Source trace is mandatory; an equation with rho instead of rho-3p fails.
    rho,pressure=s.symbols('rho pressure',positive=True)
    exact('trace_free_source', (rho-3*pressure).subs(pressure,rho/3))
    control('wrong_force_without_derivative_factor',s.simplify(-s.diff(Phi,r)-m*(1+k*s.exp(-mu*r))/r**2)!=0,str(s.simplify(-s.diff(Phi,r)-m*(1+k*s.exp(-mu*r))/r**2)))
    control('wrong_pressure_omission',rho.subs(pressure,rho/3)!=0,'rho source remains nonzero for trace-free pressure=rho/3')
    # Independent root solve of the parent analytic inverse, synthetic values only.
    mp.mp.dps=80
    rows=[]
    for ks,ms in [('0.00001','0.1'),('0.01','1'),('0.2','10')]:
     kk=mp.mpf(ks);mm=mp.mpf(ms);rr1=mp.mpf(1);rr2=mp.mpf(2);rr3=mp.mpf(3)
     ff=lambda v:(1+v)*mp.exp(-v)
     e1=kk*ff(mm*rr1);e2=kk*ff(mm*rr2);e3=kk*ff(mm*rr3)
     target=mp.log(e1/e2)
     fn=lambda v:mp.log1p(v*rr1)-mp.log1p(v*rr2)+v*(rr2-rr1)
     lo=mp.mpf(0);hi=mp.mpf(1)
     while fn(hi)<target:hi*=2
     for _ in range(300):
      mid=(lo+hi)/2
      if fn(mid)<target:lo=mid
      else:hi=mid
     est=(lo+hi)/2;kest=e1/ff(est*rr1);pred=kest*ff(est*rr3)
     errors=[abs(est-mm)/max(1,abs(mm)),abs(kest-kk)/kk,abs(pred-e3)/e3]
     control('synthetic_inverse_'+ks,all(e<mp.mpf('1e-60') for e in errors),[mp.nstr(e,12) for e in errors])
     # Numerical line integral is a cross check of exact primitive.
     bend=mp.quad(lambda zz:2/(1+zz*zz)**mp.mpf('1.5'),[-mp.inf,0,mp.inf])
     control('light_integral_'+ks,abs(bend-4)<mp.mpf('1e-65'),mp.nstr(bend,20))
     rows.append({'k':ks,'mu':ms,'radii':['1','2','3'],'excess':[mp.nstr(v,70) for v in [e1,e2,e3]],'recovered_mu':mp.nstr(est,70),'recovered_k':mp.nstr(kest,70),'third_radius_prediction':mp.nstr(pred,70)})

    return {'checks':checks,'synthetic':rows}

def check_scale():
    Q0,H,k,lam,M=s.symbols('Q0 H k lambda M',positive=True);Q=Q0*(1+k);r=H**2/Q0;Xi=Q/H**2;R,K,U,V=s.symbols('R K U V');rows=[]
    def check(n,expr):rows.append({'name':n,'passed':s.simplify(expr)==0})
    original=Q*H**-4*V*(H**2*R/2-H**2*K-2*H**2*U)
    check('four_dimensional_action_scaling',original-Xi*V*(R/2-K-2*U))
    check('variation_prefactor',s.diff(Xi*V*(R/2-K-2*U),U)/Xi-s.diff(V*(R/2-K-2*U),U))
    check('vacuum_newton_cancellation',(1+k)/(8*s.pi*Q)-1/(8*s.pi*Q0))
    check('physical_hierarchy',r-8*s.pi*(1/(8*s.pi*Q0))*H**2)
    check('units_invariance',(lam*H)**2/(lam**2*Q0)-r)
    check('prefactor_relation',Xi-(1+k)/r)
    check('worldline_coefficient',(M/H)/Xi-M*H/Q)
    for v in [s.Rational(1,7),s.Integer(2),s.Integer(11)]:
     check('unknown_mass_coefficient_'+str(v),(v*M)*H/(v*Q)-M*H/Q)
     check('unknown_mass_m_'+str(v),(v*M)/(8*s.pi*v*Q)-M/(8*s.pi*Q))
     check('known_mass_force_changes_'+str(v),M/(8*s.pi*v*Q)-(M/(8*s.pi*Q))/v)
     check('physical_hierarchy_changes_'+str(v),H**2/(v*Q0)-r/v)
     check('dimensionless_vacuum_equation_'+str(v),(v*Xi*s.Symbol('E'))/(v*Xi)-s.Symbol('E'))
    rows.extend([{'name':'positive_domain_required','passed':bool(Q.is_positive and H.is_positive and Xi.is_positive)},{'name':'nonselection_is_not_equal_known_mass_force','passed':bool(s.simplify(M/(16*s.pi*Q)-M/(8*s.pi*Q))!=0)}])

    return {'checks':rows}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    checks=[];units={};outputs={}
    for name,fn in [('inverse',check_inverse),('readout',check_readout),('scale',check_scale)]:
        result=fn();rows=result.pop('checks');normalized=[]
        for row in rows:
            item=dict(row)
            if 'pass' in item:item['passed']=item.pop('pass')
            normalized.append({**item,'name':name+'::'+item['name']})
        checks.extend(normalized);outputs[name]=result
        units[name]={'passed':sum(x['passed'] for x in normalized),'failed':sum(not x['passed'] for x in normalized)}
    result={'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'checks':checks,'units':units,'substantive_outputs':outputs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Conditional inverse and nonselection results; no observed fit or selected action/state/scale.'}
    if args.output:
        p=Path(args.output);assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(bool(result['failed']))
