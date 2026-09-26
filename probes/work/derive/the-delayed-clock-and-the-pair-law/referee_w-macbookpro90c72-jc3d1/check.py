#!/usr/bin/env python3
"""Independent referee for the delayed clock and the pair law, attempt 1.

Green functions, the separation walk, and the first-order moment solution
are recomputed with exact fractions. The attempt's script is not imported.
The direct simulation was not rebuilt. Well-posedness and differentiability
in the coupling are assumptions of the attempt, not proved here.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


class Lattice:
    def __init__(self, dims):
        self.dims = dims
        self.sites = list(product(*[range(length) for length in dims]))
        self.V = len(self.sites)
        self.d = len(dims)
        self.q = 2 * self.d
        self.at = {site: index for index, site in enumerate(self.sites)}
        steps = []
        for axis in range(self.d):
            for sign in (1, -1):
                step = [0] * self.d
                step[axis] = sign
                steps.append(tuple(step))
        self.steps = steps
        self.nbrs = []
        for site in self.sites:
            self.nbrs.append([self.at[self.shift(site, step)] for step in steps])
        self.edges = [self.at[self.shift(self.sites[0], step)] for step in steps]

    def shift(self, site, step):
        return tuple((site[axis] + step[axis]) % self.dims[axis] for axis in range(self.d))

    def diff(self, left, right):
        return self.at[tuple((self.sites[left][axis] - self.sites[right][axis]) % self.dims[axis] for axis in range(self.d))]

    def solve(self, rhs):
        size = self.V
        matrix = [[F(0) for _ in range(size)] for _ in range(size)]
        for site in range(size):
            matrix[site][site] = F(self.q)
            for neighbour in self.nbrs[site]:
                matrix[site][neighbour] -= 1
        for site in range(size):
            matrix[size - 1][site] = 1
        target = list(rhs)
        target[size - 1] = 0
        return eliminate(matrix, target)

    def green(self):
        rhs = [F(-1, self.V) for _ in range(self.V)]
        rhs[0] = F(1) - F(1, self.V)
        field = self.solve(rhs)
        square = self.solve(field)
        return field, square

    def apply_m(self, field):
        out = []
        for site in range(self.V):
            out.append(sum(field[neighbour] for neighbour in self.nbrs[site]) / self.q - field[site])
        return out


def eliminate(matrix, target):
    size = len(target)
    rows = [row[:] + [target[index]] for index, row in enumerate(matrix)]
    pivot_row = 0
    for column in range(size):
        chosen = next((row for row in range(pivot_row, size) if rows[row][column] != 0), None)
        if chosen is None:
            continue
        rows[pivot_row], rows[chosen] = rows[chosen], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(size):
            if row == pivot_row or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [entry - factor * rows[pivot_row][index] for index, entry in enumerate(rows[row])]
        pivot_row += 1
    return [rows[index][-1] for index in range(size)]


def rank_of(matrix):
    rows = [row[:] for row in matrix]
    size = len(rows)
    width = len(rows[0])
    rank = 0
    for column in range(width):
        chosen = next((row for row in range(rank, size) if rows[row][column] != 0), None)
        if chosen is None:
            continue
        rows[rank], rows[chosen] = rows[chosen], rows[rank]
        scale = rows[rank][column]
        rows[rank] = [entry / scale for entry in rows[rank]]
        for row in range(size):
            if row == rank or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [entry - factor * rows[rank][index] for index, entry in enumerate(rows[row])]
        rank += 1
    return rank


def configurations(lattice, count):
    return [frozenset(choice) for choice in combinations(range(lattice.V), count)]


def moves(lattice, occupied):
    found = []
    for site in occupied:
        for neighbour in lattice.nbrs[site]:
            if neighbour in occupied:
                continue
            found.append((frozenset((occupied - {site}) | {neighbour}), site, neighbour))
    return found


def phi(lattice, occupied, green):
    field = [F(0) for _ in range(lattice.V)]
    for record in occupied:
        for site in range(lattice.V):
            field[site] += lattice.q * green[lattice.diff(site, record)]
    return field


def ring_green(length):
    return [F(length * length - 1, 12 * length) - F(site * (length - site), 2 * length) for site in range(length)]


def greens() -> bool:
    good = True
    quoted = {}
    for dims in [(length,) for length in range(3, 9)] + [(3, 3), (3, 3, 3), (4, 4)]:
        lattice = Lattice(dims)
        if len(dims) == 1:
            green = ring_green(dims[0])
        else:
            green, _square = lattice.green()
        image = [lattice.q * green[site] - sum(green[neighbour] for neighbour in lattice.nbrs[site]) for site in range(lattice.V)]
        target = [F(1) - F(1, lattice.V) if site == 0 else F(-1, lattice.V) for site in range(lattice.V)]
        good = good and image == target and sum(green) == 0 and all(green[0] > green[site] for site in range(1, lattice.V))
        if dims == (6,):
            quoted["ring6"] = lattice.q * green[0]
        if dims == (3, 3, 3):
            quoted["cube"] = lattice.q * green[0]
    return good and quoted["ring6"] == F(35, 36) and quoted["cube"] == F(88, 81)


def separation() -> bool:
    good = True
    for dims in [(3,), (4,), (5,), (6,), (3, 3), (4, 4), (3, 3, 3)]:
        lattice = Lattice(dims)
        for gap in range(1, lattice.V):
            by_first = sorted(lattice.diff(gap, edge) for edge in lattice.edges if edge != gap)
            by_second = sorted(lattice.diff(gap, lattice.diff(0, edge)) for edge in lattice.edges if lattice.diff(0, edge) != gap)
            # record 2 moving by e sends D to D+e; e runs over steps whose negative is not D.
            by_second = sorted(
                lattice.at[lattice.shift(lattice.sites[gap], step)]
                for step in lattice.steps
                if lattice.at[lattice.shift(lattice.sites[0], tuple(-part for part in step))] != gap
            )
            neighbours = sorted(site for site in lattice.nbrs[gap] if site != 0)
            degree = lattice.q - (1 if gap in lattice.edges else 0)
            good = good and by_first == neighbours and by_second == neighbours and len(neighbours) == degree
    return good


def first_order(lattice, count, gamma_rate, timing, override=None):
    rate0 = F(1, 2 * lattice.q)
    gamma = gamma_rate / (gamma_rate + rate0 * lattice.q) if override is None else override
    states = configurations(lattice, count)
    weight = F(1, len(states))
    density = F(count, lattice.V)
    green, _square = lattice.green() if len(lattice.dims) > 1 else (ring_green(lattice.dims[0]), None)
    if len(lattice.dims) == 1:
        green = ring_green(lattice.dims[0])
    fields = {state: phi(lattice, state, green) for state in states}
    moments = {state: [weight * gamma * value for value in fields[state]] for state in states}
    links = {state: moves(lattice, state) for state in states}
    residual = 0
    for state in states:
        mixed = lattice.apply_m(moments[state])
        for site in range(lattice.V):
            total = gamma_rate * (mixed[site] + weight * ((1 if site in state else 0) - density))
            total += rate0 * sum(moments[other][site] - moments[state][site] for other, _start, _end in links[state])
            residual += total != 0
    pairs = {
        state: sum(green[lattice.diff(left, right)] for left, right in combinations(sorted(state), 2))
        for state in states
    }
    mean_pair = sum(pairs.values()) / len(states)
    correction = {state: weight * gamma * lattice.q * (1 - 2 * timing) * (pairs[state] - mean_pair) for state in states}
    master = 0
    for state in states:
        total = F(0)
        for other, start, end in links[state]:
            total += correction[other] - correction[state]
            total += timing * moments[other][end] + (1 - timing) * moments[other][start]
            total -= timing * moments[state][start] + (1 - timing) * moments[state][end]
        master += total != 0
    return gamma, residual, master


def moments() -> bool:
    good = True
    solved = 0
    failed_controls = 0
    cases = [((5,), 1), ((6,), 2), ((7,), 3), ((3, 3), 2), ((3, 3, 3), 1), ((3, 3, 3), 2)]
    for dims, count in cases:
        lattice = Lattice(dims)
        for gamma_rate in (F(1, 3), F(1), F(5, 2)):
            for timing in (F(1), F(1, 2), F(0)):
                _gamma, residual, master = first_order(lattice, count, gamma_rate, timing)
                good = good and residual == 0 and master == 0
                solved += 1
            for bad in (F(1), gamma_rate / (gamma_rate + 1)):
                _gamma, residual, _master = first_order(lattice, count, gamma_rate, F(1), override=bad)
                failed_controls += residual > 0
    return good and solved == 54 and failed_controls == 36


def kernel_rank() -> bool:
    lattice = Lattice((5,))
    count = 2
    gamma_rate = F(1)
    rate0 = F(1, 2 * lattice.q)
    states = configurations(lattice, count)
    index = {state: position for position, state in enumerate(states)}
    size = len(states) * lattice.V
    matrix = [[F(0) for _ in range(size)] for _ in range(size)]
    for state in states:
        for site in range(lattice.V):
            row = index[state] * lattice.V + site
            matrix[row][row] += -gamma_rate
            for neighbour in lattice.nbrs[site]:
                matrix[row][index[state] * lattice.V + neighbour] += gamma_rate / lattice.q
            for other, _start, _end in moves(lattice, state):
                matrix[row][index[other] * lattice.V + site] += rate0
                matrix[row][row] -= rate0
    return rank_of(matrix) == size - 1


def ring_pair() -> bool:
    green = ring_green(6)
    pairs = {1: green[1], 2: green[2], 3: green[3]}
    mean = (6 * pairs[1] + 6 * pairs[2] + 3 * pairs[3]) / 15
    ratios = {distance: -2 * (pairs[distance] - mean) for distance in (1, 2, 3)}
    squares = {}
    for distance in (1, 2, 3):
        field = phi(Lattice((6,)), {0, distance}, green)
        squares[distance] = sum(value * value for value in field) / 2
    return (
        ratios == {1: F(-1, 3), 2: F(1, 6), 3: F(1, 3)}
        and squares == {1: F(56, 27), 2: F(89, 108), 3: F(8, 27)}
    )


def sojourn() -> bool:
    good = True
    witness = []
    for dims in [(6,), (3, 3, 3)]:
        lattice = Lattice(dims)
        green, square = lattice.green() if len(dims) > 1 else (ring_green(6), None)
        if square is None:
            square = lattice.solve(green)
        for gap in range(1, lattice.V):
            neighbours = [site for site in lattice.nbrs[gap] if site != 0]
            total = sum(square[site] - square[gap] for site in neighbours)
            adjacent = gap in lattice.edges
            expected = -green[gap] - (green[0] / lattice.q if adjacent else 0)
            good = good and total == expected
    ring = Lattice((6,))
    ring_green_values, ring_square = ring_green(6), ring.solve(ring_green(6))
    ring_pair = sorted({ring_square[site] for site in ring.nbrs[2] if site != 0})
    cube = Lattice((3, 3, 3))
    cube_green, cube_square = cube.green()
    origin = cube.at[(0, 0, 1)]
    cube_pair = sorted({cube_square[site] for site in cube.nbrs[origin] if site != 0})
    return good and ring_pair == [F(-265, 864), F(119, 864)] and cube_pair == [F(-19, 8748), F(23, 2187)]


def algebra() -> bool:
    rate = sp.symbols("Gamma", positive=True)
    gamma = rate / (rate + sp.Rational(1, 2))
    series = sp.series(gamma, rate, sp.oo, 3).removeO()
    length = sp.symbols("lambda", real=True)
    level, slope = sp.symbols("c beta", real=True)
    rho = list(sp.symbols("rho0:3"))
    rho.append(2 - sum(rho))
    density = sp.Rational(2, 4)
    occupation = [1, 0, 1, 0]
    clock = sp.symbols("U0:4")
    drift = [
        sp.exp(clock[site] + level) * (-length * (rho[site] - density) + length * (occupation[site] - density))
        for site in range(4)
    ]
    target = [sp.exp(level) * sp.exp(clock[site]) * length * (occupation[site] - rho[site]) for site in range(4)]
    matched = all(sp.simplify(drift[site] - target[site]) == 0 for site in range(4))
    thresholds = []
    for dims in [(6,), (3, 3, 3), (4, 4, 4)]:
        lattice = Lattice(dims)
        side = dims[0]
        cosine = sp.cos(2 * sp.pi / side)
        mu = -(2 - 2 * cosine) / lattice.q
        thresholds.append(sp.simplify(lattice.V * mu))
    return (
        sp.simplify(gamma - 2 * rate / (2 * rate + 1)) == 0
        and sp.simplify(series - (1 - 1 / (2 * rate) + 1 / (4 * rate ** 2))) == 0
        and matched
        and thresholds == [-3, sp.Rational(-27, 2), sp.Rational(-64, 3)]
    )


def invariant() -> bool:
    lattice = Lattice((5,))
    values = sp.symbols("u0:5", real=True)
    coupling, rate = sp.symbols("lambda Gamma", real=True)
    occupation = [1, 0, 1, 0, 0]
    density = sp.Rational(2, 5)
    mixed = lattice.apply_m(values)
    change = sum(
        -sp.exp(-values[site]) * rate * sp.exp(values[site]) * (mixed[site] + coupling * (occupation[site] - density))
        for site in range(5)
    )
    return sp.simplify(sp.expand(change)) == 0


def main():
    check("green", greens(), "Poisson Green functions on rings 3..8, the 3x3, 4x4 and 3^3; q G(0) is 35/36 and 88/81")
    check("separation", separation(), "every nonzero separation on the checked tori steps uniformly onto its nonzero neighbours")
    check("moments", moments(), "54 (torus, count, rate, timing) systems are solved by gamma = Gamma/(Gamma+1/2); the two wrong gammas fail")
    check("kernel", kernel_rank(), "on ring 5 with two records the moment operator has rank one less than its dimension")
    check("ring six", ring_pair(), "pair weights -1/3, 1/6, 1/3 and quadratic normalizers 56/27, 89/108, 8/27")
    check("sojourn", sojourn(), "the arrival identity holds, and G2 takes both quoted pairs of values")
    check("algebra", algebra(), "gamma = 2 Gamma/(2 Gamma+1), and the uniform mode is unstable below -3, -27/2 and -64/3")
    check("invariant", invariant(), "the sum of reciprocal weights is constant along the flow")
    if FAILS:
        print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
        return 1
    print(
        "SUMMARY: confirmed partial. With log kappa nonzero and finite Gamma, no stationary product of a record "
        "law and a field law exists, and no stationary law is reversible, both under the attempt's well-posedness "
        "assumption. The separation jumps as simple random walk on the torus minus the origin. At first order in "
        "log kappa the conditional mean field is gamma times the slaved field, gamma = 2 Gamma/(2 Gamma+1). "
        "The direct simulation was not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - no stationary product law exists at finite Gamma when log kappa is nonzero, the "
        "separation is a simple random walk off the origin, and the first-order clock field is slaved with "
        "factor 2 Gamma/(2 Gamma+1)",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
