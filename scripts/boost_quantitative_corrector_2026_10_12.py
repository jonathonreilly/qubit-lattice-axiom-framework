#!/usr/bin/env python3
"""Full finite corrector, polynomial-growth and expectation controls."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/BOOST_QUANTITATIVE_CORRECTOR_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/BOOST_FORCED_OUTGOING_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/EXCLUDED_WALK_BOOST_BRACKET_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-11.md']
if not __debug__:
    raise RuntimeError("Run without -O: control assertions must be enabled")

def check_corrector():
    #!/usr/bin/env python3
    """Author controls, not a torus theorem or independent scientific review.

    The weighted two-antipodal-pair fixture is finite. Its I0=97/100 is not the
    torus I0. No previous campaign helper is imported.
    """
    import json
    import platform
    import numpy as np
    import scipy
    from scipy.integrate import quad_vec
    from scipy.linalg import eigh
    import sympy as sp

    checks = []


    def check(name, value):
        assert bool(value), name
        checks.append(name)
        print('checked', name, flush=True)


    def exact_zero(name, matrix):
        check(name, all(sp.simplify(v) == 0 for v in matrix))


    ii = sp.I
    sigma = [sp.Matrix([[0, 1], [1, 0]]),
             sp.Matrix([[0, -ii], [ii, 0]]),
             sp.diag(1, -1)]
    s1 = [sp.kronecker_product(p, sp.eye(2)) for p in sigma]
    s2 = [sp.kronecker_product(sp.eye(2), p) for p in sigma]
    c = sp.Matrix([0, 1, -1, 0])/sp.sqrt(2)
    T = sp.Matrix.hstack(*[p*c for p in s1])
    sines = [sp.Matrix([sp.Rational(5, 13), 0, 0]),
             sp.Matrix([0, sp.Rational(3, 5), sp.Rational(4, 5)])]
    cosines = [sp.Matrix([sp.Rational(12, 13), 1, 1]),
               sp.Matrix([1, sp.Rational(4, 5), sp.Rational(3, 5)])]
    eps = [sp.sqrt((v.T*v)[0]) for v in sines]
    normals = [v/e for v, e in zip(sines, eps)]
    cg = sp.Matrix.vstack(c, c)/sp.sqrt(2)
    P = sp.eye(8)-cg*cg.H
    H0 = sp.diag(*[sum(((s1[j]-s2[j])*v[j] for j in range(3)), sp.zeros(4)) for v in sines])
    Hstar = P*H0*P
    h0 = H0*cg
    Ifinite = sum(sp.Rational(1, 2)/(4*e**2) for e in eps)
    zeta = sp.Matrix.vstack(*[T*n/(2*e*sp.sqrt(2*Ifinite)) for n, e in zip(normals, eps)])
    transverse = sp.diag(*[T*(sp.eye(3)-n*n.T)*T.H for n in normals])
    triplet = sp.diag(T*T.H, T*T.H)
    Pi = transverse+zeta*zeta.H
    Q = P-Pi
    Qt = triplet-Pi
    Vj = [P*sp.diag(*[(s1[j]+s2[j])*cs[j]/2 for cs in cosines])*P for j in range(3)]
    kappa = [sp.Rational(1, 8), -sp.Rational(1, 12), sp.Rational(1, 16)]
    B = sum((v*k for v, k in zip(Vj, kappa)), sp.zeros(8))
    A = Pi*B*Pi

    check('finite_I0_is_not_torus_integral', Ifinite == sp.Rational(97, 100))
    exact_zero('physical_Pi_projection', Pi*Pi-Pi)
    exact_zero('physical_Pi_annihilates_contact_singlet', Pi*cg)
    exact_zero('physical_Hstar_Pi', Hstar*Pi)
    exact_zero('physical_Pi_h0', Pi*h0-zeta/sp.sqrt(Ifinite))
    alpha_test = sp.Matrix.vstack(c, -c)/sp.sqrt(2)
    triplet_test = sp.Matrix.vstack(2*T*sines[0], -2*T*sines[1])/sp.sqrt(2)
    exact_zero('direct_Pauli_mean_zero_singlet_range', Hstar*alpha_test-triplet_test)

    # delta=7/10 selects only the second pair. The cutoff is independent of kappa/time.
    cuts = [0, 1]
    raw_map = sp.diag(*[cut*c*(T*n).H/(2*e) for cut, n, e in zip(cuts, normals, eps)])
    corrector_map = P*raw_map
    low_map = sp.diag(*[(1-cut)*sp.eye(4) for cut in cuts])
    eta_map = sp.eye(8)-Hstar*corrector_map
    mean_row = cg.H*raw_map
    exact_zero('corrector_physical_mean_zero', cg.H*corrector_map*Qt)
    exact_zero('corrector_exact_residual_and_mean_term',
               (eta_map-low_map-h0*mean_row)*Qt)
    exact_zero('global_zeta_orthogonality', zeta.H*Qt)
    exact_zero('actual_residual_is_triplet', (sp.eye(8)-triplet)*Q*B*Pi)
    exact_zero('actual_source_residual_is_triplet', (sp.eye(8)-triplet)*Q*h0)
    check('bounded_perturbation_does_not_commute', any(sp.simplify(v) != 0 for v in B*Hstar-Hstar*B))

    # Analytic radial coefficients: no torus sampling or fitted powers.
    delta, radius = sp.symbols('delta radius', positive=True)
    fold_low = sp.pi**(-3)*(sp.pi**2/4)*4*sp.pi*(sp.pi*delta/2)
    fold_high = sp.pi**(-3)*(sp.pi**4/16)*4*sp.pi/delta
    check('folded_cone_low_coefficient', sp.simplify(fold_low-sp.pi*delta/2) == 0)
    check('folded_cone_high_coefficient', sp.simplify(fold_high-sp.pi**2/(4*delta)) == 0)
    L = sp.Rational(192, 7)
    Sratio = sp.Rational(203, 4)
    Caratio = 2*(L+3)
    check('source_S_constant', sp.Rational(7, 4)*L+sp.Rational(11, 4) == Sratio)
    check('source_derivative_difference_constant', 2*L+sp.Rational(17, 3) <= Caratio)
    check('source_normalization_error_bound', sp.Rational(1, 32)+6*sp.sqrt(6) < 8*Sratio)
    check('source_first_derivative_error_bound',
          sp.Rational(1, 4)+Sratio/32+2*sp.sqrt(6)*Caratio+2*sp.sqrt(6)*Sratio < 16*Sratio)

    # A continuum radial diagnostic, with normalized measure 3r^2 dr on (0,1).
    # beta=1/r-3r is orthogonal to 1/(2r), yet its exact singlet inverse is not L2.
    beta = 1/radius-3*radius
    check('radial_global_orthogonality', sp.integrate(beta/(2*radius)*3*radius**2, (radius, 0, 1)) == 0)
    md = sp.integrate(beta/(2*radius)*3*radius**2, (radius, delta, 1))
    xnorm2 = sp.integrate((beta/(2*radius))**2*3*radius**2, (radius, delta, 1))-md**2
    errnorm2 = sp.integrate((beta+2*radius*md)**2*3*radius**2, (radius, 0, delta))
    errnorm2 += sp.integrate((2*radius*md)**2*3*radius**2, (radius, delta, 1))
    check('radial_corrector_divergence_diagnostic', sp.limit(delta*xnorm2, delta, 0, dir='+') == sp.Rational(3, 4))
    check('radial_residual_square_root_diagnostic', sp.limit(errnorm2/delta, delta, 0, dir='+') == 3)


    def array(mat):
        return np.array(mat.evalf(), dtype=complex)


    pn, pin, qn, hsn, h0n, cn = map(array, [P, Pi, Q, Hstar, h0, cg])
    bn, an, xn, etan = map(array, [B, A, corrector_map, eta_map])
    vjn = [array(v) for v in Vj]
    spin1, spin2 = [array(p) for p in s1], [array(p) for p in s2]
    sin_data, cos_data = [np.array(v, float).ravel() for v in sines], [np.array(v, float).ravel() for v in cosines]
    kbase = np.array(kappa, float)
    lam = 1/32
    amplitudes0 = np.array([7/11, 4/11])
    amplitude_slopes = np.array([1/9, -1/13])
    frequencies0 = np.array([7/5, 13/8])
    frequency_slopes = np.array([1/7, -1/11])


    def block_diag(blocks):
        out = np.zeros((8, 8), complex)
        out[:4, :4], out[4:, 4:] = blocks
        return out


    def data(theta):
        kval = kbase.copy(); kval[0] += theta
        blocks = []
        derivative_blocks = []
        for ss, cs in zip(sin_data, cos_data):
            blocks.append(sum(((spin1[j]-spin2[j])*ss[j]*np.cos(lam*kval[j]/2)
                               +(spin1[j]+spin2[j])*cs[j]*np.sin(lam*kval[j]/2)
                               for j in range(3)), np.zeros((4, 4), complex)))
            derivative_blocks.append(-(spin1[0]-spin2[0])*ss[0]*np.sin(lam*kval[0]/2)/2
                                     +(spin1[0]+spin2[0])*cs[0]*np.cos(lam*kval[0]/2)/2)
        hfull = block_diag(blocks)
        gen = pn@hfull@pn/lam
        gj = pn@block_diag(derivative_blocks)@pn
        hh = hfull@cn
        hj = lam*block_diag(derivative_blocks)@cn
        bb = bn+theta*vjn[0]
        aa = pin@bb@pin
        return gen, gj, hh, hj, bb, aa


    def source(time, theta=0.0):
        amp = amplitudes0+theta*amplitude_slopes
        freq = frequencies0+theta*frequency_slopes
        phase = np.exp(-1j*time*freq)
        value = np.dot(amp, phase)
        time_derivative = np.dot(-1j*freq*amp, phase)
        phase_derivative = -1j*time*frequency_slopes*phase
        parameter_derivative = np.dot(amplitude_slopes, phase)+np.dot(amp, phase_derivative)
        return value, time_derivative, parameter_derivative


    def forced(time, operator, vector, theta=0.0):
        eig, vec = eigh(operator)
        components = vec.conj().T@vector
        amp = amplitudes0+theta*amplitude_slopes
        freq = frequencies0+theta*frequency_slopes
        multiplier = np.zeros(8, complex)
        for weight, frequency in zip(amp, freq):
            gap = frequency-eig
            # expm1 keeps the response stable for small time/gap.
            multiplier += weight*np.exp(-1j*time*eig)*(-np.expm1(-1j*time*gap))/gap
        return vec@(multiplier[:, None]*components)


    def z(time, theta=0.0):
        return forced(time, data(theta)[5], pin@h0n, theta)


    def W(time, theta=0.0):
        gen, _, hh, _, _, _ = data(theta)
        return forced(time, gen, hh, theta)


    def five_point(function, theta=0.0):
        step = 1e-4
        return (-function(theta+2*step)+8*function(theta+step)
                -8*function(theta-step)+function(theta-2*step))/(12*step)


    gen, gj, hh, hj, bb, aa = data(0.0)
    vg = gen-hsn/lam
    eg = gen-hsn/lam-bb
    ej = gj-vjn[0]
    eigenvalues, eigenvectors = eigh(gen)


    def U(time):
        return (eigenvectors*np.exp(-1j*time*eigenvalues))@eigenvectors.conj().T


    def residual(time):
        aval, at, _ = source(time)
        zz = z(time)
        zt = -1j*aa@zz+1j*pin@h0n*aval
        rr = qn@(bb@zz-h0n*aval)
        rt = qn@(bb@zt-h0n*at)
        return rr, rt


    def integrate(function, time):
        return quad_vec(function, 0, time, epsabs=2e-11, epsrel=2e-11, limit=500)[0]


    ibp_errors = []
    parameter_errors = []
    for time in [-1.7, 0.6, 2.3]:
        original = integrate(lambda ss: U(time-ss)@residual(ss)[0], time)
        xt = xn@residual(time)[0]
        x0 = xn@residual(0.0)[0]
        endpoint = -1j*lam*(xt-U(time)@x0)
        time_term = 1j*lam*integrate(lambda ss: U(time-ss)@xn@residual(ss)[1], time)
        perturbation_term = -lam*integrate(lambda ss: U(time-ss)@vg@xn@residual(ss)[0], time)
        error_term = integrate(lambda ss: U(time-ss)@etan@residual(ss)[0], time)
        combined = endpoint+time_term+perturbation_term+error_term
        ibp_errors.append(float(np.linalg.norm(original-combined)))
        check(f'noncommuting_corrector_Duhamel_t_{time}', ibp_errors[-1] < 2e-9)

        def derivative_forcing(ss):
            aval, _, aj = source(ss)
            zz = z(ss)
            zj = five_point(lambda th: z(ss, th))
            dd = W(ss)-zz
            rj = qn@(vjn[0]@zz+bb@zj-h0n*aj)
            error_j = ej@zz+eg@zj-hj*aval+(h0n-hh)*aj
            generator_term = gj@dd
            return generator_term+rj+error_j

        from_equation = -1j*integrate(lambda ss: U(time-ss)@derivative_forcing(ss), time)
        from_parameter = five_point(lambda th: W(time, th)-z(time, th))
        parameter_errors.append(float(np.linalg.norm(from_equation-from_parameter)))
        check(f'full_differentiated_error_t_{time}', parameter_errors[-1] < 2e-8)

    print(json.dumps({'controls_completed': len(checks),
                      'max_ibp_error': max(ibp_errors),
                      'max_parameter_error': max(parameter_errors),
                      'finite_I0': str(Ifinite),
                      'python': platform.python_version(), 'sympy': sp.__version__,
                      'numpy': np.__version__, 'scipy': scipy.__version__,
                      'scope': 'author finite/radial algebra controls; no torus theorem certification'}, indent=2), flush=True)


def check_polynomial():
    #!/usr/bin/env python3
    """Author controls for the polynomial refinement; no continuum certification."""
    import json
    import numpy as np
    import scipy
    from scipy.integrate import quad_vec
    from scipy.linalg import expm
    import sympy as sp

    names = []


    def check(name, condition):
        assert bool(condition), name
        names.append(name)
        print('checked', name, flush=True)


    def matrix_zero(name, value):
        check(name, all(sp.simplify(entry) == 0 for entry in value))


    J = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    matrix_zero('tangent_generator_Hermitian', J.H-J)
    matrix_zero('tangent_generator_square', J*J-sp.eye(2))
    om, dom = sp.symbols('om dom', real=True)
    matrix_zero('pointwise_parameter_commutator', (om*J)*(dom*J)-(dom*J)*(om*J))

    pauli = [sp.Matrix([[0, 1], [1, 0]]), J, sp.diag(1, -1)]
    p1 = [sp.kronecker_product(p, sp.eye(2)) for p in pauli]
    p2 = [sp.kronecker_product(sp.eye(2), p) for p in pauli]
    singlet = sp.Matrix([0, 1, -1, 0])/sp.sqrt(2)
    triplets = sp.Matrix.hstack(*[p*singlet for p in p1])
    k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
    dd = sp.Matrix([k1, k2, sp.sqrt(3)*k3/2])
    pauli_B = triplets.H*sum(((p1[j]+p2[j])*dd[j]/2 for j in range(3)), sp.zeros(4))*triplets
    g_exact = sp.Matrix([sp.I*k2, -sp.I*k1])
    block = (dd[2]*J).row_join(g_exact)
    block = block.col_join(g_exact.H.row_join(sp.zeros(1)))
    matrix_zero('direct_Pauli_transverse_block', pauli_B-block)

    time_symbol = sp.symbols('time_symbol', nonnegative=True)
    L = sp.Rational(192, 7)
    mr = sp.Integer(406)


    def nonnegative_polynomial(name, expression):
        poly = sp.Poly(sp.expand(expression), time_symbol)
        check(name, all(c >= 0 for c in poly.all_coeffs()))


    nonnegative_polynomial('weighted_z_polynomial_constant',
                           mr*(1+time_symbol)-12*(1+time_symbol/4))
    nonnegative_polynomial('weighted_zj_polynomial_constant',
                           2*mr*(1+time_symbol)**2
                           -12*(L+3+(2+(L+3)/4)*time_symbol+time_symbol**2/4))
    nonnegative_polynomial('weighted_zt_polynomial_constant',
                           mr*(1+time_symbol)-(12+sp.Rational(3, 2)*time_symbol))
    nonnegative_polynomial('weighted_zjt_polynomial_constant',
                           4*(1+time_symbol)**2-((1+time_symbol)**2+3*(1+time_symbol)))
    nonnegative_polynomial('residual_polynomial_constant',
                           3*(1+time_symbol)-(sp.Rational(5, 2)+time_symbol/2))
    nonnegative_polynomial('residual_jt_polynomial_constant',
                           6*(1+time_symbol)**2-(4*(1+time_symbol)+2*(1+time_symbol)**2))

    # A single antipodal pair at q=(0,0,pi/6): finite I0=1, zeta=e3.
    # Its three-dimensional block is only an algebra fixture; it has recurrence.
    jn = np.array(J, complex)
    kbase = np.array([1/8, -1/12, 1/16])
    kslope = np.array([1/3, 1/5, 1/7])
    zeta = np.array([0, 0, 1], complex)


    def data(theta):
        kval = kbase+theta*kslope
        dvec = kval*np.array([1, 1, np.sqrt(3)/2])
        derivative = kslope*np.array([1, 1, np.sqrt(3)/2])
        dop = dvec[2]*jn
        dj = derivative[2]*jn
        coupling = np.array([1j*dvec[1], -1j*dvec[0]])
        gj = np.array([1j*derivative[1], -1j*derivative[0]])
        operator = np.zeros((3, 3), complex)
        operator[:2, :2] = dop
        operator[:2, 2] = coupling
        operator[2, :2] = coupling.conj()
        return operator, dop, dj, coupling, gj


    def forced(time, theta=0.0):
        operator = data(theta)[0]
        frequency = 2+theta/7
        amplitude = (1+theta/5)*(3/10+theta/20)
        return amplitude*np.linalg.solve(frequency*np.eye(3)-operator,
                    (expm(-1j*time*operator)-np.exp(-1j*time*frequency)*np.eye(3))@zeta)


    def derivative(function):
        hh = 1e-4
        return (-function(2*hh)+8*function(hh)-8*function(-hh)+function(-2*hh))/(12*hh)


    operator, dop, dj, g, gj = data(0.0)
    state_errors, derivative_errors = [], []
    for time in [-2.2, 0.4, 3.1]:
        def source_integrand(ss):
            return expm(-1j*(time-ss)*dop)@g*forced(ss)[2]

        u_integral = -1j*quad_vec(source_integrand, 0, time, epsabs=1e-12, epsrel=1e-12)[0]
        state_errors.append(float(np.linalg.norm(u_integral-forced(time)[:2])))
        check(f'transverse_block_integral_t_{time}', state_errors[-1] < 1e-10)

        def differentiated_integrand(ss):
            ud = expm(-1j*(time-ss)*dop)
            alpha = forced(ss)[2]
            alpha_j = derivative(lambda th: forced(ss, th))[2]
            propagator_term = (-1j*(time-ss)*dj)@ud@g*alpha
            coupling_term = ud@gj*alpha
            amplitude_term = ud@g*alpha_j
            return propagator_term+coupling_term+amplitude_term

        from_integral = -1j*quad_vec(differentiated_integrand, 0, time, epsabs=1e-11, epsrel=1e-11)[0]
        from_state = derivative(lambda th: forced(time, th))[:2]
        derivative_errors.append(float(np.linalg.norm(from_integral-from_state)))
        check(f'transverse_three_derivatives_t_{time}', derivative_errors[-1] < 1e-8)

    print(json.dumps({'controls_completed':len(names), 'max_state_error':max(state_errors),
                      'max_derivative_error':max(derivative_errors), 'finite_I0':1,
                      'numpy':np.__version__, 'scipy':scipy.__version__, 'sympy':sp.__version__,
                      'scope':'author coefficient and finite-block controls; no continuum proof or independent review'}, indent=2))


def check_mean():
    #!/usr/bin/env python3
    """Author arithmetic and generic coefficient checks, not a continuum proof.

    The quadratic-form identity is inherited from exact X. This checks its
    all-index bookkeeping and new majorant arithmetic without a torus grid.
    """
    import json
    import sympy as sp

    checks=[]
    def check(name, condition):
        assert bool(condition), name
        checks.append(name)
        print('checked', name, flush=True)

    t=sp.symbols('t', real=True)
    # Scalar exponential-generating majorants; differentiation performs the
    # product rule independently of the termwise numbers in the manuscript.
    H=4+t+t**2/4
    h=4+t+t**2/4
    hb=1+t/2+t**2/8
    r=1+t+t**2/2
    J=r+2*hb*h
    A_comm=2*H*J
    A_ranks=2*h*r+2*(H*hb*h+H*h*hb)
    check('A_second_derivative_two_arrangements',
          sp.diff(A_comm,t,2).subs(t,0)==sp.diff(A_ranks,t,2).subs(t,0)==85)
    ha=1+t/2
    hab=sp.Rational(1,2)+t/4
    Fba=2*hab*h+2*ha*hb
    Hdelta=4+t
    Ha=1+t/2
    hq=2+t
    hbq=1+t/2
    Lh=Hdelta*hq/2+Ha*h
    Lhb=Hdelta*hbq/2+Ha*hb
    Ldagh=Hdelta*hq/2
    Ldaghb=Hdelta*hbq/2
    C=6*t+ha*r+h*r+H*Fba+Lhb*h+Lh*hb+hb*Ldagh+h*Ldaghb
    check('C_first_derivative_full_product_rule',sp.diff(C,t).subs(t,0)==sp.Rational(149,2))
    check('Taylor_operator_constant',sp.Rational(75,4)+sp.Rational(85,32)<22)
    check('limiting_operator_constant',6+4*sp.sqrt(3)<13 and 3+sp.sqrt(3)<13)

    # Generic Hermitian coefficient fixture; not a physical finite torus.
    HH=sp.diag(0,0,2)
    PP=sp.diag(1,1,0)
    Ls=[sp.Matrix([[1,sp.I,2],[-sp.I,3,sp.I],[2,-sp.I,4]]),
        sp.Matrix([[2,1,sp.I],[1,4,3],[-sp.I,3,5]]),
        sp.Matrix([[3,sp.I,1],[-sp.I,5,2*sp.I],[1,-2*sp.I,6]])]
    k=sp.symbols('k0:3', real=True)
    z=sp.Matrix([1+k[0]+sp.I*k[1],k[2]+sp.I*k[0]*k[1],0])
    all_form=True
    all_kernel=True
    for a in range(3):
        for b in range(3):
            delta=int(a==b)
            comm=HH*Ls[b]-Ls[b]*HH
            BB=k[b]*comm
            CC=delta*HH*(Ls[b]-sp.eye(3))
            all_form &= (BB.H==-BB and CC-CC.H==BB.diff(k[a]))
            qz=CC*z+BB*z.diff(k[a])
            target=HH*Ls[b]*(k[b]*z).diff(k[a])
            all_kernel &= all(sp.simplify(x)==0 for x in qz-target)
            all_kernel &= sp.simplify((z.H*qz)[0])==0
    check('all_nine_symmetric_coefficient_identities',all_form)
    check('all_nine_kernel_pairings',all_kernel)

    # Each discarded factor is <=1 on 0<lambda<=1, s>=1. Map the actual
    # monomials to the two retained powers; no fit to sampled lambda or time.
    retained=[(sp.Rational(1,2),3),(1,5)]
    actual=[(sp.Rational(1,2),1),(1,1),(sp.Rational(3,2),3),
            (sp.Rational(1,2),3),(1,5),(1,1),
            (sp.Rational(3,2),3),(sp.Rational(3,2),3),(2,5)]
    check('mean_monomials_uniform_dominance',all(any(p>=a and q<=b for a,b in retained) for p,q in actual))
    eta=sp.Rational(1,6)
    check('open_window_endpoint_arithmetic',sp.Rational(1,2)-3*eta==0 and 1-5*eta>0)
    print(json.dumps({'controls_completed':len(checks),'sympy':sp.__version__,
      'scope':'author exact product-rule arithmetic and generic all-index coefficient fixture; no independent review'},indent=2))


check_corrector()
check_polynomial()
check_mean()
print("per_element: exact mean subtraction, residual and cone majorants checked")
print("per_site: checked and not executed — finite physical blocks are not a volume limit")
print("per_mode: noncommuting Duhamel and every differentiated error term checked in finite controls")
print("per_block: full transverse derivative and generic expectation majorant controls checked")
print("lattice_wide: checked and not executed — uniform continuum bounds and growing-time limits require Q1–Q34")
print("TOTAL: PASS=51 FAIL=0")
print("SCOPE: 27 corrector, 16 polynomial and 8 mean finite control records; no analytic proof or audit verdict from this runner")
