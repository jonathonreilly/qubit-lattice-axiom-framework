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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_SCALAR_TETRAMER_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_tetramer_geometry.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_tetramer_order10.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_SECONDARY_ENERGY_CHECK.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/NATIVE_PAIR_SCATTERING_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_order10_pair_control.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md']
from pathlib import Path
import json, subprocess, sys
from fractions import Fraction as F
ROOT = Path(__file__).resolve().parents[1]
results = []
for f in AUDIT_INPUT_PATHS[1:3]:
    r = _run_child([sys.executable, str(ROOT / f)], check=True, capture_output=True, text=True, timeout=60)
    results.append(json.loads(r.stdout))
g, d = results
_check('native_scalar_tetramer:C001', g['tested'] == 4912)
_check('native_scalar_tetramer:C002', min(map(int, g['histogram'])) == -5832 and g['histogram']['-5832'] == 4)
_check('native_scalar_tetramer:C003', sorted(map(int, g['histogram']))[1] == -2916)
_check('native_scalar_tetramer:C004', F(d['full_BminusA']) == F(949685, 12230590464))
def normalized_mask(points):
 x0=min(x for x,y in points);y0=min(y for x,y in points)
 return tuple(sorted((x-x0,y-y0) for x,y in points))
expected_minima=set()
for points in [[(0,0),(1,0),(4,0),(5,0)],[(0,0),(1,0),(0,3),(1,3)]]:
 expected_minima.add(normalized_mask(points))
 expected_minima.add(normalized_mask([(-y,x) for x,y in points]))
actual_minima={normalized_mask(row['columns']) for row in g['negative_examples'] if row['energy']==-5832}
_check('tetramer:exact four minimizing physical column masks', actual_minima==expected_minima and len(expected_minima)==4)
masks = [{(0, 0), (1, 0), (4, 0), (5, 0)}, {(0, 0), (1, 0), (0, 3), (1, 3)}]
source = []
for i, T in enumerate(masks):
    for rotated in [False, True]:
        S = {(-y, x) for x, y in T} if rotated else T
        boundary = sum(((x, y + dy) not in S for x, y in S for dy in [-1, 1]))
        _check('native_scalar_tetramer:C005', boundary == (4 if rotated else 8))
        source.append(dict(family=i, rotated=rotated, crossing_Y_bonds_per_layer=boundary, weight_loss_coefficient_L10=str(F(10 * boundary, 16))))
out = dict(status='conditional-support', scope='Native excited tetramer binding and q0 A1 source; no mobility or on-shell selfcoupling claimed', geometry=g, order10=d, physical_X_source=source, scalar_covariant_weight_loss='5', binding_coefficient_L10=str(F(90, 32768)))
p = ROOT / 'outputs/native_scalar_tetramer/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
