import sys as _sys
if _sys.flags.optimize: raise RuntimeError('Optimized Python disables scientific helper assertions')
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
from neutral_continuation7_child_io_2026_10_18 import run_tee
_groups=set();_calls=0
def _check(label,condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True);raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)
def _run_child(args, **kwargs):
 result=run_tee(args, **kwargs)
 _check('child:'+str(args[1:]),result.returncode==0)
 return result
AUDIT_TIMEOUT_SEC=300
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/EIGHT_FLUX_BOUND_CLUSTER_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_q8_orientation.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_q8_isotropic_control.py']
from pathlib import Path
import subprocess, sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
a = {}
for name in ['neutral_q8_orientation.py', 'neutral_q8_isotropic_control.py']:
    r = _run_child([sys.executable, str(P / name)], capture_output=True, text=True, check=True, timeout=90)
    a[name] = json.loads(r.stdout)
_check('native_isotropic_bound_feature:C001', a['neutral_q8_orientation.py']['total'] == '607201/144000')
_check('native_isotropic_bound_feature:C002', len(a['neutral_q8_orientation.py']['kernel']) == 9)
_check('native_isotropic_bound_feature:C003', max((abs(x['relative_error']) for x in a['neutral_q8_isotropic_control.py']['rows'][-3:])) < 1e-12)
kernel = a['neutral_q8_orientation.py']['kernel']
expected_kernel = {str((x, y)): ('9673/12000' if x == y == 0 else '191/384' if x == 0 or y == 0 else '1637/4608') for x in (-1, 0, 1) for y in (-1, 0, 1)}
_check('orientation:all nine rational spatial weights', kernel == expected_kernel)
p = 5
M = 60
powers = dict(energy=14 + 2 * p, anisotropy=6 + 4 * p, tail=M - 2 * p, source_error=M - 22 - 3 * p)
_check('native_isotropic_bound_feature:C004', powers['anisotropy'] > powers['energy'] and powers['tail'] > powers['energy'] and (powers['source_error'] > 18))
out = dict(status='conditional-support', scope='Exact local orientation coefficient and derived matrix control; actual selected-sector polynomial-grid theorem analytic; no empirical test', powers=powers, controls=a)
f = ROOT / 'outputs/native_isotropic_bound_feature/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
