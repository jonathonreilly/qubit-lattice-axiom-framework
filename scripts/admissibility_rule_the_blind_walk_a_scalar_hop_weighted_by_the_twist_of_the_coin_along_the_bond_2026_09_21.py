#!/usr/bin/env python3
"""Exact checks: the blind walk (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 62, 63, 64): block 54's walk H = sum_a sigma_a S_a with the qubit as coin; block 62's frame for the coin; block 63's
torque identity; block 64 T5: a field energy that does not see the coin's axes needs a content that does not see them either.
T1 (what a varying rotation of the coin axes does to the walk, exactly at first order): for every real theta(x),
      -(i/2)[theta.sigma, H] = (1/2) sum_j {(theta x e_j).sigma, S_j} + (1/2) sum_a C_a[d_a theta_a]:
   a rotation of the frame at every site (nearest-neighbour), PLUS a coin-independent symmetric hop along each bond weighted by the difference, along
   the bond, of the rotation about the bond's own axis (the twist).
T2 (the blind walk): give every site a rotation vartheta(x) coupled as H[vartheta] = H + (1/2) sum_j {(vartheta x e_j).sigma, S_j}
   + (1/2) sum_a C_a[d_a vartheta_a].  Then the first-order change of H[vartheta] under psi -> U psi, U = exp(-i theta.sigma/2), is that of
   vartheta -> vartheta + theta.  Without the scalar hop it is not.  H[vartheta] is hermitian and nearest-neighbour.
T3 (no torque): d<H[vartheta]>/d vartheta_c(x) at vartheta = 0 equals (1/2) d(psi^dagger sigma_c psi)(x)/dt for every state: zero at every site on a
   stationary state.  Without the scalar hop the response is sum eps_cad Theta_d^a, non-zero at all 64 sites of the stationary state of block 63.
T4 (what the scalar hop is): for a frame 1 + strain the inversion-odd scalar eps.T is 2 eps^jkl d_k B_jl: zero for a symmetric strain, 4 div vartheta
   for the rotation (vartheta x e_j); at long wavelength the scalar hop is (1/2) div vartheta = (1/8) eps.T: the term that block 64's blindness removed
   from the FIELD's energy is what the CONTENT needs in order to be blind.
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
    "docs/ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "rotation_needs_no_scalar_hop": "B",
    "scalar_hop_sits_on_the_sites": "B",
    "walk_without_the_hop_is_blind": "C",
    "blind_walk_is_not_hermitian": "C",
    "torque_survives_the_hop": "D",
    "bare_walk_has_no_torque": "D",
    "odd_scalar_sees_a_symmetric_strain": "E",
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


def inner_on(tor: Torus, phi, psi):
    tot = G(0)
    for x in tor.sites:
        for c in range(2):
            tot = tot + phi[x][c].conj() * psi[x][c]
    return tot


def coin_vector(tor: Torus, vec, f):
    """(v(x).sigma) f(x) for a real vector field v on the sites."""
    out = {x: (G(0), G(0)) for x in tor.sites}
    for c in range(3):
        out = tor.add(out, tor.times(vec[c], tor.sg(c, f)))
    return out


def frame_rotation(tor: Torus, f, theta):
    """(1/2) sum_j {(theta x e_j).sigma, S_j} f: the rotation of the frame at every site, to first order."""
    out = {x: (G(0), G(0)) for x in tor.sites}
    for j in range(3):
        cross = [{x: sum((sign * theta[c][x] for (c, jj, d), sign in EPS.items() if jj == j and d == dd), ZERO) for x in tor.sites} for dd in range(3)]   # (theta x e_j)_d = eps_cjd theta_c
        term = tor.add(coin_vector(tor, cross, tor.s_op(f, j)), tor.s_op(coin_vector(tor, cross, f), j))
        out = tor.add(out, tor.scale(term, F(1, 2)))
    return out


def scalar_hop(tor: Torus, f, theta, on_sites=False):
    """(1/2) sum_a C_a[d_a theta_a] f; with on_sites the weight is put on the sites instead (a potential (1/2) sum_a (theta_a(x + e_a) - theta_a(x - e_a))/2)."""
    out = {x: (G(0), G(0)) for x in tor.sites}
    for a in range(3):
        if on_sites:
            w = {x: (theta[a][tor.sh(x, a, 1)] - theta[a][tor.sh(x, a, -1)]) / 2 for x in tor.sites}
            out = tor.add(out, tor.scale(tor.times(w, f), F(1, 2)))
        else:
            w = {x: theta[a][tor.sh(x, a, 1)] - theta[a][x] for x in tor.sites}
            out = tor.add(out, tor.scale(sym_hop(tor, f, a, w), F(1, 2)))
    return out


def rational_vector(tor: Torus, seed):
    return [{x: F((seed * 7 + 5 * c + 3 * x[0] * x[0] + x[1] * (c + 2) + 2 * x[2] * x[1] + x[0] * x[2]) % 13 - 6, 5) for x in tor.sites} for c in range(3)]


def blind_walk(tor: Torus, f, vartheta, with_hop=True):
    out = tor.add(tor.ham(f), frame_rotation(tor, f, vartheta))
    if with_hop:
        out = tor.add(out, scalar_hop(tor, f, vartheta))
    return out


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = Torus((5, 4, 3))
    psi = tor.state(7)
    theta = rational_vector(tor, 2)
    lhs = tor.scale(tor.add(coin_vector(tor, theta, tor.ham(psi)), tor.ham(coin_vector(tor, theta, psi)), -1), G(0, F(-1, 2)))      # -(i/2)[theta.sigma, H] psi
    rhs = frame_rotation(tor, psi, theta)
    if not mut("rotation_needs_no_scalar_hop"):
        rhs = tor.add(rhs, scalar_hop(tor, psi, theta, on_sites=mut("scalar_hop_sits_on_the_sites")))
    hop_alive = any(scalar_hop(tor, psi, theta)[x] != (G(0), G(0)) for x in tor.sites)
    checks.check("B1", hop_alive and all(lhs[x] == rhs[x] for x in tor.sites), "T1: on a 5x4x3 torus, for a rational rotation field theta(x) and a rational state, -(i/2)[theta.sigma, H] psi = (1/2) sum_j {(theta x e_j).sigma, S_j} psi + (1/2) sum_a C_a[d_a theta_a] psi exactly at all 60 sites: a varying rotation of the coin axes is a rotation of the frame at every site PLUS a coin-independent symmetric hop on every bond, weighted by the difference along the bond of the rotation about the bond's own axis")

    uniform = [{x: F(3 + c, 7) for x in tor.sites} for c in range(3)]
    no_hop = all(scalar_hop(tor, psi, uniform)[x] == (G(0), G(0)) for x in tor.sites)
    twist_only = [{x: (F(x[1] * x[1] + 2 * x[2], 3) if c == 0 else ZERO) for x in tor.sites} for c in range(3)]                  # theta_1 depends on x_2, x_3 only: no twist along bond 1
    no_twist = all(scalar_hop(tor, psi, twist_only)[x] == (G(0), G(0)) for x in tor.sites)
    checks.check("B2", no_hop and no_twist, "T1: the scalar hop vanishes for a uniform rotation (block 62 T1) and for a rotation about axis 1 that does not change along axis 1: only the TWIST of the coin along a bond, the change along the bond of the rotation about that bond's axis, is felt")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    tor = Torus((5, 4, 3))
    psi, phi = tor.state(7), tor.state(10)
    vartheta = rational_vector(tor, 5)
    theta = rational_vector(tor, 2)
    with_hop = not mut("walk_without_the_hop_is_blind")
    # first-order change of H[vartheta] under U = exp(-i theta.sigma/2): -(i/2)[theta.sigma, H[vartheta]] at zeroth order in vartheta is -(i/2)[theta.sigma, H];
    # the change of vartheta -> vartheta + theta is H[vartheta + theta] - H[vartheta], linear in theta.
    shifted = [{x: vartheta[c][x] + theta[c][x] for x in tor.sites} for c in range(3)]
    change_field = tor.add(blind_walk(tor, psi, shifted, with_hop), blind_walk(tor, psi, vartheta, with_hop), -1)
    change_coin = tor.scale(tor.add(coin_vector(tor, theta, tor.ham(psi)), tor.ham(coin_vector(tor, theta, psi)), -1), G(0, F(-1, 2)))
    same = all(change_field[x] == change_coin[x] for x in tor.sites)
    hermitian = inner_on(tor, phi, blind_walk(tor, psi, vartheta)) == inner_on(tor, blind_walk(tor, phi, vartheta), psi)
    if mut("blind_walk_is_not_hermitian"):
        hermitian = not hermitian
    lone = {x: (G(0), G(0)) for x in tor.sites}
    origin = (2, 2, 1)
    lone[origin] = (G(1), G(F(1, 3), F(1, 2)))
    image = blind_walk(tor, lone, vartheta)
    dist = lambda x: sum(min((x[i] - origin[i]) % tor.dims[i], (origin[i] - x[i]) % tor.dims[i]) for i in range(3))
    nearest = max(dist(x) for x in tor.sites if image[x] != (G(0), G(0))) == 1
    checks.check("C1", same and hermitian and nearest, "T2: with a rotation vartheta(x) at every site coupled as H[vartheta] = H + (1/2) sum_j {(vartheta x e_j).sigma, S_j} + (1/2) sum_a C_a[d_a vartheta_a], the first-order change of the walk under psi -> exp(-i theta.sigma/2) psi is exactly the change vartheta -> vartheta + theta; H[vartheta] is hermitian and reaches nearest neighbours only: a walk that does not see a varying rotation of its coin axes, at first order, within nearest-neighbour hops")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    tor = Torus((5, 4, 3))
    psi = tor.state(7)
    psidot = tor.scale(tor.ham(psi), MINUS_I)
    site, c0 = (3, 1, 2), 1
    zero = [{x: ZERO for x in tor.sites} for _ in range(3)]
    bump = [dict(v) for v in zero]
    bump[c0][site] = ONE
    use_hop = not mut("torque_survives_the_hop")
    slope = inner_on(tor, psi, blind_walk(tor, psi, bump, use_hop)).re - inner_on(tor, psi, tor.ham(psi)).re
    rate = tor.redot(psidot, tor.sg(c0, psi))[site]                                                   # (1/2) d(psi^dagger sigma_c psi)/dt = Re psidot^dagger sigma_c psi
    moving = rate != 0
    checks.check("D1", moving and slope == rate, "T3: the derivative of <H[vartheta]> in the rotation at one site about one axis, by an exact difference, equals (1/2) d(psi^dagger sigma_c psi)/dt there, for a rational state in motion: the content's response to a rotation of its coin axes is the rate of change of the coin's own density, nothing else")

    small = Torus((4, 4, 4))
    st = stationary_state(small)
    eigen = all(small.ham(st)[x] == st[x] for x in small.sites)
    base = inner_on(small, st, small.ham(st)).re
    with_hop, without = [], []
    for c in range(3):
        for x in small.sites[::5]:
            b = [{y: ZERO for y in small.sites} for _ in range(3)]
            b[c][x] = ONE
            with_hop.append(inner_on(small, st, blind_walk(small, st, b, True)).re - base)
            without.append(inner_on(small, st, blind_walk(small, st, b, False)).re - base)
    bare_ok = all(v != 0 for v in without) if not mut("bare_walk_has_no_torque") else all(v == 0 for v in without)
    checks.check("D2", eigen and all(v == 0 for v in with_hop) and bare_ok, f"T3: on the exactly stationary state of the 4x4x4 torus (H psi = psi) the response to a rotation of the coin axes is ZERO at every sampled site and axis with the scalar hop ({len(with_hop)} samples), and non-zero at every one of them without it: block 64 T5's cost is paid, for the rotation of the coin axes, by a nearest-neighbour term")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    xs = sp.symbols("x y z", real=True)
    strain = sp.Matrix(3, 3, lambda j, l: sp.Function(f"B{j}{l}")(*xs))
    odd = lambda b: sum(sp.LeviCivita(j, k, l) * (sp.diff(b[j, l], xs[k]) - sp.diff(b[j, k], xs[l])) for j in range(3) for k in range(3) for l in range(3))
    general = sp.expand(odd(strain) - 2 * sum(sp.LeviCivita(j, k, l) * sp.diff(strain[j, l], xs[k]) for j in range(3) for k in range(3) for l in range(3))) == 0
    sym = sp.Matrix(3, 3, lambda j, l: sp.Function(f"S{min(j, l)}{max(j, l)}")(*xs))
    sym_zero = sp.expand(odd(sym)) == 0
    if mut("odd_scalar_sees_a_symmetric_strain"):
        sym_zero = not sym_zero
    th = [sp.Function(f"th{c}")(*xs) for c in range(3)]
    rot = sp.Matrix(3, 3, lambda j, d: sum(sp.LeviCivita(c, j, d) * th[c] for c in range(3)))           # frame[j, d] = (theta x e_j)_d = eps_cjd theta_c: the coin vector of bond direction j
    coframe = -rot.T                                                                                  # the co-frame's strain is minus the transpose of the frame's, at first order
    div = sum(sp.diff(th[c], xs[c]) for c in range(3))
    value = sp.expand(odd(coframe))
    checks.check("E1", general and sym_zero and sp.expand(value + 4 * div) == 0, "T4: for a frame 1 + strain the inversion-odd scalar eps.T of the co-frame is 2 eps^jkl d_k B_jl at first order: zero for every symmetric strain, and -4 div vartheta for the rotation of T1; at long wavelength the scalar hop (1/2) sum_a (d_a vartheta_a) cos k_a is (1/2) div vartheta = -(1/8) eps.T: the scalar that blindness removed from the FIELD's energy (block 64 T2, c5 = 0) is what the CONTENT needs")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin; it reports what a rotation of the coin axes that varies from site to site does to the walk, exactly at first order, and the nearest-neighbour term that makes the walk blind to it; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — the operator identity for -(i/2)[theta.sigma, H] at all 60 sites of a 5x4x3 torus for a rational rotation field and state; the vanishing of the scalar hop for a uniform rotation and for a rotation without twist",
    "per_site: executed — the first-order change of H[vartheta] under a rotation of the coin against the shift of vartheta, site by site; hermiticity; nearest-neighbour reach; the derivative of <H[vartheta]> in one site's rotation against the rate of change of the coin's density",
    "per_mode: executed — the inversion-odd scalar of a frame's curl at first order: for a general strain, for a symmetric strain, for the rotation of T1 (exact symbolic algebra)",
    "per_block: executed — the exactly stationary state of the 4x4x4 torus: the response to a rotation of the coin axes with and without the scalar hop at 39 sampled sites and axes",
    "lattice_wide: T1 is an operator identity for every rotation field and state on every torus and on the infinite lattice; T2 and T3 hold at first order in the rotation around the identity frame, for every state, their consequence for every stationary state; T4 is a continuum identity at first order in the strain; a walk blind beyond first order, around a frame that is not the identity, or together with block 64's bond strains is not constructed; that sites carry a rotation field and that the walk has the scalar hop are not derived",
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
    print("scope: the blind walk — a rotation of the coin axes that varies from site to site acts on the walk, at first order, as a rotation of the frame at every site plus a coin-independent symmetric hop weighted by the twist of the coin along each bond; with that hop the walk does not see the rotation, the response to it is half the rate of change of the coin's density and vanishes on stationary states; at long wavelength the hop is one eighth of the inversion-odd scalar of the frame's curl")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
