import sys as _sys
if _sys.flags.optimize: raise RuntimeError('Optimized Python disables scientific helper assertions')
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
_groups=set();_calls=0
def _check(label,condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)
from pathlib import Path
import sys, subprocess, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
checks = {}
for name in ['neutral_large_collision_interval.py', 'neutral_general_contact_control.py', 'neutral_fourbody_physical_control.py', 'neutral_large_collision_quadrature.py']:
    r = subprocess.run([sys.executable, str(P / name)], check=True, text=True, timeout=90)
    checks[name] = 'completed; child stdout/stderr streamed into owning capture'
    _check('child:' + name, r.returncode == 0)
out = dict(status='bounded-support', checks=checks, scope='Native coefficient contact/Born numerator for large neutral features; no exact four-body S, lifetime, actual-H linewidth or observation test')
f = ROOT / 'outputs/native_large_feature_collision/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
