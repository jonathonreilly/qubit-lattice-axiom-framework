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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/PHYSICAL_PAIR_SOURCE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_physical_pair_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARGED_COLUMN_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/REFLECTION_GROUND_SECTOR_PROOF.md']
from pathlib import Path
import json, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
r = _run_child([sys.executable, str(ROOT / AUDIT_INPUT_PATHS[1])], check=True, capture_output=True, text=True, timeout=90)
c = json.loads(r.stdout)
_check('native_physical_pair_source:C001', c['max_error'] < 1e-12)
_check('native_physical_pair_source:C002', all((x['reversed_bonds'] == [40, 20] and x['amplitude_coefficients'] == ['-5/4', '-5/8'] for x in c['rows'])))
out = dict(status='conditional-support', scope='Finite-volume physical pair-source normalization and Pauli bond counts; uniform exact-state transfer analytic, not full ED or an observation test', control=c)
p = ROOT / 'outputs/native_physical_pair_source/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
