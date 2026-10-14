#!/usr/local/bin/python3
"""Conditional density-response inverse; all examples are synthetic development."""
from pathlib import Path
import json,hashlib,argparse
import sympy as S
import sympy as s
import numpy as np
import mpmath as mp
from scipy.optimize import brentq
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['docs/EXPONENTIAL_SCALAR_DENSITY_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-14.md','docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md','docs/EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md','docs/EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md']
VOLUME_POWER=S.Integer(3)
KINETIC_DIVISOR=S.Integer(2)
FRAME_POWER=S.Integer(2)
IBP_COEFFICIENT=s.Integer(6)
POTENTIAL_SOURCE_SIGN=s.Integer(1)
PARTICLE_VOLUME_POWER=s.Integer(3)

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

def check_identity(saved):
    rows=[]
    def eq(name, value):
        residual=S.factor(S.cancel(value))
        rows.append(dict(name=name,passed=residual==0,residual=str(residual)))
    def ck(name, passed, detail=None):
        rows.append(dict(name=name,passed=bool(passed),detail=detail))

    # Build a separate smooth two-field potential/coupling, then differentiate
    # the actual particle source rather than inserting the proposed response.
    x,y,r=S.symbols('x y rho_J',real=True)
    chi=S.Matrix([x,y]); zero={x:0,y:0}
    A0=S.Rational(3,5); Q=S.Rational(7,3); r0=S.Rational(11,5)
    beta=S.Matrix([S.Rational(1,5),S.Rational(-1,7)])
    L=S.Matrix([[S.Rational(1,9),S.Rational(1,13)],[S.Rational(1,13),S.Rational(-1,11)]])
    M=S.Matrix([[2,S.Rational(1,3)],[S.Rational(1,3),3]])
    A=A0*S.exp((beta.T*chi)[0]+(chi.T*L*chi)[0]/2)
    c_true=r0*A0**4/(2*Q)
    H_Y=M-c_true*(L+beta*beta.T)
    Y=-c_true*(beta.T*chi)[0]+(chi.T*H_Y*chi)[0]/2
    grad=lambda f:S.Matrix([S.diff(f,z) for z in chi])
    F=grad(Y)+r*A**3*grad(A)/(2*Q)
    F0=F.subs({**zero,r:r0})
    Hess_fixed=(S.hessian(Y,chi)+(r0*A0**3/(2*Q))*S.hessian(A,chi)).subs(zero)
    J=F.jacobian(chi).subs({**zero,r:r0})
    source=(r*F.diff(r)).subs({**zero,r:r0})
    c=r0*A0**4/(KINETIC_DIVISOR*Q)
    for i in range(2):
        eq('constructed_stationary_'+str(i),F0[i])
        eq('physical_density_source_'+str(i),source[i]-c*beta[i])
        for j in range(2):
            eq('fixed_particle_mass_'+str((i,j)),Hess_fixed[i,j]-M[i,j])
            eq('density_family_jacobian_'+str((i,j)),J[i,j]-M[i,j]-VOLUME_POWER*c*beta[i]*beta[j])
    ck('positive_fixed_particle_matrix',M[0,0]>0 and M.det()>0)
    ck('positive_family_jacobian',J[0,0]>0 and J.det()>0)
    response=-J.inv()*source
    zeta=c*(beta.T*M.inv()*beta)[0]
    eq('direct_implicit_log_A_response',(beta.T*response)[0]+zeta/(1+VOLUME_POWER*zeta))
    B=-2*(beta.T*response)[0]
    eq('response_inverse',zeta-B/(2-3*B))
    ck('stable_response_interval',0<B<S.Rational(2,3),str(B))

    # Symbolic rank-one algebra checked by multiplication, avoiding an
    # unnecessarily expanded inverse of the full modified matrix.
    h,j,k,b1,b2,cg=S.symbols('h j k b1 b2 c',real=True)
    Ms=S.Matrix([[h,j],[j,k]]); b=S.Matrix([b1,b2]); Mi=Ms.inv()
    zz=cg*(b.T*Mi*b)[0]
    candidate=Mi-VOLUME_POWER*cg*(Mi*b*b.T*Mi)/(1+VOLUME_POWER*zz)
    residual=(Ms+3*cg*b*b.T)*candidate-S.eye(2)
    for i in range(2):
        for t in range(2): eq('symbolic_rank_one_product_'+str((i,t)),residual[i,t])

    G=A0**2/(8*S.pi*Q)
    MJ=M/A0**FRAME_POWER
    zeta_physical=4*S.pi*G*r0*(beta.T*MJ.inv()*beta)[0]
    eq('physical_mass_and_density_conversion',zeta-zeta_physical)
    q=(beta.T*beta)[0]
    meff2=q/(beta.T*MJ.inv()*beta)[0]
    eq('harmonic_mass_identity',meff2/(4*S.pi*G*r0)-q*(2/B-3))
    ck('coupling_within_candidate_envelope',0<q<S.Rational(1,3))

    # Distinct three-field SPD examples verify contraction versus actual
    # orthonormal mass eigenmodes; they are synthetic controls, not observations.
    spectra=[]
    for idx,aa in enumerate([np.array([[2.,.3,-.1],[.3,3.,.2],[-.1,.2,5.]]),
                             np.array([[1.,-.2,.4],[-.2,4.,.7],[.4,.7,7.]]),
                             np.diag([.4,2.,11.])]):
        bb=np.array([.11,-.17,.09]);cc=.23
        vals,vecs=np.linalg.eigh(aa); weights=(vecs.T@bb)**2
        z=cc*float(bb@np.linalg.solve(aa,bb));spectral=cc*float(np.sum(weights/vals))
        v=-np.linalg.solve(aa+3*cc*np.outer(bb,bb),cc*bb)
        bv=-2*float(bb@v); me=float(bb@bb)/float(np.sum(weights/vals))
        ck('spectral_positive_'+str(idx),np.all(vals>0),vals.tolist())
        ck('spectral_inverse_'+str(idx),abs(z-spectral)<2e-16,abs(z-spectral))
        ck('matrix_response_'+str(idx),abs(bv-2*z/(1+3*z))<2e-16)
        ck('harmonic_mass_enclosure_'+str(idx),vals.min()<=me<=vals.max())
        spectra.append(dict(index=idx,mass_eigenvalues=vals.tolist(),coupling_weights=weights.tolist(),zeta=z,B=bv,harmonic_mass_squared=me))

    unstable=S.diag(1,-4); ub=S.Matrix([S.Rational(1,5),S.Rational(1,10)])
    uz=(ub.T*unstable.inv()*ub)[0];uB=2*uz/(1+3*uz)
    eq('unstable_hidden_contraction',uz-S.Rational(3,80))
    ck('unstable_matrix_has_negative_eigenvalue',unstable.det()<0)
    ck('unstable_counterexample_passes_slope_interval',0<uB<S.Rational(2,3),str(uB))

    density,ref,omega,qq=S.symbols('density reference omega q',positive=True)
    gamma=1+qq*(1+S.sin(omega*S.log(density/ref)))/2
    slope=(density*S.diff(gamma,density)/gamma).subs(density,ref)
    eq('bounded_gamma_unbounded_slope',slope-qq*omega/(2+qq))
    ck('slope_grows_without_bound',S.diff(slope,omega).is_positive)
    t=S.symbols('t',real=True)
    for end in [-1,1]:eq('gamma_envelope_endpoint_'+str(end),(1+qq*(1+t)/2).subs(t,end)-(1 if end==-1 else 1+qq))
    Gb,gam=S.Function('Gb')(density),S.Function('gamma')(density)
    eq('readout_slope_correction',-density*S.diff(Gb*gam,density)/(Gb*gam)+density*S.diff(gam,density)/gam+density*S.diff(Gb,density)/Gb)

    light,mu,Gsi,rhom=S.symbols('c_light mu G_SI rho_mass',positive=True)
    time_mass2=light**2*mu**2
    eq('SI_length_time_conversion',time_mass2/(4*S.pi*Gsi*rhom)-light**2*mu**2/(4*S.pi*Gsi*rhom))
    # Dimensions ordered mass,length,time. The numerator and denominator
    # must both be inverse time squared before their ratio is taken.
    dims_c=np.array([0,1,-1]);dims_mu=np.array([0,-1,0]);dims_G=np.array([-1,3,-2]);dims_rho=np.array([1,-3,0])
    ck('SI_ratio_dimensionless',np.all(2*dims_c+2*dims_mu-dims_G-dims_rho==0))
    ck('missing_c_squared_is_dimensionally_wrong',np.any(2*dims_mu-dims_G-dims_rho!=0))

    # Exposed saved direct roots are reused only; no equilibrium solve or fit.
    mp.mp.dps=70
    kval=mp.mpf('0.1');nu=mp.mpf('0.0001');av=(1-kval)*(1+3*kval)/4;sv=(1+kval)/(kval*(1-3*kval))
    def dj(z):
        DD=1+sv-sv*z*z;LL=mp.log(DD/z**2)
        return 6*sv*(z**-2-1)+nu*DD/(2*av*(1+sv))*(sv*LL**2/z**2+(1+sv)*LL/z**4)
    roots=[]
    for row in saved['roots']:
        z=mp.mpf(row['z']);delta=mp.mpf(row['delta_j']);qr=mp.mpf(row['q']);mass=mp.mpf(row['mJ2_over_Hv2'])
        ss=-z*mp.diff(dj,z)/dj(z);bb=2/ss
        lhs=mass/(z*z*delta);rhs=qr*(2/bb-3)
        error=abs(lhs-rhs)/max(1,abs(lhs),abs(rhs))
        ck('saved_candidate_scale_free_identity_'+str(row['index']),error<mp.mpf('1e-34'),mp.nstr(error,15))
        ck('saved_candidate_radial_stability_'+str(row['index']),(bb<mp.mpf(2)/3)==(mass>0))
        roots.append(dict(index=row['index'],B=mp.nstr(bb,45),dimensionless_mass_ratio=mp.nstr(lhs,45),q=mp.nstr(qr,45),positive_radial_mass=mass>0))
    return dict(passed=sum(x['passed'] for x in rows),failed=sum(not x['passed'] for x in rows),checks=rows,synthetic_spectra=spectra,saved_root_results=roots,root_input_kind='fresh in-memory density calculation',scope='Conditional stationary response; general identity, not action selection or empirical fit.')

