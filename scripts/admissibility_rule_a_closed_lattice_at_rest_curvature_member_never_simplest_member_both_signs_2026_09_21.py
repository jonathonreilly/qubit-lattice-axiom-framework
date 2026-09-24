#!/usr/bin/env python3
"""On a finite connected closed symmetric graph the positive-function divided-difference identity excludes nonzero net diagonal sources in the supplied curvature equations, with uniform zero-source fields as an explicit exception. Nonconstant positive solutions of the simplest supplied equation require both source signs. A distinct-site pair on a translation-invariant torus has the stated exact tuning condition."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_A_CLOSED_LATTICE_AT_REST_NEVER_IN_THE_CURVATURE_MEMBER_WHATEVER_THE_SIGNS_IN_THE_SIMPLEST_MEMBER_ONLY_WITH_BODIES_OF_BOTH_SIGNS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_STRONG_FIELD_EXACTLY_BODIES_AT_REST_MAKE_THE_CLOCK_LAW_LINEAR_IN_THE_ROOT_OF_THE_RATE_THE_LEDGER_IS_A_SURFACE_TERM_BOUNDED_BY_A_CAPACITY_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_closed_lattice_at_rest_never_in_the_curvature_member_whatever_the_signs_in_the_simplest_member_only_with_bodies_of_both_signs_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "closed_lattice_identity_has_the_other_sign": "B",
    "curvature_member_residuals_can_cancel": "B",
    "pair_condition_ignores_the_separation": "C",
    "detuned_pair_is_at_rest": "C",
    "closed_lattice_at_rest_with_positive_bodies_only": "D",
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


SIDE = 4
SITES3 = list(product(range(SIDE), repeat=3))
INDEX = {x: i for i, x in enumerate(SITES3)}


def neighbours(x):
    for a in range(3):
        for step in (1, -1):
            y = list(x)
            y[a] = (y[a] + step) % SIDE
            yield tuple(y)


BONDS = [(x, tuple((x[i] + (1 if i == a else 0)) % SIDE for i in range(3))) for x in SITES3 for a in range(3)]


def lap_of(f, z):
    return sum((f[INDEX[y]] for y in neighbours(z)), ZERO) - 6 * f[INDEX[z]]


def bond_form(f):
    return sum(((f[INDEX[x]] - f[INDEX[y]]) ** 2 / (f[INDEX[x]] * f[INDEX[y]]) for x, y in BONDS), ZERO)


def eliminate(matrix, rhs=None):
    """Gauss-Jordan over the rationals; returns (solution or None, determinant)."""
    size = len(matrix)
    aug = [row[:] + ([rhs[i]] if rhs is not None else []) for i, row in enumerate(matrix)]
    det = ONE
    for col in range(size):
        pivot = next((r for r in range(col, size) if aug[r][col] != 0), None)
        if pivot is None:
            return None, ZERO
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
            det = -det
        lead = aug[col][col]
        det *= lead
        aug[col] = [v / lead for v in aug[col]]
        for r in range(size):
            if r != col and aug[r][col] != 0:
                fac = aug[r][col]
                aug[r] = [vr - fac * vc for vr, vc in zip(aug[r], aug[col])]
    return ([aug[r][size] for r in range(size)] if rhs is not None else None), det


def minus_laplacian():
    lap = [[ZERO] * len(SITES3) for _ in SITES3]
    for x in SITES3:
        lap[INDEX[x]][INDEX[x]] += 6
        for y in neighbours(x):
            lap[INDEX[x]][INDEX[y]] -= 1
    return lap


def torus_potential():
    """-Delta G = delta_0 - 1/V, sum G = 0."""
    lap = minus_laplacian()
    size = len(SITES3)
    rhs = [F(-1, size)] * size
    rhs[0] += 1
    lap[size - 1] = [ONE] * size
    rhs[size - 1] = ZERO
    sol, _ = eliminate(lap, rhs)
    return sol


def rational_field(tag):
    return [1 + F((tag * 5 + 3 * x[0] * x[0] + 5 * x[1] + x[2] * x[1] + (tag + 1) * x[0] + x[2]) % 7, 5 + tag) for x in SITES3]


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    f = rational_field(1)
    lhs = sum((lap_of(f, z) / f[INDEX[z]] for z in SITES3), ZERO)
    rhs = bond_form(f)
    if mut("closed_lattice_identity_has_the_other_sign"):
        rhs = -rhs
    checks.check("B1", lhs == rhs and rhs > 0, 'PR8608 B1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    chi, rate_n = rational_field(2), rational_field(3)
    q = [-lap_of(chi, z) for z in SITES3]                                       # DEFINE the charges by the lengths' equation: (Delta chi)_z = -Q_z, i.e. mu_z = Q_z chi_z
    both_signs = any(v > 0 for v in q) and any(v < 0 for v in q)
    residual_sum = sum(((lap_of(rate_n, z) - (q[INDEX[z]] / chi[INDEX[z]]) * rate_n[INDEX[z]]) / rate_n[INDEX[z]] for z in SITES3), ZERO)
    total = bond_form(rate_n) + bond_form(chi)
    positive = (residual_sum == total and total > 0) if not mut("curvature_member_residuals_can_cancel") else (residual_sum == 0)
    checks.check("B2", positive and both_signs and sum(q, ZERO) == 0, 'PR8608 B2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    uniform = [ONE]*len(SITES3)
    checks.check("B3", all(lap_of(uniform,z)==0 for z in SITES3) and bond_form(uniform)==0, 'PR8608 B3: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    g = torus_potential()
    g_at = lambda x, src: g[INDEX[tuple((x[i] - src[i]) % SIDE for i in range(3))]]
    a_pos, b_pos = (0, 0, 0), (2, 1, 0)
    h = g[0] - g_at(a_pos, b_pos)
    potential_ok = all(-lap_of(g, z) == (1 if z == SITES3[0] else 0) - F(1, len(SITES3)) for z in SITES3) and sum(g, ZERO) == 0 and h > 0
    gam, m_a = F(1, 2), F(3)
    sep = h if not mut("pair_condition_ignores_the_separation") else g[0]
    m_b = -1 / (1 / m_a + gam * sep)
    c = ONE
    phi_a = c / (1 + gam / 2 * m_a * h)
    p = gam / 2 * m_a * phi_a
    phi = [c - p * (g_at(x, a_pos) - g_at(x, b_pos)) for x in SITES3]
    mass = lambda z: m_a if z == a_pos else m_b if z == b_pos else ZERO
    law = all((2 / gam) * (-lap_of(phi, z)) + mass(z) * phi[INDEX[z]] == 0 for z in SITES3)
    positive = all(v > 0 for v in phi)
    field_energy = (2 / gam) * sum(((phi[INDEX[x]] - phi[INDEX[y]]) ** 2 for x, y in BONDS), ZERO)
    content = m_a * phi[INDEX[a_pos]] ** 2 + m_b * phi[INDEX[b_pos]] ** 2
    checks.check("C1", potential_ok and law and positive and content + field_energy == 0 and content < 0 and m_a + m_b > 0 and phi[INDEX[b_pos]] > phi[INDEX[a_pos]], 'PR8608 C1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    def determinant(mb):
        op = minus_laplacian()
        op[INDEX[a_pos]][INDEX[a_pos]] += gam / 2 * m_a
        op[INDEX[b_pos]][INDEX[b_pos]] += gam / 2 * mb
        return eliminate(op)[1]
    tuned = determinant(-1 / (1 / m_a + gam * h))
    detuned = determinant(-1 / (1 / m_a + gam * h) + F(1, 10))
    ok = tuned == 0 and detuned != 0
    if mut("detuned_pair_is_at_rest"):
        ok = tuned == 0 and detuned == 0
    checks.check("C2", ok, 'PR8608 C2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    phi = rational_field(4)
    gam = F(1, 2)
    masses = [-(2 / gam) * (-lap_of(phi, z)) / phi[INDEX[z]] for z in SITES3]      # DEFINE the bodies by the law: every positive phi is at rest for these bare energies
    total_m = sum(masses, ZERO)
    identity = total_m == (2 / gam) * bond_form(phi)
    content = sum((masses[INDEX[z]] * phi[INDEX[z]] ** 2 for z in SITES3), ZERO)
    field_energy = (2 / gam) * sum(((phi[INDEX[x]] - phi[INDEX[y]]) ** 2 for x, y in BONDS), ZERO)
    signs = any(v > 0 for v in masses) and any(v < 0 for v in masses)
    if mut("closed_lattice_at_rest_with_positive_bodies_only"):
        signs = all(v >= 0 for v in masses)
    checks.check("D1", identity and total_m > 0 and content + field_energy == 0 and content < 0 and signs, 'PR8608 D1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')
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
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print('scope: On a finite connected closed symmetric graph the positive-function divided-difference identity excludes nonzero net diagonal sources in the supplied curvature equations, with uniform zero-source fields as an explicit exception. Nonconstant positive solutions of the simplest supplied equation require both source signs. A distinct-site pair on a translation-invariant torus has the stated exact tuning condition.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
