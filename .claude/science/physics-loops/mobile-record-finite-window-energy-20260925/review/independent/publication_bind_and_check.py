"""Read-only final-source and complete stored-payload correspondence.

No scientific runner, cache helper, matrix exponential, or eigensystem is
imported or executed. This program writes only its JSON report to stdout.
The cache fingerprint serialization is independently transcribed from the
separately released and pinned runner_cache.py tooling.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import ast
import difflib
import hashlib
import json
import stat
import subprocess

HERE = Path(__file__).resolve().parent
FROZEN = HERE / 'publication_frozen'
TREE = FROZEN / 'worktree'
META = FROZEN / 'metadata'
BASE = '60c5f194d940a7bbaf1cdd545296e31d74a02f1a'
EXPECTED_FINGERPRINT = 'f82ab9b31c1b7e8dc17b5009f3d58f50bb4c01d4266a4643a208a89a52b51f35'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def sha(path):
    return digest(path.read_bytes())


def load(path):
    return json.loads(path.read_text())


def check_file(path, record):
    assert path.is_file(), str(path)
    assert path.stat().st_size == record['bytes'], str(path)
    assert sha(path) == record['sha256'], str(path)


def assignments(source):
    result = {}
    for node in ast.parse(source).body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id in {
                    'AUDIT_TIMEOUT_SEC', 'AUDIT_INPUT_PATHS', 'RESULT_PATH', 'RUNTIME'
                }:
                    result[target.id] = ast.literal_eval(node.value)
    return result


def compare_leaves(old, new, path, counts, elapsed_changes):
    assert type(old) is type(new), (path, type(old).__name__, type(new).__name__)
    if isinstance(old, dict):
        assert list(old) == list(new), path
        for key in old:
            if path in {'root_generic', 'independent_native'} and key == 'elapsed_seconds':
                assert isinstance(old[key], float) and isinstance(new[key], float)
                elapsed_changes.append({'path': path + '/' + key, 'historical': old[key], 'fresh': new[key]})
            else:
                compare_leaves(old[key], new[key], path + '/' + key, counts, elapsed_changes)
    elif isinstance(old, list):
        assert len(old) == len(new), path
        for i, (a, b) in enumerate(zip(old, new)):
            compare_leaves(a, b, path + '/' + str(i), counts, elapsed_changes)
    else:
        assert old == new, (path, old, new)
        counts[type(old).__name__] += 1


def main():
    pins = load(HERE / 'PUBLICATION_SOURCE_PINS.json')
    assert len(pins['origins']) == 14
    work = Path(pins['publication_root'])
    for source in pins['origins']:
        check_file(HERE / source['frozen'], source)
        check_file(Path(source['origin']), source)

    seal_counts = {}
    expected_seals = {
        'PRE_SEAL.json': '75bdc5d36dad74adf96285cefb0896539466f4e14c179cecc30f9afe5dbbf4ca',
        'POST_SEAL.json': '5c8cf25f153a2e8d2ece143e22afa95242c93e1ebfe137efa005809c2617b6a0'
    }
    for name, expected in expected_seals.items():
        assert sha(HERE / name) == expected
        seal = load(HERE / name)
        for member in seal['members']:
            check_file(HERE / member['path'], member)
        assert len(seal['members']) == seal['member_count']
        seal_counts[name] = seal['member_count']
    assert seal_counts == {'PRE_SEAL.json': 25, 'POST_SEAL.json': 20}

    manifest = load(META / 'FINITE_WINDOW_ENERGY_PUBLICATION_FROZEN_SOURCES.json')
    assert manifest['base_revision'] == pins['base_revision'] == BASE
    assert len(manifest['files_sha256']) == 9
    for rel, expected in manifest['files_sha256'].items():
        assert sha(TREE / rel) == sha(work / rel) == expected, rel

    parent_rows = []
    for rel in manifest['parent_paths']:
        raw = subprocess.run(['git', '-C', str(work), 'show', BASE + ':' + rel],
                             capture_output=True, check=True).stdout
        assert raw == (TREE / rel).read_bytes() == (HERE / 'sources' / rel).read_bytes(), rel
        parent_rows.append({'path': rel, 'revision': BASE, 'sha256': digest(raw), 'bytes': len(raw)})

    runtime_rows = []
    baseline_sources = [HERE / 'post_frozen_author' / 'finite_window_energy_controls.py',
                        HERE / 'primitive_energy_control.py']
    for row, baseline in zip(manifest['origins'], baseline_sources):
        raw = (TREE / row['publication']).read_bytes()
        assert raw == baseline.read_bytes() == Path(row['origin']).read_bytes()
        assert digest(raw) == row['sha256']
        runtime_rows.append({**row, 'sealed_baseline': str(baseline), 'byte_identical': True})

    wrapper = TREE / manifest['runner']
    values = assignments(wrapper.read_text())
    assert values['AUDIT_TIMEOUT_SEC'] == 120
    assert values['RESULT_PATH'] == manifest['result']
    assert values['RUNTIME'] == manifest['runtime']
    declared = values['AUDIT_INPUT_PATHS']
    assert isinstance(declared, tuple) and len(declared) == 6
    assert list(declared) == [manifest['note'], *manifest['parent_paths'], *manifest['runtime']]
    assert len(set(declared)) == len(declared)
    fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    input_rows = []
    for rel in declared:
        path = Path(rel)
        assert not path.is_absolute() and '..' not in path.parts and path.as_posix() == rel
        component = work
        for part in path.parts:
            component /= part
            assert not stat.S_ISLNK(component.lstat().st_mode), str(component)
        raw = (TREE / rel).read_bytes()
        assert raw == (work / rel).read_bytes()
        label = rel.encode('utf-8')
        fingerprint.update(len(label).to_bytes(8, 'big'))
        fingerprint.update(label)
        fingerprint.update(len(raw).to_bytes(8, 'big'))
        fingerprint.update(raw)
        input_rows.append({'path': rel, 'sha256': digest(raw), 'bytes': len(raw)})
    input_fingerprint = fingerprint.hexdigest()
    assert input_fingerprint == EXPECTED_FINGERPRINT

    result_path = TREE / manifest['result']
    result_bytes = result_path.read_bytes()
    result = json.loads(result_bytes)
    assert result['source_sha256'] == sha(wrapper)
    assert result['all_assertions_passed'] is True
    assert list(result['payload']) == ['root_generic', 'independent_native']
    assert len(result['stages']) == 2
    assert len(result_bytes) == 65487
    elapsed_changes = []
    counts = Counter()
    per_program = {}
    baselines = {
        'root_generic': HERE / 'post_frozen_author' / 'FINITE_WINDOW_ENERGY_RESULTS.json',
        'independent_native': HERE / 'CONTROL_ATTEMPT_01_STDOUT.json'
    }
    reconstructed_stage_stdout = []
    for (key, baseline), stage, source in zip(baselines.items(), result['stages'], runtime_rows):
        old, new = load(baseline), result['payload'][key]
        local_counts = Counter()
        compare_leaves(old, new, key, local_counts, elapsed_changes)
        counts.update(local_counts)
        per_program[key] = dict(local_counts)
        assert new['source_sha256'] == stage['code_sha256'] == source['sha256']
        assert stage['program'] == Path(source['publication']).name
        assert stage['exit_code'] == stage['stderr_bytes'] == 0
        serialized = (json.dumps(new, indent=2, allow_nan=False) + '\n').encode('utf-8')
        assert len(serialized) == stage['stdout_bytes']
        assert digest(serialized) == stage['stdout_sha256']
        reconstructed_stage_stdout.append({'program': stage['program'], 'sha256': digest(serialized),
                                           'bytes': len(serialized), 'historical_result_sha256': sha(baseline)})
    assert dict(counts) == {'str': 464, 'int': 232, 'bool': 8, 'float': 410}
    assert len(elapsed_changes) == 2

    execution = load(META / 'FINITE_WINDOW_ENERGY_PUBLICATION_CACHE_EXECUTION.json')
    assert execution['runner'] == manifest['runner']
    assert execution['status'] == 'ok' and execution['exit_code'] == 0
    assert execution['stderr'] == '' and execution['timeout_sec'] == 120
    assert execution['stdout'].encode('utf-8') == result_bytes + b'TOTAL_PASS: 2\n'
    # This record is far shorter than the helper's 200,000-character stdout tail.
    assert len(execution['stdout']) < 200000
    header = ('===== runner cache v1 =====\n'
              f"runner: {manifest['runner']}\n"
              f'runner_sha256: {sha(wrapper)}\n'
              f'input_fingerprint_sha256: {input_fingerprint}\n'
              f"timeout_sec: {execution['timeout_sec']}\n"
              f"exit_code: {execution['exit_code']}\n"
              f"elapsed_sec: {execution['elapsed_sec']:.2f}\n"
              f"status: {execution['status']}\n"
              '----- stdout -----\n')
    expected_cache = (header + execution['stdout'] + '\n----- stderr -----\n' + execution['stderr'] + '\n').encode('utf-8')
    cache_bytes = (TREE / manifest['cache']).read_bytes()
    assert cache_bytes == expected_cache

    receipt = load(META / 'FINITE_WINDOW_ENERGY_PRIMARY_ROOT_VERIFICATION.json')
    assert receipt['all_payload_leaf_counts'] == dict(counts)
    assert receipt['source_identity'] == manifest['origins']
    assert receipt['scientific_differences'] == []
    failure = load(META / 'FINITE_WINDOW_ENERGY_PRIMARY_VERIFICATION_ATTEMPT01_FAILURE.json')
    assert 'CONTROL_ATTEMPT01_STDOUT.json' in failure['failure']
    assert 'CONTROL_ATTEMPT_01_STDOUT.json' in failure['failure']

    public = (TREE / manifest['note']).read_text()
    author = (HERE / 'post_frozen_author' / 'FINITE_WINDOW_MICROSCOPIC_ENERGY_MEASURES_ROOT.md').read_text()
    pre = (HERE / 'PRE.md').read_text()
    author_core = author[author.index('## 1.'):].strip()
    public_core = public[public.index('## 1.'):public.index('\n## 7.')].strip()
    expected_core = author_core.replace('sum_(a<c)', 'sum_(a<c, distance(a,c)=2)')
    expected_core = expected_core.replace('A finite continuous energy-response function', 'A fixed bounded continuous energy-response function')
    expected_core = expected_core.replace('This is a proposed conditional theorem and exact illustrative counterexample.\nIt must undergo selective independent reconstruction before publication.',
        'The conditional theorem and illustrative counterexample have a sealed independent\nPRE and released-source POST within the scope recorded above. No retained audit\nstatus or physical energy identification is inferred.')
    assert public_core == expected_core
    pre_section = pre[pre.index('## 5.'):pre.index('\n## 6.')].strip()
    public_native = public[public.index('## 7.'):public.index('\n## Evidence and remaining physical obligations')].strip()
    expected_native = pre_section.replace('## 5. Exact physical counterexample: vanishing spectral mass, divergent energy',
        '## 7. Independent native counterexample\n\nThis section is adapted from the sealed independent PRE, with its provenance retained.\n')
    expected_native = expected_native.replace('graph of P2--P3.', 'graph of the common-law and local-pair parents.')
    expected_native = expected_native.replace("hence P3 gives H4=0; direct computation of all terms in P1's coefficient agrees.",
        "hence the local-pair identity gives H4=0; direct computation of all terms in the bounded-compensation parent's coefficient agrees.")
    expected_native = expected_native.replace('The run completed in 0.44775387505069375 external seconds',
        'The sealed independent PRE run completed in 0.44775387505069375 external seconds')
    assert public_native == expected_native
    assert 'that additional general theorem is not needed for the deterministic\nreadout result below.' in public
    text_deltas = {
        'root_core': ''.join(difflib.unified_diff(author_core.splitlines(keepends=True), public_core.splitlines(keepends=True),
                                                 fromfile='sealed_root_sections1to6', tofile='public_sections1to6')),
        'native': ''.join(difflib.unified_diff(pre_section.splitlines(keepends=True), public_native.splitlines(keepends=True),
                                              fromfile='sealed_PRE_Section5', tofile='public_Section7'))
    }

    generic = result['payload']['root_generic']
    native = result['payload']['independent_native']
    print(json.dumps({
        'checked_utc': datetime.now(timezone.utc).isoformat(),
        'scope': __doc__, 'checker_sha256': sha(Path(__file__)),
        'source_pins_sha256': sha(HERE / 'PUBLICATION_SOURCE_PINS.json'),
        'preserved_seals': expected_seals, 'preserved_member_counts': seal_counts,
        'nine_publication_bindings_verified': 9, 'external_metadata_bindings_verified': 4,
        'separate_tooling_bindings_verified': 1, 'total_current_origins_verified': 14,
        'parent_git_bindings': parent_rows, 'runtime_exact_byte_correspondence': runtime_rows,
        'tooling_sha256': sha(FROZEN / 'tooling' / 'runner_cache.py'),
        'tool_functions_read_not_called': ['declared_input_paths', 'declared_input_fingerprint', '_lexical_path_stat_tokens',
                                          'runner_sha256', 'parse_cache_header', 'write_cache'],
        'declared_inputs_in_order': input_rows, 'input_fingerprint_sha256': input_fingerprint,
        'fingerprint_recomputed_without_import': True,
        'full_payload_leaf_counts': dict(counts), 'per_program_leaf_counts': per_program,
        'excluded_elapsed_fields_only': elapsed_changes, 'scientific_differences': [],
        'stage_stdout_exactly_reconstructed': reconstructed_stage_stdout,
        'result_sha256': digest(result_bytes), 'result_bytes': len(result_bytes),
        'cache_sha256': digest(cache_bytes), 'cache_bytes': len(cache_bytes),
        'full_cache_equals_reconstructed_header_stdout_stderr': True,
        'execution_embedded_stdout_equals_result_plus_pass_marker': True,
        'cache_header': header, 'execution_seconds': execution['elapsed_sec'],
        'wrapper_seconds': result['elapsed_seconds'], 'stage_records': result['stages'],
        'root_receipt_agrees_with_own_complete_comparison': True,
        'historical_root_path_lookup_failure': failure,
        'public_text_exact_scoped_transformations_verified': True, 'complete_text_deltas': text_deltas,
        'row_coverage': {
            'root_spectrum': len(generic['spectrum_rows']), 'root_first_event': len(generic['first_event_rows']),
            'root_characteristic': sum('time_parameter' in row for row in generic['response_rows']),
            'root_soft_and_interval': sum('soft_response' in row for row in generic['response_rows']),
            'native_structure': len(native['structure_rows']), 'native_energy_event': len(native['energy_and_event_rows']),
            'native_bounded_formula_tests': sum(len(row['bounded_tests']) for row in native['energy_and_event_rows']),
            'native_initial_layer': len(native['boundary_layer_rows']),
            'native_separate_abstract_examples': len(native['separate_abstract_operator_examples']),
            'all_primitive_words_and_matrices_compared': True
        },
        'author_and_primary_programs_imported_or_executed': [],
        'cache_helper_imported_or_called': False,
        'new_independent_scientific_reconstruction': False,
        'other_active_science_opened': [],
        'limitations': ['Source/output correspondence does not independently rerun the scientific calculation.',
                       'Fresh execution uses the exact earlier root and independent programs; independence belongs to the sealed PRE history.',
                       'A first combined metadata display was truncated; all payload and metadata were subsequently read in complete bounded batches.'],
        'binding_failures': []
    }, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
