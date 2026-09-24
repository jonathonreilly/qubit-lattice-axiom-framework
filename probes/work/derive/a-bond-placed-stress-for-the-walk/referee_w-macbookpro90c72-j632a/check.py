#!/usr/bin/env python3
"""Independent referee for a-bond-placed-stress-for-the-walk a3.

The bond current is conserved, but a uniform bond strain is a metric only at
B = 0, and the symmetric part fails on an exact stationary state. Does not
import the attempt.
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


class C:
    def __init__(self, re=0, im=0):
        self.re = re if isinstance(re, F) else F(re)
        self.im = im if isinstance(im, F) else F(im)

    def __add__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        other = other if isinstance(other, C) else C(other)
        return C(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        if not isinstance(other, C):
            return C(self.re * other, self.im * other)
        return C(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return C(-self.re, -self.im)

    def conj(self):
        return C(self.re, -self.im)

    def __eq__(self, other):
        other = other if isinstance(other, C) else C(other)
        return self.re == other.re and self.im == other.im

    def zero(self):
        return self.re == 0 and self.im == 0


I = C(0, 1)
Z = C()


def sigma(axis, spin):
    u, v = spin
    if axis == 0:
        return (v, u)
    if axis == 1:
        return (C(0, -1) * v, C(0, 1) * u)
    return (u, -v)


def dot(left, right):
    return left[0].conj() * right[0] + left[1].conj() * right[1]


def add_spin(left, right):
    return (left[0] + right[0], left[1] + right[1])


def scale_spin(spin, factor):
    return (factor * spin[0], factor * spin[1])


class Torus:
    def __init__(self, dims):
        self.dims = dims
        self.sites = list(itertools.product(*(range(n) for n in dims)))

    def shift(self, site, axis, step=1):
        q = list(site)
        q[axis] = (q[axis] + step) % self.dims[axis]
        return tuple(q)

    def S(self, psi, axis):
        out = {}
        for site in self.sites:
            forward = psi[self.shift(site, axis, 1)]
            back = psi[self.shift(site, axis, -1)]
            out[site] = scale_spin(add_spin(forward, scale_spin(back, -1)), C(0, F(-1, 2)))
        return out

    def H(self, psi):
        out = {site: (Z, Z) for site in self.sites}
        for axis in range(3):
            moved = self.S(psi, axis)
            for site in self.sites:
                out[site] = add_spin(out[site], sigma(axis, moved[site]))
        return out

    def current(self, psi, bond, momentum, phi=None):
        if phi is None:
            phi = self.S(psi, momentum)
        out = {}
        for site in self.sites:
            nxt = self.shift(site, bond, 1)
            term = dot(psi[nxt], sigma(bond, phi[site])) + dot(phi[nxt], sigma(bond, psi[site]))
            out[site] = C(term.re / 2, 0)
        return out

    def back_sum(self, field, axis):
        return {site: field[site] - field[self.shift(site, axis, -1)] for site in self.sites}


def continuity(torus, psi) -> bool:
    evolved = torus.H(psi)
    for momentum in range(3):
        phi = torus.S(psi, momentum)
        phi_evolved = torus.H(phi)
        direct = {}
        for site in torus.sites:
            # Im(psi† H phi - (H psi)† phi)
            mixed = dot(psi[site], phi_evolved[site]) - dot(evolved[site], phi[site])
            direct[site] = mixed.im
        acc = {site: C() for site in torus.sites}
        for bond in range(3):
            jay = torus.current(psi, bond, momentum, phi)
            div = torus.back_sum(jay, bond)
            for site in torus.sites:
                acc[site] = acc[site] + div[site]
        for site in torus.sites:
            if direct[site] + acc[site].re != 0:
                return False
    return True


def plane(dims, spin, momentum):
    # momentum components are multiples of pi/2, stored as integers 0.. 
    phases = {0: C(1), 1: I, 2: C(-1), 3: C(0, -1)}
    psi = {}
    for site in itertools.product(*(range(n) for n in dims)):
        phase = C(1)
        for axis, component in enumerate(momentum):
            phase = phase * phases[(component * site[axis]) % 4]
        psi[site] = scale_spin(spin, phase)
    return psi


def add_state(left, right):
    return {site: add_spin(left[site], right[site]) for site in left}


box = Torus((4, 4, 4))
witness = add_state(plane((4, 4, 4), (C(1), C(1)), (1, 0, 0)), plane((4, 4, 4), (C(1), I), (0, 1, 0)))
eigen = all(box.H(witness)[site] == witness[site] for site in box.sites)
div_zero = True
torque_values = set()
for momentum in range(3):
    acc = {site: C() for site in box.sites}
    transposed = {site: C() for site in box.sites}
    for bond in range(3):
        jay = box.current(witness, bond, momentum)
        for site, value in box.back_sum(jay, bond).items():
            acc[site] = acc[site] + value
        swapped = box.current(witness, momentum, bond)
        for site, value in box.back_sum(swapped, bond).items():
            transposed[site] = transposed[site] + value
    div_zero = div_zero and all(value.re == 0 and value.im == 0 for value in acc.values())
    torque_values |= {value.re for value in transposed.values()}
check(
    "C2 witness",
    eigen and continuity(box, witness) and div_zero and torque_values == {F(-2), F(0), F(2)},
    "the two-wave state is an exact energy-1 eigenstate, its current is conserved, and the transposed divergence is in {-2,0,2}",
)

small = Torus((2, 2, 2))
probe = {site: (Z, Z) for site in small.sites}
probe[(0, 0, 0)] = (C(1), C(0, 1))
probe[(1, 0, 0)] = (C(2), C(-1))
check(
    "A1 continuity",
    continuity(small, probe) and continuity(box, witness),
    "the continuity equation holds on a non-stationary 2-torus state and on the witness",
)

# Uniform strain: (sum sigma_a V_a)^2 = |V|^2, and flipping one cosine changes it by 4 s c (B s).
sa, sb, sc, ca, cb, cc = sp.symbols("s_a s_b s_c c_a c_b c_c", real=True)
B = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"B{i}{j}"))
s = sp.Matrix([sa, sb, sc])
c = sp.Matrix([ca, cb, cc])
V = sp.Matrix([s[i] + c[i] * (B.row(i) * s)[0] for i in range(3)])
paul = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
packed = sum((V[i] * paul[i] for i in range(3)), sp.zeros(2))
square = sp.simplify(packed * packed - sp.eye(2) * (V.dot(V)))
flipped = V.copy()
flipped[0] = s[0] - c[0] * (B.row(0) * s)[0]
delta = sp.factor(sp.simplify(V.dot(V) - flipped.dot(flipped)))
check(
    "B2 not a metric",
    square == sp.zeros(2) and delta == 4 * sa * ca * (B.row(0) * s)[0],
    "a uniform bond strain squares to |V|^2, and k_a -> pi - k_a changes it by 4 s_a c_a (B s)_a",
)

# Re-weighting at q = (0, 3*pi/2, pi/2). Momenta are integers mod 4, in units of pi/2.
SIN = (0, 1, 0, -1)
q = (0, 3, 1)
rows = []
for n in itertools.product(range(4), repeat=3):
    if sum(SIN[t] ** 2 for t in n) != 1:
        continue
    other = tuple((n[a] - q[a]) % 4 for a in range(3))
    if sum(SIN[t] ** 2 for t in other) != 1:
        continue
    both = [SIN[n[a]] + SIN[other[a]] for a in range(3)]
    if both[1] == 0 and both[2] == 0:
        continue
    rows.append(both[1:])
rank = sp.Matrix(rows).rank() if rows else 0
check(
    "C5 no reweighting",
    rank == 2 and len(rows) >= 2,
    "at q=(0, 3pi/2, pi/2) the equal-energy pairs force the two nonzero Fourier weights to vanish",
)

# Coin rotation: H[theta] = H + (1/2) sum_j {(theta x e_j).sigma, S_j} + (1/2) sum_a C_a[d_a theta_a].
# (e_c x e_j)_b = eps_bcj. Response must equal (1/2) d(psi† sigma_c psi)/dt = -Im((H psi)† sigma_c psi).
LEV = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def hop_average(torus, axis, weight, psi):
    out = {}
    for site in torus.sites:
        forward = psi[torus.shift(site, axis, 1)]
        back = psi[torus.shift(site, axis, -1)]
        back_weight = weight[torus.shift(site, axis, -1)]
        mixed = add_spin(scale_spin(forward, weight[site]), scale_spin(back, back_weight))
        out[site] = scale_spin(mixed, F(1, 2))
    return out


def coin_response(torus, psi, axis, site):
    acc = C()
    for momentum in range(3):
        for bond in range(3):
            sign = LEV.get((bond, axis, momentum), 0)
            if sign == 0:
                continue
            moved = torus.S(psi, momentum)
            left = {s: (Z, Z) for s in torus.sites}
            left[site] = sigma(bond, moved[site])
            masked = {s: (Z, Z) for s in torus.sites}
            masked[site] = sigma(bond, psi[site])
            right = torus.S(masked, momentum)
            for point in torus.sites:
                acc = acc + dot(psi[point], add_spin(left[point], right[point])) * F(sign, 2)
    twist = {s: F(0) for s in torus.sites}
    twist[site] = F(-1)
    twist[torus.shift(site, axis, -1)] = twist[torus.shift(site, axis, -1)] + F(1)
    hopped = hop_average(torus, axis, twist, psi)
    for point in torus.sites:
        acc = acc + dot(psi[point], hopped[point]) * F(1, 2)
    return acc


def spin_rate(torus, psi, axis, site):
    evolved = torus.H(psi)
    return -dot(evolved[site], sigma(axis, psi[site])).im


coin_matches = True
for axis in range(3):
    for site in small.sites:
        response = coin_response(small, probe, axis, site)
        coin_matches = coin_matches and response.im == 0 and response.re == spin_rate(small, probe, axis, site)
witness_coin = all(coin_response(box, witness, axis, site) == 0 for axis in range(3) for site in box.sites)
torque_seen = False
for bond in range(3):
    for momentum in range(3):
        direct = box.current(witness, bond, momentum)
        swapped = box.current(witness, momentum, bond)
        torque_seen = torque_seen or any(direct[site] != swapped[site] for site in box.sites)
check(
    "D2 coin rotation",
    coin_matches and witness_coin and torque_seen,
    "the coin-rotation response equals the spin-density derivative, hence vanishes on the witness, whose bond torque does not",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed no-go for a metric member. The bond current is conserved exactly. A uniform bond strain "
    "has H[B]^2 = |V|^2, which depends on cos k as well as sin k, so it is a metric form g(s) only at B = 0. "
    "On the stationary two-wave state the current divergence vanishes while the transposed divergence takes the "
    "values -2, 0 and 2. No translation-invariant reweighting removes that q-component. A coin rotation, whose "
    "response is the time derivative of the spin density, is zero on this state and cannot cancel the torque.",
    flush=True,
)
print(
    "HIT: confirmed - bond placement conserves momentum, but the symmetric metric member fails by the bond torque, "
    "and the failure is not removed by a translation-invariant reweighting",
    flush=True,
)
