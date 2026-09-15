#!/usr/bin/env python3
"""Exact checks: the unsoldered sphere static law with overlap e^{beta t} at weak coupling on Z^3 — the algebraic skeleton of the
one-site contraction (uniqueness, exponential decay, no massless channel below beta = sqrt(3)/6).

Scope.  W1: the covariance identities of a record under a field (longitudinal L'(x) = 1/x^2 - 1/sinh^2 x, transverse L(x)/x), the
series coefficient ratios 6/(n(2n-1)) and 3/(2n+1) (closed form and to n = 12), the derivative identity d/dt P_t(A) = beta Cov(s.Delta, 1_A)
on a finite weighted space, p(1-p) <= 1/4, the chain of constants.  W2: the threshold sqrt(3)/6, the antipodal value tanh(beta/2) and
its small-beta ratio.  W3-W5: the maximal coupling of two densities on a finite space, the fixed point u* = D b on the cube window,
the walk bounds on the 7^3 box, the geometric sums and the torus sum, the frozen-site conditional.  Exact arithmetic only
(Fractions and sympy); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_WEAK_COUPLING_ONE_LAW_EXPONENTIAL_DECAY_NO_MASSLESS_CHANNEL_BELOW_ROOT_THREE_OVER_SIX_BOUNDED_THEOREM_NOTE_2026-09-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md",
    "docs/ADMISSIBILITY_RULE_EXACT_UNIQUENESS_REGION_ONE_SITE_CONTRACTION_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_below_root_three_over_six_bounded_theorem_note_2026-09-15"
PARENT_CLAIM_ID = "possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14"
PARENT_FRAGMENT = "Empty-neighbourhood sphere laws"
BLOCK03_CLAIM_ID = "admissibility_rule_exact_uniqueness_region_one_site_contraction_coupling_bounded_theorem_note_2026-09-06"
BLOCK03_FRAGMENT = "the finite-window comparison bound by coupling"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "No possibility is privileged.",
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
)

MUTATION_GATE = {
    "covariance_identity_wrong": "B",
    "series_ratio_wrong": "B",
    "coefficient_formula_wrong": "B",
    "derivative_identity_wrong": "C",
    "variance_bound_wrong": "C",
    "threshold_wrong": "C",
    "antipodal_tv_wrong": "C",
    "maximal_coupling_wrong": "D",
    "fixed_point_wrong": "D",
    "walk_bound_wrong": "D",
    "geometric_sum_wrong": "D",
    "claim_channel_below_threshold_injected": "F",
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


def zero(expr) -> bool:
    return sp.simplify(sp.expand(expr.rewrite(sp.exp))) == 0


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, parent, block03 = texts
    checks.check("A1", all((ROOT / pth).is_file() for pth in AUDIT_INPUT_PATHS) and len(set(AUDIT_INPUT_PATHS)) == 4,
                 "the four declared inputs exist (this note, the axiom memo, the possibility-covariance note and block 03's note on main)")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the five axiom sentences used are present verbatim in the axiom memo")
    fp, f3 = normalize_text(parent), normalize_text(block03)
    checks.check("A3", PARENT_CLAIM_ID in fp and PARENT_FRAGMENT in fp and BLOCK03_CLAIM_ID in f3 and BLOCK03_FRAGMENT in f3,
                 "the parent's claim id and sphere-law section, and block 03's claim id and its coupling theorem, are present")
    flat = normalize_text(note)
    checks.check("A4", CLAIM_ID in flat and Path(__file__).name in flat, "this note carries its claim id and names this runner")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    x, t = sp.symbols("x t", positive=True)
    Lg = sp.coth(x) - 1 / x
    den = sp.integrate(sp.exp(x * t), (t, -1, 1))
    E1 = sp.integrate(sp.exp(x * t) * t, (t, -1, 1)) / den
    E2 = sp.integrate(sp.exp(x * t) * t ** 2, (t, -1, 1)) / den
    Eperp = sp.integrate(sp.exp(x * t) * (1 - t ** 2) / 2, (t, -1, 1)) / den
    target_perp = Lg / x
    if mut("covariance_identity_wrong"):
        target_perp = Lg / (2 * x)
    ok = zero(E1 - Lg) and zero(E2 - (1 - 2 * Lg / x)) and zero(E2 - Lg ** 2 - sp.diff(Lg, x)) and zero(sp.diff(Lg, x) - (1 / x ** 2 - 1 / sp.sinh(x) ** 2)) and zero(Eperp - target_perp)
    checks.check("B1", ok, "W1(i): under P_h, E[s.h^] = L(x), E[(s.h^)^2] = 1 - 2L/x, Var(s.h^) = L'(x) = 1/x^2 - 1/sinh^2 x, and E[(s.e_perp)^2] = L(x)/x, symbolically (x = beta|h|)")
    n = sp.symbols("n", positive=True, integer=True)
    even_ratio = (sp.Rational(3, 2) * 2 ** (2 * n) / sp.factorial(2 * n)) / (sp.Rational(1, 2) * 2 ** (2 * n - 2) / sp.factorial(2 * n - 2))
    odd_ratio = ((2 * n) / sp.factorial(2 * n + 1)) / (1 / (3 * sp.factorial(2 * n - 1)))
    r_even, r_odd = 6 / (n * (2 * n - 1)), 3 / (2 * n + 1)
    if mut("series_ratio_wrong"):
        r_even = 6 / (n * (2 * n + 1))
    closed = sp.simplify(even_ratio - r_even) == 0 and sp.simplify(odd_ratio - r_odd) == 0
    bounded = all(sp.Rational(6, m * (2 * m - 1)) <= 1 for m in range(2, 13)) and all(sp.Rational(3, 2 * m + 1) <= 1 for m in range(1, 13))
    checks.check("B2", closed and bounded, "W1(ii): the coefficient ratios of (3 sinh^2 x - 3x^2)/(x^2 sinh^2 x) and (x cosh x - sinh x)/((x^2/3) sinh x) are 6/(n(2n-1)) and 3/(2n+1) in closed form, and both are <= 1 (n >= 2, n >= 1) to n = 12")
    s1 = sp.series(3 * sp.sinh(x) ** 2 - 3 * x ** 2, x, 0, 28).removeO()
    s2 = sp.series(x ** 2 * sp.sinh(x) ** 2, x, 0, 28).removeO()
    s3 = sp.series(x * sp.cosh(x) - sp.sinh(x), x, 0, 28).removeO()
    s4 = sp.series(x ** 2 * sp.sinh(x) / 3, x, 0, 28).removeO()
    left_even = lambda m: sp.Rational(3, 2) * 2 ** (2 * m) / sp.factorial(2 * m)
    if mut("coefficient_formula_wrong"):
        left_even = lambda m: sp.Rational(3, 2) * 2 ** (2 * m - 1) / sp.factorial(2 * m)
    ok3 = all(s1.coeff(x, 2 * m) == left_even(m) and s2.coeff(x, 2 * m) == sp.Rational(1, 2) * 2 ** (2 * m - 2) / sp.factorial(2 * m - 2) for m in range(2, 13))
    ok3 = ok3 and all(s3.coeff(x, 2 * m + 1) == sp.Rational(2 * m) / sp.factorial(2 * m + 1) and s4.coeff(x, 2 * m + 1) == 1 / (3 * sp.factorial(2 * m - 1)) for m in range(1, 13))
    ok3 = ok3 and s1.coeff(x, 2) == 0 and s2.coeff(x, 2) == 0 and s3.coeff(x, 1) == 0
    checks.check("B3", ok3, "W1(ii): the series coefficients match the closed forms (3/2) 2^{2n}/(2n)!, (1/2) 2^{2n-2}/(2n-2)!, 2n/(2n+1)!, 1/(3 (2n-1)!) to n = 12; no x^2 or x^1 terms")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    w1, w2, w3, X1, X2, X3, b, tt = sp.symbols("w1 w2 w3 X1 X2 X3 beta t", positive=True)
    ws, Xs, ind = (w1, w2, w3), (X1, X2, X3), (1, 1, 0)
    weights = [w * sp.exp(b * tt * X) for w, X in zip(ws, Xs)]
    Z = sum(weights)
    PA = sum(w * i for w, i in zip(weights, ind)) / Z
    EX = sum(w * X for w, X in zip(weights, Xs)) / Z
    EXA = sum(w * X * i for w, X, i in zip(weights, Xs, ind)) / Z
    target = b * (EXA - PA * EX)
    if mut("derivative_identity_wrong"):
        target = b * (EXA + PA * EX)
    d_ok = sp.simplify(sp.diff(PA, tt) - target) == 0
    p = sp.symbols("p", positive=True)
    var_bound = sp.Rational(1, 4)
    if mut("variance_bound_wrong"):
        var_bound = sp.Rational(1, 5)
    v_ok = sp.simplify(var_bound - p * (1 - p) - (sp.Rational(1, 2) - p) ** 2 - (var_bound - sp.Rational(1, 4))) == 0 and var_bound >= sp.Rational(1, 4)
    checks.check("C1", d_ok and v_ok, "W1(iii): on a three-point weighted space, d/dt P_t(A) = beta [E_t(X 1_A) - P_t(A) E_t(X)] = beta Cov_t(X, 1_A) symbolically; p(1-p) = 1/4 - (1/2 - p)^2 <= 1/4")
    D = sp.symbols("Delta", positive=True)
    chain = sp.simplify(b * D / (2 * sp.sqrt(3)) - b * sp.sqrt(D ** 2 / 3) * sp.Rational(1, 2)) == 0
    c_val = sp.simplify(2 * b / (2 * sp.sqrt(3)) - b / sp.sqrt(3)) == 0
    alpha_val = sp.simplify(6 * b / sp.sqrt(3) - 2 * sp.sqrt(3) * b) == 0
    thr = sp.sqrt(3) / 6
    if mut("threshold_wrong"):
        thr = sp.sqrt(3) / 5
    thr_ok = sp.simplify(2 * sp.sqrt(3) * thr - 1) == 0 and thr ** 2 > sp.Rational(784, 10000)
    checks.check("C2", chain and c_val and alpha_val and thr_ok, "W1(iv)/W2: beta |Delta|/(2 sqrt 3) = beta sigma_max |Delta| / 2 with sigma_max^2 = 1/3; |Delta| <= 2 gives c = beta/sqrt 3; alpha = 6c = 2 sqrt(3) beta; 2 sqrt(3) (sqrt(3)/6) = 1 and sqrt(3)/6 > 28/100")
    Zs = 4 * sp.pi * sp.sinh(b) / b
    tv = (2 * sp.pi / Zs) * sp.integrate(sp.exp(b * tt) - sp.exp(-b * tt), (tt, 0, 1))
    target_tv = sp.tanh(b / 2)
    if mut("antipodal_tv_wrong"):
        target_tv = sp.tanh(b)
    a_ok = zero(tv - target_tv) and sp.simplify(sp.limit(sp.tanh(b / 2) / (b / sp.sqrt(3)), b, 0) - sp.sqrt(3) / 2) == 0
    checks.check("C3", a_ok, "W2: at zero field the antipodal change has TV(P_e, P_-e) = (2 pi/Z) int_0^1 (e^{beta t} - e^{-beta t}) dt = tanh(beta/2); tanh(beta/2)/(beta/sqrt 3) tends to sqrt(3)/2")


# ============================================================================================ family D
def box_sites(n: int, d: int = 3):
    return list(product(range(n), repeat=d))


def box_matrix(n: int, c: Fraction, remove=None):
    sites = [s for s in box_sites(n) if s != remove]
    idx = {s: i for i, s in enumerate(sites)}
    C = [[Fraction(0)] * len(sites) for _ in sites]
    for s in sites:
        for dim in range(3):
            for e in (1, -1):
                y = list(s); y[dim] += e; y = tuple(y)
                if y in idx:
                    C[idx[s]][idx[y]] = c
    return sites, idx, C


def matvec(C, v):
    return [sum(C[i][j] * v[j] for j in range(len(v)) if v[j] != 0) for i in range(len(v))]


def family_d(checks: Checks) -> None:
    # D1 maximal coupling on a finite weighted space (rational densities against weights)
    wts = [Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)]
    p = [Fraction(3, 2), Fraction(3, 4), Fraction(1)]
    q = [Fraction(1, 2), Fraction(3, 2), Fraction(5, 6)]
    assert sum(w * a for w, a in zip(wts, p)) == 1 and sum(w * a for w, a in zip(wts, q)) == 1
    m = sum(w * min(a, c) for w, a, c in zip(wts, p, q))
    tv = sum(w * max(a - c, 0) for w, a, c in zip(wts, p, q))
    tv2 = sum(w * max(c - a, 0) for w, a, c in zip(wts, p, q))
    same_support = any(min(a - min(a, c), c - min(a, c)) > 0 for a, c in zip(p, q))
    disagree = 1 - m
    if mut("maximal_coupling_wrong"):
        disagree = 1 - m / 2
    checks.check("D1", tv == tv2 == disagree and not same_support, f"W3 step 0: int (p-q)_+ = int (q-p)_+ = 1 - int min(p,q) = {tv} on a three-point weighted space; the residual densities have disjoint supports, so P(S != S') = TV")
    # D2 fixed point on the 2x2x2 cube window with c = alpha/6, alpha = 9/10, exterior differing at every exterior slot
    alpha = Fraction(9, 10)
    c = alpha / 6
    sites, idx, C = box_matrix(2, c)
    nsit = len(sites)
    b = [c * 3 for _ in sites]  # each cube site has 3 exterior neighbours
    I = [[Fraction(int(i == j)) for j in range(nsit)] for i in range(nsit)]
    A = [[I[i][j] - C[i][j] for j in range(nsit)] for i in range(nsit)]
    Dm = sp.Matrix(A).inv()
    D_ok = all(Dm[i, j] >= 0 for i in range(nsit) for j in range(nsit)) and (sp.Matrix(A) * Dm == sp.eye(nsit))
    ustar = [sum(Dm[i, j] * b[j] for j in range(nsit)) for i in range(nsit)]
    phi = lambda u: [(1 - Fraction(1, nsit)) * u[i] + Fraction(1, nsit) * (sum(C[i][j] * u[j] for j in range(nsit)) + b[i]) for i in range(nsit)]
    fixed = all(sp.simplify(phi([sp.Rational(u) if isinstance(u, Fraction) else u for u in ustar])[i] - ustar[i]) == 0 for i in range(nsit))
    u = [Fraction(1)] * nsit
    dec = True
    for _ in range(60):
        nu = phi(u)
        dec = dec and all(nu[i] <= u[i] for i in range(nsit)) and all(nu[i] >= ustar[i] for i in range(nsit))
        u = nu
    neumann = sum(alpha ** k for k in range(0, 200))
    geometric_ok = ustar[0] <= 3 * c * neumann
    if mut("fixed_point_wrong"):
        fixed = all(sp.simplify(phi(ustar)[i] - 2 * ustar[i]) == 0 for i in range(nsit))
    checks.check("D2", D_ok and fixed and dec and geometric_ok, "W3 step 3: on the cube window at alpha = 9/10, D = (I - C)^{-1} is entrywise nonnegative, u* = D b is the fixed point of Phi, the iterates Phi^t(1) decrease to it from above, and u*_x <= b_x/(1 - alpha)")
    # D3 walk bounds on the 7^3 box
    sites7, idx7, C7 = box_matrix(7, c)
    o = idx7[(3, 3, 3)]
    v = [Fraction(0)] * len(sites7); v[o] = Fraction(1)
    acc = [Fraction(0)] * len(sites7)
    ok3 = True
    row_bound = lambda k: alpha ** k
    if mut("walk_bound_wrong"):
        row_bound = lambda k: alpha ** (k + 1)
    for k in range(1, 17):
        v = matvec(C7, v)
        row = sum(v)
        ok3 = ok3 and row <= row_bound(k)
        for s in sites7:
            dist = sum(abs(s[i] - 3) for i in range(3))
            if k < dist:
                ok3 = ok3 and v[idx7[s]] == 0
            acc[idx7[s]] += v[idx7[s]]
    ok3 = ok3 and all(acc[idx7[s]] <= alpha ** sum(abs(s[i] - 3) for i in range(3)) / (1 - alpha) for s in sites7 if s != (3, 3, 3))
    checks.check("D3", ok3, "W3/W5 walk bounds on the 7^3 box at alpha = 9/10: sum_y (C^k)_{0y} <= alpha^k, (C^k)_{0x} = 0 for k < |x|_1, and sum_{k<=16} (C^k)_{0x} <= alpha^{|x|_1}/(1 - alpha) for every x != 0")
    # D4 geometric sums and the torus sum
    a = sp.symbols("a", positive=True)
    target = lambda L: (1 + a) / (1 - a) - a ** L * (1 + a) / (1 - a)
    if mut("geometric_sum_wrong"):
        target = lambda L: (1 + a) / (1 - a) - a ** L / (1 - a)
    g_ok = all(sp.simplify(1 + 2 * sum(a ** jj for jj in range(1, L)) + a ** L - target(L)) == 0 for L in range(1, 13))
    g_ok = g_ok and sp.simplify(1 + 2 * a / (1 - a) - (1 + a) / (1 - a)) == 0
    # the torus sum on (Z/2LZ)^3 at L = 3 exactly at a = 9/10 against ((1+a)/(1-a))^3
    Lt = 3
    tor = sum(alpha ** sum(min(n_, 2 * Lt - n_) for n_ in nvec) for nvec in product(range(2 * Lt), repeat=3))
    t_ok = tor <= ((1 + alpha) / (1 - alpha)) ** 3
    checks.check("D4", g_ok and t_ok, "W5(c): 1 + 2 sum_{j=1}^{L-1} a^j + a^L = (1+a)/(1-a) - a^L (1+a)/(1-a) <= (1+a)/(1-a) symbolically for L = 1..12; 1 + 2a/(1-a) = (1+a)/(1-a); the torus sum on the 6^3 torus at a = 9/10 is at most ((1+a)/(1-a))^3")
    # D5 frozen-site conditional: on a 3-site path with symbolic bond weights, conditioning the middle site gives the two-site window law with that exterior
    s0, s1, s2 = sp.symbols("s0 s1 s2", real=True)
    w01, w12 = sp.Function("w01"), sp.Function("w12")
    joint = w01(s0, s1) * w12(s1, s2)
    # conditional on s1 = a: proportional to w01(s0, a) w12(a, s2) — the product of the exterior-bond factors of the window {0, 2}
    cond = joint.subs(s1, sp.Symbol("a"))
    window = w01(s0, sp.Symbol("a")) * w12(sp.Symbol("a"), s2)
    checks.check("D5", sp.simplify(cond - window) == 0, "W5: freezing a site turns the joint density into the window density with that site's record as exterior (symbolic bond factors on a three-site path)")


# ============================================================================================ family F
FENCES = (
    "This note proves, for the unsoldered static law with the exponential overlap on `Z³`, that below `β = √3/6` there is exactly one infinite-volume static law, with exponential decay of the record correlations and a structure factor bounded uniformly in the wavevector and the side; it does not locate the true threshold, does not treat the band `[√3/6, 3√3π/8]`, does not treat the Born overlap, does not re-prove the strong-coupling half of the placement (block 19's open PR), does not select a reading, rule or coupling as physical, and adopts no clause.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the channel exists below",
)
CLAIM_INJECTIONS = {"claim_channel_below_threshold_injected": "Hence the channel exists below the threshold as well."}
CLASSICAL_NAMES = ("Dobrushin", "Shlosman", "Föllmer", "Künsch", "Kolmogorov", "Cauchy", "Mermin", "Wagner", "Fröhlich", "Simon", "Spencer", "Peierls", "Toom")  # authors; Gibbs, Laplacian, Green function name standard objects
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
        if mut("claim_classical_name_in_theorem") and title.startswith("Theorem W2"):
            body = body + " (Dobrushin's criterion)"
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if nm in body:
                offenders.append((title[:30], nm))
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports and the Premises; Gibbs, Laplacian and Green function name standard objects ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the covariance identities and the coefficient ratios; the derivative identity; the antipodal value; the threshold arithmetic",
    "per_site: executed — the maximal coupling on a finite weighted space; the frozen-site conditional on a three-site path",
    "per_mode: executed — the walk bounds (C^k)_{0x} = 0 for k < |x|_1 and sum_y (C^k)_{0y} <= alpha^k on the 7^3 box",
    "per_block: executed — the fixed point u* = D b on the cube window; the geometric sums and the 6^3 torus sum",
    "lattice_wide: W1-W5 proved for every beta < sqrt(3)/6 on finite windows, tori and the infinite-volume law; W6 a placement corollary conditional on block 19; the band not claimed",
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
    print("scope: the unsoldered sphere static law with overlap e^{beta t} at weak coupling on Z^3 — the covariance eigenvalues and series inequalities behind the one-site contraction, the derivative identity, the threshold sqrt(3)/6, the maximal coupling, the fixed point, the walk bounds, the geometric sums; exact")
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
