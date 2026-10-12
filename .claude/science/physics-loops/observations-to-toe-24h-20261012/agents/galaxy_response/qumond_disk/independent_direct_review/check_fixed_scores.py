#!/usr/bin/env python3
"""Independent fixed-three gates/scores from saved raw force and target arrays."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import datetime
import hashlib
import json
import math
from pathlib import Path
import time
import numpy as np

ROOT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
DATA = ROOT/'galaxy_response'
FIELD = DATA/'qumond_disk'
OUT = FIELD/'independent_direct_review'
HERE = Path(__file__).parent
KINDS = ('newtonian', 'algebraic', 'local_norm', 'full')
NAMES = ('NGC2976', 'UGC07577', 'KK98-251')
KNOWN = {'0d02f2a476d6f1edf71ae53fa84132b355ea9853703748ae98ecac76a9b0b096',
         '144cf1fa96af11fa259caa2a1585ff409f4935d851df428ef6a8152c1db60423',
         '701bc4d1ba659f9b25cd98855547864300b83c2f002a477e7bc3b2b5ac3f7b00'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def delta(new, reference):
    assert len(new) == len(reference)
    assert all(math.isfinite(x) and x > 0 for x in reference)
    assert all(math.isfinite(x) and x > 0 for x in new)
    return max(abs(x-y)/abs(y) for x, y in zip(new, reference))


def close(x, y, tol=3e-14):
    assert abs(x-y) <= tol*max(1., abs(x), abs(y)), (x, y)


def main():
    assert time.time() < read(ROOT/'DEADLINE.json')['packaging_epoch']
    assert not any((ROOT/name).exists() for name in
                   ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'))
    freeze = read(FIELD/'contract_and_subset_freeze.json')
    gates = read(FIELD/'DIRECT_NUMERICAL_GATES.json')
    score = read(FIELD/'DIRECT_FIXED_COMPARISON.json')
    original = read(DATA/'baryonic_reconstruction_64.json')
    metadata = {row['name']:row for row in original['rows']}
    assert freeze['initial_selected'] == list(NAMES)
    assert score['source_sha256'] == sha(HERE/'followup_snapshot_direct_fixed_comparison.py')
    assert score['numerical_gates_sha256'] == sha(FIELD/'DIRECT_NUMERICAL_GATES.json')
    assert score['targets_sha256'] == sha(DATA/'sealed_targets.npz')
    assert gates['controls_sha256'] == sha(FIELD/'direct_controls_v4.json')
    assert gates['solver_sha256'] == sha(HERE/'snapshot_final_direct_qumond_disk.py')
    assert gates['contract_sha256'] == sha(HERE/'snapshot_FROZEN_FORWARD_CONTRACT.md')
    assert all(sha(DATA/name)==digest for name,digest in freeze['source_hashes'].items())
    assert gates['at'] < score['at']
    assert len(gates['rows']) == len(score['per_galaxy']) == 3
    saved_scores = {row['name']:row for row in score['per_galaxy']}
    saved_gates = {row['name']:row for row in gates['rows']}
    assert set(saved_scores) == set(saved_gates) == set(NAMES)
    reference_hashes = {}
    for filename, provenance in gates['receipts'].items():
        path = FIELD/filename
        receipt = read(path)
        assert sha(path) == provenance['sha256']
        assert receipt['source_sha256'] == provenance['solver_sha256']
        assert receipt['source_sha256'] in KNOWN
        assert receipt['source_npz_sha256'] == freeze['source_hashes']['baryonic_forward_64.npz']
        assert receipt['U'] == .5605122519882025
        assert receipt['a0_SI'] == 7.658058668049826e-11
        assert receipt['source_row'] == metadata[receipt['name']]
        assert receipt['at'] < gates['at']
        reference_hashes[filename] = sha(path)
    control = read(FIELD/'direct_controls_v4.json')
    limits = {'gaussian_midplane':5e-7, 'gaussian_axis':5e-7,
              'vertical_convolution_absolute':5e-7, 'spherical_projection_relative':1e-9,
              'kuzmin_projection_relative':.003, 'gradient_radial_cancellation_normalized':5e-4,
              'nongradient_radial_normalized_error':5e-4,
              'nongradient_tangential_normalized_error':5e-4}
    assert all(math.isfinite(control['checks'][k]) and 0 <= control['checks'][k] < limit
               for k,limit in limits.items())
    assert control['checks']['zero_radial_diagnostic_handling']
    checked = []
    all_residuals = {kind:[] for kind in KINDS}
    with np.load(DATA/'baryonic_forward_64.npz') as forward, np.load(DATA/'sealed_targets.npz') as targets:
        for name in NAMES:
            saved = saved_scores[name]
            final = read(FIELD/f'direct_{name}_boundary_v4.json')
            highest = read(FIELD/f'direct_{name}_ell512_v4.json' if name=='UGC07577'
                           else FIELD/f'direct_{name}_higher_v3.json')
            previous = read(FIELD/f'direct_{name}_higher_v3.json' if name=='UGC07577'
                            else FIELD/f'direct_{name}_high_v3.json')
            newton = read(FIELD/f'direct_{name}_fine_newtonian_v1.json')
            f = final['projection']
            assert final['source_sha256'] == gates['solver_sha256']
            assert not f['metadata']['newtonian']
            assert newton['projection']['metadata']['newtonian']
            expected_mask = ((forward[name+'_R'] > 0) &
                             (forward[name+'_R'] >= .5*metadata[name]['meta']['Rd']))
            assert np.array_equal(expected_mask, forward[name+'_score_mask'])
            radii = forward[name+'_R'][expected_mask].tolist()
            observed = targets[name+'_v'][expected_mask].tolist()
            errors = targets[name+'_error'][expected_mask].tolist()
            assert radii == f['R'] == saved['R_kpc']
            assert observed == saved['observed_km_s']
            assert errors == saved['processed_error_km_s']
            assert all(v > 0 and math.isfinite(v) for v in observed)
            assert metadata[name]['split'] == 'train'
            assert saved['fixed_stellar_U'] == final['U']
            assert saved['fixed_a0_SI'] == final['a0_SI']
            assert all(read(FIELD/filename)['projection']['R']==radii
                       for filename in gates['receipts'] if filename.startswith('direct_'+name+'_'))
            # Reconstruct the Newtonian midplane comparison from actual input arrays,
            # rather than accepting the value reported by the force calculation.
            source_force = ((forward[name+'_gas'][0]+final['U']*forward[name+'_disk'][0])
                            [expected_mask]/np.array(radii)).tolist()
            computed_gates = {
                'newtonian_midplane':(delta(f['newtonian'], source_force),2e-6),
                'newtonian_projection':(delta(newton['projection']['full'], newton['projection']['newtonian']),.003),
                'last_angular_refinement':(delta(highest['projection']['full'], previous['projection']['full']),.005),
                'boundary_hankel_grid_change':(delta(f['full'], highest['projection']['full']),.003)}
            for key,(value,limit) in computed_gates.items():
                assert value <= limit
                close(value,saved_gates[name]['gates'][key][0])
                assert limit == saved_gates[name]['gates'][key][1]
            grid = f['metadata']; old_grid = highest['projection']['metadata']
            close(grid['rmin'], old_grid['rmin']/2)
            close(grid['rmax'], old_grid['rmax']*2)
            assert final['hankel'] == 4096 == 2*highest['hankel']
            assert grid['nr'] == old_grid['nr'] == 1536
            assert grid['nc'] == old_grid['nc'] and grid['lmax'] == old_grid['lmax']
            row = {'name':name, 'n_scored':len(radii), 'gates':computed_gates, 'scores':{}}
            for kind in KINDS:
                assert all(g > 0 and math.isfinite(g) for g in f[kind])
                velocities = [math.sqrt(r*g) for r,g in zip(radii,f[kind])]
                # Independent log identity instead of log of author's velocity ratio.
                residuals = [(.5*(math.log10(r)+math.log10(g))-math.log10(v))
                             for r,g,v in zip(radii,f[kind],observed)]
                mean = math.fsum(residuals)/len(residuals)
                mse = math.fsum(x*x for x in residuals)/len(residuals)
                for actual,reported in zip(velocities,saved['predictions_km_s'][kind]):close(actual,reported)
                for actual,reported in zip(residuals,saved['scores'][kind]['log10_residual']):close(actual,reported)
                close(mean,saved['scores'][kind]['mean_log10_velocity'])
                close(math.sqrt(mse),saved['scores'][kind]['rms_log10_velocity'])
                row['scores'][kind] = {'rms_log10':math.sqrt(mse),'mean_log10':mean}
                all_residuals[kind].append(residuals)
            checked.append(row)
    aggregate = {}
    for kind,galaxies in all_residuals.items():
        # Each observation's weight is 1/(3*n_galaxy), summing to 1.
        variance = math.fsum(x*x/(3*len(rows)) for rows in galaxies for x in rows)
        mean = math.fsum(x/(3*len(rows)) for rows in galaxies for x in rows)
        aggregate[kind] = {'rms_log10':math.sqrt(variance),'mean_log10':mean}
        close(aggregate[kind]['rms_log10'],score['combined'][kind]['galaxy_equal_rms_log10_velocity'])
        close(mean,score['combined'][kind]['galaxy_equal_mean_log10_velocity'])
    result = {'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'script_sha256':sha(Path(__file__)), 'passed':True,
              'source_sha256':score['source_sha256'], 'gates_sha256':sha(FIELD/'DIRECT_NUMERICAL_GATES.json'),
              'score_sha256':sha(FIELD/'DIRECT_FIXED_COMPARISON.json'),
              'targets_sha256':sha(DATA/'sealed_targets.npz'),
              'all_ref_receipt_hashes':reference_hashes,
              'per_galaxy':checked, 'aggregate':aggregate,
              'scope':'Arithmetic, mask, unit, provenance and declared finite gates only; no statistical or universal theory inference'}
    with (OUT/'fixed_score_check.json').open('x') as stream:
        json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps({'passed':True,'aggregate':aggregate,
                      'per_galaxy':checked},indent=2))


if __name__ == '__main__':
    main()
