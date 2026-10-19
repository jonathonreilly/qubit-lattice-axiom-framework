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
import sys, json, subprocess
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
checks = {}
for name in ['neutral_pair_algebra_control.py', 'neutral_pair_mixed_control.py', 'neutral_two_feature_contact_control.py', 'neutral_source_contact_control.py']:
    result = subprocess.run([sys.executable, str(P / name)], check=True, text=True, timeout=60)
    checks[name] = 'completed; child stdout/stderr streamed into owning capture'
    _check('child:' + name, result.returncode == 0)
out = dict(status='bounded-support', checks=checks, scope='Exact local algebra/contact controls for analytic two-feature window-vector theorem; no full-H ED, isolated particles, finite-density theory or empirical tests')
p = ROOT / 'outputs/native_two_feature_ladder/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
