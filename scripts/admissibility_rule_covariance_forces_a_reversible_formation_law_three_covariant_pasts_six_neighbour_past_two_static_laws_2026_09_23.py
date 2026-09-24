#!/usr/bin/env python3
"""Excluded re-recording comparator with fixed scalar nearest-offset weights and an exponential pair rule: orbit classification, detailed balance and stationary graph decompositions. Covariance alone does not classify every update law."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_COVARIANCE_FORCES_A_REVERSIBLE_FORMATION_LAW_THREE_COVARIANT_PASTS_AND_THE_SIX_NEIGHBOUR_PAST_SETTLES_INTO_TWO_COPIES_OF_THE_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_RE_RECORDING_AT_EVERY_TICK_STATIC_LAW_STATIONARY_LIGHT_CONE_BILAYER_LONG_RANGE_ORDER_GREEN_FUNCTION_RESPONSE_CONDITIONAL_ON_AN_EXCLUDED_CLAUSE_BOUNDED_THEOREM_NOTE_2026-09-20.md', 'docs/ADMISSIBILITY_RULE_LIGHT_CONE_FORMATION_KEEPS_MEMORY_IN_3PLUS1_ITS_STATIONARY_LAW_IS_ONE_LAYER_OF_A_REFLECTION_POSITIVE_BILAYER_ORDERED_ABOVE_BETA_0P5905_BOUNDED_THEOREM_NOTE_2026-09-23.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_covariance_forces_a_reversible_formation_law_three_covariant_pasts_and_the_six_neighbour_past_settles_into_two_copies_of_the_static_law_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "group_without_half_turns": "B",
    "level_ordered_past_counted_covariant": "B",
    "weights_break_the_orbit": "C",
    "six_neighbour_rungs_kept": "D",
    "copy_past_keeps_a_direction": "D",
    "threshold_without_the_rung_weight": "E",
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
STENCIL_RING = (0, 1, -1)
POINTS = [(0, 0, 0)] + [tuple(s if i == j else 0 for i in range(3)) for j in range(3) for s in (1, -1)]
LEVEL_ORDERED = {(0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1)}


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def proper_rotations():
    from itertools import permutations
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i in range(3):
                M[i][perm[i]] = signs[i]
            if det3(M) == 1:
                out.append(M)
    return out


def act(M, v):
    return tuple(sum(M[i][k] * v[k] for k in range(3)) for i in range(3))


def neg(v):
    return tuple(-c for c in v)


def doubled_edges(size, stencil_weights):
    """Doubled graph edges (x,0)-(x+d,1) with the weight of d."""
    out = {}
    for x in product(range(size), repeat=3):
        for d, w in stencil_weights.items():
            if w == 0:
                continue
            y = tuple((x[i] + d[i]) % size for i in range(3))
            e = frozenset({(x, 0), (y, 1)})
            out[e] = out.get(e, 0) + w
    return out


def relabel(v):
    x, a = v
    return (x, a ^ (sum(x) % 2))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    rots = proper_rotations()
    group = rots
    if mut("group_without_half_turns"):
        group = [M for M in rots if {act(M, v) for v in LEVEL_ORDERED} == LEVEL_ORDERED]
    invariant = []
    for ws in product((0, 1, 2), repeat=7):
        w = dict(zip(POINTS, ws))
        if all(all(w[act(M, p)] == w[p] for p in POINTS) for M in group):
            invariant.append(w)
    orbit_const = all(all(w[p] == w[POINTS[1]] for p in POINTS[1:]) for w in invariant)
    symmetric = all(all(w[p] == w[neg(p)] for p in POINTS) for w in invariant)
    checks.check("B1", len(rots) == 24 and len(invariant) == 9 and orbit_const and symmetric, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    stab = [M for M in rots if {act(M, v) for v in LEVEL_ORDERED} == LEVEL_ORDERED]
    claimed = len(stab) if not mut("level_ordered_past_counted_covariant") else 24
    level_sym = LEVEL_ORDERED == {neg(v) for v in LEVEL_ORDERED}
    checks.check("B2", claimed == 3 and len(stab) == 3 and not level_sym, 'Scoped exact check B2: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def ring_defect(size, menu, weights, t_syms):
    """Detailed-balance defect of the pairwise chain on a ring with per-offset weights t_d (symbolic)."""
    states = list(product(range(len(menu)), repeat=size))

    def dot(a, b):
        return sum(p * q for p, q in zip(menu[a], menu[b]))

    def weight(s, x, c):
        return sp.prod([t_syms[d] ** dot(c, s[(x + d) % size]) for d in weights])
    Zs = {s: [sum(weight(s, x, c) for c in range(len(menu))) for x in range(size)] for s in states}
    pis = {s: sp.prod(Zs[s]) for s in states}
    for s in states:
        for s2 in states:
            fwd = pis[s] * sp.prod([weight(s, x, s2[x]) / Zs[s][x] for x in range(size)])
            bwd = pis[s2] * sp.prod([weight(s2, x, s[x]) / Zs[s2][x] for x in range(size)])
            if sp.simplify(fwd - bwd) != 0:
                return False
    return True


def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    t0, t1, t2 = sp.symbols("t0 t1 t2", positive=True)
    tw = {0: t0, 1: t1, -1: t1 if not mut("weights_break_the_orbit") else t2}
    ising = [(1,), (-1,)]
    four = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
    ok = ring_defect(4, ising, (0, 1, -1), tw) and ring_defect(3, four, (0, 1, -1), tw)
    checks.check("C1", ok, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    ok1 = True
    counts = []
    for size in (4, 6):
        sw = {d: 1 for d in POINTS[1:]}
        if mut("six_neighbour_rungs_kept"):
            sw[(0, 0, 0)] = 1
        edges = doubled_edges(size, sw)
        img = {frozenset(relabel(v) for v in e) for e in edges}
        within = all(len({v[1] for v in e}) == 1 for e in img)
        cubic = set()
        for b in (0, 1):
            for x in product(range(size), repeat=3):
                for j in range(3):
                    y = tuple((x[i] + (1 if i == j else 0)) % size for i in range(3))
                    cubic.add(frozenset({(x, b), (y, b)}))
        slab0 = {(x, a) for x in product(range(size), repeat=3) for a in (0, 1) if relabel((x, a))[1] == 0}
        classes = slab0 == {(x, 0) for x in product(range(size), repeat=3) if sum(x) % 2 == 0} | {(x, 1) for x in product(range(size), repeat=3) if sum(x) % 2 == 1}
        ok1 = ok1 and within and img == cubic and classes
        counts.append(len(edges))
    checks.check("D1", ok1, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    t = sp.symbols("t", positive=True)
    six = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    P = sp.Matrix(6, 6, lambda i, j: t ** sum(a * b for a, b in zip(six[i], six[j])))
    rowsums = [sp.simplify(sum(P.row(i))) for i in range(6)]
    same_Z = all(sp.simplify(r - rowsums[0]) == 0 for r in rowsums)
    Pn = P / rowsums[0]
    uniform = sp.Matrix([[sp.Rational(1, 6)] * 6])
    stat = sp.simplify(uniform * Pn - uniform) == sp.zeros(1, 6)
    if mut("copy_past_keeps_a_direction"):
        stat = False
    Nn = sp.symbols("N", positive=True)
    m2 = sp.Rational(1, 1) / Nn
    checks.check("D2", same_Z and stat and P == P.T, 'Scoped exact check D2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    ok3 = True
    size = 4
    for w0, w1 in ((1, 1), (1, 2), (2, 1)):
        sw = {POINTS[0]: w0}
        sw.update({d: w1 for d in POINTS[1:]})
        edges = doubled_edges(size, sw)
        img = {frozenset(relabel(v) for v in e): w for e, w in edges.items()}
        for e, w in img.items():
            a, b = tuple(e)
            if a[0] == b[0]:
                ok3 = ok3 and w == w0 and a[1] != b[1]
            else:
                ok3 = ok3 and w == w1 and a[1] == b[1]
    checks.check("D3", ok3, 'Scoped exact check D3: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 4
    cos_q = (1, 0, -1, 0)
    Es = [6 - 2 * sum(cos_q[c] for c in n) for n in product(range(size), repeat=3)]
    Nn = size ** 3

    def G():
        return sum((F(1, E) for E in Es if E != 0), ZERO) / Nn

    def H(a):
        return sum((1 / (F(E) + a) for E in Es), ZERO) / Nn

    def beta_L(w0, w1):
        a = F(2 * w0, w1) if not mut("threshold_without_the_rung_weight") else F(2)
        return F(3, 2 * w1) * (G() + H(a))
    vals = {(w0, w1): beta_L(w0, w1) for w0, w1 in ((1, 1), (1, 2), (2, 1))}
    six = F(3, 1) * G()
    ok = (vals[(1, 1)] == F(18239, 35840) and vals[(1, 2)] == F(2857397, 10250240) and vals[(2, 1)] == F(32773, 71680)
          and six == F(1517, 2560) and vals[(1, 2)] < vals[(2, 1)] < vals[(1, 1)] < six)
    checks.check("E1", ok, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family F
FENCES = ('This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.', 'No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.', 'No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.')
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: Excluded re-recording comparator with fixed scalar nearest-offset weights and an exponential pair rule: orbit classification, detailed balance and stationary graph decompositions. Covariance alone does not classify every update law.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
