"""Conditional scalar/metric controls; constructed inputs, no file or network I/O."""
AUDIT_TIMEOUT_SEC = 120

def run_checks():
    import hashlib

    import json

    import pathlib

    import sympy as s

    checks = []

    details = {}

    def zero(name, expr):
        residual = s.factor(s.simplify(expr))
        checks.append({"name": name, "pass": residual == 0, "residual": str(residual)})

    def nonzero(name, expr):
        residual = s.factor(s.simplify(expr))
        checks.append({"name": name, "pass": residual != 0,
                       "expected_nonzero": str(residual)})

    u, r, z, eta, chi, mu = s.symbols('u r z eta chi mu', real=True)

    rp = s.symbols('rp', positive=True)

    C = 1 + u + u**2

    Pc = r**2*C

    psi = 2*s.integrate((r-z)/(r*z)*z**2*C, (z, 0, r))

    zero('polynomial_forward_kernel', psi-r**2*C/3)

    invert = lambda f: s.diff(r**2*s.diff(f, r), r)/2

    zero('polynomial_radial_inverse', invert(psi)-Pc)

    zero('radial_boundary_constant', invert(s.Function('c0')(u)))

    zero('radial_boundary_inverse_r', invert(s.Function('c1')(u)/r))

    F = r**2*(eta**2+eta*r+r**3)*(3*mu**2-1)/2

    Fcone = F.subs(eta, u-r)

    Fz = F.subs({eta: u-z, r: z}, simultaneous=True)

    psif = 2*s.integrate((r-z)/(r*z)*Fz, (z, 0, r))

    zero('time_dependent_kernel_inverse', invert(psif)-Fcone)

    zero('cone_first_time', s.diff(Fcone,u)-s.diff(F,eta).subs(eta,u-r))

    zero('cone_fixed_time_radial', s.diff(Fcone,r)+s.diff(Fcone,u)
         -s.diff(F,r).subs(eta,u-r))

    nonzero('distance_derivative_is_not_time', s.diff(Fcone,r)
            -s.diff(F,eta).subs(eta,u-r))

    u0=s.symbols('u0',real=True)

    nullF=(eta+r-u0)*r**2*(1+eta)

    zero('single_cone_metric_restriction_null',nullF.subs(eta,u0-r))

    nonzero('single_cone_null_has_normal_derivative',s.diff(nullF,eta).subs(eta,u0-r))

    lapang=lambda f:s.diff((1-mu**2)*s.diff(f,mu),mu)

    lap=lambda f:s.diff(f,r,2)+2*s.diff(f,r)/r+lapang(f)/r**2

    lapcone=lambda f:(s.diff(f,r,2)+2*s.diff(f,r,u)+s.diff(f,u,2)
                     +2*(s.diff(f,r)+s.diff(f,u))/r+lapang(f)/r**2)

    zero('coeval_laplacian_cone_chain',lapcone(Fcone)-lap(F).subs(eta,u-r))

    Hc=s.symbols('Hc',real=True)

    wavecone=lambda f:(-s.diff(f,r,2)-2*s.diff(f,r,u)-2*s.diff(f,r)/r
                       -(Hc+2/r)*s.diff(f,u)-lapang(f)/r**2)

    zero('wave_operator_second_time_cancellation',wavecone(Fcone)
         -(s.diff(F,eta,2)-Hc*s.diff(F,eta)-lap(F)).subs(eta,u-r))

    nonzero('omitted_mixed_derivative_detected',2*s.diff(Fcone,r,u))

    nonzero('omitted_clock_correction_detected',Hc*s.diff(Fcone,u))

    g=s.Function('g')(u)

    zero('observer_time_gain_spatial_product',lapcone(g*Fcone)-g*lapcone(Fcone)
         -2*s.diff(g,u)*(s.diff(Fcone,r)+s.diff(Fcone,u))
         -(s.diff(g,u,2)+2*s.diff(g,u)/r)*Fcone)

    nonzero('homogeneous_gain_replacement_fails',
            (lapcone((1+u**2)*Fcone)-(1+u**2)*lapcone(Fcone)))

    for ell in range(7):
        factor2=(ell+2)*(ell+1)*ell*(ell-1)/4
        checks.append({'name':f'shear_ell_{ell}_null_or_positive',
                       'pass': factor2 == 0 if ell<2 else factor2>0,
                       'squared_response':factor2})

    eps=s.symbols('eps')

    Po,Ps,Do,Ds,I=s.symbols('Psi_o Psi_s nv_o nv_s integral')

    Eratio=(1+eps*I)*(1-eps*Po+eps*Do)/(1-eps*Ps+eps*Ds)

    redshift=s.series(1/Eratio,eps,0,2).removeO()

    zero('redshift_energy_ratio_endpoint_doppler_integral',
         redshift-(1+eps*(Po-Ps+Ds-Do-I)))

    Psi_t,Phi_t,Psi_x,Phi_x=s.symbols('Psi_eta Phi_eta Psi_x Phi_x')

    zero('covector_geodesic_energy_source',(-2*Psi_t-2*Phi_t)/2+Psi_t+Phi_t)

    zero('transverse_geodesic_sum',-(Psi_x+Phi_x)+2*(Psi_x+Phi_x)/2)

    a=s.Function('a')(eta)

    V=s.Function('Vv')(eta)

    Psi=s.Function('Psi')(eta)

    euler=s.diff(V,eta)+s.diff(a,eta)*V/a+Psi

    zero('velocity_potential_clock_relation',s.diff(a*V,eta)/a+Psi-euler)

    for omin,omax,rmin,rmax in [(0,1,2,4),(0,3,2,4),(1,3,2,4),(0,1,2,s.Rational(5,2))]:
        lower=max(omin-rmin,omin-rmax);upper=min(omax-rmin,omax-rmax)
        zero('coverage_width_'+str((omin,omax,rmin,rmax)),
             (upper-lower)-((omax-omin)-(rmax-rmin)))

    t=s.symbols('t', positive=True)

    m=s.symbols('m', real=True)

    zz=m*(m+1)

    Y=(8*m*m+12*m+3)/(2*m+3)

    k2=4*zz*(8*zz+9)/(3-8*zz)

    H=1/t

    v=1/t

    rho=t**-3

    A=t

    rE=t**-2

    alpha=s.Integer(1)

    force=-2/t**2

    mass=7/t**2

    K2=k2/t**2

    P=t**(2*m)

    field=Y*P

    pi=s.diff(field,t)

    U=(Y-4*m-2)*t*P

    delta=(-2*k2-12*m-5+(2-2*m)*Y)*P

    zero('original_background_friedmann',3*H**2-rE-v*v/2-s.Rational(3,2)/t**2)

    zero('original_background_raychaudhuri',s.diff(H,t)+(rE+v*v)/2)

    zero('original_background_scalar',s.diff(v,t)+3*H*v+force)

    zero('original_background_dust',s.diff(rE,t)-(alpha*v-3*H)*rE)

    zero('original_background_force',s.diff(force,t)-mass*v+3*H*alpha*rE)

    zero('original_metric_momentum',s.diff(P,t)-(v*field-rE*U)/2+H*P)

    zero('original_dust_euler',s.diff(U,t)+P+alpha*field+alpha*v*U)

    zero('original_dust_continuity',s.diff(delta,t)-3*s.diff(P,t)-K2*U)

    zero('original_scalar_definition',s.diff(field,t)-pi)

    zero('original_scalar_second_order',s.diff(pi,t)+3*H*pi+(K2+mass)*field
         +alpha*rE*delta-4*v*s.diff(P,t)+2*force*P)

    zero('original_hamiltonian_constraint',-2*K2*P-3*H*(v*field-rE*U)-rE*delta
         -v*pi+v*v*P-force*field)

    zero('original_pressure_trace',s.diff(P,t,2)+4*H*s.diff(P,t)
         +(2*s.diff(H,t)+3*H**2)*P-(v*pi-v*v*P+3*field/t**2)/2)

    ell=s.symbols('ell',integer=True,nonnegative=True)

    R=s.Function('R')(r)

    Fhat=s.exp(2*m*(u-r))*R

    lapL=(s.diff(Fhat,r,2)+2*s.diff(Fhat,r,u)+s.diff(Fhat,u,2)
          +2*(s.diff(Fhat,r)+s.diff(Fhat,u))/r-ell*(ell+1)*Fhat/r**2)

    radial_rule={s.diff(R,r,2):-2*s.diff(R,r)/r-(k2-ell*(ell+1)/r**2)*R}

    zero('full_cone_helmholtz_completion',(lapL+k2*Fhat).subs(radial_rule))

    D=2*m+3

    N=8*m*m+12*m+3

    polys=[m*D,D,m*N,N]

    coef=s.Matrix([[s.expand(p).coeff(m,d) for p in polys] for d in range(4)])

    constant=s.factor(coef.det())

    details['trace_vandermonde_constant']=str(constant)

    nonzero('trace_polynomial_basis_determinant',constant)

    ms=[s.Rational(1,10),s.Rational(1,8),s.Rational(1,6),s.Rational(1,5),s.Rational(1,4)]

    trace=s.Matrix([[z,1,z*Y.subs(m,z),Y.subs(m,z)] for z in ms])

    vand=s.prod(ms[j]-ms[i] for i in range(4) for j in range(i+1,4))

    zero('trace_determinant_vandermonde',trace[:4,:].det()
         -constant*vand/s.prod(2*z+3 for z in ms[:4]))

    scalar=s.Matrix([[-z*Y.subs(m,z),-Y.subs(m,z),z,k2.subs(m,z)/4,1] for z in ms])

    nonzero('five_exact_growing_modes_scalar_rank',scalar.det())

    details['trace_minor']=str(s.factor(trace[:4,:].det()))

    details['scalar_determinant']=str(s.factor(scalar.det()))

    details['modes']=[str(z) for z in ms]

    details['mode_k2']=[str(s.factor(k2.subs(m,z))) for z in ms]

    transfer=s.Matrix([[i,2*i,3*i,4*i] for i in range(1,7)])

    checks.append({'name':'one_transfer_trace_rank_one','pass':transfer.rank()==1,'rank':transfer.rank()})

    scalar_sep=s.Matrix([[i,2*i,3*i,i**3,4*i] for i in range(1,7)])

    checks.append({'name':'one_transfer_scalar_rank_at_most_two','pass':scalar_sep.rank()==2,'rank':scalar_sep.rank()})

    L=s.symbols('L', positive=True)

    zL=6*L/(9+8*L+s.sqrt((9+8*L)**2+96*L))

    zero('growing_branch_dispersion',8*zL**2+(9+8*L)*zL-3*L)

    zero('growing_limit',s.limit(zL,L,s.oo)-s.Rational(3,8))

    details['large_L_z_correction']=str(s.limit(L*(zL-s.Rational(3,8)),L,s.oo))

    dr,du,sigma=s.symbols('dr du sigma',positive=True)

    wm=r*r/(2*dr*dr)-r/(2*dr)

    w0=-r*r/(dr*dr)

    wp=r*r/(2*dr*dr)+r/(2*dr)

    variance=s.factor(sigma*sigma*(wm*wm+w0*w0+wp*wp))

    details['P_noise_variance']=str(variance)

    details['Puu_noise_variance']=str(s.factor(6*variance/du**4))

    zero('finite_stencil_constant_response',wm+w0+wp)

    zero('finite_stencil_quadratic_inverse',wm*(r-dr)**2/3+w0*r*r/3+wp*(r+dr)**2/3-r*r)

    return checks, details
