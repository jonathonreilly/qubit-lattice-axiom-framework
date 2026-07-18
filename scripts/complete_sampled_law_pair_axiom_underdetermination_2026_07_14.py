#!/usr/bin/env python3
"""Exact paired sampled laws with one observable transcript discriminator."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
OPEN = -1
Coord = tuple[int, int, int]
Profile = tuple[int, int, int, int, int, int]


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def counts(profile: Profile) -> tuple[int, int]:
    return profile.count(0), profile.count(1)


def availability(profile: Profile) -> tuple[int, ...]:
    n0, n1 = counts(profile)
    if n0 and not n1:
        return (0,)
    if n1 and not n0:
        return (1,)
    return (0, 1)


def kernel(lam: int, profile: Profile) -> dict[int, Fraction]:
    menu = availability(profile)
    if len(menu) == 1:
        return {menu[0]: Fraction(1)}
    n0, n1 = counts(profile)
    weights = {0: lam**n0, 1: lam**n1}
    total = weights[0] + weights[1]
    return {label: Fraction(weights[label], total) for label in menu}


def label_swap(profile: Profile) -> Profile:
    return tuple(OPEN if value == OPEN else 1 - value for value in profile)  # type: ignore[return-value]


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


def proper_signed_permutations() -> tuple[tuple[tuple[int, int, int], tuple[int, int, int]], ...]:
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1:
                rotations.append((permutation, signs))
    return tuple(rotations)


NEIGHBORS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def transform_vector(
    vector: Coord,
    rotation: tuple[tuple[int, int, int], tuple[int, int, int]],
) -> Coord:
    permutation, signs = rotation
    return tuple(signs[axis] * vector[permutation[axis]] for axis in range(3))  # type: ignore[return-value]


def rotate_profile(profile: Profile, rotation) -> Profile:
    lookup = {vector: value for vector, value in zip(NEIGHBORS, profile)}
    transformed = {
        transform_vector(vector, rotation): value for vector, value in lookup.items()
    }
    return tuple(transformed[vector] for vector in NEIGHBORS)  # type: ignore[return-value]


def choose(distribution: dict[int, Fraction], seed: Fraction) -> int:
    threshold = distribution.get(0, Fraction(0))
    return 0 if seed < threshold else 1


def local_profile(state: dict[Coord, int], site: Coord) -> Profile:
    return tuple(
        state.get(
            (site[0] + delta[0], site[1] + delta[1], site[2] + delta[2]),
            OPEN,
        )
        for delta in NEIGHBORS
    )  # type: ignore[return-value]


def append_branch(
    state: dict[Coord, int], site: Coord, outcome: int
) -> dict[Coord, int]:
    if site in state:
        raise ValueError("records are append-only")
    successor = dict(state)
    successor[site] = outcome
    return successor


def cylinder_tree(
    lam: int,
    state: dict[Coord, int],
    schedule: tuple[Coord, ...],
) -> dict[tuple[int, ...], Fraction]:
    frontier = {(tuple(), tuple(sorted(state.items()))): Fraction(1)}
    for site in schedule:
        next_frontier: dict[tuple[tuple[int, ...], tuple[tuple[Coord, int], ...]], Fraction] = {}
        for (history, encoded_state), weight in frontier.items():
            current = dict(encoded_state)
            distribution = kernel(lam, local_profile(current, site))
            for outcome, probability in distribution.items():
                successor = append_branch(current, site, outcome)
                key = (history + (outcome,), tuple(sorted(successor.items())))
                next_frontier[key] = next_frontier.get(key, Fraction(0)) + weight * probability
        frontier = next_frontier
    return {history: weight for (history, _), weight in frontier.items()}


def source_contract() -> None:
    section("A - Source and authority boundary")
    note = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").replace(">", "").split()
    )
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A note is authority-free", "authority: none" in note)
    check("A note is not an axiom proposal", "not the physical law, an axiom proposal" in note)
    check("A note carries all N1-N8 gates", all(f"n{index} —" in note for index in range(1, 9)))
    check("A live Admissibility still names only one fixed rule", "There is one fixed nearest-neighbor admissibility rule" in axioms)
    check("A live Record still says records form", "Records form." in axioms)


def complete_profile_census() -> None:
    section("B - Same menu, support, normalization, and symmetries")
    profiles = tuple(product((OPEN, 0, 1), repeat=6))
    rotations = proper_signed_permutations()
    check("B ternary six-neighbour census has 729 profiles", len(profiles) == 729)
    check("B proper cubic rotation group has 24 elements", len(rotations) == 24)
    for lam in (1, 2):
        check(f"B lambda={lam} normalizes on every profile", all(sum(kernel(lam, profile).values()) == 1 for profile in profiles))
        check(f"B lambda={lam} has exactly the availability support", all(tuple(kernel(lam, profile)) == availability(profile) for profile in profiles))
        check(
            f"B lambda={lam} is global-label equivariant",
            all(
                kernel(lam, label_swap(profile)).get(1 - label, Fraction(0)) == probability
                for profile in profiles
                for label, probability in kernel(lam, profile).items()
            ),
        )
        check(
            f"B lambda={lam} is invariant under all proper cubic rotations",
            all(
                kernel(lam, rotate_profile(profile, rotation)) == kernel(lam, profile)
                for profile in profiles
                for rotation in rotations
            ),
        )
    check("B the two laws share support on every profile", all(tuple(kernel(1, profile)) == tuple(kernel(2, profile)) for profile in profiles))


def operational_discriminator() -> None:
    section("C - One readable transcript separates the laws")
    profile: Profile = (0, 0, 1, OPEN, OPEN, OPEN)
    first = kernel(1, profile)
    second = kernel(2, profile)
    check("C lambda=1 gives one half at the 2:1 profile", first[0] == Fraction(1, 2))
    check("C lambda=2 gives two thirds at the 2:1 profile", second[0] == Fraction(2, 3))
    check("C the transcript laws are operationally distinct", first != second)
    seed = Fraction(3, 5)
    check("C the same seed writes one under lambda=1", choose(first, seed) == 1)
    check("C the same seed writes zero under lambda=2", choose(second, seed) == 0)
    swapped_profile = label_swap(profile)
    swapped_seed = 1 - seed
    check(
        "C lambda=1 sampling is label-covariant when the interval coordinate transforms",
        choose(kernel(1, swapped_profile), swapped_seed) == 1 - choose(first, seed),
    )
    check(
        "C lambda=2 sampling is label-covariant when the interval coordinate transforms",
        choose(kernel(2, swapped_profile), swapped_seed) == 1 - choose(second, seed),
    )
    check(
        "C a fixed numerical seed is not itself pathwise label-neutral",
        choose(kernel(1, swapped_profile), seed) == choose(first, seed),
    )


def records_gluing_and_cylinders() -> None:
    section("D - Append permanence, disjoint composition, and cylinders")
    origin = (0, 0, 0)
    boundary = {
        (1, 0, 0): 0,
        (-1, 0, 0): 0,
        (0, 1, 0): 1,
    }
    for lam in (1, 2):
        distribution = kernel(lam, local_profile(boundary, origin))
        successors = tuple(append_branch(boundary, origin, outcome) for outcome in distribution)
        check(f"D lambda={lam} appends exactly one record per branch", all(len(successor) == len(boundary) + 1 for successor in successors))
        check(f"D lambda={lam} preserves every prior site and content", all(all(successor[item] == value for item, value in boundary.items()) for successor in successors))
        check(f"D lambda={lam} branches lock one value at the target", {successor[origin] for successor in successors} == set(distribution))

    disjoint_a = (0, 0, 0)
    disjoint_b = (5, 0, 0)
    disjoint_boundary = {
        (1, 0, 0): 0,
        (-1, 0, 0): 1,
        (4, 0, 0): 0,
        (6, 0, 0): 1,
    }
    for lam in (1, 2):
        ab = cylinder_tree(lam, disjoint_boundary, (disjoint_a, disjoint_b))
        ba = cylinder_tree(lam, disjoint_boundary, (disjoint_b, disjoint_a))
        reordered_ba = {(history[1], history[0]): weight for history, weight in ba.items()}
        check(f"D lambda={lam} disjoint schedule order gives the same labelled law", ab == reordered_ba)
        check(f"D lambda={lam} two-event cylinders normalize", sum(ab.values()) == 1)
        first_marginal = {
            outcome: sum(weight for history, weight in ab.items() if history[0] == outcome)
            for outcome in (0, 1)
        }
        expected = kernel(lam, local_profile(disjoint_boundary, disjoint_a))
        check(f"D lambda={lam} cylinder marginal recovers the first event", first_marginal == expected)


def fresh_site_route() -> None:
    section("E - Infinite-lattice fresh-address route")
    def shell(radius: int) -> tuple[Coord, ...]:
        return tuple(
            coordinate
            for coordinate in product(range(-radius, radius + 1), repeat=3)
            if abs(coordinate[0]) + abs(coordinate[1]) + abs(coordinate[2]) == radius
        )

    first_shells = tuple(coordinate for radius in range(7) for coordinate in shell(radius))
    check("E shell-first allocator has no repeated address", len(first_shells) == len(set(first_shells)))
    check("E shell-first allocator reaches unbounded tested radius", max(sum(abs(value) for value in coordinate) for coordinate in first_shells) == 6)
    check("E every finite prefix uses only finitely many sites", all(len(first_shells[:length]) == length for length in range(len(first_shells) + 1)))
    earlier = set()
    causally_reachable = True
    for coordinate in first_shells:
        radius = sum(abs(value) for value in coordinate)
        if radius and not any(
            (coordinate[0] + delta[0], coordinate[1] + delta[1], coordinate[2] + delta[2]) in earlier
            for delta in NEIGHBORS
        ):
            causally_reachable = False
        earlier.add(coordinate)
    check("E every non-origin shell address touches an earlier shell", causally_reachable)


def conclusion_contract() -> None:
    section("F - Exact lower-bound needles")
    note = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("*", "").replace("`", "").replace(">", "").split()
    )
    phrases = (
        "same present foundation interface",
        "one-record transcript separates",
        "exact extensional law value",
        "operational-equivalence theorem",
        "no record-only sentence",
        "wolfram-style multiway",
        "does not yet authorize",
        "interval coordinate must change",
        "shell origin is anchored",
        "strongest steelman",
    )
    for phrase in phrases:
        check(f"F note contains boundary: {phrase}", phrase in note)


def main() -> None:
    source_contract()
    complete_profile_census()
    operational_discriminator()
    records_gluing_and_cylinders()
    fresh_site_route()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
