#!/usr/bin/env python3
"""Independent referee for deferred-20260926-quantum-record-codes-and-pointers a1.

The depolarized pointer's generator entries are recomputed from the stencil.
The attempt's script is not imported. The random single-site search is not repeated.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def cross(left, right):
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


LABELS = []
for axis in range(3):
    for sign in (1, -1):
        direction = [0, 0, 0]
        direction[axis] = sign
        LABELS.append(("A", tuple(direction), (0, 0, 0)))
for block in itertools.product((1, -1), repeat=3):
    LABELS.append(("B", (0, 0, 0), block))
ROUTES = ((-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
RATE = F(11, 10)


def coupling(route):
    matrix = []
    for left in range(14):
        row = []
        for right in range(14):
            spin = cross(LABELS[left][1], LABELS[right][2])
            other = cross(LABELS[right][1], LABELS[left][2])
            row.append(F(1, 2) * dot(route, tuple(a + b for a, b in zip(spin, other))))
        matrix.append(row)
    return matrix


COUPLINGS = {route: coupling(route) for route in ROUTES}
symmetric = all(
    COUPLINGS[route][i][j] == COUPLINGS[route][j][i] and COUPLINGS[route][i][i] == 0
    for route in ROUTES
    for i in range(14)
    for j in range(14)
)
balanced = all(sum(row) == 0 for route in ROUTES for row in COUPLINGS[route])
bounded = all(abs(COUPLINGS[route][i][j]) <= F(1, 2) for route in ROUTES for i in range(14) for j in range(14))
check("R1 couplings", symmetric and balanced and bounded, "every route matrix is symmetric, zero on the diagonal, zero in each row, and at most 1/2")


def find(kind, direction, block):
    return LABELS.index((kind, direction, block))


colour_a = find("A", (0, 1, 0), (0, 0, 0))
colour_b = find("B", (0, 0, 0), (-1, -1, -1))
colour_c = find("B", (0, 0, 0), (1, -1, -1))
back = COUPLINGS[(-1, 0, 0)]
check(
    "R1 colours",
    back[colour_a][colour_b] == F(1, 2) and back[colour_a][colour_c] == F(1, 2),
    "S(-e1) is 1/2 on both of the author's colour pairs",
)

noise = sp.symbols("eta", positive=True)
remain, mix = 1 - noise, noise / 14
prepared = sp.Matrix(14, 14, lambda i, j: (remain if i == j else 0) + mix)
inverse = sp.Matrix(14, 14, lambda i, j: ((1 if i == j else 0) - mix) / remain)
check(
    "R2 inverse",
    sp.simplify(prepared * inverse - sp.eye(14)) == sp.zeros(14) and sp.simplify(remain + 14 * mix - 1) == 0,
    "B^{-1} = (I - q 11^T)/r with r + 14 q = 1",
)


def pair_weight(left_matrix, right_matrix, values, left, right, source, target):
    left_row = [left_matrix[left][colour] * right_matrix[colour][source] for colour in range(14)]
    right_row = [left_matrix[right][colour] * right_matrix[colour][target] for colour in range(14)]
    return sum(
        left_row[i] * values[i][j] * right_row[j]
        for i in range(14)
        for j in range(14)
        if values[i][j]
    )


symbolic_coupling = [[sp.Rational(entry.numerator, entry.denominator) for entry in row] for row in back]
symbolic_prepared = [[prepared[i, j] for j in range(14)] for i in range(14)]
symbolic_inverse = [[inverse[i, j] for j in range(14)] for i in range(14)]
pair_ok = True
for left, right in ((colour_a, colour_b), (colour_a, colour_c), (colour_b, colour_c), (0, 13), (3, 9)):
    got = pair_weight(symbolic_prepared, symbolic_inverse, symbolic_coupling, left, right, right, left)
    wanted = mix ** 2 * (1 + remain ** 2) * symbolic_coupling[left][right] / remain ** 2
    pair_ok = pair_ok and sp.simplify(got - wanted) == 0
check("R4 pair", pair_ok, "(K_S)_{ij,ji} = q^2 (1+r^2) S_ij / r^2")


def stencil(left_matrix, right_matrix, values, image, preimage):
    """Image is tested swapped and unswapped; the target tuple stays in slot order (l, c, d, r)."""
    left, centre, other, far = image
    there_left, there_centre, there_other, there_far = preimage

    def same(left_colour, right_colour):
        return 1 if left_colour == right_colour else 0

    total = 0
    arrangements = (
        ((left, other, centre, far), 1),
        ((left, centre, other, far), -1),
    )
    for (here_left, here_centre, here_other, here_far), sign in arrangements:
        total += sign * RATE / 2 * same(here_left, there_left) * same(here_centre, there_centre) * same(here_other, there_other) * same(here_far, there_far)
        total += sign * F(1, 4) * (
            pair_weight(left_matrix, right_matrix, values, here_left, here_centre, there_left, there_centre) * same(here_other, there_other) * same(here_far, there_far)
            + pair_weight(left_matrix, right_matrix, values, here_centre, here_far, there_centre, there_far) * same(here_left, there_left) * same(here_other, there_other)
            - pair_weight(left_matrix, right_matrix, values, here_left, here_other, there_left, there_other) * same(here_centre, there_centre) * same(here_far, there_far)
            - pair_weight(left_matrix, right_matrix, values, here_other, here_far, there_other, there_far) * same(here_left, there_left) * same(here_centre, there_centre)
        )
    return total


spectator = find("A", (0, 0, -1), (0, 0, 0))
author_entry = sp.simplify(
    stencil(symbolic_prepared, symbolic_inverse, symbolic_coupling, (spectator, colour_a, colour_b, colour_c), (spectator, colour_b, colour_c, colour_a))
    + stencil(symbolic_prepared, symbolic_inverse, symbolic_coupling, (colour_a, colour_b, colour_c, spectator), (colour_b, colour_c, colour_a, spectator))
)
author_formula = -noise ** 2 * (1 + (1 - noise) ** 2) / (784 * (1 - noise) ** 2)
check("R4 entry", sp.simplify(author_entry - author_formula) == 0, "the author's off-diagonal is -eta^2 [1+(1-eta)^2] / [784 (1-eta)^2]")

side = 12
even_sites = [site for site in itertools.product(range(side), repeat=3) if sum(site) % 2 == 0]


def shift(site, step, scale=1):
    return tuple((site[i] + scale * step[i]) % side for i in range(3))


stencils = []
for route in ROUTES:
    offset = tuple(route[i] - (1, 0, 0)[i] for i in range(3))
    for site in even_sites:
        stencils.append((route, (shift(site, offset, -1), site, shift(site, offset), shift(site, offset, 2))))
origin, first, second = (0, 0, 0), (10, 0, 0), (8, 0, 0)
containing = [places for _route, places in stencils if {origin, first, second} <= set(places)]
check(
    "R3 stencils",
    len(even_sites) == 864
    and len(stencils) == 4320
    and all(len(set(places)) == 4 for _route, places in stencils)
    and sorted(containing) == sorted((((2, 0, 0), origin, first, second), (origin, first, second, (6, 0, 0)))),
    "864 even sites, 4320 routes, and exactly two stencils hold the three consecutive sites",
)


def matrices(value):
    slope, share = 1 - value, value / 14
    forward = [[(slope if i == j else 0) + share for j in range(14)] for i in range(14)]
    backward = [[((1 if i == j else 0) - share) / slope for j in range(14)] for i in range(14)]
    return forward, backward


def generator_entry(value, image, preimage, background):
    forward, backward = matrices(value)
    differ = {site for site in set(image) | set(preimage) if image.get(site, background) != preimage.get(site, background)}
    total = F(0)
    for route, places in stencils:
        if differ <= set(places):
            total += stencil(
                forward,
                backward,
                COUPLINGS[route],
                tuple(image.get(site, background) for site in places),
                tuple(preimage.get(site, background) for site in places),
            )
    return total


author_colours_image = {origin: colour_a, first: colour_b, second: colour_c}
author_colours_preimage = {origin: colour_b, first: colour_c, second: colour_a}
torus_author = True
for value in (F(1, 2), F(1, 5), F(9, 10)):
    got = generator_entry(value, author_colours_image, author_colours_preimage, 7)
    wanted = -value ** 2 * (1 + (1 - value) ** 2) / (784 * (1 - value) ** 2)
    torus_author = torus_author and got == wanted
check("R5 torus", torus_author, "the author's entry on the full torus matches the closed form at 1/2, 1/5 and 9/10")

plus = find("A", (0, 1, 0), (0, 0, 0))
minus = find("A", (0, -1, 0), (0, 0, 0))
up = find("B", (0, 0, 0), (1, 1, 1))
down = find("B", (0, 0, 0), (1, 1, -1))
new_entry = sp.simplify(
    stencil(symbolic_prepared, symbolic_inverse, symbolic_coupling, (spectator, minus, down, up), (spectator, plus, up, down))
    + stencil(symbolic_prepared, symbolic_inverse, symbolic_coupling, (minus, down, up, spectator), (plus, up, down, spectator))
)
new_formula = noise * (noise - 2) * (noise ** 2 - 14 * noise + 14) / (784 * (1 - noise) ** 2)
series = sp.series(new_formula, noise, 0, 3).removeO()
roots = sp.solve(noise ** 2 - 14 * noise + 14, noise)
root_gap = sp.simplify((roots[0] - 1) * (roots[1] - 1))
check(
    "N formula",
    sp.simplify(new_entry - new_formula) == 0
    and sp.simplify(series + noise / 28 + noise ** 2 / 56) == 0
    and sp.simplify(root_gap - (6 - sp.sqrt(35)) * (6 + sp.sqrt(35))) == 0
    and sp.Integer(35) < 36,
    "the new entry is eta(eta-2)(eta^2-14 eta+14)/[784(1-eta)^2] = -eta/28 - eta^2/56, and both roots lie above 1",
)
new_image = {origin: minus, first: down, second: up}
new_preimage = {origin: plus, first: up, second: down}
torus_new = True
for value in (F(1, 2), F(1, 5), F(1, 100)):
    got = generator_entry(value, new_image, new_preimage, 7)
    wanted = value * (value - 2) * (value ** 2 - 14 * value + 14) / (784 * (value - 1) ** 2)
    torus_new = torus_new and got == wanted
check(
    "N torus",
    torus_new and generator_entry(F(1, 2), new_image, new_preimage, 7) == F(-87, 3136),
    "the new witness matches on the torus, and equals -87/3136 at eta = 1/2",
)


def propagate(value, values, image, preimage):
    forward, backward = matrices(value)
    weight = {}
    columns = [[backward[colour][preimage[slot]] for colour in range(14)] for slot in range(4)]
    for state in itertools.product(range(14), repeat=4):
        amplitude = columns[0][state[0]] * columns[1][state[1]] * columns[2][state[2]] * columns[3][state[3]]
        if amplitude:
            weight[state] = amplitude
    flowed = {}
    for state, amplitude in weight.items():
        if state[1] == state[2]:
            continue
        left, centre, right, far = state
        field = values[left][centre] + values[centre][far] - values[left][right] - values[right][far]
        rate = RATE / 2 + field / 4
        swapped = (left, right, centre, far)
        flowed[swapped] = flowed.get(swapped, 0) + rate * amplitude
        flowed[state] = flowed.get(state, 0) - rate * amplitude
    return sum(
        forward[image[0]][state[0]] * forward[image[1]][state[1]] * forward[image[2]][state[2]] * forward[image[3]][state[3]] * amplitude
        for state, amplitude in flowed.items()
    )


half = F(1, 2)
author_flow = propagate(half, back, (spectator, colour_a, colour_b, colour_c), (spectator, colour_b, colour_c, colour_a))
author_flow += propagate(half, back, (colour_a, colour_b, colour_c, spectator), (colour_b, colour_c, colour_a, spectator))
new_flow = propagate(half, back, (spectator, minus, down, up), (spectator, plus, up, down))
new_flow += propagate(half, back, (minus, down, up, spectator), (plus, up, down, spectator))
check(
    "R6 propagation",
    author_flow == F(-5, 3136) and new_flow == F(-87, 3136) and F(87, 5) * F(-5, 3136) == F(-87, 3136),
    "tensor propagation gives -5/3136 and -87/3136, and the new entry is 87/5 times the author's",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed, and sharpened. The author's generator entry is -eta^2 [1+(1-eta)^2] / [784 (1-eta)^2] for every eta. "
    "A second entry, eta(eta-2)(eta^2-14 eta+14) / [784 (1-eta)^2], equals -eta/28 - eta^2/56 and is negative for every "
    "0 < eta < 1, since the quadratic roots 7 ± sqrt(35) both lie above 1. At eta = 1/2 it is -87/3136. Any positive "
    "implementation is therefore at least eta/28 - O(eta^2) away in the sup-entry distance. The random single-site search "
    "was not repeated.",
    flush=True,
)
print(
    "HIT: confirmed - the depolarized pointer's required generator is already negative at order eta, so no positive "
    "implementation matches it through order eta^2",
    flush=True,
)
