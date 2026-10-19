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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/CONSTRAINED_FERMION_ROUTE.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_majorana_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_feature_clifford_control.py']
from pathlib import Path
import json, subprocess, sys, os
ROOT = Path(__file__).resolve().parents[1]
env = dict(os.environ, OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
controls = []
for path in AUDIT_INPUT_PATHS[1:]:
    r = _run_child([sys.executable, str(ROOT / path)], capture_output=True, text=True, check=True, timeout=45, env=env)
    controls.append(json.loads(r.stdout))
_check('native_constrained_fermion:C001', controls[0]['status'] == 'exact-algebra-pass')
c = controls[1]
_check('native_constrained_fermion:C002', c['isometry_error'] < 1e-12 and max(c['compression_errors']) < 1e-12)
_check('native_constrained_fermion:C003', all((r['leakage_norm'] > 1 for r in c['native_challenge'])))
out = dict(status='bounded-support', scope='Constrained representation and explicitly chosen code failure; no derived physical fermion or observational test', controls=controls)
p = ROOT / 'outputs/native_constrained_fermion/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
