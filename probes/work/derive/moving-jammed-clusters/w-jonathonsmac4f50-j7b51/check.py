#!/usr/bin/env python3
"""J:derive:moving-jammed-clusters:a2 - worker w-jonathonsmac4f50-j7b51 (claude-opus-5-5).

Definitions (block 39, open PR 'ail39: records that move', note ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_..._2026-09-20.md, section
'Pair-weight transit'; supplied there as a hypothesis, not adopted): a site is empty or carries one record; a record carries its
content; neighbouring records weigh W = c*omega (omega = p, q, r for equal, opposite, orthogonal axes); a bond with an empty end
weighs 1.  'A bond with exactly one occupied end is visited (bonds at any symmetric rates); the record ... moves with probability
w_y/(w_x + w_y)', w_x (w_y) the product of the weights of the record's other bonds at its position x (at the empty end y).
The unit's simulator probes/lib/moving_gas.py visits every bond once per sweep.  Formation at an empty site x at rate z Z_x,
Z_x = c^j A_j next to j aligned records, A_j = p^j + q^j + 4 r^j (block 39 T4).  Throughout: all records of the cluster carry one
content, x = c p, and each bond is visited at rate 1 (a common rate lambda rescales every departure rate, hence z_c, and nothing else).
Prior attempt a1 (w-jonathonsmac4f50-j7b81, claude-opus-5, same model family as this worker, unrefereed) counted ONE departure
attempt per surface record; section A tests that count against the definition.  All arithmetic exact (integers, sympy rationals and rational functions).
"""
import itertools
from collections import Counter

import sympy as sp

RESULTS = []


def check(tag, ok, text, detail=''):
    RESULTS.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'} {tag} {text}" + (f" :: {detail}" if detail else ''))


NB = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def shape(kind, R):
    rng = range(-R - 1, R + 2)
    if kind == 'oct':
        return {s for s in itertools.product(rng, repeat=3) if abs(s[0]) + abs(s[1]) + abs(s[2]) <= R}
    if kind == 'dod':
        return {s for s in itertools.product(rng, repeat=3)
                if abs(s[0]) + abs(s[1]) <= R and abs(s[1]) + abs(s[2]) <= R and abs(s[2]) + abs(s[0]) <= R}
    return set(itertools.product(range(R), repeat=3))


def move_census(S):
    """Counter over occupied-empty bonds (s, t) of (k_s, k_t): recorded neighbours of s, and of t with s excluded."""
    out = Counter()
    for s in S:
        ks = sum(add(s, d) in S for d in NB)
        for d in NB:
            t = add(s, d)
            if t not in S:
                out[(ks, sum(add(t, e) in S for e in NB) - 1)] += 1
    return out


def growth_census(S):
    touching = {add(s, d) for s in S for d in NB} - S
    return Counter(sum(add(t, e) in S for e in NB) for t in touching)


x, c, p, q, r_, z, L = sp.symbols('x c p q r z L', positive=True)
A = lambda n: p ** n + q ** n + 4 * r_ ** n

# ================================================================ A. the box under the definition, against a1's count
E_def = 24 / (1 + x ** 3) + 24 * (L - 2) / (1 + x ** 4) + 6 * (L - 2) ** 2 / (1 + x ** 5)
E_a1 = 8 / (1 + x ** 3) + 12 * (L - 2) / (1 + x ** 4) + 6 * (L - 2) ** 2 / (1 + x ** 5)
ok = True
for n in range(2, 8):
    mc = move_census(shape('box', n))
    ok &= all(kt == 0 for (_, kt) in mc)                        # every move of a box record ends at an isolated position
    brute = sum(m * x ** kt / (x ** ks + x ** kt) for (ks, kt), m in mc.items())
    ok &= sp.simplify(brute - E_def.subs(L, n)) == 0
    ok &= sum(mc.values()) == 6 * n * n
check('A1', ok, "EXACT (L = 2..7, every occupied-empty bond of the L-box enumerated): every move of a box record ends at an "
      "isolated position, so the box's departure rate under the definition (each bond visited at rate 1) is "
      "E(L) = 24/(1+x^3) + 24(L-2)/(1+x^4) + 6(L-2)^2/(1+x^5): a corner record departs along 3 bonds, an edge record along 2, "
      "a face record along 1; a1's count 8/(1+x^3) + 12(L-2)/(1+x^4) + 6(L-2)^2/(1+x^5) gives every record one attempt")

