#!/usr/bin/env python3
"""Read-only correspondence checks; does not run either scientific control."""
from pathlib import Path
import hashlib
import json
import subprocess


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    base = Path(__file__).resolve().parent
    preseal = json.loads((base / 'PRE_SEAL.json').read_text())
    for item in preseal['members']:
        assert sha((base / item['path']).read_bytes()) == item['sha256']
    pins = json.loads((base / 'POST_SOURCE_PINS.json').read_text())
    for item in pins['root_sources']:
        data = (base / item['snapshot']).read_bytes()
        assert sha(data) == item['sha256'] and len(data) == item['bytes']
        assert Path(item['origin']).read_bytes() == data
    for item in pins['necessary_parent_definition_reads']:
        data = (base / item['snapshot']).read_bytes()
        origin = subprocess.check_output(['git', '-C', item['repository'],
                                          'show', item['revision'] + ':' + item['path']])
        assert data == origin and sha(data) == item['sha256']
    root = base / 'post_sources'
    author = json.loads((root / 'AUTHOR_CONTROL_SEAL.json').read_text())
    for path, digest in author['files'].items():
        assert sha((root / path).read_bytes()) == digest
    result_bytes = (root / 'PHOTON_BIRTH_CONTROL_RESULTS.json').read_bytes()
    assert result_bytes == (root / 'CONTROL.stdout.txt').read_bytes()
    assert (root / 'CONTROL.stderr.txt').read_bytes() == b''
    root_result = json.loads(result_bytes)
    root_exec = json.loads((root / 'CONTROL_EXECUTION.json').read_text())
    assert root_exec['exit_code'] == 0
    assert root_result['source_sha256'] == sha((root / 'photon_birth_controls.py').read_bytes())
    assert 0 < root_result['elapsed_seconds'] < root_exec['wall_seconds']

    pre_result = json.loads((base / 'PRIMITIVE_RESULTS.json').read_text())
    pre_by_z = {g['degree']: g for g in pre_result['graphs']}
    rows = []
    for row in root_result['graphs']:
        z = row['degree']; nA = row['vertices'] // 2
        R = 2 * nA * z * (z - 1); gamma = 4 * z * (z - 1)
        assert row['edges'] == nA * z
        assert row['resolved_marks'] == 2 * row['edges']
        assert row['actual_unit_paths'] == R
        assert row['per_edge_drift_over_kappa'] == -2 * (z - 1)
        assert row['per_edge_covariance_rate_over_kappa'] == 4 * (z - 1)
        assert row['off_diagonal_second_moment_sum_abs'] == 0
        assert row['B_occupancy_rate_over_kappa'] == gamma
        coefficients = list(row['loop_acceleration_E_coefficients'].values())
        assert len(coefficients) == 4 and sum(coefficients) == 0
        assert all(abs(v) == 2 * gamma for v in coefficients)
        assert row['loop_acceleration_constant'] == -4 * gamma
        assert row['field_only_postbirth_mutant_residual'] == 12 * gamma
        assert row['one_sign_cross_noise_sum_abs'] == R
        compared = False
        if z in pre_by_z:
            independent = pre_by_z[z]
            assert row['vertices'] == independent['vertices']
            assert row['edges'] == independent['edges']
            assert R == independent['loss_rate_divided_by_kappa']
            assert gamma == independent['initial_Wilson_second_coefficient_gamma_divided_by_kappa']
            assert row['per_edge_drift_over_kappa'] == independent['per_edge_electric_drift_divided_by_kappa']
            assert row['per_edge_covariance_rate_over_kappa'] == independent['per_edge_electric_covariance_rate_divided_by_kappa']
            compared = True
        rows.append({'periods': row['periods'], 'degree': z,
                     'analytic_initial_counts_and_loop_invariants_match': True,
                     'compared_to_frozen_independent_primitive_run': compared,
                     'loop_edge_labels_not_claimed_identical': True})

    old = root / 'history/first_harness_type_error'
    old_code = (old / 'photon_birth_controls.py').read_text()
    new_code = (root / 'photon_birth_controls.py').read_text()
    assert old_code.count('mark_outputs=defaultdict(set())') == 1
    assert old_code.replace('mark_outputs=defaultdict(set())',
                            'mark_outputs=defaultdict(set)') == new_code
    old_exec = json.loads((old / 'CONTROL_EXECUTION.json').read_text())
    old_error = (old / 'CONTROL.stderr.txt').read_text()
    assert old_exec['exit_code'] == 1 and (old / 'CONTROL.stdout.txt').read_bytes() == b''
    assert 'TypeError: first argument must be callable or None' in old_error
    assert 'mark_outputs=defaultdict(set())' in old_error

    original_pins = json.loads((base / 'SOURCE_PINS.json').read_text())
    independent_by_name = {Path(p['path']).name: p for p in original_pins['sources']}
    root_source_pins = json.loads((root / 'SOURCE_PINS.json').read_text())
    matched = []
    for pin in root_source_pins['sources']:
        name = Path(pin['path']).name
        if name.startswith(('LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_',
                            'LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_')):
            assert pin['sha256'] == independent_by_name[name]['sha256']
            matched.append(name)
    assert len(matched) == 2

    output = {
        'scope': 'Released Part II source/data comparison only; no author scientific control rerun, no Part I verdict, no independent numerical replication after release.',
        'checker_source_sha256': sha(Path(__file__).read_bytes()),
        'frozen_PRE_member_count_verified': len(preseal['members']),
        'released_root_file_count_verified': len(pins['root_sources']),
        'additional_pinned_parent_definition_source_count': len(pins['necessary_parent_definition_reads']),
        'author_seal_member_count_verified': len(author['files']),
        'source_code_self_fingerprint_matches': True,
        'root_result_equals_stdout_bytes': True,
        'root_current_stderr_empty': True,
        'root_successful_execution_record': root_exec,
        'root_internal_elapsed_seconds': root_result['elapsed_seconds'],
        'field_response_rows': rows,
        'matching_primary_physics_sources': matched,
        'preserved_root_failure': {
            'execution': old_exec,
            'reason': 'defaultdict(set()) passes a set instance rather than a factory; TypeError before graph results.',
            'sole_source_change': 'defaultdict(set()) -> defaultdict(set)',
            'failure_preserved': True,
        },
        'independent_PRE_auxiliary_check_history': 'Preserved unchanged in the original 22-member PRE seal; no rewrite or erasure.',
        'overall': 'All requested correspondence checks passed within stated scope',
    }
    payload = json.dumps(output, indent=2, sort_keys=True) + '\n'
    (base / 'POST_EVIDENCE_CHECK.json').write_text(payload)
    print(payload, end='')


if __name__ == '__main__':
    main()
