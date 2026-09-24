#!/usr/bin/env python3
"""Read-only source/cache comparison. Does not import or run either primary."""
import ast
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import subprocess

BASE = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth')
HERE = BASE / 'initial-energy-balance-independent'
PUB = BASE / 'initial-energy-balance-publication'
AUTHOR = BASE / 'initial-energy-balance-personal'
NOTE = 'docs/INITIAL_CUBE_ENERGY_LAYER_AND_EXACT_BAND_BALANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER = 'scripts/initial_cube_energy_layer_and_exact_band_balance_2026_09_24.py'
RESULT = 'outputs/initial_cube_energy_balance_20260924/INITIAL_CUBE_ENERGY_BALANCE_RESULTS.json'
CACHE = 'logs/runner-cache/initial_cube_energy_layer_and_exact_band_balance_2026_09_24.txt'
BASE_REVISION = '28965d2737ee32b01bba972273fa51d399c594e4'
PINS = {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pin(path, expected=None):
    actual = sha(path)
    if expected is not None:
        assert actual == expected, (str(path), actual, expected)
    previous = PINS.setdefault(str(path), actual)
    assert previous == actual, str(path)
    return actual


def read_json(path):
    pin(path)
    return json.loads(path.read_text())


def check_seal(path, expected):
    pin(path, expected)
    seal = read_json(path)
    for name, digest in seal['files'].items():
        pin(path.parent / name, digest)
    return len(seal['files'])


def assignment(tree, name):
    return next(node.value for node in tree.body if isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == name for t in node.targets))


def functions(source, names):
    tree = ast.parse(source)
    return {name: next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == name)
            for name in names}


