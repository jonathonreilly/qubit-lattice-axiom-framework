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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_ENERGY_SOURCE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_energy_source_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md']
from pathlib import Path
import json, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
r = _run_child([sys.executable, str(ROOT / AUDIT_INPUT_PATHS[1])], check=True, capture_output=True, text=True, timeout=90)
c = json.loads(r.stdout)
_check('native_energy_source_pole:C001', len(c['square']) == 16)
_check('native_energy_source_pole:C002', all((x['vertex_ratios'] == ['-3/4'] * 4 and x['edge_ratios'] == ['1'] * 4 for x in c['square'])))
_check('native_energy_source_pole:C003', next((x for x in c['winding'] if x['L'] == 10))['x_pair_qx2'] == '-3/2')
out = dict(status='conditional-support', scope='Native energy-density marked-path coefficients; actual-H pole/source transfer analytic, not observations', control=c)
p = ROOT / 'outputs/native_energy_source_pole/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
