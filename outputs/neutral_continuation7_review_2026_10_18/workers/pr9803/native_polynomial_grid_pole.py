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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/MICROSCOPIC_GROUND_WINDOW_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_flux_connected_row.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_polynomial_dispersion.py']
from pathlib import Path
import subprocess, sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
a = {}
for name in ['neutral_flux_connected_row.py', 'neutral_polynomial_dispersion.py']:
    q = _run_child([sys.executable, str(P / name)], check=True, capture_output=True, text=True, timeout=90)
    a[name] = json.loads(q.stdout)
_check('native_polynomial_grid_pole:C001', all((r['nonzero'] == 33 and r['row_l1'] == '35/2' and (r['far_transition'] == '0') for r in a['neutral_flux_connected_row.py']['rows'])))
_check('native_polynomial_grid_pole:C002', max((r['relative_error'] for r in a['neutral_polynomial_dispersion.py']['rows'][-3:])) < 2e-06)
out = dict(status='conditional-support', controls=a, scope='Analytic selected-fibre microscopic transfer; numerical controls of connected coefficients, not full-grid diagonalization')
f = ROOT / 'outputs/native_polynomial_grid_pole/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
