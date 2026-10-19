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
import subprocess, sys, json
from fractions import Fraction as F
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
controls = {}
for name in ['neutral_sixth_loop.py', 'neutral_sixth_star.py', 'neutral_sixth_torus.py', 'neutral_sixth_plaquette.py', 'neutral_sixth_plaquette_independent.py']:
    q = _run_child([sys.executable, str(P / name)], check=True, capture_output=True, text=True, timeout=90)
    if name == 'neutral_sixth_plaquette.py':
        data = [json.loads(x) for x in q.stdout.splitlines()]
    elif name == 'neutral_sixth_plaquette_independent.py':
        data = [dict(z=int(x.split()[0]), total=x.split()[1]) for x in q.stdout.splitlines()]
    else:
        data = json.loads(q.stdout)
    controls[name] = data
_check('P9798:C001', controls['neutral_sixth_loop.py'][1]['per_layer'] == '-3/8192')
expected = ['7/2048', '-11/4608', '-11/4608', '0']
for name in ['neutral_sixth_plaquette.py', 'neutral_sixth_plaquette_independent.py']:
    _check('P9798:C002', [x['total'] for x in controls[name]] == expected)
_check('P9798:C003', sum(map(F, expected)) == F(-25, 18432))
s = controls['neutral_sixth_star.py']
_check('P9798:C004', 2.11447531630064 < s['E_over_t'] < 2.11447531630066)
_check('P9798:C005', 0.1406861564 < s['source_weight'] < 0.1406861565)
for row in controls['neutral_sixth_torus.py']:
    _check('P9798:C006', row['upper'] > 2 and row['next'] < 2)
weight = float(F(63, 8192) ** 2 * F(121, 54)) * s['source_weight']
result = dict(status='conditional-support', controls=controls, original_pole_weight_coefficient=weight, scope='Actual selected-symmetry-fibre mode in weak-coupling logarithmic-box family; not global-ground or empirical scalar')
f = ROOT / 'outputs/native_six_layer_neutral_pole/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
