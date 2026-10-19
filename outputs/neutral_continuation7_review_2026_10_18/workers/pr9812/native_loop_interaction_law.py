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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/PRIMITIVE_LOOP_INTERACTION_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_loop_interaction_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_loop_feshbach_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md']
from pathlib import Path
import json, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
controls = []
for source in AUDIT_INPUT_PATHS[1:3]:
    r = _run_child([sys.executable, str(ROOT / source)], check=True, capture_output=True, text=True, timeout=110)
    controls.append(json.loads(r.stdout))
a, b = controls
for row in b:
    _check('native_loop_interaction_law:C001', row['connected'] == a['linked'][row['dz']]['coefficient'])
_check('native_loop_interaction_law:C002', a['diagonal_interaction'] == '545/5308416')
_check('native_loop_interaction_law:C003', a['axis_interaction'] == '-9/32768')
out = dict(status='bounded-support', scope='Exact local primitive and connected interaction coefficients; no observation or isolated-band test', subset=a, independent_feshbach=b)
p = ROOT / 'outputs/native_loop_interaction_law/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
