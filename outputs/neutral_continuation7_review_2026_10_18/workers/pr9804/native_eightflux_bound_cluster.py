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
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/COLUMN_READOUT_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/EIGHT_FLUX_BOUND_CLUSTER_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_eightflux_geometry.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_detour_winding.py', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_q8_source_control.py']
from pathlib import Path
import subprocess, sys, json
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
a = {}
for name in ['neutral_eightflux_geometry.py', 'neutral_detour_winding.py', 'neutral_q8_source_control.py']:
    r = _run_child([sys.executable, str(P / name)], capture_output=True, text=True, check=True, timeout=90)
    a[name] = json.loads(r.stdout)
g = a['neutral_eightflux_geometry.py']
_check('native_eightflux_bound_cluster:C001', sorted(((x['w'], x['h']) for x in g['minima'])) == [(2, 4), (4, 2)])
_check('native_eightflux_bound_cluster:C002', len(g['paths']) == 4)
r = next((x for x in a['neutral_detour_winding.py']['rows'] if x['L'] == 10))
_check('native_eightflux_bound_cluster:C003', r['all_layers'] == '-1076510135/10567230160896' and r['marked_ratio'] == '1616665793187/110234637824')
s = a['neutral_q8_source_control.py']
_check('native_eightflux_bound_cluster:C004', s['coefficient'] == '1361400132699035/945539748965690376192')
_check('native_eightflux_bound_cluster:C005', abs(s['rows'][-1]['relative_error']) < 1e-07)
expected_paths = {
 str([(-1, 0), (1, 0)]): [(4, 12), (8, 16)],
 str([(1, 0), (3, 0)]): [(4, 12), (8, 16)],
 str([(0, -1), (2, -1)]): [(8, 14), (8, 14)],
 str([(0, 1), (2, 1)]): [(8, 14), (8, 14)],
}
actual_paths = {key: sorted((row['Q'], row['perimeter']) for row in values) for key, values in g['paths'].items()}
_check('geometry:complete intermediate charge and perimeter multisets', actual_paths == expected_paths)
out = dict(status='conditional-support', scope='Native fixed-L coefficient and source controls; actual selected-fibre transfer is analytic, not full-grid ED; no empirical test', controls=a)
f = ROOT / 'outputs/native_eightflux_bound_cluster/result.json'
f.parent.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))
(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
