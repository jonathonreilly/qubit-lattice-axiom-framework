#!/usr/bin/env python3
"""Exact checks: the axioms' own generator and a staggered rest term (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 62, 63, 65, 69, 70): block 54 T1(a)'s complete hermitian covariant nearest-neighbour family on the qubit coin,
a0 + 2a sum_j cos k_j + sum_j sigma_j sin k_j; block 54 set a0 = a = 0 by ADDING an inversion symmetry the Lattice axiom does not contain (flagged
by the fork probe of 2026-09-22). The staggered on-site term m eps(x), eps = (-1)^{x+y+z}: a coin scalar, invariant under the proper rotations
about any site, breaking translation by one site (the form a chessboard background takes).
T1 (the a-term splits the eight zeros): energies a0 + 2a(3 - 2|n|) at the zero k = pi n: four levels, multiplicities 1:3:3:1, each level of ONE
   sense; the zeros stay (no gap).
T2 (the a-term breaks the species maps, not the reversal of motion): V_n H_a V_n != det(D_n) H_a for a != 0 (exact difference computed); Theta
   still commutes.
T3 (the staggered term): m eps anticommutes with every one-step operator (the walk, the a-hops, the frame, the twist hop, the reach-two and
   reach-three strain terms) and commutes with site fields; hence (H + m eps)^2 = H^2 + m^2 for the walk, and phi (H + m eps) phi = phi H phi + m w eps.
T4 (four massive pairs, two masses): with the a-term the zeros pair as (n, n + (111)) into energies a0 +- sqrt(m^2 + 4a^2(3 - 2|n|)^2):
   one pair of mass sqrt(m^2 + 36a^2), three pairs of mass sqrt(m^2 + 4a^2); all four equal m iff a = 0.
Exact arithmetic only (integers, Fractions, Gaussian rationals, exact symbolic algebra); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_THE_AXIOMS_OWN_GENERATOR_THE_SCALAR_HOP_SPLITS_THE_EIGHT_SPECIES_INTO_FOUR_LEVELS_OF_ONE_SENSE_AND_A_STAGGERED_TERM_GIVES_THEM_MASS_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_axioms_own_generator_the_scalar_hop_splits_the_eight_species_into_four_levels_of_one_sense_and_a_staggered_term_gives_them_mass_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "a_term_gaps_the_zeros": "B",
    "levels_mix_the_senses": "B",
    "species_maps_survive_the_a_term": "C",
    "staggered_term_commutes_with_one_step_hops": "D",
    "staggered_masses_are_equal_for_a_nonzero": "D",
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


QUARTER_OVER_I = G(0, F(-1, 4))                                 # 1/(4i)


def p_op(tor: Torus, f, j):
    """(P_j f)(x) = (f(x + 2 e_j) - f(x - 2 e_j))/(4i)."""
    return {x: tuple((f[tor.sh(x, j, 2)][c] - f[tor.sh(x, j, -2)][c]) * QUARTER_OVER_I for c in range(2)) for x in tor.sites}


def zero_field(tor: Torus):
    return {x: (G(0), G(0)) for x in tor.sites}


def field(tag, a, j, x):
    """A deterministic rational field that varies with every coordinate."""
    return F(((tag * 11 + 7 * a + 3 * j + 3 * x[0] * x[0] + 5 * x[1] + x[2] * x[1] + (a + 1) * x[0] + j * x[2]) % 7) - 3, 5 + tag)


def anti_site(tor: Torus, w, op, f):
    """{w, O} f = w O f + O (w f) for a real site function w."""
    return tor.add(tor.times(w, op(f)), op(tor.times(w, f)))


def ham_rates(tor, phi, f):
    return tor.times(phi, tor.ham(tor.times(phi, f)))


def ham_frame(tor, frame, f):
    """(1/2) sum_j {E^j . sigma, S_j} f, frame[a][j] a site function."""
    out = zero_field(tor)
    for a in range(3):
        for j in range(3):
            out = tor.add(out, tor.sg(a, anti_site(tor, frame[a][j], lambda g, j=j: tor.s_op(g, j), f)), F(1, 2))
    return out


def ham_strain(tor, strain, f, reach):
    """H f + sum_a sum_j sigma_a (1/2){C_a[B_a^j], M_j} f with M_j = S_j (reach two) or P_j (reach three); strain[a][j] a bond function."""
    mom = (lambda g, j: tor.s_op(g, j)) if reach == 2 else (lambda g, j: p_op(tor, g, j))
    out = tor.ham(f)
    for a in range(3):
        for j in range(3):
            term = tor.add(sym_hop(tor, mom(f, j), a, strain[a][j]), mom(sym_hop(tor, f, a, strain[a][j]), j))
            out = tor.add(out, tor.sg(a, term), F(1, 2))
    return out


def twist_parts(tor, theta, f):
    """Block 65: the frame rotation (1/2) sum_j {(theta x e_j) . sigma, S_j} f and the twist hop (1/2) sum_a C_a[d_a theta_a] f."""
    rot = zero_field(tor)
    for a in range(3):
        for j in range(3):
            for b in range(3):
                sign = EPS.get((a, b, j), 0)
                if sign:
                    rot = tor.add(rot, tor.sg(a, anti_site(tor, theta[b], lambda g, j=j: tor.s_op(g, j), f)), F(sign, 2))
    hop = zero_field(tor)
    for a in range(3):
        w = {x: theta[a][tor.sh(x, a, 1)] - theta[a][x] for x in tor.sites}
        hop = tor.add(hop, sym_hop(tor, f, a, w), F(1, 2))
    return rot, hop


def ham_twist(tor, theta, f):
    rot, hop = twist_parts(tor, theta, f)
    return tor.add(tor.add(tor.ham(f), rot), hop)


SPECIES = list(product((0, 1), repeat=3))


def species_data(n):
    d = [(-1) ** n[a] for a in range(3)]
    s = d[0] * d[1] * d[2]
    rho = [s * d[a] for a in range(3)]
    return d, s, rho


def exchange(tor: Torus, n, f):
    """V_n f: the site sign (-1)^{n.x} and the coin's half turn about the axis that rho_n keeps (none for rho_n = 1)."""
    d, s, rho = species_data(n)
    kept = [a for a in range(3) if rho[a] == 1]
    out = {}
    for x in tor.sites:
        sign = (-1) ** sum(n[a] * x[a] for a in range(3))
        v = f[x] if len(kept) == 3 else mat_vec(SIG[kept[0]], f[x])
        out[x] = tuple(v[c] * sign for c in range(2))
    return out


