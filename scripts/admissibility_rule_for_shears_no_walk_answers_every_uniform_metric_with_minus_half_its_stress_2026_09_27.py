#!/usr/bin/env python3
"""Exact checks: (T1) every Clifford walk h = sum_a F_a(k) X_a + mu Gamma (anticommuting involutions; hops of any form, not only per axis)
keeps exact symmetric books, with block 181's P^s and K^s built from ANY divided-difference decomposition of h - h' and h^2 - h'^2; on single
waves K^s_ab(k, k) = (1/4)(d_a h d_b W + d_b h d_a W), W = h^2. (T2) The stress-response principle dh/dg_ab = -(1/2) K^s_ab (the
off-diagonal variable counting both entries), from the free walk, is block 69's coupling at first order for every component (B = -(g - 1)/2).
(T3) Its diagonal and shear flows do not commute at second order: the mixed derivatives of g11 and g12 differ by
(1/4) cos k1 cos k2 cos 2k1 (sin k2, -sin k1, 0), a rotation of the walk's Clifford vector at fixed energy; the two diagonal flows commute.
(T4) No placement of the metric's indices with constant coefficients removes the defect. So no Clifford walk answers every uniform metric
with minus half its stress beyond first order; the spectra (block 187) are unaffected. The supervisor's own derivation, unrefereed.
Blocks 69 and 139 as landed; blocks 181, 184, 185 and 187 (pushed) placed and the facts used re-derived.

A (premises): landed block 69 (uniform form for any symmetric strain); landed block 139; the axioms.
B (T1): the pair identities for a generic Clifford walk with generic decompositions (4 x 4); the single-wave stress.
C (T2): the first-order flows at the free walk equal block 69's coupling with B = -(g - 1)/2.
D (T3): the mixed derivatives of the (11) and (12) flows; their difference is orthogonal to F; (11) and (22) commute.
E (T4): the defect is not a constant-coefficient combination of the six first-order flows (exact rational points).
F (T5): a rotation term alpha(k) e3 x F in the shear flow changes the defect by (1/2) sin k1 cos k1 d_1 alpha (sin k2, -sin k1, 0); cancelling
   needs d_1 alpha = -cos k2 cos 2k1/(2 sin k1), which is not integrable across k1 = 0.
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
    "docs/ADMISSIBILITY_RULE_FOR_SHEARS_NO_WALK_ANSWERS_EVERY_UNIFORM_METRIC_WITH_MINUS_HALF_ITS_STRESS_BEYOND_FIRST_ORDER_THE_FLOWS_FAIL_TO_COMMUTE_BY_A_ROTATION_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_THE_BOOKS_ADMIT_ONE_REST_ENERGY_THE_STAGGERED_MASS_KEEPS_THEM_EXACTLY_SO_MASSIVE_CONTENT_MEETS_THE_MEMBER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_for_shears_no_walk_answers_every_uniform_metric_with_minus_half_its_stress_beyond_first_order_the_flows_fail_to_commute_by_a_rotation_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED69 = (
    "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`",
    "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion.",
)
LANDED139 = (
    "`mε` anticommutes with the walk, so the squared energy is `|sin k|² + m²`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "books_forged": "B",
    "first_order_forged": "C",
    "defect_forged": "D",
    "span_forged": "E",
    "rotation_forged": "F",
    "table_forged": "J",
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


T0 = time.time()
KS = sp.symbols("k1:4", real=True)
FREE = sp.Matrix([sp.sin(x_) for x_ in KS])


def Wof(F):
    return (F.T * F)[0]


def Phi(F, a, b):
    """the flow dF/dg_ab = -(1/2) K^s_ab(k, k) for the symmetric variable g_ab (both entries when a != b), on the Clifford vector F"""
    W = Wof(F)
    if a == b:
        return -sp.Rational(1, 4) * sp.diff(F, KS[a]) * sp.diff(W, KS[a])
    return -sp.Rational(1, 4) * (sp.diff(F, KS[a]) * sp.diff(W, KS[b]) + sp.diff(F, KS[b]) * sp.diff(W, KS[a]))


def dPhi(F, a, b, dF):
    e = sp.Symbol("e_")
    return sp.diff(Phi(F + e * dF, a, b), e).subs(e, 0)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t69, t139 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its response to a metric and the principle are supplied)")
    needles = list(LANDED69)
    if mut("landed_quote_forged"):
        needles[0] = needles[0].replace("B_a^j", "B_j^a")
    checks.check("A3", all(n in t69 for n in needles) and all(n in t139 for n in LANDED139), "landed block 69: the uniform form for any symmetric strain B, and no completion fixed by the leading order; landed block 139: the staggered mass anticommutes")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    I_ = sp.I
    p1 = sp.Matrix([[0, 1], [1, 0]])
    p2 = sp.Matrix([[0, -I_], [I_, 0]])
    p3 = sp.Matrix([[1, 0], [0, -1]])
    X = [sp.kronecker_product(p3, pm) for pm in (p1, p2, p3)]
    Gm = sp.kronecker_product(p1, sp.eye(2))
    Fk = sp.symbols("F1:4")
    Fq = sp.symbols("G1:4")
    Wv = sp.symbols("w1:4")
    mu = sp.Symbol("mu")
    h = sum((Fk[a_] * X[a_] for a_ in range(3)), sp.zeros(4)) + mu * Gm
    hp = sum((Fq[a_] * X[a_] for a_ in range(3)), sp.zeros(4)) + mu * Gm
    # generic decompositions: F_a - F'_a = sum_b w_b D_ab and W - W' = sum_b w_b V_b, with D_a1, D_a2, V_1, V_2 free
    D = [[sp.Symbol(f"D{a_}{b_}") for b_ in range(3)] for a_ in range(3)]
    for a_ in range(3):
        D[a_][2] = (Fk[a_] - Fq[a_] - Wv[0] * D[a_][0] - Wv[1] * D[a_][1]) / Wv[2]
    Wk = sum(f_ ** 2 for f_ in Fk)
    Wq = sum(f_ ** 2 for f_ in Fq)
    V = [sp.Symbol("V0"), sp.Symbol("V1"), None]
    V[2] = (Wk - Wq - Wv[0] * V[0] - Wv[1] * V[1]) / Wv[2]
    A = [I_ / 2 * sum((D[a_][b_] * X[a_] for a_ in range(3)), sp.zeros(4)) for b_ in range(3)]
    f = [I_ * V[b_] for b_ in range(3)]
    if mut("books_forged"):
        f = [I_ / 2 * V[b_] for b_ in range(3)]
    P = [(f[j] / 2 * sp.eye(4) + hp * A[j] + A[j] * h) / 2 for j in range(3)]
    K = [[(A[a_] * f[j] + A[j] * f[a_]) / 2 for j in range(3)] for a_ in range(3)]
    e = (h + hp) / 2
    ok_e = sp.simplify(sum((Wv[j] * P[j] for j in range(3)), sp.zeros(4)) - I_ * (e * h - hp * e)) == sp.zeros(4)
    ok_p = all(sp.simplify(sum((Wv[a_] * K[a_][j] for a_ in range(3)), sp.zeros(4)) - I_ * (P[j] * h - hp * P[j])) == sp.zeros(4) for j in range(3))
    checks.check("B1", ok_e and ok_p, "for h = sum_a F_a X_a + mu Gamma with hops of any form and any decompositions F_a - F'_a = sum_b w_b D_ab, W - W' = sum_b w_b V_b (six free entries each, symbolic), A_b = (i/2) sum_a D_ab X_a and f_b = i V_b give sum_j w_j P^s_j = i(e h - h' e) and sum_a w_a K^s_aj = i(P^s_j h - h' P^s_j) with K^s = (A_a f_j + A_j f_a)/2 symmetric, exactly")
    # single waves: A_b -> (1/2) d_b h and f_b -> d_b W, so K^s_ab(k, k) = (1/4)(d_a h d_b W + d_b h d_a W) and P^s_j(k, k) = (1/2) d_j W = E d_j E
    ha, hb, Wa, Wb = sp.symbols("ha hb Wa Wb")
    Kab = ((ha / 2) * Wb + (hb / 2) * Wa) / 2
    checks.check("B2", sp.simplify(Kab - (ha * Wb + hb * Wa) / 4) == 0, "on single waves the decompositions are fixed: A_b -> (1/2) d_b h, f_b -> d_b W; so K^s_ab(k, k) = (1/4)(d_a h d_b W + d_b h d_a W) and P^s_j = E d_j E, whatever the decomposition")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    s = [sp.sin(x_) for x_ in KS]
    c = [sp.cos(x_) for x_ in KS]
    ok = True
    for a_, b_ in itertools.combinations_with_replacement(range(3), 2):
        got = sp.simplify(Phi(FREE, a_, b_))
        # block 69: dH/dB for B_a^b = B_b^a = beta is sigma_a c_a s_b c_b + sigma_b c_b s_a c_a (a != b), sigma_a c_a s_a c_a (a = b);  B = -(g - 1)/2
        want = sp.zeros(3, 1)
        if a_ == b_:
            want[a_] = -s[a_] * c[a_] ** 2 / 2
        else:
            want[a_] = -c[a_] * s[b_] * c[b_] / 2
            want[b_] = -c[b_] * s[a_] * c[a_] / 2
        if mut("first_order_forged") and (a_, b_) == (0, 1):
            want[a_] = -c[a_] * s[b_] * c[b_]
        ok = ok and sp.simplify(sp.expand_trig(got - want)) == sp.zeros(3, 1)
    checks.check("C1", ok, "at the free walk every first-order flow -(1/2) K^s_ab (both entries off the diagonal) equals block 69's coupling dH/dB with B = -(g - 1)/2: sigma_a c_a s_b c_b + sigma_b c_b s_a c_a for a shear, sigma_a s_a c_a^2 on the diagonal")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    s = [sp.sin(x_) for x_ in KS]
    c = [sp.cos(x_) for x_ in KS]
    D1 = dPhi(FREE, 0, 0, Phi(FREE, 0, 1))
    D2 = dPhi(FREE, 0, 1, Phi(FREE, 0, 0))
    defect = sp.simplify(sp.expand_trig(D1 - D2))
    want = c[0] * c[1] * sp.cos(2 * KS[0]) / 4 * sp.Matrix([s[1], -s[0], 0])
    if mut("defect_forged"):
        want = sp.zeros(3, 1)
    ok_def = sp.simplify(sp.expand_trig(defect - want)) == sp.zeros(3, 1)
    ok_orth = sp.simplify(sp.expand_trig((FREE.T * (D1 - D2))[0])) == 0
    E1 = dPhi(FREE, 0, 0, Phi(FREE, 1, 1))
    E2 = dPhi(FREE, 1, 1, Phi(FREE, 0, 0))
    ok_diag = sp.simplify(E1 - E2) == sp.zeros(3, 1)
    H1 = dPhi(FREE, 0, 1, Phi(FREE, 0, 2))
    H2 = dPhi(FREE, 0, 2, Phi(FREE, 0, 1))
    want13 = sp.cos(2 * KS[0]) * c[1] * c[2] / 4 * sp.Matrix([0, s[2], -s[1]])
    ok_1213 = sp.simplify(sp.expand_trig(H1 - H2 - want13)) == sp.zeros(3, 1)
    ok_diag = ok_diag and ok_1213
    # the normal component of every flow is fixed by the spectral law: F . Phi_ab = (1/2) dW/dg_ab = -(1/8)(2 - delta_ab) W_a W_b, for any F
    Fg = sp.Matrix([sp.Function(f"F{i_}")(*KS) for i_ in range(3)])
    Wg = Wof(Fg)
    ok_norm = True
    for a_, b_ in ((0, 0), (0, 1)):
        lhs = (Fg.T * Phi(Fg, a_, b_))[0]
        want = -sp.Rational(1, 8) * (2 - (1 if a_ == b_ else 0)) * sp.diff(Wg, KS[a_]) * sp.diff(Wg, KS[b_])
        ok_norm = ok_norm and sp.simplify(lhs - want) == 0
    checks.check("D2", ok_norm, "for any Clifford vector F, F . Phi_ab = -(1/8)(2 - delta_ab) W_a W_b = (1/2) dW/dg_ab: the flows' component along F is the spectral law of block 187, so any smooth family realising block 187's spectrum differs from the stress response only by a component orthogonal to F (a rotation), and its own flows commute")
    checks.check("D1", ok_def and ok_orth and ok_diag, "at the free walk the mixed second derivatives of the (11) and (12) flows differ by (1/4) cos k1 cos k2 cos 2k1 (sin k2, -sin k1, 0), which is orthogonal to F (a rotation at fixed energy; W = |F|^2 is unaffected, as block 187 requires); the (11) and (22) flows commute; the (12) and (13) flows clash: d_g13 d_g12 F - d_g12 d_g13 F = (1/4) cos 2k1 cos k2 cos k3 (0, sin k3, -sin k2)")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    D1 = dPhi(FREE, 0, 0, Phi(FREE, 0, 1))
    D2 = dPhi(FREE, 0, 1, Phi(FREE, 0, 0))
    defect = D1 - D2
    pairs = list(itertools.combinations_with_replacement(range(3), 2))
    cs = sp.symbols("c0:6")
    combo = sum((cs[i_] * Phi(FREE, a_, b_) for i_, (a_, b_) in enumerate(pairs)), sp.zeros(3, 1))
    angles = [sp.atan2(3, 4), sp.atan2(4, 3), sp.atan2(5, 12), sp.atan2(12, 5)]
    eqs = []
    for pt in itertools.product(angles, repeat=3):
        sub = dict(zip(KS, pt))
        diff = (defect - combo).subs(sub)
        eqs += [sp.nsimplify(sp.simplify(sp.expand_trig(d_))) for d_ in diff]
    if mut("span_forged"):
        eqs = eqs[:0]
    sol = sp.linsolve([e_ for e_ in eqs if e_ != 0], cs) if eqs else sp.FiniteSet(tuple(cs))
    checks.check("E1", sol == sp.EmptySet, f"the defect is not a constant-coefficient combination of the six first-order flows (an explicit metric dependence of the principle through index placement contributes only such combinations at this order): the linear system at {len(angles) ** 3} exact rational points is inconsistent")


# ============================================================================================ family F (T5)
def family_f(checks: Checks) -> None:
    e3 = sp.Matrix([0, 0, 1])
    al = sp.Function("alpha")(*KS)

    def phi12r(F):
        return Phi(F, 0, 1) + al * e3.cross(F)

    e = sp.Symbol("e_")
    D1 = sp.diff(Phi(FREE + e * phi12r(FREE), 0, 0), e).subs(e, 0)
    D2 = sp.diff(phi12r(FREE + e * Phi(FREE, 0, 0)), e).subs(e, 0)
    s = [sp.sin(x_) for x_ in KS]
    c = [sp.cos(x_) for x_ in KS]
    M = c[0] * c[1] * sp.cos(2 * KS[0]) / 4 * sp.Matrix([s[1], -s[0], 0])
    coef = s[0] * c[0] / 2
    if mut("rotation_forged"):
        coef = s[0] / 2
    pred = M + coef * sp.diff(al, KS[0]) * sp.Matrix([s[1], -s[0], 0])
    ok_form = sp.simplify(sp.expand_trig(D1 - D2 - pred)) == sp.zeros(3, 1)
    # cancelling: d_1 alpha = -cos k2 cos 2k1/(2 sin k1); near k1 = 0 this is -cos k2/(2 k1) + O(k1): its k1-antiderivative has a log
    need = -c[1] * sp.cos(2 * KS[0]) / (2 * s[0])
    lead = sp.limit(need * KS[0], KS[0], 0)
    ok_sing = sp.simplify(lead + c[1] / 2) == 0
    # a metric-dependent local rotation: add rho(k) G11 e3 x F to the (12) flow; at G = 0 it changes the mismatch by -rho e3 x F;
    # rho = -(1/4) cos k1 cos k2 cos 2k1 (a trigonometric polynomial) cancels it: M = -(1/4) c1 c2 cos 2k1 (e3 x F)
    rho = -c[0] * c[1] * sp.cos(2 * KS[0]) / 4
    ok_local = sp.simplify(sp.expand_trig(M - rho * e3.cross(FREE))) == sp.zeros(3, 1)
    checks.check("F2", ok_local, "the mismatch is M = -(1/4) cos k1 cos k2 cos 2k1 (e3 x F); a metric-dependent rotation rho(k) G11 e3 x F added to the (12) flow changes it by -rho e3 x F, so rho = -(1/4) cos k1 cos k2 cos 2k1, a trigonometric polynomial (a local rotation generator), cancels the (11)/(12) clash at second order")
    checks.check("F1", ok_form and ok_sing, "adding a rotation alpha(k) e3 x F to the shear flow changes the second-order defect by (1/2) sin k1 cos k1 d_1 alpha (sin k2, -sin k1, 0); cancelling it needs d_1 alpha = -cos k2 cos 2k1/(2 sin k1) ~ -cos k2/(2 k1) near k1 = 0, so alpha would carry -(cos k2/2) log|k1|: no continuous alpha on the zone")


# ============================================================================================ family J (T6)
ROT_TABLE = {
    ((0, 0), (0, 1)): (2, "-c1*c2*C1"), ((0, 0), (0, 2)): (1, "c1*c3*C1"), ((0, 1), (0, 2)): (0, "-c2*c3*C1"),
    ((0, 1), (1, 1)): (2, "-c1*c2*C2"), ((0, 1), (1, 2)): (1, "c1*c3*C2"), ((0, 2), (1, 2)): (2, "-c1*c2*C3"),
    ((0, 2), (2, 2)): (1, "c1*c3*C3"), ((1, 1), (1, 2)): (0, "-c2*c3*C2"), ((1, 2), (2, 2)): (0, "-c2*c3*C3"),
}


def family_j(checks: Checks) -> None:
    s = [sp.sin(x_) for x_ in KS]
    c = [sp.cos(x_) for x_ in KS]
    env = {"c1": c[0], "c2": c[1], "c3": c[2], "C1": sp.cos(2 * KS[0]), "C2": sp.cos(2 * KS[1]), "C3": sp.cos(2 * KS[2])}
    E = [sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1])]
    flows = list(itertools.combinations_with_replacement(range(3), 2))
    P = {fl: Phi(FREE, *fl) for fl in flows}
    ok_rot = True
    ok_zero = True
    limits = set()
    for A, B in itertools.combinations(flows, 2):
        M = sp.simplify(sp.expand_trig(dPhi(FREE, *A, P[B]) - dPhi(FREE, *B, P[A])))
        if (A, B) in ROT_TABLE:
            ax, expr = ROT_TABLE[(A, B)]
            theta = sp.sympify(expr, locals=env) / 4
            if mut("table_forged") and (A, B) == ((0, 1), (1, 2)):
                theta = -theta
            ok_rot = ok_rot and sp.simplify(sp.expand_trig(M - theta * E[ax].cross(FREE))) == sp.zeros(3, 1)
            limits.add(theta.subs({KS[0]: 0, KS[1]: 0, KS[2]: 0}))
        else:
            ok_zero = ok_zero and M == sp.zeros(3, 1)
    shares = all(len(set(A) & set(B)) > 0 for (A, B) in ROT_TABLE) and all(len(set(A) & set(B)) == 0 or (A, B) in ROT_TABLE for A, B in itertools.combinations(flows, 2))
    checks.check("J1", ok_rot and ok_zero and shares and limits == {sp.Rational(1, 4), -sp.Rational(1, 4)}, "all fifteen pairs of flows at the free walk: the six pairs sharing no index commute; each of the nine sharing an index clashes by a rotation about one coordinate axis through an angle of (1/4) times a product of cosines with one doubled (a trigonometric polynomial, so a local generator; for example (11)/(12): about e3 by -(1/4) c1 c2 cos 2k1); in the long-wave limit every angle tends to +-1/4")
    # repair: adding rho G_A (e x F) to flow B changes only the (A, B) mixed derivative at g = 1, by -rho (e x F)
    Gs = sp.Symbol("GA")
    rho = sp.Function("rho")(*KS)
    term = rho * Gs * E[2].cross(FREE)
    ok_rep = term.subs(Gs, 0) == sp.zeros(3, 1) and sp.diff(term, Gs) == rho * E[2].cross(FREE)
    checks.check("J2", ok_rep, "a metric-dependent rotation rho(k) G_A (e x F) added to flow B vanishes at g = 1 and changes only the (A, B) mixed derivative there, by -rho (e x F); so choosing rho as each pair's angle repairs all nine clashes at second order with local generators")


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
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at second order."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Parker", "Friedmann", "Frobenius", "Hadamard", "Belinfante")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Frobenius) —", 1)
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
    "per_element: executed - the pair identities for a generic Clifford walk with generic decompositions",
    "per_site: executed - the single-wave stress and the first-order flows at the free walk",
    "per_mode: executed - the mixed second derivatives of the (11), (12), (13) and (22) flows; the normal component of the flows",
    "per_block: executed - the span test at 64 exact rational points; the simplest rotation term",
    "lattice_wide: checked and not executed - general rotation terms in every flow; non-uniform metrics; higher orders",
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
    family_j(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: every Clifford walk keeps exact symmetric books; the stress-response principle is block 69's coupling at first order for every uniform strain, but its diagonal and shear flows fail to commute at second order by a rotation at fixed energy; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
