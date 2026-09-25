#!/usr/bin/env python3
"""Exact checks: binding energy falls with its weight only in the curvature member - within block 60's static curvature member
and its bilinear family (as landed on main) and block 101's quadratic member with block 136's shift (as landed), with block 144
placed: the ledger of bodies at rest to second order is M - sum G M_a M_b / r_ab + (G^2/2) sum_a M_a (sum_b M_b / r_ab)^2 for every
bilinear member; for moving bodies the first-order ledger carries (1/2 + 1/p) k^2/m^2 for the member X = l^(p/2); for the curvature
member the field momentum at the shift's constraint adds (G/2r)[7 k1.k2 + (n.k1)(n.k2)], so the first-order Hamiltonian is block
144's pull plus the static term; a bound pair far from a third body couples to its potential with passive mass M + 2a<T> + 2 s2 <U>,
which is the pair's energy for the curvature member and differs from it by (1 - 1/p)<U> for any other bilinear member; with block
144's inertia the pair falls like one body (the supervisor's own derivation; not adopted).

B (T1): the static ledger to second order.
C (T2): the moving-body ledger for every bilinear member; the field momentum at the shift's constraint; the first-order Hamiltonian.
D (T3): the pair's coupling to a distant body's potential; the scalar virial bracket; the passive mass.
E (T3): the pair's inertia from the same Hamiltonian; the fall.
Exact symbolic and rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_BINDING_ENERGY_FALLS_WITH_ITS_WEIGHT_ONLY_IN_THE_CURVATURE_MEMBER_PULL_BOUND_PAIRS_FALL_LIKE_ONE_BODY_AT_FIRST_ORDER_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_binding_energy_falls_with_its_weight_only_in_the_curvature_member_pull_bound_pairs_fall_like_one_body_at_first_order_bounded_theorem_note_2026-09-25"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "static_second_order_forged": "B",
    "stretched_bond_coupling_dropped": "C",
    "field_momentum_trace_kept": "C",
    "outside_static_cross_term_dropped": "D",
    "scalar_virial_forged": "D",
    "inertia_delay_term_dropped": "E",
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


Fr = Fraction
HALF = sp.Rational(1, 2)
QUARTER = sp.Rational(1, 4)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the members, the shift, the kinetic term, the source link and the bodies are supplied; the memo does not define a time metric)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    c, eps = sp.symbols("c epsilon", positive=True)
    n = 3
    M = sp.symbols("M1:4", positive=True)
    r = {}
    for i in range(n):
        for j in range(i + 1, n):
            r[(i, j)] = r[(j, i)] = sp.Symbol("r%d%d" % (i + 1, j + 1), positive=True)
    g = lambda i, j: 1 / (4 * sp.pi * r[(i, j)])
    cs = [[sp.Symbol("q%d_%d" % (o, i)) for i in range(n)] for o in range(3)]
    Q = [sum(eps ** (o + 1) * cs[o][i] for o in range(3)) for i in range(n)]
    eqs = [sp.expand(Q[i] * (1 + sum(Q[j] * g(i, j) for j in range(n) if j != i)) - eps * M[i] / c) for i in range(n)]
    sol = {}
    for o in range(3):
        es = [sp.expand(e.subs(sol)).coeff(eps, o + 1) for e in eqs]
        sol.update(sp.solve(es, cs[o], dict=True)[0])
    ledger = sp.expand(c * sum(Q).subs(sol))
    G = 1 / (2 * sp.pi * c)
    second = sp.Rational(1, 4) if mut("static_second_order_forged") else HALF
    target = [sum(M), -sum(G * M[i] * M[j] / r[(i, j)] for i in range(n) for j in range(i + 1, n)),
              second * G ** 2 * sum(M[a] * sum(M[b] / r[(a, b)] for b in range(n) if b != a) ** 2 for a in range(n))]
    ok = all(sp.simplify(ledger.coeff(eps, o + 1) - target[o]) == 0 for o in range(3))
    checks.check("B1", ok, "block 60 T4 with charges Q_i X_i = M_i / c and self-fields dropped: the ledger c sum Q_i of three bodies at rest is M - sum G M_a M_b / r_ab + (G^2/2) sum_a M_a (sum_b M_b / r_ab)^2 to second order, G = 1/(2 pi c)")
    checks.check("B2", sp.simplify(G.subs(c, 8 * sp.Symbol("K", positive=True)) - 1 / (16 * sp.pi * sp.Symbol("K", positive=True))) == 0,
                 "for the curvature member c = 8K, so G = 1/(16 pi K), the value block 144 found for the member's quadratic action")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    s, lam = sp.symbols("s lambda")
    pw = sp.Symbol("p", positive=True)
    m1, m2, r = sp.symbols("m1 m2 r", positive=True)
    k1 = sp.Matrix(sp.symbols("k1x k1y k1z"))
    k2 = sp.Matrix(sp.symbols("k2x k2y k2z"))
    g = 1 / (4 * sp.pi * r)
    q1a, q1b, q2a, q2b = sp.symbols("q1a q1b q2a q2b")
    Q1 = s * q1a + s ** 2 * q1b
    Q2 = s * q2a + s ** 2 * q2b
    X1, X2 = 1 + Q2 * g, 1 + Q1 * g

    def energy(m, k, X):
        stretch = 1 if mut("stretched_bond_coupling_dropped") else 1 - 4 * (X - 1) / pw
        return sp.sqrt(m ** 2 + lam ** 2 * k.dot(k) * stretch)

    e1 = sp.series(energy(m1, k1, X1), s, 0, 2).removeO()
    e2 = sp.series(energy(m2, k2, X2), s, 0, 2).removeO()
    eq1, eq2 = sp.expand(Q1 * X1 - s * e1), sp.expand(Q2 * X2 - s * e2)
    sol = {}
    for order, unknowns in ((1, (q1a, q2a)), (2, (q1b, q2b))):
        es = [sp.expand(e.subs(sol)).coeff(s, order) for e in (eq1, eq2)]
        sol.update(sp.solve(es, unknowns, dict=True)[0])
    ledger = sp.expand(((Q1 + Q2) / s).subs(sol))
    free = sp.series(ledger.coeff(s, 0), lam, 0, 5).removeO()
    first = sp.series(ledger.coeff(s, 1), lam, 0, 3).removeO()
    G = HALF / sp.pi
    free_ok = sp.simplify(free - (m1 + m2 + lam ** 2 * (k1.dot(k1) / (2 * m1) + k2.dot(k2) / (2 * m2)) - lam ** 4 * (k1.dot(k1) ** 2 / (8 * m1 ** 3) + k2.dot(k2) ** 2 / (8 * m2 ** 3)))) == 0
    first_ok = sp.simplify(sp.expand(first + G * m1 * m2 / r * (1 + (HALF + 1 / pw) * lam ** 2 * (k1.dot(k1) / m1 ** 2 + k2.dot(k2) / m2 ** 2)))) == 0
    checks.check("C1", free_ok and first_ok, "moving bodies, energy sqrt(m^2 + k^2 / l^2) through bonds l = X^(2/p): the ledger is sum (m + k^2/2m - k^4/8m^3) - (G m1 m2 / r)[1 + (1/2 + 1/p)(k1^2/m1^2 + k2^2/m2^2)] at first order; 3/2 for the curvature member p = 1")
    pv = sp.Matrix(sp.symbols("w1:4", real=True))
    p2 = pv.dot(pv)
    A1 = sp.Matrix(sp.symbols("A1:4", real=True))
    B1 = sp.Matrix(sp.symbols("B1:4", real=True))

    def V(P):
        return (P / 2 - pv * pv.dot(P) / (8 * p2)) / p2

    def Pi(P):
        v = V(P)
        tr = 0 if mut("field_momentum_trace_kept") else sp.Rational(2, 3)
        return sp.Matrix(3, 3, lambda i, j: pv[i] * v[j] + pv[j] * v[i] - tr * (1 if i == j else 0) * pv.dot(v))

    PA, PB = Pi(A1), Pi(B1)
    constraint = all(sp.simplify(sum(pv[i] * PA[i, j] for i in range(3)) - A1[j] / 2) == 0 for j in range(3))
    tracefree = sp.simplify(PA.trace()) == 0
    ab = sp.simplify(sum(PA[i, j] * PB[i, j] for i in range(3) for j in range(3)))
    ab_ok = sp.simplify(ab - (A1.dot(B1) / 2 - pv.dot(A1) * pv.dot(B1) / (8 * p2)) / p2) == 0
    checks.check("C2", constraint and tracefree and ab_ok, "the shift's constraint 2 d_i Pi_ij + P_j = 0 with Pi trace-free and without free waves: Pi = i(p V + V p - (2/3) p.V), V = [P/2 - p (p.P)/(8 p^2)]/p^2, and Pi_1.Pi_2 = [P1.P2/2 - (p.P1)(p.P2)/(8 p^2)]/p^2")
    x = sp.Matrix(sp.symbols("x1:4", real=True))
    rr = sp.sqrt(x.dot(x))
    nn = x / rr
    hess = sp.Matrix(3, 3, lambda i, j: sp.diff(rr, x[i], x[j]))
    K = sp.Symbol("K", positive=True)
    Gk = 1 / (16 * sp.pi * K)
    cross = (2 / K) * (A1.dot(B1) / 2 / (4 * sp.pi * rr) - (A1.T * ((sp.eye(3) - nn * nn.T) / (8 * sp.pi * rr)) * B1)[0] / 8)
    cross_ok = sp.simplify(cross - Gk / (2 * rr) * (7 * A1.dot(B1) + nn.dot(A1) * nn.dot(B1))) == 0
    checks.check("C3", sp.simplify(hess - (sp.eye(3) - nn * nn.T) / rr) == sp.zeros(3, 3) and cross_ok,
                 "d_i d_j r = (delta_ij - n_i n_j)/r, so p_i p_j / p^4 is (delta - n n)/(8 pi r); the field momentum's energy (1/K) int Pi.Pi between two bodies is (G/2r)[7 k1.k2 + (n.k1)(n.k2)]")
    v1 = sp.Matrix(sp.symbols("v1x v1y v1z"))
    v2 = sp.Matrix(sp.symbols("v2x v2y v2z"))
    n3 = sp.Matrix(sp.symbols("nx ny nz"))
    Gs = sp.Symbol("G", positive=True)
    lag1 = Gs * m1 * m2 / r * (sp.Rational(3, 2) * (v1.dot(v1) + v2.dot(v2)) - sp.Rational(7, 2) * v1.dot(v2) - HALF * n3.dot(v1) * n3.dot(v2))
    ham1 = (-Gs * m1 * m2 / r * sp.Rational(3, 2) * (k1.dot(k1) / m1 ** 2 + k2.dot(k2) / m2 ** 2)
            + Gs / (2 * r) * (7 * k1.dot(k2) + n3.dot(k1) * n3.dot(k2)))
    legendre = sp.simplify(ham1 + lag1.subs({**{v1[i]: k1[i] / m1 for i in range(3)}, **{v2[i]: k2[i] / m2 for i in range(3)}}, simultaneous=True)) == 0
    checks.check("C4", legendre, "the curvature member's first-order momentum terms, from the ledger and the field momentum, are minus block 144's velocity terms at v = k/m: the Hamiltonian is block 144's pull changed to momenta, plus T1's static term")


# ============================================================================================ family D
def pair_hamiltonian(A, B, C, s2, G, m, p, R, NV, bodies):
    h = 0
    for a in bodies:
        h += m[a] + p[a].dot(p[a]) / (2 * m[a]) - p[a].dot(p[a]) ** 2 / (8 * m[a] ** 3)
    for a in bodies:
        for b in bodies:
            if a < b:
                r = R[(a, b)]
                n = NV[(a, b)]
                h += -G * m[a] * m[b] / r * (1 + A * (p[a].dot(p[a]) / m[a] ** 2 + p[b].dot(p[b]) / m[b] ** 2)
                                             + B * p[a].dot(p[b]) / (m[a] * m[b]) + C * n.dot(p[a]) * n.dot(p[b]) / (m[a] * m[b]))
    h += s2 * G ** 2 / 2 * sum(m[a] * sum(m[b] / R[(a, b)] for b in bodies if b != a) ** 2 for a in bodies)
    return h


def family_d(checks: Checks) -> None:
    G = sp.Symbol("G", positive=True)
    A, B, C, s2 = sp.symbols("a b c s2")
    m = sp.symbols("m1:4", positive=True)
    p = [sp.Matrix(sp.symbols("p%d_1:4" % (i + 1), real=True)) for i in range(3)]
    R, NV = {}, {}
    for a in range(3):
        for b in range(a + 1, 3):
            R[(a, b)] = R[(b, a)] = sp.Symbol("r%d%d" % (a + 1, b + 1), positive=True)
            NV[(a, b)] = sp.Matrix(sp.symbols("n%d%d_1:4" % (a + 1, b + 1), real=True))
            NV[(b, a)] = -NV[(a, b)]
    h = sp.expand(pair_hamiltonian(A, B, C, s2, G, m, p, R, NV, range(3)).subs({p[2][i]: 0 for i in range(3)}))
    per_mass = sp.expand(sp.diff(h, m[2]).subs(m[2], 0) - 1)
    phi = [-G / R[(a, 2)] for a in range(2)]
    U = -G * m[0] * m[1] / R[(0, 1)]
    cross = 0 if mut("outside_static_cross_term_dropped") else s2 * U
    expected = sum(phi[a] * (m[a] + A * p[a].dot(p[a]) / m[a] + cross) for a in range(2)) + s2 * G ** 2 / 2 * (m[0] / R[(0, 2)] + m[1] / R[(1, 2)]) ** 2
    checks.check("D1", sp.expand(per_mass - expected) == 0,
                 "a pair near a third body at rest: the Hamiltonian's coupling per unit outside mass is sum_a Phi_a [m_a + 2a T_a + s2 U] + s2 (G^2/2)(m1/r13 + m2/r23)^2, the last smaller by r12/R")
    mu = m[0] * m[1] / (m[0] + m[1])
    x = sp.Matrix(sp.symbols("x1:4", real=True))
    q = sp.Matrix(sp.symbols("q1:4", real=True))
    k = sp.Symbol("k", positive=True)
    rn = sp.sqrt(x.dot(x))
    h0 = q.dot(q) / (2 * mu) - k / rn
    br = sum(sp.diff(x.dot(q), x[i]) * sp.diff(h0, q[i]) - sp.diff(x.dot(q), q[i]) * sp.diff(h0, x[i]) for i in range(3))
    checks.check("D2", sp.simplify(br - (q.dot(q) / mu - k / rn)) == 0,
                 "scalar virial bracket: {x.q, H0} = 2T + U with U = -k/r, so 2<T> = -<U> in a bound state")
    M = m[0] + m[1]
    Tv, Uv = sp.symbols("T U")
    passive = M + 2 * A * Tv + 2 * s2 * Uv
    energy = M + Tv + Uv
    virial = -Uv / 2 if not mut("scalar_virial_forged") else -Uv
    gap = sp.expand((passive - energy).subs(Tv, virial))
    general_ok = sp.simplify(gap - (2 * s2 - A - HALF) * Uv) == 0
    pw = sp.Symbol("p", positive=True)
    member_ok = sp.simplify(gap.subs({A: sp.Rational(3, 2), s2: 1})) == 0
    family_ok = sp.simplify(gap.subs({A: HALF + 1 / pw, s2: 1}) - (1 - 1 / pw) * Uv) == 0
    checks.check("D3", general_ok and member_ok and family_ok,
                 "passive mass M + 2a<T> + 2 s2 <U> minus the pair's energy M + <T> + <U> is (2 s2 - a - 1/2)<U>: zero for the curvature member (a = 3/2, s2 = 1); (1 - 1/p)<U> for the bilinear member X = l^(p/2)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    m1, m2, k, r = sp.symbols("m1 m2 k r", positive=True)
    M = m1 + m2
    mu = m1 * m2 / M
    P = sp.Matrix(sp.symbols("P1:4"))
    q = sp.Matrix(sp.symbols("q1:4"))
    n = sp.Matrix(sp.symbols("n1:4"))
    A, B, C = sp.Rational(3, 2), (-4 if mut("inertia_delay_term_dropped") else -sp.Rational(7, 2)), (0 if mut("inertia_delay_term_dropped") else -HALF)
    p1 = m1 / M * P + q
    p2 = m2 / M * P - q
    h1 = (-p1.dot(p1) ** 2 / (8 * m1 ** 3) - p2.dot(p2) ** 2 / (8 * m2 ** 3)
          - k / r * (A * (p1.dot(p1) / m1 ** 2 + p2.dot(p2) / m2 ** 2) + B * p1.dot(p2) / (m1 * m2) + C * n.dot(p1) * n.dot(p2) / (m1 * m2)))
    sv = sp.Symbol("sv")
    coef = sp.expand(h1.subs({P[i]: sv * P[i] for i in range(3)}, simultaneous=True)).coeff(sv, 2)
    pn2 = P.dot(P)
    T = q.dot(q) / (2 * mu)
    TP = P.dot(q) ** 2 / (2 * mu * pn2)
    U = -k / r
    UP = -k * n.dot(P) ** 2 / (r * pn2)
    delta = coef / (pn2 / (2 * M))
    W1 = sp.expand(T + U + M * delta)            # (W - 1) M before averaging: E0 = M + T + U, 1/M_in = (1 + delta)/M
    tpa, upa, ta, ua = sp.symbols("TPavg UPavg Tavg Uavg")
    rep = sp.expand(-(T + 2 * TP) + 2 * ((2 * A + B) * U + C * UP) + T + U)
    rep_ok = sp.simplify(W1 - rep) == 0
    averaged = (-(ta + 2 * tpa) + 2 * ((2 * A + B) * ua + C * upa) + ta + ua).subs(tpa, -upa / 2)
    w_ok = sp.simplify(averaged) == 0
    checks.check("E1", rep_ok and w_ok,
                 "the same Hamiltonian's P^2 coefficient, with the tensor virial 2<T_P> = -<U_P>, gives W = 1 along every axis for (a, b, c) = (3/2, -7/2, -1/2): the pair's inertia is its energy (block 144 T4 re-checked)")
    Mv, Tv, Uv = sp.symbols("Mv Tv Uv", positive=True)
    ratio = sp.simplify(((Mv + 2 * A * Tv + 2 * Uv) / (Mv + Tv + Uv)).subs(Tv, -Uv / 2))
    checks.check("E2", w_ok and ratio == 1, "passive mass M + 3<T> + 2<U> over inertia M + <T> + <U> is exactly 1 with 2<T> = -<U>: a pair bound by the curvature member's pull falls in a distant body's pull like one body, at first order in its binding")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 60, 62, 101, 134, 135, 136 and 140 as landed on main (the static curvature member and its family, the member's quadratic action, one light cone, the bond shift and the long-wave kinematics), with block 144 placed; it reports how a pair bound by the member's pull falls in the pull of a distant body at first order in its binding; nothing is adopted and no gravitational claim is made.",
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
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "DeWitt", "Hojman", "Kuchar", "Kuchař", "Teitelboim", "Dirac", "Bergmann", "Lorentz", "Kato", "Rosenblum", "Ruelle", "Amrein", "Georgescu", "Enss", "Lebesgue", "Levinson", "Birman", "Krein", "Schwarz", "Liouville", "Morse", "Infeld", "Hoffmann", "Fierz", "Darwin", "Laue", "Poincare", "Poincaré", "Grommer", "Belinfante", "Rosenfeld", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
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
    "per_element: executed - the static ledger of three bodies to second order from block 60's charges, for every bilinear member",
    "per_site: executed - the moving-body ledger for the member X = l^(p/2), and the field momentum at the shift's constraint",
    "per_mode: executed - the first-order Hamiltonian against block 144's pull changed to momenta",
    "per_block: executed - a pair's coupling to a distant body's potential, the scalar and tensor virial brackets, the passive mass and the inertia",
    "lattice_wide: long wavelength; first order in the binding and in the outside field; point constituents with their own fields dropped",
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
    print("scope: the static ledger to second order is the same for every bilinear member; moving bodies carry (1/2 + 1/p) k^2/m^2; a pull-bound pair has passive mass equal to its energy only for the curvature member p = 1, and with the inertia of block 144 such a pair falls like one body at first order in its binding; supervisor derivation, unrefereed; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
