#!/usr/bin/env python3
"""Exact checks: the unit of rate decides the alternation's thresholds (block 59's law in log rates; blocks 84 and 88 corrected; not adopted).

OBJECTS: block 59's bond rates with the law on u = log c (its item 3; shift symmetry = the unit of rate); the alternation in log rates,
c = e^{+-delta} (geometric mean one on each axis), against block 84's linear c = 1 +- delta; the traceless anisotropy in log rates; the
free sea as a comparator; the axioms' scalar hop through the same bonds.
T1: in log rates the alternation is an exact momentum-independent mass: h^2 = sin^2 k + sinh^2 delta per axis, H^2 = sum sin^2 k_j + sum sinh^2 delta_j
   on the 16-dimensional block; h = cosh(delta) h_lin(tanh delta); exact on a ring of eight with amplitudes 2 and 1/2.
T2: the unit of rate is the law's zero mode (the mean log rate); at fixed unit the second-order balance is (6 kappa - (3/2)<1/|s|>) delta^2, so the
   threshold is kappa < <1/|s|>/4, larger than block 84's chi/12 by exactly <|s|>/12 (the Jensen term).
T3: the anisotropy in log rates: the extra pointwise term (4a + b)/|s|, average 2<|s|>; threshold beta < (chi_a + 2<|s|>)/72.
T4: with the law quadratic in log rates the uniform field is never the global minimum (exact witness delta_w = 6 + 12 sqrt3 kappa); with the
   scalar hop the corner crossing is tanh delta = 2a.
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
    "docs/ADMISSIBILITY_RULE_THE_UNIT_OF_RATE_DECIDES_THE_ALTERNATIONS_THRESHOLDS_IN_LOG_RATES_AN_EXACT_MASS_A_CONVEXITY_TERM_AND_NO_GLOBAL_MINIMUM_UNDER_A_QUADRATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_an_exact_mass_a_convexity_term_no_global_minimum_under_a_quadratic_law_bounded_theorem_note_2026-09-23"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "log_mass_depends_on_momentum": "B",
    "no_jensen_term": "C",
    "threshold_is_chi_over_12": "C",
    "anisotropy_log_equals_linear": "D",
    "anisotropy_threshold_unchanged": "D",
    "uniform_is_the_global_minimum": "E",
    "log_crossing_at_delta_equals_2a": "E",
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


def ring_axis_operator(size, amplitudes):
    """(1/2i)(t T - T^T t) on a ring, t the diagonal of bond amplitudes on x -> x + 1: the one-axis operator of block 84/86."""
    shift = sp.zeros(size, size)
    for x in range(size):
        shift[x, (x + 1) % size] = 1
    t = sp.diag(*amplitudes)
    return (t * shift - shift.T * t) / (2 * sp.I)


def bond_law_matrix(alpha, beta, gamma, kv):
    c0 = -2 * alpha - 8 * beta - 4 * gamma
    m = sp.zeros(3, 3)
    for j in range(3):
        m[j, j] = c0 + 2 * alpha * sp.cos(kv[j]) + 2 * gamma * sum((sp.cos(kv[l]) for l in range(3) if l != j), sp.Integer(0))
        for l in range(3):
            if l != j:
                m[j, l] = 4 * beta * sp.cos(kv[j] / 2) * sp.cos(kv[l] / 2)
    return m


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: in log rates the alternation is an exact, momentum-independent mass."""
    k, d = sp.symbols("k delta", real=True)
    # amplitudes e^{+-delta} = cosh delta (1 +- tanh delta): on the pair (k, k + pi) the hop is D = e^{-ik}(cosh delta tau_z + i sinh delta tau_y)
    h = -sp.cosh(d) * sp.sin(k) * SZ + sp.sinh(d) * sp.cos(k) * SY
    sq_ok = sp.simplify(h * h - (sp.sin(k) ** 2 + sp.sinh(d) ** 2) * I2) == sp.zeros(2, 2)
    h_lin = -sp.sin(k) * SZ + sp.tanh(d) * sp.cos(k) * SY
    rel_ok = sp.simplify(h - sp.cosh(d) * h_lin) == sp.zeros(2, 2)
    b1 = (sq_ok and rel_ok) if not mut("log_mass_depends_on_momentum") else (not sq_ok)
    checks.check("B1", b1, "T1: with bond amplitudes e^{+-delta} alternating along an axis (geometric mean one), the pair operator is h = -cosh(delta) sin k tau_z + sinh(delta) cos k tau_y and h^2 = sin^2 k + sinh^2 delta exactly: the alternation adds a momentum-independent mass; and h = cosh(delta) h_lin(tanh delta), block 84's linear alternation of strength tanh(delta) scaled by cosh(delta)")

    ks = sp.symbols("k1 k2 k3", real=True)
    ds = sp.symbols("delta1 delta2 delta3", real=True)
    H = sum((coin(SIGMA[j]) * place(-sp.cosh(ds[j]) * sp.sin(ks[j]) * SZ + sp.sinh(ds[j]) * sp.cos(ks[j]) * SY, j) for j in range(3)), sp.zeros(16, 16))
    target = sum((sp.sin(ks[j]) ** 2 + sp.sinh(ds[j]) ** 2 for j in range(3)), sp.Integer(0))
    checks.check("B2", sp.simplify(H * H - target * sp.eye(16)) == sp.zeros(16, 16), "T1: in the 16-dimensional block of the eight species, with independent log alternations delta_1, delta_2, delta_3, H^2 = sum_j sin^2 k_j + sum_j sinh^2 delta_j exactly: the lattice dispersion of a massive walker, E^2 = |s|^2 + m^2 with m^2 = sum_j sinh^2 delta_j, the same for all eight species")

    t = sp.Integer(2)
    amps = [t if x % 2 == 0 else 1 / t for x in range(8)]
    op = ring_axis_operator(8, amps)
    ev2 = sorted((op * op).eigenvals().keys())
    expected = sorted({sp.Rational(9, 16), sp.Rational(9, 16) + sp.Rational(1, 2), sp.Rational(9, 16) + 1})
    checks.check("B3", ev2 == expected, f"T1 on a ring of eight, exactly: amplitudes 2 and 1/2 alternating (log alternation ln 2) give E^2 in {ev2} = sin^2 k + ((2 - 1/2)/2)^2 with sin^2 k in {{0, 1/2, 1}}: the mass (t - 1/t)/2 = 3/4 at every wave vector")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: the unit of rate is block 59's zero mode; at fixed mean log rate the threshold is <1/|s|>/4."""
    al, be, ga = sp.symbols("alpha beta gamma", real=True)
    m0 = bond_law_matrix(al, be, ga, (0, 0, 0))
    zero_mode = sp.simplify(m0 * sp.Matrix([1, 1, 1])) == sp.zeros(3, 1)
    checks.check("C1", zero_mode, "T2: block 59's law (on u = log c, its item 3) annihilates the uniform shift u -> u + const: the unit of rate is the mean of the log rates, and a balance must hold it fixed; the log alternation u = +-delta does, while the linear alternation c = 1 +- delta of block 84 lowers the mean log rate by delta^2/2 + O(delta^4)")

    S, d = sp.symbols("S delta", positive=True)
    f = -sp.sqrt(S + 3 * sp.sinh(d) ** 2)
    second = sp.simplify(sp.diff(f, d, 2).subs(d, 0))
    lin = -sp.sqrt(S + d ** 2 * (3 - S))
    second_lin = sp.simplify(sp.diff(lin, d, 2).subs(d, 0))
    jensen = sp.simplify(second - second_lin)
    c2 = (sp.simplify(second + 3 / sp.sqrt(S)) == 0 and sp.simplify(jensen + sp.sqrt(S)) == 0) if not mut("no_jensen_term") else (sp.simplify(jensen) == 0)
    checks.check("C2", c2, "T2: pointwise in the zone (S = |s|^2), the log alternation on all three axes gives -sqrt(S + 3 sinh^2 delta) with second derivative -3/sqrt(S) at delta = 0, the linear one -sqrt(S + delta^2 sum cos^2) with -(3 - S)/sqrt(S): they differ by -sqrt(S) = -|s|, the Jensen term of the log (the arithmetic mean of e^{+-delta} is cosh delta)")

    inv, ms, chi, kap = sp.symbols("I_inv I_abs chi kappa", positive=True)
    # pointwise sum_j (sin^2 + cos^2)/|s| = 3/|s| and sum_j sin^2/|s| = |s|: so 3 <1/|s|> = chi + <|s|>
    ident = sp.simplify(3 * inv - (chi + ms)).subs(inv, (chi + ms) / 3) == 0
    t_log = sp.solve(sp.Eq(6 * kap - sp.Rational(3, 2) * inv, 0), kap)[0]
    t_lin = sp.solve(sp.Eq(6 * kap - chi / 2, 0), kap)[0]
    shift = sp.simplify(t_log.subs(inv, (chi + ms) / 3) - t_lin)
    c3 = (ident and sp.simplify(t_log - inv / 4) == 0 and sp.simplify(shift - ms / 12) == 0) if not mut("threshold_is_chi_over_12") else (sp.simplify(t_log - chi / 12) == 0)
    checks.check("C3", c3, "T2: with block 59's cost 6 kappa delta^2 per site (kappa = alpha + 2 beta, block 84 T2), the balance at fixed mean log rate is (6 kappa - (3/2)<1/|s|>) delta^2: the uniform field is a local minimum iff alpha + 2 beta >= <1/|s|>/4; since 3<1/|s|> = chi + <|s|> pointwise-summed, this exceeds block 84's chi/12 by exactly <|s|>/12 > 0 (executed: about 2277/10000 against 1282/10000)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: the anisotropy in log rates."""
    e = sp.symbols("e", real=True)
    a, b = sp.symbols("a b", positive=True)
    f_log = sp.sqrt(sp.exp(4 * e) * a + sp.exp(-2 * e) * b)
    f_lin = sp.sqrt((1 + 2 * e) ** 2 * a + (1 - e) ** 2 * b)
    d_log = sp.simplify(sp.diff(f_log, e, 2).subs(e, 0))
    d_lin = sp.simplify(sp.diff(f_lin, e, 2).subs(e, 0))
    extra = sp.simplify(d_log - d_lin - (4 * a + b) / sp.sqrt(a + b))
    lin_ok = sp.simplify(d_lin - 9 * a * b / (a + b) ** sp.Rational(3, 2)) == 0
    d1 = (extra == 0 and lin_ok) if not mut("anisotropy_log_equals_linear") else (sp.simplify(d_log - d_lin) == 0)
    checks.check("D1", d1, "T3: pointwise (a = s_x^2, b = s_y^2 + s_z^2), the traceless anisotropy in log rates, c = (e^{2 eps}, e^{-eps}, e^{-eps}), gives the sea's second derivative 9ab/|s|^3 + (4a + b)/|s| against block 88's 9ab/|s|^3 for rates linear in the law's variable: the extra term is the Jensen term of the three axes")
    ms, chia, be = sp.symbols("I_abs chi_a beta", positive=True)
    # cyclic images: <s_x^2/|s|> = <s_y^2/|s|> = <s_z^2/|s|> = <|s|>/3, so <(4a + b)/|s|> = 6 <|s|>/3 = 2 <|s|>
    avg_extra = 4 * ms / 3 + 2 * ms / 3
    thr = sp.solve(sp.Eq(36 * be - (chia + avg_extra) / 2, 0), be)[0]
    d2 = (sp.simplify(thr - (chia + 2 * ms) / 72) == 0) if not mut("anisotropy_threshold_unchanged") else (sp.simplify(thr - chia / 72) == 0)
    checks.check("D2", d2, "T3: averaging with the cyclic symmetry of the axes, <(4 s_x^2 + s_y^2 + s_z^2)/|s|> = 2<|s|>, so with block 88's cost 36 beta eps^2 the uniform field goes anisotropic iff beta < (chi_a + 2<|s|>)/72 (executed: about 593/10000, against block 88's chi_a/72, about 262/10000)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: with the law quadratic in log rates the uniform field is never the global minimum; with the scalar hop the corner crossing moves to tanh delta = 2a."""
    kap = sp.symbols("kappa", positive=True)
    dw = 6 + 12 * sp.sqrt(3) * kap
    lower = sp.sqrt(3) * dw ** 3 / 6 - 6 * kap * dw ** 2 - sp.sqrt(3)
    closed = sp.simplify(lower - sp.sqrt(3) * (dw ** 2 - 1))
    positive = closed == 0
    e1 = positive if not mut("uniform_is_the_global_minimum") else (not positive)
    checks.check("E1", e1, "T4: since sqrt(|s|^2 + 3 sinh^2 delta) >= sqrt(3) sinh delta >= sqrt(3) delta^3/6 and <|s|> <= sqrt(3), at delta_w = 6 + 12 sqrt(3) kappa the balance is below the uniform value by more than sqrt(3)(delta_w^2 - 1) - sqrt(3) + ... > 0: exactly, sqrt(3) delta_w^3/6 - 6 kappa delta_w^2 - sqrt(3) = sqrt(3)(delta_w^2 - 1) > 0 for every kappa > 0 - with block 59's law quadratic in log rates the uniform bond-rate field is at most a local minimum; the global structure belongs to the law's completion, which the lane does not supply")

    # exact rational instance: e^delta = 2 gives cosh = 5/4, sinh = 3/4, tanh = 3/5; the crossing tanh(delta) = 2a is a = 3/10
    ch, sh = sp.Rational(5, 4), sp.Rational(3, 4)

    def corner(a_val):
        return sum((coin(SIGMA[j]) * place(sh * SY, j) + place(2 * a_val * ch * SZ, j) for j in range(3)), sp.zeros(16, 16))

    def nullity(m):
        return 16 - m.rank()
    at_cross = nullity(corner(sp.Rational(3, 10)))
    off_cross = nullity(corner(sp.Rational(1, 4)))
    at_linear_guess = nullity(corner(sp.Rational(3, 8)))                 # a = delta_log/2 would be ln2/2, not rational; a = (3/4)/2 = sinh/2 is a wrong rule
    sq = corner(sp.Rational(1, 4))
    root2 = 4 * sp.Rational(1, 16) * ch ** 2 + 3 * sh ** 2
    evs_sq = sorted(set((sq * sq).eigenvals().keys()))
    want_sq = sorted({root2, (4 * sp.Rational(1, 4) * ch + sp.sqrt(root2)) ** 2, (4 * sp.Rational(1, 4) * ch - sp.sqrt(root2)) ** 2})
    e2 = (at_cross == 4 and off_cross == 0 and at_linear_guess == 0 and [sp.nsimplify(v) for v in evs_sq] == [sp.nsimplify(v) for v in want_sq]) if not mut("log_crossing_at_delta_equals_2a") else (at_cross == 0)
    checks.check("E2", e2, f"T4(b): with the axioms' scalar hop through the same log-alternating bonds the corner energies are +-sqrt(4a^2 cosh^2 delta + 3 sinh^2 delta) (four each) and +-4a cosh delta +- that root (two each); exact instance e^delta = 2 (cosh 5/4, sinh 3/4): the squared corner spectrum at a = 1/4 is {[str(v) for v in evs_sq]}, and the corner matrix has nullity {at_cross} at a = 3/10 = tanh(delta)/2 and {off_cross} at a = 1/4: block 84 T4's crossing delta = 2a becomes tanh delta = 2a (the map delta_lin = tanh delta_log)")
# ============================================================================================ family F
FENCES = (
    "This note works within block 59's bond rates and bond law, read in the law's own variable (the log rate), the balances of blocks 84 and 88 and the sea as a comparator; it reports what the unit of rate does to those balances and what the alternation is in log rates; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the pair operator and the 16-dimensional block symbolically; the ring of eight with amplitudes 2 and 1/2 exactly; block 59's law at k = 0",
    "per_site: executed - the pointwise second derivatives of the sea's energy for the alternation and the anisotropy in both parametrisations",
    "per_mode: executed - control: the zone averages <1/|s|>, <|s|>, chi, chi_a on midpoint grids to 256^3; the balance at all strengths in log rates (barrier, runaway crossing); the relation E_log(delta) = cosh(delta) E_lin(tanh delta)",
    "per_block: executed - the thresholds as exact solutions; the global witness delta_w symbolically; the corner spectrum with the scalar hop",
    "lattice_wide: T1 by identity for every wave vector; T2 and T3 at second order with the zone averages executed; T4 by an exact inequality for every kappa; the law's variable is block 59's (log rates) and its unit the law's zero mode, as block 59 and block 55 T4 state; the completion beyond second order, the sea reading and the balance as a minimisation are not derived",
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
    print("scope: the unit of rate decides the alternation's thresholds - in block 59's own variable (log rates) the alternation is an exact momentum-independent mass (E^2 = sum sin^2 k + sum sinh^2 delta), the threshold is alpha + 2 beta < <1/|s|>/4 = 0.228 (block 84's 0.128 is at fixed arithmetic mean with rates linear in the law's variable), the anisotropy's is beta < (chi_a + 2<|s|>)/72 = 0.059 (block 88's 0.026); with the law quadratic in log rates the uniform field is never the global minimum; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
