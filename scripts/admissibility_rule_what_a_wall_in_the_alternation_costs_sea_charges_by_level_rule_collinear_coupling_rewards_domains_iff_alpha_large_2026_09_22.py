#!/usr/bin/env python3
"""Exact three-ring spectral replacements at delta=3/10, a defined positive square-root comparator and a specified linear bond-law wall cost. No universal wall tension or domain-formation criterion."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_WHAT_A_WALL_IN_THE_ALTERNATION_COSTS_THE_SEA_CHARGES_IT_BY_AN_EXACT_LEVEL_RULE_BLOCK_59S_COLLINEAR_COUPLING_REWARDS_IT_DOMAINS_IFF_ALPHA_LARGE_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/ADMISSIBILITY_RULE_DEFECTS_OF_THE_ALTERNATION_ARE_SEPARABLE_WALLS_CARRY_SHEETS_OF_LOWER_MASS_LINES_LOWER_STILL_AND_THREE_CROSSING_WALLS_BIND_EXACT_ZERO_MODES_BOUNDED_THEOREM_NOTE_2026-09-22.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_what_a_wall_in_the_alternation_costs_the_sea_charges_it_by_an_exact_level_rule_block_59s_collinear_coupling_rewards_it_domains_iff_alpha_large_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "walls_shift_every_level": "B",
    "sea_rewards_a_wall": "C",
    "law_charges_a_wall": "D",
    "criterion_at_delta_one_above_a_tenth": "E",
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


def axis_operator(size, delta, walls):
    """(1/2i)(t T - T^T t) on a ring, t_x = 1 + delta s_x (-1)^x; two walls when `walls` (s flips at the half)."""
    t_shift = sp.zeros(size, size)
    for x in range(size):
        t_shift[x, (x + 1) % size] = 1
    signs = [1 if (not walls or x < size // 2) else -1 for x in range(size)]
    t = sp.diag(*[1 + delta * signs[x] * (-1) ** x for x in range(size)])
    return (t * t_shift - t_shift.T * t) / (2 * sp.I)


def squared_spectrum(m):
    out = {}
    for v, mult in (m * m).eigenvals().items():
        key = sp.nsimplify(sp.simplify(v))
        out[key] = out.get(key, 0) + mult
    return {k: v for k, v in out.items() if v != 0}


def torus_bonds(size):
    return [(x, a) for x in product(range(size), repeat=3) for a in range(3)]


def step(x, a, d, size):
    y = list(x)
    y[a] = (y[a] + d) % size
    return tuple(y)


def bond_neighbours(b, size):
    """Block 59 T3's three classes for the bond b = (x, a): collinear (2), parallel (4), perpendicular (8)."""
    x, a = b
    coll = [(step(x, a, d, size), a) for d in (1, -1)]
    par = [(step(x, l, d, size), a) for l in range(3) if l != a for d in (1, -1)]
    perp = []
    for l in range(3):
        if l == a:
            continue
        for base in (x, step(x, a, 1, size)):
            perp.append((base, l))
            perp.append((step(base, l, -1, size), l))
    return coll, par, perp


def law_energy(u, size, alpha, beta, gamma):
    """F = -1/2 sum_b u_b (c_0 u_b + alpha sum_coll u + beta sum_perp u + gamma sum_par u), c_0 = -2 alpha - 8 beta - 4 gamma (block 59 T3)."""
    c0 = -2 * alpha - 8 * beta - 4 * gamma
    tot = ZERO
    for b in torus_bonds(size):
        coll, par, perp = bond_neighbours(b, size)
        tot += u[b] * (c0 * u[b] + alpha * sum((u[n] for n in coll), ZERO) + beta * sum((u[n] for n in perp), ZERO) + gamma * sum((u[n] for n in par), ZERO))
    return -tot / 2


