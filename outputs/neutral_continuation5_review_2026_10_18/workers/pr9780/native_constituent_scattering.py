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
for name in ['neutral_scattering_resolvent_control.py', 'neutral_scattering_control.py']:
    r = subprocess.run([sys.executable, str(P / name)], check=True, text=True, timeout=160)
    checks[name] = 'completed; child stdout/stderr streamed into owning capture'
    _check('child:' + name, r.returncode == 0)
out = dict(status='bounded-support', checks=checks, scope='Native coefficient constituent scattering; broadened development controls, not full-H asymptotic scattering or empirical tests')
f = ROOT / 'outputs/native_constituent_scattering/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
