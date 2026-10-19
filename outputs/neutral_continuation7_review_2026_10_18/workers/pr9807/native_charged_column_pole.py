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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARGED_COLUMN_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/WHOLE_COLUMN_MODE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_LAYER_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_charged_column_control.py']
from pathlib import Path
import subprocess, sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
r = _run_child([sys.executable, str(P / 'neutral_charged_column_control.py')], capture_output=True, text=True, check=True, timeout=90)
control = json.loads(r.stdout)
_check('native_charged_column_pole:C001', control['gamma'] == '12155/33554432')
_check('native_charged_column_pole:C002', all((x['amplitude_correction'] == '-5/8' and x['weight_correction'] == '-5/4' and (x['minimum_shapes'] == [[1, 1, 8]]) for x in control['rows'])))
_check('native_charged_column_pole:C003', all((x['next_perimeter'] == 12 for x in control['rows'][1:])))
out = dict(status='conditional-support', scope='Native bond-level source dressing and charged geometry controls; actual-grid transfer analytic; charged source is not neutral ZZ source', control=control)
f = ROOT / 'outputs/native_charged_column_pole/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
