#!/usr/bin/env python3
"""Recheck descriptive rectangles with the actual validated candidate fields."""
import argparse
import datetime as dt
import json
from pathlib import Path

import numpy as np

import direct_shared_response_fit as fit


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fits', type=Path, required=True)
    parser.add_argument('--validation', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    fit.operator.guard()
    assert not args.output.exists()
    source = fit.operator.field.sha(__file__)
    fits = json.loads(args.fits.read_text())
    validation = json.loads(args.validation.read_text())
    assert validation['fits_sha256'] == fit.operator.field.sha(args.fits)
    assert fits['protocol_sha256'] == fit.operator.PROTOCOL_HASH
    training = {row['name']: row for row in fit.training_rows()}
    cases = []
    for case in fits['cases']:
        label = case['family'] + '_' + case['constraints']
        candidate = case['best_sampled']
        if candidate is None or candidate['status'] != 0:
            cases.append({'label': label, 'candidate_available': False})
            continue
        rows = []
        for group in validation['rows']:
            name = group['name']
            data = training[name]
            assert np.array_equal(data['R'], group['R_kpc'])
            fields = group['candidate_results'][label]
            kinds = ['base_direct_force', 'refined_direct_force', 'extended_boundary_force', 'matrix_force']
            scores = {}
            for kind in kinds:
                force = np.array(fields[kind])
                assert force.shape == data['A'].shape and np.all(np.isfinite(force))
                needed = np.maximum.reduce([np.zeros_like(force), (force-data['high'])/data['A'],
                                            (data['low']-force)/data['A']])
                positive = bool(np.all(force > 0))
                residual = .5*np.log10(force/data['A']) if positive else None
                index = int(np.argmax(needed))
                scores[kind] = {'required_rectangle_t': float(needed.max()),
                                'largest_violation_radius_kpc': float(data['R'][index]),
                                'rms_log10_velocity': None if not positive else float(np.sqrt(np.mean(residual**2))),
                                'required_t_by_row': needed.tolist()}
            rows.append({'name': name, 'numerical_field_pass': fields['passed'], 'scores': scores})
        methods = ['base_direct_force', 'refined_direct_force', 'extended_boundary_force', 'matrix_force']
        required = {kind: max(row['scores'][kind]['required_rectangle_t'] for row in rows) for kind in methods}
        aggregate = {kind: None if any(row['scores'][kind]['rms_log10_velocity'] is None for row in rows)
                     else float(np.sqrt(np.mean([row['scores'][kind]['rms_log10_velocity']**2 for row in rows]))) for kind in methods}
        cases.append({'label': label, 'candidate_available': True,
                      'numerical_field_pass': validation['candidate_passes'][label],
                      'lp_primary_t': candidate['primary_minimum_t'], 'lp_secondary_t': candidate['fitted_t'],
                      'required_t_by_force_method': required,
                      'largest_direct_required_t': max(required[k] for k in methods if k != 'matrix_force'),
                      'equal_galaxy_rms_log10_velocity': aggregate, 'per_galaxy': rows,
                      'fitted_external_physical_SI': candidate['predicted_external_physical_SI'],
                      'fitted_Q2_s_minus2': candidate['Q2_s_minus2']})
    assert fit.operator.field.sha(__file__) == source
    result = {'at': dt.datetime.now(dt.timezone.utc).isoformat(), 'source_sha256': source,
              'fits_sha256': fit.operator.field.sha(args.fits),
              'validation_sha256': fit.operator.field.sha(args.validation), 'cases': cases,
              'limits': 'Actual direct fields are rechecked against the same descriptive rectangles. Positive direct t must not be rounded into exact rectangle compatibility. Finite numerical convergence is not interval-certified existence. These three galaxies, solar and external constraints are fitting inputs; no independent prediction or significance is claimed.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'cases': [{k:v for k,v in row.items() if k != 'per_galaxy'} for row in cases]}, indent=2))


if __name__ == '__main__':
    main()
