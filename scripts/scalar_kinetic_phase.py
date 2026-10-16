"""Conditional scalar kinetic controls; computed action/record inputs only."""
AUDIT_TIMEOUT_SEC = 120
import json
import time
import sympy as s


def run_checks():
    started = time.monotonic()

    checks = []

    def zero(name, expr):
        expr = s.factor(s.simplify(expr))
        checks.append({'name': name, 'pass': bool(expr == 0), 'residual': str(expr)})

    def truth(name, expr):
        checks.append({'name': name, 'pass': bool(expr)})

    x, y, xp, yp, u, up = s.symbols('x y xp yp u up', real=True)

    Xi = x+s.I*y

    Xip = xp+s.I*yp

    V = Xi*up+Xip*u

    Wc = s.im(s.conjugate(Xi)*Xip)

    zero('real_determinant', Wc-(x*yp-y*xp))

    zero('real_U_numerator', s.im(s.conjugate(Xi)*V)-Wc*u)

    zero('real_Uprime_numerator', s.im(s.conjugate(V)*Xip)-Wc*up)

    rotation = s.Rational(3,5)+s.I*s.Rational(4,5)

    zero('constant_phase_determinant', s.im(s.conjugate(rotation*Xi)*rotation*Xip)-Wc)

    zero('constant_phase_U_numerator', s.im(s.conjugate(rotation*Xi)*rotation*V)-Wc*u)

    zero('fixed_phase_rank_zero', s.im(s.conjugate(rotation*x)*rotation*xp))

    omega = s.symbols('omega', real=True)

    zero('unregistered_phase_changes_rank',
         s.im(s.conjugate(Xi)*(Xip+s.I*omega*Xi))-Wc-omega*(x*x+y*y))

    t = s.symbols('t', positive=True)

    A = t**s.Rational(5,2)

    aE = t**s.Rational(3,2)

    a = A*aE

    H = s.Rational(3,2)/t

    v = s.Rational(5,2)/t

    rho = s.Rational(1,2)/t**2

    prime = lambda f: s.factor(s.diff(f,t)/A)

    q = v/A

    ell = H/A

    R = rho/A**2

    F = s.Rational(2,5)

    E = 4/t**7

    n = s.Rational(3,2)

    D = F*(2*n-1)

    Qyz = s.Rational(8,25)*(n-1)

    Qz = 4/t**2

    Qzz = s.Rational(4,5)*(n-5)/t**2

    P = t**-3+s.I*t**(-s.Rational(1,2))

    J = -2*t**-3+s.Rational(11,7)*s.I*t**(-s.Rational(1,2))

    Um = 2*t**-2-s.Rational(6,7)*s.I*t**s.Rational(1,2)

    db = 3*P

    # Two resolved spatial components are essential for the complex datum.
    sx, sy = s.symbols('sx sy', real=True)
    pattern = sx*sx-sy*sy+2*s.I*sx*sy
    zero('complex_spatial_pattern_harmonic', s.diff(pattern,sx,2)+s.diff(pattern,sy,2))
    zero('resolved_real_projection', s.re(P*pattern)-t**-3*(sx*sx-sy*sy)+2*t**(-s.Rational(1,2))*sx*sy)
    zero('real_pattern_discards_imaginary_response', s.re(P*s.re(pattern))-t**-3*(sx*sx-sy*sy))
    projection = s.Matrix([[1,0],[0,-2]])
    samples = s.Matrix([s.re(P*pattern).subs({sx:1,sy:0}), s.re(P*pattern).subs({sx:1,sy:1})])
    recovered_quadratures = projection.inv()*samples
    zero('resolved_spatial_samples_recover_real_response', recovered_quadratures[0]-s.re(P))
    zero('resolved_spatial_samples_recover_imaginary_response', recovered_quadratures[1]-s.im(P))

    Z = A*Um

    dy = v*s.diff(J,t)-v*v*P

    zero('full_action_momentum', 2*(s.diff(P,t)+H*P)-F*v*J+rho*Um)

    zero('full_action_Hamiltonian', -6*H*(s.diff(P,t)+H*P)-D*dy-(v*v*Qyz-Qz)*J-rho*(db+J))

    zero('full_action_pressure', 2*(s.diff(P,t,2)+4*H*s.diff(P,t)+(2*s.diff(H,t)+3*H*H)*P)-F*dy-Qz*J)

    zero('full_action_Euler', s.diff(Um,t)+P+J+v*Um)

    zero('full_action_bare_number', s.diff(db,t)-3*s.diff(P,t))

    flux = aE**3*(D*s.diff(J,t)+Qyz*v*J-(D+3*F)*v*P)

    scalar = -s.diff(flux,t)/aE**3-2*P*s.diff(aE**3*F*v,t)/aE**3+Qzz*J+Qyz*dy-rho*(db+J)

    zero('full_action_scalar', scalar)

    Xi = s.factor(q*prime(J)-q*q*P-(prime(q)+q*q)*J)

    Bd = s.factor(-6*ell*(prime(P)+ell*P)-F*(q*prime(J)-q*q*P)-(q*prime(F)-E+R)*J)

    V = s.factor(prime(Bd/R)-3*prime(P))

    Wc = s.factor(s.im(s.conjugate(Xi)*prime(Xi)))

    U = s.factor(s.im(s.conjugate(Xi)*V)/Wc)

    Up = s.factor(s.im(s.conjugate(V)*prime(Xi))/Wc)

    truth('full_action_real_rank', Wc != 0)

    zero('full_action_real_U', U-s.Rational(4,5)*t**7)

    zero('full_action_real_Uprime', Up-prime(U))

    zero('full_action_density_recovery', Bd/R-U*Xi-db)

    zero('full_action_sound_speed', F/(F+R*U)-s.Rational(1,2))

    truth('complex_Xi_no_zero', s.re(Xi).is_nonzero is True)

    z,Y = s.symbols('z Y', real=True)

    jets = []

    for nv in [s.Integer(1), s.Rational(3,2), s.Integer(2)]:
        Q = s.Rational(5,4)/nv*(s.Rational(8,25))**nv*s.exp(s.Rational(4,5)*(nv-1)*z)*Y**nv-(s.Rational(15,4)+s.Rational(5,4)/nv)*s.exp(-s.Rational(4,5)*z)
        def along(expr):
            return s.factor(s.simplify(expr.subs({z:s.Rational(5,2)*s.log(t),Y:s.Rational(25,8)/t**2})))
        Fb=along(s.diff(Q,Y))
        Eb=along(s.diff(Q,z))/A**2
        inferredB=R*(s.Rational(4,5)*(2*nv-2)*t**7)/(q*q)
        inferredL=prime(Fb)/q-inferredB*(prime(q)+q*q)
        inferredZZ=(prime(Eb)+2*q*Eb)/q-inferredL*(prime(q)+q*q)
        zero(f'n{nv}_YY', inferredB-A**2*along(s.diff(Q,Y,2)))
        zero(f'n{nv}_zY', inferredL-along(s.diff(Q,z,Y)))
        zero(f'n{nv}_zz', inferredZZ-along(s.diff(Q,z,2))/A**2)
        jets.append({'n':str(nv),'normalized_QYY':str(inferredB),'normalized_QzY':str(inferredL),'normalized_Qzz':str(inferredZZ)})

    ycurve=s.Function('y')(z)

    lam=s.Function('lam')(z)

    deformation=lam*(Y-ycurve)**3

    for iz,iy in [(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)]:
        zero(f'cubic_invisible_jet_{iz}_{iy}',s.diff(deformation,z,iz,Y,iy).subs(Y,ycurve))

    zero('cubic_third_derivative_visible',s.diff(deformation,Y,3).subs(Y,ycurve)-6*lam)

    return {'scope': 'Conditional real-quadrature inverse, original-action constructed local harmonic modes, and sampled jets; no empirical validation', 'passed': sum((c['pass'] for c in checks)), 'failed': sum((not c['pass'] for c in checks)), 'checks': checks, 'phase_fixture_Xi': str(Xi), 'phase_fixture_determinant': str(Wc), 'phase_fixture_U': str(U), 'sampled_jets': jets}
