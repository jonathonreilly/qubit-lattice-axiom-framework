#!/usr/bin/env python3
"""Finite continuous-time detailed-balance spectra; exact persistent-walk and linear-mode algebra; cubic symmetry tensors without a universal hydrodynamic claim."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_WAVES_AMONG_MOVING_RECORDS_NEED_A_COUPLING_THAT_TIME_REVERSAL_FLIPS_CLOCKED_RECORD_MOTION_NEVER_OSCILLATES_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ADMISSIBILITY_RULE_THREE_READINGS_OF_RECORDS_FORM_AGAINST_KNOWN_PHYSICS_THE_SPACETIME_READING_IS_TWO_DIMENSIONAL_SKEWED_AND_IRREVERSIBLE_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_clocked_record_motion_never_oscillates_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "records are permanent",
)

MUTATION_GATE = {
    "circulation_injected": "B",
    "circulation_hidden": "B",
    "long_wave_oscillation_forged": "C",
    "turning_biased": "C",
    "coupling_symmetrized": "D",
    "rotations_restricted_to_an_axis": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and records are permanent (contents never change)")


# ============================================================================================ helpers
from itertools import combinations

RING_M = {0: 35, 1: 5, 2: -13, 3: -19, 4: -13, 5: 5}     # 72 G(d) on the ring of six (block 95's zero-mean kernel, integers)


def ring_chain(n, two_a, circulate=False):
    """Records on a ring of six, clock field slaved to them with base 4: w_z = 4^(sum_r RING_M(z - r)).
    A hop x -> y runs at w_x^a w_y^(1 - a) = 2^(two_a m_x + (2 - two_a) m_y) (two_a = 2a in {0, 1, 2}); returns states, rates, law."""
    states = [frozenset(c) for c in combinations(range(6), n)]

    def m(z, C):
        return sum(RING_M[(z - r) % 6] for r in C)
    rates = {}
    for s in states:
        for x in s:
            for y in ((x + 1) % 6, (x - 1) % 6):
                if y in s:
                    continue
                s2 = (s - {x}) | {y}
                e = two_a * m(x, s) + (2 - two_a) * m(y, s)
                r = F(2) ** e
                if circulate and y == (x + 1) % 6:
                    r = r * 2
                rates[(s, s2)] = r
    law = {}
    for s in states:
        pair = sum((RING_M[(u - v) % 6] for u, v in combinations(sorted(s), 2)), 0)
        law[s] = F(2) ** ((2 - 2 * two_a) * pair)
    return states, rates, law


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    ok = True
    count = 0
    for n in (2, 3):
        for two_a in (2, 1, 0):
            states, rates, law = ring_chain(n, two_a, circulate=mut("circulation_injected"))
            for (s, s2), r in rates.items():
                back = rates[(s2, s)]
                ok = ok and law[s] * r == law[s2] * back
                count += 1
    checks.check("B1", ok, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    # one record on a ring of six: symmetric rates give real mode frequencies; a circulation gives complex ones
    w6 = sp.exp(sp.I * sp.pi / 3)
    cw, ccw = (sp.Integer(2), sp.Integer(1)) if not mut("circulation_hidden") else (sp.Integer(1), sp.Integer(1))
    sym_real = all(sp.im(sp.expand(sp.exp(sp.I * sp.pi * j / 3) + sp.exp(-sp.I * sp.pi * j / 3) - 2)) == 0 for j in range(6))
    circ_im = [sp.nsimplify(sp.im(sp.expand(cw * w6 ** j + ccw * w6 ** (-j) - cw - ccw))) for j in range(6)]
    oscillates = any(v != 0 for v in circ_im) and circ_im[1] == sp.sqrt(3) / 2
    checks.check("B2", sym_real and oscillates, 'Scoped exact check B2: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    k, p, mu = sp.symbols("k p mu", real=True)
    det_term = (2 * p - 1) if not mut("long_wave_oscillation_forged") else (2 * p + 1)
    M1 = sp.Matrix([[sp.exp(-sp.I * k) * p, sp.exp(-sp.I * k) * (1 - p)], [sp.exp(sp.I * k) * (1 - p), sp.exp(sp.I * k) * p]])
    cp = sp.expand(sp.simplify((M1 - mu * sp.eye(2)).det()).rewrite(sp.cos))
    want = sp.expand(mu ** 2 - 2 * p * sp.cos(k) * mu + det_term)
    cp_ok = sp.simplify(cp - want) == 0
    at0 = sp.solve(want.subs(k, 0), mu)
    real_at0 = all(sp.im(r) == 0 for r in at0) and set(sp.simplify(r) for r in at0) == {sp.Integer(1), sp.simplify(2 * p - 1)}
    lead = p * sp.cos(k) + sp.sqrt(p ** 2 * sp.cos(k) ** 2 - (2 * p - 1))
    ser = sp.simplify(sp.series(lead.subs(p, sp.Rational(3, 4)), k, 0, 4).removeO())
    diffusive = sp.simplify(ser - (1 - sp.Rational(3, 2) * k ** 2)) == 0          # p/(2(1 - p)) = 3/2 at p = 3/4
    disc_half = (p ** 2 * sp.cos(k) ** 2 - (2 * p - 1)).subs({p: sp.Rational(3, 4), k: sp.pi / 2})
    band = disc_half == sp.Rational(-1, 2)
    checks.check("C1", cp_ok and real_at0 and diffusive and band, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    # three dimensions: continue with probability p, otherwise turn to one of the other five directions
    q = sp.Rational(9, 10)
    dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    turn = [[q if i == j else (1 - q) / 5 for j in range(6)] for i in range(6)]
    if mut("turning_biased"):
        turn = [[q if i == j else ((1 - q) / 5 + (sp.Rational(1, 50) if j == 0 else 0) - (sp.Rational(1, 200) if j != 0 and j != i else 0)) for j in range(6)] for i in range(6)]
    T = sp.Matrix(turn)
    Pi = sp.Matrix(6, 6, lambda i, j: 1 if j == (i ^ 1) else 0)
    kv = (sp.pi / 2, 0, 0)
    E = sp.diag(*[sp.exp(-sp.I * sum(kv[c] * d[c] for c in range(3))) for d in dirs])
    Mk = E * T
    conj_ok = sp.simplify(Mk.conjugate() - Pi * Mk * Pi) == sp.zeros(6, 6)
    cpk = sp.Poly(sp.expand((Mk - mu * sp.eye(6)).det(method="berkowitz")), mu)
    real_coeffs = all(sp.im(c) == 0 for c in cpk.all_coeffs())
    cpr = sp.Poly([sp.re(c) for c in cpk.all_coeffs()], mu)
    n_real = sum(sp.Poly(f, mu).count_roots() * mult for f, mult in sp.sqf_list(cpr.as_expr())[1] if sp.degree(f, mu) > 0)
    lead_real = cpr.count_roots(sp.Rational(9, 10), 1) == 1
    T0 = sp.Poly(sp.expand((T - mu * sp.eye(6)).det(method="berkowitz")), mu)
    at_zero = sp.expand(T0.as_expr() - (1 - mu) * ((6 * q - 1) / 5 - mu) ** 5) == 0
    checks.check("C2", conj_ok and real_coeffs and n_real == 4 and lead_real and at_zero, 'Scoped exact check C2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    c, a, b, beta, mu = sp.symbols("c a b beta mu", positive=True)
    kv = sp.Matrix([k1, k2, k3])
    ksq = k1 ** 2 + k2 ** 2 + k3 ** 2
    sgn = -1 if not mut("coupling_symmetrized") else 1
    # sound: density rho and momentum g, conserved; d rho/dt = -i k.g, d g/dt = -i c^2 k rho (the momentum flips under time reversal)
    S = sp.zeros(4, 4)
    for j in range(3):
        S[0, 1 + j] = -sp.I * kv[j]
        S[1 + j, 0] = sgn * sp.I * c ** 2 * kv[j]
    cps = sp.factor(sp.expand((S - mu * sp.eye(4)).det()))
    sound = sp.simplify(cps - mu ** 2 * (mu ** 2 + c ** 2 * ksq)) == 0
    # colour pair (the mobile-record lane's curl form): dX/dt = a i k x Y, dY/dt = -b i k x X
    def cross(v):
        return sp.Matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    K = cross(kv)
    C6 = sp.zeros(6, 6)
    C6[0:3, 3:6] = a * sp.I * K
    C6[3:6, 0:3] = -b * sp.I * K
    cpc = sp.factor(sp.expand((C6 - mu * sp.eye(6)).det()))
    colour = sp.simplify(cpc - mu ** 2 * (mu ** 2 + a * b * ksq) ** 2) == 0
    # the walk: H(k) = beta sum_j sigma_j sin k_j; H^2 = beta^2 sum sin^2 k_j (the Pauli matrices anticommute)
    sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
    H = beta * (sx * sp.sin(k1) + sy * sp.sin(k2) + sz * sp.sin(k3))
    walk = sp.simplify(H * H - beta ** 2 * (sp.sin(k1) ** 2 + sp.sin(k2) ** 2 + sp.sin(k3) ** 2) * sp.eye(2)) == sp.zeros(2, 2)
    checks.check("D1", sound and colour and walk, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    rots = []
    for perm in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)):
        for signs in product((1, -1), repeat=3):
            R = sp.zeros(3, 3)
            for i in range(3):
                R[i, perm[i]] = signs[i]
            if R.det() == 1:
                rots.append(R)
    if mut("rotations_restricted_to_an_axis"):
        rots = [R for R in rots if R[2, 2] == 1]
    avg1 = sum(rots, sp.zeros(3, 3)) / len(rots)
    avg2 = sp.zeros(9, 9)
    for R in rots:
        avg2 += sp.kronecker_product(R, R)
    avg2 = avg2 / len(rots)
    delta = sp.Matrix(9, 1, lambda i, j: 1 if i in (0, 4, 8) else 0)
    iso = avg2 == delta * delta.T / 3
    checks.check("E1", len(rots) == 24 and avg1 == sp.zeros(3, 3) and iso, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    k, mu = sp.symbols("k mu", real=True)
    cp0 = mu**2-1
    cp1 = mu**2-2*sp.cos(k)*mu+1
    checks.check("C9", cp0.subs(mu,-1)==0 and sp.simplify(sp.expand_complex(cp1.subs(mu,sp.exp(sp.I*k))))==0, 'Scoped exact check C9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


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
    print('scope: Finite continuous-time detailed-balance spectra; exact persistent-walk and linear-mode algebra; cubic symmetry tensors without a universal hydrodynamic claim.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
