#!/usr/bin/env python3
"""J:attack-a:PR8670 - witness realizability, on ORDER_LAWS_FOR_EXTENDED_SOLDERED_SUPPORTS_... (2026-09-22).

Every stated witness, configuration or example is rebuilt in the declared setting (windows of Z^3, uniform race,
the soldered role-letter rule as the note and its runner state it, lexicographic sweeps over signed frames) and
checked literally, with exact rationals:
  W1 the three windows are the Z^3 induced subgraphs named, and E[k] = 2, 38/15, 2 over all orders;
  W2 the two antipodal cube corners have disjoint closed neighbourhoods and both nucleate in 2520 = 40320/16 orders;
  W3 "the exact 599/2048": the soldered rule, run on every one of the 40320 orders of the cube, completes with
     probability (1/8)^(k-1) on each, and the uniform average is 599/2048; the bound 121/128 is above it;
  W4 m = 60 sites with pairwise disjoint closed neighbourhoods, each of degree 6 inside a 9 x 12 x 15 window of 1620
     sites ("about 1600"); 8(7/8)^60 - 7(6/7)^60 < 1/100 and the value at m = 1 is 1;
  W5 the 48 signed frames give 48 distinct sweeps of the cube, each with exactly one nucleation, the uniform mixture
     is invariant under the 24 proper rotations, and no single sweep is invariant under a nontrivial one;
  W6 on a 5 x 5 x 5 box every one of the 48 sweeps is translation-invariant as an order, has exactly one nucleation
     (its corner), and every other site has the earlier neighbour s - d1 or another earlier neighbour.
"""
import sys
from collections import Counter
from fractions import Fraction as Fr
from itertools import permutations, product

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


def neighbours(sites):
    S = set(sites)
    return {s: [t for t in S if sum(abs(a - b) for a, b in zip(s, t)) == 1] for s in S}


def nucleations(order, nb):
    seen, k = set(), 0
    for s in order:
        if not any(t in seen for t in nb[s]):
            k += 1
        seen.add(s)
    return k


PATH5 = tuple((i, 0, 0) for i in range(5))
PLANE = tuple((i, j, 0) for i in range(3) for j in range(3))
CUBE = tuple(product((0, 1), repeat=3))

# W1
rows, good = [], True
for name, W, want in (("5-site path", PATH5, Fr(2)), ("3x3 plane", PLANE, Fr(38, 15)), ("2x2x2 cube", CUBE, Fr(2))):
    nb = neighbours(W)
    bonds = sum(len(v) for v in nb.values()) // 2
    tot = n = 0
    for o in permutations(W):
        tot += nucleations(o, nb)
        n += 1
    mean = Fr(tot, n)
    formula = sum(Fr(1, 1 + len(nb[s])) for s in W)
    good &= mean == want == formula
    rows.append(f"{name}: {len(W)} sites, {bonds} bonds, E[k] = {mean}")
ok("W1", good, "; ".join(rows) + " (all orders), equal to sum 1/(1 + deg) and to the note's 2, 38/15, 2")

# W2
NB = neighbours(CUBE)
A, B = (0, 0, 0), (1, 1, 1)
disjoint = not (set([A] + NB[A]) & set([B] + NB[B]))
both = sum(1 for o in permutations(CUBE)
           if o.index(A) < min(o.index(t) for t in NB[A]) and o.index(B) < min(o.index(t) for t in NB[B]))
ok("W2", disjoint and both == 2520 and Fr(both, 40320) == Fr(1, 16),
   f"antipodal corners: closed neighbourhoods disjoint ({disjoint}), both nucleate in {both} of 40320 orders = 1/16")

# W3: the soldered role-letter rule on every order of the cube
LETTERS = CUBE


def completion(order):
    """probability that the rule completes (no conflict) on this order: letters are parity vectors; a formed
    neighbour t across axis ax implies t's letter with bit ax flipped; none formed -> uniform; disagreement -> hole."""
    layer = {(): Fr(1)}
    for s in order:
        nxt = {}
        for part, mass in layer.items():
            formed = dict(zip(order, part))
            implied = set()
            for t in NB[s]:
                if t in formed and formed[t] != "h":
                    ax = next(i for i in range(3) if s[i] != t[i])
                    implied.add(tuple(b ^ (1 if j == ax else 0) for j, b in enumerate(formed[t])))
            if not implied:
                opts = {l: Fr(1, 8) for l in LETTERS}
            elif len(implied) == 1:
                opts = {implied.pop(): Fr(1)}
            else:
                opts = {"h": Fr(1)}
            for v, p in opts.items():
                nxt[part + (v,)] = nxt.get(part + (v,), Fr(0)) + mass * p
        layer = nxt
    return sum(m for part, m in layer.items() if "h" not in part)


dist = Counter()
per_order_ok = True
total = Fr(0)
for o in permutations(CUBE):
    k = nucleations(o, NB)
    c = completion(o)
    dist[k] += 1
    per_order_ok &= c == Fr(1, 8) ** (k - 1)
    total += c
avg = total / 40320
bound = 8 * (1 - Fr(7, 32)) ** 2 - 7 * (1 - Fr(1, 4)) ** 2
ok("W3", per_order_ok and avg == Fr(599, 2048) and bound == Fr(121, 128) and bound > avg,
   f"the rule run on all 40320 cube orders completes with (1/8)^(k-1) on each; k distribution "
   f"{sorted(dist.items())}; uniform-race completion {avg} (= the note's exact 599/2048); bound {bound} above it")

