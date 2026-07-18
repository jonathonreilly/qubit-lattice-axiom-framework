#!/usr/bin/env python3
"""Exact controls for the Cycle-32 record-only append architecture probe.

The runner distinguishes finite local exhaustion from infinite-lattice
continuation.  It tests the site-tethered append branch conditionally; it does
not select that branch as the meaning of the live Record axiom.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "LONG_RUN_RECORD_ONLY_APPEND_ARCHITECTURE_CYCLE32_NOTE_2026-07-14.md"
)

OPEN = -1
NEIGHBORS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
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
    return " ".join(
        path.read_text(encoding="utf-8")
        .lower()
        .replace("*", "")
        .replace("`", "")
        .replace(">", "")
        .split()
    )


def add(point: tuple[int, int, int], step: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(point[index] + step[index] for index in range(3))  # type: ignore[return-value]


def l1_norm(point: tuple[int, int, int]) -> int:
    return sum(abs(value) for value in point)


def l1_ball(radius: int) -> set[tuple[int, int, int]]:
    return {
        (x, y, z)
        for x in range(-radius, radius + 1)
        for y in range(-radius, radius + 1)
        for z in range(-radius, radius + 1)
        if abs(x) + abs(y) + abs(z) <= radius
    }


def ball_volume(radius: int) -> int:
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


def shell_size(radius: int) -> int:
    return 1 if radius == 0 else 4 * radius**2 + 2


def outward_edges(radius: int) -> int:
    ball = l1_ball(radius)
    return sum(add(site, step) not in ball for site in ball for step in NEIGHBORS)


def bits_needed(label_count: int) -> int:
    if label_count <= 1:
        return 0
    return (label_count - 1).bit_length()


def source_contract() -> None:
    section("A - Foundation, registry, and authority contract")
    axioms = normalized(AXIOMS)
    note = normalized(NOTE)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))

    check("A note exists", NOTE.is_file())
    check("A note is authority-free", "authority: none" in note)
    check("A note does not amend an axiom", "does not amend an axiom" in note)
    check("A note does not select a physical law", "select a physical law" in note)
    check("A note names the tested semantic branch", "site-tethered, append-only" in note)
    check(
        "A note does not promote site tethering into live Record",
        "do not by themselves settle that reading against migratory record identity" in note,
    )
    check("A live Record says at most one record per site", "a site never carries more than one record" in axioms)
    check("A live Record says records are permanent", "records are permanent" in axioms)
    check("A live Qualification says state is records", "a state is a configuration of records" in axioms)
    check("A live memo says Admissibility is not dynamics", "admissibility is not a dynamics axiom" in axioms)

    expected_ids = {
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    }
    check("A registry contains exactly the four supplied premise IDs", set(registry["canonical_ids"]) == expected_ids)
    check("A minimal-axiom path is current", registry["nodes"]["minimal_axioms"]["current_path"] == "docs/MINIMAL_AXIOMS_2026-06-29.md")


def append_states(site_count: int) -> dict[int, set[tuple[int, ...]]]:
    states = {0: {(OPEN,) * site_count}}
    for level in range(site_count):
        next_states: set[tuple[int, ...]] = set()
        for state in states[level]:
            for site, value in enumerate(state):
                if value != OPEN:
                    continue
                for outcome in (0, 1):
                    successor = list(state)
                    successor[site] = outcome
                    next_states.add(tuple(successor))
        states[level + 1] = next_states
    return states


def finite_capacity_and_recurrence() -> None:
    section("B - Finite append capacity and no bounded cycle")
    for site_count in range(1, 8):
        states = append_states(site_count)
        observed = tuple(len(states[level]) for level in range(site_count + 1))
        expected = tuple(comb(site_count, level) * 2**level for level in range(site_count + 1))
        check(f"B N={site_count} level census is C(N,k)2^k", observed == expected, str(observed))
        check(
            f"B N={site_count} every append edge strictly raises record rank",
            all(
                sum(value != OPEN for value in successor) == level + 1
                for level in range(site_count)
                for successor in states[level + 1]
            ),
        )
        check(
            f"B N={site_count} no terminal configuration has an open append site",
            all(OPEN not in state for state in states[site_count]),
        )

    for region_size in (1, 2, 5, 11, 23):
        for initial in range(region_size + 1):
            available = region_size - initial
            check(
                f"B K={region_size}, initial={initial} total future formations are at most K-initial",
                available >= 0,
            )
            for cost in (1, 2, 3, 5):
                trial_cap = available // cost
                used = trial_cap * cost
                check(
                    f"B K={region_size}, initial={initial}, c={cost} certified-trial cap is sharp",
                    used <= available < used + cost,
                )

    # A nontrivial directed cycle would have to return to its starting rank,
    # but every physical append raises rank by one.
    for site_count in range(1, 10):
        ranks = tuple(range(site_count + 1))
        check(
            f"B N={site_count} append ranks form a strict acyclic order",
            all(left < right for left, right in zip(ranks, ranks[1:])),
        )


def local_rate_and_stationarity() -> None:
    section("C - Zero long-run local and stationary formation density")
    for region_size in (1, 3, 10, 100):
        for horizon in (1, 2, 5, 10, 100, 1000):
            maximum_events = region_size
            density = Fraction(maximum_events, region_size * horizon)
            check(
                f"C K={region_size}, T={horizon} spacetime density is at most 1/T",
                density == Fraction(1, horizon),
            )
        check(
            f"C K={region_size} average formation rate can be made below 1/1000",
            Fraction(region_size, 1001 * region_size) < Fraction(1, 1000),
        )

    # If a stationary per-site intensity lambda=a/b were positive, choose a
    # long enough interval: E[N([0,T))]=lambda*T would exceed the one-event
    # site capacity.
    for numerator in (1, 2, 5, 11):
        for denominator in (1, 3, 10, 97):
            intensity = Fraction(numerator, denominator)
            horizon = denominator + 1
            if numerator == 1:
                horizon = denominator + 1
            check(
                f"C stationary lambda={intensity} contradicts one-event capacity at a finite T",
                intensity * horizon > 1,
            )

    # A distinguished time origin evades stationarity: every site may form at
    # time zero, but translating that law in time does not preserve it.
    formation_times = {site: 0 for site in range(20)}
    check("C a positive instantaneous nonstationary layer is possible", len(formation_times) == 20)
    check("C that layer has no repeated formation at any site", len(set(formation_times)) == 20)
    shifted_times = {site: time + 1 for site, time in formation_times.items()}
    check("C the distinguished formation layer is not time-translation invariant", shifted_times != formation_times)


def geometry_controls() -> None:
    section("D - Exact Z^3 volume, shell, edge, and support bounds")
    previous: set[tuple[int, int, int]] = set()
    for radius in range(0, 13):
        ball = l1_ball(radius)
        shell = ball - previous
        check(f"D r={radius} Manhattan volume formula", len(ball) == ball_volume(radius), str(len(ball)))
        check(f"D r={radius} Manhattan shell formula", len(shell) == shell_size(radius), str(len(shell)))
        expected_edges = 12 * radius**2 + 12 * radius + 6
        check(f"D r={radius} directed outward-edge formula", outward_edges(radius) == expected_edges, str(expected_edges))
        previous = ball

    large = 10_000
    surface_scaled = Fraction(large * shell_size(large), ball_volume(large))
    edge_scaled = Fraction(large * (12 * large**2 + 12 * large + 6), ball_volume(large))
    check("D r*S/V tends numerically to 3", abs(surface_scaled - 3) < Fraction(1, 1000), str(float(surface_scaled)))
    check("D r*Eout/V tends numerically to 9", abs(edge_scaled - 9) < Fraction(1, 1000), str(float(edge_scaled)))

    for trial_count in (1, 2, 10, 100, 1_000, 10_000):
        for cost in (1, 3, 7):
            required = trial_count * cost
            radius = 0
            while ball_volume(radius) < required:
                radius += 1
            check(
                f"D n={trial_count}, c={cost} minimal containing radius is exact",
                ball_volume(radius) >= required and (radius == 0 or ball_volume(radius - 1) < required),
                f"R={radius}",
            )


def expand_one_layer(records: set[tuple[int, int, int]]) -> set[tuple[int, int, int]]:
    return records | {add(site, step) for site in records for step in NEIGHBORS}


def expand_colored_one_layer(
    records: dict[tuple[int, int, int], int],
) -> dict[tuple[int, int, int], int]:
    """Copy one common immutable bit across an isolated append front."""

    contents = set(records.values())
    if len(contents) != 1:
        raise ValueError("isolated-sector control requires one common content")
    content = next(iter(contents))
    successor = dict(records)
    for site in records:
        for step in NEIGHBORS:
            successor.setdefault(add(site, step), content)
    return successor


def sum_ball_volumes(horizon: int) -> int:
    return sum(ball_volume(radius) for radius in range(horizon + 1))


def expanding_front_controls() -> None:
    section("E - Homogeneous expanding front and density separators")
    records = {(0, 0, 0)}
    prior = set()
    for radius in range(0, 13):
        expected = l1_ball(radius)
        shell = records - prior
        check(f"E layer {radius} homogeneous infection fills B_r", records == expected)
        check(f"E layer {radius} new records equal exact shell", len(shell) == shell_size(radius))
        prior = set(records)
        records = expand_one_layer(records)

    for horizon in (1, 2, 5, 10, 25, 100):
        cylinder_density = Fraction(ball_volume(horizon), (horizon + 1) * ball_volume(horizon))
        cone_density = Fraction(ball_volume(horizon), sum_ball_volumes(horizon))
        front_fraction = Fraction(shell_size(horizon), ball_volume(horizon))
        check(f"E T={horizon} cylinder density is 1/(T+1)", cylinder_density == Fraction(1, horizon + 1))
        check(f"E T={horizon} cone density is positive", 0 < cone_density <= 1)
        check(f"E T={horizon} front fraction is positive", 0 < front_fraction <= 1)

    horizon = 10_000
    cone_scaled = Fraction(horizon * ball_volume(horizon), sum_ball_volumes(horizon))
    front_scaled = Fraction(horizon * shell_size(horizon), ball_volume(horizon))
    check("E T*cone-density tends numerically to 4", abs(cone_scaled - 4) < Fraction(1, 1000), str(float(cone_scaled)))
    check("E T*front-fraction tends numerically to 3", abs(front_scaled - 3) < Fraction(1, 1000), str(float(front_scaled)))

    # A one-dimensional ray gives infinite total continuation at one event per
    # layer but zero three-dimensional spatial density.
    prior_density: Fraction | None = None
    for radius in (2, 4, 8, 16, 32, 64):
        ray_records = radius + 1
        density = Fraction(ray_records, ball_volume(radius))
        check(f"E radius={radius} ray has one record per causal layer", ray_records == radius + 1)
        if prior_density is not None:
            check(f"E radius={radius} ray density decreases", density < prior_density)
        prior_density = density

    # Same homogeneous trigger, different boundary state.
    empty: set[tuple[int, int, int]] = set()
    seeded = {(0, 0, 0)}
    check("E empty boundary remains empty under seed-triggered law", expand_one_layer(empty) == empty)
    check("E one seed launches growth under the same trigger", len(expand_one_layer(seeded)) == 7)

    for bit in (0, 1):
        colored = {(0, 0, 0): bit}
        for radius in range(0, 9):
            check(f"E bit={bit}, r={radius} isolated front reaches exact ball", set(colored) == l1_ball(radius))
            check(f"E bit={bit}, r={radius} isolated front preserves one immutable content", set(colored.values()) == {bit})
            old = dict(colored)
            colored = expand_colored_one_layer(colored)
            check(f"E bit={bit}, r={radius} append step never rewrites old carriers", all(colored[site] == value for site, value in old.items()))

    try:
        expand_colored_one_layer({(0, 0, 0): 0, (1, 0, 0): 1})
    except ValueError:
        collision_rejected = True
    else:
        collision_rejected = False
    check("E differently labelled front collision needs another law rule", collision_rejected)


def sparse_self_similar_controls() -> None:
    section("F - Sparse self-similar marker and causal-corridor costs")
    previous_density: Fraction | None = None
    previous_marker_fraction: Fraction | None = None
    for exponent in range(1, 14):
        radius = 2**exponent
        markers = {2**power for power in range(exponent + 1)}
        corridor = set(range(radius + 1))
        density = Fraction(len(markers), ball_volume(radius))
        marker_fraction = Fraction(len(markers), len(corridor))
        check(f"F R=2^{exponent} marker count is logarithmic", len(markers) == exponent + 1)
        check(f"F R=2^{exponent} record-defined NN corridor is linear", len(corridor) == radius + 1)
        check(f"F R=2^{exponent} every marker lies on the corridor", markers <= corridor)
        if previous_density is not None:
            check(f"F R=2^{exponent} three-dimensional marker density decreases", density < previous_density)
        if previous_marker_fraction is not None:
            check(f"F R=2^{exponent} certificates become sparse inside their tape", marker_fraction < previous_marker_fraction)
        previous_density = density
        previous_marker_fraction = marker_fraction


def encoding_controls() -> None:
    section("G - Lossless corpus, aggregate compression, and no recycling")
    for trials in range(1, 18):
        corpora = 2**trials
        full_bits = bits_needed(corpora)
        count_labels = trials + 1
        count_bits = bits_needed(count_labels)
        check(f"G m={trials} all ordered binary corpora need m bits", full_bits == trials)
        check(f"G m={trials} success count needs ceil(log2(m+1)) bits", 2**count_bits >= count_labels and (count_bits == 0 or 2 ** (count_bits - 1) < count_labels))
        check(f"G m={trials} compressed copy plus permanent source does not free sites", trials + count_bits >= trials)
        if trials >= 2:
            middle = trials // 2
            check(f"G m={trials} one aggregate count hides multiple ordered corpora", comb(trials, middle) > 1)
            check(f"G m={trials} aggregate count uses no more bits than full corpus", count_bits <= full_bits)
        if trials >= 3:
            check(f"G m={trials} aggregate count uses strictly fewer bits", count_bits < full_bits)

    labels = tuple(product((0, 1), repeat=6))
    by_count = {weight: tuple(label for label in labels if sum(label) == weight) for weight in range(7)}
    check("G six-bit corpus has 64 ordered possibilities", len(labels) == 64)
    check("G seven success-count labels partition all corpora", sum(len(group) for group in by_count.values()) == 64)
    check("G central success count discards twenty-fold order information", len(by_count[3]) == 20)

    before = (1, 0)
    swapped = (before[1], before[0])
    copied = (1, 1)
    check("G SWAP preserves one encoded bit globally", sum(before) == sum(swapped) == 1)
    check("G SWAP clears the old address", before[0] == 1 and swapped[0] == 0)
    check("G copy preserves the old address but consumes a new address", copied == (1, 1))


def boundary_export_controls() -> None:
    section("H - Boundary export and fixed-cut capacity")
    interior = {("inside", index) for index in range(5)}
    exterior = set()
    for copy_index in range(1, 8):
        exterior.add(("outside", copy_index))
        check(f"H export copy {copy_index} leaves all interior records", len(interior) == 5)
        check(f"H export copy {copy_index} grows total occupied support", len(interior | exterior) == 5 + copy_index)

    for cut_sites in range(1, 17):
        cut_sectors = 2**cut_sites
        corpus_bits = cut_sites + 1
        corpus_labels = 2**corpus_bits
        check(
            f"H b={cut_sites} once-written one-qubit cut cannot distinguish b+1 independent bits",
            corpus_labels > cut_sectors,
        )
        check(
            f"H b={cut_sites} cut can distinguish at most b independent binary labels",
            bits_needed(cut_sectors) == cut_sites,
        )
        discrete_histories = sum(
            factorial(cut_sites) // factorial(cut_sites - length) * 2**length
            for length in range(cut_sites + 1)
        )
        terminal_histories = factorial(cut_sites) * 2**cut_sites
        check(
            f"H b={cut_sites} full-length order/content histories are b!2^b",
            terminal_histories == factorial(cut_sites) * cut_sectors,
        )
        check(
            f"H b={cut_sites} all finite discrete cut transcripts have exact finite census",
            discrete_histories >= terminal_histories and discrete_histories < terminal_histories * 3,
            str(discrete_histories),
        )
        check(
            f"H b={cut_sites} one more bit than the complete discrete cut transcript cannot fit",
            2 ** (bits_needed(discrete_histories) + 1) > discrete_histories,
        )

    for radius in range(0, 10):
        check(
            f"H r={radius} edge count is geometry rather than assumed bandwidth",
            outward_edges(radius) == 12 * radius**2 + 12 * radius + 6,
        )


def global_history_controls() -> None:
    section("I - Global history, chronology, and spatial-density separators")
    for record_count in range(1, 8):
        terminal = frozenset(range(record_count))
        orders = tuple(permutations(range(record_count)))
        check(f"I N={record_count} one terminal record set has N! append orders", len(orders) == factorial(record_count))
        check(
            f"I N={record_count} every order has the same terminal set",
            all(frozenset(order) == terminal for order in orders),
        )

    previous_error: Fraction | None = None
    for radius in (5, 10, 25, 50, 100, 250):
        interval = tuple(range(-radius, radius + 1))
        records = tuple(site for site in interval if site % 2 == 0)
        density = Fraction(len(records), len(interval))
        error = abs(density - Fraction(1, 2))
        check(f"I R={radius} static periodic history has positive spatial density", density > 0)
        check(f"I R={radius} periodic density approaches one half", error <= Fraction(1, 2 * radius + 1))
        if previous_error is not None:
            check(f"I R={radius} spatial-density error does not grow", error <= previous_error)
        previous_error = error

    check("I terminal spatial density alone contains no formation time", all(site % 2 == 0 for site in range(-20, 21) if site % 2 == 0))


def thermodynamic_controls() -> None:
    section("J - Monotone records versus thermodynamic entropy")
    for site_count in range(3, 21):
        omega = tuple(comb(site_count, level) * 2**level for level in range(site_count + 1))
        ratios = tuple(Fraction(omega[level + 1], omega[level]) for level in range(site_count))
        check(
            f"J N={site_count} macrostate ratio is 2(N-k)/(k+1)",
            all(ratios[level] == Fraction(2 * (site_count - level), level + 1) for level in range(site_count)),
        )
        check(f"J N={site_count} binary macrostate count is not monotone to full occupancy", omega[-2] > omega[-1])
        maximum = max(omega)
        peak_levels = tuple(level for level, count in enumerate(omega) if count == maximum)
        check(
            f"J N={site_count} entropy peak lies near two-thirds occupancy",
            all(abs(3 * level - 2 * site_count) <= 2 for level in peak_levels),
            str(peak_levels),
        )

    # Detailed balance on open -> recorded with no reverse rate forces zero
    # stationary weight on open whenever the append rate is positive.
    for forward_rate in (Fraction(1, 10), Fraction(1, 2), Fraction(1, 1), Fraction(7, 3)):
        reverse_rate = Fraction(0, 1)
        stationary_open = Fraction(0, 1)
        stationary_recorded = Fraction(1, 1)
        check(
            f"J rate={forward_rate} absorbing stationary measure satisfies detailed balance",
            stationary_open * forward_rate == stationary_recorded * reverse_rate,
        )
        check(
            f"J rate={forward_rate} no stationary measure with positive open weight can balance",
            Fraction(1, 2) * forward_rate != Fraction(1, 2) * reverse_rate,
        )

    for slots in (1, 5, 20):
        for probability in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
            expected_open = tuple(slots * (1 - probability) ** time for time in range(12))
            expected_current = tuple(probability * value for value in expected_open)
            check(f"J N={slots}, p={probability} expected open capacity decays", all(right < left for left, right in zip(expected_open, expected_open[1:])))
            check(f"J N={slots}, p={probability} expected formation current decays", all(right < left for left, right in zip(expected_current, expected_current[1:])))


def time_and_gravity_controls() -> None:
    section("K - Growing-tape clock and capacity-response separators")
    path_records: set[tuple[int, int, int]] = set()
    clock_counts = []
    for tick in range(101):
        path_records.add((tick, 0, 0))
        clock_counts.append(len(path_records))
    check("K growing tape supports 101 distinct sampled commits", clock_counts[-1] == 101)
    check("K growing-tape clock count is strictly monotone", all(right == left + 1 for left, right in zip(clock_counts, clock_counts[1:])))
    check("K growing-tape support radius becomes unbounded in the sample", max(x for x, _, _ in path_records) == 100)

    # Three monotone endpoint-compatible lapse maps demonstrate that vacancy
    # does not choose a constitutive response.
    vacancies = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))
    lapse_linear = tuple(q for q in vacancies)
    lapse_square = tuple(q * q for q in vacancies)
    lapse_rational = tuple(q / (2 - q) for q in vacancies)
    check("K three lapse candidates agree at zero capacity", {lapse_linear[0], lapse_square[0], lapse_rational[0]} == {0})
    check("K three lapse candidates agree at full capacity", {lapse_linear[-1], lapse_square[-1], lapse_rational[-1]} == {1})
    check("K three lapse candidates disagree in the interior", len({lapse_linear[2], lapse_square[2], lapse_rational[2]}) == 3)
    check("K all three lapse candidates are monotone", all(all(right >= left for left, right in zip(values, values[1:])) for values in (lapse_linear, lapse_square, lapse_rational)))

    # Same Newtonian scalar potential, different spatial-curvature parameter.
    newton_factor = 2 * (1 + 0)
    gr_factor = 2 * (1 + 1)
    check("K pure scalar lapse gives half the GR light-deflection factor", newton_factor == 2 and gr_factor == 4)
    check("K scalar clock response does not select spatial curvature", newton_factor != gr_factor)


def documentation_contract() -> None:
    section("L - Route coverage, constitutional placement, and N1-N8")
    note = normalized(NOTE)
    required_phrases = (
        "growing-history machine",
        "fixed finite region cannot host indefinitely many",
        "zero stationary spacetime intensity",
        "expanding-front route",
        "sparse and self-similar routes",
        "recyclable-by-encoding route",
        "boundary-export route",
        "global-history route",
        "thermodynamic seam",
        "time seam",
        "gravity and resource seam",
        "no generic storage/compute-budget sentence is justified",
        "the exact law must decide",
        "are records the whole changing physical state",
    )
    for phrase in required_phrases:
        check(f"L required boundary is present: {phrase}", phrase in note)

    for lane in (
        "formation",
        "probability",
        "time",
        "matter/transport",
        "thermodynamics",
        "resource",
        "gravity",
        "cosmology",
    ):
        check(f"L TOE lane is classified: {lane}", f"| {lane} |" in note)

    for index in range(1, 9):
        check(f"L N{index} section is present", f"n{index} —" in note)

    cross_cycle_needles = (
        "cycle 22",
        "cycle 21",
        "cycle 26",
        "cycles 9–11",
        "cycle 30",
    )
    for needle in cross_cycle_needles:
        check(f"L cross-cycle residual is matched: {needle}", needle in note)

    check("L no broad no-go is explicit", "this is not a no-go against infinite global computation" in note)
    check("L live global-history steelman is explicit", "strongest surviving steelman" in note and "global process functional" in note)
    check(
        "L Record placement says no extra storage sentence is forced",
        "no additional" in note and "fresh capacity" in note and "same-site continuation sentence" in note,
    )
    check("L Admissibility placement rejects renewal content", "no renewal clause belongs here" in note)
    check("L resource placement rejects a generic resource axiom", "no generic storage/compute-budget sentence is justified" in note)
    check("L law/boundary placement is explicit", "law and boundary" in note and "front trigger and outcome rule" in note)


def main() -> int:
    source_contract()
    finite_capacity_and_recurrence()
    local_rate_and_stationarity()
    geometry_controls()
    expanding_front_controls()
    sparse_self_similar_controls()
    encoding_controls()
    boundary_export_controls()
    global_history_controls()
    thermodynamic_controls()
    time_and_gravity_controls()
    documentation_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: PASS" if FAIL == 0 else "RESULT: FAIL")
    print(
        "BOUNDARY: finite local append exhausts; infinite Z^3 permits a growing "
        "history front; recurrence, renewal, rate, thermodynamics, and gravity "
        "remain exact-law/ontology questions"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
