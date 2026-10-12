#!/usr/bin/env python3
"""Recompute frozen candidate fields without altering fitted weights or data."""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np

import direct_galaxy_response_operator as operator


def boundary_extension(name, base, source_receipt):
    """Extend both ends, preserving every interior node and vector exactly."""
    out = operator.OUT / f'newtonian_field_{name}_boundary_extension.npz'
    meta_path = out.with_suffix('.json')
    base_cache = operator.OUT / f'newtonian_field_{name}_base.npz'
    identity = {'base_cache_sha256': operator.field.sha(base_cache),
                'solver_sha256': operator.SOLVER_HASH,
                'extension_factor': 2, 'edge_hankel_order': 8192}
    if out.exists():
        meta = json.loads(meta_path.read_text())
        assert meta['identity'] == identity and meta['cache_sha256'] == operator.field.sha(out)
        with np.load(out) as archive:
            return {key: archive[key] for key in archive.files}
    operator.guard()
    source_row = source_receipt['source_row']
    old_radius = base['radius']
    logstep = np.median(np.diff(np.log(old_radius)))
    count = int(np.ceil(np.log(2) / logstep))
    low = np.geomspace(old_radius[0] / 2, old_radius[0], count + 1)[:-1]
    high = np.geomspace(old_radius[-1], old_radius[-1] * 2, count + 1)[1:]
    extra = np.r_[low, high]
    c = base['cosine']
    with np.load(operator.field.DATA / 'baryonic_forward_64.npz') as raw:
        source = operator.field.RingField(raw[name + '_A'], source_row['sigma'], raw[name + '_gas_masses'],
                                         source_receipt['U'] * raw[name + '_disk_masses'], source_row['h'], 8192)
        ur, uz = source(extra[:, None] * np.sqrt(1 - c * c), extra[:, None] * c)
    expanded = dict(base)
    expanded['radius'] = np.r_[low, old_radius, high]
    expanded['ur'] = np.concatenate([ur[:count], base['ur'], ur[count:]])
    expanded['uz'] = np.concatenate([uz[:count], base['uz'], uz[count:]])
    expanded['nr'] = np.array(int(base['nr']) + 2 * count)
    np.savez_compressed(out, **expanded)
    meta_path.write_text(json.dumps({'at': dt.datetime.now(dt.timezone.utc).isoformat(),
                                     'identity': identity, 'cache_sha256': operator.field.sha(out),
                                     'nodes_per_extension': count}, indent=2) + '\n')
    return expanded


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fits', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    operator.guard()
    assert not args.output.exists()
    source_hash = operator.field.sha(__file__)
    fits = json.loads(args.fits.read_text())
    assert fits['operator_source_sha256'] == operator.field.sha(operator.__file__)
    assert fits['protocol_sha256'] == operator.PROTOCOL_HASH
    candidates = {case['family'] + '_' + case['constraints']: case['best_sampled']
                  for case in fits['cases'] if case['best_sampled'] is not None
                  and case['best_sampled']['status'] == 0}
    # Prepare every actual candidate with its original full-precision weights.
    rows = []
    for name in ['NGC2976', 'UGC07577', 'KK98-251']:
        operator.guard()
        base_data, source_receipt, _ = operator.galaxy_geometry(name)
        base = operator.LinearProjection(base_data)
        print(f'{name}: computing the response-specific boundary extension', flush=True)
        boundary = operator.LinearProjection(boundary_extension(name, base_data, source_receipt))
        print(f'{name}: computing doubled radial/angular field grid', flush=True)
        refined_data, _, _ = operator.galaxy_geometry(name, tag='refined', refine=True)
        refined = operator.LinearProjection(refined_data)
        receipt_path = operator.OUT / f'operator_{name}_v1.json'
        receipt = json.loads(receipt_path.read_text())
        assert operator.field.sha(receipt_path) == fits['operator_receipts'][name]
        k, gn = np.array(receipt['K']), np.array(receipt['g_N'])
        results = {}
        for label, candidate in candidates.items():
            weights = np.array(candidate['weights'])
            direct_base = base.combined(weights)
            direct_refined = refined.combined(weights)
            direct_boundary = boundary.combined(weights)
            matrix_prediction = gn + k @ weights
            positive = bool(np.all(direct_base > 0) and np.all(direct_refined > 0)
                            and np.all(direct_boundary > 0) and np.all(matrix_prediction > 0))
            differences = {
                'direct_vs_matrix': float(np.max(np.abs(direct_base / matrix_prediction - 1))),
                'radial_angular_refinement': float(np.max(np.abs(direct_refined / direct_base - 1))),
                'boundary_extension': float(np.max(np.abs(direct_boundary / direct_base - 1))),
            } if positive else None
            passed = bool(positive and differences['direct_vs_matrix'] <= .003
                          and differences['radial_angular_refinement'] <= .005
                          and differences['boundary_extension'] <= .003)
            results[label] = {'passed': passed, 'positive_radial_forces': positive,
                              'relative_changes': differences,
                              'base_direct_force': direct_base.tolist(),
                              'refined_direct_force': direct_refined.tolist(),
                              'extended_boundary_force': direct_boundary.tolist(),
                              'matrix_force': matrix_prediction.tolist()}
            print(json.dumps({'name': name, 'candidate': label, 'passed': passed,
                              'relative_changes': differences}), flush=True)
        row = {'name': name, 'R_kpc': base_data['R'].tolist(), 'candidate_results': results,
               'base_geometry_sha256': operator.field.sha(operator.OUT / f'newtonian_field_{name}_base.npz'),
               'refined_geometry_sha256': operator.field.sha(operator.OUT / f'newtonian_field_{name}_refined.npz'),
               'boundary_geometry_sha256': operator.field.sha(operator.OUT / f'newtonian_field_{name}_boundary_extension.npz')}
        receipt_out = operator.OUT / f'candidate_field_validation_{name}_v1.json'
        assert not receipt_out.exists()
        receipt_out.write_text(json.dumps(row, indent=2) + '\n')
        rows.append(row)
    assert operator.field.sha(__file__) == source_hash
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'source_sha256': source_hash,
              'fits_sha256': operator.field.sha(args.fits), 'rows': rows,
              'candidate_passes': {label: all(row['candidate_results'][label]['passed'] for row in rows)
                                   for label in candidates},
              'limits': 'Actual fitted weights unchanged. Finite candidate-specific numerical evidence, not uniform column bounds or interval certification. Boundary extension preserves all interior nodes. No additional velocity data opened. Circular-speed readout and source premises remain conditional.'}
    args.output.write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    main()
