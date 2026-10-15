"""Full conditional scalar/dust inverse and equal-time covariance controls."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_DYNAMICAL_MOMENTUM_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_dynamical_forward.py',
    'scripts/scalar_dynamical_geometry.py',
    'scripts/scalar_dynamical_extensions.py',
    'scripts/scalar_dynamical_domains.py',
    'scripts/scalar_dynamical_covariance.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/dynamical_response/FORWARD_PROTOCOL_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/dynamical_response/NO_GO_DISCIPLINE_CHECKLIST.md',
]
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as sp
import scalar_dynamical_forward as forward
import scalar_dynamical_geometry as geometry
import scalar_dynamical_extensions as extensions
import scalar_dynamical_domains as domains
import scalar_dynamical_covariance as covariance

ROOT=Path(__file__).resolve().parents[1]


def encode(obj):
    if isinstance(obj,np.generic):return obj.item()
    if isinstance(obj,sp.Basic):return str(obj)
    raise TypeError(type(obj).__name__)


def run(protocol):
    cases=[forward.experiment(case,protocol) for case in protocol['backgrounds']]
    cov=covariance.controls()
    groups={'forward_symbolic':forward.symbolic_checks(),
            'geometry':geometry.checks(),'extensions':extensions.checks(),
            'background':extensions.background_checks()+[extensions.potential_decoder_check()],'domains':domains.checks(),
            'equal_time_covariance':cov['checks']}
    for c in cases:
        groups[c['case']['id']]=c['checks']
        beta=c['candidate']['beta_inferred'];kap=c['candidate']['kappa_inferred']
        admitted=all(np.isfinite(v) for ep in c['epochs'] for v in ep['inferred'].values())
        admitted=admitted and 0.25<beta<1/3 and kap>0 and all(ep['inferred']['R']>0 and ep['inferred']['y']!=0 and 0<ep['inferred']['q']<beta for ep in c['epochs'])
        groups[c['case']['id']].append({'name':'finite_saved_epoch_domains','passed':bool(admitted)})
        signs=[{'left_index':i,'right_index':i+1,'y_left':a['y_true'],'y_right':b['y_true']}
               for i,(a,b) in enumerate(zip(c['epochs'],c['epochs'][1:])) if a['y_true']*b['y_true']<0]
        c['turning_diagnostic']={'saved_sign_changes':signs,'scope':'Finite sampled signs; no root enclosure or uniform interval identification'}
    checks=[{**c,'name':scope+'.'+c['name']} for scope,rows in groups.items() for c in rows]
    potential=extensions.potential_diagnostics({'cases':cases})
    return {'actual_current_surface_status':'conditional-support',
            'target_claim_type':'bounded_theorem','checks':checks,'cases':cases,
            'covariance_examples':cov,'potential_diagnostics':potential,
            'counts':{'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks)},
            'empirical_tests':0,'scope':'Supplied full linear scalar/dust dynamics, exact conditional inverses and synthetic cases; no measured covariance supplier or action selection'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,default=ROOT/'outputs/scalar_dynamical_momentum_inverse')
    args=parser.parse_args();protocol=json.loads((ROOT/AUDIT_INPUT_PATHS[6]).read_text());result=run(protocol)
    result['primary_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['input_sha256']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
    result['read_inventory']={'scientific_inputs':['Fixed synthetic protocol; explicit supplied action and derived equations in the imported helpers'],
                              'integrity_reads':['Primary source and every declared input for SHA256; no external observations or ancestral result files loaded']}
    result['history_scope']={'working_coefficient_label':'Original positive-chart label exceeded observable-domain scope; narrowed to positive coefficients without changing norm theorem.',
                            'checker_setup_failure':'Independent correspondence v1 BooleanAtom counting failed; repaired v2 preserved same mathematics.',
                            'protocol_name':'reserved_scaled_max applies to absolute dimensionless residuals in the fixed root forward implementation.',
                            'precision':'Double-precision ODE/readout arithmetic; exact rational controls do not certify trajectory or measurement accuracy.'}
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'RESULTS_v1.json').write_text(json.dumps(result,default=encode,sort_keys=True,indent=2,allow_nan=False)+'\n')
    summary={k:result[k] for k in ['actual_current_surface_status','target_claim_type','scope','counts','empirical_tests','primary_sha256','input_sha256','read_inventory','history_scope']}
    summary['failed_checks']=[r for r in result['checks'] if not r['passed']]
    summary['cases']=[{k:c[k] for k in ['case','candidate','constraint_max','maximum_abs_r_minus_q','turning_diagnostic']} for c in result['cases']]
    summary['potential_diagnostics']=[{k:v for k,v in p.items() if k!='epoch_rows'} for p in result['potential_diagnostics']]
    (args.output_dir/'SUMMARY_v1.json').write_text(json.dumps(summary,default=encode,sort_keys=True,indent=2,allow_nan=False)+'\n')
    for name,scope in {
      'per_element':'checked: exact metric, constraint, covariance, rank and coefficient-error equations',
      'per_site':'checked and not executed: no lattice site or local environmental field solution',
      'per_mode':'checked: full rolling linear coupled scalar/dust modes with arbitrary supplied scalar initial data',
      'per_block':'checked: two synthetic backgrounds, four modes, seven epochs each; six separate covariance examples',
      'lattice_wide':'checked and not executed: no fundamental action, state, scale or empirical theory validation',
    }.items():print(name+': '+scope)
    print(json.dumps(summary,default=encode,sort_keys=True,indent=2,allow_nan=False));return int(result['counts']['failed']!=0)


if __name__=='__main__':raise SystemExit(main())
