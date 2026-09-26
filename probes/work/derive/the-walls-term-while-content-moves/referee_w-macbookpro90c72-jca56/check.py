#!/usr/bin/env python3
"""Independent check of the walls' term while content moves, attempt a1.

Does not import the author's script. The strong-field root and the walker
time step were not rebuilt. Existence of slaved branches stays assumed.
"""
from fractions import Fraction
from itertools import product

import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def interior(n):
    return list(product(range(1, n + 1), repeat=3))


def bonds_and_walls(sites):
    inside = set(sites)
    bonds = set()
    walls = set()
    for site in sites:
        for step in DIRS:
            other = tuple(site[k] + step[k] for k in range(3))
            bonds.add(tuple(sorted((site, other))))
            if other not in inside:
                walls.add(other)
    return sorted(bonds), sorted(walls)


def neg_laplacian(sites):
    index = {site: i for i, site in enumerate(sites)}
    size = len(sites)
    matrix = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for site, row in index.items():
        matrix[row][row] = Fraction(6)
        for step in DIRS:
            other = tuple(site[k] + step[k] for k in range(3))
            column = index.get(other)
            if column is not None:
                matrix[row][column] -= 1
    return matrix


def invert(matrix):
    size = len(matrix)
    work = [row[:] + [Fraction(i == col) for col in range(size)] for i, row in enumerate(matrix)]
    for col in range(size):
        pivot = next(row for row in range(col, size) if work[row][col] != 0)
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        for row in range(size):
            if row == col or work[row][col] == 0:
                continue
            factor = work[row][col] / scale
            for entry in range(col, 2 * size):
                work[row][entry] -= factor * work[col][entry]
        for entry in range(col, 2 * size):
            work[col][entry] /= scale
    return [row[size:] for row in work]


def lap_value(field, site):
    total = Fraction(0)
    for step in DIRS:
        other = tuple(site[k] + step[k] for k in range(3))
        total += field.get(other, Fraction(0)) - field[site]
    return total


# --- 3^3 Dirichlet Green function, zero on the walls ---
sites3 = interior(3)
index3 = {site: i for i, site in enumerate(sites3)}
green = invert(neg_laplacian(sites3))
centre, face = (2, 2, 2), (2, 2, 1)
K = Fraction(1, 2)
gcc = green[index3[centre]][index3[centre]]
goo = green[index3[face]][index3[face]]
faces = [(2, 2, 1), (2, 2, 3), (2, 1, 2), (2, 3, 2), (1, 2, 2), (3, 2, 2)]
same_faces = all(green[index3[site]][index3[site]] == goo for site in faces)
rise = (gcc - goo) / (8 * K)
check(
    "green diagonal",
    gcc == Fraction(11, 51) and goo == Fraction(145, 714) and same_faces and rise == Fraction(3, 952),
    f"g_cc = {gcc}, g_face = {goo}, centre to face raises the second-order walls term by {rise}",
)

# unit source at the centre: the order-eps flux of chi equals the source
chi = {site: green[index3[site]][index3[centre]] / (8 * K) for site in sites3}
for wall in bonds_and_walls(sites3)[1]:
    chi[wall] = Fraction(0)
flux = Fraction(0)
for left, right in bonds_and_walls(sites3)[0]:
    if left not in index3:
        flux += chi[right]
    elif right not in index3:
        flux += chi[left]
check(
    "lattice gauss",
    8 * K * flux == 1 and all(lap_value(chi, site) == (-Fraction(1, 8 * K) if site == centre else 0) for site in sites3),
    "a unit source at the centre sends flux 1 through the walls",
)

# a second body, fixed on a face, while the other moves from the opposite face to the centre
fixed, start, end = (1, 2, 2), (3, 2, 2), (2, 2, 2)


def quadratic(masses):
    total = Fraction(0)
    for left, left_mass in masses.items():
        for right, right_mass in masses.items():
            total += left_mass * right_mass * green[index3[left]][index3[right]]
    return total


