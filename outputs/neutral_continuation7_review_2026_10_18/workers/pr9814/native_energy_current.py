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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ENERGY_CURRENT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_energy_current_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ENERGY_SOURCE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md']
from pathlib import Path
import json, subprocess, sys, os
ROOT = Path(__file__).resolve().parents[1]
env = dict(os.environ, OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
r = _run_child([sys.executable, str(ROOT / AUDIT_INPUT_PATHS[1])], check=True, capture_output=True, text=True, timeout=90, env=env)
c = json.loads(r.stdout)
_check('native_energy_current:C001', max((x['operator_residual'] for x in c['continuity'])) < 1e-11)
_check('native_energy_current:C002', max((x['spectral_residual'] for x in c['continuity'])) < 1e-11)
out = dict(status='bounded-support', scope='Native energy continuity and pole Ward relation; finite control is not an L10 pole or observation test', control=c)
p = ROOT / 'outputs/native_energy_current/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
