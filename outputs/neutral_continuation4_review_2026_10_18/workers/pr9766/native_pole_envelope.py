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
from fractions import Fraction as F
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0, str(P))
from neutral_envelope_model import run
raw = json.loads((P / 'neutral_slow_fourth_kernel.json').read_text())
_check('P9766:native_pole_envelope:C001', len(raw) == 8 and sorted(((r['ell'], tuple(r['target'])) for r in raw)) == sorted(((ell, t) for ell in [5, 6] for t in [(0, ell + 1), (0, ell + 2), (1, ell + 1), (-1, ell + 1)])))
for r in raw:
    ell = r['ell']
    lo, hi = r['target']
    pred = F(19, 64) if (lo, hi) == (0, ell + 1) else F(-13, 256) if (lo, hi) == (0, ell + 2) else F(0)
    _check('P9766:native_pole_envelope:C002', F(r['coefficient']) == pred)
_check('P9766:native_pole_envelope:C003', F(29, 192) + F(19, 16) - F(13, 64) == F(109, 96))
rows = []
for lam in [0.1, 0.05, 0.03, 0.02, 0.01]:
    r = run(lam)
    s = run(lam, 131072)
    _check('P9766:native_pole_envelope:C004', (r['N'], s['N']) == (65536, 131072))
    _check('P9766:native_pole_envelope:C005', [a['k'] for a in r['tests']] == [0, 1, 3, 8] and [a['k'] for a in s['tests']] == [0, 1, 3, 8])
    _check('P9766:native_pole_envelope:C006', all((len(a['actual']) == 2 for a in r['tests'] + s['tests'])))
    r['grid_difference'] = float(max((np.linalg.norm(np.array(a['actual']) - b['actual']) for a, b in zip(r['tests'], s['tests']))))
    _check('P9766:native_pole_envelope:C007', r['grid_difference'] < 1e-10 and r['edge_mass'] < 1e-12)
    rows.append(r)
_check('P9766:native_pole_envelope:C008', max((x['error'] for x in rows[-1]['tests'])) < 1e-06)
result = dict(status='bounded-support', rows=rows, scope='Native coefficient checks plus approximate pole-kernel FFT controls and artificial rapid-phase stress test; not full microscopic signal or particle probability')
p = ROOT / 'outputs/native_pole_envelope/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
