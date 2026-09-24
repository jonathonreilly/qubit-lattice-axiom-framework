#!/usr/bin/env python3
"""Referee for J:derive:tight-sibling-vacuity:a1.

The one-set is rebuilt from the ten marks. Rooted values are minima of
E - c|A| over downward-closed sets, computed by a level bitmask sweep and,
separately, by an integer program. Neither routine is the author's.
"""
import itertools
import sys
from fractions import Fraction as Fr

FAILS = []
MARKS = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 2, 1), (1, 0, 2), (2, 1, 0), (1, 1, 3), (1, 3, 1), (3, 1, 1)}
AXES = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


def pred(x):
    return [(x[0] + a, x[1] + b, x[2] + c) for a, b, c in AXES]


def level(x):
    return x[0] + x[1] + x[2]


def ones_in(lo, hi):
    ones = set()
    for total in range(3 * lo, 3 * hi + 1):
        for x in itertools.product(range(lo, hi + 1), repeat=3):
            if level(x) != total:
                continue
            n = sum(p in ones for p in pred(x))
            if n >= 2 or x in MARKS:
                ones.add(x)
    return ones


def kind_of(x, ones):
    n = sum(p in ones for p in pred(x))
    return "seed" if n == 0 else ("amp" if n == 1 else "proc")


def sweep(z, ones, c=Fr(1), restrict=True, need_amp=False):
    """Minimum E - c|A| among downward-closed one-sets that contain z."""
    top = level(z)
    by = {}
    for x in ones:
        if restrict and level(x) > top:
            continue
        by.setdefault(level(x), []).append(x)
    levels = sorted(by)
    for sites in by.values():
        sites.sort()

    def weight(x):
        k = kind_of(x, ones)
        return Fr(0) if k == "seed" else (Fr(1) if k == "proc" else -c)

    # cost of a mask, and whether it already contains an amplified site
    start = by[levels[0]]
    state = {}
    for mask in range(1 << len(start)):
        chosen = [start[i] for i in range(len(start)) if mask >> i & 1]
        if any(kind_of(x, ones) != "seed" for x in chosen):
            continue
        state[(mask, any(kind_of(x, ones) == "amp" for x in chosen))] = sum(weight(x) for x in chosen)
    prev_sites = start
    prev_level = levels[0]
    for nxt in levels[1:]:
        here = by[nxt]
        gap = nxt != prev_level + 1
        nxt_state = {}
        for (mask, amp), cost in state.items():
            prev = {prev_sites[i] for i in range(len(prev_sites)) if mask >> i & 1}
            for mask2 in range(1 << len(here)):
                chosen = [here[i] for i in range(len(here)) if mask2 >> i & 1]
                if gap and chosen:
                    continue
                if any(kind_of(x, ones) != "seed" and not any(p in prev for p in pred(x)) for x in chosen):
                    continue
                if nxt == top and z not in chosen:
                    continue
                amp2 = amp or any(kind_of(x, ones) == "amp" for x in chosen)
                key = (mask2, amp2)
                val = cost + sum(weight(x) for x in chosen)
                if key not in nxt_state or val < nxt_state[key]:
                    nxt_state[key] = val
        state = nxt_state
        prev_sites, prev_level = here, nxt
        if not state:
            return None
    best = None
    zbit = prev_sites.index(z)
    for (mask, amp), cost in state.items():
        if mask >> zbit & 1 == 0:
            continue
        if need_amp and not amp:
            continue
        if best is None or cost < best:
            best = cost
    return best


def ilp_min(z, ones, scale_e, scale_a):
    """Min scale_e * E + scale_a * A, integers, over the same closed sets. scale_a is negative for a budget."""
    import numpy as np
    from scipy.optimize import LinearConstraint, Bounds, milp

    nodes = [x for x in ones if level(x) <= level(z)]
    idx = {x: i for i, x in enumerate(nodes)}
    n = len(nodes)
    w = []
    for x in nodes:
        k = kind_of(x, ones)
        w.append(0 if k == "seed" else (scale_e if k == "proc" else scale_a))
    rows, lo, hi = [], [], []
    for x in nodes:
        if kind_of(x, ones) == "seed":
            continue
        row = np.zeros(n)
        row[idx[x]] = 1
        for p in pred(x):
            if p in idx:
                row[idx[p]] -= 1
        rows.append(row)
        lo.append(-np.inf)
        hi.append(0)
    row = np.zeros(n)
    row[idx[z]] = 1
    rows.append(row)
    lo.append(1)
    hi.append(1)
    ans = milp(c=np.array(w, float), constraints=LinearConstraint(np.vstack(rows), lo, hi),
               integrality=np.ones(n), bounds=Bounds(0, 1))
    if not ans.success:
        return None
    return int(round(ans.fun))


