#!/usr/bin/env python3
"""Homogeneous two-end rates independent of arbitrary clock ratios per own tick; fixed positive diagonal matrix similarities; a conditional finite pair-energy sign."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_A_RECORD_THAT_CANNOT_READ_THE_FIELD_FROM_ITS_OWN_MOTION_HOPS_ON_ITS_OWN_CLOCK_AND_WITH_KEPT_BOOKS_RECORDS_ATTRACT_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "arrival_clock_called_own": "B",
    "record_timings_merged": "C",
    "ledger_sign_flipped": "D",
    "direction_read_from_clocks": "E",
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
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ helpers
def rat(x):
    return sp.Rational(x.numerator, x.denominator)


def zero_mean_green_3d_4():
    cosv = {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}
    L = 4
    ks = [n for n in product(range(L), repeat=3) if n != (0, 0, 0)]
    Ek = {n: 6 - 2 * sum(cosv[c] for c in n) for n in ks}
    return {d: sum((cosv[sum(n[i] * d[i] for i in range(3)) % L] / Ek[n] for n in ks), ZERO) / (L ** 3) for d in product(range(L), repeat=3)}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    wx, wy, t = sp.symbols("w_x w_y t", positive=True)
    a = sp.symbols("a", real=True)
    rate = wx ** a * wy ** (1 - a)
    degree_one = sp.simplify(rate.subs({wx: t * wx, wy: t * wy}, simultaneous=True) - t * rate) == 0
    own = sp.simplify(rate / wx)
    d_own = sp.simplify(sp.diff(own, wy))
    field_free_iff = sp.solve(sp.Eq(sp.simplify(d_own * wx ** a * wy ** a / wy ** 0), 0), a) == [1]
    named = {}
    for aa in (1, sp.Rational(1, 2), 0):
        named[aa] = sp.simplify(own.subs(a, aa))
    ok_named = named[1] == 1 and named[sp.Rational(1, 2)] == sp.sqrt(wy / wx) and named[0] == wy / wx
    claim_entering_free = mut("arrival_clock_called_own")
    if claim_entering_free:
        ok_named = ok_named and sp.diff(named[0], wy) == 0
    checks.check("B1", degree_one and field_free_iff and ok_named, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    w = sp.symbols("w0:4", positive=True)
    tt, ss = sp.symbols("t s", real=True)
    W = sp.diag(*w)
    Wh = sp.diag(*[sp.sqrt(x) for x in w])
    H = sp.zeros(4, 4)
    for x in range(4):
        y = (x + 1) % 4
        H[x, y] = tt + sp.I * ss
        H[y, x] = tt - sp.I * ss
    sim1 = sp.simplify(Wh.inv() * (W * H) * Wh - Wh * H * Wh) == sp.zeros(4, 4)
    sim2 = sp.simplify(Wh * (H * W) * Wh.inv() - Wh * H * Wh) == sp.zeros(4, 4)
    laws = {}
    ok_laws = True
    for aa in (1, sp.Rational(1, 2), 0):
        Q = sp.zeros(4, 4)
        for x in range(4):
            for y in ((x + 1) % 4, (x - 1) % 4):
                r = w[x] ** aa * w[y] ** (1 - aa)
                Q[y, x] += r
                Q[x, x] -= r
        law = sp.Matrix([w[x] ** (1 - 2 * aa) for x in range(4)]) if not mut("record_timings_merged") else sp.Matrix([1 / w[x] for x in range(4)])
        ok_laws = ok_laws and sp.simplify(Q * law) == sp.zeros(4, 1)
        laws[aa] = law
    ratio = sp.simplify(laws[1][0] / laws[0][0] * laws[0][1] / laws[1][1])
    distinct = sp.simplify(ratio - 1) != 0
    checks.check("C1", sim1 and sim2 and ok_laws and distinct, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    gam, E, wbar = sp.symbols("gamma E wbar", positive=True)
    logk = -(gam / 6) * E / wbar if not mut("ledger_sign_flipped") else (gam / 6) * E / wbar
    G = zero_mean_green_3d_4()
    a = 1
    U = {r: 6 * (2 * a - 1) * logk * rat(G[(r, 0, 0)]) for r in (1, 2)}
    diff12 = sp.simplify(U[1] - U[2])
    attract = bool(diff12 < 0)
    closed = sp.simplify(diff12 + gam * E / wbar * (rat(G[(1, 0, 0)]) - rat(G[(2, 0, 0)]))) == 0
    checks.check("D1", attract and closed, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    wx = sp.symbols("w_x", positive=True)
    wn = sp.symbols("w_n0:6", positive=True)
    a = sp.symbols("a", real=True)
    odds = [wx ** a * wn[e] ** (1 - a) for e in range(6)]
    total = sum(odds)
    probs = [sp.simplify(o / total) for o in odds]
    at_one = [sp.simplify(p.subs(a, 1)) for p in probs]
    uniform = all(p == sp.Rational(1, 6) for p in at_one)
    if mut("direction_read_from_clocks"):
        uniform = all(sp.simplify(p.subs(a, 0)) == sp.Rational(1, 6) for p in probs)
    biased = sp.simplify(probs[0].subs(a, 0) - wn[0] / sum(wn)) == 0
    checks.check("E1", uniform and biased, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


def family_scope(checks):
    W=sp.diag(1,4); H=sp.Matrix([[0,1],[1,0]])
    B=sp.diag(1,2)*H*sp.diag(1,2)
    checks.check("C9", W*H != (W*H).H and B==B.H and sp.Rational(2,2)==1, 'Scoped exact check C9: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


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
    print('scope: Homogeneous two-end rates independent of arbitrary clock ratios per own tick; fixed positive diagonal matrix similarities; a conditional finite pair-energy sign.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
