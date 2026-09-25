#!/usr/bin/env python3
"""Scoped publication correspondence only: no primary or author execution.

Part B is compared to the unchanged released-source POST. Other declared
inputs are hashed as opaque bytes solely to recompute the complete cache
fingerprint; Part A science and other personal/checker packets are not read.
"""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import ast
import difflib
import hashlib
import json
import stat
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PUB = BASE/'input-energy-power-publication'
FROZEN = BASE/'INPUT_ENERGY_POWER_PUBLICATION_FROZEN_SOURCES.json'
EXPECTED_FROZEN = '7c85aea8ef43782ef1a8e6dea959c8ffd2e74112f9c11be825210c0ff6bd7e76'
EXPECTED_NOTE = '9658836c90ceead6363e4cf91e6cdf2039be4e3587c009dae2447ae79026ad34'
EXPECTED_RUNNER = '30bcc516487bd268c089793b675cf4a39932e03f8fd2b3afc80183f711af5799'
EXPECTED_RESULT = '8301e6c5263d2842e1d129b1f30357c659a05fec09a6f11924ab4ec5d0256632'
EXPECTED_CACHE = 'e2b4b63baf8443841d70afa3a92024402e6a3260414c6dd760a39de0b3a720fd'


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def local_json(name):
    return json.loads((HERE/name).read_bytes())


def save_new(name, raw):
    if isinstance(raw, str):
        raw = raw.encode()
    target = HERE/name
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        assert target.read_bytes() == raw
    else:
        with target.open('xb') as output:
            output.write(raw)


def freeze(origin, name, role, expected=None):
    raw = origin.read_bytes()
    if expected:
        assert sha(raw) == expected
    save_new(name, raw)
    return dict(origin=str(origin), frozen_path=name, bytes=len(raw), sha256=sha(raw), role=role)


def literal_assignment(tree, name):
    found = [ast.literal_eval(node.value) for node in tree.body
             if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in node.targets)]
    assert len(found) == 1
    return found[0]


def compare_leaves(old, new, path, counts):
    assert type(old) is type(new), (path, type(old), type(new))
    if isinstance(old, dict):
        assert list(old) == list(new), path
        for key in old:
            compare_leaves(old[key], new[key], path+'/'+key, counts)
    elif isinstance(old, list):
        assert len(old) == len(new), path
        for j, (left, right) in enumerate(zip(old, new)):
            compare_leaves(left, right, path+'/'+str(j), counts)
    else:
        assert old == new, (path, old, new)
        counts[type(old).__name__] += 1


