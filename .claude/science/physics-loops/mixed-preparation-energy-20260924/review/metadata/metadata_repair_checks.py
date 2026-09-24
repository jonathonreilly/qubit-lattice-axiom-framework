"""Bounded metadata/cache correspondence check; never runs a physics primary."""

from pathlib import Path
import ast
import difflib
import hashlib
import json
import subprocess


BASE = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth')
OUT = BASE / 'publication-metadata-independent'
SPECS = [
    {
        'label': 'SEVENTH',
        'tree': 'no-first-birth-publication',
        'base': '918fbe18619667017c56c29677f9f02363368d89',
        'anchor': 'continuous-coherence-independent',
        'anchor_seal': '5d2676e7ead04a5e67d709d2ef2d6a9dbcbfb83468fac6acb6bb5c9083d1a318',
        'frozen_sha': 'aeb0fca4191f52c26eafdd78183e0dd8c88448ebbd869996688ec7bbb9c8507e',
        'execution_sha': 'da1ded3660f687f0b65ee818deed9766d33e06fcfb4e8448dadf540048304aa9',
        'old_note_sha': 'ab8234682ea61bff35fbd18685f65ac0b853aa20e0d3600304b9004076bd147a',
        'old_result_sha': '92d901f05b11e949eb9bbb33a63f67b7ef6ddbd33b5fe3109dacd91ec7a5af8d',
        'old_cache_sha': 'c69af646dc1e02069ea299287e04f65622c98e7e4be179ff27119ce741783ec4',
        'old_status': '**Status:** conditional bounded theorem; selective independent reconstruction,',
        'new_status': '**Type:** bounded_theorem\n\n**Status:** proposed_retained\n\nConditional bounded theorem; selective independent reconstruction,',
        'object_count': 4,
        'timing_difference_count': 4,
        'total': 'TOTAL: PASS=3 FAIL=0',
    },
    {
        'label': 'EIGHTH',
        'tree': 'mixed-preparation-publication',
        'base': 'cfac353eedae504627196bf9e48009f1b4177f94',
        'anchor': 'preparation-uniform-independent',
        'anchor_seal': '1cd9b2465460ea2be9a8e488895eac9c9e09125b8669ec0df6b563cc94985147',
        'frozen_sha': 'd4ba3cdfd0059567ae90529e1e27ac1d4d3c8d9f783f1cd6597d77584433abb5',
        'execution_sha': '2d84b7daf2ced88e2df6a06fc5e26715715937540e10562227000b0c1c4df5bc',
        'old_note_sha': '04bf4ad2def6a5d8e7a0ab711d4e6e52d1933eb9d28366b1cdb5dee1383d9726',
        'old_result_sha': '60d3ee81cc9a35b6e396a383f93c95a400b4dd803f3984779d0fe4d178c2d6e1',
        'old_cache_sha': '125a86e284d83feee379c89948ff6acd4a511cf222defb7b4fcb812a229a3515',
        'old_status': '**Status:** conditional bounded theorem with selective independent PRE/POST;',
        'new_status': '**Type:** bounded_theorem\n\n**Status:** proposed_retained\n\nConditional bounded theorem with selective independent PRE/POST;',
        'object_count': 1,
        'timing_difference_count': 1,
        'total': 'TOTAL: PASS=2 FAIL=0',
    },
]


def digest(body):
    return hashlib.sha256(body).hexdigest()


def git_body(root, revision, rel):
    return subprocess.check_output(['git', 'show', f'{revision}:{rel}'], cwd=root)


def differences(a, b, path=()):
    if isinstance(a, dict) and isinstance(b, dict):
        assert a.keys() == b.keys(), ('keys', path)
        return [item for key in a for item in differences(a[key], b[key], path + (key,))]
    if isinstance(a, list) and isinstance(b, list):
        assert len(a) == len(b), ('length', path)
        return [item for i, (x, y) in enumerate(zip(a, b)) for item in differences(x, y, path + (i,))]
    assert type(a) is type(b), ('type', path)
    return [] if a == b else [{'path': list(path), 'before': a, 'after': b}]


def fingerprint(paths, read):
    d = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    for rel in paths:
        name, body = rel.encode(), read(rel)
        d.update(len(name).to_bytes(8, 'big'))
        d.update(name)
        d.update(len(body).to_bytes(8, 'big'))
        d.update(body)
    return d.hexdigest()


def header_fields(cache):
    return dict(line.split(': ', 1) for line in cache.split('----- stdout -----', 1)[0].splitlines() if ': ' in line)


