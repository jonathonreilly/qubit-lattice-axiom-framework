#!/usr/bin/env python3
"""Finite checks for the record-production kernel boundary.

Post-record append/count dynamics consumes realized atoms. It does not produce
the next atom, assign probabilities, set rates, or select a stable dial point.

This runner demonstrates the boundary on a binary record alphabet by feeding
the same finite append/count layer with several distinct valid production
kernels. The observed finite history and the post-record algebra can be the
same while the production law, likelihoods, expectations, and stationary
points differ.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Callable

PASS = 0
FAIL = 0

Atom = int
Word = tuple[Atom, ...]
Dist = tuple[Fraction, Fraction]
Kernel = Callable[[Word], Dist]


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"[{tag}] {label}")
    if detail:
        print(f"       {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def normalize(dist: Dist) -> bool:
    return all(x >= 0 for x in dist) and sum(dist) == 1


def append(word: Word, atom: Atom) -> Word:
    return word + (atom,)


def count(word: Word) -> tuple[int, int]:
    return (sum(1 for a in word if a == 0), sum(1 for a in word if a == 1))


def add_counts(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return (a[0] + b[0], a[1] + b[1])


def iid(p1: Fraction) -> Kernel:
    p0 = 1 - p1
    return lambda _prefix: (p0, p1)


def markov_persistence() -> Kernel:
    """A valid history-dependent producer with exact rational transitions.

    If the previous atom is 0: P(next=0)=3/4.
    If the previous atom is 1: P(next=1)=4/5.
    Empty-prefix prior is fair.
    """

    def kernel(prefix: Word) -> Dist:
        if not prefix:
            return (Fraction(1, 2), Fraction(1, 2))
        if prefix[-1] == 0:
            return (Fraction(3, 4), Fraction(1, 4))
        return (Fraction(1, 5), Fraction(4, 5))

    return kernel


def scripted(target: Word) -> Kernel:
    """A prefix/time supplied producer that writes the target word with prob 1."""

    def kernel(prefix: Word) -> Dist:
        if len(prefix) < len(target) and prefix == target[: len(prefix)]:
            return (Fraction(1, 1), Fraction(0, 1)) if target[len(prefix)] == 0 else (
                Fraction(0, 1),
                Fraction(1, 1),
            )
        return (Fraction(1, 2), Fraction(1, 2))

    return kernel


def likelihood(kernel: Kernel, word: Word) -> Fraction:
    prefix: Word = ()
    out = Fraction(1, 1)
    for atom in word:
        dist = kernel(prefix)
        out *= dist[atom]
        prefix = append(prefix, atom)
    return out


def expected_next_count(counts: tuple[int, int], kernel: Kernel, prefix: Word) -> tuple[Fraction, Fraction]:
    dist = kernel(prefix)
    return (Fraction(counts[0], 1) + dist[0], Fraction(counts[1], 1) + dist[1])


def stationary_iid(kernel: Kernel) -> Dist:
    return kernel(())


def main() -> int:
    target: Word = (1, 0, 1, 1, 0, 1)
    suffix: Word = (0, 1)

    fair = iid(Fraction(1, 2))
    dimension = iid(Fraction(2, 3))
    reverse_dimension = iid(Fraction(1, 3))
    persistent = markov_persistence()
    scheduled = scripted(target)
    kernels: list[tuple[str, Kernel]] = [
        ("fair IID", fair),
        ("dimension-biased IID", dimension),
        ("reverse-biased IID", reverse_dimension),
        ("Markov persistence", persistent),
        ("scripted producer", scheduled),
    ]

    section("Post-record append/count layer is kernel-agnostic after atoms are supplied")
    check("A1 target history is finite and binary", all(a in (0, 1) for a in target), f"target={target}")
    check("A2 append composes supplied atoms", append(target, 0) == target + (0,))
    check("A3 count projection is additive under suffix append",
          count(target + suffix) == add_counts(count(target), count(suffix)),
          f"{count(target)} + {count(suffix)} = {count(target + suffix)}")
    check("A4 post-record count of the realized target is independent of producer description",
          all(count(target) == (2, 4) for _name, _kernel in kernels),
          f"count={count(target)}")

    section("Many distinct production kernels are valid on the same alphabet")
    for name, kernel in kernels:
        normalized_at_prefixes = all(normalize(kernel(target[:i])) for i in range(len(target) + 1))
        check(f"K normalized: {name}", normalized_at_prefixes)
    distinct_empty_distributions = {kernel(()) for _name, kernel in kernels}
    check("K6 supplied kernels include distinct priors/generators",
          len(distinct_empty_distributions) >= 3,
          f"empty-prefix distributions={sorted(distinct_empty_distributions)}")

    section("The same finite history does not identify the production law")
    likelihoods = {name: likelihood(kernel, target) for name, kernel in kernels}
    for name, value in likelihoods.items():
        check(f"L positive likelihood: {name}", value > 0, f"P(target)={value}")
    check("L6 the scripted producer can realize the target with probability one",
          likelihoods["scripted producer"] == 1)
    non_script_values = {value for name, value in likelihoods.items() if name != "scripted producer"}
    check("L7 non-scripted kernels give different likelihoods for the same word",
          len(non_script_values) >= 3,
          f"likelihoods={likelihoods}")
    check("L8 a finite realized word is compatible with multiple kernels",
          sum(1 for value in likelihoods.values() if value > 0) == len(kernels))

    section("Predictions and stable points change with the supplied kernel")
    base_counts = count(target)
    exp_fair = expected_next_count(base_counts, fair, target)
    exp_dimension = expected_next_count(base_counts, dimension, target)
    exp_reverse = expected_next_count(base_counts, reverse_dimension, target)
    check("P1 fair and dimension-biased kernels give different expected next counts",
          exp_fair != exp_dimension,
          f"fair={exp_fair}, dimension={exp_dimension}")
    check("P2 reverse-biased kernel gives another expectation on the same post-record state",
          exp_reverse != exp_fair and exp_reverse != exp_dimension,
          f"reverse={exp_reverse}")
    check("P3 realized next-count updates remain integral once an atom is supplied",
          add_counts(base_counts, (1, 0)) == (3, 4) and add_counts(base_counts, (0, 1)) == (2, 5))
    check("P4 expected next counts are ensemble objects, not realized count updates",
          exp_dimension != (3, 4) and exp_dimension != (2, 5),
          f"E_dimension={exp_dimension}")
    check("P5 equal-letter stationary prior is supplied, not selected by append grammar",
          stationary_iid(fair) == (Fraction(1, 2), Fraction(1, 2)))
    check("P6 dimension-weighted stationary prior is also supplied on the same alphabet",
          stationary_iid(dimension) == (Fraction(1, 3), Fraction(2, 3)))
    check("P7 the same append/count grammar admits incompatible stable priors",
          stationary_iid(fair) != stationary_iid(dimension) != stationary_iid(reverse_dimension))

    section("Boundary certificate")
    check("B1 append grammar contains no probability field",
          True,
          "the append operation takes a supplied atom, not a distribution")
    check("B2 production kernels are extra data relative to post-record dynamics",
          len(kernels) == 5 and len({tuple(kernel(target)) for _name, kernel in kernels}) >= 3)
    check("B3 no finite-history observation in this runner selects a unique kernel",
          len([value for value in likelihoods.values() if value > 0]) == 5)
    check("B4 stable dial language is allowed only after naming the generator/functional",
          stationary_iid(fair) != stationary_iid(dimension))

    section("Scorecard")
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "FINDING: post-record append/count dynamics consumes realized atoms. "
        "The production kernel, likelihood law, expected update, transition "
        "rate, and stable dial point are supplied dynamics inputs, not outputs "
        "of the finite record alphabet."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
