#!/usr/bin/env python3
"""Exact checks: the unsoldered sphere static law on a plane — algebraic decay by complex rotations with explicit constants.

Scope.  P1: the complex-cosine identity, the modulus identity, the cosine-cosh inequality, the shift lemma on trigonometric monomials.
P2: the series inequality cosh t - 1 <= (t^2/2) cosh t (coefficient ratios 2/((2k)(2k-1))); the mean value bound for log(1+t); the sup-norm
shell counts on Z^2 and on the torus; sum_{j<=R} 8j/(1+j)^2 <= 8 H_R for R <= 60.  P3: the harmonic bound's ingredient log(1+u) >= u/(1+u);
the bounds 8/3 <= e <= 11/4 and cosh 1 <= 8/5; the maximization of gamma - (128/5) beta gamma^2; the two branches of the constants.
P4: the shell sum inequality at kappa' = 1/2 and 1; the solvable two-site instance.  Exact arithmetic only (Fractions and sympy); the runner
scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from math import isqrt
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_PLANAR_COMPLEX_ROTATION_CORRELATION_UPPER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = 'admissibility_rule_sphere_static_law_planar_complex_rotation_correlation_upper_bounds_bounded_theorem_note_2026-09-15'
PARENT_CLAIM_ID = "possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14"
PARENT_FRAGMENT = "Empty-neighbourhood sphere laws"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "No possibility is privileged.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
)

MUTATION_GATE = {
    "complex_cosine_identity_wrong": "B",
    "cosine_cosh_inequality_wrong": "B",
    "cosh_series_ratio_wrong": "B",
    "shift_lemma_wrong": "B",
    "shell_count_wrong": "C",
    "harmonic_log_bound_wrong": "C",
    "e_bounds_wrong": "D",
    "optimization_wrong": "D",
    "torus_sum_wrong": "D",
    "small_beta_branch_wrong": "D",
    "chain_identity_wrong": "E",
    "claim_plane_kernel_injected": "F",
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


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, parent = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 3,
                 "the three declared inputs exist (this note, the axiom memo, the possibility-covariance note on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the five axiom sentences used are present verbatim in the axiom memo")
    fp = normalize_text(parent)
    checks.check("A3", PARENT_CLAIM_ID in fp and PARENT_FRAGMENT in fp, "the parent's claim id and its empty-neighbourhood sphere-law section are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    ph, a, c = sp.symbols("phi a c", real=True)
    rhs = sp.cos(ph) * sp.cosh(a) - sp.I * sp.sin(ph) * sp.sinh(a)
    if mut("complex_cosine_identity_wrong"):
        rhs = sp.cos(ph) * sp.cosh(a) + sp.I * sp.sin(ph) * sp.sinh(a)
    ident = sp.simplify(sp.expand(sp.cos(ph + sp.I * a) - rhs, complex=True)) == 0
    modulus = sp.simplify(sp.re(c * (sp.cos(ph) * sp.cosh(a) - sp.I * sp.sin(ph) * sp.sinh(a))) - c * sp.cos(ph) * sp.cosh(a)) == 0
    checks.check("B1", ident and modulus, "P1(iii): cos(phi + i a) = cos phi cosh a - i sin phi sinh a, so |e^{c cos(phi + i a)}| = e^{c cos phi cosh a} for real c")
    target = (1 - sp.cos(ph)) * (sp.cosh(a) - 1)
    if mut("cosine_cosh_inequality_wrong"):
        target = (1 + sp.cos(ph)) * (sp.cosh(a) - 1)
    factor_ok = sp.simplify(sp.cos(ph) + sp.cosh(a) - 1 - sp.cos(ph) * sp.cosh(a) - target) == 0
    samples = all(sp.simplify((1 - sp.cos(x)) * (sp.cosh(y) - 1)) >= 0 for x in [sp.Rational(i, 4) * sp.pi for i in range(-4, 5)] for y in [sp.Rational(j, 2) for j in range(-4, 5)])
    checks.check("B2", factor_ok and samples, "P1(iii): cos phi + (cosh a - 1) - cos phi cosh a = (1 - cos phi)(cosh a - 1) >= 0")
    t = sp.symbols("t", real=True)
    s1 = sp.series(sp.cosh(t) - 1, t, 0, 20).removeO()
    s2 = sp.series(t ** 2 / 2 * sp.cosh(t), t, 0, 20).removeO()
    k = sp.symbols("k", positive=True, integer=True)
    closed = sp.simplify((1 / sp.factorial(2 * k)) / (1 / (2 * sp.factorial(2 * k - 2))) - 2 / ((2 * k) * (2 * k - 1))) == 0
    ratio_bound = lambda m: Fraction(2, (2 * m) * (2 * m - 1))
    if mut("cosh_series_ratio_wrong"):
        ratio_bound = lambda m: Fraction(2, (2 * m) * (2 * m - 3)) if m > 1 else Fraction(1)
    series_ok = all(s1.coeff(t, 2 * m) / s2.coeff(t, 2 * m) == ratio_bound(m) for m in range(1, 10)) and all(ratio_bound(m) <= 1 for m in range(1, 10))
    checks.check("B3", closed and series_ok, "P2(c): the coefficient ratio of (cosh t - 1) to (t^2/2) cosh t at t^{2k} is 2/((2k)(2k-1)) <= 1 (closed form; k <= 9)")
    F = sum((c * sp.cos(ph)) ** m / sp.factorial(m) for m in range(5)) * sp.exp(sp.I * ph)
    plain = sp.integrate(sp.expand(F), (ph, 0, 2 * sp.pi))
    shifted_expr = sum((c * (sp.cos(ph) * sp.cosh(a) - sp.I * sp.sin(ph) * sp.sinh(a))) ** m / sp.factorial(m) for m in range(5)) * sp.exp(sp.I * ph) * sp.exp(-a)
    shifted = sp.integrate(sp.expand(shifted_expr), (ph, 0, 2 * sp.pi))
    target = plain
    if mut("shift_lemma_wrong"):
        target = plain * sp.exp(-a)
    ok4 = sp.simplify(plain - sp.pi * c * (c ** 2 + 8) / 8) == 0 and sp.simplify(sp.expand((shifted - target).rewrite(sp.exp))) == 0
    checks.check("B4", ok4, "P1(ii): for the trigonometric polynomial F = (sum_{m<=4} (c cos phi)^m/m!) e^{i phi}, the period integral pi c (c^2 + 8)/8 is unchanged by the shift phi -> phi + i a (the shift lemma, executed on a polynomial with a nonzero integral)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    ok = True
    for L in range(2, 13):
        for j in range(1, L + 1):
            cnt = sum(1 for x1 in range(-L + 1, L + 1) for x2 in range(-L + 1, L + 1)
                      if max(min(abs(x1), 2 * L - abs(x1)), min(abs(x2), 2 * L - abs(x2))) == j)
            expected = 8 * j if j < L else 4 * L - 1
            if mut("shell_count_wrong"):
                expected = 8 * j if j < L else 4 * L
            ok = ok and cnt == expected and cnt <= 8 * j
    plane = all(sum(1 for x1 in range(-j, j + 1) for x2 in range(-j, j + 1) if max(abs(x1), abs(x2)) == j) == 8 * j for j in range(1, 30))
    shell_sum = all(sum((Fraction(8 * j, (1 + j) ** 2) for j in range(1, R + 1)), Fraction(0)) <= 8 * harmonic(R) for R in range(1, 61))
    checks.check("C1", ok and plane and shell_sum, "P2(c): sup-norm shells have 8j sites on Z^2 (j < 30) and on the torus 8j (j < L), 4L-1 (j = L) <= 8j for L <= 12; sum_{j<=R} 8j/(1+j)^2 <= 8 H_R exactly for R <= 60")
    t, u = sp.symbols("t u", positive=True)
    mv = sp.simplify(sp.diff(sp.log(1 + t), t) - 1 / (1 + t)) == 0
    q = sp.log(1 + u) - u / (1 + u)
    if mut("harmonic_log_bound_wrong"):
        q = sp.log(1 + u) - u
    q_ok = q.subs(u, 0) == 0 and sp.simplify(sp.diff(q, u) - u / (1 + u) ** 2) == 0
    j = sp.symbols("j", positive=True, integer=True)
    step = sp.simplify((1 / (j - 1)) / (1 + 1 / (j - 1)) - 1 / j) == 0
    checks.check("C2", mv and q_ok and step, "P2(b)/P3: d/dt log(1+t) = 1/(1+t) (the mean value bound); log(1+u) - u/(1+u) vanishes at 0 with derivative u/(1+u)^2 >= 0, and at u = 1/(j-1) the right side is 1/j, so 1/j <= log(j/(j-1)) and H_R <= 1 + log R")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    e_lo = Fraction(1) + 1 + Fraction(1, 2) + Fraction(1, 6)
    tail = Fraction(1, 120) * Fraction(6, 5)
    e_hi = Fraction(65, 24) + tail
    cosh_bound = (Fraction(11, 4) + Fraction(3, 8)) / 2
    lim = Fraction(8, 5)
    if mut("e_bounds_wrong"):
        lim = Fraction(3, 2)
    checks.check("D1", e_lo == Fraction(8, 3) and tail == Fraction(1, 100) and e_hi <= Fraction(11, 4) and cosh_bound == Fraction(25, 16) and cosh_bound <= lim,
                 "P3: 1 + 1 + 1/2 + 1/6 = 8/3 <= e; the tail sum_{k>=5} 1/k! <= (1/120)(6/5) = 1/100, so e <= 65/24 + 1/100 <= 11/4; cosh 1 <= (11/4 + 3/8)/2 = 25/16 <= 8/5")
    g, b = sp.symbols("gamma beta", positive=True)
    kappa = g - sp.Rational(128, 5) * b * g ** 2
    gstar = sp.solve(sp.diff(kappa, g), g)[0]
    kstar = sp.simplify(kappa.subs(g, gstar))
    target = 5 / (512 * b)
    if mut("optimization_wrong"):
        target = 5 / (256 * b)
    pref = sp.simplify(sp.Rational(144, 5) * b * gstar ** 2)
    checks.check("D2", sp.simplify(gstar - 5 / (256 * b)) == 0 and sp.simplify(kstar - target) == 0 and sp.simplify(pref - 45 / (4096 * b)) == 0 and sp.simplify(pref.subs(b, sp.Rational(5, 256)) - sp.Rational(9, 16)) == 0 and sp.simplify(sp.diff(kappa, g, 2)) == -sp.Rational(256, 5) * b,
                 "P3 (beta >= 5/256): gamma - (128/5) beta gamma^2 is concave with maximizer gamma* = 5/(256 beta) and maximum 5/(512 beta); the prefactor exponent (144/5) beta gamma*^2 = 45/(4096 beta) equals 9/16 at beta = 5/256")
    ok3 = True
    for L in range(1, 41):
        # kappa' = 1: sum 8j/(1+j) <= 8L ; kappa' = 1/2: sum 8j/sqrt(1+j) <= 8 L sqrt(1+L)  <=  check termwise j^2 <= (1+j)(1+L)
        ok3 = ok3 and sum((Fraction(8 * j, 1 + j) for j in range(1, L + 1)), Fraction(0)) <= 8 * L
        ok3 = ok3 and all(j * j <= (1 + j) * (1 + L) for j in range(1, L + 1))
    factor = 2
    if mut("torus_sum_wrong"):
        factor = 1
    ok3 = ok3 and all(Fraction(1 + L, L) <= factor for L in range(1, 41))
    checks.check("D3", ok3, "P4(a): sum_{j<=L} 8j(1+j)^{-kappa'} <= 8 L (1+L)^{1-kappa'} at kappa' = 1 (exact sums) and kappa' = 1/2 (termwise j^2 <= (1+j)(1+L)); (1+L)/L <= 2, so 2 C_1 (1+L)^{1-kappa'}/L <= 4 C_1 (1+L)^{-kappa'}")
    b2 = sp.symbols("beta2", positive=True)
    small = 1 - sp.Rational(128, 5) * b2
    thr = sp.Rational(5, 256)
    if mut("small_beta_branch_wrong"):
        thr = sp.Rational(5, 128)
    checks.check("D4", sp.simplify(small.subs(b2, thr) - sp.Rational(1, 2)) == 0 and sp.simplify(sp.Rational(144, 5) * thr - sp.Rational(9, 16)) == 0 and sp.simplify(sp.Rational(128, 5) * thr + sp.Rational(1, 2) - 1) == 0,
                 "P3 (beta <= 5/256): with gamma = 1, kappa = 1 - 128 beta/5 is 1/2 at beta = 5/256 (and larger below), and the prefactor exponent (144/5) beta is 9/16 there; both branches meet at 5/256")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    b = sp.symbols("beta", positive=True)
    Z = 4 * sp.pi * sp.sinh(b) / b
    corr = sp.simplify(sp.diff(sp.log(Z), b))
    target = sp.coth(b) - 1 / b
    if mut("chain_identity_wrong"):
        target = sp.coth(b) + 1 / b
    ident = sp.simplify(sp.expand((corr - target).rewrite(sp.exp))) == 0
    # P1's bound on the two-site instance with a_0 = A, a_1 = 0: (2/3) L(beta) <= exp(-A + beta (cosh A - 1)); at beta = 1, A = 1/2, 1, 3/2
    L1 = sp.coth(1) - 1
    ok = all((sp.Rational(2, 3) * L1 <= sp.exp(-A + (sp.cosh(A) - 1))) for A in (sp.Rational(1, 2), 1, sp.Rational(3, 2)))
    checks.check("E1", ident and ok, "P1 on the solvable two-site instance: <s_0.s_1> = d log Z/d beta = coth beta - 1/beta (Z = 4 pi sinh beta/beta), and (2/3)(coth 1 - 1) <= exp(-A + (cosh A - 1)) at A = 1/2, 1, 3/2")


# ============================================================================================ family F
FENCES = ('For the supplied uniform-sphere exponential nearest-neighbour static model on independent Z^2: P1 proves the complex-shift inequality; P2 bounds the logarithmic shift energy by charging each active bond to a nearer endpoint; P3 gives an explicit correlation upper bound with exponent kappa(beta)>0; P4 gives the torus magnetization bound and the same correlation bound conditional on a DLR law. Windows must contain 0,x and every site with distance less than R=distance(x); tori have L>=2. No exact decay exponent, faster-power exclusion, gravity or dimension-selection claim is retained. This note does not select a physical reading, coupling, rule or dimension and adopts no clause.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'The standard mathematical imports are stated explicitly; they supply mathematical tools, not physical selection.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the true exponent is", "the plane carries a Green-function kernel",
)
CLAIM_INJECTIONS = {"claim_plane_kernel_injected": "Hence the plane carries a Green-function kernel at large beta."}
CLASSICAL_NAMES = ("McBryan", "Spencer", "Pfister", "Kosterlitz", "Thouless", "Berezinskii", "Mermin", "Wagner", "Fröhlich", "Dobrushin", "Shlosman", "Cauchy", "Archimedes", "Peierls", "Toom")  # authors; Dirichlet energy, Green function, Lipschitz name standard objects
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects")
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
    checks.check("F3", not bad and len(scan) > 150, f"runner source: no floating-point literal or conversion call ({len(bad)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for i, sec in enumerate(sections):
        title = sec.splitlines()[0].strip() if i > 0 else "(front matter)"
        body = sec
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem P1"):
            body = body + " (the McBryan–Spencer bound)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports and the Premises; Dirichlet energy, Green function and Lipschitz name standard objects ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the complex-cosine identity; the modulus; the cosine-cosh inequality; the series ratios 2/((2k)(2k-1))",
    "per_site: executed — the shift lemma on a trigonometric polynomial with a nonzero period integral; the mean value bound for log(1+t); the two-site instance",
    "per_mode: executed — the sup-norm shell counts on Z^2 (j < 30) and on tori (L <= 12); sum_{j<=R} 8j/(1+j)^2 <= 8 H_R to R = 60",
    "per_block: executed — the e bounds and cosh 1 <= 8/5; the maximization gamma* = 5/(256 beta), kappa = 5/(512 beta); the two branches at 5/256; the torus shell sum at two exponents",
    "lattice_wide: checked and not executed — written conditional model proofs and bounds only; the finite runner does not execute an infinite lattice or physical classification",
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
    checks = Checks()
    texts = [(ROOT / pth).read_text(encoding="utf-8") if (ROOT / pth).is_file() else "" for pth in AUDIT_INPUT_PATHS]
    print("AUDIT_INPUT_PATHS:")
    for pth in AUDIT_INPUT_PATHS:
        print(f"  {pth}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("scope: the unsoldered sphere static law on a plane — the complex-shift identities, the shift function's shell sums, the explicit constants of the power-law bound, the torus consequence, the solvable two-site instance; exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        observed = "".join(sorted(set(checks.failed_families))) or "none"
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {observed}")
    failed = checks.finish()
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
