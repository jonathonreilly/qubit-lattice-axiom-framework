"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib

    import json

    import pathlib

    import sympy as s

    u,r,eta,mu,c,z=s.symbols('u r eta mu c z',real=True)

    a=s.exp(2*(u-r))

    Hc=s.Integer(2)

    L=lambda f:s.diff(f,u)+Hc*f

    D=lambda f:s.diff(f,r)+s.diff(f,u)

    T=lambda f:s.diff(f,r)+2*s.diff(f,u)+Hc*f

    checks=[]

    def check(name,expr,expect_zero=True):
        result=s.factor(s.simplify(expr))
        checks.append({'name':name,'pass':(result==0)==expect_zero,'residual':str(result),
                       'expected_zero':expect_zero})

    Q=(3*mu*mu-1)/2

    V=s.exp(-2*(u-r))*(1+u**3+r*u+r*r)*Q

    Psi=-L(V)

    vr=D(V)

    Rz=-Psi+vr

    check('velocity_potential_residual_transport',T(V)-Rz)

    check('radial_euler',L(vr)+D(Psi))

    check('force_transport',T(Psi)+L(Rz))

    check('omitting_radial_transport_detected',2*s.diff(Psi,u)+Hc*Psi+L(Rz),False)

    check('integrating_factor_characteristic',
          s.diff((a*V).subs(u,c+2*r),r)-(a*Rz).subs(u,c+2*r))

    h=s.Function('Hc')(u-r)

    W=s.Function('W')(u,r)

    Lg=lambda f:s.diff(f,u)+h*f

    Dg=lambda f:s.diff(f,r)+s.diff(f,u)

    check('commutator_zero_for_homogeneous_background',Lg(Dg(W))-Dg(Lg(W)))

    F=(u-2*r)**3*Q

    dV=F/a

    dPsi=-L(dV)

    dvr=D(dV)

    check('homogeneous_transport_family',T(dV))

    check('same_corrected_redshift',-dPsi+dvr)

    check('nonzero_lapse_change',dPsi,False)

    check('homogeneous_force_transport',T(dPsi))

    check('homogeneous_expected_lapse',dPsi+3*(u-2*r)**2*Q/a)

    Ve=dV.subs(u,eta+r)

    Psie=dPsi.subs(u,eta+r)

    vre=s.diff(Ve,r)

    vtheta=-s.sqrt(1-mu*mu)*s.diff(Ve,mu)/r

    gradthetaPsi=-s.sqrt(1-mu*mu)*s.diff(Psie,mu)/r

    check('homogeneous_full_radial_euler',s.diff(vre,eta)+2*vre+s.diff(Psie,r))

    check('homogeneous_full_angular_euler',s.diff(vtheta,eta)+2*vtheta+gradthetaPsi)

    check('homogeneous_same_lensing_sum',dPsi-dPsi)

    B=1+c*c

    integral=s.integrate((c+2*z)**2+z,(z,0,r))

    forced=((B+integral)*s.exp(-2*(c+r))).subs(c,u-2*r)

    forcing=(u*u+r)/a

    check('forced_transport_solution',T(forced)-forcing)

    check('forced_boundary_supplied',forced.subs(r,0)-(1+u*u)*s.exp(-2*u))

    eps=s.symbols('eps',real=True)

    P=s.Function('P')(u-r,r)

    nullratio=s.series(s.sqrt((1-2*eps*P)/(1+2*eps*P)),eps,0,2).removeO()

    check('radial_null_time_sign',-nullratio-(-1+2*eps*P))

    hs,shift,epsilon=s.symbols('Hc_s delta_eta_s epsilon',real=True)

    relative=s.series((1-eps*hs*shift)*(1+eps*epsilon),eps,0,2).removeO()

    check('background_redshift_registration',relative-(1+eps*(epsilon-hs*shift)))

    check('corrected_residual_shapiro_term',(epsilon-hs*shift)+hs*shift-epsilon)

    obs=(s.Rational(0),s.Rational(1))

    point_u=s.Rational(3,4)

    point_r=s.Integer(3)

    boundary=point_u-2*point_r

    checks.append({'name':'remote_characteristic_boundary_outside_observing_strip',
                   'pass':not(obs[0]<=boundary<=obs[1]),'boundary_u':str(boundary)})

    return checks, {}
