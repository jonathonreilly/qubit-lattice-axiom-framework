"""Read-only publication identity, AST extraction and saved-runtime checks.

No primary, author control, scientific helper or cache API is imported or run.
Writes only this independent packet's own factual evidence JSON.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import re
import stat
import subprocess

HERE = Path(__file__).resolve().parent
SNAP = HERE/'PUBLICATION_sources'
PUB = HERE.parent/'full-ensemble-energy-publication'
BASE = '55dfb1a8c7924d345d961a7e4763b11f20f1786a'
RUNNER = 'scripts/full_original_cube_ensemble_energy_and_rare_density_2026_09_24.py'
NOTE = 'docs/FULL_ORIGINAL_CUBE_ENSEMBLE_ENERGY_AND_RARE_MATTER_FIELD_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-24.md'
EXPECTED = {
    'note': 'b2fe61b2a821fea5cc99e4e87b2d28536673a10cab5c2bed5b51daffa6cc2d9d',
    'runner': 'ff2af3a1caa0a0e4f4bdef7739a2ecc7cc56024990af0c82312f60d2f033ce9b',
    'result': '603bf4ed4fcb27c1c53d3cbf85a962880a1c6ef38a3e7f2375e1b6ab4a82d35e',
    'cache': '2803e5776faaa9ddf4e33648596386e83021264337c861f52e25b10b5aca93e9',
}


def digest(b): return hashlib.sha256(b).hexdigest()
def sha(p): return digest(p.read_bytes())
def load(p): return json.loads(p.read_text())
def dumped(node): return ast.dump(node, include_attributes=False)
def function_map(tree): return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
def assignment_map(tree):
    return {target.id: n for n in tree.body if isinstance(n, ast.Assign)
            for target in n.targets if isinstance(target, ast.Name)}


def verify_seal(name, expected):
    assert sha(HERE/name) == expected
    seal = load(HERE/name)
    for row in seal['members']:
        path = HERE/row['path']
        assert sha(path) == row['sha256'] and path.stat().st_size == row['bytes']
    return {'path': name, 'sha256': expected, 'unchanged_members': len(seal['members'])}


def main():
    previous = [verify_seal('PRE_SEAL.json', 'ab052a8061d0103417c6ce431d132530951df70eea588e709c31f0f4bbc7995d'),
                verify_seal('POST_SEAL.json', '72d73d581716f85e7f47521aa7acfc40707b46a8bcc119933dcc0d8eeaf975fa')]
    frozen = load(HERE/'PUBLICATION_SOURCE_FREEZE.json')
    for row in frozen['files']:
        p, original = HERE/row['snapshot'], Path(row['source'])
        assert sha(p) == row['sha256'] == sha(original)
        assert p.stat().st_size == row['bytes'] == original.stat().st_size
    runtime = load(HERE/'PUBLICATION_RUNTIME_PIN.json')
    assert sha(HERE/runtime['snapshot']) == runtime['sha256'] == sha(Path(runtime['source']))
    assert frozen['base_revision'] == BASE
    assert sha(SNAP/'worktree'/NOTE) == EXPECTED['note']
    assert sha(SNAP/'worktree'/RUNNER) == EXPECTED['runner']
    note = (SNAP/'worktree'/NOTE).read_text()
    runner_text = (SNAP/'worktree'/RUNNER).read_text()
    publication_tree = ast.parse(runner_text)
    pf = function_map(publication_tree)
    pa = assignment_map(publication_tree)
    input_paths = ast.literal_eval(pa['AUDIT_INPUT_PATHS'].value)
    result_path = ast.literal_eval(pa['RESULT_PATH'].value)
    assert input_paths[0] == NOTE and len(input_paths) == len(set(input_paths)) == 7
    assert ast.literal_eval(pa['AUDIT_TIMEOUT_SEC'].value) == 120
    assert ast.literal_eval(pa['REUSED_SHA'].value) == '8f4320e1cb333098bb3a609b0a95366380ffc7f1c693cffb8342d757fbc7a09a'
    assert ast.literal_eval(pa['ROOT_CONTROL_SHA'].value) == sha(HERE/'POST_sources/full_ensemble_energy_controls.py')

    helper = SNAP/'author_helpers/mixed_preparation_controls.py'
    helper_tree = ast.parse(helper.read_text())
    hf, ha = function_map(helper_tree), assignment_map(helper_tree)
    helper_functions = ['charges', 'weight', 'hop', 'cycle']
    helper_constants = ['A', 'B', 'EDGES', 'INDEX']
    ast_rows = []
    for name in helper_functions:
        assert dumped(pf[name]) == dumped(hf[name])
        ast_rows.append({'name': name, 'source': 'embedded_author_helper',
                         'AST_sha256': digest(dumped(pf[name]).encode()), 'exact_AST_match': True})
    for name in helper_constants:
        assert dumped(pa[name]) == dumped(ha[name])
        ast_rows.append({'name': name, 'source': 'embedded_author_helper_constant',
                         'AST_sha256': digest(dumped(pa[name]).encode()), 'exact_AST_match': True})
    root_tree = ast.parse((HERE/'POST_sources/full_ensemble_energy_controls.py').read_text())
    rf = function_map(root_tree)
    reused_functions = ['vec', 'mat', 'liouville', 'trace_norm', 'realtrace', 'driven_blocks', 'evolving_input_cascade']
    for name in reused_functions:
        assert dumped(pf[name]) == dumped(rf[name])
        ast_rows.append({'name': name, 'source': 'sealed_author_control',
                         'AST_sha256': digest(dumped(pf[name]).encode()), 'exact_AST_match': True})
    # Exactly four root loader statements are replaced by one local namespace.
    author_source_body = rf['source_algebra'].body
    public_source_body = pf['source_algebra'].body
    assert isinstance(author_source_body[0], ast.Assert)
    assert [type(n).__name__ for n in author_source_body[:4]] == ['Assert','Assign','Assign','Expr']
    assert isinstance(public_source_body[0], ast.Assign)
    namespace = public_source_body[0].value
    assert isinstance(namespace, ast.Call) and isinstance(namespace.func, ast.Name) and namespace.func.id == 'SimpleNamespace'
    assert {kw.arg: kw.value.id for kw in namespace.keywords} == {n: n for n in ['cycle','hop','INDEX','charges','weight','EDGES']}
    assert dumped(ast.Module(body=author_source_body[4:], type_ignores=[])) == dumped(ast.Module(body=public_source_body[1:], type_ignores=[]))
    assert set(pf) == set(helper_functions+reused_functions+['source_algebra', 'main'])
    assert not any(isinstance(n, ast.Name) and n.id in ('importlib','REUSED') for n in ast.walk(publication_tree))
    imports = [ast.unparse(n) for n in publication_tree.body if isinstance(n,(ast.Import,ast.ImportFrom))]

    # Reimplement the read v1 fingerprint specification; do not import cache API.
    fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    input_rows = []
    for rel in input_paths:
        rp = Path(rel)
        assert not rp.is_absolute() and '..' not in rp.parts and rp.as_posix() == rel
        component = PUB
        for part in rp.parts:
            component /= part
            assert not stat.S_ISLNK(component.lstat().st_mode)
        body = (SNAP/'worktree'/rel).read_bytes()
        assert body == (PUB/rel).read_bytes()
        path_bytes = rel.encode()
        fingerprint.update(len(path_bytes).to_bytes(8,'big'))
        fingerprint.update(path_bytes)
        fingerprint.update(len(body).to_bytes(8,'big'))
        fingerprint.update(body)
        row = {'path':rel,'sha256':digest(body),'bytes':len(body)}
        if rel != NOTE:
            committed = subprocess.check_output(['git','show',BASE+':'+rel],cwd=PUB)
            assert committed == body
            row['exact_base_blob_match'] = True
        input_rows.append(row)
    input_fp = fingerprint.hexdigest()
    assert input_fp == 'bf1190766f15bae5d1cb10d49a68d0a7773c999b3a56699846bfc301351904e7'
    assert (SNAP/'worktree/AGENTS.md').read_bytes() == (HERE/'instructions/REPOSITORY_AGENTS.md').read_bytes()
    assert (SNAP/'worktree/docs/ai_methodology/SCIENCE_WORKFLOW.md').read_bytes() == (HERE/'instructions/SCIENCE_WORKFLOW.md').read_bytes()
    prior_hashes = {row['sha256'] for row in load(HERE/'PRE_SEAL.json')['members'] if row['path'].startswith('sources/')}
    unchanged_parents = [row for row in input_rows[1:] if row['sha256'] in prior_hashes]
    new_parent = [row for row in input_rows[1:] if row['sha256'] not in prior_hashes]
    assert len(unchanged_parents) == 5 and len(new_parent) == 1
    links = re.findall(r'\]\(([^)]+\.md)\)', note)
    assert set('docs/'+x for x in links) == set(input_paths[1:])

    result_bytes = (SNAP/'worktree'/result_path).read_bytes()
    assert digest(result_bytes) == EXPECTED['result']
    result = json.loads(result_bytes)
    author = load(HERE/'POST_sources/FULL_ENSEMBLE_CONTROL_RESULTS.json')
    for key in ('source_algebra','evolving_input_cascade'):
        assert result[key] == author[key]
    assert set(result)-set(author) == {'provenance'}
    assert result['source_sha256'] == EXPECTED['runner']
    assert result['provenance'] == {'embedded_author_word_helpers':sha(helper),
                                    'reused_author_control':sha(HERE/'POST_sources/full_ensemble_energy_controls.py')}
    changed_common = [k for k in author if result[k] != author[k]]
    assert changed_common == ['elapsed_seconds','source_sha256']

    execution_path = SNAP/'external/TENTH_PUBLICATION_CACHE_EXECUTION.json'
    execution = load(execution_path)
    run = execution['result']
    assert run['runner'] == RUNNER and run['status'] == 'ok' and run['exit_code'] == 0
    assert run['timeout_sec'] == 120 and run['elapsed_sec'] == 1.1261796951293945
    expected_stdout = result_bytes.decode()+'TOTAL: PASS=2 FAIL=0\n'
    assert run['stdout'] == expected_stdout and run['stderr'] == ''
    cache_rel = 'logs/runner-cache/'+Path(RUNNER).stem+'.txt'
    cache_bytes = (SNAP/'worktree'/cache_rel).read_bytes()
    assert digest(cache_bytes) == EXPECTED['cache']
    expected_cache = ('===== runner cache v1 =====\n'+f'runner: {RUNNER}\n'+
        f'runner_sha256: {EXPECTED["runner"]}\n'+f'input_fingerprint_sha256: {input_fp}\n'+
        f'timeout_sec: {run["timeout_sec"]}\n'+f'exit_code: {run["exit_code"]}\n'+
        f'elapsed_sec: {run["elapsed_sec"]:.2f}\n'+f'status: {run["status"]}\n'+
        '----- stdout -----\n'+run['stdout'][-200000:]+'\n----- stderr -----\n'+run['stderr'][-50000:]+'\n')
    assert expected_cache.encode() == cache_bytes
    root_verify = load(SNAP/'external/TENTH_PRIMARY_ROOT_VERIFICATION.json')
    for key in EXPECTED: assert root_verify[key+'_sha256'] == EXPECTED[key]
    assert root_verify['seconds'] == run['elapsed_sec'] and root_verify['provenance'] == result['provenance']
    root_freeze = load(SNAP/'external/TENTH_PUBLICATION_FROZEN_SOURCES.json')
    assert root_freeze['base_revision'] == BASE
    assert root_freeze['files_sha256'] == {NOTE:EXPECTED['note'],RUNNER:EXPECTED['runner']}
    assert root_freeze['PRE'] == sha(HERE/'PRE.md') and root_freeze['POST'] == sha(HERE/'POST.md')

    sample = next(r for r in result['evolving_input_cascade']['rows'] if r['t']==1.1 and r['epsilon']==.01)
    numeric_literals = {'full_mean':'2.877541','mean_target':'2.876752',
                        'scaled_full_variance':'3.265279','scaled_variance_target':'3.264409'}
    for key, literal in numeric_literals.items():
        assert format(sample[key],'.6f') == literal and literal in note
    assert abs(sample['scaled_high_density_trace_distance']-.000937434) < 5e-10 and '.000937434' in note
    assert sum(r['edge_mark_checks'] for r in result['source_algebra']['rows']) == 1260 and '1,260' in note
    assert result['source_algebra']['mutant_nonzero_cases'] == 1239 and '1,239' in note

    output = {
        'created_utc':datetime.now(timezone.utc).isoformat(),
        'source_sha256':sha(Path(__file__)),
        'prior_seals_unchanged':previous,
        'live_and_snapshot_sources_match':len(frozen['files'])+1,
        'publication_hashes':EXPECTED,
        'base_revision':BASE,
        'declared_inputs':input_rows,
        'prior_byte_identical_scientific_parents':len(unchanged_parents),
        'newly_read_parent':new_parent,
        'note_citation_targets_match_six_declared_parents':True,
        'embedded_helper_and_reused_function_AST_checks':ast_rows,
        'source_algebra_change':'Four dynamic loader/hash statements replaced by one SimpleNamespace using the four copied helper functions and required constants; remainder AST exactly equal.',
        'primary_main_change':'Output redirected into repository outputs, provenance hashes added, summary printed. Both scientific controls called unchanged.',
        'primary_imports':imports,
        'scientific_payloads_exactly_equal_to_author':True,
        'changed_common_result_keys':changed_common,
        'new_result_key':'provenance',
        'source_algebra_case_count':1260,'source_algebra_mutant_nonzero_count':1239,
        'toy_rows_checked':len(result['evolving_input_cascade']['rows']),
        'toy_complex_covariance_matrices_checked':len(result['evolving_input_cascade']['targets']),
        'numeric_prose_matches_saved_results':True,
        'input_fingerprint_sha256':input_fp,
        'runner_and_declared_input_paths_have_no_symlink_components':True,
        'execution_exit_code':run['exit_code'],'execution_status':run['status'],
        'execution_elapsed_sec':run['elapsed_sec'],'timeout_sec':run['timeout_sec'],
        'complete_recorded_stdout_equals_result_plus_summary':True,
        'cache_reconstructed_byte_for_byte_from_execution_and_source_identity':True,
        'API_stderr_field_empty':True,
        'stream_caveat':'The cache API merges stderr into stdout; the complete merged output contains exactly the saved JSON and expected summary.',
        'no_scientific_output_tail_truncation':len(run['stdout'])<200000,
        'primary_or_author_code_executed':False,
        'scope':'Source/proof correspondence and declared-input cache identity; reuses immutable PRE/POST science. No new independent primary numerical result, gate execution, audit verdict, publication edit or merge.'}
    data=json.dumps(output,indent=2)+'\n'
    (HERE/'PUBLICATION_EVIDENCE_CHECK.json').write_text(data)
    print(data,end='')


if __name__=='__main__':main()
