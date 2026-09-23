#!/usr/bin/env python3
"""Exact checks: a record that cannot read the field from its own motion hops on its own clock, and with kept books records attract
(the owner's moving-records reading; block 53's clock clause, a supplied locality principle, block 55's kept books, block 95's pair law; not adopted).

B (T1): among degree-one rate laws w_x^a w_y^(1 - a), a record's hop rate per tick of its own site is field-free iff a = 1.
C (T2): for amplitudes the three timings are similar generators (one dynamics); for records they are three stationary laws (1/w, 1, w).
D (T3): a = 1 with log(kappa) = -(gamma/6) E/wbar (block 55) makes block 95's pair term attractive.
E (T1, directions): for a = 1 a record picks among empty neighbours with equal odds whatever their clocks.
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
    "docs/ADMISSIBILITY_RULE_A_RECORD_THAT_CANNOT_READ_THE_FIELD_FROM_ITS_OWN_MOTION_HOPS_ON_ITS_OWN_CLOCK_AND_WITH_KEPT_BOOKS_RECORDS_ATTRACT_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "arrival_clock_called_own": "B",
    "record_timings_merged": "C",
    "ledger_sign_flipped": "D",
    "direction_read_from_clocks": "E",
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
def rat(x):
    return sp.Rational(x.numerator, x.denominator)


def zero_mean_green_3d_4():
    cosv = {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}
    L = 4
    ks = [n for n in product(range(L), repeat=3) if n != (0, 0, 0)]
    Ek = {n: 6 - 2 * sum(cosv[c] for c in n) for n in ks}
    return {d: sum((cosv[sum(n[i] * d[i] for i in range(3)) % L] / Ek[n] for n in ks), ZERO) / (L ** 3) for d in product(range(L), repeat=3)}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: among rate laws of degree one, a record's hop rate per tick of its own site is field-free iff the hop is timed by that site."""
    wx, wy, t, a = sp.symbols("w_x w_y t a", positive=True)
    rate = wx ** a * wy ** (1 - a)
    degree_one = sp.simplify(rate.subs({wx: t * wx, wy: t * wy}, simultaneous=True) - t * rate) == 0
    own = sp.simplify(rate / wx)
    d_own = sp.simplify(sp.diff(own, wy))
    field_free_iff = sp.solve(sp.Eq(sp.simplify(d_own * wx ** a * wy ** a / wy ** 0), 0), a) == [1]
    named = {}
    for aa in (1, sp.Rational(1, 2), 0):
        named[aa] = sp.simplify(own.subs(a, aa))
    ok_named = named[1] == 1 and named[sp.Rational(1, 2)] == sp.sqrt(wy / wx) and named[0] == wy / wx
    claim_entering_free = mut("arrival_clock_called_own")
    if claim_entering_free:
        ok_named = ok_named and sp.diff(named[0], wy) == 0
    checks.check("B1", degree_one and field_free_iff and ok_named, "T1: every rate w_x^a w_y^(1 - a) is of degree one (no master clock: all rates times t gives the rate times t); the rate per tick of the record's own site is (w_y/w_x)^(1 - a), whose derivative in the neighbour's clock vanishes identically only for a = 1; timed by the bond a record hops sqrt(w_y/w_x) times per own tick, timed by the site entered w_y/w_x times: only when the site it occupies times the hop does a record's own motion carry no trace of the field")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: for amplitudes the three timings are one dynamics (similar generators); for records they are three stationary laws."""
    w = sp.symbols("w0:4", positive=True)
    tt, ss = sp.symbols("t s", real=True)
    W = sp.diag(*w)
    Wh = sp.diag(*[sp.sqrt(x) for x in w])
    H = sp.zeros(4, 4)
    for x in range(4):
        y = (x + 1) % 4
        H[x, y] = tt + sp.I * ss
        H[y, x] = tt - sp.I * ss
    sim1 = sp.simplify(Wh.inv() * (W * H) * Wh - Wh * H * Wh) == sp.zeros(4, 4)
    sim2 = sp.simplify(Wh * (H * W) * Wh.inv() - Wh * H * Wh) == sp.zeros(4, 4)
    laws = {}
    ok_laws = True
    for aa in (1, sp.Rational(1, 2), 0):
        Q = sp.zeros(4, 4)
        for x in range(4):
            for y in ((x + 1) % 4, (x - 1) % 4):
                r = w[x] ** aa * w[y] ** (1 - aa)
                Q[y, x] += r
                Q[x, x] -= r
        law = sp.Matrix([w[x] ** (1 - 2 * aa) for x in range(4)]) if not mut("record_timings_merged") else sp.Matrix([1 / w[x] for x in range(4)])
        ok_laws = ok_laws and sp.simplify(Q * law) == sp.zeros(4, 1)
        laws[aa] = law
    ratio = sp.simplify(laws[1][0] / laws[0][0] * laws[0][1] / laws[1][1])
    distinct = sp.simplify(ratio - 1) != 0
    checks.check("C1", sim1 and sim2 and ok_laws and distinct, "T2: for an amplitude on a ring of four (hermitian nearest-neighbour H, rates w_0..w_3 symbolic), timing by the site entered (WH), by the bond (sqrt(W) H sqrt(W)) and by the site left (HW) are similar generators - one dynamics in three sets of variables; for one record the three timings have the stationary laws w^(1 - 2a) = 1/w, 1, w (checked exactly) - three different dynamics, the first and last differing by w^2 per record: timing is a matter of variables for amplitudes and of physics for records")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: with records hopping on their own clocks and block 55's kept books, the pair term attracts."""
    gam, E, wbar = sp.symbols("gamma E wbar", positive=True)
    logk = -(gam / 6) * E / wbar if not mut("ledger_sign_flipped") else (gam / 6) * E / wbar
    G = zero_mean_green_3d_4()
    a = 1
    U = {r: 6 * (2 * a - 1) * logk * rat(G[(r, 0, 0)]) for r in (1, 2)}
    diff12 = sp.simplify(U[1] - U[2])
    attract = bool(diff12 < 0)
    closed = sp.simplify(diff12 + gam * E / wbar * (rat(G[(1, 0, 0)]) - rat(G[(2, 0, 0)]))) == 0
    checks.check("D1", attract and closed, f"T3: with a = 1 (T1) and block 55's kept books, log(kappa) = -(gamma/6) E/wbar (gamma, E, wbar > 0), the pair term of block 95 is U(r) = 6 log(kappa) G(r) = -(gamma E/wbar) G(r); on 4^3, U(1,0,0) - U(2,0,0) = -(gamma E/wbar)(G(1,0,0) - G(2,0,0)) = -(gamma E/wbar)(228/7680) < 0: records attract, as amplitudes fall (block 54)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T1 (directions): timed by the site it occupies, a record chooses among its empty neighbours with equal odds whatever their clocks."""
    wx = sp.symbols("w_x", positive=True)
    wn = sp.symbols("w_n0:6", positive=True)
    a = sp.symbols("a", positive=True)
    odds = [wx ** a * wn[e] ** (1 - a) for e in range(6)]
    total = sum(odds)
    probs = [sp.simplify(o / total) for o in odds]
    at_one = [sp.simplify(p.subs(a, 1)) for p in probs]
    uniform = all(p == sp.Rational(1, 6) for p in at_one)
    if mut("direction_read_from_clocks"):
        uniform = all(sp.simplify(p.subs(a, 0)) == sp.Rational(1, 6) for p in probs)
    biased = sp.simplify(probs[0].subs(a, 0) - wn[0] / sum(wn)) == 0
    checks.check("E1", uniform and biased, "T1 (directions): with six empty neighbours at clocks w_n0..w_n5 (symbolic), a record timed by the site it occupies (a = 1) goes to each with probability exactly 1/6 whatever the clocks; timed by the site it enters (a = 0) it goes to neighbour n with probability w_n/sum(w): only the first leaves no trace of the field in where the record goes")


# ============================================================================================ family F
FENCES = (
    "This note works within the owner's moving-records reading (records move, one per site at a time; the possibility at a site shifts as its neighbourhood changes) with block 53's clock clause, a supplied locality principle and block 55's kept books; it reports which end of a hop keeps its time when a record cannot read the field from its own motion, and the sign of the pull that follows; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the own-tick rate of the timing family, symbolic in the exponent and both clocks",
    "per_site: executed - the stationary laws of one record on a ring of four for three timings, symbolic clocks",
    "per_mode: executed - similarity of the three amplitude generators on a ring of four, symbolic clocks and complex hopping",
    "per_block: executed - the sign of the pair term on 4^3 with the kept books",
    "lattice_wide: T1 for every degree-one rate law (the power family symbolic; the general form w_x phi(w_y/w_x) by the same argument); T2 for every finite graph (similarity is algebraic; the laws by block 95 T1); T3 wherever block 95 T4 holds; the local-time principle and the kept books are supplied",
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
    print("scope: which end of a hop keeps its time - a record's hop rate per own tick is field-free only when the site it occupies times the hop (a = 1); for amplitudes the three timings are one dynamics, for records three laws; with a = 1 and block 55's kept books (log kappa = -(gamma/6)E/wbar) block 95's pair term attracts; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