# W4: 60 sites with disjoint closed neighbourhoods, degree 6, inside a 9 x 12 x 15 window
WIN = [(x, y, z) for x in range(9) for y in range(12) for z in range(15)]
WS = set(WIN)
PICK = [(3 * i + 1, 3 * j + 1, 3 * k + 1) for i in range(3) for j in range(4) for k in range(5)]
def closed(s):
    return {s} | {tuple(s[q] + (d if q == a else 0) for q in range(3)) for a in range(3) for d in (1, -1)}
nbhd = [closed(s) for s in PICK]
pairwise = all(not (nbhd[i] & nbhd[j]) for i in range(len(PICK)) for j in range(i + 1, len(PICK)))
inside = all(nb_ <= WS for nb_ in nbhd)
f = lambda m: 8 * Fr(7, 8) ** m - 7 * Fr(6, 7) ** m
first_m = next(m for m in range(1, 200) if f(m) < Fr(1, 100))
ok("W4", len(PICK) == 60 and len(WIN) == 1620 and pairwise and inside and f(1) == 1 and f(60) < Fr(1, 100),
   f"60 sites at 3Z^3 + (1,1,1) in the 9x12x15 window (1620 sites): closed neighbourhoods pairwise disjoint and "
   f"inside (degree 6, p = 1/7); bound at m = 60 = {float(f(60)):.5f} < 1/100 (first below 1/100 at m = {first_m})")

# W5: the 48 sweeps of the cube
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
dot = lambda u, v: sum(a * b for a, b in zip(u, v))
FRAMES = [(a, b, c) for a in DIRS for b in DIRS for c in DIRS if dot(a, b) == 0 and dot(a, c) == 0 and dot(b, c) == 0]
sweep = lambda fr, W: tuple(sorted(W, key=lambda s: tuple(dot(s, d) for d in fr)))
SW = [sweep(fr, CUBE) for fr in FRAMES]
one_each = all(nucleations(o, NB) == 1 for o in SW)
ROTS = []
for perm in permutations(range(3)):
    for sg in product((1, -1), repeat=3):
        Mx = [[sg[i] if perm[i] == j else 0 for j in range(3)] for i in range(3)]
        det = (Mx[0][0] * (Mx[1][1] * Mx[2][2] - Mx[1][2] * Mx[2][1]) - Mx[0][1] * (Mx[1][0] * Mx[2][2] - Mx[1][2] * Mx[2][0])
               + Mx[0][2] * (Mx[1][0] * Mx[2][1] - Mx[1][1] * Mx[2][0]))
        if det == 1:
            ROTS.append(Mx)


def act(Mx, s):
    """rotation of the cube about its centre (1/2,1/2,1/2), on 0/1 coordinates."""
    c = [2 * v - 1 for v in s]
    r = [sum(Mx[i][j] * c[j] for j in range(3)) for i in range(3)]
    return tuple((v + 1) // 2 for v in r)


mix = Counter(SW)
inv = all(Counter(tuple(act(R, s) for s in o) for o in SW) == mix for R in ROTS)
single = [sum(1 for R in ROTS if tuple(act(R, s) for s in o) == o) for o in SW]
ok("W5", len(FRAMES) == 48 and len(set(SW)) == 48 and one_each and len(ROTS) == 24 and inv and all(c == 1 for c in single),
   "48 signed frames, 48 distinct sweeps, one nucleation each; the mixture is invariant under all 24 proper rotations "
   "and each single sweep is fixed only by the identity")

# W6: sweeps on a 5x5x5 box
BOX = [(x, y, z) for x in range(-2, 3) for y in range(-2, 3) for z in range(-2, 3)]
NBB = neighbours(BOX)
good = True
for fr in FRAMES:
    key = lambda s: tuple(dot(s, d) for d in fr)
    o = sweep(fr, BOX)
    good &= nucleations(o, NBB) == 1
    corner = o[0]
    good &= all(any(key(t) < key(s) for t in NBB[s]) for s in BOX if s != corner)
    good &= all((key(u) < key(v)) == (key(tuple(a + b for a, b in zip(u, t))) < key(tuple(a + b for a, b in zip(v, t))))
                for u in BOX[::9] for v in BOX[::13] for t in ((3, -1, 2), (-4, 5, 0), (1, 1, 1)))
    good &= all(key(tuple(a - b for a, b in zip(s, fr[0]))) < key(s) for s in BOX)
ok("W6", good, "5x5x5 box, all 48 frames: one nucleation (the corner), every other site has an earlier neighbour, "
   "s - d1 always precedes s, and the order is translation-invariant")

if FAILS:
    print("SUMMARY: witness realizability fails at " + ", ".join(FAILS) + " on PR #8670's note")
    print("HIT: a stated witness of PR #8670's order-law note is not realized: " + ", ".join(FAILS))
    sys.exit(0)
print("SUMMARY: pattern has no purchase on this note: every stated witness is realized in the declared setting "
      "(windows, antipodal corners, the exact 599/2048 by running the soldered rule on all 40320 orders, 60 disjoint "
      "neighbourhoods in a 1620-site window, the 48 sweeps and their invariance, the 5x5x5 box)")
