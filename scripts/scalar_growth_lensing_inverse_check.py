"""Exact conditional inverse and fixed synthetic background/readout controls."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = [
    'docs/SCALAR_GROWTH_LENSING_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-15.md',
    'scripts/scalar_growth_lensing_inverse.py',
    '.claude/science/physics-loops/observations-backward-24h-20261014/growth_bridge/FORWARD_PROTOCOL_v1.json',
    '.claude/science/physics-loops/observations-backward-24h-20261014/growth_bridge/NO_GO_DISCIPLINE_CHECKLIST.md',
]

import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as sp
import scalar_growth_lensing_inverse as calculation

ROOT=Path(__file__).resolve().parents[1]


def encode(value):
    if isinstance(value,np.generic):return value.item()
    if isinstance(value,sp.Basic):return str(value)
    raise TypeError(type(value).__name__)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',type=Path,default=ROOT/'outputs/scalar_growth_lensing_inverse')
    args=parser.parse_args()
    protocol=json.loads((ROOT/AUDIT_INPUT_PATHS[2]).read_text())
    result=calculation.run(protocol)
    result.update(primary_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS},
                  actual_current_surface_status='conditional-support',
                  read_inventory={'scientific_inputs':['Fixed protocol in AUDIT_INPUT_PATHS; supplied action/response equations implemented explicitly in the imported helper'],
                                  'integrity_reads':['Primary source plus every declared input for SHA256; no raw observations or unmerged scientific source loaded']},
                  original_failures=['Working v1 omitted q>0 software gate; exact reviewer witness and original returns retained.',
                                     'Working forward v1 output serialization failed; partial file preserved and unchanged physics rerun in v2.',
                                     'Initial canonical sampled gate rounded an exact chart boundary and admitted infinite B/C; source and reviewer witnesses preserved.',
                                     'Initial later assessment evaluated a rejected pole; source and witness preserved.',
                                     'Nonfinite later readout could falsely pass via max([0, NaN]); original source/witness retained, finite input and residual gates added.'],
                  numerical_scope='Double-precision synthetic ODE and 60-digit inverse arithmetic on its rounded readouts; no rigorous integration enclosure or observed high-precision digits.')
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'RESULTS_v1.json').write_text(json.dumps(result,default=encode,sort_keys=True,indent=2)+'\n')
    summary={k:v for k,v in result.items() if k not in ['checks','histories']}
    summary['failed_checks']=[c for c in result['checks'] if not c['passed']]
    (args.output_dir/'SUMMARY_v1.json').write_text(json.dumps(summary,default=encode,sort_keys=True,indent=2)+'\n')
    for scope,explanation in {
        'per_element':'checked: exact response equations, chart domains, factors and candidate admission',
        'per_site':'checked and not executed: no lattice site dynamics or local screening field solved',
        'per_mode':'checked: coherent dust modes with exact continuity and supplied light scalar response',
        'per_block':'checked: three synthetic full radial backgrounds with two reduced perturbation modes each',
        'lattice_wide':'checked and not executed: no unconditional framework action, state or empirical scalar conclusion',
    }.items():print(scope+': '+explanation)
    print(json.dumps(summary,default=encode,sort_keys=True,indent=2))
    return int(result['failed']>0)


if __name__=='__main__':
    raise SystemExit(main())
