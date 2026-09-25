#!/usr/bin/env python3
"""Exact checks: possibility's odds - only the turn is massless (the ingredients), a precessing turn diffuses and carries sound only on a
staggered sea without relaxation, and on the six-axis massless surface a record's lean falls as 1/r only up to a logarithm (a harvest
block from three Grok-refereed probes attempts; blocks 42 and 103 as landed supplied; not adopted).

B (T1): the sphere menu's sector kernels are the modified Bessel functions; the order comparison at sample points; the large-beta chain.
C (T2): the turn's frequencies under a supplied precession, for the ordered and for the staggered sea.
D (T3): the six-axis map to third order, exactly; the slaved quadrupole and the cubic coefficient u; its value on the massless surface.
E (T4): the radial reduction of the cubic lean equation and its centre manifold: the logarithmic law of a record's far field.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_POSSIBILITYS_ODDS_ONLY_THE_TURN_IS_MASSLESS_A_PRECESSING_TURN_DIFFUSES_AND_ON_THE_SIX_AXIS_MASSLESS_SURFACE_A_RECORDS_LEAN_FALLS_AS_ONE_OVER_R_ONLY_UP_TO_A_LOGARITHM_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_possibilitys_odds_only_the_turn_is_massless_a_precessing_turn_diffuses_and_on_the_six_axis_massless_surface_a_records_lean_falls_as_one_over_r_only_up_to_a_logarithm_bounded_theorem_note_2026-09-24"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "mehler_ratio_forged": "B",
    "staggered_coupling_forged": "C",
    "cubic_coefficient_forged": "D",
    "centre_manifold_forged": "E",
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


I = sp.I
F = Fraction


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (the odds map, its menu and any precession are supplied clauses)")


# ============================================================================================ family B
XS = sp.symbols("x", positive=True)


def bessel_series(m, x, terms):
    return sum((sp.Rational(1, 2 ** (2 * j + m)) * x ** (2 * j + m) / (sp.factorial(j) * sp.factorial(j + m)) for j in range(terms)), sp.Integer(0))


def family_b(checks: Checks) -> None:
    """T1's ingredients: sector kernels, the order comparison at sample points, the large-beta Gaussian chain."""
    ok = True
    for m in range(5):
        for k in range(13):
            avg = sp.binomial(k, (k - m) // 2) / 2 ** k if (k >= m and (k - m) % 2 == 0) else sp.Integer(0)
            coeff = avg / sp.factorial(k)
            ser = sp.expand(bessel_series(m, XS, 8)).coeff(XS, k)
            ok = ok and sp.simplify(coeff - ser) == 0
    soni = True
    for x in (F(1, 2), F(1), F(3)):
        def partial(m, terms):
            return sum((F(1, 2 ** (2 * j + m)) * x ** (2 * j + m) / (sp.factorial(j) * sp.factorial(j + m)) for j in range(terms)), F(0))
        terms = 30
        for m in (2, 3, 4):
            nxt = F(1, 2 ** (2 * terms + m)) * x ** (2 * terms + m) / (sp.factorial(terms) * sp.factorial(terms + m))
            upper = partial(m, terms) + 2 * nxt
            soni = soni and upper < partial(1, terms)
    checks.check("B1", ok and soni, "T1: on the sphere menu, the one-neighbour kernel e^(beta s.b) splits by azimuthal order m into the positive kernels e^(beta t t') I_m(beta r r'): the angular average of e^(x cos psi) cos(m psi) matches I_m(x) through x^12 for m = 0..4; and I_m(x) < I_1(x) for m = 2, 3, 4 at x = 1/2, 1, 3 by exact rational bounds (the order comparison the proof imports for every x > 0)")
    beta, a = sp.symbols("beta a", positive=True)
    curv = sp.simplify(a * beta / (2 * a + beta))
    fixed = sp.solve(sp.Eq(6 * curv, a), a)
    mean_ratio = sp.simplify(beta / (2 * fixed[0] + beta))
    var = sp.simplify(1 / (2 * fixed[0] + beta))
    rho = mean_ratio if not mut("mehler_ratio_forged") else sp.Rational(1, 5)
    xx, yy = sp.symbols("xx yy", real=True)
    s2 = var / (1 - mean_ratio ** 2)
    herm_ok = True
    for n in range(1, 4):
        he = sp.hermite_prob(n, yy / sp.sqrt(s2))
        mean_y = mean_ratio * xx
        dens = sp.exp(-(yy - mean_y) ** 2 / (2 * var)) / sp.sqrt(2 * sp.pi * var)
        cond = sp.simplify(sp.integrate(he * dens, (yy, -sp.oo, sp.oo)))
        herm_ok = herm_ok and sp.simplify(cond - rho ** n * sp.hermite_prob(n, xx / sp.sqrt(s2))) == 0
    masses = [sp.simplify((1 - 6 * rho ** n) / rho ** n) for n in (1, 2, 3)]
    checks.check("B2", fixed == [5 * beta / 2] and mean_ratio == sp.Rational(1, 6) and herm_ok and masses == [0, 30, 210],
                 f"T1: as beta grows the sea tends in the tangent plane to a Gaussian of curvature a with a -> a beta/(2a + beta) under one neighbour, fixed by the sixth power at a = 5 beta/2; the per-neighbour chain is y | x Gaussian with mean x/6 and variance 1/(6 beta), whose Hermite modes have eigenvalues 6^-n (checked for n <= 3): masses (1 - 6 mu)/mu = {masses} - the turn (n = 1) massless, the lean size and m = +-2 at 30, the next at 210")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the turn's frequencies under a supplied precession."""
    gam, om, g1, kap = sp.symbols("Gamma Omega gamma kappa", positive=True)
    jm = sp.Matrix([[0, -1], [1, 0]])                       # n x (.) on the plane transverse to the lean
    ordered = -(gam * sp.eye(2) + om * jm) * (1 - g1)
    lam = sp.symbols("lam")
    ok_o = sp.simplify(sp.expand((lam * sp.eye(2) - ordered).det()) - sp.expand((lam + (gam + I * om) * (1 - g1)) * (lam + (gam - I * om) * (1 - g1)))) == 0
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    e_k = sum((2 - 2 * sp.cos(k) for k in (k1, k2, k3)), sp.Integer(0))
    gamma_k = sum((sp.cos(k) for k in (k1, k2, k3)), sp.Integer(0)) / 3
    ok_e = sp.simplify(1 - gamma_k - e_k / 6) == 0
    sign = 1 if not mut("staggered_coupling_forged") else -1
    stag = sp.Matrix([[-(gam + I * om), sign * (gam + I * om) * g1], [(gam - I * om) * g1, -(gam - I * om)]])
    charpoly = sp.expand((lam * sp.eye(2) - stag).det())
    want_c = sp.expand(lam ** 2 + 2 * gam * lam + (gam ** 2 + om ** 2) * (1 - g1 ** 2))
    ok_s = sp.simplify(charpoly - want_c) == 0
    axis = sp.simplify(1 - ((2 + sp.cos(kap)) / 3) ** 2)
    speed = sp.series(sp.sqrt(axis), kap, 0, 4).removeO()
    ok_sound = sp.simplify(speed - (kap / sp.sqrt(3) + sp.series(sp.sqrt(axis), kap, 0, 4).removeO().coeff(kap, 3) * kap ** 3)) == 0 and sp.simplify(speed.coeff(kap, 1) - 1 / sp.sqrt(3)) == 0
    eps = sp.symbols("epsilon", positive=True)
    slow = [root for root in sp.solve(sp.Eq(lam ** 2 + 2 * gam * lam + (gam ** 2 + om ** 2) * eps, 0), lam)]
    slow_series = [sp.series(root, eps, 0, 2).removeO() for root in slow]
    ok_slow = any(sp.simplify(sr + (gam ** 2 + om ** 2) * eps / (2 * gam)) == 0 for sr in slow_series)
    checks.check("C1", ok_o and ok_e and ok_s and ok_sound and ok_slow,
                 "T2: on the ordered sea the turns relax as tau' = -(Gamma + Omega n x)(tau - mean of the six neighbours), so omega(k) = (+-Omega - i Gamma) E(k)/6 exactly, E = sum(2 - 2 cos k_j): circularly polarized, omega ~ k^2, one quality factor Omega/Gamma at every k - no sound; on the staggered sea (beta < 0) the two sublattices precess oppositely and lambda^2 + 2 Gamma lambda + (Gamma^2 + Omega^2)(1 - gamma^2) = 0: at Gamma = 0, omega = +-Omega sqrt(1 - gamma^2) = +-Omega |k|/sqrt 3 + O(k^3) along an axis, and for Gamma > 0 the slow root is -(Gamma^2 + Omega^2)(1 - gamma^2)/(2 Gamma) + ..., diffusive")


# ============================================================================================ family D
AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def map_expansion(pp, qq, rr, vs, dq):
    t = sp.symbols("t")
    tt = pp + qq + 4 * rr
    l1, l2 = sp.Rational(pp - qq, tt), sp.Rational(pp + qq - 2 * rr, tt)
    quad = lambda s: 3 * s[0] ** 2 - 1
    prod = {s: sp.Integer(1) for s in AXES}
    for v, d in zip(vs, dq):
        for s in AXES:
            prod[s] *= 1 + 3 * l1 * t * v * s[0] + l2 * t ** 2 * d * quad(s)
    z = sum(prod.values(), sp.Integer(0))
    v_new = sp.series((prod[AXES[0]] - prod[AXES[1]]) / z, t, 0, 5).removeO()
    d_new = sp.series(1 - 6 * prod[AXES[2]] / z, t, 0, 4).removeO()
    s1, sv2, sv3 = sum(vs), sum(v ** 2 for v in vs), sum(v ** 3 for v in vs)
    svd, sd = sum(v * d for v, d in zip(vs, dq)), sum(dq)
    want_v = l1 * s1 * t + (3 * l1 ** 3 * (sv3 - s1 * sv2) - 2 * l1 * l2 * (svd - s1 * sd)) * t ** 3
    want_d = (l2 * sd + sp.Rational(3, 2) * l1 ** 2 * (s1 ** 2 - sv2)) * t ** 2
    return sp.expand(v_new - want_v) == 0 and sp.expand(d_new - want_d) == 0


def family_d(checks: Checks) -> None:
    """T3: the six-axis map to third order; the slaved quadrupole; the cubic coefficient on the massless surface."""
    hoods = [([sp.Rational(1, 2), sp.Rational(-1, 3), sp.Rational(2, 5), 0, sp.Rational(1, 4), sp.Rational(-1, 2)],
              [sp.Rational(1, 3), sp.Rational(-1, 2), 0, sp.Rational(2, 3), sp.Rational(-1, 5), sp.Rational(1, 7)]),
             ([1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0])]
    ok_map = all(map_expansion(pp, qq, rr, vs, dq) for (pp, qq, rr) in ((3, 1, 2), (5, 2, 4), (7, 2, 3)) for vs, dq in hoods)
    l1, l2, vv, dd = sp.symbols("l1 l2 v D")
    v_eq = sp.expand(6 * l1 * vv + 3 * l1 ** 3 * (6 * vv ** 3 - 36 * vv ** 3) - 2 * l1 * l2 * (6 * vv * dd - 36 * vv * dd))
    d_sol = sp.solve(sp.Eq(dd, 6 * l2 * dd + sp.Rational(3, 2) * l1 ** 2 * (36 * vv ** 2 - 6 * vv ** 2)), dd)[0]
    cubic = sp.simplify(sp.expand(v_eq.subs(dd, d_sol)).coeff(vv, 3) / l1)
    u_claim = 90 * l1 ** 2 * (1 - 36 * l2) / (1 - 6 * l2) if not mut("cubic_coefficient_forged") else 90 * l1 ** 2 * (1 - 30 * l2) / (1 - 6 * l2)
    ok_u = sp.simplify(d_sol - 45 * l1 ** 2 * vv ** 2 / (1 - 6 * l2)) == 0 and sp.simplify(cubic + u_claim) == 0
    q, r = sp.symbols("q r", positive=True)
    p = (7 * q + 4 * r) / 5
    tt = p + q + 4 * r
    l1s, l2s = sp.simplify((p - q) / tt), sp.simplify((p + q - 2 * r) / tt)
    u_surf = sp.simplify(u_claim.subs({l1: l1s, l2: l2s}))
    ok_s = l1s == sp.Rational(1, 6) and sp.simplify(u_surf - sp.Rational(5, 2) * (4 * r - 7 * q) / (r - q)) == 0 and sp.simplify(u_surf.subs({q: 1, r: 2})) == sp.Rational(5, 2) and sp.simplify(l2s.subs({q: 1, r: 2})) == 0
    checks.check("D1", ok_map and ok_u and ok_s,
                 "T3: for block 42's six-axis map, a site whose neighbours carry leans v_y and quadrupoles D_y gets v' = l1 S1 + 3 l1^3 (sum v^3 - S1 sum v^2) - 2 l1 l2 (sum vD - S1 sum D) + O(t^5) and D' = l2 sum D + (3/2) l1^2 (S1^2 - sum v^2) + O(t^4), exactly (three weight triples, two neighbourhoods); for slow fields the quadrupole is slaved, D = 45 l1^2 v^2/(1 - 6 l2), and the lean obeys -Lap v + m^2 v + u v^3 = source, u = 90 l1^2 (1 - 36 l2)/(1 - 6 l2); on the massless surface 5p = 7q + 4r, l1 = 1/6 and u = (5/2)(4r - 7q)/(r - q), 5/2 at (3,1,2)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the radial cubic equation and its centre manifold."""
    rr, tau, u = sp.symbols("r tau u", positive=True)
    aa = sp.Function("A")
    v = aa(rr) / rr
    lap = sp.simplify(sp.diff(v, rr, 2) + 2 / rr * sp.diff(v, rr))
    ok_lap = sp.simplify(lap - sp.diff(aa(rr), rr, 2) / rr) == 0
    bb = sp.Function("B")
    a_of_r = bb(sp.log(rr))
    second = sp.diff(a_of_r, rr, 2)
    d1 = sp.diff(bb(sp.log(rr)), rr)
    ok_chain = sp.simplify(sp.diff(bb(tau), tau).subs(tau, sp.log(rr)) / rr - d1) == 0 and sp.simplify(second - (sp.diff(bb(tau), tau, 2).subs(tau, sp.log(rr)) - sp.diff(bb(tau), tau).subs(tau, sp.log(rr))) / rr ** 2) == 0
    xs = sp.symbols("X", positive=True)
    h = -u * xs ** 3 + 3 * u ** 2 * xs ** 5 - 24 * u ** 3 * xs ** 7 if not mut("centre_manifold_forged") else -u * xs ** 3 + 2 * u ** 2 * xs ** 5
    resid = sp.expand(h * sp.diff(h, xs) - h - u * xs ** 3)
    ok_cm = all(resid.coeff(xs, k) == 0 for k in range(0, 9))
    rate = sp.expand(sp.series(-2 * xs ** -3 * h, xs, 0, 3).removeO())
    ok_rate = sp.simplify(rate - (2 * u - 6 * u ** 2 * xs ** 2)) == 0
    checks.check("E1", ok_lap and ok_chain and ok_cm and ok_rate,
                 "T4: for v = A(r)/r, Lap v = A''/r, so away from the source the cubic lean equation is A'' = u A^3/r^2, that is A_tau tau - A_tau = u A^3 in tau = log r; its decaying solutions lie on the centre manifold A_tau = -u A^3 + 3 u^2 A^5 - 24 u^3 A^7 + ... (checked through order 8), so (A^-2)_tau = 2u - 6 u^2 A^2 + ...: A^-2 = 2u log r - 3u log log r + C + o(1) - a record's lean falls as 1/r only up to this logarithm, and a weak source keeps a 1/r field out to about r0 exp(1/(2 u A0^2))")


# ============================================================================================ family F
FENCES = (
    "This note works within block 42's odds map and block 103's sphere-menu odds, as landed on main, with a supplied precession where stated; it reports which channels of possibility's odds are massless, how the massless turn moves, and how a record's lean falls off on the six-axis massless surface; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Jentzsch", "Soni", "Mehler", "Hermite", "Bessel", "Landau", "Ginzburg", "Wilson", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the sector kernels' series through x^12; the order comparison at three points by rational bounds; the large-beta Gaussian chain's Hermite eigenvalues",
    "per_site: executed - the six-axis map's third-order expansion, exactly, for three weight triples and two neighbourhoods",
    "per_mode: executed - the turn's frequencies on the ordered and the staggered sea (symbolic), the sound speed along an axis and the slow root",
    "per_block: executed - the slaved quadrupole, the cubic coefficient on the massless surface, the radial reduction and the centre manifold through order 8",
    "lattice_wide: T1 for every beta above block 103's massless point and every non-decreasing leaning sea, with the positive-kernel and order-comparison imports; T2 for the supplied precession on both seas; T3-T4 for block 42's six-axis map at every weight triple, in the gradient expansion; the maps, the menus and the precession are supplied",
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
    print("scope: possibility's odds - on the sphere menu only the turn is massless for |m| >= 1 (with named imports), the large-beta masses are 6^n - 6; a precessing turn diffuses (omega ~ k^2), sound only on a staggered sea without relaxation; on the six-axis massless surface the lean has a cubic term u = (5/2)(4r - 7q)/(r - q) and a record's 1/r field runs logarithmically; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
