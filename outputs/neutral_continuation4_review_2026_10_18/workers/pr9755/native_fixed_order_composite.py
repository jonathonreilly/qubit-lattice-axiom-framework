import sys as _sys
if _sys.flags.optimize: raise RuntimeError("Optimized Python disables scientific helper assertions")
_sys.stdout.reconfigure(line_buffering=True)
_sys.stderr.reconfigure(line_buffering=True)
_groups=set(); _calls=0
def _check(label, condition):
 global _calls
 _calls+=1
 if not bool(condition):
  print('[FAIL]',label,flush=True)
  print(f'TOTAL: PASS={len(_groups)} FAIL=1',flush=True)
  raise AssertionError(label)
 if label not in _groups:
  _groups.add(label);print('[PASS]',label,flush=True)
"""Physical finite-grid gauge check and punctured-host density controls."""
from pathlib import Path
import sys, json
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / '.claude/science/physics-loops/neutral-composite-24h-20261018/native'))
from neutral_local_normalform import model, construct
from neutral_slow_host import lattice, host

def main():
    h0, v = model()
    h, gen = construct(h0, v, 4)
    rows = []
    for energy in sorted(set(h0)):
        ids = np.flatnonzero(h0 == energy)
        p = np.zeros(len(h0))
        p[ids] = 1
        r = np.zeros(len(h0))
        q = p == 0
        r[q] = 1 / (energy - h0[q])
        R = np.diag(r)
        P = np.diag(p)
        k1 = v[np.ix_(ids, ids)]
        es, ws = np.linalg.eigh(k1)
        null = ws[:, abs(es) < 1e-10]
        if not null.shape[1]:
            continue
        B = v @ R @ v
        A = v @ (R @ R) @ v
        k4 = v @ R @ v @ R @ v @ R @ v - (A @ P @ B + B @ P @ A) / 2
        delta = null.T @ (h[4][np.ix_(ids, ids)] - k4[np.ix_(ids, ids)]) @ null
        err = float(np.linalg.norm(delta, 2))
        _check('P9755:native_fixed_order_composite:C001', err < 1e-09)
        rows.append(dict(energy=float(energy), block_dimension=len(ids), kernel_dimension=null.shape[1], local_vs_canonical_k4_error=err))
    _check('P9755:native_fixed_order_composite:C002', [(x['energy'], x['block_dimension'], x['kernel_dimension']) for x in rows] == [(-4, 16, 16), (-2, 64, 16), (0, 96, 50), (2, 64, 16), (4, 16, 16)])
    E = -2.0
    gcc = lattice(E, 0, 0)
    gcs = (1 - E * gcc) / 2
    gss = (E * E * gcc - E) / 4
    det = gcc * gss - gcs * gcs
    _check('P9755:native_fixed_order_composite:C003', abs(det - (E * gcc - 1) / 4) < 1e-12 and abs(det) > 0.1)
    sigma = host(E)[0, 0]
    a0 = sigma / (1 + sigma)
    density_points = [dict(u=1.0, v=0.0, source=0.0), dict(u=0.5, v=0.5, source=-1.0)]
    _check('P9755:native_fixed_order_composite:C004', sigma.imag < 0 and a0.imag < 0)
    holes = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    sites = holes + [(2, 0), (-2, 0), (0, 2), (0, -2)]
    cache = {}

    def g(dx, dy):
        key = (abs(dx), abs(dy))
        if key not in cache:
            cache[key] = lattice(E, *key)
        return cache[key]
    G = np.array([[g(x - u, y - v) for u, v in sites] for x, y in sites])
    source = np.r_[np.zeros(5), np.ones(4) / 2]
    b = np.linalg.solve(G[:5, :5], G[:5] @ source)
    w = source.astype(complex)
    w[:5] -= b
    spectral = float((-w.conj() @ ((G - G.conj().T) / 2j) @ w).real)
    _check('P9755:native_fixed_order_composite:C005', abs(spectral + sigma.imag) < 2e-10)
    result = dict(status='PASS', physical_grid_sites=8, gauge_controls=rows, slow_host=dict(sigma=[sigma.real, sigma.imag], hole_determinant=[det.real, det.imag], strict_density_witness=density_points, spectral_schur_density=spectral, width_coefficient=-a0.imag / 4), scope='Finite physical gauge controls and leading host checks supplement analytical fixed-order proof. No all-order microscopic pole or empirical test.')
    out = ROOT / 'outputs/native_fixed_order_composite/result.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()

print('Assertion evaluations:',_calls,'; PASS counts distinct primary assertion groups; helper assertions are additional uncounted checks.',flush=True)
from pathlib import Path as _Path
import json as _json
(_Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(_json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