small = ones_in(0, 3)
big = ones_in(-2, 6)
ok("R1", small == big and len(small) == 37 and all(0 <= t <= 3 for x in small for t in x),
   f"the ten marks give the same 37 one-sites in [0,3]^3 and [-2,6]^3 ({len(small)}, {len(big)})")

ones = small
kinds = {x: kind_of(x, ones) for x in ones}
sizes = [sum(level(x) == t for x in ones) for t in range(10)]
ns = sum(v == "seed" for v in kinds.values())
na = sum(v == "amp" for v in kinds.values())
np_ = sum(v == "proc" for v in kinds.values())
z = (3, 3, 3)
preds = [p for p in pred(z) if p in ones]
r2 = (ns, na, np_) == (1, 9, 27) and sizes == [1, 3, 3, 4, 3, 6, 7, 6, 3, 1]
r2 = r2 and kinds[z] == "proc" and preds == [(2, 3, 3), (3, 2, 3), (3, 3, 2)] and all(kinds[p] == "proc" for p in preds)
ok("R2", r2, f"1 seed, 9 amplified, 27 processed; levels {sizes}; 333 and its three predecessors are processed")

vals = {t: sweep(t, ones) for t in preds + [z]}
ilp = {t: ilp_min(t, ones, 1, -1) for t in preds + [z]}
r3 = all(vals[p] == 0 for p in preds) and vals[z] == 1 and all(ilp[t] == vals[t] for t in vals)
ok("R3", r3, f"rooted values { {t: int(v) for t, v in vals.items()} }; the integer program agrees. (Q) and (H) fail at 333")

# c* : min (9E - 10A) >= 0 and some closed set has 9E = 10A
gap = ilp_min(z, ones, 9, -10)
at_one = sweep(z, ones, c=Fr(1), need_amp=True)
at_109 = sweep(z, ones, c=Fr(10, 9), need_amp=True)
at_119 = sweep(z, ones, c=Fr(11, 9), need_amp=True)
lifted = sweep(z, ones, c=Fr(10, 9), restrict=False, need_amp=True)
r4 = gap == 0 and at_one == 1 and at_109 == 0 and at_119 == -1 and lifted == 0
ok("R4", r4, f"9E-10A minimum is {gap}; E-A = {at_one}, E-(10/9)A = {at_109}, E-(11/9)A = {at_119}; unrestricted 10/9 still 0. So c*(eta,333)=10/9")

survivors = []
not_proc = 0
for m in sorted(MARKS - {(0, 0, 0)}):
    o2 = ones_in(0, 3)
    # rebuild without m
    saved = set(MARKS)
    trial = saved - {m}
    # local rebuild
    o2 = set()
    for total in range(0, 10):
        for x in itertools.product(range(4), repeat=3):
            if level(x) != total:
                continue
            n = sum(p in o2 for p in pred(x))
            if n >= 2 or x in trial:
                o2.add(x)
    if z not in o2 or kind_of(z, o2) != "proc":
        not_proc += 1
        continue
    p2 = [p for p in pred(z) if p in o2 and kind_of(p, o2) == "proc"]
    if len(p2) >= 2 and all(sweep(p, o2) == 0 for p in p2) and sweep(z, o2) > 0:
        survivors.append(m)
r5 = not_proc == 9 and not survivors
ok("R5", r5, f"dropping any one of the nine non-seed marks makes 333 not processed ({not_proc}/9); no one-mark deletion keeps the counterexample")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - the ten-mark realization has 37 one-sites, the three predecessors of 333 are tight, v(333)=1, and c*(eta,333)=10/9.")
print("HIT: confirmed - (Q) is false at M={000,001,010,100,021,102,210,113,131,311}: 333 is processed, its three processed 1-predecessors have rooted value 0, and v(333)=1, so the tight-sibling lemma and (H) fail; the same root has c*=10/9 by an independent bitmask sweep and an integer program, with and without the level cap; every non-seed mark is necessary for 333 to be processed.")
