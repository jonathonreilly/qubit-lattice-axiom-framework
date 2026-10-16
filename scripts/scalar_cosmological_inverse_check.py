"""Conditional action membership from ideal cosmological histories.

Offline exact algebra and fixed synthetic controls. No observation is fitted.
"""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_COSMOLOGICAL_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_cosmological_inverse.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/action_selection/SYNTHETIC_PROTOCOL_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/action_selection/NO_GO_DISCIPLINE_CHECKLIST.md',
]

import argparse
import hashlib
import json
from pathlib import Path
import scalar_cosmological_inverse as calculation

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path,
                        default=ROOT/'outputs/scalar_cosmological_inverse')
    args = parser.parse_args()
    protocol_path = ROOT/AUDIT_INPUT_PATHS[2]
    protocol = json.loads(protocol_path.read_text())
    result = calculation.run(protocol)
    result.update(
        actual_current_surface_status='conditional-support',
        primary_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        input_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
                      for p in AUDIT_INPUT_PATHS},
        observed_action_selected=False,
        initial_state_principle_derived=False,
        absolute_gravity_calibrated=False,
        uncertainty_scope='Synthetic readouts assembled at50 digits from a double-precision ODE. No high-precision trajectory, measured derivative accuracy or rigorous numerical enclosure is claimed.',
        original_failure='Working v1 case9 nu recovery failed5e-7 threshold. Original91 controls (90 pass,1 fail) and all inputs retained. Precision reassembly is a separate diagnostic; thresholds and cases unchanged.')
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'RESULTS_v1.json').write_text(
        json.dumps(result,default=calculation.decimal_json,indent=2,sort_keys=True)+'\n')
    for scope,text in {
        'per_element':'checked: physical metric input combinations and candidate inverse domains',
        'per_site':'checked and not executed: no spatial lattice or local screening solution inferred',
        'per_mode':'checked: conditional tensor endpoint transport; transverse equations in the supplied action',
        'per_block':'checked: fixed12 synthetic histories; algebraic input precision and original failed recovery distinguished',
        'lattice_wide':'checked and not executed: no action selection from actual observations or realized-state principle',
    }.items():
        print(scope+': '+text)
    summary={k:v for k,v in result.items() if k not in ['histories','checks']}
    summary['failed_checks']=[c for c in result['checks'] if not c['passed']]
    (args.output_dir/'SUMMARY_v1.json').write_text(
        json.dumps(summary,default=calculation.decimal_json,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,default=calculation.decimal_json,indent=2))
    if result['failed']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
