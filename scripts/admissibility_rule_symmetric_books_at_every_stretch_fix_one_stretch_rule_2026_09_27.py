#!/usr/bin/env python3
"""Exact checks: under block 69's two-step coupling, a uniform isotropic stretch of a per-axis walk F(k, b) (F(k, 0) = sin k, first-order
term sin k cos^2 k) that acts on the stretched walk as a relabelling keeps single-wave symmetric books at every stretch (the momentum that
generates further stretch parallel to the velocity) iff its generator is gamma(b) F F_k; so u = F^2 obeys u_tau = u_k^2/2, one family up to
reparametrisation. Solved by characteristics and measured by the long-wave speed (dF/dk(0) = 1/l): k = k0 + ((l^2 - 1)/2) sin 2k0,
F = sin k0 sqrt(sin^2 k0 + l^2 cos^2 k0). It is a smooth relabelling of the free walk for 0 < l^2 < 2, never outruns the long-wave speed,
has infinite reach at every l != 1, and has no twice-differentiable continuation to l^2 >= 2 (the band top folds). The supervisor's own
derivation, unrefereed. Block 69 as landed; blocks 179 and 182 (pushed) placed and the facts used re-derived.

A (premises): landed block 69 (uniform form; the leading order does not determine a completion; the two-step momentum); the axioms.
B (T1): the single-wave current v (x) P; its antisymmetric part vanishes for every wave iff p = gamma F F_k; gamma(0) = 1; the flow
   u_tau = u_k^2/2; the fixed-generator flow and the linear completion fail it at every l != 1.
C (T2): the characteristic solution, its first two orders (block 182 T4(b)), the long-wave length tau = (1 - l^2)/2, the species corners.
D (T3): the speed bound 1 - l^2 F_k^2 = sin^2 k0/(sin^2 k0 + l^2 cos^2 k0) per axis and in three dimensions; the fold-free range
   min dk/dk0 = min(l^2, 2 - l^2); the comparison thresholds 7/6 and sqrt(3/2).
E (T4): the band-top curvature -1/(2 - l^2); at l^2 = 2 the law 1 - F ~ (1/2)(3|k - pi/2|/2)^(4/3); for l^2 > 2 three characteristics
   with different slopes meet at k = pi/2.
F (T5): u_kk along characteristics is 2 cos 2k0/(1 + (l^2 - 1) cos 2k0), with a pole at complex k0 whenever l != 1: u is not a
   trigonometric polynomial, so F has infinite reach.
I (T7): for every walk h = sum_a F_a(k_a) X_a + mu Gamma with anticommuting involutions, block 181's objects built from divided
   differences give the site energy a current P^s whose current K^s is symmetric, exactly, for arbitrary F_a (only h^2 a number is
   used; an offset breaks it, as in block 139); on single waves P^s = F F' and <K^s> = E v (x) v; the free walk gives block 181's objects.
Exact (sympy). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_SYMMETRIC_BOOKS_AT_EVERY_STRETCH_FIX_ONE_STRETCH_RULE_IT_NEVER_OUTRUNS_THE_LONG_WAVES_AND_ENDS_AT_A_STRETCH_OF_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_it_never_outruns_the_long_waves_and_ends_at_a_stretch_of_root_two_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
    "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.",
    "Set P_j=S_j C_j=(T_j^2-T_j^-2)/(4i)",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "books_forged": "B",
    "characteristic_forged": "C",
    "speed_forged": "D",
    "fold_forged": "E",
    "pole_forged": "F",
    "pair_books_forged": "I",
    "claim_transition_injected": "G",
    "claim_classical_name_in_theorem": "G",
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


def zero(expr) -> bool:
    return sp.simplify(sp.expand_trig(sp.expand(expr))) == 0


T0 = time.time()
k, b, tau, k0 = sp.symbols("k b tau k0", real=True)
L = sp.Symbol("l", positive=True)
s = sp.sin(k)
c = sp.cos(k)
s0 = sp.sin(k0)
c0 = sp.cos(k0)
x = sp.Symbol("x")


def over_s_in_x(expr):
    """expr is s times a polynomial in s^2 (with even powers of c); return that polynomial in x = s^2"""
    e = sp.expand(sp.simplify(expr / s))
    e = sp.expand(sp.expand_trig(e))
    e = e.subs(sp.cos(k), sp.sqrt(1 - sp.sin(k) ** 2))
    e = sp.expand(e).subs(sp.sin(k), sp.sqrt(x))
    return sp.expand(sp.simplify(e))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its coupling and its completion are supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[1] = "Common corner quadratic forms are a leading-order result and determine a nonlinear completion."
    checks.check("A3", all(n in t69 for n in needles), "landed block 69: the uniform form s_a + c_a sum_j B s_j c_j (isotropic B = b: F = s + b s c^2); its N1: the leading order does not determine a nonlinear completion; the two-step momentum")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    # single-wave lemma: continuity sum_a q_a J_a(k, k) = (q . grad E) rho(k, k) for every q forces J_a = v_a rho (block 179 T1)
    q1, q2, q3 = sp.symbols("q1:4")
    J = sp.symbols("J1:4")
    v = sp.symbols("v1:4")
    rho = sp.Symbol("rho")
    eqs = sp.Poly(sum(qq * (jj - vv * rho) for qq, jj, vv in zip((q1, q2, q3), J, v)), q1, q2, q3).coeffs()
    sol = sp.solve(eqs, J, dict=True)
    ok_lemma = len(sol) == 1 and all(sp.simplify(sol[0][J[i]] - v[i] * rho) == 0 for i in range(3))
    # per-axis walk: v_a = F(k_a) F'(k_a)/E; momentum P_j = p(k_j); antisymmetric part of v (x) P
    y1, y2 = sp.symbols("y1 y2", real=True)
    Ff = sp.Function("F")
    pf = sp.Function("p")
    gam = sp.Symbol("gamma")
    E = sp.Symbol("E", positive=True)

    def FF(yy):
        return Ff(yy) * sp.diff(Ff(yy), yy)

    anti = (FF(y1) / E) * pf(y2) - (FF(y2) / E) * pf(y1)
    books = anti.subs(pf(y2), gam * FF(y2)).subs(pf(y1), gam * FF(y1))
    ok_books = sp.simplify(books.doit()) == 0
    # gamma(0) = 1: at b = 0, F F_k = s c = block 69's two-step symbol
    ok_g0 = sp.simplify(s * sp.diff(s, k) - s * c) == 0
    # the flow dF/db = gamma(b) F F_k^2  <=>  u = F^2 obeys u_b = gamma u_k^2/2; with tau = int gamma db, u_tau = u_k^2/2
    u = sp.Function("u")(k, b)
    g_b = sp.Function("g")(b)
    Fs = sp.sqrt(u)
    ok_flow = sp.simplify((sp.diff(Fs, b) - g_b * Fs * sp.diff(Fs, k) ** 2).subs(sp.Derivative(u, b), g_b * sp.diff(u, k) ** 2 / 2)) == 0
    # witnesses that fail: the fixed-generator flow F = s/sqrt(l^2 c^2 + s^2) with p = s c: ratio p/(F F_k) = (l^2 c^2 + s^2)^2/l^2
    Ffix = s / sp.sqrt(L ** 2 * c ** 2 + s ** 2)
    ratio_fix = sp.simplify(s * c / (Ffix * sp.diff(Ffix, k)))
    want_fix = (L ** 2 * c ** 2 + s ** 2) ** 2 / L ** 2
    if mut("books_forged"):
        want_fix = (L ** 2 * c ** 2 + s ** 2) / L ** 2
    ok_fix = sp.simplify(ratio_fix - want_fix) == 0
    fix_a = want_fix.subs(L, 2).subs(k, sp.asin(sp.Rational(3, 5)))
    fix_b = want_fix.subs(L, 2).subs(k, sp.asin(sp.Rational(4, 5)))
    # the linear completion (block 182 T6, re-derived): F = s(1 + (l - 1)s^2)/l with generator s c/(l(1 + 3(l - 1)s^2))
    Fl = s * (1 + (L - 1) * s ** 2) / L
    pl = sp.simplify(-sp.diff(Fl, L) / sp.diff(Fl, k))
    ratio_lin = sp.simplify(pl / (Fl * sp.diff(Fl, k)))
    lin_a = sp.nsimplify(ratio_lin.subs(L, 2).subs(k, sp.asin(sp.Rational(3, 5))))
    lin_b = sp.nsimplify(ratio_lin.subs(L, 2).subs(k, sp.asin(sp.Rational(4, 5))))
    # T6: the energy current on a single wave is E v_a = (1/2) d(E^2)/dk_a = F F'(k_a) on both branches; it equals P_a = gamma F F'(k_a) iff gamma = 1
    ka, kb_ = sp.symbols("ka kb", real=True)
    E2 = Ff(ka) ** 2 + Ff(kb_) ** 2
    ok_ecur = sp.simplify(sp.diff(E2, ka) / 2 - Ff(ka) * sp.diff(Ff(ka), ka)) == 0
    gsol = sp.solve(sp.Eq(gam * FF(y1), FF(y1)), gam)
    # anisotropic diagonal stretch, each axis its own b_j: the antisymmetric part is F F'(y1) F F'(y2)(gamma(b2) - gamma(b1))/E
    b1_, b2_ = sp.symbols("b1 b2")
    gf = sp.Function("gamma")
    anti_an = sp.simplify((FF(y1) * gf(b2_) * FF(y2) - FF(y2) * gf(b1_) * FF(y1)) / E - FF(y1) * FF(y2) * (gf(b2_) - gf(b1_)) / E)
    # with gamma = 1, b = tau = (1 - l^2)/2: the long-wave metric l^2 = 1 - 2b; block 69 T4's leading inverse metric (1 + b)^2 agrees to first order only
    bb = sp.Symbol("bb")
    inv_exact = sp.series(1 / (1 - 2 * bb), bb, 0, 3).removeO()
    inv_69 = sp.expand((1 + bb) ** 2)
    ok_metric = sp.expand(inv_exact - inv_69) == 3 * bb ** 2
    # in the closed form: dF/d(l^2) at fixed k is -(1/2) F F_k^2
    # general k0: S = sin k0, C = cos k0 with dS/dk0 = C, dC/dk0 = -S, and C^2 = 1 - S^2 at the end
    m = sp.Symbol("m", positive=True)
    S_, C_ = sp.symbols("S C", real=True)

    def dk0(expr):
        return sp.diff(expr, S_) * C_ - sp.diff(expr, C_) * S_

    Fm = S_ * sp.sqrt(S_ ** 2 + m * C_ ** 2)
    km_k0 = 1 + (m - 1) * (C_ ** 2 - S_ ** 2)
    km_m = S_ * C_
    Fk_m = dk0(Fm) / km_k0
    dFdm = sp.diff(Fm, m) - Fk_m * km_m
    resid = sp.simplify(sp.together((dFdm + Fm * Fk_m ** 2 / 2).subs(C_, sp.sqrt(1 - S_ ** 2))))
    ok_dm = resid == 0
    # T8: at fixed label k, d log E/d log l = 2 l^2 dE/d(l^2)/E = -l^2 sum F_a^2 F_a'^2/E^2 = -l^2 |v|^2; at l = 1 block 180's 1 - sum s^4/E^2
    Fa = sp.symbols("Fa1:4", real=True)
    Fda = sp.symbols("Fd1:4", real=True)
    E2s = sum(f_ ** 2 for f_ in Fa)
    dE_dm = sum(Fa[i_] * (-Fa[i_] * Fda[i_] ** 2 / 2) for i_ in range(3)) / sp.sqrt(E2s)
    dlog = sp.simplify(2 * L ** 2 * dE_dm / sp.sqrt(E2s))
    v2 = sum(Fa[i_] ** 2 * Fda[i_] ** 2 for i_ in range(3)) / E2s
    ok_red = sp.simplify(dlog + L ** 2 * v2) == 0
    sv = sp.symbols("sv1:4", real=True)
    v2_free = sum(sv[i_] ** 2 * (1 - sv[i_] ** 2) for i_ in range(3)) / sum(x_ ** 2 for x_ in sv)
    ok_180 = sp.simplify(v2_free - (1 - sum(x_ ** 4 for x_ in sv) / sum(x_ ** 2 for x_ in sv))) == 0
    checks.check("B1", ok_lemma, "single-wave lemma: continuity at first order in q, sum_a q_a J_a(k, k) = (q . v) rho(k, k) for every q, forces J_a(k, k) = v_a rho(k, k); a symmetric current on single waves needs the momentum parallel to the velocity (block 179 T1)")
    checks.check("B2", ok_books and ok_g0 and ok_flow, "for a per-axis walk v_a = F F'(k_a)/E, so v (x) P is symmetric on every single wave iff p = gamma(b) F F_k (p(y1) F F'(y2) = p(y2) F F'(y1) for independent y1, y2); at b = 0, F F_k = s c, so gamma(0) = 1; the flow dF/db = gamma F F_k^2 is u_tau = u_k^2/2 for u = F^2, tau = int gamma db")
    checks.check("B3", ok_fix and fix_a != fix_b and lin_a != lin_b, f"the two other named covariant completions fail at every l != 1: the fixed-generator flow's ratio p/(F F_k) is (l^2 c^2 + s^2)^2/l^2 ({fix_a} vs {fix_b} at l = 2, sin k = 3/5, 4/5); the linear completion's is axis-dependent ({lin_a} vs {lin_b}; block 182 T6)")
    checks.check("B4", ok_ecur and gsol == [1] and anti_an == 0 and ok_metric and ok_dm, "the energy current on a single wave is E v_a = F F'(k_a) on both branches, equal to P_a = gamma F F'(k_a) iff gamma = 1 (for an anisotropic diagonal stretch, P || v alone needs gamma(b1) = gamma(b2), a common constant); then b = tau and the long-wave metric is l^2 = 1 - 2b exactly, while block 69 T4's (1 + b)^2 agrees with 1/(1 - 2b) only to first order (difference 3b^2); in closed form dF/d(l^2) = -(1/2) F F_k^2 at fixed k")
    checks.check("B5", ok_red and ok_180, "at fixed label momentum (sites held physical) the rule gives d log E/d log l = -l^2 |v|^2 = -|u|^2 for every wave, u = l v the velocity in lengths; at l = 1 this is block 180's 1 - sum s^4/E^2 = |v|^2")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    kk = k0 - tau * sp.sin(2 * k0)
    U = s0 ** 2 - tau * sp.sin(2 * k0) ** 2 / 2
    if mut("characteristic_forged"):
        U = s0 ** 2 - tau * sp.sin(2 * k0) ** 2 / 4
    uk = sp.simplify(sp.diff(U, k0) / sp.diff(kk, k0))
    ut = sp.simplify(sp.diff(U, tau) - uk * sp.diff(kk, tau))
    ok_char = zero(uk - sp.sin(2 * k0)) and zero(ut - uk ** 2 / 2) and zero(U.subs(tau, 0) - s0 ** 2) and kk.subs(tau, 0) == k0
    # second order at fixed k: invert k0 = k + tau sin 2k0 to O(tau^2)
    k0s = k + tau * sp.sin(2 * k) + tau ** 2 * sp.sin(2 * k) * 2 * sp.cos(2 * k)
    res = sp.series((kk.subs(k0, k0s) - k), tau, 0, 3).removeO()
    Us = sp.series(U.subs(k0, k0s), tau, 0, 3).removeO()
    Fs = sp.series(s * sp.sqrt(sp.expand(Us) / s ** 2), tau, 0, 3).removeO()
    f1 = sp.simplify(Fs.coeff(tau, 1))
    f2 = sp.simplify(Fs.coeff(tau, 2))
    ok_series = zero(res) and zero(f1 - s * c ** 2) and sp.simplify(over_s_in_x(f2) - (3 - 10 * x + 7 * x ** 2) / 2) == 0
    # the length: F_k = u_k/(2F) = c0/sqrt(1 - 2 tau c0^2); F_k(0) = 1/sqrt(1 - 2 tau) = 1/l  =>  tau = (1 - l^2)/2
    R = sp.sqrt(s0 ** 2 + L ** 2 * c0 ** 2)
    tl = (1 - L ** 2) / 2
    Fk = sp.sin(2 * k0) / (2 * sp.sqrt(U))
    ok_len = zero((1 - 2 * tau * c0 ** 2).subs(tau, tl) - R ** 2) and zero(U.subs(tau, tl) - (s0 * R) ** 2) and zero(kk.subs(tau, tl) - (k0 + (L ** 2 - 1) / 2 * sp.sin(2 * k0)))
    fk_formula = c0 / R
    ok_fk = all(zero((Fk.subs(tau, tl) - fk_formula).subs(k0, pt)) for pt in (sp.pi / 3, sp.pi / 4, sp.pi / 6)) and sp.simplify(fk_formula.subs(k0, 0) - 1 / L) == 0
    # species corners: k0 -> k0 + pi sends k -> k + pi and F -> -F; the speed at the corner is -1/l
    Fl = s0 * R
    kl = k0 + (L ** 2 - 1) / 2 * sp.sin(2 * k0)
    ok_sp = zero(Fl.subs(k0, k0 + sp.pi) + Fl) and zero(kl.subs(k0, k0 + sp.pi) - kl - sp.pi) and sp.simplify(fk_formula.subs(k0, sp.pi) + 1 / L) == 0
    # the classical form: with M = 2k and Ecc = 2k0, M = Ecc - (1 - l^2) sin Ecc and u_k = sin Ecc
    ok_kep = zero(2 * kl - (2 * k0 - (1 - L ** 2) * sp.sin(2 * k0)))
    checks.check("C1", ok_char, "characteristics of u_tau = u_k^2/2 from u = sin^2 k: k = k0 - tau sin 2k0, u = sin^2 k0 - tau sin^2 2k0/2; then u_k = sin 2k0 and u_tau = u_k^2/2 exactly")
    checks.check("C2", ok_series, "at fixed k the flow is F = s + tau s c^2 + tau^2 s(3 - 10 s^2 + 7 s^4)/2 + O(tau^3): block 69's first order and block 182 T4(b)'s second order")
    checks.check("C3", ok_len and ok_fk, "measured by the long-wave speed F_k(0) = 1/l: tau = (1 - l^2)/2, k = k0 + ((l^2 - 1)/2) sin 2k0, F = sin k0 sqrt(sin^2 k0 + l^2 cos^2 k0), F_k = cos k0/sqrt(sin^2 k0 + l^2 cos^2 k0)")
    checks.check("C4", ok_sp and ok_kep, "the species corners are kept: k0 -> k0 + pi gives k -> k + pi and F -> -F, speed -1/l there; with M = 2k, Ecc = 2k0 the relation is M = Ecc - (1 - l^2) sin Ecc, and u_k = sin Ecc")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    R2 = s0 ** 2 + L ** 2 * c0 ** 2
    Fk2 = c0 ** 2 / R2
    gap = 1 - L ** 2 * Fk2
    want = s0 ** 2 / R2
    if mut("speed_forged"):
        want = s0 ** 2 / (s0 ** 2 + c0 ** 2)
    ok_axis = zero(gap - want)
    # three dimensions: l^2 |v|^2 = sum F_j^2 (l^2 F_j'^2) / sum F_j^2 <= max_j l^2 F_j'^2 <= 1
    a1, a2, a3, w1, w2, w3 = sp.symbols("a1:4 w1:4", nonnegative=True)
    lhs = 1 - (a1 * (1 - w1) + a2 * (1 - w2) + a3 * (1 - w3)) / (a1 + a2 + a3)
    ok_3d = sp.simplify(lhs - (a1 * w1 + a2 * w2 + a3 * w3) / (a1 + a2 + a3)) == 0
    # fold-free: dk/dk0 = 1 + (l^2 - 1) cos 2k0 has minimum min(l^2, 2 - l^2) over real k0
    dk = sp.diff(k0 + (L ** 2 - 1) / 2 * sp.sin(2 * k0), k0)
    ok_dk = zero(dk - (1 + (L ** 2 - 1) * sp.cos(2 * k0))) and zero(dk.subs(k0, 0) - L ** 2) and zero(dk.subs(k0, sp.pi / 2) - (2 - L ** 2))
    # monotone on the half zone: F_k = c0/R >= 0 for |k0| <= pi/2 and F(pi/2) = 1: F = sin(psi(k)), psi a monotone bijection
    ok_rel = zero((s0 * sp.sqrt(R2)).subs(k0, sp.pi / 2) - 1)
    # comparison: the linear completion outruns near k = 0 iff l > 7/6; the fixed-generator flow iff l^2 > 3/2; this family never
    q = sp.Symbol("q", real=True)
    near0 = sp.expand(sp.series(sp.sqrt((1 - x) * (1 - 3 * q * x) ** 2).subs(x, sp.sin(k) ** 2), k, 0, 4).removeO())
    thr = sp.solve(sp.Eq(near0.coeff(k, 2), 0), q)
    y = sp.Symbol("y", positive=True)
    logd = sp.diff(sp.log(sp.sqrt(1 - x)) - sp.Rational(3, 2) * sp.log(y - (y - 1) * x), x).subs(x, 0)
    thr_fix = sp.solve(sp.Eq(sp.simplify(logd), 0), y)
    t_ = sp.Symbol("t", positive=True)
    self_speed = sp.simplify((L ** 2 * Fk2).subs({s0: t_ / sp.sqrt(1 + t_ ** 2), c0: 1 / sp.sqrt(1 + t_ ** 2)}))
    ok_self = sp.simplify(self_speed - L ** 2 / (L ** 2 + t_ ** 2)) == 0
    checks.check("D1", ok_axis and ok_3d, "the speed bound: 1 - l^2 F_k^2 = sin^2 k0/(sin^2 k0 + l^2 cos^2 k0) >= 0, zero only at the species points; in three dimensions 1 - l^2|v|^2 = sum F_j^2 (1 - l^2 F_j'^2)/sum F_j^2 >= 0, zero only at E = 0")
    checks.check("D2", ok_dk and ok_rel, "dk/dk0 = 1 + (l^2 - 1) cos 2k0, equal to l^2 at k0 = 0 and 2 - l^2 at k0 = pi/2: positive for every real k0 iff 0 < l^2 < 2, so the characteristic map is a diffeomorphism of the zone and F = sin(psi(k)) with psi monotone (a relabelling of the free walk)")
    checks.check("D3", thr == [-sp.Rational(1, 6)] and thr_fix == [sp.Rational(3, 2)] and ok_self, f"comparison: near k = 0 the linear completion outruns w/l iff q < {thr[0]} (l > 7/6; blocks 173, 176), the fixed-generator flow iff l^2 > {thr_fix[0]} (block 182 T4(a)); this family's l^2 F_k^2 = l^2/(l^2 + tan^2 k0) never exceeds 1")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    R = sp.sqrt(s0 ** 2 + L ** 2 * c0 ** 2)
    Fk = c0 / R
    dk = 1 + (L ** 2 - 1) * sp.cos(2 * k0)
    Fkk_top = sp.simplify((sp.diff(Fk, k0) / dk).subs(k0, sp.pi / 2))
    want = -1 / (2 - L ** 2)
    if mut("fold_forged"):
        want = -1 / (3 - L ** 2)
    ok_curv = sp.simplify(Fkk_top - want) == 0
    # at l^2 = 2, k0 = pi/2 + d: k - pi/2 = d - sin(2d)/2 = (2/3) d^3 + ..., 1 - u = sin^4 d, 1 - F = d^4/2 + ...
    d = sp.Symbol("d", real=True)
    kd = sp.series(d - sp.sin(2 * d) / 2, d, 0, 6).removeO()
    uu = sp.cos(sp.pi / 2 + d) ** 2
    one_minus_u = sp.simplify(1 - sp.sin(sp.pi / 2 + d) ** 2 * (sp.sin(sp.pi / 2 + d) ** 2 + 2 * uu))
    oneF = sp.series(1 - sp.sqrt(1 - sp.sin(d) ** 4), d, 0, 7).removeO()
    ok_top = sp.expand(kd.coeff(d, 3)) == sp.Rational(2, 3) and kd.coeff(d, 1) == 0 and zero(one_minus_u - sp.sin(d) ** 4) and sp.expand(oneF.coeff(d, 4)) == sp.Rational(1, 2)
    # beyond: l^2 = 3, g(d) = d - sin 2d: g'(0) = -1 < 0, g(pi/4) = pi/4 - 1 < 0, g(pi/2) = pi/2 > 0 -> a root d* in (pi/4, pi/2), sin 2d* > 0
    g = d - sp.sin(2 * d)
    ok_beyond = sp.diff(g, d).subs(d, 0) == -1 and bool(g.subs(d, sp.pi / 4) < 0) and bool(g.subs(d, sp.pi / 2) > 0)
    lg = sp.Symbol("lg", positive=True)
    gl = d - (lg - 1) / 2 * sp.sin(2 * d)
    ok_gen = sp.simplify(sp.diff(gl, d).subs(d, 0) - (2 - lg)) == 0 and sp.simplify(gl.subs(d, sp.pi / 2) - sp.pi / 2) == 0
    checks.check("E1", ok_curv, "the band-top curvature F_kk(pi/2) = -1/(2 - l^2): unbounded as l^2 -> 2, so no twice-differentiable member of the family reaches l = sqrt 2")
    checks.check("E2", ok_top, "at l^2 = 2, with k0 = pi/2 + d: k - pi/2 = (2/3) d^3 + O(d^5) and 1 - F = d^4/2 + O(d^6), so 1 - F = (1/2)(3|k - pi/2|/2)^(4/3) to leading order: the band top is a cusp of order 4/3")
    checks.check("E3", ok_beyond and ok_gen, "for l^2 > 2, g(d) = d - ((l^2 - 1)/2) sin 2d has g'(0) = 2 - l^2 < 0 and g(pi/2) = pi/2 > 0: characteristics from d = 0 and d = +-d* (0 < d* < pi/2) meet at k = pi/2 with slopes u_k = 0 and -+sin 2d* != 0 (at l^2 = 3, d* lies in (pi/4, pi/2)): no continuously differentiable u there")


# ============================================================================================ family F (T5)
def family_f(checks: Checks) -> None:
    dk = 1 + (L ** 2 - 1) * sp.cos(2 * k0)
    ukk = sp.simplify(sp.diff(sp.sin(2 * k0), k0) / dk)
    want = 2 * sp.cos(2 * k0) / (1 + (L ** 2 - 1) * sp.cos(2 * k0))
    ok_form = sp.simplify(ukk - want) == 0
    # the pole: cos 2k0 = -1/(l^2 - 1); numerator 2 cos 2k0 = -2/(l^2 - 1) != 0. Two exact instances.
    oks = []
    for l2, kstar in ((sp.Rational(3, 2), sp.pi / 2 + sp.I * sp.acosh(2) / 2), (sp.Rational(1, 2), sp.I * sp.acosh(2) / 2)):
        cos2 = sp.simplify(sp.expand_complex(sp.cos(2 * kstar)))
        den = sp.simplify(1 + (l2 - 1) * cos2)
        num = sp.simplify(2 * cos2)
        if mut("pole_forged"):
            den = den + 1
        oks.append(den == 0 and num != 0 and sp.im(kstar) != 0)
    # at l = 1 the same expression is 2 cos 2k0: entire (the argument does not apply)
    ok_free = sp.simplify(want.subs(L, 1) - 2 * sp.cos(2 * k0)) == 0
    checks.check("F1", ok_form, "along characteristics u_kk = d(sin 2k0)/dk = 2 cos 2k0/(1 + (l^2 - 1) cos 2k0)")
    checks.check("F2", all(oks) and ok_free, "for l^2 = 3/2 (k0 = pi/2 + i arccosh(2)/2) and l^2 = 1/2 (k0 = i arccosh(2)/2) the denominator vanishes and the numerator is -4 or 4: a pole off the real line; in general at cos 2k0 = -1/(l^2 - 1) with numerator -2/(l^2 - 1) != 0 whenever l != 1; at l = 1 the expression is entire. If F had finite reach, u = F^2 would be a trigonometric polynomial and u_kk(k(k0)) entire in k0: so F has infinite reach at every l != 1")


# ============================================================================================ family I (T7)
def family_i(checks: Checks) -> None:
    I_ = sp.I
    p1 = sp.Matrix([[0, 1], [1, 0]])
    p2 = sp.Matrix([[0, -I_], [I_, 0]])
    p3 = sp.Matrix([[1, 0], [0, -1]])
    X = [sp.kronecker_product(p3, pm) for pm in (p1, p2, p3)]
    Gm = sp.kronecker_product(p1, sp.eye(2))
    Fk = sp.symbols("F1:4")
    Fq = sp.symbols("G1:4")
    W = sp.symbols("W1:4")
    mu, V = sp.symbols("mu V")

    def books(offset):
        h = sum((Fk[a_] * X[a_] for a_ in range(3)), sp.zeros(4)) + mu * Gm + offset * sp.eye(4)
        hp = sum((Fq[a_] * X[a_] for a_ in range(3)), sp.zeros(4)) + mu * Gm + offset * sp.eye(4)
        DF = [(Fk[a_] - Fq[a_]) / W[a_] for a_ in range(3)]
        Du = [(Fk[a_] ** 2 - Fq[a_] ** 2) / W[a_] for a_ in range(3)]
        A = [I_ / 2 * DF[a_] * X[a_] for a_ in range(3)]
        f = [I_ * Du[a_] for a_ in range(3)]
        if mut("pair_books_forged"):
            f = [I_ / 2 * Du[a_] for a_ in range(3)]
        P = [(f[j] / 2 * sp.eye(4) + hp * A[j] + A[j] * h) / 2 for j in range(3)]
        K = [[(A[a_] * f[j] + A[j] * f[a_]) / 2 for j in range(3)] for a_ in range(3)]
        e = (h + hp) / 2
        ok_e = sp.simplify(sum((W[j] * P[j] for j in range(3)), sp.zeros(4)) - I_ * (e * h - hp * e)) == sp.zeros(4)
        ok_p = all(sp.simplify(sum((W[a_] * K[a_][j] for a_ in range(3)), sp.zeros(4)) - I_ * (P[j] * h - hp * P[j])) == sp.zeros(4) for j in range(3))
        ok_s = all(sp.simplify(K[a_][j] - K[j][a_]) == sp.zeros(4) for a_ in range(3) for j in range(3))
        return ok_e and ok_p and ok_s

    ok_gen = books(0)
    ok_off = not books(V)
    # single waves: the divided difference (G(k) - G(k - t))/(1 - e^{-it}) -> -i G'(k); then A -> F' X/2, f -> 2 F F'
    t_ = sp.Symbol("t")
    Gf = sp.Function("G")
    lim = sp.series((Gf(k) - Gf(k - t_)) / (1 - sp.exp(-I_ * t_)), t_, 0, 1).removeO().doit()
    ok_lim = sp.simplify(lim + I_ * sp.diff(Gf(k), k)) == 0
    Fs = sp.symbols("f1:4")
    Fd = sp.symbols("g1:4")
    h0 = sum((Fs[a_] * X[a_] for a_ in range(3)), sp.zeros(4)) + mu * Gm
    ok_anti = all(sp.simplify(h0 * X[j] + X[j] * h0 - 2 * Fs[j] * sp.eye(4)) == sp.zeros(4) for j in range(3))
    A0 = [Fd[a_] / 2 * X[a_] for a_ in range(3)]
    f0 = [2 * Fs[a_] * Fd[a_] for a_ in range(3)]
    P0 = [(f0[j] / 2 * sp.eye(4) + h0 * A0[j] + A0[j] * h0) / 2 for j in range(3)]
    ok_p0 = all(sp.simplify(P0[j] - Fs[j] * Fd[j] * sp.eye(4)) == sp.zeros(4) for j in range(3))
    K0 = (A0[0] * f0[1] + A0[1] * f0[0]) / 2
    ok_k0 = sp.simplify(K0 - Fd[0] * Fd[1] * (Fs[1] * X[0] + Fs[0] * X[1]) / 2) == sp.zeros(4)
    # the free walk: D[sin] = (e^{ik} + e^{-ik'})/(2i) and D[sin^2] = sin(k + k')(1 + e^{iq})/(2i), block 181's objects
    z, zp = sp.symbols("z zp", nonzero=True)
    sn = lambda w: (w - 1 / w) / (2 * I_)
    Dsin = (sn(z) - sn(zp)) / (1 - zp / z)
    Dsin2 = (sn(z) ** 2 - sn(zp) ** 2) / (1 - zp / z)
    ok_free = sp.simplify(Dsin - (z + 1 / zp) / (2 * I_)) == 0 and sp.simplify(Dsin2 - sn(z * zp) * (1 + z / zp) / (2 * I_)) == 0
    checks.check("I1", ok_gen and ok_off, "for h = sum_a F_a X_a + mu Gamma (X_a, Gamma anticommuting involutions; F_a arbitrary on both waves of the pair), A_a = (i/2) D_a[F_a] X_a and f_a = i D_a[F_a^2] give sum_j w_j P^s_j = i(e h - h' e) and sum_a w_a K^s_aj = i(P^s_j h - h' P^s_j) with K^s symmetric, exactly; with a constant offset V the same construction fails (block 139 T3)")
    checks.check("I2", ok_lim and ok_anti and ok_p0 and ok_k0, "single waves: the divided difference tends to -i times the derivative, so A_a -> F_a' X_a/2 and f_a -> 2 F_a F_a'; with {h, X_j} = 2 F_j, P^s_j(k, k) = F_j F_j' (the energy current E v_j) and K^s_aj(k, k) = F_a' F_j'(F_j X_a + F_a X_j)/2, whose expectation on a wave is E v_a v_j")
    checks.check("I3", ok_free, "for the free walk the divided differences are block 181's objects: D[sin] = (e^{ik} + e^{-ik'})/(2i) and D[sin^2] = sin(k + k')(1 + e^{iq})/(2i)")


# ============================================================================================ family G
FENCES = (
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
    "nothing is adopted and no gravitational claim is made.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at l = sqrt 2."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Kepler) —", 1)
    norm = normalize_text(text)
    checks.check("G1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("G2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("G3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
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
    checks.check("G4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family H
N5_LINES = (
    "per_element: executed - the single-wave lemma; the books condition for a per-axis walk; the two failing witnesses; the energy current and the strain variable",
    "per_site: executed - the characteristic solution and its first two orders at fixed k",
    "per_mode: executed - the speed bound per axis and in three dimensions; the fold-free range; the comparison thresholds; the pair-level books for arbitrary per-axis hops (symbolic)",
    "per_block: executed - the band-top curvature, the cusp at l^2 = 2, the crossing beyond; the complex pole at two exact stretches",
    "lattice_wide: checked and not executed - the pole at every l != 1 (closed form in the text); exponential decay of the hops (standard); anisotropic stretches; the position-space placement of the divided differences for infinite reach",
)


def family_h(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("H1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    family_f(checks)
    family_i(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: under block 69's two-step coupling, a uniform stretch acting as a relabelling keeps single-wave symmetric books at every stretch iff it is the self-consistent flow; measured by the long-wave speed it is a smooth relabelling for 0 < l^2 < 2, never outruns the long waves, has infinite reach at every l != 1, and cannot continue smoothly to l = sqrt 2; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
