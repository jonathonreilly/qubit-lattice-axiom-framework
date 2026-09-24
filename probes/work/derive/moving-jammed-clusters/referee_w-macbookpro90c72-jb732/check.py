#!/usr/bin/env python3
"""Referee for J:derive:moving-jammed-clusters:a2.

Independent enumeration. A bond with one occupied end is visited at rate 1.
Departure probability along that bond is w_t/(w_s+w_t). For an aligned cluster,
w = x^{k} with x = c p. Nothing is imported from the author's check.
"""
import itertools
import sys
from collections import Counter
from fractions import Fraction as Fr

import sympy as sp

FAILS = []


def ok(tag, good, msg):
    print(("ok " if good else "FAIL ") + tag + ": " + msg)
    if not good:
        FAILS.append(tag)


NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def box(L):
    return set(itertools.product(range(L), repeat=3))


def octa(R):
    return {s for s in itertools.product(range(-R, R + 1), repeat=3) if abs(s[0]) + abs(s[1]) + abs(s[2]) <= R}


def dodec(R):
    return {s for s in itertools.product(range(-R, R + 1), repeat=3)
            if abs(s[0]) + abs(s[1]) <= R and abs(s[1]) + abs(s[2]) <= R and abs(s[2]) + abs(s[0]) <= R}


def bonds(S):
    """Occupied-empty bonds as (s, t, k_s, k_t) with k_t counted after s has left."""
    out = []
    for s in S:
        ks = sum(add(s, d) in S for d in NB)
        for d in NB:
            t = add(s, d)
            if t in S:
                continue
            kt = sum(add(t, e) in S and add(t, e) != s for e in NB)
            out.append((s, t, ks, kt))
    return out


# ---------- M1. box evaporation per bond ----------
x = sp.symbols("x", positive=True)
Lsym = sp.symbols("L", positive=True)
E = 24 / (1 + x ** 3) + 24 * (Lsym - 2) / (1 + x ** 4) + 6 * (Lsym - 2) ** 2 / (1 + x ** 5)
Ea = 8 / (1 + x ** 3) + 12 * (Lsym - 2) / (1 + x ** 4) + 6 * (Lsym - 2) ** 2 / (1 + x ** 5)
good = True
for n in range(2, 8):
    rows = bonds(box(n))
    good &= all(kt == 0 for *_, kt in rows) and len(rows) == 6 * n * n
    brute = sum(x ** kt / (x ** ks + x ** kt) for _, _, ks, kt in rows)
    good &= sp.simplify(brute - E.subs(Lsym, n)) == 0
ok("M1", good, "L=2..7: every box departure ends isolated, there are 6 L^2 of them, and the rate is E(L)")

# ---------- M2. detailed balance at a corner of the 2-box ----------
S = box(2)
s0, t0 = (1, 1, 1), (2, 1, 1)
ks = sum(add(s0, d) in S for d in NB)
S1 = (S - {s0}) | {t0}
kt = sum(add(t0, d) in S1 and add(t0, d) != t0 for d in NB)
empty_s = sum(add(s0, d) not in S for d in NB)
empty_t = sum(add(t0, d) not in S1 for d in NB)
mu = x ** kt / x ** ks
Pf = x ** kt / (x ** ks + x ** kt)
Pb = x ** ks / (x ** ks + x ** kt)
flux_bond = sp.simplify(Pf / (mu * Pb))
flux_split = sp.simplify((Fr(1, empty_s) * Pf) / (mu * Fr(1, empty_t) * Pb))
ok("M2", (ks, kt, empty_s, empty_t) == (3, 0, 3, 6) and flux_bond == 1 and flux_split == 2,
   f"2-box corner: (k_s, k_t, empty before, empty after)=({ks},{kt},{empty_s},{empty_t}); "
   f"bond-rate flux {flux_bond}, one-attempt-split flux {flux_split}")

