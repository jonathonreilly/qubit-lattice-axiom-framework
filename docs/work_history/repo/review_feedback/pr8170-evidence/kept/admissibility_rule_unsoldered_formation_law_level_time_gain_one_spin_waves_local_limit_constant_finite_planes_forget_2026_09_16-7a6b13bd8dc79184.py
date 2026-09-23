#!/usr/bin/env python3
"""Exact checks: the unsoldered formation law in level time — gain-one spin waves, the local-limit constant of the level walk,
finite planes forget, and the exponent of the linearized field.

Scope.  T1: the sphere kernel's moments E[w] = A(kappa) = coth kappa - 1/kappa and E[w^2] = 1 - 2A/kappa (symbolic), the bound
A(kappa) < kappa/3 through sinh^2 kappa >= kappa^2 + kappa^4/3, the one-step magnetization A(3 beta) from the aligned plane with exact
rational enclosures.  T2: the second-order expansion of beta s.(s_1 + s_2 + s_3) in transverse coordinates has the average as its
minimizer (gain one) and the exact one-step transverse variance A(3 beta)/(3 beta) per component.  T3: the trinomial path identity,
the return sums P_k exactly for k <= 150 against the two-sided bounds with the constant 3 sqrt3/(4 pi) (rational enclosures of sqrt3,
pi and the exponentials), the Gaussian integrals of the proof, and sum_{k<=t} P_k >= (3 sqrt3/(4 pi)) H_t - 3.  T4: the one-site chain
m_t = A(3 beta)^t and the minorization 2 kappa/(e^{2 kappa} - 1) of the kernel's density.  T5: the exponent gamma(beta) with exact
enclosures at beta = 3, 6, 12, 24.  The six-axis side-by-side deviations at weights (e^beta, e^-beta, 1) in closed form.  Exact arithmetic
only (integers, Fractions, sympy); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from math import factorial, isqrt
from pathlib import Path

import sympy as sp

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_unsoldered_formation_law_in_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_and_the_simulated_algebraic_decay_of_the_initial_plane_memory_bounded_theorem_note_2026-09-16"
BLOCK01_CLAIM_ID = "admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06"
BLOCK01_FRAGMENT = "the static law of a product rule"
AXIOM_NEEDLES = (
    "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.",
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "Records form.",
    "Only records are readable.",
)

MUTATION_GATE = {
    "kernel_mean_wrong": "B",
    "second_moment_wrong": "B",
    "langevin_bound_wrong": "B",
    "gain_wrong": "C",
    "path_identity_wrong": "D",
    "return_constant_wrong": "D",
    "return_lower_bound_wrong": "D",
    "harmonic_bound_wrong": "D",
    "one_site_chain_wrong": "E",
    "minorization_wrong": "E",
    "exponent_wrong": "E",
    "sixaxis_deviation_wrong": "E",
    "claim_order_injected": "F",
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
    """Rational lower and upper bounds of e^x for rational x >= 0 from the series with a geometric tail bound."""
    assert x >= 0
    n = terms if terms is not None else 2 * (int(x) + 1) + 40
    lo = Fraction(0)
    term = Fraction(1)
    for k in range(n + 1):
        lo += term
        term = term * x / (k + 1)
    # the tail sum_{k>n} x^k/k! <= term * 1/(1 - x/(n+2)), term = x^{n+1}/(n+1)!
    assert x < n + 2
    hi = lo + term / (1 - x / (n + 2))
    return lo, hi


def exp_neg_upper(x: Fraction) -> Fraction:
    """e^{-x} <= 1/(1 + x + x^2/2 + x^3/6 + x^4/24) for x >= 0."""
    return 1 / (1 + x + x ** 2 / 2 + x ** 3 / 6 + x ** 4 / 24)


def A_bounds(kappa: Fraction) -> tuple[Fraction, Fraction]:
    """Rational enclosure of A(kappa) = coth kappa - 1/kappa: coth kappa = (E + 1)/(E - 1), E = e^{2 kappa}, decreasing in E."""
    e_lo, e_hi = exp_bounds(2 * kappa)
    return (e_hi + 1) / (e_hi - 1) - 1 / kappa, (e_lo + 1) / (e_lo - 1) - 1 / kappa


def pi_bounds() -> tuple[Fraction, Fraction]:
    """Machin: pi = 16 arctan(1/5) - 4 arctan(1/239); alternating series with decreasing terms bracket each arctan."""
    def arctan_partial(x: Fraction, n: int) -> Fraction:
        return sum((Fraction((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1) for k in range(n)), Fraction(0))
    a5_lo, a5_hi = arctan_partial(Fraction(1, 5), 14), arctan_partial(Fraction(1, 5), 13)   # 14 terms ends with a negative term
    a239_lo, a239_hi = arctan_partial(Fraction(1, 239), 4), arctan_partial(Fraction(1, 239), 3)
    return 16 * a5_lo - 4 * a239_hi, 16 * a5_hi - 4 * a239_lo


def sqrt_bounds(n: int, digits: int = 9) -> tuple[Fraction, Fraction]:
    scale = 10 ** digits
    r = isqrt(n * scale * scale)
    lo = Fraction(r, scale)
    hi = Fraction(r + 1, scale)
    assert lo * lo < n < hi * hi
    return lo, hi


PI_LO, PI_HI = pi_bounds()
S3_LO, S3_HI = sqrt_bounds(3)
C0_LO, C0_HI = 3 * S3_LO / (4 * PI_HI), 3 * S3_HI / (4 * PI_LO)   # 3 sqrt3/(4 pi)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, block01 = texts
    checks.check("A1", CLAIM_ID in note and len(re.findall(r"^claim_id:", note, flags=re.M)) == 1, "the note carries its claim_id once")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "the axioms memo carries the four sentences quoted under Premises")
    checks.check("A3", BLOCK01_CLAIM_ID in block01 and BLOCK01_FRAGMENT in block01.lower(), "block 01's note (on main) carries its claim_id and the rule's product form")
    checks.check("A4", all(Path(ROOT, p).exists() for p in AUDIT_INPUT_PATHS), "all declared inputs exist")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    k, w = sp.symbols("kappa w", positive=True)
    Z = sp.integrate(sp.exp(k * w), (w, -1, 1))
    Ew = sp.integrate(w * sp.exp(k * w), (w, -1, 1)) / Z
    Ew2 = sp.integrate(w ** 2 * sp.exp(k * w), (w, -1, 1)) / Z
    A = sp.coth(k) - 1 / k
    if mut("kernel_mean_wrong"):
        A = sp.coth(k) + 1 / k
    second = 1 - 2 * A / k
    if mut("second_moment_wrong"):
        second = 1 - A / k
    ok1 = sp.simplify((Ew - A).rewrite(sp.exp)) == 0 and sp.simplify((Ew2 - second).rewrite(sp.exp)) == 0
    # normalizer of the density with respect to the uniform probability measure on the sphere: sinh(kappa)/kappa
    norm = sp.simplify((Z / 2 - sp.sinh(k) / k).rewrite(sp.exp)) == 0
    checks.check("B1", ok1 and norm, "T1: for the sphere kernel with concentration kappa, E[w] = coth kappa - 1/kappa =: A(kappa) and E[w^2] = 1 - 2A/kappa (w the cosine to the mean direction), so E[s|S] = A u and E[s s^T|S] = (A/kappa) I + (1 - 3A/kappa) u u^T; the density against the uniform law on the sphere is (kappa/sinh kappa) e^{kappa s.u}")
    # A(kappa) < kappa/3: A' = 1/kappa^2 - 1/sinh^2 kappa <= 1/(3 + kappa^2) because sinh^2 kappa >= kappa^2 + kappa^4/3 (all series terms positive)
    Aprime = sp.simplify(sp.diff(sp.coth(k) - 1 / k, k) - (1 / k ** 2 - 1 / sp.sinh(k) ** 2)) == 0
    ser = sp.series(sp.sinh(k) ** 2, k, 0, 14).removeO()
    coeffs = [ser.coeff(k, 2 * n) for n in range(1, 7)]
    series_ok = coeffs[0] == 1 and coeffs[1] == sp.Rational(1, 3) and all(c > 0 for c in coeffs) and all(sp.simplify(c - sp.Rational(2 ** (2 * n - 1), factorial(2 * n))) == 0 for n, c in zip(range(1, 7), coeffs))
    ident = sp.simplify(1 / k ** 2 - 1 / (k ** 2 + k ** 4 / 3) - 1 / (3 + k ** 2)) == 0
    slope = Fraction(1, 3)
    if mut("langevin_bound_wrong"):
        slope = Fraction(1, 4)
    pts = [Fraction(1, 10), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(6), Fraction(9), Fraction(18), Fraction(36), Fraction(72)]
    below = all(A_bounds(kp)[1] < slope * kp for kp in pts)
    checks.check("B2", Aprime and series_ok and ident and below, "T1: A'(kappa) = 1/kappa^2 - 1/sinh^2 kappa; sinh^2 kappa = sum_{n>=1} 2^{2n-1} kappa^{2n}/(2n)! has the terms kappa^2 + kappa^4/3 + positive, so A'(kappa) <= 1/(3 + kappa^2) and A(kappa) < kappa/3; exact enclosures confirm A(kappa) < kappa/3 at ten rational points from 1/10 to 72")
    encl = {b: A_bounds(Fraction(3 * b)) for b in (3, 6, 12, 24)}
    digits = {3: (Fraction(8888, 10 ** 4), Fraction(8889, 10 ** 4)), 6: (Fraction(9444, 10 ** 4), Fraction(9445, 10 ** 4)), 12: (Fraction(9722, 10 ** 4), Fraction(9723, 10 ** 4)), 24: (Fraction(9861, 10 ** 4), Fraction(9862, 10 ** 4))}
    ok3 = all(digits[b][0] <= encl[b][0] and encl[b][1] <= digits[b][1] for b in encl)
    checks.check("B3", ok3, "T1: the one-step magnetization from the aligned plane is A(3 beta): in [8888, 8889]/10^4 at beta = 3, [9444, 9445]/10^4 at 6, [9722, 9723]/10^4 at 12, [9861, 9862]/10^4 at 24 (exact enclosures); the one-step transverse second moment is 2A(3 beta)/(3 beta)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    beta, eps = sp.symbols("beta epsilon", positive=True)
    th = sp.symbols("t1 t2", real=True)
    ths = [sp.symbols(f"a{i}1 a{i}2", real=True) for i in range(3)]

    def unit(v):
        return sp.Matrix([eps * v[0], eps * v[1], sp.sqrt(1 - eps ** 2 * (v[0] ** 2 + v[1] ** 2))])

    s = unit(th)
    total = sum((s.dot(unit(a)) for a in ths), sp.Integer(0))
    expansion = sp.series(beta * total, eps, 0, 3).removeO()
    quad = sp.expand(expansion.coeff(eps, 2))
    target = -sp.Rational(1, 2) * beta * sum(((th[0] - a[0]) ** 2 + (th[1] - a[1]) ** 2 for a in ths), sp.Integer(0))
    ok1 = sp.simplify(quad - target) == 0 and sp.simplify(expansion.coeff(eps, 0) - 3 * beta) == 0 and expansion.coeff(eps, 1) == 0
    # the minimizer of the quadratic form is the average of the three transverse coordinates (gain one)
    sol = sp.solve([sp.diff(quad, th[0]), sp.diff(quad, th[1])], th, dict=True)[0]
    avg = [sum((a[j] for a in ths), sp.Integer(0)) / 3 for j in range(2)]
    if mut("gain_wrong"):
        avg = [sum((a[j] for a in ths[:2]), sp.Integer(0)) / 2 for j in range(2)]
    ok2 = all(sp.simplify(sol[th[j]] - avg[j]) == 0 for j in range(2))
    hess = sp.hessian(quad, th)
    ok3 = sp.simplify(hess - (-3 * beta) * sp.eye(2)) == sp.zeros(2, 2)
    # exact one-step transverse variance at the aligned plane: per component A(3 beta)/(3 beta) (from E[1 - w^2] = 2A/kappa at kappa = 3 beta)
    k = sp.symbols("kappa", positive=True)
    A = sp.coth(k) - 1 / k
    per_component = sp.simplify(((1 - (1 - 2 * A / k)) / 2).subs(k, 3 * beta) - (sp.coth(3 * beta) - 1 / (3 * beta)) / (3 * beta)) == 0
    checks.check("C1", ok1 and ok2 and ok3 and per_component, "T2: beta s.(s_1 + s_2 + s_3) = 3 beta - (beta/2) sum_i |theta - theta_i|^2 + O(4) in transverse coordinates; the minimizer is the average of the three (gain one) with Hessian -3 beta I; the exact one-step transverse variance is A(3 beta)/(3 beta) per component")


# ============================================================================================ family D
def trinomial(kk: int, a: int, b: int) -> int:
    return factorial(kk) // (factorial(a) * factorial(b) * factorial(kk - a - b))


def P_exact(kk: int) -> Fraction:
    tot = 0
    for a in range(kk + 1):
        for b in range(kk + 1 - a):
            m = trinomial(kk, a, b)
            tot += m * m
    return Fraction(tot, 9 ** kk)


def family_d(checks: Checks) -> None:
    # D1: the trinomial identity against direct path enumeration (steps: stay-in-column for e_1, and the two in-plane shifts)
    base = 3
    if mut("path_identity_wrong"):
        base = 2
    ok1 = True
    for kk in range(1, 7):
        counts = {}
        for path in product(range(3), repeat=kk):
            a = sum(1 for st in path if st == 1)
            b = sum(1 for st in path if st == 2)
            counts[(a, b)] = counts.get((a, b), 0) + 1
        ok1 = ok1 and all(Fraction(c, base ** kk) == Fraction(trinomial(kk, a, b), 3 ** kk) for (a, b), c in counts.items())
        ok1 = ok1 and sum((Fraction(c, 3 ** kk) ** 2 for c in counts.values()), Fraction(0)) == P_exact(kk)
    checks.check("D1", ok1, "T3: p_k(-a, -b) = k!/(a! b! (k-a-b)!)/3^k by direct enumeration of the 3^k paths for k <= 6, and P_k = sum_y p_k(y)^2 (the return sum)")
    # D2: two-sided bounds with rational enclosures
    c_lo, c_hi = C0_LO, C0_HI
    if mut("return_constant_wrong"):
        c_lo, c_hi = 2 * C0_LO, 2 * C0_HI
    sub = Fraction(1)
    if mut("return_lower_bound_wrong"):
        sub = Fraction(0)
    ok2 = True
    worst = Fraction(0)
    for kk in range(1, 151):
        p = P_exact(kk)
        x_lo = Fraction(isqrt(kk * 10 ** 6), 10 ** 3) / 7          # a rational lower bound of sqrt(k)/7
        hi = c_hi / kk + Fraction(27, kk * kk) + exp_neg_upper(x_lo)
        lo = c_lo / kk - sub / (kk * kk) - Fraction(5, 2 * kk) * exp_neg_upper(Fraction(kk, 4))
        ok2 = ok2 and lo <= p <= hi
        worst = max(worst, abs(kk * p - (c_lo + c_hi) / 2) * kk)
    checks.check("D2", ok2 and worst < 1, "T3: for k <= 150 the exact return sums satisfy 3 sqrt3/(4 pi k) - 1/k^2 - (5/(2k)) e^{-k/4} <= P_k <= 3 sqrt3/(4 pi k) + 27/k^2 + e^{-sqrt(k)/7}, with sqrt3, pi and the exponentials enclosed rationally; k^2 |P_k - 3 sqrt3/(4 pi k)| stays below 1")
    # D3: the Gaussian integrals of the proof and the harmonic lower bound
    x, y, kk_s = sp.symbols("x y k", positive=True)
    M = sp.Matrix([[2, -1], [-1, 2]]) / 9
    detM = sp.simplify(M.det())
    lam = [sp.Rational(1, 9), sp.Rational(1, 3)]
    gauss = sp.integrate(sp.integrate(sp.exp(-kk_s * (lam[0] * x ** 2 + lam[1] * y ** 2)), (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
    g_ok = sp.simplify(gauss - 3 * sp.sqrt(3) * sp.pi / kk_s) == 0 and detM == sp.Rational(1, 27)
    q2 = sp.integrate(sp.integrate(sp.exp(-kk_s * (lam[0] * x ** 2 + lam[1] * y ** 2)) * (lam[0] * x ** 2 + lam[1] * y ** 2) ** 2, (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
    q2_ok = sp.simplify(q2 - 3 * sp.sqrt(3) * sp.pi / kk_s * 2 / kk_s ** 2) == 0
    r = sp.symbols("r", positive=True)
    quart = sp.integrate(2 * sp.pi * sp.exp(-kk_s * r ** 2 / 9) * r ** 5, (r, 0, sp.oo))
    quart_ok = sp.simplify(quart - 1458 * sp.pi / kk_s ** 3) == 0
    t1, t2 = sp.symbols("theta1 theta2", real=True)
    u = (3 + 2 * sp.cos(t1) + 2 * sp.cos(t2) + 2 * sp.cos(t1 - t2)) / 9
    ident = sp.simplify(1 - u - sp.Rational(4, 9) * (sp.sin(t1 / 2) ** 2 + sp.sin(t2 / 2) ** 2 + sp.sin((t1 - t2) / 2) ** 2)) == 0
    quad_ident = sp.simplify(sp.Rational(1, 9) * (t1 ** 2 + t2 ** 2 + (t1 - t2) ** 2) - (sp.Matrix([t1, t2]).T * M * sp.Matrix([t1, t2]))[0]) == 0
    offset = Fraction(6, 25)
    if mut("harmonic_bound_wrong"):
        offset = Fraction(0)
    acc = Fraction(0)
    H = Fraction(0)
    ok3 = True
    for t in range(1, 151):
        acc += P_exact(t)
        H += Fraction(1, t)
        ok3 = ok3 and acc >= C0_HI * H - offset
    # the tail beyond 150: sum_{k>150} 1/k^2 <= 1/150 and sum_{k>150} (5/(2k)) e^{-k/4} <= (5/302) e^{-151/4} / (1 - e^{-1/4}) with 1 - e^{-1/4} >= 1/5
    tail = Fraction(1, 150) + Fraction(5, 302) * exp_neg_upper(Fraction(151, 4)) * 5
    # the upper constant: sum_{k>=1} (27/k^2 + e^{-sqrt k/7}) <= 27 pi^2/6 + integral_0^inf e^{-sqrt x/7} dx = 27 pi^2/6 + 98 < 150
    xx = sp.symbols("x", positive=True)
    tail_int = sp.integrate(sp.exp(-sp.sqrt(xx) / 7), (xx, 0, sp.oo))
    upper_const = 27 * PI_HI ** 2 / 6 + 98 < 150 and sp.simplify(tail_int - 98) == 0
    checks.check("D3", g_ok and q2_ok and quart_ok and ident and quad_ident and ok3 and tail <= Fraction(1, 100) and upper_const, "T3: 1 - u = (4/9)[sin^2(theta1/2) + sin^2(theta2/2) + sin^2((theta1 - theta2)/2)], the quadratic part is theta^T M theta with det M = 1/27, the Gaussian integrals are 3 sqrt3 pi/k, (3 sqrt3 pi/k)(2/k^2) and 1458 pi/k^3; sum_{k<=t} P_k >= (3 sqrt3/(4 pi)) H_t - 6/25 for t <= 150 exactly and the tail beyond 150 costs at most 1/100, giving the constant 1/4 for every t; the upper error sum 27 pi^2/6 + 98 is below 150")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    beta, k = sp.symbols("beta kappa", positive=True)
    A = sp.coth(k) - 1 / k
    # E1: the one-site plane: s_{t+1} ~ K(.|3 s_t): E[s_{t+1} . e | s_t] = A(3 beta) (s_t . e), so m_t = A(3 beta)^t
    factor = A.subs(k, 3 * beta)
    if mut("one_site_chain_wrong"):
        factor = A.subs(k, beta)
    # the conditional mean is A(kappa) u with u = s_t and kappa = beta |3 s_t| = 3 beta (B1); check the concentration and the power law on t <= 4 symbolically
    m = sp.Integer(1)
    ok1 = True
    for t in range(1, 5):
        m = m * (sp.coth(3 * beta) - 1 / (3 * beta))
        ok1 = ok1 and sp.simplify(m - factor ** t) == 0
    checks.check("E1", ok1, "T4: on the one-site periodic plane the chain s_{t+1} ~ K_beta(.|3 s_t) has E[s_{t+1}.e | s_t] = A(3 beta)(s_t.e), so m_t = A(3 beta)^t exactly")
    # E2: the minorization: the density against the uniform law is (kappa/sinh kappa) e^{kappa w} >= 2 kappa/(e^{2 kappa} - 1), decreasing in kappa, >= 2 kappa e^{-2 kappa}
    dens_min = sp.simplify(((k / sp.sinh(k)) * sp.exp(-k) - 2 * k / (sp.exp(2 * k) - 1)).rewrite(sp.exp))
    g = 2 * k / (sp.exp(2 * k) - 1)
    lower = 2 * k * sp.exp(-2 * k)
    if mut("minorization_wrong"):
        lower = 4 * k * sp.exp(-2 * k)
    diff = sp.simplify((g - lower) * (sp.exp(2 * k) - 1) * sp.exp(2 * k) / (2 * k))   # = e^{2k} - (e^{2k} - 1) * c = 1 when c = 1
    decreasing = sp.simplify(sp.diff(g, k) * (sp.exp(2 * k) - 1) ** 2 / 2 - (sp.exp(2 * k) - 1 - 2 * k * sp.exp(2 * k))) == 0
    # e^{2k} - 1 - 2k e^{2k} < 0 for k > 0: its derivative is -4k e^{2k} < 0 and it vanishes at 0
    dneg = sp.simplify(sp.diff(sp.exp(2 * k) - 1 - 2 * k * sp.exp(2 * k), k) + 4 * k * sp.exp(2 * k)) == 0
    checks.check("E2", dens_min == 0 and sp.simplify(diff - 1) == 0 and decreasing and dneg, "T4: the kernel's density against the uniform law on the sphere is at least 2 kappa/(e^{2 kappa} - 1) >= 2 kappa e^{-2 kappa}, decreasing in kappa; on an L x L plane the level kernel has density at least (6 beta/(e^{6 beta} - 1))^{L^2}, a uniform minorization")
    # E3: the exponent gamma(beta) = (3 sqrt3/(4 pi)) A(3 beta)/(3 beta) with exact enclosures
    stated = {3: (Fraction(408, 10 ** 4), Fraction(409, 10 ** 4)), 6: (Fraction(216, 10 ** 4), Fraction(217, 10 ** 4)), 12: (Fraction(1116, 10 ** 5), Fraction(1117, 10 ** 5)), 24: (Fraction(566, 10 ** 5), Fraction(567, 10 ** 5))}
    c_lo, c_hi = C0_LO, C0_HI
    if mut("exponent_wrong"):
        c_lo, c_hi = 2 * C0_LO, 2 * C0_HI
    ok3 = True
    for b, (lo_s, hi_s) in stated.items():
        a_lo, a_hi = A_bounds(Fraction(3 * b))
        g_lo, g_hi = c_lo * a_lo / (3 * b), c_hi * a_hi / (3 * b)
        ok3 = ok3 and lo_s <= g_lo and g_hi <= hi_s
    checks.check("E3", ok3, "T5: gamma(beta) = (3 sqrt3/(4 pi)) A(3 beta)/(3 beta) lies in [408, 409]/10^4 at beta = 3, [216, 217]/10^4 at 6, [1116, 1117]/10^5 at 12, [566, 567]/10^5 at 24 (exact enclosures)")
    # E4: the six-axis side-by-side at (p, q, r) = (e^beta, e^-beta, 1): block 12's closed forms specialised
    p, q, r = sp.exp(beta), sp.exp(-beta), sp.Integer(1)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)
    c1 = (sp.exp(-3 * beta) + 4) / (sp.exp(3 * beta) + sp.exp(-3 * beta) + 4)
    c2 = (sp.exp(-beta) + 4) / (sp.exp(beta) + sp.exp(-beta) + 4)
    if mut("sixaxis_deviation_wrong"):
        c2 = (sp.exp(-beta) + 2) / (sp.exp(beta) + sp.exp(-beta) + 4)
    c3 = (sp.exp(-2 * beta) + sp.exp(beta) + sp.exp(-beta) + 2) / (sp.exp(2 * beta) + sp.exp(-2 * beta) + sp.exp(beta) + sp.exp(-beta) + 2)
    ok4 = all(sp.simplify(a - b) == 0 for a, b in ((d1, c1), (d2, c2), (d3, c3)))
    # at beta = 3 the aligned-triple deviation d1 = (e^-9 + 4)/(e^9 + e^-9 + 4) < 1/2000 (e^9 > 8000), and at beta = 6 below 1/10^7
    e9_lo = exp_bounds(Fraction(9))[0]
    e18_lo = exp_bounds(Fraction(18))[0]
    small = (Fraction(5) / e9_lo) < Fraction(1, 1600) and (Fraction(5) / e18_lo) < Fraction(1, 10 ** 7)
    checks.check("E4", ok4 and small, "side-by-side: at the six-axis weights (e^beta, e^-beta, 1) the three deviations are (e^{-3 beta} + 4)/(e^{3 beta} + e^{-3 beta} + 4), (e^{-beta} + 4)/(e^{beta} + e^{-beta} + 4), (e^{-2 beta} + e^{beta} + e^{-beta} + 2)/(e^{2 beta} + e^{-2 beta} + e^{beta} + e^{-beta} + 2); the aligned-triple deviation is below 1/1600 at beta = 3 and below 1/10^7 at beta = 6")


# ============================================================================================ family F
FENCES = (
    "This note proves, for the unsoldered formation law `K_β(s | s_1, s_2, s_3) ∝ e^{β s·(s_1 + s_2 + s_3)}` in level time, the exact one-step identities of its kernel, the local-limit constant `3√3/(4π)` of the level walk's return sum with explicit error bounds, the loss of the initial plane's memory on every finite periodic plane, and the exponent `γ(β) = (3√3/(4π))·A(3β)/(3β)` of the linearized transverse field; the algebraic decay of the nonlinear law's magnetization on the infinite plane is executed by simulation and is not proved; it does not select a menu, reading, order or coupling as physical, and adopts no clause.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "has no ordered phase", "does not order", "spontaneous symmetry breaking", "quasi-long-range", "proves that the sphere formation law",
)
CLAIM_INJECTIONS = {"claim_order_injected": "Hence the sphere formation law has no ordered phase."}
CLASSICAL_NAMES = ("Mermin", "Wagner", "Fisher", "Mises", "Langevin", "Toner", "Vicsek", "Toom", "Dobrushin", "Shlosman", "Pfister", "Fröhlich", "Peierls", "Bogoliubov")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T5", phrase + "\n\n## Theorem T5", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Langevin)", 1)
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
    front = sections[0]
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if nm in front]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed — the kernel's moments and normalizer symbolically; the bound A(kappa) < kappa/3 at ten rational points by exact enclosure; the second-order expansion and its minimizer",
    "per_site: executed — the one-site chain m_t = A(3 beta)^t; the minorization identities; the six-axis deviations at (e^beta, e^-beta, 1) in closed form with exact enclosures at beta = 3, 6",
    "per_mode: executed — the trinomial path identity by enumeration for k <= 6; the return sums P_k exactly for k <= 150 against the two-sided bounds with the constant 3 sqrt3/(4 pi); the Gaussian integrals of the proof",
    "per_block: executed — sum_{k<=t} P_k >= (3 sqrt3/(4 pi)) H_t - 3 for t <= 150; the exponent gamma(beta) enclosed at four couplings",
    "lattice_wide: T1-T5 proved for every beta > 0; the nonlinear decay on the infinite plane simulated at beta = 3, 6, 12, 24 (control and refuter outputs), not proved",
)


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
    family_e(checks)
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
