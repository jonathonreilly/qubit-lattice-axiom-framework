"""Source/output bindings and bounded arithmetic checks; no science rerun."""
from pathlib import Path
import hashlib
import itertools
import json
import subprocess
from datetime import datetime, timezone

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_text())


def main():
    pins = load(HERE/'SOURCE_PINS.json')
    origin_checks = []
    for row in pins['sources']:
        frozen = HERE/row['frozen']
        assert frozen.stat().st_size == row['bytes'] and sha(frozen) == row['sha256']
        if row['type'] == 'git':
            actual = subprocess.run(['git','show',row['revision']+':'+row['path']],
                cwd=row['repository'], capture_output=True, check=True).stdout
        else:
            actual = Path(row['origin']).read_bytes()
        assert actual == frozen.read_bytes()
        origin_checks.append({'frozen':row['frozen'],'sha256':sha(frozen),
                              'bytes':len(actual),'origin_matches':True})
    assert len(origin_checks) == pins['source_count'] == 13
    no_go_main = HERE/'sources/docs/ai_methodology/skills/no-go-discipline/SKILL.md'
    no_go_installed = HERE/'sources/INSTALLED_NO_GO_DISCIPLINE_SKILL.md'
    assert no_go_main.read_bytes() == no_go_installed.read_bytes()
    execution = load(HERE/'CONTROL_ATTEMPT_01_EXECUTION.json')
    data = load(HERE/'CONTROL_ATTEMPT_01_STDOUT.json')
    assert execution['exit_code'] == 0
    assert sha(HERE/'primitive_energy_control.py') == execution['source_sha256'] == data['source_sha256']
    assert sha(HERE/'CONTROL_ATTEMPT_01_STDOUT.json') == execution['stdout_sha256']
    assert sha(HERE/'CONTROL_ATTEMPT_01_STDERR.txt') == execution['stderr_sha256']
    assert (HERE/'CONTROL_ATTEMPT_01_STDERR.txt').stat().st_size == 0
    words = data['primitive_data']
    assert len(words['birth_component_words']) == 6
    assert len(words['spectator_component_words']) == 2
    for component in ('birth_component_words','spectator_component_words'):
        for charges, fields in words[component]:
            assert sum(charges) == 1 and sum(fields) == charges[0]-1
            assert all(-e == q for e,q in zip(fields,charges[1:]))
    assert all(not entries for entries in words['spectator_resolved_jumps'].values())
    assert all(value == 0 for row in words['H2_effective']+words['H4_effective']+words['full_P_gated_D'] for value in row)
    rows = data['energy_and_event_rows']
    spins = (1,2,4,8,16,32)
    assert tuple(row['spin'] for row in rows) == spins
    assert len(data['structure_rows']) == 6 and len(data['boundary_layer_rows']) == 24
    assert {(r['spin'],r['phase']) for r in data['boundary_layer_rows']} == set(itertools.product(spins, sorted({r['phase'] for r in data['boundary_layer_rows']})))
    for row in data['structure_rows']:
        assert row['dimension'] == 12 and row['P_dimension'] == 4
        assert row['maximum_structural_residual'] == 0
        assert row['resolved_channel_count_including_zero_channels'] == 6
        assert row['coherent_channel_count_including_zero_channels'] == 3
        assert row['spectator_original_jumps_identically_zero']
    summaries = []
    for row in rows:
        c = row['spin']*(row['spin']+1)
        law = row['exact_energy_law']
        assert law['low_energy'] == 0 and law['high_energy'] == c*(c+1)
        assert law['high_probability_numerator'] == 1 and law['high_probability_denominator'] == c+1
        assert row['exact_mean'] == c
        assert row['exact_second_moment'] == c*c*(c+1)
        assert row['exact_variance'] == c**3
        assert 0 < row['actual_resolved_event_probability'] < 1
        assert row['limiting_event_probability'] > 0
        assert row['moment_max_relative_residual'] < 1e-8
        assert abs(row['numerical_high_weight']-1/(c+1)) < 1e-10
        assert row['total_variation_to_delta_zero'] == 1/(c+1)
        for values in row['bounded_tests'].values():
            difference = abs(complex(*values['value'])-complex(*values['limit']))
            assert abs(difference-values['error']) < 1e-14
            assert difference <= 2/(c+1)+1e-14
        summaries.append({key:row[key] for key in ('spin','actual_resolved_event_probability',
            'exact_mean','exact_variance','total_variation_to_delta_zero','moment_max_relative_residual')})
    for row in data['boundary_layer_rows']:
        assert row['actual_selected_intensity'] >= 0
        if row['phase'] == 0:
            assert row['actual_selected_intensity'] == 0
            assert row['effective_initial_intensity'] == 1
    limits = load(HERE/'INDEPENDENCE_AND_FAILURE_RECORD.json')
    assert limits['author_candidate_directory_opened'] is False
    assert limits['author_or_parent_programs_imported_or_executed'] == []
    return {'checked_utc':datetime.now(timezone.utc).isoformat(),
        'scope':'Read-only bindings and stored-output arithmetic; not a second scientific run or an independent second researcher.',
        'verifier_sha256':sha(Path(__file__)), 'PRE_sha256':sha(HERE/'PRE.md'),
        'source_origins_verified':origin_checks,'source_origin_count':len(origin_checks),
        'scientific_parent_count':3,'scientific_execution':execution,
        'scientific_internal_seconds':data['elapsed_seconds'],
        'full_rows_checked':{'structure':6,'energy_and_event':6,'bounded_test_evaluations':18,'initial_time_layer':24,'abstract_examples':2},
        'bounded_test_provenance':'Evaluations of the derived two-atom law; separate primitive matrix checks are spectral weight and direct moments.',
        'all_physical_word_counts':{'birth_component':6,'spectator_component':2,'product':12},
        'row_summaries':summaries,
        'max_relative_moment_residual':max(r['moment_max_relative_residual'] for r in rows),
        'process_failure_preserved':limits['process_failures'],
        'current_verification_failures':[],
        'no_author_or_parent_science_program_executed':True}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2, allow_nan=False))
