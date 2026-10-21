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

def run(name, *args):
    r = _run_child([sys.executable, str(P / name), *args], check=True, capture_output=True, text=True, timeout=90)
    return json.loads(r.stdout)
result = dict(status='bounded-support', integer_moment_R13=run('neutral_bulk_moment_bound.py', '13'), integer_moment_R17=run('neutral_bulk_moment_bound.py', '17'), finite_moment_checks=run('neutral_bulk_response_control.py'), auxiliary_series=run('neutral_plaquette_series_control.py'), scope='Native coefficient response density theorem; ordered microscopic lambda then area limit, no bulk 3D scalar or empirical identification')
f = ROOT / 'outputs/native_slab_response_density/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
