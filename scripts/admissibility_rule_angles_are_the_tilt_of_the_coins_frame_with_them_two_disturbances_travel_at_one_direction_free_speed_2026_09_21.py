#!/usr/bin/env python3
"""Exact checks: angles are the tilt of the coin's frame (supplied clauses on Z^3; not adopted).

OBJECTS (supplied by blocks 53 to 61): block 54's walk, H = sum_j sigma_j S_j with S_j = (T_j - T_j^dagger)/(2i), the qubit as coin; site rates; lengths
of weight zero; a ledger linear in the rates with the curvature member.
WIDENING (supplied): a FRAME at every site, E_a^j(x) (coin axis a, bond direction j): H = (1/2) sum_j { E^j(x).sigma , S_j }.  Block 54 is E = 1; block
59's bond rates and block 61's three lengths are the diagonal frames E_j^j = 1/l_j.
T1 (what the walker sees): for a uniform frame H^2 = sum_ij g^ij sin k_i sin k_j with g^ij = sum_a E_a^i E_a^j: the walker sees a full symmetric inverse
   metric - three lengths and three angles; a rotation of the coin axes changes neither g nor the spectrum.  The symmetrised generator is hermitian for
   every frame field.
T2 (what sources the frame): <H> = sum_x sum_aj E_a^j(x) Theta_a^j(x), Theta_a^j(x) = Re psi^dagger(x) sigma_a (S_j psi)(x) = d<H>/dE_a^j(x).  For a
   plane wave of the identity frame Theta_a^j = s_a s_j/energy (s_j = sin k_j): symmetric, with off-diagonal parts unless the walker moves along an axis.
T3 (the member for the full symmetric stretching, second order): with g_ij = delta_ij + h_ij (h = -(eps + eps^T) for E = 1 + eps; the antisymmetric
   part of eps drops out) and p_j = 2 sin(k_j/2):  R_1 = -(p_i p_j h_ij - p^2 h),  R_2 = -(1/4) p^2 h_ij h_ij + (1/2)(p_i h_ij)^2 - (1/2)(p_i h_ij p_j) h
   + (1/4) p^2 h^2;  F_2 = -K wbar (u R_1 + R_2).  Both are unchanged by the relabelling h_ij -> h_ij + p_i xi_j + p_j xi_i; on diagonal h they are block
   61's forms, on h = 2 lam delta block 60's.
T4 (travelling disturbances): with T_2 = (1/wbar)[alpha hdot_ij hdot_ij + beta hdot^2] the mode determinant is
   -32 X^3 alpha^2 (alpha + beta) (p^2)^2 (K wbar^2 p^2 - 4 alpha X)^2 (K = wbar = 1 in the runner): exactly TWO travelling disturbances, transverse and
   traceless, with X = K wbar^2 p^2/(4 alpha) in EVERY direction and at every wavelength; three static relabelling modes.  A kinetic term invariant under
   the cube's symmetries only (M_3 != 2M_1 - M_2) loses this.
T5 (static response): the static equations can be solved iff the stress is divergence-free, sum_i p_i Theta_(ij) = 0 (rank test); a body at rest gives
   block 60's law; for a divergence-free stress the response stays bounded near the coordinate planes, where block 61's three-length response grows like
   1/(p_2^2 p_3^2).
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
    "docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "coin_rotation_changes_the_metric": "B",
    "unsymmetrised_generator_is_hermitian": "B",
    "frame_response_does_not_sum_to_the_energy": "C",
    "diagonal_motion_has_no_off_diagonal_response": "C",
    "member_not_invariant_under_relabelling": "D",
    "coin_rotation_enters_the_metric_at_first_order": "D",
    "three_disturbances_travel": "E",
    "cubic_kinetic_term_keeps_one_speed": "E",
    "any_stress_has_a_static_response": "E",
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


def rational_frame(seed):
    """A frame field near the identity: E_a^j(x) = delta_aj + small rational numbers; frame[x][j] is the coin vector of bond direction j."""
    out = {}
    for x in SITES:
        rows = []
        for j in range(3):
            rows.append(tuple((ONE if a == j else ZERO) + F((seed * 11 + 5 * a + 7 * j + 3 * x[0] + x[1] * (a + 1) + x[2] * (j + 2)) % 9 - 4, 20) for a in range(3)))
        out[x] = rows
    return out


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    frame = [(F(3, 2), F(1, 5), ZERO), (F(1, 2), F(4, 3), F(-1, 4)), (F(1, 7), F(2, 3), F(5, 6))]          # frame[j] = coin vector of bond direction j
    sines = (F(3, 5), F(-4, 5), F(5, 13))
    rot = [[ONE, ZERO, ZERO], [ZERO, F(3, 5), F(-4, 5)], [ZERO, F(4, 5), F(3, 5)]]                        # a rotation of the coin axes with rational entries

    def metric(fr):
        return [[sum((fr[i][a] * fr[j][a] for a in range(3)), ZERO) for j in range(3)] for i in range(3)]

    def h_squared(fr):
        h = [[G(0), G(0)], [G(0), G(0)]]
        for j in range(3):
            h = mat_add(h, mat_scale(frame_matrix(fr[j]), sines[j]))
        return mat_mul(h, h)

    g = metric(frame)
    scalar = sum((g[i][j] * sines[i] * sines[j] for i in range(3) for j in range(3)), ZERO)
    h2 = h_squared(frame)
    square_ok = h2[0][0] == scalar and h2[1][1] == scalar and h2[0][1] == 0 and h2[1][0] == 0
    turned = [tuple(sum((rot[a][b] * frame[j][b] for b in range(3)), ZERO) for a in range(3)) for j in range(3)]
    g_turned = metric(turned)
    same_metric = (g_turned == g) if not mut("coin_rotation_changes_the_metric") else (g_turned != g)
    h2t = h_squared(turned)
    off = sum((1 for i in range(3) for j in range(3) if i != j and g[i][j] != 0), 0)
    diag = [(F(2), ZERO, ZERO), (ZERO, F(1, 3), ZERO), (ZERO, ZERO, F(5, 4))]
    gd = metric(diag)
    diag_ok = all(gd[i][j] == (diag[i][i] ** 2 if i == j else 0) for i in range(3) for j in range(3))
    checks.check("B1", square_ok and same_metric and h2t[0][0] == scalar and h2t[0][1] == 0 and off == 6 and diag_ok, f"T1: for a uniform rational frame and rational sines, H^2 = (sum_ij g^ij s_i s_j) x 1 exactly, g^ij = sum_a E_a^i E_a^j = {about(scalar)} here, with all six off-diagonal entries of g non-zero: the walker sees three lengths and three angles; a rotation of the coin axes leaves g and H^2 unchanged; diagonal frames give g^jj = E_j^j squared: block 59's bond rates and block 61's lengths")

    field = rational_frame(2)
    phi, psi = rational_state(1), rational_state(4)
    symmetrised = not mut("unsymmetrised_generator_is_hermitian")
    lhs = inner(phi, generator(psi, field, symmetrised))
    rhs = inner(generator(phi, field, symmetrised), psi)
    plain_l = inner(phi, generator(psi, field, False))
    plain_r = inner(generator(phi, field, False), psi)
    checks.check("B2", lhs == rhs and plain_l != plain_r, "T1: on a 3x3x3 torus with a non-uniform rational frame field, <phi|H psi> = <H phi|psi> exactly for the symmetrised generator (1/2) sum_j {E^j.sigma, S_j}, and not for the unsymmetrised one: the bond from x along j carries the mean of the two ends' coin vectors")


# ============================================================================================ family C
def theta(psi):
    """Theta_a^j(x) = Re psi^dagger(x) sigma_a (S_j psi)(x)."""
    out = {}
    for j in range(3):
        sp_ = s_op(psi, j)
        for a in range(3):
            for x in SITES:
                v = mat_vec(SIG[a], sp_[x])
                out[(a, j, x)] = (psi[x][0].conj() * v[0] + psi[x][1].conj() * v[1]).re
    return out


def family_c(checks: Checks) -> None:
    field = rational_frame(2)
    psi = rational_state(4)
    energy = inner(psi, generator(psi, field))
    th = theta(psi)
    total = sum((field[x][j][a] * th[(a, j, x)] for a in range(3) for j in range(3) for x in SITES), ZERO)
    if mut("frame_response_does_not_sum_to_the_energy"):
        total = total + th[(0, 1, SITES[0])]
    bumped = {x: [tuple(v) for v in field[x]] for x in SITES}
    site, a0, j0 = (1, 2, 0), 2, 0
    vec = list(bumped[site][j0])
    vec[a0] += 1
    bumped[site][j0] = tuple(vec)
    slope = inner(psi, generator(psi, bumped)).re - energy.re
    checks.check("C1", energy.im == 0 and total == energy.re and slope == th[(a0, j0, site)], f"T2: <H> = sum over sites, coin axes and bond directions of E_a^j(x) Theta_a^j(x) exactly ({about(energy.re)} for a rational amplitude in a non-uniform frame), and the derivative of <H> in one entry of the frame, taken by an exact difference, is Theta there: the frame is sourced by the flux of momentum j carried along coin axis a")

    def plane_wave_response(s):
        norm2 = sum((v * v for v in s), ZERO)
        root = next(F(n, d) for d in range(1, 40) for n in range(0, 80) if F(n, d) ** 2 == norm2)
        top, bottom = G(root + s[2]), G(s[0], s[1])                                                # eigenvector of s.sigma with eigenvalue +|s|
        norm = (top.conj() * top + bottom.conj() * bottom).re
        chi = (top, bottom)
        resp = [[ZERO] * 3 for _ in range(3)]
        for a in range(3):
            v = mat_vec(SIG[a], chi)
            spin = (chi[0].conj() * v[0] + chi[1].conj() * v[1]).re / norm
            for j in range(3):
                resp[a][j] = spin * s[j]
        return resp, root

    resp, eps = plane_wave_response((F(1, 3), F(2, 3), F(2, 3)))
    s = (F(1, 3), F(2, 3), F(2, 3))
    form_ok = all(resp[a][j] == s[a] * s[j] / eps for a in range(3) for j in range(3))
    off_ok = (resp[0][1] != 0 and resp[1][2] != 0) if not mut("diagonal_motion_has_no_off_diagonal_response") else (resp[0][1] == 0)
    axis, _ = plane_wave_response((F(3, 5), ZERO, ZERO))
    axis_ok = all((axis[a][j] != 0) == (a == 0 and j == 0) for a in range(3) for j in range(3))
    checks.check("C2", form_ok and off_ok and axis_ok, f"T2: a plane wave of the identity frame with sines (1/3, 2/3, 2/3) and energy 1 has Theta_a^j = s_a s_j/energy per unit probability: symmetric, with off-diagonal parts {resp[0][1]}, {resp[0][2]}, {resp[1][2]}: a walker moving across the axes sources angles; one moving along an axis has the single entry Theta_1^1 (block 59 T2)")


# ============================================================================================ family D
P = sp.symbols("p1 p2 p3", real=True)
HS = sp.symbols("h11 h22 h33 h12 h13 h23 u")
PAIRS = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def h_entry(i, j):
    return HS[PAIRS.index((min(i, j), max(i, j)))]


def member(mutated=False):
    psq = sum(q * q for q in P)
    tr = HS[0] + HS[1] + HS[2]
    hh = sum(h_entry(i, j) ** 2 for i in range(3) for j in range(3))
    div = [sum(P[i] * h_entry(i, j) for i in range(3)) for j in range(3)]
    half = sp.Rational(1, 2) if not mutated else sp.Rational(1, 4)
    r2 = -sp.Rational(1, 4) * psq * hh + half * sum(d * d for d in div) - sp.Rational(1, 2) * sum(div[j] * P[j] for j in range(3)) * tr + sp.Rational(1, 4) * psq * tr ** 2
    r1 = -(sum(P[i] * P[j] * h_entry(i, j) for i in range(3) for j in range(3)) - psq * tr)
    return r1, r2


def family_d(checks: Checks) -> None:
    r1, r2 = member(mut("member_not_invariant_under_relabelling"))
    xi = sp.symbols("xi1 xi2 xi3", real=True)
    gauge = {h_entry(i, j): h_entry(i, j) + P[i] * xi[j] + P[j] * xi[i] for i, j in PAIRS}
    inv1 = sp.expand(r1.subs(gauge, simultaneous=True) - r1) == 0
    inv2 = sp.expand(r2.subs(gauge, simultaneous=True) - r2) == 0
    lam = sp.symbols("l1 l2 l3", real=True)
    diag = {HS[0]: 2 * lam[0], HS[1]: 2 * lam[1], HS[2]: 2 * lam[2], HS[3]: 0, HS[4]: 0, HS[5]: 0}
    a, b, c = P[0] ** 2, P[1] ** 2, P[2] ** 2
    r1_true, r2_true = member(False)
    d1 = sp.expand(r1_true.subs(diag) - 2 * ((b + c) * lam[0] + (a + c) * lam[1] + (a + b) * lam[2])) == 0
    d2 = sp.expand(r2_true.subs(diag) - 2 * (c * lam[0] * lam[1] + b * lam[0] * lam[2] + a * lam[1] * lam[2])) == 0
    one = sp.symbols("lam", real=True)
    iso = {HS[0]: 2 * one, HS[1]: 2 * one, HS[2]: 2 * one, HS[3]: 0, HS[4]: 0, HS[5]: 0}
    i1 = sp.expand(r1_true.subs(iso) - 4 * (a + b + c) * one) == 0
    i2 = sp.expand(r2_true.subs(iso) - 2 * (a + b + c) * one ** 2) == 0
    checks.check("D1", inv1 and inv2 and d1 and d2 and i1 and i2, "T3: R_1 and R_2 are unchanged by the relabelling h_ij -> h_ij + p_i xi_j + p_j xi_i for every real p, hence for the lattice's p_j = 2 sin(k_j/2); on diagonal h_jj = 2 lam_j they are block 61's 2 sum_j (p^2 - p_j^2) lam_j and 2 (p_3^2 lam_1 lam_2 + p_2^2 lam_1 lam_3 + p_1^2 lam_2 lam_3); on h = 2 lam delta they are block 60's 4 p^2 lam and 2 p^2 lam^2 (exact symbolic algebra)")

    t = sp.symbols("t", real=True)
    eps = sp.Matrix(3, 3, sp.symbols("e11 e12 e13 e21 e22 e23 e31 e32 e33", real=True))
    frame = sp.eye(3) + t * eps                                                                      # frame[a, j] = E_a^j
    g_inv = frame.T * frame                                                                           # g^ij = sum_a E_a^i E_a^j
    g_low = g_inv.inv()
    first = sp.Matrix(3, 3, lambda i, j: sp.diff(g_low[i, j], t).subs(t, 0))
    sym_ok = sp.simplify(first + eps + eps.T) == sp.zeros(3, 3)
    anti = sp.Matrix([[0, 1, -2], [-1, 0, 3], [2, -3, 0]])
    first_anti = first.subs({eps[i, j]: anti[i, j] for i in range(3) for j in range(3)})
    drops = (first_anti == sp.zeros(3, 3)) if not mut("coin_rotation_enters_the_metric_at_first_order") else (first_anti != sp.zeros(3, 3))
    checks.check("D2", sym_ok and drops, "T3: for E = 1 + eps the metric is delta + h with h = -(eps + eps^T) at first order; an antisymmetric eps (a small rotation of the coin axes) drops out: of the nine numbers of a frame, six are seen (exact symbolic algebra)")


# ============================================================================================ family E
def mode_determinant(kinetic):
    xx = sp.symbols("X", real=True)
    r1, r2 = member(False)
    v = -(HS[6] * r1 + r2)
    q = xx * kinetic - v
    hess = sp.Matrix([[sp.diff(q, s1, s2) for s2 in HS] for s1 in HS])
    return xx, hess


def family_e(checks: Checks) -> None:
    al, be = sp.symbols("alpha beta", real=True)
    tr = HS[0] + HS[1] + HS[2]
    hh = sum(h_entry(i, j) ** 2 for i in range(3) for j in range(3))
    xx, hess = mode_determinant(al * hh + be * tr ** 2)
    psq = sum(q * q for q in P)
    power = 2 if not mut("three_disturbances_travel") else 3
    expected = -32 * xx ** 3 * al ** 2 * (al + be) * psq ** 2 * (psq - 4 * al * xx) ** power
    det_ok = sp.expand(hess.det() - expected) == 0
    checks.check("E1", det_ok, "T4: with the kinetic term alpha hdot_ij hdot_ij + beta hdot^2 the mode determinant in (h_11, ..., h_23, u) is -32 X^3 alpha^2 (alpha + beta) (p^2)^2 (p^2 - 4 alpha X)^2: exactly two travelling disturbances, both with X = p^2/(4 alpha) whatever the direction, and three static modes (exact symbolic algebra; K = wbar = 1)")

    point = {P[0]: 1, P[1]: 2, P[2]: 2, al: sp.Rational(1, 4), be: 1}
    at_root = hess.subs(point).subs(xx, 9)
    null = at_root.nullspace()
    transverse = True
    for vec in null:
        hm = sp.Matrix(3, 3, lambda i, j: vec[PAIRS.index((min(i, j), max(i, j)))])
        pv = sp.Matrix([1, 2, 2])
        transverse = transverse and hm * pv == sp.zeros(3, 1) and hm.trace() == 0 and vec[6] == 0
    checks.check("E2", len(null) == 2 and transverse, "T4: at p = (1, 2, 2), X = p^2 = 9 (alpha = 1/4, beta = 1) the null space is two-dimensional and every disturbance in it has p_i h_ij = 0, zero trace and u = 0: transverse, traceless, and invisible to the rates at this order")

    m1, m2, m3 = 1, 0, 1                                                                              # invariant under the cube's symmetries only: M_3 != 2 M_1 - M_2
    cubic = m1 * (HS[0] ** 2 + HS[1] ** 2 + HS[2] ** 2) + m2 * (HS[0] * HS[1] + HS[0] * HS[2] + HS[1] * HS[2]) + m3 * (HS[3] ** 2 + HS[4] ** 2 + HS[5] ** 2)
    if mut("cubic_kinetic_term_keeps_one_speed"):
        cubic = sp.Rational(1, 2) * hh                                                               # the rotation-invariant term in its place: the two directions then share a root
    xc, hc = mode_determinant(cubic)
    v = sp.symbols("v", real=True)
    poly_a = sp.factor(hc.subs({P[0]: 1, P[1]: 2, P[2]: 2}).det().subs(xc, 9 * v))
    poly_b = sp.factor(hc.subs({P[0]: 1, P[1]: 4, P[2]: 8}).det().subs(xc, 81 * v))
    strip = lambda pol: sp.Poly(sp.cancel(pol / v ** 3), v)
    common = sp.gcd(strip(poly_a), strip(poly_b))
    checks.check("E3", common.degree() == 0, "T4: for a kinetic term invariant under the cube's symmetries only, (M_1, M_2, M_3) = (1, 0, 1), the speeds^2 X/p^2 at p = (1, 2, 2) and at p = (1, 4, 8) have no value in common (the two polynomials are coprime): one speed for all directions needs the rotation-invariant combination")

    k_ = sp.Rational(3, 4)
    r1, r2 = member(False)
    vstat = -k_ * (HS[6] * r1 + r2)
    static = sp.Matrix([[sp.diff(vstat, s1, s2) for s2 in HS] for s1 in HS])

    def source(th, energy):
        return sp.Matrix([th[0, 0] / 2, th[1, 1] / 2, th[2, 2] / 2, th[0, 1], th[0, 2], th[1, 2], -energy])

    pt = {P[0]: 1, P[1]: 2, P[2]: 2}
    a_pt = static.subs(pt)
    va = sp.Matrix([2, -1, 0])
    conserved = va * va.T
    broken = sp.diag(1, 0, 0)
    rank_a = a_pt.rank()
    ok_conserved = a_pt.row_join(source(conserved, sp.Rational(1, 3))).rank() == rank_a
    ok_broken = a_pt.row_join(source(broken, 0)).rank() == rank_a
    refused = (not ok_broken) if not mut("any_stress_has_a_static_response") else ok_broken
    energy = sp.Rational(7, 5)
    lam0 = energy / (4 * k_ * 9)
    rest = sp.Matrix([2 * lam0, 2 * lam0, 2 * lam0, 0, 0, 0, -lam0])
    rest_ok = a_pt * rest == source(sp.zeros(3, 3), energy)
    checks.check("E4", rank_a == 4 and ok_conserved and refused and rest_ok, "T5: at p = (1, 2, 2) the static matrix has rank 4 (three relabelling directions); a stress with sum_i p_i Theta_(ij) = 0 has a static response for every energy, the stress diag(1, 0, 0), which is not divergence-free, has none; a body at rest gives h = 2 lam delta, u = -lam, lam = e/(4K p^2): block 60's law")

    near = {P[0]: 1, P[1]: 2, P[2]: sp.Rational(1, 100)}
    a_near = static.subs(near)
    gauge_cols = []
    pn = [1, 2, sp.Rational(1, 100)]
    for m in range(3):
        col = [0] * 7
        for idx, (i, j) in enumerate(PAIRS):
            col[idx] = (pn[i] if j == m else 0) + (pn[j] if i == m else 0)
        gauge_cols.append(col)
    gmat = sp.Matrix(gauge_cols).T
    stress_near = va * va.T                                                                          # (2, -1, 0) is orthogonal to (1, 2, 1/100) as well
    normal = a_near.T * a_near + gmat * gmat.T
    resp = normal.solve(a_near.T * source(stress_near, 0))
    solved = a_near * resp == source(stress_near, 0) and gmat.T * resp == sp.zeros(3, 1)
    size = max(abs(x) for x in resp)
    three_length = sp.Rational(1) / (2 * 4 * sp.Rational(1, 10000)) / (2 * k_)                         # block 61: |a_1| = p_1^2 tau_1/(2 p_2^2 p_3^2)/(2K) for unit tau_1 at the same p
    checks.check("E5", solved and size < 3 and three_length > 800, f"T5: near a coordinate plane, p = (1, 2, 1/100), a divergence-free stress of size 4 has a static response (taken orthogonal to the relabellings) whose largest entry is {about(F(int(sp.numer(size)), int(sp.denom(size))))}, while block 61's three-length response to a unit of hop energy at the same p is {about(F(int(sp.numer(three_length)), int(sp.denom(three_length))))}: the one-dimensional inverses are gone")


# ============================================================================================ family F
FENCES = (
    "This note works within supplied clauses for local tick rates, for amplitudes timed by them and for lengths of weight zero, widened by a frame for the coin at every site and one declared member of the ledger at second order; it reports what the walker sees of such a frame, what sources it and what travels in it; nothing is adopted and no gravitational claim is made.",
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
    "per_element: executed — H^2 for a uniform rational frame with all six off-diagonal entries of the metric non-zero, under a rational rotation of the coin axes, and for diagonal frames; hermiticity on a 3x3x3 torus with a non-uniform frame field",
    "per_site: executed — the frame response at all 27 sites, nine entries each, summing to the energy; its derivative by an exact difference; a plane wave moving across the axes and one along an axis",
    "per_mode: executed — the relabelling invariance of both orders of the member; the mode determinant for the rotation-invariant kinetic family; the two transverse traceless disturbances at p = (1, 2, 2); coprimality of the speeds at two directions for a kinetic term of the cube's symmetry only",
    "per_block: executed — the rank test for static responses (a divergence-free stress, one that is not, a body at rest); the size of the response near a coordinate plane against block 61's; the first-order relation between frame and metric",
    "lattice_wide: T1 holds for every uniform frame and every wave vector, hermiticity for every frame field; T2 for every amplitude and frame field; T3 for every real p and hence every wave vector of a torus; T4 for the rotation-invariant kinetic family at every wave vector; T5 wave vector by wave vector on a torus; second order in the fields for T3 to T5, for the declared member only; that the coin has a frame, the member, K, alpha, beta, whether the walk's own stress is divergence-free, and any law for the rotation of the coin axes are not derived",
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
    print("scope: angles as the tilt of the coin's frame — the walker sees a full symmetric metric through H^2 = g^ij sin k_i sin k_j; the frame is sourced by the flux of momentum along coin axes; the curvature member for the full symmetric stretching is relabelling-invariant and has exactly two travelling disturbances, transverse and traceless, at one direction-free speed; static responses exist iff the stress is divergence-free and then hold no one-dimensional inverses")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
