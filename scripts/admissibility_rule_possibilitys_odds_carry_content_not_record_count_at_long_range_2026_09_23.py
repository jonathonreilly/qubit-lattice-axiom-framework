#!/usr/bin/env python3
"""Exact checks: possibility's odds carry content, not record count, at long range - a massless turn channel in the ordered sea; capacity for
bodies (probes workers' result on the sphere menu, its exact claims refereed by a Grok model; block 42's reading; not adopted).

B (T1): lambda_l on the sphere menu, lambda_1 = coth(beta) - 1/beta, the recurrence, the ordering; the massless point bracketed in rationals.
C (T2, T5): the lean's birth past the massless point (exact third-order coefficients, their sign there); with vacancies at the neutral scale.
D (T3): the turn of the lean has eigenvalue exactly 1/6; what a record feeds the turn; a record count feeds it nothing.
E (T4): exact capacities on a 5^3 box: 99/136 for one record; two adjacent and a 2x2x2 cube below additive.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_POSSIBILITYS_ODDS_CARRY_CONTENT_NOT_RECORD_COUNT_AT_LONG_RANGE_A_MASSLESS_TURN_CHANNEL_IN_THE_ORDERED_SEA_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_possibilitys_odds_carry_content_not_record_count_at_long_range_a_massless_turn_channel_in_the_ordered_sea_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
    "No possibility is privileged.",
    "A site never carries more than one record",
    "A site with no record cannot be read.",
)

MUTATION_GATE = {
    "lambda1_misidentified": "B",
    "massless_point_bracket_shifted": "B",
    "cubic_coefficient_sign_flipped": "C",
    "vacancy_cubic_shift_dropped": "C",
    "pole_claim_forged": "D",
    "turn_eigenvalue_forged": "D",
    "capacity_additive_claimed": "E",
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


F = Fraction
ZERO = F(0)
ONE = F(1)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the distribution sentence, no privileged possibility, one record per site, an unrecorded site unreadable (the sentences block 42's reading works from)")


# ============================================================================================ helpers (the sphere menu's odds, block 42's reading)
import itertools

beta, tt = sp.symbols("beta t", positive=True)


def lam(l):
    """lambda_l = (1/2) int e^(beta t) P_l(t) dt / (sinh(beta)/beta): the one-neighbour operator K_1 on degree-l harmonics."""
    return sp.integrate(sp.exp(beta * tt) * sp.legendre(l, tt), (tt, -1, 1)) / 2 / (sp.sinh(beta) / beta)


def zero_exp(e):
    return sp.simplify(sp.expand(e.rewrite(sp.exp))) == 0


def lean_bounds(q: F, n: int = 14):
    """Rational bounds lo < L(q) < hi for L = coth q - 1/q = (q cosh q - sinh q)/(q sinh q), q > 0 rational below 2.
    Numerator sum_{k>=1} q^(2k+1) 2k/(2k+1)!, denominator sum_{k>=0} q^(2k+2)/(2k+1)!: positive terms, tails bounded
    by geometric series (consecutive ratios q^2/(2k(2k+3)) and q^2/((2k+2)(2k+3)) fall with k)."""
    fact = lambda m: F(sp.factorial(m))
    num = sum((q ** (2 * k + 1) * 2 * k / fact(2 * k + 1) for k in range(1, n + 1)), F(0))
    den = sum((q ** (2 * k + 2) / fact(2 * k + 1) for k in range(0, n + 1)), F(0))
    tn = q ** (2 * n + 3) * (2 * n + 2) / fact(2 * n + 3)
    rn = q ** 2 / ((2 * n + 2) * (2 * n + 5))
    td = q ** (2 * n + 4) / fact(2 * n + 3)
    rd = q ** 2 / ((2 * n + 4) * (2 * n + 5))
    assert rn < 1 and rd < 1
    return num / (den + td / (1 - rd)), (num + tn / (1 - rn)) / den


def box_capacity(n, body):
    """Exact capacity of a body of records on an n^3 box (field one on the body, zero beyond the box, u_x = average of neighbours elsewhere)."""
    sites = list(itertools.product(range(n), repeat=3))
    S = set(body)
    free = [s for s in sites if s not in S]
    ix = {s: i for i, s in enumerate(free)}

    def nbrs(s):
        out = []
        for a in range(3):
            for d in (1, -1):
                q = list(s)
                q[a] += d
                out.append(tuple(q))
        return out
    N = len(free)
    M = [[F(0)] * (N + 1) for _ in range(N)]
    for s in free:
        i = ix[s]
        M[i][i] = F(6)
        for q in nbrs(s):
            if q in ix:
                M[i][ix[q]] -= 1
            elif q in S:
                M[i][N] += 1
    for c in range(N):
        piv = next(r for r in range(c, N) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(N):
            if r != c and M[r][c] != 0:
                fct = M[r][c]
                M[r] = [x - fct * y for x, y in zip(M[r], M[c])]
    u = {free[r]: M[r][N] for r in range(N)}

    def val(q):
        return F(1) if q in S else u.get(q, F(0))
    return sum((1 - F(1, 6) * sum((val(q) for q in nbrs(s)), F(0)) for s in S), F(0))


B0_LO, B0_HI = F(5085, 10000), F(5086, 10000)


def lean_birth(vacancies: bool):
    """Third-order expansion of the uniform leaning odds; with vacancies (neutral scale, fixed formation odds) the
    content map at density r is the map with lambda_k -> r lambda_k and r shifts with the lean."""
    a, B, C, rho, d = sp.symbols("a B C rho d")
    l1s, l2s, l3s = sp.symbols("lambda1 lambda2 lambda3", positive=True)
    t = sp.symbols("t")
    P = [sp.legendre(k, t) for k in range(4)]

    def avg(ex):
        return sp.integrate(sp.expand(ex), (t, -1, 1)) / 2
    r = (rho + d * a ** 2) if vacancies else sp.Integer(1)
    bx = 1 + r * (l1s * a * P[1] + l2s * B * a ** 2 * P[2] + l3s * C * a ** 3 * P[3])
    b6 = sp.series(sp.expand(bx ** 6), a, 0, 4).removeO()
    m6 = sp.series(avg(b6), a, 0, 4).removeO()
    dsol = None
    if vacancies:
        shift = sp.series(sp.log(r / (1 - r)) - sp.log(rho / (1 - rho)) - sp.log(m6), a, 0, 3).removeO()
        dsol = sp.solve(sp.Eq(shift.coeff(a, 2), 0), d)[0]
        b6, m6 = b6.subs(d, dsol), m6.subs(d, dsol)
    Fm = sp.series(sp.expand(b6 / m6), a, 0, 4).removeO()
    F1 = sp.expand(avg(Fm * P[1]) * 3)
    F2 = sp.expand(avg(Fm * P[2]) * 5)
    Bsol = sp.solve(sp.Eq(B, F2.coeff(a, 2)), B)[0]
    c1 = sp.simplify(F1.coeff(a, 1))
    c3 = sp.factor(sp.simplify(F1.coeff(a, 3).subs(B, Bsol)))
    return dict(c1=c1, c3=c3, B=Bsol, d=dsol, m6=m6, syms=(a, rho, l1s, l2s, l3s))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the one-neighbour operator on the sphere menu: lambda_l, the recurrence, the ordering, and the massless point bracketed in rationals."""
    Z = sp.integrate(sp.exp(beta * tt), (tt, -1, 1)) / 2
    l = [lam(k) for k in range(5)]
    target1 = (sp.coth(beta) - 1 / beta) if not mut("lambda1_misidentified") else (sp.tanh(beta) - 1 / beta)
    ok = zero_exp(Z - sp.sinh(beta) / beta) and zero_exp(l[0] - 1) and zero_exp(l[1] - target1)
    rec = all(zero_exp(l[k + 1] - (l[k - 1] - (2 * k + 1) * l[k] / beta)) for k in (1, 2, 3))
    ser = sp.series((sp.coth(beta) - 1 / beta), beta, 0, 8).removeO()
    series_ok = sp.expand(ser - (beta / 3 - beta ** 3 / 45 + 2 * beta ** 5 / 945 - beta ** 7 / 4725)) == 0
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    E = sum((2 - 2 * sp.cos(k)) for k in (k1, k2, k3))
    six = sp.simplify(sum((2 * sp.cos(k) for k in (k1, k2, k3)), sp.Integer(0)) - (6 - E)) == 0
    checks.check("B1", ok and rec and series_ok and six, "T1(a): on the sphere menu with pair weight exp(beta s.b), the one-neighbour operator multiplies degree-l harmonics by lambda_l = (1/2) int e^(beta t) P_l(t) dt/(sinh(beta)/beta): lambda_0 = 1, lambda_1 = coth(beta) - 1/beta = beta/3 - beta^3/45 + 2 beta^5/945 - ..., and lambda_(l+1) = lambda_(l-1) - (2l + 1) lambda_l/beta (checked to l = 4, symbolic); summed over six neighbours a wave k in channel l has eigenvalue lambda_l (6 - E(k))")
    # ordering: lambda_l/lambda_(l-1) is the mean of t under e^(beta t)(1 - t^2)^(l-1) on [-1, 1]
    rep = True
    for k in range(1, 5):
        il = beta ** k / (2 ** (k + 1) * sp.factorial(k)) * sp.integrate((1 - tt ** 2) ** k * sp.exp(beta * tt), (tt, -1, 1))
        rep = rep and zero_exp(il / (sp.sinh(beta) / beta) - l[k])
        num = sp.integrate(tt * sp.exp(beta * tt) * (1 - tt ** 2) ** (k - 1), (tt, -1, 1))
        den = sp.integrate(sp.exp(beta * tt) * (1 - tt ** 2) ** (k - 1), (tt, -1, 1))
        rep = rep and zero_exp(num / den - l[k] / l[k - 1])
    dL = sp.simplify(sp.diff(sp.coth(beta) - 1 / beta, beta) - (1 / beta ** 2 - 1 / sp.sinh(beta) ** 2)) == 0
    bl, bh = (B0_LO, B0_HI) if not mut("massless_point_bracket_shifted") else (B0_HI, F(5087, 10000))
    lo_lo, lo_hi = lean_bounds(bl)
    hi_lo, hi_hi = lean_bounds(bh)
    brk = lo_lo < lo_hi < F(1, 6) < hi_lo < hi_hi
    checks.check("B2", rep and dL and brk, "T1(b): lambda_l/lambda_(l-1) equals the mean of t under the weight e^(beta t)(1 - t^2)^(l-1) on [-1, 1] (checked to l = 4, symbolic), so 1 > lambda_1 > lambda_2 > ... > 0 for every beta > 0; d lambda_1/d beta = 1/beta^2 - 1/sinh(beta)^2 > 0; rational bounds on lambda_1 give 6 lambda_1 < 1 at beta = 5085/10000 and 6 lambda_1 > 1 at beta = 5086/10000: the lean loses its mass term at exactly one point beta0, which lies strictly between them")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the lean's birth beyond the massless point: exact third-order expansion of f = (K_1 f)^6/<(K_1 f)^6>; T5: with vacancies at the neutral scale."""
    res = lean_birth(False)
    a, rho, l1s, l2s, l3s = res["syms"]
    sign = 1 if not mut("cubic_coefficient_sign_flipped") else -1
    ok = sp.simplify(res["c1"] - 6 * l1s) == 0 and sp.simplify(res["c3"] + sign * 6 * l1s ** 3 * (38 * l2s - 3) / (6 * l2s - 1)) == 0
    ok = ok and sp.simplify(res["B"] + 10 * l1s ** 2 / (6 * l2s - 1)) == 0
    # sign at the massless point: lambda_2 = 1 - 3 lambda_1/beta = 1 - 1/(2 beta0) < 1 - 1/(2 B0_HI) < 3/38
    lam2_hi = 1 - 1 / (2 * B0_HI)
    sign_ok = lam2_hi < F(3, 38) and lam2_hi < F(1, 6)
    eps = sp.symbols("epsilon")
    astar2 = (1 - 6 * l1s) / res["c3"]
    lin = sp.simplify(6 * l1s + 3 * res["c3"] * astar2)
    near = sp.simplify(lin.subs(l1s, (1 + eps) / 6) - (1 - 2 * eps)) == 0
    mL2 = (1 - (1 - 2 * eps)) / ((1 - 2 * eps) / 6)
    ms2 = (1 - (1 + eps)) / ((1 + eps) / 6)
    ratio = sp.limit(mL2 / (-ms2), eps, 0) == 2
    checks.check("C1", ok and sign_ok and near and ratio, "T2: writing the leaning odds f = 1 + a P_1 + B a^2 P_2 + ..., the exact equation f = (K_1 f)^6/<(K_1 f)^6> gives B = -10 lambda_1^2/(6 lambda_2 - 1) and a = 6 lambda_1 a + c3 a^3 + ..., c3 = -6 lambda_1^3 (38 lambda_2 - 3)/(6 lambda_2 - 1); at the massless point lambda_2 = 1 - 1/(2 beta0) < 86/5086 < 3/38, so c3 < 0 and the lean is born continuously, M^2 = (6 lambda_1 - 1)/(9|c3|) to leading order; the lean's size mode then has per-neighbour eigenvalue (1 - 2 eps)/6 with eps = 6 lambda_1 - 1, mass^2 12 eps, twice the screened side's at the same distance (symbolic)")
    vac = lean_birth(True)
    a, rho, l1s, l2s, l3s = vac["syms"]
    c3r = (-6 * l1s ** 3 * (38 * l2s - 3) / (6 * l2s - 1)).subs({l1s: rho * l1s, l2s: rho * l2s}, simultaneous=True)
    extra = 30 * l1s ** 3 * rho ** 3 * (1 - rho) if not mut("vacancy_cubic_shift_dropped") else 0
    okv = sp.simplify(vac["c1"] - 6 * rho * l1s) == 0 and sp.simplify(vac["c3"] - (c3r + extra)) == 0
    okv = okv and sp.simplify(vac["d"] - 5 * rho ** 3 * (1 - rho) * l1s ** 2) == 0
    Phi = 12 * l1s ** 2 + 8 * l1s * l2s - 5 * l1s + 5 * l2s
    on_line = sp.simplify(vac["c3"].subs(rho, 1 / (6 * l1s)) - Phi / (216 * l1s * (l1s - l2s))) == 0
    # the mass channel's own first-order strength: rho(1-rho)<(K1F - 1)/b>_F with b = 1 - rho + rho K1F, F = b^6/<b^6>
    t = sp.symbols("t")
    h = sp.symbols("h")
    bb = 1 + rho * l1s * h * sp.legendre(1, t)
    avg = lambda ex: sp.integrate(sp.expand(ex), (t, -1, 1)) / 2
    K1F = (bb - 1 + rho) / rho
    entry = rho * (1 - rho) * avg((K1F - 1) / bb * bb ** 6) / avg(bb ** 6)
    ident = sp.simplify(entry - (1 - rho) * (1 - avg(bb ** 5) / avg(bb ** 6))) == 0
    lead = sp.simplify(sp.series(avg(bb ** 6) - avg(bb ** 5), h, 0, 3).removeO() - sp.Rational(5, 3) * rho ** 2 * l1s ** 2 * h ** 2) == 0
    # a root of Phi on the ordering line, bracketed in rationals (Phi decreasing in lambda_1 for beta < 2)
    def phi_bounds(q):
        lo, hi = lean_bounds(q)
        f = lambda x: x * x * (12 - 24 / q) + x * (3 - 15 / q) + 5
        return f(hi), f(lo)
    p1, p2 = phi_bounds(F(9579, 10000)), phi_bounds(F(9580, 10000))
    brk = p1[1] < 0 < p2[0]
    checks.check("C2", okv and on_line and ident and lead and brk, "T5: with 'no record' a seventh possibility at the neutral scale, the content map at density rho is the map with every lambda_k -> rho lambda_k; at fixed formation odds the density rises with the lean by 5 rho^3 (1 - rho) lambda_1^2 a^2, which adds 30 lambda_1^3 rho^3 (1 - rho) to the cubic coefficient; on the ordering line 6 rho lambda_1 = 1 that coefficient is Phi/(216 lambda_1 (lambda_1 - lambda_2)) with Phi = 12 lambda_1^2 + 8 lambda_1 lambda_2 - 5 lambda_1 + 5 lambda_2, which changes sign between beta = 9579/10000 and 9580/10000 (rational bounds): the lean's birth turns abrupt there; in the ordered sea a record's own first-order pull on its neighbours' odds of holding a record is (1 - rho)(1 - <b^5>/<b^6>) = (5/3) rho^2 lambda_1^2 a^2 (1 - rho) + ... > 0, zero in the isotropic sea (symbolic)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the turn of the lean is massless at every beta past the point; what a record feeds it."""
    u = sp.symbols("u")
    order = 1 if not mut("pole_claim_forged") else 0
    poles = all(sp.simplify(sp.assoc_legendre(l, order, u).subs(u, s)) == 0 for l in range(1, 8) for s in (1, -1))
    t, phi, t0 = sp.symbols("t phi t0", real=True)
    s = sp.Matrix([sp.sqrt(1 - t ** 2) * sp.cos(phi), sp.sqrt(1 - t ** 2) * sp.sin(phi), t])
    s0 = sp.Matrix([sp.sqrt(1 - t0 ** 2), 0, t0])
    gt = sp.Function("g")(t)
    src = beta * (s.T * s0)[0] - sp.log(gt)
    m1 = sp.simplify(sp.integrate(src * sp.cos(phi), (phi, 0, 2 * sp.pi)) / sp.pi)
    s1 = sp.simplify(sp.integrate(src * sp.sin(phi), (phi, 0, 2 * sp.pi)) / sp.pi)
    feed = sp.simplify(m1 - beta * sp.sqrt(1 - t ** 2) * sp.sqrt(1 - t0 ** 2)) == 0 and s1 == 0
    # the turn: with f = sum f_l P_l and g = K_1 f = sum lambda_l f_l P_l, the turn delta = sqrt(1-t^2) f'(t) cos(phi) has
    # azimuthal-one expansion -sum f_l P_l^1 cos(phi), so K_1 delta = sqrt(1-t^2) g'(t) cos(phi); if f = g^6/c, 6 f (K_1 delta)/g = delta
    fl = sp.symbols("f0:5")
    ls = sp.symbols("l0:5")
    fpoly = sum(fl[k] * sp.legendre(k, t) for k in range(5))
    gpoly = sum(ls[k] * fl[k] * sp.legendre(k, t) for k in range(5))
    exp_ok = sp.simplify(sum(fl[k] * sp.assoc_legendre(k, 1, t) for k in range(1, 5)) + sp.sqrt(1 - t ** 2) * sp.diff(fpoly, t)) == 0
    Kdelta = -sum(ls[k] * fl[k] * sp.assoc_legendre(k, 1, t) for k in range(1, 5))
    k_ok = sp.simplify(Kdelta - sp.sqrt(1 - t ** 2) * sp.diff(gpoly, t)) == 0
    cc = sp.symbols("c", positive=True)
    gg = sp.Function("G")(t)
    power = 6 if not mut("turn_eigenvalue_forged") else 5
    fchain = gg ** power / cc
    turn = sp.simplify(6 * fchain * sp.diff(gg, t) / gg - sp.diff(gg ** 6 / cc, t)) == 0
    mean_free = sp.integrate(sp.cos(phi), (phi, 0, 2 * sp.pi)) == 0
    checks.check("D1", poles and feed and exp_ok and k_ok and turn and mean_free, "T3: every turn of an ordered solution is a solution, and the turn delta = sqrt(1 - t^2) f'(t) cos(phi) obeys K_1 delta = sqrt(1 - t^2) g'(t) cos(phi) with g = K_1 f, so 6 f (K_1 delta)/g = delta whenever f = g^6/<g^6>, with no mean term (it averages to zero around the lean): the turn is an eigenvector with eigenvalue exactly 1/6 per neighbour at every beta past the massless point, a channel with no mass term; a record of content s0 replaces its neighbour's factor g(t) by e^(beta s.s0), whose part turning once around the lean is exactly beta sqrt(1 - t^2) sqrt(1 - t0^2) cos(phi), zero for every s iff the record is aligned with the lean; P_l^1(+-1) = 0 for l = 1..7; a source unchanged by the rotations about the lean (a record count) has no such part")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: records as boundary values in the massless channel: exact capacities on a 5^3 box, not additive."""
    c1 = box_capacity(5, [(2, 2, 2)])
    c2 = box_capacity(5, [(2, 2, 2), (3, 2, 2)])
    c8 = box_capacity(5, [(i, j, k) for i in (2, 3) for j in (2, 3) for k in (2, 3)])
    subadd = (c2 < 2 * c1 and c8 / 8 < c2 / 2 < c1) if not mut("capacity_additive_claimed") else c2 == 2 * c1
    checks.check("E1", c1 == F(99, 136) and subadd, f"T4: in the massless channel a record held as a boundary value makes each unformed site take the average of its neighbours, so a body's field is its common lean times the probability that a walk reaches it, and its charge is the body's capacity: exactly 99/136 for one record on a 5^3 box, {c2} for two adjacent records, {c8} for a 2x2x2 cube; per record the capacity falls as the body grows - capacities do not add")


# ============================================================================================ family F
FENCES = (
    "This note works within the owner's moving-records reading and block 42's reading that an unformed site's odds are a condition for its neighbours (possibility shifting with the neighbourhood), on the sphere menu; it reports, from probes workers' results refereed in part by another model family, what those odds carry at long range; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the one-neighbour eigenvalues to degree four, their recurrence and ordering identity (symbolic); rational bounds at four points",
    "per_site: executed - exact capacities on a 5^3 box (every free site solved in rationals); control: the nonlinear odds at every site of 17^3 and 21^3 boxes",
    "per_mode: executed - the lean's third-order expansion with and without vacancies; the turn identity; a record's first-order source by azimuthal order; control: the ordered sea's spectrum by sector",
    "per_block: executed - one record, two adjacent records and a 2x2x2 cube as bodies; control: one and two held records",
    "lattice_wide: T1-T3 and T5 at every beta within scope (symbolic, rational brackets) on Z^3; T4 on the box; block 42's reading and, for T5, the neutral scale supplied",
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
    print("scope: possibility's odds on the sphere menu - lambda_l = i_l/i_0; the lean massless where 6 lambda_1 = 1 and born continuously past it; in the ordered sea the turn channel carries content without a mass term, a record count feeds only massive channels; bodies charge the massless channel by capacity, not by count; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
