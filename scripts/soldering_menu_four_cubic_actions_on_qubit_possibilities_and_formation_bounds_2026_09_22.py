#!/usr/bin/env python3
"""The soldering menu: the proper cubic rotations act on a qubit's
possibilities in exactly four ways, and each action fixes which star
constraints nearest-neighbour formation can build.  Exact and finite.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.  Exact rational arithmetic; no floating point.

Declared objects
  * the proper cubic group O (24 signed permutation matrices of determinant
    +1), isomorphic to S4, acting on lattice positions;
  * automorphisms of the qubit algebra M_2(C): proper rotations of the Bloch
    ball (SO(3)); an action on possibilities is a homomorphism rho: O -> SO(3)
    (Admissibility's covariance sentence names the lattice rotations, not
    how they move possibilities);
  * the four actions constructed: trivial (the unsoldered reading), a sign
    twist diag(1, s, s), axis soldering s(g)|g| through the axis
    permutation, and full soldering rho(g) = g; s = sign of the axis
    permutation;
  * star constraints from the previous blocks: the ice count (3 of 6
    occupied), the parity-role link profile, and odd Gauss parity.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def det3(A):
    return (A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1]) - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
            + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0]))


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mt(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))


I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
O = []
for perm in permutations(range(3)):
    for signs in product((1, -1), repeat=3):
        A = [[0] * 3 for _ in range(3)]
        for i in range(3):
            A[i][perm[i]] = signs[i]
        A = tuple(tuple(r) for r in A)
        if det3(A) == 1:
            O.append(A)


def absm(g):
    return tuple(tuple(abs(x) for x in r) for r in g)


def s(g):
    return det3(absm(g))


ACTIONS = {
    "trivial": lambda g: I3,
    "sign twist": lambda g: ((1, 0, 0), (0, s(g), 0), (0, 0, s(g))),
    "axis": lambda g: tuple(tuple(s(g) * x for x in r) for r in absm(g)),
    "full": lambda g: g,
}
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def mv(g, v):
    return tuple(sum(g[i][j] * v[j] for j in range(3)) for i in range(3))


print("== 1. Exactly four actions of the proper cubic rotations on possibilities ==")
check("the four maps are homomorphisms O -> SO(3): orthogonal, determinant 1, multiplicative on all 576 pairs",
      all(mm(r(g), mt(r(g))) == I3 and det3(r(g)) == 1 for r in ACTIONS.values() for g in O)
      and all(r(mm(g, h)) == mm(r(g), r(h)) for r in ACTIONS.values() for g in O for h in O))


def cls(g):
    """Conjugacy class label of O by trace and sign: identity, 90-degree, axis 180, 120, diagonal 180."""
    t = g[0][0] + g[1][1] + g[2][2]
    return {(3, 1): "e", (1, -1): "c4", (-1, 1): "c2", (0, 1): "c3", (-1, -1): "c2d"}[(t, s(g))]


CLASSES = ("e", "c4", "c2", "c3", "c2d")
SIZES = {c: sum(1 for g in O if cls(g) == c) for c in CLASSES}
CHAR = {name: tuple(next(r(g)[0][0] + r(g)[1][1] + r(g)[2][2] for g in O if cls(g) == c) for c in CLASSES)
        for name, r in ACTIONS.items()}
IRR = {"A1": (1, 1, 1, 1, 1), "A2": (1, -1, 1, 1, -1), "E": (2, 0, 2, -1, 0),
       "T1": (3, 1, -1, 0, -1), "T2": (3, -1, -1, 0, 1)}


def inner(x, y):
    return Fr(sum(SIZES[c] * a * b for c, a, b in zip(CLASSES, x, y)), 24)


check("character table of O = S4: class sizes 1,6,3,8,6 and the five irreducible characters are orthonormal",
      [SIZES[c] for c in CLASSES] == [1, 6, 3, 8, 6]
      and all(inner(IRR[a], IRR[b]) == (1 if a == b else 0) for a in IRR for b in IRR)
      and CHAR["full"] == IRR["T1"])
DETCHAR = {"A1": 0, "A2": 1, "E": 1, "T1": 0, "T2": 1}
combos = []
for a, b, c, d, e in product(range(4), range(4), range(2), range(2), range(2)):
    if a + b + 2 * c + 3 * d + 3 * e == 3:
        odd = (b * DETCHAR["A2"] + c * DETCHAR["E"] + e * DETCHAR["T2"]) % 2
        combos.append(((a, b, c, d, e), odd == 0))
ALLOWED = [k for k, ok in combos if ok]
check("real 3-dimensional representations of S4: 8 decompositions, exactly 4 of determinant 1",
      len(combos) == 8 and sorted(ALLOWED) == sorted([(3, 0, 0, 0, 0), (1, 2, 0, 0, 0), (0, 1, 1, 0, 0), (0, 0, 0, 1, 0)]),
      "3A1 (trivial), A1+2A2 (sign twist), A2+E (axis), T1 (full); A1+E, T2 and the odd sign sums have determinant -1")


def decomp(ch):
    return {k: inner(ch, v) for k, v in IRR.items() if inner(ch, v)}


check("the constructed actions have exactly those decompositions, so they are pairwise inequivalent",
      decomp(CHAR["trivial"]) == {"A1": 3} and decomp(CHAR["sign twist"]) == {"A1": 1, "A2": 2}
      and decomp(CHAR["axis"]) == {"A2": 1, "E": 1} and decomp(CHAR["full"]) == {"T1": 1}
      and len(set(CHAR.values())) == 4,
      "characters " + "; ".join(f"{k} {v}" for k, v in CHAR.items()))
T2_90 = next(g for g in O if cls(g) == "c4")
check("the excluded T2 = sign x full has determinant -1 on a quarter-turn: not an automorphism of the qubit",
      det3(tuple(tuple(s(T2_90) * x for x in r) for r in T2_90)) == -1)

print()
print("== 2. Kernels and their orbits on the six bond directions ==")
KER = {name: [g for g in O if r(g) == I3] for name, r in ACTIONS.items()}


def orbits(G):
    out, seen = [], set()
    for d in DIRS:
        if d in seen:
            continue
        o = {mv(g, d) for g in G}
        seen |= o
        out.append(o)
    return out


ORB = {name: orbits(K) for name, K in KER.items()}
check("kernel orders 24, 12, 4, 1; orbits on the six directions 1, 1, 3, 6",
      [len(KER[n]) for n in ACTIONS] == [24, 12, 4, 1] and [len(ORB[n]) for n in ACTIONS] == [1, 1, 3, 6],
      "axis soldering's kernel is the three axis half-turns: orbits {+x,-x}, {+y,-y}, {+z,-z}")

print()
print("== 3. What a site can broadcast to neighbours formed after it ==")
GRID = [Fr(k, 12) for k in range(13)]


def ice_bound(sizes):
    best = Fr(0)
    for ps in product(GRID, repeat=len(sizes)):
        dist = {0: Fr(1)}
        for n, p in zip(sizes, ps):
            nd = {}
            for tot, m in dist.items():
                for k in range(n + 1):
                    from math import comb
                    w = comb(n, k) * p ** k * (1 - p) ** (n - k)
                    nd[tot + k] = nd.get(tot + k, Fr(0)) + m * w
            dist = nd
        best = max(best, dist.get(3, Fr(0)))
    return best


def odd_at(sizes, ps):
    """P(odd total) for independent orbits of the given sizes, occupied with probabilities ps."""
    prod = Fr(1)
    for n, p in zip(sizes, ps):
        prod *= (1 - 2 * p) ** n
    return (1 - prod) / 2


def odd_bound(sizes):
    return max(odd_at(sizes, ps) for ps in product(GRID, repeat=len(sizes)))


SIZES_BY = {n: tuple(len(o) for o in ORB[n]) for n in ACTIONS}
ICE = {n: ice_bound(SIZES_BY[n]) for n in ("trivial", "axis")}
check("ice count (3 of 6 occupied) broadcast bound: 5/16 unsoldered and sign twist, 1/2 axis, 1 full",
      ICE["trivial"] == Fr(5, 16) and ICE["axis"] == Fr(1, 2) and SIZES_BY["sign twist"] == SIZES_BY["trivial"]
      and SIZES_BY["full"] == (1,) * 6,
      "axis soldering ties +x to -x, so the occupied count comes in pairs: odd totals need a coin")
FULL_ICE = Fr(1)
for k, p_ in enumerate((1, 1, 1, 0, 0, 0)):
    FULL_ICE *= Fr(p_) if k < 3 else 1 - Fr(p_)
check("full soldering dictates the ice count: occupy three chosen directions with certainty (mass exactly 1)",
      FULL_ICE == 1 and SIZES_BY["full"] == (1,) * 6
      and ice_bound((2, 2, 2)) < FULL_ICE)
ODD = {n: odd_bound(SIZES_BY[n]) for n in ("trivial", "axis")}
check("odd Gauss parity broadcast bound: 1/2 unsoldered, sign twist and axis; only full soldering can dictate it",
      ODD["trivial"] == Fr(1, 2) and ODD["axis"] == Fr(1, 2)
      and odd_at((6,), (Fr(1, 4),)) == Fr(63, 128) and odd_at((1,) * 6, (1, 0, 0, 0, 0, 0)) == 1,
      "six links at p = 1/4 are odd with probability 63/128; full soldering sets one link and is odd with certainty")


def profile_ok(orbs):
    """Parity-role link profile at an L_x centre: V on +-x, P_xy on +-y, P_xz on +-z.
    Achievable with certainty iff each kernel orbit needs one letter only."""
    need = {(1, 0, 0): "V", (-1, 0, 0): "V", (0, 1, 0): "Pxy", (0, -1, 0): "Pxy", (0, 0, 1): "Pxz", (0, 0, -1): "Pxz"}
    return all(len({need[d] for d in o}) == 1 for o in orbs)


check("parity-role link profile: impossible to dictate unsoldered or twisted (one orbit), certain with axis or full",
      [profile_ok(ORB[n]) for n in ACTIONS] == [False, False, True, True]
      and not profile_ok([{(1, 0, 0), (-1, 0, 0)}, {(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)}])
      and max(3 * q ** 2 * (1 - q) ** 4 for q in GRID) == Fr(16, 243),
      "one orbit: the star-constraints block's bound 16/243 applies")

print()
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