# ---------- M3. finite-size signs ----------
lead = sp.factor(sp.together(sp.expand(E).coeff(Lsym, 2)))
beta = sp.factor(sp.together(sp.expand(E).coeff(Lsym, 1)))
gamma = sp.factor(sp.together(sp.expand(E).coeff(Lsym, 0)))
beta_t = sp.factor(24 * x ** 4 * (x - 1) / ((1 + x ** 4) * (1 + x ** 5)))
gamma_t = sp.factor(24 * x ** 3 * (x - 1) ** 3 * (x + 1) * (x ** 2 + 1) / ((1 + x ** 3) * (1 + x ** 4) * (1 + x ** 5)))
beta_a = sp.factor(sp.together(sp.expand(Ea).coeff(Lsym, 1)))
beta_a_t = sp.factor(12 * (x ** 5 - 2 * x ** 4 - 1) / ((1 + x ** 4) * (1 + x ** 5)))
m3 = (sp.simplify(lead - 6 / (1 + x ** 5)) == 0 and sp.simplify(beta - beta_t) == 0
      and sp.simplify(gamma - gamma_t) == 0 and sp.simplify(beta_a - beta_a_t) == 0
      and sp.simplify(E.subs(x, 1) - 3 * Lsym ** 2) == 0)
p, q, r = sp.symbols("p q r", positive=True)
neutral = sp.simplify((6 * p / (p + q + 4 * r) - 1) * (p + q + 4 * r) - (5 * p - q - 4 * r)) == 0
ok("M3", m3 and neutral,
   "beta and gamma factor as stated and carry sign(x-1); at x=1, E=3 L^2; a1's linear coefficient vanishes on x^5-2x^4-1=0; "
   "c0 p>1 iff 5p>q+4r")


def diffs(kind, pp, qq, rr, frac, Lmax=200):
    c0 = Fr(6, pp + qq + 4 * rr)
    xx = c0 * pp
    A1 = pp + qq + 4 * rr
    zc = 1 / (c0 * A1 * (1 + xx ** 5))
    out = []
    for n in range(2, Lmax + 1):
        if kind == "def":
            Ev = Fr(24) / (1 + xx ** 3) + Fr(24) * (n - 2) / (1 + xx ** 4) + Fr(6) * (n - 2) ** 2 / (1 + xx ** 5)
        else:
            Ev = Fr(8) / (1 + xx ** 3) + Fr(12) * (n - 2) / (1 + xx ** 4) + Fr(6) * (n - 2) ** 2 / (1 + xx ** 5)
        G = 6 * frac * n * n / (1 + xx ** 5)
        out.append(G - Ev)
    signs = [1 if d > 0 else -1 for d in out]
    flips = [n for n in range(2, Lmax) if signs[n - 2] != signs[n - 1]]
    return zc, signs, flips


zc, s9, f9 = diffs("def", 3, 1, 2, Fr(9, 10))
_, a9, fa9 = diffs("a1", 3, 1, 2, Fr(9, 10))
_, s1, f1 = diffs("def", 3, 1, 2, Fr(1))
_, a1s, fa1 = diffs("a1", 3, 1, 2, Fr(1))
_, s11, f11 = diffs("def", 3, 1, 2, Fr(11, 10))
_, a11, fa11 = diffs("a1", 3, 1, 2, Fr(11, 10))
_, s20, f20 = diffs("def", 20, 1, 1, Fr(3, 2))
_, a20, fa20 = diffs("a1", 20, 1, 1, Fr(3, 2))
_, s12, f12 = diffs("def", 1, 1, 2, Fr(99, 100))
m4 = (zc == Fr(16, 825) and all(v < 0 for v in s9) and fa9 == [10] and a9[0] > 0
      and all(v < 0 for v in s1) and all(v > 0 for v in a1s)
      and f11 == [17] and s11[0] < 0 and s11[-1] > 0 and all(v > 0 for v in a11)
      and fa20 == [13] and f20 == [33] and s20[0] < 0 and s20[-1] > 0
      and f12 == [18] and s12[0] > 0 and s12[-1] < 0)
ok("M4", m4,
   f"z_c(3,1,2)={zc}; (9/10) def always shrinks, a1 flips {fa9}; z_c def shrinks, a1 grows; "
   f"(11/10) def flips {f11}; (20,1,1) def {f20} a1 {fa20}; (1,1,2) def {f12}")