def same(tor, f, g, fac=1):
    return all(f[x][c] == g[x][c] * fac for x in tor.sites for c in range(2))


BIG = Torus((6, 6, 6))


QUARTER_OVER_I = G(0, F(-1, 4))


def p_op(tor: Torus, f, j):
    return {x: tuple((f[tor.sh(x, j, 2)][c] - f[tor.sh(x, j, -2)][c]) * QUARTER_OVER_I for c in range(2)) for x in tor.sites}


def c_op(tor: Torus, f, j):
    """(C_j f)(x) = (f(x + e_j) + f(x - e_j))/2."""
    return {x: tuple((f[tor.sh(x, j, 1)][c] + f[tor.sh(x, j, -1)][c]) * F(1, 2) for c in range(2)) for x in tor.sites}


def ham_a(tor: Torus, f, a0, a):
    """The axioms' own family: a0 + 2a sum_j C_j + sum_j sigma_j S_j."""
    out = tor.scale(f, a0)
    for j in range(3):
        out = tor.add(out, c_op(tor, f, j), 2 * a)
    return tor.add(out, tor.ham(f))


def stagger(tor: Torus, f):
    return {x: tuple(f[x][c] * ((-1) ** (x[0] + x[1] + x[2])) for c in range(2)) for x in tor.sites}


def ham_strain3(tor, strain, f):
    out = zero_field(tor)
    for a in range(3):
        for j in range(3):
            term = tor.add(sym_hop(tor, p_op(tor, f, j), a, strain[a][j]), p_op(tor, sym_hop(tor, f, a, strain[a][j]), j))
            out = tor.add(out, tor.sg(a, term), F(1, 2))
    return out