def main():
    expected_public = {
        NOTE: 'e9d858a9a4c456c42496159c0ec75ce085957641870dc98cdb8cd69aed04629c',
        RUNNER: '3acb32fac4d5de45177fab8b7ca728545e733a1eb44ce7d6ab2778c5c28da34a',
        RESULT: '91ecd9d08bb13d30a172be2b72b5eecdb7023c1c70aecb333cd72faa31e569e8',
        CACHE: 'a2ff8beb93dbb4f762cda3e69af5de05f21e053bcc21a0cb4cc2dda5f6b9f6f3',
        'scripts/runner_cache.py': '1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2',
    }
    for name, digest in expected_public.items():
        pin(PUB / name, digest)
    receipts = {
        'ELEVENTH_PUBLICATION_FROZEN_SOURCES.json': '9a2d596bd3bbf2a9032cd6224bba69feb0754536a5f438baafa78977d43bb435',
        'ELEVENTH_PUBLICATION_CACHE_EXECUTION.json': '7f88081ae2f3953f51ff5b630395b5080119315e674a5206dee9dd7a8c51c66a',
        'ELEVENTH_PRIMARY_ROOT_VERIFICATION.json': '9332df6687c36b159eed68083a742ed0ca8da9c06dbd54a0a8238fe5ff37d193',
    }
    for name, digest in receipts.items():
        pin(BASE / name, digest)
    counts = {
        'PRE': check_seal(HERE / 'PRE_SEAL.json', 'f459870253083462c9448a0f1ca2ea50beb9b954b34bdffd783fe27a08f060f8'),
        'POST': check_seal(HERE / 'POST_SEAL.json', '0c13e98f9aed198fa3079179d8fe03e288c61fa7035aad4e2e824482f7d64075'),
        'root_author': check_seal(AUTHOR / 'AUTHOR_SEAL.json', '498705aaeac3f6cd542ceabe0d0042fc7f301ef6b4e6402c4b56152c8c113513'),
        'root_control': check_seal(AUTHOR / 'CONTROL_SEAL.json', '97be508f590b9ad739d3fe9805dd2fdcbebfeceab9d859cc105de195c646a7ec'),
        'root_addendum': check_seal(AUTHOR / 'MATCHED_DENSITY_SEAL.json', '41b9c52af4702d0d5e77d36ef6ae5a9fdeacfd60b87826b45f6344296fec0849'),
    }
    pin(AUTHOR / 'MATCHED_DENSITY_ROOT_ADDENDUM.md', '663c2b5f5961e5bc10d8c1e268bd4dd49f8b56be65d74ca1e41d146fcdd279cb')
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=PUB, text=True).strip()
    assert head == BASE_REVISION, head
    git_status = subprocess.check_output(['git', 'status', '--short'], cwd=PUB, text=True)
    frozen = read_json(BASE / 'ELEVENTH_PUBLICATION_FROZEN_SOURCES.json')
    assert frozen['base_revision'] == BASE_REVISION
    for name, digest in frozen['files_sha256'].items():
        pin(PUB / name, digest)
    assert frozen['PRE'] == sha(HERE / 'PRE.md')
    assert frozen['POST'] == sha(HERE / 'POST.md')
    assert frozen['root_matched_density_addendum'] == sha(AUTHOR / 'MATCHED_DENSITY_ROOT_ADDENDUM.md')

    public_source = (PUB / RUNNER).read_text()
    public_tree = ast.parse(public_source)
    input_paths = ast.literal_eval(assignment(public_tree, 'AUDIT_INPUT_PATHS'))
    assert len(input_paths) == 7 and len(set(input_paths)) == 7
    d = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    input_records = []
    for name in input_paths:
        path = PUB / name
        digest = pin(path)
        body = path.read_bytes()
        rel = name.encode()
        d.update(len(rel).to_bytes(8, 'big'))
        d.update(rel)
        d.update(len(body).to_bytes(8, 'big'))
        d.update(body)
        parent_equal = None
        pre_equal = None
        if name != NOTE:
            committed = subprocess.check_output(['git', 'show', BASE_REVISION + ':' + name], cwd=PUB)
            assert body == committed, name
            parent_equal = True
            old = HERE / 'sources' / Path(name).name
            if old.exists():
                assert sha(old) == digest, name
                pre_equal = True
            else:
                assert digest == 'b2fe61b2a821fea5cc99e4e87b2d28536673a10cab5c2bed5b51daffa6cc2d9d', name
        input_records.append({'path': name, 'sha256': digest,
                              'equals_base_revision': parent_equal,
                              'equals_preserved_PRE_snapshot': pre_equal})
    fingerprint = d.hexdigest()
    assert fingerprint == 'e69945c2ed29c1e45d80532e6645281408194e8a25ac50253d7d6b1f1cfbd6c7'

    primitive_source = (HERE / 'independent_balance_controls.py').read_text()
    cascade_source = (AUTHOR / 'initial_energy_balance_controls.py').read_text()
    copied_functions = []
    for source, names, label in [
        (primitive_source, ['legal', 'combine', 'hop', 'mark', 'norm2', 'primitive_words'], 'preserved_PRE_primitive'),
        (cascade_source, ['phi_laplace', 'mean', 'controls'], 'released_root_cascade'),
    ]:
        original = functions(source, names)
        public = functions(public_source, names)
        for name in names:
            assert ast.get_source_segment(source, original[name]) == ast.get_source_segment(public_source, public[name]), name
            assert ast.dump(original[name], include_attributes=False) == ast.dump(public[name], include_attributes=False), name
            copied_functions.append({'function': name, 'source': label, 'source_and_AST_identical': True})
    primitive_tree = ast.parse(primitive_source)
    for name in ['A', 'B', 'EDGES', 'OMEGA']:
        assert ast.dump(assignment(primitive_tree, name)) == ast.dump(assignment(public_tree, name)), name
    assert not any(isinstance(n, ast.FunctionDef) and n.name == 'balance_toy' for n in public_tree.body)

    result = read_json(PUB / RESULT)
    primitive_original = read_json(HERE / 'CONTROL_RESULTS.json')['primitive_words']
    cascade_original_full = read_json(AUTHOR / 'INITIAL_ENERGY_BALANCE_CONTROL_RESULTS.json')
    cascade_original = {k: v for k, v in cascade_original_full.items() if k not in ('elapsed_seconds', 'source_sha256')}
    assert result['primitive_words'] == primitive_original
    assert result['cascade'] == cascade_original
    assert result['source_sha256'] == expected_public[RUNNER]
    assert result['provenance'] == {
        'reused_independent_primitive': sha(HERE / 'independent_balance_controls.py'),
        'reused_root_cascade': sha(AUTHOR / 'initial_energy_balance_controls.py')}
    for key, global_name in [('reused_independent_primitive', 'INDEPENDENT_SOURCE_SHA'), ('reused_root_cascade', 'ROOT_SOURCE_SHA')]:
        assert ast.literal_eval(assignment(public_tree, global_name)) == result['provenance'][key]
    assert ast.literal_eval(assignment(public_tree, 'RESULT_PATH')) == RESULT

    execution = read_json(BASE / 'ELEVENTH_PUBLICATION_CACHE_EXECUTION.json')
    recorded = execution['result']
    assert recorded['runner'] == RUNNER and execution['cache_path'] == str(PUB / CACHE)
    assert recorded['exit_code'] == 0 and recorded['status'] == 'ok'
    assert recorded['timeout_sec'] == ast.literal_eval(assignment(public_tree, 'AUDIT_TIMEOUT_SEC')) == 120
    assert recorded['elapsed_sec'] == 0.19647526741027832
    assert recorded['stderr'] == ''
    stdout = recorded['stdout']
    decoder = json.JSONDecoder()
    parsed, end = decoder.raw_decode(stdout)
    assert parsed == result
    assert stdout[end:] == '\nTOTAL: PASS=2 FAIL=0\n'
    assert stdout == (PUB / RESULT).read_text() + 'TOTAL: PASS=2 FAIL=0\n'
    body = (
        '===== runner cache v1 =====\n'
        f'runner: {RUNNER}\n'
        f'runner_sha256: {expected_public[RUNNER]}\n'
        f'input_fingerprint_sha256: {fingerprint}\n'
        f'timeout_sec: {recorded["timeout_sec"]}\n'
        f'exit_code: {recorded["exit_code"]}\n'
        f'elapsed_sec: {recorded["elapsed_sec"]:.2f}\n'
        f'status: {recorded["status"]}\n'
        '----- stdout -----\n'
        f'{stdout[-200000:]}\n'
        '----- stderr -----\n'
        f'{recorded["stderr"][-50000:]}\n'
    )
    assert (PUB / CACHE).read_bytes() == body.encode()
    root_check = read_json(BASE / 'ELEVENTH_PRIMARY_ROOT_VERIFICATION.json')
    for label, name in [('note', NOTE), ('runner', RUNNER), ('result', RESULT), ('cache', CACHE)]:
        assert root_check[label + '_sha256'] == expected_public[name]
    assert root_check['seconds'] == recorded['elapsed_sec']
    assert root_check['scientific_payloads_equal_sealed_sources'] is True
    assert root_check['stdout_exact_result_plus_summary'] is True
    for path, digest in PINS.items():
        assert sha(Path(path)) == digest, 'Changed during comparison: ' + path
    now = datetime.now(timezone.utc).isoformat()
    pins = {'checked_at_utc': now, 'base_revision': head, 'publication_root': str(PUB),
            'source_and_evidence_sha256': dict(sorted(PINS.items())), 'declared_inputs': input_records,
            'scope': 'Released milestone 11 publication/addendum and preserved comparison anchors only; no new primary run or independent derivation claim.'}
    verification = {
        'verified_at_utc': now, 'kind': 'read_only_publication_binding_comparison',
        'base_revision': head, 'git_status_at_check': git_status,
        'all_dispatched_hashes_match': True, 'source_pin_count': len(PINS),
        'all_seal_members_unchanged': counts, 'declared_input_count': len(input_paths),
        'six_transitive_inputs_equal_base_revision': True,
        'five_old_scientific_notes_equal_PRE_snapshots': True,
        'declared_input_fingerprint_sha256': fingerprint, 'cache_bytes_exactly_reconstructed': True,
        'copied_functions': copied_functions, 'primitive_global_ASTs_equal': ['A', 'B', 'EDGES', 'OMEGA'],
        'four_level_PRE_toy_present_in_public_runner': False,
        'full_primitive_payload_equals_PRE': True, 'full_cascade_payload_equals_root_original': True,
        'only_removed_cascade_original_metadata': ['elapsed_seconds', 'source_sha256'],
        'compared_rows': {'primitive': len(result['primitive_words']['rows']),
                          'initial_profile': len(result['cascade']['initial_profile_rows']),
                          'physical_flow': len(result['cascade']['physical_flow_rows']),
                          'distribution': len(result['cascade']['distribution_rows'])},
        'complete_stdout_is_one_exact_result_plus_TOTAL': True, 'stdout_characters': len(stdout),
        'recorded_api_elapsed_sec': recorded['elapsed_sec'], 'recorded_exit_code': recorded['exit_code'],
        'separate_stderr_field_bytes': len(recorded['stderr']),
        'stderr_scope': 'The API merged child stderr into stdout; the complete merged stream has only the exact result JSON and TOTAL summary.',
        'primary_or_controls_rerun': False, 'new_independent_derivation_claim': False,
        'read_only_verifier_imported_any_primary': False, 'all_pins_rechecked_before_write': True,
        'scientific_review': 'See separate PUBLICATION_COMPARISON.md; hash and payload identities are not a new proof or audit verdict.',
    }
    for name, value in [('PUBLICATION_SOURCE_PINS.json', pins), ('PUBLICATION_VERIFICATION.json', verification)]:
        with (HERE / name).open('x') as stream:
            json.dump(value, stream, indent=2)
            stream.write('\n')
    print(json.dumps(verification, indent=2))


if __name__ == '__main__':
    main()
