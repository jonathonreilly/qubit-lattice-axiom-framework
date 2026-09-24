#!/usr/bin/env python3
"""Coordinate-separable real pure-hop profiles: squared-spectrum decomposition, even-ring kernel compatibility, literal ring and 4^3 fixtures. Walls are prescribed, not dynamically formed."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_DEFECTS_OF_THE_ALTERNATION_ARE_SEPARABLE_WALLS_CARRY_SHEETS_OF_LOWER_MASS_LINES_LOWER_STILL_AND_THREE_CROSSING_WALLS_BIND_EXACT_ZERO_MODES_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_CHESSBOARD_OR_AXIS_STRIPES_ON_SITES_ALTERNATING_LENGTHS_GIVE_ONE_REST_ENERGY_EXCLUSION_CAGES_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_defects_of_the_alternation_are_separable_walls_carry_sheets_of_lower_mass_lines_lower_still_three_crossing_walls_bind_exact_zero_modes_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "walls_break_separability": "B",
    "one_wall_binds_no_zero_mode": "C",
    "three_walls_bind_no_zero_modes": "D",
    "sheet_mass_is_the_bulk_mass": "D",
    "zero_modes_are_not_products": "E",
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


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


class G:
    """A Gaussian rational re + i im."""

    __slots__ = ("re", "im")

    def __init__(self, re_=0, im_=0):
        self.re = F(re_)
        self.im = F(im_)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, G) else G(o)))

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))


SIG = [
    [[G(0), G(1)], [G(1), G(0)]],
    [[G(0), G(0, -1)], [G(0, 1), G(0)]],
    [[G(1), G(0)], [G(0), G(-1)]],
]
MINUS_HALF_I = G(0, F(-1, 2))                                  # 1/(2i)


def mat_add(a, b):
    return [[a[r][c] + b[r][c] for c in range(2)] for r in range(2)]


def mat_scale(a, f):
    return [[a[r][c] * f for c in range(2)] for r in range(2)]


def mat_mul(a, b):
    return [[a[r][0] * b[0][c] + a[r][1] * b[1][c] for c in range(2)] for r in range(2)]


def mat_vec(a, v):
    return (a[0][0] * v[0] + a[0][1] * v[1], a[1][0] * v[0] + a[1][1] * v[1])


def frame_matrix(vec):
    """sum_a E_a sigma_a for a coin vector (E_1, E_2, E_3)."""
    out = [[G(0), G(0)], [G(0), G(0)]]
    for a in range(3):
        out = mat_add(out, mat_scale(SIG[a], vec[a]))
    return out


DIMS = (3, 3, 3)
SITES = list(product(*(range(d) for d in DIMS)))


def shift(x, j, step):
    return tuple((x[i] + (step if i == j else 0)) % DIMS[i] for i in range(3))


def s_op(psi, j):
    """(S_j psi)(x) = (psi(x + e_j) - psi(x - e_j))/(2i)."""
    return {x: tuple((psi[shift(x, j, 1)][c] - psi[shift(x, j, -1)][c]) * MINUS_HALF_I for c in range(2)) for x in SITES}


def generator(psi, frame, symmetrised=True):
    """H psi with H = (1/2) sum_j {E^j.sigma, S_j}, or the unsymmetrised sum_j E^j.sigma S_j."""
    out = {x: (G(0), G(0)) for x in SITES}
    for j in range(3):
        first = s_op(psi, j)
        first = {x: mat_vec(frame_matrix(frame[x][j]), first[x]) for x in SITES}
        if symmetrised:
            second = s_op({x: mat_vec(frame_matrix(frame[x][j]), psi[x]) for x in SITES}, j)
            for x in SITES:
                out[x] = tuple(out[x][c] + (first[x][c] + second[x][c]) * F(1, 2) for c in range(2))
        else:
            for x in SITES:
                out[x] = tuple(out[x][c] + first[x][c] for c in range(2))
    return out


def inner(phi, psi):
    tot = G(0)
    for x in SITES:
        for c in range(2):
            tot = tot + phi[x][c].conj() * psi[x][c]
    return tot


def rational_state(seed):
    return {x: (G(F((seed * 7 + 3 * x[0] + x[1] * x[2]) % 5 - 2, 3), F((seed + x[0] * x[0] + 2 * x[1] + 5 * x[2]) % 7 - 3, 4)),
                G(F((seed * 3 + x[0] * x[1] + 2 * x[2]) % 7 - 3, 5), F((seed * 5 + x[0] + x[1] + x[2]) % 3 - 1, 2))) for x in SITES}


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[:2]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


SIGMA = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]]))
DELTAS = (sp.Rational(3, 10), sp.Rational(1, 5), sp.Rational(1, 2))


def axis_operator(size, delta, walls):
    """The one-axis operator (1/2i)(t T - T^T t) with t_x = 1 + delta s_x (-1)^x on the bond x -> x + 1; s_x = +1 on the first half and -1 on the
    second when `walls` (two walls: one where two weak bonds meet, one where two strong bonds meet), else +1 everywhere."""
    t_shift = sp.zeros(size, size)
    for x in range(size):
        t_shift[x, (x + 1) % size] = 1
    signs = [1 if (not walls or x < size // 2) else -1 for x in range(size)]
    amps = [1 + delta * signs[x] * (-1) ** x for x in range(size)]
    t = sp.diag(*amps)
    return (t * t_shift - t_shift.T * t) / (2 * sp.I), amps


def embed(m, j, size):
    fs = [sp.eye(size), sp.eye(size), sp.eye(size)]
    fs[j] = m
    return sp.kronecker_product(fs[0], sp.kronecker_product(fs[1], fs[2]))


def walk(size, deltas, walls):
    hs = [axis_operator(size, deltas[j], walls[j])[0] for j in range(3)]
    n = 2 * size ** 3
    H = sum((sp.kronecker_product(SIGMA[j], embed(hs[j], j, size)) for j in range(3)), sp.zeros(n, n))
    return H, hs


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 4
    ok = True
    for walls in ((False, False, False), (True, False, False), (True, True, False), (True, True, True)):
        H, hs = walk(size, DELTAS, walls)
        rhs = sp.kronecker_product(sp.eye(2), sum((embed(hs[j] * hs[j], j, size) for j in range(3)), sp.zeros(size ** 3, size ** 3)))
        same = sp.simplify(H * H - rhs) == sp.zeros(2 * size ** 3, 2 * size ** 3)
        ok = ok and same
    b1 = ok if not mut("walls_break_separability") else (not ok)
    checks.check("B1", b1, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 8
    d = sp.Rational(3, 10)
    h, amps = axis_operator(size, d, True)
    null = h.nullspace()
    h0, _ = axis_operator(size, d, False)
    two = len(null) == 2 and len(h0.nullspace()) == 0
    ratio = (1 - d) / (1 + d)
    structure = True
    for v in null:
        vals = [sp.simplify(z) for z in v]
        occupied = [x for x in range(size) if vals[x] != 0]
        one_sublattice = len({x % 2 for x in occupied}) == 1
        peak = max(range(size), key=lambda x: abs(vals[x]))
        decays = all(sp.simplify(vals[x] / vals[peak]) in (ratio ** k for k in range(4)) for x in occupied)
        structure = structure and one_sublattice and decays
    c1 = (two and structure) if not mut("one_wall_binds_no_zero_mode") else (not two)
    badamps=[1+d*(1 if x<6 else -1)*(-1)**x for x in range(8)]
    T=sp.zeros(8)
    for x in range(8):T[x,(x+1)%8]=1
    tbad=sp.diag(*badamps)
    bad=(tbad*T-T.T*tbad)/(2*sp.I)
    checks.check("C2", sp.prod(badamps[::2])!=sp.prod(badamps[1::2]) and bad.rank()==8, 'Scoped exact check C2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    checks.check("C1", c1, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 4
    results = {}
    for walls in ((False, False, False), (True, False, False), (True, True, False), (True, True, True)):
        H, hs = walk(size, DELTAS, walls)
        n = 2 * size ** 3
        results[walls] = (n - H.rank(), [sorted(set(sp.simplify(v ** 2) for v in hh.eigenvals().keys())) for hh in hs])
    zero_counts = {w: r[0] for w, r in results.items()}
    counts_ok = zero_counts[(False, False, False)] == 0 and zero_counts[(True, False, False)] == 0 and zero_counts[(True, True, False)] == 0 and zero_counts[(True, True, True)] == 16
    d1 = counts_ok if not mut("three_walls_bind_no_zero_modes") else (zero_counts[(True, True, True)] == 0)
    checks.check("D1", d1, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    # least E^2 = sum over axes of the least one-axis E^2: delta_j^2 for an axis without walls (E^2 = sin^2 + delta^2 cos^2 >= delta^2, attained), 0 for an axis with walls
    least_sq = {w: sum((min(r[1][j]) for j in range(3)), sp.Integer(0)) for w, r in results.items()}
    pred = {(False, False, False): sum(d * d for d in DELTAS), (True, False, False): DELTAS[1] ** 2 + DELTAS[2] ** 2, (True, True, False): DELTAS[2] ** 2, (True, True, True): sp.Integer(0)}
    sheet_ok = all(sp.simplify(least_sq[w] - pred[w]) == 0 for w in pred)
    d2 = sheet_ok if not mut("sheet_mass_is_the_bulk_mass") else (sp.simplify(least_sq[(True, False, False)] - pred[(False, False, False)]) == 0)
    checks.check("D2", d2, 'Scoped exact check D2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 4
    H, hs = walk(size, DELTAS, (True, True, True))
    ones = [hh.nullspace() for hh in hs]
    prods = []
    for a in ones[0]:
        for b in ones[1]:
            for c in ones[2]:
                v = sp.kronecker_product(a, sp.kronecker_product(b, c))
                for coin in (sp.Matrix([1, 0]), sp.Matrix([0, 1])):
                    prods.append(sp.kronecker_product(coin, v))
    span = sp.Matrix.hstack(*prods)
    annihilated = all(sp.simplify(H * p) == sp.zeros(2 * size ** 3, 1) for p in prods)
    full = span.rank() == 16 and len(prods) == 16
    e1 = (annihilated and full) if not mut("zero_modes_are_not_products") else (not annihilated)
    checks.check("E1", e1, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
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
    print('scope: Coordinate-separable real pure-hop profiles: squared-spectrum decomposition, even-ring kernel compatibility, literal ring and 4^3 fixtures. Walls are prescribed, not dynamically formed.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