def ham_strain2_only(tor, strain, f):
    out = zero_field(tor)
    for a in range(3):
        for j in range(3):
            term = tor.add(sym_hop(tor, tor.s_op(f, j), a, strain[a][j]), tor.s_op(sym_hop(tor, f, a, strain[a][j]), j))
            out = tor.add(out, tor.sg(a, term), F(1, 2))
    return out


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    a0, a = sp.symbols("a0 a", real=True)
    k = sp.symbols("k1 k2 k3", real=True)
    symbol = a0 + 2 * a * sum(sp.cos(ki) for ki in k)
    levels = {}
    for n in SPECIES:
        e = sp.simplify(symbol.subs({k[i]: sp.pi * n[i] for i in range(3)}))
        levels.setdefault(sp.expand(e), []).append(n)
    expected = {sp.expand(a0 + 2 * a * (3 - 2 * m)): m for m in range(4)}
    four = set(levels) == set(expected)
    mult = all(len(levels[e]) == (1, 3, 3, 1)[expected[e]] for e in levels)
    one_sense = all(len({species_data(n)[1] for n in levels[e]}) == 1 for e in levels)
    if mut("levels_mix_the_senses"):
        one_sense = not one_sense
    # no gap: the vector part still vanishes at every zero, so the two branches meet there
    vec = [sp.sin(ki) for ki in k]
    still_zero = all(all(v.subs({k[i]: sp.pi * n[i] for i in range(3)}) == 0 for v in vec) for n in SPECIES)
    if mut("a_term_gaps_the_zeros"):
        still_zero = not still_zero
    checks.check("B1", four and mult and one_sense and still_zero, "T1: for the axioms' own family a0 + 2a sum cos k_j + sum sigma_j sin k_j (block 54 T1(a) without the imported inversion) the eight zeros sit at the four energies a0 + 2a(3 - 2|n|) with multiplicities 1:3:3:1, each level containing species of ONE sense (|n| even: sense +1; odd: -1), and at each of them the coin vector sin k still vanishes: the a-term splits the species in energy and gaps none of them")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    tor = BIG
    psi = tor.state(14)
    a0, a = F(1, 3), F(1, 5)
    broken = 0
    kept = 0
    for n in SPECIES:
        d, s, rho = species_data(n)
        left = exchange(tor, n, ham_a(tor, exchange(tor, n, psi), a0, a))
        right = tor.scale(ham_a(tor, psi, a0, a), s)
        # the exact difference: (1 - s) a0 psi + 2a sum_j (D_j - s) C_j psi
        diff = tor.scale(psi, (1 - s) * a0)
        for j in range(3):
            diff = tor.add(diff, c_op(tor, psi, j), 2 * a * (d[j] - s))
        exact = same(tor, tor.add(left, right, -1), diff)
        if n == (0, 0, 0):
            kept += 1 if same(tor, left, right) else 0
        else:
            broken += 1 if (exact and not same(tor, left, right)) else 0
    reversal = lambda f: {x: mat_vec(SIG[1], (f[x][0].conj(), f[x][1].conj())) for x in tor.sites}
    theta_ok = same(tor, reversal(ham_a(tor, psi, a0, a)), ham_a(tor, reversal(psi), a0, a))
    ok = kept == 1 and broken == 7 and theta_ok
    if mut("species_maps_survive_the_a_term"):
        ok = kept == 1 and broken == 0
    checks.check("C1", ok, "T2: with a0 = 1/3, a = 1/5 on a 6x6x6 torus, V_n H_a V_n psi - det(D_n) H_a psi = (1 - det D_n) a0 psi + 2a sum_j (D_j - det D_n) C_j psi exactly at all 216 sites, nonzero for the seven species n != 0: the a-term breaks block 70's exchange maps (the species are no longer exact copies), while the reversal of motion Theta still commutes with H_a")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    tor = BIG
    psi = tor.state(15)
    eps_psi = stagger(tor, psi)
    phi = {x: 1 + field(1, 0, 0, x) / 4 for x in tor.sites}
    frame = [[{x: (1 if a == j else 0) + field(2, a, j, x) / 3 for x in tor.sites} for j in range(3)] for a in range(3)]
    theta = [{x: field(3, b, b, x) / 2 for x in tor.sites} for b in range(3)]
    strain = [[{x: field(4, a, j, x) / 2 for x in tor.sites} for j in range(3)] for a in range(3)]
    odd_steps = [lambda f: tor.ham(f), lambda f: ham_a(tor, f, ZERO, F(1, 5)), lambda f: ham_frame(tor, frame, f), lambda f: tor.add(ham_twist(tor, theta, f), tor.ham(f), -1),
                 lambda f: ham_strain3(tor, strain, f)]
    anti = all(same(tor, stagger(tor, op(eps_psi)), op(psi), -1) for op in odd_steps)
    even = same(tor, stagger(tor, ham_strain2_only(tor, strain, eps_psi)), ham_strain2_only(tor, strain, psi))
    if mut("staggered_term_commutes_with_one_step_hops"):
        anti = all(same(tor, stagger(tor, op(eps_psi)), op(psi)) for op in odd_steps)
    anti = anti and even
    commutes_rates = same(tor, stagger(tor, tor.times(phi, eps_psi)), tor.times(phi, psi))
    m = F(2, 3)
    total = lambda f: tor.add(tor.ham(f), stagger(tor, f), m)
    sq = total(total(psi))
    h2 = tor.ham(tor.ham(psi))
    square = same(tor, sq, tor.add(h2, psi, m * m))
    clocked = tor.times(phi, total(tor.times(phi, psi)))
    rest = tor.add(tor.times(phi, tor.ham(tor.times(phi, psi))), tor.times({x: phi[x] * phi[x] for x in tor.sites}, stagger(tor, psi)), m)
    checks.check("D1", anti and commutes_rates and square and same(tor, clocked, rest), "T3: eps(x) = (-1)^{x+y+z} anticommutes with every operator that moves an odd number of steps - the walk, the a-hops, block 62's frame coupling (varying frame), block 65's twist hop, the reach-THREE strain term (varying strain) - at all 216 sites, COMMUTES with the reach-two strain term (an even number of steps) and with the rates; hence (H + m eps)^2 psi = (H^2 + m^2) psi exactly and phi (H + m eps) phi = phi H phi + m w eps: a staggered on-site term is a rest energy m timed by the local clock, for every species alike; under the reach-two coupling alone the mass does not square to a scalar")

    a0, a, m, c = sp.symbols("a0 a m c", real=True)
    s_len = sp.symbols("s", nonnegative=True)
    # basis {k, k + pi(1,1,1)} (x) coin: the vector part sigma.s has eigenvalues +-|s| and flips sign between the two points, as does c = sum cos
    for sgn in (1, -1):
        block = sp.Matrix([[a0 + 2 * a * c + sgn * s_len, m], [m, a0 - 2 * a * c - sgn * s_len]])
        ev = block.eigenvals()
        target = {a0 + sp.sqrt((2 * a * c + sgn * s_len) ** 2 + m ** 2): 1, a0 - sp.sqrt((2 * a * c + sgn * s_len) ** 2 + m ** 2): 1}
        assert all(any(sp.simplify(e - t) == 0 for t in target) for e in ev)
    masses = {abs(3 - 2 * mm): sp.sqrt(m ** 2 + 4 * a ** 2 * (3 - 2 * mm) ** 2) for mm in range(4)}
    two_values = len({sp.simplify(v) for v in masses.values()}) == 2 and sp.simplify(masses[3] - sp.sqrt(m ** 2 + 36 * a ** 2)) == 0 and sp.simplify(masses[1] - sp.sqrt(m ** 2 + 4 * a ** 2)) == 0
    equal_iff = sp.simplify(masses[3].subs(a, 0) - masses[1].subs(a, 0)) == 0 and sp.simplify(masses[3] - masses[1]) != 0
    if mut("staggered_masses_are_equal_for_a_nonzero"):
        two_values = len({sp.simplify(v) for v in masses.values()}) == 1
    checks.check("D2", two_values and equal_iff, "T4: with the staggered term the wave vectors k and k + pi(1,1,1) mix in 2x2 blocks with energies a0 +- sqrt((2a sum cos k +- |sin k|)^2 + m^2) (exact symbolic eigenvalues); at the eight zeros the species pair as (n, n + (111)), opposite senses, into ONE pair of mass sqrt(m^2 + 36a^2) (the levels +-6a) and THREE pairs of mass sqrt(m^2 + 4a^2) (the levels +-2a); all four masses equal m iff a = 0")
# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin; it reports what the complete family of covariant nearest-neighbour generators allowed by the axioms does to the walk's eight species once an imported inversion symmetry is dropped, and what a staggered on-site term does; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed - the a-term's value and the coin vector at each of the eight zeros; the exact difference V_n H_a V_n - det(D) H_a for all eight species",
    "per_site: executed - the anticommutation of eps with six kinds of one-step operator (varying fields) and its commutation with the rates at all 216 sites of a 6x6x6 torus; the square of H + m eps and the clocked form at all sites",
    "per_mode: executed - the 2x2 blocks at k and k + pi(111): exact symbolic eigenvalues; the four masses at the zeros",
    "per_block: executed - the 1:3:3:1 count of the levels and the one-sense property of each level",
    "lattice_wide: T1, T2, T4 for every a0, a, m (symbolic); T3 an operator identity for every state and field on every even torus and on the infinite lattice; whether the a-term or a staggered background is present, and which species are present, are not decided",
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
    print("scope: the axioms' own generator - dropping block 54's imported inversion, the scalar hop splits the eight species into four energy levels 1:3:3:1, each of one sense, gaps none, breaks the exchange maps and keeps the reversal of motion; a staggered on-site term anticommutes with every one-step operator and commutes with the rates: a rest energy timed by the local clock, pairing the species into one heavy and three light massive pairs (all equal iff a = 0)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
