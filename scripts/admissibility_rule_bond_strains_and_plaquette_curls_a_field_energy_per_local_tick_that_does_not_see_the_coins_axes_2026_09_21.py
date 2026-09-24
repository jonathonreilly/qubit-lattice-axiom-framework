#!/usr/bin/env python3
"""Exact lattice curl/current controls and a supplied continuum density ansatz.
Divergence compatibility is necessary, not static existence. Continuum invariance
is tested only to the displayed perturbative orders. The exact additive-strain
torque condition is a separate hypothetical lattice property.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path

import sympy as sp
from sympy.calculus.euler import euler_equations


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "curl_sees_a_relabelling": "B",
    "strain_response_is_the_site_response": "B",
    "field_equations_have_a_divergence": "B",
    "blindness_leaves_the_ratios_free": "C",
    "parity_odd_term_is_blind": "C",
    "blind_density_is_not_the_curvature": "D",
    "antisymmetric_strain_is_seen": "D",
    "exponent_is_one_without_blindness": "E",
    "stationary_states_have_no_torque": "E",
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


def strained(tor: Torus, psi, strain):
    """H[B] psi = H psi + sum_aj sigma_a (1/2){C_a[B_a^j], S_j} psi; strain[(a, j)] is a function of the bond (stored at its lower site)."""
    out = tor.ham(psi)
    for (a, j), w in strain.items():
        term = tor.add(sym_hop(tor, tor.s_op(psi, j), a, w), tor.s_op(sym_hop(tor, psi, a, w), j))
        out = tor.add(out, tor.sg(a, tor.scale(term, F(1, 2))))
    return out


def curls(tor: Torus, strain):
    """F_ab^j(x) = d_a B_b^j - d_b B_a^j on the plaquette at x spanned by a < b."""
    out = {}
    for j in range(3):
        for a in range(3):
            for b in range(a + 1, 3):
                out[(a, b, j)] = {x: (strain[(b, j)][tor.sh(x, a, 1)] - strain[(b, j)][x]) - (strain[(a, j)][tor.sh(x, b, 1)] - strain[(a, j)][x]) for x in tor.sites}
    return out


def rational_strain(tor: Torus, seed):
    return {(a, j): {x: F((seed * 5 + 3 * a + 7 * j + 2 * x[0] + x[1] * (a + 2) + x[2] * x[2] * (j + 1)) % 13 - 6, 9) for x in tor.sites} for a in range(3) for j in range(3)}


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = Torus((5, 4, 3))
    strain = rational_strain(tor, 3)
    xi = [{x: F((11 * j + 3 * x[0] * x[0] + 5 * x[1] + x[2] * x[1] + j * x[0]) % 17 - 8, 3) for x in tor.sites} for j in range(3)]
    shifted = {(a, j): {x: strain[(a, j)][x] + xi[j][tor.sh(x, a, 1)] - xi[j][x] for x in tor.sites} for a in range(3) for j in range(3)}
    if mut("curl_sees_a_relabelling"):
        shifted[(0, 1)] = {x: shifted[(0, 1)][x] + (ONE if x == (1, 1, 1) else ZERO) for x in tor.sites}
    c_old, c_new = curls(tor, strain), curls(tor, shifted)
    alive = any(v != 0 for key in c_old for v in c_old[key].values())
    checks.check("B1", alive and all(c_old[key][x] == c_new[key][x] for key in c_old for x in tor.sites), "T1: on a 5x4x3 torus the nine curls F_ab^j = d_a B_b^j - d_b B_a^j of a rational strain are unchanged, plaquette by plaquette, when the strain is shifted by the differences d_a xi_j of a rational displacement of the sites")

    big = Torus((5, 5, 5))
    psi, phi = big.state(6), big.state(9)
    strain5 = rational_strain(big, 4)
    herm = inner_on(big, phi, strained(big, psi, strain5)) == inner_on(big, strained(big, phi, strain5), psi)
    site, a0, j0 = (2, 1, 3), 1, 2
    bumped = {key: dict(val) for key, val in strain5.items()}
    bumped[(a0, j0)][site] += 1
    slope = inner_on(big, psi, strained(big, psi, bumped)).re - inner_on(big, psi, strained(big, psi, strain5)).re
    response = big.current(psi, a0, j0)[site] if not mut("strain_response_is_the_site_response") else big.theta(psi, a0, j0)[site]
    checks.check("B2", herm and slope == response, "T1: on a 5x5x5 torus H[B] = H + sum sigma_a (1/2){C_a[B_a^j], S_j} is hermitian for a rational strain field, and the derivative of <H[B]> in one bond's strain, by an exact difference, is block 63's bond current J_a^j on that bond: the strain is sourced by what the walk conserves")

    weights = {key: {x: F((3 + 2 * key[0] + 5 * key[1] + 7 * key[2] + x[0] + 2 * x[1] * x[2]) % 7 + 1, 4) for x in tor.sites} for key in c_old}
    grad = {(a, j): {x: ZERO for x in tor.sites} for a in range(3) for j in range(3)}                  # dQ/dB for Q = (1/2) sum weights F^2
    for (a, b, j), field in c_old.items():
        for x in tor.sites:
            g = weights[(a, b, j)][x] * field[x]
            grad[(b, j)][tor.sh(x, a, 1)] += g
            grad[(b, j)][x] -= g
            grad[(a, j)][tor.sh(x, b, 1)] -= g
            grad[(a, j)][x] += g
    if mut("field_equations_have_a_divergence"):
        grad[(0, 0)][(1, 1, 1)] += 1
    div_ok = all(sum((grad[(a, j)][x] - grad[(a, j)][tor.sh(x, a, -1)] for a in range(3)), ZERO) == 0 for j in range(3) for x in tor.sites)
    live = any(v != 0 for key in grad for v in grad[key].values())
    checks.check("B3", div_ok and live, "T1: for a field energy (1/2) sum (weight)(F_ab^j)^2 with a different rational weight on every plaquette and index, the divergence over a of dF/dB_a^j vanishes at every site for each j: the field equations of any function of the curls are divergence-free identically, as block 63's current is for stationary states; a necessary divergence condition holds at first order, not a general existence theorem")


def inner_on(tor: Torus, phi, psi):
    tot = G(0)
    for x in tor.sites:
        for c in range(2):
            tot = tot + phi[x][c].conj() * psi[x][c]
    return tot


# ============================================================================================ symbolic machinery for families C, D, E
XS = sp.symbols("x y z", real=True)
EPS_S, ETA_S = sp.symbols("epsilon eta", real=True)
CS = sp.symbols("c0 c1 c2 c3 c4 c5")


def make_trunc(neta, neps):
    def trunc(expr):
        expr = sp.expand(expr)
        out = 0
        for i in range(neta + 1):
            ci = expr.coeff(ETA_S, i)
            for k in range(neps + 1):
                out += ci.coeff(EPS_S, k) * ETA_S ** i * EPS_S ** k
        return out
    return trunc


def frame_pieces(small, trunc):
    """For the frame e = 1 + small: det e, T1, T2, T3, d_b(det e V^b) and the parity-odd eps.T, truncated; indices moved with the frame's inverse."""
    eye = sp.eye(3)
    e = eye + small
    einv = (eye - small + small * small).applyfunc(trunc)
    tr1, tr2 = small.trace(), (small * small).trace()
    dete = trunc(1 + tr1 + (tr1 ** 2 - tr2) / 2)
    tor_ = [[[sp.diff(e[j, b], XS[a]) - sp.diff(e[j, a], XS[b]) for b in range(3)] for a in range(3)] for j in range(3)]
    tc = [[[trunc(sum(einv[a, k] * einv[b, l] * tor_[j][a][b] for a in range(3) for b in range(3))) for l in range(3)] for k in range(3)] for j in range(3)]
    t1 = trunc(sum(tc[j][k][l] ** 2 for j in range(3) for k in range(3) for l in range(3)))
    t2 = trunc(sum(tc[j][k][l] * tc[l][k][j] for j in range(3) for k in range(3) for l in range(3)))
    vec = [trunc(sum(tc[k][k][l] for k in range(3))) for l in range(3)]
    t3 = trunc(sum(v ** 2 for v in vec))
    vup = [trunc(sum(einv[b, l] * vec[l] for l in range(3))) for b in range(3)]
    div = trunc(sum(sp.diff(trunc(dete * vup[b]), XS[b]) for b in range(3)))
    odd = trunc(sum(sp.LeviCivita(j, k, l) * tc[j][k][l] for j in range(3) for k in range(3) for l in range(3)))
    return dete, t1, t2, t3, div, odd