# a1's count is not a rate law of the definition's class: detailed balance at a corner of the 2-box
S = shape('box', 2)
s0 = (1, 1, 1); t0 = (2, 1, 1)
S1 = (S - {s0}) | {t0}
ks = sum(add(s0, d) in S for d in NB)
kt = sum(add(t0, d) in (S1 - {t0}) for d in NB)                         # t0's recorded neighbours after the move
m_s = sum(add(s0, d) not in S for d in NB); m_t = sum(add(t0, d) not in S1 for d in NB)
mu_ratio = x ** kt / x ** ks                                            # static law mu(S1)/mu(S) = w_t/w_s (block 39 T1)
P_f = x ** kt / (x ** ks + x ** kt); P_b = x ** ks / (x ** ks + x ** kt)
flux_def = sp.simplify((1 * P_f) / (mu_ratio * 1 * P_b))               # every bond at rate 1
flux_a1 = sp.simplify((sp.Rational(1, m_s) * P_f) / (mu_ratio * sp.Rational(1, m_t) * P_b))   # one attempt per record, split over its empty bonds
ok = (ks, kt, m_s, m_t) == (3, 0, 3, 6) and flux_def == 1 and flux_a1 == 2
check('A2', ok, "EXACT: a1's count gives a corner record total departure rate 1/(1+x^3) over its three isolated destinations, "
      "i.e. its departure bonds at 1/3 of a face bond's rate; bond rates that depend only on the bond (the simulator's; any "
      "rate law invariant under lattice translations and rotations is one rate for all bonds) cannot do that; and block 39 T1 "
      "needs the visited bond's rate equal before and after the move - a corner record of the 2-box (3 recorded neighbours, "
      "3 empty) moving to an isolated site (6 empty neighbours) has forward/backward probability-flux ratio 1 with every bond "
      "at rate 1, and 2 when each record's one attempt is split over its empty bonds, so that realization of a1's count is "
      "not in detailed balance with the static law",
      f"(k_s, k_t, empty nbrs before, after) = {(ks, kt, m_s, m_t)}; flux ratios {flux_def}, {flux_a1}")

# the finite-size terms
G = 6 * z * c * A(1) * L ** 2
Ecoef = sp.Poly(sp.expand(E_def), L)
beta = sp.factor(sp.together(Ecoef.coeff_monomial(L)))
gamma = sp.factor(sp.together(Ecoef.coeff_monomial(1)))
lead = sp.simplify(Ecoef.coeff_monomial(L ** 2))
beta_target = 24 * x ** 4 * (x - 1) / ((1 + x ** 4) * (1 + x ** 5))
gamma_target = 24 * x ** 3 * (x - 1) ** 3 * (x + 1) * (x ** 2 + 1) / ((1 + x ** 3) * (1 + x ** 4) * (1 + x ** 5))
beta_a1 = sp.factor(sp.together(sp.Poly(sp.expand(E_a1), L).coeff_monomial(L)))
ok = sp.simplify(lead - 6 / (1 + x ** 5)) == 0 and sp.simplify(beta - beta_target) == 0 and sp.simplify(gamma - gamma_target) == 0
ok &= sp.simplify(E_def.subs(x, 1) - 3 * L ** 2) == 0
ok &= sp.simplify(beta_a1 - 12 * (x ** 5 - 2 * x ** 4 - 1) / ((1 + x ** 4) * (1 + x ** 5))) == 0
check('A3', ok, "EXACT: E(L) = 6L^2/(1+x^5) + beta L + gamma with beta = 24 x^4 (x-1)/((1+x^4)(1+x^5)) and "
      "gamma = 24 x^3 (x-1)^3 (x+1)(x^2+1)/((1+x^3)(1+x^4)(1+x^5)): both finite-size terms carry the sign of x - 1, and at "
      "x = 1 exactly E = 3L^2 (every bond's move has probability 1/2); a1's count gives beta_a1 = 12(x^5 - 2x^4 - 1)/((1+x^4)(1+x^5)) "
      "and the threshold x* = 2.05597; under the definition the threshold is x = cp = 1. With G = 6 z c A_1 L^2 and "
      "z_c = 1/(c A_1 (1+x^5)) (the same in both counts): for x > 1 a box shrinks at every size when z <= z_c and has one "
      "repelling critical size when z > z_c; for x < 1 it grows at every size when z >= z_c and has one attracting size when z < z_c",
      f"beta = {beta}; gamma = {gamma}")


