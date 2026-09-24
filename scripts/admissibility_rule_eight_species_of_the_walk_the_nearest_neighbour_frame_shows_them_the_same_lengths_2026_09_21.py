#!/usr/bin/env python3
"""Supplied uniform lattice symbols have eight corner zeros. A uniform invertible frame gives conjugate principal quadratic forms DgD; a uniform strain gives leading forms (I+BD)^T(I+BD). A separately supplied axial smooth-ray comparison has local factors 1+beta or 1-beta at the reference rate. No universal packet fall or integrated bending law is established."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_EIGHT_SPECIES_OF_THE_WALK_THE_NEAREST_NEIGHBOUR_FRAME_SHOWS_THEM_THE_SAME_LENGTHS_THE_RELABELLINGS_COUPLING_SHOWS_THEM_DIFFERENT_LENGTHS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BOND_RATES_AND_LENGTHS_A_BODY_AT_REST_SOURCES_NO_LENGTH_AND_THE_BENDING_OF_RAYS_CARRIES_ONE_MORE_FREE_NUMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_eight_species_of_the_walk_the_nearest_neighbour_frame_shows_them_the_same_lengths_the_relabellings_coupling_shows_them_different_lengths_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "walk_has_one_species": "B",
    "species_fall_differently_in_a_rate_field": "B",
    "frame_shows_species_different_lengths": "C",
    "frame_shows_species_the_same_angles": "C",
    "strain_shows_species_the_same_lengths": "D",
    "strain_square_is_not_a_sum_of_squares": "D",
    "every_species_bends_alike_under_the_strain": "E",
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


# ============================================================================================ machinery on a torus of any size
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
MINUS_I = G(0, -1)
I_UNIT = G(0, 1)


class Torus:
    def __init__(self, dims):
        self.dims = dims
        self.sites = list(product(*(range(d) for d in dims)))

    def sh(self, x, a, step=1):
        return tuple((x[i] + (step if i == a else 0)) % self.dims[i] for i in range(3))

    def up(self, f, a):
        return {x: f[self.sh(x, a, 1)] for x in self.sites}

    def dn(self, f, a):
        return {x: f[self.sh(x, a, -1)] for x in self.sites}

    def s_op(self, f, j):
        return {x: tuple((f[self.sh(x, j, 1)][c] - f[self.sh(x, j, -1)][c]) * MINUS_HALF_I for c in range(2)) for x in self.sites}

    def sg(self, a, f):
        return {x: mat_vec(SIG[a], f[x]) for x in self.sites}

    def add(self, f, g, fac=1):
        return {x: tuple(f[x][c] + g[x][c] * fac for c in range(2)) for x in self.sites}

    def scale(self, f, fac):
        return {x: tuple(f[x][c] * fac for c in range(2)) for x in self.sites}

    def times(self, w, f):
        """A real site function times a spinor field."""
        return {x: tuple(f[x][c] * w[x] for c in range(2)) for x in self.sites}

    def ham(self, f):
        out = {x: (G(0), G(0)) for x in self.sites}
        for a in range(3):
            out = self.add(out, self.sg(a, self.s_op(f, a)))
        return out

    def redot(self, f, g):
        """Re f^dagger(x) g(x) at every site."""
        return {x: (f[x][0].conj() * g[x][0] + f[x][1].conj() * g[x][1]).re for x in self.sites}

    def state(self, seed):
        return {x: (G(F((seed * 7 + 3 * x[0] + x[1] * x[2] + x[0] * x[0]) % 5 - 2, 3), F((seed + x[0] * x[2] + 2 * x[1] + 5 * x[2]) % 7 - 3, 4)),
                    G(F((seed * 3 + x[0] * x[1] + 2 * x[2] + x[1] * x[1]) % 7 - 3, 5), F((seed * 5 + x[0] + 3 * x[1] + x[2] * x[2]) % 3 - 1, 2))) for x in self.sites}

    def theta(self, psi, a, j):
        return self.redot(psi, self.sg(a, self.s_op(psi, j)))

    def current(self, psi, a, j):
        """J_a^j on the bond from x to x + e_a, stored at x."""
        sj = self.s_op(psi, j)
        first = self.redot(self.up(psi, a), self.sg(a, sj))
        second = self.redot(self.up(sj, a), self.sg(a, psi))
        return {x: (first[x] + second[x]) / 2 for x in self.sites}


def stationary_state(tor: Torus):
    """On a 4x4x4 torus: plane waves with one wave-vector component pi/2 and the coin along that axis have H psi = psi exactly (Gaussian rationals)."""
    spinors = {0: (G(1), G(1)), 1: (G(1), G(0, 1)), 2: (G(1), G(0))}
    weights = {0: G(F(2, 3), F(1, 5)), 1: G(F(-1, 2), F(3, 4)), 2: G(F(5, 7), F(-1, 3))}
    powers = [G(1), G(0, 1), G(-1), G(0, -1)]
    psi = {x: (G(0), G(0)) for x in tor.sites}
    for axis in range(3):
        for x in tor.sites:
            ph = powers[x[axis] % 4] * weights[axis]
            psi[x] = tuple(psi[x][c] + spinors[axis][c] * ph for c in range(2))
    return psi


def sym_hop(tor: Torus, f, a, w):
    """(1/2)[w(x) f(x + e_a) + w(x - e_a) f(x - e_a)]: the symmetric hop along a weighted by a function w of the bond (stored at its lower site)."""
    upf, dnf = tor.up(f, a), tor.dn(f, a)
    return {x: tuple((upf[x][c] * w[x] + dnf[x][c] * w[tor.sh(x, a, -1)]) * F(1, 2) for c in range(2)) for x in tor.sites}


def coin_matrix(vec):
    out = [[G(0), G(0)], [G(0), G(0)]]
    for a in range(3):
        out = mat_add(out, mat_scale(SIG[a], vec[a]))
    return out


def square(mat):
    return mat_mul(mat, mat)


def is_scalar(mat, value):
    return mat[0][0] == value and mat[1][1] == value and mat[0][1] == 0 and mat[1][0] == 0


# rational sines and cosines from right triangles
TRIG = ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)))


def species_point(n):
    """sin and cos of k_a = pi n_a + q_a with the rational (sin q_a, cos q_a) above."""
    s = [(-1) ** n[a] * TRIG[a][0] for a in range(3)]
    c = [(-1) ** n[a] * TRIG[a][1] for a in range(3)]
    return s, c


SPECIES = list(product((0, 1), repeat=3))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    zeros = [n for n in product(range(4), repeat=3) if all(v == 0 for v in (([ZERO, ONE, ZERO, -ONE][n[a]]) for a in range(3)))]      # k_a in {0, pi/2, pi, 3pi/2}: sin k_a
    count = len(zeros) if not mut("walk_has_one_species") else 1
    squares_ok = True
    for n in SPECIES:
        s, c = species_point(n)
        h2 = square(coin_matrix(s))
        squares_ok = squares_ok and is_scalar(h2, sum((v * v for v in s), ZERO))
    q = sp.symbols("q1 q2 q3", real=True)
    t = sp.symbols("t", positive=True)
    lead_ok = True
    for n in SPECIES:
        lin = [sp.series(sp.sin(sp.pi * n[a] + t * q[a]), t, 0, 2).removeO().coeff(t, 1) for a in range(3)]
        lead_ok = lead_ok and all(sp.simplify(lin[a] - (-1) ** n[a] * q[a]) == 0 for a in range(3))
    checks.check("B1", count == 8 and squares_ok and lead_ok, 'PR8599 B1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    rate = F(7, 4)
    same = True
    for n in SPECIES:
        s, c = species_point(n)
        energy2 = sum((v * v for v in s), ZERO)
        clocked2 = square(mat_scale(coin_matrix(s), rate))
        same = same and is_scalar(clocked2, rate * rate * energy2)
    if mut("species_fall_differently_in_a_rate_field"):
        same = not same
    checks.check("B2", same, 'PR8599 B2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family C
FRAME = [(F(3, 2), F(1, 5), ZERO), (F(1, 2), F(4, 3), F(-1, 4)), (F(1, 7), F(2, 3), F(5, 6))]             # FRAME[j] = the coin vector of bond direction j


def family_c(checks: Checks) -> None:
    g = [[sum((FRAME[i][a] * FRAME[j][a] for a in range(3)), ZERO) for j in range(3)] for i in range(3)]
    exact = True
    for n in SPECIES:
        s, c = species_point(n)
        h = [[G(0), G(0)], [G(0), G(0)]]
        for j in range(3):
            h = mat_add(h, mat_scale(coin_matrix(FRAME[j]), s[j]))
        value = sum((g[i][j] * s[i] * s[j] for i in range(3) for j in range(3)), ZERO)
        exact = exact and is_scalar(square(h), value)
        d = [(-1) ** n[a] for a in range(3)]
        mag = [TRIG[a][0] for a in range(3)]
        species_form = sum((d[i] * g[i][j] * d[j] * mag[i] * mag[j] for i in range(3) for j in range(3)), ZERO)
        exact = exact and value == species_form
    diag_same = True
    flips = True
    for n in SPECIES:
        d = [(-1) ** n[a] for a in range(3)]
        seen = [[d[i] * g[i][j] * d[j] for j in range(3)] for i in range(3)]
        diag_same = diag_same and all(seen[i][i] == g[i][i] for i in range(3))
        for i in range(3):
            for j in range(3):
                if i != j:
                    flips = flips and (seen[i][j] == (-g[i][j] if n[i] != n[j] else g[i][j]))
    lengths = diag_same if not mut("frame_shows_species_different_lengths") else (not diag_same)
    angles = flips if not mut("frame_shows_species_the_same_angles") else all(g[i][j] == 0 for i in range(3) for j in range(3) if i != j)
    checks.check("C1", exact and lengths and angles, 'PR8599 C1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family D
STRAIN = [[F(1, 5), F(-1, 7), F(1, 9)], [F(1, 6), F(-1, 4), F(2, 11)], [F(-1, 8), F(1, 10), F(1, 3)]]      # STRAIN[a][j] = B_a^j, uniform


def family_d(checks: Checks) -> None:
    sum_of_squares = True
    for n in SPECIES:
        s, c = species_point(n)
        v = [s[a] + c[a] * sum((STRAIN[a][j] * s[j] for j in range(3)), ZERO) for a in range(3)]
        h2 = square(coin_matrix(v))
        value = sum((x * x for x in v), ZERO)
        if mut("strain_square_is_not_a_sum_of_squares"):
            value = sum((x * x for x in s), ZERO)
        sum_of_squares = sum_of_squares and is_scalar(h2, value)
    checks.check("D1", sum_of_squares, 'PR8599 D1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    q = sp.symbols("q1 q2 q3", real=True)
    t = sp.symbols("t", positive=True)
    bs = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f"B{a}{j}", real=True))
    qv = sp.Matrix(q)
    metric_ok = True
    for n in SPECIES:
        dmat = sp.diag(*[(-1) ** x for x in n])
        s = sp.Matrix([(-1) ** n[a] * sp.sin(t * q[a]) for a in range(3)])
        c = [(-1) ** n[a] * sp.cos(t * q[a]) for a in range(3)]
        v = sp.Matrix([s[a] + c[a] * (bs.row(a) * s)[0] for a in range(3)])
        quad = sp.expand(sp.series(sum(x ** 2 for x in v), t, 0, 3).removeO().coeff(t, 2))
        seen = sp.eye(3) + bs * dmat
        metric_ok = metric_ok and sp.expand(quad - (qv.T * (seen.T * seen) * qv)[0]) == 0
    b = sp.Symbol("b", real=True)
    stretch = sp.diag(b, 0, 0)
    seen0 = ((sp.eye(3) + stretch * sp.diag(1, 1, 1)).T * (sp.eye(3) + stretch * sp.diag(1, 1, 1)))[0, 0]
    seen1 = ((sp.eye(3) + stretch * sp.diag(-1, 1, 1)).T * (sp.eye(3) + stretch * sp.diag(-1, 1, 1)))[0, 0]
    differ = (sp.expand(seen0 - (1 + b) ** 2) == 0 and sp.expand(seen1 - (1 - b) ** 2) == 0) if not mut("strain_shows_species_the_same_lengths") else (sp.expand(seen0 - seen1) == 0)
    checks.check("D2", metric_ok and differ, 'PR8599 D2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    tor = Torus((4, 4, 4))
    powers = [G(1), G(0, 1), G(-1), G(0, -1)]                                                          # exp(i k x) for k a multiple of pi/2
    sines, cosines = [ZERO, ONE, ZERO, -ONE], [ONE, ZERO, -ONE, ZERO]
    real_ok = True
    for modes in ((2, 1, 0), (3, 1, 2), (0, 1, 3)):                                                    # wave numbers (pi, pi/2, 0), (3pi/2, pi/2, pi), (0, pi/2, 3pi/2): species (1,0,0), (1,0,1), (0,0,1)
        coin = (G(F(2, 3), F(1, 5)), G(F(-1, 2), F(3, 4)))
        psi = {x: tuple(coin[cc] * powers[(modes[0] * x[0]) % 4] * powers[(modes[1] * x[1]) % 4] * powers[(modes[2] * x[2]) % 4] for cc in range(2)) for x in tor.sites}
        out = tor.ham(psi)
        for a in range(3):
            for j in range(3):
                w = {x: STRAIN[a][j] for x in tor.sites}
                term = tor.add(sym_hop(tor, tor.s_op(psi, j), a, w), tor.s_op(sym_hop(tor, psi, a, w), j))
                out = tor.add(out, tor.sg(a, tor.scale(term, F(1, 2))))
        s = [sines[m] for m in modes]
        c = [cosines[m] for m in modes]
        v = [s[a] + c[a] * sum((STRAIN[a][j] * s[j] for j in range(3)), ZERO) for a in range(3)]
        mat = coin_matrix(v)
        real_ok = real_ok and all(out[x] == mat_vec(mat, psi[x]) for x in tor.sites)
    checks.check("D3", real_ok, 'PR8599 D3: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    u, beta = sp.symbols("u beta", real=True)
    results = []
    for coupling in ("frame", "strain"):
        for d_a in (1, -1):
            lam = -beta * u                                                                           # l = (wbar/w)^beta, wbar = 1
            if coupling == "frame":
                log_rate = u - lam                                                                    # hop rate along a: w/l for every species
            else:
                bstrain = sp.exp(-lam) - 1                                                            # strain b with 1 + b = 1/l for the species n_a = 0
                log_rate = u + sp.log(1 + d_a * bstrain)                                              # species sees 1 + D_a b
            first = sp.series(log_rate, u, 0, 2).removeO().coeff(u, 1)
            results.append((coupling, d_a, sp.simplify(first)))
    frame_ok = all(r[2] == 1 + beta for r in results if r[0] == "frame")
    strain_plus = [r[2] for r in results if r[0] == "strain" and r[1] == 1][0]
    strain_minus = [r[2] for r in results if r[0] == "strain" and r[1] == -1][0]
    strain_ok = (sp.simplify(strain_plus - (1 + beta)) == 0 and sp.simplify(strain_minus - (1 - beta)) == 0) if not mut("every_species_bends_alike_under_the_strain") else (sp.simplify(strain_minus - (1 + beta)) == 0)
    checks.check("E1", frame_ok and strain_ok, 'PR8599 E1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


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
    print('scope: Supplied uniform lattice symbols have eight corner zeros. A uniform invertible frame gives conjugate principal quadratic forms DgD; a uniform strain gives leading forms (I+BD)^T(I+BD). A separately supplied axial smooth-ray comparison has local factors 1+beta or 1-beta at the reference rate. No universal packet fall or integrated bending law is established.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
