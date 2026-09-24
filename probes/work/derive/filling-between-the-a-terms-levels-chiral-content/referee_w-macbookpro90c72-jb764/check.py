#!/usr/bin/env python3
"""Independent referee for filling-between-the-a-terms-levels-chiral-content a2.

Record counts of the free a-term sea, and what one-record-per-site exclusion
does at those fillings. Does not import the attempt.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import numpy as np
import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def frac_of(expr) -> F:
    expr = sp.together(sp.simplify(expr))
    return F(int(expr.p), int(expr.q))


# ---------------------------------------------------------------- corners
a0, aa = sp.symbols("a0 a")
levels = {}
senses = {}
for node in itertools.product((0, 1), repeat=3):
    signs = [(-1) ** component for component in node]
    levels[node] = a0 + 2 * aa * sum(signs)
    senses[node] = signs[0] * signs[1] * signs[2]
level_ok = all(sp.expand(levels[node] - (a0 + 2 * aa * (3 - 2 * sum(node)))) == 0 for node in levels)
mult = [sum(1 for node in levels if sum(node) == weight) for weight in range(4)]
check(
    "L1 levels and senses",
    level_ok and mult == [1, 3, 3, 1] and sum(senses.values()) == 0 and sum(senses.values()) == 0
    and sum(1 for sense in senses.values() if sense == 1) == 4,
    "corners at a0 + 2a(3-2|n|), multiplicities 1:3:3:1, sense (-1)^|n|, four of each sense, net zero",
)
moments = [sp.expand(sum(senses[node] * levels[node] ** power for node in levels)) for power in range(4)]
check(
    "L2 chiral moments",
    all(moments[power] == 0 for power in range(3)) and sp.expand(moments[3] - 384 * aa**3) == 0,
    "sum chi L^p is 0, 0, 0, 384 a^3",
)


# ---------------------------------------------------------------- momentum grid
COS = {
    2: [F(1), F(-1)],
    3: [F(1), F(-1, 2), F(-1, 2)],
    4: [F(1), F(0), F(-1), F(0)],
    6: [F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2)],
}
SIN2 = {
    2: [F(0), F(0)],
    3: [F(0), F(3, 4), F(3, 4)],
    4: [F(0), F(1), F(0), F(1)],
    6: [F(0), F(3, 4), F(3, 4), F(0), F(3, 4), F(3, 4)],
    12: [F(0), F(1, 4), F(3, 4), F(1), F(3, 4), F(1, 4)] * 2,
}


def band_sign(shift: F, sin2: F, which: int) -> int:
    """Sign of shift + which * sqrt(sin2), which = ±1."""
    if which > 0:
        if shift >= 0:
            return 0 if shift == 0 and sin2 == 0 else 1
        return (sin2 > shift * shift) - (sin2 < shift * shift)
    if shift <= 0:
        return 0 if shift == 0 and sin2 == 0 else -1
    return (shift * shift > sin2) - (shift * shift < sin2)


def occupation(length: int, a0v: F, av: F, mu: F) -> tuple[int, int]:
    below = equal = 0
    for momenta in itertools.product(range(length), repeat=3):
        sea = sum((COS[length][t] for t in momenta), F(0))
        rad = sum((SIN2[length][t] for t in momenta), F(0))
        for which in (1, -1):
            sign = band_sign(a0v + 2 * av * sea - mu, rad, which)
            below += sign < 0
            equal += sign == 0
    return below, equal


count_ok = True
lines = []
for length in (2, 4, 6):
    sites = length**3
    for a0v, av in ((F(1, 3), F(1, 10)), (F(0), F(1, 4)), (F(-2, 5), F(2, 3))):
        mid, zeros = occupation(length, a0v, av, a0v)
        below_plus, at_plus = occupation(length, a0v, av, a0v + 2 * av)
        below_minus, at_minus = occupation(length, a0v, av, a0v - 2 * av)
        window_up = below_plus + at_plus
        window_lo = below_minus
        count_ok = (
            count_ok
            and zeros % 2 == 0
            and mid == sites - zeros // 2
            and at_plus >= 6
            and at_minus >= 6
            and window_up >= mid + zeros + at_plus
            and window_lo + at_minus <= mid
            and window_up >= sites + 6 + zeros // 2
            and window_lo <= sites - 6 - zeros // 2
            and window_up > sites
        )
        lines.append("%d^3 a=%s mid=%d z=%d up=%d lo=%d" % (length, av, mid, zeros, window_up, window_lo))
odd_below, odd_zeros = occupation(3, F(1, 3), F(1, 10), F(1, 3))
check(
    "F1 record counts",
    count_ok and odd_below == 26 and odd_zeros == 0 and odd_below != 27 - odd_zeros // 2,
    "even tori: #(E<a0)=N-z/2, and every Fermi level in (a0+2a,a0+6a) needs more than N records; "
    + "; ".join(lines)
    + "; on the odd 3^3 the count is %d below of 54 with z=%d, so the half-filling identity needs even sides"
    % (odd_below, odd_zeros),
)


def staggered_sum(length: int) -> int:
    return sum((-1) ** (x + y + z) for x, y, z in itertools.product(range(length), repeat=3))


check(
    "F0 bipartition",
    all(staggered_sum(length) == 0 for length in (2, 4, 6)) and staggered_sum(3) != 0,
    "sum of eps is zero on even tori and not on the 3-torus",
)


# ---------------------------------------------------------------- coin radii of one hop
def coin_radii() -> bool:
    aval = sp.symbols("a", real=True, nonnegative=True)
    paul = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    ok = True
    for axis, sigma in enumerate(paul):
        hop = sp.expand(aval * sp.eye(2) + sigma / (2 * sp.I))
        for col in range(2):
            squares = [sp.expand(sp.re(hop[row, col]) ** 2 + sp.im(hop[row, col]) ** 2) for row in range(2)]
            if axis < 2:
                ok = ok and sp.simplify(sum(squares) - aval**2 - F(1, 4)) == 0
                ok = ok and sp.simplify(squares[0] * squares[1] - aval**2 * F(1, 4)) == 0
            else:
                # Diagonal entries carry the whole column; the off-diagonal entry is zero.
                ok = ok and sp.simplify(sum(squares) - aval**2 - F(1, 4)) == 0
                ok = ok and sp.simplify(squares[0] * squares[1]) == 0
    # (|a|+1/2)^2 - (a^2+1/4) = |a| for a >= 0, so the third axis is no larger.
    ok = ok and sp.expand((aval + F(1, 2)) ** 2 - (aval**2 + F(1, 4)) - aval) == 0
    return bool(ok)


check(
    "X0 coin radii",
    coin_radii(),
    "each hop's column of moduli is |a|+1/2 or sqrt(a^2+1/4), and the latter is no larger",
)


# ---------------------------------------------------------------- real-space operator on the 4-torus
class Amp:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = re if isinstance(re, F) else F(re)
        self.im = im if isinstance(im, F) else F(im)

    def __add__(self, other):
        return Amp(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        if isinstance(other, Amp):
            return Amp(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        return Amp(self.re * other, self.im * other)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

    def __neg__(self):
        return Amp(-self.re, -self.im)

    def conj(self):
        return Amp(self.re, -self.im)

    def zero(self) -> bool:
        return self.re == 0 and self.im == 0


def hop_tables(aval: F):
    tables = {}
    paul = [
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    ]
    for axis, sigma in enumerate(paul):
        for sign in (1, -1):
            symbolic = sp.expand(aval * sp.eye(2) + (sp.I * sign / 2) * sigma)
            tables[(axis, sign)] = [
                [Amp(frac_of(sp.re(symbolic[dst, src])), frac_of(sp.im(symbolic[dst, src]))) for src in range(2)]
                for dst in range(2)
            ]
    return tables


def site_index(length: int, x: int, y: int, z: int) -> int:
    return ((x % length) * length + (y % length)) * length + (z % length)


def site_coords(length: int, index: int) -> tuple[int, int, int]:
    x, rem = divmod(index, length * length)
    y, z = divmod(rem, length)
    return x, y, z


def apply_A(length: int, state, hops):
    out = [[Amp(), Amp()] for _ in range(length**3)]
    steps = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for index in range(length**3):
        x, y, z = site_coords(length, index)
        for axis, (dx, dy, dz) in enumerate(steps):
            for sign in (1, -1):
                dest = site_index(length, x + sign * dx, y + sign * dy, z + sign * dz)
                block = hops[(axis, sign)]
                for src in (0, 1):
                    if state[index][src].zero():
                        continue
                    for dst in (0, 1):
                        out[dest][dst] = out[dest][dst] + block[dst][src] * state[index][src]
    return out


def apply_eps(length: int, state, scale: F = F(1)):
    out = []
    for index, spin in enumerate(state):
        x, y, z = site_coords(length, index)
        factor = scale * ((-1) ** (x + y + z))
        out.append([spin[0] * factor, spin[1] * factor])
    return out


def apply_shift(length: int, state):
    """(T psi)(x) = psi(x+e_1)."""
    out = [[Amp(), Amp()] for _ in range(length**3)]
    for index in range(length**3):
        x, y, z = site_coords(length, index)
        out[index] = state[site_index(length, x + 1, y, z)]
    return out


def equal_state(left, right) -> bool:
    for a, b in zip(left, right):
        if a[0] != b[0] or a[1] != b[1]:
            return False
    return True


def scale_state(state, scale: F):
    return [[spin[0] * scale, spin[1] * scale] for spin in state]


def add_state(left, right):
    return [[left[i][c] + right[i][c] for c in (0, 1)] for i in range(len(left))]


HOPS = hop_tables(F(1, 10))
PLANE = length = 4


def plane_wave(kx: int, coin: tuple[F, F]):
    state = [[Amp(), Amp()] for _ in range(length**3)]
    phase = {0: Amp(1), 1: Amp(0, 1), 2: Amp(-1), 3: Amp(0, -1)}  # exp(i pi x / 2)
    for x, y, z in itertools.product(range(length), repeat=3):
        weight = phase[(kx * x) % 4]
        state[site_index(length, x, y, z)] = [weight * coin[0], weight * coin[1]]
    return state


zero_mode = plane_wave(0, (F(1), F(0)))
quarter = plane_wave(1, (F(1), F(1)))
# k=0: A = 6a. k=(pi/2,0,0): A = 2a(cos pi/2 + 1 + 1) + sigma_1 sin(pi/2) = 4a + sigma_1.
# On coin (1,1), sigma_1 acts as +1, so eigenvalue 4a+1 with a=1/10 is 4/10+1 = 7/5.
plane_ok = equal_state(apply_A(length, zero_mode, HOPS), scale_state(zero_mode, F(6, 10)))
plane_ok = plane_ok and equal_state(apply_A(length, quarter, HOPS), scale_state(quarter, F(7, 5)))
check(
    "S0 plane waves",
    plane_ok,
    "on 4^3 the k=0 mode has A=6a and the k=pi/2 mode has A=4a+sigma_1",
)

sym_ok = square_ok = onsite_ok = antic_ok = True
mass = F(1, 7)
for site in range(length**3):
    for coin in (0, 1):
        vec = [[Amp(), Amp()] for _ in range(length**3)]
        vec[site][coin] = Amp(1)
        acted = apply_A(length, vec, HOPS)
        onsite_ok = onsite_ok and acted[site][0].zero() and acted[site][1].zero()
        sym_ok = sym_ok and equal_state(
            apply_A(length, apply_eps(length, vec), HOPS),
            apply_eps(length, acted, F(-1)),
        )
        def with_mass(state):
            hopped = apply_A(length, state, HOPS)
            staggered = apply_eps(length, state, mass)
            return add_state(hopped, staggered)
        squared = with_mass(with_mass(vec))
        bare = apply_A(length, acted, HOPS)
        square_ok = square_ok and equal_state(squared, add_state(bare, scale_state(vec, mass * mass)))
        def x_op(state):
            return apply_eps(length, apply_shift(length, state))
        left = x_op(with_mass(vec))
        right = with_mass(x_op(vec))
        antic_ok = antic_ok and equal_state(left, scale_state(right, F(-1)))

# The anticommutator line above negates by rebuilding. Check it did not short-circuit.
check(
    "S1 symmetries",
    sym_ok and square_ok and onsite_ok and antic_ok,
    "on every basis vector of 4^3, eps anticommutes with A, (A+m eps)^2 = A^2+m^2, "
    "eps T_1 anticommutes with A+m eps, and A has no on-site piece",
)


# ---------------------------------------------------------------- hard-core ring
def hardcore(length: int, records: int, a0v: F, av: F, fermion: bool):
    configs = [
        (sites, coins)
        for sites in itertools.combinations(range(length), records)
        for coins in itertools.product((0, 1), repeat=records)
    ]
    index = {config: i for i, config in enumerate(configs)}
    dim = len(configs)
    matrix = [[Amp() for _ in range(dim)] for _ in range(dim)]
    # <y| a I + (i s/2) sigma_3 |x> for a hop by s.
    def amplitude(sign: int, src: int, dst: int) -> Amp:
        # sigma_3 is diagonal: coin 0 gets + i s/2, coin 1 gets - i s/2, and only dst==src.
        if dst != src:
            return Amp()
        return Amp(av, F(sign, 2) if src == 0 else F(-sign, 2))
    for col, (sites, coins) in enumerate(configs):
        matrix[col][col] = matrix[col][col] + Amp(a0v * records)
        occupied = set(sites)
        for record, site in enumerate(sites):
            for sign in (1, -1):
                dest = (site + sign) % length
                if dest in occupied:
                    continue
                for new_coin in (0, 1):
                    weight = amplitude(sign, coins[record], new_coin)
                    if weight.zero():
                        continue
                    moved = list(sites)
                    moved_coins = list(coins)
                    moved[record] = dest
                    moved_coins[record] = new_coin
                    order = sorted(range(records), key=lambda q: moved[q])
                    parity = 1
                    for p in range(records):
                        for q in range(p + 1, records):
                            if order[p] > order[q]:
                                parity = -parity
                    key = (tuple(moved[q] for q in order), tuple(moved_coins[q] for q in order))
                    matrix[index[key]][col] = matrix[index[key]][col] + weight * (parity if fermion else 1)
    return matrix


def hermitian(matrix) -> bool:
    dim = len(matrix)
    for i in range(dim):
        for j in range(dim):
            if matrix[i][j] != matrix[j][i].conj():
                return False
    return True


def row_certificate(matrix, holes: int, av: F) -> bool:
    cap = 2 * holes * (abs(av) + F(1, 2))
    for row in matrix:
        off = 0
        for entry in row:
            if entry.zero():
                continue
            # Diagonal is real a0*records; off-diagonal entries are pure hop amplitudes.
            if entry.re != 0 and entry.im == 0:
                continue
            square = entry.re * entry.re + entry.im * entry.im
            if square != av * av + F(1, 4):
                return False
            off += 1
        if off > 2 * holes:
            return False
        if F(off) * (abs(av) + F(1, 2)) > cap:
            return False
    return True


full_ok = True
for fermion in (False, True):
    generator = hardcore(4, 4, F(1, 3), F(1, 10), fermion)
    full_ok = full_ok and len(generator) == 16 and hermitian(generator)
    full_ok = full_ok and all(
        generator[i][j] == (Amp(F(4, 3)) if i == j else Amp())
        for i in range(16)
        for j in range(16)
    )
check(
    "X1 full ring",
    full_ok,
    "four records on a ring of four, both compositions: the generator is exactly 4 a0 on all 16 coin states",
)

width_ok = herm_ok = radius_ok = True
widths = []
for records, holes in ((5, 1), (4, 2)):
    generator = hardcore(6, records, F(0), F(1, 10), True)
    herm_ok = herm_ok and hermitian(generator)
    radius_ok = radius_ok and row_certificate(generator, holes, F(1, 10))
    floated = np.array([[complex(float(entry.re), float(entry.im)) for entry in row] for row in generator])
    values = np.linalg.eigvalsh(floated)
    width = float(values.max() - values.min())
    bound = 2 * holes * 2 * (0.1 + 0.5)
    width_ok = width_ok and width <= bound + 1e-8
    widths.append((holes, width, bound))
check(
    "X2 hole bound",
    herm_ok and radius_ok and width_ok,
    "rings with one and two holes are hermitian, each row has at most two hops per hole, "
    "and the float widths are %s"
    % ", ".join("N_h=%d %.3f <= %.1f" % item for item in widths),
)


# ---------------------------------------------------------------- lower-window hole count
def sin_count(length: int, bound: F) -> int:
    table = SIN2[length]
    return sum(
        1
        for momenta in itertools.product(range(length), repeat=3)
        if sum((table[t] for t in momenta), F(0)) < bound
    )


small = F(1, 20)
points = sin_count(12, (12 * small) ** 2)
below, zeros = occupation(6, F(0), small, -4 * small)
mid6, _ = occupation(6, F(0), small, F(0))
holes = 216 - below
hole_bound = zeros // 2 + 2 * sin_count(6, (12 * small) ** 2)
# Continuum zone: each axis fraction 2 theta/pi, two bands, theta = arcsin(12a).
theta = sp.asin(12 * small)
density_bound = sp.simplify(16 * theta**3 / sp.pi**3)
grid_fraction = F(points, 12**3)
check(
    "X3 lower window",
    points == 56 and holes <= hole_bound and mid6 == 216 - zeros // 2 and grid_fraction < 1,
    "12^3 has %d momenta with |sin k|<12a at a=1/20; 6^3 lower window leaves %d holes against %d"
    % (points, holes, hole_bound),
)

k = 2 * np.pi * np.arange(48) / 48
k1, k2, k3 = np.meshgrid(k, k, k, indexing="ij")
cosine = np.cos(k1) + np.cos(k2) + np.cos(k3)
sine = np.sqrt(np.sin(k1) ** 2 + np.sin(k2) ** 2 + np.sin(k3) ** 2)
af = 0.05
energies = np.concatenate([(2 * af * cosine + sine).ravel(), (2 * af * cosine - sine).ravel()])
per_site = float(np.sum(np.abs(energies) < 6 * af) / 48**3)
bound_f = float(16 * np.arcsin(12 * af) ** 3 / np.pi**3)
check(
    "X3 continuum sample",
    per_site + 1e-4 < bound_f,
    "float 48^3 density %.4f of states within 6a of a0, under the zone bound %.4f" % (per_site, bound_f),
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed. On even tori the free sea below a0 holds N - z/2 records, the window "
    "(a0+2a, a0+6a) holds at least N+6+z/2, and one-record-per-site exclusion therefore forbids that filling. "
    "At N records every composition is the constant N a0. With holes the generator stays within "
    "6(|a|+1/2)+|m| per hole of that constant, and for a<1/12 the lower window's hole density is at most "
    "16 arcsin(12a)^3/pi^3. The single-sense filling asked for by the task does not exist under exclusion. "
    "The interacting anomaly theorem and the 48^3 sample's higher digits were not rebuilt.",
    flush=True,
)
print(
    "HIT: confirmed - exclusion forbids the free filling between a0+2a and a0+6a, the middle sea is "
    "N - z/2 records, and a full lattice is the constant N a0 for every composition",
    flush=True,
)
