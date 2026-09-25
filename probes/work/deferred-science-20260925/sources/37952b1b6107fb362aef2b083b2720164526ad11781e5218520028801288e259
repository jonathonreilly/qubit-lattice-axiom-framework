"""Read-only comparison of milestone-six publication and its frozen evidence.

Does not run the primary, execute cube controls, write caches, or alter sources.
The small new author local-star function is replayed by AST extraction; this is
source consistency, not a new independent mathematical reconstruction.
"""
from pathlib import Path
import ast
import hashlib
import itertools
import json

import sympy as sp

BASE = Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth')
PUB = BASE / 'integrated-variance-publication'
IND = BASE / 'averaged-variance-independent'
AUTHOR = BASE / 'averaged-variance-personal'
NOTE_REL = 'docs/TIME_INTEGRATED_MICROSCOPIC_CUBE_BIRTH_VARIANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER_REL = 'scripts/time_integrated_microscopic_cube_birth_variance_2026_09_24.py'
CACHE_REL = 'logs/runner-cache/time_integrated_microscopic_cube_birth_variance_2026_09_24.txt'
RESULT_REL = 'outputs/integrated_cube_birth_variance_20260924/INTEGRATED_VARIANCE_CONTROL_RESULTS.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path):
    return json.loads(path.read_text())


def verify(path, expected):
    actual = digest(path)
    assert actual == expected, (str(path), actual, expected)
    return actual


frozen = read_json(PUB / 'SIXTH_PUBLICATION_FROZEN_SOURCES.json')
assert frozen['base_revision'] == 'c234d47c9d99b7fd5590957ec08d9083877d25e6'
assert frozen['files_sha256'] == {
    NOTE_REL: 'f667f03f5b6b9fd1e50e3c01f800e19d754dae8281354ff2d0196d97ddbd44ae',
    RUNNER_REL: '1482440722ca5c91dea2067b0c0ba2024c1c2a31ea93bf1736fe62c5fcaa48bc',
}
for name, expected in frozen['files_sha256'].items():
    verify(PUB / name, expected)

runner_tree = ast.parse((PUB / RUNNER_REL).read_text())
functions = {node.name: node for node in runner_tree.body if isinstance(node, ast.FunctionDef)}
declaration = next(node for node in runner_tree.body if isinstance(node, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == 'AUDIT_INPUT_PATHS' for t in node.targets))
declared_paths = ast.literal_eval(declaration.value)
assert len(declared_paths) == len(set(declared_paths)) == 5
fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
input_hashes = {}
for name in declared_paths:
    relative = Path(name)
    assert not relative.is_absolute() and '..' not in relative.parts
    data = (PUB / name).read_bytes()
    encoded_name = name.encode()
    fingerprint.update(len(encoded_name).to_bytes(8, 'big'))
    fingerprint.update(encoded_name)
    fingerprint.update(len(data).to_bytes(8, 'big'))
    fingerprint.update(data)
    input_hashes[name] = hashlib.sha256(data).hexdigest()

cache = (PUB / CACHE_REL).read_text()
header_text, body = cache.split('----- stdout -----\n', 1)
stdout, stderr = body.split('\n----- stderr -----\n', 1)
header = dict(line.split(': ', 1) for line in header_text.splitlines()[1:] if line)
assert header['runner'] == RUNNER_REL
assert header['runner_sha256'] == digest(PUB / RUNNER_REL)
assert header['input_fingerprint_sha256'] == fingerprint.hexdigest()
assert header['status'] == 'ok' and header['exit_code'] == '0'
assert header['timeout_sec'] == '240' and header['elapsed_sec'] == '47.67'
assert not stderr.strip()
assert len(stdout) < 200000
decoder = json.JSONDecoder()
remaining = stdout.lstrip()
objects = []
while remaining.startswith('{'):
    value, end = decoder.raw_decode(remaining)
    objects.append(value)
    remaining = remaining[end:].lstrip()
assert len(objects) == 4 and remaining.strip() == 'TOTAL: PASS=4 FAIL=0'
result = read_json(PUB / RESULT_REL)
assert objects[3] == result
assert objects[:3] == result['actual_cube_low']['rows']
assert result['source_sha256'] == digest(PUB / RUNNER_REL)

execution = read_json(BASE / 'SIXTH_PUBLICATION_CACHE_EXECUTION.json')
verify(PUB / CACHE_REL, execution['cache_sha256'])
verify(PUB / RESULT_REL, execution['result_sha256'])
verify(BASE / 'SIXTH_CACHE_EXECUTION.log', execution['wrapper_log_sha256'])
assert execution['cache_header'] == {
    'runner_path': header['runner'],
    'runner_sha256': header['runner_sha256'],
    'input_fingerprint_sha256': header['input_fingerprint_sha256'],
    'status': header['status'],
    'exit_code': header['exit_code'],
}
assert execution['elapsed_sec'] == 47.67
assert execution['stderr_empty'] and execution['complete_stdout_json_objects'] == 4
assert execution['all_stdout_matched_result']
assert 'TypeError: vars() argument must have __dict__ attribute' in (BASE / 'SIXTH_CACHE_EXECUTION.log').read_text()

old_words = read_json(AUTHOR / 'SECOND_BIRTH_WORD_RESULTS.json')
old_controls = read_json(AUTHOR / 'VARIANCE_CONTROL_RESULTS.json')
assert result['original_words']['rows'] == old_words['rows']
assert result['three_grade'] == old_controls['three_grade']


