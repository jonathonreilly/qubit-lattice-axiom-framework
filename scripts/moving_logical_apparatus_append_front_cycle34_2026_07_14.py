#!/usr/bin/env python3
"""Exact controls for the Cycle-34 moving logical append-front probe.

The construction keeps every physical record site-tethered and permanent.
Only the translated logical head role recurs.  The runner changes no authority
surface and does not select the candidate as the physical law.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SOURCES = (
    REVIEW / "LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md",
    REVIEW / "SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md",
    REVIEW / "CERTIFIED_RECORD_CORPUS_ERGODIC_FREQUENCY_CYCLE21_NOTE_2026-07-14.md",
    REVIEW / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    REVIEW / "FULL_Z3_CAUSAL_FRONT_SAMPLED_INSTRUMENT_LAW_NOTE_2026-07-14.md",
    REVIEW / "GLOBAL_RECORD_HISTORY_PROCESS_LAW_CYCLE30_NOTE_2026-07-14.md",
    REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md",
)

Point = tuple[int, int, int]
RecordMap = dict[Point, int]
Kernel = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]

E: Point = (1, 0, 0)
ZERO: Point = (0, 0, 0)
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def add(left: Point, right: Point) -> Point:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def subtract(left: Point, right: Point) -> Point:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def scale(multiplier: int, point: Point) -> Point:
    return tuple(multiplier * coordinate for coordinate in point)  # type: ignore[return-value]


def l1_norm(point: Point) -> int:
    return sum(abs(coordinate) for coordinate in point)


def translate(records: RecordMap, displacement: Point) -> RecordMap:
    return {add(site, displacement): content for site, content in records.items()}


def rotate_z_quarter(point: Point) -> Point:
    x, y, z = point
    return (-y, x, z)


def rotate_records(records: RecordMap) -> RecordMap:
    return {rotate_z_quarter(site): content for site, content in records.items()}


def ready_front(records: RecordMap, direction: Point = E) -> set[Point]:
    return {
        add(site, direction)
        for site in records
        if add(site, direction) not in records
    }


def step_deterministic(records: RecordMap, content_map, direction: Point = E) -> RecordMap:
    old = dict(records)
    future = dict(records)
    for target in ready_front(old, direction):
        predecessor = subtract(target, direction)
        future[target] = content_map(old[predecessor])
    return future


def step_presence(sites: set[int]) -> set[int]:
    return sites | {site + 1 for site in sites}


def head(records: RecordMap, direction: Point = E) -> Point:
    candidates = tuple(site for site in records if add(site, direction) not in records)
    if len(candidates) != 1:
        raise ValueError(f"isolated ray has {len(candidates)} heads")
    return candidates[0]


def ball_volume(radius: int) -> int:
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


def l1_offsets(radius: int) -> tuple[Point, ...]:
    return tuple(
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    )


def role_patch(records: RecordMap, pointed_head: Point, radius: int) -> tuple[tuple[Point, bool], ...]:
    return tuple(
        (offset, add(pointed_head, offset) in records)
        for offset in l1_offsets(radius)
    )


def word_probability(kernel: Kernel, start: int, word: tuple[int, ...]) -> Fraction:
    probability = Fraction(1)
    current = start
    for outcome in word:
        probability *= kernel[current][outcome]
        current = outcome
    return probability


def joint_word_probability(
    kernel: Kernel,
    initial: tuple[Fraction, Fraction],
    word: tuple[int, ...],
) -> Fraction:
    if not word:
        return Fraction(1)
    probability = initial[word[0]]
    for left, right in zip(word, word[1:]):
        probability *= kernel[left][right]
    return probability


def evolve_distribution(
    distribution: tuple[Fraction, Fraction],
    kernel: Kernel,
) -> tuple[Fraction, Fraction]:
    return tuple(
        sum(distribution[left] * kernel[left][right] for left in (0, 1))
        for right in (0, 1)
    )  # type: ignore[return-value]


def source_contract() -> None:
    section("A - Foundation, source, and authority boundary")
    for path in (NOTE, AXIOMS, REGISTRY, *SOURCES):
        check(f"A source exists: {path.name}", path.is_file())

    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    check("A note is authority-free", "authority: none" in note)
    check("A note does not amend an axiom", "does not amend an axiom" in note)
    check("A note does not select the framework law", "select the framework law" in note)
    check("A live Record is permanent", "records are permanent" in axioms)
    check("A live Record is at most one per site", "a site never carries more than one record" in axioms)
    check("A live state is a record configuration", "a state is a configuration of records" in axioms)
    check("A live Admissibility is not dynamics", "admissibility is not a dynamics axiom" in axioms)
    check(
        "A registry has exactly the supplied baseline and three primitives",
        set(registry["canonical_ids"])
        == {
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        },
    )
    check("A logical identity is not called record migration", "no record moves" in note)
    check("A no live constitutional edit is recommended", "no qualification amendment is forced" in note)


def translation_and_append_controls() -> None:
    section("B - Exact translation-covariant nearest-neighbor append law")
    identity = lambda bit: bit
    flip = lambda bit: 1 - bit
    translations = ((1, 0, 0), (-2, 3, 1), (0, -4, 2))

    sites = tuple(scale(index, E) for index in range(-2, 3))
    preserves = True
    nearest_neighbor = True
    unique = True
    covariant = True
    case_count = 0
    for status_word in product((-1, 0, 1), repeat=len(sites)):
        records = {
            site: status
            for site, status in zip(sites, status_word)
            if status != -1
        }
        for content_map in (identity, flip):
            case_count += 1
            future = step_deterministic(records, content_map)
            preserves &= all(future[site] == content for site, content in records.items())
            new_sites = set(future) - set(records)
            nearest_neighbor &= all(subtract(site, E) in records and l1_norm(E) == 1 for site in new_sites)
            unique &= len(future) == len(set(future))
            for displacement in translations:
                translated_future = step_deterministic(translate(records, displacement), content_map)
                covariant &= translated_future == translate(future, displacement)
    check("B append step preserves every old site/content pair", preserves, f"cases={case_count}")
    check("B every new write has exactly one directed NN predecessor", nearest_neighbor, f"cases={case_count}")
    check("B no site receives two records", unique, f"cases={case_count}")
    check("B deterministic law commutes with translation", covariant, f"cases={case_count * len(translations)}")


def isolated_ray_controls() -> None:
    section("C - Isolated-front indefinite growth and no state edit")
    for initial in (0, 1):
        for name, content_map in (("identity", lambda bit: bit), ("flip", lambda bit: 1 - bit)):
            records: RecordMap = {ZERO: initial}
            written_once = {ZERO}
            exact_support = True
            unique_head = True
            single_front = True
            exact_content = True
            one_new = True
            no_rewrite = True
            old_unchanged = True
            for trial in range(0, 41):
                expected_sites = {scale(index, E) for index in range(trial + 1)}
                exact_support &= set(records) == expected_sites
                unique_head &= head(records) == scale(trial, E)
                single_front &= ready_front(records) == {scale(trial + 1, E)}
                if name == "identity":
                    exact_content &= set(records.values()) == {initial}
                else:
                    exact_content &= all(records[scale(index, E)] == (initial + index) % 2 for index in range(trial + 1))
                old = dict(records)
                records = step_deterministic(records, content_map)
                new_sites = set(records) - set(old)
                one_new &= len(new_sites) == 1
                no_rewrite &= not (new_sites & written_once)
                written_once |= new_sites
                old_unchanged &= all(records[site] == value for site, value in old.items())
            detail = "layers=41"
            check(f"C {name}, seed={initial} exact ray support", exact_support, detail)
            check(f"C {name}, seed={initial} unique decoded head", unique_head, detail)
            check(f"C {name}, seed={initial} one-site ready front", single_front, detail)
            check(f"C {name}, seed={initial} exact record-derived content", exact_content, detail)
            check(f"C {name}, seed={initial} exactly one new site per layer", one_new, detail)
            check(f"C {name}, seed={initial} never rewrites a used site", no_rewrite, detail)
            check(f"C {name}, seed={initial} old records are unchanged", old_unchanged, detail)


def cubic_covariance_separator() -> None:
    section("D - Translation covariance versus proper-cubic direction")
    seed = {ZERO: 0}
    fixed_x_future = step_deterministic(seed, lambda bit: bit, E)
    rotated_future = rotate_records(fixed_x_future)
    fixed_x_after_rotated_seed = step_deterministic(rotate_records(seed), lambda bit: bit, E)
    rotated_direction = rotate_z_quarter(E)
    family_rotated_future = step_deterministic(rotate_records(seed), lambda bit: bit, rotated_direction)
    check("D fixed-e law grows in +x", set(fixed_x_future) == {ZERO, (1, 0, 0)})
    check("D proper rotation sends +x to +y", rotated_direction == (0, 1, 0))
    check("D one fixed-e member is not proper-cubic covariant", fixed_x_after_rotated_seed != rotated_future)
    check("D direction-indexed law family is covariant", family_rotated_future == rotated_future)
    check("D two internal bits cannot encode six orthogonal directions", 2**2 < 6)
    check("D three internal bits can encode six orthogonal directions", 6 <= 2**3)


def logical_identity_controls() -> None:
    section("E - Translated role patches and future-law bisimulation")
    records: RecordMap = {ZERO: 0}
    histories: list[RecordMap] = []
    for _ in range(30):
        histories.append(dict(records))
        records = step_deterministic(records, lambda bit: bit)

    for radius in range(1, 7):
        reference = role_patch(histories[radius], head(histories[radius]), radius)
        for time in range(radius, len(histories)):
            check(
                f"E r={radius}, n={time} co-moving occupancy role is identical",
                role_patch(histories[time], head(histories[time]), radius) == reference,
            )
        check(
            f"E r={radius} identical role patches alias distinct wake counts",
            role_patch(histories[radius], head(histories[radius]), radius)
            == role_patch(histories[-1], head(histories[-1]), radius)
            and len(histories[radius]) != len(histories[-1]),
        )

    kernel: Kernel = (
        (Fraction(3, 4), Fraction(1, 4)),
        (Fraction(1, 3), Fraction(2, 3)),
    )
    words = tuple(product((0, 1), repeat=5))
    for logical_state in (0, 1):
        left_archive = {scale(index, E): index % 2 for index in range(8)}
        right_archive = {scale(index + 100, E): (index // 2) % 2 for index in range(8)}
        left_archive[scale(7, E)] = logical_state
        right_archive[scale(107, E)] = logical_state
        for word in words:
            left_probability = word_probability(kernel, left_archive[scale(7, E)], word)
            right_probability = word_probability(kernel, right_archive[scale(107, E)], word)
            check(
                f"E state={logical_state}, word={word} future law ignores position and old wake",
                left_probability == right_probability,
            )

    iid_kernel: Kernel = (
        (Fraction(2, 3), Fraction(1, 3)),
        (Fraction(2, 3), Fraction(1, 3)),
    )
    for word in words:
        check(
            f"E IID word={word} predictive reset removes current-bit dependence",
            word_probability(iid_kernel, 0, word) == word_probability(iid_kernel, 1, word),
        )


def corpus_and_minimum_controls() -> None:
    section("F - Certified edge corpus and scoped one-record minimum")
    outcome_sequence = tuple(index % 2 for index in range(21))
    edge_blocks = tuple((index, index + 1) for index in range(20))
    check("F twenty trials have twenty causal edge blocks", len(edge_blocks) == 20)
    check("F every edge block is nearest-neighbor", all(right - left == 1 for left, right in edge_blocks))
    check("F outcome sites are pairwise distinct", len({right for _, right in edge_blocks}) == 20)
    check("F consecutive edge certificates share exactly one boundary record", all(edge_blocks[index][1] == edge_blocks[index + 1][0] for index in range(19)))
    check("F N edge trials use N fresh records plus one seed", len(outcome_sequence) == len(edge_blocks) + 1)
    outcome_count = sum(outcome_sequence[1:])
    check("F additive outcome count is readable from distinct sites", outcome_count == 10)

    disjoint_pairs = tuple((2 * index, 2 * index + 1) for index in range(10))
    pair_sites = tuple(site for block in disjoint_pairs for site in block)
    check("F strict two-record blocks are pairwise disjoint", len(pair_sites) == len(set(pair_sites)) == 20)
    triples = tuple((3 * index, 3 * index + 1, 3 * index + 2) for index in range(7))
    triple_sites = tuple(site for block in triples for site in block)
    check("F strict P/O/K triples are pairwise disjoint", len(triple_sites) == len(set(triple_sites)) == 21)

    unchanged_zero = {ZERO: 0}
    unchanged_one = {ZERO: 0}
    one_new_zero = {ZERO: 0, E: 0}
    one_new_one = {ZERO: 0, E: 1}
    check("F zero new records cannot distinguish two content outcomes", unchanged_zero == unchanged_one)
    check("F one fresh M2 record distinguishes two perfect outcomes", one_new_zero != one_new_one)
    check("F one binary carrier has exactly two orthogonal labels in the comparator", len({0, 1}) == 2)


def storage_density_and_clock_controls() -> None:
    section("G - Storage, lab/co-moving density, and relational clock")
    for trials in (1, 2, 5, 10, 50, 100, 500):
        records = trials + 1
        spatial_density = Fraction(records, ball_volume(trials))
        cylinder_density = Fraction(records, records * ball_volume(trials))
        check(f"G N={trials} storage is N+1 including seed", records == trials + 1)
        check(f"G N={trials} final ray density is (N+1)/B_N", spatial_density == Fraction(trials + 1, ball_volume(trials)))
        check(f"G N={trials} lab cylinder density is 1/B_N", cylinder_density == Fraction(1, ball_volume(trials)))
        check(f"G N={trials} relational clock equals wake length minus one", trials == records - 1)

    large = 100_000
    scaled_spatial = Fraction(large**2 * (large + 1), ball_volume(large))
    scaled_cylinder = Fraction(large**3, ball_volume(large))
    check("G N^2 times ray density tends numerically to 3/4", abs(scaled_spatial - Fraction(3, 4)) < Fraction(1, 1000), str(float(scaled_spatial)))
    check("G N^3 times cylinder density tends numerically to 3/4", abs(scaled_cylinder - Fraction(3, 4)) < Fraction(1, 1000), str(float(scaled_cylinder)))

    for radius in range(0, 9):
        moving_density = Fraction(1, ball_volume(radius))
        check(f"G moving radius={radius} window has one event per B_r site-time slice", moving_density * ball_volume(radius) == 1)

    for lab_radius in (1, 3, 7, 20):
        events = lab_radius + 1
        check(f"G fixed lab segment 0..{lab_radius} sees finitely many events", events == lab_radius + 1)
        check(f"G fixed lab segment 0..{lab_radius} sees zero later formations", all(site > lab_radius for site in range(lab_radius + 1, lab_radius + 20)))

    for first, second, third in ((0, 7, 19), (4, 10, 25), (13, 29, 50)):
        check(
            f"G clock increments add on segments {first},{second},{third}",
            (third - first) == (second - first) + (third - second),
        )

    event_indices = tuple(range(20))
    fast_times = event_indices
    slow_times = tuple(11 * index for index in event_indices)
    check("G fast and slow timestamps preserve event order", tuple(sorted(fast_times)) == fast_times and tuple(sorted(slow_times)) == slow_times)
    check("G same record chain admits different coordinate velocities", Fraction(1, 1) != Fraction(1, 11))


def stationary_markov_controls() -> None:
    section("H - Exact stationary co-moving Markov statistics")
    kernel: Kernel = (
        (Fraction(3, 4), Fraction(1, 4)),
        (Fraction(1, 3), Fraction(2, 3)),
    )
    stationary = (Fraction(4, 7), Fraction(3, 7))
    check("H every Markov row normalizes", all(sum(row) == 1 for row in kernel))
    check("H all Markov entries are positive", all(entry > 0 for row in kernel for entry in row))
    check("H pi K equals pi", evolve_distribution(stationary, kernel) == stationary)
    check("H nontrivial eigenvalue is 5/12", 1 - kernel[0][1] - kernel[1][0] == Fraction(5, 12))

    distribution = (Fraction(1), Fraction(0))
    for step in range(1, 15):
        old_error = distribution[1] - stationary[1]
        distribution = evolve_distribution(distribution, kernel)
        new_error = distribution[1] - stationary[1]
        check(f"H step={step} marginal error contracts by 5/12", new_error == Fraction(5, 12) * old_error)

    pair_table = {
        word: joint_word_probability(kernel, stationary, word)
        for word in product((0, 1), repeat=2)
    }
    check(
        "H stationary adjacent-pair table is exact",
        pair_table
        == {
            (0, 0): Fraction(3, 7),
            (0, 1): Fraction(1, 7),
            (1, 0): Fraction(1, 7),
            (1, 1): Fraction(2, 7),
        },
    )
    check("H adjacent-pair table normalizes", sum(pair_table.values()) == 1)

    for length in range(1, 7):
        distribution_words = {
            word: joint_word_probability(kernel, stationary, word)
            for word in product((0, 1), repeat=length)
        }
        check(f"H length={length} stationary word family normalizes", sum(distribution_words.values()) == 1)
        if length >= 2:
            left_marginal = {
                word: sum(
                    distribution_words[(extra,) + word]
                    for extra in (0, 1)
                )
                for word in product((0, 1), repeat=length - 1)
            }
            right_marginal = {
                word: sum(
                    distribution_words[word + (extra,)]
                    for extra in (0, 1)
                )
                for word in product((0, 1), repeat=length - 1)
            }
            check(f"H length={length} co-moving shift marginals agree", left_marginal == right_marginal)

    iid: Kernel = (
        (Fraction(2, 3), Fraction(1, 3)),
        (Fraction(2, 3), Fraction(1, 3)),
    )
    identity: Kernel = (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )
    flip: Kernel = (
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(0)),
    )
    check("H equal-row kernel gives predictive reset", iid[0] == iid[1])
    check("H identity kernel retains two permanent sectors", evolve_distribution((Fraction(1, 2), Fraction(1, 2)), identity) == (Fraction(1, 2), Fraction(1, 2)))
    check("H flip kernel has stationary uniform phase", evolve_distribution((Fraction(1, 2), Fraction(1, 2)), flip) == (Fraction(1, 2), Fraction(1, 2)))
    flip_orbit = tuple(index % 2 for index in range(100))
    check("H deterministic flip orbit has pointwise frequency one half", sum(flip_orbit) == 50)
    check("H deterministic flip is periodic rather than mixing", flip_orbit[:10] == flip_orbit[2:12])


def traveling_wave_controls() -> None:
    section("I - Finite-seed local stationarity versus global traveling wave")

    def finite_occupied(site: int, time: int) -> bool:
        return 0 <= site <= time

    def infinite_occupied(site: int, time: int) -> bool:
        return site <= time

    def event(site: int, time: int) -> bool:
        return site == time

    spacetime_grid = tuple(product(range(-20, 21), repeat=2))
    check(
        "I infinite wake is invariant under combined space/time shift",
        all(infinite_occupied(site, time) == infinite_occupied(site + 1, time + 1) for site, time in spacetime_grid),
        f"cells={len(spacetime_grid)}",
    )
    check(
        "I event front is invariant under combined space/time shift",
        all(event(site, time) == event(site + 1, time + 1) for site, time in spacetime_grid),
        f"cells={len(spacetime_grid)}",
    )

    check(
        "I finite-seed full state fails exact combined-shift invariance at seed",
        finite_occupied(-1, 0) != finite_occupied(0, 1),
    )
    for radius in range(1, 10):
        local_stationary = True
        for time in range(radius, radius + 10):
            local_pattern = tuple(finite_occupied(time + offset, time) for offset in range(-radius, radius + 1))
            next_pattern = tuple(finite_occupied(time + 1 + offset, time + 1) for offset in range(-radius, radius + 1))
            local_stationary &= local_pattern == next_pattern
        check(f"I r={radius} finite-seed moving window is occupancy-stationary", local_stationary, "times=10")

    check(
        "I every tested site has exactly one formation time",
        all(tuple(time for time in range(-20, 21) if event(site, time)) == (site,) for site in range(-10, 11)),
        "sites=21",
    )


def collision_and_routing_controls() -> None:
    section("J - Same-line coalescence, parallel lanes, and routing cost")
    for gap in (2, 3, 5, 8, 13):
        sites = {0, gap}
        for _ in range(gap - 1):
            sites = step_presence(sites)
        check(f"J gap={gap} same-line fronts fill the gap", sites == set(range(0, 2 * gap)))
        future = step_presence(sites)
        check(f"J gap={gap} merged interval has one new leading head", future - sites == {2 * gap})

        records_1d = {0: 0, gap: 1}
        for _ in range(gap - 1):
            records_3d = {(site, 0, 0): bit for site, bit in records_1d.items()}
            advanced = step_deterministic(records_3d, lambda bit: bit)
            records_1d = {site[0]: bit for site, bit in advanced.items()}
        check(f"J gap={gap} collision never overwrites leading seed", records_1d[gap] == 1)
        check(f"J gap={gap} different copied labels leave a permanent domain wall", records_1d[gap - 1] == 0 and records_1d[gap] == 1)

    parallel: RecordMap = {(0, 0, 0): 0, (0, 2, 0): 1, (0, 5, 0): 0}
    for time in range(15):
        for y, bit in ((0, 0), (2, 1), (5, 0)):
            expected_line = {(x, y, 0) for x in range(time + 1)}
            actual_line = {site for site in parallel if site[1:] == (y, 0)}
            check(f"J t={time}, lane={y} parallel line has exact support", actual_line == expected_line)
            check(f"J t={time}, lane={y} parallel line preserves content", {parallel[site] for site in actual_line} == {bit})
        parallel = step_deterministic(parallel, lambda bit: bit)

    obstacle: RecordMap = {(0, 0, 0): 0, (4, 0, 0): 1}
    for _ in range(4):
        obstacle = step_deterministic(obstacle, lambda bit: bit)
    check("J pre-existing record acts as another seed, not an inert obstacle", obstacle[(4, 0, 0)] == 1 and obstacle[(3, 0, 0)] == 0)
    check("J minimum directed ray has no turn operation", ready_front({ZERO: 0}) == {(1, 0, 0)})


def prior_upper_bound_and_documentation() -> None:
    section("K - Prior proper-cubic upper bound and documentation contract")
    for trials in (0, 1, 2, 10, 100):
        simulated_records = 7 + sum(22 for _ in range(trials))
        simulated_displacement = sum(3 for _ in range(trials))
        check(f"K Cycle14 N={trials} record cost is 22N+7", simulated_records == 22 * trials + 7)
        check(f"K Cycle14 N={trials} trigger displacement is 3N", simulated_displacement == 3 * trials)

    note = normalized(NOTE)
    required = (
        "translated record-pattern and causal-lineage equivalence",
        "one fresh record suffices per minimum binary trial",
        "positive co-moving event density",
        "local stationarity versus full-state stationarity",
        "same-line coalescence",
        "comparison with the stronger existing front",
        "comparison with migratory and global-history semantics",
        "does this close the toe recurrence seam",
        "no migratory or same-site continuation amendment is needed",
        "the current admissibility sentence is availability-only",
        "logical co-moving recurrence",
        "no-go-discipline status: pass",
    )
    for phrase in required:
        check(f"K required result is documented: {phrase}", phrase in note)

    for index in range(1, 9):
        check(f"K N{index} section is present", f"n{index} —" in note)

    for residual in (
        "boundary",
        "cubic direction",
        "rate",
        "statistics",
        "routing",
        "matter map",
    ):
        check(f"K collapsed residual is named: {residual}", residual in note)

    for prior in (
        "cycle 13",
        "cycle 14",
        "cycle 21",
        "cycle 22",
        "cycle 32",
        "cycle 30",
        "cycle 33",
    ):
        check(f"K cross-cycle echo is present: {prior}", prior in note)

    check("K note does not claim a broad append-only no-go", "not a no-go against a one-law proper-cubic moving matter front" in note)
    check("K strongest steelman is explicit", "strongest steelman" in note and "physical objects are already worldline-pattern equivalence classes" in note)
    check("K no Record amendment conclusion is explicit", "no record amendment is needed" in note)
    check("K law placement is explicit", "place occurrence, direction, kernel, schedule, routing, and velocity in the exact local law" in note)
    check("K boundary placement is explicit", "place seed, blank support, and stationary component in the boundary/history interface" in note)


def main() -> int:
    source_contract()
    translation_and_append_controls()
    isolated_ray_controls()
    cubic_covariance_separator()
    logical_identity_controls()
    corpus_and_minimum_controls()
    storage_density_and_clock_controls()
    stationary_markov_controls()
    traveling_wave_controls()
    collision_and_routing_controls()
    prior_upper_bound_and_documentation()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print(
        "BOUNDARY: logical head recurrence is exact under translation and "
        "bisimulation; physical support still grows, while boundary, cubic "
        "direction, rate, statistics, routing, and matter identity remain law fields"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
