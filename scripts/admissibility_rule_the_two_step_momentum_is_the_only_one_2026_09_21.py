#!/usr/bin/env python3
"""In the infinite-lattice polynomial commutant of the supplied free walk, vector coefficients are a scalar polynomial times sin k. Reach-one scalar symbols cannot have unit own-coordinate slopes at every corner. At reach two the normalized scalar solutions have six quadratic freedoms removed by cubic covariance; a permitted term along the walk changes only higher-order dispersion. This classifies the stated normalized momenta, not all field couplings."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_THE_TWO_STEP_MOMENTUM_IS_THE_ONLY_ONE_AMONG_CONSERVED_COVARIANT_MOMENTA_OF_REACH_TWO_THAT_IS_EVERY_SPECIES_OWN_WAVE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_two_step_momentum_is_the_only_one_among_conserved_covariant_momenta_of_reach_two_that_is_every_species_own_wave_number_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "a_matrix_off_the_walks_direction_commutes": "B",
    "mixed_axes_momentum_of_reach_one_serves_all_species": "C",
    "reach_two_solution_space_is_a_point": "D",
    "covariance_leaves_a_second_momentum": "D",
    "walk_part_changes_the_lengths": "E",
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


KS = sp.symbols("k1 k2 k3", real=True)
SPECIES = list(product((0, 1), repeat=3))


def real_basis(reach):
    """Real trigonometric monomials cos(m.k), sin(m.k) with |m|_1 <= reach (one of each pair +-m), and the constant."""
    exps = [m for m in product(range(-reach, reach + 1), repeat=3) if sum(abs(v) for v in m) <= reach and m > (0, 0, 0)]
    out = [sp.Integer(1)]
    for m in exps:
        arg = sum(m[i] * KS[i] for i in range(3))
        out += [sp.cos(arg), sp.sin(arg)]
    return out


def own_wave_number_conditions(symbol, j):
    """The symbol vanishes at each of the eight zeros and its gradient there is e_j."""
    eqs = []
    for n in SPECIES:
        point = {KS[i]: sp.pi * n[i] for i in range(3)}
        eqs.append(symbol.subs(point))
        eqs += [sp.diff(symbol, KS[b]).subs(point) - (1 if b == j else 0) for b in range(3)]
    return eqs


def pauli(vec):
    return sum((vec[a] * sp.Matrix(PAULI[a]) for a in range(3)), sp.zeros(2, 2))


PAULI = ([[0, 1], [1, 0]], [[0, -sp.I], [sp.I, 0]], [[1, 0], [0, -1]])


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    s = [sp.sin(KS[a]) for a in range(3)]
    a0 = sp.Symbol("a0")
    b = sp.symbols("b1 b2 b3")
    walk = pauli(s)
    m = a0 * sp.eye(2) + pauli(b)
    comm = sp.expand(m * walk - walk * m)
    cross = [sp.expand(b[1] * s[2] - b[2] * s[1]), sp.expand(b[2] * s[0] - b[0] * s[2]), sp.expand(b[0] * s[1] - b[1] * s[0])]
    expected = 2 * sp.I * pauli(cross)
    identity = sp.simplify(comm - expected) == sp.zeros(2, 2)
    parallel = sp.simplify((m * walk - walk * m).subs({b[i]: sp.Symbol("c") * s[i] for i in range(3)})) == sp.zeros(2, 2)
    off = {b[0]: s[1], b[1]: 0, b[2]: 0}
    off_commutes = sp.simplify((m * walk - walk * m).subs(off)) == sp.zeros(2, 2)
    if mut("a_matrix_off_the_walks_direction_commutes"):
        off_commutes = not off_commutes
    checks.check("B1", identity and parallel and not off_commutes, 'PR8606 B1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    basis = real_basis(1)
    coeffs = sp.symbols(f"d0:{len(basis)}")
    symbol = sum(c * f for c, f in zip(coeffs, basis))
    solutions = sp.solve(own_wave_number_conditions(symbol, 0), coeffs, dict=True)
    none = (solutions == []) if not mut("mixed_axes_momentum_of_reach_one_serves_all_species") else (solutions != [])
    alpha = sp.Matrix(3, 3, lambda i, jj: sp.Symbol(f"al{i}{jj}"))
    bs = sp.Matrix(3, 3, lambda i, jj: sp.Symbol(f"B{i}{jj}", real=True))
    q = sp.Matrix(sp.symbols("q1 q2 q3", real=True))
    t = sp.symbols("t", positive=True)
    seen = True
    for n in SPECIES:
        d = sp.diag(*[(-1) ** v for v in n])
        kpt = [sp.pi * n[a] + t * q[a] for a in range(3)]
        mom = [sum(alpha[jj, b] * sp.sin(kpt[b]) for b in range(3)) for jj in range(3)]
        vec = [sp.sin(kpt[a]) + sp.cos(kpt[a]) * sum(bs[a, jj] * mom[jj] for jj in range(3)) for a in range(3)]
        quad = sp.expand(sp.series(sum(v ** 2 for v in vec), t, 0, 3).removeO().coeff(t, 2))
        target = (sp.eye(3) + bs * alpha * d).T * (sp.eye(3) + bs * alpha * d)
        seen = seen and sp.expand(quad - (q.T * target * q)[0]) == 0
    checks.check("C1", none and seen, 'PR8606 C1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    basis = real_basis(2)
    coeffs = sp.symbols(f"c0:{len(basis)}")
    symbol = sum(c * f for c, f in zip(coeffs, basis))
    solutions = sp.solve(own_wave_number_conditions(symbol, 0), coeffs, dict=True)
    one = len(solutions) == 1
    sol = solutions[0]
    free = [c for c in coeffs if c not in sol]
    general = symbol.subs(sol)
    particular = sp.simplify(general.subs({c: 0 for c in free}) - sp.sin(2 * KS[0]) / 2) == 0
    directions = [sp.diff(general, c) for c in free]
    second_order = [sp.sin(KS[b]) * sp.sin(KS[c]) for b in range(3) for c in range(b, 3)]
    span = sp.Matrix([[sp.integrate(sp.integrate(sp.integrate(sp.expand(u * v), (KS[0], 0, 2 * sp.pi)), (KS[1], 0, 2 * sp.pi)), (KS[2], 0, 2 * sp.pi)) for v in second_order] for u in directions])
    count = 6 if not mut("reach_two_solution_space_is_a_point") else 0
    space = one and len(free) == count and particular and (span.rank() == 6 if count else True)
    checks.check("D1", space, 'PR8606 D1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    e = sp.symbols("e1 e2 e3 c12 c13 c23")
    cand = sp.sin(2 * KS[0]) / 2 + e[0] * sp.sin(KS[0]) ** 2 + e[1] * sp.sin(KS[1]) ** 2 + e[2] * sp.sin(KS[2]) ** 2 + e[3] * sp.sin(KS[0]) * sp.sin(KS[1]) + e[4] * sp.sin(KS[0]) * sp.sin(KS[2]) + e[5] * sp.sin(KS[1]) * sp.sin(KS[2])
    quarter = {KS[1]: KS[2], KS[2]: -KS[1]}                                                  # the quarter turn about axis 1 keeps e_1: M_1 must be unchanged
    half_turn = {KS[0]: -KS[0], KS[2]: -KS[2]}                                               # the half turn about axis 2 reverses e_1: M_1 must change sign
    conds = []
    for expr in (sp.expand(cand.subs(quarter, simultaneous=True) - cand), sp.expand(cand.subs(half_turn, simultaneous=True) + cand)):
        for mono in second_order:
            conds.append(sp.integrate(sp.integrate(sp.integrate(sp.expand(expr * mono), (KS[0], 0, 2 * sp.pi)), (KS[1], 0, 2 * sp.pi)), (KS[2], 0, 2 * sp.pi)))
    forced = sp.solve(conds, e, dict=True)
    unique = forced == [{v: 0 for v in e}]
    if mut("covariance_leaves_a_second_momentum"):
        unique = forced != [{v: 0 for v in e}]
    two_step_ok = sp.expand((sp.sin(2 * KS[0]) / 2).subs(quarter, simultaneous=True) - sp.sin(2 * KS[0]) / 2) == 0 and sp.expand((sp.sin(2 * KS[0]) / 2).subs(half_turn, simultaneous=True) + sp.sin(2 * KS[0]) / 2) == 0
    checks.check("D2", unique and two_step_ok, 'PR8606 D2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    gamma = sp.Symbol("gamma", real=True)
    s = [sp.sin(KS[a]) for a in range(3)]
    c = [sp.cos(KS[a]) for a in range(3)]
    bs = sp.Matrix(3, 3, lambda i, jj: sp.Symbol(f"B{i}{jj}", real=True))
    walk = pauli(s)
    total = sp.zeros(2, 2)
    for a in range(3):
        for jj in range(3):
            m_j = gamma * s[jj] * walk                                                       # the c-part allowed by covariance at reach two: gamma sin k_j H
            sig_a = sp.Matrix(PAULI[a])
            total += bs[a, jj] * c[a] * (sig_a * m_j + m_j * sig_a) / 2
    scalar = sum(gamma * s[a] * s[jj] * c[a] * bs[a, jj] for a in range(3) for jj in range(3))
    is_scalar = sp.simplify(total - scalar * sp.eye(2)) == sp.zeros(2, 2)
    q = sp.symbols("q1 q2 q3", real=True)
    t = sp.symbols("t", positive=True)
    second = True
    firsts = []
    for n in SPECIES:
        expr = scalar.subs({KS[a]: sp.pi * n[a] + t * q[a] for a in range(3)}, simultaneous=True)
        ser = sp.series(expr, t, 0, 3).removeO()
        second = second and sp.expand(ser.coeff(t, 0)) == 0
        firsts.append(sp.expand(ser.coeff(t, 1)))
        dn = [(-1) ** v for v in n]
        lead = sum(gamma * dn[jj] * q[a] * q[jj] * bs[a, jj] for a in range(3) for jj in range(3))
        second = second and sp.expand(ser.coeff(t, 2) - lead) == 0
    no_first_order = all(v == 0 for v in firsts) if not mut("walk_part_changes_the_lengths") else any(v != 0 for v in firsts)
    checks.check("E1", is_scalar and second and no_first_order, 'PR8606 E1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')
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
    print('scope: In the infinite-lattice polynomial commutant of the supplied free walk, vector coefficients are a scalar polynomial times sin k. Reach-one scalar symbols cannot have unit own-coordinate slopes at every corner. At reach two the normalized scalar solutions have six quadratic freedoms removed by cubic covariance; a permitted term along the walk changes only higher-order dispersion. This classifies the stated normalized momenta, not all field couplings.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
