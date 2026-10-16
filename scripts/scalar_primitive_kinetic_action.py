"""Conditional scalar kinetic controls; computed action/record inputs only."""
AUDIT_TIMEOUT_SEC = 120
import json
import time
import sympy as s


def run_checks():
    start = time.monotonic()

    checks = []

    def zero(name, expr):
        expr = s.factor(s.simplify(expr))
        checks.append({"name": name, "pass": bool(expr == 0), "residual": str(expr)})

    def truth(name, expr):
        checks.append({"name": name, "pass": bool(expr)})

    t = s.symbols("t", positive=True)

    n = s.symbols("n", positive=True)

    z, Y = s.symbols("z Y", real=True, positive=True)

    r = s.Rational(5, 2)

    p = s.Rational(3, 2)

    K0 = s.Rational(5, 4)/n/(r*r/2)**n

    V0 = s.Rational(15, 4)+s.Rational(5, 4)/n

    c = (2*n-2)/r

    Q = K0*s.exp(c*z)*Y**n - V0*s.exp(-2*z/r)

    zb = r*s.log(t)

    vb = r/t

    Yb = vb*vb/2

    aE = t**p

    Ab = t**r

    rho = s.Rational(1, 2)/t**2

    H = p/t

    def along(expr):
        return s.factor(s.simplify(s.powdenest(expr.subs({z: zb, Y: Yb}), force=True)))

    qb = along(Q)

    Qy = along(s.diff(Q, Y))

    Qyy = along(s.diff(Q, Y, 2))

    Qz = along(s.diff(Q, z))

    Qyz = along(s.diff(Q, Y, z))

    Qzz = along(s.diff(Q, z, 2))

    D = s.factor(Qy+2*Yb*Qyy)

    zero("history_QY", Qy-s.Rational(2, 5))

    zero("history_D", D-s.Rational(2, 5)*(2*n-1))

    zero("history_Qz", Qz-4/t**2)

    zero("history_Qzz", Qzz-s.Rational(4, 5)*(n-5)/t**2)

    zero("background_Friedmann", 3*H**2-(2*Yb*Qy-qb+rho))

    zero("background_Raychaudhuri", -2*s.diff(H,t)-(2*Yb*Qy+rho))

    zero("background_dust", s.diff(rho,t)+3*H*rho-vb*rho)

    zero("background_scalar", D*s.diff(vb,t)+3*H*Qy*vb+2*Yb*Qyz-Qz+rho)

    zero("principal_speed", Qy/D-1/(2*n-1))

    truth("positive_domain_n_gt_half", D.subs(n,s.Rational(1,2)+s.Symbol("x",positive=True)).is_positive)

    truth("noncanonical_n2_not_luminal", (Qy/D).subs(n,2)==s.Rational(1,3))

    def prime(expr):
        return s.simplify(s.diff(expr,t)/Ab)

    aph = Ab*aE

    h = prime(aph)/aph

    q = prime(zb)

    ell = h-q

    G = s.simplify(Qy*q)

    R = s.simplify(rho/Ab**2)

    Pi = s.simplify(qb/Ab**2)

    zero("physical_Friedmann_action_value", Pi-(q*G+R-3*ell**2))

    zero("physical_Raychaudhuri", -2*(prime(ell)+q*ell)-q*G-R)

    zero("physical_dust", prime(R)-(2*q-3*h)*R)

    zero("action_zeta_derivative", (prime(Pi)+2*q*Pi-G*(prime(q)+q*q))/q-Qz/Ab**2)

    zero("background_coefficient_n_independent_G", s.diff(G,n))

    zero("background_coefficient_n_independent_R", s.diff(R,n))

    zero("background_coefficient_n_independent_Pi", s.diff(Pi,n))

    P,J,U,db = s.symbols("P J U db")

    k2 = s.symbols("k2", nonnegative=True)

    fp = s.factor((Qy*vb*J-rho*U)/2-H*P)

    fj = s.factor((-2*k2*P/aE**2-6*H*(fp+H*P)
                    +D*vb*vb*P-(2*Yb*Qyz-Qz+rho)*J-rho*db)/(D*vb))

    fu = -P-J-vb*U

    fb = 3*fp+k2*U/aE**2

    fields = (P,J,U,db)

    flow = (fp,fj,fu,fb)

    def total(expr):
        return s.factor(s.diff(expr,t)+sum(s.diff(expr,w)*f for w,f in zip(fields,flow)))

    dy = vb*fj-vb*vb*P

    pressure = 2*(total(fp)+4*H*fp+(2*s.diff(H,t)+3*H**2)*P)-Qy*dy-Qz*J

    flux = aE**3*(D*fj+Qyz*vb*J-(D+3*Qy)*vb*P)

    scalar = (-total(flux)/aE**3
              -2*P*s.diff(aE**3*Qy*vb,t)/aE**3-Qy*k2*J/aE**2
              +Qzz*J+Qyz*dy-rho*(db+J))

    zero("full_linear_pressure_from_constraints",pressure)

    zero("full_linear_scalar_from_constraints",scalar)

    zero("original_linear_momentum",2*(fp+H*P)-Qy*vb*J+rho*U)

    zero("original_linear_Hamiltonian",-2*k2*P/aE**2-6*H*(fp+H*P)-D*dy-(2*Yb*Qyz-Qz)*J-rho*(db+J))

    zero("original_linear_bare_dust",fb-3*fp-k2*U/aE**2)

    zero("original_linear_Euler",fu+P+J+vb*U)

    Z=Ab*U

    Zp=s.simplify(total(Z)/Ab)

    Pp=fp/Ab

    zero("physical_momentum",Pp+ell*P-(G*J-R*Z)/2)

    zero("physical_Euler",Zp+P+J)

    C=R/G

    d=2/G

    e=1+d*ell

    zero("photon_reduced_necessary_equation",Zp+C*Z+d*Pp+e*P)

    zero("recovered_q",h-(e-1)/d-q)

    zero("recovered_QY",G/q-Qy)

    zero("canonical_member_coordinates",q*G-s.Rational(5,2)*t**-7)

    init={t:1,P:1,J:0,U:0,db:0,k2:3}

    noncan_difference=s.factor(fj.subs(n,2).subs(init)-fj.subs(n,1).subs(init))

    truth("noncanonical_initial_response_distinct",noncan_difference!=0)

    truth("noncanonical_full_scalar_gradient_changed",s.factor(s.diff(fj,k2).subs(n,2)-s.diff(fj,k2).subs(n,1))!=0)

    truth("wrong_dust_source_sign_detected",s.factor(pressure+2*rho*J)!=0)

    truth("wrong_canonical_D_detected",s.factor((D-Qy).subs(n,2))!=0)

    m,jj,uu,bb = s.symbols("m jj uu bb")

    coef=s.Matrix([
        2*(m+s.Rational(3,2))-jj+uu/2,
        (m+s.Rational(7,2))*uu+jj+1,
        m*(bb-3),
        (2*n-1)*m*jj-(5*n-16-9*m-(2*n-s.Rational(11,2))*jj-bb/2)
    ])

    jm=s.factor((2*m*m+10*m+10)/(m+4))

    um=s.factor(2*(jm-2*m-3))

    poly=s.factor(coef[3].subs({jj:jm,uu:um,bb:3})*(m+4))

    mode_rows=[]

    for nv in [s.Integer(1),s.Integer(2),s.Rational(3,2)]:
        roots=s.solve(poly.subs(n,nv),m)
        rows=[(s.Integer(0),s.Rational(5,2),s.Integer(-1),-s.Rational(9,2))]
        rows += [(root,s.simplify(jm.subs(m,root)),s.simplify(um.subs(m,root)),s.Integer(3)) for root in roots if root!=0]
        for mode,(sv,jv,uv,bv) in enumerate(rows):
            repl={P:t**sv,J:jv*t**sv,U:uv*t**(sv+1),db:bv*t**sv,k2:0,n:nv}
            for field,flowval,target in zip(fields,flow,[t**sv,jv*t**sv,uv*t**(sv+1),bv*t**sv]):
                zero(f"mode_n{nv}_{mode}_{field}",flowval.subs(repl)-s.diff(target,t))
            mode_rows.append({"n":str(nv),"exponent":str(sv),"J_over_P":str(jv),"U_over_tP":str(uv),"db_over_P":str(bv)})

    return {'scope': 'General-kinetic necessary inverse and constructed full-action controls; no empirical validation', 'passed': sum((c['pass'] for c in checks)), 'failed': sum((not c['pass'] for c in checks)), 'checks': checks, 'Q_history': str(qb), 'QY': str(Qy), 'D': str(D), 'physical_G': str(G), 'physical_R': str(R), 'harmonic_nonzero_mode_polynomial': str(poly), 'modes': mode_rows, 'noncanonical_initial_Jdot_difference': str(noncan_difference)}
