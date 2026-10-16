#!/usr/bin/env python3
"""Synthetic checks for conditional phase elimination from coherent counts.

No external scientific data or ancestral theorem output is read. Package-local
integrity reads hash this runner, its three imported helpers and its paired note.
The finite-dimensional fixtures are illustrative constructions, not Cassini fits.
All writes go to the requested output directory (outputs/ by default).
"""
import argparse
import hashlib
import json
from pathlib import Path

import coherent_count_plasma_controls as plasma
import coherent_count_initial_phase_controls as initial
import coherent_count_chirp_controls as chirp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/COHERENT_RADIO_COUNT_INITIAL_PHASE_ELIMINATION_BOUNDED_THEOREM_NOTE_2026-10-14.md',
    'scripts/coherent_count_plasma_controls.py',
    'scripts/coherent_count_initial_phase_controls.py',
    'scripts/coherent_count_chirp_controls.py',
]


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path,
                        default=root/'outputs/coherent_radio_initial_phase')
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    results = {
        'plasma_finite_count': plasma.run_checks(),
        'initial_phase_contrasts': initial.controls(),
        'two_uplink_chirps': chirp.run(),
    }
    products = {}
    for name, result in results.items():
        assert result['total_fail'] == 0, name
        path = args.output_dir/(name+'.json')
        path.write_text(json.dumps(result, indent=2)+'\n')
        products[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    sources = [Path(__file__).resolve()]+[root/path for path in AUDIT_INPUT_PATHS]
    summary = {
        'actual_current_surface_status': 'conditional-support',
        'claim_type': 'bounded_theorem',
        'role': 'conditional observation-operator derivation and synthetic controls',
        'source_sha256': {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in sources},
        'product_sha256': products,
        'checks': {name: {'passed': r['total_pass'], 'failed': r['total_fail']}
                   for name, r in results.items()},
        'chirp_initial_phase_rank': results['two_uplink_chirps']['synthetic_model']['phase_initial_row_rank'],
        'measured_gravity_tests': 0,
        'fitted_parameters': 0,
        'scope': [
            'Known invertible fixed-unit endpoint operators are premises.',
            'The chirped physical class assumes common retarded maps and frequency-separable rays.',
            'Initial receiver phase is eliminated for stated contrasts; no scalar initial field state is derived.',
            'Standard plasma cancellation and null-space projection are reconstructed tools, not novelty claims.',
            'No archive value, empirical covariance, real error bound or independent validation enters these controls.',
        ],
    }
    (args.output_dir/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
