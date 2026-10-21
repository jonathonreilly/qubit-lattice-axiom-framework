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
from pathlib import Path
import sys, json, numpy as np
ROOT = Path(__file__).resolve().parents[1]
NATIVE = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0, str(NATIVE))
from neutral_com_model import run, residue
rows = []
for p in [0, 0.3, 0.6]:
    for lam in [0.1, 0.03, 0.01, 0.003]:
        r = run(p, lam)
        s = run(p, lam, 1.2)
        r['cutoff_difference'] = float(np.linalg.norm(np.array(r['coefficient']) - s['coefficient']))
        _check('P9764:native_com_propagation:C001', r['cutoff_difference'] < 1e-07 and r['residual'] < 1e-08 and (r['predicted_width'] > 0))
        r['source_residue'] = residue(r)
        rows.append(r)
    _check('P9764:native_com_propagation:C002', rows[-1]['error'] < 0.0002 and rows[-1]['source_residue']['error'] < 1e-05)
raw = json.loads((NATIVE / 'neutral_bulk_second_other.json').read_text())
matches = [x for x in raw if (x['ell'], x['rx'], x['ry']) == (4, 2, 0)]
_check('P9764:native_com_propagation:C003', len(matches) == 1)
r = matches[0]
expected = [([[0, 0, z], [2, 0, z]], c) for z, c in [(list(range(4)), '-4'), (list(range(-1, 4)), '-1/2'), (list(range(1, 4)), '-1/2'), (list(range(3)), '-1/2'), (list(range(5)), '-1/2')]]
_check('P9764:native_com_propagation:C004', len(r['rows']) == 5)
_check('P9764:native_com_propagation:C005', sorted(((json.dumps(x['sites']), x['coefficient']) for x in r['rows'])) == sorted(((json.dumps(s), c) for s, c in expected)))
result = dict(status='bounded-support', rows=rows, scope='Native endpoint coefficient check plus specified NN Airy/outgoing-host model, not full native mass or microscopic pole')
out = ROOT / 'outputs/native_com_propagation/result.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
