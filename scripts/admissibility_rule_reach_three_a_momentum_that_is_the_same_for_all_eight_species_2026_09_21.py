#!/usr/bin/env python3
"""Exact checks: reach three (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 62, 63, 64, 68): block 54's walk H = sum_a sigma_a S_a and its eight species; block 63's relabelling with the lattice
momentum S_j, whose deformation has second-neighbour reach and the exactly conserved bond current as its response; block 68: that coupling shows the
species different lengths, (1 + B D)^T (1 + B D), while block 62's nearest-neighbour frame shows them the same lengths and has no exact current.
T1 (no momentum of reach one is the same for all species): a x sin k + b x cos k + c cannot vanish at k = 0 and k = pi with slope +1 at both.
T2 (a momentum of reach two that is): P_j = S_j C_j, symbol (1/2) sin 2k_j, (P_j psi)(x) = (psi(x + 2e_j) - psi(x - 2e_j))/(4i): it commutes with
   the walk, vanishes at all eight zeros with slope +1, and <P_j> is conserved for every state.
T3 (the relabelling it generates): for G = (1/2) sum_j {xi_j, P_j},  i[H, G] = sum_a sum_j sigma_a (1/2){C_a[d_a xi_j], P_j}: a deformation on the bonds
   along a with REACH THREE; its response is an exactly conserved current of the density Re psi^dagger P_j psi, divergence-free on stationary states.
T4 (one geometry for all eight): for a uniform strain coupled this way, H(k) = sum_a sigma_a [s_a + c_a sum_j B_a^j s_j c_j], H^2 is the sum of the
   squares, and EVERY species sees the inverse metric (1 + B)^T (1 + B): the same lengths and the same angles; bending over fall is 1 + beta for all.
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
    "docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "reach_one_momentum_serves_all_species": "B",
    "two_step_momentum_is_not_conserved": "B",
    "two_step_relabelling_has_reach_two": "C",
    "two_step_current_is_not_the_response": "C",
    "species_still_see_different_lengths": "D",
    "angles_are_still_mirrored": "D",
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


QUARTER_OVER_I = G(0, F(-1, 4))                                 # 1/(4i)


def p_op(tor: Torus, f, j):
    """(P_j f)(x) = (f(x + 2 e_j) - f(x - 2 e_j))/(4i): the symmetric difference over two steps, symbol (1/2) sin 2k_j = sin k_j cos k_j."""
    return {x: tuple((f[tor.sh(x, j, 2)][c] - f[tor.sh(x, j, -2)][c]) * QUARTER_OVER_I for c in range(2)) for x in tor.sites}


def relabel_p(tor: Torus, psi, xi):
    out = {x: (G(0), G(0)) for x in tor.sites}
    for j in range(3):
        out = tor.add(out, tor.add(tor.times(xi[j], p_op(tor, psi, j)), p_op(tor, tor.times(xi[j], psi), j)), F(1, 2))
    return out


def coin_matrix(vec):
    out = [[G(0), G(0)], [G(0), G(0)]]
    for a in range(3):
        out = mat_add(out, mat_scale(SIG[a], vec[a]))
    return out


TRIG = ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17)))
SPECIES = list(product((0, 1), repeat=3))


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    k = sp.symbols("k", real=True)
    a, b, c = sp.symbols("a b c", real=True)
    trial = a * sp.sin(k) + b * sp.cos(k) + c
    conditions = [trial.subs(k, 0), trial.subs(k, sp.pi), sp.diff(trial, k).subs(k, 0) - 1, sp.diff(trial, k).subs(k, sp.pi) - 1]
    sol = sp.solve(conditions, [a, b, c], dict=True)
    none = (sol == []) if not mut("reach_one_momentum_serves_all_species") else (sol != [])
    two = sp.sin(2 * k) / 2
    two_ok = two.subs(k, 0) == 0 and two.subs(k, sp.pi) == 0 and sp.diff(two, k).subs(k, 0) == 1 and sp.diff(two, k).subs(k, sp.pi) == 1
    checks.check("B1", none and two_ok, "T1, T2: no momentum of reach one, a sin k + b cos k + c, vanishes at k = 0 and k = pi with slope +1 at both (the four conditions have no solution); (1/2) sin 2k does: it is the symbol of the symmetric difference over two steps, and near every one of the walk's eight zeros it is the species' own wave number")

    tor = Torus((6, 5, 5))
    psi = tor.state(5)
    commute = True
    conserved = True
    for j in range(3):
        left = tor.ham(p_op(tor, psi, j))
        right = p_op(tor, tor.ham(psi), j)
        commute = commute and all(left[x] == right[x] for x in tor.sites)
        psidot = tor.scale(tor.ham(psi), MINUS_I)
        rate = sum(tor.redot(psidot, p_op(tor, psi, j)).values(), ZERO) + sum(tor.redot(psi, p_op(tor, psidot, j)).values(), ZERO)
        conserved = conserved and rate == 0
    if mut("two_step_momentum_is_not_conserved"):
        conserved = not conserved
    alive = any(tor.redot(psi, p_op(tor, psi, 0))[x] != 0 for x in tor.sites)
    checks.check("B2", commute and conserved and alive, "T2: on a 6x5x5 torus P_j commutes with the walk on a rational state (all sites, j = 1, 2, 3) and the total of Re psi^dagger P_j psi does not change in time for a state that is not stationary: a conserved momentum that is the same for all eight species")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    tor = Torus((6, 5, 5))
    psi = tor.state(7)
    xi = [{x: F((11 * j + 3 * x[0] * x[0] + 5 * x[1] + x[2] * x[1] + j * x[0]) % 17 - 8, 3) for x in tor.sites} for j in range(3)]
    commutator = tor.scale(tor.add(tor.ham(relabel_p(tor, psi, xi)), relabel_p(tor, tor.ham(psi), xi), -1), I_UNIT)
    rhs = {x: (G(0), G(0)) for x in tor.sites}
    for a in range(3):
        for j in range(3):
            w = {x: xi[j][tor.sh(x, a, 1)] - xi[j][x] for x in tor.sites}
            term = tor.add(sym_hop(tor, p_op(tor, psi, j), a, w), p_op(tor, sym_hop(tor, psi, a, w), j))
            rhs = tor.add(rhs, tor.sg(a, tor.scale(term, F(1, 2))))
    same = all(commutator[x] == rhs[x] for x in tor.sites)
    lone = {x: (G(0), G(0)) for x in tor.sites}
    origin = (3, 2, 2)
    lone[origin] = (G(1), G(F(1, 3), F(1, 2)))
    image = tor.scale(tor.add(tor.ham(relabel_p(tor, lone, xi)), relabel_p(tor, tor.ham(lone), xi), -1), I_UNIT)
    dist = lambda x: sum(min((x[i] - origin[i]) % tor.dims[i], (origin[i] - x[i]) % tor.dims[i]) for i in range(3))
    reach = max(dist(x) for x in tor.sites if image[x] != (G(0), G(0)))
    target = 3 if not mut("two_step_relabelling_has_reach_two") else 2
    checks.check("C1", same and reach == target, "T3: i[H, G] psi = sum_a sum_j sigma_a (1/2){C_a[d_a xi_j], P_j} psi exactly at all 150 sites for a rational displacement and state, G = (1/2) sum_j {xi_j, P_j}; applied to an amplitude on one site it reaches sites three steps away: the relabelling generated with the species-blind momentum has reach three")

    expectation = sum(tor.redot(psi, commutator).values(), ZERO)
    pairing = ZERO
    for a in range(3):
        for j in range(3):
            pj = p_op(tor, psi, j)
            first = tor.redot(tor.up(psi, a), tor.sg(a, pj))
            second = tor.redot(tor.up(pj, a), tor.sg(a, psi))
            cur = {x: (first[x] + second[x]) / 2 for x in tor.sites}
            if mut("two_step_current_is_not_the_response"):
                cur = tor.current(psi, a, j)
            pairing += sum(((xi[j][tor.sh(x, a, 1)] - xi[j][x]) * cur[x] for x in tor.sites), ZERO)
    checks.check("C2", expectation == pairing, "T3: <psi| i[H, G] |psi> = sum over bonds of (d_a xi_j) K_a^j with K_a^j(x -> x + e_a) = (1/2) Re[psi^dagger(x + e_a) sigma_a (P_j psi)(x) + (P_j psi)^dagger(x + e_a) sigma_a psi(x)], for every state: block 63's current with P_j in place of S_j; it is the response to this deformation and, the left side vanishing on stationary states, divergence-free there")


# ============================================================================================ family D
STRAIN = [[F(1, 5), F(-1, 7), F(1, 9)], [F(1, 6), F(-1, 4), F(2, 11)], [F(-1, 8), F(1, 10), F(1, 3)]]


def family_d(checks: Checks) -> None:
    squares = True
    for n in SPECIES:
        s = [(-1) ** n[a] * TRIG[a][0] for a in range(3)]
        c = [(-1) ** n[a] * TRIG[a][1] for a in range(3)]
        v = [s[a] + c[a] * sum((STRAIN[a][j] * s[j] * c[j] for j in range(3)), ZERO) for a in range(3)]
        h2 = mat_mul(coin_matrix(v), coin_matrix(v))
        value = sum((x * x for x in v), ZERO)
        squares = squares and h2[0][0] == value and h2[1][1] == value and h2[0][1] == 0 and h2[1][0] == 0
    q = sp.symbols("q1 q2 q3", real=True)
    t = sp.symbols("t", positive=True)
    bs = sp.Matrix(3, 3, lambda a, j: sp.Symbol(f"B{a}{j}", real=True))
    qv = sp.Matrix(q)
    blind = True
    seen_all = (sp.eye(3) + bs).T * (sp.eye(3) + bs)
    for n in SPECIES:
        s = [(-1) ** n[a] * sp.sin(t * q[a]) for a in range(3)]
        c = [(-1) ** n[a] * sp.cos(t * q[a]) for a in range(3)]
        v = [s[a] + c[a] * sum(bs[a, j] * s[j] * c[j] for j in range(3)) for a in range(3)]
        quad = sp.expand(sp.series(sum(x ** 2 for x in v), t, 0, 3).removeO().coeff(t, 2))
        target = seen_all
        if mut("species_still_see_different_lengths"):
            dmat = sp.diag(*[(-1) ** x for x in n])
            target = (sp.eye(3) + bs * dmat).T * (sp.eye(3) + bs * dmat)
        if mut("angles_are_still_mirrored"):
            dmat = sp.diag(*[(-1) ** x for x in n])
            target = dmat * seen_all * dmat
        blind = blind and sp.expand(quad - (qv.T * target * qv)[0]) == 0
    beta, u = sp.symbols("beta u", real=True)
    ratio = sp.series(u + sp.log(sp.exp(beta * u)), u, 0, 2).removeO().coeff(u, 1)                       # hop rate w (1 + b), 1 + b = 1/l = (w/wbar)^beta, for every species
    checks.check("D1", squares and blind and sp.simplify(ratio - (1 + beta)) == 0, "T4: with a uniform strain coupled through P_j, H(k) = sum_a sigma_a [s_a + c_a sum_j B_a^j s_j c_j] and H^2 is the sum of the squares exactly at all eight species' rational wave vectors; near k = pi n + q EVERY species sees the inverse metric (1 + B)^T (1 + B) (exact symbolic expansion for a general strain): the same lengths and the same angles; with l = (wbar/w)^beta the bending is 1 + beta times the fall for all eight")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin and for the coupling of a bond strain as a relabelling's deformation; it reports a relabelling generated with a momentum that is the same for all of the walk's species, and what it costs; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — the four conditions on a momentum of reach one (no solution) and on (1/2) sin 2k; P_j against the walk at all 150 sites of a 6x5x5 torus",
    "per_site: executed — i[H, G] against sum sigma_a (1/2){C_a[d_a xi_j], P_j} at all 150 sites; the reach of the deformation from one site",
    "per_mode: executed — H^2 as the sum of squares at all eight species' rational wave vectors; the species' inverse metric (1 + B)^T (1 + B) by exact symbolic expansion for a general strain, all eight species",
    "per_block: executed — the conservation of the total two-step momentum for a state in motion; the expectation of i[H, G] against the pairing of the strain with the two-step current; bending over fall",
    "lattice_wide: T1 for every momentum of reach one along an axis; T2 and T3 for every state and displacement on every torus with sides of at least five and on the infinite lattice; T4 for every uniform strain and wave vector; whether a coupling may reach three, and whether the eight species are all physical, are not decided; the field's side is block 64's, unchanged",
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
    print("scope: reach three — no momentum of reach one is the same for all of the walk's eight species; the symmetric difference over two steps is, commutes with the walk and is conserved; the relabelling it generates is a bond deformation of reach three whose response is an exactly conserved current; a strain coupled this way shows every species the same inverse metric (1 + B)^T (1 + B): exact books and one geometry for all, at the price of reach")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
