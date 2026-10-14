#!/usr/local/bin/python3
"""Conditional finite-body geometry and stationary matter-environment bridge."""
from pathlib import Path
import sys,json,hashlib,argparse,math
import sympy as S
import numpy as np
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md','docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md','docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md','docs/EXPONENTIAL_SCALAR_THERMAL_BOUNCE_BOUNDED_THEOREM_NOTE_2026-10-14.md']

def check_finite_body():
    checks=[]
    def ck(n,v,d=None):checks.append(dict(name=n,passed=bool(v),detail=d))
    def eq(n,e):
     v=S.factor(S.simplify(e));ck(n,v==0,str(v))
    r,mu,z=S.symbols('r mu z',positive=True)
    f=(1+z)*S.exp(-z)
    eq('force_from_Yukawa_potential',S.diff(-S.exp(-mu*r)/r,r)-(1+mu*r)*S.exp(-mu*r)/r**2)
    eq('pair_force_monotone',S.diff(f,z)+z*S.exp(-z))
    eq('pair_force_at_zero',f.subs(z,0)-1)
    ck('pair_force_nonnegative',f.is_positive)
    t=S.symbols('t',positive=True)
    form=3*(z*S.cosh(z)-S.sinh(z))/z**3
    primitive=3*(z*t*S.cosh(z*t)-S.sinh(z*t))/z**3
    eq('sphere_radial_primitive',S.diff(primitive,t)-3*t*t*S.sinh(z*t)/(z*t))
    eq('sphere_formfactor_integral',primitive.subs(t,1)-primitive.subs(t,0)-form)
    ck('sphere_massless_limit',S.limit(form,z,0)==1)
    eq('stable_sphere_factor',(form*S.exp(-z)).rewrite(S.exp)-3*((z-1)+(z+1)*S.exp(-2*z))/(2*z**3))
    kappa,q,I0=S.symbols('kappa q I0',positive=True)
    plus=(kappa+1)/2;minus=(kappa-1)/2
    eq('signed_kernel_difference',plus-minus-1)
    eq('signed_kernel_total_variation',plus+minus-kappa)
    cap=1+q*(kappa+1)/2
    eq('signed_upper_normalization',cap-(1+q*plus))
    eq('signed_lower_normalization',(1-q*(kappa-1)/2)-(1-q*minus))
    eta,sigma,lam,L=S.symbols('eta sigma lam L',positive=True)
    R=S.Rational(11,4)**S.Rational(1,3)
    calcap=(1+eta)*(kappa+7)/6
    bare=2*lam**2/(R*sigma**S.Rational(4,3))
    product=bare/calcap
    eq('universal_geometry_calibration_cap',cap.subs(q,S.Rational(1,3))*(1+eta)-calcap)
    eq('joint_thermal_geometry_product',product-12*lam**2/(R*sigma**S.Rational(4,3)*(1+eta)*(kappa+7)))
    eq('positive_geometry_recovers_same_background',product.subs(kappa,1)-3*lam**2/(2*R*sigma**S.Rational(4,3)*(1+eta)))
    threshold=12/R-7
    eq('unit_geometry_threshold',product.subs({lam:1,sigma:1,eta:0,kappa:threshold})-1)
    ck('threshold_contains_positive_geometry',threshold>1)

    # A concrete signed differential observable, no particular apparatus asserted.
    def force_weight(zz):return (1+zz)*math.exp(-zz)
    for val in [.1,1.,10.]:
     ck('implemented_pair_force_'+str(val),abs(force_weight(val)-float(f.subs(z,val)))<3e-14)
    weights=np.array([1.,-.9]);seps=np.array([1.,10.]);ratio=sum(a*force_weight(b) for a,b in zip(weights,seps))/sum(weights)
    kap=sum(abs(weights))/abs(sum(weights));qq=.1;gamma=1+qq*ratio
    ck('signed_readout_exceeds_point_source_cap',gamma>1+qq,dict(ratio=ratio,gamma=gamma,kappa=kap))
    ck('signed_readout_obeys_decomposition',-(kap-1)/2<=ratio<=(kap+1)/2)
    ck('signed_geometry_not_positive_geometry',kap>1)

    # Stable full sphere factor: each S*exp(-x) is evaluated without overflow.
    def scaled_form(x):
     if x==0:return 1.
     if abs(x)<.5:
      return math.exp(-x)*sum(6*(n+1)*x**(2*n)/math.factorial(2*n+3) for n in range(10))
     return 3*((x-1)+(x+1)*math.exp(-2*x))/(2*x**3)
    def complete_factor(x,y,z):
     return scaled_form(x)*scaled_form(y)*(1+z)*math.exp(-(z-x-y))
    sphere_grid=[]
    for xx in [0.,.0001,.01,.3,1.,5.,20.,100.]:
     for yy in [0.,.02,.7,3.,30.]:
      for gap in [.001,.1,2.,10.]:
       zz=xx+yy+gap;fac=complete_factor(xx,yy,zz)
       ck('nonoverlap_sphere_cap_'+str((xx,yy,gap)),0<=fac<=1+3e-11,fac)
       sphere_grid.append(dict(x=xx,y=yy,z=zz,factor=fac))
    for xx in [.01,.1,1.,5.,20.]:
     v,e=quad(lambda t:3*t*t*math.sinh(xx*t)/(xx*t)*math.exp(-xx),0,1,epsabs=1e-13,epsrel=1e-13)
     ck('sphere_source_radial_quadrature_'+str(xx),abs(v-scaled_form(xx))<3e-12,dict(integral=v,closed=scaled_form(xx),error=e))

    # Independent integration over test-body volume of the source's exterior force.
    # Fixed spherical densities are supplied; this is not a self-consistent body model.
    def test_volume(mu,rs,rt,d,n):
     xs,ws=leggauss(n);rad=(xs+1)/2;wr=ws/2
     rr=rt*rad[:,None];cost=xs[None,:]
     distance=np.sqrt(d*d+rr*rr+2*d*rr*cost)
     projection=d+rr*cost
     kernel=3*rad[:,None]**2*wr[:,None]*ws[None,:]/2*projection/distance**3*d*d
     Ssource=scaled_form(mu*rs)*math.exp(mu*rs)
     massive=(1+mu*distance)*np.exp(-mu*distance)
     return float(np.sum(kernel)*1),float(Ssource*np.sum(kernel*massive)),float(np.min(kernel))
    volume=[]
    for case in [(0.,.4,.3,1.),(1.,.3,.2,1.),(1.,1.2,.5,2.),(1.,2.,3.,5.5),(2.,.1,.9,1.1)]:
     mm,rs,rt,dd=case;expected=complete_factor(mm*rs,mm*rt,mm*dd)
     n80=test_volume(*case,80);n160=test_volume(*case,160)
     ck('sphere_volume_Newton_normalization_'+str(case),abs(n80[0]-1)<3e-11,n80[0])
     ck('sphere_volume_Yukawa_formula_'+str(case),abs(n80[1]-expected)<3e-11,dict(volume=n80[1],formula=expected))
     ck('sphere_volume_resolution_'+str(case),abs(n80[1]-n160[1])<3e-11)
     ck('sphere_volume_positive_kernel_'+str(case),n80[2]>=0)
     volume.append(dict(case=case,n80=n80,n160=n160,expected=expected))
    return {'checks':checks,'sphere_grid':sphere_grid,'test_volume_quadratures':volume,'signed_control':dict(ratio=ratio,gamma=gamma,kappa=kap),'thermal_geometry_threshold':str(S.N(threshold,25))}

