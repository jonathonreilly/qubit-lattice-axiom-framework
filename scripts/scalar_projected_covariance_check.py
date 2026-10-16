"""Conditional scalar constraints from ideal projected shell correlations."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_PROJECTED_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_projected_geometry.py',
    'scripts/scalar_projected_weak.py',
    'scripts/scalar_projected_forward.py',
    'scripts/scalar_dynamical_forward.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/projected_covariance/FORWARD_PROTOCOL_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/projected_covariance/NO_GO_DISCIPLINE_CHECKLIST.md',
]
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import scalar_projected_geometry as geometry
import scalar_projected_weak as weak
import scalar_projected_forward as forward

ROOT=Path(__file__).resolve().parents[1]


def encode(value):
    if isinstance(value,np.generic): return value.item()
    raise TypeError(type(value).__name__)


def run(protocol):
    geometric=geometry.controls(); weighted=weak.controls()
    cases=[forward.experiment(case,protocol) for case in protocol['backgrounds']]
    groups={'geometry':geometric['checks'],'weak':weighted['checks']}
    for case in cases: groups[case['case']['id']]=case['checks']
    checks=[{**check,'name':group+'.'+check['name']} for group,rows in groups.items() for check in rows]
    return {'actual_current_surface_status':'conditional-support','target_claim_type':'bounded_theorem',
            'scope':'Exact necessary implication under supplied measurement geometry, statistics and field law; synthetic tests only',
            'checks':checks,'geometry':geometric,'weak':weighted,'cases':cases,
            'counts':{'passed':sum(check['passed'] for check in checks),'failed':sum(not check['passed'] for check in checks)},
            'empirical_tests':0}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=ROOT/'outputs/scalar_projected_covariance')
    args=parser.parse_args()
    result=run(json.loads((ROOT/AUDIT_INPUT_PATHS[5]).read_text()))
    result['primary_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['input_sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
    result['read_inventory']={'scientific_inputs':['Fixed synthetic protocol; supplied candidate and operators in declared imported helpers'],
        'integrity_reads':['Source and declared inputs for SHA256; no external observational arrays or ancestral result files loaded']}
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'RESULTS_v1.json').write_text(json.dumps(result,default=encode,sort_keys=True,indent=2,allow_nan=False)+'\n')
    summary={k:result[k] for k in ['actual_current_surface_status','target_claim_type','scope','counts','empirical_tests','primary_sha256','input_sha256','read_inventory']}
    summary['failed_checks']=[r for r in result['checks'] if not r['passed']]
    summary['local_condition_inf']=result['geometry']['synthetic']['condition_inf']
    summary['rolling']=[{'case':c['case']['id'],
        'max_scaled_identity_residual':max(abs(r['identity_scaled']) for e in c['epochs'] for r in e['rows']),
        'max_condition_row_scaled':max(e['condition_row_scaled'] for e in c['epochs']),
        'inverse_errors':[e['inverse_absolute_error'] for e in c['epochs']]} for c in result['cases']]
    (args.output_dir/'SUMMARY_v1.json').write_text(json.dumps(summary,default=encode,sort_keys=True,indent=2,allow_nan=False)+'\n')
    for name,scope in {
        'per_element':'checked: projection signs, operator order, commutator, weak kernels and five coefficient slots',
        'per_site':'checked and not executed: no local environmental solution or measured calibration',
        'per_mode':'checked: five homogeneous scalar spectral shells; full supplied linear scalar/dust evolution',
        'per_block':'checked: two synthetic backgrounds, five epochs and six separation rows; separate local rank diagnostic',
        'lattice_wide':'checked and not executed: no fundamental action, state, scale or empirical validation',
    }.items():print(name+': '+scope)
    print(json.dumps(summary,default=encode,sort_keys=True,indent=2,allow_nan=False))
    return int(result['counts']['failed']!=0)


if __name__=='__main__':raise SystemExit(main())
