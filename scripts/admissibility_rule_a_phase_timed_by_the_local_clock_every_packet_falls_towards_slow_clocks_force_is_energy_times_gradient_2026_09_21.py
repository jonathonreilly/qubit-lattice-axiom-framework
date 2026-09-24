#!/usr/bin/env python3
"""Exact arithmetic controls for the supplied clocked-amplitude model.
Generator classification, fixed-rate finite weighted adjoints, polynomial translation identities,
an explicit counterexample to universal packet force, and conditional smooth ray acceleration.
No global exponential-field evolution, general ray-limit theorem or physical identification is asserted.
"""

from __future__ import annotations

import ast
import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)
PACKET_NEEDLE = "S_test(phi; x) = L_test (1 - phi(x))"

MUTATION_GATE = {
    "content_matrices_commute": "B",
    "inversion_leaves_the_content_alone": "B",
    "a_rest_energy_matrix_exists": "B",
    "inner_product_without_the_clock_weight": "C",
    "bond_timing_of_degree_two": "C",
    "clock_ratio_inverted": "D",
    "rate_field_not_exponential": "D",
    "fall_without_the_velocity_term": "E",
    "lattice_factor_dropped": "E",
    "energy_offset_is_harmless": "E",
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
E6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


class G:
    """A Gaussian rational re + i im."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

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

    def is_zero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        return f"({self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i)"


I_UNIT = G(0, 1)
HALF_I = G(0, F(1, 2))


def content_matrices():
    s1 = [[G(0), G(1)], [G(1), G(0)]]
    s2 = [[G(0), G(0, -1)], [G(0, 1), G(0)]]
    s3 = [[G(1), G(0)], [G(0), G(-1)]]
    if mut("content_matrices_commute"):
        s2 = [[G(0), G(1)], [G(1), G(0)]]
    return [s1, s2, s3]


def mmul(a, b):
    return [[a[i][0] * b[0][j] + a[i][1] * b[1][j] for j in range(2)] for i in range(2)]


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def mscale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def mconj(a):
    return [[a[i][j].conj() for j in range(2)] for i in range(2)]


def meq(a, b):
    return all(a[i][j] == b[i][j] for i in range(2) for j in range(2))


IDENT = [[G(1), G(0)], [G(0), G(1)]]
NULL = [[G(0), G(0)], [G(0), G(0)]]


def proper_rotations():
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            parity = 1
            p = list(perm)
            for i in range(3):
                for j in range(i + 1, 3):
                    if p[i] > p[j]:
                        parity = -parity
            if parity * signs[0] * signs[1] * signs[2] == 1:
                out.append((perm, signs))
    return out


def rotate(g, v):
    perm, signs = g
    return tuple(signs[i] * v[perm[i]] for i in range(3))


def rank(rows):
    rows = [[F(c) for c in r] for r in rows]
    rk = 0
    ncols = len(rows[0]) if rows else 0
    for col in range(ncols):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        pv = rows[rk][col]
        rows[rk] = [c / pv for c in rows[rk]]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                fac = rows[i][col]
                rows[i] = [a - fac * b for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk


# ------------------------------------------------------------------------------ sparse amplitudes on the infinite lattice: {(x, y, z, s): G}
def vadd(a, b, cb=ONE):
    out = dict(a)
    for key, val in b.items():
        new = out.get(key, G(0)) + val * cb
        if new.is_zero():
            out.pop(key, None)
        else:
            out[key] = new
    return out


def vscale(a, c):
    return {k: v * c for k, v in a.items() if not (v * c).is_zero()}


def veq(a, b):
    return not vadd(a, b, -ONE)


def shift(vec, a):
    return {(k[0] + a[0], k[1] + a[1], k[2] + a[2], k[3]): v for k, v in vec.items()}


def apply_walk(vec, sqrt_w=None, bond=None, sig=None):
    """(H psi)(x) = sum_j sigma_j (i/2)(psi(x - e_j) - psi(x + e_j)); with clocks the amplitude on a bond is sqrt(w_x w_y) (or `bond`(x, y))."""
    sig = sig or content_matrices()
    out: dict = {}
    for (x, y, z, s), val in vec.items():
        src = (x, y, z)
        for j, e in enumerate(AXES):
            for sign in (+1, -1):
                tgt = (x + sign * e[0], y + sign * e[1], z + sign * e[2])
                if bond is not None:
                    amp = bond(src, tgt)
                elif sqrt_w is not None:
                    amp = sqrt_w(src) * sqrt_w(tgt)
                else:
                    amp = ONE
                for s2 in range(2):
                    c = sig[j][s2][s]
                    if c.is_zero():
                        continue
                    key = tgt + (s2,)
                    new = out.get(key, G(0)) + c * HALF_I * val * (amp * sign)
                    if new.is_zero():
                        out.pop(key, None)
                    else:
                        out[key] = new
    return out


def delta(site, s):
    return {tuple(site) + (s,): G(1)}


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, packet = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clause works in that opening)")
    checks.check("A3", PACKET_NEEDLE in packet, "weak-field packet on main: its third supplied piece is the test response S_test = L_test (1 - phi): a path's phase reduced in proportion to the field")


# ============================================================================================ family B
def generator_space(inversion: str):
    """Dimension of the real space of nearest-neighbour generators sum_e A_e T_e (A_e in M_2(C), e = 0 and the six directions) that are
    covariant under the 24 rotations and hermitian, with the chosen behaviour under lattice inversion; returns (dimension, rows)."""
    dirs = [(0, 0, 0)] + E6
    col = {(e, mu, part): 8 * i + 2 * mu + part for i, e in enumerate(dirs) for mu in range(4) for part in range(2)}
    rows = []

    def row(entries):
        r = [ZERO] * 56
        for key, val in entries:
            r[col[key]] += val
        rows.append(r)

    for g in proper_rotations():
        perm, signs = g
        for e in dirs:
            ge = rotate(g, e)
            for part in range(2):
                row([((ge, 0, part), ONE), ((e, 0, part), -ONE)])
                for i in range(3):                                   # vector part: c(g e)_i = signs[i] c(e)_perm[i]
                    row([((ge, 1 + i, part), ONE), ((e, 1 + perm[i], part), -F(signs[i]))])
    for e in dirs:                                                  # hermitian: A_{-e} = A_e^dagger (the basis 1, sigma_j is hermitian)
        me = tuple(-c for c in e)
        for mu in range(4):
            row([((me, mu, 0), ONE), ((e, mu, 0), -ONE)])
            row([((me, mu, 1), ONE), ((e, mu, 1), ONE)])
    for e in dirs:
        me = tuple(-c for c in e)
        for mu in range(4):
            if inversion == "none":
                continue
            if inversion in ("content_reversed_symmetry", "content_reversed_with_motion_reversed"):
                # antiunitary: Theta (c_0 + c.sigma) Theta^-1 = conj(c_0) - conj(c).sigma;  Theta A_{-e} Theta^-1 = -A_e (symmetry) or +A_e
                sgn = -ONE if inversion == "content_reversed_symmetry" else ONE
                flip = ONE if mu == 0 else -ONE
                row([((me, mu, 0), flip), ((e, mu, 0), -sgn)])
                row([((me, mu, 1), -flip), ((e, mu, 1), -sgn)])
            else:
                # unitary, content untouched: A_{-e} = A_e (symmetry) or -A_e (with the motion reversed)
                sgn = ONE if inversion == "content_untouched_symmetry" else -ONE
                row([((me, mu, 0), ONE), ((e, mu, 0), -sgn)])
                row([((me, mu, 1), ONE), ((e, mu, 1), -sgn)])
    return 56 - rank(rows), rows, col


def family_b(checks: Checks) -> None:
    sig = content_matrices()
    two = G(2)
    anti = all(meq(madd(mmul(sig[j], sig[l]), mmul(sig[l], sig[j])), mscale(two if j == l else G(0), IDENT)) for j in range(3) for l in range(3))
    # consequence on the lattice: H^2 = sum_j D_j^2, a scalar: (H^2 delta)(x) = (1/4) sum_j (2 delta - delta_{+2e_j} - delta_{-2e_j}), content untouched
    ok_sq = True
    for s in range(2):
        v = delta((0, 0, 0), s)
        lhs = apply_walk(apply_walk(v, sig=sig), sig=sig)
        rhs: dict = {}
        for e in AXES:
            rhs = vadd(rhs, v, F(2, 4))
            rhs = vadd(rhs, shift(v, tuple(2 * c for c in e)), -F(1, 4))
            rhs = vadd(rhs, shift(v, tuple(-2 * c for c in e)), -F(1, 4))
        ok_sq = ok_sq and veq(lhs, rhs)
    checks.check("B1", anti and ok_sq, "T1: the three content matrices anticommute and square to one, so the walk H = sum_j sigma_j D_j squares to the scalar sum_j D_j^2 (checked on the infinite lattice: H(H delta) touches only the second neighbours along the axes and leaves the content alone): energies +-sqrt(sum_j sin^2 k_j)")
    dims = {name: generator_space(name)[0] for name in ("none", "content_reversed_symmetry", "content_untouched_symmetry", "content_reversed_with_motion_reversed", "content_untouched_with_motion_reversed")}
    # the surviving generator under content_reversed_symmetry is the walk: A_{+-e_j} = +-(i/2) sigma_j, A_0 = 0
    _, rows, col = generator_space("content_reversed_symmetry" if not mut("inversion_leaves_the_content_alone") else "content_untouched_symmetry")
    walk = [ZERO] * 56
    for j, e in enumerate(AXES):
        walk[col[(e, 1 + j, 1)]] = F(1, 2)
        walk[col[(tuple(-c for c in e), 1 + j, 1)]] = -F(1, 2)
    walk_ok = all(sum(a * b for a, b in zip(r, walk)) == 0 for r in rows)
    ok = dims == {"none": 3, "content_reversed_symmetry": 1, "content_untouched_symmetry": 2, "content_reversed_with_motion_reversed": 2, "content_untouched_with_motion_reversed": 1} and walk_ok
    checks.check("B2", ok, f"T1: nearest-neighbour generators sum_e A_e T_e that are hermitian and covariant under the 24 rotations form a real space of dimension {dims['none']} (a_0, a, beta); with lattice inversion a symmetry of the evolution and the content reversed by it (an antiunitary map), dimension {dims['content_reversed_symmetry']}, spanned by the walk A_(+-e_j) = +-(i/2) sigma_j; with the content untouched by inversion, dimension {dims['content_untouched_symmetry']} and the walk is excluded (beta = 0)")
    # no 2x2 matrix anticommutes with all three content matrices; equivalently no unitary (no linear map X . X^-1) reverses all three
    rows = []
    for j in range(3):
        for a in range(2):
            for b in range(2):
                for part in range(2):
                    r = [ZERO] * 8
                    for c in range(2):
                        for (i1, i2, coef) in ((a, c, sig[j][c][b]), (c, b, sig[j][a][c])):       # (X sigma_j)_{ab} + (sigma_j X)_{ab}
                            # entry X_{i1 i2} = xr + i xi, times coef = cr + i ci
                            xr, xi = 2 * (2 * i1 + i2), 2 * (2 * i1 + i2) + 1
                            if part == 0:
                                r[xr] += coef.re
                                r[xi] -= coef.im
                            else:
                                r[xr] += coef.im
                                r[xi] += coef.re
                    rows.append(r)
    rk = rank(rows)
    if mut("a_rest_energy_matrix_exists"):
        rk = 7
    theta_ok = all(meq(mmul(mmul(sig[1], mconj(sig[j])), sig[1]), mscale(G(-1), sig[j])) for j in range(3))
    checks.check("B3", rk == 8 and theta_ok, f"T1: the equations X sigma_j + sigma_j X = 0 (j = 1, 2, 3) have rank {rk} of 8: only X = 0.  So no nonzero 2x2 anticommuting mass matrix preserves the walk square; other modified dispersion gaps are outside this obstruction, and no linear map reverses all three content matrices; the antiunitary map sigma_2 conj(.) sigma_2 does")
    # velocity operator: i [H, X_j] = sigma_j (x) (T_j + T_j^dagger)/2
    ok_v = True
    for s in range(2):
        for j, e in enumerate(AXES):
            site = (2, -1, 3)
            v = delta(site, s)
            hx = apply_walk({k: val * F(k[j]) for k, val in v.items() if k[j] != 0}, sig=sig)
            xh = {k: val * F(k[j]) for k, val in apply_walk(v, sig=sig).items() if k[j] != 0}
            comm = vscale(vadd(hx, xh, -ONE), I_UNIT)
            want: dict = {}
            for sign in (+1, -1):
                tgt = tuple(site[i] + sign * e[i] for i in range(3))
                for s2 in range(2):
                    if not sig[j][s2][s].is_zero():
                        want = vadd(want, {tgt + (s2,): sig[j][s2][s] * F(1, 2)}, ONE)
            ok_v = ok_v and veq(comm, want)
    checks.check("B4", ok_v, "T1: the velocity operator of the walk is i[H, X_j] = sigma_j (T_j + T_j^dagger)/2: at long wavelength the velocity IS the content (block 44's 'content = direction of travel' is its expectation value), and the limiting speed is one site per unit time")


# ============================================================================================ family C
def torus_matrices(side, w):
    sites = list(product(range(side), repeat=3))
    idx = {(x, s): 2 * i + s for i, x in enumerate(sites) for s in range(2)}
    n = 2 * len(sites)
    sig = content_matrices()
    h = [[G(0)] * n for _ in range(n)]
    for x in sites:
        for j, e in enumerate(AXES):
            for sign in (+1, -1):
                tgt = tuple((x[i] + sign * e[i]) % side for i in range(3))
                for s in range(2):
                    for s2 in range(2):
                        h[idx[(tgt, s2)]][idx[(x, s)]] = h[idx[(tgt, s2)]][idx[(x, s)]] + sig[j][s2][s] * HALF_I * F(sign)
    return sites, idx, n, h


def family_c(checks: Checks) -> None:
    side = 3
    root = {x: ONE + F((3 * x[0] + 5 * x[1] + 7 * x[2]) % 11, 13) for x in product(range(side), repeat=3)}          # sqrt(w), rational
    w = {x: r * r for x, r in root.items()}
    sites, idx, n, h = torus_matrices(side, w)
    wt = [w[x] for x in sites for _ in range(2)]
    rt = [root[x] for x in sites for _ in range(2)]
    herm = all(h[a][b] == h[b][a].conj() for a in range(n) for b in range(n))
    gen = [[h[a][b] * wt[a] for b in range(n)] for a in range(n)]                     # the clause's generator w H
    # self-adjoint for <phi, psi>_w = sum conj(phi) psi / w  <=>  conj(gen[b][a]) / w_b = gen[a][b] / w_a
    if mut("inner_product_without_the_clock_weight"):
        self_adj = all(gen[a][b] == gen[b][a].conj() for a in range(n) for b in range(n))
    else:
        self_adj = all(gen[b][a].conj() * (1 / wt[b]) == gen[a][b] * (1 / wt[a]) for a in range(n) for b in range(n))
    plain = all(gen[a][b] == gen[b][a].conj() for a in range(n) for b in range(n))
    checks.check("C1", herm and self_adj and not plain, "T2: on the 3x3x3 torus with a rational rate field, the clause's generator w H is self-adjoint for the inner product sum_x conj(phi_x) psi_x / w_x and NOT for the plain one: the conserved quantity of an amplitude timed by local clocks is sum_x |psi_x|^2 / w_x")
    sym = [[h[a][b] * (rt[a] * rt[b]) for b in range(n)] for a in range(n)]
    similar = all(gen[a][b] * (rt[b] / rt[a]) == sym[a][b] for a in range(n) for b in range(n))
    sym_herm = all(sym[a][b] == sym[b][a].conj() for a in range(n) for b in range(n))
    sender = [[h[a][b] * wt[b] for b in range(n)] for a in range(n)]                  # timed by the sending site: H w
    similar_sender = all(sender[a][b] * (rt[a] / rt[b]) == sym[a][b] for a in range(n) for b in range(n))
    checks.check("C2", similar and sym_herm and similar_sender, "T2: w^(-1/2) (w H) w^(1/2) = sqrt(w) H sqrt(w) =: H_w, hermitian: every bond carries the amplitude sqrt(w_x w_y); chi = psi / sqrt(w) is the variable with the plain norm; timing by the sending site, H w, is similar to the same H_w (conserved sum |psi|^2 w): the three timings differ by which variable is called the amplitude, not in the motion")
    t, root_t = F(49, 9), F(7, 3)                                          # the unit of rate changed by t = (7/3)^2
    degree = 2 if mut("bond_timing_of_degree_two") else 1
    scaled_ok = True
    for x in sites:
        for e in E6:
            y = tuple((x[i] + e[i]) % side for i in range(3))
            symmetrized = (root_t * root[x]) * (root_t * root[y]) == t * (root[x] * root[y])
            if degree == 2:
                other = (t * w[x]) * (t * w[y]) == t * (w[x] * w[y])
            else:
                other = (t * w[x] + t * w[y]) / 2 == t * ((w[x] + w[y]) / 2)
            scaled_ok = scaled_ok and symmetrized and other
    checks.check("C3", scaled_ok, "T2: multiplying every rate by t multiplies H_w by t (the bond amplitude sqrt(w_x w_y), like any bond timing of degree one such as (w_x + w_y)/2, scales by t): a change of the unit of time and nothing else, as 'only ratios of rates mean anything' demands")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    sig = content_matrices()
    # w(x) = 9^x1 4^x3: sqrt(w) = 3^x1 2^x3, rational; a uniform gradient of log w
    if mut("rate_field_not_exponential"):
        sqrt_w = lambda x: F(1 + x[2] * x[2])
    else:
        sqrt_w = lambda x: F(3) ** x[0] * F(2) ** x[2]
    lam = lambda a: F(9) ** a[0] * F(4) ** a[2]
    ok1 = True
    ok_pow = True
    for site in ((0, 0, 0), (1, -2, 3), (-2, 1, -1)):
        for s in range(2):
            v = delta(site, s)
            for a in ((0, 0, 1), (1, 0, 0), (1, -2, 1), (0, 3, 0)):
                factor = lam(a) if not mut("clock_ratio_inverted") else 1 / lam(a)
                left = apply_walk(shift(v, a), sqrt_w=sqrt_w, sig=sig)
                right = vscale(shift(apply_walk(v, sqrt_w=sqrt_w, sig=sig), a), G(factor))
                ok1 = ok1 and veq(left, right)
                l2 = apply_walk(apply_walk(apply_walk(shift(v, a), sqrt_w=sqrt_w, sig=sig), sqrt_w=sqrt_w, sig=sig), sqrt_w=sqrt_w, sig=sig)
                r2 = vscale(shift(apply_walk(apply_walk(apply_walk(v, sqrt_w=sqrt_w, sig=sig), sqrt_w=sqrt_w, sig=sig), sqrt_w=sqrt_w, sig=sig), a), G(factor ** 3))
                ok_pow = ok_pow and veq(l2, r2)
    checks.check("D1", ok1, "T3: in a uniform gradient, w(x + a) = lambda_a w(x) (here w = 9^x1 4^x3), H_w T_a = lambda_a T_a H_w exactly on the infinite lattice, for shifts along, across and oblique to the gradient")
    checks.check("D2", ok_pow, "T3: the third-power translation identity holds on the tested finite-support states; this does not establish global time evolution or a universal packet phase rate")
    w_of = lambda x: F(9) ** x[0] * F(4) ** x[2]
    mean_bond = lambda x, y: (w_of(x) + w_of(y)) / 2
    ok3 = True
    for s in range(2):
        v = delta((1, 0, -1), s)
        for a in ((0, 0, 1), (1, -2, 1)):
            left = apply_walk(shift(v, a), bond=mean_bond, sig=sig)
            right = vscale(shift(apply_walk(v, bond=mean_bond, sig=sig), a), G(lam(a)))
            ok3 = ok3 and veq(left, right)
    checks.check("D3", ok3, "T3: the identity holds for the bond timing (w_x + w_y)/2 too: it rests on the degree-one scaling of the timing, not on the symmetrization chosen")
    # a rate field that is not exponential: H_w T_a delta is not a multiple of T_a H_w delta
    quad = lambda x: F(1 + x[2] * x[2])
    v = delta((0, 0, 1), 0)
    left = apply_walk(shift(v, (0, 0, 1)), sqrt_w=quad, sig=sig)
    right = shift(apply_walk(v, sqrt_w=quad, sig=sig), (0, 0, 1))
    ratios = set()
    for key in left:
        a, b = left[key], right.get(key, G(0))
        num = a * b.conj()
        den = (b * b.conj()).re
        ratios.add((num.re / den, num.im / den) if den != 0 else None)
    checks.check("D4", set(left) == set(right) and len(ratios) > 1, f"T3 (control): for sqrt(w) = 1 + x3^2 the two sides differ by site-dependent factors {sorted(r[0] for r in ratios if r)}: no time rescaling relates a packet to its translate; the exact identity is a property of uniform gradients")

    # A finite-support counterexample to replacing <T H>/<T> by <H>.
    xs=list(range(-4,5));v=[F({0:1,1:2,2:3}.get(x,0)) for x in xs]
    h=[[F(0) for _ in xs] for _ in xs];t=[[F(0) for _ in xs] for _ in xs]
    for j,x in enumerate(xs[:-1]):
        h[j+1][j]=h[j][j+1]=F(2)**(2*x+1);t[j+1][j]=1
    def mv(a,b):return [sum((c*d for c,d in zip(row,b)),F(0)) for row in a]
    def dot(a,b):return sum((c*d for c,d in zip(a,b)),F(0))
    norm=dot(v,v);tv=mv(t,v);hv=mv(h,v);htv=mv(h,tv);thv=mv(t,hv)
    phase=dot(v,[a-b for a,b in zip(htv,thv)])/dot(v,tv)
    energy=dot(v,hv)/norm
    checks.check("D5",htv==[4*y for y in thv] and dot(v,tv)/norm==F(4,7) and energy==F(52,7) and phase==F(519,16) and phase!=3*energy,"T3: exact local intertwining coexists with phase rate519/16 versus3*mean-energy156/7; arbitrary packet phase does not follow the claimed universal force")


# ============================================================================================ family E
class Jet:
    """Value, gradient and matrix of second derivatives of a function of three variables, in exact arithmetic."""

    def __init__(self, val, grad=None, hess=None):
        self.val = F(val)
        self.grad = [F(g) for g in (grad or [0, 0, 0])]
        self.hess = [[F(c) for c in row] for row in (hess or [[0] * 3 for _ in range(3)])]

    def __add__(self, o):
        o = o if isinstance(o, Jet) else Jet(o)
        return Jet(self.val + o.val, [a + b for a, b in zip(self.grad, o.grad)], [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(self.hess, o.hess)])

    __radd__ = __add__

    def __mul__(self, o):
        o = o if isinstance(o, Jet) else Jet(o)
        grad = [self.val * o.grad[i] + o.val * self.grad[i] for i in range(3)]
        hess = [[self.val * o.hess[i][j] + o.val * self.hess[i][j] + self.grad[i] * o.grad[j] + self.grad[j] * o.grad[i] for j in range(3)] for i in range(3)]
        return Jet(self.val * o.val, grad, hess)

    __rmul__ = __mul__

    def sqrt(self, root):
        root = F(root)
        assert root * root == self.val and root > 0
        grad = [g / (2 * root) for g in self.grad]
        hess = [[self.hess[i][j] / (2 * root) - self.grad[i] * self.grad[j] / (4 * root ** 3) for j in range(3)] for i in range(3)]
        return Jet(root, grad, hess)


def sin_cos_jets(sines, cosines):
    s_j, c_j = [], []
    for i in range(3):
        gs = [ZERO] * 3; gs[i] = cosines[i]
        hs = [[ZERO] * 3 for _ in range(3)]; hs[i][i] = -sines[i]
        gc = [ZERO] * 3; gc[i] = -sines[i]
        hc = [[ZERO] * 3 for _ in range(3)]; hc[i][i] = -cosines[i]
        s_j.append(Jet(sines[i], gs, hs)); c_j.append(Jet(cosines[i], gc, hc))
    return s_j, c_j


def ray_acceleration(eps: Jet, w, grad_u):
    """dv_j/dt from the ray equations of E = w(x) eps(k):  v_j = w d_j eps,  dx/dt = w d eps,  dk/dt = -eps w grad u."""
    v = [w * eps.grad[j] for j in range(3)]
    acc = []
    for j in range(3):
        a = ZERO
        for l in range(3):
            a += (w * grad_u[l] * eps.grad[j]) * (w * eps.grad[l])          # d v_j / d x_l  times  dx_l/dt
            a += (w * eps.hess[j][l]) * (-eps.val * w * grad_u[l])          # d v_j / d k_l  times  dk_l/dt
        acc.append(a)
    return v, acc


def family_e(checks: Checks) -> None:
    # rational points of the walk's energy surface: sin k_j, cos k_j and eps = sqrt(m^2 + sum sin^2) all rational
    points = [                                                          # (sines, cosines, rest energy, eps)
        ((F(3, 5), ZERO, ZERO), (F(4, 5), ONE, ONE), F(4, 5), ONE),
        ((F(3, 5), F(4, 5), ZERO), (F(4, 5), -F(3, 5), ONE), ZERO, ONE),
        ((F(3, 5), F(4, 5), ZERO), (-F(4, 5), F(3, 5), ONE), F(3, 4), F(5, 4)),
        ((F(4, 5), F(4, 5), F(3, 5)), (F(3, 5), -F(3, 5), F(4, 5)), F(4), F(21, 5)),
        ((F(8, 17), F(15, 17), F(4, 5)), (F(15, 17), F(8, 17), -F(3, 5)), F(4), F(21, 5)),
        ((F(5, 13), F(12, 13), ZERO), (F(12, 13), F(5, 13), -ONE), F(4, 3), F(5, 3)),
    ]
    w = F(3, 2)
    grad_u = (F(1, 50), -F(3, 100), F(1, 20))
    ok, used = True, 0
    for sines, cosines, m, eps_root in points:
        if any(sines[j] ** 2 + cosines[j] ** 2 != 1 for j in range(3)) or eps_root * eps_root != m * m + sum(s * s for s in sines):
            ok = False
            continue
        s_j, c_j = sin_cos_jets(sines, cosines)
        f_jet = Jet(m * m)
        for j in range(3):
            f_jet = f_jet + s_j[j] * s_j[j]
        eps = f_jet.sqrt(eps_root)
        v, acc = ray_acceleration(eps, w, grad_u)
        v_dot_g = sum(v[l] * grad_u[l] for l in range(3))
        for j in range(3):
            cos2 = cosines[j] ** 2 - sines[j] ** 2
            if mut("lattice_factor_dropped"):
                cos2 = ONE
            law = -w * w * cos2 * grad_u[j] + (ZERO if mut("fall_without_the_velocity_term") else 2 * v_dot_g * v[j])
            ok = ok and acc[j] == law
        used += 1
    checks.check("E1", ok and used == 6, f"T4: at {used} rational points of the walk's energy surface (with and without rest energy, a general gradient, both signs of the group velocity) the ray equations of E = w(x) eps(k) give exactly dv_j/dt = -w^2 cos(2 k_j) d_j u + 2 (v . grad u) v_j: the rest energy and the energy do not appear")
    # at rest along the gradient axis: the fall is -w^2 g whatever the rest energy, even at large transverse wave vector
    falls = set()
    for sx, cx in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(24, 25), F(7, 25)), (F(8, 17), -F(15, 17))):
        s_j, c_j = sin_cos_jets((sx, ZERO, ZERO), (cx, ONE, ONE))
        f_jet = s_j[0] * s_j[0] + s_j[1] * s_j[1] + s_j[2] * s_j[2]
        eps = f_jet.sqrt(sx)
        _, acc = ray_acceleration(eps, w, (ZERO, ZERO, F(1, 20)))
        falls.add((acc[0], acc[1], acc[2]))
    checks.check("E2", falls == {(ZERO, ZERO, -w * w * F(1, 20))}, f"T4: a ray with no motion along an axis gradient falls at exactly -w^2 g for transverse 'rest energies' 3/5, 5/13, 24/25, 8/17 alike ({len(falls)} distinct value): bodies of different energy fall together")
    # long-wavelength dispersion eps = sqrt(m^2 + k^2): second derivatives of eps^2/2 are the unit matrix; along the gradient the sign changes at v = w/sqrt 2
    outs = []
    for kz, m, root in ((F(3), F(4), F(5)), (F(4), F(3), F(5))):
        kj = [Jet(0, [1, 0, 0]), Jet(0, [0, 1, 0]), Jet(kz, [0, 0, 1])]
        f_jet = Jet(m * m) + kj[0] * kj[0] + kj[1] * kj[1] + kj[2] * kj[2]
        unit = all(f_jet.hess[i][j] == (2 if i == j else 0) for i in range(3) for j in range(3))
        eps = f_jet.sqrt(root)
        g = F(1, 20)
        v, acc = ray_acceleration(eps, ONE, (ZERO, ZERO, g))
        outs.append((v[2], acc[2] / g, unit))
    checks.check("E3", outs == [(F(3, 5), -F(7, 25), True), (F(4, 5), F(7, 25), True)], "T4: for eps^2 = m^2 + k^2 the second derivatives of eps^2/2 form the unit matrix and dv/dt = -w^2 grad u + 2 (v . grad u) v: along the gradient a ray at 3/5 of the limiting speed is accelerated by -(7/25) g, at 4/5 by +(7/25) g; the sign changes at v = w/sqrt 2")
    # a constant e_0 added to the energy breaks universality: transverse fall -g (1 + e_0/|k|)
    e0 = F(1, 2)
    kj = [Jet(F(3, 10), [1, 0, 0]), Jet(F(4, 10), [0, 1, 0]), Jet(0, [0, 0, 1])]
    f_jet = kj[0] * kj[0] + kj[1] * kj[1] + kj[2] * kj[2]
    eps = f_jet.sqrt(F(1, 2)) + Jet(e0)
    g = F(1, 20)
    _, acc = ray_acceleration(eps, ONE, (ZERO, ZERO, g))
    factor = acc[2] / (-g)
    want = ONE if mut("energy_offset_is_harmless") else ONE + e0 / F(1, 2)
    checks.check("E4", factor == want and factor == 2, f"T4: with a constant e_0 = 1/2 added to the energy (the term a_0 + 6a of T1's family), a transverse ray of wave number 1/2 falls {factor} times faster than -g: the fall would depend on the wave number as 1 + e_0/|k|; universality needs the walk's spectrum to pass through zero energy at zero wave vector")


    # a walker whose content does not couple to its motion (beta = 0): eps = e_0 + k^2/(2M); weight e_0 and inertia M are two separate numbers
    ratios = []
    for e0, big_m in ((F(3), F(2)), (F(1), F(1)), (F(1, 2), F(5))):
        kj = [Jet(0, [1, 0, 0]), Jet(0, [0, 1, 0]), Jet(0, [0, 0, 1])]
        eps = Jet(e0) + (kj[0] * kj[0] + kj[1] * kj[1] + kj[2] * kj[2]) * (1 / (2 * big_m))
        g = F(1, 20)
        _, acc = ray_acceleration(eps, ONE, (ZERO, ZERO, g))
        ratios.append(acc[2] / (-g))
    checks.check("E5", ratios == [F(3, 2), F(1), F(1, 10)], f"T4: for the generator with beta = 0 (content not coupled to motion), eps = e_0 + k^2/(2M), a ray at rest falls at (e_0/M) times -g: {ratios[0]}, {ratios[1]}, {ratios[2]} for (e_0, M) = (3, 2), (1, 1), (1/2, 5); weight and inertia are two separate numbers there, while the normalized continuum ray dispersion gives a fixed coefficient for transverse/rest rays")


# ============================================================================================ family F
FENCES = (
    "This note works within a supplied clause for an amplitude whose phase is timed by local tick rates; it reports how such an amplitude moves in a given rate field; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Rindler", "Bloch", "Berry", "Hesse", "Schrodinger", "Liouville", "Lorentz", "Kramers", "Wilson", "Eotvos", "Shapiro")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Weyl)", 1)
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
    "per_element: executed — the three content matrices' products; the 24 rotations acting on the 56 real coefficients of a nearest-neighbour generator, with each of the four behaviours under inversion; the eight real equations for a matrix anticommuting with all three content matrices",
    "per_site: executed — the walk, its square and its velocity operator applied to single-site amplitudes on the infinite lattice; the translation identity at three sites, four shifts and two contents, with its third power",
    "per_mode: executed — the ray equations at rational points of the energy surface with exact second-order jets: the walk with and without rest energy, the long-wavelength dispersion at 3/5 and 4/5 of the limiting speed, an energy offset",
    "per_block: executed — the clocked generator on the 3x3x3 torus with a rational rate field: self-adjointness for the weighted inner product and not for the plain one, similarity to the symmetrized form, scaling of the bond timing",
    "lattice_wide: T1 is a statement about every translation-invariant, hermitian, rotation-covariant nearest-neighbour generator on two-component amplitudes; T2 for finite Hermitian matrices and fixed positive rate fields; T3 is finite-support polynomial algebra, with a counterexample to universal packet force; T4 about rays of any energy function of the form w(x) eps(k); the passage from the walk to its rays is executed in the controls, not proved; the clause itself, the rate field, the formation of records from the amplitude and any rest energy of one walker are not derived",
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
    print("scope: supplied nearest-neighbour amplitude models; generator classification, fixed-rate weighted matrices, finite-support translation algebra and an exact counterexample to universal packet phase; separate conditional ray identities")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
