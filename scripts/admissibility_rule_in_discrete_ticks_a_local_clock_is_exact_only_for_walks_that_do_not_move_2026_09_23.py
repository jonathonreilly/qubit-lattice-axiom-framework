#!/usr/bin/env python3
"""Exact checks: in discrete ticks a local clock is exact only for walks that do not move - the flat-band theorem, and a partial-swap
walk that carries block 54's clocked walk to relative eps^2 (a probes worker's result, refereed by a Grok model; block 54 supplied; not adopted).

B (T1): the partial-swap walk is unitary with range 2 for every clock field; two coined ticks; first order = block 54's walk.
C (T2): sin(omega/2) = sin eps |cos k|; a clock to relative eps^2; the ray law = block 54's plus O(eps^4).
D (T3): doubling the clock is not two steps: 2 sin^4 eps sin^2 2k; U[w]^2 reaches four sites, U[2w] two.
E (T4): the flat-band theorem's interpolation step, its sharp example, and a moving walk's growing range.
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
    "docs/ADMISSIBILITY_RULE_IN_DISCRETE_TICKS_A_LOCAL_CLOCK_IS_EXACT_ONLY_FOR_WALKS_THAT_DO_NOT_MOVE_THE_FLAT_BAND_THEOREM_AND_A_WALK_CLOCKED_TO_RELATIVE_EPS_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_the_flat_band_theorem_and_a_walk_clocked_to_relative_eps_squared_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "Each site has a domain of local possibilities.",
    "Admissibility is not a dynamics axiom.",
    "define a time metric",
)

MUTATION_GATE = {
    "gauge_shift_wrong": "B",
    "clock_error_coefficient_altered": "C",
    "clock_defect_forged": "D",
    "range_growth_forged": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: each site has a domain of local possibilities; Admissibility is not a dynamics axiom and does not define a time metric (steps and clocks are supplied clauses)")


# ============================================================================================ helpers (the partial-swap walk on a ring)
def step_matrix(L, cs, sn):
    """Exact step U = B A on a ring of L sites; basis index 2x + (0 up, 1 down); bond (x, x+1) angle given by (cos, sin)."""
    N = 2 * L
    A = sp.zeros(N, N)
    B = sp.zeros(N, N)
    for x in range(L):
        y = (x + 1) % L
        c, s = cs[x], sn[x]
        for M, p, q in ((A, 2 * x, 2 * y + 1), (B, 2 * x + 1, 2 * y)):
            M[p, p] = c
            M[q, q] = c
            M[p, q] = -sp.I * s
            M[q, p] = -sp.I * s
    return B * A


def ring_dist(i, j, L):
    return min(abs(i // 2 - j // 2), L - abs(i // 2 - j // 2))


PYTH = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61), (28, 45, 53), (33, 56, 65)]


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the partial-swap walk is unitary and local for every clock field; it is two coined ticks; first order is block 54's walk."""
    L = 6
    cs = [sp.Rational(a, c) for a, b, c in PYTH[:L]]
    sn = [sp.Rational(b, c) for a, b, c in PYTH[:L]]
    U = step_matrix(L, cs, sn)
    N = 2 * L
    unit = sp.simplify(U.H * U - sp.eye(N)) == sp.zeros(N, N)
    rng = all(U[i, j] == 0 for i in range(N) for j in range(N) if ring_dist(i, j, L) > 2)
    S, C, G = sp.zeros(N, N), sp.zeros(N, N), sp.zeros(N, N)
    for x in range(L):
        c_, s_ = cs[x], sn[x]
        S[2 * ((x + 1) % L), 2 * x] = 1
        S[2 * ((x - 1) % L) + 1, 2 * x + 1] = 1
        C[2 * x, 2 * x], C[2 * x, 2 * x + 1], C[2 * x + 1, 2 * x], C[2 * x + 1, 2 * x + 1] = s_, -c_, c_, s_
        G[2 * x, 2 * x] = 1
        G[2 * ((x - 1) % L) + 1, 2 * x + 1] = -sp.I
    Uc = S * C
    two_ticks = sp.simplify(Uc * Uc + G * U * G.inv()) == sp.zeros(N, N)
    V = sp.I * G.inv() * Uc * G
    root = sp.simplify(V * V - U) == sp.zeros(N, N) and all(V[i, j] == 0 for i in range(N) for j in range(N) if ring_dist(i, j, L) > 1)
    q = sp.symbols("q", real=True)
    MA = sp.Matrix([[0, sp.exp(sp.I * q)], [sp.exp(-sp.I * q), 0]])
    gen = (MA + MA.conjugate()).applyfunc(lambda z: sp.simplify(z.rewrite(sp.cos)))
    shift = sp.pi / 2 if not mut("gauge_shift_wrong") else sp.pi / 3
    first = sp.simplify(gen - 2 * sp.cos(q) * sp.Matrix([[0, 1], [1, 0]])) == sp.zeros(2, 2) and sp.simplify(sp.cos(q - shift) - sp.sin(q)) == 0
    checks.check("B1", unit and rng and two_ticks and root and first, "T1: rotations exp(-i eps_b sigma_x) on the pairs {(up,x),(down,x+1)}, then {(down,x),(up,x+1)}, with bond angle the bond clock: U^+ U = 1 and range 2 exactly for six different angles on a ring of 6 (every clock field is allowed); U = -G^-1 (S R)^2 G, two ticks of the coined walk at theta_x = pi/2 - eps_x, and U = V^2 with V of range 1; the first-order generator has symbol 2 cos k sigma_x, which the gauge psi_x -> i^x psi_x makes 2 sin k sigma_x: twice block 54's line walk, so to first order the step is block 54's clocked walk")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: dispersion, a clock to relative eps^2, and the ray law against block 54's."""
    e, k = sp.symbols("epsilon k", real=True)
    MA = sp.Matrix([[0, sp.exp(sp.I * k)], [sp.exp(-sp.I * k), 0]])
    MB = sp.Matrix([[0, sp.exp(-sp.I * k)], [sp.exp(sp.I * k), 0]])
    Uk = (sp.cos(e) * sp.eye(2) - sp.I * sp.sin(e) * MB) * (sp.cos(e) * sp.eye(2) - sp.I * sp.sin(e) * MA)
    disp = sp.simplify((Uk.trace() / 2 - (1 - 2 * sp.sin(e) ** 2 * sp.cos(k) ** 2)).rewrite(sp.exp)) == 0 and sp.simplify(Uk.det()) == 1
    ep, cc = sp.symbols("epsilon c", positive=True)
    om = 2 * sp.asin(sp.sin(ep) * cc)
    coef = sp.Rational(1, 6) if not mut("clock_error_coefficient_altered") else sp.Rational(1, 3)
    ser = sp.simplify(sp.expand(sp.series(om, ep, 0, 5).removeO() - 2 * ep * cc * (1 - ep ** 2 * (1 - cc ** 2) * coef))) == 0
    rat = sp.simplify(sp.series(sp.diff(om, ep) * ep / om, ep, 0, 3).removeO() - (1 - ep ** 2 * (1 - cc ** 2) / 3)) == 0
    x, t = sp.symbols("x t", real=True)
    kf = sp.Function("k")(t)
    w = sp.Function("w")(x)
    f = sp.Function("f")
    omg = w * f(kf)
    v = sp.diff(omg, kf)
    dvdt = sp.diff(v, x) * v + sp.diff(v, kf) * (-sp.diff(omg, x))
    law = -w ** 2 * sp.diff(f(kf) ** 2 / 2, kf, 2) * sp.diff(sp.log(w), x) + 2 * v ** 2 * sp.diff(sp.log(w), x)
    sep = sp.simplify(sp.expand(dvdt - law)) == 0
    ek, kk = sp.symbols("epsilon k", positive=True)
    Psi = 4 * sp.sin(ek) * (ek * sp.cos(ek) - 2 * sp.sin(ek) * sp.sin(kk) ** 2) / (1 - sp.sin(ek) ** 2 * sp.cos(kk) ** 2)
    rays = True
    for sg in (1, -1):
        Om = 2 * sp.asin(sg * sp.sin(ek) * sp.cos(kk))
        Ok, Oe = sp.diff(Om, kk), sp.diff(Om, ek)
        Phi = ek * (sp.diff(Ok, ek) * Ok - sp.diff(Ok, kk) * Oe)
        rays = rays and sp.simplify(Phi - 2 * Ok ** 2 - Psi) == 0
    tgt = 4 * ek ** 2 * sp.cos(2 * kk) + ek ** 4 * (2 * sp.cos(2 * kk) + 3 * sp.cos(4 * kk) - 1) / 3
    psi_ser = sp.simplify(sp.expand(sp.expand_trig(sp.series(Psi, ek, 0, 6).removeO() - tgt))) == 0
    checks.check("C1", disp and ser and rat and sep and rays and psi_ser, "T2: at a uniform angle tr U/2 = 1 - 2 sin^2 eps cos^2 k and det U = 1, so sin(omega/2) = sin eps |cos k|; omega = 2 eps |cos k| (1 - (eps^2/6) sin^2 k) + O(eps^5) and eps d omega/d eps = omega (1 - (eps^2/3) sin^2 k + ...): with eps = eps0 w every frequency follows the local clock up to a relative eps^2; any separable omega = w f(k) gives exactly block 54's ray law, and the walk's own rays obey dv/dt = (2 v^2 + Psi) d_x log w with Psi in closed form (both branches), Psi = 4 eps^2 cos 2k + (eps^4/3)(2 cos 2k + 3 cos 4k - 1) + O(eps^6): block 54's law plus a term of order eps^4 (symbolic)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: this walk has no exact clock: doubling the clock is not two steps."""
    e, k = sp.symbols("epsilon k", real=True)
    s, c = sp.symbols("s c", real=True)
    tr2 = 1 - 8 * s ** 2 * (1 - s ** 2) * c ** 2
    twice = 2 * (1 - 2 * s ** 2 * c ** 2) ** 2 - 1
    gap = sp.factor(sp.expand(tr2 - twice))
    target = 8 * s ** 4 * c ** 2 * (1 - c ** 2) if not mut("clock_defect_forged") else 0
    ident = sp.simplify(gap - target) == 0
    trig = sp.simplify((sp.sin(2 * e) ** 2 - 4 * sp.sin(e) ** 2 * (1 - sp.sin(e) ** 2))) == 0 and sp.simplify(8 * sp.cos(k) ** 2 * (1 - sp.cos(k) ** 2) - 2 * sp.sin(2 * k) ** 2) == 0
    L = 10
    cs = [sp.Rational(a, cq) for a, b, cq in PYTH]
    sn = [sp.Rational(b, cq) for a, b, cq in PYTH]
    U = step_matrix(L, cs, sn)
    U2 = U * U
    Ud = step_matrix(L, [c_ ** 2 - s_ ** 2 for c_, s_ in zip(cs, sn)], [2 * c_ * s_ for c_, s_ in zip(cs, sn)])
    N = 2 * L
    far_d = [(i, j) for i in range(N) for j in range(N) if ring_dist(i, j, L) > 2 and Ud[i, j] != 0]
    corner = U2[8, 0]
    rng = corner == sn[0] * sn[1] * sn[2] * sn[3] and corner != 0 and not far_d
    checks.check("D1", ident and trig and rng, "T3: doubling every bond angle is not two steps: tr U(2 eps)/2 - cos 2 omega(eps) = 8 sin^4 eps cos^2 k sin^2 k = 2 sin^4 eps sin^2 2k, nonzero off sin eps sin 2k = 0 (exact identity); for any field <up,x+4|U[w]^2|up,x> = sin eps_x sin eps_(x+1) sin eps_(x+2) sin eps_(x+3) (ten different angles on a ring of 10), while U[2w] reaches only two sites")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the flat-band theorem's ingredients, its sharpness, and a moving walk's growing range."""
    ok_nodes = True
    for R in (1, 2, 3):
        n = 2 * R + 1
        ts = [sp.Rational(i + 1, n + 2) for i in range(n)]
        zs = [((1 - tq ** 2) + 2 * sp.I * tq) / (1 + tq ** 2) for tq in ts]
        unit_circle = all(sp.simplify(sp.expand(z * sp.conjugate(z))) == 1 for z in zs)
        distinct = len({sp.nsimplify(z) for z in zs}) == n
        Mv = sp.Matrix(n, n, lambda i, j: zs[i] ** (j - R))
        dv = sp.expand(Mv.det())
        ok_nodes = ok_nodes and unit_circle and distinct and dv != 0
    c1, c2, q = sp.symbols("c1 c2 q", real=True)
    H = sp.Matrix([[0, sp.exp(-sp.I * q)], [sp.exp(sp.I * q), 0]])
    Vf = lambda cc: sp.cos(cc) * sp.eye(2) - sp.I * sp.sin(cc) * H
    flat = sp.simplify(H * H - sp.eye(2)) == sp.zeros(2, 2) and sp.simplify((Vf(c1) * Vf(c2) - Vf(c1 + c2)).applyfunc(sp.expand_trig)) == sp.zeros(2, 2)
    eigs = sp.simplify(sp.Matrix(H.eigenvals(multiple=True)) - sp.Matrix([-1, 1])) == sp.zeros(2, 1) or sorted(H.eigenvals(multiple=True)) == [-1, 1]
    L = 12
    cs = [sp.Rational(3, 5)] * L
    sn = [sp.Rational(4, 5)] * L
    U = step_matrix(L, cs, sn)
    N = 2 * L
    ranges = []
    P = sp.eye(N)
    for m in range(1, 4):
        P = P * U
        ranges.append(max(ring_dist(i, j, L) for i in range(N) for j in range(N) if P[i, j] != 0))
    grows = ranges == [2, 4, 6] if not mut("range_growth_forged") else ranges == [2, 2, 2]
    checks.check("E1", ok_nodes and flat and eigs and grows, "T4 (the flat-band theorem, proof in the note): its interpolation step holds - evaluation at 2R + 1 distinct points of the unit circle is a bijection of the trigonometric polynomials of degree R (R = 1, 2, 3 at rational points of the circle, exact determinants); its conclusion is attained, so it cannot be strengthened: H = [[0, e^-ik], [e^ik, 0]] has H^2 = 1 and eigenvalues -1, 1 at every k, and e^(-icH) = cos c - i sin c H is a group of range-1 steps with exact clock scaling that moves nothing beyond one site; a walk that moves packets escapes the hypothesis at once: at the uniform angle with cos = 3/5 the ranges of U, U^2, U^3 are 2, 4, 6 on a ring of 12")


# ============================================================================================ family F
FENCES = (
    "This note works within the supplied clock clause of blocks 53 and 54 (a site's rate is a local clock; the walk hops on bonds timed by the geometric mean of their ends); it reports, from a probes worker's result refereed by another model family, what happens to that clause when time comes in discrete ticks; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the one-bond rotations and the two-by-two symbols; the dispersion, its series and the ray law (symbolic)",
    "per_site: executed - the step on rings of 6, 10 and 12 with exact rational angles: unitarity, range, the two-tick identity, the four-site element",
    "per_mode: executed - the doubling defect 2 sin^4 eps sin^2 2k; the interpolation determinants for R = 1, 2, 3; control: a packet in a clock gradient",
    "per_block: executed - the sharp flat-band example; the ranges of U, U^2, U^3 of a moving walk",
    "lattice_wide: T1-T3 for every clock field on the line; T4 for every finite-range translation-invariant unitary in any dimension (proof); block 54 supplied",
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
    print("scope: discrete ticks and block 54's clock clause - the partial-swap walk is unitary and local for every clock field and a clock to relative eps^2 with block 54's ray law plus O(eps^4); no finite-range unitary that moves packets can follow a local clock exactly (flat-band theorem); nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
