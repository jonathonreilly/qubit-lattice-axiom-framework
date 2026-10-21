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
import subprocess, sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
controls = {}
for name in ['neutral_complementary_all_length.py', 'neutral_third_height_symbolic.py']:
    args = ['6', '6'] if name == 'neutral_third_height_symbolic.py' else []
    q = _run_child([sys.executable, str(P / name), *args], check=True, capture_output=True, text=True, timeout=90)
    controls[name] = json.loads(q.stdout)
for row in controls['neutral_complementary_all_length.py']:
    _check('P9796:C001', row['scaled'] == '1')
result = dict(status='conditional-support', controls=controls, scope='Fixed-height canonical prepared background vertex; no empirical scalar or hierarchy selection')
f = ROOT / 'outputs/native_all_height_assisted_hop/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
