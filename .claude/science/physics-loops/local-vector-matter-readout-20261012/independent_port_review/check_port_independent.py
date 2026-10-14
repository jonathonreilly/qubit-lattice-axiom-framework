#!/usr/bin/env python3
"""Light port-only controls: AST, exact linkage, isolated CLI/aggregation.

Never import or run the complete author runner. Compile only its new main
and digest functions; supply immutable synthetic result fixtures in place
of the two scientific producers. All writes stay below this review folder.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'

import argparse
import ast
import base64
import contextlib
import copy
import datetime
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import sys

import numpy as np
import scipy
import sympy

HERE = Path(__file__).resolve().parent
PACK = HERE.parent
ROOT = HERE.parents[4]
RUNNER = ROOT / 'scripts/local_vector_matter_readout_2026_10_12.py'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    freeze = json.loads((HERE / 'SOURCE_FREEZE_v1.json').read_text())
    for row in freeze['paths']:
        assert sha(ROOT / row['path']) == row['sha256'], row['path']
    checked = []

    def record(name, passed, detail):
        checked.append({'name': name, 'passed': bool(passed), 'detail': detail})

    canonical = json.loads((PACK / 'evidence/CANONICAL_RUN_v1.json').read_text())
    for key, folder, elapsed in [
            ('radiation', 'direct_vector_matter_radiation', 'elapsed_sec'),
            ('readout', 'direct_vector_readout', 'elapsed_seconds')]:
        original = json.loads((PACK / 'source_recovery' / folder / 'evidence_v1/RESULTS.json').read_text())
        actual = copy.deepcopy(canonical[key])
        original.pop('source_sha256')
        original.pop(elapsed)
        actual.pop(elapsed)
        record(key + '_scientific_result_exactly_preserved', original == actual,
               'Every scientific JSON value agrees exactly; only source identities and elapsed time are excluded.')

    tree = ast.parse(RUNNER.read_text())
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    module = ast.Module(body=[copy.deepcopy(functions['digest']), copy.deepcopy(functions['main'])], type_ignores=[])
    isolated = compile(ast.fix_missing_locations(module), str(RUNNER), 'exec')
    declared = next(ast.literal_eval(node.value) for node in tree.body
                    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'AUDIT_INPUT_PATHS' for t in node.targets))
    inputs_fingerprint = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0')
    for name in declared:
        label, content = name.encode(), (ROOT / name).read_bytes()
        inputs_fingerprint.update(len(label).to_bytes(8, 'big'))
        inputs_fingerprint.update(label)
        inputs_fingerprint.update(len(content).to_bytes(8, 'big'))
        inputs_fingerprint.update(content)
    cache = (ROOT / 'logs/runner-cache/local_vector_matter_readout_2026_10_12.txt').read_text()
    record('canonical_cache_identity',
           'runner_sha256: ' + sha(RUNNER) in cache
           and 'input_fingerprint_sha256: ' + inputs_fingerprint.hexdigest() in cache
           and 'exit_code: 0' in cache and 'status: ok' in cache,
           {'runner_sha256': sha(RUNNER), 'input_fingerprint_sha256': inputs_fingerprint.hexdigest()})
    v1 = json.loads((PACK / 'evidence/CANONICAL_CACHE_RUN_v1.json').read_text())
    v2 = json.loads((PACK / 'evidence/CANONICAL_CACHE_RUN_v2.json').read_text())
    record('cache_stdout_stable_across_whitespace_only_version',
           v1['stdout'] == v2['stdout'] and v1['stderr'] == v2['stderr'] == ''
           and v1['exit_code'] == v2['exit_code'] == 0,
           'Distinct raw executions retained; no earlier result is relabelled with the later source hash.')

    fixtures = HERE / 'io_fixtures'
    fixtures.mkdir(exist_ok=True)
    attempts = []

    def invoke(label, arguments=(), radiation=None, readout=None,
               fail_radiation=False, fail_readout=False):
        r = copy.deepcopy(canonical['radiation'] if radiation is None else radiation)
        d = copy.deepcopy(canonical['readout'] if readout is None else readout)
        calls = []

        def radiation_fixture():
            calls.append('radiation')
            if fail_radiation:
                raise AssertionError('reviewer injected scientific producer failure')
            return r

        def readout_fixture():
            calls.append('readout')
            if fail_readout:
                raise AssertionError('reviewer injected scientific producer failure')
            return d

        scope = {'argparse': argparse, 'Path': Path, 'np': np, 'json': json,
                 'hashlib': hashlib, 'sys': sys, 'scipy': scipy, 's': sympy,
                 'ROOT': ROOT, '__file__': str(RUNNER), 'AUDIT_INPUT_PATHS': declared,
                 'radiation_controls': radiation_fixture, 'readout_controls': readout_fixture}
        exec(isolated, scope)
        output, errors = io.StringIO(), io.StringIO()
        old_argv = sys.argv
        exception = None
        try:
            sys.argv = [str(RUNNER), *map(str, arguments)]
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
                scope['main']()
        except (Exception, SystemExit) as exc:
            exception = {'type': type(exc).__name__, 'message': str(exc)}
        finally:
            sys.argv = old_argv
        attempt = {'label': label, 'argv': list(map(str, arguments)), 'producer_calls': calls,
                   'stdout': output.getvalue(), 'stderr': errors.getvalue(), 'exception': exception}
        attempts.append(attempt)
        return attempt

    first, second = invoke('default_first'), invoke('default_second')
    record('repeatable_default_output', first['stdout'] == second['stdout'] == v2['stdout']
           and first['exception'] is None and second['exception'] is None,
           'Only new entrypoint/digest AST executed; scientific producer fixtures are fixed copies of preserved results.')
    sidecar = fixtures / 'same_run.json'
    json_run = invoke('json_plus_exclusive_sidecar', ['--json', '--output-json', sidecar])
    parsed = json.loads(json_run['stdout'])
    record('json_and_sidecar_same_result', json_run['exception'] is None
           and sidecar.read_text() == json_run['stdout'] and parsed['checks_passed'] == 11
           and parsed['checks_failed'] == 0 and len(parsed['check_families']) == 11,
           {'sidecar_sha256': sha(sidecar), 'families': list(parsed['check_families'])})
    before = sidecar.read_bytes()
    collision = invoke('sidecar_collision', ['--output-json', sidecar])
    record('exclusive_sidecar_collision_preserves_existing_bytes',
           collision['exception']['type'] == 'FileExistsError' and sidecar.read_bytes() == before
           and collision['stdout'] == '',
           'Producer calls precede exclusive open; collisions fail without overwriting evidence or printing PASS.')

    for which in ['radiation', 'readout']:
        outcome = invoke(which + '_producer_assertion', **{'fail_' + which: True})
        record(which + '_producer_failure_stops_publication', outcome['exception']['type'] == 'AssertionError'
               and not outcome['stdout'], {'producer_calls': outcome['producer_calls']})

    def failing_mutation(label, mutate_r=None, mutate_d=None):
        r, d = copy.deepcopy(canonical['radiation']), copy.deepcopy(canonical['readout'])
        if mutate_r:
            mutate_r(r)
        if mutate_d:
            mutate_d(d)
        outcome = invoke(label, radiation=r, readout=d)
        record(label, outcome['exception'] is not None
               and outcome['exception']['type'] == 'AssertionError' and not outcome['stdout'],
               {'exception': outcome['exception']})

    failing_mutation('reject_missing_radiation_row', lambda r: r['controls'].pop())
    failing_mutation('reject_wrong_angular_power', lambda r: r['controls'][0]['angular_tensor_power'].__setitem__(0, 0))
    failing_mutation('reject_nonzero_odd_density', lambda r: r['controls'][0].__setitem__('max_odd_density_coefficient', .1))
    failing_mutation('reject_wrong_convergence', lambda r: r['controls'][0].__setitem__('relative_to_leading_minus_one', r['controls'][1]['relative_to_leading_minus_one']))
    failing_mutation('reject_failed_radiation_alternative', lambda r: r['mutations'][0].__setitem__('detected', False))
    failing_mutation('reject_missing_bracket_endpoint', lambda r: r['calibration_example']['sqrt_q_bracket'].pop())
    failing_mutation('reject_reported_readout_failure', mutate_d=lambda d: d.__setitem__('fail_count', 1))
    failing_mutation('reject_duplicate_readout_family', mutate_d=lambda d: d['families'][1].__setitem__('family', d['families'][0]['family']))

    # Record the aggregation's exact scope: it summarizes asserted producer
    # completion; it is not an independent verifier of arbitrary returned data.
    altered = copy.deepcopy(canonical['readout'])
    altered['families'][-1]['wrong_sign_detected'] = False
    diagnostic = invoke('aggregation_scope_false_payload_without_producer_failure', readout=altered)
    record('aggregation_scope_documented', diagnostic['exception'] is None,
           'The readout family map uses literal True after its producer returns. Artificially false payload fields with fail_count=0 are not independently revalidated. In the unchanged real producer, corresponding assertions execute before return; their failures propagate, as tested above. This is a summary layer, not a second math verifier.')

    # Independent exact linkage check, using rational bisection in r^2 instead
    # of the author's floating root search in sqrt(q).
    # Equality of squared positive sides: 36 q^7 = (21q+20)^2.
    def comparison_polynomial(q):
        return 36*q**7 - (21*q+20)**2

    lo, hi = Fraction(1), Fraction(3)
    assert comparison_polynomial(lo) < 0 < comparison_polynomial(hi)
    for _ in range(150):
        mid = (lo + hi)/2
        if comparison_polynomial(mid) < 0:
            lo = mid
        else:
            hi = mid
    speed_sq_lo, speed_sq_hi = 1/hi, 1/lo
    potential_lo, potential_hi = 2*lo/(1+lo), 2*hi/(1+hi)
    vertical_lo, vertical_hi = (3-hi)/(1+hi), (3-lo)/(1+lo)
    expected = canonical['radiation']['calibration_example']
    record('cross_block_calibration_is_stable_and_anisotropic',
           1 < lo < hi < 3 and 0 < speed_sq_lo < speed_sq_hi < 1
           and 1 < potential_lo < potential_hi < 2 and 0 < vertical_lo < vertical_hi < 1
           and abs(float((lo+hi)/2)-expected['q_approx']) < 1e-14,
           {'q_lower': str(lo), 'q_upper': str(hi), 'r_squared_interval': [str(speed_sq_lo), str(speed_sq_hi)],
            'polar_equatorial_ratio_interval': [str(potential_lo), str(potential_hi)],
            'vertical_squared_frequency_ratio_interval': [str(vertical_lo), str(vertical_hi)],
            'independent_elimination': 'With r=cT/cL, static ratio=2/(1+r^2), vertical ratio=(3r^2-1)/(1+r^2).',
            'domain': 'Unique q>=1 root already proved monotone; positive square-root branch preserved when squaring. These are conditional calibration consequences, not observation fits.'})

    # Scale-free sphere moments independently check the radiation coefficients.
    # Sphere averages <nx^2 ny^2>=1/15 and <nx^2 ny^2 nz^2>=1/105.
    transverse = Fraction(64, 4) * (Fraction(1, 15)-Fraction(1, 105))
    longitudinal = Fraction(64, 4) * Fraction(1, 105)
    record('sphere_moment_power_normalization',
           transverse == Fraction(32, 35) and longitudinal == Fraction(16, 105),
           {'transverse': str(transverse), 'longitudinal': str(longitudinal),
            'route': 'At one orbital phase n.Ithird.n=-8 nx ny in units reduced_mass*a^2*Omega^3; sphere moments and G/(16*pi*alpha) give these coefficients. No author quadrature executed.'})

    for row in freeze['paths']:
        assert sha(ROOT / row['path']) == row['sha256'], row['path']
    result = {'schema': 'independent_canonical_port_controls_v1',
              'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'script_sha256': sha(Path(__file__)), 'frozen_source_manifest_sha256': sha(HERE/'SOURCE_FREEZE_v1.json'),
              'full_author_runner_imported_or_executed': False,
              'author_numerical_producer_executed': False,
              'isolated_author_code_executed': ['main AST', 'digest AST'],
              'checks': checked, 'checks_passed': sum(x['passed'] for x in checked),
              'checks_failed': sum(not x['passed'] for x in checked), 'isolated_attempts': attempts}
    with (HERE/'PORT_CONTROLS_v1.json').open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'passed': result['checks_passed'], 'failed': result['checks_failed'],
                      'isolated_attempts': len(attempts), 'result_sha256': sha(HERE/'PORT_CONTROLS_v1.json')}))
    if result['checks_failed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
