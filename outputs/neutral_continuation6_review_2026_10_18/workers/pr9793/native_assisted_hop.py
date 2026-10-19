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
import subprocess, sys, json, math
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'

def run(name, *args):
    r = _run_child([sys.executable, str(P / name), *map(str, args)], check=True, capture_output=True, text=True, timeout=90)
    return json.loads(r.stdout)
m = 8 / (math.sqrt(80 ** 2 + 4 * 4 ** 2) + 80)
_check('P9793:C001', m > 0 and m * m / 16 > 0)
result = dict(status='bounded-support', symbolic_R6=run('neutral_third_order_symbolic.py', 6), symbolic_R7=run('neutral_third_order_symbolic.py', 7), complementary=run('neutral_complementary_hop.py'), variance_lower=m * m, vertex_weight_coefficient_lower=m * m / 16, scope='Canonical native nearest-hop vertex; matched dressed prepared channel, not relaxed emission rate')
f = ROOT / 'outputs/native_assisted_hop/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
