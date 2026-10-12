#!/usr/bin/env python3
"""Open processed targets only after the frozen three-source numerical gates."""
import datetime as dt
import hashlib
import json
from pathlib import Path

import numpy as np

from direct_qumond_disk import DATA, guard, sha

OUT = DATA / 'qumond_disk'
NAMES = ['NGC2976', 'UGC07577', 'KK98-251']
SOURCE = '701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00'


def read(name):
    return json.loads((OUT / name).read_text())


def relative_change(a, b):
    return float(np.max(np.abs(np.asarray(a) / np.asarray(b) - 1)))


def numerical_gates():
    frozen = read('contract_and_subset_freeze.json')
    assert frozen['initial_selected'] == NAMES
    assert sha(Path(__file__).with_name('FROZEN_FORWARD_CONTRACT.md')) == frozen['contract_sha256']
    assert sha(Path(__file__).with_name('direct_qumond_disk.py')) == SOURCE
    for filename, digest in frozen['source_hashes'].items():
        assert sha(DATA / filename) == digest, filename
    controls = read('direct_controls_v4.json')
    assert controls['source_sha256'] == SOURCE and controls['passed']
    provenance = {}
    rows = []
    for name in NAMES:
        tags = ['coarse_v1', 'fine_v1', 'fine_newtonian_v1', 'high_v3', 'higher_v3', 'boundary_v4']
        if name == 'UGC07577':
            tags.append('ell512_v4')
        values = {tag: read(f'direct_{name}_{tag}.json') for tag in tags}
        for tag in tags:
            filename = f'direct_{name}_{tag}.json'
            provenance[filename] = {'sha256': sha(OUT / filename),
                                    'solver_sha256': values[tag]['source_sha256']}
        fine = values['fine_v1']['projection']
        coarse = values['coarse_v1']['projection']
        high = values['high_v3']['projection']
        higher = values['higher_v3']['projection']
        final = values['boundary_v4']
        assert final['source_sha256'] == SOURCE
        for tag in tags:
            assert values[tag]['source_npz_sha256'] == frozen['source_hashes']['baryonic_forward_64.npz']
            assert values[tag]['U'] == final['U'] and values[tag]['a0_SI'] == final['a0_SI']
            assert values[tag]['projection']['R'] == final['projection']['R']
        prev, current = ((higher, values['ell512_v4']['projection']) if name == 'UGC07577'
                         else (high, higher))
        newton = values['fine_newtonian_v1']['projection']
        tests = {
            'newtonian_midplane': [final['newtonian_midplane_relative_error'], 2e-6],
            'newtonian_projection': [relative_change(newton['full'], newton['newtonian']), .003],
            'last_angular_refinement': [relative_change(current['full'], prev['full']), .005],
            'boundary_hankel_grid_change': [relative_change(final['projection']['full'], current['full']), .003],
        }
        rows.append({'name': name, 'gates': tests,
                     'passed': all(value <= limit for value, limit in tests.values()),
                     'final_metadata': final['projection']['metadata'],
                     'final_hankel_order': final['hankel'],
                     'earlier_coarse_to_fine_change': relative_change(fine['full'], coarse['full']),
                     'earlier_l128_to_l256_change': relative_change(higher['full'], high['full']),
                     'force_ratio_minmax': [min(final['full_over_algebraic']), max(final['full_over_algebraic'])]})
    return {
        'at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'contract_sha256': frozen['contract_sha256'],
        'solver_sha256': SOURCE,
        'controls_sha256': sha(OUT / 'direct_controls_v4.json'),
        'passed': all(row['passed'] for row in rows),
        'rows': rows, 'receipts': provenance,
        'working_relative_force_budget': .01,
        'limits': 'Finite refinement evidence, not an interval certificate. Boundary check also doubles Hankel order and changes radial spacing. Different source versions only repaired controls/zero-field diagnostics, not positive-field projection mathematics. Full numerical history retained. Three exposed training sources, fixed geometry and parameters.'}


def main():
    guard()
    gates_path = OUT / 'DIRECT_NUMERICAL_GATES.json'
    score_path = OUT / 'DIRECT_FIXED_COMPARISON.json'
    assert not gates_path.exists() and not score_path.exists(), 'Never overwrite research receipts'
    source_hash = sha(__file__)
    gates = numerical_gates()
    gates_path.write_text(json.dumps(gates, indent=2) + '\n')
    assert gates['passed'], 'Do not read observed velocities before every numerical gate passes'
    # These data have been exposed by prior algebraic fits; this is a forward
    # model-development comparison, not a new blind test or likelihood.
    rows = []
    with np.load(DATA / 'baryonic_forward_64.npz') as forward, np.load(DATA / 'sealed_targets.npz') as targets:
        for name in NAMES:
            final = read(f'direct_{name}_boundary_v4.json')
            field = final['projection']
            radius = np.asarray(field['R'])
            mask = forward[name + '_score_mask']
            assert np.array_equal(radius, forward[name + '_R'][mask])
            observed = targets[name + '_v'][mask]
            error = targets[name + '_error'][mask]
            assert np.all(np.isfinite(observed) & (observed > 0))
            predictions, scores = {}, {}
            for kind in ['newtonian', 'algebraic', 'local_norm', 'full']:
                force = np.asarray(field[kind])
                assert np.all(np.isfinite(force) & (force > 0)), 'Nonpositive radial force requires explicit model failure reporting'
                velocity = np.sqrt(radius * force)
                residual = np.log10(velocity / observed)
                predictions[kind] = velocity.tolist()
                scores[kind] = {'rms_log10_velocity': float(np.sqrt(np.mean(residual ** 2))),
                                'mean_log10_velocity': float(np.mean(residual)),
                                'log10_residual': residual.tolist()}
            rows.append({'name': name, 'data_role': 'previously exposed training source',
                         'R_kpc': radius.tolist(), 'observed_km_s': observed.tolist(),
                         'processed_error_km_s': error.tolist(), 'predictions_km_s': predictions,
                         'scores': scores, 'fixed_stellar_U': final['U'], 'fixed_a0_SI': final['a0_SI']})
    combined = {kind: {'galaxy_equal_rms_log10_velocity': float(np.sqrt(np.mean([
                             row['scores'][kind]['rms_log10_velocity'] ** 2 for row in rows]))),
                       'galaxy_equal_mean_log10_velocity': float(np.mean([
                             row['scores'][kind]['mean_log10_velocity'] for row in rows]))}
                for kind in ['newtonian', 'algebraic', 'local_norm', 'full']}
    assert sha(__file__) == source_hash
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'source_sha256': source_hash,
              'numerical_gates_sha256': sha(gates_path), 'targets_sha256': sha(DATA / 'sealed_targets.npz'),
              'score': 'Unweighted log10 velocity residual within each galaxy; equal total weight per galaxy.',
              'combined': combined, 'per_galaxy': rows,
              'limits': 'No parameters refitted; no likelihood or significance, no covariance treatment. Fixed distances, inclinations, vertical source models, isolated boundary and processed baryonic reconstructions are conditional. This is not a full sample QUMOND calibration or validation of the earlier solar prediction.'}
    score_path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'numerical_gates_passed': gates['passed'], 'combined': combined,
                      'per_galaxy': [{k: v for k, v in row.items() if k in ['name', 'scores']} for row in rows]}, indent=2))


if __name__ == '__main__':
    main()
