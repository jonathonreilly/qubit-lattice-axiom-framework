#!/usr/bin/env python3
"""Exact checks: which species' fall the ledger owes (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 63, 64, 66, 69, 70): the clocked walk H_w = phi H phi; block 66: a field energy counted per local tick and blind to
relabellings requires of the content that its stress gradient equal its weight, and for the relabelling generated with S_j the walk's exact law is
d<G_xi>/dt = sum (d xi) J[phi psi] - sum xi f, with f_j = e d_j u at leading order for a SMOOTH amplitude (the first species); block 69's relabelling
generated with the two-step momentum P_j = S_j C_j; block 70's exchange maps V_n.
T1 (the walk's law for the two-step relabelling, exactly): i[phi, P_j] = -(1/2) C2_j[d2_j phi] (a two-step hop weighted by the two-step difference);
   i[H_w, G] = phi (i[H, G]) phi - (Lam H phi + phi H Lam); d<G>/dt = sum (d xi) K[phi psi] - sum xi fP.
T2 (the species): f_j[V_n psi] = s_n D_j f_j[psi], fP_j[V_n psi] = s_n fP_j[psi], e[V_n psi] = s_n e[psi], for every state and rate field.
T3 (what the ledger's requirement becomes): at leading order f_j = D_j e d_j u for species n under reach two and fP_j = e d_j u for every species
   under reach three: the requirement "stress gradient = weight" is met by all eight species under reach three, and under reach two it fails with the
   opposite sign for a species reflected along a direction in which the rates vary.
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
    "docs/ADMISSIBILITY_RULE_WHICH_SPECIES_FALL_THE_LEDGER_OWES_UNDER_REACH_TWO_A_REFLECTED_SPECIES_HAS_MINUS_ITS_WEIGHT_UNDER_REACH_THREE_ALL_EIGHT_AGREE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_which_species_fall_the_ledger_owes_under_reach_two_a_reflected_species_has_minus_its_weight_under_reach_three_all_eight_agree_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "rate_commutes_with_the_two_step_momentum": "B",
    "two_step_force_density_ignores_the_gradient": "B",
    "reach_two_force_is_the_same_for_all_species": "C",
    "reach_three_force_flips_for_reflected_species": "C",
    "staggered_amplitude_meets_the_requirement_under_reach_two": "D",
    "two_step_weight_is_half": "D",
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


def relabelling(tor: Torus, psi, xi):
    """G_xi psi = (1/2) sum_j {xi_j, S_j} psi."""
    out = {x: (G(0), G(0)) for x in tor.sites}
    for j in range(3):
        out = tor.add(out, tor.add(tor.times(xi[j], tor.s_op(psi, j)), tor.s_op(tor.times(xi[j], psi), j)), F(1, 2))
    return out


def rate_root(tor: Torus, seed):
    """A positive rational field phi = sqrt(w) on the sites."""
    return {x: ONE + F((seed * 5 + 3 * x[0] + x[1] * x[1] + 2 * x[2] * x[0] + x[1] * x[2]) % 11 - 5, 20) for x in tor.sites}


def bond_diff(tor: Torus, field, j):
    return {x: field[tor.sh(x, j, 1)] - field[x] for x in tor.sites}


def clocked(tor: Torus, psi, phi):
    """H_w psi = phi H (phi psi)."""
    return tor.times(phi, tor.ham(tor.times(phi, psi)))


def lam_op(tor: Torus, psi, xi, phi):
    """Lam psi = (1/2) sum_j {xi_j, C_j[d_j phi]} psi."""
    out = {x: (G(0), G(0)) for x in tor.sites}
    for j in range(3):
        w = bond_diff(tor, phi, j)
        out = tor.add(out, tor.add(tor.times(xi[j], sym_hop(tor, psi, j, w)), sym_hop(tor, tor.times(xi[j], psi), j, w)), F(1, 2))
    return out


def force_density(tor: Torus, psi, phi, j):
    """f_j(x) = Re[(C_j[d_j phi] psi)^dagger g + psi^dagger C_j[d_j phi] g](x), g = H (phi psi)."""
    g = tor.ham(tor.times(phi, psi))
    w = bond_diff(tor, phi, j)
    first = tor.redot(sym_hop(tor, psi, j, w), g)
    second = tor.redot(psi, sym_hop(tor, g, j, w))
    return {x: first[x] + second[x] for x in tor.sites}


QUARTER_OVER_I = G(0, F(-1, 4))                                 # 1/(4i)


def p_op(tor: Torus, f, j):
    """(P_j f)(x) = (f(x + 2 e_j) - f(x - 2 e_j))/(4i)."""
    return {x: tuple((f[tor.sh(x, j, 2)][c] - f[tor.sh(x, j, -2)][c]) * QUARTER_OVER_I for c in range(2)) for x in tor.sites}


def relabel_p(tor: Torus, psi, xi):
    out = {x: (G(0), G(0)) for x in tor.sites}
    for j in range(3):
        out = tor.add(out, tor.add(tor.times(xi[j], p_op(tor, psi, j)), p_op(tor, tor.times(xi[j], psi), j)), F(1, 2))
    return out


def two_step_diff(tor: Torus, field, j):
    return {x: field[tor.sh(x, j, 2)] - field[x] for x in tor.sites}


def two_step_hop(tor: Torus, f, j, w):
    """(1/2) C2_j[w] f = (1/4)[w(x) f(x + 2 e_j) + w(x - 2 e_j) f(x - 2 e_j)], w a function of the two-step bond stored at its lower site."""
    return {x: tuple((f[tor.sh(x, j, 2)][c] * w[x] + f[tor.sh(x, j, -2)][c] * w[tor.sh(x, j, -2)]) * F(1, 4) for c in range(2)) for x in tor.sites}


def lam_p(tor: Torus, psi, xi, phi):
    """Lam psi = (1/2) sum_j {xi_j, (1/2) C2_j[d2_j phi]} psi."""
    out = {x: (G(0), G(0)) for x in tor.sites}
    for j in range(3):
        w = two_step_diff(tor, phi, j)
        out = tor.add(out, tor.add(tor.times(xi[j], two_step_hop(tor, psi, j, w)), two_step_hop(tor, tor.times(xi[j], psi), j, w)), F(1, 2))
    return out


def force_density_p(tor: Torus, psi, phi, j):
    """fP_j(x) = Re[((1/2) C2_j[d2_j phi] psi)^dagger g + psi^dagger (1/2) C2_j[d2_j phi] g](x), g = H (phi psi)."""
    g = tor.ham(tor.times(phi, psi))
    w = two_step_diff(tor, phi, j)
    first = tor.redot(two_step_hop(tor, psi, j, w), g)
    second = tor.redot(psi, two_step_hop(tor, g, j, w))
    return {x: first[x] + second[x] for x in tor.sites}


def current_p(tor: Torus, chi, a, j):
    pj = p_op(tor, chi, j)
    first = tor.redot(tor.up(chi, a), tor.sg(a, pj))
    second = tor.redot(tor.up(pj, a), tor.sg(a, chi))
    return {x: (first[x] + second[x]) / 2 for x in tor.sites}


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



# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = Torus((6, 5, 5))
    psi = tor.state(4)
    phi = rate_root(tor, 2)
    xi = [{x: F((11 * j + 3 * x[0] * x[0] + 5 * x[1] + x[2] * x[1] + j * x[0]) % 17 - 8, 3) for x in tor.sites} for j in range(3)]
    ok1 = True
    for j in range(3):
        lhs = tor.scale(tor.add(tor.times(phi, p_op(tor, psi, j)), p_op(tor, tor.times(phi, psi), j), -1), I_UNIT)
        rhs = tor.scale(two_step_hop(tor, psi, j, two_step_diff(tor, phi, j)), F(-1))
        if mut("rate_commutes_with_the_two_step_momentum"):
            rhs = {x: (G(0), G(0)) for x in tor.sites}
        ok1 = ok1 and all(lhs[x] == rhs[x] for x in tor.sites)
    checks.check("B1", ok1, "T1: i[phi, P_j] psi = -(1/2) C2_j[d2_j phi] psi exactly at all 150 sites of a 6x5x5 torus for a rational rate field and state: what the root of the rate leaves of the two-step momentum is a symmetric hop over TWO steps weighted by the change of phi over those two steps")

    hw = lambda f: clocked(tor, f, phi)
    commutator = tor.scale(tor.add(hw(relabel_p(tor, psi, xi)), relabel_p(tor, hw(psi), xi), -1), I_UNIT)
    chi = tor.times(phi, psi)
    bare = tor.scale(tor.add(tor.ham(relabel_p(tor, chi, xi)), relabel_p(tor, tor.ham(chi), xi), -1), I_UNIT)
    rhs = tor.times(phi, bare)
    rest = tor.add(lam_p(tor, tor.ham(chi), xi, phi), tor.times(phi, tor.ham(lam_p(tor, psi, xi, phi))))
    rhs = tor.add(rhs, rest, -1)
    operator_ok = all(commutator[x] == rhs[x] for x in tor.sites)
    expectation = sum(tor.redot(psi, commutator).values(), ZERO)
    current_term = ZERO
    for a in range(3):
        for j in range(3):
            cur = current_p(tor, chi, a, j)
            current_term += sum(((xi[j][tor.sh(x, a, 1)] - xi[j][x]) * cur[x] for x in tor.sites), ZERO)
    force_term = ZERO
    for j in range(3):
        fj = force_density_p(tor, psi, phi, j) if not mut("two_step_force_density_ignores_the_gradient") else {x: ZERO for x in tor.sites}
        force_term += sum((xi[j][x] * fj[x] for x in tor.sites), ZERO)
    uniform = [{x: (ONE if j == 0 else ZERO) for x in tor.sites} for j in range(3)]
    rate_of_momentum = sum(tor.redot(psi, tor.scale(tor.add(hw(relabel_p(tor, psi, uniform)), relabel_p(tor, hw(psi), uniform), -1), I_UNIT)).values(), ZERO)
    total_force = sum(force_density_p(tor, psi, phi, 0).values(), ZERO)
    checks.check("B2", operator_ok and expectation == current_term - force_term and rate_of_momentum == -total_force and total_force != 0, "T1: i[H_w, G] psi = phi (i[H, G]) phi psi - (Lam H phi + phi H Lam) psi exactly at all 150 sites for G = (1/2) sum {xi_j, P_j}, Lam = (1/2) sum_j {xi_j, (1/2) C2_j[d2_j phi]}; for every state d<G>/dt = sum over bonds (d_a xi_j) K_a^j[phi psi] - sum_x xi_j(x) fP_j(x), and for uniform xi the total two-step momentum changes at minus the total force (not zero): block 66 T3 with the two-step momentum, exactly")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    tor = Torus((6, 6, 6))
    psi = tor.state(5)
    phi = rate_root(tor, 3)
    energy = lambda f: tor.redot(f, clocked(tor, f, phi))
    e0 = energy(psi)
    f2 = [force_density(tor, psi, phi, j) for j in range(3)]
    f3 = [force_density_p(tor, psi, phi, j) for j in range(3)]
    two = True
    three = True
    energies = True
    for n in SPECIES:
        d, s, rho = species_data(n)
        vpsi = exchange(tor, n, psi)
        en = energy(vpsi)
        energies = energies and all(en[x] == s * e0[x] for x in tor.sites)
        for j in range(3):
            g2 = force_density(tor, vpsi, phi, j)
            g3 = force_density_p(tor, vpsi, phi, j)
            sign2 = s * d[j] if not mut("reach_two_force_is_the_same_for_all_species") else s
            sign3 = s if not mut("reach_three_force_flips_for_reflected_species") else s * d[j]
            two = two and all(g2[x] == sign2 * f2[j][x] for x in tor.sites)
            three = three and all(g3[x] == sign3 * f3[j][x] for x in tor.sites)
    alive = all(any(f2[j][x] != 0 for x in tor.sites) and any(f3[j][x] != 0 for x in tor.sites) for j in range(3))
    checks.check("C1", two and energies and alive, "T2: on a 6x6x6 torus with a varying rational rate field, for all eight species and j = 1, 2, 3, at all 216 sites: the reach-two force density of V_n psi is det(D_n) D_j times that of psi, while its energy density is det(D_n) times that of psi: per unit of energy density, the force density of a species reflected along j has the OPPOSITE sign")
    checks.check("C2", three and energies and alive, "T2: the two-step force density fP_j of V_n psi is det(D_n) times that of psi at all 216 sites, all eight species, j = 1, 2, 3: per unit of energy density it is the same for every species")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    x = sp.symbols("x", real=True)
    h = sp.symbols("h", positive=True)
    a, b = sp.Function("a", real=True)(x), sp.Function("b", real=True)(x)                             # a complex envelope a + i b with the coin along sigma_3 (upper component), on a line
    phi = sp.Function("phi", real=True)(x)

    def sh(f, s):
        """f(x + s h) through second order in the lattice spacing."""
        return f + s * h * sp.diff(f, x) + (s * h) ** 2 * sp.diff(f, x, 2) / 2

    def cut(expr):
        expr = sp.expand(expr)
        return sum(expr.coeff(h, k) * h ** k for k in range(3))

    conj = lambda f: f.subs(sp.I, -sp.I)
    real = lambda f: sp.expand((f + conj(f)) / 2)
    amp = a + sp.I * b
    results = {}
    for stagger in (1, -1):                                                                           # the amplitude is stagger^(x/h) times the smooth envelope: a shift by one step brings the factor stagger
        sgn = lambda s: stagger ** abs(s)
        shift_amp = lambda f, s: sgn(s) * sh(f, s)
        chi = phi * amp
        g = cut((shift_amp(chi, 1) - shift_amp(chi, -1)) / (2 * sp.I))                               # H (phi psi), upper component; g carries the same staggering as the amplitude
        w1_here, w1_back = cut(sh(phi, 1) - phi), cut(phi - sh(phi, -1))
        hop1 = lambda f: cut((w1_here * shift_amp(f, 1) + w1_back * shift_amp(f, -1)) / 2)
        w2_here, w2_back = cut(sh(phi, 2) - phi), cut(phi - sh(phi, -2))
        hop2 = lambda f: cut((w2_here * shift_amp(f, 2) + w2_back * shift_amp(f, -2)) / 4)
        force2 = real(cut(conj(hop1(amp)) * g + conj(amp) * hop1(g)))
        force3 = real(cut(conj(hop2(amp)) * g + conj(amp) * hop2(g)))
        energy = real(cut(conj(chi) * g))
        weight = cut(energy * (2 * sp.diff(phi, x) / phi) * h)
        results[stagger] = (force2, force3, weight)
    f2s, f3s, ws = results[1]
    f2r, f3r, wr = results[-1]
    half = sp.Rational(1) if not mut("two_step_weight_is_half") else sp.Rational(1, 2)
    smooth_ok = sp.simplify(f2s.coeff(h, 2) - ws.coeff(h, 2)) == 0 and sp.simplify(f3s.coeff(h, 2) - half * ws.coeff(h, 2)) == 0 and sp.simplify(ws.coeff(h, 2)) != 0
    target = -1 if not mut("staggered_amplitude_meets_the_requirement_under_reach_two") else 1
    reflected_ok = sp.simplify(f2r.coeff(h, 2) - target * wr.coeff(h, 2)) == 0 and sp.simplify(f3r.coeff(h, 2) - wr.coeff(h, 2)) == 0 and sp.simplify(wr.coeff(h, 2)) != 0
    lower = all(sp.simplify(q.coeff(h, k)) == 0 for q in (f2s, f3s, f2r, f3r) for k in (0, 1))
    checks.check("D1", smooth_ok and reflected_ok and lower, "T3: on a line with lattice spacing h, smooth phi, exact symbolic expansion at the leading order (h^2): for a SMOOTH amplitude f = e du (block 66 T4) and fP = e du; for a STAGGERED amplitude (a species reflected along the line) f = -e du while fP = +e du: the ledger's requirement 'stress gradient = weight' is met by every species under reach three, and under reach two it fails with the opposite sign for a species reflected along a direction in which the rates vary")
# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice timed by local clocks and for a field energy counted per local tick and blind to relabellings; it reports for which of the walk's species the requirement that such a ledger places on its content is met, under the relabellings of reach two and of reach three; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — i[phi, P_j] against the two-step weighted hop at all 150 sites of a 6x5x5 torus, j = 1, 2, 3",
    "per_site: executed — the operator identity for i[H_w, G] at all 150 sites; the force densities of both relabellings and the energy density of V_n psi against those of psi at all 216 sites of a 6x6x6 torus, all eight species",
    "per_mode: executed — the leading order of f, fP and e du for a smooth and for a staggered amplitude on a line (exact symbolic expansion)",
    "per_block: executed — d<G>/dt against the pairing with the two-step current minus the force term for a varying displacement; the total two-step momentum against the total force for a uniform one",
    "lattice_wide: T1 and T2 are identities for every state, rate field and displacement on every torus (even sides for T2, sides of at least five for the two-step momentum) and on the infinite lattice; T3 is the leading order for smooth envelopes and smooth rates, with block 66 T1 and T2 restated for the field's side; which coupling is supplied and which species are present are not decided",
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
    print("scope: which species' fall the ledger owes — the walk's exact law for the two-step relabelling in a rate field; per unit of energy density the reach-two force density of a species reflected along j has the opposite sign, the reach-three one is the same for all eight; at leading order the ledger's requirement (stress gradient = weight) is met by every species under reach three and fails with the opposite sign for reflected species under reach two")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