def bond_pattern(size, delta, walls_x):
    u = {}
    for (x, a) in torus_bonds(size):
        s = -1 if (a == 0 and walls_x and x[0] >= size // 2) else 1
        u[(x, a)] = delta * s * ((-1) ** x[a])
    return u


DELTA = sp.Rational(3, 10)


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    ok = True
    report = []
    for size in (4, 8, 12):
        uni = squared_spectrum(axis_operator(size, DELTA, False))
        wal = squared_spectrum(axis_operator(size, DELTA, True))
        conj = dict(uni)
        conj[DELTA ** 2] = conj.get(DELTA ** 2, 0) - 2
        conj[sp.Integer(1)] = conj.get(sp.Integer(1), 0) - 2
        conj[sp.Integer(0)] = conj.get(sp.Integer(0), 0) + 2
        conj[1 + DELTA ** 2] = conj.get(1 + DELTA ** 2, 0) + 2
        conj = {k: v for k, v in conj.items() if v != 0}
        same = conj == wal
        ok = ok and same
        report.append(f"ring {size}: {len(uni)} distinct E^2 without walls, {len(wal)} with; rule holds: {same}")
    b1 = ok if not mut("walls_shift_every_level") else (not ok)
    checks.check("B1", b1, 'Scoped exact check B1: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    checks.check("B3", sp.Integer(1) not in squared_spectrum(axis_operator(6,DELTA,False)), 'Scoped exact check B3: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')
    d = sp.symbols("delta", positive=True)
    pair_energy = 1 + d - sp.sqrt(1 + d ** 2)
    positive = sp.simplify(sp.expand((1 + d) ** 2 - (1 + d ** 2))) == 2 * d
    checks.check("B2", positive, 'Scoped exact check B2: stated algebraic or finite fixture. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    d, e2 = sp.symbols("delta e2", positive=True)
    integrand = sp.sqrt(d ** 2 + e2) + sp.sqrt(1 + e2) - sp.sqrt(e2) - sp.sqrt(1 + d ** 2 + e2)
    # concavity of sqrt: for 0 <= p <= q <= r <= s with p + s = q + r, sqrt(q) + sqrt(r) >= sqrt(p) + sqrt(s); here p = e2, q = e2 + delta^2, r = e2 + 1, s = e2 + 1 + delta^2
    sums_match = sp.simplify((e2) + (1 + d ** 2 + e2) - (d ** 2 + e2) - (1 + e2)) == 0
    # a rational check point: e2 = 9/16, delta = 3/10 -> values with exact square roots compared exactly
    val = integrand.subs({d: sp.Rational(3, 10), e2: sp.Rational(9, 16)})
    positive_point = bool(sp.simplify(val) > 0)
    at_one = sp.simplify(integrand.subs({d: 1, e2: 2}) - (2 * sp.sqrt(3) - sp.sqrt(2) - 2)) == 0
    c1 = (sums_match and positive_point and at_one) if not mut("sea_rewards_a_wall") else (not positive_point)
    checks.check("C1", c1, 'Scoped exact check C1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    size = 4
    al, be, ga = F(1, 7), F(1, 11), F(1, 5)
    dl = F(3, 10)
    fu = law_energy(bond_pattern(size, dl, False), size, al, be, ga)
    fw = law_energy(bond_pattern(size, dl, True), size, al, be, ga)
    uniform_ok = fu == 3 * size ** 3 * 2 * (al + 2 * be) * dl * dl
    per_area = (fw - fu) / (2 * size * size)
    reward_ok = per_area == -2 * al * dl * dl
    only_alpha = True
    for (a_, b_, g_) in ((F(1, 7), ZERO, ZERO), (ZERO, F(1, 11), ZERO), (ZERO, ZERO, F(1, 5))):
        diff = (law_energy(bond_pattern(size, dl, True), size, a_, b_, g_) - law_energy(bond_pattern(size, dl, False), size, a_, b_, g_)) / (2 * size * size)
        only_alpha = only_alpha and diff == -2 * a_ * dl * dl
    d1 = (uniform_ok and reward_ok and only_alpha) if not mut("law_charges_a_wall") else (per_area > 0)
    checks.check("D1", d1, 'Scoped exact check D1: stated finite or symbolic comparison. General conclusions and exceptions are in the companion note.')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """Exact checks for the scoped companion statements."""
    d = sp.symbols("delta", positive=True)
    # at delta = 1 the transverse average is exact: sigma_sea(1) = 2 sqrt(3) - sqrt(2) - 2; the criterion there is alpha > (2 sqrt 3 - sqrt 2 - 2)/2
    crit = (2 * sp.sqrt(3) - sp.sqrt(2) - 2) / 2
    bounds = bool(sp.Rational(2, 100) < crit) and bool(crit < sp.Rational(3, 100))
    e1 = bounds if not mut("criterion_at_delta_one_above_a_tenth") else bool(crit > sp.Rational(1, 10))
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
    print('scope: Exact three-ring spectral replacements at delta=3/10, a defined positive square-root comparator and a specified linear bond-law wall cost. No universal wall tension or domain-formation criterion.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