before = quadratic({fixed: 1, start: 1})
after = quadratic({fixed: 1, end: 1})
fall = -(after - before) / (8 * K)
check(
    "two bodies",
    fall == Fraction(-61, 2856),
    f"moving one body from the far face onto the centre, beside a fixed face body, changes Wt by {fall}",
)

# rate at first order in the speed: d/dt[-rho.g.rho/(8K)] = -(1/(4K)) rhodot.g.rho
# smooth step S = 3t^2 - 2t^3 carries the single body from the centre to the face
step = [Fraction(0), Fraction(0), Fraction(3), Fraction(-2)]


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly = poly[:-1]
    return poly


def pscale(poly, factor):
    return trim([factor * term for term in poly])


def padd(left, right):
    width = max(len(left), len(right))
    out = [Fraction(0) for _ in range(width)]
    for i, term in enumerate(left):
        out[i] += term
    for i, term in enumerate(right):
        out[i] += term
    return trim(out)


def pmul(left, right):
    out = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, left_term in enumerate(left):
        for j, right_term in enumerate(right):
            out[i + j] += left_term * right_term
    return trim(out)


def pder(poly):
    return trim([index * term for index, term in enumerate(poly) if index] or [Fraction(0)])


def peval(poly, point):
    total = Fraction(0)
    power = Fraction(1)
    for term in poly:
        total += term * power
        power *= point
    return total


one = [Fraction(1)]
rest = padd(one, pscale(step, -1))
rho = {site: [Fraction(0)] for site in sites3}
rho[centre] = rest
rho[face] = step
gr = {site: [Fraction(0)] for site in sites3}
for row_site in sites3:
    for col_site in sites3:
        gr[row_site] = padd(gr[row_site], pscale(rho[col_site], green[index3[row_site]][index3[col_site]]))
quad = [Fraction(0)]
dot_g = [Fraction(0)]
for site in sites3:
    quad = padd(quad, pmul(rho[site], gr[site]))
    dot_g = padd(dot_g, pmul(pder(rho[site]), gr[site]))
static_rate = pder(pscale(quad, -1 / (8 * K)))
claimed_rate = pscale(dot_g, -1 / (4 * K))
ck = -6 * K
chi1 = {site: pscale(gr[site], 1 / (8 * K)) for site in sites3}
kinetic = [Fraction(0)]
for site in sites3:
    lam_dot = pscale(pder(chi1[site]), 2)
    kinetic = padd(kinetic, pscale(pmul(lam_dot, lam_dot), ck))
chi_ddot = {site: pder(pder(chi1[site])) for site in sites3}
green_ddot = {site: [Fraction(0)] for site in sites3}
for row_site in sites3:
    for col_site in sites3:
        green_ddot[row_site] = padd(
            green_ddot[row_site], pscale(chi_ddot[col_site], green[index3[row_site]][index3[col_site]])
        )
w1_dot = [Fraction(0)]
for site in sites3:
    weight = padd(pscale(chi1[site], -2), pscale(green_ddot[site], ck / K))
    w1_dot = padd(w1_dot, pmul(weight, pder(rho[site])))
full_rate = pder(padd(pscale(quad, -1 / (8 * K)), kinetic))
check(
    "slow rate",
    static_rate == claimed_rate and full_rate == w1_dot
    and peval(pder(step), 0) == 0 and peval(pder(step), 1) == 0,
    "the first order in speed is -(1/(4K)) rhodot.g.rho; with c_k = -6K the kinetic piece keeps dWt/dt = sum w1 rhodot",
)

# --- bond identity and the Euler relation, on the 2^3 box, at one rational point ---
sites2 = interior(2)
inside2 = set(sites2)
bonds2, walls2 = bonds_and_walls(sites2)
point_w = {}
point_chi = {}
for number, site in enumerate(sites2):
    point_w[site] = Fraction(number + 2, 3)
    point_chi[site] = Fraction(number + 5, 4)
for wall in walls2:
    point_w[wall] = Fraction(1)
    point_chi[wall] = Fraction(1)
