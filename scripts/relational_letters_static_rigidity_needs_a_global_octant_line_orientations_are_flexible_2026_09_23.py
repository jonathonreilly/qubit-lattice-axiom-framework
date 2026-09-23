#!/usr/bin/env python3
"""Static relational rigidity needs a global octant: orienting each site, or
each lattice line, leaves the seven letters flexible.

Open PR 8743 proved that under the static reading of open PR 8691 (back
neighbours x - e_i, forward neighbours x + e_i) every static record of the
seven letters (1, 2, 4) x 360/7 is a spiral, and that letting each core
site choose its own octant loses rigidity (15024 records on the core of
side 2).  Between the two sits a reading that orients each lattice line: a
core site uses the octant given by the orientations of its three lines.
  * A global octant (every line along an axis oriented alike) gives exactly
    the 12 spirals aligned with it, for each of the 8 octants; the 4
    opposite pairs give 48 distinct records.
  * Over all 4096 orientation fields of the 12 lines through the core of
    side 2, the records number 11136, of which 48 are spirals; 1300 fields
    admit records, and one field that is not a global octant admits 108.
  * Every line-field record is a per-site-octant record (the 15024 of open
    PR 8743), and every global-octant record is a line-field record.
So the reading must supply one orientation per axis for the whole core;
orientations attached to sites or to lines are not enough.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * the seven letters in the planar form (residues modulo 7); at a core site
    with octant sigma the back neighbours are x - sigma_i e_i and the
    forward neighbours x + sigma_i e_i, and the back differences and the
    forward differences must each be a common-sign permutation of the
    angles (open PR 8743);
  * the side-4 box with its core of side 2 and one core value fixed (a
    global rotation); values outside the core are free;
  * the 12 lines through the core, 4 along each axis; a line-orientation
    field gives each line a sign, and a core site takes its octant from its
    three lines;
  * budget guards: a search stops at 5000 records (20000 for the per-site
    search) or 100000 steps, and all searches together stop after
    1700000000 comparisons with a triple; the true run makes about
    564000000 and at most 27062 steps; a stopped search returns None,
    which fails its check;
  * exact modular arithmetic.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
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

print("B. one orientation per lattice line is not enough")
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

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
