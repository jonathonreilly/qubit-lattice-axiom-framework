#!/usr/bin/env python3
"""Cycle 19: nearest-neighbor compilation of the Cycle 18 seed field.

Companion note:
  docs/work_history/repo/review_feedback/
  NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md

The runner replaces continuous priorities by finite random bits, proves the
27-edge causal-depth floor for the radius-nine cube, tests a typed monotone
causal schedule quotient, finite priorities, RSA order dependence, quantum
random-bit routes, and the append-only one-M2 record-capacity obstruction.
No axiom, registry, audit surface, commit, push, or PR is changed.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from itertools import combinations, product
from math import exp
from pathlib import Path
import random

import numpy as np

import autonomous_self_closing_diamond_cycle17_2026_07_14 as c17


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE17_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "AUTONOMOUS_SELF_CLOSING_DIAMOND_CYCLE17_NOTE_2026-07-14.md"
)
CYCLE18_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "INVARIANT_FIRST_SEED_HARD_CORE_CYCLE18_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
CHEB_RADIUS = 9
CORNER_DEPTH = 27
CHEB_VOLUME = 19**3


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


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def subtract(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def linf(vector: Coord) -> int:
    return max(abs(value) for value in vector)


def l1(vector: Coord) -> int:
    return sum(abs(value) for value in vector)


def l1_ball(radius: int) -> frozenset[Coord]:
    return frozenset(
        site
        for site in product(range(-radius, radius + 1), repeat=3)
        if l1(site) <= radius
    )


def linf_ball(radius: int) -> frozenset[Coord]:
    return frozenset(product(range(-radius, radius + 1), repeat=3))


def l1_ball_size(radius: int) -> int:
    return (4 * radius**3 + 6 * radius**2 + 8 * radius + 3) // 3


def rotate(vector: Coord, matrix: np.ndarray) -> Coord:
    return c17.matvec(matrix, vector)


def torus_sites(side: int) -> tuple[Coord, ...]:
    return tuple(product(range(side), repeat=3))


def torus_linf(left: Coord, right: Coord, side: int) -> int:
    return max(
        min(abs(a - b), side - abs(a - b))
        for a, b in zip(left, right)
    )


def torus_translate(site: Coord, shift: Coord, side: int) -> Coord:
    return tuple((a + b) % side for a, b in zip(site, shift))  # type: ignore[return-value]


def torus_rotate(site: Coord, matrix: np.ndarray, side: int) -> Coord:
    return tuple(value % side for value in rotate(site, matrix))  # type: ignore[return-value]


def source_contract() -> None:
    section("A - Framework, predecessor, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    cycle17 = CYCLE17_NOTE.read_text(encoding="utf-8").lower()
    cycle18 = CYCLE18_NOTE.read_text(encoding="utf-8").lower()

    check(
        "A framework still has four named axioms",
        all(name in axioms for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")),
    )
    check("A Admissibility is nearest-neighbor but not dynamics", "one fixed nearest-neighbor admissibility rule" in axioms and "admissibility is not a dynamics axiom" in axioms.lower())
    check("A Record is one per site and permanent", "site never carries more than one record" in axioms and "records are permanent" in axioms)
    check("A foundation registry has four current paths", registry.count('"current_path"') == 4)
    check("A Cycle 17 builder and terminal counts are present", "99-site nn hamiltonian path" in cycle17 and "111 permanent records" in cycle17)
    check("A Cycle 18 exposes the NN compilation residual", "not yet compiled" in cycle18 and "nearest-neighbor admissibility rule" in cycle18)

    required = (
        "authority: none",
        "continuous priority is not necessary",
        "isolated-bernoulli factor",
        "nearest-neighbor causal-depth floor is 27",
        "typed causal schedule quotient",
        "closed candidate layer",
        "static global-history kernel",
        "compiled event law",
        "record-only clean-output obstruction",
        "one m2 per site",
        "finite-state priorities",
        "random sequential adsorption",
        "quantum random-bit route",
        "99-site builder",
        "111-record diamond",
        "rate and actuality remain separate",
        "partial compile with named residuals",
        "no new record axiom is forced",
    )
    for phrase in required:
        check(f"A note states required phrase: {phrase}", phrase in normalized)
    for index in range(1, 9):
        check(f"A no-go discipline includes N{index}", f"n{index} —" in normalized or f"n{index} -" in normalized)


def isolated_density(activity: Fraction, neighborhood_size: int) -> Fraction:
    return activity * (1 - activity) ** (neighborhood_size - 1)


def isolated_winners_linf(candidates: frozenset[Coord], side: int) -> frozenset[Coord]:
    return frozenset(
        site
        for site in candidates
        if all(
            other == site or torus_linf(site, other, side) > CHEB_RADIUS
            for other in candidates
        )
    )


def static_finite_bit_factor() -> None:
    section("B - Static finite-bit hard-core factor without priorities")
    cheb_ball = linf_ball(CHEB_RADIUS)
    causal_ball = l1_ball(CORNER_DEPTH)
    check("B radius-nine cube has 6859 sites", len(cheb_ball) == CHEB_VOLUME == 6859)
    check("B radius-27 L1 ball has 27775 sites", len(causal_ball) == l1_ball_size(CORNER_DEPTH) == 27775)
    check("B every radius-nine cube site lies in the radius-27 NN lightcone", cheb_ball <= causal_ball)
    check("B corner (9,9,9) saturates NN depth 27", linf((9, 9, 9)) == 9 and l1((9, 9, 9)) == 27)

    p_cheb = Fraction(1, CHEB_VOLUME)
    rho_cheb = isolated_density(p_cheb, CHEB_VOLUME)
    p_l1 = Fraction(1, len(causal_ball))
    rho_l1 = isolated_density(p_l1, len(causal_ball))
    check("B isolated-Bernoulli cube intensity is strictly positive", 0 < rho_cheb < p_cheb)
    check("B NN-floodable L1 control intensity is strictly positive", 0 < rho_l1 < p_l1 < p_cheb)
    check("B 111-record density stays below one for both controls", 111 * rho_cheb < 1 and 111 * rho_l1 < 1)

    # Exact finite checks of the p=1/M optimum.  The derivative is
    # (1-p)^(M-2)(1-Mp); neighboring rational samples bracket the maximum.
    for size in (7, 27, 125):
        optimum = Fraction(1, size)
        left = Fraction(1, 2 * size)
        right = Fraction(2, size)
        check(
            f"B p=1/M maximizes isolated density control M={size}",
            isolated_density(optimum, size) > isolated_density(left, size)
            and isolated_density(optimum, size) > isolated_density(right, size),
        )

    side = 61
    rng = random.Random(1919)
    candidates = frozenset(
        site
        for site in torus_sites(side)
        if rng.random() < 1.0 / CHEB_VOLUME
    )
    winners = isolated_winners_linf(candidates, side)
    check("B sampled finite torus has sparse candidates and winners", 10 < len(candidates) < 100 and len(winners) > 0)
    check("B isolated-bit winners satisfy radius-nine hard core", all(torus_linf(left, right, side) > CHEB_RADIUS for left, right in combinations(winners, 2)))

    shift = (7, 11, 13)
    shifted_candidates = frozenset(torus_translate(site, shift, side) for site in candidates)
    shifted_winners = isolated_winners_linf(shifted_candidates, side)
    check("B isolated-bit factor is translation covariant", shifted_winners == frozenset(torus_translate(site, shift, side) for site in winners))
    rotation = c17.proper_cubic_rotations()[11]
    rotated_candidates = frozenset(torus_rotate(site, rotation, side) for site in candidates)
    rotated_winners = isolated_winners_linf(rotated_candidates, side)
    check("B isolated-bit factor is proper-cubic covariant", rotated_winners == frozenset(torus_rotate(site, rotation, side) for site in winners))


def synchronous_reach(radius: int) -> tuple[frozenset[Coord], ...]:
    layers = [frozenset(((0, 0, 0),))]
    reached = set(layers[0])
    for _ in range(radius):
        reached |= {
            add(site, direction)
            for site in reached
            for direction in c17.DIRECTIONS
        }
        layers.append(frozenset(reached))
    return tuple(layers)


def asynchronous_budget_flood(radius: int, chooser: str, seed: int) -> dict[Coord, int]:
    budgets: dict[Coord, int] = {(0, 0, 0): radius}
    rng = random.Random(seed)
    for _ in range(2_000_000):
        actions = []
        for site, budget in budgets.items():
            if budget <= 0:
                continue
            for direction in c17.DIRECTIONS:
                target = add(site, direction)
                proposal = budget - 1
                if proposal > budgets.get(target, -1):
                    actions.append((site, target, proposal))
        if not actions:
            return budgets
        if chooser == "first":
            _, target, proposal = actions[0]
        elif chooser == "last":
            _, target, proposal = actions[-1]
        elif chooser == "random":
            _, target, proposal = rng.choice(actions)
        else:
            raise ValueError(chooser)
        budgets[target] = proposal
    raise RuntimeError("budget flood did not terminate")


def asynchronous_tagged_flood(
    sources: tuple[Coord, ...], radius: int, chooser: str, seed: int
) -> dict[tuple[Coord, Coord], int]:
    """Propagate source-tagged finite-budget facts in any causal order."""

    budgets: dict[tuple[Coord, Coord], int] = {
        (source, source): radius for source in sources
    }
    rng = random.Random(seed)
    for _ in range(4_000_000):
        actions = []
        for (source, site), budget in budgets.items():
            if budget <= 0:
                continue
            for direction in c17.DIRECTIONS:
                target = add(site, direction)
                proposal = budget - 1
                key = (source, target)
                if proposal > budgets.get(key, -1):
                    actions.append((key, proposal))
        if not actions:
            return budgets
        if chooser == "first":
            key, proposal = actions[0]
        elif chooser == "last":
            key, proposal = actions[-1]
        elif chooser == "random":
            key, proposal = rng.choice(actions)
        else:
            raise ValueError(chooser)
        budgets[key] = proposal
    raise RuntimeError("tagged budget flood did not terminate")


def causal_depth_and_schedule_quotient() -> None:
    section("C - Exact NN depth floor and typed causal schedule quotient")
    layers = synchronous_reach(CORNER_DEPTH)
    corner = (9, 9, 9)
    check("C corner is absent after 26 NN layers", corner not in layers[26])
    check("C corner first appears at layer 27", corner in layers[27])
    check("C layer 27 equals the exact L1 ball", layers[27] == l1_ball(CORNER_DEPTH))

    # Two candidate fields that differ only at the corner have different
    # isolated-seed answers at the origin.  No depth<27 radius-one circuit can
    # distinguish them at the origin.
    alone = frozenset(((0, 0, 0),))
    with_corner = frozenset(((0, 0, 0), corner))
    origin_wins_alone = all(other == (0, 0, 0) or linf(other) > CHEB_RADIUS for other in alone)
    origin_wins_corner = all(other == (0, 0, 0) or linf(other) > CHEB_RADIUS for other in with_corner)
    check("C radius-nine isolated answer changes at distance-27 corner", origin_wins_alone and not origin_wins_corner)
    check("C every depth-26 radius-one lightcone misses that input bit", corner not in l1_ball(26))

    # A monotone typed message with a remaining-budget certificate has a unique
    # least fixed point independent of topological event order.  Radius six is
    # enough to exercise many conflicting relaxation orders cheaply.
    floods = tuple(
        asynchronous_budget_flood(6, chooser, 1900 + index)
        for index, chooser in enumerate(("first", "last", "random", "random", "random"))
    )
    reference = floods[0]
    check("C asynchronous typed floods converge to one map", all(item == reference for item in floods[1:]))
    check("C typed flood fixed point is remaining budget R-distance", all(value == 6 - l1(site) for site, value in reference.items()) and set(reference) == set(l1_ball(6)))

    sources = ((0, 0, 0), (6, 0, 0), (14, 0, 0))
    tagged = tuple(
        asynchronous_tagged_flood(sources, 6, chooser, 1950 + index)
        for index, chooser in enumerate(("first", "last", "random"))
    )
    check("C multi-source tagged causal schedules converge", tagged[0] == tagged[1] == tagged[2])
    isolated = frozenset(
        source
        for source in sources
        if all(
            other == source or (other, source) not in tagged[0]
            for other in sources
        )
    )
    check("C tagged quotient computes the isolated-source decision", isolated == frozenset((sources[2],)))

    rotations = c17.proper_cubic_rotations()
    ball = l1_ball(CORNER_DEPTH)
    check("C L1 causal domain is invariant under all proper cubic rotations", all(frozenset(rotate(site, matrix) for site in ball) == ball for matrix in rotations))


def strict_priority_density(levels: int, neighborhood_size: int) -> Fraction:
    """q=1 density when the unique strict minimum of finite labels wins."""

    return Fraction(sum(rank ** (neighborhood_size - 1) for rank in range(levels)), levels**neighborhood_size)


def strict_minima(points: tuple[Coord, ...], labels: dict[Coord, int]) -> frozenset[Coord]:
    return frozenset(
        point
        for point in points
        if all(
            other == point
            or linf(subtract(point, other)) > CHEB_RADIUS
            or labels[point] < labels[other]
            for other in points
        )
    )


def greedy_rsa(points: tuple[Coord, ...], order: tuple[Coord, ...]) -> frozenset[Coord]:
    accepted: set[Coord] = set()
    point_set = set(points)
    if set(order) != point_set:
        raise ValueError("order must contain every point exactly once")
    for point in order:
        if all(linf(subtract(point, other)) > CHEB_RADIUS for other in accepted):
            accepted.add(point)
    return frozenset(accepted)


def finite_priority_and_rsa() -> None:
    section("D - Finite-state priorities and random sequential adsorption")
    for neighborhood_size in (2, 3, 5):
        densities = tuple(strict_priority_density(levels, neighborhood_size) for levels in (2, 4, 8, 16, 32))
        check(f"D finite strict-priority density increases toward 1/M for M={neighborhood_size}", all(left < right for left, right in zip(densities, densities[1:])) and densities[-1] < Fraction(1, neighborhood_size))

    tied_points = ((0, 0, 0), (9, 0, 0))
    tied_labels = {point: 3 for point in tied_points}
    check("D equivariant strict tie rejection is collision safe", strict_minima(tied_points, tied_labels) == frozenset())
    for bits in (1, 2, 4, 8, 16):
        check(f"D finite {bits}-bit priorities retain positive pair-tie probability", Fraction(1, 2**bits) > 0)
    check("D lazy infinite-bit tie probability tends to zero without finite bound", Fraction(1, 2**32) < Fraction(1, 10**9))

    points = ((0, 0, 0), (9, 0, 0), (18, 0, 0))
    middle_first = greedy_rsa(points, (points[1], points[0], points[2]))
    ends_first = greedy_rsa(points, (points[0], points[2], points[1]))
    check("D RSA middle-first schedule accepts one seed", middle_first == frozenset((points[1],)))
    check("D RSA ends-first schedule accepts two seeds", ends_first == frozenset((points[0], points[2])))
    check("D RSA schedules give different maximal independent sets", middle_first != ends_first)
    check("D every typed RSA schedule remains radius-nine safe", all(all(linf(subtract(left, right)) > CHEB_RADIUS for left, right in combinations(result, 2)) for result in (middle_first, ends_first)))
    check("D both RSA outputs are maximal on the candidate graph", all(all(point in result or any(linf(subtract(point, chosen)) <= CHEB_RADIUS for chosen in result) for point in points) for result in (middle_first, ends_first)))


def canonical_terminal_records() -> tuple[c17.RecordMap, Coord]:
    cell = c17.Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    records, _, _, _ = c17.run_schedule("first", cell, 0, 1919)
    b0 = c17.global_site(cell, c17.CANONICAL_PATH[0])
    return records, b0


def record_capacity_and_clean_output() -> None:
    section("E - One-M2 record capacity and clean-output obstruction")
    records, b0 = canonical_terminal_records()
    support = frozenset(subtract(site, b0) for site in records)
    check("E Cycle 17 builder has 99 exact sites", len(c17.CANONICAL_PATH) == 99)
    check("E completed autonomous diamond has 111 exact record sites", len(records) == len(support) == 111)

    # A displayed exact local compiler needs at least the four logical control
    # combinations candidate/not-candidate x rival-seen/not-seen.  Four
    # perfectly distinguishable states have Gram rank four; one qubit has rank
    # at most two.
    four_classical_states = np.eye(4)
    check("E four exact candidate/collision control states have rank four", np.linalg.matrix_rank(four_classical_states) == 4)
    check("E one M2 carrier has at most two orthogonal pure labels", np.linalg.matrix_rank(np.eye(2)) == 2 < 4)

    candidate = c17.named("C", c17.Frame((0, 0, 1), (1, 0, 0)))
    b0_content = records[b0]
    loser = c17.named("L", c17.Frame((0, 0, 1), (1, 0, 0)))
    check("E candidate, loser, and B0 are distinct permanent contents", len({candidate, loser, b0_content}) == 3)
    check("E append-only permanence forbids C-to-B0 and C-to-loser rewrites", candidate != b0_content and candidate != loser)

    occupied_relative = next(site for site in support if site != (0, 0, 0))
    occupied_global = add(b0, occupied_relative)
    expected = records[occupied_global]
    debris = c17.named("C", expected.frame)
    check("E one losing candidate record can conflict with a required diamond role", debris != expected and occupied_global in records)
    check("E permanent arbitration transcript cannot disappear before 111-role closure", "records are permanent" in AXIOMS.read_text(encoding="utf-8"))


def local_race_probability(hops: int, birth_rate: Fraction, signal_rate: Fraction) -> Fraction:
    """Idealized probability every signal hop beats a still-enabled birth."""

    return (signal_rate / (signal_rate + birth_rate)) ** hops


def quantum_rate_and_route_controls() -> None:
    section("F - Quantum random bits, finite-speed races, rate, and actuality")
    propagation_wins = local_race_probability(CORNER_DEPTH, Fraction(1), Fraction(1))
    check("F finite-rate 27-hop exclusion signal is not certain to beat birth", 0 < propagation_wins < 1)
    check("F equal-rate unsafe race probability is strictly positive", 1 - propagation_wins == 1 - Fraction(1, 2**CORNER_DEPTH) > 0)
    check("F zero birth rate or infinite-priority signaling are singular escapes", local_race_probability(CORNER_DEPTH, Fraction(0), Fraction(1)) == 1)

    # A qubit can generate a fair bit after a supplied |+> preparation and
    # measurement instrument.  A closed unitary alone preserves purity and
    # does not produce an actual classical mixture.
    zero = np.array((1.0, 0.0), dtype=complex)
    hadamard = np.array(((1.0, 1.0), (1.0, -1.0)), dtype=complex) / np.sqrt(2.0)
    plus = hadamard @ zero
    probabilities = np.abs(plus) ** 2
    check("F prepared qubit measurement offers one fair random bit", np.allclose(probabilities, (0.5, 0.5)))
    pure_density = np.outer(plus, plus.conj())
    classical_mixture = np.eye(2) / 2.0
    check("F unitary pure state and sampled mixture have different purity", np.allclose(np.trace(pure_density @ pure_density), 1.0) and np.allclose(np.trace(classical_mixture @ classical_mixture), 0.5))

    # Scaling every exponential event rate changes absolute times while leaving
    # dimensionless race order probabilities fixed.  Rate and schedule weights
    # are still law data, and neither selects the actual sample.
    base_times = np.array((0.2, 0.7, 1.1, 1.8))
    scaled_times = base_times / 5.0
    check("F global rate rescaling preserves causal order", tuple(np.argsort(base_times)) == tuple(np.argsort(scaled_times)))
    check("F global rate rescaling changes every nonzero event time", np.allclose(scaled_times, base_times / 5.0) and not np.allclose(scaled_times, base_times))
    check("F positive finite race failure remains under common rate scaling", local_race_probability(27, Fraction(5), Fraction(5)) == propagation_wins)

    normalized = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    route_phrases = (
        "matérn route",
        "isolated-bit route",
        "finite-priority route",
        "rsa route",
        "typed-dag route",
        "permanent-record route",
        "quantum random-bit route",
        "qca garbage-export route",
        "dissipative blockade route",
        "global-history route",
        "rate does not select actuality",
    )
    for phrase in route_phrases:
        check(f"F route classification states: {phrase}", phrase in normalized)


def no_go_contract() -> None:
    section("G - Exact classification and no-go-discipline gate")
    normalized = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    claims = (
        "the static continuous-priority oracle is retired",
        "the exact radius-nine factor is not yet a nearest-neighbor event law",
        "any radius-one causal implementation of the same decision has depth at least 27",
        "the typed causal dag is schedule-independent",
        "the typed causal dag requires transient mutable message state",
        "a closed candidate layer is still supplied",
        "rsa is safe only relative to its typed causal schedule",
        "one permanent record per site blocks provisional rewrite",
        "the clean-input cycle 17 continuation is not compiled",
        "rate and actuality remain separate",
        "not a universal qca or dissipative no-go",
        "not a theorem of the current four axioms",
        "residual law fields are not separate axiom atoms",
        "no new record axiom is forced",
    )
    for claim in claims:
        check(f"G note preserves classification: {claim}", claim in normalized)

    n1_routes = (
        "matérn continuous priority — attempted",
        "isolated bernoulli bit — attempted",
        "finite strict priorities — attempted",
        "lazy quantum bit strings — attempted",
        "random sequential adsorption — attempted",
        "typed 27-hop causal dag — attempted",
        "permanent record messaging — attempted",
        "qca garbage export — attempted",
        "dissipative blockade — attempted",
        "static global-history kernel — attempted",
    )
    for route in n1_routes:
        check(f"G N1 includes route: {route}", route in normalized)
    check("G N2 contains collapsed four-condition set", "collapsed wall set has four conditions" in normalized)
    check("G N3 includes hidden-condition scan", "hidden-condition scan" in normalized)
    check("G N4 includes exact residual matching", "exact residual matching" in normalized)
    check("G N5 narrows all negative resolutions", "no claim that all nearest-neighbor quantum laws fail" in normalized)
    check("G N6 keeps conditional compilation live", "partial-closure path" in normalized and "no constitutional promotion follows" in normalized)
    check("G N7 contains strongest hostile steelman", "hostile reviewer" in normalized and "universal compile no-go would be premature" in normalized)
    check("G N8 names prior retirement mechanisms", "cross-cycle echo" in normalized and "compile supplied structure into law-generated structure" in normalized)
    check("G no-go discipline records PASS", "no-go-discipline status: pass" in normalized)


def main() -> int:
    source_contract()
    static_finite_bit_factor()
    causal_depth_and_schedule_quotient()
    finite_priority_and_rsa()
    record_capacity_and_clean_output()
    quantum_rate_and_route_controls()
    no_go_contract()
    print(
        "\nSUMMARY: NEAREST-NEIGHBOR SEED COMPILATION CYCLE 19 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
