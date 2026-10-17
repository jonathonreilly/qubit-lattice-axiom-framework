"""Portable weighted author/reviewer calculation bodies.

All mathematical statements remain in source order. File reads are mapped to
explicit frozen local bytes; original caps/identity fields are historical.
No calculation executes on import. Current review and execution status is
recorded in the paired publication packet; frozen source files remain unchanged."""

def run_weighted_author(inputs):
    """Exact author arithmetic for the proposed weighted emitter estimates.

The analytical integral bounds and provisional installed theorem need their
own separate checks. No matrix, quadrature, parameter search or dynamics runs.
"""
    from pathlib import Path
    from fractions import Fraction as F
    import datetime
    import hashlib
    import json
    import resource
    import time
    started = time.monotonic()
    for row in json.loads(inputs.read_text('weighted_author', 'SOURCE_PINS.json'))['files']:
        raw = inputs.read_bytes('weighted_author', row['snapshot'])
        assert len(raw) == row['bytes']
        assert hashlib.sha256(raw).hexdigest() == row['sha256']
    src = json.loads(inputs.read_text('weighted_author', 'inputs/INSTALLED_CERTIFICATE.json'))
    k = F(src['parameters']['coupling'])
    sigma = F(src['parameters']['half_width'])
    assert k == F(1, 10 ** 12) and sigma == F(1, 10 ** 6)
    v, d, F0 = (F(1, 40), F(61, 1000), F(1, 500))
    assert 560 * k * k < v / 2
    assert 8 / (19 * v) < 17
    assert 4 / (361 * v) < F(1, 2)
    assert 34 * sigma < 1
    xi = F(src['uniform_schur']['relative_resonant_denominator_error']['exact_rational'])
    delta = F(src['uniform_schur']['closed_tail_factor']['exact_rational'])
    spq, sqp = (2 * sigma * 206 * delta, delta * 206 * 2)
    inverse_rank_factor = (1 + 6 * k * k * spq) * (1 + 6 * k * k * sqp) / (1 - xi)
    assert inverse_rank_factor < 2
    a1 = 2 / sigma + 13
    f1 = a1 + 17 * d / k
    phase_weight = 2 * F0 + 48960 * k + 320 * d / k
    assert f1 < 2 / k
    assert f1 + F(5, 2) * F0 < 3 / k
    assert f1 + phase_weight + F(5, 2) * F0 < 23 / k
    assert 3 * d * 36 + 180 < 187
    assert 3 * d * 24 + 60 < 65
    assert 3 * d * 4 < 1
    assert 1 + 20000 * k < 2 and 36 * k < 1
    assert 374 * k + 18 * 10 ** 6 * k * k < 1
    assert 6 * 10 ** 6 * k * k < k
    Dj = 236 * a1 + 5518 + 544 * d / k + (6 * d + 1) / (k * k)
    assert Dj < F(3, 2) / (k * k)
    D = 3 / (k * k)
    assert 2 * Dj * Dj < D * D
    A0, B0 = (3 / k, 23 / k)
    T = 10 ** 36
    sqrt_lower = 27 * 10 ** 16
    assert sqrt_lower * sqrt_lower < 3 * v * T
    assert v * T > 1 and B0 / sqrt_lower < F(1, 2)
    escape = (A0 + B0) / sqrt_lower + D / (F(12, 5) * v * T)
    complete = F(3, 1000) + F(714, 10 ** 6) + escape
    assert escape < F(97, 10 ** 6)
    assert complete < F(4, 1000)
    Tobs, M = (2 * T, 5 * 10 ** 37)
    distance = M - src['parameters']['L'] - 1
    assert distance > 19 * Tobs * F(6, 5) + 9
    assert complete + F(1, 1000) < F(5, 1000)

    def scalar(q):
        return {'exact_rational': str(q), 'display_only_float': float(q)}
    out = {'scope': 'Author scalar checks only. Weighted integral proof and installed theorem remain provisional pending separate review.', 'weighted_constants': {key: scalar(value) for key, value in {'resonant_rank_factor': inverse_rank_factor, 'F1_upper': f1, 'weighted_phase_derivative_upper': phase_weight, 'localized_column_upper': Dj, 'grouped_D': D, 'A0': A0, 'B0': B0, 'escape_at_onset': escape, 'complete_isometry_at_onset': complete, 'finite_complete_isometry_upper': complete + F(1, 1000)}.items()}, 'time_and_clock': {'onset': T, 'Tobs': Tobs, 'M': M, 'first_omitted_distance': distance}, 'unchanged_comparator': 'Same f, rho, beta, zeta, actual scalar nu+2kappa and total old aging as the installed source.', 'limits': {'matrices': 0, 'quadrature': False, 'parameter_search': False, 'time_evolution': False, 'independent_review': False, 'historical_source_run_limits': {'cpu_cap_seconds': 5, 'wrapper_wall_cap_seconds': 10}, 'actual_shared_process_limits': inputs.shared_limits()}, 'elapsed_seconds': time.monotonic() - started}
    out['portable_execution'] = inputs.execution_metadata('weighted_author')
    return out

