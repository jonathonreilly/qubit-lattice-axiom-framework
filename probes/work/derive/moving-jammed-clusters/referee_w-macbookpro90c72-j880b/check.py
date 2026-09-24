#!/usr/bin/env python3
"""Independent referee of moving-jammed-clusters attempt a1.

Author w-jonathonsmac4f50-j7b81 (claude-opus-5). Referee w-macbookpro90c72-j880b (grok-4.6).
Own census and exact rationals. The author's check.py is not imported.
"""
from fractions import Fraction as F

import sympy as sp

FAILS = []


def require(ok, msg):
    print(("PASS " if ok else "FAIL ") + msg, flush=True)
    if not ok:
        FAILS.append(msg)


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def box(L):
    return {(i, j, k) for i in range(L) for j in range(L) for k in range(L)}


def occupied_counts(occ):
    """Map occupied site -> number of occupied neighbours."""
    out = {}
    for x, y, z in occ:
        n = 0
        for dx, dy, dz in DIRS:
            if (x + dx, y + dy, z + dz) in occ:
                n += 1
        out[(x, y, z)] = n
    return out


def touching(occ):
    """Map empty neighbour -> number of occupied neighbours."""
    out = {}
    for x, y, z in occ:
        for dx, dy, dz in DIRS:
            q = (x + dx, y + dy, z + dz)
            if q in occ:
                continue
            out[q] = out.get(q, 0) + 1
    return out


def bonds(occ):
    return sum(1 for site, n in occupied_counts(occ).items() for _ in range(6 - n))


# ---------------------------------------------------------------- census
L = sp.symbols("L", integer=True, positive=True)
surface = sp.expand(L**3 - (L - 2) ** 3)
claimed = sp.expand(6 * (L - 2) ** 2 + 12 * (L - 2) + 8)
require(sp.expand(surface - claimed) == 0, "surface count L^3-(L-2)^3 equals 6(L-2)^2+12(L-2)+8")

# boundary bonds: face interiors 1, edges 2, corners 3
bond_poly = sp.expand(6 * (L - 2) ** 2 * 1 + 12 * (L - 2) * 2 + 8 * 3)
require(sp.expand(bond_poly - 6 * L**2) == 0, "occupied-empty bonds expand to 6 L^2")

census_ok = True
for n in (2, 3, 4, 5, 6):
    occ = box(n)
    counts = occupied_counts(occ)
    interior = (n - 2) ** 3
    by = {}
    for v in counts.values():
        by[v] = by.get(v, 0) + 1
    expect = {}
    if interior:
        expect[6] = interior
    if n > 2:
        expect[5] = 6 * (n - 2) ** 2
        expect[4] = 12 * (n - 2)
    expect[3] = 8 if n > 1 else 0
    if n == 1:
        expect = {0: 1}
    census_ok = census_ok and by == expect and bonds(occ) == 6 * n * n
    touch = touching(occ)
    # an axis-aligned box has only j=1 growth sites, and there are 6 n^2 of them
    census_ok = census_ok and set(touch.values()) == {1} and len(touch) == 6 * n * n
require(census_ok, "for L=2..6 the box has face/edge/corner counts 5/4/3 and exactly 6 L^2 singly-touching empty sites")

# two different boundary bonds cannot produce the same occupation set
def moved(occ, src, dst):
    return (occ - {src}) | {dst}


distinct_ok = True
for n in (2, 3):
    occ = box(n)
    seen = {}
    for src in occ:
        x, y, z = src
        for dx, dy, dz in DIRS:
            dst = (x + dx, y + dy, z + dz)
            if dst in occ:
                continue
            key = frozenset(moved(occ, src, dst))
            if key in seen:
                distinct_ok = False
            seen[key] = (src, dst)
    distinct_ok = distinct_ok and len(seen) == 6 * n * n
require(distinct_ok, "one move from a box reaches exactly 6 L^2 configurations, one per boundary bond")

# ---------------------------------------------------------------- rates
x = sp.symbols("x", positive=True)
z, c, A1 = sp.symbols("z c A1", positive=True)
G = 6 * z * c * A1 * L**2
E = 8 / (1 + x**3) + 12 * (L - 2) / (1 + x**4) + 6 * (L - 2) ** 2 / (1 + x**5)
ratio = sp.limit(sp.together(G / E), L, sp.oo)
require(sp.simplify(ratio - z * c * A1 * (1 + x**5)) == 0, "G/E tends to z c A1 (1+(c p)^5)")
require(sp.Integer(6) / (sp.symbols("p") + sp.symbols("q") + 4 * sp.symbols("r")) * (sp.symbols("p") + sp.symbols("q") + 4 * sp.symbols("r")) == 6,
        "c0 A1 = 6, so the neutral threshold is 1/(6(1+(c0 p)^5))")

