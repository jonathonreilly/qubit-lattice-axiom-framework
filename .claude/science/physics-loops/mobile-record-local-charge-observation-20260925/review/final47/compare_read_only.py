"""Read-only final correspondence: no author imports, writer execution or science rerun."""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import ast
import difflib
import json
import math
import os
import re
import stat
import subprocess

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent
EXT = PREVIOUS.parent
PUB = EXT / 'local-charge-observation-publication'
S = HERE / 'sources'
SP = S / 'publication'
SE = S / 'external'
STAT_KEYS = ('sha256', 'bytes', 'mode', 'dev', 'ino', 'mtime_ns', 'ctime_ns', 'nlink')


def identity(path):
    s = path.stat()
    return dict(sha256=sha256(path.read_bytes()).hexdigest(), bytes=s.st_size,
                mode=s.st_mode, dev=s.st_dev, ino=s.st_ino, mtime_ns=s.st_mtime_ns,
                ctime_ns=s.st_ctime_ns, nlink=s.st_nlink)


def load(path):
    return json.loads(path.read_text())


def literal(source, name):
    matches = [node.value for node in ast.parse(source).body
               if isinstance(node, ast.Assign) and len(node.targets) == 1
               and isinstance(node.targets[0], ast.Name) and node.targets[0].id == name]
    assert len(matches) == 1, name
    return ast.literal_eval(matches[0])


def compare_payload(old, new, path=(), counts=None, differences=None):
    if counts is None:
        counts = Counter(); differences = []
    assert type(old) is type(new), path
    if isinstance(old, dict):
        assert old.keys() == new.keys(), path
        for key in old:
            compare_payload(old[key], new[key], (*path, key), counts, differences)
    elif isinstance(old, list):
        assert len(old) == len(new), path
        for i, (a, b) in enumerate(zip(old, new)):
            compare_payload(a, b, (*path, i), counts, differences)
    elif path == ('elapsed_seconds',):
        assert isinstance(old, float) and all(math.isfinite(v) and v >= 0 for v in (old, new))
        differences.append(dict(path=list(path), old=old, fresh=new))
    else:
        if isinstance(old, float):
            assert math.isfinite(old) and math.isfinite(new)
        assert old == new, path
        counts[type(old).__name__] += 1
    return counts, differences