def general_strain():
    return sp.Matrix(3, 3, lambda j, a: sp.Function(f"B{j}{a}")(*XS))


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    c0, c1, c2, c3, c4, c5 = CS
    om = [sp.Function(f"om{i}")(*XS) for i in range(3)]
    gen = sp.Matrix([[0, -om[2], om[1]], [om[2], 0, -om[0]], [-om[1], om[0], 0]])
    strain = general_strain()
    trunc = make_trunc(1, 1)
    small = ETA_S * gen + EPS_S * strain + ETA_S * EPS_S * gen * strain                                # (1 + eta Om)(1 + eps B) - 1
    dete, t1, t2, t3, div, odd = frame_pieces(small, trunc)
    dens = trunc(c0 * dete + c5 * dete * odd + dete * (c1 * t1 + c2 * t2 + c3 * t3) + c4 * div)
    conditions = set()
    for order in (0, 1):
        part = sp.expand(dens.coeff(ETA_S, 1).coeff(EPS_S, order))
        if part != 0:
            atoms = sorted(part.atoms(sp.Derivative) | part.atoms(sp.core.function.AppliedUndef), key=str)
            conditions |= set(sp.Poly(part, *atoms).coeffs())
    sol = sp.solve(list(conditions), [c1, c2, c3, c5], dict=True)
    expected = {c1: -c4 / 8, c2: -c4 / 4, c3: c4 / 2, c5: 0}
    unique = (len(sol) == 1 and all(sp.simplify(sol[0][k] - v) == 0 for k, v in expected.items())) if not mut("blindness_leaves_the_ratios_free") else (len(sol) != 1)
    free_volume = all(not cond.has(c0) for cond in conditions)
    odd_killed = any(sp.simplify(cond - 4 * c5) == 0 or sp.simplify(cond + 4 * c5) == 0 for cond in conditions) if not mut("parity_odd_term_is_blind") else all(not cond.has(c5) for cond in conditions)
    checks.check("C1", unique and free_volume and odd_killed, "T2: rotate the coin axes by an angle that varies from place to place; to first order in the rotation and in a general strain, the density c0 det e + c5 det e (eps.T) + det e [c1 T1 + c2 T2 + c3 T3] + c4 div(det e V) is unchanged point by point iff c5 = 0 and (c1, c2, c3) = (-c4/8, -c4/4, c4/2); c0 is free (exact symbolic algebra, three rotation functions and nine strain functions)")

    # the weaker demand: unchanged up to a divergence (appropriate to a field energy that is NOT multiplied by the rates)
    part = sp.expand(dens.coeff(ETA_S, 1).coeff(EPS_S, 1))
    fields = [strain[j, a] for j in range(3) for a in range(3)] + om
    weak = set()
    for eq in euler_equations(part, fields, list(XS)):
        lhs = sp.expand(eq.lhs)
        if lhs != 0:
            atoms = sorted(lhs.atoms(sp.Derivative) | lhs.atoms(sp.core.function.AppliedUndef), key=str)
            weak |= set(sp.Poly(lhs, *atoms).coeffs())
    weak_sol = sp.solve(list(weak), [c1, c2, c5], dict=True)
    weak_ok = len(weak_sol) == 1 and sp.simplify(weak_sol[0][c1] + c3 / 4) == 0 and sp.simplify(weak_sol[0][c2] + c3 / 2) == 0 and weak_sol[0][c5] == 0 and all(not w.has(c4) for w in weak)
    checks.check("C2", weak_ok, "T2: the weaker demand, unchanged UP TO A DIVERGENCE (all variational derivatives of the first-order change vanish), fixes c5 = 0 and c1 : c2 : c3 = 1 : 2 : -4 and leaves c4 free: without the point-by-point demand the strength with which the rates couple to the lengths, and with it beta, stays free; pointwise invariance follows if local invariance is separately required for arbitrary rate multipliers")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    strain = general_strain()
    trunc = make_trunc(0, 2)
    small = EPS_S * strain
    dete, t1, t2, t3, div, _ = frame_pieces(small, trunc)
    star = trunc(dete * (t1 / 4 + t2 / 2 - t3) - 2 * div)
    eye = sp.eye(3)
    e = eye + small
    h = (e.T * e - eye).applyfunc(sp.expand)
    ginv = (eye - h + h * h).applyfunc(trunc)
    gfull = eye + h
    gam = [[[trunc(sum(ginv[i, l] * (sp.diff(gfull[l, k], XS[j]) + sp.diff(gfull[l, j], XS[k]) - sp.diff(gfull[j, k], XS[l])) for l in range(3)) / 2) for k in range(3)] for j in range(3)] for i in range(3)]
    ric = sp.zeros(3, 3)
    for j in range(3):
        for k in range(3):
            ric[j, k] = trunc(sum(sp.diff(gam[i][j][k], XS[i]) - sp.diff(gam[i][j][i], XS[k]) + sum(gam[i][i][l] * gam[l][j][k] - gam[i][k][l] * gam[l][j][i] for l in range(3)) for i in range(3)))
    scalar = trunc(sum(ginv[j, k] * ric[j, k] for j in range(3) for k in range(3)))
    sign = 1 if not mut("blind_density_is_not_the_curvature") else -1
    same = sp.expand(star + sign * trunc(dete * scalar)) == 0
    checks.check("D1", same, "T3: D* = det e [T1/4 + T2/2 - T3] - 2 div(det e V) equals MINUS (volume density) x (scalar curvature) of the metric g = e^T e, point by point, through second order in a general strain of nine functions (exact symbolic algebra): with c4 = -2K the blind density is block 60's member, -K x volume x curvature")

    second = sp.expand(star.coeff(EPS_S, 2))
    sym = sp.Matrix(3, 3, lambda j, a: sp.Function(f"S{min(j, a)}{max(j, a)}")(*XS))
    ant_f = [sp.Function(f"A{i}")(*XS) for i in range(3)]
    ant = sp.Matrix([[0, -ant_f[2], ant_f[1]], [ant_f[2], 0, -ant_f[0]], [-ant_f[1], ant_f[0], 0]])
    sub = {strain[j, a]: sym[j, a] + ant[j, a] for j in range(3) for a in range(3)}
    second_split = sp.expand(second.subs(sub).doit())
    el = [sp.expand(eq.lhs) for eq in euler_equations(second_split, ant_f, list(XS))]
    unseen = all(v == 0 for v in el) if not mut("antisymmetric_strain_is_seen") else any(v != 0 for v in el)
    checks.check("D2", unseen, "T3: split the strain into its symmetric and antisymmetric parts; the second-order part of D* has NO variational derivative with respect to the three antisymmetric functions: at second order the blind member does not see them (they enter through a total derivative only)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    c0, c1, c2, c3, c4, c5 = CS
    lam = sp.Function("lam")(*XS)
    trunc = make_trunc(0, 2)
    dete, t1, t2, t3, div, _ = frame_pieces(EPS_S * lam * sp.eye(3), trunc)
    dens = trunc(dete * (c1 * t1 + c2 * t2 + c3 * t3) + c4 * div)
    lap = sum(sp.diff(lam, v, 2) for v in XS)
    grad2 = sum(sp.diff(lam, v) ** 2 for v in XS)
    first_ok = sp.expand(dens.coeff(EPS_S, 1) + 2 * c4 * lap) == 0
    second_ok = sp.expand(dens.coeff(EPS_S, 2) - (4 * c1 + 2 * c2 + 4 * c3) * grad2) == 0
    beta = c4 / (4 * c1 + 2 * c2 + 4 * c3)                                                            # from a = -2 c4, ap - b = -(4c1 + 2c2 + 4c3) in block 60's form
    blind = {c1: -c4 / 8, c2: -c4 / 4, c3: c4 / 2}
    maxwell = {c2: 0, c3: 0}
    beta_blind = sp.simplify(beta.subs(blind))
    beta_maxwell = sp.simplify(beta.subs(maxwell))
    one = (beta_blind == 1 and beta_maxwell == c4 / (4 * c1)) if not mut("exponent_is_one_without_blindness") else (beta_maxwell == 1)
    block60 = sp.simplify((-2 * c4).subs(c4, -2 * sp.Symbol("K")) - 4 * sp.Symbol("K")) == 0
    checks.check("E1", first_ok and second_ok and one and block60, "T4: on the tested frame (1+epsilon*lam) times identity, the family has first order -2 c4 Lap lam and second order (4c1 + 2c2 + 4c3)|grad lam|^2: in block 60's form a = -2 c4, ap - b = -(4c1 + 2c2 + 4c3), so beta = c4/(4c1 + 2c2 + 4c3); for the member with c1 alone beta = c4/(4 c1), a free number; for the blind member beta = 1, and c4 = -2K gives block 60's a = 4K")

    strain = general_strain()
    dete, t1, t2, t3, div, _ = frame_pieces(EPS_S * strain, trunc)
    second = sp.expand(trunc(dete * t1).coeff(EPS_S, 2))
    ant_f = [sp.Function(f"A{i}")(*XS) for i in range(3)]
    ant = sp.Matrix([[0, -ant_f[2], ant_f[1]], [ant_f[2], 0, -ant_f[0]], [-ant_f[1], ant_f[0], 0]])
    sub = {strain[j, a]: ant[j, a] for j in range(3) for a in range(3)}
    el = [sp.expand(eq.lhs) for eq in euler_equations(sp.expand(second.subs(sub).doit()), ant_f, list(XS))]
    checks.check("E2", any(v != 0 for v in el), "T4: for the member with c1 alone (one field of curls for each coin axis) the antisymmetric strain has a non-zero variational derivative at second order: a member that sees the coin axes has three more fields, which the walker in a uniform frame does not see (block 62 T1)")

    small = Torus((4, 4, 4))
    st = stationary_state(small)
    hst = small.ham(st)
    eigen = all(hst[x] == st[x] for x in small.sites)
    counts = []
    sums_zero = True
    response_ok = True
    for a in range(3):
        for j in range(a + 1, 3):
            ja, jj = small.current(st, a, j), small.current(st, j, a)
            tau = {x: ja[x] - jj[x] for x in small.sites}
            counts.append(sum(1 for v in tau.values() if v != 0))
            sums_zero = sums_zero and sum(tau.values(), ZERO) == 0
    site = (1, 2, 3)
    turn = {(a, j): {x: ZERO for x in small.sites} for a in range(3) for j in range(3)}
    turn[(0, 1)][site] = ONE                                                                            # a rotation of the site's forward bonds about axis 3: dB_0^1 = +1, dB_1^0 = -1
    turn[(1, 0)][site] = -ONE
    slope = inner_on(small, st, strained(small, st, turn)).re - inner_on(small, st, small.ham(st)).re
    response_ok = slope == small.current(st, 0, 1)[site] - small.current(st, 1, 0)[site]
    torque = all(c == 64 for c in counts) if not mut("stationary_states_have_no_torque") else all(c == 0 for c in counts)
    checks.check("E3", eigen and torque and sums_zero and response_ok, "T5: on the exactly stationary state of the 4x4x4 torus (H psi = psi) the response to a rotation of one site's three forward bonds is J_a^j(x) - J_j^a(x) (by an exact difference), and it is non-zero at all 64 sites for each of the three rotation axes, summing to zero over the torus: a field energy that does not see the coin's axes gives that rotation no field equation, so that specific fixed source violates the necessary condition if exact additive antisymmetric lattice independence is supplied")

    sx,sy,cx,cy=F(3,5),F(4,5),F(4,5),F(3,5)
    torque_uniform=sx*sy*(cx-cy)
    checks.check("E4",sx*sx+sy*sy==1 and torque_uniform==F(12,125),"T5 boundary: a positive-energy unit plane wave has uniform bond torque 12/125; additive antisymmetric bond strain is not a global coin-rotation symmetry")
    # Exponential and linear frame paths differ at second order by a divergence.
    small_exp=(EPS_S*lam+EPS_S**2*lam**2/2)*sp.eye(3)
    de,a1,a2,a3,dv,_=frame_pieces(small_exp,trunc)
    expdens=trunc(de*(c1*a1+c2*a2+c3*a3)+c4*dv)
    remainder=sp.expand(expdens.coeff(EPS_S,2)-(4*c1+2*c2+4*c3)*grad2)
    exp_ok=all(sp.simplify(eq.lhs)==0 for eq in euler_equations(remainder,[lam],list(XS)))
    checks.check("E5",exp_ok,"T4: exponential isotropic frame has the same integrated quadratic gradient coefficient up to a total derivative; pointwise density equality is not asserted for the two frame paths")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes with the qubit as their coin and for a ledger linear in the rates, widened by a strain on every bond; it reports what the lattice keeps exactly and which field energies do not see the orientation of the coin's axes; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — the nine curls of a rational strain on a 5x4x3 torus under a rational relabelling, plaquette by plaquette; hermiticity of H[B] and the derivative of <H[B]> in one bond's strain on a 5x5x5 torus",
    "per_site: executed — the divergence of the field equations of a weighted sum of squared curls at every site of a 5x4x3 torus for each coin axis",
    "per_mode: executed — the change of the six-number family of densities under a rotation of the coin axes that varies from place to place, to first order in three rotation functions and nine strain functions: all coefficient conditions and their solution",
    "per_block: executed — the blind density against the curvature density of e^T e through second order for nine strain functions; the variational derivatives with respect to the antisymmetric strain for the blind member and for the member with c1 alone; the exponent beta on the isotropic frame; the torque J_a^j(x) - J_j^a(x) of an exactly stationary state at all 64 sites of a 4x4x4 torus",
    "lattice_wide: T1 holds for every strain, relabelling, state and function of the curls on every torus and on the infinite lattice, the consistency of the static equations at first order in the strain and for uniform rates; T2 and T3 are continuum identities for every smooth frame, to the orders stated; T4 for the whole family; T5(a), (b) for every state and every field energy that does not depend on the rotation of the three forward bonds of a site, T5(c) for the stated stationary state; on the lattice the contractions that mix the coin index with the bond index have no unique placement, so T2 to T4 are statements at leading order in the wave vector; that bonds carry strains, the second-neighbour coupling, the blindness, K, c0 = 0 and the kinetic terms are not derived",
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
    print("scope: exact lattice curl and current identities; necessary source compatibility; coefficient selection within a supplied perturbative continuum ansatz; conditional nonzero beta=1; separate hypothetical lattice torque obstruction, not a complete invariant discretization")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
