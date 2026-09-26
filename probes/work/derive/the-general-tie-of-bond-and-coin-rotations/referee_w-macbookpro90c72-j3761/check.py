#!/usr/bin/env python3
"""Independent referee for the bond-coin tie at reach two.

The constraint rows are rebuilt from the plane-wave symbol and reduced
mod two primes. The attempt's script is not imported. Reach three is
not rebuilt.
"""
from __future__ import annotations

import itertools

import numpy as np
import sympy as sp

FAILS: list[str] = []
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


def primes(count: int) -> list[int]:
    found = []
    candidate = 1 << 20
    while len(found) < count:
        if candidate % 120 == 1 and sp.isprime(candidate):
            found.append(candidate)
        candidate += 1
    return found


def embed(prime: int) -> dict:
    root = {value: int(sp.sqrt_mod(value if value != -1 else prime - 1, prime)) for value in (2, 3, 5)}
    root[-1] = int(sp.sqrt_mod(prime - 1, prime))
    inverse = pow(root[2], prime - 2, prime)
    zeta8 = (1 + root[-1]) * inverse % prime
    zeta6 = (1 + root[-1] * root[3]) * pow(2, prime - 2, prime) % prime
    return {"i": root[-1], "2": root[2], "3": root[3], "5": root[5], "z8": zeta8, "z6": zeta6}


def taxicab(point) -> int:
    return sum(abs(coordinate) for coordinate in point)


def stencil(reach: int):
    windows = []
    for axis, step in enumerate(AXES):
        sites = []
        for offset in itertools.product(range(-reach, reach + 2), repeat=3):
            other = tuple(offset[i] - step[i] for i in range(3))
            if min(taxicab(offset), taxicab(other)) <= reach:
                sites.append(offset)
        windows.append(sites)
    columns = [(axis, component, offset) for axis in range(3) for component in range(3) for offset in windows[axis]]
    return windows, columns


def ball(reach: int):
    if reach == 1:
        return [(0, 0, 0)] + [tuple(sign * AXES[axis][i] for i in range(3)) for axis in range(3) for sign in (1, -1)]
    return [offset for offset in itertools.product(range(-reach, reach + 1), repeat=3) if taxicab(offset) <= reach]


def relabel_matrix(columns, reach: int, prime: int) -> np.ndarray:
    index = {column: position for position, column in enumerate(columns)}
    rows = []
    for component in range(3):
        for shift in ball(reach):
            row = np.zeros(len(columns), dtype=np.int64)
            for axis, step in enumerate(AXES):
                ahead = tuple(step[i] + shift[i] for i in range(3))
                row[index[(axis, component, ahead)]] += 1
                row[index[(axis, component, shift)]] -= 1
            rows.append(row % prime)
    return np.array(rows, dtype=np.int64)


def sigma(prime: int, unit: int) -> np.ndarray:
    return np.array(
        [
            [[0, 1], [1, 0]],
            [[0, (prime - unit) % prime], [unit, 0]],
            [[1, 0], [0, prime - 1]],
        ],
        dtype=np.int64,
    )


def amplitude(length: int, prime: int, data: dict) -> dict:
    half = pow(2, prime - 2, prime)
    quarter = pow(4, prime - 2, prime)
    table = {0: 0}
    plane = {
        1: pow(data["2"], prime - 2, prime),
        2: 1,
        3: data["3"] * pow(data["2"], prime - 2, prime) % prime,
        4: data["2"],
        5: data["5"] * pow(data["2"], prime - 2, prime) % prime,
        6: data["3"],
    }
    for mass in range(1, 7):
        table[mass * half % prime] = plane[mass]
    for count in range(1, 4):
        cube = {1: data["3"] * half % prime, 2: data["2"] * data["3"] * half % prime, 3: 3 * half % prime}
        table[3 * count * quarter % prime] = cube[count]
        table.setdefault(count % prime, {1: 1, 2: data["2"], 3: data["3"]}[count])
    return table


