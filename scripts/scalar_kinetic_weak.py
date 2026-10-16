"""Conditional scalar kinetic controls; computed action/record inputs only."""
AUDIT_TIMEOUT_SEC = 120
import sympy as s
import json, time


def run_checks():
    start=time.monotonic()

    checks=[]

    def zero(n,e):
        e=s.factor(s.simplify(e));checks.append({'name':n,'pass':bool(e==0),'residual':str(e)})

    def truth(n,e):checks.append({'name':n,'pass':bool(e)})

    t=s.symbols('t',positive=True)

    x=s.symbols('x',nonnegative=True)

    A=t**s.Rational(5,2)

    a=t**4

    def dp(f):return s.factor(s.diff(f,t)/A)

    q=s.Rational(5,2)*t**-s.Rational(7,2)

    ell=s.Rational(3,2)*t**-s.Rational(7,2)

    R=s.Rational(1,2)*t**-7

    F=s.Rational(2,5)

    E=4*t**-7

    P=t**-3

    J=-2*t**-3

    Z=2*t**s.Rational(1,2)

    db=3*t**-3

    Utrue=s.Rational(4,5)*t**7

    lam=(t-1)**3*(2-t)**3

    Xi=q*dp(J)-q*q*P-(dp(q)+q*q)*J

    Bd=-6*ell*(dp(P)+ell*P)-F*(q*dp(J)-q*q*P)-(q*dp(F)-E+R)*J

    zero('actual_density_rewrite',Bd-R*Utrue*Xi-R*db)

    zero('actual_bare_density_evolution',dp(db)-3*dp(P))

    zero('time_transform',dp(t**s.Rational(7,2)/s.Rational(7,2))-1)

    for endpoint in [1,2]:
        zero(f'test_endpoint_value_{endpoint}',lam.subs(t,endpoint))
        zero(f'test_endpoint_trace_{endpoint}',dp(lam).subs(t,endpoint))

    def weights(U,k2=0):
        alpha=-6*ell/R
        beta=-q*(F/R+U)
        gamma=2/(R*a*a)
        delta=(-6*ell*ell+F*q*q)/R-3+U*q*q
        eps=-(q*dp(F)-E+R)/R+U*(dp(q)+q*q)
        return [s.factor(-dp(alpha*dp(lam))+(delta-k2*gamma)*dp(lam)),
                s.factor(-dp(beta*dp(lam))+eps*dp(lam)),
                s.factor(k2*lam/a**2)]

    moments={}

    # Nonzero spatial eigenvalue checks the adjoint beyond the harmonic fixture.
    # These arbitrary probe functions test an operator identity, not a solution.
    pk, jk, zk, k2 = t**2, t**3, t**4, s.Rational(7,3)
    xik = q*dp(jk)-q*q*pk-(dp(q)+q*q)*jk
    bdk = -2*k2*pk/a**2-6*ell*(dp(pk)+ell*pk)-F*(q*dp(jk)-q*q*pk)-(q*dp(F)-E+R)*jk
    hk = bdk/R-3*pk-Utrue*xik
    wk = weights(Utrue,k2)
    alphak = -6*ell/R
    betak = -q*(F/R+Utrue)
    boundaryk = dp(lam*hk-dp(lam)*(alphak*pk+betak*jk))
    zero('nonzero_spatial_mode_adjoint',wk[0]*pk+wk[1]*jk+wk[2]*zk+lam*(dp(hk)-k2*zk/a**2)-boundaryk)

    for label,U in [('true',Utrue),('wrong',s.Integer(0))]:
        w=weights(U)
        primitive=s.factor(A*(w[0]*P+w[1]*J+w[2]*Z))
        prior=s.factor(A*dp(lam)*(Bd/R-3*P-U*Xi))
        mp=s.integrate(primitive,(t,1,2));mi=s.integrate(prior,(t,1,2))
        zero(label+'_primitive_equals_once_weak',mp-mi)
        # Difference is a total derivative; this checks local integration by parts.
        alpha=-6*ell/R;beta=-q*(F/R+U)
        boundary=s.factor(s.diff(dp(lam)*(alpha*P+beta*J),t))
        zero(label+'_local_adjoint_identity',prior-primitive-boundary)
        moments[label]=s.simplify(mp)

    zero('true_candidate_passes',moments['true'])

    wp,wj,wz=[s.factor(A*w) for w in weights(0)]

    zero('fixed_wrong_Pweight',wp-(18*t*s.diff(lam,t,2)-7*s.diff(lam,t)))

    zero('fixed_wrong_Jweight',wj-(2*t*s.diff(lam,t,2)+9*s.diff(lam,t)))

    zero('fixed_wrong_Zweight',wz)

    positiveform=9*s.integrate(lam*t**-4,(t,1,2))

    zero('wrong_closed_log_form', moments['wrong']-(567*s.log(2)-393))

    zero('wrong_positive_integral',moments['wrong']-positiveform)

    truth('wrong_nominal_positive',moments['wrong'].evalf(80)>0)

    def monomial_L1_bound(poly):
        co=s.Poly(s.expand(poly.subs(t,x+1)),x)
        return sum(abs(c)/s.Rational(i[0]+1) for i,c in co.terms())

    K=monomial_L1_bound(wp)+monomial_L1_bound(wj)

    # Separate bounded-polynomial perturbation, without differentiating errors.
    uniform_error = s.Rational(1,10**6)
    moment_shift = s.integrate(wp*uniform_error*(2*t-3)+wj*uniform_error*(t-1)**2,(t,1,2))
    truth('bounded_polynomial_error_budget',abs(moment_shift)<=K*uniform_error)

    radius=s.simplify(moments['wrong']/(2*K))

    # Exact log enclosure: log(2)=2 sum_j (1/3)^(2j+1)/(2j+1).
    # The remaining positive terms are bounded by a geometric tail.
    truncation = 12
    log2_lower = 2*sum(s.Rational(1,3)**(2*j+1)/s.Integer(2*j+1) for j in range(truncation))
    log2_upper = log2_lower+2*s.Rational(1,3)**(2*truncation+1)/(s.Integer(2*truncation+1)*(1-s.Rational(1,9)))
    truth('rational_wrong_moment_positive',567*log2_lower-393>0)
    truth('rational_log_enclosure_width',log2_upper-log2_lower<s.Rational(1,10**12))
    truth('rational_fixed_error_rejection',567*log2_lower-393>2*K/s.Integer(10**6))
    truth('positive_error_radius',radius.evalf(80)>0)

    truth('bound_nonzero',K>0)

    eta=radius/4

    truth('strict_uniform_rejection',moments['wrong']-eta*K>eta*K)

    zero('factor_two_radius_definition',2*K*radius-moments['wrong'])

    truth('wrong_sign_mutation_detected',s.integrate(A*dp(lam)*(Bd/R-3*P+Utrue*Xi),(t,1,2)).evalf()!=0)

    return {'scope': 'Fixed original-action constructed metric histories, no measured-data validation', 'passed': sum((c['pass'] for c in checks)), 'failed': sum((not c['pass'] for c in checks)), 'checks': checks, 'true_moment': str(moments['true']), 'wrong_moment': str(moments['wrong']), 'wrong_moment_numeric': str(moments['wrong'].evalf(25)), 'rational_error_coefficient_bound': str(K), 'uniform_rejection_radius': str(radius), 'uniform_rejection_radius_numeric': str(radius.evalf(25)), 'amplitude_scaling': 'Every perturbation and allowable input error scales by the same small common amplitude. Background errors are separate.'}
