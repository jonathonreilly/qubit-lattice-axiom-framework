"""Exact projective histories and physical nearest-neighbor copy checks.

Density updates are compared with independently propagated pure-ensemble
amplitudes. Geometry is assembled from actual Z3 sites, not a virtual comb.
The supplied trace rule and preparation remain explicit model inputs.
"""
from __future__ import annotations

from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import time
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / 'docs/PROJECTIVE_HISTORY_LOCAL_COPY_RECORD_PROCESS_BOUNDED_THEOREM_NOTE_2026-09-13.md'
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'docs/PROJECTIVE_HISTORY_LOCAL_COPY_RECORD_PROCESS_BOUNDED_THEOREM_NOTE_2026-09-13.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/RECORD_PROJECTIVE_HISTORY_LOCAL_APPEND_DOWNSTREAM_LAW_CANDIDATE_BOUNDED_THEOREM_NOTE_2026-08-21.md',
    '.claude/science/physics-loops/projective-history-local-copy-20260913/SOURCE_MANIFEST.json',
    '.claude/science/physics-loops/projective-history-local-copy-20260913/NO_GO_DISCIPLINE_CHECKLIST.md',
    '.claude/science/physics-loops/projective-history-local-copy-20260913/mutations/RESULTS.json',
)
I2 = sp.eye(2)
I4 = sp.eye(4)
ZERO = sp.ImmutableMatrix(sp.zeros(2))
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
SIGNS = (1, -1)
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
OFFSETS = tuple(tuple(s * c for c in axis) for axis in AXES for s in SIGNS)


def normal(x):
    return sp.expand(x)


def clean(matrix):
    return sp.ImmutableMatrix(matrix.applyfunc(normal))


def scalar(x):
    return sp.simplify(sp.radsimp(x))


def proj(observable, sign):
    return clean((I2 + sign * observable) / 2)


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def center(n, wing):
    return (40 * (2 * n + wing), 0, 0)


def bank_index(setting, sign):
    return 2 * setting + (1 - sign) // 2 + 1


def path(c, index):
    return [add(c, (3 * index, y, 0)) for y in (2, 1, 0)] + [add(c, (x, 0, 0)) for x in range(3 * index - 1, -1, -1)]


def neighbors(site, records):
    return {add(site, d) for d in OFFSETS} & set(records)


def support(site, records):
    shell = neighbors(site, records)
    return {records[x] for x in shell} if shell else {ZERO}


def measure(site, records):
    shell = neighbors(site, records)
    if not shell:
        return {ZERO: sp.Integer(1)}
    result = {}
    for neighbor in shell:
        content = records[neighbor]
        result[content] = result.get(content, 0) + sp.Rational(1, len(shell))
    return result