def verdicts(E_expr, pp, qq, rr, frac, Lmax=200):
    c0 = sp.Rational(6, pp + qq + 4 * rr)
    sub = {c: c0, p: pp, q: qq, r_: rr, x: c0 * pp}
    zc = 1 / (c0 * A(1).subs(sub) * (1 + (c0 * pp) ** 5))
    diff = [sp.Rational((G - E_expr).subs(sub).subs(z, frac * zc).subs(L, n)) for n in range(2, Lmax + 1)]   # exact rationals
    signs = [1 if d > 0 else (-1 if d < 0 else 0) for d in diff]
    flips = [n for n in range(2, Lmax) if signs[n - 2] != signs[n - 1]]
    return zc, signs, flips


rows = []
ok = True
# (3,1,2): x = 3/2 > 1; a1's (9/10) z_c attracting size 10.768 and 'grows at every size tested' at z_c, (11/10) z_c
for frac in (sp.Rational(9, 10), sp.Integer(1), sp.Rational(11, 10)):
    zc, s_def, f_def = verdicts(E_def, 3, 1, 2, frac)
    _, s_a1, f_a1 = verdicts(E_a1, 3, 1, 2, frac)
    rows.append(f"(3,1,2) z={frac}z_c: definition sign changes at {f_def} (first sign {s_def[0]:+d}), a1 count at {f_a1} (first sign {s_a1[0]:+d})")
    if frac == sp.Rational(9, 10):
        ok &= all(v < 0 for v in s_def) and f_a1 == [10] and s_a1[0] > 0
    elif frac == 1:
        ok &= all(v < 0 for v in s_def) and all(v > 0 for v in s_a1)
    else:
        ok &= f_def == [17] and s_def[0] < 0 and s_def[-1] > 0 and all(v > 0 for v in s_a1)
ok &= zc == sp.Rational(16, 825)
# (20,1,1): x = 24/5 > both thresholds; a1: repelling size 13.445 at (3/2) z_c
zc2, s_def2, f_def2 = verdicts(E_def, 20, 1, 1, sp.Rational(3, 2))
_, s_a12, f_a12 = verdicts(E_a1, 20, 1, 1, sp.Rational(3, 2))
rows.append(f"(20,1,1) z=(3/2)z_c: definition sign changes at {f_def2}, a1 count at {f_a12}")
ok &= f_a12 == [13] and len(f_def2) == 1 and s_def2[0] < 0 and s_def2[-1] > 0
# (1,1,2): x = 3/5 < 1 at the neutral scale -> attracting size under the definition
zc3, s_def3, f_def3 = verdicts(E_def, 1, 1, 2, sp.Rational(99, 100))
rows.append(f"(1,1,2) z=(99/100)z_c: definition sign changes at {f_def3} (first sign {s_def3[0]:+d})")
ok &= len(f_def3) == 1 and s_def3[0] > 0 and s_def3[-1] < 0
# neutral-scale criterion: c0 p > 1 iff 5p > q + 4r
ok &= sp.simplify((6 * p / (p + q + 4 * r_) - 1) * (p + q + 4 * r_) - (5 * p - q - 4 * r_)) == 0
check('A4', ok, "EXACT (G - E evaluated as rationals at L = 2..200; beyond, the signs of the three coefficients decide): at the "
      "neutral scale x = c0 p > 1 exactly when 5p > q + 4r; at (3,1,2) (x = 3/2, z_c = 16/825) a1's count and the definition give "
      "opposite verdicts - at (9/10) z_c a1 finds growth up to L = 10 (its attracting 'maximum stable size'), the definition "
      "shrinkage at every size; at z_c a1 finds growth at every size, the definition shrinkage at every size; at (11/10) z_c a1 "
      "finds growth at every size, the definition a repelling critical size between 17 and 18; at (20,1,1) both are repelling, "
      "at different sizes; an attracting size under the definition needs x < 1, e.g. (1,1,2) at the neutral scale (x = 3/5)",
      "; ".join(rows))

