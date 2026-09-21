#!/usr/bin/env python3
"""Exact checks: the fall is owed by the ledger (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 55, 60, 63, 64): block 54's walk timed by site rates, H_w = phi H phi with phi = sqrt(w), u = log w; block 55's energy
density e = Re psi^dagger H_w psi; block 60's ledger linear in the rates, F = sum_x w_x D_x; block 63's relabelling G_xi and bond current; block 64's
densities built from the curls of a frame e = 1 + strain.
T1 (the field's identity; continuum, exact symbolic algebra): for F = int exp(u) D(e) with D any member of block 64's family (each a scalar density under
   relabellings), E_j^a := dF/de^j_a and U := dF/du satisfy  E_j^a d_b e^j_a - d_a(E_j^a e^j_b) + U d_b u = 0  identically, checked through the order
   at which the fall first appears (second order in the fields, third order of the ledger).
T2 (the fall is owed): with the rates' constraint U = -e_content and the strains' equations E = -(the content's response), the content MUST satisfy
   d_a(J_j^a e^j_b) - J_j^a d_b e^j_a = e_content d_b u: at lowest order the divergence of its stress equals its energy density times the gradient of
   the log rate - its weight.  A body with no stress gradient cannot be static: its momentum changes at -energy x gradient (block 54).
T3 (the walk's own law, exact on the lattice): i[phi, S_j] = -C_j[d_j phi];  i[H_w, G_xi] = phi (i[H, G_xi]) phi - (Lam H phi + phi H Lam) with
   Lam = (1/2) sum_j {xi_j, C_j[d_j phi]};  hence d<G_xi>/dt = sum over bonds (d_a xi_j) J_a^j[phi psi] - sum_x xi_j(x) f_j(x) for EVERY state, with the
   force density f_j(x) = Re[(C_j[d_j phi] psi)^dagger (H phi psi) + psi^dagger C_j[d_j phi](H phi psi)](x).
T4 (they agree): to leading order in the lattice spacing f_j = e d_j u, the weight; so on stationary states the divergence of the walk's bond current
   equals minus its weight, which is what T2 asks.  The law of fall is not an extra clause next to such a ledger: it is the ledger's consistency condition.
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
    "docs/ADMISSIBILITY_RULE_THE_FALL_IS_OWED_BY_THE_LEDGER_A_FIELD_ENERGY_PER_LOCAL_TICK_REQUIRES_THE_CONTENTS_STRESS_GRADIENT_TO_EQUAL_ITS_WEIGHT_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "rate_commutes_with_the_momentum": "B",
    "clocked_walk_conserves_momentum": "B",
    "force_density_ignores_the_gradient": "B",
    "ledger_identity_without_the_rates": "C",
    "ledger_identity_needs_the_curvature_member": "C",
    "weight_is_half_the_energy_times_gradient": "D",
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


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = Torus((5, 4, 3))
    psi = tor.state(4)
    phi = rate_root(tor, 2)
    xi = [{x: F((11 * j + 3 * x[0] * x[0] + 5 * x[1] + x[2] * x[1] + j * x[0]) % 17 - 8, 3) for x in tor.sites} for j in range(3)]
    ok1 = True
    for j in range(3):
        lhs = tor.scale(tor.add(tor.times(phi, tor.s_op(psi, j)), tor.s_op(tor.times(phi, psi), j), -1), I_UNIT)
        rhs = tor.scale(sym_hop(tor, psi, j, bond_diff(tor, phi, j)), F(-1))
        if mut("rate_commutes_with_the_momentum"):
            rhs = {x: (G(0), G(0)) for x in tor.sites}
        ok1 = ok1 and all(lhs[x] == rhs[x] for x in tor.sites)
    checks.check("B1", ok1, "T3: i[phi, S_j] psi = -C_j[d_j phi] psi exactly at all 60 sites of a 5x4x3 torus for a rational rate field and state: the root of the rate does not commute with the lattice momentum; what is left is a symmetric hop weighted by the change of phi along the bond")

    hw = lambda f: clocked(tor, f, phi)
    commutator = tor.scale(tor.add(hw(relabelling(tor, psi, xi)), relabelling(tor, hw(psi), xi), -1), I_UNIT)
    chi = tor.times(phi, psi)
    bare = tor.scale(tor.add(tor.ham(relabelling(tor, chi, xi)), relabelling(tor, tor.ham(chi), xi), -1), I_UNIT)
    rhs = tor.times(phi, bare)
    if not mut("clocked_walk_conserves_momentum"):
        rest = tor.add(lam_op(tor, tor.ham(chi), xi, phi), tor.times(phi, tor.ham(lam_op(tor, psi, xi, phi))))
        rhs = tor.add(rhs, rest, -1)
    checks.check("B2", all(commutator[x] == rhs[x] for x in tor.sites), "T3: i[H_w, G_xi] psi = phi (i[H, G_xi]) phi psi - (Lam H phi + phi H Lam) psi exactly at all 60 sites, Lam = (1/2) sum_j {xi_j, C_j[d_j phi]}: a relabelling carries the rates along, and on the lattice what it makes of a rate is a weighted hop")

    expectation = sum(tor.redot(psi, commutator).values(), ZERO)
    current_term = ZERO
    for a in range(3):
        for j in range(3):
            cur = tor.current(chi, a, j)
            current_term += sum(((xi[j][tor.sh(x, a, 1)] - xi[j][x]) * cur[x] for x in tor.sites), ZERO)
    force_term = ZERO
    for j in range(3):
        fj = force_density(tor, psi, phi, j) if not mut("force_density_ignores_the_gradient") else {x: ZERO for x in tor.sites}
        force_term += sum((xi[j][x] * fj[x] for x in tor.sites), ZERO)
    uniform = [{x: (ONE if j == 1 else ZERO) for x in tor.sites} for j in range(3)]
    rate_of_momentum = sum(tor.redot(psi, tor.scale(tor.add(hw(relabelling(tor, psi, uniform)), relabelling(tor, hw(psi), uniform), -1), I_UNIT)).values(), ZERO)
    total_force = sum(force_density(tor, psi, phi, 1).values(), ZERO)
    checks.check("B3", expectation == current_term - force_term and rate_of_momentum == -total_force and total_force != 0, f"T3: for every state d<G_xi>/dt = sum over bonds (d_a xi_j) J_a^j[phi psi] - sum_x xi_j(x) f_j(x), with the force density f_j(x) = Re[(C_j[d_j phi] psi)^dagger H phi psi + psi^dagger C_j[d_j phi] H phi psi](x); for a uniform displacement the total lattice momentum changes at minus the total force ({about(-total_force)} here): in a rate field the walk's momentum is not conserved, it falls")


# ============================================================================================ symbolic machinery
XS = sp.symbols("x y z", real=True)
EPS_S = sp.symbols("epsilon", real=True)
CS = sp.symbols("c0 c1 c2 c3 c4")


def trunc3(expr, n=3):
    expr = sp.expand(expr)
    return sum(expr.coeff(EPS_S, k) * EPS_S ** k for k in range(n + 1))


def varder(lag, f):
    """Variational derivative of a density that holds f and its first and second derivatives."""
    out = sp.diff(lag, f)
    for i in range(3):
        out -= sp.diff(sp.diff(lag, sp.Derivative(f, XS[i])), XS[i])
        for k in range(i, 3):
            d2 = sp.Derivative(f, XS[i], XS[k]) if i != k else sp.Derivative(f, (XS[i], 2))
            out += sp.diff(sp.diff(lag, d2), XS[i], XS[k])
    return out


def family_density(strain):
    """The pieces of block 64's family for the co-frame e = 1 + eps strain, through third order in eps."""
    eye = sp.eye(3)
    small = EPS_S * strain
    e = eye + small
    einv = (eye - small + small * small - small * small * small).applyfunc(trunc3)
    t1, t2, t3_ = small.trace(), (small * small).trace(), (small * small * small).trace()
    dete = trunc3(1 + t1 + (t1 ** 2 - t2) / 2 + (t1 ** 3 - 3 * t1 * t2 + 2 * t3_) / 6)
    tor_ = [[[sp.diff(e[j, b], XS[a]) - sp.diff(e[j, a], XS[b]) for b in range(3)] for a in range(3)] for j in range(3)]
    tc = [[[trunc3(sum(einv[a, k] * einv[b, l] * tor_[j][a][b] for a in range(3) for b in range(3))) for l in range(3)] for k in range(3)] for j in range(3)]
    q1 = trunc3(sum(tc[j][k][l] ** 2 for j in range(3) for k in range(3) for l in range(3)))
    q2 = trunc3(sum(tc[j][k][l] * tc[l][k][j] for j in range(3) for k in range(3) for l in range(3)))
    vec = [trunc3(sum(tc[k][k][l] for k in range(3))) for l in range(3)]
    q3 = trunc3(sum(v ** 2 for v in vec))
    vup = [trunc3(sum(einv[b, l] * vec[l] for l in range(3))) for b in range(3)]
    div = trunc3(sum(sp.diff(trunc3(dete * vup[b]), XS[b]) for b in range(3)))
    return e, dete, q1, q2, q3, div


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    c0, c1, c2, c3, c4 = CS
    strain = sp.Matrix(3, 3, lambda j, a: sp.Function(f"B{j}{a}")(*XS))
    u = sp.Function("u")(*XS)
    e, dete, q1, q2, q3, div = family_density(strain)
    expu = 1 + EPS_S * u + EPS_S ** 2 * u ** 2 / 2 + EPS_S ** 3 * u ** 3 / 6
    members = {
        "the blind member": dete * (q1 / 4 + q2 / 2 - q3) - 2 * div,
        "a member that sees the coin axes, with the volume": sp.Rational(1, 3) * dete + dete * (2 * q1 - q2 / 5 + 3 * q3) + sp.Rational(7, 2) * div,
    }
    results = []
    for name, dens in members.items():
        lag = trunc3(expu * trunc3(dens))
        e_field = sp.Matrix(3, 3, lambda j, a: trunc3(varder(lag, strain[j, a]) / EPS_S, 2))
        u_field = trunc3(varder(lag, u) / EPS_S, 2)
        if mut("ledger_identity_without_the_rates"):
            u_field = sp.Integer(0)
        ok = True
        for b in range(3):
            ident = sum(e_field[j, a] * sp.diff(e[j, a], XS[b]) for j in range(3) for a in range(3)) - sum(sp.diff(e_field[j, a] * e[j, b], XS[a]) for j in range(3) for a in range(3)) + u_field * EPS_S * sp.diff(u, XS[b])
            ok = ok and trunc3(ident, 2) == 0
        results.append(ok)
    both = all(results) if not mut("ledger_identity_needs_the_curvature_member") else (results[0] and not results[1])
    checks.check("C1", both, "T1: for F = int exp(u) D(e), with E_j^a = dF/de^j_a and U = dF/du, the identity E_j^a d_b e^j_a - d_a(E_j^a e^j_b) + U d_b u = 0 holds through second order in nine strain functions and the log rate, for the blind member AND for a member that sees the coin axes and has a volume term (exact symbolic algebra): it is the counting per local tick together with the blindness to relabellings that gives it, not the choice of member")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    x = sp.symbols("x", real=True)
    h = sp.symbols("h", positive=True)
    a, b = sp.Function("a", real=True)(x), sp.Function("b", real=True)(x)                             # a complex amplitude a + i b with the coin along sigma_3 (upper component), on a line
    phi = sp.Function("phi", real=True)(x)

    def sh(f, s):
        """f(x + s h) through second order in the lattice spacing."""
        return f + s * h * sp.diff(f, x) + (s * h) ** 2 * sp.diff(f, x, 2) / 2

    def cut(expr):
        expr = sp.expand(expr)
        return sum(expr.coeff(h, k) * h ** k for k in range(3))

    amp = a + sp.I * b
    chi = phi * amp
    g = cut((sh(chi, 1) - sh(chi, -1)) / (2 * sp.I))                                                  # H (phi psi) for the upper component: sigma_3 = +1
    w_here, w_back = cut(sh(phi, 1) - phi), cut(phi - sh(phi, -1))
    hop = lambda f: cut((w_here * sh(f, 1) + w_back * sh(f, -1)) / 2)
    conj = lambda f: f.subs(sp.I, -sp.I)
    force = cut(conj(hop(amp)) * g + conj(amp) * hop(g))
    force = sp.expand((force + conj(force)) / 2)
    energy = cut(conj(chi) * g)
    energy = sp.expand((energy + conj(energy)) / 2)
    weight = cut(energy * (2 * sp.diff(phi, x) / phi) * h)                                            # e du, u = 2 log phi, across one lattice spacing
    factor = sp.Rational(1) if not mut("weight_is_half_the_energy_times_gradient") else sp.Rational(1, 2)
    lead_force, lead_weight = force.coeff(h, 2), weight.coeff(h, 2)
    same = sp.simplify(lead_force - factor * lead_weight) == 0
    lower = sp.simplify(force.coeff(h, 0)) == 0 and sp.simplify(force.coeff(h, 1)) == 0
    checks.check("D1", same and lower and sp.simplify(lead_force) != 0, "T4: on a line with lattice spacing h, for smooth phi and a smooth complex amplitude, the force density and the weight e du agree at the leading order in h (exact symbolic expansion): f_j = e d_j u; the walk's momentum balance has exactly the form the ledger's identity requires, so on stationary states the divergence of its bond current is minus its weight")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for amplitudes timed by them and for a ledger linear in the rates built from the strains of a frame; it reports an identity of such a ledger and the exact momentum balance of the clocked walk, and that the two agree; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — i[phi, S_j] at all 60 sites of a 5x4x3 torus for a rational rate field and state",
    "per_site: executed — i[H_w, G_xi] against phi (i[H, G_xi]) phi - (Lam H phi + phi H Lam) at all 60 sites; the force density site by site",
    "per_mode: executed — the ledger's identity through second order in nine strain functions and the log rate, for two members of block 64's family (exact symbolic algebra)",
    "per_block: executed — d<G_xi>/dt against the current term minus the force term for a rational displacement field; the rate of change of the total lattice momentum against minus the total force; the force density against the weight at leading order in the lattice spacing",
    "lattice_wide: T1 is a continuum identity for every frame and rate field, checked through the order at which the fall first appears; T2 follows from T1 for every content coupled through a ledger of this kind; T3 holds for every state, rate field and displacement on every torus and on the infinite lattice; T4 at leading order in the lattice spacing; the ledger's form, the strains, the relabellings and the clocked walk are supplied; an exact lattice form of T1 is not given",
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
    print("scope: the fall is owed by the ledger — a field energy counted per local tick and blind to relabellings obeys an identity that ties the divergence of the strains' field equations to the rates' equation times the gradient of the log rate; with the rates' constraint it requires the content's stress gradient to equal its weight; the clocked walk's exact momentum balance has that form, with a force density that is the weight at leading order")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
