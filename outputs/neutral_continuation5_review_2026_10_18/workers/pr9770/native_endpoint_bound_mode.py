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
from neutral_endpoint_model import matrix
rows = []
for L in [20, 40, 80]:
    for k in [0, 0.3, 0.6, 1.0]:
        H, s = matrix(L, k)
        _check('P9770:C001', len(s) == 4 * L + 3)
        e, u = eigsh(H, k=2, which='SA', tol=1e-12)
        q = np.zeros(len(s), complex)
        q[0] = 1 / np.sqrt(3)
        for i, h in enumerate(s[1:], 1):
            n = max(h)
            if h in [(0, 0, n, n), (n, n, 0, 0)]:
                q[i] = 3 ** (-n / 2) / np.sqrt(3)
            elif h in [(0, n, 0, n), (n, 0, n, 0)]:
                q[i] = (-1) ** n * 3 ** (-n / 2) / np.sqrt(3)
        pred = -8 * np.cos(k / 2) / np.sqrt(3)
        res = float(np.linalg.norm(H @ q - pred * q))
        _check('P9770:C002', res < 5 * 3 ** (-L / 2) + 1e-12 and abs(min(e) - pred) < 1e-08)
        form = []
        for p in [0, 0.3, 0.6]:
            density = np.array([sum(np.exp(1j * p * (np.array(h) - np.mean(h)))) for h in s])
            v = np.vdot(q, density * q)
            expected = 4 * (1 + np.cos(p / 2)) / (5 - 3 * np.cos(p / 2))
            err = float(abs(v - expected))
            _check('P9770:C003', err < 1e-08)
            form.append(dict(p=p, error=err))
        idx = {h: i for i, h in enumerate(s)}
        rq = np.zeros_like(q)
        for i, h in enumerate(s):
            rot = (h[2], h[0], h[3], h[1])
            rq[idx[rot]] += (-1) ** (sum(h) // 2) * q[i]
        _check('P9770:C004', np.linalg.norm(rq - q) < 1e-12)
        rows.append(dict(L=L, k=k, dimension=len(s), energy=float(min(e)), predicted=pred, analytic_vector_residual=res, form_checks=form))
leak = []
for nx, ny in [(2, 2), (2, 3), (3, 3), (4, 4)]:
    F = {(x, y) for x in range(nx) for y in range(ny)}
    ell = 4
    s = {(x, y, z) for x, y in F for z in range(ell)}
    targets = set()
    wall = lambda S: sum((((x, y, z) in S) != ((x, y, z + 1) in S) for x, y in F for z in range(-2, ell + 1)))
    for x, y in F:
        for dx, dy in [(1, 0), (0, 1)]:
            if (x + dx, y + dy) not in F:
                continue
            for z in [-1, 0, ell - 1, ell]:
                t = s ^ {(x, y, z), (x + dx, y + dy, z)}
                _check('P9770:C005', wall(t) == wall(s))
                targets.add(frozenset(t))
    E = (nx - 1) * ny + nx * (ny - 1)
    _check('P9770:C006', len(targets) == 4 * E)
    leak.append(dict(nx=nx, ny=ny, distinct_targets=len(targets)))
for ell in range(2, 12):
    S = set(range(ell))
    mismatch = sum(((z in S) != (z + 2 in S) for z in range(-3, ell + 2)))
    _check('P9770:C007', mismatch == 4)
for h in range(-3, 4):
    for p in [0, 0.3, 0.6]:
        direct = sum((-2 * np.exp(1j * p * (z + 1)) for z in range(h - 3, h + 3) if (z <= h) != (z + 2 <= h)))
        _check('P9770:C008', abs(direct + 4 * np.cos(p / 2) * np.exp(1j * p * (h + 0.5))) < 1e-12)
out = dict(status='bounded-support', fibers=rows, rigid_leakage_controls=leak, scope='Exact K1 boundary-sector bound mode and original excess-readout form factor; not finite-droplet/full-H particle theorem or observation')
p = ROOT / 'outputs/native_endpoint_bound_mode/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
