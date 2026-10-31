#!/usr/bin/env python3
# cf1b — POST-HOC (DRIVE_BRIEF rule 3). Written AFTER cf1_funnel.py ran and AFTER seeing that
# control C3 did NOT fire. Two jobs:
#   (1) diagnose why the wrap-around control cancelled, so the reader can judge the gate's power;
#   (2) supply a control that DOES break A1 (support) and A4 (transpose diagonality), since
#       cf1_criteria.md's own reporting rule says a gate whose control does not fire is reported
#       as unsupported.
# Exact Fractions only. No numpy, no BLAS, one thread.

from fractions import Fraction
from itertools import product
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):   # cf1_funnel has no __main__ guard; silence it
    import cf1_funnel as cf1      # reuses the unedited kernel builder (cf1_funnel.py NOT edited)

print('=' * 78)
print('cf1b  POST-HOC  (designed after seeing C3 pass; labelled per rule 3)')
print('=' * 78)

# ---------------------------------------------------------------- (1) why C3 did not fire
print('\n(1) Diagnosis of control C3 (wrap-around path), d=2, L=3, M=3')
d, L, M, side = 2, 3, 3, 9
off = (L - 1) // 2
X = (1, 1)
c = tuple(X[mu] * L + off for mu in range(d))
per_y = {}
for r in product(range(L), repeat=d):
    y = tuple(X[mu] * L + r[mu] for mu in range(d))
    steps = cf1.walk(cf1.axial_steps(c, y, d, side, 'wrap'), c, d, side)
    for (lk, sg) in steps:
        z, mu = lk
        inside = all(X[i] * L <= z[i] < X[i] * L + L for i in range(d))
        zp = tuple((z[i] + (1 if i == mu else 0)) % side for i in range(d))
        inside = inside and all(X[i] * L <= zp[i] < X[i] * L + L for i in range(d))
        if not inside:
            per_y.setdefault(lk, []).append((y, sg))

outside_links = len(per_y)
net_nonzero = 0
for lk, lst in per_y.items():
    net = sum(sg for (_, sg) in lst)
    if net != 0:
        net_nonzero += 1
print(f'    out-of-block links touched by at least one path : {outside_links}')
print(f'    of those, links with NONZERO net signed count    : {net_nonzero}')
ex = next(iter(per_y.items()))
print(f'    example link {ex[0]}: contributions {[(yy, s) for (yy, s) in ex[1]]}')
print('    => the long-way excursions of the y above the root and the y below the root carry')
print('       opposite signs and are equinumerous for L odd with a CENTRAL root, so every')
print('       out-of-block coefficient cancels exactly. C3 therefore has NO POWER against A1/A4')
print('       at a central root. Reported as a control that did not fire, per cf1_criteria.md.')

# ---------------------------------------------------------------- (2) a control that does fire
print('\n(2) Control C5 (POST-HOC): root placed one site OUTSIDE its own block')


def build_outside(d, L, M):
    side = L * M
    w = Fraction(1, L ** d)
    kern = {}
    for X in product(range(M), repeat=d):
        c = tuple(X[mu] * L + ((L - 1) // 2) for mu in range(d))
        c = (X[0] * L - 1,) + c[1:]           # root pushed out of the block in coordinate 0
        row = {}
        for r in product(range(L), repeat=d):
            y = tuple(X[mu] * L + r[mu] for mu in range(d))
            for (lk, sg) in cf1.walk(cf1.axial_steps(c, y, d, side, 'axial'), c, d, side):
                row[lk] = row.get(lk, Fraction(0)) + sg * w
        kern[X] = {k: v for k, v in row.items() if v != 0}
    return kern, side


for (d, L, M) in [(2, 3, 3), (4, 3, 3)]:
    kern, side = build_outside(d, L, M)
    bad = 0
    for X, row in kern.items():
        for (z, mu) in row:
            zp = tuple((z[i] + (1 if i == mu else 0)) % side for i in range(d))
            ok = (all(X[i] * L <= z[i] < X[i] * L + L for i in range(d))
                  and all(X[i] * L <= zp[i] < X[i] * L + L for i in range(d)))
            if not ok:
                bad += 1
    owners = {}
    for X, row in kern.items():
        for lk in row:
            owners[lk] = owners.get(lk, 0) + 1
    mo = max(owners.values())
    print(f'    (d={d}, L={L}): A1 support violations = {bad:<4} -> A1 '
          f'{"FAIL" if bad else "PASS"}   (must be FAIL)')
    print(f'    (d={d}, L={L}): max owners per link   = {mo:<4} -> A4 '
          f'{"FAIL" if mo > 1 else "PASS"}   (must be FAIL)')

print('\n(3) Re-report of control C2 against its registered expectation')
r = cf1.run_full(4, 3, 3, mode='backtrack')
v, ec, er = cf1.verdicts(4, 3, r)
print(f'    registered: "A3 row sum rises". Observed l1 row = {r["A3_max_row_l1"]} '
      f'= the unperturbed {er}. A3 {v["A3"]}.')
print('    => the registered A3 expectation was WRONG: the -1/+1 pair of the back-track cancels')
print('       in the SIGNED kernel, so A3 cannot see a back-track. A7 (multiplicity '
      f'{r["A7_max_multiplicity"]}) is the only gate with power against it. Reported as a failed')
print('       pre-registration of mine, not as a passed gate.')

print('\n(4) Control C6 (POST-HOC): wrap-around path with a CORNER root')
print('    (C5 broke A1 but not A4; A4 needs two blocks to claim one link.)')
for (d, L, M) in [(2, 3, 3), (4, 3, 3)]:
    r = cf1.run_full(d, L, M, root='corner', mode='wrap')
    v, _, _ = cf1.verdicts(d, L, r)
    print(f'    (d={d}, L={L}): A1 violations = {r["A1_violations"]:<5} -> A1 {v["A1"]}'
          f'   |  max owners = {r["A4_max_owners"]:<4} -> A4 {v["A4"]}   (both must be FAIL)')
print('    With a corner root every y lies on one side, so the wrap excursions no longer')
print('    cancel in pairs: that is exactly the cancellation diagnosed in (1).')
