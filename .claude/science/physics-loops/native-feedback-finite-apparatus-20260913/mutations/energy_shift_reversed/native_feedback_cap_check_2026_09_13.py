AUDIT_TIMEOUT_SEC = 180


def run():
    """Exact commensurate native witness for the capped comparison lemma.

    The local subinteraction tests cap algebra, not a metric-radius error claim.
    The battery here is a padded discrete ladder, not the theorem's sine packet.
    Predicted before execution: complete refusal9/25; feedback full/capped rates
    17/50 and8/25, versus exact source1/2. No refusal is added to feedback.
    """
    from pathlib import Path
    import hashlib
    import json
    import sympy as s

    ROOT = Path(__file__).resolve().parent
    checks = {}


    def equal(a, b):
        delta = a-b
        if isinstance(delta, s.MatrixBase):
            return all(s.expand(v) == 0 for v in delta.values()) if isinstance(delta, s.SparseMatrix) else all(s.expand(v) == 0 for v in delta)
        return s.simplify(delta) == 0


    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)


    def hs2(matrix):
        return s.expand(sum(s.conjugate(v)*v for v in matrix.todok().values()))


    i2 = s.eye(2)
    pauli_z = s.diag(1, -1)
    pauli_y = s.Matrix([[0, -s.I], [s.I, 0]])
    z0 = s.kronecker_product(i2, pauli_z)
    z1 = s.kronecker_product(pauli_z, i2)
    i4 = s.eye(4)
    t0 = s.kronecker_product(i2, pauli_y)*(i4-z1)/2
    t1 = s.kronecker_product(pauli_y, i2)*(i4-z0)/2
    n0, n1 = (i4-z0)/2, (i4-z0*z1)/2
    jump = t0*n0*(i4-n1)
    record = [(i4+sign*z0)/2 for sign in (1, -1)]
    Ain, Aout = 3*t0+4*t1+10*i4, 4*t1+5*i4
    Ain_R, Aout_R = 3*t0+5*i4, s.zeros(4)


    def projectors(ham, values):
        result = {}
        for value in values:
            p = i4
            for other in values:
                if other != value:
                    p = p*(ham-other*i4)/(value-other)
            result[value] = s.SparseMatrix(p)
            check(f'projector_{tuple(values)}_{value}', equal(p*p, p))
        check(f'spectrum_{tuple(values)}', equal(sum((value*p for value, p in result.items()), s.zeros(4)), ham))
        check(f'complete_projectors_{tuple(values)}', equal(sum(result.values(), s.zeros(4)), i4))
        return result


    pin = projectors(Ain, (5, 10, 15))
    pout = projectors(Aout, (1, 5, 9))
    pin_R = projectors(Ain_R, (2, 5, 8))
    pout_R = projectors(Aout_R, (0,))
    ladder_size = 33
    sector_size = 4*ladder_size
    dimension = 2*sector_size
    zero = s.SparseMatrix(dimension, dimension, {})
    P = s.SparseMatrix.diag(*[int(k % ladder_size <= 16) for k in range(dimension)])
    eligibility = s.SparseMatrix.diag(*[int(k >= sector_size and k % ladder_size <= 16)
                                     for k in range(dimension)])


    def lift(seed, source, target):
        entries = {}
        for a, pa in source.items():
            for b, pb in target.items():
                block = s.SparseMatrix(pb*seed*pa)
                for (i, j), amplitude in block.todok().items():
                    for energy in range(ladder_size):
                        shifted = energy+b-a
                        if 0 <= shifted < ladder_size:
                            key = (i*ladder_size+shifted,
                                   sector_size+j*ladder_size+energy)
                            entries[key] = entries.get(key, 0)+amplitude
        return s.SparseMatrix(dimension, dimension, entries)


    rho_entries = {(sector_size+i*ladder_size+12, sector_size+j*ladder_size+12): v
                   for (i, j), v in pin[5].todok().items()}
    rho = s.SparseMatrix(dimension, dimension, rho_entries)
    check('source_state_pure_normalized', equal(rho*rho, rho) and equal(s.trace(rho), 1))
    check('source_cap_safe', equal(P*rho*P, rho))
    results = {}
    for law in ('complete', 'feedback'):
        seeds = record if law == 'complete' else [q*jump for q in record]
        full = [lift(b, pin, pout) for b in seeds]
        local_full = [lift(b, pin_R, pout_R) for b in seeds]
        exact = [P*v*P for v in full]
        local = [P*v*P for v in local_full]
        delta = [k-l for k, l in zip(local, exact)]
        uncut_delta = [k-l for k, l in zip(local_full, full)]
        e2 = sum(hs2(d*rho) for d in uncut_delta)
        input_error2 = sum(hs2(d*rho) for d in delta)
        adjoint_error = sum((d.H*l*rho for d, l in zip(delta, exact)), zero)
        loss_delta = sum((k.H*k-l.H*l for k, l in zip(local, exact)), zero)
        expanded = sum((l.H*d+d.H*l+d.H*d for l, d in zip(exact, delta)), zero)
        check(law+'_loss_expansion', equal(loss_delta, expanded))
        regrouped = sum((k.H*d+d.H*l for k, l, d in zip(local, exact, delta)), zero)
        check(law+'_regrouped_loss_identity', equal(loss_delta, regrouped))
        check(law+'_input_weighted_bound', input_error2 <= e2)
        # The theorem's e is a UNIFORM FIBER upper bound, not the measured forward
        # error. Both columns have norm<=1, so e^2=4 is always a valid common
        # bound. The two state-weighted premises can also be measured separately.
        adjoint_error2 = hs2(adjoint_error)
        check(law+'_uniform_fiber_forward_bound', e2 <= 4)
        check(law+'_uniform_fiber_adjoint_bound', adjoint_error2 <= 4)
        two_premise_bound2 = max(e2, adjoint_error2)
        check(law+'_loss_bound_with_both_premises', hs2(loss_delta*rho) <= 4*two_premise_bound2)
        check(law+'_exact_outputs_safe', all(equal(P*v*rho, v*rho) for v in full))
        source_rate = sum(hs2(v*rho) for v in full)
        local_full_rate = sum(hs2(v*rho) for v in local_full)
        local_cap_rate = sum(hs2(v*rho) for v in local)
        leak = sum(hs2((s.eye(dimension)-P)*v*rho) for v in local_full)
        check(law+'_cap_mass_account', equal(local_full_rate, local_cap_rate+leak))
        results[law] = {'exact_source_rate': str(source_rate),
                        'uncapped_local_rate': str(local_full_rate),
                        'capped_local_rate': str(local_cap_rate),
                        'local_cap_leakage': str(leak),
                        'uncapped_column_difference_squared': str(e2),
                        'capped_column_difference_squared': str(input_error2),
                        'adjoint_error_squared': str(hs2(adjoint_error)),
                        'common_bound_from_two_separate_premises_squared': str(two_premise_bound2),
                        'loss_error_squared': str(hs2(loss_delta*rho))}
        if law == 'complete':
            effect = eligibility-sum((k.H*k for k in local), zero)
            check('complete_refusal_effect_is_projector', equal(effect*effect, effect))
            check('complete_refusal_effect_Hermitian', equal(effect.H, effect))
            refusal_mass = s.trace(effect*rho)
            check('complete_refusal_equals_leakage', equal(refusal_mass, leak))
            check('complete_refusal_predicted_9_over_25', equal(refusal_mass, s.Rational(9, 25)))
            check('complete_refusal_bounded_by_column_error', refusal_mass <= e2)
            check('complete_total_loss_exact', equal(sum((k.H*k for k in local), zero)+effect, eligibility))
            check('complete_actual_refusal_output_mass', equal(hs2(effect*rho), refusal_mass))
            check('complete_all_output_mass_one', equal(local_cap_rate+refusal_mass, 1))
            results[law]['actual_refusal_mass'] = str(refusal_mass)
        else:
            check('feedback_forward_error_alone_does_not_bound_adjoint', adjoint_error2 > e2)
            check('feedback_source_rate_predicted_half', equal(source_rate, s.Rational(1, 2)))
            check('feedback_local_rate_predicted_17_over_50', equal(local_full_rate, s.Rational(17, 50)))
            check('feedback_cap_rate_predicted_8_over_25', equal(local_cap_rate, s.Rational(8, 25)))
            check('feedback_uses_actual_rate_not_identity', local_cap_rate != 1)

    # A separate two-state Lindblad calculation distinguishes the new factor4
    # from an unjustified factor2. It is not a native apparatus fixture.
    amplitude = s.Matrix([[0, 1], [0, 0]])
    attenuated = s.Rational(3, 4)*amplitude
    excited = s.diag(0, 1)
    def dissipator(j):
        rate = j.H*j
        return j*excited*j.H-(rate*excited+excited*rate)/2
    change = dissipator(attenuated)-dissipator(amplitude)
    norm_change = sum(abs(value)*multiplicity for value, multiplicity in change.eigenvals().items())
    weighted_error = s.Rational(1, 4)
    comparison_multiplier = 4
    check('two_state_actual_generator_difference', equal(norm_change, s.Rational(7, 8)))
    check('four_factor_dissipator_bound', norm_change <= comparison_multiplier*weighted_error)
    check('two_factor_competitor_rejected', norm_change > 2*weighted_error)
    results['two_state_lemma'] = {'scope': 'synthetic amplitude damping',
                                'generator_trace_norm': str(norm_change),
                                'common_weighted_error': str(weighted_error),
                                'comparison_multiplier': comparison_multiplier}
    payload = {'status': 'small_exact_cap_checks_passed', 'author_check_only': True,
               'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               'check_count': len(checks), 'checks': checks, 'results': results,
               'scope': 'Commensurate finite native cap algebra; not a metric-radius or sine-packet error certificate.'}

    return payload


if __name__ == "__main__":
    import json
    result = run()
    print(json.dumps(result, indent=2))
    print(f"TOTAL: PASS={result['check_count']} FAIL=0")
