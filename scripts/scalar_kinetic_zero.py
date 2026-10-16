"""Conditional scalar kinetic controls; computed action/record inputs only."""
AUDIT_TIMEOUT_SEC = 120
import sympy as s, json, time


def run_checks():
    start=time.monotonic()

    checks=[]

    def zero(n,e):
        e=s.factor(s.simplify(e));checks.append({'name':n,'pass':bool(e==0),'residual':str(e)})

    def truth(n,e):checks.append({'name':n,'pass':bool(e)})

    t=s.symbols('t',positive=True)

    A=t**s.Rational(5,2)

    aE=t**s.Rational(3,2)

    a=t**4

    H=s.Rational(3,2)/t

    rho=s.Rational(1,2)/t**2

    vb=s.Rational(5,2)/t

    Qy=s.Rational(2,5)

    D=s.Rational(4,5)

    Qz=4/t**2

    Qyz=s.Rational(4,25)

    Qzz=-s.Rational(14,5)/t**2

    Y=vb*vb/2

    P=t**-3+s.Rational(7,8)*t**-s.Rational(1,2)

    J=-2*t**-3+s.Rational(11,8)*t**-s.Rational(1,2)

    Um=2*t**-2-s.Rational(3,4)*t**s.Rational(1,2)

    db=3*P

    deltaY=vb*s.diff(J,t)-vb*vb*P

    zero('original_momentum',2*(s.diff(P,t)+H*P)-Qy*vb*J+rho*Um)

    zero('original_00',-6*H*(s.diff(P,t)+H*P)-D*deltaY-(2*Y*Qyz-Qz)*J-rho*(db+J))

    zero('original_pressure',2*(s.diff(P,t,2)+4*H*s.diff(P,t)+(2*s.diff(H,t)+3*H**2)*P)-Qy*deltaY-Qz*J)

    zero('original_Euler',s.diff(Um,t)+P+J+vb*Um)

    zero('original_number',s.diff(db,t)-3*s.diff(P,t))

    flux=aE**3*(D*s.diff(J,t)+Qyz*vb*J-(D+3*Qy)*vb*P)

    scalar=-s.diff(flux,t)/aE**3-2*P*s.diff(aE**3*Qy*vb,t)/aE**3+Qzz*J+Qyz*deltaY-rho*(db+J)

    zero('original_scalar',scalar)

    def dp(x):return s.factor(s.diff(x,t)/A)

    q=vb/A

    ell=H/A

    R=rho/A**2

    F=Qy

    E=Qz/A**2

    Xi=s.factor(q*dp(J)-q*q*P-(dp(q)+q*q)*J)

    Bd=s.factor(-6*ell*(dp(P)+ell*P)-F*(q*dp(J)-q*q*P)-(q*dp(F)-E+R)*J)

    V=s.factor(dp(Bd/R)-3*dp(P))

    Utrue=s.Rational(4,5)*t**7

    zero('transverse_excursion_formula',Xi-s.Rational(15,4)*(t**-10-t**-s.Rational(15,2)))

    zero('zero_at_reference',Xi.subs(t,1))

    zero('nonzero_crossing_slope',dp(Xi).subs(t,1)+s.Rational(75,8))

    zero('reference_V',V.subs(t,1)+s.Rational(15,2))

    zero('reference_U_recovered',V.subs(t,1)/dp(Xi).subs(t,1)-s.Rational(4,5))

    zero('history_equation',dp(Utrue*Xi)-V)

    integral=s.integrate(s.expand(A*V),t)

    fromzero=s.factor(integral-integral.subs(t,1))

    zero('regular_history_reconstruction',s.cancel(fromzero/Xi)-Utrue)

    zero('regular_limit_at_zero',s.limit(fromzero/Xi,t,1)-s.Rational(4,5))

    C=s.symbols('C',real=True)

    zero('away_from_zero_homogeneous_freedom',dp((Utrue+C/Xi)*Xi)-V)

    zero('pole_coefficient_nonzero',s.limit((t-1)*C/Xi,t,1)+s.Rational(8,75)*C)

    truth('nonzero_constant_forces_pole',s.limit((t-1)*C/Xi,t,1)!=0)

    Bn=s.Rational(5,4)

    X0=s.Rational(1,1000)

    Xmin=s.Rational(1,10)

    Cn=Bn*X0

    worst=Cn/Xmin

    zero('near_zero_uncertainty_enclosure',worst-s.Rational(1,80))

    return {'scope': 'One full-action linear history with a simple internal zero; no measured crossing or global action selection', 'passed': sum((c['pass'] for c in checks)), 'failed': sum((not c['pass'] for c in checks)), 'checks': checks, 'Xi': str(Xi), 'V': str(V), 'recovered_U': str(s.cancel(fromzero / Xi)), 'pole_coefficient': str(s.limit((t - 1) * C / Xi, t, 1))}
