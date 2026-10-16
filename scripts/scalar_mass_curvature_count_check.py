#!/usr/bin/env python3
"""Conditional mass/curvature bridge from a stated proper-count observation.

Only package-local source integrity is read. No observations or external
scientific files are read. Products stay below the requested output directory.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_MASS_CURVATURE_COUNT_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_massive_response_controls.py',
    'scripts/scalar_massive_refinement_controls.py',
    'scripts/scalar_curved_count_controls.py',
]

import argparse
import hashlib
import json
from pathlib import Path
import scalar_massive_response_controls as massive
import scalar_massive_refinement_controls as refined
import scalar_curved_count_controls as curved


def main():
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=root/'outputs/scalar_mass_curvature_count')
    args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    results={'massive_response':massive.run_checks(),
             'mass_refinement':refined.run_checks(),
             'curved_count':curved.run_checks()}
    products={}
    for name,value in results.items():
        path=args.output_dir/(name+'.json')
        path.write_text(json.dumps(value,indent=2)+'\n')
        products[name]=hashlib.sha256(path.read_bytes()).hexdigest()
    inputs=[Path(__file__).resolve()]+[root/name for name in AUDIT_INPUT_PATHS]
    summary={
        'actual_current_surface_status':'conditional-support',
        'claim_type':'bounded_theorem',
        'checks':{key:value['checks_passed'] for key,value in results.items()},
        'checks_passed':sum(value['checks_passed'] for value in results.values()),
        'source_sha256':{str(path.relative_to(root)):hashlib.sha256(path.read_bytes()).hexdigest() for path in inputs},
        'product_sha256':products,'external_scientific_inputs_read':[],
        'observational_tests':0,'fitted_parameters':0,'physical_energy_estimates':0,
        'scope':[
            'Mass comparison uses a common energy-amplitude isometry, not identical Cauchy data.',
            'The variable-potential comparison preserves the same chi initial data.',
            'An exact count contrast removes stated initial orbit/clock and constant-response columns.',
            'Mass and curved propagation errors compose with the same curved-reference observation weights.',
            'Physical energy conversion applies on the declared initial slice only.',
            'No physical action, state, scale, measured residual, error or energy upper budget is derived.',
            'Finite Fourier/ODE/quadrature probes are diagnostics; analytic suppliers carry the operator bounds.',
            'No formal audit status, integrated landing result or independent empirical confirmation is asserted.',
        ],
    }
    (args.output_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