def main():
    preserved = []
    for name, expected in [('PRE_SEAL.json','a1cc8dc5b9af73952b55402902076e1b7b28b7bc7bbc2de4834c65dd8297031d'),
                           ('POST_SEAL.json','583af00f065fbc2d9c5de9fff379b441f9c09a67cad630612380929329932369')]:
        raw = (HERE/name).read_bytes()
        assert sha(raw) == expected
        seal = json.loads(raw)
        for row in seal['members']:
            member = (HERE/row['path']).read_bytes()
            assert len(member) == row['bytes'] and sha(member) == row['sha256']
        preserved.append(dict(seal=name, sha256=expected, unchanged_members=len(seal['members'])))
    # Refresh earlier source identities without reopening any other personal packet.
    for row in local_json('SOURCE_PINS.json')['sources']:
        assert sha(Path(row['origin']).read_bytes()) == row['sha256']

    source_rows = [freeze(FROZEN, 'publication_sources/FROZEN_SOURCES.json', 'Frozen publication manifest; process/source identities', EXPECTED_FROZEN)]
    manifest = json.loads(FROZEN.read_bytes())
    runner_raw = (PUB/manifest['runner']).read_bytes()
    assert sha(runner_raw) == EXPECTED_RUNNER
    tree = ast.parse(runner_raw)
    declared = literal_assignment(tree, 'AUDIT_INPUT_PATHS')
    assert tuple(declared) == tuple([manifest['note']]+manifest['parent_paths']+manifest['runtime'])
    assert len(declared) == 13 and len(set(declared)) == 13
    assert literal_assignment(tree, 'AUDIT_TIMEOUT_SEC') == 120
    assert literal_assignment(tree, 'RESULT_PATH') == manifest['result']
    assert literal_assignment(tree, 'RUNTIME') == manifest['runtime']
    expected_inputs = dict(manifest['files_sha256'])
    expected_inputs.update({r['path']:r['sha256'] for r in manifest['parents']})
    fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    input_rows = []
    for rel in declared:
        path = Path(rel)
        assert not path.is_absolute() and '..' not in path.parts and path.as_posix() == rel
        current = PUB
        for part in path.parts:
            current /= part
            assert not stat.S_ISLNK(current.lstat().st_mode)
        body = (PUB/rel).read_bytes()
        assert sha(body) == expected_inputs[rel]
        encoded = rel.encode()
        fingerprint.update(len(encoded).to_bytes(8,'big'))
        fingerprint.update(encoded)
        fingerprint.update(len(body).to_bytes(8,'big'))
        fingerprint.update(body)
        if '/runtime/power/' in rel:
            role = 'Part B exact power source; bytes and full AST compared to released author source already read in POST'
        elif rel == manifest['note']:
            role = 'Whole note pinned; only Part B and shared front matter/footer interpreted'
        else:
            role = 'Declared input bytes for fingerprint; no new scientific review of Part A or extra parents'
        record = freeze(PUB/rel, 'publication_sources/declared_inputs/'+rel, role, expected_inputs[rel])
        source_rows.append(record)
        input_rows.append(dict(path=rel, bytes=len(body), sha256=sha(body), role=role))
    fp = fingerprint.hexdigest()
    assert fp == '54f912d616790c7c2956051ba6c2e70215fa1ae7cbebf9657de924dcc18e8336'
    source_rows.append(freeze(PUB/manifest['runner'], 'publication_sources/primary_runner.py', 'Shared primary wrapper, read completely; not executed', EXPECTED_RUNNER))
    source_rows.append(freeze(PUB/'scripts/runner_cache.py', 'publication_sources/runner_cache.py', 'Mechanical cache encoding and declared-input algorithm; read, not executed'))
    source_rows.append(freeze(PUB/manifest['result'], 'publication_sources/ENERGY_POWER_RESULTS.json', 'Whole combined result pinned; only Part B scientific payload compared', EXPECTED_RESULT))
    receipt_path = BASE/'INPUT_ENERGY_POWER_PUBLICATION_CACHE_EXECUTION.json'
    source_rows.append(freeze(receipt_path, 'publication_sources/CACHE_EXECUTION.json', 'Reported primary API execution and complete merged stdout, without a new execution'))
    process_path = BASE/'INPUT_ENERGY_POWER_PRIMARY_ROOT_VERIFICATION.json'
    source_rows.append(freeze(process_path, 'publication_sources/ROOT_VERIFICATION.json', 'Root process record; not independent scientific authority'))
    cache_rel = 'logs/runner-cache/'+Path(manifest['runner']).stem+'.txt'
    source_rows.append(freeze(PUB/cache_rel, 'publication_sources/PRIMARY_CACHE.txt', 'Actual canonical cache bytes', EXPECTED_CACHE))
    assert len(source_rows) == 20

    note_raw = (PUB/manifest['note']).read_bytes()
    assert sha(note_raw) == EXPECTED_NOTE
    note = note_raw.decode()
    a_start = note.index('## A. ')
    b_start = note.index('## B. ')
    c_start = note.index('## C. ')
    assert a_start < b_start < c_start
    scoped_note = note[:a_start]+'<!-- Part A omitted from this scientific review. -->\n\n'+note[b_start:]
    save_new('PUBLICATION_SCOPED_NOTE.md', scoped_note)
    part_b = note[b_start:c_start]
    body = part_b[part_b.index('### 1. '):].strip()+'\n'
    original = (HERE/'post_sources/author/ORIGINAL_SELECTED_MARK_ENERGY_POWER_ROOT.md').read_text()
    old_body = original[original.index('## 1. '):].strip()+'\n'
    old_body = '\n'.join('### '+line[3:] if line.startswith('## ') else line for line in old_body.split('\n'))
    amendments = [
      ('normalized input psi in the domain of D define this single channel\'s power',
       'normalized input with both psi and B psi in the domain of D, define this\nsingle channel\'s power'),
      ('Smooth compact packets and finite Wilson shifts preserve the electric\noperator domain, so both terms in (1) are defined at every fixed g>0.',
       'The declared smooth compact packets and their finite Wilson shifts lie in\nthe domains of all powers of N_E=1+sum_e E_e^2. D is controlled by N_E there,\nso both terms in (1) are defined at every fixed g>0. This does not claim that\nfinite shifts preserve the full domain of the degenerate occupied-B D for\narbitrary inputs. At fixed g, diagonal D commutes with N_E; bounded finite\nshifts are bounded on each N_E graph norm. The interaction-picture expansion\ntherefore preserves the weighted trace domains. With the extra moments of\nthese compact packets, differentiating the energy mean at zero gives (1).\nOrdinary trace-norm convergence alone would not justify this step.'),
      ('The distinct earlier root29\ncandidate concerning INPUT mean-energy increments is not used to prove (4).',
       'The input mean-energy result in Part A is not used to prove (4).'),
      ('Independent checking\nis still required before publication promotion. No audit verdict is applied.',
       'The independently sealed\nPRE reconstructs the power limit. The separate released-source POST verifies\nthe complete coefficient and the 525-link filling, and independently checks\nthe all-volume positivity and hard-band arguments. It confirms the sufficient\nsmooth-packet domain statement above. No audit verdict is applied.'),
    ]
    adjusted = old_body
    for old, new in amendments:
        assert adjusted.count(old) == 1
        adjusted = adjusted.replace(old, new)
    assert adjusted == body
    diff = ''.join(difflib.unified_diff(old_body.splitlines(keepends=True), body.splitlines(keepends=True),
        fromfile='sealed-author-Part-B-with-heading-depth-normalized', tofile='publication-Part-B'))
    save_new('PUBLICATION_PART_B_DIFF.txt', diff)

    runtime_rows = []
    for rel in manifest['runtime']:
        if '/power/' not in rel:
            continue
        pub_source = (PUB/rel).read_bytes()
        prior_source = (HERE/'post_sources/author'/Path(rel).name).read_bytes()
        assert pub_source == prior_source
        parsed = ast.parse(pub_source)
        assert ast.dump(parsed, include_attributes=False) == ast.dump(ast.parse(prior_source), include_attributes=False)
        definitions = [node.name for node in ast.walk(parsed) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
        runtime_rows.append(dict(path=rel, sha256=sha(pub_source), bytes=len(pub_source),
            exact_prior_POST_source_bytes=True, full_AST_identical=True, function_definitions=definitions,
            code_executed_or_imported=False))
    assert len(runtime_rows) == 3

    result_raw = (PUB/manifest['result']).read_bytes()
    result = json.loads(result_raw)
    assert result['source_sha256'] == EXPECTED_RUNNER and result['all_assertions_passed'] is True
    receipt = json.loads(receipt_path.read_bytes())
    execution = receipt['result']
    assert execution['runner'] == manifest['runner'] and execution['exit_code'] == 0
    assert execution['status'] == 'ok' and execution['timeout_sec'] == 120 and execution['stderr'] == ''
    assert execution['stdout'] == result_raw.decode()+'TOTAL_PASS: 5\n'
    assert receipt['cache_path'] == str(PUB/cache_rel) and receipt['cache_status'] == 'fresh'
    stdout_tail, stderr_tail = execution['stdout'][-200000:], execution['stderr'][-50000:]
    expected_cache = (
        '===== runner cache v1 =====\n'
        f"runner: {manifest['runner']}\n"
        f'runner_sha256: {EXPECTED_RUNNER}\n'
        f'input_fingerprint_sha256: {fp}\n'
        f"timeout_sec: {execution['timeout_sec']}\n"
        f"exit_code: {execution['exit_code']}\n"
        f"elapsed_sec: {execution['elapsed_sec']:.2f}\n"
        f"status: {execution['status']}\n"
        f'----- stdout -----\n{stdout_tail}\n----- stderr -----\n{stderr_tail}\n')
    assert (PUB/cache_rel).read_bytes() == expected_cache.encode()

    power_keys = ['POWER_POLYNOMIAL_RESULTS.json','POWER_SPECTRAL_RESULTS.json','POWER_POSITIVE_CERTIFICATE.json']
    exempt = {power_keys[0]:('elapsed_seconds',), power_keys[1]:('elapsed_seconds','source_sha256'),
              power_keys[2]:('elapsed_seconds','input_sha256')}
    stage_map = {row['result']:row for row in result['stages']}
    payload_rows = []
    totals = Counter()
    for key in power_keys:
        old_raw = (HERE/'post_sources/author'/key).read_bytes()
        old, fresh = json.loads(old_raw), result['payload'][key]
        assert set(old) == set(fresh)
        allowed_changes = {field:dict(old=old[field], fresh=fresh[field]) for field in exempt[key]}
        counts = Counter()
        compare_leaves({k:v for k,v in old.items() if k not in exempt[key]},
                       {k:v for k,v in fresh.items() if k not in exempt[key]}, key, counts)
        totals.update(counts)
        stage_bytes = (json.dumps(fresh, indent=2)+'\n').encode()
        stage = stage_map[key]
        assert stage['stdout_bytes'] == len(stage_bytes) and stage['stdout_sha256'] == sha(stage_bytes)
        assert stage['stderr_bytes'] == 0 and stage['exit_code'] == 0
        assert stage['code_sha256'] == sha((HERE/'post_sources/author'/stage['program']).read_bytes())
        assert 0 <= fresh['elapsed_seconds'] <= stage['elapsed_seconds']
        save_new('publication_sources/Part_B_payload/'+key, stage_bytes)
        payload_rows.append(dict(result=key, old_sha256=sha(old_raw), fresh_stage=stage,
            fresh_stage_bytes_reconstructed_exactly=True, scientific_leaf_counts=dict(counts),
            all_scientific_leaves_and_types_exact=True, allowed_top_level_changes=allowed_changes))
    assert result['payload'][power_keys[1]]['source_sha256'] == stage_map[power_keys[0]]['stdout_sha256']
    assert result['payload'][power_keys[2]]['input_sha256'] == stage_map[power_keys[1]]['stdout_sha256']
    root_record = json.loads(process_path.read_bytes())
    for key in power_keys:
        root_row = next(row for row in root_record['rows'] if row['result'] == key)
        assert root_row['fresh_stage'] == stage_map[key]
    assert root_record['cache_sha256'] == EXPECTED_CACHE and root_record['result_sha256'] == EXPECTED_RESULT

    # Hash-only exact source-object correspondence; no new premise import.
    parent_rows = []
    for parent in manifest['parents']:
        command = ['git','-C',str(PUB),'show',parent['revision']+':'+parent['path']]
        checked = subprocess.run(command, capture_output=True)
        assert checked.returncode == 0 and not checked.stderr
        assert len(checked.stdout) == parent['bytes'] and sha(checked.stdout) == parent['sha256']
        assert checked.stdout == (PUB/parent['path']).read_bytes()
        parent_rows.append(dict(path=parent['path'], revision=parent['revision'],sha256=parent['sha256'],
            exact_git_and_publication_bytes=True, stdout_retained='publication_sources/declared_inputs/'+parent['path'],
            new_scientific_review=False))

    pin_record = dict(created_utc=datetime.now(timezone.utc).isoformat(),
        scope='Part B and shared framing only; opaque declared-input bytes cover whole-run fingerprint',
        preserved_PRE_POST=preserved, sources=source_rows, declared_inputs=input_rows,
        input_fingerprint_sha256=fp, parent_identity_checks=parent_rows,
        forbidden_personal_or_checker_sources_read=False, primary_or_author_program_executed=False)
    save_new('PUBLICATION_SOURCE_PINS.json', json.dumps(pin_record,indent=2)+'\n')
    comparison = dict(created_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(Path(__file__).read_bytes()),
        scope=__doc__, preserved_PRE_POST=preserved, source_count=len(source_rows),
        note_sha256=EXPECTED_NOTE, runner_sha256=EXPECTED_RUNNER,
        scoped_note_lines=dict(front_matter=[1,53],Part_B=[308,522],shared_footer=[523,len(note.splitlines())]),
        Part_B_exact_author_body_except_declared_amendments=True, amendment_count=len(amendments),
        amendment_roles=['Explicit psi and Bpsi electric domain','Smooth-packet weighted derivative precision',
                         'Rename excluded Part A reference','Actual independent PRE/POST attribution'],
        power_runtime_sources=runtime_rows, new_scientific_reruns=0,
        whole_result_sha256=EXPECTED_RESULT, Part_B_payload=payload_rows,
        total_Part_B_nonruntime_leaf_counts=dict(totals), unallowed_payload_changes=[],
        all_fresh_power_input_hashes_match_stage_bytes=True,
        complete_execution_stdout_equals_result_plus_trailer=True,
        execution_record_sha256=sha(receipt_path.read_bytes()), reported_API_elapsed_seconds=execution['elapsed_sec'],
        primary_internal_elapsed_seconds=result['elapsed_seconds'], reported_exit_code=execution['exit_code'],
        reported_separate_stderr_bytes=0, complete_merged_stdout_bytes=len(execution['stdout'].encode()),
        cache_sha256=EXPECTED_CACHE, cache_bytes=len(expected_cache.encode()),
        cache_exact_format_and_tail_of_execution=True, input_fingerprint_sha256=fp,
        declared_input_count=len(declared), all_declared_bytes_match_expected=True,
        freshness_scope='Current content/fingerprint and captured execution/cache correspondence; no new primary execution or historical stat-token reconstruction',
        root_verification_process_record_only=True, Part_A_scientific_review=False,
        parent_hash_checks=parent_rows)
    save_new('PUBLICATION_CHECK_RESULTS.json', json.dumps(comparison,indent=2)+'\n')
    print(json.dumps(comparison,indent=2))


if __name__ == '__main__':
    main()
