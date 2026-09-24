#!/usr/bin/env python3
"""Exact local current and coin-density identities for the uniform supplied walk.
The specified infinitesimal unitary deformation generically reaches second neighbours;
special displacements may cancel it. No universal improved-current or q-only-symbol
no-go theorem is established by these finite tests.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "momentum_flows_through_sites": "B",
    "continuity_holds_only_at_rest": "B",
    "relabelling_is_nearest_neighbour": "C",
    "current_not_the_relabellings_response": "C",
    "site_response_is_the_bond_current": "D",
    "conserved_symbol_is_a_function_of_q": "D",
    "antisymmetric_part_has_no_torque": "E",
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


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = Torus((5, 5, 5))
    psi = tor.state(3)
    psidot = tor.scale(tor.ham(psi), MINUS_I)
    ok = True
    for j in range(3):
        sj = tor.s_op(psi, j)
        rate = tor.redot(psidot, sj)
        rate2 = tor.redot(psi, tor.s_op(psidot, j))
        div = {x: ZERO for x in tor.sites}
        for a in range(3):
            if mut("momentum_flows_through_sites"):
                th = tor.theta(psi, a, j)
                cur = {x: (th[x] + th[tor.sh(x, a, 1)]) / 2 for x in tor.sites}
            else:
                cur = tor.current(psi, a, j)
            for x in tor.sites:
                div[x] += cur[x] - cur[tor.sh(x, a, -1)]
        ok = ok and all(rate[x] + rate2[x] + div[x] == 0 for x in tor.sites)
    moving = any(tor.redot(psidot, tor.s_op(psi, 0))[x] != 0 for x in tor.sites)
    holds = ok if not mut("continuity_holds_only_at_rest") else (not ok)
    checks.check("B1", holds and moving, "T1: on a 5x5x5 torus, for a rational state that is NOT stationary, d(pi_j)/dt(x) + sum_a [J_a^j(x -> x + e_a) - J_a^j(x - e_a -> x)] = 0 exactly at all 125 sites for j = 1, 2, 3: momentum is conserved locally, and it flows on the bonds")

    x0 = (1, 2, 3)
    a0, j0 = 0, 1
    far = tor.sh(tor.sh(x0, a0, 1), j0, 1)                                                          # x + e_a + e_j: a second neighbour of x
    bumped = dict(psi)
    bumped[far] = (psi[far][0] + G(1, F(1, 3)), psi[far][1] + G(F(2, 5), 1))
    checks.check("B2", tor.current(bumped, a0, j0)[x0] != tor.current(psi, a0, j0)[x0] and tor.theta(bumped, a0, j0)[x0] == tor.theta(psi, a0, j0)[x0],
                 "T1: the current on the bond from x along a depends on the amplitude at x + e_a + e_j, a second neighbour of x, which block 62's site-placed response Theta_a^j(x) does not see: a three-site object")


# ============================================================================================ family C
def relabelling(tor: Torus, psi, xi):
    """G_xi psi = (1/2) sum_j {xi_j, S_j} psi."""
    out = {x: (G(0), G(0)) for x in tor.sites}
    for j in range(3):
        out = tor.add(out, tor.add(tor.times(xi[j], tor.s_op(psi, j)), tor.s_op(tor.times(xi[j], psi), j)), F(1, 2))
    return out


def sym_hop(tor: Torus, f, a, w):
    """(1/2)[w(x) f(x + e_a) + w(x - e_a) f(x - e_a)]: the symmetric hop along a weighted by a function w of the bond (stored at its lower site)."""
    upf, dnf = tor.up(f, a), tor.dn(f, a)
    return {x: tuple((upf[x][c] * w[x] + dnf[x][c] * w[tor.sh(x, a, -1)]) * F(1, 2) for c in range(2)) for x in tor.sites}


def family_c(checks: Checks) -> None:
    tor = Torus((5, 5, 5))
    psi = tor.state(5)
    xi = [{x: F((7 * j + 3 * x[0] + x[1] * x[1] + 2 * x[2] * x[0] + j * x[1]) % 11 - 5, 4) for x in tor.sites} for j in range(3)]
    commutator = tor.scale(tor.add(tor.ham(relabelling(tor, psi, xi)), relabelling(tor, tor.ham(psi), xi), -1), I_UNIT)
    rhs = {x: (G(0), G(0)) for x in tor.sites}
    for a in range(3):
        for j in range(3):
            w = {x: xi[j][tor.sh(x, a, 1)] - xi[j][x] for x in tor.sites}                              # d_a xi_j on the bond from x along a
            if mut("relabelling_is_nearest_neighbour"):
                wbar = {x: (w[x] + w[tor.sh(x, a, -1)]) / 2 for x in tor.sites}                       # a site-placed frame in its place: no hop along a
                term = tor.add(tor.times(wbar, tor.s_op(psi, j)), tor.s_op(tor.times(wbar, psi), j))
            else:
                term = tor.add(sym_hop(tor, tor.s_op(psi, j), a, w), tor.s_op(sym_hop(tor, psi, a, w), j))
            rhs = tor.add(rhs, tor.sg(a, tor.scale(term, F(1, 2))))
    same = all(commutator[x] == rhs[x] for x in tor.sites)
    checks.check("C1", same, "T2: i[H, G_xi] psi = sum_a sum_j sigma_a (1/2){(d_a xi_j) C_a, S_j} psi exactly at all 125 sites for rational xi and psi: what a relabelling of the sites generates is a deformation placed on the BONDS along a (the difference of xi_j across the bond) that hops along a and differences along j")

    expectation = sum(tor.redot(psi, commutator).values(), ZERO)
    pairing = ZERO
    for a in range(3):
        for j in range(3):
            cur = tor.current(psi, a, j)
            if mut("current_not_the_relabellings_response"):
                cur = tor.theta(psi, a, j)
            pairing += sum(((xi[j][tor.sh(x, a, 1)] - xi[j][x]) * cur[x] for x in tor.sites), ZERO)
    checks.check("C2", expectation == pairing, "T2: <psi| i[H, G_xi] |psi> = sum over bonds of (d_a xi_j) J_a^j exactly, for every state: the bond current is the response to the deformation a relabelling generates")

    small = Torus((4, 4, 4))
    st = stationary_state(small)
    hst = small.ham(st)
    eigen = all(hst[x] == st[x] for x in small.sites)
    div_ok = True
    nonzero = False
    for j in range(3):
        div = {x: ZERO for x in small.sites}
        for a in range(3):
            cur = small.current(st, a, j)
            nonzero = nonzero or any(cur[x] != cur[small.sh(x, a, -1)] for x in small.sites)
            for x in small.sites:
                div[x] += cur[x] - cur[small.sh(x, a, -1)]
        div_ok = div_ok and all(v == 0 for v in div.values())
    checks.check("C3", eigen and div_ok and nonzero, "T2: on a 4x4x4 torus a superposition of three plane waves (wave vectors pi/2 along each axis, coin along that axis) has H psi = psi exactly; its bond current is divergence-free at all 64 sites for each j, while the currents themselves vary from bond to bond")

    lone = {x: (G(0), G(0)) for x in tor.sites}
    origin = (2, 2, 2)
    lone[origin] = (G(1), G(0, F(1, 2)))
    image = tor.scale(tor.add(tor.ham(relabelling(tor, lone, xi)), relabelling(tor, tor.ham(lone), xi), -1), I_UNIT)
    support = {x for x in tor.sites if image[x] != (G(0), G(0))}
    dist = lambda x: sum(min((x[i] - origin[i]) % 5, (origin[i] - x[i]) % 5) for i in range(3))
    first_only = {x for x in tor.sites if tor.ham(lone)[x] != (G(0), G(0))}
    checks.check("C4", max(dist(x) for x in support) == 2 and any(dist(x) == 2 and sum(1 for i in range(3) if x[i] != origin[i]) == 2 for x in support)
                 and any(dist(x) == 2 and sum(1 for i in range(3) if x[i] != origin[i]) == 1 for x in support) and max(dist(x) for x in first_only) == 1,
                 "T4: applied to an amplitude on one site, H reaches the six nearest neighbours only, while i[H, G_xi] reaches second neighbours of both kinds, x +- e_a +- e_j and x +- 2 e_a: this tested displacement leaves the nearest-neighbour matrix class; the generic family is not closed")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    tor = Torus((5, 5, 5))
    psi = tor.state(8)
    ok = True
    gap = False
    for a in range(3):
        da = tor.add(tor.up(psi, a), psi, -1)
        for j in range(3):
            sj = tor.s_op(psi, j)
            dsj = tor.add(tor.up(sj, a), sj, -1)
            corr = tor.redot(da, tor.sg(a, dsj))
            th = tor.theta(psi, a, j)
            cur = tor.current(psi, a, j)
            for x in tor.sites:
                mean = (th[x] + th[tor.sh(x, a, 1)]) / 2
                expected = mean - corr[x] / 2 if not mut("site_response_is_the_bond_current") else mean
                ok = ok and cur[x] == expected
                gap = gap or corr[x] != 0
    checks.check("D1", ok and gap, "T3: J_a^j(x -> x + e_a) = (1/2)[Theta_a^j(x) + Theta_a^j(x + e_a)] - (1/2) Re (d_a psi)^dagger sigma_a (d_a S_j psi) exactly on all 375 bonds for all nine (a, j): the conserved current is the bond average of block 62's site response minus a term with two more differences along a")

    def spinor(s):
        return (G(1 + s[2]), G(s[0], s[1]))                                                          # eigenvector of s.sigma with eigenvalue +1 when |s| = 1

    s1 = (F(1, 3), F(2, 3), F(2, 3))
    s2 = (F(2, 3), F(1, 3), F(2, 3))
    c1, c2 = spinor(s1), spinor(s2)
    eig_ok = True
    for s, c in ((s1, c1), (s2, c2)):
        h = [[G(0), G(0)], [G(0), G(0)]]
        for a in range(3):
            h = mat_add(h, mat_scale(SIG[a], s[a]))
        eig_ok = eig_ok and mat_vec(h, c) == c
    m = []
    for a in range(3):
        v = mat_vec(SIG[a], c1)
        m.append(c2[0].conj() * v[0] + c2[1].conj() * v[1])                                           # M_a = chi'^dagger sigma_a chi
    weights = (ONE, ONE, ONE) if not mut("conserved_symbol_is_a_function_of_q") else (F(5, 4), F(5, 3), ONE)
    law = G(0)
    for a in range(3):
        law = law + m[a] * ((s1[a] - s2[a]) * weights[a])
    sin_h, cos_h, sin_k, cos_k = F(3, 5), F(4, 5), F(5, 13), F(12, 13)                                # half the difference and the mean of two wave numbers
    s_plus = sin_k * cos_h + cos_k * sin_h
    s_minus = sin_k * cos_h - cos_k * sin_h
    trig = s_plus - s_minus == 2 * sin_h * cos_k
    checks.check("D2", eig_ok and law == 0 and any(v != 0 for v in m) and trig, "T3: for two plane waves of equal energy with sines (1/3, 2/3, 2/3) and (2/3, 1/3, 2/3) the conserved law is sum_a (sin k_a - sin k'_a) M_a = 0 exactly, M_a = chi'^dagger sigma_a chi; and sin k_a - sin k'_a = 2 sin(q_a/2) cos(kbar_a): the symbol of the law carries the cosine of the MEAN wave number, component by component, a dependence of this displayed vertex, not a classification of all possible on-shell divergence laws")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    tor = Torus((5, 5, 5))
    psi = tor.state(11)
    psidot = tor.scale(tor.ham(psi), MINUS_I)
    theta = {(a, j): tor.theta(psi, a, j) for a in range(3) for j in range(3)}
    ok = True
    torque_seen = False
    for c in range(3):
        rate = tor.redot(psidot, tor.sg(c, psi))
        bond = tor.redot(psi, tor.up(psi, c))
        for x in tor.sites:
            torque = 2 * sum((sign * theta[(d, a)][x] for (cc, a, d), sign in EPS.items() if cc == c), ZERO)
            torque_seen = torque_seen or torque != 0
            used = torque if not mut("antisymmetric_part_has_no_torque") else ZERO
            ok = ok and 2 * rate[x] == used - (bond[x] - bond[tor.sh(x, c, -1)])
    checks.check("E1", ok and torque_seen, "T5: d(psi^dagger sigma_c psi)/dt = 2 sum eps_cad Theta_d^a - [b_c(x) - b_c(x - e_c)], b_c(x) = Re psi^dagger(x) psi(x + e_c), exactly at all 125 sites for c = 1, 2, 3 and a state that is not stationary: the antisymmetric part of the site response is the torque on the coin")

    small = Torus((4, 4, 4))
    st = stationary_state(small)
    pure_div = True
    alive = False
    for c in range(3):
        bond = small.redot(st, small.up(st, c))
        for x in small.sites:
            anti = 2 * sum((sign * small.theta(st, d, a)[x] for (cc, a, d), sign in EPS.items() if cc == c), ZERO)
            alive = alive or anti != 0
            pure_div = pure_div and anti == bond[x] - bond[small.sh(x, c, -1)]
    checks.check("E2", pure_div and alive, "T5: on the exactly stationary state of the 4x4x4 torus the coin's density does not change, and the antisymmetric part of Theta equals the lattice divergence of b_c at all 64 sites while not vanishing: for stationary states it is a pure divergence")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin; it reports exact identities of the walk - what it conserves, what a relabelling of the sites generates, and how block 62's site-placed response differs from the conserved current; nothing is adopted and no gravitational claim is made.",
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
    nodes=list(ast.walk(ast.parse(src)))
    float_hits=[n for n in nodes if isinstance(n,ast.Constant) and isinstance(n.value,float)]
    float_hits += [n for n in nodes if isinstance(n,ast.Call) and ((isinstance(n.func,ast.Name) and n.func.id in ('float','N')) or (isinstance(n.func,ast.Attribute) and n.func.attr in ('evalf','N')))]
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
    "per_element: executed — the continuity equation of the momentum density with its bond current at all 125 sites of a 5x5x5 torus for a state in motion; the dependence of the current on a second neighbour",
    "per_site: executed — the operator identity for i[H, G_xi] at all 125 sites; the bond current against the bond average of the site response on all 375 bonds for nine index pairs; the torque identity at all 125 sites",
    "per_mode: executed — two plane waves of equal energy with rational sines and rational coins: the conserved law with the symbol sin k_a - sin k'_a; the identity sin k - sin k' = 2 sin(q/2) cos(kbar) at rational points",
    "per_block: executed — an exactly stationary superposition on a 4x4x4 torus: H psi = psi, divergence-free bond currents that vary from bond to bond, and an antisymmetric site response that is a pure divergence and not zero",
    "lattice_wide: T1, T2, T3 (the real-space identity) and T5 are operator identities of block 54's walk in the identity frame and hold for every state on every torus and on the infinite lattice; T2's and T5's consequences hold for every stationary state; T3's plane-wave form holds for every pair of wave vectors; T4 generic range statement on lattices with distinct second neighbours; special displacements can cancel; rates, frames that vary, a member that would use the bond current, and any law for the rotation of the coin axes are not treated",
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
    print("scope: what the walk conserves — momentum flows on bonds through a three-site current; a relabelling of the sites generates exactly the deformation whose response that current is, with second-neighbour reach; the bond current is the endpoint average of the site response minus the stated difference-product term, the cosine of the mean wave number in a plane-wave pair; the antisymmetric part of the site response is the torque on the coin")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