def main():
    pins = load(HERE / 'SOURCE_PINS.json')
    prior = load(HERE / 'PRIOR_PRESERVATION_BEFORE.json')['files']
    observed = {}
    by_origin = {}
    for row in pins['sources']:
        origin = Path(row['origin']); snapshot = HERE / row['snapshot']
        now = identity(origin)
        assert all(now[key] == row[key] for key in STAT_KEYS), str(origin)
        assert identity(snapshot)['sha256'] == row['sha256'] and snapshot.stat().st_size == row['bytes']
        observed[str(origin)] = now; observed[str(snapshot)] = identity(snapshot)
        by_origin[str(origin)] = snapshot
    for row in prior:
        now = identity(Path(row['path']))
        assert all(now[key] == row[key] for key in STAT_KEYS)
        observed[row['path']] = now
    base_graph = HERE / pins['base_graph']['snapshot']
    assert identity(base_graph)['sha256'] == pins['base_graph']['sha256']
    observed[str(base_graph)] = identity(base_graph)
    assert len(observed) == 174 and len(prior) == 85
    frozen = load(SE / 'LOCAL_CHARGE_OBSERVATION_FROZEN_SOURCES.json')
    assert identity(SE / 'LOCAL_CHARGE_OBSERVATION_FROZEN_SOURCES.json')['sha256'] == pins['frozen_manifest_sha256']
    working = load(SE / 'LOCAL_CHARGE_OBSERVATION_PUBLICATION_WORKING_SOURCES.json')
    assert {k: v for k, v in frozen.items() if k not in ('files_sha256', 'frozen_utc')} == working
    for rel, h in frozen['files_sha256'].items():
        assert identity(SP / rel)['sha256'] == h == identity(PUB / rel)['sha256']
    assert len(frozen['files_sha256']) == 14 and len(frozen['source_files_sha256']) == 7

    note = (SP / frozen['note']).read_text()
    writer = (SE / 'build_local_charge_observation_publication.py').read_text()
    changes = literal(writer, 'changes')
    assert changes == [[(r['old'], r['new']) for r in rows] for rows in frozen['presentation_replacements']]
    bodies = []
    for origin, rows in zip(frozen['source_notes'], frozen['presentation_replacements']):
        text = by_origin[origin].read_text()
        for row in rows:
            assert text.count(row['old']) == 1
            text = text.replace(row['old'], row['new'], 1)
        text = re.sub(r'^(#{1,6}) ', lambda m: '#' * (len(m[1]) + 2) + ' ', text, flags=re.M)
        assert note.count(text) == 1
        bodies.append(text)
    parents = frozen['parent_paths']; parent_ids = [Path(p).stem.lower() for p in parents]
    cid = Path(frozen['note']).stem.lower()
    header = ('---\nclaim_id: ' + cid + '\nclaim_type: bounded_theorem\n'
              'claim_scope: "Bounded original charge current, initial charge covariance and a fixed-local-support finite-time covariance remainder for the supplied common generator and minimum-number preparation; no measured charge or detector identification."\nupstream_dependencies:\n'
              + ''.join('  - ' + p + '\n' for p in parent_ids)
              + 'runner: ' + frozen['runner'] + '\n---\n\n')
    footer_nodes = [n.value for n in ast.parse(writer).body if isinstance(n, ast.Assign)
                    and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name) and n.targets[0].id == 'footer']
    assert len(footer_nodes) == 1 and isinstance(footer_nodes[0], ast.BinOp)
    footer = ast.literal_eval(footer_nodes[0].left) + ''.join(
        '- [' + Path(p).stem + '](' + Path(p).name + ').\n' for p in parents)
    expected_note = header + literal(writer, 'front') + bodies[0] + '\n## Part II: local finite-time covariance\n\n' + bodies[1] + footer
    assert expected_note == note
    assert re.findall(r'^  - (.+)$', note.split('---', 2)[1], re.M) == parent_ids
    assert re.findall(r'^- \[[^\]]+\]\(([^)]+)\)\.$', footer, re.M) == [Path(p).name for p in parents]

    qualified = S / 'native-charge-current-noise-qualified'
    qualification = load(qualified / 'QUALIFICATION_SEAL.json')
    for row in qualification['members']:
        assert identity(qualified / row['path'])['sha256'] == row['sha256']
    original46 = (S / 'native-charge-current-noise-personal/CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md').read_text()
    qualified46 = (qualified / 'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_QUALIFIED.md').read_text()
    old = ('remain for arbitrary field input. Only for the separately supplied zero-field\n'
           'basis vector does the expectation of that off-diagonal Hamiltonian current\n'
           'vanish. The charge-mean formula (A) needs no such extra field premise.')
    new = ('remain for arbitrary field input. For the separately supplied zero-field basis vector, the expectation of\n'
           'that off-diagonal Hamiltonian current vanishes; it need not vanish for\n'
           'arbitrary field input. The charge-mean formula (A) needs no such extra field premise.')
    assert original46.count(old) == 1 and original46.replace(old, new, 1) == qualified46
    expected_diff = ''.join(difflib.unified_diff(original46.splitlines(True), qualified46.splitlines(True),
        fromfile=str(EXT / 'native-charge-current-noise-personal/CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md'),
        tofile=str(EXT / 'native-charge-current-noise-qualified/CHARGE_CURRENT_AND_INITIAL_COVARIANCE_QUALIFIED.md')))
    assert expected_diff == (qualified / 'WORDING_ONLY.diff').read_text()

    wrapper_path = SP / frozen['runner']; wrapper = wrapper_path.read_text()
    declarations = {name: literal(wrapper, name) for name in ('AUDIT_TIMEOUT_SEC', 'AUDIT_INPUT_PATHS', 'OUTPUT_DIRECTORY', 'RUNTIMES')}
    expected_inputs = (frozen['note'], *parents, *frozen['runtime'])
    assert declarations['AUDIT_INPUT_PATHS'] == expected_inputs
    assert declarations['AUDIT_TIMEOUT_SEC'] == 120
    assert declarations['RUNTIMES'] == tuple(frozen['runtime']) and declarations['OUTPUT_DIRECTORY'] == frozen['output_directory']
    static_body = [n.value.value for n in ast.parse(writer).body if isinstance(n, ast.AugAssign)
                   and isinstance(n.target, ast.Name) and n.target.id == 'wrapper'
                   and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str)]
    assert len(static_body) == 1
    expected_wrapper = (literal(writer, 'wrapper') + 'AUDIT_TIMEOUT_SEC = 120\nAUDIT_INPUT_PATHS = ' + repr(expected_inputs) + '\n'
                        + 'OUTPUT_DIRECTORY = ' + repr(frozen['output_directory']) + '\nRUNTIMES = ' + repr(tuple(frozen['runtime'])) + '\n' + static_body[0])
    assert expected_wrapper == wrapper

    comparisons = []
    for index, (label, directory, program) in enumerate([
        ('current', 'native-charge-current-noise-personal', 'current_noise_controls.py'),
        ('finite_time', 'native-charge-finite-time-personal', 'local_support_controls.py')]):
        author = S / directory
        author_seal = load(author / 'AUTHOR_SEAL.json')
        sealed = {r['path']: r for r in author_seal['members']}
        for rel in (program, 'attempt01/EXECUTION.json', 'attempt01/stdout.json', 'attempt01/stderr.txt'):
            assert identity(author / rel)['sha256'] == sealed[rel]['sha256']
        runtime = SP / frozen['runtime'][index]
        assert runtime.read_bytes() == (author / program).read_bytes()
        old_output = author / 'attempt01/stdout.json'
        fresh_output = SP / frozen['output_directory'] / (label + '.stdout.json')
        old_data, fresh_data = load(old_output), load(fresh_output)
        counts, differences = compare_payload(old_data, fresh_data)
        assert len(differences) == 1
        receipt = load(author / 'attempt01/EXECUTION.json')
        assert receipt['source_sha256'] == identity(runtime)['sha256']
        assert receipt['stdout_sha256'] == identity(old_output)['sha256']
        assert receipt['exit_code'] == 0 and (author / 'attempt01/stderr.txt').read_bytes() == b''
        assert (SP / frozen['output_directory'] / (label + '.stderr.txt')).read_bytes() == b''
        if label == 'current':
            assert fresh_data['source_sha256'] == identity(runtime)['sha256']
            assert fresh_data['primitive_count'] == len(fresh_data['primitive_rows']) == 8480
            assert fresh_data['real_polarized_covariance_entries'] == 180
            compact = [dict(graph=g['graph'], vertices=g['vertices'], A=g['A'], primitive_rows=g['primitive_rows'],
                            Fourier=g['Fourier']) for g in fresh_data['graph_summaries']]
        else:
            assert fresh_data['program_sha256'] == identity(runtime)['sha256']
            assert [g['L'] for g in fresh_data['graphs']] == [4, 6, 8, 12, 16, 20]
            assert (author / program).read_bytes() == (PREVIOUS / 'post_sources/author47/local_support_controls.py').read_bytes()
            assert old_output.read_bytes() == (PREVIOUS / 'post_sources/author47/attempt01/stdout.json').read_bytes()
            prior_check = load(PREVIOUS / 'post_comparison.stdout.txt')
            assert prior_check['full_primary_output_sha256'] == identity(old_output)['sha256']
            compact = [dict(L=g['L'], M=g['M'], illustrative=g['illustrative_delta_kappa_equal_one']) for g in fresh_data['graphs']]
        comparisons.append(dict(label=label, runtime_sha256=identity(runtime)['sha256'],
                                author_output_sha256=identity(old_output)['sha256'], fresh_output_sha256=identity(fresh_output)['sha256'],
                                non_timing_leaf_count=sum(counts.values()), leaf_types=dict(counts),
                                only_differences=differences, complete_compact_results=compact))

    # Implement the already-read cache-v1 byte protocol directly, without importing its module.
    fp = sha256(b'runner-cache-input-fingerprint-v1\0')
    input_rows = []
    for rel in expected_inputs:
        assert not Path(rel).is_absolute() and '..' not in Path(rel).parts and str(Path(rel)) == rel
        component = PUB
        for part in Path(rel).parts:
            component /= part
            assert not stat.S_ISLNK(component.lstat().st_mode)
        raw = (SP / rel).read_bytes(); name = rel.encode()
        fp.update(len(name).to_bytes(8, 'big')); fp.update(name)
        fp.update(len(raw).to_bytes(8, 'big')); fp.update(raw)
        input_rows.append(dict(path=rel, bytes=len(raw), sha256=sha256(raw).hexdigest()))
    fingerprint = fp.hexdigest()
    result_path = SP / frozen['result']; result_text = result_path.read_text(); result = load(result_path)
    execution_receipt = load(SE / 'LOCAL_CHARGE_OBSERVATION_PRIMARY_EXECUTION.json')
    execution = execution_receipt['execution']
    assert execution['runner'] == frozen['runner'] and execution['status'] == 'ok'
    assert execution['exit_code'] == 0 and execution['timeout_sec'] == 120 and execution['stderr'] == ''
    assert execution['stdout'] == result_text + 'TOTAL_PASS: 1\n'
    assert result['source_sha256'] == identity(wrapper_path)['sha256'] and result['all_assertions_passed'] is True
    assert result['runtime_sha256'] == {rel: identity(SP / rel)['sha256'] for rel in frozen['runtime']}
    assert [a['label'] for a in result['artifacts']] == ['current', 'finite_time']
    for i, row in enumerate(result['artifacts']):
        assert row['path'] == frozen['output_directory'] + '/' + row['label'] + '.stdout.json'
        assert identity(SP / row['path'])['sha256'] == row['sha256']
        assert (SP / row['path']).stat().st_size == row['bytes']
        assert row['exit_code'] == row['stderr_bytes'] == 0
        assert row['runtime_source_sha256'] == identity(SP / frozen['runtime'][i])['sha256']
    expected_cache = ('===== runner cache v1 =====\nrunner: ' + frozen['runner'] + '\nrunner_sha256: ' + identity(wrapper_path)['sha256']
                      + '\ninput_fingerprint_sha256: ' + fingerprint
                      + '\ntimeout_sec: 120\nexit_code: 0\nelapsed_sec: ' + format(execution['elapsed_sec'], '.2f')
                      + '\nstatus: ok\n----- stdout -----\n' + execution['stdout'][-200000:]
                      + '\n----- stderr -----\n' + execution['stderr'][-50000:] + '\n')
    assert (SP / frozen['cache']).read_bytes() == expected_cache.encode()
    assert fingerprint == '3b9e82f6cbffbeea7c9d1f08bd5b065d974e5c33a7201679c0db6c077cc6471b'

    old_graph, new_graph = load(base_graph), load(SP / 'docs/audit/data/citation_graph_manifest.json')
    assert old_graph['schema_version'] == new_graph['schema_version'] == 1
    assert set(new_graph['nodes']) - set(old_graph['nodes']) == {cid}
    assert not (set(old_graph['nodes']) - set(new_graph['nodes']))
    assert all(new_graph['nodes'][key] == value for key, value in old_graph['nodes'].items())
    expected_node = dict(out_degree=3, deps_hash=sha256('\n'.join(sorted(parent_ids)).encode()).hexdigest()[:12])
    assert new_graph['nodes'][cid] == expected_node
    assert new_graph['node_count'] == len(new_graph['nodes']) == old_graph['node_count'] + 1
    assert new_graph['edge_count'] == sum(n['out_degree'] for n in new_graph['nodes'].values()) == old_graph['edge_count'] + 3

    history = SE / 'local-charge-observation-publication-history'
    failure = load(history / 'PREMATURE_GRAPH_DEPENDENCY_FAILURE.json')
    old_verify = (history / 'verify_publication_attempt01.py').read_text()
    new_verify = (SE / 'verify_local_charge_observation_publication.py').read_text()
    assert sha256(old_verify.encode()).hexdigest() == failure['source_sha256']
    reports = [n for n in ast.parse(new_verify).body if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call)
               and any(isinstance(t, ast.Name) and t.id == 'report' for t in n.targets)]
    assert len(reports) == 1
    kw = [k for k in reports[0].value.keywords if k.arg == 'failed_build_attempts']
    assert len(kw) == 1 and len(ast.literal_eval(kw[0].value)) == 1
    expression = ast.get_source_segment(new_verify, kw[0].value)
    assert old_verify.count('failed_build_attempts=[]') == 1
    assert old_verify.replace('failed_build_attempts=[]', 'failed_build_attempts=' + expression, 1) == new_verify
    assert failure['exit_code'] == 1 and failure['failed_before_science_or_manifest_mutation'] is True

    root_check = load(SE / 'LOCAL_CHARGE_OBSERVATION_PRIMARY_ROOT_VERIFICATION.json')
    assert len(root_check['comparisons']) == len(comparisons)
    for own, root in zip(comparisons, root_check['comparisons']):
        assert own['label'] == root['label'] and own['non_timing_leaf_count'] == root['all_non_timing_leaves_exact']
        assert own['only_differences'][0]['old'] == root['old_elapsed_seconds']
        assert own['only_differences'][0]['fresh'] == root['new_elapsed_seconds']
    assert root_check['cache_status'] == 'fresh' and root_check['old_graph_nodes_unchanged'] == len(old_graph['nodes'])

    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0')
    git_now = []
    recorded_git = load(HERE / 'GIT_SOURCE_EVIDENCE.json')['commands']
    readonly_commands = [
        ['git', 'rev-parse', '--verify', 'HEAD'], ['git', 'branch', '--show-current'],
        ['git', 'rev-parse', '--verify', frozen['base_branch']],
        ['git', 'merge-base', '--is-ancestor', frozen['base_revision'], frozen['base_branch']],
        ['git', 'status', '--porcelain=v1', '--untracked-files=all'],
        ['git', 'diff', '--name-status', frozen['base_revision']]]
    for old, command in zip(recorded_git[:6], readonly_commands):
        assert old['command'] == command
        run = subprocess.run(command, cwd=PUB, env=env, capture_output=True)
        now = dict(command=old['command'], exit_code=run.returncode, stdout=run.stdout.decode(), stderr=run.stderr.decode())
        assert now == old
        git_now.append(now)
    changed_files = {line[3:] for line in git_now[4]['stdout'].splitlines()}
    assert changed_files == set(frozen['files_sha256']) - set(parents)
    for path, initial in observed.items():
        assert identity(Path(path)) == initial, path
    print(json.dumps(dict(
        scope='Final released-source comparison. Science assessment Part II and initial-compression joins; both payloads compared mechanically. No primary, author, historical writer, audit or pipeline executed.',
        frozen_manifest_sha256=pins['frozen_manifest_sha256'], frozen_files=14,
        source_origins=44, protected_prior_files=85, observed_paths_unchanged=len(observed),
        base=frozen['base_revision'], branch=frozen['branch'], candidate_changed_paths=sorted(changed_files),
        complete_note_and_wrapper_match_inert_writer=True,
        presentation_replacements=[len(v) for v in changes], qualification46_exactly_one_prose_replacement=True,
        comparisons=comparisons,
        declared_inputs=input_rows, input_fingerprint_sha256=fingerprint,
        exact_full_cache_reconstruction=True, cache_semantics='fresh; stored status ok and exit0',
        wrapper_elapsed_seconds=result['elapsed_seconds'], API_elapsed_seconds=execution['elapsed_sec'],
        outer_receipt_elapsed_seconds=execution_receipt['elapsed_seconds'],
        cache_sha256=identity(SP / frozen['cache'])['sha256'], result_sha256=identity(result_path)['sha256'],
        graph=dict(old_nodes=len(old_graph['nodes']), new_nodes=len(new_graph['nodes']),
                   old_edges=old_graph['edge_count'], new_edges=new_graph['edge_count'], added_node=cid,
                   exact_parent_ids=parent_ids, new_node=expected_node, all_prior_nodes_identical=True),
        failure_history=dict(old_verifier_sha256=failure['source_sha256'],
                             current_verifier_only_adds_failure_metadata=True,
                             historical_cause='Author-recorded premature graph dependency; no independent historical trace reconstruction claimed.'),
        independent_science_reproduction=False, own_scientific_authority='Unchanged PRE47/POST47, not root verification metadata.'), indent=2))


if __name__ == '__main__':
    main()
