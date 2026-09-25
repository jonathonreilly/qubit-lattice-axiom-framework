#!/usr/bin/env python3
"""Exact checks: aligned clusters of moving records - with block 39's motion counted bond by bond, a box loses records at
E(L) = 24/(1+x^3) + 24(L-2)/(1+x^4) + 6(L-2)^2/(1+x^5), x = cp, so its turning size switches from largest-stable to
nucleating at cp = 1; tied facets lose no record in one move, and a growth law per facet must follow two moves (a harvest
block from a Grok-refereed probes attempt; blocks 39 and 40 as landed; not adopted).

B (T1): the box's departures, per bond, and detailed balance.
C (T2): growth against departure; the switch at cp = 1; exact values at (3,1,2).
D (T3): which surface records leave in one move; the octahedron and the rhombic dodecahedron.
E (T4): two moves; the weight of a displacement; what one move reaches.
Exact arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_ALIGNED_CLUSTERS_OF_MOVING_RECORDS_A_BOX_LOSES_RECORDS_BOND_BY_BOND_ITS_TURNING_SIZE_SWITCHES_AT_CP_EQUALS_ONE_AND_TIED_FACETS_NEED_TWO_MOVES_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_aligned_clusters_of_moving_records_a_box_loses_records_bond_by_bond_its_turning_size_switches_at_cp_equals_one_and_tied_facets_need_two_moves_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Records form.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "box_rate_forged": "B",
    "switch_forged": "C",
    "facet_rule_forged": "D",
    "path_weight_forged": "E",
    "claim_transition_injected": "F",
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
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


Fr = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: a site never carries more than one record (a move needs an empty site); records form (block 39 T4 rate); Admissibility is not a dynamics axiom (the motion, the rate convention and the formation rate are supplied)")


# ============================================================================================ block 39's moving records around an aligned cluster
XS = sp.symbols("x", positive=True)
NB = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add3(v, d):
    return (v[0] + d[0], v[1] + d[1], v[2] + d[2])


def departures(inside, cells):
    """for a cluster given by the predicate inside() and its cell list: the occupied-empty bonds (s, t), with k_s = the
    number of recorded neighbours of s and whether t is isolated once the record has moved there."""
    out = []
    for s in cells:
        ks = sum(1 for d in NB if inside(add3(s, d)))
        for d in NB:
            t = add3(s, d)
            if inside(t):
                continue
            iso = all(not inside(add3(t, e)) for e in NB if add3(t, e) != s)
            out.append((s, t, ks, iso))
    return out


def box_rate(ll):
    cells = list(product(range(ll), repeat=3))
    inside = lambda v: all(0 <= v[i] < ll for i in range(3))
    return departures(inside, cells)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the box's departures, counted per bond."""
    ok = True
    for ll in range(2, 8):
        deps = box_rate(ll)
        rate = sum(1 / (1 + XS ** ks) for (_, _, ks, _) in deps)
        want = 24 / (1 + XS ** 3) + 24 * (ll - 2) / (1 + XS ** 4) + 6 * (ll - 2) ** 2 / (1 + XS ** 5)
        if mut("box_rate_forged"):
            want = 8 / (1 + XS ** 3) + 12 * (ll - 2) / (1 + XS ** 4) + 6 * (ll - 2) ** 2 / (1 + XS ** 5)
        ok = ok and len(deps) == 6 * ll * ll and all(iso for (_, _, _, iso) in deps) and sp.simplify(rate - want) == 0
    ll_ = sp.symbols("L")
    e_l = 24 / (1 + XS ** 3) + 24 * (ll_ - 2) / (1 + XS ** 4) + 6 * (ll_ - 2) ** 2 / (1 + XS ** 5)
    beta = 24 * XS ** 4 * (XS - 1) / ((1 + XS ** 4) * (1 + XS ** 5))
    gamma = 24 * XS ** 3 * (XS - 1) ** 3 * (XS + 1) * (XS ** 2 + 1) / ((1 + XS ** 3) * (1 + XS ** 4) * (1 + XS ** 5))
    ok_split = sp.simplify(e_l - (6 * ll_ ** 2 / (1 + XS ** 5) + beta * ll_ + gamma)) == 0 and sp.simplify(e_l.subs(XS, 1) - 3 * ll_ ** 2) == 0
    fwd_bond, back_bond = 1 / (1 + XS ** 3), XS ** 3 / (1 + XS ** 3)
    fwd_a1, back_a1 = sp.Rational(1, 3) / (1 + XS ** 3), sp.Rational(1, 6) * XS ** 3 / (1 + XS ** 3)
    ok_db = sp.simplify(fwd_bond / back_bond - XS ** -3) == 0 and sp.simplify(fwd_a1 / back_a1 - 2 * XS ** -3) == 0
    checks.check("B1", ok and ok_split and ok_db,
                 "T1: for the aligned L-box (L = 2..7) every record move ends at an isolated site, there are 6L^2 occupied-empty bonds, and with every bond visited at one rate the departure rate is E(L) = 24/(1+x^3) + 24(L-2)/(1+x^4) + 6(L-2)^2/(1+x^5), x = cp; E = 6L^2/(1+x^5) + beta L + gamma with beta = 24x^4(x-1)/((1+x^4)(1+x^5)) and gamma = 24x^3(x-1)^3(x+1)(x^2+1)/((1+x^3)(1+x^4)(1+x^5)), both of the sign of x - 1, and E = 3L^2 at x = 1; the per-bond rule is in detailed balance with the static law at a corner (ratio x^-3), while one attempt per record split over its empty bonds is off by the factor 2")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: growth against departure for the box: the switch is at cp = 1."""
    p, q, r = 3, 1, 2
    c0 = Fraction(6, p + q + 4 * r)
    x = c0 * p
    a1 = p + q + 4 * r
    zc = 1 / (c0 * a1 * (1 + x ** 5))
    if mut("switch_forged"):
        zc = zc * 2

    def gap(z, ll, count="bond"):
        grow = 6 * z * c0 * a1 * ll * ll
        if count == "bond":
            ev = 24 / (1 + x ** 3) + 24 * (ll - 2) / (1 + x ** 4) + 6 * (ll - 2) ** 2 / (1 + x ** 5)
        else:
            ev = 8 / (1 + x ** 3) + 12 * (ll - 2) / (1 + x ** 4) + 6 * (ll - 2) ** 2 / (1 + x ** 5)
        return grow - ev
    sizes = range(2, 201)
    ok_zc = zc == Fraction(16, 825)
    lo = all(gap(Fraction(9, 10) * zc, ll) < 0 for ll in sizes)
    at = all(gap(zc, ll) < 0 for ll in sizes)
    hi = gap(Fraction(11, 10) * zc, 17) < 0 < gap(Fraction(11, 10) * zc, 18) and all(gap(Fraction(11, 10) * zc, ll) > 0 for ll in range(18, 201))
    a1_lo = gap(Fraction(9, 10) * zc, 10, "a1") > 0 > gap(Fraction(9, 10) * zc, 11, "a1")
    neutral = Fraction(6 * p, p + q + 4 * r) - 1 > 0 and 5 * p > q + 4 * r and (Fraction(6 * p, p + q + 4 * r) > 1) == (5 * p > q + 4 * r)
    checks.check("C1", ok_zc and lo and at and hi and a1_lo and neutral,
                 "T2: with growth G = 6 z c A_1 L^2 at the touching sites and z_c = 1/(c A_1 (1 + x^5)), the finite-size terms of E carry the sign of x - 1, so the switch between a largest stable size (x < 1, z < z_c) and a repelling nucleation size (x > 1, z > z_c) is at cp = 1, at the neutral scale 5p = q + 4r; at (3,1,2), c = c0 = 1/2, x = 3/2: z_c = 16/825 exactly, the box shrinks at every size L = 2..200 at (9/10) z_c and at z_c, and at (11/10) z_c it has a repelling size between 17 and 18; the per-record count would instead let it grow up to L = 10 at (9/10) z_c")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: which surface records can leave in one move."""
    normals = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 1, 1), (2, 2, 1), (3, 1, 0), (3, 2, 1), (3, 3, 1), (4, 1, 1), (4, 3, 2),
               (-1, 2, 0), (1, -1, 1), (2, -1, 1), (-3, 1, 2), (1, 2, -4), (0, -2, 3), (4, -4, 1), (-2, -2, -1)]
    ok = True
    for n in normals:
        a = sorted((abs(v) for v in n), reverse=True)
        h, k = a[0], a[1]
        inside = lambda v, n=n: n[0] * v[0] + n[1] * v[1] + n[2] * v[2] <= 0
        rng = range(-6, 7)
        for v in product(rng, repeat=3):
            m = -(n[0] * v[0] + n[1] * v[1] + n[2] * v[2])
            if not (0 <= m < h):
                continue
            nbrs = sum(1 for d in NB if inside(add3(v, d)))
            one_move = []
            for d in NB:
                t = add3(v, d)
                if inside(t):
                    continue
                if all(not inside(add3(t, e)) for e in NB if add3(t, e) != v):
                    one_move.append(d)
            want_n = 3 + sum(1 for i in range(3) if abs(n[i]) <= m)
            can = m < h - k
            if mut("facet_rule_forged"):
                can = m <= h - k
            ok = ok and nbrs == want_n and (len(one_move) == 1) == can and len(one_move) <= 1
            if one_move:
                i = [abs(c) for c in one_move[0]].index(1)
                ok = ok and abs(n[i]) == h
    octa, dode = True, True
    for rr in range(1, 9):
        cells = [v for v in product(range(-rr, rr + 1), repeat=3) if abs(v[0]) + abs(v[1]) + abs(v[2]) <= rr]
        inside = lambda v, rr=rr: abs(v[0]) + abs(v[1]) + abs(v[2]) <= rr
        deps = departures(inside, cells)
        movers = {s for (s, _, _, iso) in deps if iso}
        octa = octa and len(movers) == 6 and all(sorted(map(abs, s)) == [0, 0, rr] for s in movers)
        cells = [v for v in product(range(-rr, rr + 1), repeat=3) if max(abs(v[0]) + abs(v[1]), abs(v[1]) + abs(v[2]), abs(v[0]) + abs(v[2])) <= rr]
        inside = lambda v, rr=rr: max(abs(v[0]) + abs(v[1]), abs(v[1]) + abs(v[2]), abs(v[0]) + abs(v[2])) <= rr
        deps = departures(inside, cells)
        n_iso = sum(1 for (_, _, _, iso) in deps if iso)
        dode = dode and n_iso == (6 + 12 * rr if rr % 2 == 0 else 6 + 12 * (rr - 1))
    checks.check("D1", ok and octa and dode,
                 "T3: on 19 facet normals (signed, |coordinates| <= 4) a record in surface layer m of {n.v <= 0} has 3 + #{i: |n_i| <= m} recorded neighbours and can reach an isolated site in one move iff m < h - k (h >= k the two largest |n_i|), then along the largest normal component only: no record of a tied facet ((110), (111), (221), (331), ...) can leave in one move; the octahedron |x|+|y|+|z| <= R (R = 1..8) loses records in one move only at its six tips, and the rhombic dodecahedron at 6 + 12R (R even) or 6 + 12(R - 1) (R odd) bonds")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: one move is not enough, and what one move reaches."""
    two = True
    for n, ks_want, kt_want in (((1, 1, 1), 3, 2), ((1, 1, 0), 4, 1), ((1, 0, 0), 5, 0)):
        inside = lambda v, n=n: n[0] * v[0] + n[1] * v[1] + n[2] * v[2] <= 0
        o = (0, 0, 0)
        ks = sum(1 for d in NB if inside(add3(o, d)))
        kts = [sum(1 for e in NB if inside(add3(add3(o, d), e)) and add3(add3(o, d), e) != o) for d in NB if not inside(add3(o, d))]
        kt = max(kts)
        hop = 1 / (1 + XS ** (ks - kt))
        want_hop = {3: 1 / (1 + XS), 4: 1 / (1 + XS ** 3), 5: 1 / (1 + XS ** 5)}[ks_want]
        weight = XS ** (-ks)
        if mut("path_weight_forged"):
            weight = XS ** (-ks + 1)
        two = two and ks == ks_want and kt == kt_want and sp.simplify(hop - want_hop) == 0 and sp.simplify(weight * XS ** ks_want - 1) == 0
    # a two-move escape on (111): from the top layer, one move to a site with two recorded neighbours, then one to an isolated site
    inside = lambda v: v[0] + v[1] + v[2] <= 0
    found = False
    for d1 in NB:
        t = add3((0, 0, 0), d1)
        if inside(t):
            continue
        kt = sum(1 for e in NB if inside(add3(t, e)) and add3(t, e) != (0, 0, 0))
        for d2 in NB:
            u = add3(t, d2)
            if inside(u) or u == (0, 0, 0):
                continue
            if all(not inside(add3(u, e)) for e in NB if add3(u, e) != t) and kt == 2:
                found = True
    proj = True
    for ll in range(2, 6):
        cells = set(product(range(ll), repeat=3))
        inside = lambda v, cells=cells: v in cells
        nd = len(departures(inside, list(cells)))
        pa = sum(len({tuple(c[j] for j in range(3) if j != i) for c in cells}) for i in range(3))
        proj = proj and nd == 2 * pa == 6 * ll * ll
    for rr in range(1, 6):
        for shape in ("octa", "dode"):
            if shape == "octa":
                cells = {v for v in product(range(-rr, rr + 1), repeat=3) if abs(v[0]) + abs(v[1]) + abs(v[2]) <= rr}
            else:
                cells = {v for v in product(range(-rr, rr + 1), repeat=3) if max(abs(v[0]) + abs(v[1]), abs(v[1]) + abs(v[2]), abs(v[0]) + abs(v[2])) <= rr}
            inside = lambda v, cells=cells: v in cells
            nd = len(departures(inside, list(cells)))
            pa = sum(len({tuple(c[j] for j in range(3) if j != i) for c in cells}) for i in range(3))
            proj = proj and nd == 2 * pa == 12 * rr * rr + 12 * rr + 6
    checks.check("E1", two and found and proj,
                 "T4: a top-layer record of (111), (110), (100) has k_s = 3, 4, 5 recorded neighbours; on (111) it reaches an isolated site in two moves, the first a hop of probability 1/(1+x) to a site with two recorded neighbours (1/(1+x^3) on (110)), and any displacement to an isolated site multiplies the static weight by x^{-k_s}: a one-move balance is no growth law for tied facets; one move reaches exactly twice the sum of the projection areas: 6L^2 for the box (L = 2..5) and 12R^2 + 12R + 6 for the octahedron and the rhombic dodecahedron (R = 1..5)")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 39 and 40 as landed on main (records that move: the motion clause counted bond by bond, the formation rate, and the neutral scale); it reports how an aligned cluster of moving records loses and gains records at its surface; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Wulff", "Kelvin", "Thomson", "Becker", "Doring", "Döring", "Ostwald", "Slyozov", "Wagner", "Kawasaki", "Glauber", "Metropolis", "Kolmogorov", "Ising", "Potts", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - every occupied-empty bond of the L-box for L = 2..7, with its departure weight and the isolation of its destination",
    "per_site: executed - the surface layers of 19 facet normals: recorded neighbours and one-move destinations of every surface record in a window",
    "per_mode: executed - the rate's split into its L^2, L and constant terms, symbolically in x; detailed balance at a corner for both counts",
    "per_block: executed - growth against departure at (3,1,2) for L = 2..200 at three formation rates; the octahedron, the rhombic dodecahedron and the projection counts",
    "lattice_wide: the box for every L by the census, the facets by the layer rule; the instantaneous accounting of the ideal shape; the motion, the rate convention, the scale and the formation rate supplied",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: aligned clusters of moving records - per-bond departures of the box; the turning size switches at cp = 1 (neutral scale: 5p = q + 4r); tied facets lose no record in one move; growth per facet needs two moves; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
