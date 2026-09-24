"""Mechanical publication comparison only; never imports or runs scientific code."""
from pathlib import Path
import ast
import copy
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
SNAP = ROOT/'publication_final_sources'
PUB = ROOT.parent/'prepared-observation-publication'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def function_map(source):
    tree = ast.parse(source)
    return tree, {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}


def float_count(obj):
    if isinstance(obj, float):
        return 1
    if isinstance(obj, dict):
        return sum(float_count(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(float_count(v) for v in obj)
    return 0


def main():
    previous = {}
    for name, expected in [('PRE_SEAL.json', 'a2cea48da4281d1210637af88331ef24f1e0dfbc9d9c4df46a75e3e691a1f04a'),
                           ('POST_SEAL.json', '90b97eef5b8d85355a133252be82ebbf4dff31230ed845090a79941af2ebf876')]:
        assert sha(ROOT/name) == expected
        seal = json.loads((ROOT/name).read_text())
        for item in seal['members']:
            path = ROOT/item['path']
            assert sha(path) == item['sha256']
            assert path.stat().st_size == item['bytes']
        previous[name] = {'sha256': expected, 'members_unchanged': len(seal['members'])}
    bindings = json.loads((ROOT/'PUBLICATION_FINAL_SOURCE_BINDINGS.json').read_text())
    for item in bindings['sources']:
        assert sha(ROOT/item['snapshot']) == sha(Path(item['origin'])) == item['sha256']
        assert (ROOT/item['snapshot']).stat().st_size == item['bytes']
    frozen = json.loads((SNAP/'PREPARED_OBSERVATION_PUBLICATION_FROZEN_SOURCES.json').read_text())
    execution = json.loads((SNAP/'PREPARED_OBSERVATION_PUBLICATION_CACHE_EXECUTION.json').read_text())
    for relative, expected in frozen['files_sha256'].items():
        assert sha(PUB/relative) == expected
    runner = SNAP/Path(frozen['runner']).name
    source = runner.read_text()
    tree, public_functions = function_map(source)
    original_source = (ROOT/'post_sources/observable_calibration_controls.py').read_text()
    _, original_functions = function_map(original_source)
    helpers = ['displacement_element', 'characteristic', 'quadrature_characteristic',
               'lower', 'inner', 'moment_data']
    functions = {}
    for name in helpers:
        public_text = ast.get_source_segment(source, public_functions[name])
        original_text = ast.get_source_segment(original_source, original_functions[name])
        assert public_text == original_text
        assert ast.dump(public_functions[name], include_attributes=False) == ast.dump(original_functions[name], include_attributes=False)
        functions[name] = {'source_segment_identical': True,
                           'source_segment_sha256': hashlib.sha256(public_text.encode()).hexdigest(),
                           'frozen_function_pin': frozen['root_functions'][name]}
    old_main = ast.get_source_segment(original_source, original_functions['main'])
    new_group = ast.get_source_segment(source, public_functions['calibration_control_group'])
    assert old_main.replace('def main():', 'def calibration_control_group():', 1) == new_group
    transformed = copy.deepcopy(original_functions['main'])
    transformed.name = 'calibration_control_group'
    assert ast.dump(transformed, include_attributes=False) == ast.dump(public_functions['calibration_control_group'], include_attributes=False)
    declarations = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in ('AUDIT_INPUT_PATHS', 'AUDIT_TIMEOUT_SEC', 'ROOT_CONTROL_SOURCES', 'RESULT_PATH'):
                    declarations[target.id] = ast.literal_eval(node.value)
    paths = declarations['AUDIT_INPUT_PATHS']
    assert len(paths) == len(set(paths)) == 6
    fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    for relative in paths:
        path = Path(relative)
        assert not path.is_absolute() and '..' not in path.parts and path.as_posix() == relative
        body = (PUB/relative).read_bytes()
        name_bytes = relative.encode()
        fingerprint.update(len(name_bytes).to_bytes(8, 'big'))
        fingerprint.update(name_bytes)
        fingerprint.update(len(body).to_bytes(8, 'big'))
        fingerprint.update(body)
    fp = fingerprint.hexdigest()
    assert fp == '6f056f941810763336abe84c3ed4518cdbc54923d8a2435539e2b88d76250739'
    run = execution['result']
    assert run['status'] == 'ok' and run['exit_code'] == 0 and run['stderr'] == ''
    assert run['runner'] == frozen['runner']
    assert run['timeout_sec'] == declarations['AUDIT_TIMEOUT_SEC'] == 120
    assert run['elapsed_sec'] == 0.8937721252441406
    result_path = SNAP/Path(frozen['result']).name
    result = json.loads(result_path.read_text())
    stdout = run['stdout']
    stdout_result, end = json.JSONDecoder().raw_decode(stdout)
    assert stdout_result == result
    assert stdout[end:] == '\nTOTAL_PASS: 3\n'
    assert result_path.read_bytes() == (stdout[:end]+'\n').encode()
    assert result['source_sha256'] == sha(runner)
    assert result['all_assertions_passed'] is True
    expected_cache = (
        '===== runner cache v1 =====\n'
        f"runner: {run['runner']}\n"
        f"runner_sha256: {sha(runner)}\n"
        f"input_fingerprint_sha256: {fp}\n"
        f"timeout_sec: {run['timeout_sec']}\n"
        f"exit_code: {run['exit_code']}\n"
        f"elapsed_sec: {run['elapsed_sec']:.2f}\n"
        f"status: {run['status']}\n"
        f"----- stdout -----\n{stdout}\n"
        f"----- stderr -----\n{run['stderr']}\n")
    cache_path = SNAP/Path(execution['path']).name
    assert cache_path.read_text() == expected_cache
    old = json.loads((ROOT/'post_sources/OBSERVABLE_CALIBRATION_RESULTS.json').read_text())
    new = copy.deepcopy(result['calibration'])
    old_timer = old.pop('elapsed_seconds')
    new_timer = new.pop('elapsed_seconds')
    assert old == new
    old_stdout = (ROOT/'post_sources/CONTROL.stdout').read_text()
    _, old_end = json.JSONDecoder().raw_decode(old_stdout)
    assert result['calibration_certificates'] == old_stdout[old_end:].strip().splitlines()
    assert declarations['ROOT_CONTROL_SOURCES'][0] == (
        'record-observable-calibration-personal/observable_calibration_controls.py',
        sha(ROOT/'post_sources/observable_calibration_controls.py'))
    assert declarations['RESULT_PATH'] == frozen['result']

    old_note = (ROOT/'publication_sources'/Path(frozen['note']).name).read_text()
    new_note = (SNAP/Path(frozen['note']).name).read_text()
    old_sentence = 'The original two-record response measures a real field-quadrature second\nmoment.'
    new_sentence = 'The leading weak-field, vacuum-subtracted original two-record response\nmeasures a real field-quadrature second moment.'
    assert old_note.count(old_sentence) == 1
    assert old_note.replace(old_sentence, new_sentence, 1) == new_note
    assert sha(SNAP/Path(frozen['note']).name) == '979cef8109013ff632dc5b5cc704d770e201f75fdaa8da6e577944a5f282a4f8'
    assert sha(ROOT/'publication_sources/PREPARED_OBSERVATION_PUBLICATION_CACHE_EXECUTION.json') == sha(SNAP/'PREPARED_OBSERVATION_PUBLICATION_CACHE_EXECUTION_BEFORE_FRONT_QUALIFICATION.json')
    initial_result = json.loads((ROOT/'publication_sources'/Path(frozen['result']).name).read_text())
    final_result = copy.deepcopy(result)
    timer_deltas = {}
    for path in (['elapsed_seconds'], ['calibration', 'elapsed_seconds']):
        left, right = initial_result, final_result
        for key in path[:-1]:
            left, right = left[key], right[key]
        timer_deltas['.'.join(path)] = {'before': left.pop(path[-1]), 'final': right.pop(path[-1])}
    full_payload_same_except_timers = initial_result == final_result
    assert full_payload_same_except_timers

    report = {
        'verified_utc': datetime.now(timezone.utc).isoformat(),
        'opening_sentence_only_note_delta_verified': True,
        'earlier_execution_receipt_preserved_exactly': True,
        'whole_combined_payload_equal_after_two_timer_removals_mechanical_only': full_payload_same_except_timers,
        'timer_deltas_between_publication_runs': timer_deltas,
        'scope': 'Section A/C.1 source comparison and full cache/output mechanical correspondence; Section B/C.2 science excluded.',
        'prior_seals': previous,
        'publication_source_snapshots_and_origins_verified': len(bindings['sources']),
        'all_frozen_file_hashes_verified': len(frozen['files_sha256']),
        'unchanged_calibration_helpers': functions,
        'calibration_main_identical_after_function_rename_only': True,
        'calibration_complete_payload_equal_excluding_elapsed_seconds': True,
        'equal_calibration_float_values_excluding_timer': float_count(new),
        'calibration_response_rows': len(new['response_rows']),
        'calibration_time_average_rows': len(new['time_average_rows']),
        'calibration_five_certificates_exact': True,
        'old_calibration_timer': old_timer,
        'new_calibration_timer': new_timer,
        'declared_input_paths': list(paths),
        'declared_input_fingerprint_reconstructed_from_bytes': fp,
        'execution_receipt_whole_stdout_equals_result_plus_TOTAL': True,
        'cache_complete_bytes_reconstructed_from_receipt_and_identities': True,
        'result_sha256': sha(result_path),
        'runner_sha256': sha(runner),
        'cache_sha256': sha(cache_path),
        'retained_primary_exit_code': run['exit_code'],
        'retained_primary_stderr_bytes': len(run['stderr'].encode()),
        'retained_primary_elapsed_seconds': run['elapsed_sec'],
        'retained_primary_internal_seconds': result['elapsed_seconds'],
        'count_parent_scientifically_recertified': False,
        'other_prepared_matter_packets_opened': False,
        'canonical_or_author_scientific_runner_executions': 0,
        'Section_B_C2_scientific_verdict': None,
        'publication_audit_or_prior_seal_mutations': False,
    }
    (ROOT/'PUBLICATION_FINAL_VERIFICATION_REPORT.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
