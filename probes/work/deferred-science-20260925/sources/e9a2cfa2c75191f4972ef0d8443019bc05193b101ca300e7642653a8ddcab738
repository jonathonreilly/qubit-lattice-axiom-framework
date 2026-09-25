#!/usr/bin/env python3
"""Read/hash/parse the blind PRE packet, printing one JSON report.

No file writes, subprocesses, imports of evidence code, or source execution.
"""
from pathlib import Path
from fractions import Fraction
import ast
import datetime
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def verify():
    manifest = read(HERE / 'SOURCE_PINS_INITIAL.json')
    checked_sources = []
    for entry in manifest['sources']:
        source, snapshot = Path(entry['origin']), HERE / entry['snapshot']
        assert digest(source) == entry['sha256']
        assert digest(snapshot) == entry['sha256']
        assert source.stat().st_size == snapshot.stat().st_size == entry['bytes']
        checked_sources.append({'snapshot': entry['snapshot'],
                                'sha256': entry['sha256']})
    results = []
    receipts = []
    for number in (1, 2):
        directory = HERE / f'control_attempt0{number}'
        script = directory / 'response_primitive_control.py'
        ast.parse(script.read_text())
        receipt = read(directory / 'EXECUTION.json')
        assert receipt['source_sha256'] == digest(script)
        assert receipt['exit_code'] == 0
        assert receipt['stderr_bytes'] == 0
        assert (directory / 'stderr.log').read_bytes() == b''
        assert receipt['stdout_bytes'] == (directory / 'stdout.log').stat().st_size
        assert (directory / 'stdout.log').read_bytes() == (
            directory / 'RESPONSE_PRIMITIVE_RESULTS.json').read_bytes()
        result = read(directory / 'RESPONSE_PRIMITIVE_RESULTS.json')
        assert result['source_sha256'] == receipt['source_sha256']
        assert result['all_assertions_passed'] is True
        results.append(result); receipts.append(receipt)
    old, new = results
    original_script = HERE / 'control_attempt01/response_primitive_control.py'
    current_script = HERE / 'response_primitive_control.py'
    assert current_script.read_bytes() == (
        HERE / 'control_attempt02/response_primitive_control.py').read_bytes()
    expected_diff = ''.join(difflib.unified_diff(
        original_script.read_text().splitlines(keepends=True),
        current_script.read_text().splitlines(keepends=True),
        fromfile='attempt01', tofile='attempt02_geometry_extension'))
    assert (HERE / 'GEOMETRY_SCOPE_EXTENSION.diff').read_text() == expected_diff
    for group in ('operator_rows', 'coherence_rows', 'primitive_rows',
                  'global_balance_rows'):
        assert old[group] == new[group]
    for previous, current in zip(old['geometry_rows'], new['geometry_rows']):
        assert all(current[key] == value for key, value in previous.items())
    geometry = []
    for row in new['geometry_rows']:
        length = row['L']
        assert row['vertices'] == length**3
        assert row['B_sites'] == length**3 // 2
        assert row['plaquettes'] == 3*length**3
        assert 4*row['plaquettes_per_B'] == row['response_per_vacancy_at_K1'] == 48
        extra = 3*length**2 if length == 4 else 0
        assert row['extra_straight_winding_four_cycles'] == extra
        assert row['all_graph_four_cycles'] == row['plaquettes']+extra
        assert row['response_per_vacancy_if_all_four_cycles_summed'] == (
            60 if length == 4 else 48)
        geometry.append(row)
    lookup = {(row['state'], row['plaquette']): row
              for row in new['operator_rows']}
    assert len(lookup) == 21
    for row in lookup.values():
        assert row['A_p'] in (0, 2, 4)
        assert row['XX_YY_XY_and_sum_exact'] is True
    determinants = set()
    for row in new['coherence_rows']:
        xx, yy, xy, determinant, total = (
            Fraction(row[key]) for key in ('XX', 'YY', 'XY', 'matrix_determinant', 'sum'))
        Ap = lookup[(row['state'], row['plaquette'])]['A_p']
        assert xx+yy == total == 2*Ap
        assert determinant == xx*yy-xy*xy >= 0
        assert xx >= 0 and yy >= 0
        if row['phase'] == 'plus':
            assert (xx, yy, xy) == (Fraction(Ap, 2), Fraction(3*Ap, 2), 0)
        elif row['phase'] == 'minus':
            assert (xx, yy, xy) == (Fraction(3*Ap, 2), Fraction(Ap, 2), 0)
        else:
            assert row['phase'] == 'imaginary'
            assert (xx, yy, xy) == (Ap, Ap, Fraction(Ap, 2))
        determinants.add(str(determinant))
    primitive = {}
    for row in new['primitive_rows']:
        assert row['Wilson_commutator_exact']
        assert row['Gauss_and_number_change_exact']
        assert row['response_loss_balance_exact']
        assert Fraction(row['jump_norm_squared']) == row['jump_output_words']
        primitive[(row['state'], row['instrument'])] = row
    for state in {row['state'] for row in new['primitive_rows']}:
        minus = primitive[(state, 'resolved_minus')]['jump_output_words']
        plus = primitive[(state, 'resolved_plus')]['jump_output_words']
        coherent = primitive[(state, 'coherent_edge')]['jump_output_words']
        assert coherent == minus+plus
    for row in new['global_balance_rows']:
        assert row['N']+row['vacant_B'] == 64
        assert row['summed_response'] == 48*row['vacant_B']
        assert row['capacity_relation_exact']
    assert 48*2 == 96 and 60*2 == 120
    counts = {key: len(value) for key, value in new.items() if isinstance(value, list)}
    assert counts == {'geometry_rows': 3, 'operator_rows': 21, 'coherence_rows': 63,
                      'primitive_rows': 21, 'global_balance_rows': 7}
    return {
        'verified_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Read-only source/evidence verification; not a rerun of scientific code or audit verdict.',
        'sources_verified': checked_sources,
        'source_entries': len(checked_sources),
        'scientific_group_counts': counts,
        'all_previous_scientific_entries_unchanged': True,
        'geometry_extension_diff_exact': True,
        'geometry_complete': geometry,
        'coherence_determinants': sorted(determinants),
        'count_coefficient_elementary': 96,
        'count_coefficient_all_four_cycles_L4': 120,
        'controls': [{'source_sha256': r['source_sha256'],
                      'elapsed_seconds': r['elapsed_seconds'],
                      'exit_code': r['exit_code'], 'stdout_bytes': r['stdout_bytes'],
                      'stderr_bytes': r['stderr_bytes']} for r in receipts],
        'current_scientific_source_sha256': digest(current_script),
        'final_scientific_result_sha256': digest(
            HERE / 'control_attempt02/RESPONSE_PRIMITIVE_RESULTS.json'),
        'scientific_programs_imported_or_executed_by_verifier': False,
        'file_writes_or_processes_by_verifier': False,
        'all_checks_passed': True,
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, allow_nan=False))
