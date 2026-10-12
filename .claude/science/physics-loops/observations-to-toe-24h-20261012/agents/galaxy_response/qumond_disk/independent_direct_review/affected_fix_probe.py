#!/usr/bin/env python3
"""Same-session zero-field, correction-mutation and source-identity checks."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import datetime
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np

ROOT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = ROOT/'galaxy_response/qumond_disk/independent_direct_review'
HERE = Path(__file__).parent


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def subject(path, replacement=None):
    code = path.read_text()
    if replacement:
        old, new = replacement
        assert code.count(old) == 1
        code = code.replace(old, new)
    namespace = {'__name__':'review_subject', '__file__':str(path)}
    exec(compile(code, str(path), 'exec'), namespace)
    return namespace


def zero_checks(namespace):
    rows = []
    for test in ('zero_radial', 'zero_vector', 'negative_radial'):
        def field(R, z):
            amplitude = np.exp(-np.hypot(R, z))
            radial = -amplitude if test == 'negative_radial' else np.zeros_like(R)
            normal = np.zeros_like(z) if test == 'zero_vector' else amplitude
            return radial, normal
        try:
            result = namespace['project'](field, np.array([.4, 1., 2.]), .01, 30., .2,
                                          nr=128, nc=32, lmax=16)
            rows.append({'test':test, 'finite_full':bool(np.all(np.isfinite(result['full']))),
                         'local_norm':result['local_norm'].tolist(),
                         'full':result['full'].tolist(),
                         'algebraic_all_nan':bool(np.all(np.isnan(result['algebraic'])))})
        except Exception as exc:
            rows.append({'test':test, 'exception':type(exc).__name__, 'message':str(exc)})
    return rows


def identity_check(source):
    path = OUT/'identity_probe_subject.py'
    with path.open('xb') as stream:
        stream.write(source.read_bytes())
    namespace = subject(path)
    def perturb_during_compute():
        with path.open('a') as stream:
            stream.write('\n# Intentional review-only source-identity perturbation.\n')
        return {'passed':True}
    namespace['controls'] = perturb_during_compute
    output = OUT/'identity_probe_should_not_exist.json'
    assert not output.exists()
    before = digest(path)
    old_args = sys.argv
    sys.argv = ['review_identity', '--controls', '--output', str(output)]
    try:
        namespace['main']()
    except RuntimeError as exc:
        result = {'exception':type(exc).__name__, 'message':str(exc)}
    else:
        result = {'exception':None}
    finally:
        sys.argv = old_args
    result.update(before=before, after=digest(path), output_created=output.exists())
    return result


def main():
    assert time.time() < json.loads((ROOT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((ROOT/name).exists() for name in
                   ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'))
    original = HERE/'snapshot_direct_qumond_disk.py'
    final = HERE/'snapshot_final_direct_qumond_disk.py'
    mutations = [
        ('reverse_correction_sign',
         ('full = local_norm - correction_modes.sum(axis=1)',
          'full = local_norm + correction_modes.sum(axis=1)')),
        ('halve_correction',
         ('full = local_norm - correction_modes.sum(axis=1)',
          'full = local_norm - .5*correction_modes.sum(axis=1)')),
        ('reverse_polar_basis_sign',
         ('dtheta = -sine[:, None] * dp', 'dtheta = sine[:, None] * dp'))]
    result = {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'script_sha256':digest(__file__), 'original_sha256':digest(original),
              'final_sha256':digest(final), 'original_zero_checks':zero_checks(subject(original)),
              'final_zero_checks':zero_checks(subject(final)), 'mutations':[]}
    for name, replacement in mutations:
        control = subject(final, replacement)['controls']()
        result['mutations'].append({'name':name, 'passed':control['passed'],
                                    'checks':control['checks']})
    result['source_identity_mutation'] = identity_check(final)
    assert all('exception' not in row for row in result['final_zero_checks'])
    assert all(row['finite_full'] and row['algebraic_all_nan'] for row in result['final_zero_checks'])
    assert result['final_zero_checks'][1]['full'] == [0.,0.,0.]
    assert not any(row['passed'] for row in result['mutations'])
    assert result['source_identity_mutation']['exception'] == 'RuntimeError'
    assert not result['source_identity_mutation']['output_created']
    with (OUT/'affected_fix_probe_v4.json').open('x') as stream:
        json.dump(result,stream,indent=2)
        stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
