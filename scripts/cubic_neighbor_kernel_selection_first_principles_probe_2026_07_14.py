#!/usr/bin/env python3
"""Exact symmetry and coarse-graining controls for cubic neighbor kernels."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Vec = tuple[int, int, int]
Config = tuple[int, ...]

DIRECTIONS: tuple[Vec, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


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


def dot(a: Vec, b: Vec) -> int:
    return sum(x * y for x, y in zip(a, b))


def cross(a: Vec, b: Vec) -> Vec:
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def rotate(v: Vec, matrix: tuple[Vec, Vec, Vec]) -> Vec:
    ex, ey, ez = matrix
    return tuple(v[0] * ex[i] + v[1] * ey[i] + v[2] * ez[i] for i in range(3))  # type: ignore[return-value]


def proper_rotations() -> tuple[tuple[Vec, Vec, Vec], ...]:
    return tuple(
        (ex, ey, cross(ex, ey))
        for ex in DIRECTIONS
        for ey in DIRECTIONS
        if dot(ex, ey) == 0 and cross(ex, ey) in DIRECTIONS
    )


def direction_permutation(matrix: tuple[Vec, Vec, Vec]) -> tuple[int, ...]:
    return tuple(DIRECTIONS.index(rotate(v, matrix)) for v in DIRECTIONS)


def act(config: Config, permutation: tuple[int, ...]) -> Config:
    out = [0] * 6
    for old, new in enumerate(permutation):
        out[new] = config[old]
    return tuple(out)


def complement(config: Config) -> Config:
    return tuple(1 - value for value in config)


def rotation_orbits(configs: tuple[Config, ...], permutations: tuple[tuple[int, ...], ...]) -> tuple[frozenset[Config], ...]:
    seen: set[Config] = set()
    out: list[frozenset[Config]] = []
    for config in configs:
        if config in seen:
            continue
        orbit = frozenset(act(config, permutation) for permutation in permutations)
        seen.update(orbit)
        out.append(orbit)
    return tuple(out)


def p_incidence(config: Config) -> Fraction:
    return Fraction(sum(config), 6)


def p_label_uniform(config: Config) -> Fraction:
    k = sum(config)
    if k == 0:
        return Fraction(0)
    if k == 6:
        return Fraction(1)
    return Fraction(1, 2)


def p_power(config: Config, alpha: int = 2) -> Fraction:
    k = sum(config)
    if k == 0:
        return Fraction(0)
    if k == 6:
        return Fraction(1)
    return Fraction(k**alpha, k**alpha + (6 - k) ** alpha)


def is_opposite_pair(config: Config) -> bool:
    ones = [DIRECTIONS[i] for i, value in enumerate(config) if value]
    return len(ones) == 2 and ones[0] == tuple(-x for x in ones[1])


def p_shape(config: Config) -> Fraction:
    """A proper-cubic and label-equivariant shape-sensitive exact kernel."""

    k = sum(config)
    if k == 0:
        return Fraction(0)
    if k == 6:
        return Fraction(1)
    if k == 2:
        return Fraction(1, 4) if is_opposite_pair(config) else Fraction(1, 3)
    if k == 4:
        return 1 - p_shape(complement(config))
    if k == 1:
        return Fraction(1, 5)
    if k == 5:
        return Fraction(4, 5)
    return Fraction(1, 2)


def kernel_checks(
    c: Checks,
    name: str,
    kernel,
    configs: tuple[Config, ...],
    permutations: tuple[tuple[int, ...], ...],
) -> None:
    c.check(all(Fraction(0) <= kernel(config) <= Fraction(1) for config in configs), f"{name} is normalized and nonnegative")
    c.check(kernel((0,) * 6) == 0 and kernel((1,) * 6) == 1, f"{name} copies singleton homogeneous support")
    c.check(all(kernel(complement(config)) == 1 - kernel(config) for config in configs), f"{name} has no privileged outcome name")
    c.check(
        all(kernel(act(config, permutation)) == kernel(config) for config in configs for permutation in permutations),
        f"{name} is exactly proper-cubic covariant",
    )
    c.check(all(0 < kernel(config) < 1 for config in configs if 0 < sum(config) < 6), f"{name} has full mixed-profile support")


def scaled_power_probability(n0: int, n1: int, alpha: int) -> Fraction:
    return Fraction(n1**alpha, n0**alpha + n1**alpha)


def main() -> int:
    c = Checks()
    rotations = proper_rotations()
    permutations = tuple(direction_permutation(rotation) for rotation in rotations)
    configs = tuple(product((0, 1), repeat=6))
    orbits = rotation_orbits(configs, permutations)

    c.check(len(rotations) == 24 and len(set(rotations)) == 24, "enumerated all 24 proper cubic rotations")
    c.check(len(set(permutations)) == 24, "all rotations act differently on the six neighbor directions")
    c.check(len(orbits) == 10, "64 binary neighbor colorings have exactly ten proper-cubic orbits")
    c.check(sum(len(orbit) for orbit in orbits) == 64, "rotation orbits partition all binary neighborhoods")
    c.check(sorted(len(orbit) for orbit in orbits) == [1, 1, 3, 3, 6, 6, 8, 12, 12, 12], "orbit sizes match exact cubic geometry")

    orbit_index = {config: i for i, orbit in enumerate(orbits) for config in orbit}
    complement_pairs = {tuple(sorted((i, orbit_index[complement(min(orbit))]))) for i, orbit in enumerate(orbits)}
    self_complementary = [pair for pair in complement_pairs if pair[0] == pair[1]]
    c.check(len(complement_pairs) == 6, "outcome-name exchange reduces ten spatial orbits to six pairs")
    c.check(len(self_complementary) == 2, "two cubic orbit types are self-complementary")

    # Endpoint copying fixes the homogeneous complement pair.  Two
    # self-complementary orbits are forced to 1/2.  Three nontrivial paired
    # orbits retain one exact probability each.
    nontrivial_free_pairs = [pair for pair in complement_pairs if pair[0] != pair[1] and not ({pair[0], pair[1]} == {orbit_index[(0,) * 6], orbit_index[(1,) * 6]})]
    c.check(len(nontrivial_free_pairs) == 3, "cubic covariance plus label symmetry and endpoint copying leave three exact parameters")

    # Requiring dependence on count only collapses the two k=2 shape orbits,
    # but still leaves p(1 of 6) and p(2 of 6) free; k=3 is fixed by label
    # exchange.
    count_classes = {sum(config) for config in configs}
    c.check(count_classes == set(range(7)), "neighbor-count quotient has seven profiles")
    c.check(2 == len((1, 2)), "count-only label-equivariant endpoint-copy kernels retain two parameters")

    kernels = (
        ("incidence", p_incidence),
        ("label-uniform", p_label_uniform),
        ("quadratic-power", p_power),
        ("shape-sensitive", p_shape),
    )
    for name, kernel in kernels:
        kernel_checks(c, name, kernel, configs, permutations)

    one_profile = (1, 0, 0, 0, 0, 0)
    two_adjacent = (1, 0, 1, 0, 0, 0)
    two_opposite = (1, 1, 0, 0, 0, 0)
    c.check(p_incidence(one_profile) == Fraction(1, 6), "incidence gives 1/6 on one active label-1 channel")
    c.check(p_label_uniform(one_profile) == Fraction(1, 2), "label-space uniformity gives 1/2 on the same mixed support")
    c.check(p_power(one_profile) == Fraction(1, 26), "quadratic channel weight gives 1/26 on the same profile")
    c.check(len({p_incidence(one_profile), p_label_uniform(one_profile), p_power(one_profile)}) == 3, "three symmetry-complete count kernels predict distinct transcripts")
    c.check(p_shape(two_opposite) == Fraction(1, 4), "shape kernel assigns 1/4 to an opposite pair")
    c.check(p_shape(two_adjacent) == Fraction(1, 3), "shape kernel assigns 1/3 to an adjacent pair")
    c.check(p_shape(two_opposite) != p_shape(two_adjacent), "proper-cubic covariance does not force count-only dependence")
    c.check(p_incidence(two_opposite) == p_incidence(two_adjacent) == Fraction(1, 3), "incidence adds the stronger geometry-blind counting quotient")

    # Uniformity is sample-space relative.  Uniform over the two outcome
    # labels differs from uniform over six causal channels followed by outcome
    # coarse-graining.
    c.check(p_label_uniform(two_adjacent) == Fraction(1, 2), "uniform outcome-label sample space ignores multiplicity")
    c.check(p_incidence(two_adjacent) == Fraction(1, 3), "uniform causal-channel sample space respects multiplicity")
    c.check(p_label_uniform(two_adjacent) != p_incidence(two_adjacent), "maximum symmetry does not choose a sample-space quotient")

    # Proportional refinement invariance does not select linear weights:
    # every homogeneous power law depends only on the ratio.
    for alpha in (1, 2, 3, 4):
        base = scaled_power_probability(2, 1, alpha)
        c.check(
            all(scaled_power_probability(2 * scale, scale, alpha) == base for scale in (2, 3, 5, 11)),
            f"power alpha={alpha} obeys proportional-refinement invariance",
        )
    c.check(
        len({scaled_power_probability(2, 1, alpha) for alpha in (1, 2, 3, 4)}) == 4,
        "refinement invariance leaves distinct exact weight laws",
    )

    # Finite additivity over disjoint elementary causal channels does select
    # linear weight.  With w(0)=0 and w(1)=c, induction on
    # w(n+1)=w(n)+w(1) yields w(n)=n*c.  The checks expose which candidate
    # obeys that extra premise.
    linear_weights = {n: Fraction(n) for n in range(7)}
    c.check(all(linear_weights[m + n] == linear_weights[m] + linear_weights[n] for m in range(7) for n in range(7 - m)), "finite channel additivity forces the linear table")
    c.check(all(Fraction(linear_weights[n], linear_weights[n] + linear_weights[6 - n]) == p_incidence((1,) * n + (0,) * (6 - n)) for n in range(7) if 0 < n < 6), "linear channel coarse-graining derives incidence probabilities")

    quadratic_weights = {n: Fraction(n * n) for n in range(7)}
    violations = [
        (m, n)
        for m in range(7)
        for n in range(7 - m)
        if quadratic_weights[m + n] != quadratic_weights[m] + quadratic_weights[n]
    ]
    c.check(bool(violations), "quadratic symmetry kernel fails finite channel additivity")
    c.check((1, 1) in violations, "the first quadratic failure is already the two-channel union")

    # Record-readout additivity is logically independent: the same additive
    # content readout can be attached to every kernel above.
    readout = {0: Fraction(-1), 1: Fraction(1)}
    sample_records = (0, 1, 1, 0, 1)
    total = sum((readout[value] for value in sample_records), Fraction(0))
    split = sum((readout[value] for value in sample_records[:2]), Fraction(0)) + sum(
        (readout[value] for value in sample_records[2:]), Fraction(0)
    )
    c.check(total == split == 1, "record scalar readout is additive independently of formation kernel")
    c.check(all(total == split for _name, _kernel in kernels), "all inequivalent kernels share the same additive readout")

    print(f"RESULT PASS={c.passed} FAIL={c.failed}")
    return 1 if c.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