def check_density_environment():
    mp.mp.dps=80
    checks=[]
    def ck(name,ok,**data):
     checks.append(dict(name=name,passed=bool(ok),**data))
    def eq(name,expr):
     v=S.factor(S.together(S.expand(expr)))
     ck(name,v==0,residual=str(v))
    z,s,a,nu,ds,Q,H,rj=S.symbols('z s a nu ds Q H rj',positive=True)
    D=1+s-s*z*z;L=S.log(D/z**2)
    U=S.Rational(3,2)+S.Rational(3,2)*s*(1-z*z)**2+nu*D**2*L**2/(8*a*(1+s))
    dstar=6*s*z*(1-z*z)+nu*D/(2*a*(1+s))*(s*z*L**2+(1+s)*L/z)
    dj=dstar/z**3
    particle_power=1
    source_factor=S.Integer(1)
    W=U+source_factor*ds*z**particle_power
    fixed_density_hessian=S.diff(U,z,2)
    physical_mass_power=2
    # Vary actual energy from -sum m A ds_E and the supplied -2QH^2U action.
    actual_energy=2*Q*H**2*U+(2*Q*H**2*ds)*z
    eq('source_from_actual_particle_and_scalar_energy',S.diff(actual_energy,z)/(2*Q*H**2)-S.diff(W,z))
    eq('closed_negative_potential_derivative',S.diff(U,z)+dstar)
    eq('physical_density_A_cubed',dj*z**3-dstar)
    eq('fixed_particle_stationarity',S.diff(W,z)-(ds-dstar))
    eq('physical_density_force_from_trace',rj*z**4/z-rj*z**3)
    eq('fixed_particle_hessian',S.diff(W,z,2)-fixed_density_hessian)
    eq('density_map_derivative_hessian',fixed_density_hessian+z**3*S.diff(dj,z)+3*z**2*dj)
    eq('log_derivative',S.diff(L,z)+2*(1+s)/(z*D))
    eq('D_derivative',S.diff(D,z)+2*s*z)
    eq('first_monotone_term_derivative',S.diff(6*s*(z**-2-1),z)+12*s/z**3)
    # Derivative of each positive product is a sum of negative terms on 0<z<1.
    Lz=-2*(1+s)/(z*D);Dz=-2*s*z
    term1prime=Dz*L**2/z**2+2*D*L*Lz/z**2-2*D*L**2/z**3
    term2prime=Dz*L/z**4+D*Lz/z**4-4*D*L/z**5
    eq('first_product_monotonic_decomposition',S.diff(D*L**2/z**2,z)-term1prime)
    eq('second_product_monotonic_decomposition',S.diff(D*L/z**4,z)-term2prime)
    eq('full_physical_density_monotonic_decomposition',S.diff(dj,z)-(-12*s/z**3+nu*(s*term1prime+(1+s)*term2prime)/(2*a*(1+s))))
    eq('endpoint_dstar_one',dstar.subs(z,1))
    eq('endpoint_dj_one',dj.subs(z,1))
    # Independent exact sign brackets; no decimal logarithm establishes existence.
    kr=S.Rational(1,10);sr=S.Rational(110,7);ar=S.Rational(117,400);nr=S.Rational(1,10000)
    eq('candidate_a',ar-(1-kr)*(1+3*kr)/4)
    eq('candidate_s',sr-(1+kr)/(kr*(1-3*kr)))
    zlo=S.Rational(1,10);Dlo=D.subs({z:zlo,s:sr});ratio=S.factor(Dlo/zlo**2)
    eq('bracket_log_argument',ratio-S.Rational(11590,7))
    ck('exp_one_lower_bound',sum(S.Rational(1,S.factorial(i)) for i in range(5))>S.Rational(8,3))
    ck('exp_eight_lower_bound',(S.Rational(8,3))**8>ratio)
    upper=(6*s*z*(1-z*z)+nu*D/(2*a*(1+s))*(s*z*64+(1+s)*8/z)).subs({z:zlo,s:sr,a:ar,nu:nr})
    ck('dstar_tenth_less_than_twenty',upper<20,exact_upper=str(upper),upper=float(upper))
    ck('dstar_half_greater_than_twenty',S.Rational(9,4)*sr>20,exact_lower=str(S.Rational(9,4)*sr))
    # Full three-field stationary mass uses K>0 and zero full gradient.
    K,zu,mp2=S.symbols('K zu mp2',positive=True)
    predicted_mj=mp2/z**physical_mass_power
    eq('physical_mass_frame_conversion',predicted_mj*z**2-mp2)
    eq('stationary_coordinate_hessian_mass',zu**2*fixed_density_hessian/K-zu**2*S.diff(W,z,2)/K)
    # Parameter/grid evaluations only check implementations of the analytic signs.
    fn=S.lambdify((z,s,a,nu),dstar,'mpmath');fj=S.lambdify((z,s,a,nu),dj,'mpmath');fjp=S.lambdify((z,s,a,nu),S.diff(dj,z),'mpmath')
    fU=S.lambdify((z,s,a,nu),U,'mpmath');fU2=S.lambdify((z,s,a,nu),S.diff(U,z,2),'mpmath')
    srmp=mp.mpf(110)/7;armp=mp.mpf(117)/400;nrmp=mp.mpf(1)/10000
    rows=[]
    for kv in ['0.01','0.1','0.3']:
     k=mp.mpf(kv);sv=(1+k)/(k*(1-3*k));av=(1-k)*(1+3*k)/4
     for nv in ['0.0001','1','100']:
      for zv in ['0.00001','0.01','0.1','0.5','0.9','0.999']:
       zz=mp.mpf(zv);nn=mp.mpf(nv);dv=fj(zz,sv,av,nn);der=fjp(zz,sv,av,nn)
       ck('density_positive_and_decreasing_'+kv+'_'+nv+'_'+zv,dv>0 and der<0)
       rows.append(dict(k=kv,nu=nv,z=zv,dj=mp.nstr(dv,40),dj_prime=mp.nstr(der,40)))
    def bisect(lo,hi):
     fl=fn(lo,srmp,armp,nrmp)-20;fh=fn(hi,srmp,armp,nrmp)-20
     assert fl*fh<0
     for _ in range(300):
      mid=(lo+hi)/2;fm=fn(mid,srmp,armp,nrmp)-20
      if abs(fm)<mp.mpf('1e-65'):return mid
      if fl*fm<0:hi=mid;fh=fm
      else:lo=mid;fl=fm
     return (lo+hi)/2
    roots=[]
    for i,(lo,hi,sign) in enumerate([('0.000001','0.1',1),('0.1','0.5',-1),('0.5','0.999999',1)]):
     zz=bisect(mp.mpf(lo),mp.mpf(hi));res=fn(zz,srmp,armp,nrmp)-20;hess=fU2(zz,srmp,armp,nrmp)
     zz_double=brentq(lambda q:float(fn(mp.mpf(q),srmp,armp,nrmp))-20,float(lo),float(hi),xtol=1e-15,rtol=1e-14)
     dd=1+srmp-srmp*zz*zz;ll=mp.log(dd/zz**2);uu=-ll/(2*mp.sqrt(armp));ee=zz*zz/dd;FF=1+srmp*ee;JJ=1+(1-3*armp)*srmp*ee;kuu=JJ/FF**2;zz_u=mp.sqrt(armp)*zz/FF
     mass=zz_u**2*hess/kuu;massj=mass/zz**physical_mass_power;djv=20/zz**3;qq=armp/JJ;mu=zz**2*(1+qq)/(1+mp.mpf('0.1'))
     ck('root_stationarity_'+str(i),abs(res)<mp.mpf('1e-60'),residual=mp.nstr(res,8))
     ck('root_local_hessian_sign_'+str(i),sign*hess>0)
     ck('independent_bracket_solver_'+str(i),abs(zz-mp.mpf(zz_double))<mp.mpf('2e-14'))
     ck('root_observed_density_map_'+str(i),abs(fj(zz,srmp,armp,nrmp)-djv)/djv<mp.mpf('1e-60'))
     # Check mass by varying the original u parametrization at fixed particle density.
     def orig(uv):
      ev=mp.exp(2*mp.sqrt(armp)*uv);fv=1+srmp*ev;cv=(1+srmp)*ev/fv
      return mp.mpf('1.5')+mp.mpf('1.5')*srmp*(ev-1)**2/fv**2+nrmp*(1+srmp)*uv**2/(2*fv**2)+20*mp.sqrt(cv)
     mh=mp.diff(orig,uu,2)/kuu
     ck('original_u_mass_'+str(i),abs(mh-mass)/(1+abs(mass))<mp.mpf('1e-60'))
     roots.append(dict(index=i,z=mp.nstr(zz,60),u=mp.nstr(uu,40),delta_j=mp.nstr(djv,40),Uzz=mp.nstr(hess,40),mE2_over_Hv2=mp.nstr(mass,40),mJ2_over_Hv2=mp.nstr(massj,40),W=mp.nstr(fU(zz,srmp,armp,nrmp)+20*zz,40),q=mp.nstr(qq,40),principal_G_over_vacuum=mp.nstr(mu,40)))
    ck('distinct_physical_densities',len(set(r['delta_j'] for r in roots))==3)
    ck('two_positive_one_negative_local_masses',all(float(r['mE2_over_Hv2'])*sg>0 for r,sg in zip(roots,[1,-1,1])))
    ck('stability_not_implied_by_monotone_density',float(roots[1]['Uzz'])<0 and fjp(mp.mpf(roots[1]['z']),srmp,armp,nrmp)<0)
    return {'checks':checks,'exact_upper_at_tenth':str(upper),'grid':rows,'roots':roots}

