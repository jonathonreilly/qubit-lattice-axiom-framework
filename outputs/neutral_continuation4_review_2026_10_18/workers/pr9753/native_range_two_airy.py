import sys as _sys
if _sys.flags.optimize: raise RuntimeError("Optimized Python disables scientific helper assertions")
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
_groups=set(); _calls=0
def _check(label, condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  print(f'TOTAL: PASS={len(_groups)} FAIL=1',flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)
"""Growing-cutoff controls of the specified range-two outgoing-host model."""
from pathlib import Path
import sys, json, numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_range_two_airy import run

def main():
    rows = []
    for lam in [0.2, 0.1, 0.05, 0.02, 0.01, 0.005]:
        r = run(lam)
        s = run(lam, 1.2)
        r['cutoff_coefficient_difference'] = float(np.linalg.norm(np.array(r['coefficient']) - s['coefficient']))
        _check('P9753:native_range_two_airy:C001', r['cutoff_coefficient_difference'] < 1e-07 and r['schur_residual'] < 1e-08 and (r['error_over_lambda_two_thirds'] < 0.04))
        rows.append(r)
    result = dict(status='PASS', rows=rows, scope='Specified slowK4+outgoinghost only. Uniform infinite-arm asymptotic proof is separate; Schur residual is not a certified pole error. No full-H pole or original-source residue theorem.')
    out = ROOT / 'outputs/native_range_two_airy/result.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
