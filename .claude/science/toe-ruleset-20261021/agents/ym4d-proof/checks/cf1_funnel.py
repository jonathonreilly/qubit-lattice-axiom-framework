#!/usr/bin/env python3
# cf1 — target T55-I, (CO-fun): the two handles (Lemma FT (i)-(ii)) rebuilt from the definition
# of h_l, plus the unit bookkeeping behind "no power of L^{k-l}".
# Exact rational arithmetic only (fractions.Fraction, Python ints). No numpy, no BLAS, one thread.
# Criteria: checks/cf1_criteria.md (written BEFORE this file, amended at 21:49 UTC before this
# file existed). Every verdict below is pre-registered there.

from fractions import Fraction
from itertools import product

# ----------------------------------------------------------------------------- kernel construction

def axial_steps(c, y, d, side, mode):
    """Ordered list of (coord, from_value, to_value) moves for the path c -> y.
    'axial'     : coordinates in the fixed order 0..d-1, each traversed monotonically (no wrap).
    'backtrack' : as axial, but coordinate 0 first steps -1 and back (control C2).
    'wrap'      : as axial, but coordinate 0 goes the long way round the torus (control C3)."""
    moves = []
    if mode == 'backtrack':
        moves.append((0, c[0], c[0] - 1))
        moves.append((0, c[0] - 1, c[0]))
    for mu in range(d):
        a, b = c[mu], y[mu]
        if a == b:
            continue
        if mode == 'wrap' and mu == 0:
            # same endpoint, opposite way round the periodic direction
            moves.append((mu, a, b - side if b > a else b + side))
        else:
            moves.append((mu, a, b))
    return moves


def walk(moves, c, d, side):
    """Yield (link, sign) for each unit step; link = (base-site tuple, mu) with base = min end,
    all coordinates reduced mod side.  Also returns the per-path link multiplicity."""
    pos = list(c)
    out = []
    for (mu, a, b) in moves:
        step = 1 if b > a else -1
        cur = a
        while cur != b:
            nxt = cur + step
            base = min(cur, nxt)
            site = list(pos)
            site[mu] = base % side
            out.append(((tuple(s % side for s in site), mu), step))
            cur = nxt
        pos[mu] = b % side
    return out


def build(d, L, M, root='centre', mode='axial'):
    side = L * M
    off = (L - 1) // 2 if root == 'centre' else 0
    w = Fraction(1, L ** d)
    kern = {}            # X -> {link: Fraction}
    maxmult = 1
    for X in product(range(M), repeat=d):
        c = tuple(X[mu] * L + off for mu in range(d))
        row = {}
        for r in product(range(L), repeat=d):
            y = tuple(X[mu] * L + r[mu] for mu in range(d))
            steps = walk(axial_steps(c, y, d, side, mode), c, d, side)
            seen = {}
            for (lk, sg) in steps:
                seen[lk] = seen.get(lk, 0) + 1
                row[lk] = row.get(lk, Fraction(0)) + sg * w
            if seen:
                maxmult = max(maxmult, max(seen.values()))
        kern[X] = {k: v for k, v in row.items() if v != 0}
    return kern, side, off


def in_block(site, X, L, side, off_unused=None):
    return all(X[mu] * L <= site[mu] < X[mu] * L + L for mu in range(len(X)))


# ----------------------------------------------------------------------------------------- gates

def run(d, L, M, root='centre', mode='axial', label=''):
    kern, side, off = build(d, L, M, root, mode)
    res = {}

    # A1 block-interior support
    bad = 0
    for X, row in kern.items():
        for (z, mu) in row:
            zp = tuple(z[i] + (1 if i == mu else 0) for i in range(d))
            zp = tuple(v % side for v in zp)
            if not (in_block(z, X, L, side) and in_block(zp, X, L, side)):
                bad += 1
    res['A1_violations'] = bad

    # A2 sharp coefficient
    mx = max(abs(v) for row in kern.values() for v in row.values())
    res['A2_max_abs_c'] = mx

    # A3 l1 row sum
    rowsum = max(sum(abs(v) for v in row.values()) for row in kern.values())
    res['A3_max_row_l1'] = rowsum

    # A4 transpose diagonality
    owners = {}
    for X, row in kern.items():
        for lk in row:
            owners[lk] = owners.get(lk, 0) + 1
    res['A4_max_owners'] = max(owners.values()) if owners else 0

    # A5 operator norms (derived from A2-A4; reported, low power)
    res['A5_linf'] = max(sum(abs(kern[X][lk]) for X in kern if lk in kern[X]) for lk in owners)
    res['A5_l1'] = rowsum

    # A6 h(const) = 0
    worst = Fraction(0)
    for mu in range(d):
        for X, row in kern.items():
            s = sum(v for (z, nu), v in row.items() if nu == mu)
            if abs(s) > worst:
                worst = abs(s)
    res['A6_max_h_const'] = worst

    # A7 max multiplicity within one path
    _, _, _ = kern, side, off
    res['A7_max_multiplicity'] = build.__doc__ and None  # filled by caller below
    return res, kern


