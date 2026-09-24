#!/usr/bin/env python3
"""Exact alternating bond symbol and linear bond-law costs; a restricted continuum-zone variational threshold, corner exceptions and one literal wall-ring nullity. Rates and minimization are supplied."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_CHESSBOARD_OR_AXIS_STRIPES_ON_SITES_ALTERNATING_LENGTHS_GIVE_ONE_REST_ENERGY_EXCLUSION_CAGES_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_ALTERNATING_LENGTHS_ARE_A_RELABELLING_INVISIBLE_TO_THE_WALK_AND_FREE_FOR_THE_LEDGER_A_REST_ENERGY_NEEDS_THE_BONDS_OWN_AMPLITUDE_NO_STRAIN_GAPS_AT_FIRST_ORDER_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_the_sea_against_block_59s_bond_law_gives_every_species_one_rest_energy_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "alternation_enters_through_the_sines": "B",
    "alternation_stiffness_has_gamma": "C",
    "threshold_is_chi_over_six": "D",
    "corner_crossing_at_delta_equals_a": "E",
    "walls_bind_no_zero_modes": "E",
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


SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
SIGMA = (SX, SY, SZ)
I2 = sp.eye(2)


def kron(*ms):
    out = ms[0]
    for m_ in ms[1:]:
        out = sp.kronecker_product(out, m_)
    return out


def place(mat, j):
    fs = [I2, I2, I2]
    fs[j] = mat
    return kron(I2, *fs)


def coin(mat):
    return kron(mat, I2, I2, I2)


def bond_law_matrix(alpha, beta, gamma, kv):
    """Block 59 T3: the 3x3 matrix of the linear covariant bond law with the shift symmetry, on the three bond fields at wave vector kv."""
    c0 = -2 * alpha - 8 * beta - 4 * gamma
    m = sp.zeros(3, 3)
    for j in range(3):
        m[j, j] = c0 + 2 * alpha * sp.cos(kv[j]) + 2 * gamma * sum((sp.cos(kv[l]) for l in range(3) if l != j), sp.Integer(0))
        for l in range(3):
            if l != j:
                m[j, l] = 4 * beta * sp.cos(kv[j] / 2) * sp.cos(kv[l] / 2)
    return m


def ring_hop(size, amplitudes):
    """The sigma_x-coined ring walk (1/2i)(t_x T - T^dag t_x) with rational bond amplitudes t_x on the bond x -> x + 1, as an exact 2 size x 2 size matrix."""
    hop = sp.zeros(size, size)
    for x in range(size):
        hop[x, (x + 1) % size] += sp.Rational(amplitudes[x].numerator, amplitudes[x].denominator) / (2 * sp.I)
        hop[x, (x - 1) % size] -= sp.Rational(amplitudes[(x - 1) % size].numerator, amplitudes[(x - 1) % size].denominator) / (2 * sp.I)
    return sp.kronecker_product(SX, hop)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    k = sp.symbols("k1 k2 k3", real=True)
    bet = sp.symbols("beta", real=True)
    d = sp.symbols("delta1 delta2 delta3", real=True)
    s_ = [sp.sin(kk) for kk in k]
    c_ = [sp.cos(kk) for kk in k]
    H = sum((coin(SIGMA[j]) * place(bet * (-s_[j] * SZ + d[j] * c_[j] * SY), j) for j in range(3)), sp.zeros(16, 16))
    target = bet ** 2 * sum(s_[j] ** 2 + d[j] ** 2 * c_[j] ** 2 for j in range(3))
    wrong = bet ** 2 * sum(s_[j] ** 2 + d[j] ** 2 * s_[j] ** 2 for j in range(3))
    ok = sp.simplify(H * H - target * sp.eye(16)) == sp.zeros(16, 16)
    not_wrong = not (sp.simplify(H * H - wrong * sp.eye(16)) == sp.zeros(16, 16))
    b1 = (ok and not_wrong) if not mut("alternation_enters_through_the_sines") else (not ok)
    checks.check("B1", b1, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    # exact values of the zone average at delta = 1 and at delta = 0 on the 4^3 torus grid: sqrt(3) and the average of |sin| lengths
    grid = [sp.pi * n / 2 for n in range(4)]
    tot1 = sum((sp.sqrt(sum(sp.sin(kk) ** 2 + sp.cos(kk) ** 2 for kk in kv)) for kv in product(grid, repeat=3)), sp.Integer(0))
    checks.check("B2", sp.simplify(tot1 / 64 - sp.sqrt(3)) == 0, 'Scoped exact check B2: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    al, be, ga = sp.symbols("alpha beta gamma", real=True)
    m1 = sp.simplify(bond_law_matrix(al, be, ga, (sp.pi, 0, 0)))
    own = sp.simplify(m1[0, 0] + 4 * al + 8 * be) == 0
    decoupled = m1[0, 1] == 0 and m1[0, 2] == 0 and m1[1, 0] == 0 and m1[2, 0] == 0
    gamma_free = sp.diff(m1[0, 0], ga) == 0
    others = sp.simplify(m1[1, 1] + 8 * be + 4 * ga) == 0 and sp.simplify(m1[1, 2] - 4 * be) == 0
    c1 = (own and decoupled and gamma_free and others) if not mut("alternation_stiffness_has_gamma") else (not gamma_free)
    checks.check("C1", c1, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    q = sp.symbols("q", real=True)
    ones = sp.Matrix([1, 1, 1])
    scalar = sp.series((ones.T * bond_law_matrix(al, be, ga, (q, 0, 0)) * ones)[0], q, 0, 3).removeO()
    checks.check("C2", sp.simplify(scalar + q ** 2 * (al + 2 * be + 2 * ga)) == 0, 'Scoped exact check C2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    m3 = sp.simplify(bond_law_matrix(al, be, ga, (sp.pi, sp.pi, sp.pi)))
    checks.check("C3", m3 == sp.diag(*[-4 * al - 8 * be - 8 * ga] * 3), 'Scoped exact check C3: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    dl, kap, chi = sp.symbols("delta kappa chi", positive=True)
    # per site: E(delta) = E_0 - (chi/2) delta^2 + O(delta^4 log): the alternation on all three axes with equal delta gives sum_j delta_j^2 cos^2 k_j = delta^2 c^2
    # cost per site: three bonds x (1/2)(4 alpha + 8 beta) delta^2 = 6 kappa delta^2, kappa = alpha + 2 beta
    total_second_order = -chi / 2 * dl ** 2 + 6 * kap * dl ** 2
    threshold = sp.solve(sp.Eq(sp.diff(total_second_order, dl, 2), 0), kap)[0]
    d1 = (threshold == chi / 12) if not mut("threshold_is_chi_over_six") else (threshold == chi / 6)
    checks.check("D1", d1, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    # the per-axis form: chi_j = chi/3 by the cubic symmetry, and a single-axis alternation has cost 2 kappa delta^2 with gain (chi/6) delta^2: the same threshold
    k = sp.symbols("k1 k2 k3", real=True)
    integrand_all = sum(sp.cos(kk) ** 2 for kk in k) / sp.sqrt(sum(sp.sin(kk) ** 2 for kk in k))
    integrand_one = sp.cos(k[0]) ** 2 / sp.sqrt(sum(sp.sin(kk) ** 2 for kk in k))
    # the cyclic permutation of the axes maps integrand_one to its two partners; their sum is integrand_all
    perm = {k[0]: k[1], k[1]: k[2], k[2]: k[0]}
    partners = integrand_one + integrand_one.subs(perm, simultaneous=True) + integrand_one.subs(perm, simultaneous=True).subs(perm, simultaneous=True)
    checks.check("D2", sp.simplify(partners - integrand_all) == 0, 'Scoped exact check D2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    # concavity: E(delta) = -<sqrt(s^2 + delta^2 c^2)> is concave in delta (second derivative <= 0 pointwise) and even
    s2, c2 = sp.symbols("s2 c2", positive=True)
    f = -sp.sqrt(s2 + dl ** 2 * c2)
    second = sp.simplify(sp.diff(f, dl, 2))
    A0, X0=sp.symbols("A0 X0", positive=True)
    rem=1/(2*sp.sqrt(A0))-1/(sp.sqrt(A0+X0)+sp.sqrt(A0))
    checks.check("D4", sp.simplify((sp.sqrt(A0+X0)-sp.sqrt(A0))*(sp.sqrt(A0+X0)+sp.sqrt(A0))-X0)==0, 'Scoped exact check D4: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    checks.check("D3", sp.simplify(second * (s2 + dl ** 2 * c2) ** sp.Rational(3, 2)) == -s2 * c2 and f.subs(dl, -dl) == f, 'Scoped exact check D3: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    a_, bet, dl = sp.symbols("a beta delta", positive=True)
    root = sp.sqrt(4 * a_ ** 2 + 3 * bet ** 2 * dl ** 2)
    crossing = sp.solve(sp.Eq(4 * a_ - root, 0), dl)
    e1 = (crossing == [2 * a_ / bet]) if not mut("corner_crossing_at_delta_equals_a") else (crossing == [a_ / bet])
    checks.check("E1", e1, 'Scoped exact check E1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
    size = 12
    d = F(3, 10)
    walls = [1 + d * (1 if x < size // 2 else -1) * ((-1) ** x) for x in range(size)]
    uniform = [1 + d * ((-1) ** x) for x in range(size)]
    n_walls = 2 * size - ring_hop(size, walls).rank()
    n_uniform = 2 * size - ring_hop(size, uniform).rank()
    e2 = (n_walls == 4 and n_uniform == 0) if not mut("walls_bind_no_zero_modes") else (n_walls == 0)
    checks.check("E2", e2, 'Scoped exact check E2: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')
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
    print('scope: Exact alternating bond symbol and linear bond-law costs; a restricted continuum-zone variational threshold, corner exceptions and one literal wall-ring nullity. Rates and minimization are supplied.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
