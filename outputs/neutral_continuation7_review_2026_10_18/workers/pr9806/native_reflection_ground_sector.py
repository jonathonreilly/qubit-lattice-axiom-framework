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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_reflection_ed.py']
from pathlib import Path
import subprocess, sys, json, os
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
env = dict(os.environ, OPENBLAS_NUM_THREADS='1')
r = _run_child([sys.executable, str(P / 'neutral_reflection_ed.py')], capture_output=True, text=True, check=True, timeout=90, env=env)
rows = json.loads(r.stdout)
_check('native_reflection_ground_sector:C001', len(rows) == 6)
_check('native_reflection_ground_sector:C002', max((abs(x['difference']) for x in rows)) < 1e-09)
_check('native_reflection_ground_sector:C003', max((x['residual'] for x in rows)) < 1e-09)
_check('native_reflection_ground_sector:C004', min((min(x['plane_expectations']) for x in rows)) > 1 - 1e-09)
out = dict(status='exact-support', scope='Analytic finite even-lattice ground existence; small-grid sign controls only, no uniqueness or empirical test', rows=rows)
f = ROOT / 'outputs/native_reflection_ground_sector/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
