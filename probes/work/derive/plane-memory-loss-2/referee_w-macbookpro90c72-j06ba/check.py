#!/usr/bin/env python3
"""Referee for plane memory loss 2, a4.

Author w-jonathonsmac4f50-j5926 (claude-opus-5). Own rational solve of the cone.
The positive infinite-T limit is an extrapolation from the decrements, not a proof.
The plane walk's return sum is a different object and was not re-summed.
"""
from fractions import Fraction as Fr

import sympy as sp

fails = []
QUOTED = {
    1: Fr(3, 1),
    2: Fr(9, 4),
    3: Fr(117, 59),
    4: Fr(2595, 1408),
    5: Fr(369612, 210437),
    6: Fr(519757389, 306198359),
    7: Fr(4011089980525, 2423987521503),
    8: Fr(992844286053523947, 611962959395348995),
}


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def entropy():
    kappa = sp.symbols("kappa", positive=True)
    moment = sp.coth(kappa) - 1 / kappa
    series = sp.series(kappa * moment, kappa, 0, 5).removeO()
    report(
        "entropy",
        sp.simplify(series - (kappa ** 2 / 3 - kappa ** 4 / 45)) == 0,
        "kappa A(kappa) = kappa^2/3 - kappa^4/45 + O(kappa^6), so one site's small-twist cost is quadratic in the angle",
    )


def sites_of(depth):
    points = []
    for total in range(depth + 1):
        for first in range(total + 1):
            for second in range(total - first + 1):
                points.append((first, second, total - first - second))
    return points


def solve(matrix, rhs):
    size = len(rhs)
    rows = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(size):
        pivot = next(i for i in range(col, size) if rows[i][col] != 0)
        rows[col], rows[pivot] = rows[pivot], rows[col]
        scale = rows[col][col]
        for j in range(col, size + 1):
            rows[col][j] /= scale
        for i in range(size):
            if i != col and rows[i][col] != 0:
                factor = rows[i][col]
                for j in range(col, size + 1):
                    rows[i][j] -= factor * rows[col][j]
    return [rows[i][size] for i in range(size)]


def conductance(depth):
    points = sites_of(depth)
    present = set(points)
    base = {point for point in points if sum(point) == depth}
    apex = (0, 0, 0)
    free = [point for point in points if point not in base and point != apex]
    index = {point: i for i, point in enumerate(free)}
    size = len(free)
    matrix = [[Fr(0) for _ in range(size)] for _ in range(size)]
    rhs = [Fr(0) for _ in range(size)]
    for point in free:
        row = index[point]
        for axis in range(3):
            for sign in (1, -1):
                step = list(point)
                step[axis] += sign
                step = tuple(step)
                if min(step) < 0 or step not in present:
                    continue
                matrix[row][row] += 1
                if step == apex:
                    rhs[row] += 1
                elif step not in base:
                    matrix[row][index[step]] -= 1
    potential = {apex: Fr(1)}
    if size:
        solved = solve(matrix, rhs)
        for point, value in zip(free, solved):
            potential[point] = value
    for point in base:
        potential[point] = Fr(0)
    energy = Fr(0)
    for point in points:
        for axis in range(3):
            step = list(point)
            step[axis] += 1
            step = tuple(step)
            if step in present:
                gap = potential[point] - potential[step]
                energy += gap * gap
    flux = Fr(0)
    for axis in range(3):
        child = tuple(1 if i == axis else 0 for i in range(3))
        if child in potential:
            flux += potential[apex] - potential[child]
    return energy, flux


def cone():
    values = {}
    ok = True
    for depth in range(1, 9):
        energy, flux = conductance(depth)
        ok &= energy == flux == QUOTED[depth]
        values[depth] = energy
    decrements = [values[t] - values[t + 1] for t in range(1, 8)]
    scaled = [float(decrements[i] * (i + 2) ** 2) for i in range(7)]
    ok &= all(values[t] > values[t + 1] for t in range(1, 8))
    ok &= all(value > Fr(8, 5) for value in values.values())
    ok &= abs(scaled[0] - 3) < 1e-9 and all(2.0 < item < 2.41 for item in scaled[1:])
    report(
        "cone",
        ok,
        "conductances T=1..8 are 3, 9/4, 117/59, 2595/1408, 369612/210437, 519757389/306198359, "
        f"4011089980525/2423987521503, 992844286053523947/611962959395348995; "
        f"decrement*T^2 runs {', '.join(f'{item:.3f}' for item in scaled)}",
    )


def main():
    entropy()
    cone()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the backward cone's twist conductance is exactly 3, 9/4, 117/59, 2595/1408, "
        "369612/210437, 519757389/306198359, 4011089980525/2423987521503, 992844286053523947/611962959395348995. "
        "It decreases, every value is above 8/5, and the decrements scale like 2/T^2. "
        "A site-wise twist therefore costs a positive amount through T=8, not o(1)."
    )
    print(
        "SUMMARY: confirmed the von Mises series and the eight exact conductances. "
        "The infinite-depth limit being about 1.4 is an extrapolation, not a proof. "
        "The plane walk's return sum was not re-summed; it is a different object."
    )


if __name__ == "__main__":
    main()
