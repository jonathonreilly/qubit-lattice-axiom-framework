"""Necessary full-three-field metric compatibility for a supplied scalar action."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_FULL_FIELD_METRIC_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_full_field_metric.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/full_field_metric/PROTOCOL_v1.json',
    'docs/SCALAR_PHYSICAL_CURVATURE_ENVIRONMENT_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'docs/SCALAR_VACUUM_METRIC_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md',
]
import argparse
import hashlib
import json
from pathlib import Path
import scalar_full_field_metric as full

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=ROOT/'outputs/scalar_full_field_metric')
    args = parser.parse_args()
    result = full.controls(ROOT/AUDIT_INPUT_PATHS[2])
    result.update({
        'actual_current_surface_status': 'conditional-support',
        'target_claim_type': 'bounded_theorem',
        'counts': {'passed': sum(c['passed'] for c in result['checks']),
                   'failed': sum(not c['passed'] for c in result['checks'])},
        'primary_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
        'read_inventory': {'scientific_inputs': 'Declared two-case synthetic protocol and helper functions; no observed data or independent reviewer outputs',
                           'integrity_inputs': 'Primary source and declared note/helper/protocol/premise sources'},
        'remaining_inputs': ['Candidate action and k,Hv,nu,C', 'Calibrated metric through N third and B second derivatives',
                             'Static radial material vacuum', 'Smooth roots, derivative kinetic compatibility and both transverse equations',
                             'Global state/preparation, physical normalization and stability'],
    })
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/'RESULTS_v1.json').write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+'\n')
    summary = {k: v for k, v in result.items() if k not in ['checks', 'cases']}
    summary['failed_checks'] = [c for c in result['checks'] if not c['passed']]
    (args.output_dir/'SUMMARY_v1.json').write_text(json.dumps(summary, indent=2, sort_keys=True, allow_nan=False)+'\n')
    for label, value in {
        'per_element': 'checked: complete original Jordan equations and necessary envelope',
        'per_site': 'checked: two synthetic local full-field ODE jets; no observed metric',
        'per_mode': 'checked: x and y both active; no selected sector or state',
        'per_block': 'checked: conditional squared-amplitude reconstruction; not sufficient solution membership',
        'lattice_wide': 'not executed: no full theory, global history or measured normalization derivation',
    }.items():
        print(label+': '+value)
    print(json.dumps(summary, indent=2, sort_keys=True, allow_nan=False))
    print(f"TOTAL: PASS={result['counts']['passed']} FAIL={result['counts']['failed']}")
    return int(result['counts']['failed'] != 0)


if __name__ == '__main__':
    raise SystemExit(main())
