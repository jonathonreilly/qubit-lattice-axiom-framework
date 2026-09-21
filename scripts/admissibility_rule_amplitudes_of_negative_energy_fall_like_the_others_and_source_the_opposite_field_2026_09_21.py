#!/usr/bin/env python3
"""Exact checks: amplitudes of negative energy as sources (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 54, 55, 56, 60, 70): block 54's walk and its reduced form H = m sigma_1 + sigma_3 D, whose spectra are symmetric about
zero; block 55's ledger (the rate field's source is the amplitudes' ENERGY density e_x; its theorems assumed a positive energy); the static members of
blocks 56 and 60 (their theorems assumed positive bodies); block 70's maps A_n = Theta V_n.
T1 (twins source oppositely): e_x[A_n psi] = -e_x[psi] at every site in any rate field; on the reduced walk a real envelope with the content (1, -1)
   has e_x = -m w_x |chi_x|^2.
T2 (a mixed pair): block 55 T3's pulls stay matched for E_A > 0 > E_B with S = cE, but both accelerations point the same way: the negative body
   follows, the positive one recedes; rays of negative energy follow the paths of rays of positive energy (p -> -p).
T3 (strong field): in block 60's curvature member one negative body at rest has a static field with positive rates iff m > -2K/g_0;
   w_0 = (1 + g_0 m/(2K))^(-1/2) for both signs of m; the second root of the quadratic has a negative rate; at the bound the unit-source potential
   is a zero mode of -Delta + Q/chi; block 56's member has the same zero mode at m = -2/(gamma g_0).
T4 (no rule of finite reach keeps only positive energies): the symbol of the walk's positive-energy projector is discontinuous at each zero; with a
   rest energy it is continuous but not a trigonometric polynomial.
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
    "docs/ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "twin_sources_alike": "B",
    "mixed_pair_attracts_mutually": "B",
    "negative_body_has_no_bound": "C",
    "second_root_is_admissible": "C",
    "positive_energy_projector_has_finite_reach": "D",
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
def exact_solve(matrix, rhs):
    """Gauss-Jordan elimination over the rationals."""
    aug = [row[:] + [b] for row, b in zip(matrix, rhs)]
    size = len(aug)
    for col in range(size):
        pivot = next(r for r in range(col, size) if aug[r][col] != 0)
        aug[col], aug[pivot] = aug[pivot], aug[col]
        lead = aug[col][col]
        aug[col] = [v / lead for v in aug[col]]
        for r in range(size):
            if r != col and aug[r][col] != 0:
                fac = aug[r][col]
                aug[r] = [vr - fac * vc for vr, vc in zip(aug[r], aug[col])]
    return [aug[r][size] for r in range(size)]


def family_b(checks: Checks) -> None:
    tor = BIG
    psi = tor.state(9)
    phi = {x: 1 + field(1, 0, 0, x) / 4 for x in tor.sites}
    reversal = lambda f: {x: mat_vec(SIG[1], (f[x][0].conj(), f[x][1].conj())) for x in tor.sites}
    before = tor.redot(psi, ham_rates(tor, phi, psi))
    opposite = True
    for n in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)):
        twin = reversal(exchange(tor, n, psi))
        after = tor.redot(twin, ham_rates(tor, phi, twin))
        sign = -1 if not mut("twin_sources_alike") else 1
        opposite = opposite and all(after[x] == sign * before[x] for x in tor.sites) and tor.redot(twin, twin) == tor.redot(psi, psi)
    alive = any(before[x] != 0 for x in tor.sites)
    ring = 12
    mass = F(3, 4)
    root = [1 + F((5 * x * x + 3 * x) % 7, 9) for x in range(ring)]                       # phi_x, w = phi^2
    env = [F((x * x + 2 * x) % 5 + 1, 3) for x in range(ring)]                            # a real envelope
    reduced = True
    for content, expected_sign in (((G(1), G(-1)), -1), ((G(1), G(1)), 1)):
        chi = [(content[0] * env[x], content[1] * env[x]) for x in range(ring)]
        scaled = [(chi[x][0] * root[x], chi[x][1] * root[x]) for x in range(ring)]
        for x in range(ring):
            up, dn = scaled[(x + 1) % ring], scaled[(x - 1) % ring]
            hop = tuple((up[c] - dn[c]) * MINUS_HALF_I for c in range(2))                 # D (phi chi)
            h_chi = tuple((mat_vec(SIG[0], scaled[x])[c] * mass + mat_vec(SIG[2], hop)[c]) * root[x] for c in range(2))
            e_x = (chi[x][0].conj() * h_chi[0] + chi[x][1].conj() * h_chi[1]).re
            density = (chi[x][0].conj() * chi[x][0] + chi[x][1].conj() * chi[x][1]).re
            reduced = reduced and e_x == expected_sign * mass * root[x] * root[x] * density
    checks.check("B1", opposite and alive and reduced, "T1: on a 6x6x6 torus with a varying rational rate field, the twin A_n psi = Theta V_n psi of a rational state has the energy density -e_x at every one of the 216 sites and the same site density, for four odd species; on block 54's reduced walk H = m sigma_1 + sigma_3 D on a ring of 12 sites with varying rates, a real envelope with the content (1, -1) has e_x = -m w_x |chi_x|^2 at every site (and +m w_x |chi_x|^2 with the content (1, 1), block 55 T2(c)): under block 55's law an amplitude of negative energy sources the opposite field")

    size = 12
    op = [[F(0)] * size for _ in range(size)]
    for x in range(size):
        op[x][x] += 1
        op[x][(x + 1) % size] -= F(1, 2)
        op[x][(x - 1) % size] -= F(1, 2)
    rhs = [F(-1, size)] * size
    rhs[0] += 1
    op[size - 1] = [F(1)] * size                                                           # replace one (dependent) equation by the zero-mean condition
    rhs[size - 1] = F(0)
    g_ring = exact_solve(op, rhs)
    solves = all(g_ring[x] - (g_ring[(x + 1) % size] + g_ring[(x - 1) % size]) / 2 == (1 if x == 0 else 0) - F(1, size) for x in range(size)) and sum(g_ring, ZERO) == 0
    central = lambda d: (g_ring[(d + 1) % size] - g_ring[(d - 1) % size]) / 2
    x_a, x_b, e_a, e_b, gam = 2, 7, F(2), F(-3, 2), F(1, 5)
    s_a, s_b = e_a, e_b                                                                     # S = cE with c = 1
    pull_a = gam * e_a * s_b * central(x_a - x_b)
    pull_b = gam * e_b * s_a * central(x_b - x_a)
    acc_a, acc_b = pull_a / e_a, pull_b / e_b                                               # block 54: inertia and weight are both the energy
    towards_b = 1                                                                           # x_b > x_a on the short arc
    chase = pull_a + pull_b == 0 and pull_a != 0 and acc_a * acc_b > 0 and acc_a * towards_b < 0 and acc_b * towards_b < 0
    if mut("mixed_pair_attracts_mutually"):
        chase = pull_a + pull_b == 0 and acc_a * acc_b < 0
    pos_pair = gam * e_a * e_a * central(x_a - x_b)
    attract = pos_pair / e_a * towards_b > 0                                                # two positive bodies: A accelerates towards B
    neg_a = gam * e_b * e_b * central(x_a - x_b) / e_b                                      # two negative bodies of energy e_b: acceleration of the one at x_a
    neg_b = gam * e_b * e_b * central(x_b - x_a) / e_b
    repel = neg_a * towards_b < 0 and neg_b * towards_b > 0
    p, xs, m_s = sp.symbols("p x m", real=True)
    wfun = sp.Function("w")(xs)
    eps = sp.sqrt(m_s ** 2 + sp.sin(p) ** 2)
    xdot = lambda e, mom: (wfun * sp.diff(e, p)).subs(p, mom)
    pdot = lambda e, mom: (-e * sp.diff(wfun, xs)).subs(p, mom)
    rays = sp.simplify(xdot(-eps, -p) - xdot(eps, p)) == 0 and sp.simplify(pdot(-eps, -p) + pdot(eps, p)) == 0
    for branch in (eps, -eps):
        vel, force = wfun * sp.diff(branch, p), -branch * sp.diff(wfun, xs)
        accel = (sp.diff(vel, xs) * vel + sp.diff(vel, p) * force).subs(p, 0)
        rays = rays and sp.simplify(accel + wfun * sp.diff(wfun, xs)) == 0
    checks.check("B2", solves and chase and attract and repel and rays, "T2: on a ring of 12 sites with the exact zero-mean potential of block 55's operator, bodies of energies 2 and -3/2 sourcing in proportion to their energies: the two pulls sum to zero exactly (block 55 T3 holds for either sign), and the two accelerations (pull over energy) have the SAME direction - the positive body recedes from the negative one, which follows it; two positive bodies attract and two negative bodies REPEL (each raises the rates around itself, and every body falls towards slow clocks); rays: if (x(t), p(t)) solves Hamilton's equations for w(x) eps(p) then (x(t), -p(t)) solves them for -w(x) eps(p): rays of negative energy follow the same paths, and a ray starting from rest has d^2x/dt^2 = -w w' on either branch")


# ============================================================================================ family C
def box_potential():
    side = 3
    sites = list(product(range(side), repeat=3))
    index = {x: i for i, x in enumerate(sites)}

    def neighbours(x):
        for a in range(3):
            for step in (1, -1):
                y = list(x)
                y[a] += step
                yield tuple(y)
    lap = [[F(0)] * len(sites) for _ in sites]
    for x in sites:
        lap[index[x]][index[x]] = F(6)
        for y in neighbours(x):
            if y in index:
                lap[index[x]][index[y]] = F(-1)
    body = (1, 1, 1)
    g = exact_solve(lap, [F(1) if x == body else F(0) for x in sites])
    return sites, index, neighbours, lap, body, g


def family_c(checks: Checks) -> None:
    sites, index, neighbours, lap, body, g = box_potential()
    g0 = g[index[body]]

    def delta(f, z):
        return sum(((f[index[y]] if y in index else F(1)) for y in neighbours(z)), ZERO) - 6 * f[index[z]]
    good = True
    for r in (F(1, 2), F(1, 10), F(3, 2)):
        q = (r - 1) / (2 * g0)
        mu = q * (1 + q * g0)
        pch = q / r
        chi = [1 + q * gi for gi in g]
        rate_n = [1 - pch * gi for gi in g]
        lengths = all(delta(chi, z) == (-mu / chi[index[z]] if z == body else 0) for z in sites)
        rates = all(delta(rate_n, z) == ((q / chi[index[z]]) * rate_n[index[z]] if z == body else 0) for z in sites)
        positive = all(v > 0 for v in rate_n) and all(v > 0 for v in chi)
        closed = rate_n[index[body]] / chi[index[body]] == 1 / r and r * r == 1 + 4 * g0 * mu and chi[index[body]] == (1 + r) / 2
        ledger = (8 * q) + (8 * q) ** 2 * g0 / 8 == 8 * mu                                  # K = 1: M + M^2 g_0/(8K) = m with M = 8KQ, m = 8K mu
        good = good and lengths and rates and positive and closed and ledger
    beyond = 1 + 4 * g0 * (F(-1, 2) / g0)
    no_root = (beyond < 0) if not mut("negative_body_has_no_bound") else (beyond >= 0)
    checks.check("C1", good and no_root, f"T3: block 60's curvature member on a box (3x3x3 interior, walls at w = l = 1, g_0 = {g0}), one body at rest with m/(8K) = mu of EITHER sign: chi = 1 + Q g, N = 1 - P g with Q = (r - 1)/(2 g_0), P = Q/r, r = (1 + 4 g_0 mu)^(1/2) solve both field equations at all 27 sites with positive lengths and rates, for r = 1/2 and 1/10 (negative bodies) and 3/2 (positive); w_0 = 1/r, chi_0 = (1 + r)/2, M + M^2 g_0/(8K) = m; for mu = -1/(2 g_0) the quadratic has no real root: a negative body at rest has a static field only for m > -2K/g_0, and its clock rate (1 + g_0 m/(2K))^(-1/2) grows without bound as m decreases to it")

    r = F(1, 2)
    q2 = (-r - 1) / (2 * g0)
    mu = q2 * (1 + q2 * g0)
    chi2 = [1 + q2 * gi for gi in g]
    n2 = [1 - (q2 / (-r)) * gi for gi in g]
    second_solves = mu == ((r - 1) / (2 * g0)) * (1 + ((r - 1) / (2 * g0)) * g0) and all(delta(chi2, z) == (-mu / chi2[index[z]] if z == body else 0) for z in sites) \
        and all(delta(n2, z) == ((q2 / chi2[index[z]]) * n2[index[z]] if z == body else 0) for z in sites)
    second_solves = second_solves and all(v > 0 for v in chi2) and all(0 <= gi <= g0 for gi in g)
    negative_rate = (n2[index[body]] < 0) if not mut("second_root_is_admissible") else (n2[index[body]] > 0)

    def pivots(v0):
        a = [row[:] for row in lap]
        a[index[body]][index[body]] += v0
        out = []
        for col in range(len(a)):
            out.append(a[col][col])
            for row in range(col + 1, len(a)):
                fac = a[row][col] / a[col][col]
                a[row] = [vr - fac * vc for vr, vc in zip(a[row], a[col])]
        return out
    q1 = (r - 1) / (2 * g0)
    definite = all(v > 0 for v in pivots(q1 / (1 + q1 * g0))) and not all(v > 0 for v in pivots(q2 / (1 + q2 * g0)))
    qb = F(-1) / (2 * g0)
    v_bound = qb / (1 + qb * g0)
    zero_mode = v_bound == -1 / g0 and all(sum((lap[i][j] * g[j] for j in range(len(g))), ZERO) + (v_bound * g[i] if sites[i] == body else 0) == 0 for i in range(len(g)))
    gam = F(1, 4)
    m56 = -1 / (gam * g0)
    phi0 = 1 / (1 + gam * m56 * g0 / 2)
    phi = [1 - (gam / 2) * m56 * phi0 * gi for gi in g]
    law56 = all((2 / gam) * (-delta(phi, z)) + (m56 * phi[index[z]] if z == body else 0) == 0 for z in sites) and phi0 == 2 and phi[index[body]] == phi0
    pole56 = 1 + gam * (-2 / (gam * g0)) * g0 / 2 == 0 and (gam / 2) * (-2 / (gam * g0)) == -1 / g0
    checks.check("C2", second_solves and negative_rate and definite and zero_mode and law56 and pole56, "T3: the quadratic's second root solves both field equations with positive lengths at all 27 sites (0 <= g <= g_0) but its rate at the body is negative (not admissible); the Dirichlet operator -Delta + Q/chi is positive definite at the admissible root (all 27 pivots positive) and not at the second; at the bound Q/chi = -1/g_0 and the unit-source potential g is its zero mode at every site; block 56's member (law linear in phi = sqrt(w)): phi_0 = 1/(1 + gamma m g_0/2) = 2 at m = -1/(gamma g_0), exact at all 27 sites, with the same zero mode at m = -2/(gamma g_0)")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    t = sp.symbols("t", real=True)
    k = sp.symbols("k", real=True)
    right = sp.limit(sp.sin(t) / sp.sqrt(sp.sin(t) ** 2), t, 0, "+")
    left = sp.limit(sp.sin(t) / sp.sqrt(sp.sin(t) ** 2), t, 0, "-")
    jump = (right == 1 and left == -1) if not mut("positive_energy_projector_has_finite_reach") else (right == left)
    z, m_s = sp.symbols("z m", positive=True)
    sin2 = -(z - 1 / z) ** 2 / 4
    tops = True
    for deg in range(0, 4):
        coeffs = sp.symbols(f"a0:{2 * deg + 1}")
        poly = sum(coeffs[i] * z ** (i - deg) for i in range(2 * deg + 1))
        product_top = sp.expand(poly ** 2 * (m_s ** 2 + sin2) * z ** (2 * deg + 2)).coeff(z, 4 * deg + 4)
        tops = tops and sp.simplify(product_top + coeffs[-1] ** 2 / 4) == 0
    checks.check("D1", jump and tops, "T4: along k = (t, 0, 0) the unit vector sin k/|sin k| of the walk tends to +e_1 for t -> 0+ and to -e_1 for t -> 0-: the symbol (1/2)(1 + sigma.s/|s|) of the positive-energy projector is discontinuous at the zero (and, by block 70's maps, at each of the eight), while a rule of finite reach - or of summable reach - has a continuous symbol; with a rest energy, p(z)^2 (m^2 + sin^2 k) has the top coefficient -a^2/4 for every trigonometric polynomial p of degree 0 to 3 with top coefficient a, so it is never 1: the projector is continuous but not of finite reach")
# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for amplitudes on the lattice timed by local clocks and for a ledger that makes their energy density the source of the rate field; it reports what those clauses say about amplitudes of negative energy; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — the energy density of a state and of its twin at all 216 sites of a 6x6x6 torus in a varying rate field; the reduced walk's two contents at all 12 sites of a ring",
    "per_site: executed — both field equations of the curvature member at all 27 interior sites of the box for three sizes of body of either sign, and for the second root; the zero mode at the bound at every site; block 56's linear law at all 27 sites",
    "per_mode: executed — the 27 pivots of -Delta + Q/chi at the admissible and at the second root; the one-sided limits of the projector's symbol at the zero; top coefficients for trigonometric polynomials of degree 0 to 3",
    "per_block: executed — the two pulls and the two accelerations of a mixed pair on a ring with the exact zero-mean potential; the symmetry of the rays' equations under the reversal of the energy and the momentum",
    "lattice_wide: T1 for every state and rate field; T2 for point bodies in the weak field and for rays; T3 for one body at rest in a box with held walls (closed forms in g_0), many bodies through the stated criterion; T4 for the walk and its reduced form; whether amplitudes of negative energy are present, and what would exclude them, are not decided",
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
    print("scope: amplitudes of negative energy — as test bodies they are exact twins of those of positive energy; as sources they are exact opposites; a mixed pair keeps its pulls matched while both bodies accelerate the same way; a negative body at rest in the curvature member has a static field only above -2K/g_0, where its clock rate grows without bound; no rule of finite reach keeps only the positive energies")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