point_n = {site: point_w[site] * point_chi[site] for site in list(sites2) + walls2}
rho2 = {site: Fraction(number + 1, 2) for number, site in enumerate(sites2)}
lam_dot = {site: Fraction(number - 3, 5) for number, site in enumerate(sites2)}


def curvature(weight, length):
    total = Fraction(0)
    for left, right in bonds2:
        total += (weight[right] - weight[left]) * (length[right] - length[left])
    return -8 * K * total


def partial_u(site):
    """w dF/dw from the bond sum, evaluated at the rational point."""
    total = Fraction(0)
    for left, right in bonds2:
        if site == right:
            total += -8 * K * point_chi[right] * (point_chi[right] - point_chi[left])
        elif site == left:
            total += -8 * K * point_chi[left] * (point_chi[left] - point_chi[right])
    return point_w[site] * total


all_sites = list(sites2) + walls2
neighbors = {site: [] for site in all_sites}
for left, right in bonds2:
    neighbors[left].append(right)
    neighbors[right].append(left)


def box_lap(field, site):
    return sum(field[other] - field[site] for other in neighbors[site])


lap_chi = {site: box_lap(point_chi, site) for site in all_sites}
bond_match = all(partial_u(site) == 8 * K * point_n[site] * lap_chi[site] for site in all_sites)
zero_sum = sum(lap_chi.values()) == 0
walls_term = 8 * K * sum(lap_chi[wall] for wall in walls2)
kinetic = {
    site: ck * point_chi[site] ** 6 * lam_dot[site] ** 2 / point_w[site] for site in sites2
}
content = {site: point_w[site] * rho2[site] for site in sites2}
energy = sum(kinetic.values()) + sum(content.values()) + curvature(point_n, point_chi)
interior_derivative = sum(-kinetic[site] - content[site] - partial_u(site) for site in sites2)
check(
    "euler",
    bond_match and zero_sum and energy - walls_term + interior_derivative == 0
    and walls_term == -8 * K * sum(lap_chi[site] for site in sites2),
    "on the 2^3 box, dF/du = 8K N Lap chi, the lap sums to zero, and h - Wt = -sum_I dL/du",
)

# walker: i psi_dot = G psi. d<H>/dt = i <[G, H]> , and it vanishes when G = H
generator = sp.Matrix([[1, 2], [2, 0]])
member = sp.Matrix([[0, 3], [3, -1]])
state = sp.Matrix([1, sp.I])
time = sp.symbols("t", real=True)
series = state
term = state
for order in range(1, 6):
    term = (-sp.I * time / order) * generator * term
    series = series + term
expect = sp.expand((series.H * member * series)[0])
commutator = sp.expand((sp.I * (state.H * (generator * member - member * generator) * state))[0])
own = sp.series((series.H * generator * series)[0], time, 0, 6).removeO()
check(
    "walker rate",
    sp.diff(expect, time).subs(time, 0) == commutator and sp.expand(own - own.subs(time, 0)) == 0,
    "a different generator moves <H> at i<[G, H]>; the generator's own expectation is constant",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL on the 3^3 interior with K = 1/2, g_cc = 11/51 and g_face = 145/714, "
        "so a body carried from the centre to a face raises the second-order walls term by 3/952, "
        "and a body carried from the opposite face to the centre beside a fixed one lowers it by 61/2856. "
        "The first order in the speed is -(1/(4K)) rhodot.g.rho, the supply's work, not zero. "
        "On the 2^3 box the ledger equals the walls' term once the interior rate equations hold. "
        "A walker generated by its own ledger has constant <H>; a different generator changes it at i<[G,H]>. "
        "The strong-field root and the slaved time step were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - while content is supplied, the walls' term moves at the supply's work. "
        "To first order in the speed that rate is -(1/(4K)) rhodot.g.rho. "
        "On the 3^3 box at K = 1/2 the centre-to-face change is 3/952 and the two-body change is -61/2856.",
        flush=True,
    )
