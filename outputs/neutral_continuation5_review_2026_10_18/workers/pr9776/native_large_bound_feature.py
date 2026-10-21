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
import sys, json, numpy as np
from scipy.sparse.linalg import eigsh
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'
sys.path.insert(0, str(P))
from neutral_threshold_interval import run_certificate
from neutral_threshold_highprecision import run_roots
from neutral_transverse_bound_model import matrix
certificate = run_certificate()
rows = run_roots()
controls = []
expected = -4.4 - float(rows[0]['gap'])
for L in [50, 100]:
    H, s, idx = matrix(L, b=0.1)
    e = eigsh(H, k=1, which='SA', tol=1e-12, return_eigenvectors=False)[0]
    controls.append(dict(L=L, energy=float(e), error=float(e - expected)))
_check('P9776:C001', abs(controls[-1]['error']) < 1e-08)
_check('P9776:C002', abs(controls[-1]['error']) < abs(controls[0]['error']))
_check('P9776:C003', all((float(rows[i]['gap']) > float(rows[i + 1]['gap']) for i in range(len(rows) - 1))))
_check('P9776:C004', all((float(rows[i]['scaled_log']) < float(rows[i + 1]['scaled_log']) < 0.954 for i in range(len(rows) - 1))))
out = dict(status='bounded-support', threshold_certificate=certificate, coefficient_binding_roots=rows, finite_graph_control=controls, scope='Selected native K1 momentum family and original-source coefficient; no full-H scalar or empirical test')
p = ROOT / 'outputs/native_large_bound_feature/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
