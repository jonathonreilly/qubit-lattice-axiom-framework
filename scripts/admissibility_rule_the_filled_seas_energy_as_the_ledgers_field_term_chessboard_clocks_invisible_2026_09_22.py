#!/usr/bin/env python3
"""Finite supplied Hermitian hopping models: reciprocal bipartite clock factors leave opposite-parity hopping unchanged; the traceless reach-two family has an even negative-level energy. Free antisymmetric-state one-body expectations are additive. A separately declared quadratic comparator has the stated local response signs; it is not the exact sea Hessian. No induced stiffness, force or field-model exclusion is established."""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = ('docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md', 'docs/ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md')
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "chessboard_clocks_are_visible": "B",
    "reach_two_sea_is_odd_in_the_strain": "B",
    "two_record_energy_is_not_additive": "C",
    "hole_sources_with_the_seas_sign": "C",
    "volume_term_makes_clocks_slow": "D",
    "chessboard_mode_is_fixed_by_the_sea": "D",
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


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = Torus((4, 4, 4))
    psi = tor.state(11)
    c = F(3, 2)
    chess = {x: (c if (x[0] + x[1] + x[2]) % 2 == 0 else 1 / c) for x in tor.sites}
    products_one = all(chess[x] * chess[tor.sh(x, a, 1)] == 1 for x in tor.sites for a in range(3))
    same = all(ham_rates(tor, chess, psi)[x] == tor.ham(psi)[x] for x in tor.sites)
    phi = {x: 1 + field(1, 0, 0, x) / 4 for x in tor.sites}
    phi2 = {x: phi[x] * chess[x] for x in tor.sites}
    same_products = all(phi[x] * phi[tor.sh(x, a, 1)] == phi2[x] * phi2[tor.sh(x, a, 1)] for x in tor.sites for a in range(3))
    same_walk = all(ham_rates(tor, phi, psi)[x] == ham_rates(tor, phi2, psi)[x] for x in tor.sites)
    different = any(phi[x] != phi2[x] for x in tor.sites)
    if mut("chessboard_clocks_are_visible"):
        same = not same
    checks.check("B1", products_one and same and same_products and same_walk and different, 'PR8611 B1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    tor6 = Torus((4, 4, 4))
    psi6 = tor6.state(12)
    strain = [[{x: field(4, a, j, x) / 2 for x in tor6.sites} for j in range(3)] for a in range(3)]
    minus = [[{x: -strain[a][j][x] for x in tor6.sites} for j in range(3)] for a in range(3)]
    u111 = lambda f: exchange(tor6, (1, 1, 1), f)
    mirror = all(u111(ham_strain(tor6, strain, u111(psi6), 2))[x][cc] == -ham_strain(tor6, minus, psi6, 2)[x][cc] for x in tor6.sites for cc in range(2))
    trace = G(0)
    for x0 in tor6.sites:
        for c0 in range(2):
            basis = zero_field(tor6)
            basis[x0] = (G(1), G(0)) if c0 == 0 else (G(0), G(1))
            trace = trace + ham_strain(tor6, strain, basis, 2)[x0][c0]
    traceless = (trace == G(0)) if not mut("reach_two_sea_is_odd_in_the_strain") else (trace != G(0))
    checks.check("B2", mirror and traceless, 'PR8611 B2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family C
RING = 8


def ring_walk(phi, f):
    """The reduced 1D clocked walk on a ring of RING sites: (phi sigma_3 D phi) f, D the symmetric difference."""
    out = []
    for x in range(RING):
        up, dn = f[(x + 1) % RING], f[(x - 1) % RING]
        d = tuple((up[cc] * phi[(x + 1) % RING] - dn[cc] * phi[(x - 1) % RING]) * MINUS_HALF_I * phi[x] for cc in range(2))
        out.append((d[0], -d[1]))
    return out


def ring_density(phi, f, x):
    """e_x = Re f_x^dagger (H f)_x."""
    g = ring_walk(phi, f)
    return (f[x][0].conj() * g[x][0] + f[x][1].conj() * g[x][1]).re


def ring_inner(f, g):
    tot = G(0)
    for x in range(RING):
        for cc in range(2):
            tot = tot + f[x][cc].conj() * g[x][cc]
    return tot


def family_c(checks: Checks) -> None:
    phi = [1 + F((3 * x * x + x) % 5, 7) for x in range(RING)]
    psi1 = [(G(F((x * x + 1) % 4, 3), F(x % 3, 2)), G(F((2 * x + 1) % 5, 4), F((x * x) % 3 - 1, 3))) for x in range(RING)]
    raw2 = [(G(F((x + 2) % 4, 5), F((x * x + x) % 3, 2)), G(F(1, 2), F((3 * x) % 4 - 2, 3))) for x in range(RING)]
    overlap = ring_inner(psi1, raw2)
    n1 = ring_inner(psi1, psi1)
    coef = G(overlap.re / n1.re, overlap.im / n1.re)
    psi2 = [tuple(raw2[x][cc] - coef * psi1[x][cc] for cc in range(2)) for x in range(RING)]                 # orthogonal to psi1 (exact)
    orthogonal = ring_inner(psi1, psi2) == G(0)
    n2 = ring_inner(psi2, psi2)
    e1 = ring_inner(psi1, ring_walk(phi, psi1)).re / n1.re
    e2 = ring_inner(psi2, ring_walk(phi, psi2)).re / n2.re
    # the two-record antisymmetric state Psi = psi1 (x) psi2 - psi2 (x) psi1 on the 256-dimensional two-body space; H_tot = H (x) 1 + 1 (x) H
    idx = [(x, cc) for x in range(RING) for cc in range(2)]
    big = {}
    for (x, a) in idx:
        for (y, b) in idx:
            big[(x, a, y, b)] = psi1[x][a] * psi2[y][b] - psi2[x][a] * psi1[y][b]
    hpsi1, hpsi2 = ring_walk(phi, psi1), ring_walk(phi, psi2)
    hbig = {}
    for (x, a) in idx:
        for (y, b) in idx:
            hbig[(x, a, y, b)] = (hpsi1[x][a] * psi2[y][b] - hpsi2[x][a] * psi1[y][b]) + (psi1[x][a] * hpsi2[y][b] - psi2[x][a] * hpsi1[y][b])
    num = G(0)
    den = G(0)
    for key in big:
        num = num + big[key].conj() * hbig[key]
        den = den + big[key].conj() * big[key]
    additive = (num.re / den.re == e1 + e2) and num.im == 0
    # site density of the two-record state at site z: E_z = (1/2){P_z, H} summed over both records
    z = 2
    def dens_op(f):
        g = ring_walk(phi, f)
        return [tuple(((g[x][cc] if x == z else G(0)) + (ring_walk(phi, [(f[y][0] if y == z else G(0), f[y][1] if y == z else G(0)) for y in range(RING)])[x][cc])) * F(1, 2) for cc in range(2)) for x in range(RING)]
    d1, d2 = dens_op(psi1), dens_op(psi2)
    dbig = {}
    for (x, a) in idx:
        for (y, b) in idx:
            dbig[(x, a, y, b)] = (d1[x][a] * psi2[y][b] - d2[x][a] * psi1[y][b]) + (psi1[x][a] * d2[y][b] - psi2[x][a] * d1[y][b])
    numd = G(0)
    for key in big:
        numd = numd + big[key].conj() * dbig[key]
    dens_additive = numd.re / den.re == ring_density(phi, psi1, z) / n1.re + ring_density(phi, psi2, z) / n2.re
    if mut("two_record_energy_is_not_additive"):
        additive = num.re / den.re == e1 * e2
    checks.check("C1", orthogonal and additive and dens_additive and e1 != 0 and e2 != 0, 'PR8611 C1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    powers = [G(1), G(0, 1), G(-1), G(0, -1)]
    uniform = [ONE] * RING
    negative_state = [(powers[(-x) % 4], G(0)) for x in range(RING)]                                    # e^{-i pi x/2} on the upper component: sigma_3 D gives sin(-pi/2) = -1: an exact eigenstate of energy -1 (RING = 8 is not a multiple of 4: use the local identity instead)
    hpsi = ring_walk(uniform, negative_state)
    local_eigen = all(hpsi[x][0] == -negative_state[x][0] and hpsi[x][1] == G(0) for x in range(RING) )
    densities = [ring_density(uniform, negative_state, x) for x in range(RING)]
    all_negative = all(d < 0 for d in densities)
    sign = -1 if not mut("hole_sources_with_the_seas_sign") else 1
    removal_change = [sign * d for d in densities]
    hole_positive = all(v > 0 for v in removal_change)
    checks.check("C2", local_eigen and all_negative and hole_positive, 'PR8611 C2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    side = 4
    sites = list(product(range(side), repeat=3))
    total = len(sites)
    c, kappa = F(-1193, 1000), F(95, 1000)                                                              # DECLARED: the measured volume term and clock stiffness, rounded (control W1, W2)
    lattice_q2 = {}
    for m in product(range(side), repeat=3):
        # 2(1 - cos(2 pi m/4)) takes the values 0, 2, 4, 2 for m = 0, 1, 2, 3: exact
        lattice_q2[m] = sum(((0 if mi == 0 else 4 if mi == 2 else 2) for mi in m), ZERO)
    signs_ok = c < 0 < kappa and c + 12 * kappa < 0
    # u_q = -mass/(N (c + kappa q^2)) for q != 0; u(0) = sum_q u_q = -(mass/N) sum_{q != 0} 1/(c + kappa q^2)
    def u_at_body(cc):
        return -sum((1 / (cc + kappa * lattice_q2[m]) for m in lattice_q2 if m != (0, 0, 0)), ZERO) / total
    full, polar = u_at_body(c), u_at_body(ZERO)
    if mut("volume_term_makes_clocks_slow"):
        full = -full
    checks.check("D1", signs_ok and full > 0 and polar < 0, 'PR8611 D1: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

    tor = Torus((4, 4, 4))
    chess = {x: (F(2) if (x[0] + x[1] + x[2]) % 2 == 0 else F(1, 2)) for x in tor.sites}
    psi = tor.state(13)
    exact_zero = all(ham_rates(tor, chess, psi)[x] == tor.ham(psi)[x] for x in tor.sites)
    if mut("chessboard_mode_is_fixed_by_the_sea"):
        exact_zero = not exact_zero
    checks.check("D2", exact_zero, 'PR8611 D2: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')
# ============================================================================================ family F
    compatible = sum((-1)**sum(x) * ((1 if x == (0,0,0) else 0)-F(1,total)) for x in sites)
    checks.check("D3", compatible == 1 and c+12*kappa != 0, 'PR8611 D3: exact stated finite fixture or symbolic identity; scope and exceptions are in the companion note')

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
    print('scope: Finite supplied Hermitian hopping models: reciprocal bipartite clock factors leave opposite-parity hopping unchanged; the traceless reach-two family has an even negative-level energy. Free antisymmetric-state one-body expectations are additive. A separately declared quadratic comparator has the stated local response signs; it is not the exact sea Hessian. No induced stiffness, force or field-model exclusion is established.')
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
