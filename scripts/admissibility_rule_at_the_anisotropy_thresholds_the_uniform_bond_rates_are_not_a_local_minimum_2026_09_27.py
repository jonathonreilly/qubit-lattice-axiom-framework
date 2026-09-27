#!/usr/bin/env python3
"""Exact checks: at the anisotropy thresholds of blocks 88 and 89 the uniform bond rates are not a local minimum along the
traceless path, because the sea energy has a cubic term of definite sign there and the law's cost has none (a harvest of
probe #9222, confirmed by an other-family referee in #9337). Blocks 88 and 89 as landed.

A (premises): landed block 88's cost 36 beta eps^2, threshold chi_a/72 and its open equality case; block 89's threshold
   (chi_a + 2J)/72 and its open equality case; the axioms.
B (T1, linear rates at fixed arithmetic mean): sqrt(Q), Q = (1+2e)^2 a + (1-e)^2 b, has second derivative 9ab/Q^(3/2) at every e;
   the sea energy's cubic coefficient, averaged over the axes, is (3/2) sum_i u_i (u_j - u_k)^2/|s|^5 >= 0 (u_j = sin^2 k_j).
C (T2, rates at fixed mean log): Q = e^(4e) a + e^(-2e) b; the cubic coefficient is -(s1^3 + 9 s1 s2/2 + 81 s3/2)/(3|s|^5) < 0;
   the second derivative exceeds the linear model's by (4a + b)/sqrt(a + b), as block 89 states.
D (T3): every e-derivative of sqrt(Q) is homogeneous of degree one in s, so it is bounded by a constant times |s| near e = 0
   and differentiation under the zone average is justified; the linear cubic integrand is positive at a sample point.
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_AT_THE_ANISOTROPY_THRESHOLDS_THE_UNIFORM_BOND_RATES_ARE_NOT_A_LOCAL_MINIMUM_BECAUSE_THE_SEA_HAS_A_CUBIC_TERM_OF_DEFINITE_SIGN_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THE_TWO_INSTABILITIES_OF_THE_UNIFORM_BOND_RATES_THE_ALTERNATION_BREAKS_TRANSLATION_BELOW_ALPHA_PLUS_2BETA_THE_ANISOTROPY_BREAKS_ROTATION_BELOW_BETA_ALONE_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/ADMISSIBILITY_RULE_THE_UNIT_OF_RATE_DECIDES_THE_ALTERNATIONS_THRESHOLDS_IN_LOG_RATES_AN_EXACT_MASS_A_CONVEXITY_TERM_AND_NO_GLOBAL_MINIMUM_UNDER_A_QUADRATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-23.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_at_the_anisotropy_thresholds_the_uniform_bond_rates_are_not_a_local_minimum_because_the_sea_has_a_cubic_term_of_definite_sign_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED88 = (
    "Thus u=epsilon(2,-1,-1) has quadratic cost 36beta epsilon^2 per site.",
    "Their sign changes are alpha+2beta=chi/12 and beta=chi_a/72.",
    "A zero anisotropy coefficient alone does not settle a minimum; higher orders can matter.",
)
LANDED89 = (
    "Its zero is beta=(chi_a+2J)/72",
    "at equality higher-order analysis is needed",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "linear_cubic_forged": "B",
    "log_cubic_forged": "C",
    "homogeneity_forged": "D",
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
e = sp.Symbol("e", real=True)
a, b = sp.symbols("a b", positive=True)
u1, u2, u3 = sp.symbols("u1 u2 u3", positive=True)
U = (u1, u2, u3)


def symmetrize(expr_in_u):
    """average over the six permutations of (u1, u2, u3)"""
    total = 0
    for perm in itertools.permutations(U):
        total += expr_in_u.subs(dict(zip(U, perm)), simultaneous=True)
    return sp.simplify(total / 6)


def cubic_coeff(Q):
    """the coefficient of e^3 in -sqrt(Q(e)), with a = u1 and b = u2 + u3"""
    f = sp.sqrt(Q)
    third = sp.diff(f, e, 3).subs(e, 0)
    return sp.simplify(-third / 6).subs({a: u1, b: u2 + u3}, simultaneous=True)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t88, t89 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the rates, the law's cost and the sea are supplied)")
    n88 = list(LANDED88)
    if mut("landed_quote_forged"):
        n88[1] = "Their sign changes are alpha+2beta=chi/12 and beta=chi_a/36."
    checks.check("A3", all(n in t88 for n in n88) and all(n in t89 for n in LANDED89), "landed block 88: the cost 36 beta eps^2 of u = eps(2, -1, -1), the threshold beta = chi_a/72 and 'a zero anisotropy coefficient alone does not settle a minimum'; landed block 89: the threshold beta = (chi_a + 2J)/72 and 'at equality higher-order analysis is needed'")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    Q = (1 + 2 * e) ** 2 * a + (1 - e) ** 2 * b
    second = sp.simplify(sp.diff(sp.sqrt(Q), e, 2) - 9 * a * b / Q ** sp.Rational(3, 2))
    c3 = cubic_coeff(Q)
    s1 = u1 + u2 + u3
    target = sp.Rational(3, 2) * (u1 * (u2 - u3) ** 2 + u2 * (u1 - u3) ** 2 + u3 * (u1 - u2) ** 2) / s1 ** sp.Rational(5, 2)
    if mut("linear_cubic_forged"):
        target = -target
    ok = second == 0 and sp.simplify(symmetrize(c3) - target) == 0
    second0 = sp.simplify(-sp.diff(sp.sqrt(Q), e, 2).subs(e, 0) + 9 * a * b / (a + b) ** sp.Rational(3, 2))
    checks.check("B1", ok and second0 == 0, "linear rates at fixed arithmetic mean, Q = (1 + 2e)^2 a + (1 - e)^2 b with a = s_x^2, b = s_y^2 + s_z^2: d^2 sqrt(Q)/de^2 = 9ab/Q^(3/2) at every e (block 88's -9ab/|s|^3 at e = 0), and the sea energy's cubic coefficient averaged over the axes is (3/2) sum_i u_i (u_j - u_k)^2/|s|^5 >= 0, u_j = sin^2 k_j")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    Q = sp.exp(4 * e) * a + sp.exp(-2 * e) * b
    c3 = cubic_coeff(Q)
    s1 = u1 + u2 + u3
    s2 = u1 * u2 + u1 * u3 + u2 * u3
    s3 = u1 * u2 * u3
    target = -(s1 ** 3 + sp.Rational(9, 2) * s1 * s2 + sp.Rational(81, 2) * s3) / (3 * s1 ** sp.Rational(5, 2))
    if mut("log_cubic_forged"):
        target = -(s1 ** 3 + sp.Rational(9, 2) * s1 * s2 + sp.Rational(27, 2) * s3) / (3 * s1 ** sp.Rational(5, 2))
    ok = sp.simplify(symmetrize(c3) - target) == 0
    Ql = (1 + 2 * e) ** 2 * a + (1 - e) ** 2 * b
    excess = sp.simplify(sp.diff(sp.sqrt(Q), e, 2).subs(e, 0) - sp.diff(sp.sqrt(Ql), e, 2).subs(e, 0) - (4 * a + b) / sp.sqrt(a + b))
    checks.check("C1", ok and excess == 0, "rates at fixed mean log, Q = e^(4e) a + e^(-2e) b: the second derivative exceeds the linear model's by (4a + b)/sqrt(a + b) (block 89 T3), and the cubic coefficient averaged over the axes is -(s1^3 + 9 s1 s2/2 + 81 s3/2)/(3|s|^5) < 0, the s_i the elementary symmetric functions of the u_j")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    lam = sp.Symbol("lam", positive=True)
    ok = True
    for Q in ((1 + 2 * e) ** 2 * a + (1 - e) ** 2 * b, sp.exp(4 * e) * a + sp.exp(-2 * e) * b):
        for n in (1, 2, 3, 4):
            d = sp.diff(sp.sqrt(Q), e, n)
            scaled = d.subs({a: lam ** 2 * a, b: lam ** 2 * b}, simultaneous=True)
            deg = 1 if not mut("homogeneity_forged") else 2
            ok = ok and sp.simplify(scaled - lam ** deg * d) == 0
    lin = sp.Rational(3, 2) * (u1 * (u2 - u3) ** 2 + u2 * (u1 - u3) ** 2 + u3 * (u1 - u2) ** 2) / (u1 + u2 + u3) ** sp.Rational(5, 2)
    ok = ok and lin.subs({u1: 1, u2: sp.Rational(1, 2), u3: 0}) > 0
    checks.check("D1", ok, "every e-derivative of sqrt(Q) (orders 1..4, both paths) is homogeneous of degree one in s, so near e = 0 it is bounded by a constant times |s| on the zone and the averages may be differentiated; the linear cubic integrand is positive at u = (1, 1/2, 0), so its average is strictly positive, while the log one is negative wherever s != 0")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 88 and 89 as landed on main (the uniform bond rates, the supplied quadratic law's cost and the walker sea's energy along the traceless anisotropy) and settles the equality case both left open; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at beta = chi_a/72."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Landau", "Daleckii", "Krein",
                   "Lebesgue", "Jahn", "Teller", "Peierls")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Landau) —", 1)
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
    "per_element: executed - the second and third e-derivatives of sqrt(Q) on both paths",
    "per_site: executed - the axis-averaged cubic integrands in the symmetric functions of the u_j",
    "per_mode: executed - homogeneity of every derivative to fourth order; the sign at a sample point",
    "per_block: executed - agreement with blocks 88 and 89's second-order statements",
    "lattice_wide: checked and not executed - the window above threshold (the probe's exact lower sums); intermediate-q directions; finite grids with zero modes",
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
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: blocks 88 and 89 as landed: along the traceless anisotropy the sea energy's cubic coefficient is (3/2)<sum u_i(u_j - u_k)^2/|s|^5> > 0 in linear rates and -<(s1^3 + 9 s1 s2/2 + 81 s3/2)/(3|s|^5)> < 0 in log rates; the law's cost is quadratic; so at each threshold the uniform rates are not a local minimum along the path; harvest of #9222 (confirmed by #9337); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
