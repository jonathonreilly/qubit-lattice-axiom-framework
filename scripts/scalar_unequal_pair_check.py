"""Conditional scalar constraints as finite shear/velocity pair statistics."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_UNEQUAL_PAIR_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_unequal_geometry.py',
    'scripts/scalar_unequal_sampling.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/unequal_window/NO_GO_DISCIPLINE_CHECKLIST.md',
]
import argparse
import hashlib
import json
from pathlib import Path
import scalar_unequal_geometry as geometry
import scalar_unequal_sampling as sampling

ROOT = Path(__file__).resolve().parents[1]


def run():
    results = {'geometry': geometry.controls(), 'sampling': sampling.controls()}
    checks = [{**row, 'name': name+'.'+row['name']}
              for name, result in results.items() for row in result['checks']]
    return {
        'actual_current_surface_status': 'conditional-support',
        'target_claim_type': 'bounded_theorem',
        'scope': 'Necessary scalar constraint and finite-pair ensemble expectation under supplied field, geometry, statistics, sampling and calibration premises',
        'checks': checks,
        'components': results,
        'counts': {'passed': sum(row['passed'] for row in checks),
                   'failed': sum(not row['passed'] for row in checks)},
        'empirical_tests': 0,
        'observational_datasets_opened': 0,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path,
                        default=ROOT/'outputs/scalar_unequal_pair')
    args = parser.parse_args()
    result = run()
    result['primary_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['input_sha256'] = {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                              for p in AUDIT_INPUT_PATHS}
    result['read_inventory'] = {
        'scientific_inputs': ['Explicit symbolic operators and fixed synthetic fixtures in declared helpers'],
        'integrity_reads': ['This source and declared inputs for SHA256; no external observations or inherited output arrays read'],
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/'RESULTS_v1.json').write_text(
        json.dumps(result, sort_keys=True, indent=2, allow_nan=False)+'\n')
    summary = {k: result[k] for k in [
        'actual_current_surface_status', 'target_claim_type', 'scope', 'counts',
        'empirical_tests', 'observational_datasets_opened', 'primary_sha256',
        'input_sha256', 'read_inventory']}
    summary['failed_checks'] = [r for r in result['checks'] if not r['passed']]
    summary['remaining_inputs'] = [
        'Actual field law and calibrated distance/velocity/shear identification',
        'Actual pair selection and conditional mark/noise law',
        'Actual survey masks, distance windows, error and variance bounds',
        'Action, initial state, absolute scales and environmental gravity bridge',
    ]
    (args.output_dir/'SUMMARY_v1.json').write_text(
        json.dumps(summary, sort_keys=True, indent=2, allow_nan=False)+'\n')
    for label, scope in {
        'per_element': 'checked: Cartesian signs, ordered commutator, angular nuisance, weak adjoints and pair normalization',
        'per_site': 'checked and not executed: no physical source/environment solution or survey calibration',
        'per_mode': 'checked: exact radial polynomial controls, positive random-wave covariance, spin ell2..5',
        'per_block': 'checked: unequal-distance chart, full ordered weak composition and finite catalogue enumeration',
        'lattice_wide': 'checked and not executed: no action/state/scale selection, parameter uniqueness or empirical validation',
    }.items():
        print(label+': '+scope)
    print(json.dumps(summary, sort_keys=True, indent=2, allow_nan=False))
    print(f"TOTAL: PASS={result['counts']['passed']} FAIL={result['counts']['failed']}")
    return int(result['counts']['failed'] != 0)


if __name__ == '__main__':
    raise SystemExit(main())
