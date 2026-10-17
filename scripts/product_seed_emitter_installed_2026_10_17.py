"""Portable installed author/reviewer calculation bodies.

All mathematical statements remain in source order. File reads are mapped to
explicit frozen local bytes; original caps/identity fields are historical.
No calculation executes on import. Current review and execution status is
recorded in the paired publication packet; frozen source files remain unchanged."""

def run_installed_author(inputs):
    """Analytic uniform Schur/envelope certificate, plus bounded algebra diagnostics.

Exact Fraction inequalities certify the interval. On-shell mpmath points only
check implementation/signs. They are not a nonsingularity grid certificate.
"""
    from fractions import Fraction as F
    from pathlib import Path
    import hashlib
    import json
    import platform
    import resource
    import sys
    import time
    started = time.monotonic()
    import sympy as sy
    import mpmath as mp
    mp.mp.dps = 90
    for row in json.loads(inputs.read_text('installed_author', 'SOURCE_MANIFEST.json'))['sources']:
        data = inputs.read_bytes('installed_author', row['snapshot_path'])
        assert len(data) == row['bytes'] and hashlib.sha256(data).hexdigest() == row['sha256']
    old = json.loads(inputs.read_text('installed_author', 'inputs/two_body_interval_bridge__CERTIFICATE.json'))
    par = {k: F(v) for k, v in old['exact_parameters'].items()}
    J, cs, sn, E0 = (par[k] for k in ['J', 'cos_k', 'sin_k', 'epsilon'])
    assert cs * cs + sn * sn == 1 and E0 == 2 * J * (1 - cs)
    L = 12
    coupling = F(1, 10 ** 12)
    sigma = F(1, 10 ** 6)
    v = F(1, 40)
    gap = F(9, 50)
    qr = F(1, 7)
    qprime = F(1, 24)
    assert old['matching']['chosen_M16_inverse_2_upper'] == 166
    assert old['matching']['X0'] == 16 and old['matching']['X1_and_L'] == 700
    assert F(old['interval']['chosen_closed_gap']) == gap
    assert F(old['interval']['kappa_upper']) == qr
    assert 2 * J * (sn - sigma) > v and 2 * coupling < E0
    assert 2 * J / v < F(5, 2) and 166 < 1 / (18 * coupling ** 2)
    sin2 = 2 * sn * cs
    amax = 2 * sigma
    bmin = 2 * sin2 - 2 * sigma
    bmax = F(2)
    eta = amax / bmin
    delta = (1 + qr * qr) * qr ** (L - 1)
    wclosed = 16 * (1 + qr * qr) * qr ** (L - 2)
    wclosed1 = (700 * (1 + qr * qr) + 16 * 2 * qr * qprime) * qr ** (L - 2)
    wclosed1 += 16 * (L - 2) * (1 + qr * qr) * qprime * qr ** (L - 3)
    assert delta < amax and bmin > F(3, 2)
    A0 = F(40)
    A1 = F(100)
    R0 = F(166)
    T0 = R0 + A0
    M16prime = 2 * J / (1 - qr * qr)
    R1 = R0 ** 2 * M16prime
    assert R1 < 1710 and R1 + A1 < 2000
    T1 = F(2000)
    assert 2 * J / v ** 2 < A1 and 2 * J / gap ** 2 < A1
    gamma0 = bmin * bmin / (4 * J)
    assert gamma0 > 19
    SigmaQQ = 2 * (1 + qr * qr) / gap + delta * delta * T0
    closed_lower = gap - coupling ** 2 * SigmaQQ
    assert closed_lower > F(1, 6)
    RQ = F(6)
    sigPQ = amax * T0 * delta
    sigQP = delta * T0 * bmax
    closed_schur = coupling ** 4 * sigPQ * RQ * sigQP
    xi_closed = closed_schur / (coupling ** 2 * gamma0)
    xi = 2 * eta + xi_closed
    schur_im_lower = coupling ** 2 * gamma0 * (1 - xi)
    assert schur_im_lower > 19 * coupling ** 2
    De_bound = (1 + coupling ** 2 * sigPQ * RQ) * (1 + coupling ** 2 * sigQP * RQ) / (19 * coupling ** 2) + RQ
    assert De_bound < 1 / (18 * coupling ** 2)
    aug_bound = (1 + R0 * coupling * bmax) * (1 + R0 * coupling * amax) / (18 * coupling ** 2)
    assert aug_bound < 1 / (17 * coupling ** 2)
    num_error = eta + coupling ** 2 * sigPQ * RQ * wclosed / bmin
    relative_seed = (num_error + xi) / (1 - xi)
    assert relative_seed < F(4, 10 ** 6)
    off_overlap = RQ * coupling * wclosed + RQ * coupling ** 2 * delta * T0 * bmax * (1 + relative_seed)
    assert off_overlap < F(1, 10 ** 18)
    inner = sigma / 2
    inner_eta = inner / (sin2 - inner)
    reference_mass_loss = 2 * coupling ** 2 / (v * inner) ** 2 + inner_eta ** 2
    assert reference_mass_loss < F(13, 10 ** 9)
    assert 1 - reference_mass_loss > F(99, 100) ** 2
    seed_distance_sq = 2 * (reference_mass_loss + relative_seed + off_overlap)
    assert seed_distance_sq < F(3, 1000) ** 2
    closed_reflection = RQ * coupling ** 2 * T0 * delta * wclosed
    closed_reflection += RQ * coupling ** 2 * delta ** 2 * T0 ** 2 * bmax * (1 + relative_seed) * (4 * J / bmin)
    phase_correction = 2 * eta + 2 * (1 + eta) * relative_seed + closed_reflection + 4 * eta ** 2
    assert phase_correction < F(11, 10 ** 6)
    gate_delta = F(176, 10 ** 15) + 702 * sigma
    aug_delta = gate_delta + phase_correction
    assert aug_delta < F(714, 10 ** 6)
    Sigmafree0 = 4 / v
    Sigmafree1 = 4 * A1 + 4 * A0
    XYprime = F(2 * L)
    Sigma1 = Sigmafree1 + XYprime * T0 * bmax + amax * T1 * bmax + amax * T0 * XYprime
    assert Sigma1 < 11000
    Ddiag1 = 2 * J + coupling ** 2 * (Sigmafree1 + XYprime * A0 * bmax + amax * A1 * bmax + amax * A0 * XYprime)
    Maug1 = max(M16prime, Ddiag1) + coupling * XYprime
    assert Maug1 < F(63, 1000)
    De1 = 2 * J + 11000 * coupling ** 2
    assert De1 < F(61, 1000)
    w0 = bmax + amax + wclosed
    w1 = 2 * L + 2 + 700 * amax + (L * amax + 2) + wclosed1
    assert w0 < 3 and w1 < 30
    y0 = F(1) / coupling
    y1 = F(1) / coupling ** 3
    assert coupling * (3 * De1 / (18 * coupling ** 2) ** 2 + 30 / (18 * coupling ** 2)) < y1
    assert 3 / (18 * coupling) < y0
    tail0 = 2 * A0 + T0 * bmax
    tail1 = 2 * A1 + 2 * A0 + (L + 1) * T0 * bmax + T1 * bmax + T0 * XYprime
    brow0 = tail0
    brow1 = (L + 2) * tail0 + tail1
    assert tail0 == 492 and tail1 == 14580 and (brow1 == 21468)
    contact1 = 2 * F(1710) + R0 * XYprime
    finite_row1 = 2 * A1 + 2 * L * A0 + L * T0 * bmax + T1 * bmax + T0 * XYprime
    assert finite_row1 < 16000
    K0 = R0 * bmax + 2 * brow0 + L * (tail0 + brow0) + tail0 * F(1011, 1000)
    K1 = contact1 + brow0 + 2 * brow1 + L * (16000 + (L + 1) * brow0 + brow1)
    K1 += tail1 * F(1011, 1000) + tail0 * qprime * F(21, 20)
    assert 1 / (1 - qr * qr) < F(1011, 1000) ** 2
    assert (1 + qr * qr) / (1 - qr * qr) ** 3 < F(21, 20) ** 2
    assert K0 < 20000 and K1 < 10 ** 6
    C0 = F(2 * 10 ** 12)
    C1 = F(2 * 10 ** 36)
    assert 31 + (1 + coupling * 20000) * y0 < C0
    assert 2700 + coupling * 10 ** 6 * y0 + (1 + coupling * 20000) * y1 < C1
    Laug = 1000 / coupling ** 2
    assert 700 + coupling * (brow1 * y0 + brow0 * y1) < Laug
    Df1 = 2 * J + coupling ** 2 * Sigmafree1
    assert Df1 < F(61, 1000)
    assert 2 / (19 * coupling) < y0
    assert (2 * L + 2) / (19 * coupling) + 2 * Df1 / (19 ** 2 * coupling ** 3) < y1
    F0 = F(1, 500)
    F1 = F(2 * 10 ** 30)
    assert 2 * sigma < F0 ** 2
    assert F(12, 5) * F(99, 100) > 2
    assert 1 / coupling + sigma / coupling ** 3 < F1
    tminus1 = F(720, 19) + 160 * Df1 / (19 ** 2 * coupling ** 2)
    assert tminus1 < 1 / coupling ** 2 and 4 * eta ** 2 < F(1, 4)
    Lrho = 5 / coupling ** 2
    assert 2 + 4 / coupling ** 2 < Lrho
    AA = BB = F(3 * 10 ** 30)
    assert F1 + F(5, 2) * F0 < AA
    assert F1 + (Lrho + F(5, 2)) * F0 < BB
    Dj = F1 * C0 + F0 * C1 + F(5, 2) * F0 * C0
    Dpacket = F(8 * 10 ** 42)
    assert Dj < 5 * 10 ** 42 and 2 * Dj ** 2 < Dpacket ** 2
    onset = 10 ** 72
    sqrt_lower = 27 * 10 ** 34
    assert sqrt_lower ** 2 < 3 * v * onset
    escape = (AA + BB) / sqrt_lower + Dpacket / (F(12, 5) * v * onset)
    assert BB / sqrt_lower < F(1, 2) and v * onset > 1
    joint = F(3, 1000) + F(714, 10 ** 6) + escape
    assert joint < F(4, 1000)
    Tobs = 2 * onset
    M = 5 * 10 ** 73
    dM = M - L - 1
    assert dM > 19 * Tobs * F(6, 5) + 9
    assert joint + F(1, 1000) < F(5, 1000)
    bound_state_op = 2 * coupling / (v * sigma)
    assert bound_state_op == F(8, 10 ** 5)

    def sq(x):
        return sy.Rational(x.numerator, x.denominator) if isinstance(x, F) else sy.Rational(x)

    def mpq(x):
        if isinstance(x, F):
            return mp.mpf(x.numerator) / x.denominator
        x = sy.Rational(x)
        return mp.mpf(int(x.p)) / int(x.q)

    def mm(a):
        return mp.matrix([[mpq(a[i, j]) for j in range(a.cols)] for i in range(a.rows)])

    def maxabs(a):
        return max((abs(vv) for vv in a))
    I2 = sy.eye(2)
    I4 = sy.eye(4)
    I8 = sy.eye(8)
    X = sy.Matrix([[0, 1], [1, 0]])
    Z = sy.diag(1, -1)
    nA = sy.diag(0, 0, 1, 1)
    nB = sy.diag(0, 1, 0, 1)
    hop = sy.zeros(4)
    hop[1, 2] = hop[2, 1] = 1
    gA, gB, h, la, lb, u, dA, dB, mu0, mu1 = (sq(par[k]) for k in ['gA', 'gB', 't', 'lambdaA', 'lambdaB', 'u', 'DeltaA', 'DeltaB', 'mu0', 'mu1'])
    XA = sy.kronecker_product(X, I2)
    XB = sy.kronecker_product(I2, X)
    VA = la * sy.kronecker_product(I4 + XA, I2) + mu0 * I8
    VB = lb * sy.kronecker_product(I4 + XB, I2) + mu1 * I8
    Cbare = dA * nA + dB * nB + h * (nA + nB - hop) + u * nA * nB
    K4 = 2 * I4 + sy.kronecker_product(Z, Z)
    Bfull = sy.kronecker_product(I4, K4) + sy.kronecker_product(Cbare, I4)
    Bfull += gA * sy.kronecker_product(nA, I4 + sy.kronecker_product(X, I2))
    Bfull += gB * sy.kronecker_product(nB, I4 + sy.kronecker_product(I2, X))
    Pfull = sy.kronecker_product(I4, sy.kronecker_product(X, X))
    assert Bfull == Bfull.T and Bfull * Pfull == Pfull * Bfull
    assert Bfull[:4, :4] == K4 and Bfull[4:, :4] == sy.zeros(12, 4)
    qt = sy.Rational(3, 5)
    jt = sy.Integer(1)
    et = sy.Rational(1, 7)
    kt = sy.Rational(1, 10)
    pt = sy.Rational(3, 5) + sy.I * sy.Rational(4, 5)
    lamt = 2 - qt - 1 / qt
    vt0 = sy.Rational(1, 3)
    vt1 = -sy.Rational(1, 4)
    nt = L + 4
    emitter = nt - 1
    full = sy.zeros(nt)
    for n in range(L + 3):
        full[n, n] = lamt - 2
    full[0, 0] -= vt0
    full[1, 1] -= vt1
    full[L + 2, L + 2] += qt
    for n in range(L + 2):
        full[n, n + 1] = full[n + 1, n] = 1
    full[emitter, emitter] = lamt - et
    full[L, emitter] = full[emitter, L] = -kt
    full[L + 2, emitter] = kt * pt
    full[emitter, L + 2] = kt * sy.conjugate(pt)
    keep = [0, 1, emitter]
    elim = list(range(2, L + 3))
    direct = full.extract(keep, keep) - full.extract(keep, elim) * full.extract(elim, elim).inv() * full.extract(elim, keep)
    at = 1 / (qt - 1 / qt)
    xt = qt ** (L - 1) * (1 - sy.conjugate(pt) * qt ** 2)
    yt = qt ** (L - 1) * (1 - pt * qt ** 2)
    st = at * (2 - (pt + sy.conjugate(pt)) * qt ** 2)
    mt = sy.Matrix([[lamt - 2 - vt0, 1], [1, -1 / qt - vt1]])
    pred = sy.zeros(3)
    pred[:2, :2] = mt
    pred[1, 2] = -kt * yt
    pred[2, 1] = -kt * xt
    pred[2, 2] = lamt - et - kt ** 2 * (st - xt * at * yt)
    assert (direct - pred).applyfunc(sy.simplify) == sy.zeros(3)
    scalar_schur = pred[2, 2] - (pred[2, :2] * mt.inv() * pred[:2, 2])[0]
    assert sy.simplify(scalar_schur - (lamt - et - kt ** 2 * (st + xt * (mt.inv()[1, 1] - at) * yt))) == 0
    jm = mpq(J)
    km = mpq(coupling)
    e0m = mpq(E0)
    z0 = mpq(cs) + mp.j * mpq(sn)
    phase = z0 * z0
    vAm, vBm = (mm(VA), mm(VB))
    diagnostics = []
    for p in [1, -1]:
        C = (dA + gA) * nA + (dB + gB) * nB + h * (nA + nB - hop) + u * nA * nB
        G = gA * nA + p * gB * nB
        B = sy.kronecker_product(I4, 2 * I2 + Z) + sy.kronecker_product(C, I2) + sy.kronecker_product(G, X)
        Uold = sy.Matrix([[1, 0], [0, p], [0, 1], [p, 0]])
        U = sy.kronecker_product(I4, Uold)
        assert U.T * U == 2 * I8 and U.T * Bfull * U == 2 * B
        bm = mm(B)
        eig, ev = mp.eigsy(mm(B[2:, 2:]))
        for spin in [1, -1]:
            inc = 0 if spin == 1 else 1
            for shift in [-sigma, F(0), sigma]:
                z = z0 * mp.exp(mp.j * mpq(shift))
                cosk = mp.re(z)
                sink = mp.im(z)
                lam = 2 + spin + 2 * jm * (1 - cosk)
                vg = 2 * jm * sink
                Q = mp.zeros(8)
                A = mp.zeros(8)
                for idx in [0, 1]:
                    if idx == inc:
                        q = z
                    else:
                        dd = (2 * jm + (3 if idx == 0 else 1) - lam) / jm
                        q = (dd - mp.sign(dd) * mp.sqrt(dd * dd - 4)) / 2
                    Q[idx, idx] = q
                    A[idx, idx] = 1 / (jm * (q - 1 / q))
                qs = []
                aas = []
                for ee in eig:
                    dd = (2 * jm + ee - lam) / jm
                    q = (dd - mp.sign(dd) * mp.sqrt(dd * dd - 4)) / 2
                    qs.append(q)
                    aas.append(1 / (jm * (q - 1 / q)))
                Q[2:, 2:] = ev * mp.diag(qs) * ev.T
                A[2:, 2:] = ev * mp.diag(aas) * ev.T
                M16 = mp.zeros(16)
                M16[:8, :8] = (lam - 2 * jm) * mp.eye(8) - bm - vAm
                M16[:8, 8:] = jm * mp.eye(8)
                M16[8:, :8] = jm * mp.eye(8)
                M16[8:, 8:] = -jm * Q ** (-1) - vBm
                R = M16 ** (-1)
                T = R[8:, 8:] - A
                XX = Q ** (L - 1) * (mp.eye(8) - mp.conj(phase) * Q ** 2)
                YY = Q ** (L - 1) * (mp.eye(8) - phase * Q ** 2)
                Sfree = A * (2 * mp.eye(8) - (phase + mp.conj(phase)) * Q ** 2)
                DD = (lam - e0m) * mp.eye(8) - bm - km ** 2 * (Sfree + XX * T * YY)
                aug = mp.zeros(24)
                aug[:16, :16] = M16
                aug[8:16, 16:24] = -km * YY
                aug[16:24, 8:16] = -km * XX
                aug[16:24, 16:24] = (lam - e0m) * mp.eye(8) - bm - km ** 2 * (Sfree - XX * A * YY)
                inv = aug ** (-1)
                dinv = DD ** (-1)
                residual = maxabs(aug * inv - mp.eye(24))
                schur_match = maxabs(inv[16:, 16:] - dinv) / max(1, maxabs(dinv))
                assert residual < mp.mpf('1e-50') and schur_match < mp.mpf('1e-50')
                rhs = mp.zeros(16, 1)
                rhs[8 + inc] = 2 * mp.j * jm * sink / z
                contact = R * rhs
                x1 = contact[8:16, 0]
                rg = x1[inc] / z - 1 / z ** 2
                tpp_error = abs(T[inc, inc] - A[inc, inc] * z * z * rg)
                assert tpp_error < mp.mpf('1e-50')
                unit = mp.zeros(8, 1)
                unit[inc] = 1
                closedx = mp.matrix(x1)
                closedx[inc] = 0
                phiL = (z ** (-L) + rg * z ** L) * unit + Q ** (L - 1) * closedx
                phiL2 = (z ** (-L - 2) + rg * z ** (L + 2)) * unit + Q ** (L + 1) * closedx
                w = phiL - mp.conj(phase) * phiL2
                ye = km * dinv * w
                gp = z ** (-L) * (1 - phase / z ** 2)
                gm = z ** L * (1 - phase * z ** 2)
                df = 2 * jm * (1 - cosk) - e0m - km ** 2 * Sfree[inc, inc]
                yr = km * mp.conj(gm) / df
                rel = abs(ye[inc] / yr - 1)
                tail = A * (Q ** 2 - phase * mp.eye(8)) + Q ** (L + 1) * T * YY
                raug = rg + km * z ** (-L - 2) * (tail * ye)[inc]
                flux = abs(abs(raug) ** 2 - 1)
                assert rel < mpq(relative_seed) and flux < mp.mpf('1e-50')
                diagnostics.append({'p': p, 's': spin, 'shift_exact': str(shift), 'augmented_inverse_max_entry_display': mp.nstr(maxabs(inv), 25), 'inverse_residual_max_entry_display': mp.nstr(residual, 8), 'schur_inverse_relative_difference_display': mp.nstr(schur_match, 8), 'open_T_reflection_identity_error_display': mp.nstr(tpp_error, 8), 'open_emitter_relative_profile_error_display': mp.nstr(rel, 20), 'augmented_flux_error_display': mp.nstr(flux, 8)})

    def pack(x):
        return {'exact_rational': str(x), 'display_float': float(x)}
    report = {'status': 'new conditional author certificate, not independent review or native-hardware validation', 'parameters': {'L': L, 'coupling': str(coupling), 'half_width': str(sigma), 'center_z_real': str(cs), 'center_z_imag': str(sn), 'E0': str(E0), 'old_source_dimension': 16, 'parity_dimension': 8, 'closed_coordinates_per_parity': 7}, 'uniform_schur': {'closed_tail_factor': pack(delta), 'closed_drive_norm': pack(wclosed), 'closed_emitter_inverse_upper': 6, 'free_optical_lower_after_dividing_by_coupling_squared': pack(gamma0), 'relative_resonant_denominator_error': pack(xi), 'resonant_imaginary_lower': '19 coupling^2', 'De_inverse_2_upper': '1/(18 coupling^2)', 'augmented_matching_inverse_2_upper': '1/(17 coupling^2)', 'augmented_matching_dimension_per_parity': 24, 'full_dimension': 48, 'augmented_matching_derivative_2_upper': '63/1000', 'all_in_band_bound_states_excluded': True, 'why': 'original matching invertible, finite augmented Schur invertible, and homogeneous outgoing tail matching'}, 'common_seed': {'profile': 'yref= coupling conjugate(g_minus translated)/Df', 'envelope': 'f=chi conjugate(yref)/(sqrt(2pi) N); chi=1 on inner half-band, linear to zero at endpoints; N^2=integral chi^2 |yref|^2/(2pi)', 'normalization_mass_loss_upper': pack(reference_mass_loss), 'relative_diagonal_profile_error': pack(relative_seed), 'off_diagonal_overlap_error': pack(off_overlap), 'seed_isometry_error_squared_upper': pack(seed_distance_sq), 'chosen_seed_isometry_error_upper': '3/1000', 'bound_state_operator_amplitude_upper': str(bound_state_op)}, 'target': {'same_fixed_gate_scalar': 'zeta from frozen interval candidate; no refitting', 'common_outgoing_phase': 'rho(k)=r0(k) t_minus(k)/|t_minus(k)|', 'physical_scalar': 'exp(-i (nu+2 coupling) t)', 'old_aging': 'exp(-i t K) for total time since product seed', 'emitter_reflection_phase_correction': pack(phase_correction), 'original_gate_band_error': pack(gate_delta), 'augmented_phase_error': pack(aug_delta), 'chosen_augmented_phase_error_upper': '714/1000000'}, 'regularity': {'C0': str(C0), 'C1': str(C1), 'R_aug_derivative_upper': str(Laug), 'rho_derivative_upper': str(Lrho), 'F0': str(F0), 'F1': str(F1), 'CA': str(AA), 'CB': str(BB), 'Dj': pack(Dj), 'grouped_D': str(Dpacket), 'clock_resolvent_localized_map_K0': 20000, 'K1': 1000000}, 'conditional_complete_output': {'onset': onset, 'all_future_infinite_clock': True, 'escape_bound': pack(escape), 'complete_isometry_error': pack(joint), 'strict_ceiling': '4/1000', 'unhalved_trace_strict_ceiling': '8/1000', 'finite_horizon': Tobs, 'finite_clock_sites': M, 'first_omitted_site_distance': dM, 'finite_boundary_tolerance': '1/1000', 'finite_complete_isometry_strict_ceiling': '5/1000', 'time_source': 'integration by parts with explicit uniform constants; not a linewidth or exponential-decay inference'}, 'distinct_exact_algebra': {'direct_scalar_tail_elimination_equals_augmented_matching': True, 'scalar_geometry_dimension': nt, 'contact_to_emitter_signs_checked': True, 'all_16_internal_B_and_parity_identities_checked': True}, 'physical_point_diagnostics_not_interval_proof': diagnostics, 'limits': ['supplied clean clock/source vacuum and excited seed', 'static complex loop couplings are an explicit additional physical permission', 'no practical size or time claim', 'no arbitrary exact fit family', 'new packet implication and Schur argument require independent review'], 'runtime': {'python': sys.version, 'executable': sys.executable, 'sympy': sy.__version__, 'mpmath': mp.__version__, 'mpmath_dps': mp.mp.dps, 'platform': platform.platform(), 'elapsed_seconds': time.monotonic() - started, 'largest_executed_matrix_dimension': 24, 'equivalent_full_two_parity_matching_dimension': 48, 'on_shell_diagnostic_points': 3, 'sectors_per_point': 4, 'optimizers': 0, 'time_evolution_simulations': 0, 'historical_source_run_limits': {'cpu_cap_seconds': 30, 'wall_cap_seconds': 60}, 'actual_shared_process_limits': inputs.shared_limits()}, 'historical_source_program_sha256': hashlib.sha256(inputs.original_program_bytes('installed_author')).hexdigest()}
    report['portable_execution'] = inputs.execution_metadata('installed_author')
    return report

