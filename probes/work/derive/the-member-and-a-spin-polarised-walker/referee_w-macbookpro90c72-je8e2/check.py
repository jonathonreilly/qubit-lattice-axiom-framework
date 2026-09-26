#!/usr/bin/env python3
"""Independent referee for the-member-and-a-spin-polarised-walker a1.

The walk is H = sum_a sigma_a S_a, with the two-step momentum S_j C_j.
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


def mul(left, right):
    return (left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0])


def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def conj(value):
    return (value[0], -value[1])


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
MINUS = (F(-1), F(0))
HALF = (F(1, 2), F(0))
MINUS_I_HALF = (F(0), F(-1, 2))
PAULI = (
    ((ZERO, ONE), (ONE, ZERO)),
    ((ZERO, (F(0), F(-1))), ((F(0), F(1)), ZERO)),
    ((ONE, ZERO), (ZERO, MINUS)),
)
LEVY = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def apply_pauli(axis, spin):
    matrix = PAULI[axis]
    return (
        add(mul(matrix[0][0], spin[0]), mul(matrix[0][1], spin[1])),
        add(mul(matrix[1][0], spin[0]), mul(matrix[1][1], spin[1])),
    )


def add_spin(left, right):
    return (add(left[0], right[0]), add(left[1], right[1]))


def scale_spin(spin, factor):
    return (mul(spin[0], factor), mul(spin[1], factor))


def bracket(left, right):
    return add(mul(conj(left[0]), right[0]), mul(conj(left[1]), right[1]))


class Lattice:
    def __init__(self, length, state):
        self.length = length
        self.sites = list(itertools.product(range(length), repeat=3))
        self.state = state
        self.evolved = self._hamiltonian(state)
        self.momentum = [self._difference(self._average(state, axis), axis) for axis in range(3)]
        self._bond = {}

    def move(self, site, axis, sign=1):
        point = list(site)
        point[axis] = (point[axis] + sign) % self.length
        return tuple(point)

    def move_by(self, site, vector):
        return tuple((site[i] + vector[i]) % self.length for i in range(3))

    def _average(self, field, axis):
        return {
            site: scale_spin(add_spin(field[self.move(site, axis)], field[self.move(site, axis, -1)]), HALF)
            for site in self.sites
        }

    def _difference(self, field, axis):
        return {
            site: scale_spin(
                add_spin(field[self.move(site, axis)], scale_spin(field[self.move(site, axis, -1)], MINUS)),
                MINUS_I_HALF,
            )
            for site in self.sites
        }

    def _hamiltonian(self, field):
        out = {}
        for site in self.sites:
            total = (ZERO, ZERO)
            for axis in range(3):
                forward = apply_pauli(axis, field[self.move(site, axis)])
                backward = apply_pauli(axis, field[self.move(site, axis, -1)])
                total = add_spin(total, scale_spin(add_spin(forward, scale_spin(backward, MINUS)), MINUS_I_HALF))
            out[site] = total
        return out

    def real_overlap(self, left_site, axis, right_spin):
        right = right_spin if axis is None else apply_pauli(axis, right_spin)
        return bracket(self.state[left_site], right)[0]

    def rate_overlap(self, left_site, axis, right_site):
        dress = (lambda spin: spin) if axis is None else (lambda spin: apply_pauli(axis, spin))
        left = -bracket(self.evolved[left_site], dress(self.state[right_site]))[1]
        right = bracket(self.state[left_site], dress(self.evolved[right_site]))[1]
        return left + right

    def energy(self, site):
        return bracket(self.state[site], self.evolved[site])[0]

    def pi(self, axis, site):
        return bracket(self.state[site], self.momentum[axis][site])[0]

    def current(self, bond, momentum, site):
        key = (bond, momentum, site)
        if key not in self._bond:
            ahead = self.move(site, bond)
            forward = self.real_overlap(ahead, bond, self.momentum[momentum][site])
            backward = bracket(self.momentum[momentum][ahead], apply_pauli(bond, self.state[site]))[0]
            self._bond[key] = (forward + backward) / 2
        return self._bond[key]

    def stress(self, row, column, site):
        transverse = [axis for axis in range(3) if axis != column]
        total = F(0)
        for signs in itertools.product((1, -1), repeat=2):
            place = self.move(self.move(site, transverse[0], signs[0]), transverse[1], signs[1])
            total += self.current(row, column, place) + self.current(row, column, self.move(place, column))
        return total / 8

    def face(self, axis, site, rate=False):
        other = [direction for direction in range(3) if direction != axis]
        sample = self.rate_overlap if rate else (lambda left, coin, right: self.real_overlap(left, coin, self.state[right]))
        first = sample(site, axis, self.move(self.move(site, other[0]), other[1]))
        second = sample(self.move(site, other[1]), axis, self.move(site, other[0]))
        return (first + second) / 2

    def spin(self, axis, site, rate=False):
        total = F(0)
        for shift in itertools.product((1, -1), repeat=3):
            total += self.face(axis, self.move_by(site, shift), rate)
        return total / 8

    def curl(self, axis, site):
        total = F(0)
        for (first, second, third), sign in LEVY.items():
            if first == axis:
                total += sign * (self.spin(third, site) - self.spin(third, self.move(site, second, -1)))
        return total

    def diagonal(self, site):
        corners = (((0, 0, 0), (1, 1, 1)), ((0, 0, 1), (1, 1, 0)), ((0, 1, 0), (1, 0, 1)), ((1, 0, 0), (0, 1, 1)))
        total = F(0)
        for start, end in corners:
            total += self.real_overlap(self.move_by(site, start), None, self.state[self.move_by(site, end)])
        return total / 4

    def averaged_diagonal(self, site):
        total = F(0)
        for shift in itertools.product((1, -1), repeat=3):
            total += self.diagonal(self.move_by(site, shift))
        return total / 8

    def torque(self, axis, site):
        total = F(0)
        for (first, row, column), sign in LEVY.items():
            if first == axis:
                total -= sign * (self.stress(row, column, site) - self.stress(column, row, site))
        return total


def coin_identity():
    left = sp.symbols("s1:4")
    right = sp.symbols("t1:4")
    pauli = (
        sp.Matrix([[0, 1], [1, 0]]),
        sp.Matrix([[0, -sp.I], [sp.I, 0]]),
        sp.Matrix([[1, 0], [0, -1]]),
    )

    def pack(vector):
        return vector[0] * pauli[0] + vector[1] * pauli[1] + vector[2] * pauli[2]

    good = True
    for axis in range(3):
        commutator = pack(right) * pauli[axis] - pauli[axis] * pack(left)
        correction = (right[axis] - left[axis]) * sp.eye(2)
        for first in range(3):
            for second in range(3):
                correction += sp.I * LEVY.get((first, axis, second), 0) * (left[first] + right[first]) * pauli[second]
        good = good and sp.simplify(commutator - correction) == sp.zeros(2)
    bar, half = sp.symbols("kbar q", real=True)
    good = good and sp.simplify(sp.sin(bar + half / 2) - sp.sin(bar - half / 2) - 2 * sp.cos(bar) * sp.sin(half / 2)) == 0
    good = good and sp.simplify((sp.sin(bar + half / 2) + sp.sin(bar - half / 2)) * sp.cos(bar) - sp.sin(2 * bar) * sp.cos(half / 2)) == 0
    angles = sp.symbols("a b c")
    diagonal = sum(sp.cos(angles[0] + sign_b * angles[1] + sign_c * angles[2]) for sign_b in (1, -1) for sign_c in (1, -1))
    good = good and sp.simplify(4 * angles[0] * 0 + 4 * sp.cos(angles[0]) * sp.cos(angles[1]) * sp.cos(angles[2]) - diagonal) == 0
    return good


check(
    "C3 beats",
    coin_identity(),
    "the coin commutator, the sum-to-product identities, and the four body-diagonal cosines",
)

probe = {}
for site in itertools.product(range(5), repeat=3):
    probe[site] = ((F(site[0] - 2), F(site[1] - 1)), (F(1, site[2] + 1), F(site[0] - site[1])))
box = Lattice(5, probe)
residual = F(0)
saw_rate = saw_torque = saw_diagonal = False
for site in box.sites:
    for axis in range(3):
        rate = box.spin(axis, site, rate=True)
        difference = box.averaged_diagonal(site) - box.averaged_diagonal(box.move(site, axis, -1))
        torque = box.torque(axis, site)
        residual = max(residual, abs(rate + difference - torque))
        saw_rate = saw_rate or rate != 0
        saw_torque = saw_torque or torque != 0
        saw_diagonal = saw_diagonal or difference != 0
check(
    "C1 balance",
    residual == 0 and saw_rate and saw_torque and saw_diagonal,
    "on a rational 5-torus state the face spin, the diagonal current and the stress torque balance, and none is identically zero",
)

spinor = ((F(3, 5), F(0)), (F(0), F(4, 5)))
magnetisation = [bracket(spinor, apply_pauli(axis, spinor))[0] for axis in range(3)]
support = {(i, j, k) for i in range(3) for j in range(3) for k in range(3)}
rest_state = {
    site: (spinor if site in support else (ZERO, ZERO))
    for site in itertools.product(range(6), repeat=3)
}
rest = Lattice(6, rest_state)
quiet = all(rest.energy(site) == 0 for site in rest.sites)
quiet = quiet and all(rest.pi(axis, site) == 0 for site in rest.sites for axis in range(3))
quiet = quiet and all(rest.current(bond, axis, site) == 0 for site in rest.sites for bond in range(3) for axis in range(3))
check(
    "A1 rest source",
    magnetisation == [F(0), F(24, 25), F(-7, 25)] and quiet,
    "a real envelope times (3/5, 4i/5) has spin (0, 24/25, -7/25) and sources neither energy, two-step momentum nor bond current",
)

def bond_energy(lattice, axis, site):
    ahead = lattice.move(site, axis)
    forward = lattice.real_overlap(ahead, axis, lattice.evolved[site])
    backward = bracket(lattice.evolved[ahead], apply_pauli(axis, lattice.state[site]))[0]
    return (forward + backward) / 2


def averaged_bond(lattice, axis, site):
    total = F(0)
    for shift in itertools.product((1, -1), repeat=3):
        total += bond_energy(lattice, axis, lattice.move_by(site, shift))
    return total / 8


pairs = [(axis, site, averaged_bond(rest, axis, site) / 2, rest.curl(axis, site) / 4) for axis in range(3) for site in rest.sites]
nonzero_bonds = sum(1 for _axis, _site, _bond, curl in pairs if curl != 0)
check(
    "A2 source",
    all(bond == curl for _axis, _site, bond, curl in pairs) and 0 < nonzero_bonds < 3 * 6**3,
    f"P^B = Q/2 equals one quarter of the curl of the face spin, nonzero on {nonzero_bonds} bonds",
)
total_spin = [sum(rest.spin(axis, site) for site in rest.sites) for axis in range(3)]
check(
    "A3 moment",
    total_spin == [12 * value for value in magnetisation],
    "the 3-box has total face spin 3*2^2 n",
)

symbol = sp.symbols("lam")
polynomial = sp.Poly(sp.interpolate([(0, 0)] + [(value, sp.Rational(1, value)) for value in range(1, 13)], symbol))
coefficients = [F(sp.fraction(term)[0], sp.fraction(term)[1]) for term in polynomial.all_coeffs()]
spectrum_ok = all(
    polynomial.subs(symbol, value) == (0 if value == 0 else sp.Rational(1, value)) for value in range(13)
)


def negative_laplacian(field):
    return {
        site: sum(2 * field[site] - field[rest.move(site, axis)] - field[rest.move(site, axis, -1)] for axis in range(3))
        for site in rest.sites
    }


def green(field):
    acc = {site: F(0) for site in rest.sites}
    for coefficient in coefficients:
        acc = negative_laplacian(acc)
        acc = {site: acc[site] + coefficient * field[site] for site in rest.sites}
    return acc


alpha, sea = F(1, 4), F(1)
solved = {axis: green({site: sea * averaged_bond(rest, axis, site) / 2 / (4 * alpha) for site in rest.sites}) for axis in range(3)}
solves = all(
    4 * alpha * negative_laplacian(solved[axis])[site] == sea * averaged_bond(rest, axis, site) / 2
    for axis in range(3)
    for site in rest.sites
)
mean_spin = [total / (6**3) for total in total_spin]
stored = {
    axis: green({site: rest.spin(axis, site) - mean_spin[axis] for site in rest.sites})
    for axis in range(3)
}
potential = {}
for axis in range(3):
    potential[axis] = {}
    for site in rest.sites:
        total = F(0)
        for (first, second, third), sign in LEVY.items():
            if first == axis:
                total += sign * (stored[third][site] - stored[third][rest.move(site, second, -1)])
        potential[axis][site] = sea / (16 * alpha) * total
matches = all(solved[axis][site] == potential[axis][site] for axis in range(3) for site in rest.sites)
nonzero_shift = any(solved[axis][site] != 0 for axis in range(3) for site in rest.sites)
check(
    "A4 vector potential",
    spectrum_ok and solves and matches and nonzero_shift,
    "on the 6-torus, 4 alpha (-Laplacian) N = wbar P^B and N is the curl of the inverse Laplacian of wbar S~/(16 alpha)",
)
divergence = max(
    abs(sum(solved[axis][site] - solved[axis][rest.move(site, axis, -1)] for axis in range(3)))
    for site in rest.sites
)
check("A5 transverse", divergence == 0, "the static shift has zero lattice divergence")

momentum_rate = F(0)
for site in rest.sites:
    for axis in range(3):
        acted = rest._difference(rest._average(rest.evolved, axis), axis)[site]
        gap = -bracket(rest.evolved[site], rest.momentum[axis][site])[1] + bracket(rest.state[site], acted)[1]
        momentum_rate = max(momentum_rate, abs(gap))
gradient = all(
    rest.spin(axis, site, rate=True) == -(rest.averaged_diagonal(site) - rest.averaged_diagonal(rest.move(site, axis, -1)))
    for axis in range(3)
    for site in rest.sites
)
curl_of_rate = F(0)
cached_rate = {(axis, site): rest.spin(axis, site, rate=True) for axis in range(3) for site in rest.sites}
for axis in range(3):
    for site in rest.sites:
        total = F(0)
        for (first, second, third), sign in LEVY.items():
            if first == axis:
                total += sign * (cached_rate[(third, site)] - cached_rate[(third, rest.move(site, second, -1))])
        curl_of_rate = max(curl_of_rate, abs(total))
check(
    "B1 instant",
    momentum_rate == 0 and gradient and curl_of_rate == 0 and any(value != 0 for value in cached_rate.values()),
    "at that instant the two-step momentum is still, and the face spin changes only by the diagonal gradient",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. The face-spin balance holds on a rational 5-torus state, and the coin and cosine "
    "identities are the beat that extends it. A real envelope times a fixed spinor sources neither the energy nor "
    "the two-step current. Its shift source is one quarter of the curl of the face spin, and on the 6-torus the "
    "static solution is the lattice vector potential of wbar S~/(16 alpha), divergence-free. The spin changes only "
    "by a gradient at that instant, so the curl source is momentarily still. Block 136's Fourier constraint is read "
    "as this lattice equation; the later spreading of the walker is not computed.",
    flush=True,
)
print(
    "HIT: confirmed - the face spin balances an isotropic diagonal current against the antisymmetric two-step stress, "
    "and a spin-polarised walker at rest sources only the shift, whose static field is the vector potential of "
    "wbar S~/(16 alpha)",
    flush=True,
)
