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
"""Finite controls of a general arm lemma, not a native coefficient fit."""
from pathlib import Path
import sys, json
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_general_band_control import green

def main():
    rows = []
    for lam in [0.2, 0.1, 0.05]:
        g, N = green(lam)
        h, _ = green(lam, 1.1)
        err = float(np.max(abs(g - h)))
        _check('P9750:native_finite_range_arm:C001', err < 1e-08 and g[0, 0].imag > 0.3 and (np.max(abs(g)) < 2))
        rows.append(dict(lam=lam, N=N, cutoff_error=err, endpoint_imag=float(g[0, 0].imag), max_entry=float(np.max(abs(g)))))
    N = 40
    T = np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)
    P = -2 * T - 0.03 * T @ T + 0.004 * T @ T @ T
    A = np.diag(np.full(N, -0.06)) + np.diag(np.full(N - 1, -1.988), 1) + np.diag(np.full(N - 1, -1.988), -1) + np.diag(np.full(N - 2, -0.03), 2) + np.diag(np.full(N - 2, -0.03), -2) + np.diag(np.full(N - 3, 0.004), 3) + np.diag(np.full(N - 3, 0.004), -3)
    _check('P9750:native_finite_range_arm:C002', np.max(abs((A - P)[3:-3])) < 1e-14)
    result = dict(status='PASS', controls=rows, scope='Chosen cubic correction is a mathematical test, not a native coefficient. Uniform strip and native structural statements are analytical; no full microscopic pole.')
    out = ROOT / 'outputs/native_finite_range_arm/result.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