def drop_timings(value):
    if isinstance(value, dict):
        return {key: drop_timings(item) for key, item in value.items() if key != 'elapsed_seconds'}
    if isinstance(value, list):
        return [drop_timings(item) for item in value]
    return value


assert drop_timings(result['actual_cube_low']['rows']) == drop_timings(old_controls['actual_cube_low']['rows'])
assert result['actual_cube_low']['scope'] == old_controls['actual_cube_low']['scope']
assert execution['all_reused_scientific_values_identical_except_timings']

builder_path = BASE / 'ordinary-energy-publication/scripts/ordinary_microscopic_cube_energy_after_birth_layer_2026_09_24.py'
verify(builder_path, '4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d')
builder_functions = {n.name: n for n in ast.parse(builder_path.read_text()).body if isinstance(n, ast.FunctionDef)}
builder_names = ['complete_spin_one', 'jump_matrix', 'canonical_preparation', 'riesz_action']
for name in builder_names:
    assert ast.dump(functions[name], include_attributes=False) == ast.dump(builder_functions[name], include_attributes=False)
control_functions = {n.name: n for n in ast.parse((AUTHOR / 'variance_controls.py').read_text()).body if isinstance(n, ast.FunctionDef)}
for name in ['exponential_integral', 'three_grade_controls']:
    assert ast.dump(functions[name], include_attributes=False) == ast.dump(control_functions[name], include_attributes=False)

# Read-only replay of the new small publication control, without importing or
# executing the runner's main entry or any cube construction.
A = (0, 3, 5, 6)
B = (1, 2, 4, 7)
EDGES = tuple((a, b) for a in A for b in B if a ^ b in (1, 2, 4))
local_module = ast.Module(body=[functions['local_star_controls']], type_ignores=[])
namespace = {'A': A, 'B': B, 'EDGES': EDGES, 'sp': sp, 'itertools': itertools}
exec(compile(local_module, str(PUB / RUNNER_REL), 'exec'), namespace)
replayed_local = namespace['local_star_controls']()
replayed_local_json = json.loads(json.dumps(replayed_local, default=int))
assert replayed_local_json == result['local_rotor_loss']

pre = read_json(IND / 'FINITE_CHECKS.json')
local = result['local_rotor_loss']
assert local['local_blocks'][0]['hop_matrix'] == pre['same_sign_F']
assert local['local_blocks'][0]['Gram_eigenvalues'] == pre['same_sign_Gram_spectrum']
assert local['local_blocks'][1]['Gram_eigenvalues'] == pre['opposite_sign_Gram_spectrum']
assert local['cover_counts'] == pre['cover_counts']
pre_cover = {(tuple(row['vacant_B']), row['q'].index(-1)):
             (row['active_A'], row['negative_outside_local_pair_count'])
             for row in pre['complete_cover_rows']}
publication_cover = {(tuple(row['vacant_B']), row['negative_site']):
                     (row['active_A'], row['same_sign_centers']) for row in local['cover']}
assert len(pre_cover) == len(publication_cover) == 36 and pre_cover == publication_cover

# Existing sealed independent evidence remains unchanged.
verify(IND / 'PRE.md', '57819426fec612dcb000612dcb8419cca34d3538904dcaefea13fb4820181d8e')
verify(IND / 'PRE_SEAL.json', '35101d25eaf758e0d1f82abcfa6eda7e86779bd5f5d16cca6ffcb514b1924450')
verify(IND / 'POST.md', '5a53e72b0efa31bfd73d3d94246378a7748cf0e71f7f1f28a3ef374334e5f9d5')
verify(IND / 'POST_SEAL.json', 'cc44f74754512cd5dd7b6b7d2d24559fdf18244fe7c3b842df7b8cdd5ce02665')
for seal_name in ['PRE_SEAL.json', 'POST_SEAL.json']:
    seal = read_json(IND / seal_name)
    for name, expected in seal.get('evidence_hashes', seal.get('files', {})).items():
        verify(IND / name, expected)

report = {
    'kind': 'source_and_completed_cache_comparison_not_new_blind_reconstruction',
    'publication_note_sha256': digest(PUB / NOTE_REL),
    'publication_runner_sha256': digest(PUB / RUNNER_REL),
    'source_fingerprint_independently_recomputed': fingerprint.hexdigest(),
    'declared_input_sha256': input_hashes,
    'cache_sha256': digest(PUB / CACHE_REL),
    'result_sha256': digest(PUB / RESULT_REL),
    'cache_status': 'fresh_success',
    'primary_exit_code': 0,
    'primary_elapsed_seconds_recorded': 47.67,
    'complete_stdout_json_objects': len(objects),
    'all_stdout_objects_match_result': True,
    'complete_stdout_without_truncation': True,
    'stderr_empty': True,
    'post_execution_wrapper_exception_preserved': True,
    'unchanged_builder_function_ASTs': builder_names,
    'toy_functions_AST_unchanged': True,
    'reused_word_and_toy_scientific_results_identical': True,
    'reused_cube_scientific_results_identical_except_timings': True,
    'new_author_local_star_control_replay_matches_cache': True,
    'local_Gram_spectra_match_preserved_PRE': True,
    'all_36_local_cover_rows_match_preserved_PRE': True,
    'primary_or_cube_controls_rerun': False,
    'publication_or_cache_mutated': False,
    'PRE_POST_and_sealed_evidence_unchanged': True,
    'verification_script_sha256': digest(Path(__file__)),
}
(IND / 'PUBLICATION_EVIDENCE_VERIFICATION.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
