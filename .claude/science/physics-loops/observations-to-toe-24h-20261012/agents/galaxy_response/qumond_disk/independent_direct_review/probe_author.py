#!/usr/bin/env python3
"""Run the author as subject against independently frozen source controls."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
from numpy.polynomial.legendre import Legendre

ROOT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT = ROOT/'galaxy_response/qumond_disk/independent_direct_review'


def guard():
    assert time.time() < json.loads((ROOT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((ROOT/n).exists() for n in
                   ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'))


def field_for(row):
    ell, alpha, beta = row['ell'], row['alpha'], row['beta']
    polynomial = Legendre.basis(ell)
    derivative = polynomial.deriv()
    def field(R, z):
        radius = np.hypot(R, z)
        c, s = z/radius, R/radius
        profile = radius**(ell-1)*np.exp(-radius)
        ar = alpha*profile*polynomial(c)
        at = -beta*profile*s*derivative(c)
        return s*ar+c*at, c*ar-s*at
    return field


def check(source, fixture, mutate=False):
    guard()
    code = source.read_text()
    if mutate:
        old = 'full = local_norm - correction_modes.sum(axis=1)'
        assert code.count(old) == 1
        code = code.replace(old, 'full = local_norm.copy()')
    # Execute the subject only. Independent expectations were written by a
    # different program that does not load this namespace or these helpers.
    subject = {'__name__':'review_subject', '__file__':str(source)}
    exec(compile(code, str(source), 'exec'), subject)
    own_controls = subject['controls']()
    rows = []
    for fixture_row in fixture['projection_controls']:
        R = np.array(fixture_row['R'])
        exact = np.array(fixture_row['expected_midplane'])
        by_grid = []
        for nr in (384, 768, 1536):
            result = subject['project'](field_for(fixture_row), R, 1e-5, 100., 1.,
                                        nr=nr, nc=32, lmax=8, newtonian=True)
            scale = float(np.max(np.abs(exact)))
            by_grid.append({'nr':nr, 'calculated':result['full'].tolist(),
                            'max_absolute':float(np.max(np.abs(result['full']-exact))),
                            'max_normalized':float(np.max(np.abs(result['full']-exact))/scale)})
        rows.append({**fixture_row, 'subject_results':by_grid})
    vertical_errors = []
    for row in fixture['vertical_controls']:
        Z, V = subject['vertical'](np.array([row['k']]),np.array([row['z']]),row['h'])
        vertical_errors.extend([abs(float(Z[0,0])-row['Z']),abs(float(V[0,0])-row['V'])])
    return {'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'mutated_drop_nonlocal_correction':mutate,
            'author_controls':own_controls, 'projection_controls':rows,
            'vertical_absolute_error':max(vertical_errors)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source',type=Path, default=Path(__file__).with_name('snapshot_direct_qumond_disk.py'))
    parser.add_argument('--name',default='author_probe_v1.json')
    args = parser.parse_args()
    fixture_path = OUT/'independent_fixture_v1.json'
    fixture = json.loads(fixture_path.read_text())
    started = time.time()
    result = {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'fixture_sha256':hashlib.sha256(fixture_path.read_bytes()).hexdigest(),
              'original':check(args.source,fixture), 'mutation':check(args.source,fixture,True),
              'elapsed_seconds':time.time()-started,
              'max_rss':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    with (OUT/args.name).open('x') as file:
        json.dump(result,file,indent=2)
        file.write('\n')
    for tag in ('original','mutation'):
        row = result[tag]
        print(tag,'author_controls_passed',row['author_controls']['passed'],
              'vertical_error',row['vertical_absolute_error'])
        print([(r['ell'],r['alpha'],r['beta'],
                [(v['nr'],v['max_normalized']) for v in r['subject_results']])
               for r in row['projection_controls']])
    print('elapsed_seconds',result['elapsed_seconds'],'max_rss',result['max_rss'])
