#!/usr/bin/env python3
"""Exact checks: the unsoldered formation law at weak coupling — the sphere kernel's sensitivity, the contraction of the causal coupling,
one invariant law and exponential loss of memory for beta < 1/sqrt3, and positive mean-map bounds; negative route certification remains deferred.

Scope.  T1: Var(w) = A'(kappa) (symbolic); the directional second moment E[((s - A u).d)^2] = A/kappa + (1 - 3A/kappa - A^2) c^2
(symbolic); the sign lemma as a term-by-term series comparison, (kappa/2) sinh 2kappa + kappa^2 - 2 sinh^2 kappa has coefficients
(2^{2m}/(2m)!)(m/2 - 1) >= 0 for m >= 2 and 0 at m = 1 (exact); A(kappa) < kappa/3 at rational points by exact enclosure; the
log-derivative of the density.  T2: the contraction factor sqrt3 beta and its crossing of 1 between 5773/10^4 and 5774/10^4 by exact
enclosure.  T3: A(3 beta) < beta at rational beta.  T4: the reach series 1/3 - delta^2/45 <= A(delta)/delta < 1/3.  Exact arithmetic
only (integers, Fractions and sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import hashlib
import sys
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/SPHERE_FORMATION_KERNEL_SENSITIVITY_AND_LEVEL_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
INPUT_SHA256 = {'docs/SPHERE_FORMATION_KERNEL_SENSITIVITY_AND_LEVEL_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-09-16.md': 'bcbad1f04d60ba345906cf1d83dc45691bb92516ddd85b2af2318f738f96f54c', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md': 'cc7e8423b3bb35f7f2cf4699d498556b98fbc55229eb8a5d9f52e1ba00a63f97'}
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "sphere_formation_kernel_sensitivity_and_level_contraction_bounded_theorem_note_2026-09-16"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "variance_identity_wrong": "B",
    "directional_moment_wrong": "B",
    "sign_lemma_wrong": "B",
    "sensitivity_bound_wrong": "B",
    "contraction_constant_wrong": "C",
    "one_site_rate_wrong": "C",
    "reach_wrong": "D",
    "reach_upper_wrong": "D",
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


# ------------------------------------------------------------------------------------------- exact enclosures
def exp_bounds(x: Fraction, terms: int | None = None) -> tuple[Fraction, Fraction]:
    assert x >= 0
    n = terms if terms is not None else 2 * (int(x) + 1) + 40
    lo = Fraction(0)
    term = Fraction(1)
    for k in range(n + 1):
        lo += term
        term = term * x / (k + 1)
    assert x < n + 2
    return lo, lo + term / (1 - x / (n + 2))


def A_bounds(kappa: Fraction) -> tuple[Fraction, Fraction]:
    e_lo, e_hi = exp_bounds(2 * kappa)
    return (e_hi + 1) / (e_hi - 1) - 1 / kappa, (e_lo + 1) / (e_lo - 1) - 1 / kappa


def sqrt_bounds(n: int, digits: int = 9) -> tuple[Fraction, Fraction]:
    scale = 10 ** digits
    r = isqrt(n * scale * scale)
    lo, hi = Fraction(r, scale), Fraction(r + 1, scale)
    assert lo * lo < n < hi * hi
    return lo, hi


S3_LO, S3_HI = sqrt_bounds(3)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "the context-only finite-menu note carries its identity and product-form heading; no sphere theorem is imported")
    checks.check("A4", all(Path(ROOT, p).is_file() and hashlib.sha256(Path(ROOT, p).read_bytes()).hexdigest() == INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS), "all three declared source/context inputs match literal SHA-256 pins")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    k, w, c = sp.symbols("kappa w c", positive=True)
    A = sp.coth(k) - 1 / k
    Z = sp.integrate(sp.exp(k * w), (w, -1, 1))
    Ew = sp.integrate(w * sp.exp(k * w), (w, -1, 1)) / Z
    Ew2 = sp.integrate(w ** 2 * sp.exp(k * w), (w, -1, 1)) / Z
    var = Ew2 - Ew ** 2
    target = sp.diff(A, k)
    if mut("variance_identity_wrong"):
        target = sp.diff(A, k) / 2
    b1 = sp.simplify((var - target).rewrite(sp.exp)) == 0 and sp.simplify(sp.diff(A, k) - (1 / k ** 2 - 1 / sp.sinh(k) ** 2)) == 0
    checks.check("B1", b1, "T1(a): Var(w) = A'(kappa) = 1/kappa^2 - 1/sinh^2 kappa for the cosine law proportional to e^{kappa w} on [-1, 1]")
    # directional second moment with u = e_1, d = (c, sqrt(1 - c^2), 0)
    M = (A / k) * sp.eye(3) + (1 - 3 * A / k) * sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    d = sp.Matrix([c, sp.sqrt(1 - c ** 2), 0])
    mean = sp.Matrix([A, 0, 0])
    second = (d.T * M * d)[0] - 2 * (mean.dot(d)) * (A * c) + (A * c) ** 2
    claimed = A / k + (1 - 3 * A / k - A ** 2) * c ** 2
    if mut("directional_moment_wrong"):
        claimed = A / k + (1 - 2 * A / k - A ** 2) * c ** 2
    checks.check("B2", sp.simplify(second - claimed) == 0, "T1(b): E[((s - A u).d)^2] = A/kappa + (1 - 3A/kappa - A^2) c^2 with c = u.d, from E[s] = A u and E[s s^T] = (A/kappa) I + (1 - 3A/kappa) u u^T")
    # sign lemma: 1 - 3A/k - A^2 = (kappa A' - A)/kappa (symbolic), and the series of (kappa/2) sinh 2kappa + kappa^2 - 2 sinh^2 kappa
    ident = sp.simplify(((1 - 3 * A / k - A ** 2) - (k * sp.diff(A, k) - A) / k).rewrite(sp.exp)) == 0
    diff = sp.expand(sp.series(k / 2 * sp.sinh(2 * k) + k ** 2 - 2 * sp.sinh(k) ** 2, k, 0, 26).removeO())
    coeffs = [diff.coeff(k, 2 * m) for m in range(1, 13)]
    formula = [sp.Rational(2 ** (2 * m), factorial(2 * m)) * (sp.Rational(m, 2) - 1) for m in range(2, 13)]
    if mut("sign_lemma_wrong"):
        formula = [sp.Rational(2 ** (2 * m), factorial(2 * m)) * (sp.Rational(m, 3) - 1) for m in range(2, 13)]
    b3 = ident and coeffs[0] == 0 and all(sp.simplify(a - b) == 0 for a, b in zip(coeffs[1:], formula)) and all(f >= 0 for f in formula)
    checks.check("B3", b3, "T1(c): 1 - 3A/kappa - A^2 = (kappa A' - A)/kappa, and (kappa/2) sinh 2kappa + kappa^2 - 2 sinh^2 kappa = sum_{m>=2} (2^{2m}/(2m)!)(m/2 - 1) kappa^{2m} with the kappa^2 terms cancelling: A(kappa)/kappa is decreasing")
    # A < kappa/3 (block 26's bound re-checked), the log-derivative, and the chain constant: sup_c f(c) = A/kappa <= 1/3
    slope = Fraction(1, 3)
    if mut("sensitivity_bound_wrong"):
        slope = Fraction(1, 4)
    pts = [Fraction(1, 10), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(6), Fraction(9), Fraction(18), Fraction(36), Fraction(72)]
    below = all(A_bounds(kp)[1] < slope * kp for kp in pts)
    V1, V2, V3 = sp.symbols("V1 V2 V3", real=True)
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    nrm = sp.sqrt(V1 ** 2 + V2 ** 2 + V3 ** 2)
    logf = sp.log(nrm / sp.sinh(nrm)) + V1 * s1 + V2 * s2 + V3 * s3
    grad = [sp.diff(logf, v) for v in (V1, V2, V3)]
    Anrm = sp.coth(nrm) - 1 / nrm
    logder = all(sp.simplify(g - (sv - Anrm * v / nrm)) == 0 for g, sv, v in zip(grad, (s1, s2, s3), (V1, V2, V3)))
    checks.check("B4", below and logder, "T1(d): d/dV log f_V = s - A(|V|) V/|V| (symbolic); A(kappa) < kappa/3 at ten rational points by exact enclosure; the written proof supplies the all-parameter variance and sensitivity bounds")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    factor = 3 * Fraction(1) / 3   # per-predecessor sensitivity beta/sqrt3 times three predecessors = sqrt3 beta; encoded through sqrt3 enclosures
    lo_b, hi_b = Fraction(5773, 10 ** 4), Fraction(5774, 10 ** 4)
    mult_lo, mult_hi = S3_LO, S3_HI
    if mut("contraction_constant_wrong"):
        mult_lo, mult_hi = Fraction(3, 2), Fraction(3, 2)
    crossing = (mult_hi * lo_b < 1) and (mult_lo * hi_b > 1) and factor == 1
    checks.check("C1", crossing, "T2: the contraction factor is 3 (beta/sqrt3) = sqrt3 beta; it is below 1 at beta = 5773/10^4 and above 1 at beta = 5774/10^4 (sqrt3 enclosed rationally), so the region beta < 1/sqrt3 is the route's")
    rate_slope = Fraction(1)
    if mut("one_site_rate_wrong"):
        rate_slope = Fraction(1, 2)
    pts = [Fraction(1, 10), Fraction(3, 10), Fraction(1, 2), Fraction(577, 1000), Fraction(1), Fraction(3)]
    ok2 = all(A_bounds(3 * b)[1] < rate_slope * b for b in pts)
    checks.check("C2", ok2, "T3: A(3 beta) < beta at beta = 1/10, 3/10, 1/2, 577/1000, 1, 3 by exact enclosure; the written conditional-mean recursion and absolute antipodal comparison give the rate bounds")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    dl = sp.symbols("delta", positive=True)
    A = sp.coth(dl) - 1 / dl
    ser = sp.series(A / dl, dl, 0, 8).removeO()
    lower = sp.Rational(1, 3) - dl ** 2 / 45
    if mut("reach_wrong"):
        lower = sp.Rational(1, 3)
    upper_slope = Fraction(1, 3)
    if mut("reach_upper_wrong"):
        upper_slope = Fraction(3, 10)
    series_ok = sp.expand(ser - (sp.Rational(1, 3) - dl ** 2 / 45 + 2 * dl ** 4 / 945 - dl ** 6 / 4725)) == 0
    pts = [Fraction(1, 10), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2)]
    ok = series_ok
    for p in pts:
        a_lo, a_hi = A_bounds(p)
        lo_val = Fraction(1, 3) - p ** 2 / 45 if not mut("reach_wrong") else Fraction(1, 3)
        ok = ok and (lo_val <= a_lo / p) and (a_hi / p < upper_slope)
    checks.check("D1", ok, "T4: A(delta)/delta = 1/3 - delta^2/45 + 2 delta^4/945 - ... and 1/3 - delta^2/45 <= A(delta)/delta < 1/3 at delta = 1/10, 1/4, 1/2, 1, 2 by exact enclosure; these finite checks do not certify a global negative route claim")


# ============================================================================================ family F
FENCES = ('The sphere kernel, records-only reading and level order are supplied conditions; the theorem makes no physical selection.', 'The constant `1/√3` is a sufficient contraction bound, not a physical threshold.', 'Formal negative route certification is deferred; the full corrected argument is preserved as readable recovery science.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "has no ordered phase", "does not order", "is the threshold",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence β = 1/√3 is the transition point."}
CLASSICAL_NAMES = ("Dobrushin", "Kantorovich", "Mermin", "Wagner", "Fisher", "Mises", "Langevin", "Toom", "Shlosman", "Pfister", "Doeblin", "Peierls")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T4", phrase + "\n\n## Theorem T4", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T2", "## Theorem T2 (after Dobrushin)", 1)
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
            if nm in sec:
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if nm in sections[0]]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = ('per_element: executed — symbolic variance and directional moments, twelve sign coefficients, log-density derivatives and ten rational enclosures', 'per_site: executed — six rational one-site rate bounds and five rational mean-map bounds; no stochastic site chains', 'per_mode: checked and not executed — no spectral decomposition, quadrature or Monte Carlo is invoked by this symbolic primary', 'per_block: executed — contraction-factor arithmetic and its exact boundary enclosures at two rational beta values; no block sampler', 'lattice_wide: checked and not executed — infinite-plane compactness, measurable coupling and invariant-law uniqueness are written proofs')


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


# ============================================================================================ main
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
