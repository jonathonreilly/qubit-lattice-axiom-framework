"""Conditional nonlinear radial vacuum inverse from a physical metric."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_VACUUM_METRIC_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_vacuum_metric_inverse.py',
    'scripts/scalar_vacuum_metric_weak.py',
    'docs/SCALAR_PHYSICAL_CURVATURE_ENVIRONMENT_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'docs/EXPONENTIAL_SCALAR_ACTION_SCALE_BOUNDED_THEOREM_NOTE_2026-10-14.md',
    '.claude/science/physics-loops/observations-backward-24h-20261014/material_metric_consistency/NO_GO_DISCIPLINE_CHECKLIST.md',
]
import argparse
import hashlib
import json
from pathlib import Path
import scalar_vacuum_metric_inverse as inverse
import scalar_vacuum_metric_weak as weak

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=ROOT/'outputs/scalar_vacuum_metric')
    args=parser.parse_args()
    result=inverse.controls()
    result['weak_moment_checks']=weak.controls()
    result['checks']+=result['weak_moment_checks']['checks']
    result.update({
        'actual_current_surface_status':'conditional-support',
        'target_claim_type':'bounded_theorem',
        'scope':'Nondegenerate static spherical material vacuum, supplied candidate action and consistent x=y=0 sector; exact metric-to-field/parameter inverse with full-domain consistency checks',
        'counts':{'passed':sum(c['passed'] for c in result['checks']),
                  'failed':sum(not c['passed'] for c in result['checks'])},
        'primary_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
        'read_inventory':{'scientific_inputs':'Symbolic action/metric and three fixed synthetic coupled local solutions in the declared helper; inverse routine receives metric jets only',
                          'integrity_inputs':'Primary and declared notes/helper/checklist only; no observed arrays, inherited result values or independent-review outputs loaded'},
        'remaining_inputs':['Pointwise route: calibrated metric through lapse third and B second derivatives with error envelopes',
                            'Weak alternative uses lapse second/B first derivatives and complete weighted profiles with calibrated errors',
                            'Justified vacuum, static spherical geometry, and single-scalar sector',
                            'Action selection, physical preparation/global history, and measured Newton/action normalization'],
    })
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'RESULTS_v1.json').write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+'\n')
    summary={k:v for k,v in result.items() if k not in ['checks','synthetic_fixtures','weak_moment_checks']}
    summary['failed_checks']=[c for c in result['checks'] if not c['passed']]
    (args.output_dir/'SUMMARY_v1.json').write_text(json.dumps(summary,indent=2,sort_keys=True,allow_nan=False)+'\n')
    for k,v in {
        'per_element':'checked: original Ricci/Hessian, null differences, Bianchi identity and inverse formulas',
        'per_site':'checked: three synthetic local vacuum profiles; no observed metric or empirical bound',
        'per_mode':'checked: x=y=0 is supplied consistent sector, not selected; other scalar motion remains open',
        'per_block':'checked: local inverse, integral consistency, potential discrimination and stated degeneracies',
        'lattice_wide':'checked and not executed: no full theory, global solution, history or absolute action normalization derivation',
    }.items():print(k+': '+v)
    print(json.dumps(summary,indent=2,sort_keys=True,allow_nan=False))
    print(f"TOTAL: PASS={result['counts']['passed']} FAIL={result['counts']['failed']}")
    return int(result['counts']['failed']!=0)


if __name__=='__main__':raise SystemExit(main())
