#!/usr/bin/env python3
"""Score all six preselected extension fields only after their numerical gates."""
import datetime as dt
import json
from pathlib import Path

import numpy as np

from direct_fixed_comparison import DATA, OUT, SOURCE, guard, read, relative_change, sha


def main():
    guard()
    output = OUT / 'DIRECT_EXPANSION_COMPARISON.json'
    assert not output.exists(), 'Preserve every scientific execution receipt'
    source_hash = sha(__file__)
    frozen = read('contract_and_subset_freeze.json')
    assert sha(Path(__file__).with_name('direct_qumond_disk.py')) == SOURCE
    assert sha(Path(__file__).with_name('FROZEN_FORWARD_CONTRACT.md')) == frozen['contract_sha256']
    for name, digest in frozen['source_hashes'].items():
        assert sha(DATA / name) == digest
    gates = read('DIRECT_EXPANSION_GATES.json')
    assert gates['passed'] and gates['solver_sha256'] == SOURCE
    assert [row['name'] for row in gates['rows']] == frozen['conditional_expansion']
    previous_roles = {row['name']: row['split'] for group in frozen['bins'] for row in group['ordered']}
    receipts, finals = {}, {}
    for row in gates['rows']:
        name, ell = row['name'], row['converged_modes']
        tags = ['newtonian', f'ell{ell // 2}', f'ell{ell}', 'boundary']
        values = {}
        for tag in tags:
            filename = f'expanded_{name}_{tag}_v4.json'
            values[tag] = read(filename)
            receipts[filename] = sha(OUT / filename)
            assert values[tag]['source_sha256'] == SOURCE
            assert values[tag]['source_npz_sha256'] == frozen['source_hashes']['baryonic_forward_64.npz']
        final = values['boundary']
        for value in values.values():
            assert value['U'] == final['U'] and value['a0_SI'] == final['a0_SI']
            assert value['projection']['R'] == final['projection']['R']
        assert relative_change(values['newtonian']['projection']['full'], values['newtonian']['projection']['newtonian']) <= .003
        assert relative_change(values[f'ell{ell}']['projection']['full'], values[f'ell{ell // 2}']['projection']['full']) <= .005
        assert relative_change(final['projection']['full'], values[f'ell{ell}']['projection']['full']) <= .003
        assert final['newtonian_midplane_relative_error'] <= 2e-6
        finals[name] = final
    # Opening the six targets follows the completed field checks. They are
    # outside the upcoming three-object inverse fit, but were exposed earlier.
    rows = []
    kinds = ['newtonian', 'algebraic', 'local_norm', 'full']
    with np.load(DATA / 'baryonic_forward_64.npz') as raw, np.load(DATA / 'sealed_targets.npz') as target:
        for name in frozen['conditional_expansion']:
            final = finals[name]
            field = final['projection']
            radius = np.asarray(field['R'])
            mask = raw[name + '_score_mask']
            assert np.array_equal(radius, raw[name + '_R'][mask])
            observed = target[name + '_v'][mask]
            error = target[name + '_error'][mask]
            assert np.all(np.isfinite(observed) & (observed > 0))
            predictions, scores = {}, {}
            for kind in kinds:
                force = np.asarray(field[kind])
                assert np.all(np.isfinite(force) & (force > 0)), 'Record a nonpositive force as a model failure'
                velocity = np.sqrt(radius * force)
                residual = np.log10(velocity / observed)
                predictions[kind] = velocity.tolist()
                scores[kind] = {'rms_log10_velocity': float(np.sqrt(np.mean(residual ** 2))),
                                'mean_log10_velocity': float(np.mean(residual)),
                                'log10_residual': residual.tolist()}
            rows.append({'name': name, 'earlier_algebraic_split': previous_roles[name],
                         'data_role': 'previously exposed; outside three-source inverse fit',
                         'R_kpc': radius.tolist(), 'observed_km_s': observed.tolist(),
                         'processed_error_km_s': error.tolist(), 'predictions_km_s': predictions,
                         'scores': scores, 'fixed_stellar_U': final['U'], 'fixed_a0_SI': final['a0_SI']})
    original = read('DIRECT_FIXED_COMPARISON.json')
    assert original['targets_sha256'] == sha(DATA / 'sealed_targets.npz')
    groups = {'six_extension': rows, 'all_nine': original['per_galaxy'] + rows}
    combined = {label: {kind: float(np.sqrt(np.mean([
        row['scores'][kind]['rms_log10_velocity'] ** 2 for row in group]))) for kind in kinds}
        for label, group in groups.items()}
    assert sha(__file__) == source_hash
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'source_sha256': source_hash,
              'solver_sha256': SOURCE, 'gate_sha256': sha(OUT / 'DIRECT_EXPANSION_GATES.json'),
              'targets_sha256': sha(DATA / 'sealed_targets.npz'),
              'original_comparison_sha256': sha(OUT / 'DIRECT_FIXED_COMPARISON.json'),
              'field_receipts': receipts, 'combined_equal_galaxy_rms_log10_velocity': combined,
              'per_galaxy': rows,
              'limits': 'No parameter refit. Subset selected by source geometry and gas bins before PDE results. Exposed development data, not blind validation or a full-sample ranking. Processed error bars are not an independent likelihood. Circular-speed identification, pressure support, baryons and geometry remain conditional; see DIRECT_KINEMATIC_READOUT_FINDING.md.'}
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'combined': combined, 'per_galaxy': [
        {'name': row['name'], 'rms': {k: row['scores'][k]['rms_log10_velocity'] for k in kinds}} for row in rows]}, indent=2))


if __name__ == '__main__':
    main()
