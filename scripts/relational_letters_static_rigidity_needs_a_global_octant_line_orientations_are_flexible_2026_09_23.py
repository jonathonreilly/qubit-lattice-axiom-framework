#!/usr/bin/env python3
"""Finite orientation-field contrasts for seven-value core rigidity.

Only the declared seven-value planar support model and side-two core are exhausted. Values outside the core are free. No larger-window classification, unique necessary orientation supply, or physical interpretation is established.

See the companion note for proofs and exact execution scope.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
from itertools import permutations, product

RESULTS = []
WORK, WORK_CAP = [0], 1700000000


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


TH, M = (1, 2, 4), 7
T = [tuple((s * TH[p[i]]) % M for i in range(3)) for p in permutations(range(3)) for s in (1, -1)]
L = 4
CORE = sorted(product(range(1, L - 1), repeat=3), key=lambda x: (sum(x), x))
CS = set(CORE)
sh = lambda x, i, s: tuple(x[k] + s * (k == i) for k in range(3))
NBRS = {x: [y for i in range(3) for s in (1, -1) for y in [sh(x, i, s)] if y in CS] for x in CORE}
LINES = sorted({(i, tuple(x[k] for k in range(3) if k != i)) for x in CORE for i in range(3)})
LIDX = {l: j for j, l in enumerate(LINES)}
LINE_OF = {(x, i): LIDX[(i, tuple(x[k] for k in range(3) if k != i))] for x in CORE for i in range(3)}


def records(octant_of, cap=5000, step_cap=100000):
    """Core records when core site x uses the octant octant_of(x); None if a budget binds."""
    sg = {x: octant_of(x) for x in CORE}

    def ok_at(z, A):
        WORK[0] += len(T)
        if WORK[0] > WORK_CAP:
            raise OverflowError
        for side in (-1, 1):
            known = {}
            for i in range(3):
                y = sh(z, i, side * sg[z][i])
                if y in CS:
                    if y not in A:
                        return True
                    known[i] = (side * (A[y] - A[z])) % M
            if not any(all(t[i] == v for i, v in known.items()) for t in T):
                return False
        return True

    out, steps = [], [0]

    def rec(idx, A):
        steps[0] += 1
        if steps[0] > step_cap or len(out) >= cap:
            raise OverflowError
        if idx == len(CORE):
            out.append(tuple(A[x] for x in CORE))
            return
        x = CORE[idx]
        for v in ([0] if idx == 0 else range(M)):
            A[x] = v
            if ok_at(x, A) and all(ok_at(z, A) for z in NBRS[x] if z in A):
                rec(idx + 1, A)
            del A[x]

    try:
        rec(0, {})
    except OverflowError:
        return None
    return out


def per_site_records(cap=20000, step_cap=100000):
    """Core records when every core site may use any octant of its own."""

    def ok_at(z, A):
        WORK[0] += 8 * len(T)
        if WORK[0] > WORK_CAP:
            raise OverflowError
        for sg in product((1, -1), repeat=3):
            good = True
            for side in (-1, 1):
                known = {i: (side * (A[y] - A[z])) % M for i in range(3) for y in [sh(z, i, side * sg[i])] if y in CS and y in A}
                if not any(all(t[i] == v for i, v in known.items()) for t in T):
                    good = False
                    break
            if good:
                return True
        return False

    out, steps = [], [0]

    def rec(idx, A):
        steps[0] += 1
        if steps[0] > step_cap or len(out) >= cap:
            raise OverflowError
        if idx == len(CORE):
            out.append(tuple(A[x] for x in CORE))
            return
        x = CORE[idx]
        for v in ([0] if idx == 0 else range(M)):
            A[x] = v
            if ok_at(x, A) and all(ok_at(z, A) for z in NBRS[x] if z in A):
                rec(idx + 1, A)
            del A[x]

    try:
        rec(0, {})
    except OverflowError:
        return None
    return out


def diffs(vals):
    A = dict(zip(CORE, vals))
    x0 = CORE[0]
    return tuple((A[sh(x0, i, 1)] - A[x0]) % M for i in range(3))


def is_spiral(vals):
    A = dict(zip(CORE, vals))
    x0 = CORE[0]
    d = diffs(vals)
    return all((A[x] - A[x0] - sum(d[i] * (x[i] - x0[i]) for i in range(3))) % M == 0 for x in CORE)


def aligned(d, sigma):
    """d is s sigma (a permutation of the angles) for a common sense s."""
    return any(tuple((s * sigma[i] * t[i]) % M for i in range(3)) == d for s in (1, -1)
               for t in [tuple(TH[p[i]] for i in range(3)) for p in permutations(range(3))])


print("A. a global octant gives exactly the aligned spirals")
glob, glob_ok = set(), True
for sigma in product((1, -1), repeat=3):
    r = records(lambda x, s=sigma: s)
    glob_ok = glob_ok and r is not None and len(r) == 12 and all(is_spiral(v) and aligned(diffs(v), sigma) for v in r)
    glob |= set(r or ())
check("each of the 8 global octants gives exactly the 12 spirals aligned with it; the 4 opposite pairs give 48 records",
      glob_ok and len(glob) == 48 and all(is_spiral(v) for v in glob),
      "the fixed octant of open PR 8743 is the octant (+, +, +)")

print("B. arbitrary line fields do not guarantee rigidity on this core")
union, fields_with, best, best_field, complete = set(), 0, 0, None, True
for field in product((1, -1), repeat=len(LINES)):
    r = records(lambda x, f=field: tuple(f[LINE_OF[(x, i)]] for i in range(3)))
    if r is None:
        complete = False
        break
    if r:
        fields_with += 1
    if len(r) > best:
        best, best_field = len(r), field
    union |= set(r)
n_spirals = sum(is_spiral(v) for v in union)
global_field = best_field is not None and all(len({best_field[LIDX[l]] for l in LINES if l[0] == i}) == 1 for i in range(3))
check("over all 4096 orientation fields of the 12 lines through the core, the records number 11136, only 48 of them spirals",
      complete and len(union) == 11136 and n_spirals == 48 and fields_with == 1300 and best == 108 and not global_field,
      f"{fields_with} fields admit records; the largest count on one field is {best}, on a field that is not a global "
      f"octant (lines flipped against (+, +, +): {sum(1 for l in LINES if best_field and best_field[LIDX[l]] == -1)} of 12)")

print("C. sites, lines and a global octant are nested")
ps = per_site_records()
check("every line-field record is a per-site-octant record, and every global-octant record is a line-field record",
      ps is not None and len(ps) == 15024 and union <= set(ps) and glob <= union,
      f"per-site octants: {len(ps) if ps else 'cap'} records (open PR 8743); line fields: {len(union)}; global octants: "
      f"{len(glob)}")

print('per_element: Exact arithmetic tests the declared angle, star or linear-system objects; no physical qubit encoding is inferred.')
print('per_site: Site checks cover only the explicit finite boxes, tori and samples printed above; boundary freedoms remain as stated in the note.')
print('per_mode: Analytic mode or symmetry arguments are conditional source proofs; finite runner cases alone do not prove untested universality.')
print('per_block: This is one bounded support result in a supplied relational record model, with the controls and counts declared above.')
print('lattice_wide: No physical infinite-volume conclusion is inferred; any whole-lattice or all-size statement is limited to the explicit source theorem hypotheses.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
