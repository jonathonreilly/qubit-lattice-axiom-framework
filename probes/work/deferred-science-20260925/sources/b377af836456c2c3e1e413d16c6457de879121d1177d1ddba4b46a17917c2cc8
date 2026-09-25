#!/usr/bin/env python3
"""Independent POST comparisons and certificate checks; no author code imports.

Author JSON is treated as data. The magnetic coefficient was reconstructed in
the sealed PRE. Plaquettes here are walked in A-to-B coordinates. No linear
program is run and the released author programs are never executed.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import time

import numpy as np

HERE = Path(__file__).resolve().parent
AUTHOR = HERE / 'post_sources' / 'author'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(name, directory=HERE):
    return json.loads((directory / name).read_bytes())


def strip(counter):
    return {key: value for key, value in counter.items() if value}


def centered(point, side):
    return tuple((int(v) + side // 2) % side - side // 2 for v in point)


def word_from_author(row, side):
    result = defaultdict(Fraction)
    for a, b, value in row['word']:
        a, b = centered(a, side), centered(b, side)
        assert sum(a) % 2 == 0 and sum(b) % 2 == 1
        assert sum(abs(x-y) for x, y in zip(a, b)) == 1
        result[a, b] += Fraction(value)
    assert sum(abs(v) for v in result.values()) == row['length']
    return tuple(sorted(strip(result).items()))


def word_from_pre(row, side):
    result = defaultdict(Fraction)
    for entry in row['flow']:
        a, b = tuple(entry['a']), tuple(entry['b'])
        if side:
            a, b = centered(a, side), centered(b, side)
        result[a, b] += Fraction(entry['shift'])
    return tuple(sorted(strip(result).items()))


def divergence(vector):
    out = defaultdict(Fraction)
    for (a, b), value in vector.items():
        out[a] += value
        out[b] -= value
    return strip(out)


def walk_face(origin, first, second):
    """Construct an oriented face by four successive unit steps, using parity."""
    current = tuple(origin)
    out = defaultdict(Fraction)
    for axis, sign in ((first, 1), (second, 1), (first, -1), (second, -1)):
        nxt = tuple(x + (sign if j == axis else 0) for j, x in enumerate(current))
        if sum(current) % 2 == 0:
            out[current, nxt] += 1
        else:
            out[nxt, current] -= 1
        current = nxt
    assert current == tuple(origin)
    assert not divergence(out)
    return strip(out)


def positive_axis(vector):
    result = defaultdict(Fraction)
    for (a, b), value in vector.items():
        change = tuple(y-x for x, y in zip(a, b))
        assert sum(abs(v) for v in change) == 1
        axis = next(j for j, v in enumerate(change) if v)
        direction = change[axis]
        result[a if direction == 1 else b, axis] += direction * value
    return strip(result)


def pretty_fraction(value):
    value = Fraction(value)
    return str(value)


def all_seal_bindings():
    pre_raw = (HERE / 'PRE_SEAL.json').read_bytes()
    assert sha(pre_raw) == 'a1cc8dc5b9af73952b55402902076e1b7b28b7bc7bbc2de4834c65dd8297031d'
    pre = json.loads(pre_raw)
    for row in pre['members']:
        raw = (HERE / row['path']).read_bytes()
        assert len(raw) == row['bytes'] and sha(raw) == row['sha256']
    pins = read('POST_SOURCE_PINS.json')
    for row in pins['author_sources']:
        live, frozen = Path(row['origin']).read_bytes(), (HERE / row['frozen_path']).read_bytes()
        assert live == frozen and len(frozen) == row['bytes'] and sha(frozen) == row['sha256']
    for row in pins['reused_PRE_sources']:
        assert sha(Path(row['origin']).read_bytes()) == row['sha256']
    receipts = []
    specifications = [
        ('selected_power_polynomial.py', 'EXECUTION.json', 'CONTROL.stdout', 'CONTROL.stderr', 'POWER_POLYNOMIAL_RESULTS.json'),
        ('power_spectral_controls.py', 'SPECTRAL_EXECUTION.json', 'SPECTRAL.stdout', 'SPECTRAL.stderr', 'POWER_SPECTRAL_RESULTS.json'),
        ('power_positive_certificate.py', 'POSITIVE_EXECUTION.json', 'POSITIVE.stdout', 'POSITIVE.stderr', 'POWER_POSITIVE_CERTIFICATE.json'),
    ]
    for script, receipt_name, stdout_name, stderr_name, result_name in specifications:
        receipt = read(receipt_name, AUTHOR)
        output, stderr = (AUTHOR / stdout_name).read_bytes(), (AUTHOR / stderr_name).read_bytes()
        result = (AUTHOR / result_name).read_bytes()
        assert receipt['code_sha256'] == sha((AUTHOR / script).read_bytes())
        assert receipt['exit_code'] == 0 and not stderr and output == result
        if 'stdout_sha256' in receipt:
            assert receipt['stdout_sha256'] == sha(output)
        internal = json.loads(output)['elapsed_seconds']
        assert 0 <= internal <= receipt['elapsed_seconds']
        receipts.append(dict(script=script, receipt=receipt_name, source_sha256=receipt['code_sha256'],
            stdout_result_sha256=sha(output), stdout_result_bytes=len(output), stdout_equals_result=True,
            stderr_bytes=0, recorded_execution_elapsed_seconds=receipt['elapsed_seconds'],
            internal_elapsed_seconds=internal, independently_executed=False))
    spectral = read('POWER_SPECTRAL_RESULTS.json', AUTHOR)
    positive = read('POWER_POSITIVE_CERTIFICATE.json', AUTHOR)
    assert spectral['source_sha256'] == sha((AUTHOR / 'POWER_POLYNOMIAL_RESULTS.json').read_bytes())
    assert positive['input_sha256'] == sha((AUTHOR / 'POWER_SPECTRAL_RESULTS.json').read_bytes())
    return dict(PRE_members_unchanged=len(pre['members']), author_sources_frozen_and_live_equal=len(pins['author_sources']),
        earlier_live_origins_unchanged=len(pins['reused_PRE_sources']), author_execution_correspondence=receipts,
        author_internal_result_dependency_hashes_exact=True,
        receipt_limit='First two execution receipts bind code and exit/time only; stdout/result binding is by the unchanged author seal, not a new execution receipt.')


def exact_comparisons():
    pre = read('L16_RESULTS.json')
    infinite = read('infinite_RESULTS.json')
    jet = read('JET_CHECK_RESULTS.json')
    author = read('POWER_POLYNOMIAL_RESULTS.json', AUTHOR)
    spectral = read('POWER_SPECTRAL_RESULTS.json', AUTHOR)
    rows = []
    polynomials = []
    for item in author['rows']:
        sigma, side = item['sigma'], item['L']
        local_pre = next(r for r in pre['answers'] if r['sigma'] == sigma)
        local_inf = next(r for r in infinite['answers'] if r['sigma'] == sigma)
        words = {word_from_author(r, side): Fraction(r['coefficient']) for r in item['words']}
        assert len(words) == len(item['words']) == 303
        old_words = {word_from_pre(r, side): Fraction(r['coefficient'], 2) for r in local_pre['twice_power_laurent']}
        inf_words = {word_from_pre(r, 0): Fraction(r['coefficient'], 2) for r in local_inf['twice_power_laurent']}
        assert words == old_words == inf_words
        assert sum(words.values()) == 0 and words[()] == 2794
        assert sum(abs(v) for v in words.values()) == 6700
        assert max(sum(abs(n) for e, n in w) for w in words) == 8
        for w, value in words.items():
            assert not divergence(dict(w))
            assert words[tuple((e, -n) for e, n in w)] == value
            for axis in range(3):
                assert sum(n * (b[axis]-a[axis]) for (a, b), n in w) == 0
        pre_pairs = {tuple(sorted(centered(v, side) for v in r['pair'])): r for r in local_pre['pair_inventory']}
        seen = set()
        for r in item['pair_rows']:
            key = tuple(sorted(centered(v, side) for v in r['pair']))
            assert key not in seen
            seen.add(key)
            old = pre_pairs[key]
            assert r['terms'] == old['power2_terms']
            assert Fraction(r['value_at_zero']) == Fraction(old['power2_coefficient_sum'], 2)
        assert seen == set(pre_pairs) and len(seen) == 264
        assert item['all_pairs'] == 9 * side**3 // 2 == 18432
        rows.append(dict(sigma=sigma, L=side, words_compared_exactly=len(words),
            PRE_stored_coefficient_divisor=2, equals_PRE_L16=True, equals_PRE_infinite_lift=True,
            all_pair_rows_compared=len(seen), nonzero_pair_rows=sum(r['terms'] > 0 for r in item['pair_rows']),
            constant='2794', coefficient_sum='0', absolute_coefficient_sum='6700', maximum_word_length=8,
            exact_zero_divergence_and_zero_winding=True))
        polynomials.append(words)
    assert polynomials[0] == polynomials[1]
    r_pre = {(tuple(r['a']), tuple(r['b'])): Fraction(r['value'], 4) for r in jet['r4']}
    assert len(r_pre) == 67
    positive_pre = positive_axis(r_pre)
    t_author = {(tuple(r['positive_edge_origin']), r['axis']): Fraction(r['coefficient']) for r in spectral['t_vector']}
    assert positive_pre == t_author
    ell = walk_face((0, 0, 0), 0, 1)
    hessian = defaultdict(Fraction)
    for word, coefficient in polynomials[0].items():
        for e, n in word:
            for f, m in word:
                hessian[e, f] -= coefficient * n * m
    hessian = strip(hessian)
    edges = sorted({e for w in polynomials[0] for e, n in w} | set(r_pre) | set(ell))
    residuals = []
    for e in edges:
        for f in edges:
            residual = hessian.get((e, f), 0) - ell.get(e, 0)*r_pre.get(f, 0) - r_pre.get(e, 0)*ell.get(f, 0)
            if residual:
                residuals.append((e, f, str(residual)))
    assert not residuals and len(hessian) == 520
    contraction = sum(evalue * hessian.get((e, f), 0) * fvalue for e, evalue in ell.items() for f, fvalue in ell.items())
    assert contraction == 49600 == Fraction(spectral['hessian_cp_contraction'])
    assert len(hessian) == spectral['hessian_nonzero_entries']
    return dict(polynomial_rows=rows, all_author_words_read_and_compared=606,
        all_author_pair_rows_read_and_compared=528, t_vector_edges_compared_exactly=67,
        t_equals_PRE_r_after_orientation_conversion=True, hessian_entries=len(hessian),
        hessian_full_matrix_rows=len(edges), hessian_full_matrix_equalities=len(edges)**2,
        hessian_factorization_exact=True, cp_H_cp=str(contraction), ell_dot_r=str(sum(ell.get(e, 0)*v for e, v in r_pre.items()))), r_pre, ell


def filling_check(r_pre, ell):
    data = read('POWER_POSITIVE_CERTIFICATE.json', AUTHOR)
    target = {e: r_pre.get(e, 0)-1550*ell.get(e, 0) for e in set(r_pre)|set(ell)}
    reassembled = defaultdict(Fraction)
    face_rows = []
    for row in data['filling']:
        origin, mu, nu, coefficient = tuple(row['origin']), row['mu'], row['nu'], Fraction(row['coefficient'])
        assert mu < nu and mu in range(3) and nu in range(3)
        assert all(-2 <= x <= 2 for x in origin) and coefficient.denominator == 1
        boundary = walk_face(origin, mu, nu)
        for e, v in boundary.items():
            reassembled[e] += coefficient*v
        face_rows.append(dict(origin=origin, mu=mu, nu=nu, coefficient=str(coefficient),
            independent_A_to_B_boundary=[dict(a=a, b=b, value=str(v)) for (a, b), v in sorted(boundary.items())]))
    all_faces = [walk_face(origin, mu, nu) for origin in product(range(-2, 3), repeat=3) for mu, nu in combinations(range(3), 2)]
    domain = sorted(set(target) | {e for boundary in all_faces for e in boundary})
    assert len(all_faces) == 375 and len(domain) == 525
    residual = {e: reassembled.get(e, 0)-target.get(e, 0) for e in domain}
    assert not strip(residual)
    area = sum(abs(Fraction(row['coefficient'])) for row in data['filling'])
    assert len(face_rows) == 32 and area == 646
    assert data['lambda'] == 1550 and Fraction(data['residual_filling_l1']) == area
    assert Fraction(data['vacuum_covariance_lower_multiple_vp']) == 1550-area == 904
    assert Fraction(data['vacuum_covariance_upper_multiple_vp']) == 1550+area == 2196
    # A one-unit change of one supplied face coefficient must fail exact recomposition.
    first = data['filling'][0]
    corrupted_residual = dict(walk_face(tuple(first['origin']), first['mu'], first['nu']))
    assert len(corrupted_residual) == 4 and sum(abs(v) for v in corrupted_residual.values()) == 4
    return dict(source='Released author certificate, checked against the independently sealed PRE r',
        candidate_faces=375, link_equalities=525, all_equalities_exact=True,
        supplied_nonzero_faces=32, filling_l1=str(area), baseline_coefficient=1550,
        covariance_lower_multiple=904, covariance_upper_multiple=2196,
        altered_first_coefficient_by_one_is_rejected=True, negative_control_residual_edges=4,
        all_face_rows=face_rows, optimizer_run=False, optimizer_tolerance_or_optimality_used=False)


def own_low_band_control(ell):
    # This small finite control uses the squared norm of an explicitly formed
    # discrete Fourier plaquette; it does not execute the author's finite sums.
    side = 16
    points = np.array(list(product(range(-side//2, side//2), repeat=3)), dtype=float)
    nonzero = np.any(points != 0, axis=1)
    points = points[nonzero]
    k = 2*math.pi*points/side
    gradient = 1-np.exp(-1j*k)
    omega = np.sqrt(np.sum(abs(gradient)**2, axis=1))
    volume = side**3

    def transform(vector):
        out = np.zeros((len(points), 3), dtype=complex)
        for (origin, axis), coefficient in positive_axis(vector).items():
            out[:, axis] += float(coefficient)*np.exp(-1j*(k@np.array(origin)))
        return out

    c = transform(ell)
    c2 = np.sum(abs(c)**2, axis=1)
    transversality_error = float(np.max(abs(np.sum(gradient*c, axis=1))))
    assert transversality_error < 3e-14
    assert np.max(c2-omega**2) < 3e-14
    assert np.min(omega-4*np.linalg.norm(points, axis=1)/side) > -1e-14
    vp = float(np.sum(c2/omega)/(2*volume))
    previous = next(row for row in read('FOURIER_CORRESPONDENCE_RESULTS.json')['numeric'] if row['L'] == side)
    assert abs(vp-previous['vacuum_ell_variance']) < 2e-15
    certificate = read('POWER_POSITIVE_CERTIFICATE.json', AUTHOR)
    face_transforms = [transform(walk_face(tuple(row['origin']), row['mu'], row['nu'])) for row in certificate['filling']]
    rows = []
    for epsilon in (0.1, 0.2, 0.4, 0.7, 1.0, 2.0):
        band = omega <= epsilon
        count = int(np.count_nonzero(band))
        v_band = float(np.sum(c2[band]/omega[band])/(2*volume))
        numeric_bound = 27*epsilon**4/128
        count_bound = 27*volume*epsilon**3/64
        deviations = [abs(float(np.sum(np.sum(abs(f[band])**2, axis=1)/omega[band])/(2*volume))-v_band) for f in face_transforms]
        assert v_band <= numeric_bound+1e-15 and max(deviations) < 1e-15
        if count:
            assert side*epsilon >= 4 and count <= count_bound
            assert np.max(abs(points[band])) <= side*epsilon/4+1e-14
        rows.append(dict(L=side, epsilon=epsilon, nonzero_momenta=count,
            momentum_count_bound=count_bound, restricted_plaquette_covariance=v_band,
            covariance_bound=numeric_bound, empty_band=(count == 0),
            maximum_deviation_over_32_certificate_face_covariances=max(deviations)))
    return dict(scope='Independent finite Fourier locality/band check at L16; theorem proved analytically in POST',
        L=side, nonzero_momenta=len(points), transverse_residual=transversality_error,
        vacuum_plaquette_covariance=vp, equals_PRE_value_within_roundoff=True, rows=rows,
        author_L32_L64_reexecuted=False, interval_arithmetic=False)


def author_spectral_arithmetic():
    data = read('POWER_SPECTRAL_RESULTS.json', AUTHOR)
    prior = next(row for row in read('FOURIER_CORRESPONDENCE_RESULTS.json')['numeric'] if row['L'] == 16)
    summaries = []
    count = 0
    for graph in data['rows']:
        side, vp, covariance = graph['L'], graph['v_p'], graph['vacuum_covariance_cp_t']
        assert math.isfinite(vp) and math.isfinite(covariance)
        assert vp >= 1/math.sqrt(3) and 904*vp <= covariance <= 2196*vp
        if side == 16:
            assert abs(vp-prior['vacuum_ell_variance']) < 2e-15
            assert abs(covariance-prior['vacuum_cross']) < 2e-12
            assert abs(covariance/4-prior['selected_vacuum_power_in_kappa_over_tau_units']) < 5e-13
        rows = []
        for row in graph['rows']:
            count += 1
            epsilon = row['epsilon']
            if row['empty']:
                assert side == 16 and epsilon == .2
                rows.append(dict(row, theorem_band=True, arithmetic_fields_available=False))
                continue
            mean, baseline, added, total = [row[key] for key in ['reference_mu', 'vacuum_magnetic_power_units', 'one_minus_vacuum_power_units', 'one_magnetic_power_units']]
            assert all(math.isfinite(v) for v in (mean, baseline, added, total))
            assert 0 < mean <= epsilon and baseline == covariance
            assert abs(total-baseline-added) < 1e-12
            if epsilon <= 2:
                assert abs(added) <= (2196*27/64)*epsilon**4
                assert abs(added/baseline) <= (2196/904)*(27*math.sqrt(3)/64)*epsilon**4
            if epsilon == 3.5:
                assert epsilon > math.sqrt(12)
                assert abs(added-2*baseline) < 2e-12 and abs(total-3*baseline) < 2e-12
            rows.append(dict(row, theorem_band=epsilon <= 2, arithmetic_fields_available=True))
        summaries.append(dict(L=side, v_p=vp, covariance= covariance, rows=rows))
    assert count == 18
    return dict(all_rows_read=count, L16_agrees_with_sealed_PRE=True,
        units='Root tables: kappa/(4 tau); PRE power tables: kappa/tau.',
        scope='All stored scalar arithmetic and bounds checked; no new independent reproduction of L32/L64 sums.',
        historical_pending_electric_proof_label_preserved=data['units'], graph_rows=summaries)


def scalar_domain_control():
    minimum = None
    for electric, original, created in product(range(-100, 101), (-1, 1), (-1, 1)):
        difference = 2*electric*(electric-original)+2-electric*(electric-created)
        assert difference >= 0
        minimum = difference if minimum is None else min(minimum, difference)
    return dict(integer_rows_checked=201*4, minimum_nonnegative_gap=minimum,
        inequality='E(E-sigma) <= 2 E(E-q) + 2, E integer and q,sigma in {-1,1}',
        limit='Bounded diagnostic only; complete integer proof and original B path/mask argument are in POST.')


def main():
    tic = time.perf_counter()
    bindings = all_seal_bindings()
    exact, r, ell = exact_comparisons()
    result = dict(scope=__doc__, created_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(Path(__file__).read_bytes()), bindings=bindings,
        exact_coefficient_correspondence=exact, exact_filling=filling_check(r, ell),
        own_low_band_control=own_low_band_control(ell),
        author_spectral_arithmetic=author_spectral_arithmetic(),
        scalar_domain_diagnostic=scalar_domain_control(),
        author_code_run_or_imported=False, forbidden_references_followed=False)
    result['elapsed_seconds'] = time.perf_counter()-tic
    raw = json.dumps(result, indent=2)+'\n'
    with (HERE/'POST_CHECK_RESULTS.json').open('x') as out:
        out.write(raw)
    print(raw, end='')


if __name__ == '__main__':
    main()