# ================================================================ B. which surface records can leave to an isolated position
FACETS = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 1, 1), (2, 2, 1), (3, 1, 0), (3, 1, 1), (3, 2, 0), (3, 2, 1),
          (3, 2, 2), (3, 3, 1), (3, 3, 2), (4, 1, 0), (4, 3, 0), (5, 3, 1), (0, -2, 1), (-1, 2, -3), (2, -5, 3)]


def facet_layers(nvec, box=4):
    """For the half-space {n.v <= 0}: per layer m = -n.s of surface records, the multiset of (k_s, tuple of isolated
    destinations as directions, sorted k_t of all destinations); per layer m' = n.t >= 1 of touching empty sites, the set of j."""
    inH = lambda v: v[0] * nvec[0] + v[1] * nvec[1] + v[2] * nvec[2] <= 0
    rec, gro = {}, {}
    for s in itertools.product(range(-box, box + 1), repeat=3):
        ns = s[0] * nvec[0] + s[1] * nvec[1] + s[2] * nvec[2]
        if inH(s):
            empt = [d for d in NB if not inH(add(s, d))]
            if not empt:
                continue
            ks = 6 - len(empt)
            kts, iso = [], []
            for d in empt:
                t = add(s, d)
                kt = sum(inH(add(t, e)) for e in NB if add(t, e) != s)
                kts.append(kt)
                if kt == 0:
                    iso.append(d)
            rec.setdefault(-ns, set()).add((ks, tuple(iso), tuple(sorted(kts))))
        else:
            j = sum(inH(add(s, e)) for e in NB)
            if j:
                gro.setdefault(ns, set()).add(j)
    return rec, gro


ok = True
table = []
for nvec in FACETS:
    a = sorted((abs(v) for v in nvec), reverse=True)
    h, k, l = a
    i1 = max(range(3), key=lambda i: abs(nvec[i]))
    e1 = tuple((1 if nvec[i1] > 0 else -1) if i == i1 else 0 for i in range(3))
    rec, gro = facet_layers(nvec)
    ok &= sorted(rec) == list(range(h)) and sorted(gro) == list(range(1, h + 1))
    for m, props in rec.items():
        ok &= len(props) == 1                                           # every record of a layer behaves the same
        ks, iso, kts = next(iter(props))
        ok &= ks == 3 + sum(v <= m for v in a)
        if m < h - k:
            ok &= iso == (e1,)                                          # exactly one isolated destination, along the largest normal component
        else:
            ok &= iso == ()
        want = sorted(sum(1 for i2 in range(3) if i2 != i and a[i2] >= a[i] - m) for i in range(3) if a[i] > m)
        ok &= list(kts) == want
    for mm, js in gro.items():
        ok &= js == {sum(v >= mm for v in a)}
    table.append(f"({','.join(map(str, nvec))}): leaving layers {h - k} of {h}")
check('B1', ok, "EXACT (every lattice point of |coordinates| <= 4 near the plane, for 19 facets including permuted and signed "
      "normals): on a facet {n.v <= 0} with primitive n and sorted |n| = (h, k, l), h >= k >= l, the surface records are the "
      "layers m = -n.s = 0..h-1, a record of layer m has 3 + #{i: |n_i| <= m} recorded neighbours, it can reach an isolated "
      "position in one move iff m < h - k, and then along exactly one bond (the largest normal component); its other moves end "
      "next to #{i' != i: |n_i'| >= |n_i| - m} records; touching empty sites of layer m' = 1..h have j = #{i: |n_i| >= m'}. "
      "A facet whose two largest |n_i| are equal - (110), (111), (221), (331), (332) - has NO record that can leave in one move",
      "; ".join(table))

