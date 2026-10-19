import sys as _sys
if _sys.flags.optimize: raise RuntimeError('Optimized Python disables scientific helper assertions')
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
from neutral_continuation6_child_io_2026_10_18 import run_tee
_groups=set();_calls=0
def _check(label,condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)

def _run_child(args, **kwargs):
 result=run_tee(args, **kwargs)
 _check('child:'+str(args[1:]), result.returncode==0)
 return result
from pathlib import Path
import sys, subprocess, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
r = _run_child([sys.executable, str(P / 'neutral_fixed_ladder_control.py')], check=True, capture_output=True, text=True, timeout=60)
out = dict(status='bounded-support', algebra_controls=json.loads(r.stdout), scope='Every fixed finite occupation under inherited native normal-form bounds; numerical controls check algebra, not the microscopic many-body spectrum or observations')
f = ROOT / 'outputs/native_fixed_occupation_ladder/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
