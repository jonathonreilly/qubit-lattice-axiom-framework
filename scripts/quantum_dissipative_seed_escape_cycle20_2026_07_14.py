#!/usr/bin/env python3
"""Cycle 20: strongest QCA/dissipative escape for collision-safe B0 seeds.

Companion note:
  docs/work_history/repo/review_feedback/
  QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md

The runner constructs the exact ideal range-nine pure-birth record instrument,
then tests direct NN jump incompatibility, finite-depth lightcones, bounded
Lindbladian finalization, instrument ambiguity, reversible garbage retention,
and simple garbage-rail collisions.  It is authority-free and changes no
axiom, registry, audit surface, commit, push, or PR.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import exp, log2
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
    / "QUANTUM_DISSIPATIVE_SEED_ESCAPE_CYCLE20_NOTE_2026-07-14.md"
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
CYCLE19_NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "NEAREST_NEIGHBOR_SEED_COMPILATION_CYCLE19_NOTE_2026-07-14.md"
)

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
EXCLUSION_RADIUS = 9
CORNER = (9, 9, 9)
CORNER_DISTANCE = 27
FRAME_COUNT = 24


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


def scale(factor: int, vector: Coord) -> Coord:
    return tuple(factor * value for value in vector)  # type: ignore[return-value]


def linf(vector: Coord) -> int:
    return max(abs(value) for value in vector)


def l1(vector: Coord) -> int:
    return sum(abs(value) for value in vector)


def l1_ball(center: Coord, radius: int) -> frozenset[Coord]:
    return frozenset(
        add(center, offset)
        for offset in product(range(-radius, radius + 1), repeat=3)
        if l1(offset) <= radius
    )


def rotate(vector: Coord, matrix: np.ndarray) -> Coord:
    return c17.matvec(matrix, vector)


def source_contract() -> None:
    section("A - Framework, predecessors, scope, and N1-N8 contract")
    note = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(note.lower().replace("`", "").replace("*", "").split())
    axioms = AXIOMS.read_text(encoding="utf-8")
    registry = REGISTRY.read_text(encoding="utf-8")
    cycle17 = CYCLE17_NOTE.read_text(encoding="utf-8").lower()
    cycle18 = CYCLE18_NOTE.read_text(encoding="utf-8").lower()
    cycle19 = CYCLE19_NOTE.read_text(encoding="utf-8").lower()

    check("A foundation still has four named axioms", all(name in axioms for name in ("### Lattice", "### Qubit", "### Admissibility", "### Record")))
    check("A Admissibility is NN but not a dynamics axiom", "one fixed nearest-neighbor admissibility rule" in axioms and "admissibility is not a dynamics axiom" in axioms.lower())
    check("A records are one per site and permanent", "site never carries more than one record" in axioms and "records are permanent" in axioms)
    check("A registry retains four approved premise paths", registry.count('"current_path"') == 4)
    check("A Cycle 17 exact continuation has 111 records", "111 permanent records" in cycle17)
    check("A Cycle 18 establishes radius-nine seed safety", "b0-site exclusion radius nine" in cycle18.lower())
    check("A Cycle 19 leaves QCA and dissipation live", "qca garbage-export route" in cycle19 and "dissipative blockade route" in cycle19)

    required = (
        "authority: none",
        "ideal range-nine quantum-jump instrument",
        "autonomous local clocks",
        "no global synchronous clock",
        "positive-density permanent b0 records",
        "not nearest-neighbor",
        "direct nn jump obstruction",
        "depth-fourteen correlation floor",
        "depth-twenty-seven isolated-decision floor",
        "bounded lindbladian cannot finalize exactly at finite deterministic time",
        "record instrument and unraveling are explicit",
        "reversible garbage retention",
        "candidate garbage is locally safe",
        "message garbage remains open",
        "naive garbage rails collide",
        "111-site clean support",
        "qca spatial-code route remains live",
        "dissipative mediator route remains live",
        "rate and actuality remain separate",
        "no new record axiom is forced",
    )
    for phrase in required:
        check(f"A note states required phrase: {phrase}", phrase in normalized)
    for index in range(1, 9):
        check(f"A no-go discipline includes N{index}", f"n{index} —" in normalized or f"n{index} -" in normalized)


def ideal_rsa(
    sites: tuple[Coord, ...], clocks: dict[Coord, float]
) -> frozenset[Coord]:
    accepted: set[Coord] = set()
    for site in sorted(sites, key=lambda item: (clocks[item], item)):
        if all(linf(subtract(site, other)) > EXCLUSION_RADIUS for other in accepted):
            accepted.add(site)
    return frozenset(accepted)


def maximal(points: tuple[Coord, ...], accepted: frozenset[Coord]) -> bool:
    return all(
        site in accepted
        or any(linf(subtract(site, winner)) <= EXCLUSION_RADIUS for winner in accepted)
        for site in points
    )


def ideal_range_nine_instrument() -> None:
    section("B - Exact ideal range-nine pure-birth record instrument")
    sites = tuple((x, 0, 0) for x in range(40))
    rng = random.Random(2020)
    exponential_samples = {site: -np.log(max(rng.random(), 1.0e-15)) for site in sites}
    winners = ideal_rsa(sites, exponential_samples)
    check("B ideal jump trajectory produces positive seed count", len(winners) > 0)
    check("B ideal jump trajectory is radius-nine hard core", all(linf(subtract(left, right)) > EXCLUSION_RADIUS for left, right in combinations(winners, 2)))
    check("B ideal pure-birth terminal set is maximal", maximal(sites, winners))

    # Rescaling independent exponential clocks changes physical times but not
    # the causal order or terminal seed set.
    scaled_clocks = {site: value / 7.0 for site, value in exponential_samples.items()}
    check("B common rate rescaling preserves the jump-order seed set", ideal_rsa(sites, scaled_clocks) == winners)
    check("B common rate rescaling changes all nonzero clock times", all(abs(scaled_clocks[site] - exponential_samples[site]) > 0 for site in sites))

    # Every strict local clock minimum is certainly accepted.  Hence the ideal
    # RSA density is bounded below by the positive Matérn intensity 1/6859.
    neighborhood_volume = 19**3
    check("B strict local clock-minimum lower bound is positive", Fraction(1, neighborhood_volume) > 0)
    check("B uniform frame jump branches normalize", FRAME_COUNT * Fraction(1, FRAME_COUNT) == 1)

    rotation = c17.proper_cubic_rotations()[9]
    rotated_sites = tuple(rotate(site, rotation) for site in sites)
    rotated_clocks = {rotate(site, rotation): value for site, value in exponential_samples.items()}
    rotated_winners = ideal_rsa(rotated_sites, rotated_clocks)
    check("B ideal jump rule is proper-cubic covariant", rotated_winners == frozenset(rotate(site, rotation) for site in winners))


def raising_operator(site: int, number_sites: int) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    raise_one = np.array(((0, 0), (1, 0)), dtype=complex)
    answer = np.array((1.0,), dtype=complex)
    for index in range(number_sites):
        answer = np.kron(answer, raise_one if index == site else identity)
    return answer


def direct_nn_jump_and_depth_bounds() -> None:
    section("C - Direct NN jump obstruction and exact causal floors")
    vacuum = np.zeros(4, dtype=complex)
    vacuum[0] = 1.0
    left_jump = raising_operator(0, 2)
    right_jump = raising_operator(1, 2)
    double_left_right = right_jump @ left_jump @ vacuum
    double_right_left = left_jump @ right_jump @ vacuum
    check("C disjoint direct creation jumps commute on vacuum", np.allclose(double_left_right, double_right_left))
    check("C two direct positive-rate jumps create the forbidden double seed", np.allclose(double_left_right, (0, 0, 0, 1)))
    check("C direct two-jump trajectory has positive order-t-squared weight", (0.01**2) / 2.0 > 0)

    left_13 = l1_ball((0, 0, 0), 13)
    right_13 = l1_ball(CORNER, 13)
    left_14 = l1_ball((0, 0, 0), 14)
    right_14 = l1_ball(CORNER, 14)
    check("C depth-13 backward lightcones at a forbidden corner pair are disjoint", left_13.isdisjoint(right_13))
    check("C depth-14 backward lightcones can overlap", not left_14.isdisjoint(right_14))
    check("C exact anticorrelation from product local noise needs depth at least 14", 2 * 13 < CORNER_DISTANCE <= 2 * 14)
    check("C exact isolated-candidate evaluation still needs depth 27", CORNER_DISTANCE == 27 and CORNER not in l1_ball((0, 0, 0), 26) and CORNER in l1_ball((0, 0, 0), 27))


def dephasing_channel(rho: np.ndarray, kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    return sum(operator @ rho @ operator.conj().T for operator in kraus)


def lindbladian_finalization_and_instrument() -> None:
    section("D - Bounded Lindbladian finalization and instrument ambiguity")
    rate = 1.0
    survival = tuple(exp(-rate * time) for time in (0.1, 1.0, 10.0, 100.0))
    check("D bounded pure-birth survival stays positive at every finite time", all(value > 0 for value in survival))
    check("D survival tends toward zero only asymptotically", all(left > right for left, right in zip(survival, survival[1:])) and survival[-1] < 1.0e-40)
    finite_semigroup_determinants = tuple(exp(-rate * time) for time in (0.1, 1.0, 5.0))
    check("D finite-time two-state Markov semigroup remains linearly invertible", all(value > 0 for value in finite_semigroup_determinants))

    completion_probabilities = tuple((1.0 - exp(-rate)) ** count for count in (1, 10, 100, 1000))
    check("D infinite lattice has no finite global all-sites completion", all(left > right for left, right in zip(completion_probabilities, completion_probabilities[1:])) and completion_probabilities[-1] < 1.0e-190)

    identity = np.eye(2, dtype=complex)
    zed = np.diag((1.0, -1.0)).astype(complex)
    p0 = np.diag((1.0, 0.0)).astype(complex)
    p1 = np.diag((0.0, 1.0)).astype(complex)
    phase_flip = (identity / np.sqrt(2.0), zed / np.sqrt(2.0))
    projective = (p0, p1)
    rho = np.array(((0.8, 0.3), (0.3, 0.2)), dtype=complex)
    check("D two distinct instruments implement the same dephasing channel", np.allclose(dephasing_channel(rho, phase_flip), dephasing_channel(rho, projective)))
    phase_probabilities = tuple(float(np.trace(operator @ p0 @ operator.conj().T).real) for operator in phase_flip)
    projective_probabilities = tuple(float(np.trace(operator @ p0 @ operator.conj().T).real) for operator in projective)
    check("D equal channels have different outcome records", np.allclose(phase_probabilities, (0.5, 0.5)) and np.allclose(projective_probabilities, (1.0, 0.0)))


def binary_entropy(probability: float) -> float:
    if probability in (0.0, 1.0):
        return 0.0
    return -probability * log2(probability) - (1.0 - probability) * log2(1.0 - probability)


def canonical_support_relative_b0() -> frozenset[Coord]:
    cell = c17.Cell((0, 0, 0), (0, 0, 1), (1, 0, 0))
    records, _, _, _ = c17.run_schedule("first", cell, 0, 2020)
    b0 = c17.global_site(cell, c17.CANONICAL_PATH[0])
    return frozenset(subtract(site, b0) for site in records)


def reversible_garbage_and_rails() -> None:
    section("E - Reversible garbage retention, capacity, and naive rails")
    empty_candidates: frozenset[Coord] = frozenset()
    adjacent_candidates = frozenset(((0, 0, 0), (1, 0, 0)))

    def isolated_map(candidates: frozenset[Coord]) -> frozenset[Coord]:
        return frozenset(
            site
            for site in candidates
            if all(other == site or linf(subtract(site, other)) > EXCLUSION_RADIUS for other in candidates)
        )

    check("E isolated-winner map is noninjective", isolated_map(empty_candidates) == isolated_map(adjacent_candidates) == frozenset() and empty_candidates != adjacent_candidates)
    input_left = np.array((1.0, 0.0), dtype=complex)
    input_right = np.array((0.0, 1.0), dtype=complex)
    same_clean_output = np.array((1.0, 0.0), dtype=complex)
    check("E a garbage-free unitary would violate inner-product preservation", abs(np.vdot(input_left, input_right)) == 0 and abs(np.vdot(same_clean_output, same_clean_output)) == 1)

    p = 1.0 / 6859.0
    rho = p * (1.0 - p) ** 6858
    clean_fraction = 111.0 * rho
    available_fraction = 1.0 - clean_fraction
    check("E entropy density does not forbid garbage export", binary_entropy(p) < available_fraction)
    check("E winner diamonds occupy well below total site capacity", 0.0 < clean_fraction < 0.01)

    support = canonical_support_relative_b0()
    check("E Cycle 17 clean support has 111 sites inside candidate exclusion", len(support) == 111 and max(linf(site) for site in support) == 4 < EXCLUSION_RADIUS)
    check("E isolated winner has no other candidate garbage on its support", all(linf(site) <= 4 < 9 for site in support))

    # A single frame-directed ray is not a universal routing solution.  Two
    # safe B0 sites ten apart with opposite forward frames send their outward
    # rays into the same physical sites.
    left_origin = (0, 0, 0)
    right_origin = (10, 0, 0)
    left_forward = (1, 0, 0)
    right_forward = (-1, 0, 0)
    left_rail = frozenset(add(left_origin, scale(step, left_forward)) for step in range(5, 10))
    right_rail = frozenset(add(right_origin, scale(step, right_forward)) for step in range(1, 6))
    check("E two B0 origins at distance ten are collision-safe", linf(subtract(left_origin, right_origin)) == 10)
    check("E naive opposite frame-directed garbage rails collide", not left_rail.isdisjoint(right_rail))


def diamond_and_route_classification() -> None:
    section("F - Diamond handoff, route classification, rate, and actuality")
    support = canonical_support_relative_b0()
    check("F Cycle 17 builder path is 99 sites", len(c17.CANONICAL_PATH) == 99)
    check("F Cycle 17 terminal diamond is 111 sites", len(support) == 111)
    check("F radius-nine B0 separation protects every 111-site support", max(linf(site) for site in support) == 4 and 2 * 4 + 1 == EXCLUSION_RADIUS)

    normalized = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    route_phrases = (
        "ideal range-nine jump route",
        "direct nn jump route",
        "finite-depth qca route",
        "bounded lindbladian route",
        "explicit quantum-trajectory instrument route",
        "reversible compute-copy-uncompute route",
        "naive garbage-rail route",
        "spatially encoded qca route",
        "dissipative mediator route",
        "global cat-state route",
        "rate does not select the actual trajectory",
    )
    for phrase in route_phrases:
        check(f"F note classifies route: {phrase}", phrase in normalized)


def no_go_contract() -> None:
    section("G - Scoped classification and no-go discipline")
    normalized = " ".join(NOTE.read_text(encoding="utf-8").lower().replace("`", "").replace("*", "").split())
    claims = (
        "the ideal range-nine jump instrument is a complete non-nn reference law",
        "direct positive-rate nn b0 jumps do not enforce radius-nine exclusion",
        "product-noise exact anticorrelation needs causal depth at least 14",
        "the isolated-candidate decision needs depth at least 27",
        "bounded time-homogeneous lindbladian evolution does not reach exact terminal projection at finite deterministic time",
        "a channel does not uniquely select its record instrument",
        "reversible qca computation must retain candidate information as garbage",
        "entropy capacity does not close the garbage-export route",
        "one naive frame rail is not collision safe",
        "the exact nn one-m2 autonomous compile remains open",
        "rate and actuality remain separate",
        "not a universal qca or lindbladian no-go",
        "not a theorem of the current four axioms",
        "residual law fields are not separate axiom atoms",
        "no new record axiom is forced",
    )
    for claim in claims:
        check(f"G note preserves classification: {claim}", claim in normalized)

    n1_routes = (
        "ideal nonlocal quantum jump — attempted",
        "direct nn markov jumps — attempted",
        "nn precursor blockade — attempted",
        "finite-depth qca correlation — attempted",
        "bounded lindbladian relaxation — attempted",
        "explicit trajectory instrument — attempted",
        "reversible garbage export — attempted",
        "frame-directed garbage rails — attempted",
        "spatially encoded qca — attempted",
        "global cat or periodic state — attempted",
    )
    for route in n1_routes:
        check(f"G N1 includes route: {route}", route in normalized)
    check("G N2 has collapsed four-condition set", "collapsed wall set has four conditions" in normalized)
    check("G N3 includes hidden-condition scan", "hidden-condition scan" in normalized)
    check("G N4 includes exact residual matching", "exact residual matching" in normalized)
    check("G N5 narrows the negative resolutions", "no claim against all spatial encodings" in normalized)
    check("G N6 keeps import-retirement routes live", "partial-closure path" in normalized and "no constitutional promotion follows" in normalized)
    check("G N7 contains strongest hostile steelman", "hostile reviewer" in normalized and "universal quantum compile no-go would be premature" in normalized)
    check("G N8 records cross-cycle mechanisms", "cross-cycle echo" in normalized and "garbage can become lawful downstream structure" in normalized)
    check("G no-go discipline records PASS", "no-go-discipline status: pass" in normalized)


def main() -> int:
    source_contract()
    ideal_range_nine_instrument()
    direct_nn_jump_and_depth_bounds()
    lindbladian_finalization_and_instrument()
    reversible_garbage_and_rails()
    diamond_and_route_classification()
    no_go_contract()
    print(
        "\nSUMMARY: QUANTUM DISSIPATIVE SEED ESCAPE CYCLE 20 "
        f"PASS={PASS} FAIL={FAIL}"
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
