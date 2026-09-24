#!/usr/bin/env python3
"""Compare frozen publication bytes and existing records; execute no primary."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    base = Path(__file__).resolve().parent
    pins = json.loads((base / 'PUBLICATION_SOURCE_PINS.json').read_text())
    prior = {}
    for name in ('PRE_SEAL.json', 'POST_SEAL.json'):
        raw = (base / name).read_bytes()
        assert digest(raw) == pins['prior_seals'][name]
        seal = json.loads(raw)
        for member in seal['members']:
            assert digest((base / member['path']).read_bytes()) == member['sha256']
        prior[name] = len(seal['members'])
    for item in pins['sources']:
        snap = (base / item['snapshot']).read_bytes()
        assert len(snap) == item['bytes'] and digest(snap) == item['sha256']
        assert Path(item['origin']).read_bytes() == snap
    root = base / 'publication_sources/worktree'
    external = base / 'publication_sources/external'
    np = 'docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
    rp = 'scripts/photon_dispersion_observation_and_live_formation_response_2026_09_24.py'
    op = 'outputs/photon_observation_live_formation_20260924/PHOTON_OBSERVATION_LIVE_FORMATION_RESULTS.json'
    cp = 'logs/runner-cache/photon_dispersion_observation_and_live_formation_response_2026_09_24.txt'
    note = (root / np).read_text(); runner = (root / rp).read_text()
    rootnote = (base / 'post_sources/PHOTON_OBSERVATION_AND_LIVE_BIRTH_ROOT_DERIVATION.md').read_text()
    rootsource = (base / 'post_sources/photon_birth_controls.py').read_text()
    rootpart = rootnote[rootnote.index('## II.'):]
    pubpart = note[note.index('## II.'):note.index('## Sources, evidence and disposition')]
    changes = [
        ("state's trace distance is", "state's trace-norm distance is"),
        ('bounded function of the link angles', 'bounded gauge-invariant periodic function of the link angles'),
        ('bounded periodic angle functions', 'bounded gauge-invariant periodic angle functions'),
        ('a real normalized transverse oscillator', 'a real normalized positive-frequency transverse oscillator'),
        ('omega_k=2sqrt(KJ lambda_k).', 'omega_k=2sqrt(KJ lambda_k)>0.'),
        ('Equation (9) applied to this q-diagonal expression therefore gives',
         'Summing the original joint marked paths (8), including their output matter, therefore gives'),
    ]
    corrected = rootpart
    locations = []
    for old, new in changes:
        assert corrected.count(old) == 1
        corrected = corrected.replace(old, new)
        locations.append({'publication_text': new, 'line': note[:note.index(new)].count('\n') + 1})
    assert corrected.rstrip() == pubpart.rstrip()

    def functions(code):
        return {n.name: ast.get_source_segment(code, n) for n in ast.parse(code).body
                if isinstance(n, ast.FunctionDef)}
    froot, fpub = functions(rootsource), functions(runner)
    function_checks = {}
    for name in ('graph', 'graph_control', 'dispersion_controls'):
        assert froot[name] == fpub[name]
        function_checks[name] = {'exact_source_segment_equal': True,
                                'sha256': digest(fpub[name].encode())}
    tree = ast.parse(runner)
    literals = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                literals[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
    inputs = literals['AUDIT_INPUT_PATHS']
    assert list(inputs) == pins['declared_input_paths']
    assert len(inputs) == len(set(inputs)) == 6
    fp = hashlib.sha256(); fp.update(b'runner-cache-input-fingerprint-v1\0')
    input_records = []
    for rel in inputs:
        assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
        data = (root / rel).read_bytes(); name = rel.encode()
        fp.update(len(name).to_bytes(8, 'big')); fp.update(name)
        fp.update(len(data).to_bytes(8, 'big')); fp.update(data)
        input_records.append({'path': rel, 'bytes': len(data), 'sha256': digest(data)})
    fingerprint = fp.hexdigest()
    assert fingerprint == '0a004bc3e1d50958450b87fde302135af636dc5ee2da558cd4ade6c4dc89b9cc'
    external_run = json.loads((external / 'FOURTEENTH_PUBLICATION_CACHE_EXECUTION.json').read_text())
    run = external_run['result']
    result_bytes = (root / op).read_bytes(); result = json.loads(result_bytes)
    rootresult = json.loads((base / 'post_sources/PHOTON_BIRTH_CONTROL_RESULTS.json').read_text())
    assert result['source_sha256'] == digest((root / rp).read_bytes())
    assert result['reused_root_source_sha256'] == literals['ROOT_CONTROL_SOURCE_SHA'] == digest(rootsource.encode())
    assert result['graphs'] == rootresult['graphs']
    # Opaque payload preservation only; no Part I scientific review is inferred.
    assert result['dispersion'] == rootresult['dispersion']
    assert run['runner'] == rp and run['status'] == 'ok' and run['exit_code'] == 0
    assert run['timeout_sec'] == literals['AUDIT_TIMEOUT_SEC'] == 120
    assert run['stderr'] == ''
    assert run['stdout'].encode() == result_bytes + b'TOTAL: PASS=4 FAIL=0\n'
    cache_expected = (
        '===== runner cache v1 =====\n'
        f'runner: {rp}\n'
        f'runner_sha256: {result["source_sha256"]}\n'
        f'input_fingerprint_sha256: {fingerprint}\n'
        f'timeout_sec: {run["timeout_sec"]}\n'
        f'exit_code: {run["exit_code"]}\n'
        f'elapsed_sec: {run["elapsed_sec"]:.2f}\n'
        f'status: {run["status"]}\n'
        '----- stdout -----\n' + run['stdout'][-200000:] + '\n'
        '----- stderr -----\n' + run['stderr'][-50000:] + '\n'
    )
    assert (root / cp).read_bytes() == cache_expected.encode()
    assert len(run['stdout']) < 200000 and len(run['stderr']) < 50000
    freeze = json.loads((external / 'FOURTEENTH_PUBLICATION_FROZEN_SOURCES.json').read_text())
    verify = json.loads((external / 'FOURTEENTH_PRIMARY_ROOT_VERIFICATION.json').read_text())
    for rel, h in freeze['files_sha256'].items():
        assert digest((root / rel).read_bytes()) == h
    for key, rel in [('note_sha256', np), ('runner_sha256', rp), ('result_sha256', op), ('cache_sha256', cp)]:
        assert verify[key] == digest((root / rel).read_bytes())
    assert verify['seconds'] == run['elapsed_sec'] == 0.372133731842041
    assert freeze['root_candidate_sha256'] == digest(rootnote.encode())
    assert freeze['root_control_sha256'] == digest(rootsource.encode())
    assert freeze['base_revision'] == pins['base_revision']
    result_check = {
        'scope': 'Final Part II correspondence only; no primary execution, no new physics derivation and no Part I scientific verdict.',
        'checker_source_sha256': digest(Path(__file__).read_bytes()),
        'unchanged_prior_seal_members_verified': prior,
        'publication_source_snapshot_count': len(pins['sources']),
        'all_current_origins_equal_snapshots': True,
        'Part_II_equals_frozen_root_after_only_the_four_requested_corrections_and_trailing_whitespace': True,
        'correction_text_locations': locations,
        'disclosed_function_copy_checks': function_checks,
        'declared_input_fingerprint_sha256': fingerprint,
        'declared_inputs': input_records,
        'all_three_graph_rows_equal_frozen_root': True,
        'Part_I_payload_equal_as_opaque_data_only': True,
        'source_and_root_self_fingerprints_match': True,
        'execution_stdout_exact_result_plus_summary': True,
        'cache_complete_bytes_match_execution_and_current_input_fingerprint': True,
        'cache_did_not_truncate_output': True,
        'stderr_empty': True,
        'reported_external_wall_seconds': run['elapsed_sec'],
        'reported_runner_internal_seconds': result['elapsed_seconds'],
        'cache_printed_wall_seconds': f'{run["elapsed_sec"]:.2f}',
        'primary_rerun_by_this_checker': False,
        'new_independence_claim': False,
        'overall': 'Requested narrow correspondence checks passed',
    }
    output = json.dumps(result_check, indent=2, sort_keys=True) + '\n'
    (base / 'PUBLICATION_BINDING_CHECK.json').write_text(output)
    print(output, end='')


if __name__ == '__main__':
    main()
