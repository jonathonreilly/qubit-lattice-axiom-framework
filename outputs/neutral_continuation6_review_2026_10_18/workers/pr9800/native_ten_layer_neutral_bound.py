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
import subprocess, sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
a = {}
for name in ['neutral_eighth_rectangle.py', 'neutral_ten_layer_star.py']:
    q = _run_child([sys.executable, str(P / name)], check=True, capture_output=True, text=True, timeout=60)
    a[name] = json.loads(q.stdout)
x = a['neutral_eighth_rectangle.py']
_check('P9800:C001', x['loops'][2]['coefficient'] == '-9/262144')
_check('P9800:C002', F(x['heights'][0]['v_over_two_gamma']) < 1)
G = F(12155, 33554432)
beta = F(165, 17)
weight = 2 * G * G * beta * beta / 10
_check('P9800:C003', weight == F(2783620125, 1125899906842624))
y = a['neutral_ten_layer_star.py']
r = y['rows'][-1]
_check('P9800:C004', abs(r['source_weight'] - 2) < 3e-08)
_check('P9800:C005', abs(r['curvature_scaled'] / y['expected_curvature'] - 1) < 3e-05)
_check('P9800:C006', abs(r['splitting_scaled'] / y['expected_splitting'] - 1) < 5e-05)
out = dict(status='conditional-support', controls=a, source_weight_coefficient=str(weight), scope='Actual selected-fibre zero-momentum pole in logarithmic boxes; positive curvature separately at coefficient level with q much smaller than lambda; no empirical scalar')
f = ROOT / 'outputs/native_ten_layer_neutral_bound/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
