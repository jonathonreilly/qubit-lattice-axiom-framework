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
import json, itertools, numpy as np
ROOT = Path(__file__).resolve().parents[1]

def walls(s):
    return sum(((x, y, z - 1) not in s for x, y, z in s)) + sum(((x, y, z + 1) not in s for x, y, z in s))

def cex(s):
    cols = {(x, y) for x, y, z in s}
    return sum((-2 for x, y in cols for z in range(-3, 9) if ((x, y, z) in s) != ((x, y, z + 2) in s)))
for bits in range(256):
    s = {(c, 0, z) for c in range(2) for z in range(4) if bits >> 4 * c + z & 1}
    w = {(c, 0, z) for c in range(2) for z in range(-1, 4) if ((c, 0, z) in s) != ((c, 0, z + 1) in s)}
    A = sum(((c, y, z + 1) in w for c, y, z in w))
    _check('P9773:C001', cex(s) == -4 * walls(s) + 4 * A)
F = {(0, 0), (1, 0), (0, 1), (1, 1)}
s = {(x, y, z) for x, y in F for z in range(5)}
path = []

def flip(a, b):
    global s
    t = s ^ {a, b}
    _check('P9773:C002', walls(t) == walls(s) == 8)
    _check('P9773:C003', abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 and a[2] == b[2])
    amp = -1 if a[0] != b[0] or (a in s) != (b in s) else 1
    path.append(dict(a=a, b=b, amplitude=amp, delta_C=cex(t) - cex(s)))
    s = t
for z in range(4, 0, -1):
    for y in [0, 1]:
        flip((0, y, z), (1, y, z))
_check('P9773:C004', cex(s) == -16 and any((abs(row['delta_C']) == 8 for row in path)))
for a, d, n in [((0, 0, 0), (-1, 0, 0), 5), ((1, 0, 0), (1, 0, 0), 5), ((0, 1, 0), (0, 1, 0), 5), ((1, 1, 0), (1, 0, 0), 5), ((6, 1, 0), (0, 1, 0), 5)]:
    for _ in range(n):
        b = tuple((a[j] + d[j] for j in range(3)))
        flip(a, b)
        a = b
_check('P9773:C005', min((sum((abs(a[j] - b[j]) for j in range(3))) for a, b in itertools.combinations(s, 2))) > 1)
rows = []
theta = np.arccos(1 / np.sqrt(3))
e = -4 * np.cos(theta)
for M in [16, 32, 64, 128]:
    x = np.arange(1, M + 1)
    v = np.zeros((M + 2, M + 2), complex)
    u = np.sin(np.pi * x / (M + 1)) * np.exp(1j * theta * x)
    v[1:-1, 1:-1] = np.outer(u, u)
    v /= np.linalg.norm(v)
    h = np.zeros_like(v)
    h[1:] -= v[:-1]
    h[:-1] -= v[1:]
    h[:, 1:] -= v[:, :-1]
    h[:, :-1] -= v[:, 1:]
    d = h - e * v
    res = np.linalg.norm(d)
    mean = np.vdot(v, d).real
    four = np.sqrt(4 * res ** 2 + 12 * mean ** 2)
    _check('P9773:C006', four * M < 50)
    rows.append(dict(M=M, single_residual=float(res), four_product_residual=float(four), energy=4 * e))
_check('P9773:C007', rows[-1]['four_product_residual'] < rows[0]['four_product_residual'] / 6)
for q in [0.01, 0.001]:
    _check('P9773:C008', abs(16 / np.sqrt(3) * (1 - np.cos(q / 2)) / q ** 2 - 2 / np.sqrt(3)) < 3e-06)
out = dict(status='bounded-support', identity_configurations=256, native_path=path, final_defects=sorted(s), free_packet_controls=rows, relative_kinetic=2 / np.sqrt(3), length_prefactor=(32 / np.sqrt(3)) ** (1 / 3), energy_prefactor=(1 / (128 * np.sqrt(3))) ** (1 / 3), scope='K1 continuum/contact source and conditional scales; no radiation width or finite particle theorem')
p = ROOT / 'outputs/native_finite_feature_collision/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
