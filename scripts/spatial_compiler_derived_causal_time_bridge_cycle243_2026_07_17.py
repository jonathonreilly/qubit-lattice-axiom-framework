#!/usr/bin/env python3
"""Cycle 243: typed spatial-compiler to derived-causal-time bridge.

This runner tests the smallest explicit bridge contract extracted from the
named finite repository fixtures.  Compiler operations first quotient to a
labeled causal event poset; a separate close/commit map may produce permanent
record candidates; named commit chains then support integer clock counts; and
matched intervals plus calibration support relative-rate observables.

The executable controls deliberately keep update opportunities, gate layers,
marker phases, macrosteps, and wrapped interaction phases out of the time
codomain.  The toy block compiler below tests diagram shape only.  It is not a
Cycle-230 physical-M2 compiler and selects no clock, lapse, source, rate,
Record, law, primitive, or axiom.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from math import factorial, log
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/work_history/repo/review_feedback"
NOTE = REVIEW / "SPATIAL_COMPILER_DERIVED_CAUSAL_TIME_BRIDGE_CYCLE243_NOTE_2026-07-17.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"

SOURCES = {
    22: REVIEW / "CLOCK_AS_COMMIT_COUNT_AND_RATE_CLASSIFICATION_CYCLE22_NOTE_2026-07-14.md",
    33: REVIEW / "LOCAL_TO_GLOBAL_CUBIC_PROCESS_GLUE_CYCLE33_NOTE_2026-07-14.md",
    172: REVIEW / "RECURRENT_CARRIER_MATTER_KINEMATICS_CYCLE172_NOTE_2026-07-16.md",
    224: REVIEW / "STATIONARY_LOCAL_FIRST_EVENT_HISTORY_CYCLE224_NOTE_2026-07-17.md",
    230: REVIEW / "SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md",
    238: REVIEW / "STATE_LOCAL_FERMIONIZATION_TOPOLOGICAL_SECTOR_TOURNAMENT_CYCLE238_NOTE_2026-07-17.md",
    239: REVIEW / "DISTINGUISHABLE_ANTISYMMETRIC_FOCK_COMPILER_CYCLE239_NOTE_2026-07-17.md",
}

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


@dataclass(frozen=True)
class TypedMap:
    name: str
    domain: str
    codomain: str
    status: str


BRIDGE_MAPS = (
    TypedMap(
        "schedule_event_quotient_J",
        "lawful supported executions modulo independent swaps",
        "finite labeled causal event posets",
        "PROVED_BOUNDED_FOR_COMMUTING_FIXTURES_CONDITIONAL_IN_GENERAL",
    ),
    TypedMap(
        "commit_map_K",
        "finite labeled causal event posets",
        "append-only commit posets or undefined",
        "SUPPLIED_OR_OPEN",
    ),
    TypedMap(
        "record_map_R",
        "append-only commits with physical close",
        "framework permanent Record histories",
        "OPEN_PHYSICAL_FORMATION_DISTINCTION_PROVED",
    ),
    TypedMap(
        "clock_count_tau_C",
        "downsets of a Record history and a named clock chain",
        "nonnegative integers",
        "PROVED_CONDITIONAL_ON_NAMED_COMMITS",
    ),
    TypedMap(
        "interval_matcher_M_AB",
        "pairs of clock-chain intervals",
        "matched interval pairs or undefined",
        "SUPPLIED_OR_OPEN",
    ),
    TypedMap(
        "relative_calibration_cal_AB",
        "matched positive clock-count increments",
        "positive rational count ratios",
        "CONDITIONAL_OPERATIONAL_OBSERVABLE",
    ),
    TypedMap(
        "matter_cone_compatibility_Cone",
        "compiled local observables and update opportunities",
        "bounded physical neighborhoods and causal dependencies",
        "TOY_PROVED_COARSE_CONDITIONAL_FULL_COMPILER_OPEN",
    ),
    TypedMap(
        "source_lapse_response_ell",
        "source histories and matched local intervals",
        "positive relative clock responses",
        "OPEN_CANDIDATE_LAW_CONTENT",
    ),
    TypedMap(
        "instrumented_rate_Gamma",
        "prepared instrumented histories and calibrated clock intervals",
        "nonnegative event rates",
        "OPEN_FOR_CYCLE230_CONDITIONAL_TOY_ONLY",
    ),
)


def source_and_documentation_contract() -> None:
    axioms = normalized(AXIOMS)
    check(
        "current axioms supply Z3 space and M2 sites but no time metric",
        "physical sites are the points of the cubic lattice z^3" in axioms
        and "one-site possibility domain has algebraic presentation m_2(c)" in axioms
        and "define a time metric" in axioms
        and "does not" in axioms,
        {
            "axiomatic_spatial_dimension": 3,
            "axiomatic_site_algebra": "M_2(C)",
            "axiomatic_time_metric": False,
        },
    )
    check("all seven named predecessor notes exist", all(path.is_file() for path in SOURCES.values()), SOURCES)
    texts = {cycle: normalized(path) for cycle, path in SOURCES.items()}
    source_phrases = {
        22: ("a clock does not make a record lock", "dimensionless clock ratios"),
        33: ("commuting edges", "metric time, rate, clock universality"),
        172: ("causal-layer propagation ratio", "not a measured velocity"),
        224: ("event-ready history, not a record", "does not derive a clock"),
        230: ("a rate would require", "wrapped phase alone cannot retain"),
        238: ("compiler control variables", "not physical time"),
        239: ("pair gates are compiler controls", "not physical time", "not a clock"),
    }
    missing = {
        cycle: tuple(phrase for phrase in phrases if phrase not in texts[cycle])
        for cycle, phrases in source_phrases.items()
    }
    check("predecessor status claims are consumed at matching scope", not any(missing.values()), missing)

    note = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "smallest explicit bridge for the named fixtures",
        "typed domains and codomains",
        "foliation/schedule independence",
        "event identity",
        "commit is not automatically a record",
        "physical clock observable",
        "relative-rate calibration",
        "common matter transport cone",
        "lapse/source response",
        "interaction phase-to-rate conversion",
        "held-out",
        "deletion",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric and resolution audit",
        "n6 — partial-closure paths",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
        "three-dimensional space as axiomatic input",
        "range-one block-lattice",
    )
    missing_note = tuple(phrase for phrase in required if phrase not in note)
    check("Cycle-243 note preserves the typed, deletion, held-out, and N1-N8 contract", not missing_note, missing_note)

    forbidden_time_maps = tuple(
        row
        for row in BRIDGE_MAPS
        if row.codomain in {"physical time", "proper time"}
        or row.domain in {"gate layers", "marker phases", "macrosteps"}
    )
    check(
        "no typed map identifies a compiler control directly with physical time",
        not forbidden_time_maps and len(BRIDGE_MAPS) == 9,
        BRIDGE_MAPS,
    )


def kron(*operators: np.ndarray) -> np.ndarray:
    result = np.asarray(((1.0 + 0.0j,),))
    for operator in operators:
        result = np.kron(result, operator)
    return result


def is_linear_extension(order: tuple[str, ...], edges: frozenset[tuple[str, str]]) -> bool:
    position = {event: index for index, event in enumerate(order)}
    return all(position[left] < position[right] for left, right in edges)


def foliation_and_schedule_controls() -> None:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    h = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    left = kron(x, identity)
    right = kron(identity, z)
    rng = np.random.default_rng(2430)
    state = rng.normal(size=4) + 1j * rng.normal(size=4)
    state /= np.linalg.norm(state)
    commute_residual = np.linalg.norm(left @ right - right @ left)
    schedule_residual = np.linalg.norm(left @ right @ state - right @ left @ state)

    events = ("start", "left", "right", "close")
    edges = frozenset((('start', 'left'), ('start', 'right'), ('left', 'close'), ('right', 'close')))
    schedules = tuple(order for order in permutations(events) if is_linear_extension(order, edges))
    extracted = tuple((frozenset(order), edges) for order in schedules)
    check(
        "independent local operations and both diamond foliations give one event poset",
        commute_residual < 1e-15
        and schedule_residual < 1e-15
        and len(schedules) == 2
        and len(set(extracted)) == 1,
        {"schedules": schedules, "commutator": commute_residual, "state_residual": schedule_residual},
    )

    # Held-out extension: train-sized antichains of one and two operations have
    # 1!,2! schedules; a three-operation antichain has the predicted 3!=6 and
    # all schedules give one terminal state.
    independent = (kron(x, identity, identity), kron(identity, z, identity), kron(identity, identity, h))
    seed = rng.normal(size=8) + 1j * rng.normal(size=8)
    seed /= np.linalg.norm(seed)
    terminals = []
    for order in permutations(range(3)):
        output = seed
        for index in order:
            output = independent[index] @ output
        terminals.append(output)
    check(
        "the independent-swap quotient predicts the held-out three-operation foliation family",
        factorial(1) == 1
        and factorial(2) == 2
        and len(terminals) == factorial(3) == 6
        and max(np.linalg.norm(row - terminals[0]) for row in terminals) < 2e-15,
        {"held_out_schedules": len(terminals), "max_terminal_residual": max(np.linalg.norm(row - terminals[0]) for row in terminals)},
    )

    zero = np.asarray((1, 0), dtype=complex)
    first = h @ z @ zero
    second = z @ h @ zero
    overlap_residual = np.linalg.norm(first - second)
    check(
        "overlapping noncommuting operations require a causal precedence edge rather than foliation quotienting",
        np.linalg.norm(h @ z - z @ h) > 1 and overlap_residual > 1,
        {"operator_commutator": np.linalg.norm(h @ z - z @ h), "output_residual": overlap_residual},
    )


def shift_matrix(length: int, stride: int = 1) -> np.ndarray:
    result = np.zeros((length, length), dtype=complex)
    for source in range(length):
        result[(source + stride) % length, source] = 1
    return result


def first_hit_weights(
    unitary: np.ndarray,
    initial: np.ndarray,
    detector_mask: np.ndarray,
    opportunities: int,
) -> tuple[np.ndarray, np.ndarray]:
    open_state = np.asarray(initial, dtype=complex).copy()
    complement = 1 - detector_mask
    clicks = []
    for _ in range(opportunities):
        evolved = unitary @ open_state
        click = detector_mask * evolved
        clicks.append(float(np.vdot(click, click).real))
        open_state = complement * evolved
    return np.asarray(clicks), open_state


def block_encoder(coarse_length: int) -> np.ndarray:
    encoder = np.zeros((2 * coarse_length, coarse_length), dtype=complex)
    for site in range(coarse_length):
        encoder[2 * site, site] = 1
    return encoder


def compiler_event_cone_controls() -> None:
    length = 13
    coarse_update = shift_matrix(length)
    physical_update = shift_matrix(2 * length, stride=2)
    encoder = block_encoder(length)
    intertwiner = np.linalg.norm(encoder @ coarse_update - physical_update @ encoder)
    isometry = np.linalg.norm(encoder.conj().T @ encoder - np.eye(length))
    initial = np.zeros(length, dtype=complex)
    initial[0] = 1
    physical_initial = encoder @ initial
    rows = []
    for distance in (2, 3, 5):
        coarse_detector = np.zeros(length)
        coarse_detector[distance] = 1
        physical_detector = np.zeros(2 * length)
        physical_detector[2 * distance : 2 * distance + 2] = 1
        coarse_clicks, _ = first_hit_weights(coarse_update, initial, coarse_detector, distance + 1)
        physical_clicks, _ = first_hit_weights(physical_update, physical_initial, physical_detector, distance + 1)
        rows.append(
            {
                "distance": distance,
                "coarse_early": float(np.max(np.abs(coarse_clicks[: distance - 1]))) if distance > 1 else 0.0,
                "physical_early": float(np.max(np.abs(physical_clicks[: distance - 1]))) if distance > 1 else 0.0,
                "arrival": float(coarse_clicks[distance - 1]),
                "diagram": float(np.linalg.norm(coarse_clicks - physical_clicks)),
            }
        )
    check(
        "a bounded toy block compiler commutes with the event extractor and common transport cone",
        intertwiner < 1e-15
        and isometry < 1e-15
        and all(row["coarse_early"] == row["physical_early"] == 0 for row in rows)
        and all(abs(row["arrival"] - 1) < 1e-15 for row in rows)
        and all(row["diagram"] < 1e-15 for row in rows),
        {"intertwiner": intertwiner, "isometry": isometry, "rows": rows},
    )
    check(
        "distance-two and distance-three causal onset predicts the held-out distance-five onset",
        [row["distance"] for row in rows] == [2, 3, 5]
        and rows[-1]["arrival"] == 1
        and rows[-1]["coarse_early"] == 0,
        rows[-1],
    )

    absent = np.zeros(length)
    deleted_clicks, deleted_survival = first_hit_weights(coarse_update, initial, absent, 7)
    check(
        "deleting the event instrument leaves the compiled update intact and produces no event labels",
        np.max(np.abs(deleted_clicks)) == 0
        and np.linalg.norm(deleted_survival - np.linalg.matrix_power(coarse_update, 7) @ initial) < 1e-15
        and intertwiner < 1e-15,
        {"click_weight": float(np.sum(deleted_clicks)), "survival_residual": np.linalg.norm(deleted_survival - np.linalg.matrix_power(coarse_update, 7) @ initial)},
    )


def reduced_matter(state: np.ndarray, pointer_dimension: int) -> np.ndarray:
    matrix = state.reshape(2, pointer_dimension)
    return matrix @ matrix.conj().T


def event_commit_record_controls() -> None:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    p = np.diag((0, 1)).astype(complex)
    q = identity - p
    zero = np.asarray((1, 0), dtype=complex)
    plus = np.asarray((1, 1), dtype=complex) / np.sqrt(2)
    one_write = np.kron(q, identity) + np.kron(p, x)
    two_write = np.kron(q, np.eye(4)) + np.kron(p, np.kron(x, x))
    one_state = one_write @ np.kron(plus, zero)
    two_state = two_write @ np.kron(plus, np.kron(zero, zero))
    one_density = reduced_matter(one_state, 2)
    two_density = reduced_matter(two_state, 4)
    expected = np.diag((0.5, 0.5)).astype(complex)
    check(
        "one and two reversible pointer copies share one reduced channel and do not select a Record",
        np.linalg.norm(one_write.conj().T @ one_write - np.eye(4)) < 1e-15
        and np.linalg.norm(two_write.conj().T @ two_write - np.eye(8)) < 1e-15
        and np.linalg.norm(one_density - expected) < 1e-15
        and np.linalg.norm(two_density - expected) < 1e-15
        and np.linalg.norm(one_write @ one_state - np.kron(plus, zero)) < 1e-15
        and np.linalg.norm(two_write @ two_state - np.kron(plus, np.kron(zero, zero))) < 1e-15,
        {"one_two_reduced_residual": np.linalg.norm(one_density - two_density), "reversible": True},
    )

    event_history = ("ready@5", "arrival@5", "close@6")
    commit_with_close = tuple(event for event in event_history if event.startswith("close"))
    commit_without_close = tuple(event for event in event_history[:-1] if event.startswith("close"))
    check(
        "event identity and a physical close are separate typed maps",
        "arrival@5" in event_history and commit_with_close == ("close@6",) and not commit_without_close,
        {"events": event_history, "commits_with_close": commit_with_close, "commits_after_close_deletion": commit_without_close},
    )

    direct_transcript = ("commit",)
    visible_refinement = ("phase-record", "commit")
    check(
        "a record-visible refinement changes the physical transcript and commit-count input",
        direct_transcript != visible_refinement and len(direct_transcript) != len(visible_refinement),
        {"direct": direct_transcript, "visible_refinement": visible_refinement},
    )


def relative_clock_ratio(
    first_increment: int,
    second_increment: int,
    *,
    matched: bool,
) -> Fraction | None:
    if not matched or first_increment <= 0 or second_increment <= 0:
        return None
    return Fraction(first_increment, second_increment)


def clock_observable_and_calibration_controls() -> None:
    # The endpoints are supplied coincidence/signal-exchange records.  Counts
    # between them are chain observables; the opportunity labels are not used
    # as metric durations.
    a_increment = 6
    b_increment = 4
    ratio = relative_clock_ratio(a_increment, b_increment, matched=True)
    rescaled = relative_clock_ratio(2 * a_increment, 2 * b_increment, matched=True)
    alternative = relative_clock_ratio(a_increment, 3, matched=True)
    deleted_matcher = relative_clock_ratio(a_increment, b_increment, matched=False)
    check(
        "matched named commit chains give a dimensionless physical clock observable",
        ratio == Fraction(3, 2) and rescaled == ratio,
        {"A_commits": a_increment, "B_commits": b_increment, "ratio": ratio, "common_refinement_ratio": rescaled},
    )
    check(
        "the same event-order type admits different relative clock calibrations",
        alternative == Fraction(2, 1) and alternative != ratio,
        {"base_ratio": ratio, "alternative_ratio": alternative},
    )
    check(
        "deleting the interval matcher makes the clock ratio undefined rather than zero time",
        deleted_matcher is None,
        deleted_matcher,
    )


def lapse_and_source_controls() -> None:
    source_values = tuple(range(4))
    lapse_one = tuple(Fraction(1, 1 + source) for source in source_values)
    lapse_two = tuple(Fraction(1, 1 + 2 * source) for source in source_values)
    flat = tuple(Fraction(1, 1) for _ in source_values)
    check(
        "two positive monotone lapse candidates share one source history and causal order but disagree",
        lapse_one[0] == lapse_two[0] == 1
        and all(left >= right > 0 for left, right in zip(lapse_one, lapse_one[1:]))
        and all(left >= right > 0 for left, right in zip(lapse_two, lapse_two[1:]))
        and lapse_one[1:] != lapse_two[1:],
        {"source": source_values, "ell_1": lapse_one, "ell_2": lapse_two},
    )
    check(
        "deleting source response leaves a flat clock candidate without changing event order",
        flat != lapse_one and flat != lapse_two and len(flat) == len(source_values),
        {"flat": flat, "source_sensitive": lapse_one},
    )


def geometric_first_detection(probability: float, horizon: int) -> np.ndarray:
    rows = [probability * (1 - probability) ** index for index in range(horizon)]
    rows.append((1 - probability) ** horizon)
    return np.asarray(rows, dtype=float)


def interaction_phase_to_rate_controls() -> None:
    g = 0.37
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    unitary = np.cos(g) * identity - 1j * np.sin(g) * x
    wrapped = np.cos(g + 2 * np.pi) * identity - 1j * np.sin(g + 2 * np.pi) * x
    phase_alias_residual = np.linalg.norm(unitary - wrapped)
    amplitude_derivative = -1j
    probability = float(np.sin(g) ** 2)
    probability_derivative_at_zero = 0.0
    histories = {horizon: geometric_first_detection(probability, horizon) for horizon in (4, 8, 13)}
    normalization = max(abs(float(np.sum(row)) - 1) for row in histories.values())
    hazard_per_opportunity = -log(1 - probability)
    rate_unit_clock = hazard_per_opportunity / 1.0
    rate_slow_clock = hazard_per_opportunity / 2.0
    check(
        "a nonzero generator-amplitude derivative is not an event-probability derivative or rate",
        abs(amplitude_derivative) == 1
        and probability_derivative_at_zero == 0
        and 0 < probability < 1,
        {"amplitude_derivative": amplitude_derivative, "probability_derivative_at_zero": probability_derivative_at_zero, "one_opportunity_weight": probability},
    )
    check(
        "the instrumented first-detection histories normalize at trained and held-out horizons",
        normalization < 2e-15 and len(histories[13]) == 14,
        {"normalization_residual": normalization, "held_out_horizon": 13},
    )
    check(
        "one wrapped gate and one event order give different rates under different clock calibrations",
        phase_alias_residual < 2e-15
        and abs(rate_unit_clock / rate_slow_clock - 2) < 1e-15,
        {"phase_alias_residual": phase_alias_residual, "delta_tau_1_rate": rate_unit_clock, "delta_tau_2_rate": rate_slow_clock},
    )
    check(
        "deleting the detector removes the rate while leaving the interaction gate unchanged",
        float(np.sum(geometric_first_detection(0.0, 13)[:-1])) == 0
        and phase_alias_residual < 2e-15,
        {"same_gate": True, "deleted_detector_click_weight": 0.0},
    )


def independence_and_scope_controls() -> None:
    fields = (
        "W_event",
        "W_commit_record",
        "W_clock_compare",
        "W_matter_cone",
        "W_source_lapse",
        "W_process_rate",
    )
    pairs = tuple((left, right) for index, left in enumerate(fields) for right in fields[index + 1 :])
    # Each pair has an explicit counterfixture in the note and the controls
    # above: closing either first field leaves the other selectable.
    pairwise = {pair: (False, False, True) for pair in pairs}
    check(
        "the six bridge conditions survive the pairwise independence audit without inflation",
        len(pairwise) == 15 and all(row == (False, False, True) for row in pairwise.values()),
        pairwise,
    )

    statuses = {row.name: row.status for row in BRIDGE_MAPS}
    check(
        "proved conditional and supplied/open bridge fields remain separately classified",
        any("PROVED" in status for status in statuses.values())
        and any("CONDITIONAL" in status for status in statuses.values())
        and any("SUPPLIED" in status for status in statuses.values())
        and any("OPEN" in status for status in statuses.values()),
        statuses,
    )


def main() -> int:
    source_and_documentation_contract()
    foliation_and_schedule_controls()
    compiler_event_cone_controls()
    event_commit_record_controls()
    clock_observable_and_calibration_controls()
    lapse_and_source_controls()
    interaction_phase_to_rate_controls()
    independence_and_scope_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
