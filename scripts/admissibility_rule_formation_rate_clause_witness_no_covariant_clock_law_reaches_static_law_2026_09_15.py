#!/usr/bin/env python3
"""Exact checks: the formation-rate clause witness and the plaquette no-go.

Scope.  Six-axis menu, covariant positive product rule (p, q, r) = (3, 1, 2), records-only reading; records form one at a time
under independent memoryless clocks with covariant rates.  R1: competing clocks give jump probabilities lambda_x/Lambda (exact
integral); value-blind laws give mixtures over orders computed by multiset classes (checked against full enumeration).  R2: the
uniform, seeded and attracting laws on 2x3 (28 classes) give pairwise different finished laws; the uniform distance to the static
law equals the census note's rational; the cube's all-+x probability differs; four laws on the plaquette.  R3: on the path and
the star the seeded law equals the static law.  R4: the plaquette identity mu / prod K = (1/4) sum_s G(p_type(s), d) with
G(p, d) = (1-p) d/6 + p d^2/36, checked against four explicit laws and symbolically for every (p_in, p_out); the type assignment.
R5: the class ratios are strictly increasing in d.  R6: the parallel-growth law is outside the affine span of the order laws.
Exact rational and symbolic arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
from collections import defaultdict
from fractions import Fraction
from functools import reduce
from itertools import permutations, product
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FORMATION_RATE_CLAUSE_WITNESS_NO_COVARIANT_CLOCK_LAW_REACHES_THE_STATIC_LAW_ON_A_PLAQUETTE_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_formation_rate_clause_witness_no_covariant_clock_law_reaches_the_static_law_on_a_plaquette_bounded_theorem_note_2026-09-15"
CENSUS_CLAIM_ID = "admissibility_formation_order_menu_order_mixture_monotone_box_and_cube_census_bounded_theorem_note_2026-09-13"
CENSUS_FRAGMENT = "372254646387017/12790481418000000"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "Theorem B"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
    "it does not supply the formation site, probability, or rate.",
)

MUTATION_GATE = {
    "jump_probability_wrong": "B",
    "class_mixture_differs_from_enumeration": "B",
    "rate_laws_give_same_law_claimed": "C",
    "census_rational_mismatch": "C",
    "cube_probabilities_equal_claimed": "C",
    "seeded_tree_not_static_claimed": "D",
    "plaquette_identity_wrong": "E",
    "static_reached_on_plaquette_claimed": "E",
    "type_assignment_wrong": "E",
    "class_ratios_not_monotone_claimed": "E",
    "parallel_law_in_span_claimed": "E",
    "claim_rate_clause_adopted": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: list[str] = []

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        if not ok:
            self.failed_families.append(label[0])
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize_text(text: str) -> str:
    return " ".join(text.split())


F = Fraction
M = 6
P_, Q_, R_ = 3, 1, 2


def dec(x: Fraction, n: int = 6) -> str:
    s = x.numerator * 10 ** n // x.denominator
    return f"{s // 10 ** n}.{str(s % 10 ** n).zfill(n)}"


def orbit_type(s: int, u: int) -> str:
    if s == u:
        return "p"
    if s // 2 == u // 2:
        return "q"
    return "r"


WEIGHTS = {"p": P_, "q": Q_, "r": R_}
PHI = [[WEIGHTS[orbit_type(s, t)] for t in range(M)] for s in range(M)]
Z1 = sum(PHI[0])
AXIS = {0: (1, 0, 0), 1: (-1, 0, 0), 2: (0, 1, 0), 3: (0, -1, 0), 4: (0, 0, 1), 5: (0, 0, -1)}
_COND: dict = {}


def cond(rec: tuple, s: int) -> Fraction:
    key = (rec, s)
    if key in _COND:
        return _COND[key]
    if not rec:
        val = F(1, M)
    else:
        num = reduce(lambda a, b: a * b, [PHI[s][a] for a in rec], 1)
        den = sum(reduce(lambda a, b: a * b, [PHI[u][a] for a in rec], 1) for u in range(M))
        val = F(num, den)
    _COND[key] = val
    return val


def K2(a: int, b: int) -> Fraction:
    return sum((F(PHI[u][a] * PHI[u][b], Z1 * Z1) for u in range(M)), F(0))


# ------------------------------------------------------------------ windows
def window(name: str):
    if name == "plaquette":
        pos = {0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0)}
    elif name == "2x3":
        pos = {i: (i // 3, i % 3, 0) for i in range(6)}
    elif name == "cube":
        pos = {i: (i & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)}
    elif name == "path3":
        pos = {0: (0, 0, 0), 1: (1, 0, 0), 2: (2, 0, 0)}
    elif name == "star4":
        pos = {0: (0, 0, 0), 1: (1, 0, 0), 2: (-1, 0, 0), 3: (0, 1, 0), 4: (0, -1, 0)}
    else:
        raise KeyError(name)
    sites = sorted(pos)
    edges = [(i, j) for i in sites for j in sites if i < j and sum(abs(pos[i][k] - pos[j][k]) for k in range(3)) == 1]
    nb = {i: [j for j in sites if (min(i, j), max(i, j)) in edges] for i in sites}
    return sites, pos, edges, nb


def static_law(sites, edges):
    w = {}
    for v in product(range(M), repeat=len(sites)):
        x = 1
        for (i, j) in edges:
            x *= PHI[v[i]][v[j]]
        w[v] = x
    Z = sum(w.values())
    return {v: F(x, Z) for v, x in w.items()}


def prod_K(v, edges) -> Fraction:
    x = F(1)
    for (i, j) in edges:
        x *= F(PHI[v[i]][v[j]], Z1)
    return x


def tv(a: dict, b: dict) -> Fraction:
    return sum((abs(a[v] - b[v]) for v in a), F(0)) / 2


# ------------------------------------------------------------------ rate laws: rate(x, S, vmap, nb, pos)
def uniform(x, S, v, nb, pos):
    return F(1)


def seeded(x, S, v, nb, pos):
    return F(1) if (len(S) == 0 or any(y in S for y in nb[x])) else F(0)


def attracting(x, S, v, nb, pos):
    return F(1 + sum(1 for y in nb[x] if y in S))


def parallel(x, S, v, nb, pos):
    bias = 0
    for y in nb[x]:
        if y in S:
            d = tuple(pos[x][k] - pos[y][k] for k in range(3))
            if AXIS[v[y]] == d:
                bias = 1
    return F(1 + bias)


RATE_LAWS = {"uniform": uniform, "seeded": seeded, "attracting": attracting, "parallel": parallel}


def finished_law(sites, nb, pos, rate) -> dict:
    """Exact finished law by dynamic programming over histories (order and values)."""
    n = len(sites)
    layer = {((), ()): F(1)}
    for _ in range(n):
        new: dict = defaultdict(F)
        for (S, vals), pr in layer.items():
            Sset = set(S)
            vmap = dict(zip(S, vals))
            rates = {x: rate(x, Sset, vmap, nb, pos) for x in sites if x not in Sset}
            tot = sum(rates.values())
            for x, lam in rates.items():
                if lam == 0:
                    continue
                rec = tuple(vmap[y] for y in nb[x] if y in Sset)
                for s in range(M):
                    new[(S + (x,), vals + (s,))] += pr * lam / tot * cond(rec, s)
        layer = new
    law: dict = defaultdict(F)
    for (S, vals), pr in layer.items():
        v = [0] * n
        for x, s in zip(S, vals):
            v[x] = s
        law[tuple(v)] += pr
    return dict(law)


def multiset_key(order, nb):
    S: set = set()
    key = []
    for x in order:
        A = tuple(sorted(y for y in nb[x] if y in S))
        if len(A) >= 2:
            key.append(A)
        S.add(x)
    return tuple(sorted(key))


def order_prob(order, nb, pos, rate) -> Fraction:
    S: set = set()
    pr = F(1)
    for x in order:
        rates = {y: rate(y, S, {}, nb, pos) for y in nb if y not in S}
        tot = sum(rates.values())
        if rates[x] == 0:
            return F(0)
        pr *= rates[x] / tot
        S.add(x)
    return pr


def order_law_single(order, nb, v) -> Fraction:
    S: set = set()
    pr = F(1)
    for x in order:
        rec = tuple(v[y] for y in nb[x] if y in S)
        pr *= cond(rec, v[x])
        S.add(x)
    return pr


def class_laws(sites, nb):
    classes: dict = {}
    for order in permutations(sites):
        classes.setdefault(multiset_key(order, nb), []).append(order)
    laws = {}
    for k, orders in classes.items():
        rep = orders[0]
        laws[k] = {v: order_law_single(rep, nb, v) for v in product(range(M), repeat=len(sites))}
    return classes, laws


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, census, b01 = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, the census note and block 01, both on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axiom sentences and the reading-note clause used are present verbatim in the axiom memo")
    fc, f01 = normalize_text(census), normalize_text(b01)
    checks.check("A3", CENSUS_CLAIM_ID in fc and CENSUS_FRAGMENT in fc and BLOCK01_CLAIM_ID in f01 and BLOCK01_FRAGMENT in f01,
                 "the parents' claim ids, the census note's Theorem 3 rational and block 01's Theorem B are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks, report: dict) -> None:
    t = sp.symbols("t", positive=True)
    rates = (1, 2, 3)
    probs = []
    for i, lx in enumerate(rates):
        integrand = lx * sp.exp(-lx * t) * sp.prod([sp.exp(-ly * t) for j, ly in enumerate(rates) if j != i])
        probs.append(sp.integrate(integrand, (t, 0, sp.oo)))
    expected = [sp.Rational(lx, sum(rates)) for lx in rates]
    if mut("jump_probability_wrong"):
        expected = [sp.Rational(lx * lx, sum(r * r for r in rates)) for lx in rates]
    checks.check("B1", all(sp.simplify(a - b) == 0 for a, b in zip(probs, expected)) and sum(probs) == 1,
                 "R1: for rates (1, 2, 3) the exact integrals give P(x rings first) = 1/6, 1/3, 1/2 = lambda_x / Lambda")
    sites, pos, edges, nb = window("plaquette")
    classes, laws = class_laws(sites, nb)
    report["plq"] = (sites, pos, edges, nb, classes, laws)
    ok = True
    for name in ("uniform", "seeded", "attracting"):
        rate = RATE_LAWS[name]
        Pc = {k: sum((order_prob(o, nb, pos, rate) for o in orders), F(0)) for k, orders in classes.items()}
        mix = {v: sum((Pc[k] * laws[k][v] for k in classes), F(0)) for v in laws[next(iter(laws))]}
        direct = finished_law(sites, nb, pos, rate)
        if mut("class_mixture_differs_from_enumeration") and name == "seeded":
            mix = {v: mix[v] * F(1001, 1000) for v in mix}
        ok = ok and all(mix[v] == direct[v] for v in mix) and sum(Pc.values()) == 1
    # 2x3: classes vs full enumeration on 30 random patterns for the seeded law
    sites6, pos6, edges6, nb6 = window("2x3")
    classes6, laws6 = class_laws(sites6, nb6)
    report["2x3"] = (sites6, pos6, edges6, nb6, classes6, laws6)
    random.seed(20260915)
    sample = [tuple(random.randrange(M) for _ in range(6)) for _ in range(30)]
    orders6 = list(permutations(sites6))
    Pc6 = {k: sum((order_prob(o, nb6, pos6, seeded) for o in orders), F(0)) for k, orders in classes6.items()}
    for v in sample:
        by_class = sum((Pc6[k] * laws6[k][v] for k in classes6), F(0))
        by_orders = sum((order_prob(o, nb6, pos6, seeded) * order_law_single(o, nb6, v) for o in orders6), F(0))
        ok = ok and by_class == by_orders
    checks.check("B2", ok and len(classes) == 4, f"R1: the mixtures by multiset classes equal the full history enumeration (plaquette: {len(classes)} classes, three laws, all 1296 patterns; 2x3: 30 random patterns, 720 orders, seeded law)")


# ============================================================================================ family C
def family_c(checks: Checks, report: dict, exact: bool) -> None:
    sites6, pos6, edges6, nb6, classes6, laws6 = report["2x3"]
    stat6 = static_law(sites6, edges6)
    mixes = {}
    tvs = {}
    charged = {}
    for name in ("uniform", "seeded", "attracting"):
        rate = RATE_LAWS[name]
        Pc = {k: sum((order_prob(o, nb6, pos6, rate) for o in orders), F(0)) for k, orders in classes6.items()}
        charged[name] = sum(1 for k in Pc if Pc[k] > 0)
        mixes[name] = {v: sum((Pc[k] * laws6[k][v] for k in classes6), F(0)) for v in stat6}
        tvs[name] = tv(mixes[name], stat6)
    pairs = {(a, b): tv(mixes[a], mixes[b]) for a, b in (("uniform", "seeded"), ("uniform", "attracting"), ("seeded", "attracting"))}
    distinct = all(x > 0 for x in pairs.values())
    if mut("rate_laws_give_same_law_claimed"):
        distinct = all(x == 0 for x in pairs.values())
    checks.check("C1", distinct and len(classes6) == 28 and charged["seeded"] == 6 and charged["uniform"] == 28,
                 f"R2: on 2x3 (28 classes) the uniform, seeded (6 classes charged) and attracting laws are pairwise different: TV = " + ", ".join(f"{a}-{b}: {dec(x)}" for (a, b), x in pairs.items()))
    census = F(372254646387017, 12790481418000000)
    c2 = tvs["uniform"] == census
    if mut("census_rational_mismatch"):
        c2 = tvs["uniform"] == census * F(1001, 1000)
    checks.check("C2", c2 and tvs["seeded"] == F(5951761987229, 292725576000000), f"R2: distances to the static law on 2x3: uniform {tvs['uniform']} (the census note's rational), seeded {tvs['seeded']}, attracting {tvs['attracting']}")
    report["tv23"] = (tvs, pairs)
    # cube: all-+x probability
    sites8, pos8, edges8, nb8 = window("cube")
    classes8: dict = {}
    for order in permutations(sites8):
        classes8.setdefault(multiset_key(order, nb8), []).append(order)
    allx = tuple([0] * 8)
    cube = {}
    for name in ("uniform", "seeded", "attracting"):
        rate = RATE_LAWS[name]
        tot = F(0)
        for k, orders in classes8.items():
            pk = sum((order_prob(o, nb8, pos8, rate) for o in orders), F(0))
            if pk:
                tot += pk * order_law_single(orders[0], nb8, allx)
        cube[name] = tot
    # static all-+x on the cube: prod_edges phi / Z with Z by enumeration over 6^8 patterns is heavy; use the transfer over the two faces
    face = list(product(range(M), repeat=4))
    def face_weight(f):
        w = 1
        for (i, j) in ((0, 1), (1, 3), (3, 2), (2, 0)):
            w *= PHI[f[i]][f[j]]
        return w
    Zc = 0
    fw = {f: face_weight(f) for f in face}
    for f1 in face:
        for f2 in face:
            w = fw[f1] * fw[f2]
            for i in range(4):
                w *= PHI[f1[i]][f2[i]]
            Zc += w
    static_allx = F(P_ ** 12, Zc)
    cube_ok = len({cube[n] for n in cube}) == 3 and all(cube[n] != static_allx for n in cube) and len(classes8) == 542
    if mut("cube_probabilities_equal_claimed"):
        cube_ok = len({cube[n] for n in cube}) == 1
    checks.check("C3", cube_ok, f"R2: on the open cube (542 classes) the all-+x probability differs across the three laws and from the static law: " + ", ".join(f"{n}: {cube[n]}" for n in cube) + f"; static {static_allx}")
    report["cube"] = (cube, static_allx)
    sites, pos, edges, nb, classes, laws = report["plq"]
    stat4 = static_law(sites, edges)
    plq = {name: finished_law(sites, nb, pos, RATE_LAWS[name]) for name in RATE_LAWS}
    report["plq_laws"] = (plq, stat4)
    tv4 = {name: tv(plq[name], stat4) for name in plq}
    pairwise = all(tv(plq[a], plq[b]) > 0 for a in plq for b in plq if a < b)
    checks.check("C4", pairwise and all(x > 0 for x in tv4.values()), "R2: on the plaquette the four laws are pairwise different and none is the static law: TV to static " + ", ".join(f"{n}: {tv4[n]}" for n in tv4))
    report["tv4"] = tv4
    if exact:
        print("exact 2x3 pairwise TVs:", "; ".join(f"{a}-{b}: {x}" for (a, b), x in pairs.items()))
        print("exact 2x3 attracting TV to static:", tvs["attracting"])


# ============================================================================================ family D
def family_d(checks: Checks, report: dict) -> None:
    res = {}
    for name in ("path3", "star4"):
        sites, pos, edges, nb = window(name)
        st = static_law(sites, edges)
        se = finished_law(sites, nb, pos, seeded)
        un = finished_law(sites, nb, pos, uniform)
        res[name] = (tv(se, st), tv(un, st))
    seeded_ok = all(res[n][0] == 0 for n in res)
    if mut("seeded_tree_not_static_claimed"):
        seeded_ok = all(res[n][0] > 0 for n in res)
    checks.check("D1", seeded_ok, "R3: on the path of three sites and the four-leaf star the seeded law equals the static law exactly")
    checks.check("D2", all(res[n][1] > 0 for n in res), "R3: the uniform law differs from the static law on both trees: TV " + ", ".join(f"{n}: {res[n][1]}" for n in res))
    report["trees"] = res


# ============================================================================================ family E
DELTA = {0: (1, 1, 0), 1: (-1, 1, 0), 2: (-1, -1, 0), 3: (1, -1, 0)}


def vtype(s: int, val: int) -> str:
    d = sum(AXIS[val][k] * DELTA[s][k] for k in range(3))
    return "in" if d > 0 else ("out" if d < 0 else "perp")


def family_e(checks: Checks, report: dict) -> None:
    sites, pos, edges, nb, classes, laws = report["plq"]
    plq, stat4 = report["plq_laws"]
    d_same, d_anti, d_orth = 1 / K2(0, 0), 1 / K2(0, 1), 1 / K2(0, 2)
    G = lambda p, d: (1 - p) * d / 6 + p * d * d / 36
    P1, P3, P4 = (0, 1, 0, 1), (0, 0, 1, 1), (0, 1, 2, 2)
    # type probabilities of each law from the rate function at S = {0} with value of each type
    ok = True
    ratios = {}
    for name, rate in RATE_LAWS.items():
        ptype = {}
        for val, typ in ((0, "in"), (1, "out"), (4, "perp")):
            S = {0}
            vm = {0: val}
            lam = {x: rate(x, S, vm, nb, pos) for x in (1, 2, 3)}
            ptype[typ] = lam[2] / (lam[1] + lam[2] + lam[3])
        for pat, d in ((P1, d_same), (P3, d_anti), (P4, d_orth)):
            predicted = sum((G(ptype[vtype(s, pat[s])], d) for s in range(4)), F(0)) / 4
            actual = plq[name][pat] / prod_K(pat, edges)
            ratios[(name, pat)] = actual
            if mut("plaquette_identity_wrong"):
                predicted = predicted * F(1001, 1000)
            ok = ok and predicted == actual
    checks.check("E1", ok, "R4: mu/prod K = (1/4) sum_s G(p_type(s), d) reproduces the exact ratios of all four laws at P1, P3, P4 (uniform: " + ", ".join(str(ratios[("uniform", p)]) for p in (P1, P3, P4)) + ")")
    p_in, p_out, pp, qq, rr = sp.symbols("p_in p_out p q r", positive=True)
    ZZ = pp + qq + 4 * rr
    K2s_num, K2a_num, K2o_num = pp ** 2 + qq ** 2 + 4 * rr ** 2, 2 * pp * qq + 4 * rr ** 2, 2 * rr * (pp + qq) + 2 * rr ** 2
    ds, da, do = ZZ ** 2 / K2s_num, ZZ ** 2 / K2a_num, ZZ ** 2 / K2o_num
    Gs = lambda p, d: (1 - p) * d / 6 + p * d ** 2 / 36
    # (i) G(p, d') - G(p, d) = (d' - d) * ((1 - p)/6 + p (d' + d)/36): a convex combination of 1/6 and (d'+d)/36 for p in [0, 1]
    ident = all(sp.simplify(Gs(pt, dd) - Gs(pt, ds) - (dd - ds) * ((1 - pt) / 6 + pt * (dd + ds) / 36)) == 0 for pt in (p_in, p_out) for dd in (da, do))
    # (ii) d_anti - d_same = Z^2 (p - q)^2 / (K2a K2s); d_orth - d_same = Z^2 ((p - r)^2 + (q - r)^2) / (K2o K2s), positive denominators
    gap_anti = sp.simplify(da - ds - ZZ ** 2 * (pp - qq) ** 2 / (K2a_num * K2s_num)) == 0
    gap_orth = sp.simplify(do - ds - ZZ ** 2 * ((pp - rr) ** 2 + (qq - rr) ** 2) / (K2o_num * K2s_num)) == 0
    sym_ok = ident and gap_anti and gap_orth
    if mut("static_reached_on_plaquette_claimed"):
        sym_ok = sp.simplify(Gs(p_in, da) - Gs(p_in, ds)) == 0
    checks.check("E2", sym_ok, "R4: for every (p_in, p_out) in [0,1]^2 and positive (p, q, r), mu/prod K at P3 minus at P1 is (d_anti - d_same) times a convex combination of 1/6 and (d_anti + d_same)/36, with d_anti - d_same = Z_1^2 (p-q)^2/(K2a K2s); likewise P4 minus P1 with ((p-r)^2 + (q-r)^2): never the static law unless p = q = r")
    types = {pat: tuple(sorted(vtype(s, pat[s]) for s in range(4))) for pat in (P1, P3, P4)}
    dvals = {P1: (1 / K2(P1[0], P1[2]), 1 / K2(P1[1], P1[3])), P3: (1 / K2(P3[0], P3[2]), 1 / K2(P3[1], P3[3])), P4: (1 / K2(P4[0], P4[2]), 1 / K2(P4[1], P4[3]))}
    t_ok = types[P1] == types[P3] == types[P4] == ("in", "in", "out", "out") and dvals[P1] == (d_same, d_same) and dvals[P3] == (d_anti, d_anti) and dvals[P4] == (d_orth, d_orth)
    if mut("type_assignment_wrong"):
        t_ok = types[P1] == ("in", "in", "in", "out")
    checks.check("E3", t_ok and d_same == F(72, 13) and d_anti == F(72, 11) and d_orth == 6, "R4: P1, P3, P4 all have type multiset {in, in, out, out}; their diagonal pairs give d_same = 72/13, d_anti = 72/11, d_orth = 6")
    # E4: class ratios at P1, P3, P4 are strictly increasing in d for every class
    mono = True
    for k, law in laws.items():
        vec = [law[pat] / prod_K(pat, edges) for pat in (P1, P3, P4)]  # d increases: same < anti ... check order by d values
        order_d = sorted([(d_same, 0), (d_anti, 1), (d_orth, 2)])
        seq = [vec[i] for _, i in order_d]
        mono = mono and seq[0] < seq[1] < seq[2]
    if mut("class_ratios_not_monotone_claimed"):
        mono = not mono
    checks.check("E4", mono, "R5: each of the four class laws has ratio to prod K strictly increasing along d_same < d_orth < d_anti at P1, P4, P3, so no convex combination is constant")
    # E5: rank of the five laws
    pats = list(stat4)
    rows = [[laws[k][v] for v in pats] for k in laws] + [[plq["parallel"][v] for v in pats]]
    def rank(mat):
        mat = [r[:] for r in mat]
        rk = 0
        ncol = len(mat[0])
        for c in range(ncol):
            piv = next((i for i in range(rk, len(mat)) if mat[i][c] != 0), None)
            if piv is None:
                continue
            mat[rk], mat[piv] = mat[piv], mat[rk]
            for i in range(len(mat)):
                if i != rk and mat[i][c] != 0:
                    f = mat[i][c] / mat[rk][c]
                    mat[i] = [x - f * y for x, y in zip(mat[i], mat[rk])]
            rk += 1
            if rk == len(mat):
                break
        return rk
    r5 = rank(rows)
    r4 = rank(rows[:4])
    span_ok = r5 == 5 and r4 == 4
    if mut("parallel_law_in_span_claimed"):
        span_ok = r5 == 4
    checks.check("E5", span_ok, f"R6: the four class laws have rank {r4} and with the parallel-growth law rank {r5}: the value-dependent law lies outside the affine span of the order laws")


# ============================================================================================ family F
FENCES = (
    "This note exhibits the formation-rate witness and settles where a covariant rate law can reproduce the static law (trees) and where none can (a plaquette); it does not classify larger windows, does not treat clocks with memory or joint formation, does not select an order, rate, rule or coupling as physical, and adopts no clause.",
    "No plane, bridge, Born or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical rate", "for every coupling", "selects the", "fires wake condition", "the Bridge weights",
    "the Bridge conjecture", "certified", "converge", "emergent", "the rate clause is adopted", "washes out", "toward the plane", "the trend",
)
CLAIM_INJECTIONS = {"claim_rate_clause_adopted": "Hence the rate clause is adopted and selects the physical rate."}
CLASSICAL_NAMES = ("Gillespie", "Eden", "Toom", "Peierls", "Fourier", "Dobrushin", "Kolmogorov", "Doeblin")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text + "\n" + phrase
    flat = normalize_text(text)
    checks.check("F1", all(f in flat for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [ph for ph in FORBIDDEN if ph.lower() in flat.lower()]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    source_lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    scan = [ln for ln in source_lines if SCAN_MARKER not in ln]
    float_literal = re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])|(?<![\w.])\d+[eE][-+]?\d+(?![\w.])")
    conversion = "flo" + "at("  # float-scan-marker-line
    evalf = "eva" + "lf("  # float-scan-marker-line
    numeric = "N" + "("  # float-scan-marker-line
    bad = [ln for ln in scan if float_literal.search(ln) or conversion in ln or evalf in ln or numeric in ln]
    checks.check("F3", not bad and len(scan) > 200, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem R1"):
            body = body + " (Gillespie's construction)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the classical names appear only under Prior art and Imports ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the jump probabilities by exact integral; the ratios mu/prod K at P1, P3, P4 for four laws and the general identity in (p_in, p_out) symbolically",
    "per_site: executed — every pattern of the plaquette (1296) and of 2x3 (46656) under three value-blind laws; 30 random 2x3 patterns against the full order enumeration",
    "per_mode: executed — the 4 classes of the plaquette, the 28 of 2x3 and the 542 of the cube; the rank of the class laws with the parallel-growth law",
    "per_block: executed — the plaquette, 2x3, the cube, the path and the star",
    "lattice_wide: R1, R3, R4, R5 proved for every positive triple (R4, R5 at every non-constant rule); larger windows with a plaquette are not claimed; no clause adopted",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5 and all(len(l) >= 40 for l in N5_LINES), "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    exact = "--exact" in argv
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: formation-rate laws — clocks to orders, the rate witness on 2x3, the cube and the plaquette, trees under seeded growth, the plaquette no-go for every covariant rate law; exact; no clause adopted")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    report: dict = {}
    family_a(checks, texts)
    family_b(checks, report)
    family_c(checks, report, exact)
    family_d(checks, report)
    family_e(checks, report)
    family_f(checks, texts[0])
    family_g(checks)
    if exact:
        tvs, pairs = report["tv23"]
        print("exact tree TVs (uniform):", report["trees"])
        print("exact plaquette TVs:", report["tv4"])
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
