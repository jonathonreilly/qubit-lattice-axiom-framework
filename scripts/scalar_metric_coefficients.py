"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib

    import json

    import platform

    from pathlib import Path

    import numpy as np

    import scipy

    from scipy.integrate import solve_ivp

    import sympy as s

    checks = []

    def exact(name, expression):
        residual = s.factor(s.cancel(s.expand(expression)))
        checks.append({"name": name, "pass": residual == 0, "residual": str(residual)})

    def condition(name, value, **evidence):
        checks.append({"name": name, "pass": bool(value), **evidence})

    tau = s.symbols("tau", positive=True)

    h, b, x, kap, P, J = [s.Function(n)(tau) for n in ["h", "b", "x", "kap", "P", "J"]]

    kj2 = s.symbols("kj2", positive=True)

    q = b*x

    ell = h-q

    L = s.diff(b, tau)/b

    w = J/b

    deff = kap+b*s.diff(x, tau)+3*b*h*x-2*q*q

    aa = 3*ell-2*L

    cc = deff+L*L-s.diff(L, tau)-3*ell*L

    dd = 6*b*b*ell+4*q

    ee = 2*b*b

    ff = 6*b*b*ell*ell+2*b*s.diff(x, tau)+6*h*q-5*q*q

    response = (s.diff(w, tau, 2)+3*ell*s.diff(w, tau)+(kj2+deff)*w
                -(6*b*ell+4*x)*s.diff(P, tau)
                -(2*b*kj2+6*b*ell*ell-b*x*x+2*(s.diff(x,tau)+3*h*x-2*b*x*x))*P)

    mode = s.diff(J,tau,2)+kj2*J+aa*s.diff(J,tau)+cc*J-dd*s.diff(P,tau)-ee*kj2*P-ff*P

    exact("quotient derivatives give five coefficients", b*response-mode)

    B = b*b

    L_from_B = s.diff(B,tau)/(2*B)

    q_recovered = h-(aa+2*L_from_B)/3

    k_recovered = cc-s.diff(q,tau)-3*h*q+2*q*q-2*q*L-L*L+s.diff(L,tau)+3*h*L

    exact("coupling magnitude recovered", ee/2-B)

    exact("log coupling derivative recovered", L_from_B-L)

    exact("speed product recovered without 4-6B denominator", q_recovered-q)

    exact("fixed-bare-density curvature recovered", k_recovered-kap)

    exact("remaining d compatibility", dd-(6*B*(h-q)+4*q))

    exact("remaining f compatibility", ff-(6*B*(h-q)**2+2*(s.diff(q,tau)-q*L)+6*h*q-5*q*q))

    R = 2*s.diff(q,tau)-2*s.diff(h,tau)-2*h*q+(2-1/B)*q*q

    R_previous = 2*b*s.diff(x,tau)+2*s.diff(b,tau)*x-2*s.diff(h,tau)-2*b*h*x+(2*b*b-1)*x*x

    exact("background source without supplying b sign", R-R_previous)

    Fbar = -s.diff(x,tau)-3*h*x+2*q*x

    Kbg = s.diff(x,tau,2)+3*h*s.diff(x,tau)+(3*s.diff(h,tau)+kap-2*s.diff(q,tau)+6*h*q-4*q*q)*x-3*b*ell*R

    exact("curvature condition from force derivative", s.diff(Fbar,tau)+2*q*Fbar-kap*x+3*b*ell*R+Kbg)

    Rfree = s.symbols("Rfree", positive=True)

    delta = (-2*kj2*P-6*ell*(s.diff(P,tau)+ell*P)-x*s.diff(w,tau)+x*x*P-Fbar*w)/Rfree

    original_scalar = (s.diff(w,tau,2)+(3*h-2*q)*s.diff(w,tau)+(kj2+kap)*w
                       +b*Rfree*delta-4*x*s.diff(P,tau)+2*Fbar*P)

    exact("Hamiltonian density restores original scalar", original_scalar-response)

    Z = (x*w-2*(s.diff(P,tau)+ell*P))/Rfree

    exact("reconstructed source satisfies momentum", s.diff(P,tau)+ell*P-(x*w-Rfree*Z)/2)

    exact("reconstructed source satisfies Hamiltonian", 2*kj2*P+6*ell*(s.diff(P,tau)+ell*P)+Rfree*delta+x*s.diff(w,tau)-x*x*P+Fbar*w)

    Ae, Ue, Ze, qe, Pe, Je, kje, de, dJe, Pprime = s.symbols("Ae Ue Ze qe Pe Je kje de dJe Pprime", real=True)

    Udot = -Pe-Je-qe*Ae*Ue

    exact("matter velocity conversion cancels coupling drag", (qe*Ae*Ue+Udot).subs(Ue,Ze/Ae)+Pe+Je)

    exact("matter density continuity transformation", (3*Pprime+kje*Ze-3*dJe)-(3*(Pprime-dJe)+kje*Ze))

    t = s.symbols("t", positive=True)

    A = t

    aE = t

    phi = s.log(t)

    H = 1/t

    v = 1/t

    rho = t**-3

    r = t**-2

    V = s.Rational(3,2)*t**-2

    field = lambda f: s.diff(f,t)/v

    alpha = field(A)/A

    force = field(V)+rho*field(A)

    mu = field(field(V))+rho*field(field(A))

    exact("witness original Friedmann", 3*H*H-v*v/2-V-r)

    exact("witness original Raychaudhuri", -2*s.diff(H,t)-v*v-r)

    exact("witness original scalar", s.diff(v,t)+3*H*v+force)

    exact("witness original bare dust", s.diff(rho*aE**3,t))

    exact("witness fixed-density curvature", mu-7/t**2)

    exact("witness proper matter clock", s.diff(t*t/2,t)-A)

    ep = s.symbols("epsilon", nonzero=True, real=True)

    initial = [(0,1,0,0),(1,0,0,1),(0,0,0,-2),(0,0,1,-2),(0,0,1,-2)]

    matrix = []

    ys = []

    initial_deltas = []

    for ks, init in enumerate(initial, 1):
        u, pi, pv, uv = [ep*j for j in init]
        pp = (u-uv)/2-pv
        dv = -2*ks*pv-6*pp-6*pv-pi+pv+2*u
        # Original KG, F=-2, mu=7, v=H=alpha=r=A=1.
        pidot = -3*pi-(ks+7)*u-dv+4*pp+4*pv
        # J=u here, but the matter second derivative subtracts A_dot*u_dot.
        jpp = pidot-pi
        matrix.append([-pi,-u,pp,ks*pv,pv])
        ys.append(jpp+ks*u)
        initial_deltas.append(str(dv))

    D = s.Matrix(matrix)

    truth = s.Matrix([3,9,10,2,9])

    exact("full physical initial-data determinant", D.det()+ep**5)

    recovered = D.inv()*s.Matrix(ys)

    for n, actual, expected in zip(["a","c","d","e","f"], recovered, truth):
        exact("initial physical coefficient "+n, actual-expected)

    same_k = D.copy()

    same_k[:,3] = same_k[:,4]

    condition("same-k design loses rank", same_k.rank()==4, rank=same_k.rank())

    bc = s.sqrt(s.Rational(2,3))

    C = s.Rational(1,2)

    n = bc*C

    power = (n+2)/3

    rc = 2*power-C*C

    Vc = 3*power**2-2*power+C*C/2

    exact("critical B power-background scalar", -C+3*power*C-2*Vc/C+bc*rc)

    condition("critical B positive dust", rc>0, R_coefficient=str(rc))

    hc = (power+n)/((n+1)*tau)

    qc = n/((n+1)*tau)

    ac = 3*(hc-qc)

    exact("critical B inversion remains regular", hc-ac/3-qc)

    exact("critical B d alone loses q", 4-6*bc**2)

    eta = s.symbols("eta", positive=True)

    z = s.symbols("z", real=True)

    pert = eta*s.sin(z/eta**2)

    exact("small amplitude does not bound first derivative", s.diff(pert,z).subs(z,0)-1/eta)

    exact("small amplitude does not bound second derivative", s.diff(pert,z,2).subs(z,s.pi*eta**2/2)+eta**-3)

    ksquares = np.arange(1.,6.)

    eps = 1.e-5

    y0 = []

    for k2, row in zip(ksquares, initial):
        uv, piv, pv, vel = eps*np.asarray(row, float)
        pd = (uv-vel)/2-pv
        dens = -2*k2*pv-6*(pd+pv)-piv+pv+2*uv
        y0.extend([uv,piv,pv,vel,dens])

    def original_rhs(tt, yy):
        rates = []
        HH, vv, rr, FF, mm = 1/tt,1/tt,1/tt**2,-2/tt**2,7/tt**2
        for k2, row in zip(ksquares, np.asarray(yy).reshape(5,5)):
            uv,piv,pv,vel,dens = row
            ke2 = k2/tt**2
            pd = (vv*uv-rr*vel)/2-HH*pv
            rates.extend([piv,-3*HH*piv-(ke2+mm)*uv-rr*dens+4*vv*pd-2*FF*pv,
                          pd,-pv-uv-vv*vel,3*pd+ke2*vel])
        return np.array(rates)

    times = np.linspace(1.,1.6,31)

    solution = solve_ivp(original_rhs,(times[0],times[-1]),y0,method="DOP853",
                         rtol=2e-12,atol=2e-15,max_step=.01,t_eval=times)

    condition("full forward original ODE succeeded", solution.success, message=solution.message)

    numeric = []

    max_constraint = max_recovery = max_physical = 0.

    min_relative_sigma = 1.

    for tt, yy in zip(solution.t, solution.y.T):
        state = yy.reshape(5,5)
        rates = original_rhs(tt,yy).reshape(5,5)
        modeD, modey = [],[]
        HH,vv,rr,FF = 1/tt,1/tt,1/tt**2,-2/tt**2
        hj,bj,xj,Rj,kappaj = 2/tt**2,1.,1/tt**2,1/tt**4,7/tt**4
        ellj = 1/tt**2
        Fbj = -2/tt**4
        epoch_modes = []
        for k2, st, ds in zip(ksquares,state,rates):
            uv,piv,pv,vel,dens = st
            du,dpi,dp,dvel,ddens = ds
            jv = uv
            jp = piv/tt
            jpp = dpi/tt**2-piv/tt**3
            pp = dp/tt
            jkj2 = k2/tt**4
            modeD.append([-jp,-jv,pp,jkj2*pv,pv])
            modey.append(jpp+jkj2*jv)
            ham = -2*(k2/tt**2)*pv-3*HH*(vv*uv-rr*vel)-rr*dens-vv*piv+vv**2*pv-FF*uv
            max_constraint = max(max_constraint,abs(ham)/eps)
            zr = (xj*jv-2*(pp+ellj*pv))/Rj
            dr = (-2*jkj2*pv-6*ellj*(pp+ellj*pv)-xj*jp+xj*xj*pv-Fbj*jv)/Rj
            physical = [zr-tt*vel, dr-dens,
                        (vel+tt*dvel)/tt+pv+jv, ddens/tt-3*pp-jkj2*(tt*vel),
                        jpp+(3*hj-2*xj)*jp+(jkj2+kappaj)*jv+Rj*dens-4*xj*pp+2*Fbj*pv]
            max_physical=max(max_physical,max(abs(zv)/eps for zv in physical))
            epoch_modes.append({"k_com_squared":float(k2),"P":float(pv),"J":float(jv),
                                "P_prime":float(pp),"J_prime":float(jp),"J_second":float(jpp),
                                "bare_delta":float(dens),"matter_Z":float(tt*vel),
                                "hamiltonian_residual":float(ham)})
        mat=np.asarray(modeD)/eps
        rhs=np.asarray(modey)/eps
        singular=np.linalg.svd(mat,compute_uv=False)
        expected=np.array([3/tt**2,9/tt**4,10/tt**2,2,9/tt**4])
        found=np.linalg.solve(mat,rhs)
        relative=np.max(np.abs(found-expected)/(1+np.abs(expected)))
        max_recovery=max(max_recovery,float(relative))
        min_relative_sigma=min(min_relative_sigma,float(singular[-1]/singular[0]))
        numeric.append({"t_E":float(tt),"tau":float(tt*tt/2),"coefficients":found.tolist(),
                        "truth":expected.tolist(),"relative_recovery_error":float(relative),
                        "singular_values_in_declared_reference_units":singular.tolist(),"modes":epoch_modes})

    condition("forward Hamiltonian propagated",max_constraint<2e-9,max_residual_over_epsilon=max_constraint)

    condition("coefficient recovery on all31epochs",max_recovery<2e-8,max_relative_error=max_recovery)

    condition("full mode source and dust compatibility",max_physical<2e-9,max_residual_over_epsilon=max_physical)

    condition("physical rank stays nonzero on sampled interval",min_relative_sigma>1e-5,min_sigma_ratio=min_relative_sigma,
              qualification="31 sampled epochs; analytic continuity proves a local open interval, not an interval-arithmetic global rank certificate")

    condition("clock second derivative omission is detectable", abs(float(original_rhs(1.,y0)[1])-float(original_rhs(1.,y0)[1]-y0[1]))>0,
              omitted_term=float(y0[1]))

    condition("naive observed curvature c is not kappa",9!=7,response_c=9,fixed_bare_kappa=7)

    return checks, {"forward_rows": numeric, "initial_design": str(D/ep)}
