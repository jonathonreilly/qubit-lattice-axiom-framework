#!/usr/bin/env python3
"""Read-only publication/source/cache correspondence. Runs no scientific builder."""
from pathlib import Path
import ast
import copy
import difflib
import hashlib
import json

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'PUBLICATION_sources'
PUB = SNAP / 'publication'
RUNNER = 'scripts/actual_cube_birth_apparatus_coherence_and_energy_range_2026_09_24.py'
NOTE = 'docs/ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def functions(path):
    text = path.read_text()
    tree = ast.parse(text)
    return text, tree, {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}


class Rename(ast.NodeTransformer):
    def __init__(self, mapping):
        self.mapping = mapping

    def visit_Name(self, node):
        node.id = self.mapping.get(node.id, node.id)
        return node

    def visit_FunctionDef(self, node):
        node.name = self.mapping.get(node.name, node.name)
        return self.generic_visit(node)


class RemoveBuilderPrefix(ast.NodeTransformer):
    def visit_Attribute(self, node):
        if isinstance(node.value, ast.Name) and node.value.id == 'builder':
            assert node.attr in {'complete_spin_one', 'jump_matrix', 'canonical_preparation'}
            return ast.copy_location(ast.Name(id=node.attr, ctx=node.ctx), node)
        return self.generic_visit(node)


def dump(node):
    return ast.dump(node, include_attributes=False)


def source_correspondence():
    final_text, final_tree, final = functions(PUB / RUNNER)
    origin_text, origin_tree, origin = functions(SNAP / 'extraction_origin/ordinary_microscopic_cube_energy_after_birth_layer_2026_09_24.py')
    author_text, _, author = functions(HERE / 'POST_sources/coherence_controls.py')
    range_text, _, range_functions = functions(SNAP / 'author_range/range_controls.py')
    rows = []
    for group, src, src_text, names in [
        ('prior cube definitions', origin, origin_text, ['complete_spin_one', 'jump_matrix', 'canonical_preparation']),
        ('sealed Fisher author controls', author, author_text, ['fisher', 'trace_norm', 'witness_controls', 'conserving_resource_controls'])]:
        for name in names:
            assert dump(src[name]) == dump(final[name]), name
            exact = ast.get_source_segment(src_text, src[name]) == ast.get_source_segment(final_text, final[name])
            assert exact
            rows.append({'origin': group, 'function': name, 'exact_source_segment_equal': exact})
    def assignment_for(tree, variable):
        return next(n for n in tree.body if isinstance(n, ast.Assign) and
                    any(isinstance(t, ast.Name) and t.id == variable for t in n.targets))
    for variable in ['A', 'B', 'EDGES']:
        assert dump(assignment_for(origin_tree, variable)) == dump(assignment_for(final_tree, variable))
    mapping = {'project': 'range_project', 'trnorm': 'range_trnorm',
               'fisher': 'range_fisher', 'bandwidth': 'coherence_bandwidth'}
    for name in ['project', 'trnorm', 'fisher', 'bandwidth', 'exact_block_frequency_control', 'prepared_output_swap_controls']:
        normalized = Rename(mapping).visit(copy.deepcopy(range_functions[name]))
        target_name = mapping.get(name, name)
        assert dump(normalized) == dump(final[target_name]), name
        rows.append({'origin': 'post-PRE author range controls', 'function': target_name,
                     'AST_equal_after_explicit_helper_renaming': True})
    old_cube = copy.deepcopy(author['actual_cube_controls'])
    # Remove exactly the previously reviewed assert/importlib loader prelude.
    assert len(old_cube.body[:4]) == 4
    assert isinstance(old_cube.body[0], ast.Assert)
    assert isinstance(old_cube.body[3], ast.Expr)
    old_cube.body = old_cube.body[4:]
    old_cube = RemoveBuilderPrefix().visit(old_cube)
    new_cube = copy.deepcopy(final['actual_cube_controls'])
    for node in [old_cube, new_cube]:
        returned = node.body[-1].value
        assert isinstance(returned, ast.Dict)
        retained = [(key, value) for key, value in zip(returned.keys, returned.values)
                    if ast.literal_eval(key) in {'rows', 'scope'}]
        returned.keys = [key for key, value in retained]
        returned.values = [value for key, value in retained]
    assert dump(old_cube) == dump(new_cube)
    cube_diff = list(difflib.unified_diff(
        ast.get_source_segment(author_text, author['actual_cube_controls']).splitlines(),
        ast.get_source_segment(final_text, final['actual_cube_controls']).splitlines(),
        fromfile='sealed author actual_cube_controls', tofile='publication actual_cube_controls', lineterm=''))
    imported = []
    for n in ast.walk(final_tree):
        if isinstance(n, ast.Import): imported += [a.name for a in n.names]
        if isinstance(n, ast.ImportFrom): imported.append(n.module)
    assert set(imported) == {'pathlib', 'hashlib', 'json', 'math', 'time', 'numpy', 'scipy.sparse', 'scipy.sparse.linalg'}
    return {'function_comparisons': rows, 'cube_constants_equal': True,
            'actual_cube_numerical_body_equal_after_loader_and_provenance_changes': True,
            'actual_cube_complete_diff': cube_diff, 'imports': imported}


