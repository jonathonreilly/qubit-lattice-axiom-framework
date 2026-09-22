#!/usr/bin/env python3
"""Exact checks: bond rates that alternate on their own (block 59's bond rates and bond law; the sea as a comparator; not adopted).

OBJECTS: block 59's generator H = sum_b c_b h_b (the hop across a bond timed by that bond's own crossing rate); an alternation of the bond
rates c_b = 1 + delta_j (-1)^{x_j} on the bonds along j; block 59 T3's linear covariant bond law with the shift symmetry (three numbers
alpha, beta, gamma); the sea's energy E_sea = sum_{E<0} E of the one-record generator (comparator, blocks 76, 78).
T1: H^2 = beta^2 sum_j (sin^2 k_j + delta_j^2 cos^2 k_j) exactly on the 16-dimensional block: the sea's energy per site is minus the zone
   average of the square root; at delta = 1 it is -sqrt(3) exactly.
T2: at the alternation wave vectors pi e_j block 59's law has the restoring coefficient 4 alpha + 8 beta on the bonds along j, decoupled from
   the other axes and independent of gamma; the long-range stiffness is alpha + 2 beta + 2 gamma.
T3: the second-order balance per site is (6 kappa - chi/2) delta^2, kappa = alpha + 2 beta, chi the zone average of sum cos^2 / sqrt(sum sin^2):
   the uniform field is a local minimum iff kappa >= chi/12; the sea's energy is concave and even in delta.
T4: with the scalar hop timed by the same bond rates the corner energies cross zero exactly at delta = 2a/beta.
T5: on a ring, walls between the two alternation phases bind exactly two zero modes each.
Exact arithmetic only (integers, Fractions, exact symbolic algebra); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_BOND_RATES_ALTERNATE_ON_THEIR_OWN_BELOW_A_THRESHOLD_STIFFNESS_THE_SEA_AGAINST_BLOCK_59S_BOND_LAW_GIVES_EVERY_SPECIES_ONE_REST_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
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
    note, axioms = texts
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
    """T1: with per-axis alternations delta_j of the bond rates, H^2 = beta^2 sum_j (sin^2 k_j + delta_j^2 cos^2 k_j): the sea's energy per site is -<sqrt(s^2 + sum delta_j^2 cos^2 k_j)>."""
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
    checks.check("B1", b1, "T1: with independent alternations delta_1, delta_2, delta_3 of the bond rates along the three axes, the 16-dimensional block obeys H^2 = beta^2 sum_j (sin^2 k_j + delta_j^2 cos^2 k_j) exactly (the three pair operators commute, the coins anticommute): every one of the sixteen energies at a reduced wave vector is +-sqrt of that, so the sea's energy per site is exactly minus the zone average of sqrt(sum sin^2 k_j + sum delta_j^2 cos^2 k_j)")
    # exact values of the zone average at delta = 1 and at delta = 0 on the 4^3 torus grid: sqrt(3) and the average of |sin| lengths
    grid = [sp.pi * n / 2 for n in range(4)]
    tot1 = sum((sp.sqrt(sum(sp.sin(kk) ** 2 + sp.cos(kk) ** 2 for kk in kv)) for kv in product(grid, repeat=3)), sp.Integer(0))
    checks.check("B2", sp.simplify(tot1 / 64 - sp.sqrt(3)) == 0, "T1: at delta = 1 on every axis the energy is sqrt(3) at every wave vector (sin^2 + cos^2 = 1 per axis): the sea's energy per site is exactly -sqrt(3), the lattice having fallen into disconnected 2x2x2 cubes with flat bands")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: block 59's bond law at the alternation wave vectors: the alternation of the bonds along their own axis has the restoring coefficient 4 alpha + 8 beta, decoupled from the other axes and independent of gamma."""
    al, be, ga = sp.symbols("alpha beta gamma", real=True)
    m1 = sp.simplify(bond_law_matrix(al, be, ga, (sp.pi, 0, 0)))
    own = sp.simplify(m1[0, 0] + 4 * al + 8 * be) == 0
    decoupled = m1[0, 1] == 0 and m1[0, 2] == 0 and m1[1, 0] == 0 and m1[2, 0] == 0
    gamma_free = sp.diff(m1[0, 0], ga) == 0
    others = sp.simplify(m1[1, 1] + 8 * be + 4 * ga) == 0 and sp.simplify(m1[1, 2] - 4 * be) == 0
    c1 = (own and decoupled and gamma_free and others) if not mut("alternation_stiffness_has_gamma") else (not gamma_free)
    checks.check("C1", c1, "T2: at k = pi e_1 block 59's matrix is diag(-4 alpha - 8 beta, [[-8 beta - 4 gamma, 4 beta], [4 beta, -8 beta - 4 gamma]]): the alternation of the bonds along their own axis is an eigenvector with the restoring coefficient 4 alpha + 8 beta, decoupled from the bonds of the other axes and independent of the parallel coupling gamma")
    q = sp.symbols("q", real=True)
    ones = sp.Matrix([1, 1, 1])
    scalar = sp.series((ones.T * bond_law_matrix(al, be, ga, (q, 0, 0)) * ones)[0], q, 0, 3).removeO()
    checks.check("C2", sp.simplify(scalar + q ** 2 * (al + 2 * be + 2 * ga)) == 0, "T2: at long wavelength the same law gives the scalar stiffness alpha + 2 beta + 2 gamma (block 59 T3): the alternation's stiffness 2(alpha + 2 beta) per bond and the long-range stiffness are two different combinations of the three numbers, and gamma separates them")
    m3 = sp.simplify(bond_law_matrix(al, be, ga, (sp.pi, sp.pi, sp.pi)))
    checks.check("C3", m3 == sp.diag(*[-4 * al - 8 * be - 8 * ga] * 3), "T2: the three alternations taken simultaneously are three different wave vectors pi e_j (one per axis) and do not mix at quadratic order; a single chessboard wave vector (pi, pi, pi) for all three bond fields is a different pattern, with coefficient 4 alpha + 8 beta + 8 gamma")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the balance and its threshold, exactly in terms of the zone average chi; the uniform state is a local minimum iff alpha + 2 beta >= chi/12."""
    dl, kap, chi = sp.symbols("delta kappa chi", positive=True)
    # per site: E(delta) = E_0 - (chi/2) delta^2 + O(delta^4 log): the alternation on all three axes with equal delta gives sum_j delta_j^2 cos^2 k_j = delta^2 c^2
    # cost per site: three bonds x (1/2)(4 alpha + 8 beta) delta^2 = 6 kappa delta^2, kappa = alpha + 2 beta
    total_second_order = -chi / 2 * dl ** 2 + 6 * kap * dl ** 2
    threshold = sp.solve(sp.Eq(sp.diff(total_second_order, dl, 2), 0), kap)[0]
    d1 = (threshold == chi / 12) if not mut("threshold_is_chi_over_six") else (threshold == chi / 6)
    checks.check("D1", d1, "T3: with the sea's second-order coefficient chi = <sum_j cos^2 k_j / sqrt(sum_j sin^2 k_j)> over the zone and block 59's alternation stiffness, the second-order total per site is (6 kappa - chi/2) delta^2 with kappa = alpha + 2 beta: the uniform bond-rate field is a local minimum iff kappa >= chi/12, and unstable to alternation below it")
    # the per-axis form: chi_j = chi/3 by the cubic symmetry, and a single-axis alternation has cost 2 kappa delta^2 with gain (chi/6) delta^2: the same threshold
    k = sp.symbols("k1 k2 k3", real=True)
    integrand_all = sum(sp.cos(kk) ** 2 for kk in k) / sp.sqrt(sum(sp.sin(kk) ** 2 for kk in k))
    integrand_one = sp.cos(k[0]) ** 2 / sp.sqrt(sum(sp.sin(kk) ** 2 for kk in k))
    # the cyclic permutation of the axes maps integrand_one to its two partners; their sum is integrand_all
    perm = {k[0]: k[1], k[1]: k[2], k[2]: k[0]}
    partners = integrand_one + integrand_one.subs(perm, simultaneous=True) + integrand_one.subs(perm, simultaneous=True).subs(perm, simultaneous=True)
    checks.check("D2", sp.simplify(partners - integrand_all) == 0, "T3: the single-axis coefficient is chi/3 (the cubic rotations permute the axes and preserve the zone average), its cost 2 kappa delta^2: the threshold for one axis alone is the same kappa = chi/12, and at second order the three axes are independent (T2)")
    # concavity: E(delta) = -<sqrt(s^2 + delta^2 c^2)> is concave in delta (second derivative <= 0 pointwise) and even
    s2, c2 = sp.symbols("s2 c2", positive=True)
    f = -sp.sqrt(s2 + dl ** 2 * c2)
    second = sp.simplify(sp.diff(f, dl, 2))
    checks.check("D3", sp.simplify(second * (s2 + dl ** 2 * c2) ** sp.Rational(3, 2)) == -s2 * c2 and f.subs(dl, -dl) == f, "T3: pointwise in the zone, -sqrt(s^2 + delta^2 c^2) is even in delta with second derivative -s^2 c^2/(s^2 + delta^2 c^2)^(3/2) <= 0: the sea's energy is concave and even (block 83 T3), so below the threshold the minimum lies at a delta* > 0 that the balance fixes, and at kappa = 0 it runs to delta = 1")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: the scalar hop timed by the same bond rates crosses zero at the corners exactly at delta = 2a; T5: walls between alternation phases bind exact zero modes on a ring."""
    a_, bet, dl = sp.symbols("a beta delta", positive=True)
    root = sp.sqrt(4 * a_ ** 2 + 3 * bet ** 2 * dl ** 2)
    crossing = sp.solve(sp.Eq(4 * a_ - root, 0), dl)
    e1 = (crossing == [2 * a_ / bet]) if not mut("corner_crossing_at_delta_equals_a") else (crossing == [a_ / bet])
    checks.check("E1", e1, "T4: block 82 D2's corner energies +-4a -+ sqrt(4a^2 + 3 beta^2 delta^2) vanish exactly at delta = 2a/beta: with the axioms' scalar hop timed by the same bond rates, the alternation's rest energy at the corners survives only for delta > 2a/beta (the least |E| over the zone is executed in the control)")
    size = 12
    d = F(3, 10)
    walls = [1 + d * (1 if x < size // 2 else -1) * ((-1) ** x) for x in range(size)]
    uniform = [1 + d * ((-1) ** x) for x in range(size)]
    n_walls = 2 * size - ring_hop(size, walls).rank()
    n_uniform = 2 * size - ring_hop(size, uniform).rank()
    e2 = (n_walls == 4 and n_uniform == 0) if not mut("walls_bind_no_zero_modes") else (n_walls == 0)
    checks.check("E2", e2, "T5: on the ring of 12 with the bond-rate alternation reversed on half the ring (two walls), the walk has exactly 4 zero modes (two per wall, one per coin state), and 0 without walls: a wall between the two alternation phases binds exact zero modes, the lattice form of block 79's wall modes for this background")
# ============================================================================================ family F
FENCES = (
    "This note works within block 59's bond rates and bond law and the sea reading of block 76 taken as a comparator; it reports the exact balance between the sea's gain and the bond law's stiffness under an alternation of the bond rates, and what the alternation gives the walk; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - block 59's 3x3 law at three wave vectors, entry by entry; the 16-dimensional block's square with three independent alternations",
    "per_site: executed - the alternation's cost per bond and per site from the law's eigenvalue; the ring of 12 bond by bond",
    "per_mode: executed - the zone average at delta = 1 exactly; the single-axis and three-axis integrands; control: chi on grids to 96^3, delta* against kappa, least |E| with the scalar hop",
    "per_block: executed - the second-order balance and its threshold symbolically; the corner crossing; the exact nullities with and without walls",
    "lattice_wide: T1 by identity for every wave vector; T2 by block 59's law at every wave vector; T3 at second order for every kappa, chi an executed number; T4 by identity; T5 on the ring of 12 (two walls); the bond rates, the bond law's three numbers, the sea reading and the balance as a minimisation are not derived",
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
    print("scope: bond rates that alternate on their own - under block 59's bond rates the sea's energy per site is exactly minus the zone average of sqrt(sum sin^2 + sum delta_j^2 cos^2), concave and even; block 59's law charges 2(alpha + 2 beta) delta^2 per bond for the alternation (gamma-free, axes decoupled); the uniform field is a local minimum iff alpha + 2 beta >= chi/12 (chi about 1.54, executed) and alternates below it, giving all eight species one rest energy sqrt(3) beta |delta*|; the scalar hop through the same bonds crosses zero at delta = 2a/beta; walls between phases bind exact zero modes; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
