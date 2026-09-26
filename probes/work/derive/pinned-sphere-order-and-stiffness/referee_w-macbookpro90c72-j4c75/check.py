#!/usr/bin/env python3
"""Independent check of pinned-sphere order and stiffness, attempt a3.

Does not import the author's script. The domination route (b)-(d) is not
reopened. Positivity of every higher spherical eigenvalue is not re-proved.
"""
from fractions import Fraction
from itertools import product

import numpy as np
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


def gone(expr):
    return sp.simplify(sp.expand(expr.rewrite(sp.exp))) == 0


beta, coupling, line = sp.symbols("beta c t", positive=True)
i0 = sp.simplify(sp.integrate(sp.exp(beta * line), (line, -1, 1)) / 2)
i1 = sp.simplify(sp.integrate(line * sp.exp(beta * line), (line, -1, 1)) / 2)
closed0 = sp.sinh(beta) / beta
closed1 = (beta * sp.cosh(beta) - sp.sinh(beta)) / beta**2
slope = sp.diff(beta * sp.cosh(beta) - sp.sinh(beta), beta)
block = sp.Matrix([[1, 1], [1, coupling * i0]])
at_threshold = block.subs(coupling, beta / sp.sinh(beta))
check(
    "sphere block",
    gone(i0 - closed0)
    and gone(i1 - closed1)
    and sp.simplify(slope - beta * sp.sinh(beta)) == 0
    and sp.limit(beta * sp.cosh(beta) - sp.sinh(beta), beta, 0) == 0
    and sp.simplify(block.det() - (coupling * sp.sinh(beta) / beta - 1)) == 0
    and at_threshold.rank(simplify=True) == 1,
    "i0 = sinh(beta)/beta, i1 = (beta cosh beta - sinh beta)/beta^2 > 0, and the empty-constant block forces c >= beta/sinh beta",
)

# two-valued contents: empty, +1, -1. No spherical-harmonic input.
growth = sp.exp(beta)
kernel = sp.Matrix([
    [1, 1, 1],
    [1, coupling * growth, coupling / growth],
    [1, coupling / growth, coupling * growth],
])
odd = sp.Matrix([0, 1, -1])
odd_value = sp.simplify((odd.T * kernel * odd)[0] / (odd.T * odd)[0])
even = sp.Matrix([
    [kernel[0, 0], (kernel[0, 1] + kernel[0, 2]) / sp.sqrt(2)],
    [(kernel[1, 0] + kernel[2, 0]) / sp.sqrt(2), (kernel[1, 1] + kernel[1, 2] + kernel[2, 1] + kernel[2, 2]) / 2],
])
threshold = 1 / sp.cosh(beta)
pinned = kernel.subs(coupling, threshold)
minor = sp.simplify((pinned[1, 1] * pinned[2, 2] - pinned[1, 2]**2).rewrite(sp.exp))
check(
    "two-valued",
    gone(odd_value - 2 * coupling * sp.sinh(beta))
    and gone(even.det() - (2 * coupling * sp.cosh(beta) - 2))
    and gone(pinned.det())
    and minor != 0,
    "PSD iff c >= 1/cosh beta, because the odd eigenvalue is 2c sinh beta and the even determinant is 2c cosh beta - 2; rank 2 at the threshold",
)

# 4^3 torus Green function of -Delta, zero mode removed. Momenta make every term rational.
side = 4
count = side**3


def mode_energy(mode):
    total = 0
    for coordinate in mode:
        total += (0, 2, 4, 2)[coordinate]
    return total


def mode_cos(mode, shift):
    quarter = sum(mode[axis] * shift[axis] for axis in range(3)) % 4
    return (1, 0, -1, 0)[quarter]


def torus_green(shift):
    total = Fraction(0)
    for mode in product(range(side), repeat=3):
        if mode == (0, 0, 0):
            continue
        total += Fraction(mode_cos(mode, shift), mode_energy(mode))
    return total / count


green0 = torus_green((0, 0, 0))
green1 = torus_green((1, 0, 0))
green2 = torus_green((2, 0, 0))
gap = green0 - green2
stiffness = 2 / (1 - gap)
check(
    "torus green",
    green0 - green1 == Fraction(count - 1, 6 * count) and stiffness == Fraction(320, 129),
    f"G0 - G1 = (1 - 1/N)/6 and a_L = 2/(1 - (G0 - G(2,0,0))) = {stiffness}",
)


