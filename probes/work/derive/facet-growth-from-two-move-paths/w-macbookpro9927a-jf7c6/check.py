#!/usr/bin/env python3
"""check.py for J:derive:facet-growth-from-two-move-paths:a1 (worker w-macbookpro9927a-jf7c6, claude-opus-5-5).

Setting (block 39 as landed; block 127's accounting). Aligned records on Z^3; x = cp is the weight of a record-record
bond and a bond with an empty end weighs 1. Every bond with exactly one occupied end is visited at rate 1, and the record
at s moves to the empty end t with probability x^{k_t}/(x^{k_s} + x^{k_t}); k_s and k_t count the recorded neighbours of s
other than t and of t other than s. A record that reaches an isolated site (no recorded neighbour) has left.
Held-shape first passage: after a first hop s -> t the moved record keeps moving, with the rest of the shape held (s stays
empty, no other record moves), until it reaches an isolated site (departure) or s (return). E_F = departure rate per
surface record of the ideal facet F; formation z Z_x at an empty site with j aligned recorded neighbours, Z_x = c^j A_j.

Families
  Q  pinned sources (block 39 on main; block 127 on its branch; the task)
  A  facet departure rates, exact: (100) 1/(1+x^5) (one move); (111) 9/(x^3+4x+3) (exactly two moves); (110) with
     sigma = sqrt(x^2+2): E = 4(sigma+x^2+2x)/((x^4+3x^3+2)sigma + 3x^5+5x^4+2x^2+4x) (first hop, then a walk along the
     groove): lattice first passage at rational x, the infinite groove bracketed by capped chains; the groove solution
     symbolically; the strict two-move part 4/((x+1)(3x^3+2)); pathwise balance x^{-k_s}; the Metropolis contrast
  B  growth law per facet: one touching site per surface record, with j = 1, 2, 3; net rate per surface record
     n_F = z c^j A_j - E_F, normal velocity n_F/|n|; critical rates at (3,1,2): 16/825, 4(1201 - 81 sqrt 17)/72475, 16/165
  C  clusters: octahedron E(R), G(R) closed forms (face, edge and tip classes) against the lattice; block 127's box against
     the lattice; the rhombic dodecahedron exactly per R; size-dependent critical rates E/G; turning sizes at z = 1/10 and
     1/20; kinetic-Wulff presence conditions and the thresholds z1 = 112/275, z2 = 8/11 - E_110
  N  [float] the facet ordering over a range of x; the critical-rate ordering along (p, 1, 2) at the neutral scale
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from fractions import Fraction as F
from math import isqrt

import numpy as np
import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []
ONLY = set(sys.argv[1:])


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


# ------------------------------------------------------------------ Q
N39 = ("docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE"
       "_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md")
N127 = ("docs/ADMISSIBILITY_RULE_ALIGNED_CLUSTERS_OF_MOVING_RECORDS_A_BOX_LOSES_RECORDS_BOND_BY_BOND_ITS_TURNING_SIZE"
        "_SWITCHES_AT_CP_EQUALS_ONE_AND_TIED_FACETS_NEED_TWO_MOVES_BOUNDED_THEOREM_NOTE_2026-09-24.md")
SRC = [("block39", "60c5f194d940a7bbaf1cdd545296e31d74a02f1a", N39,
        "38d4121f57b84241c1ca8c87d2396a08e1d4c34e554e65ac797ee70e55138d9f",
        ["- **Pair-weight transit.** A bond with exactly one occupied end is visited (bonds at any symmetric rates); the "
         "record, of content `a` at `x`, with `y` the empty end, has local weights `w_x = Π_{v∼x, v≠y, v∈η} W(a, s_v)` and "
         "`w_y` likewise at `y`; it moves with probability `w_y/(w_x + w_y)`",
         "- **Neutral scale.** `c₀ = 6/(p + q + 4r)`, so that `(1/6) Σ_b W(a, b) = 1` for every `a`.",
         "so `λ = zZ_x` and no other rate."], "main"),
       ("block127", "2cc2429c48b374d727fcb22f4722ddb8ddb5b4b3", N127,
        "a8ff1413a6114df43362589311a648b85cdb2489ea7bb66825752201d75f38a2",
        ["  - On `(111)` it reaches an isolated site in two moves. The first is a hop of probability `1/(1+x)` to a site "
         "with two recorded neighbours. On `(110)` that hop has probability `1/(1+x³)`.",
         "- **Rate convention.** Every bond is visited at rate `1`.",
         "  - `E` counts moves to an isolated site; the departed record has left the cluster.",
         "  - Formation at the touching sites gives `G = 6zcA₁L²`.",
         "Open: a growth law from two-move paths."],
        "physics-loop/admissibility-induced-law-block127-aligned-clusters-of-moving-records-turning-size-switches-at-cp-one-20260924")]
TASKQ = ("61392c8874c5ba4d96f3f225679576e0b433a8bc", "J:derive:facet-growth-from-two-move-paths:a1",
         ["(a) the exact departure rate per unit area of the (111) and (110) facets from two-move paths (first passage to "
          "an isolated site), as functions of x;",
          "(b) the growth law per facet with formation z Z_x;",
          "(c) the facet whose turning size is largest, and the resulting shape of a growing aligned cluster (compare the box).",
          "HIT: (a)-(b) exact for one tied facet."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or spec.split(":")[0]], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, c, p, h, quotes, br in SRC:
        b = git_show(f"{c}:{p}", br)
        if b is None:
            rep("Q", False, f"{tag} unreadable")
            return
        good = hashlib.sha256(b).hexdigest() == h
        n = sum(q in b.decode() for q in quotes)
        ok &= good and n == len(quotes)
        msg.append(f"{tag}@{c[:8]} {'sha ok' if good else 'SHA MISMATCH'} {n}/{len(quotes)}")
    b = git_show(f"{TASKQ[0]}:probes/TASKS.json", "ai/probes")
    what = next((t["what"] for t in json.loads(b.decode()) if t["id"] == TASKQ[1]), "") if b else ""
    n = sum(q in what for q in TASKQ[2])
    ok &= n == len(TASKQ[2])
    msg.append(f"task@{TASKQ[0][:8]} {n}/{len(TASKQ[2])}")
    rep("Q", ok, "; ".join(msg))


# ------------------------------------------------------------------ lattice machinery (exact)
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def nbrs(v):
    return [(v[0] + d[0], v[1] + d[1], v[2] + d[2]) for d in DIRS]


def kcount(occ, v, exclude):
    return sum(1 for w in nbrs(v) if w != exclude and occ(w))


def heat_bath(ku, kw, x):
    return x ** kw / (x ** ku + x ** kw)


def metropolis(ku, kw, x):
    return min(F(1), x ** kw / x ** ku)


def move_prob(occ, u, w, x, acc=heat_bath):
    """the moving record sits at u (not in occ); w is empty."""
    return acc(kcount(occ, u, w), kcount(occ, w, u), x)


def solve(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * bb for a, bb in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def escape_prob(occ, s, t, x, cap=None, bval=F(0), acc=heat_bath, two_move=False):
    """P(the record now at t reaches an isolated site before s), held shape occ (s already removed).
    cap: sites farther than cap (sup-norm from s) are absorbing with value bval. two_move: only the next move counts."""
    if kcount(occ, t, None) == 0:
        return F(1)
    if two_move:
        esc = tot = F(0)
        for w in nbrs(t):
            if occ(w):
                continue
            pr = move_prob(occ, t, w, x, acc)
            tot += pr
            if w != s and kcount(occ, w, None) == 0:
                esc += pr
        return esc / tot
    order, idx, stack = [t], {t: 0}, [t]
    while stack:
        u = stack.pop()
        for w in nbrs(u):
            if w == s or occ(w) or w in idx or kcount(occ, w, None) == 0:
                continue
            if cap is not None and max(abs(w[i] - s[i]) for i in range(3)) > cap:
                continue
            idx[w] = len(order)
            order.append(w)
            stack.append(w)
    n = len(order)
    A = [[F(0)] * n for _ in range(n)]
    b = [F(0)] * n
    for i, u in enumerate(order):
        tot = F(0)
        for w in nbrs(u):
            if occ(w):
                continue
            pr = move_prob(occ, u, w, x, acc)
            tot += pr
            if w == s:
                continue
            if kcount(occ, w, None) == 0:
                b[i] += pr
            elif w in idx:
                A[i][idx[w]] -= pr
            else:
                b[i] += pr * bval
        A[i][i] += tot
    return solve(A, b)[0]


def facet_E(normal, x, **kw):
    """departure rate of the surface record at the origin of the facet {n.v <= 0}."""
    s = (0, 0, 0)
    occ = lambda v: v != s and sum(normal[i] * v[i] for i in range(3)) <= 0
    E = F(0)
    for t in nbrs(s):
        if occ(t):
            continue
        E += move_prob(occ, s, t, x, kw.get("acc", heat_bath)) * escape_prob(occ, s, t, x, **kw)
    return E


def E110_closed(x, sigma):
    return 4 * (sigma + x ** 2 + 2 * x) / ((x ** 4 + 3 * x ** 3 + 2) * sigma + 3 * x ** 5 + 5 * x ** 4 + 2 * x ** 2 + 4 * x)


def sqrt_bounds(v, digits=40):
    D = 10 ** digits
    n = v.numerator * D * D // v.denominator
    lo = isqrt(n)
    return F(lo, D), F(lo + 1, D)


# ------------------------------------------------------------------ A
def fam_A():
    t0 = time.time()
    xs = [F(1, 3), F(1, 2), F(1), F(3, 2), F(2), F(3), F(5)]
    ok100 = all(facet_E((0, 0, 1), x) == 1 / (1 + x ** 5) for x in xs)
    ok111 = all(facet_E((1, 1, 1), x) == F(9) / (x ** 3 + 4 * x + 3) for x in xs)
    rep("A", ok100 and ok111, f"lattice first passage at x in {[str(v) for v in xs]}: E(100) = 1/(1+x^5) (one move), "
        f"E(111) = 9/(x^3+4x+3) (every first hop, prob 1/(1+x), leads to a site whose only moves are back or to an isolated "
        f"site): {ok100}, {ok111}")

    # (110): capped chains bracket the infinite groove; the closed form lies inside, widths shrink
    okb, widths = True, []
    for x in (F(1, 2), F(1), F(3, 2), F(2), F(3)):
        slo, shi = sqrt_bounds(x * x + 2)
        c_lo, c_hi = E110_closed(x, shi), E110_closed(x, slo)          # E decreasing in sigma
        w = []
        for cap in (8, 16, 32):
            lo = facet_E((1, 1, 0), x, cap=cap, bval=F(0))
            hi = facet_E((1, 1, 0), x, cap=cap, bval=F(1))
            okb &= lo <= c_lo and c_hi <= hi
            w.append(float(hi - lo))
        okb &= w[0] > w[1] > w[2] and w[2] < 1e-8
        widths.append(w[2])
    x_, sg = sp.symbols("x sigma", positive=True)
    S = sp.sqrt(x_ ** 2 + 2)
    mu = (S - 1) / (S + 1)
    al, be = 1 / (1 + x_), 2 / (1 + x_ ** 2)
    rho1 = (S - 1) / (S + x_)
    Phi = 1 + x_ * (1 - rho1)
    f0 = 2 * al * Phi / (x_ ** 3 / (1 + x_ ** 3) + 2 * al * Phi)
    sym = [sp.simplify(mu ** 2 - 2 * (1 + be) * mu + 1),                                   # groove root
           sp.simplify(rho1 * (sp.Rational(1, 2) + al + be) - (sp.Rational(1, 2) * rho1 * mu + al)),   # site next to g0
           sp.simplify(2 / (1 + x_ ** 3) * f0 - E110_closed(x_, S)),                        # assembly
           sp.factor(3 * x_ ** 5 + 5 * x_ ** 4 + 2 * x_ ** 2 + 4 * x_ - (x_ ** 2 + 2 * x_) * (x_ ** 4 + 3 * x_ ** 3 + 2)) + x_ ** 4 * (x_ + 1) ** 2]
    oksym = all(v == 0 for v in sym)
    ok2 = all(facet_E((1, 1, 0), x, two_move=True) == F(4) / ((x + 1) * (3 * x ** 3 + 2)) for x in xs)
    e32 = E110_closed(sp.Rational(3, 2), sp.sqrt(sp.Rational(17, 4)))
    okv = sp.simplify(e32 - (2402 - 162 * sp.sqrt(17)) / 5575) == 0
    okv &= sp.simplify(E110_closed(sp.Integer(1), sp.sqrt(3)) - 2 * sp.sqrt(3) / (1 + 2 * sp.sqrt(3))) == 0
    okv &= sp.limit(E110_closed(x_, S) * x_ ** 3, x_, sp.oo) == 1 and sp.limit(9 * x_ ** 3 / (x_ ** 3 + 4 * x_ + 3), x_, sp.oo) == 9
    rep("A", okb and oksym and ok2 and okv,
        f"(110): capped chains (cap 8, 16, 32; boundary as return or as escape) bracket the closed form at x in "
        f"(1/2,1,3/2,2,3), widths at cap 32 <= {max(widths):.1e}; groove solution mu = (sigma-1)/(sigma+1), "
        f"rho1 = (sigma-1)/(sigma+x), assembly exact (sympy); strict two-move part 4/((x+1)(3x^3+2)) at 7 points; "
        f"E(110)(3/2) = (2402 - 162 sqrt 17)/5575 = {float(e32):.10f}; E(110)(1) = 2 sqrt3/(1+2 sqrt3); x^3 E -> 1 (110), 9 (111)")

    # pathwise balance: forward/backward of every two-move departure path equals x^{-k_s}
    okbal, npaths = True, 0
    for normal in ((1, 1, 1), (1, 1, 0)):
        s = (0, 0, 0)
        occ = lambda v, n=normal: v != s and sum(n[i] * v[i] for i in range(3)) <= 0
        ks = kcount(occ, s, None)
        for x in (F(2, 3), F(3, 2), F(3)):
            for t in nbrs(s):
                if occ(t):
                    continue
                Qt = sum(move_prob(occ, t, w, x) for w in nbrs(t) if not occ(w))
                for u in nbrs(t):
                    if occ(u) or u == s or kcount(occ, u, None) != 0:
                        continue
                    fwd = move_prob(occ, s, t, x) * move_prob(occ, t, u, x) / Qt
                    bwd = move_prob(occ, u, t, x) * move_prob(occ, t, s, x) / Qt
                    okbal &= fwd / bwd == x ** (-ks)
                    npaths += 1
    # acceptance dependence: Metropolis gives E(111) = 9/(x(x^2+3)) for x >= 1
    okm = all(facet_E((1, 1, 1), x, acc=metropolis) == F(9) / (x * (x * x + 3)) for x in (F(1), F(3, 2), F(2), F(3)))
    rep("A", okbal and okm, f"{npaths} two-move paths on (111) and (110): forward/backward = x^(-k_s) exactly (k_s = 3, 4); "
        f"with the Metropolis acceptance block 39 also allows, E(111) = 9/(x(x^2+3)) for x >= 1: rates depend on the "
        f"acceptance, balance ratios do not  ({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ B
PQR = (3, 1, 2)
C0 = F(6, PQR[0] + PQR[1] + 4 * PQR[2])                     # neutral scale, 1/2
XN = C0 * PQR[0]                                           # 3/2
ZJ = {j: C0 ** j * (PQR[0] ** j + PQR[1] ** j + 4 * PQR[2] ** j) for j in range(7)}


def fam_B():
    ok_touch, js = True, {}
    for normal, jexp in (((0, 0, 1), 1), ((1, 1, 0), 2), ((1, 1, 1), 3)):
        occ = lambda v, n=normal: sum(n[i] * v[i] for i in range(3)) <= 0
        W = 4
        box = [(a, b, c) for a in range(-W, W + 1) for b in range(-W, W + 1) for c in range(-W, W + 1)]
        surf = [v for v in box if occ(v) and any(not occ(w) for w in nbrs(v))]
        touch = [v for v in box if not occ(v) and any(occ(w) for w in nbrs(v))]
        # the map v -> v + e (e the unit vector along a positive normal component) is a bijection surf -> touch
        e = next(DIRS[2 * i] for i in range(3) if normal[i] > 0)
        img = {(v[0] + e[0], v[1] + e[1], v[2] + e[2]) for v in surf}
        inner = [v for v in touch if max(map(abs, v)) <= W - 1]
        ok_touch &= all(v in img for v in inner) and all(not occ(w) and any(occ(y) for y in nbrs(w)) for w in img)
        jset = {sum(1 for w in nbrs(v) if occ(w)) for v in touch}
        js[normal] = jset
        ok_touch &= jset == {jexp} and all(not occ(v) and sum(1 for w in nbrs(v) if occ(w)) == 0
                                           for v in box if not occ(v) and v not in touch)
    e100, e111 = 1 / (1 + XN ** 5), F(9) / (XN ** 3 + 4 * XN + 3)
    zc100, zc111 = e100 / ZJ[1], e111 / ZJ[3]
    e110 = (2402 - 162 * sp.sqrt(17)) / 5575
    zc110 = e110 / sp.Rational(ZJ[2].numerator, ZJ[2].denominator)
    ok_vals = zc100 == F(16, 825) and zc111 == F(16, 165) and sp.simplify(zc110 - 4 * (1201 - 81 * sp.sqrt(17)) / 72475) == 0
    ok_order = bool(sp.Rational(16, 825) < zc110) and bool(zc110 < sp.Rational(16, 165))
    rep("B", ok_touch and ok_vals and ok_order,
        f"one touching site per surface record (v -> v + e), with j = 1, 2, 3 recorded neighbours on (100), (110), (111); "
        f"no other empty site touches; net rate per surface record n_F = z c^j A_j - E_F, velocity n_F/|n|; at (3,1,2), "
        f"c = 1/2, x = 3/2: Z = 6, 13/2, 15/2; z_c = E_F/Z_F = 16/825 (block 127's), 4(1201 - 81 sqrt 17)/72475 = "
        f"{float(zc110):.6f}, 16/165: ordered (100) < (110) < (111)")


# ------------------------------------------------------------------ C
def cluster_EG(occ0, sites, x, Z):
    occset = {v for v in sites if occ0(v)}
    E, touching = F(0), set()
    for s in occset:
        occ = lambda v, s=s: v != s and v in occset
        for t in nbrs(s):
            if t in occset:
                continue
            touching.add(t)
            E += move_prob(occ, s, t, x) * escape_prob(occ, s, t, x)
    G = sum((Z[sum(1 for w in nbrs(t) if w in occset)] for t in touching), F(0))
    return E, G, len(occset)


def cube(R, lo=None):
    lo = -R - 2 if lo is None else lo
    rng = range(lo, R + 3)
    return [(a, b, c) for a in rng for b in rng for c in rng]


def oct_forms(x, Z):
    e3 = F(9) / (x ** 3 + 4 * x + 3)
    e2 = F(8) / ((1 + x) * (4 + x)) + F(6) / (7 + x ** 2)
    e1 = 1 / (1 + x) + F(16) / (9 + x)
    E = lambda R: 4 * (R - 1) * (R - 2) * e3 + 12 * (R - 1) * e2 + 6 * e1
    G = lambda R: 4 * R * (R - 1) * Z[3] + 12 * R * Z[2] + 6 * Z[1]
    return E, G, (e1, e2, e3)


def fam_C():
    t0 = time.time()
    ok_oct = True
    for x, Rmax in ((XN, 8), (F(2, 3), 5), (F(5, 2), 5)):
        Z = {j: ZJ[j] for j in ZJ}
        Eo, Go, _ = oct_forms(x, Z)
        for R in range(1, Rmax + 1):
            E, G, _ = cluster_EG(lambda v, R=R: abs(v[0]) + abs(v[1]) + abs(v[2]) <= R, cube(R), x, Z)
            ok_oct &= E == Eo(R) and G == Go(R)
    Ebox = lambda L: 24 / (1 + XN ** 3) + 24 * (L - 2) / (1 + XN ** 4) + 6 * (L - 2) ** 2 / (1 + XN ** 5)
    ok_box = True
    for L in range(2, 7):
        E, G, _ = cluster_EG(lambda v, L=L: all(0 <= v[i] < L for i in range(3)), cube(L, -2), XN, ZJ)
        ok_box &= E == Ebox(L) and G == 6 * L * L * ZJ[1]
    rep("C", ok_oct and ok_box, "octahedron |v|_1 <= R: E(R) = 4(R-1)(R-2)e3 + 12(R-1)e2 + 6e1 with e3 = 9/(x^3+4x+3), "
        "e2 = 8/((1+x)(4+x)) + 6/(7+x^2), e1 = 1/(1+x) + 16/(9+x), G(R)/z = 4R(R-1)Z3 + 12R Z2 + 6Z1, equal to the lattice "
        "first passage at x = 3/2 (R<=8), 2/3 and 5/2 (R<=5); block 127's box E(L) equal to it (L = 2..6): all its "
        f"departures are one move  ({time.time() - t0:.0f}s)")

    # critical rates E/G per size, and turning sizes
    Eo, Go, (e1, e2, e3) = oct_forms(XN, ZJ)
    Gbox = lambda L: 6 * L * L * ZJ[1]
    dod = {}
    for R in range(1, 11):
        d = lambda v, R=R: abs(v[0]) + abs(v[1]) <= R and abs(v[1]) + abs(v[2]) <= R and abs(v[0]) + abs(v[2]) <= R
        E, G, N = cluster_EG(d, cube(R), XN, ZJ)
        dod[R] = (E, G, N)
    zo = [Eo(R) / Go(R) for R in range(1, 11)]
    zd = [dod[R][0] / dod[R][1] for R in range(1, 11)]
    zb = [Ebox(L) / Gbox(L) for L in range(2, 12)]
    order = all(zo[i] > zd[i] for i in range(1, 10)) and zo[0] == zd[0] and max(zd[1:]) < min(zo) and max(zb) < min(zd[1:])
    # z = 1/10: octahedron turns between R = 12 and 13 and grows beyond (positive leading coefficient); box and
    # dodecahedron grow at every computed size. z = 1/20: octahedron shrinks at every size (negative leading
    # coefficient and negative maximum); dodecahedron sign pattern; box grows at every size.
    z = F(1, 10)
    net_o = lambda R, z: z * Go(R) - Eo(R)
    a2 = 4 * (z * ZJ[3] - e3)
    turn = [R for R in range(1, 60) if net_o(R, z) < 0 < net_o(R + 1, z)]
    ok10 = a2 > 0 and turn == [12] and all(net_o(R, z) > 0 for R in range(13, 200)) \
        and all(z * dod[R][1] - dod[R][0] > 0 for R in range(2, 11)) and all(z * Gbox(L) - Ebox(L) > 0 for L in range(2, 200))
    z = F(1, 20)
    a2b = 4 * (z * ZJ[3] - e3)
    b1 = -4 * z * ZJ[3] + 12 * z * ZJ[2] + 12 * e3 - 12 * e2
    c0 = 6 * z * ZJ[1] - 8 * e3 + 12 * e2 - 6 * e1
    oct_neg = a2b < 0 and (b1 * b1 < 4 * a2b * c0 or all(net_o(R, z) < 0 for R in range(1, 200)))
    dsign = ''.join('+' if z * dod[R][1] - dod[R][0] > 0 else '-' for R in range(1, 11))
    ok20 = oct_neg and all(z * Gbox(L) - Ebox(L) > 0 for L in range(2, 200))
    rep("C", order and ok10 and ok20,
        f"E/G at x = 3/2, (3,1,2): octahedron {[round(float(v), 4) for v in zo[:6]]}.. -> 16/165; dodecahedron "
        f"{[round(float(v), 4) for v in zd[:6]]}.. -> {4 * (1201 - 81 * 17 ** 0.5) / 72475:.4f}; box "
        f"{[round(float(v), 4) for v in zb[:5]]}.. -> 16/825 [floats shown, comparisons exact]; octahedron highest at every "
        f"size; z = 1/10: octahedron turns between R = 12 and 13, box and dodecahedron grow at every size computed; z = 1/20: "
        f"octahedron shrinks at every size, dodecahedron signs R=1..10 '{dsign}', box grows")

    # kinetic-Wulff presence conditions from per-record net rates, and the thresholds at (3,1,2)
    e100, e111 = 1 / (1 + XN ** 5), F(9) / (XN ** 3 + 4 * XN + 3)
    z1 = (e111 - e100) / (ZJ[3] - ZJ[1])
    s17 = sp.sqrt(17)
    e110 = (2402 - 162 * s17) / 5575
    z2 = sp.Rational(e111.numerator, e111.denominator) - e110           # (Z3 - Z2) = 1
    z110_100 = (e110 - sp.Rational(e100.numerator, e100.denominator)) / sp.Rational(1, 2)
    e100s, e111s = sp.Rational(e100.numerator, e100.denominator), sp.Rational(e111.numerator, e111.denominator)
    always = [e111s - 3 * e100s, e111s - sp.Rational(3, 2) * e110, e110 - 2 * e100s]   # (111) at every z; (110) vs (100)
    okw = z1 == F(112, 275) and bool(z110_100 < sp.Rational(112, 275)) and bool(sp.Rational(112, 275) < z2) \
        and all(bool(v > 0) for v in always)
    # the presence rules follow from the facet's central point: n.c_F compared with the other planes (exact algebra)
    n100, n110, n111 = sp.symbols("n100 n110 n111", positive=True)
    c111 = sp.Matrix([1, 1, 1]) * (n111 / sp.sqrt(3)) / sp.sqrt(3)
    c110 = sp.Matrix([1, 1, 0]) * (n110 / sp.sqrt(2)) / sp.sqrt(2)
    c100 = sp.Matrix([1, 0, 0]) * n100
    rules = [sp.simplify(c111.dot(sp.Matrix([1, 0, 0])) - n100 - (n111 / 3 - n100)),
             sp.simplify(c111.dot(sp.Matrix([1, 1, 0]) / sp.sqrt(2)) - n110 / sp.sqrt(2) - (sp.sqrt(2) / 3 * n111 - n110 / sp.sqrt(2))),
             sp.simplify(c110.dot(sp.Matrix([1, 0, 0])) - n100 - (n110 / 2 - n100)),
             sp.simplify(c110.dot(sp.Matrix([1, 1, 1]) / sp.sqrt(3)) - n111 / sp.sqrt(3) - ((n110 - n111) / sp.sqrt(3))),
             sp.simplify(c100.dot(sp.Matrix([1, 1, 0]) / sp.sqrt(2)) - n110 / sp.sqrt(2) - ((n100 - n110) / sp.sqrt(2))),
             sp.simplify(c100.dot(sp.Matrix([1, 1, 1]) / sp.sqrt(3)) - n111 / sp.sqrt(3) - ((n100 - n111) / sp.sqrt(3)))]
    okr = all(v == 0 for v in rules)
    rep("C", okw and okr, f"kinetic Wulff (planes at n_F/|n| along the unit normals): (100) present iff n100 <= n110, n111; "
        f"(110) iff n110 <= 2 n100, n111; (111) iff n111 <= 3 n100, (3/2) n110 (sympy); at (3,1,2) (111) is present at every z "
        f"and the growth shape is an "
        f"octahedron for 16/165 < z < z1 = 112/275, (100) facets join at z1, (110) facets at z2 = 8/11 - E(110) = "
        f"{float(z2):.6f}  ({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ N
def fam_N():
    xs = np.linspace(0.05, 20, 2000)
    s = np.sqrt(xs ** 2 + 2)
    e110 = 4 * (s + xs ** 2 + 2 * xs) / ((xs ** 4 + 3 * xs ** 3 + 2) * s + 3 * xs ** 5 + 5 * xs ** 4 + 2 * xs ** 2 + 4 * xs)
    e111 = 9 / (xs ** 3 + 4 * xs + 3)
    e100 = 1 / (1 + xs ** 5)
    ordE = bool(np.all(e111 > e110) and np.all(e110 > e100))
    rows = []
    okz = True
    for p in np.linspace(1.5, 20, 400):
        c = 6 / (p + 1 + 8)
        x = c * p
        Z = [c ** j * (p ** j + 1 + 4 * 2 ** j) for j in range(4)]
        sx = np.sqrt(x * x + 2)
        E1 = 4 * (sx + x * x + 2 * x) / ((x ** 4 + 3 * x ** 3 + 2) * sx + 3 * x ** 5 + 5 * x ** 4 + 2 * x * x + 4 * x)
        zc = (1 / (1 + x ** 5) / Z[1], E1 / Z[2], 9 / (x ** 3 + 4 * x + 3) / Z[3])
        okz &= zc[0] < zc[1] < zc[2]
    rep("N", ordE and okz, f"[float] E(111) > E(110) > E(100) for x in [0.05, 20] (2000 points); along (p,1,2) at the "
        f"neutral scale, p in [1.5, 20] (400 points): z_c(100) < z_c(110) < z_c(111)")


if __name__ == "__main__":
    for tag, fn in (("Q", fam_Q), ("A", fam_A), ("B", fam_B), ("C", fam_C), ("N", fam_N)):
        if not ONLY or tag in ONLY:
            fn()
    print(f"total {time.time() - T0:.0f}s; failing families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + ",".join(sorted(set(FAILS))))
    else:
        print("SUMMARY: PARTIAL exact held-shape first-passage departure rates per surface record: (111) 9/(x^3+4x+3) "
              "(two moves exactly), (110) 4(s+x^2+2x)/((x^4+3x^3+2)s+3x^5+5x^4+2x^2+4x), s = sqrt(x^2+2) (first hop, "
              "then the groove); per unit area divide by sqrt3, sqrt2; growth law n_F = z c^j A_j - E_F (j = 3, 2, 1); "
              "octahedron closed forms; (111) turns last and bounds the kinetic growth shape up to z = 112/275 at (3,1,2)")
        print("HIT: for aligned moving records (block 39's transit, bonds visited at rate 1, x = cp), with the shape held "
              "while the moved record wanders: the (111) facet loses 9/(x^3+4x+3) records per surface site, exactly "
              "along two-move paths; the (110) facet loses 4(s+x^2+2x)/((x^4+3x^3+2)s+3x^5+5x^4+2x^2+4x), s = "
              "sqrt(x^2+2), a first hop followed by a walk along the groove; with formation z c^j A_j at the touching "
              "sites (j = 3 on (111), 2 on (110)) each facet advances iff z > E_F/(c^j A_j); at (3,1,2) the critical "
              "rates are 16/825 < 4(1201-81 sqrt17)/72475 < 16/165 for (100), (110), (111)")