def check_susceptibility(prior):
    mp.mp.dps=80
    rows=[]
    def ck(n,v,detail=None):rows.append(dict(name=n,passed=bool(v),detail=detail))
    def eq(n,v):
     print('CHECK',n,file=sys.stderr,flush=True);r=S.cancel(S.together(v));ck(n,r==0,str(r))
    z,s,a,nu,q=S.symbols('z s a nu q',positive=True);D=1+s-s*z*z;L=S.log(D/z**2)
    U=S.Rational(3,2)+S.Rational(3,2)*s*(1-z*z)**2+nu*D**2*L**2/(8*a*(1+s))
    dj=6*s*(z**-2-1)+nu*D/(2*a*(1+s))*(s*L**2/z**2+(1+s)*L/z**4)
    slope=-z*S.diff(dj,z)/dj
    stable_threshold=3
    mass_formula=q*z*z*dj*(slope-stable_threshold)
    eq('mass_slope_identity',mass_formula-q*S.diff(U,z,2))
    eq('density_slope_definition',slope*dj+z*S.diff(dj,z))
    eq('stationary_log_susceptibility',(-1/slope)*(z*S.diff(dj,z))-dj)
    eq('weighted_density_decomposition',z*z*dj-(6*s*(1-z*z)+nu*D/(2*a*(1+s))*(s*L**2+(1+s)*L/z**2)))
    Dz=-2*s*z;Lz=-2*(1+s)/(z*D)
    negative_terms=-12*s*z+nu/(2*a*(1+s))*(Dz*(s*L**2+(1+s)*L/z**2)+D*(2*s*L*Lz+(1+s)*(Lz/z**2-2*L/z**3)))
    eq('weighted_density_strict_derivative',S.diff(z*z*dj,z)-negative_terms)
    eq('slope_above_two_identity',z*S.diff(z*z*dj,z)-z*z*dj*(2-slope))
    eq('near_vacuum_density_derivative',S.diff(dj,z).subs(z,1)+12*s+nu*(1+s)/a)
    lead=nu*(1+s)*L/(2*a*z**4)
    ratio_decomp=D/(1+s)+D*s*z*z*L/(1+s)**2+12*a*s*z*z*(1-z*z)/(nu*(1+s)*L)
    eq('small_A_density_leading_decomposition',dj/lead-ratio_decomp)
    # These elementary limits control the subleading terms and their derivatives.
    t=S.symbols('t',positive=True)
    ck('elementary_log_power_limit',S.limit(z*z*S.log(z),z,0,dir='+')==0)
    ck('elementary_inverse_log_power_limit',S.limit(z*z/S.log(z),z,0,dir='+')==0)
    ck('constant_density_leading_D',S.limit(D/(1+s),z,0,dir='+')==1)
    f=S.lambdify((z,s,a,nu),slope,'mpmath');fd=S.lambdify((z,s,a,nu),dj,'mpmath')
    ss=mp.mpf(110)/7;aa=mp.mpf(117)/400;nn=mp.mpf(1)/10000
    root_rows=[]
    for r in prior['roots']:
     zz=mp.mpf(r['z']);dd=fd(zz,ss,aa,nn);sl=f(zz,ss,aa,nn);qq=mp.mpf(r['q']);mm=qq*zz*zz*dd*(sl-stable_threshold);expected=mp.mpf(r['mJ2_over_Hv2'])
     ck('saved_root_mass_'+str(r['index']),abs(mm-expected)/(1+abs(expected))<mp.mpf('1e-37'))
     ck('saved_root_susceptibility_range_'+str(r['index']),-mp.mpf('.5') < -1/sl <0)
     ck('saved_root_stability_equivalence_'+str(r['index']),(sl>3)==(expected>0))
     root_rows.append(dict(index=r['index'],S_env=mp.nstr(sl,40),stationary_log_susceptibility=mp.nstr(-1/sl,40)))
    small=[];near=[]
    for zz in [mp.mpf('1e-4'),mp.mpf('1e-6'),mp.mpf('1e-9'),mp.mpf('1e-12')]:
     sl=f(zz,ss,aa,nn);ll=mp.log((1+ss-ss*zz*zz)/zz**2);ld=nn*(1+ss)*ll/(2*aa*zz**4);ratio=fd(zz,ss,aa,nn)/ld
     ck('small_A_slope_bound_'+str(zz),sl>4 and sl<mp.mpf('4.2'))
     remainder_bound=ss*zz**2/(1+ss)+(1+ss-ss*zz**2)*ss*zz**2*ll/(1+ss)**2+12*aa*ss*zz**2*(1-zz**2)/(nn*(1+ss)*ll)
     ck('small_A_density_exact_remainder_'+str(zz),abs(ratio-1)<=remainder_bound+mp.mpf('1e-70'))
     small.append(dict(A=str(zz),S_env=mp.nstr(sl,40),density_over_leading=mp.nstr(ratio,40)))
    for eps in [mp.mpf('1e-3'),mp.mpf('1e-5'),mp.mpf('1e-7')]:
     zz=1-eps;sl=f(zz,ss,aa,nn);ratio=fd(zz,ss,aa,nn)/(eps*(12*ss+nn*(1+ss)/aa))
     ck('near_vacuum_positive_mass_slope_'+str(eps),sl>3)
     ck('near_vacuum_first_order_'+str(eps),abs(ratio-1)<2*eps)
     near.append(dict(one_minus_A=str(eps),S_env=mp.nstr(sl,40),density_over_linear=mp.nstr(ratio,40)))
    ck('small_A_slope_approaches_four',all(abs(mp.mpf(small[i+1]['S_env'])-4)<abs(mp.mpf(small[i]['S_env'])-4) for i in range(len(small)-1)))
    ck('small_A_density_relative_error_contracts',all(abs(mp.mpf(small[i+1]['density_over_leading'])-1)<abs(mp.mpf(small[i]['density_over_leading'])-1) for i in range(len(small)-1)))
    return {'checks':rows,'root_diagnostics':root_rows,'small_A_controls':small,'near_vacuum_controls':near}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    checks=[];units={};outputs={}
    for name,fn in [('finite_body',check_finite_body),('density_environment',check_density_environment),('susceptibility',lambda:check_susceptibility(outputs['density_environment']))]:
        result=fn();rows=result.pop('checks');outputs[name]=result
        units[name]={'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows)}
        checks.extend([{**row,'name':name+'::'+row['name']} for row in rows])
    result={'scope':'Conditional finite-body and stationary-density mathematics; no actual apparatus fit or state selection.','passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'units':units,'checks':checks,'substantive_outputs':outputs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        p=Path(args.output);assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));raise SystemExit(bool(result['failed']))
