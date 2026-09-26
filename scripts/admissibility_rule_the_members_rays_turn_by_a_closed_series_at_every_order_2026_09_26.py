#!/usr/bin/env python3
"""Exact checks: the curvature member's rays turn by a closed series at every order, and the series reaches exactly down to the
capture threshold at every charge ratio (a harvest of probe #9231, confirmed by an other-family referee in #9326). Block 110's
declared model as landed: the index n = (1 + a u)^3/(1 - p u), u = 1/r, and the invariant r n sin(psi) = b along each ray.

A (premises): landed block 110's index, its turn to third order and its capture threshold; the axioms.
B (T1): the substitution w = u/n(u) in the orbit integral; the moments m_k; [w^k] log n(u(w)) = (1/k)[u^k] n^k exactly to
   order 12 on five rational indices and the member; the orbit integral expanded directly to order 5 for a generic index.
C (T2): the member's coefficients as a double binomial sum; block 110 T4's four; the equal-charge series to k = 6; block 110
   T5's series; at a fixed first-order turn the second-order term and the third-order term, which rises with rho.
D (T3): capture by the discriminant of the turning-point cubic: its one positive root is block 110's threshold, with the
   double root u*; values and limit.
E (T4): the radius: nonnegative coefficients; w'(u) and its stationary points; w increasing on [0, u*); d log n/du > 0;
   w''(u*) = -2S/(1 + a u*)^4; the exact coefficient ratios lie in [b_c(1 - 3/(2k)), b_c) for 10 <= k <= 80 at four ratios.
Exact (sympy, fractions). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import math
import random
import re
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_MEMBERS_RAYS_TURN_BY_A_CLOSED_SERIES_AT_EVERY_ORDER_AND_THE_SERIES_REACHES_EXACTLY_DOWN_TO_THE_CAPTURE_THRESHOLD_AT_EVERY_CHARGE_RATIO_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_AROUND_A_BODY_THE_WALKS_RAYS_MATCH_THE_COMPARATORS_AT_EVERY_ORDER_EXACTLY_WHEN_ITS_TWO_CHARGES_AGREE_AND_THEY_AGREE_ONLY_WHEN_HOP_ENERGY_BALANCES_THE_SLOWED_CLOCKS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_members_rays_turn_by_a_closed_series_at_every_order_and_the_series_reaches_exactly_down_to_the_capture_threshold_at_every_charge_ratio_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    "n = χ³/N = (r + a)³/(r²(r − p))",
    "(4/3)(ν₁³ + 6ν₁ν₂ + 3ν₃)/b³",
    "b_c/M = 2(ρ + s + 2)³/((ρ + 3)(s + 1)(ρ + s + 1))",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "inversion_forged": "B",
    "third_order_forged": "C",
    "discriminant_forged": "D",
    "stationary_slope_forged": "E",
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
u, v, t, y, eps = sp.symbols("u v t y epsilon")
a, p, M, rho, b, S, s = sp.symbols("a p M rho b S s", positive=True)


def m_k(k: int):
    """the moment m_k = 2 int_0^1 y^k (1 - y^2)^(-1/2) dy in closed form"""
    return sp.sqrt(sp.pi) * sp.gamma(sp.Rational(k + 1, 2)) / sp.gamma(sp.Rational(k, 2) + 1)


def member_coef(k: int, aa=a, pp=p):
    """[u^k] ((1 + a u)^3/(1 - p u))^k as the double binomial sum"""
    return sum(sp.binomial(3 * k, k - j) * sp.binomial(k + j - 1, j) * aa ** (k - j) * pp ** j for j in range(k + 1))


def reduce_mod(expr, gen, rel):
    """the numerator of expr reduced modulo the polynomial relation rel(gen) = 0"""
    num = sp.numer(sp.together(expr))
    return sp.expand(sp.rem(sp.Poly(sp.expand(num), gen), sp.Poly(rel, gen)).as_expr())


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, landed = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the member, the rates, the ray model and the content are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[0] = "n = χ²/N = (r + a)²/(r(r − p))"
    checks.check("A3", all(n in landed for n in needles), "landed block 110: the index n = chi^3/N = (r + a)^3/(r^2 (r - p)) (T1), the turn's third order (4/3)(nu1^3 + 6 nu1 nu2 + 3 nu3)/b^3 (T4) and the threshold b_c/M = 2(rho + s + 2)^3/((rho + 3)(s + 1)(rho + s + 1)) (T3)")


# ============================================================================================ family B (T1)
KL = 12


def smul(A, B):
    C = [Fr(0)] * (KL + 1)
    for i, x_ in enumerate(A):
        if x_:
            for j in range(KL + 1 - i):
                C[i + j] += x_ * B[j]
    return C


def compose(nc, U):
    """n(U) for n = sum nc[k] u^k and U = O(w), truncated at order KL"""
    out, P = [Fr(0)] * (KL + 1), [Fr(1)] + [Fr(0)] * KL
    for k in range(KL + 1):
        out = [o + nc[k] * q for o, q in zip(out, P)]
        P = smul(P, U)
    return out


def logser(X):
    """log(1 + X) for X = O(w), truncated at order KL"""
    out, P = [Fr(0)] * (KL + 1), [Fr(1)] + [Fr(0)] * KL
    for j in range(1, KL + 1):
        P = smul(P, X)
        out = [o + Fr((-1) ** (j + 1), j) * q for o, q in zip(out, P)]
    return out


def powcoef(nc, k: int):
    """[u^k] n^k"""
    P = [Fr(1)] + [Fr(0)] * KL
    for _ in range(k):
        P = smul(P, nc)
    return P[k]


def trunc_eps(expr, order: int):
    poly = sp.Poly(sp.expand(expr), eps)
    return sum(cf * eps ** mon[0] for mon, cf in poly.terms() if mon[0] <= order)


def family_b(checks: Checks) -> None:
    # B1: the substitution.  With w(u) = u/n(u) and g(w) = log n(u(w)), du/(n sqrt(1/b^2 - w^2)) = (1 + w g'(w)) dw/sqrt(1/b^2 - w^2),
    # and n^2/b^2 - u^2 = n^2 (1/b^2 - w^2).
    nf = sp.Function("n")(u)
    wu = u / nf
    dwdu = sp.diff(wu, u)
    gprime = (sp.diff(nf, u) / nf) / dwdu                 # g'(w) = (d log n/du)(du/dw)
    lhs = (1 / dwdu) / nf                                 # (du/dw)/n
    rhs = 1 + wu * gprime
    ok1 = sp.simplify(lhs - rhs) == 0 and sp.simplify(nf ** 2 / b ** 2 - u ** 2 - nf ** 2 * (1 / b ** 2 - wu ** 2)) == 0
    half = sp.integrate(1 / sp.sqrt(1 - y ** 2), (y, 0, 1))
    checks.check("B1", ok1 and half == sp.pi / 2, "the orbit integral: with w = u/n(u) and g(w) = log n(u(w)), du/(n sqrt(1/b^2 - w^2)) = (1 + w g'(w)) dw/sqrt(1/b^2 - w^2) and n^2/b^2 - u^2 = n^2 (1/b^2 - w^2); the '1' gives exactly the half-turn pi/2")
    # B2: the moments
    ms = [sp.integrate(2 * y ** k / sp.sqrt(1 - y ** 2), (y, 0, 1)) for k in range(1, 9)]
    listed = [2, sp.pi / 2, sp.Rational(4, 3), 3 * sp.pi / 8, sp.Rational(16, 15), 5 * sp.pi / 16, sp.Rational(32, 35), 35 * sp.pi / 128]
    ok2 = all(sp.simplify(ms[k - 1] - m_k(k)) == 0 and sp.simplify(ms[k - 1] - listed[k - 1]) == 0 for k in range(1, 9))
    checks.check("B2", ok2, "the moments m_k = 2 int_0^1 y^k (1 - y^2)^(-1/2) dy = sqrt(pi) Gamma((k+1)/2)/Gamma(k/2 + 1) = 2, pi/2, 4/3, 3pi/8, 16/15, 5pi/16, 32/35, 35pi/128 (k = 1..8), integrated exactly")
    # B3: the inversion identity, exactly to order 12
    rng = random.Random(1)
    indices = [[Fr(1)] + [Fr(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(KL)] for _ in range(5)]
    Am, Pm = Fr(2, 7), Fr(3, 5)
    indices.append([sum(Fr(math.comb(3, i)) * Am ** i * Pm ** (k - i) for i in range(0, min(3, k) + 1)) for k in range(KL + 1)])
    ok3 = True
    for nc in indices:
        U = [Fr(0), Fr(1)] + [Fr(0)] * (KL - 1)
        for _ in range(KL + 1):
            U = [Fr(0)] + compose(nc, U)[:KL]                # u = w n(u)
        g = logser([x_ - (1 if i == 0 else 0) for i, x_ in enumerate(compose(nc, U))])
        den = (lambda k: k + 1) if mut("inversion_forged") else (lambda k: k)
        ok3 = ok3 and all(g[k] == powcoef(nc, k) / den(k) for k in range(1, KL + 1))
    checks.check("B3", ok3, "for the root u(w) of u = w n(u) with u(0) = 0: [w^k] log n(u(w)) = (1/k)[u^k] n(u)^k, exactly to order 12, on five random rational indices and on the member at (a, p) = (2/7, 3/5)")
    # B4: the orbit integral expanded directly (an independent route), to order 5 for a generic index
    KA = 5
    nus = sp.symbols("nu1:%d" % (KA + 1))
    n_gen = 1 + sum(nus[k] * u ** (k + 1) for k in range(KA))
    N2 = sp.expand(sp.series(n_gen ** 2, u, 0, KA + 1).removeO())
    c = [sp.expand(N2.coeff(u, k)) for k in range(KA + 1)]
    x0 = sp.Integer(1)                                     # the scaled turning point: x0 = n(eps x0), as a series in eps = 1/b
    for _ in range(KA + 1):
        x0 = trunc_eps(1 + sum(nus[k] * (eps * x0) ** (k + 1) for k in range(KA)), KA)
    ok_tp = trunc_eps(sum(c[k] * (eps * x0) ** k for k in range(KA + 1)) - x0 ** 2, KA) == 0
    dx = 1 - x0                                            # O(eps), so 1/x0 = sum_j dx^j
    x0inv = trunc_eps(sum(dx ** j for j in range(KA + 1)), KA)
    ok_tp = ok_tp and trunc_eps(x0 * x0inv, KA) == 1

    def x0pow(n_: int):
        return x0inv if n_ == -1 else x0 ** n_

    # n(eps x0 v)^2 - x0^2 v^2 = (1 - v) x0^2 [(1 + v) - T(v)],  T(v) = sum_k c_k eps^k x0^(k-2) (1 + v + ... + v^(k-1))
    T = trunc_eps(sum(c[k] * eps ** k * x0pow(k - 2) * sum(v ** i for i in range(k)) for k in range(1, KA + 1)), KA)
    cache = {}

    def ivj(mm: int, j: int):
        if (mm, j) not in cache:
            cache[(mm, j)] = sp.integrate(sp.Integer(2) ** (1 - j) * (1 - t ** 2) ** mm * (1 + t ** 2) ** (j - mm - 1), (t, 0, 1))
        return cache[(mm, j)]

    tot, Tj = sp.Integer(0), sp.Integer(1)
    for j in range(KA + 1):
        if j:
            Tj = trunc_eps(Tj * T, KA)
        for (mm,), cm in sp.Poly(Tj, v).terms():
            tot += sp.binomial(2 * j, j) / sp.Integer(4) ** j * cm * ivj(mm, j)
    chi_direct = sp.expand(2 * tot - sp.pi)
    ok4 = ok_tp and sp.simplify(chi_direct.coeff(eps, 0)) == 0
    for k in range(1, KA + 1):
        closed = sp.expand(m_k(k) * sp.series(n_gen ** k, u, 0, k + 1).removeO().coeff(u, k))
        ok4 = ok4 and sp.simplify(chi_direct.coeff(eps, k) - closed) == 0
    landed_t4 = [2 * nus[0], sp.pi * (nus[1] + nus[0] ** 2 / 2), sp.Rational(4, 3) * (nus[0] ** 3 + 6 * nus[0] * nus[1] + 3 * nus[2])]
    ok4 = ok4 and all(sp.simplify(chi_direct.coeff(eps, k + 1) - landed_t4[k]) == 0 for k in range(3))
    fourth = sp.factor(chi_direct.coeff(eps, 4))
    ok4 = ok4 and sp.simplify(fourth - 3 * sp.pi / 8 * (nus[0] ** 4 + 12 * nus[0] ** 2 * nus[1] + 12 * nus[0] * nus[2] + 6 * nus[1] ** 2 + 4 * nus[3])) == 0
    checks.check("B4", ok4, "the orbit integral 2 int_0^u0 du/sqrt(n^2/b^2 - u^2) expanded directly in 1/b for n = 1 + nu1 u + ... + nu5 u^5 (turning point x0 = n(x0/b), exact rational integrals in tan(theta/2)): the (1/b)^k coefficient is m_k [u^k] n^k for k = 1..5; orders 1-3 are landed block 110 T4's; order 4 is (3pi/8)(nu1^4 + 12 nu1^2 nu2 + 12 nu1 nu3 + 6 nu2^2 + 4 nu4)")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    n_mem = (1 + a * u) ** 3 / (1 - p * u)
    ok1 = all(sp.expand(member_coef(k) - sp.series(n_mem ** k, u, 0, k + 1).removeO().coeff(u, k)) == 0 for k in range(1, 9))
    checks.check("C1", ok1, "the member: [u^k] ((1 + a u)^3/(1 - p u))^k = sum_j C(3k, k - j) C(k + j - 1, j) a^(k-j) p^j for k = 1..8")
    landed = [2 * (3 * a + p), sp.Rational(3, 2) * sp.pi * (5 * a ** 2 + 4 * a * p + p ** 2),
              sp.Rational(8, 3) * (42 * a ** 3 + 54 * a ** 2 * p + 27 * a * p ** 2 + 5 * p ** 3),
              sp.Rational(15, 8) * sp.pi * (99 * a ** 4 + 176 * a ** 3 * p + 132 * a ** 2 * p ** 2 + 48 * a * p ** 3 + 7 * p ** 4)]
    ok2 = all(sp.expand(m_k(k + 1) * member_coef(k + 1) - landed[k]) == 0 for k in range(4))
    checks.check("C2", ok2, "m_k [u^k] n^k reproduces landed block 110 T4's four coefficients 2(3a + p), (3pi/2)(5a^2 + 4ap + p^2), (8/3)(42a^3 + 54a^2 p + 27ap^2 + 5p^3), (15pi/8)(99a^4 + ... + 7p^4)")
    eq = [sp.simplify(m_k(k) * member_coef(k, M / 2, M / 2) / M ** k) for k in range(1, 7)]
    listed = [4, 15 * sp.pi / 4, sp.Rational(128, 3), 3465 * sp.pi / 64, sp.Rational(3584, 5), 255255 * sp.pi / 256]
    checks.check("C3", all(sp.simplify(x - y_) == 0 for x, y_ in zip(eq, listed)), "at equal charges a = p = M/2 the series is 4, 15pi/4, 128/3, 3465pi/64, 3584/5, 255255pi/256 times (M/b)^k, k = 1..6")
    kap = sp.Symbol("kappa", positive=True)
    ok4 = all(sp.simplify(m_k(k) * sp.series(sp.exp(k * kap * u), u, 0, k + 1).removeO().coeff(u, k)
                          - sp.sqrt(sp.pi) * k ** k * sp.gamma(sp.Rational(k + 1, 2)) / (sp.factorial(k) * sp.gamma(sp.Rational(k, 2) + 1)) * kap ** k) == 0
              for k in range(1, 9))
    checks.check("C4", ok4, "for the index e^(kappa u) the closed series gives landed block 110 T5's c_k = sqrt(pi) k^k Gamma((k+1)/2)/(k! Gamma(k/2+1)) kappa^k, k = 1..8")
    aa = 2 * M / (3 + rho)
    sec = sp.simplify(m_k(2) * member_coef(2, aa, rho * aa) / M ** 2)
    third = sp.simplify(m_k(3) * member_coef(3, aa, rho * aa) / M ** 3)
    third_claim = sp.Rational(64, 3) * (42 + 54 * rho + 27 * rho ** 2 + 5 * rho ** 3) / (3 + rho) ** 3
    if mut("third_order_forged"):
        third_claim = sp.Rational(64, 3) * (42 + 55 * rho + 27 * rho ** 2 + 5 * rho ** 3) / (3 + rho) ** 3
    slope = sp.simplify(sp.diff(third_claim, rho) - 384 * (rho + 1) * (rho + 2) / (3 + rho) ** 4)
    ok5 = (sp.simplify(sec - 6 * sp.pi * (5 + 4 * rho + rho ** 2) / (3 + rho) ** 2) == 0
           and sp.simplify(third - third_claim) == 0 and slope == 0
           and third_claim.subs(rho, 0) == sp.Rational(896, 27) and third_claim.subs(rho, 1) == sp.Rational(128, 3)
           and sp.limit(third_claim, rho, sp.oo) == sp.Rational(320, 3))
    checks.check("C5", ok5, "at a fixed first-order turn (3a + p = 2M, rho = p/a): second order 6pi(5 + 4rho + rho^2)/(3 + rho)^2 (landed); third order (64/3)(42 + 54rho + 27rho^2 + 5rho^3)/(3 + rho)^3 (M/b)^3, slope 384(rho + 1)(rho + 2)/(3 + rho)^4 > 0, from 896/27 through 128/3 at rho = 1 to 320/3")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    cub = sp.expand((1 + a * u) ** 3 - b * u * (1 - p * u))
    disc = sp.expand(sp.discriminant(cub, u))
    c0 = 26 if mut("discriminant_forged") else 27
    bracket = c0 * a ** 2 * (a + p) ** 2 + (4 * p ** 3 + 6 * a * p ** 2 - 6 * a ** 2 * p - 4 * a ** 3) * b - p ** 2 * b ** 2
    checks.check("D1", sp.expand(disc + b ** 2 * bracket) == 0, "turning points solve E_b(u) = (1 + a u)^3 - b u (1 - p u) = 0; Disc_u E_b = -b^2 [27a^2 (a + p)^2 + (4p^3 + 6ap^2 - 6a^2 p - 4a^3) b - p^2 b^2]")
    br = sp.Poly(bracket, b)
    prod_roots = sp.simplify(br.coeff_monomial(1) / br.coeff_monomial(b ** 2))
    at_p0 = sp.solve(bracket.subs(p, 0), b)
    checks.check("D2", sp.simplify(prod_roots + 27 * a ** 2 * (a + p) ** 2 / p ** 2) == 0 and at_p0 == [27 * a / 4],
                 "for p > 0 the bracket's two roots in b have product -27a^2 (a + p)^2/p^2 < 0, so exactly one is positive; at p = 0 the bracket is linear with root 27a/4")
    aa = 2 * M / (3 + rho)
    bc_landed = 2 * M * (rho + s + 2) ** 3 / ((rho + 3) * (s + 1) * (rho + s + 1))
    red = reduce_mod(bracket.subs({a: aa, p: rho * aa, b: bc_landed}), s, s ** 2 - rho ** 2 - rho - 1)
    checks.check("D3", red == 0, "landed block 110 T3's b_c/M = 2(rho + s + 2)^3/((rho + 3)(s + 1)(rho + s + 1)), s^2 = rho^2 + rho + 1, is that positive root (the bracket reduces to 0)")
    us = 1 / (a + p + S)
    bcs = (1 / us + a) ** 3 / ((1 / us) * (1 / us - p))
    rel = S ** 2 - (a ** 2 + a * p + p ** 2)
    e0 = reduce_mod(cub.subs({u: us, b: bcs}), S, rel)
    e1 = reduce_mod(sp.diff(cub, u).subs({u: us, b: bcs}), S, rel)
    gap = reduce_mod(1 / p - us - (a + S) / (p * (a + p + S)), S, rel)
    checks.check("D4", e0 == 0 and e1 == 0 and gap == 0, "at b = b_c = f(r*), r* = a + p + S, S = sqrt(a^2 + ap + p^2), the cubic has the double root u* = 1/r* (the circular ray), and 1/p - u* = (a + S)/(p(a + p + S)) > 0")
    vals = []
    for rv in (0, sp.Rational(1, 2), 1, 3):
        sv = sp.sqrt(rv ** 2 + rv + 1)
        vals.append(sp.radsimp(sp.simplify((bc_landed / M).subs({rho: rv, s: sv}))))
    target = [sp.Rational(9, 2), 4 * sp.sqrt(7) - sp.Rational(40, 7), 3 * sp.sqrt(3), (70 + 26 * sp.sqrt(13)) / 27]
    lim = sp.limit((bc_landed / M).subs(s, sp.sqrt(rho ** 2 + rho + 1)), rho, sp.oo)
    checks.check("D5", all(sp.simplify(x - y_) == 0 for x, y_ in zip(vals, target)) and lim == 8, "b_c/M = 9/2, 4 sqrt7 - 40/7, 3 sqrt3, (70 + 26 sqrt13)/27 at rho = 0, 1/2, 1, 3, tending to 8")


# ============================================================================================ family E (T4)
def surd_lt(x: Fr, q1: Fr, q2: Fr, d: int) -> bool:
    """x < q1 + q2 sqrt(d), exactly, for q2 > 0"""
    z = x - q1
    return z < 0 or z * z < q2 * q2 * d


def surd_gt(x: Fr, q1: Fr, q2: Fr, d: int) -> bool:
    """x > q1 + q2 sqrt(d), exactly, for q2 > 0"""
    z = x - q1
    return z > 0 and z * z > q2 * q2 * d


def family_e(checks: Checks) -> None:
    n_mem = (1 + a * u) ** 3 / (1 - p * u)
    ok1 = True
    for k in range(1, 13):
        cf = sp.Poly(sp.expand(sp.series(n_mem ** k, u, 0, k + 1).removeO().coeff(u, k)), a, p)
        ok1 = ok1 and all(c_ > 0 for c_ in cf.coeffs())
    checks.check("E1", ok1, "the coefficients: [u^k] n^k is a polynomial in (a, p) with positive coefficients (k = 1..12; in general, (1 + a u)^(3k) and (1 - p u)^(-k) have nonnegative coefficients), so lambda_k = (1/k)[u^k] n^k >= 0 whenever a, p >= 0")
    wexpr = u * (1 - p * u) / (1 + a * u) ** 3
    q = 1 - 2 * (a + p) * u + a * p * u ** 2
    ok2 = sp.simplify(sp.diff(wexpr, u) - q / (1 + a * u) ** 4) == 0
    ok2 = ok2 and sp.simplify(wexpr * (1 / u + a) ** 3 / ((1 / u) * (1 / u - p)) - 1) == 0
    rel = S ** 2 - (a ** 2 + a * p + p ** 2)
    us, um = 1 / (a + p + S), 1 / (a + p - S)
    ok2 = ok2 and reduce_mod(q.subs(u, us), S, rel) == 0 and reduce_mod(q.subs(u, um), S, rel) == 0
    ok2 = ok2 and reduce_mod((a + p) ** 2 - S ** 2 - a * p, S, rel) == 0
    checks.check("E2", ok2, "w(u) = u(1 - p u)/(1 + a u)^3 = 1/(r n) has w'(u) = q(u)/(1 + a u)^4, q = 1 - 2(a + p)u + a p u^2, with roots u* = 1/(a + p + S) and u- = 1/(a + p - S) ((a + p)^2 - S^2 = ap >= 0), so q > 0 on [0, u*) and w rises there to w(u*) = 1/b_c")
    dlog = sp.simplify(sp.diff(sp.log(n_mem), u) - (3 * a / (1 + a * u) + p / (1 - p * u)))
    checks.check("E3", dlog == 0, "d log n/du = 3a/(1 + a u) + p/(1 - p u) > 0 on [0, 1/p), which contains [0, u*] (D4)")
    slope_rhs = -S if mut("stationary_slope_forged") else S
    ident = reduce_mod((a + p) - a * p * us - slope_rhs, S, rel)
    qprime = sp.diff(q, u)
    ident2 = reduce_mod(qprime.subs(u, us) + 2 * slope_rhs, S, rel)
    checks.check("E4", ident == 0 and ident2 == 0, "at the stationary point, a + p - a p u* = S exactly, so q'(u*) = -2S and w''(u*) = -2S/(1 + a u*)^4 < 0: u(w) - u* ~ -c sqrt(w* - w) with c > 0, and g'(w) = (d log n/du) u'(w) is unbounded as w -> w* = 1/b_c")
    # E5: exact evidence, not a proof: the coefficient ratios lambda_{k+1}/lambda_k in [b_c(1 - 3/(2k)), b_c)
    cases = {Fr(0): (Fr(9, 2), Fr(0), 1), Fr(1, 2): (Fr(-40, 7), Fr(4), 7), Fr(1): (Fr(0), Fr(3), 3), Fr(3): (Fr(70, 27), Fr(26, 27), 13)}
    ok5 = True
    for rv, (q1, q2, d) in cases.items():
        A_ = Fr(2) / (3 + rv)
        P_ = rv * A_
        lam = []
        for k in range(1, 82):
            tot = Fr(0)
            for j in range(k + 1):
                tot += math.comb(3 * k, k - j) * math.comb(k + j - 1, j) * A_ ** (k - j) * P_ ** j
            lam.append(tot / k)
        for k in range(10, 81):
            r_k = lam[k] / lam[k - 1]
            lo = Fr(2 * k - 3, 2 * k)
            if d == 1:
                ok5 = ok5 and r_k < q1 and r_k > q1 * lo
            else:
                ok5 = ok5 and surd_lt(r_k, q1, q2, d) and surd_gt(r_k / lo, q1, q2, d)
    checks.check("E5", ok5, "exact evidence: at rho = 0, 1/2, 1, 3 (M = 1) every ratio lambda_{k+1}/lambda_k for 10 <= k <= 80 lies in [b_c(1 - 3/(2k)), b_c), the window of a square-root singularity at w = 1/b_c (compared exactly with 9/2, 4 sqrt7 - 40/7, 3 sqrt3, (70 + 26 sqrt13)/27)")


# ============================================================================================ family F
FENCES = (
    "This note works within block 110 as landed on main (the curvature member's exterior fields and the long-wave ray model of the walk, in the continuum exterior of a spherical body); it reports the turn of the rays at every order in closed form and the exact reach of its series; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the capture threshold."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Bouguer", "Bürmann",
                   "Buermann", "Pringsheim", "Vivanti", "Cauchy", "Lambert", "Schwarzschild", "Richardson", "Abel", "Buchdahl", "Komar", "Tolman")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Lagrange) —", 1)
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
    "per_element: executed - the substitution w = u/n(u) for an arbitrary index; the moments m_k integrated exactly",
    "per_site: executed - the inversion identity to order 12 on six rational indices; the direct expansion to order 5",
    "per_mode: executed - the member's coefficients to k = 8 and k = 12; the discriminant and its positive root",
    "per_block: executed - the stationary points of w, the sign of d log n/du, w''(u*); exact coefficient ratios to k = 81 at four charge ratios",
    "lattice_wide: checked and not executed - lattice corrections to the exterior and finite wave numbers (block 110's model is continuum and long-wave)",
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
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 110's continuum exterior and long-wave ray model: the turn is sum_k m_k [u^k] n^k b^-k at every order; for the member its radius in 1/b is exactly 1/b_c at every charge ratio; the third-order term at a fixed first-order turn rises with rho; harvest of #9231 (confirmed by #9326); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