# the polytopes: exact move and growth censuses
Rs = sp.symbols('R', positive=True)
MOVE = {
    'oct': {(1, 0): 6, (1, 1): 24, (2, 1): 24 * (Rs - 1), (2, 2): 24 * (Rs - 1), (3, 2): 12 * (Rs - 1) * (Rs - 2)},
    ('dod', 0): {(1, 0): 6, (1, 1): 24, (3, 0): 12 * Rs, (3, 1): 24 * (Rs - 2), (4, 1): 2 * (6 * Rs ** 2 - 12 * Rs + 12)},
    ('dod', 1): {(1, 0): 6, (1, 1): 24, (3, 0): 12 * (Rs - 1), (3, 1): 24 * (Rs - 1), (4, 1): 2 * (6 * Rs ** 2 - 12 * Rs + 6)},
}
GROW = {'oct': {1: 6, 2: 12 * Rs, 3: 4 * Rs ** 2 - 4 * Rs}, ('dod', 0): {1: 12 * Rs + 6, 2: 6 * Rs ** 2},
        ('dod', 1): {1: 12 * Rs - 6, 2: 6 * Rs ** 2 + 6}}
ok = True
for n in range(2, 13):
    for kind in ('oct', 'dod'):
        key = 'oct' if kind == 'oct' else ('dod', n % 2)
        S = shape(kind, n)
        want = {kk: int(sp.sympify(v).subs(Rs, n)) for kk, v in MOVE[key].items() if int(sp.sympify(v).subs(Rs, n))}
        ok &= dict(move_census(S)) == want
        wantg = {kk: int(sp.sympify(v).subs(Rs, n)) for kk, v in GROW[key].items() if int(sp.sympify(v).subs(Rs, n))}
        ok &= dict(growth_census(S)) == wantg
check('B2', ok, "EXACT (enumerated, R = 2..12): the octahedron |x|+|y|+|z| <= R has one-move departures (to an isolated "
      "position) only from its 6 tips, one bond each, at every size; its other moves: tips to 1-neighbour sites 24, edge records "
      "to 1- and 2-neighbour sites 24(R-1) each, (111) face records to 2-neighbour sites 12(R-1)(R-2) (three per face record); "
      "the rhombic dodecahedron has departures from its 6 tips and along 12R (R even) or 12(R-1) (R odd) bonds from its edges and "
      "3-fold vertices, and its (110) face records only move to 1-neighbour sites (two per face record); growth sites: "
      "octahedron j = 1, 2, 3 on 6, 12R, 4R^2 - 4R sites, dodecahedron j = 1, 2 on 12R+6, 6R^2 (R even) or 12R-6, 6R^2+6 (R odd)")

# one-move accounting for the tied shapes
ok = True
D = {}
for key in ('oct', ('dod', 0), ('dod', 1)):
    D[key] = sum(v / (1 + x ** kk[0]) for kk, v in MOVE[key].items() if kk[1] == 0)
    Gk = z * sum(v * c ** j * A(j) for j, v in GROW[key].items())
    ok &= sp.limit(Gk / D[key], Rs, sp.oo) == sp.oo
ok &= sp.simplify(D['oct'] - 6 / (1 + x)) == 0
ok &= sp.simplify(D[('dod', 0)] - (6 / (1 + x) + 12 * Rs / (1 + x ** 3))) == 0
check('B3', ok, "EXACT: in the one-move accounting (departures to isolated positions, a1's reading of evaporation, with the "
      "definition's bond count) the octahedron evaporates at 6/(1+x) and the dodecahedron at 6/(1+x) + 12R/(1+x^3) (R even) at "
      "every size, while surface formation grows as R^2: the accounting gives these shapes no critical formation rate at all - "
      "for every z > 0 they grow above a finite size; for the box it gives z_c (A3)")

