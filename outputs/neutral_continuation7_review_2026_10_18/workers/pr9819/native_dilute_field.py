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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_DILUTE_FIELD_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_cluster_fock_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_dilute_field_scaling.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARACTER_INDEPENDENT_COLLISION_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md']
from pathlib import Path
import json, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
results = []
for f in AUDIT_INPUT_PATHS[1:3]:
    r = _run_child([sys.executable, str(ROOT / f)], check=True, capture_output=True, text=True, timeout=110)
    results.append(json.loads(r.stdout))
for row in results[0]['rows']:
    _check('native_dilute_field:C001', abs(row['rows'][0]['full_lowering_error'] * row['R'] ** 2 - 99) < 1e-08)
out = dict(status='conditional-support', scope='Native finite-mode fixed-occupation bosonic limit; no relativistic or finite-density field claim', motif_control=results[0], derived_matrix_control=results[1])
p = ROOT / 'outputs/native_dilute_field/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
