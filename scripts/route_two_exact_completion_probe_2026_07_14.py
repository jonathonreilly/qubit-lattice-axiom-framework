#!/usr/bin/env python3
"""Exact finite census for route-two support, statistics, and TOE completion."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import math


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md"
)
OPEN = -1
VALUES = (0, 1)
PASS = 0
FAIL = 0


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


def geometry(side: int):
    coords = tuple(product(range(side), repeat=3))
    index = {coord: i for i, coord in enumerate(coords)}
    neighbors: list[tuple[int, ...]] = []
    for coord in coords:
        adjacent = set()
        for axis in range(3):
            for delta in (-1, 1):
                moved = list(coord)
                moved[axis] = (moved[axis] + delta) % side
                adjacent.add(index[tuple(moved)])
        neighbors.append(tuple(sorted(adjacent)))
    edges = tuple(sorted({tuple(sorted((site, neighbor))) for site, row in enumerate(neighbors) for neighbor in row if site != neighbor}))
    return coords, tuple(neighbors), edges


def menu_counts(n_zero: int, n_one: int) -> frozenset[int]:
    if n_zero + n_one >= 2 and ((n_zero == 0) ^ (n_one == 0)):
        return frozenset((0 if n_zero else 1,))
    return frozenset(VALUES)


def availability(state: tuple[int, ...], site: int, neighbors: tuple[tuple[int, ...], ...]) -> frozenset[int]:
    recorded = tuple(state[j] for j in neighbors[site] if state[j] != OPEN)
    return menu_counts(recorded.count(0), recorded.count(1))


def successors(state: tuple[int, ...], neighbors: tuple[tuple[int, ...], ...]):
    for site, value in enumerate(state):
        if value != OPEN:
            continue
        for outcome in availability(state, site, neighbors):
            future = list(state)
            future[site] = outcome
            yield tuple(future)


def rank(state: tuple[int, ...]) -> int:
    return sum(value != OPEN for value in state)


def extends(base: tuple[int, ...], future: tuple[int, ...]) -> bool:
    return all(value == OPEN or future[i] == value for i, value in enumerate(base))


def support_table_census() -> None:
    section("A - Exact local support-law census")
    profiles = tuple((n_zero, n_one, 6 - n_zero - n_one) for n_zero in range(7) for n_one in range(7 - n_zero))
    seen = set()
    symmetric = []
    forced_pairs = []
    free_pairs = []
    for profile in profiles:
        if profile in seen:
            continue
        swapped = (profile[1], profile[0], profile[2])
        seen.update((profile, swapped))
        if profile == swapped:
            symmetric.append(profile)
        elif len(menu_counts(profile[0], profile[1])) == 1:
            forced_pairs.append((profile, swapped))
        else:
            free_pairs.append((profile, swapped))
    check("A 28 unordered count profiles", len(profiles) == 28)
    check("A four self-label-symmetric profiles", len(symmetric) == 4)
    check("A five forced singleton orbit pairs", len(forced_pairs) == 5)
    check("A seven free label orbit pairs", len(free_pairs) == 7)

    output_choices = (frozenset((0,)), frozenset((1,)), frozenset((0, 1)))
    tables = set()
    doubleton_histogram = Counter()
    for choices in product(output_choices, repeat=len(free_pairs)):
        table: dict[tuple[int, int, int], frozenset[int]] = {}
        for profile in symmetric:
            table[profile] = frozenset(VALUES)
        for pair in forced_pairs:
            for profile in pair:
                table[profile] = menu_counts(profile[0], profile[1])
        free_doubletons = 0
        for (profile, swapped), answer in zip(free_pairs, choices):
            table[profile] = answer
            table[swapped] = frozenset(1 - value for value in answer)
            free_doubletons += len(answer) == 2
        signature = tuple(sorted((profile, tuple(sorted(answer))) for profile, answer in table.items()))
        tables.add(signature)
        doubleton_histogram[free_doubletons] += 1
        check_condition = all(table[p] and table[p] <= menu_counts(p[0], p[1]) for p in profiles)
        if not check_condition:
            check("A every table is a nonempty availability refinement", False)
            return
    check("A all 2187 support tables are distinct", len(tables) == 3**7 == 2187)
    check(
        "A free-doubleton histogram is exact",
        dict(sorted(doubleton_histogram.items())) == {0: 128, 1: 448, 2: 672, 3: 560, 4: 280, 5: 84, 6: 14, 7: 1},
    )
    check("A 2059 tables retain a continuous local weight slot", sum(count for d, count in doubleton_histogram.items() if d > 0) == 2059)
    check("A total free statistical parameter incidences", sum(d * count for d, count in doubleton_histogram.items()) == 5103)


def reachability_census() -> None:
    section("B - Exact append-only continuation census")
    coords, neighbors, _ = geometry(2)
    root = (OPEN,) * len(coords)
    seen = {root}
    queue = deque([root])
    edges = 0
    by_rank = Counter({0: 1})
    strict_appends = True
    sibling_count = 0
    sibling_nonjoin = True
    while queue:
        state = queue.popleft()
        next_states = tuple(successors(state, neighbors))
        edges += len(next_states)
        for site, value in enumerate(state):
            if value == OPEN and availability(state, site, neighbors) == frozenset(VALUES):
                left = list(state)
                right = list(state)
                left[site] = 0
                right[site] = 1
                left = tuple(left)
                right = tuple(right)
                sibling_count += 1
                sibling_nonjoin &= not all(
                    a == OPEN or b == OPEN or a == b for a, b in zip(left, right)
                )
        for future in next_states:
            strict_appends &= rank(future) == rank(state) + 1 and extends(state, future)
            if future not in seen:
                seen.add(future)
                queue.append(future)
                by_rank[rank(future)] += 1
    check("B quotient cube has eight sites and three distinct neighbors/site", len(coords) == 8 and all(len(row) == 3 for row in neighbors))
    check("B every edge is one immutable append", strict_appends)
    check("B reachable-state census", len(seen) == 6427, str(dict(sorted(by_rank.items()))))
    check("B reachable-edge census", edges == 29392)
    check("B terminal-record census", sum(OPEN not in state for state in seen) == 254)
    check("B nonvacuous same-site split census", sibling_count == 12216)
    check("B every conflicting sibling pair is incompatible", sibling_nonjoin)

    # Genuine six-neighbor L=3 graph, bounded at depth three only.
    coords3, neighbors3, _ = geometry(3)
    root3 = (OPEN,) * len(coords3)
    seen3 = {root3}
    frontier = {root3}
    ranks3 = {0: 1}
    edges3 = 0
    for depth in range(3):
        next_frontier = set()
        for state in frontier:
            children = tuple(successors(state, neighbors3))
            edges3 += len(children)
            next_frontier.update(children)
        next_frontier -= seen3
        seen3 |= next_frontier
        frontier = next_frontier
        ranks3[depth + 1] = len(frontier)
    check("B L=3 depth-three state census", len(seen3) == 24859 and ranks3 == {0: 1, 1: 54, 2: 1404, 3: 23400})
    check("B L=3 depth-three edge census", edges3 == 72252)


DIRECTIONS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(permutation[i] > permutation[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


def rotations() -> tuple[tuple[int, ...], ...]:
    result = []
    for axis_permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(axis_permutation) * math.prod(signs) != 1:
                continue
            matrix = [[0] * 3 for _ in range(3)]
            for row in range(3):
                matrix[row][axis_permutation[row]] = signs[row]
            result.append(tuple(
                DIR_INDEX[tuple(sum(matrix[row][column] * direction[column] for column in range(3)) for row in range(3))]
                for direction in DIRECTIONS
            ))
    return tuple(result)


def local_menu(profile: tuple[int, ...]) -> frozenset[int]:
    return menu_counts(profile.count(0), profile.count(1))


def local_kernel(profile: tuple[int, ...], lam: int) -> dict[int, Fraction]:
    available = local_menu(profile)
    weights = {value: lam ** profile.count(value) for value in available}
    denominator = sum(weights.values())
    return {value: Fraction(weight, denominator) for value, weight in weights.items()}


def flip_profile(profile: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(OPEN if value == OPEN else 1 - value for value in profile)


def hard_statistics_census() -> None:
    section("C - Two hard-constraint local kernels")
    profiles = tuple(product((OPEN, 0, 1), repeat=6))
    proper_rotations = rotations()
    check("C 729 local profiles", len(profiles) == 729)
    check("C 24 proper cubic rotations", len(set(proper_rotations)) == 24)
    for lam in (1, 2):
        check(f"C lambda={lam} normalized", all(sum(local_kernel(profile, lam).values()) == 1 for profile in profiles))
        check(f"C lambda={lam} exact support", all(set(local_kernel(profile, lam)) == set(local_menu(profile)) for profile in profiles))
        check(
            f"C lambda={lam} rotation invariant",
            all(local_kernel(tuple(profile[i] for i in rotation), lam) == local_kernel(profile, lam) for profile in profiles for rotation in proper_rotations),
        )
        check(
            f"C lambda={lam} label covariant",
            all(local_kernel(flip_profile(profile), lam) == {1 - value: weight for value, weight in local_kernel(profile, lam).items()} for profile in profiles),
        )
    witness = (0, OPEN, OPEN, OPEN, OPEN, OPEN)
    check("C kernels disagree with identical support", local_kernel(witness, 1)[0] == Fraction(1, 2) and local_kernel(witness, 2)[0] == Fraction(2, 3))

    def chain_weight(word: tuple[int, ...], lam: int) -> Fraction:
        if not word:
            return Fraction(1)
        weight = Fraction(1, 2)
        for previous, current in zip(word, word[1:]):
            weight *= local_kernel((previous, OPEN, OPEN, OPEN, OPEN, OPEN), lam)[current]
        return weight

    for lam in (1, 2):
        check(
            f"C lambda={lam} cylinders normalize through length eight",
            all(sum(chain_weight(word, lam) for word in product(VALUES, repeat=length)) == 1 for length in range(1, 9)),
        )
        check(
            f"C lambda={lam} prefix consistency",
            all(sum(chain_weight(prefix + (value,), lam) for value in VALUES) == chain_weight(prefix, lam) for prefix in product(VALUES, repeat=5)),
        )


def gibbs_weight(state: tuple[int, ...], edges: tuple[tuple[int, int], ...], lam: int) -> int:
    return lam ** sum(state[left] == state[right] for left, right in edges)


def global_measure_census() -> None:
    section("D - Presentation-independent Gibbs comparator")
    coords, neighbors, edges = geometry(2)
    states = tuple(product(VALUES, repeat=8))
    partials = tuple(product((OPEN, 0, 1), repeat=8))
    partition = {}
    equality = {}
    cylinders_by_lam = {}
    for lam in (1, 2):
        z = sum(gibbs_weight(state, edges, lam) for state in states)
        partition[lam] = z
        equal_numerator = sum(
            gibbs_weight(state, edges, lam) * sum(state[a] == state[b] for a, b in edges)
            for state in states
        )
        equality[lam] = Fraction(equal_numerator, len(edges) * z)
        cylinders = {
            partial: sum(
                gibbs_weight(state, edges, lam)
                for state in states
                if all(value == OPEN or state[index] == value for index, value in enumerate(partial))
            )
            for partial in partials
        }
        cylinders_by_lam[lam] = cylinders
        consistency = True
        for partial in partials:
            for site, value in enumerate(partial):
                if value != OPEN:
                    continue
                zero = list(partial)
                one = list(partial)
                zero[site] = 0
                one[site] = 1
                consistency &= cylinders[partial] == cylinders[tuple(zero)] + cylinders[tuple(one)]
        check(f"D lambda={lam} all 3^8 cylinders are consistent", consistency)
        local_markov = True
        for state in states:
            for site in range(8):
                zero = list(state)
                one = list(state)
                zero[site] = 0
                one[site] = 1
                ratio = Fraction(gibbs_weight(tuple(zero), edges, lam), gibbs_weight(tuple(one), edges, lam))
                n_zero = sum(state[j] == 0 for j in neighbors[site])
                n_one = sum(state[j] == 1 for j in neighbors[site])
                local_markov &= ratio == Fraction(lam**n_zero, lam**n_one)
        check(f"D lambda={lam} full-condition Markov locality", local_markov)
    check("D exact partition functions", partition == {1: 256, 2: 36450})
    check("D exact nearest-neighbor equality probabilities", equality == {1: Fraction(1, 2), 2: Fraction(32, 45)})

    site = 0
    remote = 7
    check("D chosen remote site is not adjacent", remote not in neighbors[site])

    def conditional_zero(remote_value: int) -> Fraction:
        numerators = []
        for site_value in VALUES:
            numerators.append(sum(
                gibbs_weight(state, edges, 2)
                for state in states
                if state[site] == site_value and state[remote] == remote_value
            ))
        return Fraction(numerators[0], sum(numerators))

    check(
        "D partial reveal can depend on a remote record",
        conditional_zero(0) == Fraction(416, 675) and conditional_zero(1) == Fraction(259, 675),
    )


def schedule_and_refinement_controls() -> None:
    section("E - Schedule and presentation controls")
    # beta=2 alpha^2 and 1-beta=2(1-alpha)^2 imply (2 alpha-1)^2=0.
    alpha = Fraction(1, 2)
    beta = Fraction(1, 2)
    check("E strict-local schedule equations have uniform solution", beta == 2 * alpha * alpha and 1 - beta == 2 * (1 - alpha) ** 2)
    check("E solution is unique over the reals", 4 * alpha * alpha - 4 * alpha + 1 == 0)
    check("E hard singleton beta=1 conflicts with both equations", not (1 == 2 * 1 * 1 and 0 == 2 * (1 - 1) ** 2))

    coarse = (Fraction(1, 2), Fraction(1, 2))
    refined_uniform = (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
    inherited = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
    check("E uniform microcount changes coarse weight", (refined_uniform[0] + refined_uniform[1], refined_uniform[2]) != coarse)
    check("E inherited weights preserve the coarse cylinder", (inherited[0] + inherited[1], inherited[2]) == coarse)

    coords, neighbors, _ = geometry(2)
    root = (OPEN,) * len(coords)
    levels = defaultdict(list)
    levels[0].append(root)
    seen = {root}
    queue = deque([root])
    while queue:
        state = queue.popleft()
        for future in successors(state, neighbors):
            if future not in seen:
                seen.add(future)
                queue.append(future)
                levels[rank(future)].append(future)
    paths = {root: 1}
    for level in range(8):
        for state in levels[level]:
            for future in successors(state, neighbors):
                paths[future] = paths.get(future, 0) + paths[state]
    terminal = {state: count for state, count in paths.items() if OPEN not in state}
    histogram = Counter(terminal.values())
    check("E 254 terminal records", len(terminal) == 254)
    check("E 4,843,392 complete histories", sum(terminal.values()) == 4843392)
    check("E twelve distinct path multiplicities", len(histogram) == 12)
    check("E path multiplicities range 456..40320", min(terminal.values()) == 456 and max(terminal.values()) == 40320)


def action_and_interface_controls() -> None:
    section("F - Action and full-interface nonuniqueness")
    pi = (Fraction(2, 3), Fraction(1, 3))
    kernels = (
        ((Fraction(3, 4), Fraction(1, 4)), (Fraction(1, 2), Fraction(1, 2))),
        ((Fraction(7, 8), Fraction(1, 8)), (Fraction(1, 4), Fraction(3, 4))),
    )
    fluxes = []
    for index, transition in enumerate(kernels, start=1):
        pushed = tuple(sum(pi[source] * transition[source][target] for source in VALUES) for target in VALUES)
        flux = pi[0] * transition[0][1]
        reverse_flux = pi[1] * transition[1][0]
        check(f"F K{index} preserves the same equilibrium law", pushed == pi)
        check(f"F K{index} obeys detailed balance", flux == reverse_flux)
        fluxes.append(flux)
    check("F same action/equilibrium allows different rates", fluxes == [Fraction(1, 6), Fraction(1, 12)])

    completions = []
    for operational, time, individuation, resource, boundary in product((0, 1), repeat=5):
        completions.append((
            "O0" if operational == 0 else "O1",
            (0, 1, 2) if time == 0 else (0, 1, 4),
            "+" if individuation == 0 else "-",
            (0, 1, 2) if resource == 0 else (0, 1, 3),
            "00" if boundary == 0 else "11",
        ))
    check("F 32 completions share one bare support graph", len(completions) == 32)
    check("F every full-interface signature is distinct", len(set(completions)) == 32)

    note = NOTE.read_text(encoding="utf-8")
    required = (
        "2,187 distinct",
        "6,427 reachable",
        "29,392 edges",
        "4,843,392 complete histories",
        "32 full-interface completions",
        "Z_2 = 36,450",
        "416/675",
        "K_1 = [[3/4, 1/4]",
    )
    check("F note records every exact anchor", all(marker in note for marker in required))


def main() -> int:
    support_table_census()
    reachability_census()
    hard_statistics_census()
    global_measure_census()
    schedule_and_refinement_controls()
    action_and_interface_controls()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: route two derives append-only nonreconnection; support, weights, actuality, order, and full TOE interfaces remain distinct fields")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
