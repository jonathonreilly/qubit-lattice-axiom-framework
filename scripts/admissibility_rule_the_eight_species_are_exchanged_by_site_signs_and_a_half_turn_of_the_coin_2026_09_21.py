#!/usr/bin/env python3
"""Exact checks: the species-exchange maps (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 62, 63, 64, 65, 68, 69): block 54's walk H = sum_a sigma_a S_a and its eight species n in {0,1}^3, D = diag((-1)^{n_a});
rates (phi H phi); block 62's frame H[E] = (1/2) sum_j {E^j.sigma, S_j}; block 65's blind walk H[theta] (frame rotation plus the twist hop); the
relabelling's strain couplings of reach two (with S_j) and of reach three (with P_j = S_j C_j). Blocks 68 and 69 compared the species in UNIFORM fields.
T1 (the exchange maps): U_n = (-1)^{n.x}, rho_n = det(D) D (the identity or a half turn about an axis), R_n the coin's half turn for rho_n, V_n = R_n U_n:
   V_n H V_n = det(D) H, and the same with any rate field; V_n^2 = 1; the even maps anticommute pairwise; site densities are unchanged.
T2 (what each VARYING field becomes): frame E -> rho E rho; twist theta -> rho theta; reach-two strain B -> B D; reach-three strain B -> B; each with
   the overall sign det(D).
T3 (consequences): with rates and reach-three strains the four even maps are exact symmetries for every field configuration; U_(111) reverses the
   energy for rates, frames, twists and reach-three strains, so their spectra are symmetric about zero; a reach-two strain is sent to its negative,
   and the spectrum of the walk in a varying reach-two strain is NOT symmetric: tr H^3 = -735/8192 for a rational strain field on a 4x4x4 torus.
Exact arithmetic only (integers, Fractions, Gaussian rationals); the runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "odd_species_keep_the_sign_of_the_energy": "B",
    "even_maps_commute": "B",
    "frame_is_unchanged_under_exchange": "C",
    "twist_is_unchanged_under_exchange": "C",
    "reach_two_strain_is_unchanged": "D",
    "reach_three_strain_is_mirrored": "D",
    "reach_two_keeps_the_energy_reversal": "E",
    "exchange_with_reversal_keeps_the_energy": "E",
    "inversion_is_a_symmetry_of_every_field": "E",
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


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    tor = BIG
    psi = tor.state(3)
    phi = {x: 1 + field(1, 0, 0, x) / 4 for x in tor.sites}
    walk = True
    rates = True
    for n in SPECIES:
        d, s, rho = species_data(n)
        if mut("odd_species_keep_the_sign_of_the_energy"):
            s = 1
        vpsi = exchange(tor, n, psi)
        walk = walk and same(tor, exchange(tor, n, tor.ham(vpsi)), tor.ham(psi), s)
        rates = rates and same(tor, exchange(tor, n, ham_rates(tor, phi, vpsi)), ham_rates(tor, phi, psi), s)
    k = sp.symbols("k", real=True)
    slopes = {0: sp.diff(sp.sin(k), k).subs(k, 0), 1: sp.diff(sp.sin(k), k).subs(k, sp.pi)}
    senses = [int(slopes[n[0]] * slopes[n[1]] * slopes[n[2]]) for n in SPECIES]
    sense_ok = all(senses[i] == species_data(n)[1] for i, n in enumerate(SPECIES)) and senses.count(1) == 4 and senses.count(-1) == 4
    checks.check("B1", walk and rates and sense_ok, "T1: on a 6x6x6 torus, for all eight species n and a rational state, V_n H V_n psi = det(D_n) H psi and V_n (phi H phi) V_n psi = det(D_n) (phi H phi) psi at all 216 sites, phi a varying rational rate field: the four species with an even number of reflected axes are exchanged with the first by exact symmetries of the walk in any rate field; the four odd ones by maps that reverse the energy; det(D_n) is the sense of species n (the determinant of the slopes of sin k_a at its zero): four of each sense")

    involution = all(same(tor, exchange(tor, n, exchange(tor, n, psi)), psi) for n in SPECIES)
    ab = exchange(tor, (1, 1, 0), exchange(tor, (0, 1, 1), psi))
    ba = exchange(tor, (0, 1, 1), exchange(tor, (1, 1, 0), psi))
    third = tor.scale(exchange(tor, (1, 0, 1), psi), I_UNIT)
    algebra = same(tor, ab, ba, -1) and same(tor, ab, third)
    if mut("even_maps_commute"):
        algebra = same(tor, ab, ba)
    densities = True
    for n in SPECIES:
        d, s, rho = species_data(n)
        vpsi = exchange(tor, n, psi)
        densities = densities and tor.redot(vpsi, vpsi) == tor.redot(psi, psi)
        e_before, e_after = tor.redot(psi, tor.ham(psi)), tor.redot(vpsi, tor.ham(vpsi))
        densities = densities and all(e_after[x] == s * e_before[x] for x in tor.sites) and any(e_before[x] != 0 for x in tor.sites)
        for a in range(3):
            before, after = tor.redot(psi, tor.sg(a, psi)), tor.redot(vpsi, tor.sg(a, vpsi))
            densities = densities and all(after[x] == rho[a] * before[x] for x in tor.sites)
    checks.check("B2", involution and algebra and densities, "T1: V_n V_n = 1 for all eight; V_(110) V_(011) = - V_(011) V_(110) = i V_(101): the even maps anticommute pairwise; the site density psi^dagger psi is unchanged at every site and the coin densities psi^dagger sigma_a psi are turned by rho_n, the energy density Re psi^dagger (H psi) is multiplied by det(D_n): a record that reads the site density cannot tell the species apart")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    tor = BIG
    psi = tor.state(4)
    frame = [[{x: (1 if a == j else 0) + field(2, a, j, x) / 3 for x in tor.sites} for j in range(3)] for a in range(3)]
    ok = True
    moved = False
    for n in SPECIES:
        d, s, rho = species_data(n)
        target = [[{x: rho[a] * frame[a][j][x] * rho[j] for x in tor.sites} for j in range(3)] for a in range(3)]
        moved = moved or any(target[a][j] != frame[a][j] for a in range(3) for j in range(3))
        if mut("frame_is_unchanged_under_exchange"):
            target = frame
        ok = ok and same(tor, exchange(tor, n, ham_frame(tor, frame, exchange(tor, n, psi))), ham_frame(tor, target, psi), s)
    checks.check("C1", ok and moved, "T2: for a VARYING rational frame field E(x) (all nine entries), V_n H[E] V_n psi = det(D_n) H[rho_n E rho_n] psi at all 216 sites for all eight n: species n in the frame E is the first species in the frame rho E rho (the same lengths, mirrored angles - block 68 T2 for fields that vary)")

    theta = [{x: field(3, b, b, x) / 2 for x in tor.sites} for b in range(3)]
    rot, hop = twist_parts(tor, theta, psi)
    theta_sigma = lambda g: tor.add(tor.add(tor.times(theta[0], tor.sg(0, g)), tor.times(theta[1], tor.sg(1, g))), tor.times(theta[2], tor.sg(2, g)))
    commutator = tor.scale(tor.add(theta_sigma(tor.ham(psi)), tor.ham(theta_sigma(psi)), -1), G(0, F(-1, 2)))
    block65 = same(tor, commutator, tor.add(rot, hop))
    ok = True
    for n in SPECIES:
        d, s, rho = species_data(n)
        target = [{x: rho[b] * theta[b][x] for x in tor.sites} for b in range(3)]
        if mut("twist_is_unchanged_under_exchange"):
            target = theta
        ok = ok and same(tor, exchange(tor, n, ham_twist(tor, theta, exchange(tor, n, psi))), ham_twist(tor, target, psi), s)
    checks.check("C2", block65 and ok, "T2: block 65's identity -(i/2)[theta.sigma, H] psi = (frame rotation + twist hop) psi re-verified at all 216 sites for a varying rational theta; then V_n H[theta] V_n psi = det(D_n) H[rho_n theta] psi for all eight n: the blind walk is blind for every species, with the rotation vector turned by the half turn rho_n")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    tor = BIG
    psi = tor.state(6)
    strain = [[{x: field(4, a, j, x) / 2 for x in tor.sites} for j in range(3)] for a in range(3)]
    two = True
    three = True
    for n in SPECIES:
        d, s, rho = species_data(n)
        mirrored = [[{x: strain[a][j][x] * d[j] for x in tor.sites} for j in range(3)] for a in range(3)]
        target2 = mirrored if not mut("reach_two_strain_is_unchanged") else strain
        target3 = strain if not mut("reach_three_strain_is_mirrored") else mirrored
        vpsi = exchange(tor, n, psi)
        two = two and same(tor, exchange(tor, n, ham_strain(tor, strain, vpsi, 2)), ham_strain(tor, target2, psi, 2), s)
        three = three and same(tor, exchange(tor, n, ham_strain(tor, strain, vpsi, 3)), ham_strain(tor, target3, psi, 3), s)
    checks.check("D1", two, "T2: for a VARYING rational strain on the bonds (all nine components), reach two: V_n H2[B] V_n psi = det(D_n) H2[B D_n] psi at all 216 sites for all eight n: species n in the strain B is the first species in the strain B D - a stretch along a reflected axis is a squeeze (block 68 T3 for fields that vary); B D is a one-sided change, not a turn of the strain")
    checks.check("D2", three, "T2: reach three: V_n H3[B] V_n psi = det(D_n) H3[B] psi at all 216 sites for all eight n and the same varying strain: with rates and reach-three strains the even maps are exact symmetries for every field configuration, and the odd maps reverse the energy: no field of those two kinds tells the species apart")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    tor = Torus((4, 4, 4))
    strain = [[{x: F(((7 * a + 3 * j + 3 * x[0] * x[0] + 5 * x[1] + x[2] * x[1] + (a + 1) * x[0] + j * x[2]) % 5) - 2, 4) for x in tor.sites} for j in range(3)] for a in range(3)]
    trace = ZERO
    hermitian = True
    for x0 in tor.sites:
        for c0 in range(2):
            basis = zero_field(tor)
            basis[x0] = (G(1), G(0)) if c0 == 0 else (G(0), G(1))
            v = ham_strain(tor, strain, basis, 2)
            hv = ham_strain(tor, strain, v, 2)
            total = G(0)
            for x in tor.sites:
                for c in range(2):
                    total = total + v[x][c].conj() * hv[x][c]
            hermitian = hermitian and total.im == 0
            trace += total.re
    nonzero = (trace != 0) if not mut("reach_two_keeps_the_energy_reversal") else (trace == 0)
    checks.check("E1", hermitian and nonzero and (trace == F(-735, 8192) or mut("reach_two_keeps_the_energy_reversal")), f"T3: on a 4x4x4 torus with a rational reach-two strain field, tr H2[B]^3 = {trace} exactly (sum over all 128 basis states of <H e|H|H e>), not zero: the spectrum of the walk in a varying reach-two strain is NOT symmetric about zero, whereas U_(111) H U_(111) = -H for rates, frames, twists and reach-three strains (B1, C1, C2, D2 with n = (1,1,1), rho = 1) makes theirs symmetric for every field configuration")

    big = BIG
    psi = big.state(8)
    phi = {x: 1 + field(1, 0, 0, x) / 4 for x in big.sites}
    frame = [[{x: (1 if a == j else 0) + field(2, a, j, x) / 3 for x in big.sites} for j in range(3)] for a in range(3)]
    theta = [{x: field(3, b, b, x) / 2 for x in big.sites} for b in range(3)]
    strain = [[{x: field(4, a, j, x) / 2 for x in big.sites} for j in range(3)] for a in range(3)]
    generators = [lambda f: ham_rates(big, phi, f), lambda f: ham_frame(big, frame, f), lambda f: ham_twist(big, theta, f),
                  lambda f: ham_strain(big, strain, f, 2), lambda f: ham_strain(big, strain, f, 3)]
    reversal = lambda f: {x: mat_vec(SIG[1], (f[x][0].conj(), f[x][1].conj())) for x in big.sites}
    commutes = all(same(big, reversal(gen(psi)), gen(reversal(psi))) for gen in generators)
    squares = same(big, reversal(reversal(psi)), psi, -1)
    twin = True
    for n in SPECIES:
        d, s, rho = species_data(n)
        if s == 1:
            continue
        both = lambda f, n=n: reversal(exchange(big, n, f))
        for gen in (generators[0], generators[4]):
            sign = -1 if not mut("exchange_with_reversal_keeps_the_energy") else 1
            twin = twin and same(big, gen(both(psi)), both(gen(psi)), sign)
        twin = twin and big.redot(both(psi), both(psi)) == big.redot(psi, psi)
    checks.check("E2", commutes and squares and twin, "T3: the reversal of motion Theta = sigma_2 x (complex conjugation) commutes with the walk in all five kinds of varying real field (rates, frame, twist, reach-two and reach-three strains) at all 216 sites, and Theta Theta = -1; for the four odd species A_n = Theta V_n anticommutes with the walk in rates and in reach-three strains and keeps the site density: antilinear, it carries every solution to a solution in the SAME fields with the same site densities and the energy reversed")

    inv = lambda x: tuple((-x[i]) % big.dims[i] for i in range(3))
    flip_state = lambda f: {x: f[inv(x)] for x in big.sites}
    site_image = lambda w: {x: w[inv(x)] for x in big.sites}
    bond_image = lambda w, a: {x: w[inv(big.sh(x, a, 1))] for x in big.sites}
    phi_m = site_image(phi)
    frame_m = [[site_image(frame[a][j]) for j in range(3)] for a in range(3)]
    theta_m = [site_image(theta[b]) for b in range(3)]
    strain_m = [[bond_image(strain[a][j], a) for j in range(3)] for a in range(3)]
    if mut("inversion_is_a_symmetry_of_every_field"):
        phi_m, frame_m, theta_m, strain_m = phi, frame, theta, strain
    pairs = [(generators[0], lambda f: ham_rates(big, phi_m, f)), (generators[1], lambda f: ham_frame(big, frame_m, f)), (generators[2], lambda f: ham_twist(big, theta_m, f)),
             (generators[3], lambda f: ham_strain(big, strain_m, f, 2)), (generators[4], lambda f: ham_strain(big, strain_m, f, 3))]
    mirror = all(same(big, flip_state(gen(flip_state(psi))), gen_m(psi), -1) for gen, gen_m in pairs)
    checks.check("E3", mirror, "T3: the inversion x -> -x (no action on the coin) sends the walk in each of the five kinds of varying field to MINUS the walk in the mirror image of that field (site fields at -x; bond fields on the inverted bond), at all 216 sites: with the reversal of motion it carries a solution of one class to a solution of the other class in the mirror-image fields - the two classes of eight branches are mirror images of each other")
# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice with the qubit as their coin and for the couplings of rates, frames, twists and bond strains to them; it reports the exact maps that exchange the walk's eight species and what each varying field becomes under them; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — V_n V_n = 1 for all eight maps; the anticommutation of the even maps; the site density and the three coin densities at all 216 sites of a 6x6x6 torus",
    "per_site: executed — every exchange identity (walk, rates, frame, twist, reach-two strain, reach-three strain) as an equality of spinor fields at all 216 sites, all eight species, fields varying with every coordinate",
    "per_mode: executed — the cubic trace of the walk in a reach-two strain over all 128 basis states of a 4x4x4 torus (exact, not zero); the energy reversal by U_(111) for the other four kinds of field; the sense of each of the eight zeros",
    "per_block: executed — block 65's first-order identity re-verified for the varying rotation vector used; all nine components of the frame and of the strain varied at once; the reversal of motion and the inversion against all five kinds of field",
    "lattice_wide: T1 and T2 are operator identities for every state and every field on every torus with even sides and on the infinite lattice; T3's cubic trace is one executed rational strain field; whether the eight species are all physical, which coupling is supplied and how far it may reach are not decided",
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
    print("scope: the species-exchange maps — site signs and a half turn of the coin exchange the walk's eight species exactly, for fields that vary: rates are unchanged, a frame and a twist are turned by the half turn, a reach-two strain is changed on one side only (B -> B D), a reach-three strain is unchanged; odd species come with the energy reversed; the reach-two strain alone breaks the energy reversal")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
