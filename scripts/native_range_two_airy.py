#!/usr/bin/env python3
"""Growing-cutoff controls of the specified range-two outgoing-host model."""
from pathlib import Path
import sys,json,numpy as np
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_range_two_airy.py','.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_slow_host.py']
sys.path.insert(0,str(ROOT/'.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_range_two_airy import run

def main():
 rows=[]
 for lam in [.2,.1,.05,.02,.01,.005]:
  r=run(lam);s=run(lam,1.2);r['cutoff_coefficient_difference']=float(np.linalg.norm(np.array(r['coefficient'])-s['coefficient']));assert r['cutoff_coefficient_difference']<1e-7 and r['schur_residual']<1e-8 and r['error_over_lambda_two_thirds']<.04;rows.append(r)
 result=dict(status='PASS',rows=rows,scope='Specified slowK4+outgoinghost only. Uniform infinite-arm asymptotic proof is separate; Schur residual is not a certified pole error. No full-H pole or original-source residue theorem.')
 out=ROOT/'outputs/native_range_two_airy/result.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