# ================================================================ C. the no-go for one-move accounting on tied facets
ok = True
detail = []
for nvec, ks_want, kt_want in (((1, 1, 1), 3, 2), ((1, 1, 0), 4, 1), ((2, 2, 1), None, None), ((3, 3, 1), None, None)):
    inH = lambda v, n=nvec: v[0] * n[0] + v[1] * n[1] + v[2] * n[2] <= 0
    s = (0, 0, 0)
    ks = sum(inH(add(s, d)) for d in NB)
    best = None
    for d in NB:
        t = add(s, d)
        if inH(t):
            continue
        occ = lambda v, s=s, t=t: (inH(v) and v != s) or v == t          # after the hop s -> t
        kt = sum(1 for e in NB if occ(add(t, e)))
        iso = [e for e in NB if not occ(add(t, e)) and add(t, e) != s and all(not occ(add(add(t, e), f)) or add(add(t, e), f) == t for f in NB)]
        if iso and (best is None or kt > best[1]):
            best = (d, kt, len(iso))
    ok &= best is not None
    if ks_want is not None:
        ok &= ks == ks_want and best[1] == kt_want
    P_hop = sp.simplify(x ** best[1] / (x ** ks + x ** best[1])); P_leave = sp.simplify(1 / (1 + x ** best[1]))
    detail.append(f"({','.join(map(str, nvec))}) layer-0 record: k_s = {ks}, hop to a {best[1]}-neighbour site w.p. {P_hop}, "
                  f"then {best[2]} isolated destinations w.p. {P_leave} each; displaced weight x^-{ks}")
check('C1', ok, "EXACT: on every tied facet tested ((111), (110), (221), (331)) a top-layer record reaches an isolated position in "
      "TWO moves - a hop to a bonded site (probability 1/(1+x) on (111), 1/(1+x^3) on (110)) and then a move to an isolated "
      "site - and by block 39 T1 the static-law weight of the displaced record relative to the ideal facet is x^-k_s whatever "
      "the path: x^-3 on (111), x^-4 on (110), x^-5 on (100). So the one-move zero of B1-B3 is not a zero of evaporation: in "
      "the static law displacing a record costs x^3 from (111) against x^5 from (100), and a growth law per face orientation "
      "must follow at least two moves - the route 'one-move balance per orientation' (a1's section 4 item 1) fails at its first step",
      "; ".join(detail))

# ================================================================ D. what one move reaches
ok = True
for kind in ('box', 'oct', 'dod'):
    for n in (2, 3, 4, 5):
        S = shape(kind, n)
        results = set()
        bonds = 0
        for s in S:
            for d in NB:
                t = add(s, d)
                if t not in S:
                    bonds += 1
                    results.add(frozenset((S - {s}) | {t}))
        proj = sum(len({tuple(v for i, v in enumerate(s) if i != ax) for s in S}) for ax in range(3))
        ok &= len(results) == bonds == 2 * proj
    ok &= 2 * sum(len({tuple(v for i, v in enumerate(s) if i != ax) for s in shape('oct', 6)}) for ax in range(3)) == 12 * 36 + 12 * 6 + 6
check('D1', ok, "(a) EXACT: for every cluster whose axis-parallel lines meet it in intervals (every convex lattice cluster), the "
      "arrangements reachable in one move number exactly 2(|pi_x C| + |pi_y C| + |pi_z C|), twice the sum of its three "
      "projection areas (each such line contributes its two end bonds, and distinct bonds give distinct arrangements): 6L^2 "
      "for the box (a1), 12R^2 + 12R + 6 for both the octahedron and the rhombic dodecahedron (checked on box, octahedron, "
      "dodecahedron, sizes 2..5, and the octahedron's projections at R = 6)")

# (c) what the first move reads: contents one layer below the surface, and nothing deeper
def first_move_law(content, pp, qq, rr, cc):
    """content: dict site -> axis 0..5 (opposite pairs 0/1, 2/3, 4/5); returns the exact move probability of every
    occupied-empty bond, as a sorted tuple ((s, t), P)."""
    om = lambda a, b: pp if a == b else (qq if a == (b ^ 1) else rr)
    law = []
    for s, a in content.items():
        for d in NB:
            t = add(s, d)
            if t in content:
                continue
            ws = 1
            for e in NB:
                u = add(s, e)
                if u in content:
                    ws *= cc * om(a, content[u])
            wt = 1
            for e in NB:
                u = add(t, e)
                if u in content and u != s:
                    wt *= cc * om(a, content[u])
            law.append(((s, t), sp.Rational(wt) / (sp.Rational(ws) + sp.Rational(wt))))
    return tuple(sorted(law))