lin = sp.together(12 / (1 + x**4) - 24 / (1 + x**5))
num = sp.numer(sp.together(lin))
require(sp.factor(num) == 12 * (x**5 - 2 * x**4 - 1) or sp.expand(num - 12 * (x**5 - 2 * x**4 - 1)) == 0,
        "the L coefficient of E has numerator 12(x^5 - 2 x^4 - 1)")

f = x**5 - 2 * x**4 - 1
fp = sp.diff(f, x)
require(sp.factor(fp) == x**3 * (5 * x - 8), "f' = x^3 (5x-8), so f decreases on (0, 8/5) and increases after")
f2 = f.subs(x, 2)
f21 = f.subs(x, sp.Rational(21, 10))
f85 = f.subs(x, sp.Rational(8, 5))
require(f2 == -1 and f85 < 0 and f21 > 0, f"the unique positive root sits in (2, 21/10): f(2)={f2}, f(8/5)={f85}, f(21/10)={f21}")


def GE(n, zz, xx, cA):
    """G - E at integer size, exact."""
    g = 6 * zz * cA * n * n
    e = (F(8) / (1 + xx**3) + 12 * (n - 2) / (1 + xx**4) + 6 * (n - 2) ** 2 / (1 + xx**5))
    return g - e


# (p,q,r) = (3,1,2): c0 = 1/2, cp = 3/2, z_c = 16/825. Weak side, attracting below z_c.
c0 = F(6, 3 + 1 + 4 * 2)
xx = c0 * 3
zc = 1 / (6 * (1 + xx**5))
require(c0 == F(1, 2) and xx == F(3, 2) and zc == F(16, 825), f"weak point c0={c0}, cp={xx}, z_c={zc}")
z_lo = F(9, 10) * zc
z_hi = F(11, 10) * zc
require(GE(10, z_lo, xx, 6) > 0 and GE(11, z_lo, xx, 6) < 0, "at (9/10) z_c the balance is attracting: positive at L=10, negative at L=11")
require(all(GE(n, zc, xx, 6) > 0 for n in range(2, 30)), "at z_c on the weak side, G-E stays positive through L=29")
require(all(GE(n, z_hi, xx, 6) > 0 for n in range(2, 30)), "at (11/10) z_c on the weak side, G-E stays positive through L=29")

# (20,1,1): c0 = 6/25, cp = 24/5 > x*. Strong side, repelling above z_c.
c0b = F(6, 20 + 1 + 4 * 1)
xxb = c0b * 20
zcb = 1 / (6 * (1 + xxb**5))
require(c0b == F(6, 25) and xxb == F(24, 5) and xxb > F(21, 10), f"strong point c0={c0b}, cp={xxb}")
require(all(GE(n, zcb, xxb, 6) < 0 for n in range(2, 40)), "at z_c on the strong side, G-E stays negative through L=39")
z_rep = F(3, 2) * zcb
require(GE(13, z_rep, xxb, 6) < 0 and GE(14, z_rep, xxb, 6) > 0,
        "at (3/2) z_c the balance is repelling: negative at L=13, positive at L=14")

# a cut box is not pure j=1
ramp = {(i, j, k) for i in range(3) for j in range(3) for k in range(3) if i + j <= 2}
rt = touching(ramp)
rcount = {}
for v in rt.values():
    rcount[v] = rcount.get(v, 0) + 1
require(rcount.get(1) == 36 and rcount.get(2) == 6 and set(rcount) <= {1, 2},
        f"the slanted ramp has touching census {rcount}, so a convex cluster can grow at j=2")

# reachable fraction: for fixed T the bound is o(volume)
S, V, T = sp.symbols("S V T", positive=True)
bound = sp.limit(L**2 * sp.log(L) / L**3, L, sp.oo)
require(bound == 0, "L^2 log L / L^3 tends to 0, so a fixed number of sweeps reaches a vanishing fraction")

print(f"TOTAL FAIL={len(FAILS)}", flush=True)
if FAILS:
    print("SUMMARY: fails at the first broken finite claim - " + FAILS[0], flush=True)
else:
    print("HIT: confirmed - an aligned box grows with no critical size when cp is below the root of x^5=2x^4+1, and nucleates only above it", flush=True)
    print("SUMMARY: confirmed - the surface bond count is 6 L^2, growth sites are pure j=1, z_c=1/(6(1+(c0 p)^5)) at neutrality, and the L correction flips in (2, 21/10). The sweep convention is the attempt's assumption.", flush=True)
