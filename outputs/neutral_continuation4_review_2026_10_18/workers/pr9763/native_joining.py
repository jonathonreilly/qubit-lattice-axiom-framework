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
from fractions import Fraction as F
import json
from pathlib import Path

def path(J):
    L = len(J) + 1
    v = {0: F(1)}
    for S in range(1, 1 << L):
        x = sum((v[S ^ 1 << i] for i in range(L) if S >> i & 1))
        if S != (1 << L) - 1:
            den = 4 * sum((J[i] for i in range(L - 1) if (S >> i ^ S >> i + 1) & 1))
            x /= den
        v[S] = x
    pred = F(1)
    for j in J:
        pred /= 2 * j
    _check('P9763:native_joining:C001', v[(1 << L) - 1] == pred)
    return str(pred)
out = []
for g in [F(1, 3), F(1), F(2)]:
    out.append(dict(g=str(g), t10=path([F(1)] * 4 + [g] + [F(1)] * 4)))
Nx, Ny = (4, 6)
patterns = []
for a in range(1 << Nx - 1):
    aa = [1] + [1 - 2 * (a >> i & 1) for i in range(Nx - 1)]
    for b in range(1 << Ny):
        bb = [1 - 2 * (b >> j & 1) for j in range(Ny)]
        patterns.append(tuple((x * y for x in aa for y in bb)))
_check('P9763:native_joining:C002', len(set(patterns)) == 512)
mismatches = [sum((x != 1 for x in s)) for s in patterns]
_check('P9763:native_joining:C003', min((k for k in mismatches if k)) == 4)
for h in range(512):
    trace = sum(((-1) ** (h & x).bit_count() for x in range(512)))
    _check('P9763:native_joining:C004', trace == (512 if h == 0 else 0))
result = dict(status='bounded-support', pair_coefficients=out, pattern_count=len(patterns), min_pattern_interface_cost_over_g=2 * min((k for k in mismatches if k)), characters=512, neutral_multiplicity=1, scope='Exact path and representation controls, not240-spin diagonalization or observational test')
p = Path(__file__).resolve().parents[1] / 'outputs/native_joining/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