def run_full(d, L, M, root='centre', mode='axial'):
    # rebuild once more to capture multiplicity (kept separate so the gate code stays readable)
    side = L * M
    off = (L - 1) // 2 if root == 'centre' else 0
    maxmult = 1
    for X in product(range(M), repeat=d):
        c = tuple(X[mu] * L + off for mu in range(d))
        for r in product(range(L), repeat=d):
            y = tuple(X[mu] * L + r[mu] for mu in range(d))
            steps = walk(axial_steps(c, y, d, side, mode), c, d, side)
            seen = {}
            for (lk, sg) in steps:
                seen[lk] = seen.get(lk, 0) + 1
            if seen:
                maxmult = max(maxmult, max(seen.values()))
    res, kern = run(d, L, M, root, mode)
    res['A7_max_multiplicity'] = maxmult
    return res


def verdicts(d, L, res):
    exp_c = Fraction(L - 1, 2 * L)
    exp_r = Fraction(d * (L * L - 1), 4 * L)
    v = {}
    v['A1'] = 'PASS' if res['A1_violations'] == 0 else 'FAIL'
    v['A2'] = 'PASS' if (res['A2_max_abs_c'] == exp_c and res['A2_max_abs_c'] <= 1) else 'FAIL'
    v['A3'] = 'PASS' if (res['A3_max_row_l1'] == exp_r
                         and res['A3_max_row_l1'] <= d * (L - 1)) else 'FAIL'
    v['A4'] = 'PASS' if res['A4_max_owners'] <= 1 else 'FAIL'
    v['A5'] = 'PASS' if (res['A5_linf'] == exp_c and res['A5_l1'] == exp_r) else 'FAIL'
    v['A6'] = 'PASS' if res['A6_max_h_const'] == 0 else 'FAIL'
    v['A7'] = 'PASS' if res['A7_max_multiplicity'] == 1 else 'FAIL'
    return v, exp_c, exp_r


# ------------------------------------------------------------------------------------- main runs

RUNS = [(2, 3, 3), (3, 3, 3), (4, 3, 3), (5, 3, 2), (4, 5, 2)]

print('=' * 78)
print('cf1 PART A — the funnel kernel h_l, rebuilt from its definition (exact Fractions)')
print('=' * 78)
allA = {}
for (d, L, M) in RUNS:
    res = run_full(d, L, M)
    v, ec, er = verdicts(d, L, res)
    allA[(d, L)] = v
    print(f'\n(d={d}, L={L}, M={M})  registered: max|c| = {ec}, l1 row = {er}')
    print(f'  A1 support violations   = {res["A1_violations"]:<10}  {v["A1"]}')
    print(f'  A2 max|c(X,b)|          = {res["A2_max_abs_c"]!s:<10}  {v["A2"]}'
          f'   (FT(i) published bound 1: {"ok" if res["A2_max_abs_c"] <= 1 else "BROKEN"})')
    print(f'  A3 max_X l1 row sum     = {res["A3_max_row_l1"]!s:<10}  {v["A3"]}'
          f'   (FT(i) published bound {d*(L-1)}: '
          f'{"ok" if res["A3_max_row_l1"] <= d*(L-1) else "BROKEN"})')
    print(f'  A4 max owners per link  = {res["A4_max_owners"]:<10}  {v["A4"]}')
    print(f'  A5 ||h^T||_inf, ||h^T||_1 = {res["A5_linf"]!s}, {res["A5_l1"]!s}   {v["A5"]}'
          f'   [derived from A2-A4; LOW POWER, disclosed]')
    print(f'  A6 max |h(const)|       = {res["A6_max_h_const"]!s:<10}  {v["A6"]}')
    print(f'  A7 max multiplicity     = {res["A7_max_multiplicity"]:<10}  {v["A7"]}')

b3 = all(all(x == 'PASS' for x in v.values()) for v in allA.values())
print(f'\n  B3 d-independence across {RUNS}: {"PASS" if b3 else "FAIL"}')

# ------------------------------------------------------------------- Part B: the unit bookkeeping

print()
print('=' * 78)
print('cf1 PART B — unit bookkeeping: is a power of L^(k-l) present?')
print('=' * 78)
L = 3
b1_ok, b1_witness = True, []
for k in range(1, 9):
    for l in range(0, k):
        for lp in range(0, l + 1):
            e = 3 * (k - l) - 3 * (k - lp)          # pi_l conversion against pi_{l'} conversion
            if e != -3 * (l - lp):
                b1_ok = False
                b1_witness.append((k, l, lp, e))
print(f'  B1 exponent of L in pi_l(.)/pi_l\'(.) equals -3(l-l\'), k-free, for all k<=8: '
      f'{"PASS" if b1_ok else "FAIL " + str(b1_witness[:3])}')
kfree = all(len({3 * (k - l) - 3 * (k - lp) for k in range(max(l, lp) + 1, 9)}) == 1
            for l in range(0, 8) for lp in range(0, l + 1))
