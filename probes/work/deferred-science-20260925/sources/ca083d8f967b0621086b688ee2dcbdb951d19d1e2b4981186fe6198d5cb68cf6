"""Read-only bookkeeping for released POST evidence; no author runner imports."""
from pathlib import Path
import hashlib
import json
import math
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(path, sha, size=None):
    assert digest(path) == sha, str(path)
    if size is not None:
        assert path.stat().st_size == size, str(path)


def main():
    check(ROOT/'PRE_SEAL.json', 'a2cea48da4281d1210637af88331ef24f1e0dfbc9d9c4df46a75e3e691a1f04a')
    pre = json.loads((ROOT/'PRE_SEAL.json').read_text())
    for entry in pre['members']:
        check(ROOT/entry['path'], entry['sha256'], entry['bytes'])
    bindings = json.loads((ROOT/'POST_SOURCE_BINDINGS.json').read_text())
    for entry in bindings['released_sources']:
        check(ROOT/entry['snapshot'], entry['sha256'], entry['bytes'])
        check(Path(entry['origin']), entry['sha256'], entry['bytes'])
    packet = ROOT/'post_sources'
    author = json.loads((packet/'AUTHOR_SEAL.json').read_text())
    for name, entry in author['files'].items():
        check(packet/name, entry['sha256'], entry['bytes'])
    assert author['created_utc'] < pre['sealed_utc']
    execution = json.loads((packet/'EXECUTION.json').read_text())
    assert execution['exit_code'] == 0
    assert execution['stderr_bytes'] == (packet/'CONTROL.stderr').stat().st_size == 0
    for name, key in [('observable_calibration_controls.py', 'code_sha256'),
                      ('CONTROL.stdout', 'stdout_sha256'),
                      ('OBSERVABLE_CALIBRATION_RESULTS.json', 'result_sha256')]:
        check(packet/name, execution[key])
    raw = (packet/'CONTROL.stdout').read_text()
    decoded, end = json.JSONDecoder().raw_decode(raw)
    result = json.loads((packet/'OBSERVABLE_CALIBRATION_RESULTS.json').read_text())
    assert decoded == result
    expected_tail = [
        'per_element: finite reference characteristic elements checked against independent quadrature.',
        'per_site: checked and not executed — no physical single-site detector dynamics is simulated.',
        'per_mode: finite occupation and equal-energy phase-sensitive reference examples are exercised.',
        'per_block: a two-mode, three-probe harmonic block checks anomalous and ordinary second moments.',
        'lattice_wide: checked and not executed — the full cubic curl identity is analytic, not simulated here.',
    ]
    assert raw[end:].splitlines() == ['']+expected_tail
    assert (packet/'OBSERVABLE_CALIBRATION_RESULTS.json').read_bytes() == (raw[:end]+'\n').encode()
    names = {'one_in_first', 'one_two_mode_superposition', 'vacuum_plus_two', 'vacuum_minus_two'}
    rows = result['response_rows']
    assert len(rows) == 36
    assert {(r['state'], r['t'], r['g']) for r in rows} == {
        (n, t, g) for n in names for t in (0., .4, 1.1) for g in (.2, .1, .05)}
    max_stored_remainder_discrepancy = 0.
    for row in rows:
        assert len(row['deficit_over_g_squared']) == len(row['leading_quadratic_response']) == 3
        calculated = max(abs(x-y) for x, y in zip(row['deficit_over_g_squared'], row['leading_quadratic_response']))/row['g']**2
        error = abs(calculated-row['maximum_scaled_remainder'])
        max_stored_remainder_discrepancy = max(error, max_stored_remainder_discrepancy)
        assert error < 1e-14
    average_rows = result['time_average_rows']
    assert len(average_rows) == 12
    assert {(r['state'], r['time_window']) for r in average_rows} == {
        (n, t) for n in names for t in (.3, 2., 20.)}
    for row in average_rows:
        assert abs(row['averaged_leading_response']-row['excitation_energy']) <= row['oscillatory_bound']+1e-14
    phase = result['same_energy_phase_example']
    assert abs(phase['plus']-(.2+math.sqrt(.18))) < 1e-15
    assert abs(phase['minus']-(.2-math.sqrt(.18))) < 1e-15
    bench = result['empirical_normalization_check']
    assert bench['corresponding_raw_normalized_coincidence'] == 1-.34**2
    assert bench['poisson_reference_bin_counts'] == 5780*5990*1e-9*11450
    pre_pins = json.loads((ROOT/'SOURCE_PINS.json').read_text())
    available = {Path(e['snapshot']).name: e for e in pre_pins['scientific_sources']}
    author_pins = json.loads((packet/'SOURCE_PINS.json').read_text())
    shared = []
    not_opened = []
    for entry in author_pins['files']:
        name = Path(entry['path']).name
        if name in available:
            own = available[name]
            assert own['sha256'] == entry['sha256']
            assert own['bytes'] == entry['bytes']
            check(ROOT/own['snapshot'], own['sha256'], own['bytes'])
            shared.append({'name': name, 'sha256': entry['sha256']})
        else:
            not_opened.append(entry)
    assert len(shared) == 5
    report = {
        'verified_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Hashes and stored-output arithmetic only; no author runner execution or new scientific simulation.',
        'PRE_seal_sha256': digest(ROOT/'PRE_SEAL.json'),
        'PRE_members_unchanged': len(pre['members']),
        'released_origin_and_snapshot_bindings_verified': len(bindings['released_sources']),
        'author_seal_members_verified': len(author['files']),
        'author_seal_precedes_PRE_seal': True,
        'stdout_complete_json_equals_result': True,
        'stdout_json_prefix_plus_newline_equals_result_bytes': True,
        'stdout_certificate_lines': expected_tail,
        'stderr_bytes': 0,
        'retained_author_exit_code': execution['exit_code'],
        'retained_author_wall_seconds': execution['elapsed_seconds'],
        'retained_author_internal_seconds': result['elapsed_seconds'],
        'response_rows_read_and_inventoried': len(rows),
        'time_average_rows_read_and_inventoried': len(average_rows),
        'maximum_stored_remainder_recalculation_discrepancy': max_stored_remainder_discrepancy,
        'stored_maximum_characteristic_quadrature_error': result['maximum_characteristic_quadrature_error'],
        'stored_maximum_quadrature_refinement_error': result['maximum_quadrature_refinement_error'],
        'common_scientific_source_pins_verified_against_unchanged_PRE_snapshots': shared,
        'author_declared_other_pins_not_opened_or_certified': not_opened,
        'external_count_dependency_certified': False,
        'author_runner_executions_by_this_checker': 0,
        'new_primary_retrievals': 0,
        'other_active_packets_read': False,
        'publication_repository_audit_mutations': False,
        'qualifications': ['Unweighted effect average requires survival correction for first-pair sampling.',
                           'Small-background leading-limit condition does not preserve displayed remainder rates.'],
    }
    (ROOT/'POST_VERIFICATION_REPORT.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
