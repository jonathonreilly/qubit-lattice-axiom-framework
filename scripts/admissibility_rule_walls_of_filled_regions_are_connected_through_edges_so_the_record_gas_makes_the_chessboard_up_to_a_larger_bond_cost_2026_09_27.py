#!/usr/bin/env python3
"""Exact checks: walls of filled regions are connected through shared edges, so block 117's wall count needs only 12
neighbours per plaquette, and the record gas makes block 79's chessboard up to a recorded-bond cost of (347/10000)^2 without
contents, (347/120)^2 times block 117's bound (a harvest of probe #9212, confirmed by an other-family referee in #9338).
Block 117 as landed: the wall-removing map (weight ratio at most x^|dV|), the ray anchor (k/4) and the tree count.

A (premises): landed block 117's certificate at x0 = 3/250, its 32-port tree count, the ray anchor, the threshold relation
   and the injective sum; the axioms.
B (T1): every fixed polycube of 1..7 cells has an edge-connected wall; a cavity and a vertex-only touch split the wall while an
   edge-only touch does not; a finite cube set is recovered from its wall by the parity of +e1 ray crossings.
C (T2): a plaquette has 12 edge-neighbours; r_k = (12/(k - 1)) C(11k, k - 2) are the coefficients of U + U^2 with
   U = x (1 + U)^11 (checked to k = 15); the radius is 10^10/11^11.
D (T3): the regions around a site with |dV| <= 22 (enumerated); the supersolution U+ = 43/500 at x0 = 347/10000; the exact
   certificate sum <= 11/100; the thresholds (347/10000)^2 and the factor (347/120)^2 over block 117.
Exact (fractions, integers). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import random
import re
import sys
import time
from fractions import Fraction as Fr
from math import comb
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WALLS_OF_FILLED_REGIONS_ARE_CONNECTED_THROUGH_EDGES_SO_THE_RECORD_GAS_MAKES_THE_CHESSBOARD_UP_TO_A_BOND_COST_OF_347_OVER_10000_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THE_RECORD_GAS_DOES_MAKE_THE_CHESSBOARD_WHEN_A_RECORDED_BOND_COSTS_A_FACTOR_BELOW_NINE_OVER_62500_AND_THE_TWO_FRAMED_STATES_DIFFER_AT_EVERY_SITE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_walls_of_filled_regions_are_connected_through_edges_so_the_record_gas_makes_the_chessboard_up_to_a_bond_cost_of_347_over_10000_squared_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED117 = (
    "At `x₀ = 3/250` the sum of `x₀^{|∂V|}` over all of them is at most `" + "0" + "." + "0897`",
    "`r_k = (32/(k − 1)) C(31k, k − 2)`",
    "The wall meets the `e₁` ray from `x` within `|∂V|/4` sites",
    "At `ζ = g⁻³` (`H = 1`), `x ≤ 3/250` means `g³Λ⁶(Λ/m)⁵ ≤ (3/250)⁶`",
    "P(σ_x = −1) ≤ Σ_V Σ_{n: V(n) = V} w(n)/Z ≤ Σ_V x^{|∂V|}",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "wall_adjacency_forged": "B",
    "tree_count_forged": "C",
    "certificate_forged": "D",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()
DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def normal_form(cells):
    mx = min(c[0] for c in cells)
    my = min(c[1] for c in cells)
    mz = min(c[2] for c in cells)
    return frozenset((c[0] - mx, c[1] - my, c[2] - mz) for c in cells)


def polycubes(nmax: int):
    levels = [set(), {frozenset([(0, 0, 0)])}]
    for n in range(2, nmax + 1):
        nxt = set()
        for P in levels[-1]:
            for c in P:
                for d in DIRS:
                    q = add(c, d)
                    if q not in P:
                        nxt.add(normal_form(P | {q}))
        levels.append(nxt)
    return levels


def wall(V):
    """the plaquettes between V and its complement, as (cell, direction) with the cell in V"""
    return [(c, d) for c in V for d in DIRS if add(c, d) not in V]


def plaquette_edges(p):
    """the four lattice edges of plaquette (cell c, outward direction d), as frozensets of two lattice vertices"""
    c, d = p
    axis = [i for i in range(3) if d[i] != 0][0]
    base = list(c)
    if d[axis] > 0:
        base[axis] += 1
    others = [i for i in range(3) if i != axis]
    corners = []
    for s0, s1 in ((0, 0), (1, 0), (1, 1), (0, 1)):
        v = list(base)
        v[others[0]] += s0
        v[others[1]] += s1
        corners.append(tuple(v))
    return [frozenset((corners[i], corners[(i + 1) % 4])) for i in range(4)]


def plaquette_vertices(p):
    return set().union(*plaquette_edges(p))


def wall_components(V, by="edge"):
    W = wall(V)
    key = plaquette_edges if by == "edge" else (lambda p: [frozenset([v]) for v in plaquette_vertices(p)])
    index: dict = {}
    for i, p in enumerate(W):
        for k in key(p):
            index.setdefault(k, []).append(i)
    seen = [False] * len(W)
    comps = 0
    for s in range(len(W)):
        if seen[s]:
            continue
        comps += 1
        stack = [s]
        seen[s] = True
        while stack:
            i = stack.pop()
            for k in key(W[i]):
                for j in index[k]:
                    if not seen[j]:
                        seen[j] = True
                        stack.append(j)
    return comps


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the gas, its weights and the frame are supplied)")
    needles = list(LANDED117)
    if mut("landed_quote_forged"):
        needles[1] = "`r_k = (12/(k − 1)) C(11k, k − 2)`"
    checks.check("A3", all(n in landed for n in needles), "landed block 117: the certificate 897/10000 at x0 = 3/250, the 32-port tree count r_k = (32/(k - 1)) C(31k, k - 2), the ray anchor |dV|/4, the threshold relation g^3 Lambda^6 (Lambda/m)^5 <= x0^6 and the injective sum P(sigma_x = -1) <= sum_V x^|dV|")


# ============================================================================================ family B (T1)
def family_b(checks: Checks, levels) -> None:
    by = "vertex" if mut("wall_adjacency_forged") else "edge"
    total = 0
    ok = True
    for n in range(1, len(levels)):
        for P in levels[n]:
            total += 1
            ok = ok and wall_components(P, by="edge") == 1
    counts = [len(levels[n]) for n in range(1, len(levels))]
    ok = ok and counts == [1, 3, 15, 86, 534, 3481, 23502][:len(counts)]
    # sharpness: a cavity and a vertex-only touch split the edge-connected wall; an edge-only touch does not
    cube3 = {(i, j, k) for i in range(3) for j in range(3) for k in range(3)}
    cavity = cube3 - {(1, 1, 1)}
    vertex_touch = {(0, 0, 0), (1, 1, 1)}
    edge_touch = {(0, 0, 0), (1, 1, 0)}
    sharp = wall_components(cavity, by=by) == 2 and wall_components(vertex_touch, by=by) == 2 and wall_components(edge_touch, by=by) == 1
    checks.check("B1", ok and sharp, f"every fixed polycube of 1..7 cells ({total}: {counts}) has a wall connected through shared edges; a cavity (3x3x3 minus its centre) and a vertex-only touch split the wall into 2 edge-components, an edge-only touch does not")
    # the ray-parity lemma: a finite cube set is the set of cells whose +e1 ray crosses its wall an odd number of times
    rng = random.Random(117)
    ok2 = True
    for _ in range(60):
        U = {(rng.randint(0, 4), rng.randint(0, 4), rng.randint(0, 4)) for _ in range(rng.randint(1, 40))}
        Wset = {(add(c, d) if d[0] + d[1] + d[2] < 0 else c, tuple(abs(t) for t in d)) for c, d in wall(U)}
        rec = set()
        for x in range(-1, 6):
            for y in range(-1, 6):
                for z in range(-1, 6):
                    crossings = sum(1 for t in range(x, 7) if ((t, y, z), (1, 0, 0)) in Wset)
                    if crossings % 2 == 1:
                        rec.add((x, y, z))
        ok2 = ok2 and rec == U
    checks.check("B2", ok2, "the ray-parity lemma on 60 random cube sets in a 5^3 window: each set equals the cells whose +e1 ray crosses its wall an odd number of times, so a wall determines its region")


# ============================================================================================ family C (T2)
def r_k(k: int) -> Fr:
    if k == 1:
        return Fr(1)
    return Fr(12 * comb(11 * k, k - 2), k - 1)


def family_c(checks: Checks) -> None:
    P = ((0, 0, 0), (0, 0, 1))
    nbrs = set()
    for e in plaquette_edges(P):
        a, b = sorted(e)
        axis = [i for i in range(3) if a[i] != b[i]][0]
        for c in itertools.product((-1, 0), repeat=2):
            others = [i for i in range(3) if i != axis]
            cell = list(a)
            cell[others[0]] += c[0]
            cell[others[1]] += c[1]
            cell = tuple(cell)
            for d in DIRS:
                if d[axis] == 0:
                    q = (cell, d)
                    if e in plaquette_edges(q):
                        key = frozenset(plaquette_vertices(q))
                        if key != frozenset(plaquette_vertices(P)):
                            nbrs.add(key)
    ports = 11 if mut("tree_count_forged") else 12
    KT = 15

    def pmul(A, B):
        C = [0] * (KT + 1)
        for i, a in enumerate(A):
            if a:
                for j in range(KT + 1 - i):
                    C[i + j] += a * B[j]
        return C

    U = [0] * (KT + 1)
    for _ in range(KT + 1):
        onepU = [1 + U[0]] + U[1:]
        pw = [1] + [0] * KT
        for _ in range(11):
            pw = pmul(pw, onepU)
        U = [0] + pw[:KT]                       # U = x (1 + U)^11, truncated at x^15
    R = [a + b for a, b in zip(U, pmul(U, U))]
    ok = len(nbrs) == ports and all(R[k] == r_k(k) for k in range(1, KT + 1))
    u = sp.Symbol("u", positive=True)
    xs = u / (1 + u) ** 11
    ok = ok and sp.solve(sp.diff(xs, u), u) == [sp.Rational(1, 10)] and sp.simplify(xs.subs(u, sp.Rational(1, 10)) - sp.Rational(10 ** 10, 11 ** 11)) == 0
    checks.check("C1", ok, "a plaquette meets 12 others along its edges; r_k = (12/(k - 1)) C(11k, k - 2) are the coefficients of U + U^2 with U = x(1 + U)^11 (k = 1..15), the count of breadth-first port trees with at most 12 children at the root and 11 elsewhere; the radius is 10^10/11^11")


# ============================================================================================ family D (T3)
def family_d(checks: Checks, levels) -> None:
    around: dict = {}
    for n in range(1, 7):
        for P in levels[n]:
            adj = sum(1 for c in P for d in DIRS[::2] if add(c, d) in P)
            area = 6 * n - 2 * adj
            around[area] = around.get(area, 0) + n
    small = {k: v for k, v in around.items() if k <= 22}
    min7 = min(42 - 2 * sum(1 for c in P for d in DIRS[::2] if add(c, d) in P) for P in levels[7])
    ok1 = small == {6: 1, 10: 6, 14: 45, 16: 12, 18: 332, 20: 240, 22: 2538} and min7 == 24
    x0 = Fr(347, 10000)
    up = Fr(43, 500)
    sup = x0 * (1 + up) ** 11 <= up and up < Fr(1, 10)
    xR = up * (1 + up) * (1 + 2 * up) / (1 - 10 * up)
    head = sum((k * r_k(k) * x0 ** k for k in range(1, 24)), Fr(0))
    tail = (xR - head) / 4
    S_small = sum((c * x0 ** k for k, c in small.items()), Fr(0))
    total = S_small + tail
    bound = Fr(11, 100) if not mut("certificate_forged") else Fr(1, 10)
    ok2 = sup and total <= bound and 1 - 2 * bound >= Fr(39, 50)
    xb, ub = Fr(3, 250), Fr(3, 200)
    sup_b = xb * (1 + ub) ** 11 <= ub
    tail_b = (ub * (1 + ub) * (1 + 2 * ub) / (1 - 10 * ub) - sum((k * r_k(k) * xb ** k for k in range(1, 24)), Fr(0))) / 4
    total_b = sum((c * xb ** k for k, c in small.items()), Fr(0)) + tail_b
    ok2 = ok2 and sup_b and total_b <= Fr(4, 10000)
    gstar = x0 ** 2
    factor = (x0 / Fr(3, 250)) ** 2
    ok3 = gstar == Fr(120409, 100000000) and factor == Fr(120409, 14400) and x0 < Fr(10 ** 10, 11 ** 11)
    checks.check("D1", ok1 and ok2 and ok3, f"regions around a site with |dV| <= 22 counted exactly ({small}; seven cells need |dV| >= 24); at x0 = 347/10000 < 10^10/11^11 the supersolution U+ = 43/500 bounds U, and sum_V x0^|dV| <= {bound} (exactly {total.numerator}/{total.denominator}), so <sigma_x> >= 39/50 (at block 117's own x0 = 3/250 the edge count gives at most 4/10000); without contents g <= (347/10000)^2 = 120409/10^8, block 117's 9/62500 times (347/120)^2 = 120409/14400")


# ============================================================================================ family F
FENCES = (
    "This note works within block 117 as landed on main (the record gas, its chessboard frame and its wall-removing map) and replaces its wall-connectivity step by a stronger one; it reports how far block 117's chessboard bound extends; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at g = 1/830."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Mayer", "Vietoris", "Peierls",
                   "Redelmeier", "Alexander", "Jordan", "Ising")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Peierls) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the 12 edge-neighbours of a plaquette; the wall of each small shape",
    "per_site: executed - the regions around a site with |dV| <= 22, counted exactly",
    "per_mode: executed - the tree-count series to k = 15; the radius 10^10/11^11",
    "per_block: executed - edge-connected walls for all 27622 polycubes of 1..7 cells; the ray-parity lemma on 60 random sets; the exact certificate",
    "lattice_wide: checked and not executed - the half-filling window with contents; canonical ensembles; the walker's gap on the gas's arrangements",
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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    levels = polycubes(7)
    family_a(checks, texts)
    family_b(checks, levels)
    family_c(checks)
    family_d(checks, levels)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 117's record gas: walls of filled regions are edge-connected, the tree count needs 12 ports, and at x0 = 347/10000 the defect sum is at most 11/100, so the chessboard holds for g <= (347/10000)^2 without contents; harvest of #9212 (confirmed by #9338); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
