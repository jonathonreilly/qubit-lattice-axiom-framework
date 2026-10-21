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
from neutral_transverse_bound_model import matrix
from neutral_transverse_physical_control import run_checks
physical = run_checks()
rows = []
for L in [30, 60]:
    H, s, idx = matrix(L)
    v = np.zeros(len(s))
    r = 1 / np.sqrt(2)
    for x in range(-L, L + 1):
        v[idx[x, 1]] = 0.5 * r ** abs(x)
    for ell in range(2, L + 2):
        v[idx['y', ell]] = 0.5 * (-r) ** (ell - 1)
    residual = np.linalg.norm(H @ v + 3 * np.sqrt(2) * v)
    _check('P9775:C001', residual < 4 * r ** L + 1e-12)
    for b in [0, 0.001, 0.005, 0.01, 0.02]:
        H, s, idx = matrix(L, b=b)
        e, U = eigsh(H, k=1, which='SA', tol=1e-12)
        q = U[:, 0]
        q *= np.sign(q[idx[0, 1]])
        src = -q[idx[1, 0]] + b * q[idx[0, 1]]
        if b == 0:
            _check('P9775:C002', abs(e[0] + 3 * np.sqrt(2)) < 1e-08 and abs(src) < 1e-09)
        if b == 0.001:
            _check('P9775:C003', abs(src / b + 1.5) < 0.0002)
            _check('P9775:C004', abs((e[0] + 3 * np.sqrt(2)) / b ** 2 + 25 / np.sqrt(2)) < 0.002)
        rows.append(dict(L=L, b=b, energy=float(e[0]), source_over_lambda=float(src), analytic_anchor_residual=float(residual)))
n = np.arange(1, 101)
Spp = np.sum(r ** (n[:, None] + n[None, :] + abs(n[:, None] - n[None, :])))
n = np.arange(-100, 101)
Sabs = np.sum(r ** (abs(n[:, None]) + abs(n[None, :]) + abs(n[:, None] - n[None, :])))
_check('P9775:C005', abs(Spp - 3) < 1e-12 and abs(Sabs - 13) < 1e-12)
out = dict(status='bounded-support', physical_bit_Bloch_controls=physical, fibers=rows, geometric_sums=[float(Spp), float(Sabs)], scope='Complete compact layer-even N4 K1 bound eigenstate and leading original source; supplied H/reference, no full-H or empirical scalar claim')
p = ROOT / 'outputs/native_transverse_bound_composite/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