def solve(matrix, rhs):
    size = len(rhs)
    work = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(size):
        pivot = next(row for row in range(col, size) if work[row][col] != 0)
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        for row in range(size):
            if row == col or work[row][col] == 0:
                continue
            factor = work[row][col] / scale
            for entry in range(col, size + 1):
                work[row][entry] -= factor * work[col][entry]
        for entry in range(col, size + 1):
            work[col][entry] /= scale
    return [work[i][size] for i in range(size)]


vacancy = (0, 0, 0)
sites = [site for site in product(range(side), repeat=3) if site != vacancy]
index = {site: i for i, site in enumerate(sites)}
size = len(sites)
matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
rhs = [Fraction(0) for _ in range(size)]
links = []
for site in sites:
    for axis in range(3):
        neighbor = list(site)
        neighbor[axis] = (neighbor[axis] + 1) % side
        neighbor = tuple(neighbor)
        if neighbor == vacancy:
            continue
        drive = Fraction(-1) if axis == 0 else Fraction(0)
        links.append((site, neighbor, drive))
        left, right = index[site], index[neighbor]
        matrix[left][left] += 1
        matrix[left][right] -= 1
        rhs[left] += drive
        matrix[right][right] += 1
        matrix[right][left] -= 1
        rhs[right] -= drive
matrix[0] = [Fraction(1 if column == 0 else 0) for column in range(size)]
rhs[0] = Fraction(0)
voltage = solve(matrix, rhs)
power = sum((voltage[index[left]] - voltage[index[right]] - drive) ** 2 for left, right, drive in links)
check(
    "vacancy power",
    power == count - stiffness and power == Fraction(7936, 129),
    f"removing one site drops the twisted dissipation from {count} to {power}",
)

# near full occupancy the algebra is exact for any vacancy cost a
density_shift, cost = sp.symbols("epsilon a")
rho = 1 - density_shift
expanded = sp.series(rho**2 / (1 - cost * density_shift), density_shift, 0, 2).removeO()
check(
    "stiffness algebra",
    sp.expand(expanded - (1 + (cost - 2) * density_shift)) == 0,
    "rho^2/(beta (1 - a epsilon)) = (1/beta)(1 + (a - 2) epsilon) + O(epsilon^2)",
)

# infinite-lattice difference, quadrature only. The integrand is bounded.
grid = 160
coordinates = (np.arange(grid) + 0.5) / grid * (2 * np.pi) - np.pi
kx, ky, kz = np.meshgrid(coordinates, coordinates, coordinates, indexing="ij")
symbol = 2 * ((1 - np.cos(kx)) + (1 - np.cos(ky)) + (1 - np.cos(kz)))
integrand = (1 - np.cos(2 * kx)) / symbol
difference = float(integrand.mean())
infinite = 2 / (1 - difference)
check(
    "infinite lattice",
    abs(infinite - 2.531138) < 5e-4 and infinite < 3,
    f"quadrature on a {grid}^3 grid gives a = {infinite:.6f}, against the printed 2.531138; six separate bonds would cost 3",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL the two-valued bond kernel is positive semidefinite iff c >= 1/cosh beta, and has rank 2 there. "
        "The sphere kernel's empty-constant block requires c >= beta/sinh beta, with i0 = sinh(beta)/beta and i1 > 0. "
        "On the 4^3 torus one vacancy drops the twisted dissipation from 64 to 7936/129 = 64 - 320/129. "
        "The stiffness factor is (1/beta)(1 + (a - 2) epsilon) + O(epsilon^2). "
        "A 160^3 quadrature gives a = 2.5311 on Z^3. "
        "Higher spherical eigenvalues and the domination route were not re-proved.",
        flush=True,
    )
    print(
        "HIT: confirmed - vacancies keep the two-valued bond kernel positive semidefinite exactly for c >= 1/cosh beta. "
        "On the 4^3 torus a site vacancy lowers the twisted dissipation from 64 to 7936/129.",
        flush=True,
    )