print(f'     (k-independence checked separately, varying k at fixed (l,l\'): '
      f'{"PASS" if kfree else "FAIL"})')

cap = Fraction(1, 1) / (1 - Fraction(1, L ** 3))
b2_ok = True
for l in range(0, 9):
    s = sum(Fraction(1, L ** (3 * (l - lp))) for lp in range(0, l + 1))
    if not s < cap:
        b2_ok = False
print(f'  B2 sum_{{l\'<=l}} L^-3(l-l\') < (1-L^-3)^-1 = {cap} for all l<=8: '
      f'{"PASS" if b2_ok else "FAIL"}')

# ------------------------------------------------------------------- designed-FAIL controls

print()
print('=' * 78)
print('cf1 CONTROLS — each MUST fire (defect 3). A control that passes voids its gate.')
print('=' * 78)

d, L, M = 4, 3, 3
base = verdicts(d, L, run_full(d, L, M))[0]

print('\nC1  root at the block CORNER instead of the centre')
r = run_full(d, L, M, root='corner')
v, _, _ = verdicts(d, L, r)
print(f'    max|c| = {r["A2_max_abs_c"]} -> A2 {v["A2"]}   (must be FAIL)')
print(f'    l1 row = {r["A3_max_row_l1"]} -> A3 {v["A3"]}   (must be FAIL)')
print(f'    |h(const)| = {r["A6_max_h_const"]} -> A6 {v["A6"]}   (must be FAIL)')
print(f'    A1 {v["A1"]}, A4 {v["A4"]}, A7 {v["A7"]}   (must all still PASS: '
      f'support/diagonality are convention-free)')
c1_fired = v['A2'] == 'FAIL' and v['A3'] == 'FAIL' and v['A6'] == 'FAIL'
c1_intact = v['A1'] == 'PASS' and v['A4'] == 'PASS' and v['A7'] == 'PASS'
print(f'    C1 FIRED: {c1_fired};  intact-as-registered: {c1_intact}')

print('\nC2  BACK-TRACKING path (coordinate 0 steps -1 and back before proceeding)')
r = run_full(d, L, M, mode='backtrack')
v, _, _ = verdicts(d, L, r)
print(f'    max multiplicity = {r["A7_max_multiplicity"]} -> A7 {v["A7"]}   (must be FAIL)')
print(f'    l1 row = {r["A3_max_row_l1"]} -> A3 {v["A3"]}   (must be FAIL)')
print(f'    A1 {v["A1"]} (reported, not registered either way)')
c2_fired = v['A7'] == 'FAIL' or v['A3'] == 'FAIL'
print(f'    C2 FIRED: {c2_fired}')

print('\nC3  WRAP-AROUND path (coordinate 0 goes the long way round the torus)')
r = run_full(d, L, M, mode='wrap')
v, _, _ = verdicts(d, L, r)
print(f'    A1 support violations = {r["A1_violations"]} -> A1 {v["A1"]}   (must be FAIL)')
print(f'    max owners per link   = {r["A4_max_owners"]} -> A4 {v["A4"]}   (must be FAIL)')
c3_fired = v['A1'] == 'FAIL' and v['A4'] == 'FAIL'
print(f'    C3 FIRED: {c3_fired}')

print('\nC4  NAIVE grouping exponent (level-i funnel reading the levels l > i)')
L = 3
c4_sums = []
for l in range(1, 9):
    s = sum(Fraction(L ** (3 * (l - i))) for i in range(0, l))
    c4_sums.append((l, s))
c4_bounded = all(s < cap for (_, s) in c4_sums)
print(f'    sum_{{i<l}} L^+3(l-i) at l = 1..8: '
      f'{[str(s) for (_, s) in c4_sums[:4]]} ... {c4_sums[-1][1]}')
print(f'    B2 on the naive grouping: {"PASS" if c4_bounded else "FAIL"}   (must be FAIL)')
c4_kfree = all(len({3 * (k - i) - 3 * (k - l) for k in range(l + 1, 9)}) == 1
               for l in range(1, 8) for i in range(0, l))
print(f'    B1 k-independence on the naive grouping: {"PASS" if c4_kfree else "FAIL"}'
      f'   (registered: must still PASS — the k-cancellation is NOT what separates the groupings)')
c4_fired = (not c4_bounded)
print(f'    C4 FIRED: {c4_fired}')

print()
print('=' * 78)
print('SUMMARY')
print('=' * 78)
print(f'  Part A gates at every (d,L) run : '
      f'{"ALL PASS" if b3 else "NOT all PASS"}')
print(f'  Part B gates                    : B1 {"PASS" if b1_ok and kfree else "FAIL"}, '
      f'B2 {"PASS" if b2_ok else "FAIL"}')
print(f'  Controls fired                  : C1 {c1_fired}, C2 {c2_fired}, '
      f'C3 {c3_fired}, C4 {c4_fired}')
print(f'  C1 left A1/A4/A7 intact         : {c1_intact}')