def cache_correspondence():
    runner_path = PUB / RUNNER
    _, tree, _ = functions(runner_path)
    inputs = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
                  and any(isinstance(t, ast.Name) and t.id == 'AUDIT_INPUT_PATHS' for t in n.targets))
    digest = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    entries = []
    for rel in inputs:
        label = rel.encode('utf-8')
        body = (PUB / rel).read_bytes()
        digest.update(len(label).to_bytes(8, 'big')); digest.update(label)
        digest.update(len(body).to_bytes(8, 'big')); digest.update(body)
        entries.append({'path': rel, 'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()})
    fingerprint = digest.hexdigest()
    execution = json.loads((SNAP / 'external/FIFTH_PUBLICATION_CACHE_EXECUTION.json').read_text())
    result = execution['result']
    assert result['runner'] == RUNNER and result['status'] == 'ok' and result['exit_code'] == 0
    assert result['timeout_sec'] == 180 and result['stderr'] == ''
    cache = PUB / 'logs/runner-cache/actual_cube_birth_apparatus_coherence_and_energy_range_2026_09_24.txt'
    expected_cache = (
        '===== runner cache v1 =====\n'
        f'runner: {RUNNER}\nrunner_sha256: {sha(runner_path)}\n'
        f'input_fingerprint_sha256: {fingerprint}\n'
        f'timeout_sec: {result["timeout_sec"]}\nexit_code: {result["exit_code"]}\n'
        f'elapsed_sec: {result["elapsed_sec"]:.2f}\nstatus: {result["status"]}\n'
        f'----- stdout -----\n{result["stdout"][-200000:]}\n'
        f'----- stderr -----\n{result["stderr"][-50000:]}\n')
    assert cache.read_bytes() == expected_cache.encode('utf-8')
    assert len(result['stdout']) < 200000
    output = json.loads((PUB / 'outputs/actual_birth_coherence_20260924/COHERENCE_RANGE_CONTROL_RESULTS.json').read_text())
    text = result['stdout']; decoder = json.JSONDecoder(); pos = 0; objects = []
    for _ in range(4):
        while text[pos].isspace(): pos += 1
        obj, end = decoder.raw_decode(text, pos); objects.append(obj); pos = end
    assert objects[-1] == output and objects[:3] == output['actual_cube']['rows']
    resolution = text[pos:].strip().splitlines()
    assert len(resolution) == 6
    assert [line.split(':', 1)[0] for line in resolution[:-1]] == ['per_element', 'per_site', 'per_mode', 'per_block', 'lattice_wide']
    assert resolution[-1] == 'TOTAL: PASS=5 FAIL=0'
    assert output['source_sha256'] == sha(runner_path)
    old = json.loads((HERE / 'POST_sources/COHERENCE_CONTROL_RESULTS.json').read_text())
    assert old['phase_witness'] == output['phase_witness']
    assert old['conserving_resource'] == output['conserving_resource']
    def without_elapsed(row): return {k: v for k, v in row.items() if k != 'elapsed_seconds'}
    assert [without_elapsed(row) for row in old['actual_cube']['rows']] == [without_elapsed(row) for row in output['actual_cube']['rows']]
    author_range = json.loads((SNAP / 'author_range/RANGE_CONTROL_RESULTS.json').read_text())
    assert author_range['frequency'] == output['frequency']
    assert author_range['prepared_output_swap'] == output['prepared_output_swap']
    assert (SNAP / 'author_range/RANGE_CONTROL.stdout').read_bytes() == (SNAP / 'author_range/RANGE_CONTROL_RESULTS.json').read_bytes()
    assert not (SNAP / 'author_range/RANGE_CONTROL.stderr').read_bytes()
    return {'declared_inputs_in_order': entries, 'fingerprint': fingerprint,
            'cache_exact_bytes_match_execution_and_actual_input_bytes': True,
            'runner_sha256': sha(runner_path), 'cache_sha256': sha(cache),
            'execution_seconds': result['elapsed_sec'], 'timeout_seconds': result['timeout_sec'],
            'stdout_bytes': len(text.encode()), 'stdout_sha256': hashlib.sha256(text.encode()).hexdigest(),
            'all_four_stdout_JSON_objects_match_results': True, 'resolution_lines': resolution,
            'all_scientific_values_match_prior_author_runs': True}


def prose_and_process():
    result = json.loads((PUB / 'outputs/actual_birth_coherence_20260924/COHERENCE_RANGE_CONTROL_RESULTS.json').read_text())
    row = result['actual_cube']['rows'][-1]
    assert row['epsilon'] == .03
    values = [x['scaled_coefficient'] for x in row['outputs']]
    assert [f'{v:.5f}' for v in values] == ['0.16084', '0.08049', '0.24137']
    assert f'{row["initial_fisher"]:.2f}' == '196.66'
    freq = result['frequency']
    assert freq['apparatus_spectral_diameter'] == 200 and freq['apparatus_coherence_bandwidth'] == 1
    assert f'{freq["apparatus_energy_variance"]:.2f}' == '3394.79'
    assert f'{freq["output_high_energy_probability"]:.3f}' == '0.231'
    assert freq['forbidden_output_coherence_max'] == 0
    for swap in result['prepared_output_swap']:
        assert abs(swap['apparatus_mean_above_ground'] - .04) < 2e-15
    inventory = json.loads((SNAP / 'author_process/N8_LEDGER_SEARCH.json').read_text())
    matches = inventory['matching_ledgers']; paths = [x['path'] for x in matches]
    assert inventory['ledgers_scanned'] == 187 and len(matches) == len(set(paths)) == 30
    six = ['record-matter-block04-20260905', 'record-matter-block05-20260905',
           'record-battery-transport-20260907', 'toe-axiom-closure-block100-record-jump-resource-generator-20260814',
           'conformal-causal-source-repair-block01-20260716',
           'eta-affine-repeat-correction-20260909/bodies/9974a09029ed36dd056f6a01fd9bd3c2de463e3e']
    matched_six = [next(p for p in paths if name in p) for name in six]
    for entry in matches:
        assert all(1 <= hit['line'] <= entry['line_count'] for hit in entry['matches'])
    main = (HERE / 'POST_sources/ACTUAL_BIRTH_COHERENCE_PERSONAL_DERIVATION.md').read_text()
    supplement = (HERE / 'POST_sources/FREQUENCY_RANGE_AND_ONE_INPUT_RELAXATION.md').read_text()
    main = main[main.index('## 1. Exact operational target'):main.index('## 7. Verification obligations')]
    supplement = supplement[supplement.index('## 1. A finite frequency-support lemma'):]
    for old, new in [('## 1.', '## 7.'), ('## 2.', '## 8.'), ('## 3.', '## 9.'), ('## 4.', '## 10.')]:
        supplement = supplement.replace(old, new)
    final = (PUB / NOTE).read_text()
    final_core = final[final.index('## 1. Exact operational target'):final.index('## 11. Verification and limits')]
    difference = ''.join(difflib.unified_diff((main + supplement).splitlines(True), final_core.splitlines(True),
                                            fromfile='sealed root mathematics', tofile='final publication mathematics'))
    (HERE / 'PUBLICATION_MATHEMATICS_DIFF.patch').write_text(difference)
    return {'cube_scaled_values': values, 'input_fisher': row['initial_fisher'],
            'frequency_values': freq, 'swap_means': [x['apparatus_mean_above_ground'] for x in result['prepared_output_swap']],
            'all_empirical_numeric_prose_matches': True,
            'process_inventory_reported_scanned': inventory['ledgers_scanned'],
            'process_inventory_matching_distinct_paths': len(paths), 'six_named_paths_present': matched_six,
            'process_limits': 'The inventory reports 187 scanned but does not enumerate all 187. Its 30 matching paths are counted directly. Six complete ledger reads and the bridge read remain author-reported; no independent historical audit-status verification.'}


def main():
    pins = json.loads((HERE / 'PUBLICATION_SOURCE_PINS.json').read_text())
    for entry in pins['files'].values():
        assert sha(Path(entry['snapshot'])) == entry['sha256']
        assert sha(Path(entry['original'])) == entry['sha256']
    counts = {}
    for name, expected in [('PRE_SEAL.json', 'df11a67f0f37956e98c407a5b50de3e670b939cf2274d2d798c27cc91e98fdc2'),
                           ('POST_SEAL.json', '0094217873a5501e321a3cda4d82fa60cf26b391cee69c7ff8bb8b2ca10a6762')]:
        assert sha(HERE / name) == expected
        seal = json.loads((HERE / name).read_text())
        for rel, expected_sha in seal['files_sha256'].items(): assert sha(HERE / rel) == expected_sha
        counts[name] = len(seal['files_sha256'])
    record = {'source_sha256': sha(Path(__file__)), 'original_and_snapshot_files_revalidated': len(pins['files']),
              'immutable_members_revalidated': counts, 'extraction': source_correspondence(),
              'cache': cache_correspondence(), 'prose': prose_and_process(),
              'scope': 'Deterministic correspondence only. No author scientific runner imported or executed; no new frontier derivation or audit verdict.'}
    (HERE / 'PUBLICATION_CORRESPONDENCE_RESULTS.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
