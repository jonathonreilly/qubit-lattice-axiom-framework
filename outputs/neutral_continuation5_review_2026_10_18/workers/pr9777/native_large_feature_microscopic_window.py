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
import sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0, str(P))
from neutral_window_orbit_control import run_checks
out = dict(status='bounded-support', physical_bit_controls=run_checks(), scope='Exact symmetry/orbit controls supporting analytic uniform local bounds and spectral-window inequality; no finite-lambda full-H spectrum or empirical data')
_check('P9777:C001', out['physical_bit_controls']['backgrounds'] == 128 and out['physical_bit_controls']['seed_and_symmetry_checks'] == 384)
p = ROOT / 'outputs/native_large_feature_microscopic_window/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
