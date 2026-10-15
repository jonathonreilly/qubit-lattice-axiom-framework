#!/usr/bin/env python3
"""Conditional proper-count -> accelerated joint scalar energy construction.

No external scientific inputs or observations are read. Package-local integrity
reads hash this runner, its five source helpers, and its paired proof note.
All result products are written below the requested output directory.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_ACCELERATED_COHERENT_COUNT_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_accelerated_gram_controls.py',
    'scripts/scalar_proper_count_controls.py',
    'scripts/scalar_count_adjoint_controls.py',
    'scripts/scalar_coherent_count_controls.py',
    'scripts/scalar_coherent_exact_energy_controls.py',
]

import argparse
import hashlib
import json
from pathlib import Path
import scalar_accelerated_gram_controls as gram
import scalar_proper_count_controls as endpoint
import scalar_count_adjoint_controls as adjoint
import scalar_coherent_count_controls as coherent
import scalar_coherent_exact_energy_controls as exact


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=root/'outputs/scalar_accelerated_coherent_count')
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = {'joint_gram':gram.run_checks(), 'proper_endpoint':endpoint.run_checks(),
               'one_way_adjoint':adjoint.run_checks(), 'coherent_adjoint':coherent.run_checks(),
               'exact_coherent_energy':exact.run_checks()}
    products = {}
    for key, value in results.items():
        path = args.output_dir/(key+'.json')
        path.write_text(json.dumps(value, indent=2)+'\n')
        products[key] = hashlib.sha256(path.read_bytes()).hexdigest()
    sources = [Path(__file__).resolve()]+[root/p for p in AUDIT_INPUT_PATHS]
    summary = {
        'actual_current_surface_status':'conditional-support', 'claim_type':'bounded_theorem',
        'checks':{key:value['checks_passed'] for key, value in results.items()},
        'checks_passed':sum(value['checks_passed'] for value in results.values()),
        'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'product_sha256':products,
        'external_scientific_inputs_read':[], 'observational_tests':0, 'fitted_parameters':0,
        'physical_energy_estimates':0,
        'scope':[
            'A supplied conformal free massless field and proper-clock/link model remain conditional.',
            'Actual endpoint counts derive joint clock and force weights through the trajectory adjoint.',
            'Exact contrast conditions remove initial orbit/clock, declared nuisance and constant-offset response.',
            'The accelerated norm retains acceleration and common-arrival cross-path terms.',
            'Ideal coherent transfer removes the spacecraft direct clock channel, retaining its force response.',
            'The stationary exact composition fixture has rational moments and exact Gram entries.',
            'Other quadrature, perturbation and rank experiments are finite numerical diagnostics.',
            'No actual orbit calibration, scalar residual, field energy upper budget, nonlinear error bound or positive-mass accelerated extension is supplied.',
        ],
    }
    (args.output_dir/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
