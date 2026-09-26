#!/usr/bin/env python3
"""Independent referee for formation-price-from-local-data a2.

Green's functions on odd held cubes are recomputed in exact arithmetic.
The attempt's script is not imported.
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


class HeldCube:
    def __init__(self, side):
        self.side = side
        self.interior = side - 2
        self.sites = list(itertools.product(range(1, side - 1), repeat=3))
        self.index = {site: position for position, site in enumerate(self.sites)}
        self.count = len(self.sites)
        self.neighbours = []
        for site in self.sites:
            adjacent = []
            for axis in range(3):
                for step in (1, -1):
                    moved = list(site)
                    moved[axis] += step
                    adjacent.append(self.index.get(tuple(moved)))
            self.neighbours.append(adjacent)
        bandwidth = self.interior * self.interior
        upper = [{position: F(1), **{neighbour: F(-1, 6) for neighbour in self.neighbours[position] if neighbour is not None}} for position in range(self.count)]
        lower = [dict() for _ in range(self.count)]
        for pivot in range(self.count):
            scale = upper[pivot][pivot]
            for row in range(pivot + 1, min(self.count, pivot + bandwidth + 1)):
                factor = upper[row].get(pivot)
                if not factor:
                    continue
                quotient = factor / scale
                lower[row][pivot] = quotient
                for column, value in upper[pivot].items():
                    if column > pivot:
                        upper[row][column] = upper[row].get(column, F(0)) - quotient * value
                del upper[row][pivot]
        self.lower, self.upper = lower, upper
        self.columns = {}

    def solve(self, rhs):
        image = [F(value) for value in rhs]
        for row in range(self.count):
            for column, quotient in self.lower[row].items():
                image[row] -= quotient * image[column]
        solution = [F(0)] * self.count
        for row in range(self.count - 1, -1, -1):
            total = image[row] - sum(value * solution[column] for column, value in self.upper[row].items() if column > row)
            solution[row] = total / self.upper[row][row]
        return solution

    def column(self, site_index):
        if site_index not in self.columns:
            rhs = [F(0)] * self.count
            rhs[site_index] = F(1)
            self.columns[site_index] = self.solve(rhs)
        return self.columns[site_index]

    def apply(self, field):
        return [field[site] - sum(field[neighbour] for neighbour in self.neighbours[site] if neighbour is not None) / 6 for site in range(self.count)]

    def centre(self):
        middle = self.side // 2
        return (middle, middle, middle)


CUBES = {}


def cube(side):
    if side not in CUBES:
        CUBES[side] = HeldCube(side)
    return CUBES[side]


def solve_small(matrix, rhs):
    width = len(matrix)
    augmented = [row[:] + [rhs[index]] for index, row in enumerate(matrix)]
    for column in range(width):
        pivot = next(row for row in range(column, width) if augmented[row][column] != 0)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        augmented[column] = [entry / augmented[column][column] for entry in augmented[column]]
        for row in range(width):
            if row != column and augmented[row][column] != 0:
                factor = augmented[row][column]
                augmented[row] = [entry - factor * other for entry, other in zip(augmented[row], augmented[column])]
    return [augmented[row][width] for row in range(width)]


def resting_field(box, masses, coupling):
    support = sorted(masses)
    columns = {site: box.column(site) for site in support}
    matrix = [[(F(1) if left == right else F(0)) + coupling * columns[right][left] * masses[right] for right in support] for left in support]
    rates = solve_small(matrix, [F(1)] * len(support))
    source = {site: masses[site] * rate for site, rate in zip(support, rates)}
    field = [coupling * sum(columns[site][point] * source[site] for site in support) for point in range(box.count)]
    return field, source


def price(total, green, coupling):
    return total / (1 - coupling * total * green)


def chebyshev(left, right):
    return max(abs(left[axis] - right[axis]) for axis in range(3))


coupling = F(1, 12)
greens = {}
for side in (3, 5, 7, 9):
    box = cube(side)
    centre = box.index[box.centre()]
    greens[side] = box.column(centre)[centre]
check(
    "centre green",
    greens[3] == 1
    and greens[5] == F(22, 17)
    and greens[7] == F(136, 99)
    and greens[9] == F(79271956, 56195761)
    and greens[3] < greens[5] < greens[7] < greens[9],
    "g_yy = 1, 22/17, 136/99, 79271956/56195761",
)

growth_ok = True
for side in (5, 7):
    smaller, larger = cube(side), cube(side + 2)
    small_centre, large_centre = smaller.centre(), larger.centre()
    small_green = smaller.column(smaller.index[small_centre])
    large_green = larger.column(larger.index[large_centre])
    for site in smaller.sites:
        shifted = tuple(coordinate + 1 for coordinate in site)
        if not (large_green[larger.index[shifted]] > small_green[smaller.index[site]]):
            growth_ok = False
prices = {side: F(1) / (1 - coupling * greens[side]) for side in greens}
check(
    "records only",
    growth_ok and len(set(prices.values())) == 4 and prices[3] == F(12, 11),
    "the same central source has four different prices, " + ", ".join(f"{float(prices[side]):.6f}" for side in (3, 5, 7, 9)),
)

ledger_ok = True
box = cube(7)
uniform = {box.index[(x, y, z)]: F(1, 27) for x in (2, 3, 4) for y in (2, 3, 4) for z in (2, 3, 4)}
field, source = resting_field(box, uniform, coupling)
rates = [1 - value for value in field]
ledger = sum(mass * rates[site] for site, mass in uniform.items())
total = sum(source.values())
ledger_ok = ledger == total and all(box.apply(field)[site] + coupling * uniform.get(site, F(0)) * (field[site] - 1) == 0 for site in range(box.count))
site_prices = []
for site in ((2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)):
    index = box.index[site]
    formed = price(ledger, box.column(index)[index], coupling)
    clock = 1 / (1 + coupling * formed * box.column(index)[index])
    post = [coupling * formed * clock * box.column(index)[point] for point in range(box.count)]
    ledger_ok = ledger_ok and formed * clock == ledger and all(box.apply(post)[point] + coupling * (formed if point == index else 0) * (post[point] - 1) == 0 for point in range(box.count))
    site_prices.append(formed)
ledger_ok = ledger_ok and site_prices == sorted(site_prices) and len(set(site_prices)) == 4
ledger_ok = ledger_ok and all(abs(float(value) - target) < 1e-6 for value, target in zip(site_prices, (1.105484, 1.106710, 1.108108, 1.109712)))
for side in (7, 9):
    current = cube(side)
    centre = current.centre()
    index = current.index[centre]
    star = [centre] + [tuple(centre[axis] + (step if direction == axis else 0) for axis in range(3)) for direction in range(3) for step in (1, -1)]
    cross = [centre] + [tuple(centre[axis] + (2 * step if direction == axis else 0) for axis in range(3)) for direction in range(3) for step in (1, -1)]
    for label, points in (("star", star), ("cross", cross)):
        masses = {current.index[point]: F(1, 7) for point in points}
        _field, weights = resting_field(current, masses, coupling)
        formed = price(sum(weights.values()), current.column(index)[index], coupling)
        if label == "star":
            ledger_ok = ledger_ok and formed == F(1188, 1091)
        else:
            ledger_ok = ledger_ok and abs(float(formed) - {7: 1.105773, 9: 1.105054}[side]) < 1e-6
check("ledger", ledger_ok, f"the side-7 cube has ledger {float(ledger):.6f} and four increasing site prices; the star is 1188/1091")

cage_ok = True
for side, radius, amplitude, charge in (
    (7, 0, {(3, 3, 3): F(1, 2)}, F(1, 5)),
    (9, 1, {(4, 4, 4): F(1, 2), (5, 4, 4): F(1, 3)}, F(1, 4)),
    (9, 1, {(4, 4, 4): F(2, 3), (4, 3, 4): F(1, 6), (3, 4, 5): F(1, 5)}, F(-1, 7)),
):
    current = cube(side)
    centre = current.centre()
    index = current.index[centre]
    masses = {current.index[point]: value for point, value in amplitude.items()}
    field, weights = resting_field(current, masses, coupling)
    rates = [1 - value for value in field]
    before = sum(weights.values())
    green = current.column(index)
    shell = [green[point] if chebyshev(current.sites[point], centre) > radius + 1 else F(0) for point in range(current.count)]
    density = current.apply(shell)
    cage_ok = cage_ok and sum(density) == 1
    cage_ok = cage_ok and all(chebyshev(current.sites[point], centre) in (radius + 1, radius + 2) for point in range(current.count) if density[point] != 0)
    updated_rates = [rates[point] - coupling * charge * shell[point] for point in range(current.count)]
    updated = dict(masses)
    for point, value in enumerate(density):
        if value:
            updated[point] = charge * value / updated_rates[point]
    updated_field = [1 - rate for rate in updated_rates]
    cage_ok = cage_ok and all(current.apply(updated_field)[point] + coupling * updated.get(point, F(0)) * (updated_field[point] - 1) == 0 for point in range(current.count))
    window = [point for point in range(current.count) if chebyshev(current.sites[point], centre) <= radius]
    cage_ok = cage_ok and all(rates[point] == updated_rates[point] and masses.get(point, 0) == updated.get(point, 0) for point in window)
    after = sum(updated[point] * updated_rates[point] for point in updated)
    centre_green = green[index]
    cage_ok = cage_ok and after - before == charge and price(before, centre_green, coupling) != price(after, centre_green, coupling)
    slope = F(3, current.interior + 1)
    lower = slope ** 2 / 2 - slope ** 4 / 24
    cage_ok = cage_ok and lower + coupling * min(min(updated.values()), F(0)) > 0
check("cage", cage_ok, "a unit cage outside the window shifts the ledger by c and leaves the window data unchanged")

local_ok = True
for side, centre, total, shape in (
    (7, (3, 3, 3), F(9, 10), {(0, 0, 0): F(-1, 5), (1, 0, 0): F(1, 10), (0, -1, 0): F(1, 20)}),
    (9, (4, 3, 5), F(9, 10), {(0, 0, 0): F(-1, 5), (1, 0, 0): F(1, 10), (0, -1, 0): F(1, 20)}),
    (9, (4, 4, 4), F(3, 4), {(0, 0, 0): F(1, 3), (0, 1, 1): F(-1, 4), (-1, 0, 0): F(1, 6)}),
):
    current = cube(side)
    index = current.index[centre]
    correction = {current.index[tuple(centre[axis] + offset[axis] for axis in range(3))]: value for offset, value in shape.items()}
    excess = {}
    for site, value in correction.items():
        excess[site] = excess.get(site, F(0)) + value
        for neighbour in current.neighbours[site]:
            if neighbour is not None:
                excess[neighbour] = excess.get(neighbour, F(0)) - value / 6
    source = dict(excess)
    source[index] = source.get(index, F(0)) + total
    source = {site: value for site, value in source.items() if value}
    field = current.solve([coupling * source.get(site, F(0)) for site in range(current.count)])
    rates = [1 - value for value in field]
    masses = {site: value / rates[site] for site, value in source.items()}
    checked_field, checked_source = resting_field(current, masses, coupling)
    formed = price(total, current.column(index)[index], coupling)
    local_ok = local_ok and checked_field == field and sum(checked_source.values()) == total
    local_ok = local_ok and total / (rates[index] + coupling * correction[index]) == formed
    local_ok = local_ok and 1 / (1 + coupling * formed * current.column(index)[index]) == rates[index] + coupling * correction[index]
rest_mass, arm_mass, symbol_k, centre_rate, arm_rate = sp.symbols("m0 m1 k a b", positive=True)
ledger_symbol = rest_mass * centre_rate + 6 * arm_mass * arm_rate
constant = rest_mass / (1 + symbol_k * rest_mass) + 6 * arm_mass
star_rule = (ledger_symbol / (centre_rate - 6 * symbol_k * arm_mass * arm_rate)).subs(centre_rate, arm_rate / (1 + symbol_k * rest_mass))
coordinate_x, coordinate_y, coordinate_z = sp.symbols("X Y Z")
polynomial = coordinate_x ** 4 - 6 * coordinate_x ** 2 * coordinate_y ** 2 + coordinate_y ** 4 - 2 * coordinate_z ** 2
laplacian = sum(polynomial.subs(variable, variable + 1) + polynomial.subs(variable, variable - 1) - 2 * polynomial for variable in (coordinate_x, coordinate_y, coordinate_z))
arms = [tuple(step if axis == direction else 0 for axis in range(3)) for direction in range(3) for step in (1, -1)]


def pair_with(points, scale):
    return sum(polynomial.subs({coordinate_x: scale * point[0], coordinate_y: scale * point[1], coordinate_z: scale * point[2]}) for point in points)


local_ok = local_ok and sp.simplify(star_rule - constant / (1 - symbol_k * constant)) == 0
local_ok = local_ok and sp.expand(laplacian) == 0
local_ok = local_ok and pair_with(arms, 1) - 6 * polynomial.subs({coordinate_x: 0, coordinate_y: 0, coordinate_z: 0}) == 0
local_ok = local_ok and pair_with(arms, 2) - 6 * polynomial.subs({coordinate_x: 0, coordinate_y: 0, coordinate_z: 0}) == 48
check("point source", local_ok, "E' = Q/(phi_y + k f_y) matches the exact price, and the cross is not point-equivalent")

time, frequency, static_response = sp.symbols("t omega u", positive=True)
response = (1 - sp.cos(frequency * time)) * static_response
check(
    "delay",
    sp.simplify(sp.diff(response, time, 2) + frequency ** 2 * response - frequency ** 2 * static_response) == 0
    and response.subs(time, 0) == 0
    and sp.diff(response, time).subs(time, 0) == 0
    and sp.simplify(response.subs(time, sp.pi / (2 * frequency)) - static_response) == 0
    and sp.simplify(response.subs(time, sp.pi / frequency) - 2 * static_response) == 0,
    "the single-frequency step reaches the static change at pi/(2 omega) and twice that change at pi/omega",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. The ledger equals the total effective source. No records-only rule of radius 0, 1 or 2 "
    "can give the same price in every held box, because the centre Green values 1, 22/17, 136/99 and 79271956/56195761 "
    "are strictly increasing. A charged cage outside the window changes the ledger by exactly its charge and leaves the "
    "window data fixed. For a point-equivalent source the price is Q/(phi_y + k f_y). Under the single-frequency delay "
    "the kept-ledger clock reaches the new value at pi/(2 omega) and overshoots at pi/omega. The note hashes were not re-checked.",
    flush=True,
)
print(
    "HIT: confirmed - no local rule of any fixed radius sets the formation price in every held box, while a point-equivalent "
    "source has the exact local price Q/(phi_y + k f_y)",
    flush=True,
)
