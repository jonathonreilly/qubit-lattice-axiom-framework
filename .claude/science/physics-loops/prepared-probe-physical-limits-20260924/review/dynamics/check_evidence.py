"""Inspect all saved control payloads and bindings without rerunning H4 actions."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from collections import defaultdict
import json

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def frac(x):
    return Fraction(x['numerator'], x['denominator'])


def check_run(source, label, result_name):
    record = json.loads((HERE / (label + '_EXECUTION.json')).read_text())
    assert record['code_sha256'] == digest(HERE / source)
    assert record['stdout_sha256'] == digest(HERE / (label + '.stdout.log'))
    assert record['stderr_sha256'] == digest(HERE / (label + '.stderr.log'))
    assert record['exit_code'] == 0
    assert (HERE / (label + '.stderr.log')).read_bytes() == b''
    assert (HERE / result_name).read_bytes() == (HERE / (label + '.stdout.log')).read_bytes()
    payload = json.loads((HERE / result_name).read_text())
    if 'source_sha256' in payload:
        assert payload['source_sha256'] == digest(HERE / source)
    if 'code_sha256' in payload:
        assert payload['code_sha256'] == digest(HERE / source)
    if 'primitive_source_sha256' in payload:
        assert payload['primitive_source_sha256'] == digest(HERE / 'primitive_dynamics_control.py')
    return payload, {'source': source, 'result': result_name,
                     'source_sha256': digest(HERE / source),
                     'result_sha256': digest(HERE / result_name),
                     'wall_seconds': record['wall_seconds'],
                     'exit_code': record['exit_code'], 'stderr_bytes': 0}


def witness_check(side, common_paths, witness):
    common_div = defaultdict(int)
    for path in common_paths:
        common_div[tuple(path[0])] -= 1
        common_div[tuple(path[-1])] += 1
        for x, y in zip(path, path[1:]):
            distances = [(y[d]-x[d]) % side for d in range(3)]
            assert sum(t != 0 for t in distances) == 1
            assert next(t for t in distances if t) in (1, side-1)
    target_div = defaultdict(int)
    for row in witness['matter_deviations']:
        v = tuple(row['site'])
        target_div[v] = row['charge'] - int(sum(v) % 2 == 0)
    raw = witness.get('terms', witness.get('Laurent_terms'))
    coefficient_sum = 0
    for term in raw:
        coefficient_sum += term['coefficient']
        shifts = term.get('shifts')
        if shifts is None:
            shifts = [(s['edge'][0], s['edge'][1], s['power']) for s in term['electric_shift']]
        div = common_div.copy()
        signature = [0,0,0]
        for aa, bb, power in shifts:
            aa, bb = tuple(aa), tuple(bb)
            assert sum(aa) % 2 == 0 and sum(bb) % 2 == 1
            distances = [(bb[d]-aa[d]) % side for d in range(3)]
            nonzero = [(d, t) for d, t in enumerate(distances) if t]
            assert len(nonzero) == 1
            axis, step = nonzero[0]
            assert step in (1, side-1)
            sign = 1 if step == 1 else -1
            signature[axis] += power * sign
            div[aa] += power
            div[bb] -= power
        assert signature == witness['harmonic_signature_without_common_flow']
        for v in set(div) | set(target_div):
            assert div[v] == target_div[v], (side, v, div[v], target_div[v])
    assert coefficient_sum == witness['group_coefficient_before_dividing_sqrt2']
    return {'terms_checked': len(raw), 'coefficient_sum': coefficient_sum,
            'witness_norm_contribution': {'numerator': coefficient_sum**2, 'denominator': 2},
            'all_shifts_adjacent_A_to_B': True, 'all_term_Gauss_and_harmonic_signatures_match': True}


def moment_row(m):
    mu, second, variance = map(frac, (m['mean_H4'],m['second_H4'],m['variance_H4']))
    assert second - mu*mu == variance and variance >= 0
    assert all(x.denominator == 1 for x in (mu,second,variance))
    return {'mean_H4': int(mu), 'second_H4': int(second), 'variance_H4': int(variance)}


def main():
    primitive, pbind = check_run('primitive_dynamics_control.py','CONTROL','PRIMITIVE_DYNAMICS_RESULTS.json')
    topology, tbind = check_run('topology_and_gram_control.py','TOPOLOGY','TOPOLOGY_GRAM_RESULTS.json')
    output, obind = check_run('output_energy_control.py','OUTPUT_ENERGY','OUTPUT_ENERGY_RESULTS.json')
    single, sbind = check_run('single_hop_energy_control.py','SINGLE_HOP','SINGLE_HOP_ENERGY_RESULTS.json')
    pins, pinbind = check_run('pin_sources.py','SOURCE_PIN','SOURCE_PINS.json')
    assert pins['pin_script_sha256'] == digest(HERE/'pin_sources.py')
    for row in pins['records']:
        copied = HERE / row['copy']
        assert len(copied.read_bytes()) == row['bytes'] and digest(copied) == row['sha256']
        if 'origin' in row:
            assert digest(Path(row['origin'])) == row['sha256']
    assert topology['side_six_result_sha256'] == digest(HERE/'PRIMITIVE_DYNAMICS_RESULTS.json')
    assert primitive['rows'][0]['flat_moments'] == topology['rows'][0]['flat_moments']
    prep_rows = []
    witness_total = 0
    # The original side-six verbose witness is also fully traversed.
    for row in primitive['rows']:
        for birth in row['selected_birth_rows']:
            w = witness_check(row['side'], row['common_flow_paths'], birth['witness'])
            witness_total += w['terms_checked']
    for row in topology['rows']:
        correct = moment_row(row['flat_moments']['harmonic_averaged'])
        wrong = moment_row(row['flat_moments']['all_angles_zero'])
        assert frac(row['Gram_cross_check']['minus_two_Gram_sum']) == correct['mean_H4']
        assert row['H4_Gauss_terms_checked'] == row['H4_Laurent_terms']
        births = []
        for birth in row['selected_birth_rows']:
            assert frac(birth['initial_flat_fiber_birth_norm_squared']) == 0
            assert birth['all_BH4_terms_Gauss_checked'] == birth['BH4_Laurent_terms']
            gamma = frac(birth['gamma_harmonic_averaged'])
            assert 0 < gamma <= 25*correct['variance_H4']
            witness = witness_check(row['side'], row['common_flow_paths'], birth['witness'])
            assert gamma >= Fraction(witness['witness_norm_contribution']['numerator'],2)
            witness_total += witness['terms_checked']
            births.append({'sigma': birth['sigma'], 'gamma': int(gamma),
                           'gamma_all_zero': int(frac(birth['gamma_all_angles_zero'])),
                           'BH4_Laurent_terms': birth['BH4_Laurent_terms'], 'witness': witness})
        prep_rows.append({'side': row['side'], 'edges': row['edges'],
                          'H4_Laurent_terms': row['H4_Laurent_terms'],
                          'H4_four_hop_paths': row['H4_four_hop_paths'],
                          'correct_moments': correct, 'all_angles_zero_moments': wrong,
                          'selected_birth_rows': births})
    output_rows = []
    for row in output['rows']:
        correct = moment_row(row['flat_moments']['harmonic_averaged'])
        wrong = moment_row(row['flat_moments']['all_angles_zero'])
        assert -2*frac(row['sum_positive_Gram_norms']) == correct['mean_H4']
        assert row['all_H4_terms_Gauss_checked'] == row['H4_Laurent_terms']
        prep = next(r for r in prep_rows if r['side'] == row['side'])
        assert row['M_rotor_mean_exact_for_any_field_in_this_matter_word'] == prep['edges']-36
        output_rows.append({'side': row['side'], 'sigma': row['sigma'],
                            'correct_moments': correct, 'all_angles_zero_moments': wrong,
                            'output_minus_input_mean_H4': correct['mean_H4']-prep['correct_moments']['mean_H4'],
                            'exact_mean_M': row['M_rotor_mean_exact_for_any_field_in_this_matter_word']})
    single_summary = []
    for row in single['rows']:
        coefficients = [frac(r['coefficient']) for r in row['polynomial']]
        assert sorted(coefficients) == [Fraction(-1,2),Fraction(-1,2),Fraction(row['edges']-24)]
        assert row['flat_mean_M'] == row['edges']-25
        assert row['selected_output_mean_M'] == row['edges']-36
        assert row['flat_output_minus_input_M'] == -11
        single_summary.append({k:v for k,v in row.items() if k != 'polynomial'})
    result = {'scope': 'Complete saved-payload/binding inspection and exact arithmetic checks; no repeated H4 computation and no author controls read or executed.',
              'bindings': [pbind,tbind,obind,sbind,pinbind],
              'source_records_checked': len(pins['records']),
              'prepared_rows': prep_rows, 'normalized_output_rows': output_rows,
              'single_hop_rows': single_summary,
              'witness_terms_traversed_including_original_and_compact_copies': witness_total,
              'failure_history': 'No execution failed. The tempting all-link-angles-zero replacement gives different second moments and instability coefficients; those unfavorable comparator rows are preserved in full. Harmonic Haar averaging is the stated physical coefficient.',
              'checker_sha256': digest(Path(__file__))}
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