# ---------- M5. facet layers ----------
FACETS = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 1, 1), (2, 2, 1), (3, 1, 0), (3, 1, 1),
          (3, 2, 0), (3, 2, 1), (3, 2, 2), (3, 3, 1), (3, 3, 2), (4, 1, 0), (4, 3, 0), (5, 3, 1),
          (0, -2, 1), (-1, 2, -3), (2, -5, 3)]
good = True
for nvec in FACETS:
    order = sorted((abs(v) for v in nvec), reverse=True)
    h, k, l = order
    axis = max(range(3), key=lambda i: abs(nvec[i]))
    outward = tuple((1 if nvec[axis] > 0 else -1) if i == axis else 0 for i in range(3))

    def dot(v, nvec=nvec):
        return v[0] * nvec[0] + v[1] * nvec[1] + v[2] * nvec[2]

    layers, growth = {}, {}
    for s in itertools.product(range(-4, 5), repeat=3):
        if dot(s) <= 0:
            empty = [d for d in NB if dot(add(s, d)) > 0]
            if not empty:
                continue
            ks = 6 - len(empty)
            dest = []
            for d in empty:
                t = add(s, d)
                kt = sum(dot(add(t, e)) <= 0 and add(t, e) != s for e in NB)
                dest.append((d, kt))
            layers.setdefault(-dot(s), set()).add((ks, tuple(d for d, kt in dest if kt == 0), tuple(sorted(kt for _, kt in dest))))
        else:
            j = sum(dot(add(s, e)) <= 0 for e in NB)
            if j:
                growth.setdefault(dot(s), set()).add(j)
    good &= sorted(layers) == list(range(h)) and sorted(growth) == list(range(1, h + 1))
    for m, props in layers.items():
        good &= len(props) == 1
        ks, iso, kts = next(iter(props))
        good &= ks == 3 + sum(v <= m for v in order)
        good &= iso == ((outward,) if m < h - k else ())
        for mm, js in growth.items():
            good &= js == {sum(v >= mm for v in order)}
ok("M5", good, "19 normals, |coord|<=4: a record in layer m < h-k leaves along exactly one bond, and a tied facet (h=k) has no such layer")

# ---------- M6. octahedron proof-check and dodecahedron census ----------
good = True
for R in range(1, 9):
    dep = [(s, t, ks, kt) for s, t, ks, kt in bonds(octa(R)) if kt == 0]
    tips = []
    for ax in range(3):
        for sg in (1, -1):
            s = [0, 0, 0]
            s[ax] = sg * R
            tips.append(tuple(s))
    good &= sorted(s for s, *_ in dep) == sorted(tips) and all(ks == 1 and kt == 0 for _, _, ks, kt in dep) and len(dep) == 6
# dodecahedron one-move departures: 6 tips plus 12R (even) or 12(R-1) (odd), checked R=2..8
def growth(S):
    touch = {add(s, d) for s in S for d in NB} - S
    return Counter(sum(add(t, e) in S for e in NB) for t in touch)


for R in range(2, 9):
    dep = [row for row in bonds(dodec(R)) if row[3] == 0]
    want = 6 + (12 * R if R % 2 == 0 else 12 * (R - 1))
    good &= len(dep) == want
    g_oct = growth(octa(R))
    good &= g_oct[1] == 6 and g_oct[2] == 12 * R and g_oct[3] == 4 * R * R - 4 * R
    g_dod = growth(dodec(R))
    if R % 2 == 0:
        good &= g_dod[1] == 12 * R + 6 and g_dod[2] == 6 * R * R and 3 not in g_dod
    else:
        good &= g_dod[1] == 12 * R - 6 and g_dod[2] == 6 * R * R + 6 and 3 not in g_dod
ok("M6", good, "octahedron: only the 6 tips leave in one move, R=1..8, and growth is 6+12R+(4R^2-4R); "
   "dodecahedron departures are 6+12R or 6+12(R-1) and growth is quadratic, R=2..8")