class Reducer:
    def __init__(self, width: int, prime: int):
        self.prime = prime
        self.basis = np.zeros((0, width), dtype=np.int64)
        self.pivots: list[int] = []

    def add(self, rows: np.ndarray) -> None:
        prime = self.prime
        rows = rows % prime
        if self.pivots:
            coeff = rows[:, self.pivots].astype(np.float64)
            product = np.rint(coeff @ self.basis.astype(np.float64)).astype(np.int64)
            rows = (rows - product) % prime
        alive = rows[np.nonzero(rows.any(axis=1))[0]]
        while alive.shape[0]:
            leading = alive[0]
            column = int(np.nonzero(leading)[0][0])
            scale = pow(int(leading[column]), prime - 2, prime)
            reduced = leading * scale % prime
            if self.pivots:
                self.basis = (self.basis - np.outer(self.basis[:, column], reduced)) % prime
            self.basis = np.vstack([self.basis, reduced])
            self.pivots.append(column)
            alive = (alive - np.outer(alive[:, column], reduced)) % prime
            alive = alive[np.nonzero(alive.any(axis=1))[0]]


def constraint_rows(length: int, columns, prime: int, data: dict, chunk: int = 4000):
    phase = {4: data["i"], 6: data["z6"], 8: data["z8"]}[length]
    powers = np.array([pow(phase, exponent, prime) for exponent in range(length)], dtype=np.int64)
    unit = data["i"]
    inverse_two_i = pow(2 * unit % prime, prime - 2, prime)

    def sine(index: int) -> int:
        return (int(powers[index % length]) - int(powers[(-index) % length])) * inverse_two_i % prime

    shells: dict[int, list] = {}
    for momentum in itertools.product(range(length), repeat=3):
        values = [sine(component) for component in momentum]
        key = sum(value * value for value in values) % prime
        shells.setdefault(key, []).append(momentum)
    roots = amplitude(length, prime, data)
    pauli = sigma(prime, unit)
    identity = np.eye(2, dtype=np.int64)
    offsets = np.array([offset for _axis, _component, offset in columns], dtype=np.int64)
    bond = np.array([axis for axis, _component, _offset in columns])
    current = np.array([component for _axis, component, _offset in columns])
    for key, momenta in shells.items():
        root = roots[key]
        if root * root % prime != key:
            raise RuntimeError("amplitude is not a square root of the shell")
        wave = np.array(momenta, dtype=np.int64)
        spins = np.array([[sine(component) for component in momentum] for momentum in momenta], dtype=np.int64)
        forward = np.array([[int(powers[component]) for component in momentum] for momentum in momenta], dtype=np.int64)
        backward = np.array([[int(powers[(-component) % length]) for component in momentum] for momentum in momenta], dtype=np.int64)
        branches = [None] if key == 0 else [root, (prime - root) % prime]
        for branch in branches:
            if branch is None:
                projector = np.broadcast_to(identity, (len(momenta), 2, 2)).copy()
            else:
                projector = (branch * identity[None] + np.einsum("na,aij->nij", spins, pauli)) % prime
            pairs = [(left, right) for left in range(len(momenta)) for right in range(len(momenta))]
            for start in range(0, len(pairs), chunk):
                chosen = np.array(pairs[start : start + chunk])
                left, right = chosen[:, 0], chosen[:, 1]
                transfer = (wave[right] - wave[left]) % length
                phase_row = powers[(-(transfer @ offsets.T)) % length]
                weight = phase_row * ((forward[right][:, bond] + backward[left][:, bond]) % prime) % prime
                weight = weight * ((spins[right][:, current] + spins[left][:, current]) % prime) % prime
                coupled = np.einsum("mij,ajk->maik", projector[left], pauli) % prime
                coupled = np.einsum("maik,mkl->mail", coupled, projector[right]) % prime
                selected = coupled[:, bond]
                for row_entry, column_entry in ((0, 0), (0, 1), (1, 0), (1, 1)):
                    yield weight * selected[:, :, row_entry, column_entry] % prime