def run_installed_reviewer(inputs):
    """Independent exact noncommuting-tail and conservative-bound checks.

No author code is imported or executed. The small model contains one open
and one closed channel, noncommuting real contact matrices, and complex loop
bonds. Its direct finite outgoing problem is the source of the comparisons.
The physical interval bounds are independently enclosed by looser rational
ceilings; no momentum sampling is used as an interval certificate.
"""
    import json
    import resource
    import sys
    import time
    from fractions import Fraction as F
    from pathlib import Path
    START = time.monotonic()
    import sympy as s

    def simp(x):
        return s.cancel(s.expand_complex(x))

    def cleaned(m):
        return m.applyfunc(simp)

    def exact_zero(m):
        return cleaned(m) == s.zeros(*m.shape)

    def serial(m):
        return [[str(simp(m[i, j])) for j in range(m.cols)] for i in range(m.rows)]

    def first_nonzero(m):
        for i in range(m.rows):
            for j in range(m.cols):
                x = simp(m[i, j])
                if x != 0:
                    return {'row': i, 'column': j, 'value': str(x)}
        raise AssertionError('Discriminator did not distinguish the wrong expression')

    def rat(x):
        return {'exact': str(x), 'approximate_display': float(x)}
    R = s.Rational
    ii = s.I
    eye = s.eye(2)
    J = s.Integer(1)
    z = (3 + 4 * ii) / 5
    q = R(1, 7)
    phase = (5 + 12 * ii) / 13
    coupling = R(1, 13)
    E0toy = R(1, 7)
    energy = R(4, 5)
    bulk = s.diag(0, R(208, 35))
    Q = s.diag(z, q)
    A = (J * (Q - Q.inv())).inv()
    assert exact_zero((energy - 2 * J) * eye - bulk + J * (Q + Q.inv()))
    V0 = s.Matrix([[R(1, 3), R(1, 5)], [R(1, 5), -R(2, 7)]])
    V1 = s.Matrix([[R(1, 4), -R(1, 6)], [-R(1, 6), R(2, 9)]])
    assert not exact_zero(V0 * bulk - bulk * V0)
    assert not exact_zero(V1 * bulk - bulk * V1)
    L = 3
    last = 5
    size = 2 * (last + 1)
    clock = s.zeros(size)
    for n in range(last + 1):
        clock[2 * n:2 * n + 2, 2 * n:2 * n + 2] = (energy - 2 * J) * eye - bulk
        if n < last:
            clock[2 * n:2 * n + 2, 2 * n + 2:2 * n + 4] = J * eye
            clock[2 * n + 2:2 * n + 4, 2 * n:2 * n + 2] = J * eye
    clock[:2, :2] -= V0
    clock[2:4, 2:4] -= V1
    clock[-2:, -2:] += J * Q
    green = cleaned(clock.inv(method='DM'))
    assert exact_zero(clock * green - s.eye(size))
    small = s.zeros(4)
    small[:2, :2] = (energy - 2 * J) * eye - bulk - V0
    small[:2, 2:] = J * eye
    small[2:, :2] = J * eye
    small[2:, 2:] = -J * Q.inv() - V1
    small_inv = cleaned(small.inv(method='DM'))
    T = cleaned(small_inv[2:, 2:] - A)
    assert not exact_zero(T * Q - Q * T)
    gluing_pairs = []
    for n in range(2, last + 1):
        for m in range(2, last + 1):
            prediction = A * Q ** abs(n - m) + Q ** (n - 1) * T * Q ** (m - 1)
            assert exact_zero(green[2 * n:2 * n + 2, 2 * m:2 * m + 2] - prediction)
            gluing_pairs.append([n, m])
    wrong_order = A * Q ** 2 + T * Q ** 4
    wrong_order_residual = green[4:6, 8:10] - wrong_order
    V = s.zeros(size, 2)
    V[2 * L:2 * L + 2, :] = eye
    V[2 * (L + 2):2 * (L + 2) + 2, :] = -phase * eye
    X = Q ** (L - 1) * (eye - s.conjugate(phase) * Q ** 2)
    Y = Q ** (L - 1) * (eye - phase * Q ** 2)
    sigma_direct = cleaned(V.H * green * V)
    sigma_free = cleaned(A * (2 * eye - (phase + s.conjugate(phase)) * Q ** 2))
    assert exact_zero(sigma_direct - (sigma_free + X * T * Y))
    wrong_sigma_residual = sigma_direct - (sigma_free + Y * T * X)
    whole = s.zeros(size + 2)
    whole[:size, :size] = clock
    whole[:size, size:] = -coupling * V
    whole[size:, :size] = -coupling * V.H
    whole[size:, size:] = (energy - E0toy) * eye - bulk
    keep = list(range(4)) + list(range(size, size + 2))
    remove = list(range(4, size))
    direct_aug = cleaned(whole.extract(keep, keep) - whole.extract(keep, remove) * whole.extract(remove, remove).inv(method='DM') * whole.extract(remove, keep))
    aug = s.zeros(6)
    aug[:4, :4] = small
    aug[2:4, 4:6] = -coupling * Y
    aug[4:6, 2:4] = -coupling * X
    aug[4:6, 4:6] = (energy - E0toy) * eye - bulk - coupling ** 2 * (sigma_free - X * A * Y)
    assert exact_zero(direct_aug - aug)
    de_direct = cleaned(direct_aug[4:, 4:] - direct_aug[4:, :4] * small_inv * direct_aug[:4, 4:])
    assert exact_zero(de_direct - ((energy - E0toy) * eye - bulk - coupling ** 2 * sigma_direct))
    wrong_aug = aug.copy()
    wrong_aug[4:6, 2:4] *= -1
    rhs = s.zeros(size, 1)
    rhs[-2, 0] = J * (z - z ** (-1)) * z ** (-last)
    background = cleaned(green * rhs)
    rbg = simp((background[-2, 0] - z ** (-last)) / z ** last)
    assert simp(rbg * s.conjugate(rbg) - 1) == 0
    assert simp(T[0, 0] - A[0, 0] * z * z * rbg) == 0
    rhs_all = s.zeros(size + 2, 1)
    rhs_all[:size, :] = rhs
    solution = cleaned(whole.inv(method='DM') * rhs_all)
    drive = cleaned(V.H * background)
    ye = cleaned(coupling * de_direct.inv(method='DM') * drive)
    assert exact_zero(solution[-2:, :] - ye)
    assert exact_zero(solution[:size, :] - (background + coupling * green * V * ye))
    raug = simp((solution[-4, 0] - z ** (-last)) / z ** last)
    assert simp(raug * s.conjugate(raug) - 1) == 0
    dtail = A * (Q ** 2 - phase * eye) + Q ** (L + 1) * T * Y
    brow = z ** (-L - 2) * dtail[0, :]
    assert simp(raug - rbg - coupling * (brow * ye)[0]) == 0
    gp = z ** (-L) * (1 - phase * z ** (-2))
    gm = z ** L * (1 - phase * z ** 2)
    assert simp(brow[0] - A[0, 0] * (gp + rbg * gm)) == 0
    assert simp(drive[0] - s.conjugate(gm) - rbg * s.conjugate(gp)) == 0
    assert drive[1] != 0 and ye[1] != 0
    kernel = A[0, 0] * s.Matrix([[1, z * z], [z * z, 1]])
    vlocal = s.Matrix([1, -phase])
    sf = simp((vlocal.H * kernel * vlocal)[0])
    df = simp(energy - E0toy - coupling ** 2 * sf)
    speed = J * (z - z ** (-1)) / ii
    aa = simp(gp * s.conjugate(gp))
    bb = simp(gm * s.conjugate(gm))
    jump_dk_times_pi = simp(-s.im(1 / df) * speed)
    weights_dk_times_pi = simp(coupling ** 2 * (aa + bb) / (2 * df * s.conjugate(df)))
    assert simp(jump_dk_times_pi - weights_dk_times_pi) == 0
    wrong_density = simp(-s.im(1 / df) - weights_dk_times_pi)
    assert wrong_density != 0
    seed = s.eye(4)[:, :2]
    rot = s.Matrix([[R(3, 5), R(4, 5)], [-R(4, 5), R(3, 5)]])
    unitary = (5 + 12 * ii) / 13 * rot
    packet = s.zeros(4, 2)
    packet[:2, :] = R(12, 13) * unitary
    packet[2:, :] = R(5, 13) * eye
    assert exact_zero(packet.H * packet - eye)
    overlap = cleaned(seed.H * packet)
    error_gram = cleaned((seed - packet).H * (seed - packet))
    assert exact_zero(error_gram - (2 * eye - overlap - overlap.H))
    error_eigenvalues = sorted(error_gram.eigenvals().keys())
    diagonal_only = error_gram[0, 0]
    assert error_eigenvalues[-1] > diagonal_only
    off = s.Matrix([[0, R(3, 1000) + ii * R(4, 1000)], [R(5, 2000) - ii * R(12, 2000), 0]])
    assert exact_zero(off.H * off - s.diag(R(169, 4000000), R(25, 1000000)))
    aligned = s.Matrix([[1, 1]])
    assert (aligned * aligned.H)[0] == 2
    j = F('0.030021107107032')
    center_q = F('4.510351185997098')
    cs = (center_q ** 2 - 1) / (center_q ** 2 + 1)
    sn = 2 * center_q / (center_q ** 2 + 1)
    sin2 = 2 * cs * sn
    k = F(1, 10 ** 12)
    width = F(1, 10 ** 6)
    v = F(1, 40)
    gap = F(9, 50)
    r = F(1, 7)
    assert cs * cs + sn * sn == 1
    assert 2 * j * (sn - width) > v and 2 * k < 2 * j * (1 - cs)
    eta = F(131, 10 ** 8)
    delta = F(52, 10 ** 11)
    wc = F(58, 10 ** 9)
    assert width / (sin2 - width) < eta
    assert (1 + r * r) * r ** 11 < delta
    assert 16 * (1 + r * r) * r ** 10 < wc
    assert sin2 > F(3, 4)
    gamma = F(977, 50)
    assert (2 * sin2 - 2 * width) ** 2 / (4 * j) > gamma
    Sclosed = 2 * (1 + r * r) / gap + delta * delta * 206
    assert gap - k * k * Sclosed > F(1, 6)
    pq, qp = (2 * width * 206 * delta, delta * 206 * 2)
    xi = F(263, 10 ** 8)
    assert 2 * eta + k * k * pq * 6 * qp / gamma < xi
    assert gamma * (1 - xi) > 19
    de_bound = (1 + k * k * pq * 6) * (1 + k * k * qp * 6) / (19 * k * k) + 6
    aug_bound = (1 + 166 * k * 2) * (1 + 166 * k * 2 * width) / (18 * k * k)
    assert de_bound < 1 / (18 * k * k) and aug_bound < 1 / (17 * k * k)
    eta_profile = F(3941, 10 ** 9)
    assert (eta + k * k * pq * 6 * wc / F(3, 2) + xi) / (1 - xi) < eta_profile
    off_bound = F(35, 10 ** 20)
    assert 6 * k * wc + 6 * k * k * delta * 206 * 2 * (1 + eta_profile) < off_bound
    mass_bound = F(13, 10 ** 9)
    h = width / 2
    assert 2 * k * k / (v * h) ** 2 + (h / (F(3, 4) - h)) ** 2 < mass_bound
    seed_sq_bound = 2 * (mass_bound + eta_profile + off_bound)
    assert seed_sq_bound < F(3, 1000) ** 2
    eps_closed = 6 * k * k * 206 * delta * wc + 6 * k * k * delta ** 2 * 206 ** 2 * 2 * (1 + eta_profile) * 4 * j / F(3, 2)
    phase_bound = 2 * eta + 2 * (1 + eta) * eta_profile + eps_closed + 4 * eta ** 2
    assert phase_bound < F(11, 10 ** 6)
    assert F(176, 10 ** 15) + 702 * width + F(11, 10 ** 6) < F(714, 10 ** 6)
    assert 2 * j / (1 - r * r) < F(62, 1000)
    assert 166 ** 2 * F(62, 1000) < 1710
    assert 2 * j / v ** 2 < 100 and 2 * j / gap ** 2 < 100
    sigma_prime = 560 + 24 * 206 * 2 + 2 * width * 2000 * 2 + 2 * width * 206 * 24
    assert sigma_prime < 11000
    assert 2 * j + 11000 * k * k < F(61, 1000)
    diag_prime = 2 * j + k * k * (560 + 24 * 40 * 2 + 2 * width * 100 * 2 + 2 * width * 40 * 24)
    assert max(F(62, 1000), diag_prime) + 24 * k < F(63, 1000)
    assert k * (3 * F(61, 1000) / (18 * k * k) ** 2 + 30 / (18 * k * k)) < k ** (-3)
    wc_prime = (700 * (1 + r * r) + 32 * r / F(24)) * r ** 10 + 16 * 10 * (1 + r * r) * r ** 9 / F(24)
    assert 26 + 700 * 2 * width + (12 * 2 * width + 2) + wc_prime < 30
    assert 1 / (1 - r * r) < F(1011, 1000) ** 2
    assert (1 + r * r) / (1 - r * r) ** 3 < F(21, 20) ** 2
    K0 = 332 + 2 * 492 + 12 * (492 + 492) + 492 * F(1011, 1000)
    K1 = 7404 + 492 + 2 * 21468 + 12 * (16000 + 13 * 492 + 21468) + 14580 * F(1011, 1000) + 492 * F(1, 24) * F(21, 20)
    assert K0 < 20000 and K1 < 10 ** 6
    assert 31 + (1 + 20000 * k) / k < 2 * 10 ** 12
    assert 2700 + 10 ** 6 + (1 + 20000 * k) / k ** 3 < 2 * 10 ** 36
    assert 700 + 21468 + 492 / k ** 2 < 1000 / k ** 2
    assert 26 / (19 * k) + 2 * F(61, 1000) / (19 ** 2 * k ** 3) < 1 / k ** 3
    assert 2 * width < F(1, 500) ** 2
    assert F(12, 5) * F(99, 100) > 2
    assert 1 / k + width / k ** 3 < 2 * 10 ** 30
    assert F(720, 19) + 160 * F(61, 1000) / (19 ** 2 * k ** 2) < 1 / k ** 2
    assert 2 + 4 / k ** 2 < 5 / k ** 2
    F0, F1 = (F(1, 500), F(2 * 10 ** 30))
    assert F1 + F(5, 2) * F0 < 3 * 10 ** 30
    assert F1 + (5 / k ** 2 + F(5, 2)) * F0 < 3 * 10 ** 30
    Dj = F1 * 2 * 10 ** 12 + F0 * 2 * 10 ** 36 + F(5, 2) * F0 * 2 * 10 ** 12
    assert Dj < 5 * 10 ** 42 and 2 * Dj ** 2 < (8 * 10 ** 42) ** 2
    onset = 10 ** 72
    root_floor = 27 * 10 ** 34
    assert root_floor ** 2 < 3 * v * onset
    escape = F(6 * 10 ** 30, root_floor) + F(8 * 10 ** 42) / (F(12, 5) * v * onset)
    joint = F(3, 1000) + F(714, 10 ** 6) + escape
    assert joint < F(4, 1000)
    assert F(3 * 10 ** 30, root_floor) < F(1, 2)
    M = 5 * 10 ** 73
    distance = M - 12 - 1
    horizon_margin = distance - 19 * (2 * onset) * F(6, 5) - 9
    assert horizon_margin > 0
    assert joint + F(1, 1000) < F(5, 1000)
    assert 2 * k / (v * width) == F(1, 12500)
    result = {'scope': 'New exact model and independent conservative inequalities; no author-code replay or physical momentum sampling', 'small_model': {'internal_dimension': 2, 'open_channels': 1, 'closed_channels': 1, 'L': L, 'last_retained_clock': last, 'largest_matrix_dimension': size + 2, 'J': str(J), 'z': str(z), 'q': str(q), 'phase': str(phase), 'coupling': str(coupling), 'emitter_energy': str(E0toy), 'energy': str(energy), 'B': serial(bulk), 'V0': serial(V0), 'V1': serial(V1), 'commutator_T_Q_nonzero': first_nonzero(T * Q - Q * T), 'tail_pairs_exactly_checked': gluing_pairs, 'direct_augmented_matching': serial(direct_aug), 'direct_emitter_schur': serial(de_direct), 'background_reflection': str(rbg), 'augmented_reflection': str(raug), 'full_closed_emitter_coordinate': str(ye[1]), 'green_jump_and_matching_identities': 'exact', 'full_augmented_flux': 'exact unit modulus', 'wrong_tail_order': first_nonzero(wrong_order_residual), 'wrong_X_Y_order': first_nonzero(wrong_sigma_residual), 'wrong_augmented_lower_sign': first_nonzero(direct_aug - wrong_aug)}, 'reference_measure': {'jump_times_velocity_equals_sum_dk_weights': str(jump_dk_times_pi), 'omitted_velocity_residual': str(wrong_density), 'global_mass_reason': 'normalized seed spectral measure of a bounded selfadjoint full-line Hamiltonian; analytically reviewed, not inferred from this point'}, 'complete_overlap_discriminators': {'rectangular_isometry_shape': [4, 2], 'seed_overlap_matrix': serial(overlap), 'exact_error_gram': serial(error_gram), 'exact_squared_operator_error': str(error_eigenvalues[-1]), 'incorrect_diagonal_only_ceiling': str(diagonal_only), 'off_diagonal_matrix_gram': serial(off.H * off), 'aligned_column_squared_operator_norm': 2, 'aligned_maximum_individual_column_squared_norm': 1}, 'independent_uniform_enclosures': {'eta': rat(eta), 'delta': rat(delta), 'closed_drive': rat(wc), 'gamma_lower': rat(gamma), 'xi': rat(xi), 'profile_relative_error': rat(eta_profile), 'off_overlap': rat(off_bound), 'reference_mass_loss': rat(mass_bound), 'seed_squared_error': rat(seed_sq_bound), 'reflection_correction': rat(phase_bound), 'K0_expression': rat(K0), 'K1_expression': rat(K1), 'Dj': rat(Dj), 'escape': rat(escape), 'all_future_error': rat(joint), 'finite_horizon_exponent_margin': str(horizon_margin), 'point_spectrum_operator_ceiling': '1/12500', 'headline_bounds_recovered': {'seed': '3/1000', 'phase': '714/1000000', 'all_future': '4/1000', 'finite_horizon': '5/1000'}}, 'runtime': {'python': sys.version, 'sympy': s.__version__, 'elapsed_seconds': time.monotonic() - START, 'maximum_matrix_dimension': size + 2}, 'limits': ['The small exact model checks conventions and noncommuting identities, not the physical interval', 'The interval certificate follows analytic norm inequalities with inherited ladder constants', 'No new physical point-state certificate, optimizer, wavepacket quadrature or large-clock evolution', 'Reviewer authored earlier stationary ladder and reviewed earlier generic packet proof; source-exposed same model']}
    result['portable_execution'] = inputs.execution_metadata('installed_reviewer')
    return result
