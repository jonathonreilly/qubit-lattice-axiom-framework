#!/usr/bin/env python3
"""Conditional finite-window scalar history controls.
No external scientific input or ancestor result is read. Package-local integrity
reads hash the paired note, primary and three imported helpers. All output goes
to the requested directory. These are synthetic controls, not empirical fits.
"""
import argparse
import hashlib
import json
from pathlib import Path
import scalar_temporal_history_controls as temporal
import scalar_moving_history_controls as moving
import scalar_force_energy_controls as force

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_FINITE_WINDOW_INITIAL_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_temporal_history_controls.py',
    'scripts/scalar_moving_history_controls.py',
    'scripts/scalar_force_energy_controls.py',
]

def main():
    root=Path(__file__).resolve().parents[1]
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=root/'outputs/scalar_finite_window_history')
    args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    results={'temporal':temporal.run_checks(),'moving':moving.run_checks(),'force_energy':force.run_checks()}
    products={}
    for name,result in results.items():
        dest=args.output_dir/(name+'.json')
        dest.write_text(json.dumps(result,indent=2)+'\n')
        products[name]=hashlib.sha256(dest.read_bytes()).hexdigest()
    sources=[Path(__file__).resolve()]+[root/p for p in AUDIT_INPUT_PATHS]
    summary={
        'actual_current_surface_status':'conditional-support',
        'claim_type':'bounded_theorem',
        'checks':{k:r['checks_passed'] for k,r in results.items()},
        'source_sha256':{str(p.relative_to(root)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'product_sha256':products,
        'measured_gravity_tests':0,'fitted_parameters':0,
        'scope':[
            'Flat stable free-field operator and prescribed regular subluminal paths are premises.',
            'Finite-window bounds use a quantitative scalar energy input; no initial profile is selected.',
            'Conformal test-particle force and constant-frame energy normalization are derived conditionally.',
            'Actual clock/ray/trajectory calibration, nonlinear forcing error and physical energy budget remain open.',
            'Finite control witnesses do not assert theory-wide impossibility or exhaust alternative routes.',
        ],
    }
    (args.output_dir/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    return 0
if __name__=='__main__':raise SystemExit(main())