def main():
    pins, baseline_pins, reports = {}, {}, {}
    def pin(path):
        value = digest(path.read_bytes())
        pins[str(path)] = value
        return value

    for spec in SPECS:
        label = spec['label']
        root = BASE / spec['tree']
        revision = spec['base']
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
        assert head == revision
        anchor = BASE / spec['anchor']
        anchor_seal = anchor / 'PUBLICATION_COMPARISON_SEAL.json'
        assert pin(anchor_seal) == spec['anchor_seal']
        a = json.loads(anchor_seal.read_text())
        members = a.get('members', a.get('files'))
        if isinstance(members, dict):
            members = [{'path': name, 'sha256': value} for name, value in members.items()]
        for member in members:
            assert pin(anchor / member['path']) == member['sha256'], member['path']

        frozen_path = BASE / (label + '_METADATA_REPAIR_FROZEN.json')
        execution_path = BASE / (label + '_METADATA_CACHE_EXECUTION.json')
        assert pin(frozen_path) == spec['frozen_sha']
        assert pin(execution_path) == spec['execution_sha']
        frozen = json.loads(frozen_path.read_text())
        execution = json.loads(execution_path.read_text())
        assert frozen['comparison_base'] == revision
        files = frozen['files_sha256']
        assert len(files) == 4
        note = next(x for x in files if x.startswith('docs/'))
        runner = next(x for x in files if x.startswith('scripts/'))
        cache = next(x for x in files if x.startswith('logs/'))
        result = next(x for x in files if x.startswith('outputs/'))
        for rel, value in files.items():
            assert pin(root / rel) == value, rel
            old = git_body(root, revision, rel)
            baseline_pins[f'{root}@{revision}:{rel}'] = digest(old)
        old_note = git_body(root, revision, note).decode()
        new_note = (root / note).read_text()
        assert digest(old_note.encode()) == spec['old_note_sha']
        assert old_note.count(spec['old_status']) == 1
        assert new_note == old_note.replace(spec['old_status'], spec['new_status'], 1)
        assert 'claim_type: bounded_theorem\n' in old_note
        assert 'not a retained audit verdict.' in new_note
        note_diff = ''.join(difflib.unified_diff(old_note.splitlines(True), new_note.splitlines(True), fromfile=revision + ':' + note, tofile=str(root / note)))
        (OUT / (label + '_METADATA_ONLY_DIFF.txt')).write_text(note_diff)

        runner_body = (root / runner).read_bytes()
        assert runner_body == git_body(root, revision, runner)
        tree = ast.parse(runner_body.decode())
        literals = {}
        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in ['AUDIT_INPUT_PATHS', 'AUDIT_TIMEOUT_SEC']:
                        literals[target.id] = ast.literal_eval(node.value)
        paths = literals['AUDIT_INPUT_PATHS']
        assert isinstance(paths, tuple) and len(paths) == len(set(paths))
        changed_inputs, input_rows = [], []
        for rel in paths:
            assert not Path(rel).is_absolute() and '..' not in Path(rel).parts and Path(rel).as_posix() == rel
            current = root
            for part in Path(rel).parts:
                current = current / part
                assert not current.is_symlink(), rel
            before = git_body(root, revision, rel)
            after = (root / rel).read_bytes()
            before_sha, after_sha = digest(before), pin(root / rel)
            baseline_pins[f'{root}@{revision}:{rel}'] = before_sha
            input_rows.append({'path': rel, 'before_sha256': before_sha, 'after_sha256': after_sha})
            if before != after:
                changed_inputs.append(rel)
        assert changed_inputs == [note]
        old_fp = fingerprint(paths, lambda rel: git_body(root, revision, rel))
        new_fp = fingerprint(paths, lambda rel: (root / rel).read_bytes())
        assert old_fp != new_fp
        cache_text = (root / cache).read_text()
        old_cache = git_body(root, revision, cache).decode()
        assert digest(old_cache.encode()) == spec['old_cache_sha']
        assert header_fields(old_cache)['input_fingerprint_sha256'] == old_fp
        assert header_fields(cache_text)['input_fingerprint_sha256'] == new_fp

        ex = execution['result']
        assert ex['runner'] == runner and execution['cache_path'] == str(root / cache)
        assert ex['status'] == 'ok' and ex['exit_code'] == 0
        assert ex['timeout_sec'] == literals['AUDIT_TIMEOUT_SEC']
        assert ex['elapsed_sec'] == frozen['fresh_primary_seconds']
        assert len(ex['stdout']) < 200000 and len(ex['stderr']) == 0
        rebuilt = (
            '===== runner cache v1 =====\n'
            f'runner: {runner}\n'
            f'runner_sha256: {digest(runner_body)}\n'
            f'input_fingerprint_sha256: {new_fp}\n'
            f"timeout_sec: {ex['timeout_sec']}\n"
            f"exit_code: {ex['exit_code']}\n"
            f"elapsed_sec: {ex['elapsed_sec']:.2f}\n"
            f"status: {ex['status']}\n"
            '----- stdout -----\n'
            f"{ex['stdout']}\n"
            '----- stderr -----\n'
            f"{ex['stderr']}\n"
        )
        assert rebuilt.encode() == (root / cache).read_bytes()
        objects, encoded_objects, rem = [], [], ex['stdout']
        while rem.lstrip().startswith('{'):
            rem = rem.lstrip()
            value, end = json.JSONDecoder().raw_decode(rem)
            objects.append(value)
            encoded_objects.append(rem[:end])
            rem = rem[end:]
        assert len(objects) == frozen['stdout_objects'] == spec['object_count']
        assert rem.strip() == spec['total']
        result_bytes = (root / result).read_bytes()
        assert encoded_objects[-1].encode() + b'\n' == result_bytes
        aggregate = json.loads(result_bytes)
        assert objects[-1] == aggregate and aggregate['source_sha256'] == digest(runner_body)
        if label == 'SEVENTH':
            assert objects[:3] == aggregate['actual_spin_one']['rows']
        old_result_bytes = git_body(root, revision, result)
        assert digest(old_result_bytes) == spec['old_result_sha']
        changed = differences(json.loads(old_result_bytes), aggregate)
        assert len(changed) == spec['timing_difference_count']
        assert all(item['path'][-1] == 'elapsed_seconds' for item in changed)
        assert frozen['scientific_results_equal_original_except_timings'] is True
        api_sha = pin(root / 'scripts/runner_cache.py')
        assert api_sha == '1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2'

        reports[label] = {
            'publication_tree': str(root), 'comparison_base_and_observed_HEAD': revision,
            'prior_comparison_anchor_seal_sha256': spec['anchor_seal'],
            'prior_anchor_members_preserved': len(members),
            'committed_note_result_and_cache_match_prior_scientific_comparison': True,
            'only_note_delta_is_exact_visible_metadata_replacement': True,
            'all_mathematics_and_conditional_audit_caveats_unchanged': True,
            'runner_byte_identical_to_committed_source': True,
            'declared_inputs': input_rows,
            'only_changed_declared_input': note,
            'old_declared_input_fingerprint_sha256': old_fp,
            'fresh_declared_input_fingerprint_sha256': new_fp,
            'full_cache_byte_reconstruction_matches': True,
            'cache_bytes': len(rebuilt.encode()),
            'execution_status': ex['status'], 'execution_exit_code': ex['exit_code'],
            'execution_elapsed_seconds': ex['elapsed_sec'], 'timeout_seconds': ex['timeout_sec'],
            'complete_merged_stdout_characters': len(ex['stdout']),
            'complete_merged_stdout_sha256': digest(ex['stdout'].encode()),
            'complete_stdout_JSON_objects': len(objects),
            'progress_object_count': len(objects) - 1,
            'progress_objects_match_final_rows': True if label == 'SEVENTH' else None,
            'final_stdout_JSON_plus_newline_byte_identical_to_result': True,
            'complete_stream_remainder': rem.strip(),
            'API_separate_stderr_field_bytes': 0,
            'API_merges_process_stderr_into_stdout': True,
            'scientific_values_exactly_unchanged': True,
            'complete_recursive_result_differences': changed,
            'physics_primary_rerun_by_checker': False,
        }
    pins_payload = {
        'scope': 'Metadata-only follow-up and fresh execution/cache correspondence; prior reports are comparison anchors only.',
        'source_and_evidence_sha256': pins,
        'committed_baseline_blob_sha256': baseline_pins,
    }
    evidence = {
        'reports': reports,
        'new_blind_scientific_review_claim': False,
        'physics_primaries_executed_or_imported': False,
        'prior_seals_changed': False,
        'publication_or_audit_state_changed': False,
        'other_active_scientific_packets_read': False,
        'citation_manifest_review_in_scope': False,
        'writes_confined_to_new_assigned_directory': True,
    }
    (OUT / 'METADATA_REPAIR_SOURCE_PINS.json').write_text(json.dumps(pins_payload, indent=2) + '\n')
    (OUT / 'METADATA_REPAIR_EVIDENCE.json').write_text(json.dumps(evidence, indent=2) + '\n')
    print(json.dumps(evidence, indent=2))


if __name__ == '__main__':
    main()