def rotations():
    answer = []
    for p in permutations(range(3)):
        parity = (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        for signs in product(SIGNS, repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                answer.append(tuple(tuple(signs[j] * c for c in AXES[p[j]]) for j in range(3)))
    return answer


def rotate(r, v):
    return tuple(sum(r[j][i] * v[j] for j in range(3)) for i in range(3))


def run():
    start = time.monotonic()
    checks = []

    def checked(name, condition, **data):
        assert bool(condition), name
        checks.append({'name': name, **data})

    # First round uses the singlet CHSH directions; second includes complex Y
    # and noncommuting changes, as well as a repeated Z program with zero branches.
    observables = (((Z, X), ((Z + X) / sp.sqrt(2), (Z - X) / sp.sqrt(2))),
                   ((Y, Z), (X, Y)))
    projectors = {(n, w, a, s): proj(observables[n][w][a], s)
                  for n, w, a, s in product(range(2), range(2), range(2), SIGNS)}
    program_tests = 0
    for n, w, a in product(range(2), repeat=3):
        pp = projectors[n, w, a, 1]
        pm = projectors[n, w, a, -1]
        assert clean(pp * pp) == pp and clean(pm * pm) == pm
        assert pp.H == pp and pm.H == pm and clean(pp * pm) == sp.zeros(2)
        assert pp + pm == I2 and sp.trace(pp) == sp.trace(pm) == 1
        program_tests += 1
    checked('all_exact_rank_one_programs_including_complex_Y', program_tests == 8, programs=program_tests)

    basis = [I4[:, j] for j in range(4)]
    singlet = (basis[1] - basis[2]) / sp.sqrt(2)
    singlet_rho = clean(singlet * singlet.H)
    rho = clean(sp.Rational(3, 4) * singlet_rho + I4 / 16)
    ensemble = [(sp.Rational(3, 4), singlet)] + [(sp.Rational(1, 16), v) for v in basis]
    checked('mixed_preparation_from_independent_ensemble',
            clean(sum((w * v * v.H for w, v in ensemble), sp.zeros(4))) == rho
            and sp.trace(rho) == 1 and set(rho.eigenvals()) == {sp.Rational(1, 16), sp.Rational(13, 16)})

    def joint(n, a, b, s, t):
        return clean(sp.kronecker_product(projectors[n, 0, a, s], projectors[n, 1, b, t]))

    # Explicitly cache only mathematical projectors; no expected probability
    # table is injected into the reconstruction.
    joints = {(n, a, b, s, t): joint(n, a, b, s, t)
              for n, a, b, s, t in product(range(2), range(2), range(2), SIGNS, SIGNS)}
    initial = [(rho, sp.Integer(1), sp.Integer(1), sp.ImmutableMatrix(I4), tuple())]
    frontier = initial
    zero_children = 0
    histories = 0
    repeat_tests = 0
    confluence_tests = 0
    for n in range(2):
        next_frontier = []
        for sigma, sequence_weight, setting_weight, matrix_product, history in frontier:
            parent_mass = scalar(sp.trace(sigma))
            assert parent_mass > 0
            for a, b in product(range(2), repeat=2):
                total_conditional = 0
                for s, t in product(SIGNS, repeat=2):
                    j = joints[n, a, b, s, t]
                    child = clean(j * sigma * j)
                    child_mass = scalar(sp.trace(child))
                    conditional = scalar(child_mass / parent_mass)
                    total_conditional += conditional
                    assert conditional >= 0
                    if child_mass == 0:
                        zero_children += 1
                        assert child == sp.zeros(4)
                        continue
                    new_product = clean(j * matrix_product)
                    direct_density = clean(new_product * rho * new_product.T)
                    assert direct_density == child
                    amplitude_mass = scalar(sum(weight * (new_product * vector).dot(sp.conjugate(new_product * vector))
                                                for weight, vector in ensemble))
                    assert amplitude_mass == child_mass
                    updated_sequence = scalar(sequence_weight * conditional)
                    assert updated_sequence == amplitude_mass
                    updated_setting = setting_weight / 4
                    pa = clean(sp.kronecker_product(projectors[n, 0, a, s], I2))
                    pb = clean(sp.kronecker_product(I2, projectors[n, 1, b, t]))
                    partial_a = clean(pa * sigma * pa)
                    partial_b = clean(pb * sigma * pb)
                    mass_a = scalar(sp.trace(partial_a))
                    mass_b = scalar(sp.trace(partial_b))
                    assert mass_a > 0 and mass_b > 0
                    assert clean(pb * partial_a * pb) == clean(pa * partial_b * pa) == child
                    ordered_a = scalar(sp.Rational(1, 2) * mass_a / parent_mass * child_mass / mass_a)
                    ordered_b = scalar(sp.Rational(1, 2) * mass_b / parent_mass * child_mass / mass_b)
                    assert scalar(ordered_a + ordered_b) == conditional
                    confluence_tests += 1
                    repeated = child
                    la, lb = 3 * bank_index(a, s) + 3, 3 * bank_index(b, t) + 3
                    # Each step inserts the actual projector(s) copied at that
                    # physical relay layer, after the first joint event.
                    for step in range(1, max(la, lb)):
                        copy_op = I4
                        if step < la:
                            copy_op = pa * copy_op
                        if step < lb:
                            copy_op = pb * copy_op
                        repeated = clean(copy_op * repeated * copy_op.H)
                        assert repeated == child
                        repeat_tests += 1
                    assert clean((I4 - pa) * child * (I4 - pa)) == sp.zeros(4)
                    assert clean((I4 - pb) * child * (I4 - pb)) == sp.zeros(4)
                    next_frontier.append((child, updated_sequence, updated_setting, new_product,
                                          history + ((a, b, s, t),)))
                    histories += 1
                assert scalar(total_conditional) == 1
        frontier = next_frontier
        checked('round_' + str(n + 1) + '_prefix_mass',
                scalar(sum(seq * setting for _, seq, setting, _, _ in frontier)) == 1,
                positive_prefixes=len(frontier))
    checked('complete_two_round_density_amplitude_history_identity', histories > 200, comparisons=histories)
    checked('supported_conditioning_and_exact_zero_children', zero_children > 0, rejected_zero_children=zero_children)
    checked('all_actual_repeated_projector_layers_preserve_density', repeat_tests > 1000, layers=repeat_tests)
    checked('one_event_refinement_confluence_and_order_mixture', confluence_tests == histories, comparisons=confluence_tests)

    # Challenge omitting the earlier update in a genuine noncommuting future.
    first = joints[0, 0, 0, 1, 1]
    sigma = clean(first * rho * first)
    future = joints[1, 1, 0, -1, 1]
    right = scalar(sp.trace(future * sigma * future) / sp.trace(sigma))
    wrong = scalar(sp.trace(future * rho * future))
    checked('skipped_earlier_state_update_is_detected', right == 0 and wrong > 0,
            actual=str(right), omitted_update=str(wrong))
    correlations = {}
    for a, b in product(range(2), repeat=2):
        table = {(s, t): scalar(sp.trace(joints[0, a, b, s, t] * singlet_rho))
                 for s, t in product(SIGNS, repeat=2)}
        assert sum(table.values()) == 1
        assert all(scalar(sum(table[s, t] for t in SIGNS)) == sp.Rational(1, 2) for s in SIGNS)
        assert all(scalar(sum(table[s, t] for s in SIGNS)) == sp.Rational(1, 2) for t in SIGNS)
        correlations[a, b] = scalar(sum(s * t * value for (s, t), value in table.items()))
    checked('singlet_CHSH_from_supplied_trace_and_preparation',
            scalar(correlations[0, 0] + correlations[0, 1] + correlations[1, 0] - correlations[1, 1]) == -2 * sp.sqrt(2),
            correlations={str(k): str(v) for k, v in correlations.items()})
    product_rho = clean(sp.kronecker_product(proj(Z, 1), proj(X, 1)))
    product_tests = []
    for a, b, s, t in product(range(2), range(2), SIGNS, SIGNS):
        weight = scalar(sp.trace(joints[0, a, b, s, t] * product_rho))
        factored = scalar(sp.trace(projectors[0, 0, a, s] * proj(Z, 1)) * sp.trace(projectors[0, 1, b, t] * proj(X, 1)))
        product_tests.append(weight == factored)
    checked('product_preparation_factorizes', len(product_tests) == 16 and all(product_tests))
    marginal_tests = []
    for preparation in (rho, singlet_rho, product_rho):
        for n, a, s in product(range(2), range(2), SIGNS):
            marginal = [scalar(sum(sp.trace(joints[n, a, b, s, t] * preparation) for t in SIGNS)) for b in range(2)]
            marginal_tests.append(marginal[0] == marginal[1])
    checked('marginals_independent_of_remote_program', len(marginal_tests) == 24 and all(marginal_tests), preparations=3)
    comparison_readout = 2 * Z + X
    checked('fixed_content_only_readout_for_all_Bell_projectors',
            all(sp.sign(scalar(sp.trace(comparison_readout * projectors[0, w, a, s]))) == s
                for w, a, s in product(range(2), range(2), SIGNS)))
    for label in ('uniform', 'parity'):
        es = {}
        for a, b in product(range(2), repeat=2):
            table = {(s, t): sp.Rational(1, 4) if label == 'uniform' else
                     (sp.Rational(1, 2) if s * t == (-1) ** (a * b) else 0)
                     for s, t in product(SIGNS, repeat=2)}
            assert sum(table.values()) == 1
            assert all(sum(table[s, t] for t in SIGNS) == sp.Rational(1, 2) for s in SIGNS)
            assert all(sum(table[s, t] for s in SIGNS) == sp.Rational(1, 2) for t in SIGNS)
            es[a, b] = sum(s * t * weight for (s, t), weight in table.items())
        chsh = abs(es[0, 0] + es[0, 1] + es[1, 0] - es[1, 1])
        checked('supplied_alternative_occurrence_' + label, chsh == (0 if label == 'uniform' else 4),
                CHSH=str(chsh), scope='comparison law, not the selected trace sector law')

    # Literal physical occurrence geometry, using immutable matrix contents.
    def make_initial(rounds):
        records = {}
        f = (-10, -10, -10)
        marker_data = ((10, ((0, 0, 0), (-1, 0, 0))), (11, ((1, 0, 0), (2, 0, 0))),
                       (12, ((0, 2, 0), (1, 2, 0))), (13, ((0, 0, 3), (1, 0, 3))))
        for value, offsets in marker_data:
            for offset in offsets:
                records[add(f, offset)] = clean(value * I2)
        for k in range(4):
            br, bc = divmod(k, 2)
            block = clean(rho[2 * br:2 * br + 2, 2 * bc:2 * bc + 2])
            point = (-50 + 5 * k, -50, -50)
            records[point] = block
            records[add(point, AXES[1])] = block
        for n, w in product(range(rounds), range(2)):
            c = center(n, w)
            for a, s in product(range(2), SIGNS):
                j = bank_index(a, s)
                value = projectors[n % 2, w, a, s]
                records[add(c, (3 * j, 3, 0))] = value
                records[add(c, (3 * j, 3, 1))] = value
            for sign in SIGNS:
                for distance in (1, 2):
                    records[add(c, (0, 10, sign * distance))] = proj(Z, sign)
        return records

    prepared = make_initial(2)
    checked('empty_condition_has_intrinsic_zero_measure', measure((10000, 0, 0), prepared) == {ZERO: 1})
    duplicate_fixture = {AXES[0]: proj(Z, 1), AXES[1]: proj(Z, 1), AXES[2]: proj(Z, -1)}
    checked('empirical_measure_retains_neighbor_multiplicity', measure((0, 0, 0), duplicate_fixture) ==
            {proj(Z, 1): sp.Rational(2, 3), proj(Z, -1): sp.Rational(1, 3)})
    checked('exact_prepared_record_count', len(prepared) == 64)
    checked('all_prepared_records_have_current_support', all(value in support(site, prepared) for site, value in prepared.items()))
    reconstructed = sp.zeros(4)
    for k in range(4):
        br, bc = divmod(k, 2)
        reconstructed[2 * br:2 * br + 2, 2 * bc:2 * bc + 2] = prepared[(-50 + 5 * k, -50, -50)]
    checked('four_physical_record_blocks_reconstruct_preparation', reconstructed == rho)
    checked('bank_indices_biject_all_program_outcomes', {bank_index(a, s) for a, s in product(range(2), SIGNS)} == {1, 2, 3, 4})

    # Reconstruct the conditional calculator from ACTUAL physical Records,
    # using all224 supported final histories and no saved hidden state.
    decoded_histories = 0
    for expected_sigma, _, _, _, history in frontier:
        recorded = dict(prepared)
        for n, (a, b, s, t) in enumerate(history):
            for wing, setting, sign in ((0, a, s), (1, b, t)):
                c = center(n, wing)
                j = bank_index(setting, sign)
                recorded[add(c, (0, 10, 0))] = proj(Z, 1 if setting == 0 else -1)
                source_content = recorded[add(c, (3 * j, 3, 0))]
                for site in path(c, j):
                    recorded[site] = source_content
        # Deliberately reverse insertion order: indexing is by physical sites.
        recorded = dict(reversed(tuple(recorded.items())))
        decoded = sp.zeros(4)
        for k in range(4):
            br, bc = divmod(k, 2)
            decoded[2 * br:2 * br + 2, 2 * bc:2 * bc + 2] = recorded[(-50 + 5 * k, -50, -50)]
        for n in range(2):
            ps = []
            for wing in range(2):
                c = center(n, wing)
                hits = [(j, add(c, (3 * j, 2, 0))) for j in range(1, 5) if add(c, (3 * j, 2, 0)) in recorded]
                assert len(hits) == 1
                j, first_site = hits[0]
                setting = (j - 1) // 2
                assert recorded[add(c, (0, 10, 0))] == proj(Z, 1 if setting == 0 else -1)
                assert c in recorded, "fixed_terminal_register_is_present"
                assert recorded[c] == recorded[first_site]
                ps.append(recorded[first_site])
            actual_projector = clean(sp.kronecker_product(*ps))
            decoded = clean(actual_projector * decoded * actual_projector)
        assert decoded == expected_sigma
        decoded_histories += 1
    checked('current_Record_only_history_reconstruction', decoded_histories == 224,
            supported_final_histories=decoded_histories, insertion_order='reversed')

    geometry_steps = 0
    support_cases = 0
    resource_cases = []
    sample_transitions = []
    for rounds in (1, 2, 7):
        for settings_and_signs in product(range(2), range(2), SIGNS, SIGNS):
            a, b, s, t = settings_and_signs
            records = make_initial(rounds)
            original = dict(records)
            transitions = 0
            new_count = 0
            for n in range(rounds):
                cs = (center(n, 0), center(n, 1))
                indices = (bank_index(a, s), bank_index(b, t))
                values = (projectors[n % 2, 0, a, s], projectors[n % 2, 1, b, t])
                paths = [path(c, j) for c, j in zip(cs, indices)]
                ds = [add(c, (0, 10, 0)) for c in cs]
                before = dict(records)
                for wing, d in enumerate(ds):
                    assert d not in records and neighbors(d, records) == {add(d, AXES[2]), add(d, (0, 0, -1))}
                    assert support(d, records) == {proj(Z, 1), proj(Z, -1)}
                    assert measure(d, records) == {proj(Z, 1): sp.Rational(1, 2), proj(Z, -1): sp.Rational(1, 2)}
                    records[d] = proj(Z, 1 if (a, b)[wing] == 0 else -1)
                transitions += 1
                new_count += 2
                for step in range(max(map(len, paths))):
                    before = dict(records)
                    sites = []
                    for wing, (c, j, trace_path, value) in enumerate(zip(cs, indices, paths, values)):
                        if step >= len(trace_path):
                            continue
                        site = trace_path[step]
                        predecessor = add(c, (3 * j, 3, 0)) if step == 0 else trace_path[step - 1]
                        assert site not in before and neighbors(site, before) == {predecessor}
                        assert support(site, before) == {value}
                        assert measure(site, before) == {value: 1}
                        sites.append(site)
                    if len(sites) == 2:
                        assert sites[1] not in {add(sites[0], d) for d in OFFSETS}
                    for wing, (trace_path, value) in enumerate(zip(paths, values)):
                        if step < len(trace_path):
                            records[trace_path[step]] = value
                    assert all(records[x] == v for x, v in before.items())
                    assert all(v in support(x, records) for x, v in records.items())
                    support_cases += len(records)
                    geometry_steps += len(sites)
                    new_count += len(sites)
                    transitions += 1
                    if rounds == 1 and indices == (4, 4):
                        sample_transitions.append((before, tuple(sites)))
                assert all(records[c] == value for c, value in zip(cs, values))
                assert transitions <= 16 * (n + 1)
            assert len(records) == 24 * rounds + 16 + new_count
            assert 38 * rounds + 16 <= len(records) <= 56 * rounds + 16
            assert all(records[x] == value for x, value in original.items())
            resource_cases.append((rounds, len(records), transitions))
    checked('literal_six_neighbor_paths_all_program_outcomes', geometry_steps > 3000, data_site_checks=geometry_steps, horizons=[1, 2, 7])
    checked('permanent_support_through_every_checked_append', support_cases > 100000, record_support_checks=support_cases)
    checked('exact_linear_resources_and_fixed_terminal_contents', len(resource_cases) == 48
            and all(38 * n + 16 <= count <= 56 * n + 16 and ticks <= 16 * n for n, count, ticks in resource_cases),
            supplied_horizons=[1, 2, 7])
    checked('path_length_formula_at_all_four_leaves', all(len(path((0, 0, 0), j)) == 3 * j + 3 for j in range(1, 5)))
    missing_buddy = dict(prepared)
    del missing_buddy[(3, 3, 1)]
    checked('missing_prepared_bank_buddy_rejected', prepared[(3, 3, 0)] not in support((3, 3, 0), missing_buddy))
    contaminated = dict(prepared)
    contaminated[(3, 2, 1)] = projectors[0, 0, 0, -1]
    checked('nonselected_neighbor_contamination_rejected', support((3, 2, 0), contaminated) != {projectors[0, 0, 0, 1]})

    proper = rotations()
    checked('all_twenty_four_proper_cubic_frames', len(proper) == len(set(proper)) == 24)
    candidates = []
    for origin, content in prepared.items():
        if content != 10 * I2:
            continue
        for r in proper:
            if all(prepared.get(add(origin, rotate(r, offset))) == value * I2
                   for offset, value in (((1, 0, 0), 11), ((0, 2, 0), 12), ((0, 0, 3), 13))):
                candidates.append((origin, r))
    checked('unique_recoverable_marker_frame', candidates == [((-10, -10, -10), AXES)])
    translation = (19, -23, 5)
    covariance_checks = 0
    for r in proper:
        def transform(point):
            return add(rotate(r, point), translation)
        for before, sites in sample_transitions:
            carried = {transform(x): content for x, content in before.items()}
            for site in sites:
                assert neighbors(transform(site), carried) == {transform(x) for x in neighbors(site, before)}
                assert support(transform(site), carried) == support(site, before)
                covariance_checks += 1
    checked('transported_physical_content_law_covariance', covariance_checks == 720, cases=covariance_checks)

    return {'status': 'passed', 'count': len(checks), 'checks': checks,
            'seconds': time.monotonic() - start,
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'derivation_sha256': hashlib.sha256(NOTE.read_bytes()).hexdigest(),
            'scope': 'Exact finite density/ensemble checks and physical geometry for a separately written all-N conditional trace-history embedding. Trace weights, preparation, projective calibration and nonlocal occurrence remain supplied. Fixed final registers repeat outcomes first committed at outcome-dependent sites. No independent source review or axiom no-go.'}


if __name__ == '__main__':
    import signal
    signal.alarm(AUDIT_TIMEOUT_SEC)
    result = run()
    print(json.dumps(result, indent=2))
    print('per_element: Exact projector identities, trace updates, zero branches and empirical multiplicities are checked.')
    print('per_site: Actual six-neighbor formation measures, permanent support and fixed terminal contents are checked.')
    print('per_mode: Two programs per wing with noncommuting complex projectors are checked; no field-mode claim.')
    print('per_block: Two-round density, pure-ensemble and physical-Record reconstructions agree on the supported fixture.')
    print('lattice_wide: checked and not executed — the finite-preparation all-N result follows from the written geometry and trace induction, not a thermodynamic extrapolation.')
    print(f"TOTAL: PASS={result['count']} FAIL=0")
    signal.alarm(0)
