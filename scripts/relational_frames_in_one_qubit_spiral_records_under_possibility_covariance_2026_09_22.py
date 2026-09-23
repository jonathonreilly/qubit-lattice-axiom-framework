#!/usr/bin/env python3
"""Relational frames in one qubit: under possibility covariance (rules that
commute with rotations of the Bloch sphere, so no possibility is singled
out), coordinate letters cannot be fixed points, but spiral records can
carry the lattice frame.  In a sweep and under the static reading the
spirals are stationary records of a covariant unsoldered rule; at any
first formation a lone child's value is symmetric about its parent's, so
the spiral is missed almost surely.  Exact rational arithmetic.

Next-steps campaign after the TOE derivation campaign by underdetermination
witnesses.

Declared objects
  * possibilities: rational points of the Bloch sphere; possibility
    covariance: R(h.config) = h_* R(config) for rotations h (the independent
    internal action of the landed possibility-covariance note), together
    with the unsoldered lattice reading of open PR 8676;
  * Pythagorean angles t1, t2, t3 with (cos, sin) = (3/5, 4/5), (5/13, 12/13),
    (8/17, 15/17), and spiral records b(x) = R_n(t . x) b0, b0 perpendicular
    to n;
  * the spiral rule: from three back-neighbour values on one great circle,
    the unique point b with b = R_n(t_pi(i)) w_i for some assignment pi and
    orientation of n; otherwise no record;
  * orders: the sweep (three back-neighbours), the static reading (all six
    neighbours), and first formations with lone children.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import sys
from fractions import Fraction as Fr
from itertools import permutations, product
from math import isqrt

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def scale(k, a):
    return tuple(k * x for x in a)


def vsum(*vs):
    return tuple(sum(c) for c in zip(*vs))


def rot(n, c, s, v):
    return vsum(scale(c, v), scale(s, cross(n, v)), scale((1 - c) * dot(n, v), n))


def fsqrt(q):
    q = Fr(q)
    if q < 0:
        return None
    a, b = isqrt(q.numerator), isqrt(q.denominator)
    return Fr(a, b) if a * a == q.numerator and b * b == q.denominator else None


ANG = [(Fr(3, 5), Fr(4, 5)), (Fr(5, 13), Fr(12, 13)), (Fr(8, 17), Fr(15, 17))]
SIGNED = [(c, s) for c, s in ANG] + [(c, -s) for c, s in ANG]


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cpow(z, k):
    out = (Fr(1), Fr(0))
    base = z if k >= 0 else (z[0], -z[1])
    for _ in range(abs(k)):
        out = cmul(out, base)
    return out


Z = (Fr(0), Fr(0), Fr(1))
B0 = (Fr(1), Fr(0), Fr(0))


def spiral(x):
    z = (Fr(1), Fr(0))
    for i in range(3):
        z = cmul(z, cpow(ANG[i], x[i]))
    return (z[0], z[1], Fr(0))


def rule(ws):
    base = cross(ws[0], ws[1])
    norm = fsqrt(dot(base, base))
    if not norm:
        return None
    n = scale(1 / norm, base)
    if dot(ws[2], n) != 0:
        return None
    found = set()
    for m in (n, scale(-1, n)):
        for p in permutations(range(3)):
            cand = rot(m, *ANG[p[0]], ws[0])
            if all(rot(m, *ANG[p[i]], ws[i]) == cand for i in (1, 2)):
                found.add(cand)
    return next(iter(found)) if len(found) == 1 else None


# ---------- A. the angles ----------
print("A. the angles")
unit = all(c * c + s * s == 1 for c, s in ANG)
plaq = all((cmul(a, b) == cmul(c, d)) == (sorted([a, b]) == sorted([c, d]))
           for a, b, c, d in product(ANG, repeat=4))
nontriv = all(cmul(a, b) != (1, 0) for a, b in product(ANG, repeat=2))
check("three Pythagorean rotations: six distinct signed angles, and the plaquette lemma for the positive ones",
      unit and len(set(SIGNED)) == 6 and plaq and nontriv, "e(a) e(b) = e(c) e(d) only for {a,b} = {c,d}; 81 cases")

# ---------- B. spirals are stationary in a sweep ----------
print("B. spiral records in a sweep")
L = 4
BOX = list(product(range(L), repeat=3))
HAX = (Fr(2, 3), Fr(2, 3), Fr(1, 3))
H = lambda v: rot(HAX, Fr(3, 5), Fr(4, 5), v)
recs = {"spiral": {x: spiral(x) for x in BOX}, "rotated spiral": {x: H(spiral(x)) for x in BOX}}
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def back(x):
    return [tuple(x[j] - (1 if j == i else 0) for j in range(3)) for i in range(3)]


inner = [x for x in BOX if all(c >= 1 for c in x)]
stat = {name: all(rule([r[y] for y in back(x)]) == r[x] for x in inner) for name, r in recs.items()}
check("every site with three back-neighbours equals the spiral rule's unique output, for a spiral and a rotated spiral",
      all(stat.values()), f"{len(inner)} sites each; the rule tries all assignments and both orientations")
sym = all(rule([[r[y] for y in back(x)][k] for k in p]) == r[x]
          for r in recs.values() for x in inner for p in [(1, 2, 0), (2, 0, 1), (1, 0, 2)])
outs = [rule([recs["spiral"][y] for y in back(x)]) for x in inner]
comm = all(o is not None and rule([H(recs["spiral"][y]) for y in back(x)]) == H(o) for x, o in zip(inner, outs))
check("the rule does not care which back-neighbour is which (unsoldered), and commutes with rotating the sphere",
      sym and comm)

# ---------- C. the record carries the frame ----------
print("C. what the record carries")
core = [x for x in BOX if all(1 <= c <= L - 2 for c in x)]
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def read(r, x, d):
    y = tuple(a + b for a, b in zip(x, d))
    c, s = dot(r[x], r[y]), dot(Z if r is recs["spiral"] else H(Z), cross(r[x], r[y]))
    return [k for k, a in enumerate(SIGNED) if a == (c, s)]


frame = all(read(r, x, d) == [DIRS.index(d) // 2 + (3 if DIRS.index(d) % 2 else 0)]
            for r in recs.values() for x in core for d in DIRS)
check("each site reads every neighbour's direction from the rotation that takes its value to the neighbour's",
      frame, "the six signed angles label the six bond directions; roles and ice follow as in open PR 8676")
static = all(rule([r[y] for y in back(x)]) == r[x] and
             rule([r[tuple(a + b for a, b in zip(x, e))] for e in E3]) == r[x] for r in recs.values() for x in core)
check("under the static reading each core site is the unique covariant completion of its neighbours",
      static, "forward neighbours determine it too (the rule applied with the angles reversed)")

# ---------- D. first formations ----------
print("D. first formations")
par = recs["spiral"][(0, 0, 0)]
G = lambda v: rot(par, Fr(3, 5), Fr(4, 5), v)
twin = {x: G(recs["spiral"][x]) for x in BOX}
both = all(rule([twin[y] for y in back(x)]) == twin[x] for x in inner)
split = twin[(0, 0, 0)] == par and twin[(1, 0, 0)] != recs["spiral"][(1, 0, 0)]
axis_only = all(G(v) != v for v in [recs["spiral"][(1, 0, 0)], recs["spiral"][(0, 1, 0)]])
check("a lone child's value is fixed only up to rotation about its parent: two stationary spirals agree at the parent, differ at the child",
      both and split and axis_only, "a covariant lone-child law is symmetric about the parent; its only atoms are the two poles")
poles = all(recs["spiral"][tuple(c + (1 if j == i else 0) for j, c in enumerate((0, 0, 0)))] not in (par, scale(-1, par))
            for i in range(3))
check("spiral values are never at the parent's poles, so each lone child hits its spiral value with probability 0",
      poles, "registration at a first formation fails almost surely under possibility covariance")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
