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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/BOUND_MODE_ENVIRONMENT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PROBE_LOOP_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ALL_HEIGHT_ASSISTED_HOP_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_bound_return.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_flux_green.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_flux_retarded.py']
from pathlib import Path
import subprocess, sys, json, math
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
a = {}
for name in ['neutral_bound_return.py', 'neutral_flux_green.py', 'neutral_flux_retarded.py']:
    q = _run_child([sys.executable, str(P / name)], check=True, capture_output=True, text=True, timeout=90)
    a[name] = json.loads(q.stdout)
x = a['neutral_bound_return.py']
_check('native_bound_mode_environment:C001', [z['trace_difference'] for z in x['moments']] == [0, 0, 0, -64, 0, -1440, 0, -26112, 0, -439840])
y = a['neutral_flux_green.py']
_check('native_bound_mode_environment:C002', all((z['full_schur_error'] < 1e-12 and z['residual'] < 1e-10 for z in y['rows'])))
_check('native_bound_mode_environment:C003', abs(y['rows'][-1]['ratio'] - y['ratio_limit']) < 2e-07)
z = a['neutral_flux_retarded.py']
_check('native_bound_mode_environment:C004', z['rows'][-1]['relative_error'] < 2e-06)
_check('native_bound_mode_environment:C005', abs(z['limit'] - 2 * y['scaled_source_limit']) < 1e-12)
out = dict(status='conditional-support', controls=a, scope='Matched dressed finite-time pole return plus separate static-background coefficient scattering; not full native on-shell emission')
f = ROOT / 'outputs/native_bound_mode_environment/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