def run_weighted_reviewer(inputs):
    """Independent exact checks of a conditional weighted-integral refinement.

No author program is imported. No numerical integration, resonance grid,
installed physical inverse replay, parameter fit, or dynamics is performed.
The installed optical, regularity, seed and reflection claims are provisional
premises; this program checks the new manipulations of those premises.
"""
    from pathlib import Path
    import argparse
    import hashlib
    import json
    import platform
    import resource
    import sys
    import time
    start = time.monotonic()
    import sympy as s
    pins = json.loads(inputs.read_text('weighted_reviewer', 'SOURCE_PINS.json'))
    for row in pins['files']:
        data = inputs.read_bytes('weighted_reviewer', row['snapshot'])
        assert len(data) == row['bytes']
        assert hashlib.sha256(data).hexdigest() == row['sha256'], row['snapshot']
    prior = json.loads(inputs.read_text('weighted_reviewer', 'sources/author/inputs/INSTALLED_CERTIFICATE.json'))
    R = s.Rational
    I = s.I
    result = {'status': 'started', 'premise_status': 'Installed theorem is PROVISIONAL; this execution does not accept or recheck its physical inverse, optical, seed-overlap, or reflection certificates.', 'checks': {}, 'positive_exact_margins': {}, 'identities': {}, 'countercases': {}}

    def require(name, condition):
        assert bool(condition), name
        result['checks'][name] = True

    def identity(name, expression):
        simplified = s.simplify(expression)
        require(name, simplified == 0)

    def pos(name, value):
        value = s.cancel(value)
        require(name, value.is_Rational and value.p > 0 and (value.q > 0))
        result['positive_exact_margins'][name] = str(value)

    def zero_matrix(name, mat):
        require(name, mat.applyfunc(s.cancel) == s.zeros(*mat.shape))

    def positive_polynomial(name, expression, var):
        poly = s.Poly(s.expand(expression), var)
        for j, value in enumerate(poly.all_coeffs()):
            pos(name + '_coefficient_' + str(j), value)
        result['identities'][name] = str(poly.as_expr())

    def scalar(value):
        value = s.cancel(value)
        return {'exact': str(value), 'display_only_float': float(value)}
    k = R(1, 10 ** 12)
    sigma = R(1, 10 ** 6)
    v = R(1, 40)
    d = R(61, 1000)
    J = R('0.030021107107032')
    L = 12
    require('coupling_and_width_match_provisional_inputs', k == R(prior['parameters']['coupling']) and sigma == R(prior['parameters']['half_width']) and (L == prior['parameters']['L']))
    x = s.Symbol('x', real=True)
    h = s.Symbol('h', positive=True)
    A2 = s.atan(x / h) / h
    A3 = x / (h ** 2 * s.sqrt(x * x + h * h))
    identity('I2_antiderivative', s.diff(A2, x) - 1 / (x * x + h * h))
    identity('I3_antiderivative', s.diff(A3, x) - 1 / (x * x + h * h) ** R(3, 2))
    int2 = s.limit(A2, x, s.oo) - s.limit(A2, x, -s.oo)
    int3 = s.limit(A3, x, s.oo) - s.limit(A3, x, -s.oo)
    identity('I2_whole_line_value', int2 - s.pi / h)
    identity('I3_whole_line_value', int3 - 2 / h ** 2)
    result['identities']['whole_line_I2'] = str(int2)
    result['identities']['whole_line_I3'] = str(int3)
    pos('real_denominator_monotonicity_margin', v / 2 - 560 * k * k)
    i2_coefficient = 2 / v * 4 / 19
    i3_coefficient = 2 / v * 2 / 19 ** 2
    pos('I2_coefficient_below_17', 17 - i2_coefficient)
    pos('I3_coefficient_below_one_half', R(1, 2) - i3_coefficient)
    pos('Cauchy_Schwarz_I1_squared_margin', 1 - 2 * sigma * 17)
    identity('I3_linewidth_scaling', int3.subs(h, 19 * k * k) - R(2, 361) / k ** 4)
    t = s.Symbol('t', real=True)
    sig = s.Symbol('sig', positive=True)
    left = 2 * (t + sig) / sig
    right = 2 * (sig - t) / sig
    require('cutoff_left_zero_trace', left.subs(t, -sig) == 0)
    require('cutoff_right_zero_trace', right.subs(t, sig) == 0)
    require('cutoff_left_join_continuous', left.subs(t, -sig / 2) == 1)
    require('cutoff_right_join_continuous', right.subs(t, sig / 2) == 1)
    chi_variation = s.integrate(s.diff(left, t), (t, -sig, -sig / 2)) - s.integrate(s.diff(right, t), (t, sig / 2, sig))
    require('cutoff_total_variation_two', chi_variation == 2)
    chi, G, Dbar = [s.Function(n)(t) for n in ('chi', 'G', 'Dbar')]
    normalizer = s.Symbol('normalizer', positive=True)
    f_expr = k * chi * G / (normalizer * Dbar)
    f_derivative = k / normalizer * ((s.diff(chi, t) * G + chi * s.diff(G, t)) / Dbar - chi * G * s.diff(Dbar, t) / Dbar ** 2)
    identity('cutoff_and_quotient_derivative', s.diff(f_expr, t) - f_derivative)
    gmax = R(2)
    gprime = 2 * L + 2
    require('form_factor_derivative_bound_26', gprime == 26)
    a1 = 2 / sigma * gmax / 2 + R(gprime, 2)
    require('packet_a1', a1 == 2 / sigma + 13)
    require('packet_U_squared_coefficient', gmax * d / 2 == d)
    result['countercases']['cutoff_omission'] = {'test': 'Constant nonzero form factor and denominator; only chi varies.', 'actual_normalized_taper_variation': str(chi_variation), 'variation_if_cutoff_derivative_is_omitted': 0, 'meaning': 'Omitting the taper derivative fails even before resonance behavior is considered.'}
    Q = s.diag(*range(2, 9))
    for j in range(6):
        Q[j, j + 1] = R(1, 10)
        Q[j + 1, j] = I / 11
    brow = s.Matrix([[R(j + 1, 100) + I / 200 for j in range(7)]])
    ccol = s.Matrix([R(1, 200) - I * R(j + 1, 300) for j in range(7)])
    Qinv = Q.inv()
    ds = R(1, 10) + I / 100
    top = ds + (brow * Qinv * ccol)[0]
    De = s.Matrix([[top]]).row_join(brow).col_join(ccol.row_join(Q))
    column = s.Matrix([1]).col_join(-Qinv * ccol)
    row = s.Matrix([[1]]).row_join(-brow * Qinv)
    closed = s.diag(s.zeros(1), Qinv)
    rankterm = column * row / ds
    inv_formula = closed + rankterm
    zero_matrix('full_eight_coordinate_rank_one_inverse', De * inv_formula - s.eye(8))
    zero_matrix('rank_one_inverse_matches_direct_inverse', De.inv() - inv_formula)
    require('all_complementary_coordinates_present', len(brow) == 7 and len(ccol) == 7 and all((z != 0 for z in brow)) and all((z != 0 for z in ccol)))
    require('discarding_closed_summand_fails', (De * rankterm - s.eye(8)).applyfunc(s.cancel) != s.zeros(8))
    require('scalar_only_inverse_fails', (De * s.diag(1 / ds, *[0] * 7) - s.eye(8)).applyfunc(s.cancel) != s.zeros(8))
    result['countercases']['closed_inverse_omission'] = {'dimension': 8, 'complementary_coordinates': 7, 'rank_of_retained_resonant_term': 1, 'meaning': 'The rank-one resonant term alone is not an inverse of the eight-coordinate system; the closed summand is essential.'}
    zr = R(prior['parameters']['center_z_real'])
    zi = R(prior['parameters']['center_z_imag'])
    identity('exact_center_on_unit_circle', zr * zr + zi * zi - 1)
    r = R(1, 7)
    delta = (1 + r * r) * r ** (L - 1)
    bmin = 4 * zr * zi - 2 * sigma
    eta = 2 * sigma / bmin
    gamma0 = bmin * bmin / (4 * J)
    pos('reference_form_factor_lower', bmin - R(3, 2))
    pos('reference_optical_coefficient_lower', gamma0 - 19)
    spq = 2 * sigma * 206 * delta
    sqp = delta * 206 * 2
    xi = 2 * eta + k * k * spq * 6 * sqp / gamma0
    require('closed_tail_formula_matches_input', delta == R(prior['uniform_schur']['closed_tail_factor']['exact_rational']))
    require('reconstructed_xi_matches_input', xi == R(prior['uniform_schur']['relative_resonant_denominator_error']['exact_rational']))
    pos('xi_below_one', 1 - xi)
    u, w = (6 * k * k * spq, 6 * k * k * sqp)
    pos('rank_factor_below_two_cross_multiplied', 1 - 2 * xi - u - w - u * w)
    rank_factor = (1 + u) * (1 + w) / (1 - xi)
    ar, br, ap, bp = s.symbols('ar br ap bp', real=True)
    identity('unit_phase_derivative_Cauchy_identity', (ar * ar + br * br) * (ap * ap + bp * bp) - (ar * bp - br * ap) ** 2 - (ar * ap + br * bp) ** 2)
    phi = s.Symbol('phi', real=True)
    g_squared = 2 - 2 * s.cos(phi + 2 * t)
    identity('form_factor_modulus_squared_derivative', s.diff(g_squared, t) - 4 * s.sin(phi + 2 * t))
    nmax = 4 * 40
    nprime = 4 * 100 + 8 * 40
    require('n_derivative_constants', nmax == 160 and nprime == 720)
    moment = {1: 1 / k, 2: 17 / k ** 2, 3: R(1, 2) / k ** 4}
    F0 = R(1, 500)
    F1_upper = k * a1 * moment[1] + k * d * moment[2]
    phase_upper = 2 * F0 + 4 * k ** 3 * (nprime * moment[2] + nmax * d * moment[3])
    A0 = R(3) / k
    B0 = R(23) / k
    pos('F1_below_two_over_kappa', 2 / k - F1_upper)
    pos('incoming_A0_margin', A0 - F1_upper - R(5, 2) * F0)
    pos('outgoing_B0_margin', B0 - F1_upper - phase_upper - R(5, 2) * F0)
    U = s.Symbol('U', nonnegative=True)
    inverse_upper = 6 + 2 * U
    y_upper = k * 3 * inverse_upper
    yprime_raw = k * (3 * d * inverse_upper ** 2 + 30 * inverse_upper)
    yprime_upper = k * (187 + 65 * U + U * U)
    positive_polynomial('y_derivative_rounding', yprime_upper - yprime_raw, U)
    C_raw = 31 + (1 + 20000 * k) * y_upper
    C_upper = 32 + 12 * k * U
    positive_polynomial('complete_C_rounding', C_upper - C_raw, U)
    Cp_raw = 2700 + k * 10 ** 6 * y_upper + (1 + 20000 * k) * yprime_upper
    Cp_upper = 2701 + 131 * k * U + 2 * k * U * U
    positive_polynomial('complete_C_derivative_rounding', Cp_upper - Cp_raw, U)
    f_upper = k * U
    fp_upper = k * (a1 * U + d * U * U)
    integrand = s.Poly(s.expand(fp_upper * C_upper + f_upper * Cp_upper + R(5, 2) * f_upper * C_upper), U)
    require('weighted_integrand_has_no_constant_term', integrand.nth(0) == 0)
    require('weighted_integrand_degree_three', integrand.degree() == 3)
    coefficients = {n: s.cancel(integrand.nth(n)) for n in range(1, 4)}
    require('U_coefficient_complete', coefficients[1] == k * (32 * a1 + 2781))
    require('U2_coefficient_complete', coefficients[2] == k * k * (12 * a1 + 161) + 32 * k * d)
    require('U3_coefficient_complete', coefficients[3] == k * k * (12 * d + 2))
    Dj = s.cancel(sum((coefficients[n] * moment[n] for n in range(1, 4))))
    identity('weighted_column_bound_rearrangement', Dj - (236 * a1 + 5518 + 544 * d / k + (6 * d + 1) / k ** 2))
    pos('column_bound_below_1p5_over_kappa_squared', R(3, 2) / k ** 2 - Dj)
    Dgroup = 3 / k ** 2
    pos('within_parity_square_sum_ceiling', Dgroup ** 2 - 2 * Dj ** 2)
    result['identities']['weighted_product_coefficients'] = {str(n): str(coefficients[n]) for n in coefficients}
    result['countercases']['emitter_coordinate_omission'] = {'test': 'Clock correction zero and emitter correction a unit vector.', 'full_localized_norm': 1, 'clock_only_norm': 0, 'meaning': 'The separate y and y-prime terms must remain in the complete localized norm.'}
    amp = s.Function('amp')(t)
    energy = s.Function('energy')(t)
    tau = s.Symbol('tau', nonzero=True, real=True)
    ibp = s.diff(amp / s.diff(energy, t), t)
    identity('weighted_IBP_product_derivative', ibp - (s.diff(amp, t) / s.diff(energy, t) - amp * s.diff(energy, t, 2) / s.diff(energy, t) ** 2))
    epsilon = s.Symbol('epsilon', nonnegative=True)
    identity('positive_real_normalization_inequality_polynomial', 1 - epsilon ** 2 - (1 - epsilon) ** 2 - 2 * epsilon * (1 - epsilon))
    T = 10 ** 36
    sqrt_lower = 27 * 10 ** 16
    pos('square_root_denominator_lower', 3 * v * T - sqrt_lower ** 2)
    pos('sqrt_two_pi_lower_from_pi_above_three', 6 - R(12, 5) ** 2)
    pos('normalization_vT_above_one', v * T - 1)
    pos('normalization_outgoing_tail_below_half', R(1, 2) - B0 / sqrt_lower)
    escape = (A0 + B0) / sqrt_lower + Dgroup / (R(12, 5) * v * T)
    seed = R(3, 1000)
    reflection = R(714, 10 ** 6)
    require('seed_error_is_an_inherited_premise', seed == R(prior['common_seed']['chosen_seed_isometry_error_upper']))
    require('reflection_error_is_an_inherited_premise', reflection == R(prior['target']['chosen_augmented_phase_error_upper']))
    complete = seed + reflection + escape
    pos('escape_below_0p000097', R(97, 10 ** 6) - escape)
    pos('complete_below_0p004', R(4, 1000) - complete)
    Tobs = 2 * T
    M = 5 * 10 ** 37
    distance = M - (L + 2) + 1
    require('graph_distance_formula', distance == M - L - 1)
    pos('finite_clock_chebyshev_margin', distance - 19 * Tobs * R(6, 5) - 9)
    finite = complete + R(1, 1000)
    pos('finite_complete_below_0p005', R(5, 1000) - finite)
    result['derived_bounds'] = {name: scalar(value) for name, value in {'real_denominator_derivative_lower': v - 560 * k * k, 'I2_coefficient_pi_below_four': i2_coefficient, 'I3_coefficient': i3_coefficient, 'rank_one_factor': rank_factor, 'F1_upper': F1_upper, 'weighted_phase_upper': phase_upper, 'localized_column_upper': Dj, 'grouped_D': Dgroup, 'A0': A0, 'B0': B0, 'outgoing_tail_norm_upper_at_T': B0 / sqrt_lower, 'escape_at_T': escape, 'complete_at_T': complete, 'finite_complete': finite}.items()}
    result['time_and_distance'] = {'onset': T, 'observation_horizon': Tobs, 'clock_sites': M, 'first_omitted_distance': distance}
    result['resources'] = {'largest_matrix_dimension': 8, 'largest_inverse_dimension': 8, 'quadrature': False, 'resonance_samples': 0, 'time_evolution': False, 'author_program_imported_or_executed': False, 'installed_physical_inverse_recomputed': False, 'seed_overlap_recomputed': False, 'python': sys.version, 'sympy': s.__version__, 'python_executable': sys.executable, 'platform': platform.platform(), 'elapsed_seconds': time.monotonic() - start, 'historical_source_run_limits': {'cpu_cap_seconds': 45, 'external_wall_cap_seconds': 60}, 'actual_shared_process_limits': inputs.shared_limits()}
    result['status'] = 'Declared exact algebra and inequalities completed; all installed-system premises remain conditional.'
    result['portable_execution'] = inputs.execution_metadata('weighted_reviewer')
    return result
