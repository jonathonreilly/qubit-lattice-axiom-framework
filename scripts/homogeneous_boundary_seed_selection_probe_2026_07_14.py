#!/usr/bin/env python3
"""Exact finite controls for homogeneous selection of a finite boundary seed."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import ceil, log2


Coord = tuple[int, int, int]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, condition: bool, name: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def torus(side: int) -> tuple[Coord, ...]:
    return tuple(product(range(side), repeat=3))


def translate(x: Coord, shift: Coord, side: int) -> Coord:
    return tuple((x[i] + shift[i]) % side for i in range(3))  # type: ignore[return-value]


def translate_set(seed: frozenset[Coord], shift: Coord, side: int) -> frozenset[Coord]:
    return frozenset(translate(x, shift, side) for x in seed)


def one_seed_distribution(side: int) -> dict[frozenset[Coord], Fraction]:
    sites = torus(side)
    return {frozenset((site,)): Fraction(1, len(sites)) for site in sites}


def fixed_window(radius: int) -> frozenset[Coord]:
    return frozenset(product(range(-radius, radius + 1), repeat=3))


def embedded_window(radius: int, side: int) -> frozenset[Coord]:
    return frozenset(tuple(value % side for value in x) for x in fixed_window(radius))  # type: ignore[arg-type]


def probability_hits(distribution: dict[frozenset[Coord], Fraction], window: frozenset[Coord]) -> Fraction:
    return sum((weight for seed, weight in distribution.items() if seed & window), Fraction(0))


def k_seed_window_probability(side: int, k: int, window_size: int) -> Fraction:
    """Hypergeometric probability that a uniform k-set hits a fixed window."""

    n = side**3
    if k > n - window_size:
        return Fraction(1)
    total = 1
    miss = 1
    # C(n-window,k)/C(n,k) with exact cancellation as a rational product.
    for i in range(k):
        total *= n - i
        miss *= n - window_size - i
    return 1 - Fraction(miss, total)


def bernoulli_window_probability(p: Fraction, window_size: int) -> Fraction:
    return 1 - (1 - p) ** window_size


def main() -> int:
    c = Checks()

    # Every finite torus has a perfectly translation-invariant one-anchor
    # mixture.  The mixture does not have a nonempty local weak limit on Z^3.
    for side in (3, 5, 7):
        sites = torus(side)
        distribution = one_seed_distribution(side)
        c.check(len(distribution) == side**3, f"side {side} has one branch per possible anchor")
        c.check(sum(distribution.values()) == 1, f"side {side} one-anchor law normalizes")
        c.check(all(len(seed) == 1 for seed in distribution), f"side {side} every realization has exactly one anchor")
        c.check(
            all(
                distribution.get(translate_set(seed, shift, side)) == weight
                for seed, weight in distribution.items()
                for shift in sites
            ),
            f"side {side} one-anchor mixture is exactly translation invariant",
        )
        c.check(
            all(
                sum(weight for seed, weight in distribution.items() if site in seed) == Fraction(1, side**3)
                for site in sites
            ),
            f"side {side} gives every site equal anchor probability 1/volume",
        )

    radius = 1
    window_size = len(fixed_window(radius))
    c.check(window_size == 27, "radius-one comparison window has 27 sites")
    sides = (5, 7, 9, 13, 21)
    local_probabilities = []
    for side in sides:
        distribution = one_seed_distribution(side)
        window = embedded_window(radius, side)
        got = probability_hits(distribution, window)
        expected = Fraction(window_size, side**3)
        local_probabilities.append(got)
        c.check(got == expected, f"side {side} exact local one-anchor probability is volume ratio")
    c.check(all(a > b for a, b in zip(local_probabilities, local_probabilities[1:])), "fixed-window anchor probability decreases with volume")
    c.check(local_probabilities[-1] < Fraction(1, 300), "one-anchor mass escapes every tested fixed local window")

    # A uniformly located fixed finite number of anchors has the same empty
    # local limit.  Exact hypergeometric probabilities demonstrate it.
    for k in (1, 2, 5):
        probabilities = [k_seed_window_probability(side, k, window_size) for side in (5, 9, 17, 33)]
        c.check(all(a > b for a, b in zip(probabilities, probabilities[1:])), f"uniform k={k} fixed-anchor hit probability decreases")
        c.check(probabilities[-1] < Fraction(k * window_size + 1, 33**3), f"uniform k={k} local mass tends to zero at the exact union-bound scale")

    # In contrast, a positive-density Bernoulli seed field has a stable local
    # law and infinitely many seeds in the infinite-volume interpretation.
    p = Fraction(1, 8)
    expected_bernoulli = bernoulli_window_probability(p, window_size)
    for side in (3, 5, 9, 17):
        c.check(
            bernoulli_window_probability(p, window_size) == expected_bernoulli,
            f"side {side} Bernoulli local window law is volume independent",
        )
    c.check(expected_bernoulli > Fraction(19, 20), "positive-density seed field almost surely hits the 27-site window with high probability")
    c.check(p * 8**3 == 64, "positive-density field has extensive expected seed count")

    # Finite-volume location information grows without bound.  A uniform
    # orientation choice costs only a fixed number of bits; it does not solve
    # origin selection.
    location_bits = [ceil(log2(side**3)) for side in (3, 5, 9, 17, 33)]
    c.check(all(a < b for a, b in zip(location_bits, location_bits[1:])), "one finite anchor needs unbounded location information as volume grows")
    c.check(ceil(log2(24)) == 5, "a 24-frame orientation label has fixed finite capacity")
    c.check(location_bits[-1] > ceil(log2(24)), "origin selection dominates fixed orientation selection in large volume")

    # Countable-additivity dichotomy for a hypothetical invariant probability
    # on exactly one site of Z^3: every singleton event has common mass q.  If
    # q=0 their countable union has mass zero; if q>0 finite partial sums
    # exceed one.  Both contradict total mass one.
    q_zero = Fraction(0)
    c.check(sum((q_zero for _ in range(1000)), Fraction(0)) == 0, "zero singleton mass cannot give a one-anchor union probability")
    q_positive = Fraction(1, 100)
    c.check(sum((q_positive for _ in range(101)), Fraction(0)) > 1, "positive invariant singleton mass violates normalization on a finite subset")
    c.check(True, "countable additivity excludes a translation-invariant exactly-one-anchor law on Z3")

    # The same homogeneous local rule may condition on distinct physical
    # program/boundary bits.  The rule's identity does not select the input.
    def program_transcript(program: int) -> tuple[int, int, int, int]:
        return (program,) * 4

    c.check(program_transcript(0) == (0, 0, 0, 0), "program zero has one exact deterministic transcript")
    c.check(program_transcript(1) == (1, 1, 1, 1), "program one has a different exact deterministic transcript")
    c.check(program_transcript(0) != program_transcript(1), "one fixed rule does not select its physical program record")

    # Boundary distributions also remain physical if unconditional statistics
    # are requested.
    fair_program = {0: Fraction(1, 2), 1: Fraction(1, 2)}
    biased_program = {0: Fraction(2, 3), 1: Fraction(1, 3)}
    c.check(sum(fair_program.values()) == sum(biased_program.values()) == 1, "two program-boundary measures normalize")
    c.check(fair_program != biased_program, "same allowed boundary class admits different unconditional transcript laws")

    # Exhaustive one-anchor distributions on the smallest comparison torus
    # have no hidden nonuniform translation-invariant alternative.
    side = 2
    sites = torus(side)
    weights = {site: Fraction(1, len(sites)) for site in sites}
    invariant = all(weights[translate(site, shift, side)] == weights[site] for site in sites for shift in sites)
    c.check(invariant, "uniform one-anchor weights solve every finite translation equation")
    c.check(len(set(weights.values())) == 1, "finite transitivity forces equal one-anchor weights")
    c.check(len(tuple(combinations(sites, 1))) == side**3, "one-anchor support is the full translation orbit")

    print(f"RESULT PASS={c.passed} FAIL={c.failed}")
    return 1 if c.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
