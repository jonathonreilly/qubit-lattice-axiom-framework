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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PAIR_SCATTERING_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_order10_pair_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_scattering_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/SECONDARY_NEUTRAL_MOLECULE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/PRIMITIVE_LOOP_INTERACTION_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARGED_COLUMN_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_collision_packet.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_pair_collision_packet.json']
from pathlib import Path
import subprocess, sys, json, os
ROOT = Path(__file__).resolve().parents[1]
env = dict(os.environ, OPENBLAS_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1')
controls = []
for path in AUDIT_INPUT_PATHS[1:3]:
    r = _run_child([sys.executable, str(ROOT / path)], check=True, capture_output=True, text=True, timeout=45, env=env)
    controls.append(json.loads(r.stdout))
_check('native_pair_scattering:C001', controls[0]['pair_contrast'] == '333355/24461180928')
_check('native_pair_scattering:C002', controls[1]['core_size'] == 37 and controls[1]['potential_sites'] == 20)
out = dict(status='conditional-support', scope='Derived leading native pair collision operator and its threshold T; not a fixed-lambda microscopic S-matrix or empirical fit', controls=controls)
p = ROOT / 'outputs/native_pair_scattering/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
