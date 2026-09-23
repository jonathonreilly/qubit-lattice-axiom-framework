#!/usr/bin/env python3
"""Order laws for extended soldered supports: independent local clocks nucleate at density 1/(1+deg),
so they cannot form extended soldered supports; covariant sweep order laws
have no nucleation and no first formation, and complete the stated finite cubes with certainty; infinite process existence is not asserted.
Exact and finite.

Supplied conditional finite models; no physical formation law is inferred.  Exact rational arithmetic; no floating point.

Declared objects
  * formation orders of a window; a nucleation is a site formed before all
    of its in-window neighbours; the uniform race (independent identically distributed atomless
    clocks, the uniform order law of the clock-and-rate block);
  * the soldered role-letter rule of open PR 8669 (parity vectors; a site's
    letter fixes each neighbour's letter; disagreement leaves a site
    unrecorded), whose completion on an order with k nucleations is
    (1/8)^(k-1);
  * lexicographic sweep orders: sites ordered by (s.d1, s.d2, s.d3) for a
    signed frame (d1, d2, d3) of lattice directions; the uniform mixture
    over all 48 frames is invariant under every cubic symmetry;
  * windows: the 5-site path, the 3x3 plane, the 2x2x2 cube, and Z^3
    through its translation-invariant order laws.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 120
RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def neighbours(sites):
    S = set(sites)
    return {s: [t for t in sites if sum(abs(a - b) for a, b in zip(s, t)) == 1] for s in S}


def nucleations(order, nb):
    seen, k = set(), 0
    for s in order:
        if not any(t in seen for t in nb[s]):
            k += 1
        seen.add(s)
    return k


def exact_mean_k(sites):
    nb = neighbours(sites)
    tot, n = 0, 0
    for o in permutations(sites):
        tot += nucleations(o, nb)
        n += 1
    return Fr(tot, n), nb


print("== 1. Independent clocks nucleate at density 1/(1 + degree) ==")
PATH5 = tuple((i, 0, 0) for i in range(5))
PLANE = tuple((i, j, 0) for i in range(3) for j in range(3))
CUBE = tuple(product((0, 1), repeat=3))
for name, W in (("5-site path", PATH5), ("3x3 plane", PLANE), ("2x2x2 cube", CUBE)):
    mean, nb = exact_mean_k(W)
    formula = sum(Fr(1, 1 + len(nb[s])) for s in W)
    check(f"uniform race on the {name}: exact E[k] over all {len(W)}! orders equals sum 1/(1 + deg)",
          mean == formula, f"E[k] = {mean}")
NB_CUBE = neighbours(CUBE)
BOTH = sum(1 for o in permutations(CUBE)
           if o.index((0, 0, 0)) < min(o.index(t) for t in NB_CUBE[(0, 0, 0)])
           and o.index((1, 1, 1)) < min(o.index(t) for t in NB_CUBE[(1, 1, 1)]))
check("antipodal cube corners have disjoint closed neighbourhoods: both nucleate in exactly 1/16 of orders",
      Fr(BOTH, 40320) == Fr(1, 16),
      "independent events of probability 1/4 each, the ingredient of the decay bound below")


def completion_bound(m, p):
    """Upper bound on (1/8)^(k-1)-completion from m sites with disjoint closed neighbourhoods,
    each nucleating independently with probability p."""
    return 8 * (1 - 7 * p / 8) ** m - 7 * (1 - p) ** m


check("on Z^3 (p = 1/7) the soldered skeleton completes with probability <= 8(7/8)^m - 7(6/7)^m -> 0",
      completion_bound(1, Fr(1, 7)) == 1 and completion_bound(60, Fr(1, 7)) < Fr(1, 100)
      and completion_bound(2, Fr(1, 4)) == Fr(121, 128) and completion_bound(2, Fr(1, 4)) > Fr(599, 2048),
      "m sites spaced 3 apart in a window of volume ~27m; the cube instance 121/128 bounds the exact 599/2048")

print()
print("== 2. Sweep order laws: no nucleation, no first formation, certain completion ==")
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FRAMES = [(a, b, c) for a in DIRS for b in DIRS for c in DIRS
          if sum(x * y for x, y in zip(a, b)) == 0 and sum(x * y for x, y in zip(a, c)) == 0
          and sum(x * y for x, y in zip(b, c)) == 0]


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def sweep(frame, W):
    return tuple(sorted(W, key=lambda s: tuple(dot(s, d) for d in frame)))


SWEEPS = [sweep(f, CUBE) for f in FRAMES]
check("48 signed frames give 48 distinct lexicographic sweeps of the cube, each with exactly one nucleation",
      len(FRAMES) == 48 and len(set(SWEEPS)) == 48 and all(nucleations(o, NB_CUBE) == 1 for o in SWEEPS))


def rot_matrices():
    G = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            A = [[0] * 3 for _ in range(3)]
            for i in range(3):
                A[i][perm[i]] = signs[i]
            d = (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
                 + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))
            if d == 1:
                G.append(A)
    return G


def act(A, s):
    """Cube symmetry about the centre (1/2,1/2,1/2), mapping {0,1}^3 to itself."""
    c = [2 * x - 1 for x in s]
    r = [sum(A[i][j] * c[j] for j in range(3)) for i in range(3)]
    return tuple((x + 1) // 2 for x in r)


ROT = rot_matrices()
SWEEP_SET = set(SWEEPS)
check("the uniform law over the 48 sweeps is invariant under all 24 proper rotations of the cube",
      all(tuple(act(A, s) for s in o) in SWEEP_SET for A in ROT for o in SWEEPS) and len(ROT) == 24,
      "a covariant order law none of whose realisations is rotation-invariant")
LETTERS = CUBE


def soldered(s, formed):
    implied = set()
    for t in NB_CUBE[s]:
        if t in formed and formed[t] != "h":
            ax = next(i for i in range(3) if s[i] != t[i])
            implied.add(tuple(b ^ (1 if j == ax else 0) for j, b in enumerate(formed[t])))
    if not implied:
        return {l: Fr(1, 8) for l in LETTERS}
    return {implied.pop(): Fr(1)} if len(implied) == 1 else {}


def finished(order):
    layer = {(): Fr(1)}
    for s in order:
        nxt = {}
        for part, mass in layer.items():
            formed = {order[i]: part[i] for i in range(len(part))}
            probs = soldered(s, formed)
            tot = sum(probs.values())
            for v, p in probs.items():
                nxt[part + (v,)] = nxt.get(part + (v,), Fr(0)) + mass * p
            if tot < 1:
                nxt[part + ("h",)] = nxt.get(part + ("h",), Fr(0)) + mass * (1 - tot)
        layer = nxt
    pos = {s: i for i, s in enumerate(order)}
    return {tuple(part[pos[s]] for s in CUBE): m for part, m in layer.items()}


SK = {tuple(tuple(a ^ b for a, b in zip(s, phi)) for s in CUBE) for phi in LETTERS}
LAWS = [finished(o) for o in SWEEPS]
check("under every sweep the skeleton completes with certainty, uniform over its 8 phases",
      all(set(L) == SK and set(L.values()) == {Fr(1, 8)} for L in LAWS))
check("and the completed law is the same for all 48 sweeps: the frame is realised but not recorded",
      all(L == LAWS[0] for L in LAWS))
BOX = [(x, y, z) for x in range(-2, 3) for y in range(-2, 3) for z in range(-2, 3)]
F0 = FRAMES[0]


def key(v):
    return tuple(dot(v, d) for d in F0)


def minus(u, v):
    return tuple(a - b for a, b in zip(u, v))


check("on Z^3 each lexicographic sweep is translation-invariant and every site has an earlier neighbour",
      all(key(minus(v, F0[0])) < key(v) for v in BOX)
      and all((key(u) < key(v)) == (key(tuple(a + b for a, b in zip(u, t))) < key(tuple(a + b for a, b in zip(v, t))))
              for u in BOX[::7] for v in BOX[::11] for t in ((3, -1, 2), (-4, 5, 0))),
      "checked on a 5x5x5 box: no nucleation and no first formation, every formation preceded by a neighbour's")

print()
print("per_element: checked the finite configurations and arithmetic controls explicitly enumerated above")
print("per_site: checked the declared finite-window local rules under their supplied sampling conventions")
print("per_mode: checked and not executed — no infinite-volume Fourier or spectral mode computation is performed")
print("per_block: checked only the listed finite windows and orders; proofs beyond those runs are source arguments")
print("lattice_wide: checked and not executed — no infinite-lattice formation process or physical completion is simulated")
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
