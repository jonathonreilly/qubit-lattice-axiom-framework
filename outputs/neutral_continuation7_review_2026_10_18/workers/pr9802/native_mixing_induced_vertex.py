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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/MIXING_INDUCED_VERTEX_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/BOUND_MODE_ENVIRONMENT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mixing_vertex.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_mixing_scattering.py']
from pathlib import Path
import subprocess, sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
a = {}
for name in ['neutral_mixing_vertex.py', 'neutral_mixing_scattering.py']:
    q = _run_child([sys.executable, str(P / name)], check=True, capture_output=True, text=True, timeout=90)
    a[name] = json.loads(q.stdout)
_check('native_mixing_induced_vertex:C001', a['neutral_mixing_vertex.py']['duhamel_error'] < 1e-12)
_check('native_mixing_induced_vertex:C002', a['neutral_mixing_scattering.py']['threshold_rows'][-1]['relative_error'] < 1e-05)
out = dict(status='conditional-support', controls=a, scope='Native local matched vertex; separate pinned coefficient scattering, not full microscopic rate')
f = ROOT / 'outputs/native_mixing_induced_vertex/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
