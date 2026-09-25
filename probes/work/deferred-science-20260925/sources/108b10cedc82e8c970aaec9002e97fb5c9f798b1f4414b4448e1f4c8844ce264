#!/usr/bin/env python3
"""Read-only source/output correspondence; never runs a scientific control."""
import ast
import copy
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTE = 'docs/RECENT_BIRTHS_FORCE_FULL_CUBE_ENERGY_VARIANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md'
RUNNER = 'scripts/recent_births_full_cube_energy_variance_2026_09_24.py'
RESULT = 'outputs/recent_birth_full_cube_variance_20260924/RECENT_BIRTH_FULL_ENSEMBLE_RESULTS.json'
CACHE = 'logs/runner-cache/recent_births_full_cube_energy_variance_2026_09_24.txt'
PUBLICATION = HERE.parent / 'recent-birth-publication'
CHECKS = []


def check(label, condition, **detail):
    CHECKS.append({'check': label, 'pass': bool(condition), **detail})


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def readj(path):
    return json.loads(path.read_text())


def dump(node):
    return ast.dump(node, include_attributes=False)


def functions(tree):
    return {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}


def assignments(tree):
    return {target.id: node.value for node in tree.body if isinstance(node, ast.Assign)
            for target in node.targets if isinstance(target, ast.Name)}


def without(obj, *keys):
    return {key: value for key, value in obj.items() if key not in keys}


def fingerprint(worktree, inputs):
    h = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    for rel in inputs:
        name, body = rel.encode('utf-8'), (worktree / rel).read_bytes()
        for data in (name, body):
            h.update(len(data).to_bytes(8, 'big'))
            h.update(data)
    return h.hexdigest()


