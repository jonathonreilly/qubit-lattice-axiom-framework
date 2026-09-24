"""Read-only publication identity/correspondence checks; no physics controls run."""

from pathlib import Path
import ast
import copy
import hashlib
import json
import subprocess


BASE = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth')
PUB = BASE / 'mixed-preparation-publication'
AUTHOR = BASE / 'preparation-uniform-personal'
OUT = BASE / 'preparation-uniform-independent'
NOTE = 'docs/MIXED_LOW_FIELD_INPUTS_RETAIN_CUBE_BIRTH_ENERGY_AND_COHERENCE_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER = 'scripts/mixed_low_field_inputs_cube_birth_energy_and_coherence_2026_09_24.py'
RESULT = 'outputs/mixed_low_field_birth_energy_20260924/MIXED_PREPARATION_CONTROL_RESULTS.json'
CACHE = 'logs/runner-cache/mixed_low_field_inputs_cube_birth_energy_and_coherence_2026_09_24.txt'
EXPECTED = {
    NOTE: '04bf4ad2def6a5d8e7a0ab711d4e6e52d1933eb9d28366b1cdb5dee1383d9726',
    RUNNER: 'ec6abee27fc084839d8c50f8d386ffc20010668bbcb681044ff8be0827bfb802',
    RESULT: '60d3ee81cc9a35b6e396a383f93c95a400b4dd803f3984779d0fe4d178c2d6e1',
    CACHE: '125a86e284d83feee379c89948ff6acd4a511cf222defb7b4fcb812a229a3515',
    'docs/GENERAL_MICROSCOPIC_BIRTH_ENERGY_AND_CUBE_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md': '9e13c659e9a418e9e77e619a3cbd82d371f8219003a92e49fb2cc9ac5f87d6c7',
    'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md': 'af0b8e6494ea54cdb450e430a45e9d89d9e1e931e21b9a74ab2b4ea260a3a718',
    'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md': 'f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9',
    'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md': 'c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b',
    'docs/ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md': '150bd5ba19195a55402d8f74112417f37e168bf50f50dc94d7dcab7d1d3a96a7',
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def main():
    pins = {}
    for rel, expected in EXPECTED.items():
        p = PUB / rel
        pins[str(p)] = sha(p)
        assert pins[str(p)] == expected, rel

    preserved = {}
    seal_specs = (
        (OUT, 'PRE_SEAL.json', 'files', '5acf2efb724fe89e525b25fcadf5b2d27bad3da4a2ca88b7392b1efae9accff1'),
        (OUT, 'POST_SEAL.json', 'files', '704b934d1624f152c9a5bb9a6159fc843337e2bea1481dc31c92e4fe33e05e10'),
        (AUTHOR, 'AUTHOR_SEAL.json', 'files_sha256', '5699fe83bc73bf6947f0b91f80de26bb32c66e6c665b2487ef19361e971c0235'),
        (AUTHOR, 'CONTROL_SEAL.json', 'files_sha256', '0ad1f74ffe289698693788f0483dcf7fa5b3baecf5263093cf8f6f5c0e2bb477'),
    )
    for parent, rel, member_key, expected in seal_specs:
        seal = parent / rel
        assert sha(seal) == expected, rel
        pins[str(seal)] = expected
        members = json.loads(seal.read_text())[member_key]
        for name, expected_member in members.items():
            p = parent / name
            actual = sha(p)
            assert actual == expected_member, str(p)
            pins[str(p)] = actual
        preserved[str(seal)] = {'member_count': len(members), 'all_member_hashes_match': True}

    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=PUB, text=True).strip()
    assert head == 'e846ee9d4133f65d3778fa4dc36524a9ada6db6b', head
    runner_tree = ast.parse((PUB / RUNNER).read_text())
    inputs = None
    for node in runner_tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'AUDIT_INPUT_PATHS' for t in node.targets):
            inputs = ast.literal_eval(node.value)
    assert isinstance(inputs, tuple) and len(inputs) == 6 and len(set(inputs)) == 6
    fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    for rel in inputs:
        raw_name = rel.encode()
        body = (PUB / rel).read_bytes()
        assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
        assert sha(PUB / rel) == EXPECTED[rel]
        fingerprint.update(len(raw_name).to_bytes(8, 'big'))
        fingerprint.update(raw_name)
        fingerprint.update(len(body).to_bytes(8, 'big'))
        fingerprint.update(body)

    cache_text = (PUB / CACHE).read_text()
    header, tail = cache_text.split('----- stdout -----\n', 1)
    stdout, stderr = tail.split('----- stderr -----\n', 1)
    fields = dict(line.split(': ', 1) for line in header.splitlines() if ': ' in line)
    assert fields['runner'] == RUNNER
    assert fields['runner_sha256'] == EXPECTED[RUNNER]
    assert fields['input_fingerprint_sha256'] == fingerprint.hexdigest()
    assert fields['exit_code'] == '0' and fields['status'] == 'ok' and fields['timeout_sec'] == '120'
    assert not stderr.strip()
    assert len(stdout) < 200000
    raw_stdout = stdout.lstrip()
    cache_object, end = json.JSONDecoder().raw_decode(raw_stdout)
    assert raw_stdout[end:].strip() == 'TOTAL: PASS=2 FAIL=0'
    result_text = (PUB / RESULT).read_text()
    result = json.loads(result_text)
    assert cache_object == result
    assert raw_stdout[:end] == result_text.rstrip('\n')
    assert result['source_sha256'] == EXPECTED[RUNNER]

    author_result = json.loads((AUTHOR / 'MIXED_PREPARATION_CONTROL_RESULTS.json').read_text())
    actual_science, author_science = copy.deepcopy(result), copy.deepcopy(author_result)
    ignored_fields = ['elapsed_seconds', 'source_sha256']
    for key in ignored_fields:
        actual_science.pop(key)
        author_science.pop(key)
    assert actual_science == author_science
    science_digest = hashlib.sha256(json.dumps(actual_science, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

    author_tree = ast.parse((AUTHOR / 'mixed_preparation_controls.py').read_text())
    def functions(tree):
        return {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    af, pf = functions(author_tree), functions(runner_tree)
    assert set(af) == set(pf)
    identical_functions = []
    for name in af:
        if name == 'main':
            continue
        assert ast.dump(af[name], include_attributes=False) == ast.dump(pf[name], include_attributes=False), name
        identical_functions.append(name)
    adapted_main = copy.deepcopy(pf['main'])
    first, last = adapted_main.body.pop(0), adapted_main.body.pop()
    assert ast.unparse(first) == 'HERE.mkdir(parents=True, exist_ok=True)'
    assert ast.unparse(last) == "print('TOTAL: PASS=2 FAIL=0', flush=True)"
    assert ast.dump(adapted_main, include_attributes=False) == ast.dump(af['main'], include_attributes=False)

    receipt_path = BASE / 'SEVENTH_EIGHTH_PRIMARY_ROOT_VERIFICATION.json'
    pins[str(receipt_path)] = sha(receipt_path)
    receipt = json.loads(receipt_path.read_text())
    matching_reports = {k: v for k, v in receipt['reports'].items() if v.get('output_sha256') == EXPECTED[RESULT]}
    assert len(matching_reports) == 1
    report = next(iter(matching_reports.values()))
    assert report['stdout_objects'] == 1 and report['stderr_bytes'] == 0
    assert report['scientific_values_identical_to_sealed_author_except_timings'] is True
    assert f"{report['elapsed_sec']:.2f}" == fields['elapsed_sec']
    pins[str(PUB / 'scripts/runner_cache.py')] = sha(PUB / 'scripts/runner_cache.py')
    evidence = {
        'kind': 'mixed_preparation_publication_read_only_correspondence_checks',
        'publication_HEAD': head,
        'preserved_seals': preserved,
        'publication_expected_hashes_match': True,
        'all_five_unchanged_parent_hashes_match_PRE_sources': True,
        'declared_input_paths': inputs,
        'recomputed_input_fingerprint_sha256': fingerprint.hexdigest(),
        'cache_header': fields,
        'stdout_characters_in_cache': len(stdout),
        'complete_stdout_json_byte_matches_result_without_terminal_newline': True,
        'stdout_json_object_count': 1,
        'stdout_tail': 'TOTAL: PASS=2 FAIL=0',
        'cache_stderr_whitespace_only': True,
        'root_receipt_matching_report': matching_reports,
        'all_scientific_values_exactly_match_frozen_author_result': True,
        'only_ignored_result_fields': ignored_fields,
        'canonical_scientific_values_sha256': science_digest,
        'AST_identical_computational_functions': identical_functions,
        'main_AST_identical_after_removing_output_mkdir_and_TOTAL_print': True,
        'physics_controls_rerun': False,
        'runner_imported_or_executed': False,
        'other_active_scientific_packets_read': False,
        'writes_confined_to_assigned_independent_directory': True,
    }
    dump(OUT / 'PUBLICATION_COMPARISON_SOURCE_PINS.json', {
        'source_and_evidence_hashes': pins,
        'publication_HEAD': head,
        'scope': 'Final publication comparison against sealed PRE/POST; no new independent derivation or formal audit.',
    })
    dump(OUT / 'PUBLICATION_EVIDENCE_VERIFICATION.json', evidence)
    print(json.dumps(evidence, indent=2))


if __name__ == '__main__':
    main()
