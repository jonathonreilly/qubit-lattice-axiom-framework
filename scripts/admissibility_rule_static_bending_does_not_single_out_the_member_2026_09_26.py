#!/usr/bin/env python3
"""Exact checks: static bending does not single out the member (a harvest of probe #9202, confirmed by an other-family
referee in #9294). Within block 60's weight-one static completions F = -K int e^u [A(lam) grad u.grad lam + C(lam)|grad lam|^2
+ D(lam)|grad u|^2] with block 60 T3's second-order jet, at long wavelength around a spherical body:

A (premises): the landed notes carry the curvature member, its index and the second-order jet; the completion's field
   equations are harmonic at first order and reproduce the curvature member's exact exterior (block 110 T1) at orders 2, 3.
B (the turn): the ray invariant gives the turn 2 nu1/b + pi(nu2 + nu1^2/2)/b^2 + (4 nu1^3/3 + 8 nu1 nu2 + 4 nu3)/b^3; the
   comparator's index (1 + M/2r)^3/(1 - M/2r) has nu = (2M, 7M^2/4, M^3) and turn (4M, 15 pi M^2/4, 128 M^3/3).
C (T1, the plane): nu2/M^2 = -2(2A1 - C1 + D1 s^2 - 4 D1 s - 2 s^2 - s - 2)/(1 + s)^2; at s = 1 the comparator's 7/4 holds
   iff 4A1 - 2C1 - 6D1 = 3; the curvature member is on the plane, constant coefficients give 5/2; at third order the
   comparator's value is one linear condition on the fourth-order jet, slopes (-1/3, 1/6, 1/2); a body at rest, general beta.
D (T2, bilinear members; T3, the clauses): X = w f(l), Y = g(l) with f'(1) = 1/2; the index equals the comparator's at every
   order iff l f = ((1 + g)/2)^3; five g's; power laws Y = l^gamma give (17 - 6 gamma)/8, the comparator's only at gamma = 1/2;
   capture of the comparator's index at r n = 3 sqrt3 M; the ledger's wall term is A(0) L1, blind to the third-order jet.
Exact arithmetic (sympy); the probe's floating-point radial integrations are not used. The runner scans its own source for
floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_STATIC_BENDING_DOES_NOT_SINGLE_OUT_THE_MEMBER_A_PLANE_OF_JETS_BENDS_LIKE_THE_COMPARATOR_AND_BILINEAR_MEMBERS_MATCH_ITS_INDEX_AT_EVERY_ORDER_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_AROUND_A_BODY_THE_WALKS_RAYS_MATCH_THE_COMPARATORS_AT_EVERY_ORDER_EXACTLY_WHEN_ITS_TWO_CHARGES_AGREE_AND_THEY_AGREE_ONLY_WHEN_HOP_ENERGY_BALANCES_THE_SLOWED_CLOCKS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_static_bending_does_not_single_out_the_member_a_plane_of_jets_bends_like_the_comparator_and_bilinear_members_match_its_index_at_every_order_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    (2, "there is no term in `u` alone"),
    (3, "n = χ³/N = (r + a)³/(r²(r − p))"),
    (3, "`F = −8K Σ_bonds (N_y − N_x)(χ_y − χ_x)`"),
)

MUTATION_GATE = {
    "curvature_member_jet_forged": "A",
    "turn_moment_forged": "B",
    "plane_constant_forged": "C",
    "matching_power_forged": "D",
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

# ============================================================================================ the completion's exterior (probe #9202's machinery, ported)
r, eps = sp.symbols("r epsilon", positive=True)
A1, A2, C1, C2, D1, D2, beta = sp.symbols("A1 A2 C1 C2 D1 D2 beta")
L1, U1, l2, u2, l3, u3, M, sig = sp.symbols("L1 U1 l2 u2 l3 u3 M sigma")
RES: dict = {}


def exterior():
    """Field equations of r^2 e^u [A(lam) u' lam' + C(lam) lam'^2 + D(lam) u'^2] with A = 1 + A1 x + A2 x^2/2,
    C = 1/(2 beta) + C1 x + C2 x^2/2, D = D1 x + D2 x^2/2, solved order by order in 1/r; the index n = l/w = e^(lam - u)."""
    Af = lambda y: 1 + A1 * y + A2 * y ** 2 / 2
    Cf = lambda y: 1 / (2 * beta) + C1 * y + C2 * y ** 2 / 2
    Df = lambda y: D1 * y + D2 * y ** 2 / 2
    u = sp.Function("u")(r)
    lam = sp.Function("lam")(r)
    Lag = r ** 2 * sp.exp(u) * (Af(lam) * u.diff(r) * lam.diff(r) + Cf(lam) * lam.diff(r) ** 2 + Df(lam) * u.diff(r) ** 2)
    EL = [sp.diff(Lag, f) - sp.diff(sp.diff(Lag, f.diff(r)), r) for f in (u, lam)]
    ua = eps * U1 / r + eps ** 2 * u2 / r ** 2 + eps ** 3 * u3 / r ** 3
    la = eps * L1 / r + eps ** 2 * l2 / r ** 2 + eps ** 3 * l3 / r ** 3
    res = []
    for e in EL:
        ex = e.subs({u.diff(r, 2): ua.diff(r, 2), lam.diff(r, 2): la.diff(r, 2)})
        ex = ex.subs({u.diff(r): ua.diff(r), lam.diff(r): la.diff(r)}).subs({u: ua, lam: la})
        res.append(sp.expand(sp.series(sp.expand(ex), eps, 0, 4).removeO()))
    o1 = [sp.simplify(e.coeff(eps, 1)) for e in res]
    s2 = sp.solve([sp.expand(e.coeff(eps, 2) * r ** 4) for e in res], [u2, l2], dict=True)[0]
    s3 = sp.solve([sp.expand((e.coeff(eps, 3) * r ** 5).subs(s2)) for e in res], [u3, l3], dict=True)[0]
    n = sp.series(sp.exp(la - ua), eps, 0, 4).removeO()
    nu1 = sp.expand(n.coeff(eps, 1) * r)
    nu2 = sp.expand((n.coeff(eps, 2) * r ** 2).subs(s2))
    nu3 = sp.expand((n.coeff(eps, 3) * r ** 3).subs(s2).subs(s3))
    return o1, s2, s3, nu1, nu2, nu3


def ensure_exterior():
    if not RES:
        o1, s2, s3, nu1, nu2, nu3 = exterior()
        RES.update(o1=o1, s2=s2, s3=s3, nu1=nu1, nu2=nu2, nu3=nu3)


CM = {A1: 1, A2: 1, C1: sp.Rational(1, 2), C2: sp.Rational(1, 2), D1: 0, D2: 0}     # the curvature member's jets


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the completions and the comparator are supplied)")
    ok_landed = all(needle in texts[i] for i, needle in LANDED_NEEDLES)
    ensure_exterior()
    s2, s3, nu2 = RES["s2"], RES["s3"], RES["nu2"]
    a, p = sp.symbols("a p", positive=True)
    cm = dict(CM)
    cm[beta] = 1
    if mut("curvature_member_jet_forged"):
        cm[C1] = sp.Rational(1, 4)
    lam_ex = sp.series(2 * sp.log(1 + eps * a / r), eps, 0, 4).removeO()
    u_ex = sp.series(sp.log(1 - eps * p / r) - sp.log(1 + eps * a / r), eps, 0, 4).removeO()
    chg = {L1: 2 * a, U1: -(a + p)}
    ok_cm = all(sp.simplify(e) == 0 for e in (
        s2[l2].subs(cm).subs(chg) - sp.expand(lam_ex).coeff(eps, 2) * r ** 2,
        s2[u2].subs(cm).subs(chg) - sp.expand(u_ex).coeff(eps, 2) * r ** 2,
        s3[l3].subs(cm).subs(chg) - sp.expand(lam_ex).coeff(eps, 3) * r ** 3,
        s3[u3].subs(cm).subs(chg) - sp.expand(u_ex).coeff(eps, 3) * r ** 3,
        nu2.subs(cm).subs(chg) - (3 * a ** 2 + 3 * a * p + p ** 2)))
    checks.check("A3", ok_landed and all(v == 0 for v in RES["o1"]) and ok_cm, "landed blocks 60 and 110 carry the second-order jet (no term in u alone), the curvature member and the index chi^3/N; the completion's field equations are harmonic at first order and reproduce the curvature member's exact exterior chi = 1 + a/r, N = 1 - p/r at orders 2 and 3, with nu2 = 3a^2 + 3ap + p^2")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    n1, n2, n3, z, a1, a2, a3 = sp.symbols("nu1 nu2 nu3 z a1 a2 a3")
    rr = (1 + a1 * z + a2 * z ** 2 + a3 * z ** 3) / z                   # r as a function of rho = r n(r), z = 1/rho
    eq = sp.expand(sp.series(rr * (1 + n1 / rr + n2 / rr ** 2 + n3 / rr ** 3) * z - 1, z, 0, 4).removeO())
    sol = sp.solve([eq.coeff(z, k) for k in (1, 2, 3)], [a1, a2, a3], dict=True)[0]
    rr = rr.subs(sol)
    lnn = sp.expand(sp.series(sp.log(1 + n1 / rr + n2 / rr ** 2 + n3 / rr ** 3), z, 0, 4).removeO())
    t = sp.symbols("t", positive=True)
    Ik = [sp.integrate(1 / (t ** (k + 1) * sp.sqrt(t ** 2 - 1)), (t, 1, sp.oo)) for k in (1, 2, 3)]
    if mut("turn_moment_forged"):
        Ik[1] = sp.pi / 2
    alpha = [sp.simplify(2 * k * lnn.coeff(z, k) * Ik[k - 1]) for k in (1, 2, 3)]
    ok_turn = (alpha[0] == 2 * n1 and sp.simplify(alpha[1] - sp.pi * (n2 + n1 ** 2 / 2)) == 0
               and sp.simplify(alpha[2] - (sp.Rational(4, 3) * n1 ** 3 + 8 * n1 * n2 + 4 * n3)) == 0)
    sch = {n1: 2 * M, n2: sp.Rational(7, 4) * M ** 2, n3: M ** 3}
    comp = [sp.simplify(x.subs(sch)) for x in alpha]
    idx = sp.series(((1 + M / (2 * r)) ** 3 / (1 - M / (2 * r))).subs(r, 1 / eps), eps, 0, 4).removeO()
    ok_idx = [sp.expand(idx).coeff(eps, k) for k in (1, 2, 3)] == [2 * M, sp.Rational(7, 4) * M ** 2, M ** 3]
    checks.check("B1", ok_turn and ok_idx and comp == [4 * M, sp.Rational(15, 4) * sp.pi * M ** 2, sp.Rational(128, 3) * M ** 3],
                 "with rho = r n(r) kept along a ray, the turn is 2 nu1/b + pi(nu2 + nu1^2/2)/b^2 + (4 nu1^3/3 + 8 nu1 nu2 + 4 nu3)/b^3 (moments 1, pi/4, 2/3); the comparator's index (1 + M/2r)^3/(1 - M/2r) has nu = (2M, 7M^2/4, M^3) and turn (4M, 15 pi M^2/4, 128 M^3/3)")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    ensure_exterior()
    nu1, nu2, nu3 = RES["nu1"], RES["nu2"], RES["nu3"]
    sub = {beta: 1, U1: -sig * L1}
    Ls = sp.solve(sp.Eq(nu1.subs(sub), 2 * M), L1)[0]
    n2 = sp.simplify(nu2.subs(sub).subs(L1, Ls) / M ** 2)
    n3 = sp.simplify(nu3.subs(sub).subs(L1, Ls) / M ** 3)
    claim2 = -2 * (2 * A1 - C1 + D1 * sig ** 2 - 4 * D1 * sig - 2 * sig ** 2 - sig - 2) / (1 + sig) ** 2
    k_plane = 2 if mut("plane_constant_forged") else 3
    ok2 = sp.simplify(n2 - claim2) == 0
    plane = sp.simplify(n2.subs(sig, 1) - sp.Rational(7, 4) - (-(4 * A1 - 2 * C1 - 6 * D1 - k_plane) / 4)) == 0
    const = sp.simplify(n2.subs(sig, 1).subs({A1: 0, C1: 0, D1: 0}))
    on_plane = sp.simplify(n2.subs(sig, 1).subs(CM)) == sp.Rational(7, 4)
    checks.check("C1", ok2 and plane and on_plane and const == sp.Rational(5, 2), "nu2/M^2 = -2(2A1 - C1 + D1 s^2 - 4 D1 s - 2 s^2 - s - 2)/(1 + s)^2 (s = sigma, beta = 1); at s = 1 it equals the comparator's 7/4 iff 4A1 - 2C1 - 6D1 = 3; the curvature member (1, 1/2, 0) is on the plane; constant coefficients give 5/2")
    third = sp.expand(n3.subs(sig, 1))
    lin4 = [sp.diff(third, v) for v in (A2, C2, D2)]
    ok3 = lin4 == [-sp.Rational(1, 3), sp.Rational(1, 6), sp.Rational(1, 2)] and sp.simplify(third.subs(CM)) == 1
    n2b = sp.simplify(nu2.subs(U1, -L1 / beta).subs(L1, sp.solve(sp.Eq(nu1.subs(U1, -L1 / beta), 2 * M), L1)[0]) / M ** 2)
    claimb = -(2 * A1 * beta ** 2 + 2 * A1 * beta - 2 * C1 * beta ** 2 - 4 * D1 * beta - 2 * D1 - 2 * beta ** 2 - 5 * beta - 3) / (beta + 1) ** 2
    checks.check("C2", ok3 and sp.simplify(n2b - claimb) == 0, "at s = 1, nu3/M^3 is linear in the fourth-order jet with slopes (-1/3, 1/6, 1/2), so the comparator's 128/3 is one further linear condition, met by the curvature member; for a body at rest at general beta (sigma = 1/beta): nu2/M^2 = -(2A1 beta^2 + 2A1 beta - 2C1 beta^2 - 4D1 beta - 2D1 - 2 beta^2 - 5 beta - 3)/(beta + 1)^2")
    RES.update(n2=n2, n3=third)


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    x, lam = sp.symbols("x lam", positive=True)
    s_ = sp.symbols("s")
    ok_s = sp.solve(s_ * (1 - s_), s_) == [0, 1]
    f, g = sp.Function("f"), sp.Function("g")
    Aexpr = f(x) * sp.diff(g(x), x) * x
    Cexpr = sp.diff(g(x), x) * x ** 2 * sp.diff(f(x), x)
    ratio = sp.simplify((Cexpr / Aexpr).subs(x, 1).subs(f(1), 1))
    ok_jet = sp.simplify(ratio - sp.Subs(sp.diff(f(x), x), x, 1).doit()) == 0
    rr, Mm = sp.symbols("r M", positive=True)
    Y = 1 + Mm / rr
    X = 1 - Mm / (2 * rr)
    power = 2 if mut("matching_power_forged") else 3
    ok_match = sp.simplify(((1 + Y) / 2) ** power / X - (1 + Mm / (2 * rr)) ** 3 / (1 - Mm / (2 * rr))) == 0
    qq, pp = sp.symbols("q p", positive=True)
    ok_sigma = sp.solve(sp.Eq((pp + qq / 2) / qq, 1), pp) == [qq / 2]
    if "n2" not in RES:
        family_c(Checks())
    n2, n3 = RES["n2"], RES["n3"]
    okg = True
    gs = [2 * sp.sqrt(x) - 1, x, 1 + sp.log(x), 1 + (x ** 3 - 1) / 3, (3 - 1 / x ** 2) / 2]
    for gx in gs:
        okg &= gx.subs(x, 1) == 1 and sp.simplify(sp.diff(gx, x).subs(x, 1)) == 1
        fx = ((1 + gx) / 2) ** power / x
        Ae = sp.series((fx * sp.diff(gx, x) * x).subs(x, sp.exp(lam)), lam, 0, 3).removeO()
        Ce = sp.series((sp.diff(gx, x) * x ** 2 * sp.diff(fx, x)).subs(x, sp.exp(lam)), lam, 0, 3).removeO()
        jets = {A1: Ae.coeff(lam, 1) / Ae.coeff(lam, 0), A2: 2 * Ae.coeff(lam, 2) / Ae.coeff(lam, 0),
                C1: Ce.coeff(lam, 1) / Ae.coeff(lam, 0), C2: 2 * Ce.coeff(lam, 2) / Ae.coeff(lam, 0), D1: 0, D2: 0}
        okg &= sp.simplify(Ae.coeff(lam, 0)) == 1 and sp.simplify(Ce.coeff(lam, 0)) == sp.Rational(1, 2)
        okg &= sp.simplify(n2.subs(sig, 1).subs(jets)) == sp.Rational(7, 4) and sp.simplify(n3.subs(jets)) == 1
    checks.check("D1", ok_s and ok_jet and ok_match and ok_sigma and okg, "bilinear members F = -c sum (X_y - X_x)(Y_y - Y_x): weight one and D(0) = 0 force X = w f(l), Y = g(l); the jet forces f'(1) = 1/2; with g(1) = g'(1) = 1 and p = q/2 the index l f/X is the comparator's identically iff l f = ((1 + g)/2)^3; five choices of g (the curvature member 2 sqrt(l) - 1, and l, 1 + log l, 1 + (l^3 - 1)/3, (3 - 1/l^2)/2) give nu2 = 7/4 and nu3 = 1")
    gam = sp.symbols("gamma", positive=True)
    npow = (1 + gam * Mm / rr) ** (3 / (2 * gam)) / (1 - Mm / (2 * rr))
    ser = sp.series(npow.subs(rr, 1 / eps), eps, 0, 3).removeO()
    ok_pow = sp.simplify(sp.expand(ser).coeff(eps, 1) - 2 * Mm) == 0 and sp.simplify(sp.expand(ser).coeff(eps, 2) - (17 - 6 * gam) / 8 * Mm ** 2) == 0
    only_half = sp.solve(sp.Eq((17 - 6 * gam) / 8, sp.Rational(7, 4)), gam) == [sp.Rational(1, 2)]
    rn = rr * (1 + Mm / (2 * rr)) ** 3 / (1 - Mm / (2 * rr))
    stat = [c for c in sp.solve(sp.diff(rn.subs(Mm, 1), rr), rr) if c.is_real and c > sp.Rational(1, 2)]
    ok_cap = len(stat) == 1 and sp.simplify(rn.subs(Mm, 1).subs(rr, stat[0]) - 3 * sp.sqrt(3)) == 0
    checks.check("D2", ok_pow and only_half and ok_cap, "power laws Y = l^gamma (X = w sqrt(l)): nu2 = (17 - 6 gamma) M^2/8, the comparator's 7/4 only at gamma = 1/2 (the curvature member); the comparator's index has its capture minimum r n = 3 sqrt3 M")
    u = sp.Function("u")(r)
    lm = sp.Function("lam")(r)
    Lag = sp.exp(u) * ((1 + A1 * lm) * u.diff(r) * lm.diff(r) + (sp.Rational(1, 2) + C1 * lm) * lm.diff(r) ** 2 + D1 * lm * u.diff(r) ** 2)
    flux = sp.diff(Lag, u.diff(r))
    fl = flux.subs({u.diff(r): -U1 / r ** 2, lm.diff(r): -L1 / r ** 2}).subs({u: U1 / r, lm: L1 / r})
    wall = sp.limit(-r ** 2 * fl, r, sp.oo)
    checks.check("D3", sp.simplify(wall - L1) == 0, "the ledger's wall term, the far-field flux of dL/du', is A(0) L1 whatever the third-order jet (A1, C1, D1): the named clause that fixes the ledger is blind to the plane")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 55, 60 and 110 as landed on main (the ledger per tick, the weight-one field energies of rates and lengths with their second-order jet, the curvature member and the index its rays see); it reports which static completions bend rays like the comparator; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the plane."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Ivanenko", "Belinfante", "Rosenfeld", "Cartan", "Kibble",
                   "Sciama", "Hehl", "Wilson", "Pauli", "Fierz", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace", "Poisson", "Gauss", "Planck", "Green", "Hamilton",
                   "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Bouguer", "Schwarzschild", "Eddington")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Weyl) —", 1)
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
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the completion's field equations order by order (general jets, general beta), and the curvature member's exact exterior",
    "per_site: executed - the turn from the ray invariant and the comparator's index coefficients",
    "per_mode: executed - the plane of third-order jets, the fourth-order slopes, the general-beta formula for a body at rest",
    "per_block: executed - bilinear members: the matching identity, five choices of g, power laws, the capture minimum; the wall term",
    "lattice_wide: checked and not executed - the exact lattice exterior (the long-wave reduction is assumed), and clauses beyond the three named",
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 60's weight-one static completions around a spherical body, long wavelength: the comparator's second-order bending on the plane 4A1 - 2C1 - 6D1 = 3 of third-order jets (sigma = 1); bilinear members match its index at every order iff l f = ((1 + g)/2)^3; the named clauses leave the jet free; harvest of #9202 (confirmed by #9294); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