# ---------- M7. two moves, and the static weight is x^{-k_s} ----------
good = True
for nvec, ks_want, kt_want in (((1, 1, 1), 3, 2), ((1, 1, 0), 4, 1), ((1, 0, 0), 5, 0), ((2, 2, 1), 3, 1), ((3, 3, 1), 3, 1)):
    def inside(v, nvec=nvec):
        return v[0] * nvec[0] + v[1] * nvec[1] + v[2] * nvec[2] <= 0

    s = (0, 0, 0)
    ks = sum(inside(add(s, d)) for d in NB)
    found = []
    for d in NB:
        t = add(s, d)
        if inside(t):
            continue
        kt = sum(inside(add(t, e)) and add(t, e) != s for e in NB)
        for e in NB:
            u = add(t, e)
            if u == s:
                continue
            if sum(inside(add(u, f)) for f in NB) == 0 and any(add(u, f) == t for f in NB):
                found.append(kt)
    good &= ks == ks_want and kt_want in found
    hop = sp.simplify(x ** kt_want / (x ** ks + x ** kt_want))
    if nvec == (1, 1, 1):
        good &= hop == 1 / (1 + x)
    if nvec == (1, 1, 0):
        good &= hop == 1 / (1 + x ** 3)
ok("M7", good, "top layer of (111),(110),(100),(221),(331): two moves reach an isolated site; hop probability 1/(1+x) on (111) and 1/(1+x^3) on (110); static weight x^{-k_s}")

# ---------- M8. one move reaches twice the projected area; depth 1 enters the law ----------
def proj_area(S):
    return sum(len({tuple(v for i, v in enumerate(s) if i != ax) for s in S}) for ax in range(3))


good = True
for kind, builder in (("box", box), ("oct", octa), ("dod", dodec)):
    for n in (2, 3, 4, 5):
        S = builder(n)
        reached = set()
        n_bonds = 0
        for s, t, _, _ in bonds(S):
            n_bonds += 1
            reached.add(frozenset((S - {s}) | {t}))
        good &= len(reached) == n_bonds == 2 * proj_area(S)


def law(content, pp, qq, rr, cc):
    def omega(a, b):
        return pp if a == b else (qq if a == (b ^ 1) else rr)

    out = []
    for s, a in content.items():
        for d in NB:
            t = add(s, d)
            if t in content:
                continue
            ws, wt = 1, 1
            for e in NB:
                u = add(s, e)
                if u in content:
                    ws *= cc * omega(a, content[u])
            for e in NB:
                u = add(t, e)
                if u in content and u != s:
                    wt *= cc * omega(a, content[u])
            out.append(((s, t), Fr(wt, ws + wt)))
    return tuple(sorted(out))


for n, site, expect_three in ((3, (1, 1, 1), True), (4, (1, 1, 1), True), (5, (1, 2, 2), True), (5, (2, 2, 2), False)):
    laws = []
    for b in (0, 1, 2):
        cont = {s: 0 for s in box(n)}
        cont[site] = b
        laws.append(law(cont, 3, 1, 2, Fr(1, 2)))
    good &= (len(set(laws)) == 3) if expect_three else (len(set(laws)) == 1)
ok("M8", good, "one move reaches 2(|pi_x|+|pi_y|+|pi_z|) distinct arrangements on box, octahedron and dodecahedron, sizes 2..5; "
   "at (3,1,2) a depth-1 content changes the surface law and the 5-box centre does not")

if FAILS:
    print("SUMMARY: fails at step " + ", ".join(FAILS) + " - independent check disagreed")
    sys.exit(1)
print("SUMMARY: confirmed - per-bond box evaporation, the cp=1 threshold, the facet leaving rule, and the two-move weight all survive independent enumeration.")
print("HIT: confirmed - with every occupied-empty bond visited once, the box evaporates at E(L)=24/(1+x^3)+24(L-2)/(1+x^4)+6(L-2)^2/(1+x^5), whose finite-size terms have the sign of x-1, so the stable-size/nucleation switch is at cp=1 (5p=q+4r at the neutral scale), not at a one-attempt-per-record threshold; at (3,1,2), z_c=16/825, the two counts disagree, and (11/10)z_c is repelling between L=17 and 18. A facet with sorted |normal|(h,k,l) lets only layers m<h-k leave in one move, so tied facets and all but the octahedron's 6 tips do not; those records leave in two moves at static weight x^{-k_s}. One move reaches twice the sum of the projection areas, and the move law reads depth 1 only.")
