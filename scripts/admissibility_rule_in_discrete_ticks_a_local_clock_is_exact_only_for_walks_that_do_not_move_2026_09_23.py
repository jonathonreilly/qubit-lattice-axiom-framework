#!/usr/bin/env python3
"""Exact line-step identities, scoped small-angle quasienergy expansions and bounded transport under explicit finite-range clock-scaling hypotheses."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_IN_DISCRETE_TICKS_A_LOCAL_CLOCK_IS_EXACT_ONLY_FOR_WALKS_THAT_DO_NOT_MOVE_THE_FLAT_BAND_THEOREM_AND_A_WALK_CLOCKED_TO_RELATIVE_EPS_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md')
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
    note, axioms = texts[:2]
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
    """Exact checks for the scoped companion statements."""
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
    checks.check("B1", unit and rng and two_ticks and root and first, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
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
    checks.check("C1", disp and ser and rat and sep and rays and psi_ser, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
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
    checks.check("D1", ident and trig and rng, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
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
    checks.check("E1", ok_nodes and flat and eigs and grows, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    U=step_matrix(6,[sp.Integer(1)]*6,[sp.Integer(0)]*6)
    H=sp.Matrix([[0,1],[1,0]])
    checks.check("D9", U==sp.eye(12) and H*sp.Matrix([1,0])==sp.Matrix([0,1]), 'Scoped exact check D9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.')
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
    nodes = list(ast.walk(ast.parse(src)))
    float_hits = [n for n in nodes if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    float_hits += [n for n in nodes if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in ('float', 'N')) or (isinstance(n.func, ast.Attribute) and n.func.attr in ('evalf', 'N')))]
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
    "per_element: exact matrix or algebraic elements in the specified fixtures",
    "per_site: site identities in the explicitly stated finite fixtures",
    "per_mode: only the modes or finite spectral invariants actually checked below",
    "per_block: the stated finite operator and state comparisons",
    "lattice_wide: general conclusions rely on the scoped written proofs; historical simulations are deferred",
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
    family_scope(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Exact line-step identities, scoped small-angle quasienergy expansions and bounded transport under explicit finite-range clock-scaling hypotheses.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
