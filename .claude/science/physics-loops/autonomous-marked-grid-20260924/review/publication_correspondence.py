#!/usr/bin/env python3
"""Read-only publication correspondence; does not run or import the science runner."""
import ast
import copy
import difflib
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'publication_sources'
WORK = SNAP / 'worktree'
EXT = SNAP / 'external'
RUNNER = 'scripts/finite_autonomous_marked_dynamics_under_grid_observations_2026_09_24.py'
NOTE = 'docs/FINITE_AUTONOMOUS_MARKED_DYNAMICS_UNDER_GRID_OBSERVATIONS_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RESULT = 'outputs/autonomous_marked_grid_observations_20260924/PROCESS_CONTROL_RESULTS.json'
CACHE = 'logs/runner-cache/finite_autonomous_marked_dynamics_under_grid_observations_2026_09_24.txt'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ast_text(node):
    return ast.dump(node, include_attributes=False)


def differences(a, b, path='$'):
    if isinstance(a, dict) and isinstance(b, dict):
        assert a.keys() == b.keys(), (path, a.keys(), b.keys())
        return sum((differences(a[k], b[k], path + '.' + k) for k in a), [])
    if isinstance(a, list) and isinstance(b, list):
        assert len(a) == len(b), path
        return sum((differences(x, y, path + '[' + str(i) + ']')
                    for i, (x, y) in enumerate(zip(a, b))), [])
    return [] if a == b else [{'path': path, 'root': a, 'publication': b}]


