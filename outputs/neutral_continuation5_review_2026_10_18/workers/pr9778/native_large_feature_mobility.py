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
from neutral_mobility_control import run_checks
from neutral_mobility_finite_graph import run_checks as finite_checks
rows = run_checks()
finite = finite_checks()
_check('P9778:C001', rows[0]['curvature_y'] < 0 and rows[-1]['curvature_y'] > 0)
_check('P9778:C002', all((r['curvature_z'] > 0 and r['source_weight_over_lambda2'] > 0 for r in rows)))
out = dict(status='bounded-support', cavity_controls=rows, finite_graph_control=finite, scope='Native K1 curvature and leading source coefficient, not full-H dispersion or empirical scalar test')
p = ROOT / 'outputs/native_large_feature_mobility/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
