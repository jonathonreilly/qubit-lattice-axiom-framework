#!/usr/bin/env python3
"""Exact checks: persistent records in three dimensions - with block 96's direction memory (keep with probability p, turn to
one of the other five otherwise) the density branch stays real and leads at every wave number along the axes, and along the
body diagonal it turns complex exactly past |sin kappa| = 3(1 - p)/(3p + 2), below the line's (1 - p)/p; the waves are damped
(a harvest block from a Grok-refereed probes attempt; block 96 as landed supplied; not adopted).

B (T1): the axis - the factorization, the secular function's monotonicity, and the realness of the leading multiplier.
C (T2): the body diagonal - the factorization and the exact threshold.
D (T3): the long-memory scaling and block 96's executed grid.
E (T4): the line, and the damping of every density branch.
Exact symbolic arithmetic only; the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_PERSISTENT_RECORDS_IN_THREE_DIMENSIONS_CARRY_DAMPED_DENSITY_WAVES_ALONG_THE_BODY_DIAGONALS_PAST_AN_EXACT_THRESHOLD_AND_NONE_ALONG_THE_AXES_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_persistent_records_in_three_dimensions_carry_damped_density_waves_along_the_body_diagonals_past_an_exact_threshold_and_none_along_the_axes_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "A site never carries more than one record; records are permanent.",
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "axis_cubic_forged": "B",
    "diagonal_threshold_forged": "C",
    "scaling_forged": "D",
    "damping_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: one record per site; each site has a domain of local possibilities (the direction a record carries); Admissibility is not a dynamics axiom (the persistent motion is a supplied clause)")


# ============================================================================================ block 96's direction-memory matrix
P_, LAM, Z, C_, T_ = sp.symbols("p lambda z c t")
Q_ = (1 - P_) / 5
A_ = P_ - Q_


def mode_charpoly(phases):
    """det(lambda - E(k) T), T = p I + q (J - I), E = diag(e^(-i k.d)) over d = +e1, -e1, +e2, -e2, +e3, -e3."""
    tm = sp.Matrix(6, 6, lambda i, j: P_ if i == j else Q_)
    mat = sp.diag(*phases) * tm
    return sp.expand((LAM * sp.eye(6) - mat).det())


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: on the axes the density branch is real and simple, and it leads."""
    full = mode_charpoly([Z, 1 / Z, 1, 1, 1, 1])
    cubic = LAM ** 3 - ((10 * C_ * P_ + 2 * P_ + 3) / 5) * LAM ** 2 + (6 * P_ - 1) * (2 * C_ * P_ + 8 * C_ + 4 * P_ + 1) * LAM / 25 - (6 * P_ - 1) ** 2 / 25
    if mut("axis_cubic_forged"):
        cubic += LAM / 100
    target = sp.expand(((LAM - A_) ** 3 * cubic).subs(C_, (Z + 1 / Z) / 2))
    ok_fact = sp.simplify(full - target) == 0
    d = LAM ** 2 - 2 * A_ * LAM * C_ + A_ ** 2
    n = LAM ** 2 * C_ - 2 * A_ * LAM + A_ ** 2 * C_
    ok_mono = sp.expand(d ** 2 - n ** 2 - (1 - C_ ** 2) * (LAM ** 2 - A_ ** 2) ** 2) == 0
    ok_pa = sp.expand(cubic.subs(LAM, A_) + 8 * Q_ * A_ ** 2 * (1 - C_)) == 0
    p_of_t = (5 * T_ ** 3 + 1) / 6
    bracket = sp.expand(sp.simplify(cubic.subs(P_, p_of_t).subs(LAM, T_ ** 2) / (T_ ** 4 / 5)))
    ok_br = (sp.factor(bracket.subs(C_, 1) - 5 * (T_ - 1) ** 3 * (T_ + 1)) == 0
             and sp.factor(bracket.subs(C_, -1) - sp.Rational(5, 3) * (T_ - 1) * (T_ + 1) * (T_ ** 2 + 4 * T_ + 1)) == 0
             and sp.degree(bracket, C_) == 1)
    checks.check("B1", ok_fact and ok_mono and ok_pa and ok_br,
                 "T1: along an axis det(lambda - M) = (lambda - a)^3 P(lambda) exactly (a = (6p - 1)/5), with P the stated cubic in c = cos kappa; D^2 - N^2 = (1 - c^2)(lambda^2 - a^2)^2 makes the secular function strictly decreasing on (a, oo), so P has one simple root above a, the density branch; P(a) = -8 q a^2 (1 - c); with a = t^3 the bracket of P(t^2) is linear in c and equals 5(t - 1)^3 (t + 1) at c = 1 and (5/3)(t - 1)(t + 1)(t^2 + 4t + 1) at c = -1, both negative, so any complex pair has modulus below the density branch: on the axes the leading multiplier is real at every kappa")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: along the body diagonal the density branch turns complex exactly past |sin kappa| = 3(1 - p)/(3p + 2)."""
    full = mode_charpoly([Z, 1 / Z, Z, 1 / Z, Z, 1 / Z])
    quad = LAM ** 2 - 2 * LAM * C_ * (3 * P_ + 2) / 5 + (6 * P_ - 1) / 5
    target = sp.expand(((LAM - A_ * Z) ** 2 * (LAM - A_ / Z) ** 2 * quad).subs(C_, (Z + 1 / Z) / 2))
    ok_fact = sp.simplify(full - target) == 0
    s = sp.symbols("s", nonnegative=True)
    qdisc = sp.expand((C_ * (3 * P_ + 2) / 5) ** 2 - (6 * P_ - 1) / 5)
    want = (9 * (1 - P_) ** 2 - s ** 2 * (3 * P_ + 2) ** 2) / 25
    if mut("diagonal_threshold_forged"):
        want = (9 * (1 - P_) ** 2 - s ** 2 * (3 * P_ + 1) ** 2) / 25
    ok_disc = sp.expand(qdisc.subs(C_ ** 2, 1 - s ** 2) - want) == 0 and sp.expand((3 * P_ + 2) ** 2 - 5 * (6 * P_ - 1) - 9 * (1 - P_) ** 2) == 0
    below_edge = sp.solve(sp.Eq(3 * (1 - P_), 3 * P_ + 2), P_) == [sp.Rational(1, 6)]
    gap = sp.simplify((1 - P_) / P_ - 3 * (1 - P_) / (3 * P_ + 2) - 2 * (1 - P_) / (P_ * (3 * P_ + 2))) == 0
    checks.check("C1", ok_fact and ok_disc and below_edge and gap,
                 "T2: along the body diagonal det(lambda - M) = (lambda - a z)^2 (lambda - a/z)^2 Q(lambda) exactly, Q = lambda^2 - 2 lambda c (3p + 2)/5 + (6p - 1)/5; its quarter-discriminant is [9(1 - p)^2 - sin^2 kappa (3p + 2)^2]/25 (by (3p + 2)^2 - 5(6p - 1) = 9(1 - p)^2), so the density branch is complex exactly when |sin kappa| > 3(1 - p)/(3p + 2), a threshold inside the zone iff p > 1/6 and below the line's (1 - p)/p by 2(1 - p)/(p(3p + 2)); the complex pair has modulus sqrt(a) > a, so the leading multiplier leaves the real line there")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the long-memory scaling and block 96's executed grid."""
    eps = sp.symbols("epsilon", positive=True)
    kstar = sp.asin(3 * eps / (5 - 3 * eps))
    ser = sp.series(kstar, eps, 0, 4).removeO()
    want = sp.Rational(3, 5) * eps + sp.Rational(9, 25) * eps ** 2 + sp.Rational(63, 250) * eps ** 3
    if mut("scaling_forged"):
        want += eps ** 3 / 1000
    ok_ser = sp.simplify(ser - want) == 0
    thr = lambda pv: 3 * (1 - pv) / (3 * pv + 2)
    s12, s6 = sp.sin(sp.pi / 12), sp.sin(sp.pi / 6)
    grid = (sp.simplify(s12 - thr(sp.Rational(9, 10))) > 0 and sp.simplify(s12 - thr(sp.Rational(99, 100))) > 0
            and sp.simplify(s12 - thr(sp.Rational(1, 2))) < 0 and sp.simplify(s6 - thr(sp.Rational(1, 2))) > 0)
    checks.check("D1", ok_ser and grid,
                 "T3: with eps = 1 - p the diagonal threshold is kappa* = arcsin(3 eps/(5 - 3 eps)) = 3 eps/5 + 9 eps^2/25 + 63 eps^3/250 + ..., so the memory length per coordinate is about 5/(3 eps); on block 96's 24^3 grid (kappa = n pi/12) the first diagonal point is past the threshold at p = 9/10 and 99/100, while at p = 1/2 the first is below it and the second past it (exact comparisons with sin(pi/12) = (sqrt 6 - sqrt 2)/4)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the line (block 96 T2.1) and the damping."""
    mu, k = sp.symbols("mu k", real=True)
    s = sp.symbols("s", nonnegative=True)
    line = mu ** 2 - 2 * P_ * sp.cos(k) * mu + (2 * P_ - 1)
    qd = sp.expand((P_ * sp.cos(k)) ** 2 - (2 * P_ - 1))
    ok_line = sp.expand(qd.subs(sp.cos(k) ** 2, 1 - s ** 2) - ((1 - P_) ** 2 - P_ ** 2 * s ** 2)) == 0
    damped = True
    for pv in (sp.Rational(1, 2), sp.Rational(9, 10), sp.Rational(99, 100)):
        for cv in (sp.Rational(3, 5), sp.Rational(0), sp.Rational(-4, 5)):
            quad = (LAM ** 2 - 2 * LAM * C_ * (3 * P_ + 2) / 5 + (6 * P_ - 1) / 5).subs({P_: pv, C_: cv})
            roots = sp.solve(quad, LAM)
            damped = damped and all(sp.simplify(sp.Abs(r) ** 2 - 1) < 0 for r in roots)
    if mut("damping_forged"):
        damped = not damped
    checks.check("E1", ok_line and damped,
                 "T4: on the line (block 96 T2.1) the density multiplier mu^2 - 2p cos k mu + (2p - 1) is complex exactly when |sin k| > (1 - p)/p; the diagonal's complex density branches have modulus sqrt(a) < 1 and its real ones lie inside the unit disk (exact at p = 1/2, 9/10, 99/100 and three angles): the density waves of persistent records are damped, as every nonnegative gain-one rule's must be (block 122)")


# ============================================================================================ family F
FENCES = (
    "This note works within block 96's direction-memory motion of records, as landed on main; it reports where in three dimensions the density branch of persistent records turns complex, along the axes and along the body diagonals, and that the resulting density waves are damped; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Perron", "Frobenius", "Wielandt", "Schur", "Cohn", "Jury", "Cayley", "Hamilton", "Markov", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the axis cubic P and the diagonal quadratic Q against the full 6x6 determinants, symbolic in p and z = e^(-i kappa)",
    "per_site: executed - the monotonicity identity D^2 - N^2 = (1 - c^2)(lambda^2 - a^2)^2 and P(a) = -8 q a^2 (1 - c)",
    "per_mode: executed - the bracket of P(t^2) at c = 1 and c = -1; the diagonal quarter-discriminant and threshold; the long-memory series",
    "per_block: executed - block 96's 24^3 grid points against the threshold (exact); the damping of the diagonal branches at three p and three angles",
    "lattice_wide: the axes and the body diagonals for every p in (1/6, 1) and every kappa; general directions and the extremality of the diagonal are not claimed (a second attempt, unrefereed, treats them); the motion is supplied",
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
    print("scope: persistent records in 3D - along the axes the density branch is real and leads at every kappa; along the body diagonal it turns complex exactly past |sin kappa| = 3(1 - p)/(3p + 2); every density branch is damped; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
