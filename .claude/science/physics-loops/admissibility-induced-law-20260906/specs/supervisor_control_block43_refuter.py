#!/usr/bin/env python3
"""Block 43 refuting pass: machinery disjoint from the runner's (enumeration of whole paths; an explicit relaxation on a torus).

W1  mean-square reach and tail shares of the simple walk by enumeration of all 6^s paths, s <= 7
W2  the lazy walk (hop probability 1/12 per neighbour, stay 1/2) by enumeration of all weighted paths, s <= 5: mean-square reach s/2, tail share at most (s/2)/R^2
W3  the slowest mode of the 6^3 torus relaxed tick by tick on all 216 sites: amplitude (1 - h E_min)^n, and its half-life against the bound 1/(2 h E_min)
W4  the longest-lived mode with a mass term: half-life against 1/(4 h m^2)
Exact arithmetic only.
"""
import sys
from fractions import Fraction as F
from itertools import product

STEPS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
fails = 0


def report(tag, ok, msg):
    global fails
    fails += 0 if ok else 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


def w1():
    ok = True
    for s in range(1, 8):
        msd = 0
        beyond = {r: 0 for r in (2, 3, 4)}
        for path in product(range(6), repeat=s):
            x = [0, 0, 0]
            for k in path:
                st = STEPS[k]
                x[0] += st[0]; x[1] += st[1]; x[2] += st[2]
            d2 = x[0] ** 2 + x[1] ** 2 + x[2] ** 2
            msd += d2
            for r in beyond:
                beyond[r] += d2 >= r * r
        ok = ok and msd == s * 6 ** s and all(F(beyond[r], 6 ** s) <= F(s, r * r) for r in beyond)
    report("W1", ok, "all 6^s paths of the simple walk, s = 1..7: mean-square reach exactly s; the share at distance 2, 3, 4 or more never exceeds s/R^2")


def w2():
    ok = True
    moves = [(st, F(1, 12)) for st in STEPS] + [((0, 0, 0), F(1, 2))]
    for s in range(1, 6):
        msd, tot = F(0), F(0)
        far = F(0)
        for path in product(range(7), repeat=s):
            x = [0, 0, 0]
            w = F(1)
            for k in path:
                st, pw = moves[k]
                x[0] += st[0]; x[1] += st[1]; x[2] += st[2]
                w *= pw
            d2 = x[0] ** 2 + x[1] ** 2 + x[2] ** 2
            msd += w * d2
            tot += w
            far += w * (d2 >= 4)
        ok = ok and tot == 1 and msd == F(s, 2) and far <= F(s, 2) / 4
    report("W2", ok, "the lazy walk with hop probability 1/12, all weighted paths, s = 1..5: weight 1, mean-square reach s/2 = 6 h s, share at distance 2 or more at most (s/2)/4")


def w3():
    L = 6
    cosv = (F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2))
    sites = list(product(range(L), repeat=3))
    ok = True
    lives = []
    for h in (F(1, 6), F(1, 12)):
        field = {x: cosv[x[0]] for x in sites}
        e_min = 2 * (1 - cosv[1])
        half = None
        for n in range(1, 40):
            field = {x: field[x] + h * (sum(field[tuple((x[i] + st[i]) % L for i in range(3))] for st in STEPS) - 6 * field[x]) for x in sites}
            ok = ok and all(field[x] == (1 - h * e_min) ** n * cosv[x[0]] for x in sites[:40])
            if half is None and field[(0, 0, 0)] < F(1, 2):
                half = n
        ok = ok and half is not None and half >= 1 / (2 * h * e_min)
        lives.append(f"h = {h}: half-life {half} ticks, bound {1 / (2 * h * e_min)}")
    report("W3", ok, "the slowest mode of the 6^3 torus stepped on all 216 sites: amplitude (1 - h E_min)^n exactly; " + "; ".join(lives))


def w4():
    ok = True
    for h in (F(1, 6), F(1, 12)):
        for m2 in (F(1, 10), F(1, 50)):
            factor = (1 - h * m2) * (1 - h * m2)            # a mode with E(k) = m^2
            n, amp = 0, F(1)
            while amp >= F(1, 2):
                amp *= factor
                n += 1
            ok = ok and n >= 1 / (4 * h * m2)
    report("W4", ok, "with a mass term m^2 and a mode with E(k) = m^2, the number of ticks to lose half the deviation is at least 1/(4 h m^2) at h = 1/6, 1/12 and m^2 = 1/10, 1/50")


if __name__ == "__main__":
    for fn in (w1, w2, w3, w4):
        fn()
    print(f"REFUTER TOTAL: FAIL={fails}")
    sys.exit(1 if fails else 0)
