#!/usr/bin/env python3
"""Referee for one set of variables for strains and coin rotations, a2.

Author w-macbookpro90c72-j6027 (claude-opus-5-5). Own plane-wave series and an
exact Gaussian-rational sum on the 4^3 torus.
A general linear tie, beyond the forward and shared placements, was not excluded.
"""
import itertools
from fractions import Fraction as Fr

import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


class G:
    def __init__(self, real, imag=0):
        self.real = Fr(real)
        self.imag = Fr(imag)

    def __add__(self, other):
        return G(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return G(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        if isinstance(other, G):
            return G(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)
        return G(self.real * other, self.imag * other)

    def __rmul__(self, other):
        return self * other

    def conj(self):
        return G(self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __repr__(self):
        return f"({self.real}+{self.imag}i)"


def dot(left, right):
    return left[0].conj() * right[0] + left[1].conj() * right[1]


def apply(matrix, spin):
    return (
        matrix[0][0] * spin[0] + matrix[0][1] * spin[1],
        matrix[1][0] * spin[0] + matrix[1][1] * spin[1],
    )


I = G(0, 1)
ZERO = G(0)
ONE = G(1)
SIGMA = [
    ((ZERO, ONE), (ONE, ZERO)),
    ((ZERO, G(0, -1)), (I, ZERO)),
    ((ONE, ZERO), (ZERO, G(-1))),
]


def symbol():
    k, q = sp.symbols("k q", real=True)
    hop = sp.exp(-sp.I * q / 2) * sp.cos(k + q / 2)
    raw_hop = (sp.exp(sp.I * k) + sp.exp(-sp.I * q) * sp.exp(-sp.I * k)) / 2
    sine = sp.sin(k + q / 2) * sp.cos(q / 2)
    raw_sine = (sp.sin(k) + sp.sin(k + q)) / 2
    twist = sp.I * sp.sin(q / 2) * sp.cos(k + q / 2)
    raw_twist = (sp.exp(sp.I * q) - 1) * (sp.exp(sp.I * k) + sp.exp(-sp.I * q) * sp.exp(-sp.I * k)) / 4
    scale = sp.symbols("lam")
    frame = (hop - 1) * sine
    series_frame = sp.series(frame.subs({k: scale * k, q: scale * q}), scale, 0, 4).removeO()
    series_twist = sp.series((-twist).subs({k: scale * k, q: scale * q}), scale, 0, 3).removeO()
    uniform = ((sp.cos(scale * k) - 1) * sp.sin(scale * k))
    series_uniform = sp.series(uniform, scale, 0, 4).removeO()
    ok = (
        sp.simplify(sp.expand_complex(raw_hop - hop)) == 0
        and sp.simplify(sp.expand(raw_sine - sine)) == 0
        and sp.simplify(sp.expand_complex(raw_twist - twist)) == 0
        and series_frame.coeff(scale, 1) == 0
        and series_frame.coeff(scale, 2) != 0
        and sp.simplify(series_twist.coeff(scale, 1) + sp.I * q / 2) == 0
        and series_uniform.coeff(scale, 1) == 0
        and series_uniform.coeff(scale, 2) == 0
        and series_uniform.coeff(scale, 3) != 0
    )
    report(
        "symbol",
        ok,
        "the bond and coin symbols match; a uniform rotation differs at order k^3, and the first order in the rotation's wave vector is -(i/2) theta.q",
    )


def eighth(value):
    return (value.real * 8).denominator == 1


def levi(i, j, k):
    sign = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
    return sign.get((i, j, k), 0)


def torus():
    side = 4
    sites = list(itertools.product(range(side), repeat=3))
    index = {site: i for i, site in enumerate(sites)}
    coins = ((ONE, ONE), (ONE, I), (ONE, ZERO))
    waves = (ONE, I, G(-1), G(0, -1))

    def shift(site, axis, step):
        moved = list(site)
        moved[axis] = (moved[axis] + step) % side
        return index[tuple(moved)]

    psi = [(ZERO, ZERO) for _ in sites]
    for axis, coin in enumerate(coins):
        for site in sites:
            factor = waves[site[axis]]
            psi[index[site]] = (
                psi[index[site]][0] + factor * coin[0],
                psi[index[site]][1] + factor * coin[1],
            )

    def hop(vector, axis, step=1):
        out = [(ZERO, ZERO) for _ in sites]
        for site in sites:
            out[index[site]] = vector[shift(site, axis, step)]
        return out

    def current(axis, vector):
        forward, backward = hop(vector, axis, 1), hop(vector, axis, -1)
        return [((forward[i][0] - backward[i][0]) * G(0, Fr(-1, 2)), (forward[i][1] - backward[i][1]) * G(0, Fr(-1, 2))) for i in range(len(sites))]

    # (a-b)/(2i) = (a-b) * (-i/2)
    streams = [current(axis, psi) for axis in range(3)]
    energy = [(ZERO, ZERO) for _ in sites]
    for axis in range(3):
        for i in range(len(sites)):
            acted = apply(SIGMA[axis], streams[axis][i])
            energy[i] = (energy[i][0] + acted[0], energy[i][1] + acted[1])
    stationary = energy == psi

    theta = [[[dot(psi[i], apply(SIGMA[axis], streams[spin][i])) for i in range(len(sites))] for spin in range(3)] for axis in range(3)]
    bond = []
    for axis in range(3):
        bond.append([])
        for spin in range(3):
            row = []
            for site in sites:
                there = shift(site, axis, 1)
                here = index[site]
                left = dot(psi[there], apply(SIGMA[axis], streams[spin][here]))
                right = dot(streams[spin][there], apply(SIGMA[axis], psi[here]))
                row.append((left + right) * Fr(1, 2))
            bond[-1].append(row)
    link = [[dot(psi[index[site]], psi[shift(site, axis, 1)]) for site in sites] for axis in range(3)]

    def real_part(value):
        return value.real

    coin = []
    forward = []
    shared = []
    for axis in range(3):
        coin.append([])
        forward.append([])
        shared.append([])
        for n, site in enumerate(sites):
            coin_sum = Fr(0)
            forward_sum = Fr(0)
            shared_sum = Fr(0)
            for a in range(3):
                for b in range(3):
                    coin_sum += levi(axis, a, b) * real_part(theta[b][a][n])
                    forward_sum += levi(axis, a, b) * real_part(bond[a][b][n])
                    back = shift(site, a, -1)
                    shared_sum += levi(axis, a, b) * (real_part(bond[a][b][n]) + real_part(bond[a][b][back])) / 2
            coin_sum -= (real_part(link[axis][n]) - real_part(link[axis][shift(site, axis, -1)])) / 2
            coin[-1].append(coin_sum)
            forward[-1].append(forward_sum)
            shared[-1].append(shared_sum)
    def walk(obj):
        if isinstance(obj, G):
            yield obj
        elif isinstance(obj, list):
            for item in obj:
                yield from walk(item)

    exact = all(eighth(item) for item in walk([theta, bond, link]))
    exact &= all((entry * 8).denominator == 1 for row in coin + forward + shared for entry in row)
    coin_zero = all(entry == 0 for row in coin for entry in row)
    forward_sites = sum(1 for n in range(len(sites)) if any(forward[axis][n] != 0 for axis in range(3)))
    shared_sites = sum(1 for n in range(len(sites)) if any(shared[axis][n] != 0 for axis in range(3)))
    report(
        "torus",
        stationary and exact and coin_zero and forward_sites == 64 and shared_sites == 60,
        f"H psi = psi on 4^3; the coin response is 0 at every site, the forward torque is nonzero at {forward_sites}, and the shared torque at {shared_sites}",
    )


def main():
    symbol()
    torus()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - on plane waves the forward-bond rotation and the coin rotation differ by a symbol that is O(k^3) "
        "for a uniform rotation and -(i/2) theta.q at first order in the rotation's wave vector. "
        "On the stationary 4^3 state the coin response is zero at all 64 sites, while the forward torque is nonzero at 64 "
        "and the shared torque at 60. Neither of those two ties is consistent for a field energy blind to theta."
    )
    print(
        "SUMMARY: confirmed the symbol identities, the orders, and the 4^3 responses. "
        "A general linear tie, other than the forward and shared placements, was not excluded."
    )


if __name__ == "__main__":
    main()
