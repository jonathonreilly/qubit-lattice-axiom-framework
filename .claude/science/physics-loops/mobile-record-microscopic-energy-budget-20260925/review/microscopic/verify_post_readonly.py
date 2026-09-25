#!/usr/bin/env python3
"""Read-only released-source correspondence; no scientific code is executed.

This program reads/hash-checks explicit files, parses ASTs and stored JSON,
and prints one JSON report. It does not write any file, spawn a process,
import an evidence program, or follow unapproved source-manifest references.
The surrounding recorder, not this verifier, stores the printed report.
"""
from pathlib import Path
from fractions import Fraction
import ast
import datetime
import difflib
import hashlib
import json
import math

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'microscopic-ground-stationarity-personal'
SNAPSHOT = HERE / 'post_sources' / 'author37'
PRE_SEAL_HASH = '81464c8af25297f2f5765d785e2fe0a01accf566cccfce10e767d86fb79c9baa'
AUTHOR_SEAL_HASH = 'b2ed6d091f07232dec83eadc338e6385f1e20f5efddfff29288e871b0c792dd3'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def data(path):
    return json.loads(path.read_text())


def member_check(root, rows):
    for row in rows:
        path = root / row['path']
        assert path.stat().st_size == row['bytes'], str(path)
        assert digest(path) == row['sha256'], str(path)
    return len(rows)


def close(x, y, absolute=2e-12, relative=2e-12):
    assert math.isclose(x, y, abs_tol=absolute, rel_tol=relative), (x, y)


def functions(tree):
    return {node.name: ast.dump(node, include_attributes=False)
            for node in tree.body if isinstance(node, ast.FunctionDef)}