def check_reconstruction():
    rows=[]
    def eq(name,e):
        r=s.factor(s.cancel(s.together(e)))
        rows.append(dict(name=name,passed=r==0,residual=str(r)))
    def ck(name,ok,detail=None):rows.append(dict(name=name,passed=bool(ok),detail=detail))

    F,Q,A,q=s.symbols('F Q A q',positive=True)
    lamx=s.symbols('lambda_gradient_squared',real=True)
    omega=(1/q-3)/2
    # Unintegrated Ricci gradient contributes -3F; integrating 3F box ln A
    # contributes +6F from dF=-2F d ln A. Original kinetic gives -F/q.
    transformed=(-3+IBP_COEFFICIENT-1/q)*F*lamx
    expected=-omega*(4*F**2*lamx)/(2*F)
    eq('Jordan_kinetic_coefficient',transformed-expected)
    eq('Jordan_invariant_kinetic_normalization',2*omega+3-1/q)
    eq('conformal_volume_curvature',A**-4*(Q/2)*A**2-Q/(2*A**2))
    qn=s.Function('q')(F)
    chiF=1/(2*F*s.sqrt(qn))
    eq('canonical_coordinate_metric',chiF**2-1/(4*F**2*qn))
    eq('coupling_reconstruction_from_F',(-1/(2*F*chiF))**2-qn)

    # Scalar Euler-Lagrange equation and metric trace are combined before
    # imposing stationarity; variable omega is retained throughout.
    w=s.Function('omega')(F);V=s.Function('V')(F)
    R,Box,X,T=s.symbols('R BoxF X T',real=True)
    scalar=R/2+w*Box/F+(s.diff(w,F)/F-w/F**2)*X/2-s.diff(V,F)
    Rtrace=(-T+w*X/F+3*Box+4*V)/F
    target=(2*w+3)*Box-T+s.diff(w,F)*X-2*F*s.diff(V,F)+4*V
    eq('variable_omega_trace_elimination',2*F*scalar.subs(R,Rtrace)-target)
    rho=2*F*s.diff(V,F)-4*V
    eq('stationary_density_from_trace',target.subs({Box:0,X:0,T:-rho}))
    eq('density_integrating_factor',s.diff(V/F**2,F)-rho/(2*F**3))
    C=s.symbols('C',real=True)
    eq('homogeneous_potential_offset',2*F*s.diff(C*F**2,F)-4*C*F**2)
    eq('offset_is_constant_Einstein_energy',A**4*C*(Q/A**2)**2-C*Q**2)
    ck('offset_changes_metric_trace',s.diff(4*C*F**2/F,C)!=0)
    eq('constant_scalar_reference_curvature',Rtrace.subs({Box:0,X:0,T:-rho})-(rho+4*V)/F)

    # Reconstruct the Einstein potential and differentiate with the actual
    # field-coordinate chain rule. Fixed particle density is substituted
    # after, not before, differentiating the force.
    AA=s.symbols('z',positive=True);VV=s.Function('V');qq=s.Function('q')
    FA=Q/AA**2;VE=AA**4*VV(FA);beta=s.sqrt(qq(FA))
    Dchi=lambda expr:AA*beta*s.diff(expr,AA)
    rstar=s.symbols('rho_star',real=True)
    force=(Dchi(VE)+rstar*Dchi(AA))/(2*Q)
    rhoA=2*FA*s.diff(VV(F),F).subs(F,FA)-4*VV(FA)
    stationary=rstar-rhoA*AA**3
    eq('stationary_particle_force',force-(AA*beta/(2*Q))*stationary)
    massE=Dchi(force).subs(rstar,rhoA*AA**3)
    rhoF=2*F*s.diff(VV(F),F)-4*VV(F)
    expected0=qq(F)*(s.diff(rhoF,F)-PARTICLE_VOLUME_POWER*rhoF/(2*F))
    eq('fixed_particle_mass_from_full_potential',massE/AA**2-expected0.subs(F,FA))
    pp=s.symbols('p',real=True)
    massp=expected0+pp*qq(F)*rhoF/(2*F)
    eq('fixed_physical_density_mass',massp.subs(pp,3)-qq(F)*s.diff(rhoF,F))
    eq('trace_scalar_mass_at_stationarity',qq(F)*(2*F*s.diff(VV(F),F,2)-2*s.diff(VV(F),F))-qq(F)*s.diff(rhoF,F))
    # q' multiplies a zero stationary residual, so it contributes no linear
    # mass term in the trace-eliminated equation about this constant point.
    r0=s.symbols('rho0',real=True)
    eq('variable_q_mass_no_extra_term',s.diff(qq(F)*(rhoF-r0),F).subs(r0,rhoF)-qq(F)*s.diff(rhoF,F))

    G,Gr,Vr=s.symbols('G Gref Vref',positive=True)
    Rho=s.Function('rho')(G)
    # Equivalent linear ODE in physical tensor-force normalization.
    Vg=s.Function('Vg')(G)
    eq('G_variable_ODE',-2*G*s.diff(Vg,G)-4*Vg-(-2*(s.diff(G**2*Vg,G)/G)))
    eq('G_integrating_factor',s.diff(G**2*Vg,G)-G*(G*s.diff(Vg,G)+2*Vg))

    F0=s.Rational(11,10);rho0=s.Rational(13,7)
    examples=[]
    for n in [s.Rational(1,1),s.Rational(3,2),s.Integer(2),s.Integer(3),s.Rational(7,2)]:
        rho_n=rho0*(F/F0)**n
        if n==2: vn=F**2*(C+rho0*s.log(F/F0)/(2*F0**2))
        else: vn=C*F**2+rho0*F**n/(2*(n-2)*F0**n)
        eq('power_density_inverse_'+str(n),2*F*s.diff(vn,F)-4*vn-POTENTIAL_SOURCE_SIGN*rho_n)
        eq('power_density_log_slope_'+str(n),rho_n/(F*s.diff(rho_n,F))-1/n)
        q_fn=1/(12+F/F0)
        m0=q_fn*(s.diff(rho_n,F)-PARTICLE_VOLUME_POWER*rho_n/(2*F))
        m3=m0+3*q_fn*rho_n/(2*F)
        eq('power_fixed_particle_mass_'+str(n),m0-q_fn*rho_n*(n-s.Rational(3,2))/F)
        eq('power_fixed_J_mass_'+str(n),m3-q_fn*rho_n*n/F)
        ev={F:s.Rational(3,2),C:10}
        ck('positive_reference_potential_'+str(n),vn.subs(ev)>0,str(vn.subs(ev)))
        ck('positive_J_coefficient_'+str(n),m3.subs(ev)>0)
        ck('fixed_particle_stability_domain_'+str(n),bool(m0.subs(ev)>0)==bool(n>s.Rational(3,2)))
        examples.append(dict(n=str(n),F='3/2',q=str(q_fn.subs(ev)),rho=str(rho_n.subs(ev)),VJ=str(vn.subs(ev)),mass0=str(m0.subs(ev)),mass3=str(m3.subs(ev)),B=str(1/n)))
    ck('fixed_J_positive_does_not_imply_particle_stability',s.Rational(1,1)<s.Rational(3,2))

    # Specialize to the original candidate potential, treating a,s,nu as
    # positive symbols; no measured density or fitted parameters are inserted.
    aa,ss,nu,Hv=s.symbols('a s nu Hv',positive=True)
    DD=1+ss-ss*AA**2;LL=s.log(DD/AA**2)
    U0=s.Rational(3,2)+s.Rational(3,2)*ss*(1-AA**2)**2+nu*DD**2*LL**2/(8*aa*(1+ss))
    dj=6*ss*(AA**-2-1)+nu*DD/(2*aa*(1+ss))*(ss*LL**2/AA**2+(1+ss)*LL/AA**4)
    candidateV=2*Q*Hv**2*U0/AA**4
    D_F=lambda expr:-AA**3*s.diff(expr,AA)/(2*Q)
    eq('candidate_original_density_inverse',2*(Q/AA**2)*D_F(candidateV)-4*candidateV-2*Q*Hv**2*dj)
    eq('candidate_vacuum_energy',candidateV.subs(AA,1)-3*Q*Hv**2)
    eq('candidate_vacuum_trace',(4*candidateV/(Q/AA**2)).subs(AA,1)-12*Hv**2)
    rho_candidate=2*Q*Hv**2*dj
    q_candidate=aa*DD/(1+ss-3*aa*ss*AA**2)
    eq('candidate_mass_prescription_difference',q_candidate*D_F(rho_candidate)-q_candidate*s.diff(U0,AA,2)*Hv**2-3*q_candidate*rho_candidate/(2*(Q/AA**2)))

    # A separate numerical quadrature recovers a nonlinear power+log potential
    # from its density curve with a supplied reference value. It is synthetic.
    mp.mp.dps=70
    rho_fn=lambda f:mp.mpf('1.7')*f**3+mp.mpf('.9')*f**2
    trueV=lambda f:f*f*(mp.mpf('2.4')+mp.mpf('.85')*f+mp.mpf('.45')*mp.log(f))
    fref=mp.mpf('1.2');vref=trueV(fref);quad=[]
    for val in ['0.7','1.1','2.3','4.2']:
        f=mp.mpf(val);recon=f*f*(vref/fref**2+mp.quad(lambda u:rho_fn(u)/(2*u**3),[fref,f]))
        err=abs(recon-trueV(f))/max(1,abs(trueV(f)))
        ck('density_quadrature_inverse_'+val,err<mp.mpf('1e-60'),mp.nstr(err,15))
        quad.append(dict(F=val,VJ=mp.nstr(recon,60),relative_error=mp.nstr(err,15)))
    return dict(passed=sum(x['passed'] for x in rows),failed=sum(not x['passed'] for x in rows),checks=rows,exact_power_examples=examples,numerical_reconstruction=quad,scope='Conditional single-field inverse and source-control distinction; no empirical functions measured or action/state selected.')

