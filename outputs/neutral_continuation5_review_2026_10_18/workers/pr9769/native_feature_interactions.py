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
from fractions import Fraction as F
from itertools import permutations
import json, random
ROOT = Path(__file__).resolve().parents[1]

def boundary(S):
    ps = {(x - dx, y - dy) for x, y in S for dx in [0, 1] for dy in [0, 1]}
    return {p for p in ps if sum(((p[0] + dx, p[1] + dy) in S for dx in [0, 1] for dy in [0, 1])) % 2}
edges = [(0, 1, 'X'), (2, 3, 'X'), (0, 2, 'Y'), (1, 3, 'Y')]
coeff = []
for initial in range(16):
    total = F(0)
    for order in permutations(range(4)):
        state = initial
        v = F(1)
        for k, idx in enumerate(order):
            a, b, axis = edges[idx]
            v *= -1 if axis == 'X' else (-1) ** ((state >> a & 1) + (state >> b & 1))
            state ^= 1 << a | 1 << b
            if k < 3:
                v /= -4 * (state ^ initial).bit_count()
        _check('P9769:C001', state == initial)
        total += v
    _check('P9769:C002', total == -F((-1) ** initial.bit_count(), 128))
    coeff.append(str(total))
rect = []
for nx in range(1, 9):
    for ny in range(1, 9):
        S = {(x, y) for x in range(nx) for y in range(ny)}
        _check('P9769:C003', len(boundary(S)) == 4)
        rect.append(dict(nx=nx, ny=ny, area=nx * ny, tension_over_Jlambda4='1/16', H0_energy_over_J=4 * nx * ny))
a = {(0, 0), (2, 0)}
b = {(0, 1), (2, 1)}
_check('P9769:C004', len(boundary(a) & boundary(b)) == 4)
rng = random.Random(212)
checks = 0
for _ in range(200):
    sites = [(x, y) for x in range(4) for y in range(4)]
    rng.shuffle(sites)
    a = set(sites[:rng.randrange(1, 7)])
    b = set(sites[8:8 + rng.randrange(1, 7)])
    ps = boundary(a) | boundary(b)
    sign = {p: rng.choice([-1, 1]) for p in ps}
    delta = lambda S: 2 * sum((sign[p] for p in boundary(S)))
    _check('P9769:C005', delta(a ^ b) - delta(a) - delta(b) == -4 * sum((sign[p] for p in boundary(a) & boundary(b))))
    checks += 1
basis = [{(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)} for x in range(3) for y in range(3)]
walsh = 0
for mask in range(1, 512):
    S = set()
    for k, Q in enumerate(basis):
        if mask >> k & 1:
            S ^= Q
    _check('P9769:C006', all((sum((x == xx for x, y in S)) % 2 == 0 for xx in range(4))) and all((sum((y == yy for x, y in S)) % 2 == 0 for yy in range(4))))
    counts = []
    for nx, ny in [(8, 9), (10, 13), (14, 11)]:
        count = 0
        for dx in range(-4, nx + 1):
            for dy in range(-4, ny + 1):
                T = {(x + dx, y + dy) for x, y in S}
                changed = sum((0 <= x < nx and 0 <= y < ny for x, y in T)) % 2
                if changed:
                    _check('P9769:C007', min((x for x, y in T)) < 0 <= max((x for x, y in T)) or min((x for x, y in T)) < nx <= max((x for x, y in T)))
                    _check('P9769:C008', min((y for x, y in T)) < 0 <= max((y for x, y in T)) or min((y for x, y in T)) < ny <= max((y for x, y in T)))
                count += changed
        counts.append(count)
    _check('P9769:C009', len(set(counts)) == 1)
    walsh += 1
result = dict(status='bounded-support', native_square_coefficients=coeff, rectangle_checks=rect, background_shape_checks=checks, all_even_4x4_walsh_masks=walsh, scope='Exact coefficient and combinatorial checks; no eigenmode, binding, full-series or observation claim')
p = ROOT / 'outputs/native_feature_interactions/result.json'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))

(Path(__file__).resolve().parents[1]/'assertion-groups.json').write_text(json.dumps({'groups':sorted(_groups),'evaluations':_calls})+'\n')
