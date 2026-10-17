"""Portable independent physical-bit, recurrence and exact scalar check.

The mathematical body is unchanged except for resource-report metadata.
Original source-run limits are historical; canonical execution shares the
primary process and its external runner-cache wall limit.
The parent imports this module; it does not import the author's calculation.
"""
from pathlib import Path
import hashlib
import json
import platform
import sys
import time
import sympy as sp

def run_independent_checks(ROOT):
    started = time.monotonic()
    pins = json.loads((ROOT / 'SOURCE_PINS.json').read_text())
    for row in pins['files']:
        raw = (ROOT / row['snapshot']).read_bytes()
        assert len(raw) == row['bytes']
        assert hashlib.sha256(raw).hexdigest() == row['sha256'], row['snapshot']
    source = json.loads((ROOT / 'sources/author/inputs/CERTIFICATE.json').read_text())
    R = sp.Rational
    I = sp.I
    evidence = {'scope': 'Independent exact finite algebra and scalar comparisons; conditional infinite-operator proof reviewed separately.',
                'checks': {}, 'strict_positive_margins': {}, 'countercases': {}}


    def require(name, condition):
        assert bool(condition), name
        evidence['checks'][name] = True


    def pos(name, expression):
        value = sp.cancel(expression)
        require(name, value.is_Rational and value.p > 0 and value.q > 0)
        evidence['strict_positive_margins'][name] = str(value)


    def zero(name, matrix):
        require(name, matrix.applyfunc(sp.cancel) == sp.zeros(*matrix.shape))


    def record(value):
        value = sp.cancel(value)
        return {'exact': str(value), 'display_only_float': float(value)}


    # Physical basis: old1,old2,A,B; bit3 is old1 and bit0 is B.
    # Coefficient norms follow from exact projector polynomials, not eigensolvers.
    dim = 16
    eye = sp.eye(dim)


    def flip(bit):
        mat = sp.zeros(dim)
        for j in range(dim):
            mat[j ^ (1 << bit), j] = 1
        return mat


    def number(bit):
        return sp.diag(*[(j >> bit) & 1 for j in range(dim)])


    X1, X2, XA, XB = [flip(b) for b in (3, 2, 1, 0)]
    nA, nB = number(1), number(0)
    LAB = sp.zeros(dim)
    for j in range(dim):
        if ((j >> 1) & 1) != (j & 1):
            LAB[j ^ 3, j] = 1
    K = sp.diag(*[2 + (-1) ** (((j >> 3) & 1) + ((j >> 2) & 1)) for j in range(dim)])
    parity = X1 * X2
    iota = sp.zeros(16, 4)
    for j in range(4):
        iota[4*j, j] = 1
    derivatives = {'DeltaA': nA, 'DeltaB': nB, 'h': nA+nB-LAB,
                   'u': nA*nB, 'gA': nA*(eye+X1), 'gB': nB*(eye+X2)}
    weights = {'DeltaA': 1, 'DeltaB': 1, 'h': 2, 'u': 1, 'gA': 2, 'gB': 2}
    for name, D in derivatives.items():
        zero(name+'_selfadjoint', D-D.T)
        zero(name+'_spectral_polynomial', D*D-weights[name]*D)
        require(name+'_nonzero_positive_eigenvalue', sp.trace(D) > 0)
        zero(name+'_annihilates_full_vacuum_embedding', D*iota)
        zero(name+'_reduces_parity', D*parity-parity*D)
        zero(name+'_preserves_source_number', D*(nA+nB)-(nA+nB)*D)
    for name, D in {'lambdaA': eye+XA, 'lambdaB': eye+XB}.items():
        zero(name+'_positive_norm_two', D*D-2*D)
        zero(name+'_reduces_parity', D*parity-parity*D)
    require('interaction_need_not_commute_with_old_K', derivatives['gA']*K-K*derivatives['gA'] != sp.zeros(16))
    for s, pair in ((1, (0, 3)), (-1, (1, 2))):
        for p in (-1, 1):
            v = sp.zeros(16, 1)
            v[4*pair[0], 0] = 1
            v[4*pair[1], 0] = p
            P = v*v.T/2
            zero(f'open_{s}_{p}_projector', P*P-P)
            zero(f'open_{s}_{p}_old_energy', K*v-(2+s)*v)
            zero(f'open_{s}_{p}_parity', parity*v-p*v)
            for name, D in derivatives.items():
                zero(f'open_{s}_{p}_{name}_fixed_channel', (eye-P)*D*P)

    # Full-qubit positive contact/vacancy blocks, before one-head reduction.
    n = sp.diag(0, 1)
    x = sp.Matrix([[0, 1], [1, 0]])
    contact = sp.kronecker_product(n, sp.eye(2)+x)
    vacancy = sp.eye(2)-n
    zero('full_qubit_clock_source_contact_positive_norm_two', contact*contact-2*contact)
    zero('full_qubit_vacancy_positive_norm_one', vacancy*vacancy-vacancy)
    require('physical_vacancy_reduction_has_scalar_plus_negative_contact',
            sp.eye(2)-n == sp.eye(2)+(-n))

    # Exact rational scalars are derived from certificate input decimals/fractions.
    # No author result or author checker is used to construct these bounds.
    params = {k: R(v) for k, v in source['exact_parameters'].items()}
    params['h'] = params['t']
    params['nu'] = -params['mu1']
    J = params['J']
    require('fixed_J_literal', J == R('0.030021107107032'))
    a = R(1, 10**8)
    for name in ('DeltaA','DeltaB','h','u','gA','gB','lambdaA','lambdaB','mu0','nu'):
        pos(name+'_remains_positive', params[name]-a)
    b = a*sum(weights.values())
    c = a*(2+1)
    g = R(9, 50)
    A = R(166)
    den_tail = g*(g-b)
    num_match = (b+c)*den_tail+J**2*b
    den_inverse = den_tail-A*num_match
    pos('Neumann_denominator', den_inverse)
    eta = num_match/den_tail
    A_actual = A*den_tail/den_inverse
    # Difference of the two inverse ceilings, an independent rearrangement of
    # the author's 2 J A^2 eta/(1-A eta) expression.
    extra = 2*J*(A_actual-A)
    pos('gap_above_17_over_100', g-b-R(17,100))
    pos('matching_radius_below_1p226e_minus7', R(1226,10**10)-eta)
    pos('physical_inverse_below_167', 167-A_actual)
    pos('extra_reflection_below_0p000203', R(203,10**6)-extra)
    require('reflection_bound_algebra', sp.cancel(extra-2*J*A*A*eta/(1-A*eta)) == 0)

    # Scalar semi-infinite tail is solved from its recurrence, both signs.
    surface_rows = []
    for q in (R(1,7), -R(1,8)):
        d = J*(q+1/q)
        G = q/J
        require('surface_endpoint_'+str(q), sp.cancel(d*G-J*q*G) == 1)
        require('surface_bulk_'+str(q), sp.cancel(d*q*G-J*G-J*q*q*G) == 0)
        F = -d+J*J*G
        require('outgoing_closed_match_'+str(q), sp.cancel(F+J/q) == 0)
        wrong_F = -d-J*J*G
        require('wrong_resolvent_sign_rejected_'+str(q), sp.cancel(wrong_F-F) != 0)
        surface_rows.append({'q': str(q), 'G': str(G), 'correct_F': str(F),
                             'wrong_sign_F_error': str(sp.cancel(wrong_F-F)),
                             'wrong_sign_endpoint_rhs': '-1'})
    evidence['countercases']['surface_resolvent_sign'] = surface_rows

    # A noncommuting closed-block resolvent test checks the order/sign algebra.
    # This finite toy is a discriminator, not a proof for the infinite tail.
    jt = R(1,5)
    Bt = sp.Matrix([[4, 1], [1, 5]])
    dBt = R(1,1000)*sp.Matrix([[2, 1], [1, -1]])
    require('resolvent_toy_noncommuting', Bt*dBt-dBt*Bt != sp.zeros(2))
    Ht = sp.kronecker_product(sp.Matrix([[2*jt,-jt],[-jt,2*jt]]),sp.eye(2))+sp.kronecker_product(sp.eye(2),Bt)-sp.eye(4)
    dHt = sp.kronecker_product(sp.eye(2), dBt)
    Rt, Rs = Ht.inv(), (Ht+dHt).inv()
    zero('noncommuting_resolvent_identity', Rs-Rt+Rs*dHt*Rt)
    E = sp.eye(4)[:, :2]
    zero('compressed_surface_resolvent_identity', E.T*(Rs-Rt)*E+E.T*Rs*dHt*Rt*E)
    require('opposite_resolvent_difference_sign_rejected', E.T*(Rs-Rt)*E-E.T*Rs*dHt*Rt*E != sp.zeros(2))

    # Shared site-1 RHS from exact extrapolation and row-zero boundary.
    z = (3+4*I)/5
    rr = 2-I
    rhs = J*(z-1/z)
    require('incident_extrapolation_identity', sp.cancel((1/z+rr*z)-z*(1+rr)-(1/z-z)) == 0)
    Mfree = sp.Matrix([[-J*(z+1/z), J], [J, -J/z]])
    xfree = sp.Matrix([z-z**3, 1-z**4])
    zero('site1_free_matching_with_shared_rhs', Mfree*xfree-sp.Matrix([0,rhs]))
    require('wrong_rhs_sign_rejected', Mfree*xfree+sp.Matrix([0,rhs]) != sp.zeros(2,1))
    r_site1 = -z**4
    r_abs = sp.cancel(r_site1/z**2)
    require('absolute_origin_free_reflection', sp.cancel(r_abs+z*z) == 0)
    require('omitted_origin_factor_rejected', sp.cancel(r_abs-r_site1) != 0)
    alpha = (5+12*I)/13
    zeta = -alpha/z**4
    require('nominal_common_phase_contract', sp.cancel((-z*z)*zeta-alpha/z**2) == 0)

    # A changed-M, same-RHS exact solve checks the resolvent-to-state identity.
    D0, D1 = sp.Matrix([[2,1],[1,4]]), sp.Matrix([[3,R(1,2)],[R(1,2),5]])
    Mt = D0.row_join(jt*sp.eye(2)).col_join((jt*sp.eye(2)).row_join(D1))
    d0 = sp.diag(R(1,1000), -R(1,2000))
    d1 = sp.Matrix([[R(1,4000),R(1,5000)],[R(1,5000),-R(1,6000)]])
    dM = sp.diag(d0,d1)
    shared_rhs = sp.Matrix([0,0,2*I*jt*R(4,5),0])
    xt, xs = Mt.inv()*shared_rhs, (Mt+dM).inv()*shared_rhs
    zero('matching_shared_rhs_solution_identity', xs-xt+(Mt+dM).inv()*dM*xt)
    zero('matching_perturbation_square_block_diagonal', dM.T*dM-sp.diag(d0.T*d0,d1.T*d1))

    # No eigenvector perturbation estimate is needed. For each fixed actual B,
    # the same root and bridge derivative bounds follow from the smaller gap.
    kappa = R(1,7)
    pos('root_modulus_gap_condition', 2+R(17,100)/J-(kappa+1/kappa))
    require('closed_root_derivative_ceiling', 2*kappa*kappa/(1-kappa*kappa) == R(1,24))
    inv24 = 2*167+1/J
    pos('Schur_inverse_below_368', 368-inv24)
    lm_factor_sq = 9+4/(1-kappa*kappa)**2
    # Independently chosen rational radical ceilings, rather than the author's
    # remainder-square X1 test.
    pos('sqrt2_below_99_over_70', R(99,70)**2-2)
    pos('sqrt5_below_56_over_25', R(56,25)**2-5)
    pos('LM_radical_below_3p63', R(363,100)**2-lm_factor_sq)
    lm_proxy = J*R(363,100)
    x0_proxy = R(99,70)*J*368
    x1_proxy = (R(56,25)*J+lm_proxy*16)*368
    pos('LM_below_0p11', R(11,100)-lm_proxy)
    pos('X0_below_16', 16-x0_proxy)
    pos('X1_below_700', 700-x1_proxy)
    C0sq = 2*(16+2)**2+16**2/(1-kappa*kappa)
    pos('C0_below_31', 31**2-C0sq)
    pos('C1_contact_radical_below_1982', 1982**2-(1400**2+1402**2))
    pos('tail_norm_radical_below_1p011', R(1011,1000)**2-1/(1-kappa*kappa))
    pos('tail_derivative_radical_below_1p05', R(21,20)**2-(1+kappa*kappa)/(1-kappa*kappa)**3)
    C1proxy = 1982+700*R(1011,1000)+16*R(1,24)*R(21,20)
    pos('C1_below_2700', 2700-C1proxy)
    pos('E2_over_v_below_5_over_2', R(5,2)-2*J*40)
    sigma = R(1,10**6)
    pos('F0_below_1_over_750', R(1,750)**2-15*sigma/9)
    pos('F1_below_2000', 2000**2-15/(4*sigma))
    pos('CB_below_2001', 2001-(2000+(700+R(5,2))/750))
    Dj = 2000*31+(2700+R(5,2)*31)/750
    pos('grouped_D_below_88000', 88000**2-2*Dj**2)

    # Directly sum positive physical block weights, then compare inherited
    # bounds; the previous certificate values do not generate these sums.
    Bbound = 3+params['DeltaA']+params['DeltaB']+2*params['h']+params['u']+2*params['gA']+2*params['gB']
    VA_norm = 2*params['lambdaA']+params['mu0']
    VB_norm = max(params['nu'], abs(2*params['lambdaB']-params['nu']))
    Vmax = max(VA_norm, VB_norm)
    require('B_bound_agrees_with_prior', Bbound == R(source['finite_horizon']['positive_block_B_upper']['rational']))
    require('V_bound_agrees_with_prior', Vmax == R(source['finite_horizon']['Vmax']['rational']))
    pos('actual_B_below_20', 20-Bbound-b)
    pos('actual_contact_norm_below_8', 8-Vmax-c)
    pos('full_scalar_removed_spectral_radius_below_18', 18-(R(19,2)+2*J+8))
    T, N, M, Tobs = 10**13, 22*10**12, 9*10**14, 4*10**13
    eta_p = R(1,1000)
    readiness_requirement = max(1,2*J*T,16*(2000+R(1,750))**2/(3*eta_p**2))
    pos('finite_ready_support_margin', N-2*J*T-readiness_requirement)
    dM_clock = M-N+1
    require('first_omitted_clock_distance', dM_clock == 878000000000001)
    pos('finite_clock_chebyshev_exponent_margin', dM_clock-18*Tobs*R(6,5)-9)
    require('prior_resource_parameters_unchanged', (source['packet']['T'],source['packet']['support_sites'],source['finite_horizon']['clock_sites'],source['finite_horizon']['Tobs']) == (T,N,M,Tobs))
    base_ready = R(296197282504763,27062500000000000)
    base_finite = R(323259782504763,27062500000000000)
    require('inherited_ready_exact_budget', base_ready == R(source['packet']['infinite_finite_preparation_isometry_upper']['rational']))
    require('inherited_finite_exact_budget', base_finite == R(source['finite_horizon']['complete_isometry_upper']['rational']))
    new_ready, new_finite = base_ready+extra, base_finite+extra
    pos('complete_ready_below_0p0112', R(112,10000)-new_ready)
    pos('complete_finite_below_0p0122', R(122,10000)-new_finite)
    pos('oldA_added_cap_two', 2-2*(params['gA']+a))
    pos('oldB_added_cap_two', 2-2*(params['gB']+a))
    load_weights = {'old1': {'gA': 2}, 'old2': {'gB': 2},
                    'sourceA': {'DeltaA':1,'h':2,'u':1,'gA':2,'lambdaA':2},
                    'sourceB': {'DeltaB':1,'h':2,'u':1,'gB':2,'lambdaB':2},
                    'c0': {'lambdaA':2,'mu0':1}, 'c1': {'lambdaB':2,'nu':1}}
    incident_changes = {site:a*sum(w.values()) for site,w in load_weights.items()}
    require('source_incident_radius_8a', incident_changes['sourceA'] == 8*a == incident_changes['sourceB'])
    require('contact_incident_radius_3a', incident_changes['c0'] == 3*a == incident_changes['c1'])

    # Excluded-case discriminator: even a positive arbitrarily small leakage
    # block destroys the *fixed* vacuum eigenchannel used by this proof.
    eps = R(1,10**12)
    Ptoy = sp.diag(1,0)
    Qtoy = sp.eye(2)-Ptoy
    leak = eps*sp.ones(2)
    zero('leakage_block_positive_polynomial', leak*leak-2*eps*leak)
    require('leakage_changes_fixed_open_subspace', Qtoy*leak*Ptoy != sp.zeros(2))
    evidence['countercases']['excluded_vacuum_leakage'] = {
        'base_B': [[1,0],[0,4]], 'positive_error': 'epsilon*[[1,1],[1,1]]',
        'epsilon': str(eps), 'operator_norm': str(2*eps),
        'Q_deltaB_P_nonzero_entry': str(eps),
        'meaning': 'Invalidates fixed open projector/shared incident-channel proof; not a counterexample inside the structural coefficient box.'}
    # An allowed nu error reaches opposite nominal phase at an arbitrarily late
    # odd multiple of pi/a. pi>3 proves this chosen time exceeds 2T.
    odd = 80001
    phase_time_lower = odd*3/a
    pos('phase_countercase_is_after_readiness', phase_time_lower-2*T)
    require('odd_multiple_nominal_phase_is_minus_one', sp.exp(-I*odd*sp.pi) == -1)
    evidence['countercases']['fixed_nominal_scalar'] = {
        'allowed_nu_error': str(a), 'time': f'{odd}*pi/a',
        'strict_time_lower': str(phase_time_lower), 'comparison_phase_distance': 2,
        'conditional_actual_output_distance_from_nominal_comparator_lower': str(2-R(112,10000)),
        'meaning': 'Exact comparator mismatch, plus triangle inequality conditional on the actual-scalar theorem; no dynamics simulated.'}

    evidence['derived_bounds'] = {name:record(value) for name,value in {
        'bulk_radius': b, 'contact_radius': c, 'closed_gap_remaining':g-b,
        'matching_radius':eta, 'physical_inverse':A_actual,
        'bridge_inverse':inv24, 'extra_reflection':extra,
        'LM_proxy':lm_proxy, 'X0_proxy':x0_proxy, 'X1_proxy':x1_proxy,
        'C1_proxy':C1proxy, 'D_each':Dj, 'ready_complete':new_ready,
        'finite_complete':new_finite, 'actual_B_upper':Bbound+b,
        'actual_contact_upper':Vmax+c}.items()}
    evidence['physical_coefficient_weights'] = weights
    evidence['incident_load_changes'] = {k:str(v) for k,v in incident_changes.items()}
    evidence['resources'] = {'historical_source_run_limits': {'cpu_cap_seconds':45,
            'external_wall_cap_seconds':60},
        'actual_combined_process_limits': {'cpu_cap_seconds':60,
            'external_wall_cap_seconds':60},
        'largest_matrix_dimension':16,'largest_inverse_dimension':4,
        'coefficient_grid_points':0,'time_evolution':False,'author_program_executed':False,
        'historical_point_state_or_reflection_recomputed':False,
        'clock_sites_allocated':0,'elapsed_seconds':time.monotonic()-started,
        'python':sys.version,'python_executable':sys.executable,
        'sympy':sp.__version__,'platform':platform.platform()}
    evidence['status'] = 'All declared exact algebra and strict comparisons completed; scope remains conditional.'
    return evidence