def run(length: int, reach: int, prime: int, data: dict):
    windows, columns = stencil(reach)
    gauge = relabel_matrix(columns, reach, prime)
    reducer = Reducer(len(columns), prime)
    rows = 0
    violations = 0
    gauge_float = gauge.T.astype(np.float64)
    for block in constraint_rows(length, columns, prime, data):
        rows += block.shape[0]
        product = np.rint(block.astype(np.float64) @ gauge_float).astype(np.int64) % prime
        violations += int(np.count_nonzero(product))
        if len(reducer.pivots) < len(columns):
            reducer.add(block)
    lifted = [[int(entry) if entry < prime // 2 else int(entry) - prime for entry in row] for row in gauge]
    exact_rank = sp.Matrix(lifted).rank()
    span = max(max(site) - min(site) for site in zip(*windows[0]))
    return {
        "unknowns": len(columns),
        "rows": rows,
        "rank": len(reducer.pivots),
        "gauge": exact_rank,
        "violations": violations,
        "sizes": [len(window) for window in windows],
        "span": span,
    }


def main():
    found = primes(2)
    check(
        "primes",
        found[0] == 1048681 and all(prime % 120 == 1 for prime in found) and all(prime * prime * 400 < 2**53 for prime in found),
        f"the first prime is {found[0]}, and both dot products of the elimination stay inside the exact float range",
    )
    data = [embed(prime) for prime in found]
    embedded = data[0]
    check(
        "embedding",
        pow(embedded["i"], 2, found[0]) == found[0] - 1
        and pow(embedded["2"], 2, found[0]) == 2
        and pow(embedded["3"], 2, found[0]) == 3
        and pow(embedded["5"], 2, found[0]) == 5
        and pow(embedded["z8"], 8, found[0]) == 1
        and pow(embedded["z8"], 4, found[0]) == found[0] - 1,
        "i, sqrt2, sqrt3 and sqrt5 embed, and zeta8 is primitive",
    )
    reach_one = run(4, 1, found[0], data[0])
    reach_one_six = run(6, 1, found[0], data[0])
    reach_one_eight = run(8, 1, found[0], data[0])
    check(
        "reach one",
        reach_one["unknowns"] == 108
        and reach_one["gauge"] == 21
        and reach_one["rank"] == 81
        and reach_one_six["rank"] == 87
        and reach_one_eight["rank"] == 87
        and reach_one["violations"] == reach_one_six["violations"] == reach_one_eight["violations"] == 0,
        f"ranks {reach_one['rank']}, {reach_one_six['rank']}, {reach_one_eight['rank']} on 4^3, 6^3, 8^3",
    )
    reached = [run(8, 2, prime, datum) for prime, datum in zip(found, data)]
    same = all(item["rank"] == reached[0]["rank"] and item["violations"] == 0 for item in reached)
    head = reached[0]
    check(
        "reach two",
        same
        and head["sizes"] == [38, 38, 38]
        and head["unknowns"] == 342
        and head["gauge"] == 75
        and head["rank"] == 267
        and head["span"] <= 5,
        f"38 sites, rank {head['rank']} on primes {found}, gauge rank {head['gauge']}, "
        f"rows {head['rows']}, stencil span {head['span']}",
    )
    if FAILS:
        print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
        return 1
    print(
        "SUMMARY: confirmed partial. At reach two on the 8^3 torus the constraint rank is 267 out of 342 "
        "over two primes, and the 75 relabelling ties are independent and lie in the kernel. The solution "
        "space is exactly those relabellings. Reach three was not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - at reach two the ties with vanishing current adjoint are exactly the relabelling "
        "ties on the radius-two ball, 75 per component, so the nine-plus-three variables stay forced",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