ok = True
half = sp.Rational(1, 2)
for n, site, differs in ((3, (1, 1, 1), True), (5, (2, 2, 2), False), (5, (1, 2, 2), True), (4, (1, 1, 1), True)):
    laws = []
    for b in (0, 1, 2):                                   # aligned, opposite, orthogonal content at one interior site
        cont = {s: 0 for s in shape('box', n)}
        cont[site] = b
        laws.append(first_move_law(cont, 3, 1, 2, half))
    distinct = len(set(laws)) == 3
    same = len(set(laws)) == 1
    ok &= distinct if differs else same
check('D2', ok, "(c) EXACT at (3,1,2), c = 1/2: changing the content of ONE interior record (aligned -> opposite -> orthogonal) "
      "changes the exact first-move law of the surface when the record lies one layer below the surface (3-box centre, 4-box "
      "core, 5-box site (1,2,2): three distinct laws) and leaves it identical when it lies two layers deep (5-box centre): "
      "a move's probability involves only the moving record's neighbours at both ends, so the surface's motion reads the "
      "contents at depth 1 without any erosion and is blind to depth >= 2 until erosion exposes depth d - 1 - the reachable "
      "SET is blind to the interior (a1), the LAW of the moves is not")

npass = sum(RESULTS)
print(f"TOTAL: PASS={npass} FAIL={len(RESULTS) - npass}")
print("SUMMARY: PARTIAL, exact: under block 39's definition (every occupied-empty bond visited at one rate) the box's "
      "evaporation counts corners 3 times and edges twice, E(L) = 24/(1+x^3) + 24(L-2)/(1+x^4) + 6(L-2)^2/(1+x^5), and its "
      "finite-size terms have the sign of x - 1, so the threshold between a maximum stable size and nucleation is cp = 1, "
      "not a1's 2.05597 (a1's one-attempt-per-record count breaks detailed balance by a factor 2 at a corner; at (3,1,2) the two "
      "counts give opposite verdicts); which surface records can leave in one move is decided per facet: layers m < h - k of "
      "a facet with sorted |normal| (h, k, l), none on tied facets (110)/(111)/..., octahedron 6 tips only at every size; the "
      "one-move balance therefore has no critical rate for tied shapes, but tied-facet records leave in two moves with static "
      "weight x^-3 (111) against x^-5 (100), so a per-orientation growth law must follow two moves; one move reaches exactly "
      "twice the sum of the projection areas; the law of the surface's moves reads the contents one layer below the surface "
      "and nothing deeper")
if all(RESULTS):
    print("HIT: for block 39's pair-weight transit (each occupied-empty bond visited at one rate) and a convex cluster of aligned "
          "records: (1) the box evaporates at E(L) = 24/(1+x^3) + 24(L-2)/(1+x^4) + 6(L-2)^2/(1+x^5), x = cp, whose finite-size "
          "terms 24x^4(x-1)/((1+x^4)(1+x^5)) L + 24x^3(x-1)^3(x+1)(x^2+1)/((1+x^3)(1+x^4)(1+x^5)) have the sign of x - 1, so "
          "the dichotomy (attracting maximum size vs repelling nucleation size) switches at cp = 1 exactly, i.e. at 5p = q + 4r "
          "at the neutral scale - attempt a1's threshold 2.05597 comes from one attempt per record, which is not in the "
          "definition's class (detailed balance off by 2 at a corner), and at (3,1,2) its verdicts are reversed; (2) on a facet "
          "with sorted |normal| (h, k, l) exactly the top h - k layers can leave to an isolated position in one move, one bond "
          "each, so tied facets ((110), (111), ...) have none and the octahedron's one-move evaporation is 6/(1+x) at every "
          "size; (3) this zero is not an evaporation law: tied-facet records leave in two moves and carry static weight x^-3 "
          "on (111) against x^-5 on (100); (4) one move reaches exactly 2(|pi_x C| + |pi_y C| + |pi_z C|) arrangements, and "
          "the law of the surface's moves depends on the contents at depth 1 below the surface and on nothing deeper")
