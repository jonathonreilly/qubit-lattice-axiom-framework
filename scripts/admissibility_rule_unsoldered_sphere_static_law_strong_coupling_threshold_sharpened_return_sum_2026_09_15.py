#!/usr/bin/env python3
"""Exact checks: block 19's strong-coupling constant 3 G(0) = (1/2) sum_n P_{2n}(0,0) pinned between 75/100 and 76/100 — the
return-sum identity, the closed-walk counts, the tail bound's inequalities, and the certificate at N = 1000.

Scope.  V1: closed walks of length 2n on Z^3 by enumeration (n <= 3) and the Vandermonde form against the multinomial sum (n <= 12);
the paired geometric series; the cube integrals of phi^{2n} by exact cosine moments (n <= 6) and the vanishing odd integrals.  V2: the
quartic cosine bound and the chord bound (derivative identities and sample points); the Gaussian integral and the tail constant; the
two-region step on the symbol; e^{-x} <= 1 - x + x^2/2 and the integral comparison for sum n^{-3/2}.  V3: S_1000 as one rational; the
rational majorants of the tail; the certificate 3 G(0) < 76/100 and the lower bound 3 G(0) > 75/100.  Exact arithmetic only (integers,
Fractions and sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from math import comb, factorial
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_CUBIC_WALK_RETURN_SUM_AND_SPHERE_STATIC_MAGNETIZATION_SUFFICIENT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
    'docs/ADMISSIBILITY_RULE_SPHERE_STATIC_LAW_ZERO_FIELD_COMPONENT_FOURIER_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md',
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = 'admissibility_rule_cubic_walk_return_sum_and_sphere_static_magnetization_sufficient_bound_bounded_theorem_note_2026-09-15'
PARENT_CLAIM_ID = "possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14"
PARENT_FRAGMENT = "Empty-neighbourhood sphere laws"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "No possibility is privileged.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
)
N_TERMS = 1000

MUTATION_GATE = {
    "walk_count_wrong": "B",
    "vandermonde_wrong": "B",
    "paired_series_wrong": "B",
    "cosine_quartic_wrong": "C",
    "gaussian_integral_wrong": "C",
    "two_region_wrong": "C",
    "exp_bound_wrong": "C",
    "partial_sum_wrong": "D",
    "majorant_wrong": "D",
    "certificate_target_wrong": "D",
    "lower_bound_wrong": "D",
    "claim_true_threshold_injected": "F",
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


def T_n(n: int) -> int:
    return sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n + 1))


def closed_walks(n: int) -> int:
    return comb(2 * n, n) * T_n(n)


def partial_sum(N: int, start: int = 0) -> Fraction:
    num = 0
    for n in range(start, N + 1):
        num += closed_walks(n) * 6 ** (2 * (N - n))
    return Fraction(num, 6 ** (2 * N))


def int_decimal(x: Fraction, digits: int) -> int:
    return (x.numerator * 10 ** digits) // x.denominator


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, parent, infrared_parent = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist, including the corrected component Fourier parent")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the five axiom sentences used are present verbatim in the axiom memo")
    fp = normalize_text(parent)
    checks.check("A3", PARENT_CLAIM_ID in fp and PARENT_FRAGMENT in fp and 'admissibility_rule_sphere_static_law_zero_field_component_fourier_bounds_bounded_theorem_note_2026-09-15' in infrared_parent and "Theorem G5 — component bounds along momentum sequences" in infrared_parent, "the parent's claim id and its empty-neighbourhood sphere-law section are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def family_b(checks: Checks) -> None:
    counts = []
    for n in range(4):
        c = 0
        for seq in product(range(6), repeat=2 * n):
            d = [0, 0, 0]
            for s in seq:
                st = STEPS[s]
                d[0] += st[0]; d[1] += st[1]; d[2] += st[2]
            c += int(d == [0, 0, 0])
        counts.append(c)
    formula = [closed_walks(n) for n in range(4)]
    if mut("walk_count_wrong"):
        formula = [comb(2 * n, n) * sum(comb(n, a) ** 2 * comb(2 * (n - a), n - a) for a in range(n)) for n in range(4)]
    checks.check("B1", counts == formula == [1, 6, 90, 1860], f"V1(iii): closed walks of length 2n on Z^3 by enumeration of all 6^(2n) walks, n <= 3: {counts} = C(2n,n) sum_a C(n,a)^2 C(2(n-a),n-a)")
    ok = True
    for n in range(13):
        multi = sum((factorial(n) // (factorial(a) * factorial(b) * factorial(n - a - b))) ** 2 for a in range(n + 1) for b in range(n - a + 1))
        vand = T_n(n)
        if mut("vandermonde_wrong"):
            vand = sum(comb(n, a) ** 2 * comb(2 * (n - a) + 1, n - a) for a in range(n + 1))
        ok = ok and multi == vand
    checks.check("B2", ok, "V1(iii): sum_{a+b+c=n} (n!/(a!b!c!))^2 = sum_a C(n,a)^2 C(2(n-a), n-a) for n <= 12 (Vandermonde)")
    ph = sp.symbols("phi", real=True)
    target = 1 / (1 - ph)
    if mut("paired_series_wrong"):
        target = 1 / (1 + ph)
    paired = sp.simplify((1 + ph) / (1 - ph ** 2) - target) == 0
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    moments_ok = all(sp.simplify(sp.integrate(sp.cos(k1) ** m, (k1, -sp.pi, sp.pi)) - (2 * sp.pi * sp.Rational(comb(m, m // 2), 2 ** m) if m % 2 == 0 else 0)) == 0 for m in range(7))

    def cube_average(power: int) -> Fraction:
        # (2 pi)^{-3} int phi^power over the cube by exact cosine moments: phi = (c1 + c2 + c3)/3
        total = Fraction(0)
        for a in range(power + 1):
            for b in range(power - a + 1):
                c = power - a - b
                if a % 2 or b % 2 or c % 2:
                    continue
                coef = factorial(power) // (factorial(a) * factorial(b) * factorial(c))
                total += Fraction(coef * comb(a, a // 2) * comb(b, b // 2) * comb(c, c // 2), 2 ** power)
        return total / 3 ** power

    even_ok = all(cube_average(2 * n) == Fraction(closed_walks(n), 6 ** (2 * n)) for n in range(7))
    odd_ok = all(cube_average(2 * n + 1) == 0 for n in range(6))
    checks.check("B3", paired and moments_ok and even_ok and odd_ok, "V1(i)-(ii): (1 + phi)/(1 - phi^2) = 1/(1 - phi); the cosine moments int cos^m = 2 pi C(m, m/2)/2^m (m <= 6, symbolic); (2 pi)^{-3} int_Q phi^{2n} = P_{2n} for n <= 6 and the odd integrals vanish, by exact moments")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    u = sp.symbols("u", real=True)
    g = 1 - u ** 2 / 2 + u ** 4 / 24 - sp.cos(u)
    h = sp.cos(u) - 1 + u ** 2 / 2
    d_ok = sp.simplify(sp.diff(g, u, 2) - h) == 0 and sp.simplify(sp.diff(h, u) - (u - sp.sin(u))) == 0 and g.subs(u, 0) == 0 and sp.diff(g, u).subs(u, 0) == 0
    const = sp.Rational(11, 24)
    if mut("cosine_quartic_wrong"):
        const = sp.Rational(12, 24)
    samples = [sp.Rational(i, 10) for i in range(-10, 11)]
    quart_ok = const == sp.Rational(1, 2) - sp.Rational(1, 24) and all(sp.simplify(1 - sp.cos(x) - const * x ** 2) >= 0 for x in samples)
    chord = all(sp.simplify(1 - sp.cos(x) - 2 * x ** 2 / sp.pi ** 2) >= 0 for x in [sp.Rational(i, 10) * sp.pi for i in range(-10, 11)])
    checks.check("C1", d_ok and quart_ok and chord, "V2(i): g = 1 - u^2/2 + u^4/24 - cos u has g(0) = g'(0) = 0 and g'' = cos u - 1 + u^2/2 =: h with h' = u - sin u; 1 - cos u >= 11 u^2/24 at 21 points of [-1, 1] (11/24 = 1/2 - 1/24); 1 - cos u >= 2u^2/pi^2 at 21 points of [-pi, pi]")
    a, n = sp.symbols("a n", positive=True)
    k = sp.symbols("k", real=True)
    gauss1 = sp.integrate(sp.exp(-a * k ** 2), (k, -sp.oo, sp.oo))
    gauss3 = sp.simplify(gauss1 ** 3 - (sp.pi / a) ** sp.Rational(3, 2)) == 0
    target = (36 * sp.pi / (11 * n)) ** sp.Rational(3, 2)
    if mut("gaussian_integral_wrong"):
        target = (36 * sp.pi / (11 * n)) ** sp.Rational(1, 2) * 3
    g_ok = sp.simplify((sp.pi / (11 * n / 36)) ** sp.Rational(3, 2) - target) == 0
    const_ok = sp.simplify(2 * (2 * sp.pi) ** (-3) * (36 * sp.pi / 11) ** sp.Rational(3, 2) - sp.Rational(36, 11) ** sp.Rational(3, 2) / (4 * sp.pi ** sp.Rational(3, 2))) == 0
    checks.check("C2", gauss3 and g_ok and const_ok, "V2(iv): int_R^3 e^{-a|k|^2} = (pi/a)^{3/2}; at a = 11n/36 this is (36 pi/(11 n))^{3/2}; 2 (2 pi)^{-3} (36 pi/11)^{3/2} = (36/11)^{3/2}/(4 pi^{3/2})")
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (sp.cos(k1) + sp.cos(k2) + sp.cos(k3)) / 3
    shifted = phi.subs({k1: k1 - sp.pi, k2: k2 - sp.pi, k3: k3 - sp.pi})
    shift_target = -phi
    if mut("two_region_wrong"):
        shift_target = phi
    shift_ok = sp.simplify(shifted - shift_target) == 0
    pts_small = [(sp.Rational(1, 2), sp.Rational(1, 3), -sp.Rational(3, 4)), (1, 1, 1), (0, sp.Rational(9, 10), 0), (-1, sp.Rational(1, 5), sp.Rational(1, 2))]
    small_ok = all(sp.simplify((1 - phi.subs({k1: p[0], k2: p[1], k3: p[2]})) - sp.Rational(11, 72) * (p[0] ** 2 + p[1] ** 2 + p[2] ** 2)) >= 0 for p in pts_small)
    pts_large = [(sp.pi, 0, 0), (sp.Rational(3, 2), sp.Rational(1, 2), 0), (2, 2, 2), (sp.pi, sp.pi, sp.pi), (sp.Rational(11, 10), -sp.pi / 2, sp.pi / 3)]
    large_ok = all(sp.simplify((1 - phi.subs({k1: p[0], k2: p[1], k3: p[2]})) - 2 / (3 * sp.pi ** 2)) >= 0 for p in pts_large)
    t = sp.symbols("t", positive=True)
    minmax = sp.simplify(sp.exp(-sp.Min(t, 2 * t)) - sp.exp(-t)) == 0
    checks.check("C3", shift_ok and small_ok and large_ok and minmax, "V2(ii)-(iii): phi(k - (pi,pi,pi)) = -phi(k), so 1 + phi(k) = 1 - phi(k - pi); 1 - phi >= (11/72)|k|^2 at four wavevectors with |k|_inf <= 1 and >= 2/(3 pi^2) at five with |k|_inf > 1; e^{-min(a,b)} <= e^{-a} + e^{-b}")
    x = sp.symbols("x", positive=True)
    q = 1 - x + x ** 2 / 2 - sp.exp(-x)
    e_ok = q.subs(x, 0) == 0 and sp.simplify(sp.diff(q, x) - (-1 + x + sp.exp(-x))) == 0 and sp.simplify(sp.diff(q, x, 2) - (1 - sp.exp(-x))) == 0
    val = sp.Rational(197, 225)
    if mut("exp_bound_wrong"):
        val = sp.Rational(196, 225)
    val_ok = (1 - sp.Rational(2, 15) + sp.Rational(2, 225)) == val
    tt = sp.symbols("tt", positive=True)
    cmp_ok = sp.simplify(sp.diff(-2 / sp.sqrt(tt), tt) - tt ** sp.Rational(-3, 2)) == 0 and sp.simplify(sp.diff(tt ** sp.Rational(-3, 2), tt) + sp.Rational(3, 2) * tt ** sp.Rational(-5, 2)) == 0
    checks.check("C4", e_ok and val_ok and cmp_ok, "V3: 1 - x + x^2/2 - e^{-x} vanishes at 0 with derivative -1 + x + e^{-x} (itself vanishing at 0 with derivative 1 - e^{-x} >= 0), so e^{-2/15} <= 1 - 2/15 + 2/225 = 197/225; d/dt(-2 t^{-1/2}) = t^{-3/2} and t^{-3/2} is decreasing, so sum_{n>N} n^{-3/2} <= 2/sqrt N")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    N = N_TERMS
    S = partial_sum(N)
    if mut("partial_sum_wrong"):
        S = partial_sum(N, start=1)
    d6 = int_decimal(S, 6)
    checks.check("D1", d6 == 1501637 and len(str(S.denominator)) == 1553, f"V3: S_1000 = sum_{{n<=1000}} P_2n as one rational (denominator {len(str(S.denominator))} digits); floor(10^6 S) = {d6}")
    ratio = sp.Rational(36, 11)
    denom = 108
    if mut("majorant_wrong"):
        denom = 54
    t1_ok = sp.simplify((ratio ** sp.Rational(3, 2) / (2 * 3 ** sp.Rational(3, 2) * sp.sqrt(sp.Symbol("N", positive=True)))) ** 2 - ratio ** 3 / (denom * sp.Symbol("N", positive=True))) == 0
    r = Fraction(197, 225)
    t2_ok = 2 * r ** 3 / (1 - r) == Fraction(225, 14) * r ** 3
    T1sq = Fraction(36, 11) ** 3 / (denom * N)
    T2 = Fraction(225, 14) * r ** (N + 1)
    checks.check("D2", t1_ok and t2_ok and int_decimal(T1sq, 12) == 324567993 and T1sq < Fraction(181, 10 ** 4) ** 2 and T2 < Fraction(1, 10 ** 50), f"V3: T_1(N)^2 = (36/11)^3/(108 N) with pi >= 3 (floor(10^12 T_1^2) = {int_decimal(T1sq, 12)}, so T_1 < 181/10^4 at N = 1000); T_2(N) = (225/14)(197/225)^(N+1) < 10^-50")
    S_true = partial_sum(N)
    target = Fraction(76, 100)
    if mut("certificate_target_wrong"):
        target = Fraction(75, 100)
    X = 2 * target - S_true - T2
    cert = X > 0 and X * X > Fraction(36, 11) ** 3 / (108 * N)
    checks.check("D3", cert, f"V3: X = 2 (76/100) - S_N - T_2 = {int_decimal(X, 6) if X > 0 else 'negative'} x 10^-6 > 0 and X^2 > (36/11)^3/(108 N): hence 3 G(0) <= (S_N + T_1 + T_2)/2 < 76/100")
    lower = Fraction(150, 100)
    if mut("lower_bound_wrong"):
        lower = Fraction(152, 100)
    checks.check("D4", S_true > lower and partial_sum(250) < partial_sum(500) < S_true and int_decimal(partial_sum(250), 6) == 1486921,
                 f"V3: S_N > 150/100, so 3 G(0) >= S_N/2 > 75/100; the partial sums increase (floor(10^6 S_250) = {int_decimal(partial_sum(250), 6)})")


# ============================================================================================ family F
FENCES = ('V1–V3 prove the exact cubic-walk identity and scalar interval 75/100 < 3G(0) < 76/100 with the unchanged N=1000 rational certificate. Conditional on the corrected zero-field sphere static parent and its explicit mathematical imports, beta>76/100 gives M²>=1−3G(0)/beta>0 and the corresponding component Fourier bounds. This is a sufficient model condition, not a true transition threshold, physical kernel window or exclusion of other proof routes. No physical rule is selected and no clause is adopted.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'All mathematical imports are explicit; no physical selection follows from the scalar interval.')
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the true threshold is",
)
CLAIM_INJECTIONS = {"claim_true_threshold_injected": "Hence the true threshold is 76/100."}
CLASSICAL_NAMES = ("Watson", "Glasser", "Zucker", "Mermin", "Wagner", "Fröhlich", "Simon", "Spencer", "Dobrushin", "Peierls", "Toom", "Jordan", "Wallis")  # authors; Vandermonde, Gaussian, Green function name standard objects
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
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem V1"):
            body = body + " (Watson's integral)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports and the Premises; Vandermonde, Gaussian and Green function name standard objects ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the closed-walk counts 1, 6, 90, 1860 by enumeration; the Vandermonde form to n = 12; the cosine derivative identities",
    "per_site: executed — the two-region step on the symbol at nine wavevectors; the shift identity phi(k - pi) = -phi(k)",
    "per_mode: executed — the exact cosine moments and the cube integrals of phi^{2n} for n <= 6; the Gaussian integral and the tail constant; the integral comparison for sum n^{-3/2}",
    "per_block: executed — S_1000 as one rational; the majorants T_1^2 = (36/11)^3/(108 N) and T_2 = (225/14)(197/225)^(N+1); the two rational comparisons",
    "lattice_wide: checked and not executed — V1-V3 infinite-series proof and V4 conditional parent implication; finite checks do not execute an infinite lattice or physical classification",
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
    print("scope: block 19's constant 3 G(0) as half the return sum of the cubic walk — closed-walk counts, the paired series, the tail bound's inequalities, S_1000 exactly, the certificate 75/100 < 3 G(0) < 76/100; exact")
    print(f"mutation: {ACTIVE_MUTATION or 'none'}")
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
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
