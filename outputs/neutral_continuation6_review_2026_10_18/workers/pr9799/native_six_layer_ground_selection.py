import sys as _sys
if _sys.flags.optimize: raise RuntimeError('Optimized Python disables scientific helper assertions')
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
from neutral_continuation6_child_io_2026_10_18 import run_tee
_groups=set();_calls=0
def _check(label,condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)

def _run_child(args, **kwargs):
 result=run_tee(args, **kwargs)
 _check('child:'+str(args[1:]), result.returncode==0)
 return result
from pathlib import Path
from fractions import Fraction as F
from math import comb
import json
ROOT = Path(__file__).resolve().parents[1]
rows = []
for n in range(4, 13):
    full = (1 << n) - 1
    dp = [F(0)] * (full + 1)
    dp[0] = F(1)
    for mask in range(1, full + 1):
        total = sum((dp[mask ^ 1 << i] for i in range(n) if mask >> i & 1), F(0))
        c = sum((bool(mask >> i & 1) and (not bool(mask >> (i - 1) % n & 1)) for i in range(n)))
        dp[mask] = total if mask == full else total / c
    _check('P9799:C001', dp[full] == comb(2 * n - 2, n - 1))
    R = 2 * n
    t = 2 * dp[full] * F(63, 8192) ** n / F(3, 8) ** (n - 1)
    rows.append(dict(R=R, ordering_sum=str(dp[full]), t_R=str(t), leading_power=R + 4))
flat = []
for R in [4, 6, 8]:
    weights = []
    for a in range(1 << R):
        for b in range(1 << R - 1):
            k = a.bit_count()
            l = b.bit_count()
            w = R * (k + l) - 2 * k * l
            if w:
                weights.append(w)
    _check('P9799:C002', min(weights) == R and weights.count(R) == 2 * R)
    flat.append(dict(R=R, min_nonzero_weight=min(weights), minimizers=weights.count(R)))
for r in range(1, 8):
    for extra in range(12):
        total = 2 * r + 2 * extra
        _check('P9799:C003', 3 * total - 4 * (r - 1) == total + 4 + 4 * extra)
out = dict(status='conditional-support', matching_controls=rows, flat_controls=flat, scope='Fixed-R sufficiently weak coupling; no uniform size threshold. Finite checks corroborate the analytic proof, not replace it.')
p = ROOT / 'outputs/native_six_layer_ground_selection/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
