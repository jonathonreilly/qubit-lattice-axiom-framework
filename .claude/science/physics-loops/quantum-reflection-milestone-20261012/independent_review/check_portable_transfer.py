#!/usr/bin/env python3
"""Scoped transfer checks; writes only to this independent review directory."""
import os
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import sys
sys.dont_write_bytecode = True
import ast
import datetime as dt
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re
import subprocess
import time

import mpmath as mp
import sympy as sy

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[4]
PACK = OUT.parent
NOTE = 'docs/SPHERE_QUANTUM_VISIBILITY_REFLECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md'
RUNNER = 'scripts/sphere_quantum_visibility_reflection_2026_10_12.py'
CACHE = 'logs/runner-cache/sphere_quantum_visibility_reflection_2026_10_12.txt'
ORIGIN = Path('/Users/jonBridger/.codex/worktrees/observations-to-toe-24h-20261012/New Axioms Lets Go/.claude/science/physics-loops/observations-to-toe-24h-20261012/agents/boundary_quantum/sphere_completion')
PRIOR_RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/quantum')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def q(value):
    return F(int(value['numerator']), int(value['denominator']))


def node_map(source):
    return {n.name:n for n in ast.parse(source).body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}


def main():
    started = time.time()
    freeze = json.loads((PACK/'evidence/SOURCE_FREEZE_v2.json').read_text())
    identities = {path:sha(ROOT/path) for path in freeze['paths']}
    assert identities == freeze['paths']
    note = (ROOT/NOTE).read_text()
    source = (ROOT/RUNNER).read_text()
    assert identities[NOTE] == 'cd2f4f552f3f95b3e91e0ab046f0bf3da2a29f52383f7e920b316afd99d1a3ef'
    assert identities[RUNNER] == 'cf57773d518b09544dfdb75e0aa91bc8f1a18786d6c895ff2b51955c240482dc'
    compile(source, RUNNER, 'exec')
    mutation = json.loads((PACK/'evidence/MUTATIONS_v1.json').read_text())
    assert hashlib.sha256((source+'\n').encode()).hexdigest() == mutation['source_sha256']
    assert len(mutation['mutations']) == 9 and mutation['all_detected']
    mutation_summary = []
    for row in mutation['mutations']:
        assert source.count(row['old']) == 1
        assert row['exit'] != 0 and row['intended_failure_observed']
        assert 'FAIL '+row['family']+':' in row['stdout']
        mutation_summary.append({'family':row['family'],'exit':row['exit'],
                                 'intended_failure_present':True})

    old_helpers = node_map((ORIGIN/'sphere_certificate.py').read_text())
    new_helpers = node_map(source)
    identical_helpers = []
    for name in ('atan_fraction_interval','pi_interval','IV','polynomial','sincos_interval','exp_interval'):
        assert ast.dump(old_helpers[name], include_attributes=False) == ast.dump(new_helpers[name], include_attributes=False)
        identical_helpers.append(name)
    tree = ast.parse(source)
    imports = [ast.unparse(n) for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom))]
    io = [ast.unparse(n) for n in ast.walk(tree) if isinstance(n,ast.Call)
          and (isinstance(n.func,ast.Name) and n.func.id in ('open','eval','exec','__import__')
               or isinstance(n.func,ast.Attribute) and n.func.attr in
               ('read_text','read_bytes','write_text','write_bytes','load','loads','run','Popen'))]
    assert not io
    metadata = {n.targets[0].id:ast.literal_eval(n.value) for n in tree.body
                if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name)
                and n.targets[0].id in ('AUDIT_TIMEOUT_SEC','AUDIT_INPUT_PATHS')}
    assert metadata == {'AUDIT_TIMEOUT_SEC':120,'AUDIT_INPUT_PATHS':(NOTE,)}

    sys.path.insert(0,str(ROOT/'scripts'))
    import runner_cache
    assert runner_cache.cache_status(RUNNER) == 'fresh'
    assert runner_cache.declared_timeout_for(RUNNER) == 120
    input_hash = runner_cache.declared_input_fingerprint(RUNNER)
    cache_path,header,cache_body = runner_cache.load_cache(RUNNER)
    assert header['input_fingerprint_sha256'] == input_hash
    raw = json.loads((PACK/'evidence/RUN_RAW_v2.json').read_text())
    assert raw['exit_code'] == 0 and raw['status'] == 'ok'
    cached_stdout = cache_body.split('----- stdout -----\n',1)[1].split('\n----- stderr -----',1)[0].rstrip('\n')
    assert cached_stdout == raw['stdout'].rstrip('\n')

    before_cache = sha(ROOT/CACHE)
    result = subprocess.run([sys.executable,RUNNER,'--json'],cwd=ROOT,
                            capture_output=True,text=True,timeout=120,env=os.environ.copy())
    (OUT/'PORTABLE_JSON_RUN_v1.json').write_text(json.dumps({
        'command':[sys.executable,RUNNER,'--json'],'exit_code':result.returncode,
        'stdout':result.stdout,'stderr':result.stderr},indent=2)+'\n')
    assert result.returncode == 0 and not result.stderr
    run = json.loads(result.stdout)
    assert run['pass'] == 9 and run['fail'] == 0 and len(run['checks']) == 9
    assert all(row['passed'] for row in run['checks'])
    assert sha(ROOT/CACHE) == before_cache
    families = {row['name']:row['detail'] for row in run['checks']}
    old_result = json.loads((PRIOR_RUNTIME/'direct_reflection/RESULTS_v1.json').read_text())
    independent = json.loads((PRIOR_RUNTIME/'direct_reflection/independent_reflection_review/CHECKS_v1.json').read_text())
    assert sha(PRIOR_RUNTIME/'direct_reflection/RESULTS_v1.json') == independent['author_results_sha256']
    cert = families['degree_three_exact_enclosure']
    assert list(map(q,cert['a3_exact_interval'])) == list(map(q,old_result['a3_interval']))
    assert list(map(q,cert['k_interval'])) == list(map(q,old_result['k_exact_interval']))
    assert q(cert['quadrature_error']) == q(old_result['quadrature_error_upper'])
    independent_interval = list(map(q,independent['independent_certificate']['independent_a3_interval']))
    assert q(cert['a3_exact_interval'][0]) < independent_interval[0] < independent_interval[1] < q(cert['a3_exact_interval'][1])

    # New exact polynomial derivation, including the corrected negative P3 case.
    c = sy.symbols('c',real=True)
    P3 = (5*c**3-3*c)/2
    def B_of_C(C):
        return sy.simplify(-C.subs(c,1)+7*sy.integrate(P3*C,(c,-1,1)))
    exact_controls = [B_of_C(-c),B_of_C(-P3),
                      B_of_C(-sy.Rational(3,4)*(sy.Rational(5,4)*c-P3/4)),
                      B_of_C(-sy.Rational(3,4)*(c-P3/4))]
    assert exact_controls == [1,-1,sy.Rational(9,8),sy.Rational(15,16)]
    assert [float(x) for x in exact_controls] == families['reflection_diagonal_and_multiplicity']['independent_polynomial_values']
    assert sy.integrate(c*P3,(c,-1,1)) == 0
    assert sy.integrate(P3**2,(c,-1,1)) == sy.Rational(2,7)
    assert F(91,18)+2*F(7,6)*7+25 == F(835,18) < 48
    mp.mp.dps = 75
    k = mp.sqrt(2)*(mp.atanh(1/mp.sqrt(2))-mp.atanh(mp.mpf(1)/2))
    calibration_error = abs(mp.tanh(mp.atanh(mp.mpf(1)/2)+k/mp.sqrt(2))-1/mp.sqrt(2))
    assert calibration_error < mp.mpf('1e-70')

    sys.path.insert(0,str(ROOT/'docs/audit/scripts'))
    import no_go_discipline_gate as gate
    no_go = {'source_is_no_go_artifact':gate.source_is_no_go_artifact(NOTE,note,'bounded_theorem'),
             'negative_boundary_assertion':gate._has_negative_boundary_assertion(note)}
    for flag in ('0','1'):
        os.environ['AUDIT_FORENSIC_MODE'] = flag
        no_go['requires_in_forensic_mode_'+flag] = gate.source_requires_no_go_discipline(NOTE,note,'bounded_theorem')
    assert not any(no_go.values())
    link_targets = re.findall(r'\]\(([^)]+)\)',note)
    local_links = []
    for target in link_targets:
        if target.startswith(('http://','https://')):
            continue
        resolved = ((ROOT/NOTE).parent/target).resolve()
        assert resolved.is_relative_to(ROOT) and resolved.is_file() and not resolved.is_symlink()
        local_links.append(str(resolved.relative_to(ROOT)))
    assert set(local_links) == {RUNNER,CACHE}
    assert identities == {path:sha(ROOT/path) for path in identities}
    checks = {'at':dt.datetime.now(dt.timezone.utc).isoformat(),
              'reviewer_session':'/root/direct_quantum_visibility_review',
              'checker_sha256':sha(__file__),'reviewed_sources':identities,
              'source_freeze_sha256':sha(PACK/'evidence/SOURCE_FREEZE_v2.json'),
              'runner_imports':imports,'runtime_file_IO':io,
              'literal_metadata':metadata,'cache_status':'fresh',
              'input_fingerprint_sha256':input_hash,'local_link_targets':local_links,
              'old_helper_AST_identity':identical_helpers,'mutation_evidence':mutation_summary,
              'JSON_execution_pass_count':9,'JSON_execution_fail_count':0,
              'canonical_cache_unchanged_by_execution':True,
              'rational_certificate_exactly_matches_prior_reviewed_source':True,
              'independent_interval_still_nested':True,
              'reused_independent_exact_check_sha256':sha(PRIOR_RUNTIME/'direct_reflection/independent_reflection_review/CHECKS_v1.json'),
              'new_exact_reflection_controls':[str(x) for x in exact_controls],
              'calibration_identity_error':str(calibration_error),'no_go_detector':no_go,
              'no_go_semantic_disposition':'Not a route-exhaustion or framework-wall claim; no N1-N8 packet required for this algebraic criterion and prospective bounded statistic.',
              'elapsed_seconds':time.time()-started,'combined_pipeline_executed':False,
              'limits':'Source readiness only; no integration/landing, retained status, original all-sphere classification, apparatus or empirical claim.'}
    out = OUT/'CHECKS_v1.json'
    assert not out.exists()
    out.write_text(json.dumps(checks,indent=2)+'\n')
    print(json.dumps(checks,indent=2))


if __name__ == '__main__':
    main()