def verify():
    assert digest(HERE / 'PRE_SEAL.json') == PRE_SEAL_HASH
    pre = data(HERE / 'PRE_SEAL.json')
    pre_count = member_check(HERE, pre['members'])
    assert digest(AUTHOR / 'AUTHOR_SEAL.json') == AUTHOR_SEAL_HASH
    assert digest(SNAPSHOT / 'AUTHOR_SEAL.json') == AUTHOR_SEAL_HASH
    author_seal = data(SNAPSHOT / 'AUTHOR_SEAL.json')
    author_count = member_check(AUTHOR, author_seal['members'])
    assert member_check(SNAPSHOT, author_seal['members']) == author_count
    initial = data(HERE / 'POST_SOURCE_PINS_INITIAL.json')
    assert initial['preserved_pre_seal_sha256'] == PRE_SEAL_HASH
    for row in initial['author_sources']:
        assert digest(Path(row['origin'])) == row['sha256']
        assert digest(HERE / row['snapshot']) == row['sha256']

    # Explicitly reuse only the four allowed main notes and two provisional
    # root36 author files. Do not traverse the author's independent36 pins.
    pre_sources = data(HERE / 'SOURCE_PINS.json')['sources'][:6]
    source_rows = []
    for row in pre_sources:
        assert digest(Path(row['origin'])) == row['sha256']
        assert digest(HERE / row['snapshot']) == row['sha256']
        source_rows.append({'origin': row['origin'], 'sha256': row['sha256']})
    allowed = {row['origin']: row['sha256'] for row in pre_sources}
    author_pins = data(SNAPSHOT / 'SOURCE_PINS.json')['sources']
    matched = []
    not_followed = []
    for row in author_pins:
        if row['path'] in allowed:
            assert row['sha256'] == allowed[row['path']]
            matched.append(row['path'])
        else:
            not_followed.append(row['path'])
    assert len(matched) == 6 and len(not_followed) == 4

    old_path = SNAPSHOT / 'history/attempt01/primitive_spin_energy_controls.py'
    new_path = SNAPSHOT / 'primitive_spin_energy_controls.py'
    old_source, new_source = old_path.read_text(), new_path.read_text()
    old_ast, new_ast = ast.parse(old_source), ast.parse(new_source)
    old_functions, new_functions = functions(old_ast), functions(new_ast)
    assert old_functions.keys() == new_functions.keys()
    changed = [key for key in old_functions
               if old_functions[key] != new_functions[key]]
    assert changed == ['build']
    expected_diff = ''.join(difflib.unified_diff(
        old_source.splitlines(keepends=True), new_source.splitlines(keepends=True),
        fromfile='attempt01', tofile='attempt02'))
    assert expected_diff == (SNAPSHOT / 'history/attempt01/REPAIR.diff').read_text()
    for name in ('CONTROL_ATTEMPT01.stdout', 'CONTROL_ATTEMPT01.stderr',
                 'EXECUTION_ATTEMPT01.json'):
        assert (SNAPSHOT / name).read_bytes() == (
            SNAPSHOT / 'history/attempt01' / name).read_bytes()
    for attempt in (1, 2):
        receipt = data(SNAPSHOT / f'EXECUTION_ATTEMPT0{attempt}.json')
        code_path = old_path if attempt == 1 else new_path
        assert receipt['source_sha256'] == digest(code_path)
        assert receipt['exit_code'] == (1 if attempt == 1 else 0)
        for stream in ('stdout', 'stderr'):
            assert receipt[f'{stream}_bytes'] == (
                SNAPSHOT / f'CONTROL_ATTEMPT0{attempt}.{stream}').stat().st_size
    result_path = SNAPSHOT / 'SPIN_ENERGY_CONTROL_RESULTS.json'
    assert result_path.read_bytes() == (SNAPSHOT / 'CONTROL_ATTEMPT02.stdout').read_bytes()
    result = data(result_path)
    assert result['source_sha256'] == digest(new_path)
    assert result['all_assertions_passed'] is True
    assert len(result['identity_rows']) == 6
    assert len(result['spectral_rows']) == 4
    assert len(result['integer_rows']) == 4

    identities = []
    for row in result['identity_rows']:
        length, spin = row['cycle_length'], row['spin']
        assert length in (4, 8)
        assert row['ordered_local_pairs'] + row['distant_ordered_A_pairs'] == (length // 2)**2
        assert row['full_outward_D_monotonic_paths'] > 0
        assert row['rotor_boundary_paths_retained'] > 0
        assert row['coefficient_identity_max_abs'] < 3e-12
        assert row['second_order_identity_max_abs'] < 3e-14
        assert row['resolved_coherent_loss_max_abs'] < 1e-12
        assert row['S1_exact_rational_identity'] == (spin == 1)
        if spin == 1:
            assert row['coefficient_identity_max_abs'] == 0
            assert row['second_order_identity_max_abs'] == 0
            assert row['resolved_coherent_loss_max_abs'] == 0
        identities.append({'cycle_length': length, 'spin': spin,
                           'dimension': row['full_dimension'],
                           'coefficient_residual': row['coefficient_identity_max_abs'],
                           'loss_residual': row['resolved_coherent_loss_max_abs']})

    spectral = []
    for row in result['spectral_rows']:
        spin, eps = row['spin'], row['epsilon']
        close(eps**2 * spin * (spin + 1), 0.01)
        close(row['bare_P_energy'], 400 * spin * (spin + 1), absolute=1e-8)
        assert row['bare_P_intensity'] == 0
        close(row['embedded_rotor_intensity'], 8)
        close(row['low_block_remainder_norm'] / eps**2,
              row['remainder_over_epsilon_squared'])
        close(row['microscopic_jump_amplitude_error'] / eps,
              row['jump_error_over_epsilon'])
        assert row['ground_D_in_rotated_P'] >= 0
        assert row['full_ground_energy'] > row['embedded_rotor_energy']
        spectral.append({'spin': spin,
                         'energy_minus_common': row['full_ground_energy'] - row['embedded_rotor_energy'],
                         'rate_error_over_epsilon': (row['full_ground_intensity'] - row['embedded_rotor_intensity']) / eps,
                         'eigenvector_residual': row['ground_residual_norm']})

    # Independent polynomial arithmetic on the disclosed integer inequality;
    # this does not import/re-execute any author function.
    integer_rows = []
    for row in result['integer_rows']:
        q, sig = row['q'], row['sigma']
        linear = -(2*q + sig)
        # Same signs: (e-q)(e-2q). Opposite: e(e-q)+2.
        factored = (1, -3*q, 2) if q == sig else (1, -q, 2)
        assert (1, linear, 2) == factored
        values = [e*e + linear*e + 2 for e in range(-100, 101)]
        assert min(values) == row['minimum_over_minus100_to100']
        assert min(values) >= 0
        integer_rows.append({'q': q, 'sigma': sig,
                             'polynomial_coefficients': [1, linear, 2],
                             'minimum_on_stored_integer_range': min(values)})

    own_primitive = data(HERE / 'primitive_attempt03/PRIMITIVE_RESULTS.json')
    own_micro = data(HERE / 'microscopic_attempt01/MICROSCOPIC_RESULTS.json')
    assert len(own_primitive['local_identity_rows']) == 51
    assert all(row['canonical_equals_local'] for row in own_primitive['local_identity_rows'])
    assert len(own_primitive['scalar_weight_rows']) == 7
    assert len(own_primitive['unconfined_flux_operator_counterexample_rows']) == 8
    assert len(own_micro['rows']) == 5
    coherence_rows = []
    for row in own_micro['rows']:
        eps = row['epsilon']
        close(eps**2 * row['S'] * (row['S'] + 1), 1)
        assert len(row['mixed_state_rows']) == 4
        for mixed in row['mixed_state_rows']:
            close(mixed['rotated_high_weight'], eps**4 / 2)
            close((mixed['actual_rate'] - mixed['normalized_low_common_rate']) / eps,
                  mixed['rate_difference_over_epsilon'])
            close(mixed['actual_mean_energy'] - row['ground_energy'], mixed['mean_energy_excess'])
        coherence_rows.append({'spin': row['S'], 'rows': 4,
                               'energy_excess': row['mixed_state_rows'][0]['mean_energy_excess'],
                               'min_rate': min(x['actual_rate'] for x in row['mixed_state_rows']),
                               'max_rate': max(x['actual_rate'] for x in row['mixed_state_rows'])})

    # Exact conditional coefficient division, with kappa,n and delta symbolic.
    stationary_gap_coefficient = Fraction(16, 5) / Fraction(4, 5)
    assert stationary_gap_coefficient == 4
    report = {
        'verified_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope': 'Released-source correspondence and stored-evidence arithmetic only; no scientific runner execution or applied audit verdict.',
        'pre_seal_sha256': PRE_SEAL_HASH,
        'pre_members_unchanged': pre_count,
        'author_seal_sha256': AUTHOR_SEAL_HASH,
        'author_members_live_and_snapshot_verified': author_count,
        'permitted_parent_origins_verified': source_rows,
        'author_manifest_entries_matched_to_allowed_parents': len(matched),
        'author_manifest_references_not_followed': not_followed,
        'author_program_functions_parsed': list(new_functions),
        'changed_functions_from_preserved_failed_attempt': changed,
        'preserved_repair_diff_exact': True,
        'attempt01_exit_code': 1,
        'attempt02_exit_code': 0,
        'attempt02_wall_seconds': data(SNAPSHOT / 'EXECUTION_ATTEMPT02.json')['seconds'],
        'attempt02_internal_seconds': result['elapsed_seconds'],
        'result_stdout_byte_identity': True,
        'author_identity_row_review': identities,
        'author_spectral_stored_arithmetic': spectral,
        'creation_defect_polynomial_checks': integer_rows,
        'own_sealed_primitive_groups': {'identity': 51, 'scalar': 7, 'flux': 8},
        'own_sealed_coherence_comparison': coherence_rows,
        'stationary_gap_in_delta_n_units': str(stationary_gap_coefficient),
        'root_and_PRE_parameters_compared': 'Root K=100 versus PRE K=1; numerical spectra are not asserted identical.',
        'scientific_programs_imported_or_executed': False,
        'verifier_writes_files_or_spawns_processes': False,
        'all_checks_passed': True,
    }
    return report


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, allow_nan=False))