def main():
    pins = json.loads((HERE / 'PUBLICATION_SOURCE_PINS.json').read_text())
    for row in pins['sources']:
        for p in [Path(row['source']), HERE / row['snapshot']]:
            assert p.stat().st_size == row['bytes'] and sha(p) == row['sha256'], str(p)
    for name, row in pins['prior_seals'].items():
        assert sha(HERE / name) == row['sha256'], name
        seal = json.loads((HERE / name).read_text())
        assert len(seal['files']) == row['members_unchanged']
        for rel, digest in seal['files'].items():
            assert sha(HERE / rel) == digest, rel

    frozen = json.loads((EXT / 'FOURTH_PUBLICATION_FROZEN_SOURCES.json').read_text())
    for rel, digest in frozen['source_hashes'].items():
        assert sha(WORK / rel) == digest, rel
    assert frozen['seals_reverified'] == {'PRE_SEAL.json': 5, 'POST_SEAL.json': 22}
    root_code = (HERE / 'released_sources/process_controls.py').read_text()
    new_code = (WORK / RUNNER).read_text()
    delta = ''.join(difflib.unified_diff(root_code.splitlines(True), new_code.splitlines(True),
                                       fromfile='sealed_root', tofile='publication'))
    assert delta == (EXT / 'FOURTH_PUBLICATION_RUNNER_DELTA.diff').read_text()

    old_tree, new_tree = ast.parse(root_code), ast.parse(new_code)
    normalized = copy.deepcopy(new_tree)
    old_here = next(n for n in old_tree.body if isinstance(n, ast.Assign)
                    and any(isinstance(t, ast.Name) and t.id == 'HERE' for t in n.targets))
    declarations = {}
    clean = []
    for node in normalized.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            if name in ('AUDIT_TIMEOUT_SEC', 'AUDIT_INPUT_PATHS'):
                declarations[name] = ast.literal_eval(node.value)
                continue
            if name == 'HERE':
                assert ast_text(node.value) == ast_text(ast.parse(
                    "Path(__file__).resolve().parents[1]/'outputs/autonomous_marked_grid_observations_20260924'",
                    mode='eval').body)
                node.value = copy.deepcopy(old_here.value)
        if isinstance(node, ast.FunctionDef) and node.name == 'main':
            assert ast_text(node.body[0]) == ast_text(ast.parse('HERE.mkdir(parents=True,exist_ok=True)').body[0])
            assert ast_text(node.body[-1]) == ast_text(ast.parse("print('TOTAL: PASS=4 FAIL=0',flush=True)").body[0])
            node.body = node.body[1:-1]
        clean.append(node)
    normalized.body = clean
    assert ast_text(normalized) == ast_text(old_tree)
    assert declarations['AUDIT_TIMEOUT_SEC'] == 180
    declared = declarations['AUDIT_INPUT_PATHS']
    assert isinstance(declared, tuple) and len(declared) == len(set(declared)) == 3
    assert set(declared) == set(frozen['source_hashes']) - {RUNNER}

    # Independently implement the documented v1 byte serialization, without
    # importing the cache implementation or executing any declared input.
    fp = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    for rel in declared:
        p = Path(rel)
        assert not p.is_absolute() and '..' not in p.parts and p.as_posix() == rel
        name = rel.encode('utf-8')
        body = (WORK / rel).read_bytes()
        fp.update(len(name).to_bytes(8, 'big')); fp.update(name)
        fp.update(len(body).to_bytes(8, 'big')); fp.update(body)
    fingerprint = fp.hexdigest()

    execution = json.loads((EXT / 'FOURTH_PUBLICATION_CACHE_EXECUTION.json').read_text())
    ex = execution['result']
    assert ex['runner'] == RUNNER and ex['status'] == 'ok' and ex['exit_code'] == 0
    assert ex['stderr'] == '' and ex['timeout_sec'] == 180
    assert Path(execution['cache_path']).name == Path(CACHE).name
    assert len(ex['stdout']) < 200000
    expected_cache = (
        '===== runner cache v1 =====\n'
        f'runner: {RUNNER}\nrunner_sha256: {sha(WORK / RUNNER)}\n'
        f'input_fingerprint_sha256: {fingerprint}\n'
        f"timeout_sec: {ex['timeout_sec']}\nexit_code: {ex['exit_code']}\n"
        f"elapsed_sec: {ex['elapsed_sec']:.2f}\nstatus: {ex['status']}\n"
        f"----- stdout -----\n{ex['stdout']}\n----- stderr -----\n{ex['stderr']}\n"
    )
    assert (WORK / CACHE).read_text() == expected_cache
    objects = []
    remaining = ex['stdout']
    decoder = json.JSONDecoder()
    while remaining.lstrip().startswith('{'):
        remaining = remaining.lstrip()
        obj, end = decoder.raw_decode(remaining)
        objects.append(obj)
        remaining = remaining[end:]
    assert len(objects) == 3 and remaining.strip() == 'TOTAL: PASS=4 FAIL=0'
    result = json.loads((WORK / RESULT).read_text())
    assert objects[-1] == result and objects[:2] == result['process']
    assert result['source_sha256'] == sha(WORK / RUNNER)
    root_result = json.loads((HERE / 'released_sources/PROCESS_CONTROL_RESULTS.json').read_text())
    changed = differences(root_result, result)
    allowed = {'$.source_sha256', '$.elapsed_seconds', '$.process[0].elapsed_seconds', '$.process[1].elapsed_seconds'}
    assert all(row['path'] in allowed for row in changed)
    assert len(result['packet']) == 7 and len(result['marked_bin']['rows']) == 4 and len(result['process']) == 2

    root_note = (HERE / 'released_sources/FINITE_INTERVENTION_PERSONAL_DERIVATION.md').read_text()
    new_note = (WORK / NOTE).read_text()
    def section(text, number):
        return text.split(f'## {number}. ', 1)[1].split(f'## {number+1}. ', 1)[0]
    for number in range(2, 7):
        assert section(root_note, number) == section(new_note, number), number
    assert section(root_note, 7).replace('complete proposed finite-grid process bound', 'complete finite-grid process bound') == section(new_note, 7)
    compact = ' '.join(new_note.split())
    assert 'final accessible quantum state at t_q. Any additional readout at T>t_q counts as another interval and observation in q.' in compact
    assert 'L=ceil(c_L C^2), n=ceil(c_n C^15), tau=T/n, w=max(2,ceil(n^(1/3))), and R=ceil(8a), with fixed positive c_L,c_n' in compact
    note_delta = ''.join(difflib.unified_diff(root_note.splitlines(True), new_note.splitlines(True),
                                            fromfile='frozen_root_argument', tofile='publication_argument'))
    (HERE / 'PUBLICATION_NOTE_DELTA.diff').write_text(note_delta)
    report = {
        'status': 'PASS-correspondence-only',
        'checker_sha256': sha(__file__),
        'publication_source_pins_sha256': sha(HERE / 'PUBLICATION_SOURCE_PINS.json'),
        'source_snapshot_pairs_checked': len(pins['sources']),
        'prior_seals_unchanged': pins['prior_seals'],
        'runner_sha256': sha(WORK / RUNNER), 'note_sha256': sha(WORK / NOTE),
        'input_fingerprint_sha256': fingerprint,
        'complete_cache_bytes_match_recorded_execution_and_recomputed_fingerprint': True,
        'complete_stdout_parsed_and_matches_saved_result': True,
        'recorded_exit_code': ex['exit_code'], 'recorded_stderr': ex['stderr'],
        'recorded_wall_seconds': ex['elapsed_sec'],
        'runner_ast_identical_after_four_explicit_packaging_changes': True,
        'supplied_runner_delta_matches_direct_diff': True,
        'proof_sections_2_to_6_byte_identical': True,
        'proof_section_7_only_drops_proposed_qualifier': True,
        'both_post_scope_clarifications_present': True,
        'scientific_result_payload_exactly_equals_frozen_root_result': True,
        'root_result_differences': changed,
        'packet_width_count': 7, 'marked_step_count': 4, 'adaptive_process_case_count': 2,
        'independent_numerical_replication_performed': False,
        'scope': 'Source, complete output, execution record and cache fingerprint correspondence. Reuses frozen analytic POST and separate independent controls; no numerical runner import or execution, no audit verdict.'
    }
    (HERE / 'PUBLICATION_EVIDENCE_CHECK.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