def main():
    prior = {}
    expected_seals = {
        'PRE_SEAL.json': '71ed041319a34f1a58a53bddbf1e7686094cb7fc7a0ca92886dbb6209868828f',
        'POST_SEAL.json': '3152d1e7a2bacd06f615f97ec0de54d0dc0f7f109af1347e25d31771b0373b38'}
    for rel, expected in expected_seals.items():
        seal = readj(HERE / rel)
        rows = {member: sha(HERE / member) == value for member, value in seal['files'].items()}
        prior[rel] = {'sha256': sha(HERE / rel), 'member_count': len(rows),
                      'all_members_unchanged': all(rows.values())}
        check('frozen ' + rel, sha(HERE / rel) == expected and all(rows.values()), members=rows)

    for stage, name in [('initial', 'PUBLICATION_INITIAL_SOURCE_PINS.json'),
                        ('final', 'PUBLICATION_SOURCE_PINS.json')]:
        pins = readj(HERE / name)
        rows = []
        for item in pins['sources']:
            snap = HERE / item['snapshot']
            ok = sha(snap) == item['sha256'] and snap.stat().st_size == item['bytes']
            if stage == 'final':
                ok = ok and Path(item['source']).read_bytes() == snap.read_bytes()
            rows.append({'snapshot': item['snapshot'], 'pass': ok})
        check(stage + ' snapshot pins' + (' and current sources' if stage == 'final' else ''),
              all(row['pass'] for row in rows), members=rows)

    initial = HERE / 'publication_initial_sources/worktree'
    final = HERE / 'publication_final_sources/worktree'
    oldnote, note = (initial / NOTE).read_text(), (final / NOTE).read_text()
    addition = ('Fix t>0 and delta,K,kappa>0. Take the joint integer-spin limit\n'
                'S->infinity with epsilon^2 S(S+1)=delta/K. These parameters, the cube,\n'
                'the canonical input and the original instrument are fixed as specified.\n\n')
    marker = '**Status:** proposed_retained\n\n'
    check('sole note correction restores explicit fixed-parameter integer-spin limit',
          oldnote.count(marker) == 1 and addition not in oldnote
          and note == oldnote.replace(marker, marker + addition, 1))
    pre = (HERE / 'PRE.md').read_text()
    proof_start = 'The cube has A='
    pre_proof = pre[pre.index(proof_start):pre.index('No unresolved mathematical step')]
    final_proof = note[note.index(proof_start):note.index('The proof depends on the stated source expansion')]
    check('complete conventions, sections 1-5 proof and section 6 exclusions identical to PRE',
          final_proof == pre_proof, shared_characters=len(pre_proof),
          shared_sha256=hashlib.sha256(pre_proof.encode()).hexdigest())
    check('final publication runner unchanged from initial attempt',
          (initial / RUNNER).read_bytes() == (final / RUNNER).read_bytes())

    pubtree = ast.parse((final / RUNNER).read_text())
    primtree = ast.parse((HERE / 'primitive_source_check.py').read_text())
    toytree = ast.parse((HERE / 'released_sources/recent_birth_controls.py').read_text())
    pubf, primf, toyf = map(functions, (pubtree, primtree, toytree))
    prim_helpers = ['clean', 'add', 'hop', 'birth', 'mark', 'adjoint_product_polynomial', 'check_gauss']
    toy_helpers = ['subnormalized_fisher', 'controls']
    helpers = {name: dump(pubf[name]) == dump(primf[name]) for name in prim_helpers}
    helpers.update({name: dump(pubf[name]) == dump(toyf[name]) for name in toy_helpers})
    check('all nine reused helpers have identical ASTs', all(helpers.values()), helpers=helpers)
    puba, prima = map(assignments, (pubtree, primtree))
    consts = {name: dump(puba[name]) == dump(prima[name]) for name in ['A', 'B', 'EDGES', 'OMEGA']}
    check('primitive graph and zero-field input definitions unchanged', all(consts.values()), constants=consts)

    adapted = copy.deepcopy(primf['main'])
    expected_removed = ast.parse("here = Path(__file__).resolve().parent\n"
                                "(here / 'PRIMITIVE_SOURCE_RESULTS.json').write_text(json.dumps(result, indent=2) + '\\n')\n"
                                "print(json.dumps(result, indent=2))\n").body
    removed_ok = [dump(x) for x in adapted.body[-3:]] == [dump(x) for x in expected_removed]
    adapted.name = 'primitive_source_controls'
    adapted.body = adapted.body[:-3] + [ast.Return(value=ast.Name(id='result', ctx=ast.Load()))]
    check('primitive main only renamed and output statements replaced by return',
          removed_ok and dump(adapted) == dump(pubf['primitive_source_controls']))
    primsha = sha(HERE / 'primitive_source_check.py')
    toysha = sha(HERE / 'released_sources/recent_birth_controls.py')
    check('disclosed reused-code provenance constants match sealed originals',
          ast.literal_eval(puba['INDEPENDENT_PRIMITIVE_SOURCE_SHA']) == primsha
          and ast.literal_eval(puba['ROOT_TOY_SOURCE_SHA']) == toysha)

    old_primitive = readj(HERE / 'PRIMITIVE_SOURCE_RESULTS.json')
    old_toy = readj(HERE / 'released_sources/RECENT_BIRTH_CONTROL_RESULTS.json')
    inputs = ast.literal_eval(puba['AUDIT_INPUT_PATHS'])
    check('declared timeout and five authorized note inputs',
          ast.literal_eval(puba['AUDIT_TIMEOUT_SEC']) == 120
          and inputs == (NOTE,
              'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md',
              'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
              'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md',
              'docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md'))
    stages = {}
    for stage, worktree in [('initial', initial), ('final', final)]:
        external = worktree.parent / 'external'
        execution = readj(external / 'NINTH_PUBLICATION_CACHE_EXECUTION.json')
        ex = execution['result']
        result = readj(worktree / RESULT)
        manifest = readj(external / 'NINTH_PUBLICATION_FROZEN_SOURCES.json')
        root_check = readj(external / 'NINTH_PRIMARY_ROOT_VERIFICATION.json')
        runner_sha = sha(worktree / RUNNER)
        fp = fingerprint(worktree, inputs)
        expected_cache = (
            '===== runner cache v1 =====\n'
            f'runner: {RUNNER}\n'
            f'runner_sha256: {runner_sha}\n'
            f'input_fingerprint_sha256: {fp}\n'
            f'timeout_sec: {ex["timeout_sec"]}\n'
            f'exit_code: {ex["exit_code"]}\n'
            f'elapsed_sec: {ex["elapsed_sec"]:.2f}\n'
            f'status: {ex["status"]}\n'
            f'----- stdout -----\n{ex["stdout"]}\n'
            f'----- stderr -----\n{ex["stderr"]}\n')
        parsed, end = json.JSONDecoder().raw_decode(ex['stdout'])
        check(stage + ' recorded execution is successful and stdout completely bound to result',
              ex['runner'] == RUNNER and ex['status'] == 'ok' and ex['exit_code'] == 0
              and ex['stderr'] == '' and ex['timeout_sec'] == 120
              and parsed == result and ex['stdout'][end:] == '\nTOTAL: PASS=2 FAIL=0\n'
              and ex['stdout'] == (worktree / RESULT).read_text() + 'TOTAL: PASS=2 FAIL=0\n'
              and len(ex['stdout']) < 200000
              and execution['cache_path'] == str(PUBLICATION / CACHE))
        check(stage + ' whole cache matches execution, runner hash and independent input fingerprint',
              (worktree / CACHE).read_text() == expected_cache, input_fingerprint_sha256=fp)
        check(stage + ' external frozen-source manifest and verification hashes agree',
              manifest['base_revision'] == 'c234d47c9d99b7fd5590957ec08d9083877d25e6'
              and manifest['files_sha256'] == {NOTE: sha(worktree / NOTE), RUNNER: runner_sha}
              and root_check['result_sha256'] == sha(worktree / RESULT)
              and root_check['cache_sha256'] == sha(worktree / CACHE)
              and root_check['seconds'] == ex['elapsed_sec']
              and root_check.get('note_sha256', sha(worktree / NOTE)) == sha(worktree / NOTE)
              and root_check.get('runner_sha256', runner_sha) == runner_sha)
        check(stage + ' all 36 primitive result rows and remaining scientific payload reused exactly',
              without(result['primitive_sources'], 'source_sha256')
              == without(old_primitive, 'source_sha256')
              and result['primitive_sources']['source_sha256'] == runner_sha)
        check(stage + ' complete eight-row toy payload reused exactly',
              result['toy'] == without(old_toy, 'elapsed_seconds', 'source_sha256'))
        check(stage + ' top-level source and provenance identities correct',
              result['source_sha256'] == runner_sha
              and result['provenance'] == {'reused_independent_primitive_source': primsha,
                                           'reused_root_toy_source': toysha})
        stages[stage] = {'note_sha256': sha(worktree / NOTE), 'runner_sha256': runner_sha,
                         'result_sha256': sha(worktree / RESULT), 'cache_sha256': sha(worktree / CACHE),
                         'input_fingerprint_sha256': fp, 'recorded_execution_seconds': ex['elapsed_sec'],
                         'runner_internal_seconds': result['elapsed_seconds'],
                         'complete_stdout_characters': len(ex['stdout']), 'result': result}

    check('initial-to-final result changes only elapsed_seconds',
          without(stages['initial']['result'], 'elapsed_seconds')
          == without(stages['final']['result'], 'elapsed_seconds'))
    check('restored declared note input changes fingerprint',
          stages['initial']['input_fingerprint_sha256'] != stages['final']['input_fingerprint_sha256'])

    toy = stages['final']['result']['toy']
    row = next(r for r in toy['rows'] if r['t'] == .6 and r['epsilon'] == .015)
    prose = {'eps4_full_variance': '4.49336', 'limiting_eps4_variance': '4.49237',
             'eps4_recent_within_path_variance': '2.41397', 'recent_variance_target': '2.41509',
             'full_mean': '3.45643', 'limiting_mean': '3.45567', 'full_Fisher': '1.53044'}
    check('all seven toy values quoted in numerical prose round correctly',
          all(format(row[key], '.5f') == value and value in note for key, value in prose.items()),
          rounded_values=prose)
    par = toy['parameters']
    analytic_integral = 1 / par['kappa'] + par['kappa'] / (2 * (par['delta'] * par['g']) ** 2)
    check('POST analytic toy integral agrees with saved value and quoted digits',
          abs(analytic_integral - toy['fast_integral_infinite']) < 2e-14
          and format(analytic_integral, '.14f') == '2.68491124260355'
          and '2.68491124260355' in note, analytic_integral=analytic_integral)
    check('literal zero comparator remains expressly labeled',
          all(r['field_only_mutant_high_probability'] == 0 for r in toy['rows'])
          and 'literal zero comparator, not a separately run mutation' in note)

    for info in stages.values():
        del info['result']
    out = {'scope': 'Complete source/AST/payload/cache correspondence and arithmetic check; no scientific runner execution, independent numerical replication, or audit verdict.',
           'status': 'PASS' if all(item['pass'] for item in CHECKS) else 'FAIL',
           'checker_sha256': sha(Path(__file__)), 'prior_seals': prior,
           'publication_attempts': stages, 'checks': CHECKS,
           'preserved_finding': 'Initial omitted integer-spin scaling hypothesis; final note restores it, with fresh recorded execution and changed declared-input fingerprint.'}
    text = json.dumps(out, indent=2) + '\n'
    (HERE / 'PUBLICATION_EVIDENCE_CHECK.json').write_text(text)
    print(text, end='')
    raise SystemExit(0 if out['status'] == 'PASS' else 1)


if __name__ == '__main__':
    main()