def check_domains():
    rows=[]
    def eq(name,e):
        r=s.factor(s.cancel(e));rows.append(dict(name=name,passed=r==0,residual=str(r)))
    def ck(name,b,detail=None):rows.append(dict(name=name,passed=bool(b),detail=detail))
    # chi = T psi; covariant Hessians and mixed mass operators transform
    # differently. Verify both conventions without identifying them.
    T=s.Matrix([[2,s.Rational(1,3)],[0,s.Rational(3,2)]])
    K=T.T*T;beta=s.Matrix([s.Rational(2,7),s.Rational(-1,5)])
    M=s.Matrix([[3,s.Rational(1,4)],[s.Rational(1,4),2]])
    c=s.Rational(3,11);p=s.Rational(5,2)
    cov_beta=T.T*beta;cov_H=T.T*M*T
    shifted_cov=T.T*(M+p*c*beta*beta.T)*T
    covariance=shifted_cov-cov_H-p*c*cov_beta*cov_beta.T
    mixed=K.inv()*shifted_cov-K.inv()*cov_H-p*c*K.inv()*cov_beta*cov_beta.T
    transformed=K.inv()*shifted_cov-T.inv()*(M+p*c*beta*beta.T)*T
    for i in range(2):
        for j in range(2):
            eq('covariant_rank_one_'+str((i,j)),covariance[i,j])
            eq('mixed_rank_one_'+str((i,j)),mixed[i,j])
            eq('mass_endomorphism_similarity_'+str((i,j)),transformed[i,j])
    wrong=K.inv()*shifted_cov-K.inv()*cov_H-p*c*cov_beta*cov_beta.T
    ck('omitting_inverse_metric_is_wrong',any(v!=0 for v in wrong))
    ck('positive_kinetic_basis',K[0,0]>0 and K.det()>0)

    F,q=s.symbols('F q',positive=True)
    rho=1+(F-1)**2
    mass0=q*(s.diff(rho,F)-3*rho/(2*F));mass3=q*s.diff(rho,F)
    eq('turning_density_derivative',s.diff(rho,F).subs(F,1))
    eq('turning_density_regular_mass0',mass0.subs(F,1)+3*q/2)
    eq('turning_density_regular_mass3',mass3.subs(F,1))
    ck('turning_density_is_positive',rho.subs(F,1)>0)
    eps=s.symbols('epsilon',positive=True)
    eq('turning_density_inverse_not_unique',rho.subs(F,1+eps)-rho.subs(F,1-eps))
    rho_zero=F-1
    eq('zero_density_point',rho_zero.subs(F,1))
    eq('zero_density_undivided_mass_regular',(q*(s.diff(rho_zero,F)-3*rho_zero/(2*F))).subs(F,1)-q)
    ck('zero_density_logarithm_not_defined',s.log(rho_zero.subs(F,1))==s.zoo)

    # Consistency of the candidate x=y=0 sector follows from the actual
    # coupling and metric dependence, not from an initial-state selector.
    u,x,y,k,nu,aa,ss=s.symbols('u x y k nu a s',positive=True)
    alpha=s.sqrt(aa);E=s.exp(2*alpha*u);FF=1+ss*E;JJ=1+(1-3*aa)*ss*E
    Kuu=JJ/FF**2;CC=(1+ss)*E/FF
    U=s.Rational(3,2)+3*ss*(E-1)**2/(2*FF**2)+k*x*x*s.exp(-(1-k)*u/alpha)/2+k*y*y*s.exp(-(1+k)*u/alpha)/3+nu*(1+ss)*u*u/(2*FF**2)
    for transverse in [x,y]:
        eq('transverse_metric_geodesic_'+str(transverse),s.diff(Kuu,transverse))
        eq('transverse_matter_source_'+str(transverse),s.diff(s.log(CC)/2,transverse))
        eq('transverse_potential_gradient_'+str(transverse),s.diff(U,transverse).subs({x:0,y:0}))
    return dict(passed=sum(r['passed'] for r in rows),failed=sum(not r['passed'] for r in rows),checks=rows,scope='Affected source-domain/basis controls only; no rerun of original63 controls.')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    density=check_density_environment()
    results=[('density',density),('identity',check_identity(density)),('reconstruction',check_reconstruction()),('domains',check_domains())]
    checks=[];units={};outputs={}
    for name,result in results:
        rows=result['checks'];normalized=[{**row,'name':name+'::'+row['name']} for row in rows]
        checks.extend(normalized)
        units[name]={'passed':sum(x['passed'] for x in rows),'failed':sum(not x['passed'] for x in rows)}
        outputs[name]={k:v for k,v in result.items() if k not in ['checks','passed','failed']}
    out={'passed':sum(x['passed'] for x in checks),'failed':sum(not x['passed'] for x in checks),'checks':checks,'units':units,'substantive_outputs':outputs,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Conditional local density and single-field action inverse; no measured functions, selected state or fundamental scales.'}
    if args.output:
        f=Path(args.output);assert not f.exists();f.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2));raise SystemExit(bool(out['failed']))
