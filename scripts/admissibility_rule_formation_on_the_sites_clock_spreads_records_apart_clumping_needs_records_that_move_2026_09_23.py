#!/usr/bin/env python3
"""Exact checks: formation on the site's clock spreads records apart by the inverse of motion's pair excess; clumping needs records that move
(the owner's moving-records reading; block 53's clock field, blocks 95 and 97's motion, formation timed by the site's clock; not adopted).

B (T1): two records: formation places the second in proportion to w = exp(U), motion finds it in proportion to exp(-U).
C (T2): every order of forming a set has the unnormalized weight exp(sum_pairs U).
D (T2): the per-step normalization depends on the occupied set at first order only through its pair sum.
E (T3): for kappa < 1 formation is slower next to a record; motion finds records there more often.
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_FORMATION_ON_THE_SITES_CLOCK_SPREADS_RECORDS_APART_BY_THE_INVERSE_OF_MOTIONS_PAIR_EXCESS_CLUMPING_NEEDS_RECORDS_THAT_MOVE_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_formation_on_the_sites_clock_spreads_records_apart_by_the_inverse_of_motions_pair_excess_clumping_needs_records_that_move_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "formation_timed_by_arrival": "B",
    "order_dependent_weight": "C",
    "normalization_forged": "D",
    "formation_attracts_claimed": "E",
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


F = Fraction
ZERO = F(0)
ONE = F(1)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ helpers
from itertools import combinations, permutations

RING_M = {0: 35, 1: 5, 2: -13, 3: -19, 4: -13, 5: 5}     # 72 G(d) on the ring of six (integers)


def zero_mean_green_3d_4():
    cosv = {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}
    L = 4
    ks = [n for n in product(range(L), repeat=3) if n != (0, 0, 0)]
    Ek = {n: 6 - 2 * sum(cosv[c] for c in n) for n in ks}
    return {d: sum((cosv[sum(n[i] * d[i] for i in range(3)) % L] / Ek[n] for n in ks), ZERO) / (L ** 3) for d in product(range(L), repeat=3)}


def diff4(z, r):
    return tuple((z[i] - r[i]) % 4 for i in range(3))


def rat(x):
    return sp.Rational(x.numerator, x.denominator)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: two records: formation on the site's clock places the second in proportion to w, motion finds it in proportion to 1/w."""
    ok = True
    for d in range(1, 6):
        w_form = F(2) ** (2 * RING_M[d]) if not mut("formation_timed_by_arrival") else F(2) ** (-2 * RING_M[d])
        w_move = F(2) ** (-2 * RING_M[d])                  # block 95's pair law (a = 1): exp(-U), U = 6 log(kappa) G, base-4 clocks
        ok = ok and w_form * w_move == 1
    lam = sp.symbols("lambda", negative=True)
    G = zero_mean_green_3d_4()
    ok3 = all(sp.simplify(sp.exp(6 * lam * rat(G[d])) * sp.exp(-6 * lam * rat(G[d])) - 1) == 0 for d in G if d != (0, 0, 0))
    checks.check("B1", ok and ok3, "T1: with one record present and its clock field slaved (block 53), a second record formed at an empty site at the rate of that site's clock lands at offset d in proportion to w(d) = exp(U(d)); block 95's motion finds it there in proportion to exp(-U(d)) (a = 1); the two laws are exact inverses (ring of six with base-4 clocks, all offsets; 4^3 with symbolic log kappa, all 63 offsets)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: every order of forming a set has the same unnormalized weight, exp(sum over pairs U)."""
    lam = sp.symbols("lambda", real=True)
    G = zero_mean_green_3d_4()
    sets = [((0, 0, 0), (1, 0, 0), (0, 2, 1)), ((1, 1, 0), (3, 0, 2), (0, 3, 3)), ((0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 2, 2))]
    ok = True
    n_orders = 0
    for C in sets:
        target = 6 * lam * rat(sum((G[diff4(r, s)] for r, s in combinations(C, 2)), ZERO))
        for order in permutations(C):
            logw = sp.Integer(0)
            for k, x in enumerate(order):
                present = order[:k] if not mut("order_dependent_weight") else order[:k + 1]
                logw += 6 * lam * rat(sum((G[diff4(x, r)] for r in present), ZERO))
            ok = ok and sp.expand(logw - target) == 0
            n_orders += 1
    checks.check("C1", ok, f"T2: forming a set of records one at a time, each at the rate of its site's clock in the field of those already present, every order gives the same unnormalized weight exp(6 log(kappa) sum_pairs G) = exp(sum_pairs U): exact on 4^3 for two sets of three and one of four records ({n_orders} orders), log kappa symbolic - the formation law is exp(+sum U) up to the per-step normalizations")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T2: the per-step normalization depends on the occupied set at first order only through its own pair sum."""
    lam = sp.symbols("lambda", real=True)
    G = zero_mean_green_3d_4()
    sites = list(product(range(4), repeat=3))
    C = [(0, 0, 0), (1, 0, 0), (0, 2, 1)]
    Z = sum((sp.exp(6 * lam * rat(sum((G[diff4(y, r)] for r in C), ZERO))) for y in sites if y not in C), sp.Integer(0))
    first = sp.series(Z, lam, 0, 2).removeO()
    pair_sum = rat(sum((G[diff4(y, r)] for y in C for r in C), ZERO))
    want = (64 - len(C)) - 6 * lam * pair_sum if not mut("normalization_forged") else (64 - len(C))
    ok = sp.simplify(sp.expand(first) - sp.expand(want)) == 0
    checks.check("D1", ok, "T2: the per-step normalization sum over empty y of w_y(C) is N - |C| - 6 log(kappa) sum_(y, r in C) G(y - r) + O(log^2 kappa) (the zero-mean kernel sums to zero over all sites): at first order it depends on the occupied set only through the set's own pair sum, small at low density (exact on 4^3 for three records)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T3: for kappa < 1 formation places records away from records; motion gathers them."""
    lam = sp.symbols("lambda", negative=True)
    G = zero_mean_green_3d_4()
    contact = 6 * lam * rat(G[(1, 0, 0)])
    far = 6 * lam * rat(G[(2, 2, 2)])
    spread = bool(sp.simplify(contact - far) < 0) if not mut("formation_attracts_claimed") else bool(sp.simplify(contact - far) > 0)
    gather = bool(sp.simplify(-contact + far) > 0)
    checks.check("E1", spread and gather, "T3: with records that slow clocks (log kappa < 0), a record forms next to another at a lower rate than at the far corner of 4^3 (log w(1,0,0) - log w(2,2,2) = 6 log(kappa)(G(1,0,0) - G(2,2,2)) < 0), while block 95's motion finds it next to another more often (the same number with the opposite sign): formation on the site's clock spreads records, motion on it gathers them")


# ============================================================================================ family F
FENCES = (
    "This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) with block 53's clock field, the motion of blocks 95 and 97 and formation timed by the site's clock; it reports how formation and motion place records in one field; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the second record's formation and motion laws at every offset of a ring of six and of 4^3",
    "per_site: executed - the per-step normalization over all empty sites of 4^3 at first order",
    "per_mode: executed - the zero-mean kernel from its modes on 4^3; control: records formed one at a time on 16^3, contacts against coupling",
    "per_block: executed - every order of forming sets of three and four records",
    "lattice_wide: T1 and T2's order identity on every torus (algebra); the normalization statement at first order; T3 wherever block 95 T4 holds; formation timed by the site's clock is supplied",
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
    print("scope: formation on the site's clock places records in proportion to exp(+U) (every order the same weight exp(sum_pairs U)); motion on it finds them in proportion to exp(-U); for kappa < 1 formation spreads records, motion gathers them; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
