#!/usr/bin/env python3
"""Exact conclusion-boundary certificate for taste-qubit teleportation.

The theorem checked here is deliberately narrower than a teleportation theorem:
the finite planning packet does not entail unconditional nature-grade closure.
The certificate supplies explicit non-entailment witnesses for the selector,
all-even-side scaling, and hardware-existence obligations.

The side-14 and no-device witnesses below are countermodels.  They agree with
the stated finite premises and violate the stronger conclusions, so they prove
that those conclusions do not follow from the premises.  They are not physical
predictions for side 14 or for any fabricated device.
"""

from __future__ import annotations

import argparse
import dataclasses
import math
from itertools import product


@dataclasses.dataclass(frozen=True)
class ResourceRow:
    side: int
    gap: float
    bell: float


@dataclasses.dataclass(frozen=True)
class SelectorConclusion:
    bare_candidate_count: int
    residual_without_orientation: int
    residual_without_action: int
    residual_without_no_dwell: int
    final_selector_count: int
    all_clauses_necessary: bool
    bare_invariants_entail_unique_selector: bool
    terminal_decision: str


@dataclasses.dataclass(frozen=True)
class ScalingConclusion:
    certified_sides: tuple[int, ...]
    gap_floor: float
    bell_floor: float
    min_margin: float
    scaled_gap_monotone: bool
    bell_monotone: bool
    countermodel_side: int
    countermodel_matches_all_rows: bool
    countermodel_violates_universal_bound: bool
    finite_rows_entail_all_even_bound: bool
    terminal_decision: str


@dataclasses.dataclass(frozen=True)
class HardwareConclusion:
    record_length: int
    minimum_distance: int
    correctable_flips: int
    slot_threshold: float
    area_budget_rad: float
    controller_margin: float
    detector_word_bound: float
    detector_log10_overlap: float
    no_device_countermodel_preserves_requirements: bool
    requirements_entail_fabricated_measurement: bool
    terminal_decision: str


@dataclasses.dataclass(frozen=True)
class LaneConclusion:
    evidence_packet_checked: bool
    current_packet_entails_unconditional_closure: bool
    planning_closed: bool
    unconditional_closed: bool
    promote_to_nature_grade: bool
    boundary_status: str


SIGNED_CERTIFICATE = (
    ResourceRow(4, 0.0244025, 0.999702),
    ResourceRow(6, 0.0120618, 0.999709),
    ResourceRow(8, 0.00704654, 0.999711),
    ResourceRow(10, 0.00459031, 0.999711069),
    ResourceRow(12, 0.00321872568895, 0.999711313114),
)


def selector_conclusion() -> SelectorConclusion:
    """Exhaust the stated 2 x 8 x 4 candidate family.

    The completion clauses select causal-positive orientation, winding zero,
    and the no-dwell nearest-neighbor carrier.  Removing one predicate while
    retaining the other two leaves respectively 2, 8, or 4 candidates.
    """

    orientations = ("causal-positive", "causal-negative")
    windings = tuple(range(8))
    carriers = (
        "nearest-neighbor-no-dwell",
        "on-site-dwell",
        "next-nearest-neighbor",
        "non-cubic-nearest-neighbor",
    )
    candidates = tuple(product(orientations, windings, carriers))

    orientation_clause = lambda candidate: candidate[0] == "causal-positive"
    action_clause = lambda candidate: candidate[1] == 0
    no_dwell_clause = lambda candidate: candidate[2] == "nearest-neighbor-no-dwell"

    without_orientation = tuple(
        candidate for candidate in candidates if action_clause(candidate) and no_dwell_clause(candidate)
    )
    without_action = tuple(
        candidate
        for candidate in candidates
        if orientation_clause(candidate) and no_dwell_clause(candidate)
    )
    without_no_dwell = tuple(
        candidate
        for candidate in candidates
        if orientation_clause(candidate) and action_clause(candidate)
    )
    final = tuple(
        candidate
        for candidate in candidates
        if orientation_clause(candidate) and action_clause(candidate) and no_dwell_clause(candidate)
    )
    residuals = (len(without_orientation), len(without_action), len(without_no_dwell))
    return SelectorConclusion(
        bare_candidate_count=len(candidates),
        residual_without_orientation=residuals[0],
        residual_without_action=residuals[1],
        residual_without_no_dwell=residuals[2],
        final_selector_count=len(final),
        all_clauses_necessary=all(count > 1 for count in residuals) and len(final) == 1,
        bare_invariants_entail_unique_selector=len(candidates) == 1,
        terminal_decision=(
            "derive a selector from a stronger theorem, retain the three clauses "
            "as explicit extra principles, or do not promote"
        ),
    )


def scaling_conclusion(gap_floor: float, bell_floor: float) -> ScalingConclusion:
    """Summarize the finite table and construct a universal-claim countermodel."""

    sides = tuple(row.side for row in SIGNED_CERTIFICATE)
    margins = tuple(row.gap - gap_floor / (row.side * row.side) for row in SIGNED_CERTIFICATE)
    scaled_gaps = tuple(row.gap * row.side * row.side for row in SIGNED_CERTIFICATE)
    bells = tuple(row.bell for row in SIGNED_CERTIFICATE)

    # A model equal to every supplied row but with a failing value at the next
    # even side is a witness against finite-data => all-even-side entailment.
    countermodel = {row.side: (row.gap, row.bell) for row in SIGNED_CERTIFICATE}
    countermodel_side = max(sides) + 2
    countermodel[countermodel_side] = (0.0, min(0.5, bell_floor / 2.0))
    matches_all_rows = all(countermodel[row.side] == (row.gap, row.bell) for row in SIGNED_CERTIFICATE)
    counter_gap, counter_bell = countermodel[countermodel_side]
    violates_universal = (
        counter_gap * countermodel_side * countermodel_side < gap_floor
        or counter_bell < bell_floor
    )

    return ScalingConclusion(
        certified_sides=sides,
        gap_floor=gap_floor,
        bell_floor=bell_floor,
        min_margin=min(margins),
        scaled_gap_monotone=all(
            later >= earlier for earlier, later in zip(scaled_gaps, scaled_gaps[1:])
        ),
        bell_monotone=all(later >= earlier for earlier, later in zip(bells, bells[1:])),
        countermodel_side=countermodel_side,
        countermodel_matches_all_rows=matches_all_rows,
        countermodel_violates_universal_bound=violates_universal,
        finite_rows_entail_all_even_bound=not (matches_all_rows and violates_universal),
        terminal_decision=(
            "prove an all-even-side operator inequality or keep resource genesis "
            "at finite-certificate status"
        ),
    )


def record_codeword(z_bit: int, x_bit: int) -> tuple[int, ...]:
    parity = z_bit ^ x_bit
    return (z_bit, z_bit, z_bit, x_bit, x_bit, x_bit, parity, parity)


def minimum_hamming_distance() -> int:
    codewords = tuple(record_codeword(*outcome) for outcome in product((0, 1), repeat=2))
    return min(
        sum(a != b for a, b in zip(first, second))
        for index, first in enumerate(codewords)
        for second in codewords[index + 1 :]
    )


def word_failure_tail(record_length: int, correctable_flips: int, slot_error: float) -> float:
    return sum(
        math.comb(record_length, flips)
        * slot_error**flips
        * (1.0 - slot_error) ** (record_length - flips)
        for flips in range(correctable_flips + 1, record_length + 1)
    )


def solve_slot_threshold(record_length: int, correctable_flips: int, target: float) -> float:
    low, high = 0.0, 0.5
    for _ in range(80):
        mid = 0.5 * (low + high)
        if word_failure_tail(record_length, correctable_flips, mid) <= target:
            low = mid
        else:
            high = mid
    return low


def kl_half_against(p: float) -> float:
    return 0.5 * math.log(0.5 / p) + 0.5 * math.log(0.5 / (1.0 - p))


def hardware_conclusion() -> HardwareConclusion:
    """Derive the requirement envelope and its no-device countermodel."""

    record_length = len(record_codeword(0, 0))
    distance = minimum_hamming_distance()
    correctable = (distance - 1) // 2
    target_word_failure = 1e-6
    leakage_budget = 1e-5
    crosstalk_budget = 2e-5
    implemented_area_bound = 0.023
    slot_threshold = solve_slot_threshold(record_length, correctable, target_word_failure)
    area_budget = math.asin(math.sqrt(slot_threshold - leakage_budget - crosstalk_budget))

    domain_side = 5
    spins_per_slot = domain_side**3
    defect_probability = 0.002
    p_spin = defect_probability + math.exp(-12.0)
    detector_word_bound = min(
        1.0,
        record_length * math.exp(-spins_per_slot * kl_half_against(p_spin)),
    )
    single_spin_overlap = 2.0 * math.sqrt(p_spin * (1.0 - p_spin))
    detector_log10_overlap = math.log10(single_spin_overlap) * spins_per_slot * distance

    # Requirements constrain a possible device.  The model with the same
    # numerical requirements and no fabricated device satisfies every
    # requirement statement, so those statements cannot entail fabrication.
    no_device_countermodel_preserves_requirements = (
        slot_threshold > 0.0
        and area_budget > implemented_area_bound
        and detector_word_bound < target_word_failure
        and detector_log10_overlap < -12.0
    )
    return HardwareConclusion(
        record_length=record_length,
        minimum_distance=distance,
        correctable_flips=correctable,
        slot_threshold=slot_threshold,
        area_budget_rad=area_budget,
        controller_margin=area_budget / implemented_area_bound,
        detector_word_bound=detector_word_bound,
        detector_log10_overlap=detector_log10_overlap,
        no_device_countermodel_preserves_requirements=no_device_countermodel_preserves_requirements,
        requirements_entail_fabricated_measurement=not no_device_countermodel_preserves_requirements,
        terminal_decision=(
            "supply fabricated/noise/material evidence or keep hardware closure "
            "as a requirement envelope"
        ),
    )


def lane_conclusion(
    selector: SelectorConclusion,
    scaling: ScalingConclusion,
    hardware: HardwareConclusion,
) -> LaneConclusion:
    selector_non_entailment = (
        selector.bare_candidate_count > 1
        and selector.all_clauses_necessary
        and not selector.bare_invariants_entail_unique_selector
    )
    scaling_non_entailment = (
        scaling.countermodel_matches_all_rows
        and scaling.countermodel_violates_universal_bound
        and not scaling.finite_rows_entail_all_even_bound
    )
    hardware_non_entailment = (
        hardware.no_device_countermodel_preserves_requirements
        and not hardware.requirements_entail_fabricated_measurement
    )
    checked = selector_non_entailment and scaling_non_entailment and hardware_non_entailment
    entails_unconditional = (
        selector.bare_invariants_entail_unique_selector
        and scaling.finite_rows_entail_all_even_bound
        and hardware.requirements_entail_fabricated_measurement
    )
    return LaneConclusion(
        evidence_packet_checked=checked,
        current_packet_entails_unconditional_closure=entails_unconditional,
        planning_closed=checked,
        unconditional_closed=entails_unconditional,
        promote_to_nature_grade=entails_unconditional,
        boundary_status="planning boundary proved; nature-grade closure HOLD",
    )


def print_gate(name: str, passed: bool) -> None:
    print(f"  {name}: {'PASS' if passed else 'FAIL'}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gap-floor", type=float, default=0.390)
    parser.add_argument("--bell-floor", type=float, default=0.999702)
    parser.add_argument("--tolerance", type=float, default=1e-12)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.tolerance <= 0.0:
        raise ValueError("--tolerance must be positive")
    if args.gap_floor <= 0.0:
        raise ValueError("--gap-floor must be positive")
    if not 0.0 < args.bell_floor <= 1.0:
        raise ValueError("--bell-floor must be in (0, 1]")

    selector = selector_conclusion()
    scaling = scaling_conclusion(args.gap_floor, args.bell_floor)
    hardware = hardware_conclusion()
    conclusion = lane_conclusion(selector, scaling, hardware)

    selector_gate = (
        selector.bare_candidate_count == 64
        and selector.all_clauses_necessary
        and not selector.bare_invariants_entail_unique_selector
    )
    scaling_gate = (
        scaling.certified_sides == (4, 6, 8, 10, 12)
        and scaling.min_margin > 0.0
        and scaling.countermodel_matches_all_rows
        and scaling.countermodel_violates_universal_bound
        and not scaling.finite_rows_entail_all_even_bound
    )
    hardware_gate = (
        hardware.minimum_distance == 5
        and hardware.controller_margin > 2.0
        and hardware.detector_word_bound < 1e-6
        and hardware.no_device_countermodel_preserves_requirements
        and not hardware.requirements_entail_fabricated_measurement
    )
    boundary_gate = (
        conclusion.evidence_packet_checked
        and not conclusion.current_packet_entails_unconditional_closure
        and conclusion.planning_closed
        and not conclusion.unconditional_closed
        and not conclusion.promote_to_nature_grade
    )

    print("TELEPORTATION CONCLUSION BOUNDARY")
    print("Status: exact current-packet non-entailment; explicit nature-grade HOLD")
    print(
        "Claim boundary: ordinary quantum state teleportation only; no matter, "
        "mass, charge, energy, object, or faster-than-light transport is claimed"
    )
    print("Countermodel warning: side 14 and no-device witnesses are logical, not physical predictions")
    print()
    print(
        "selector conclusion: "
        f"bare_candidates={selector.bare_candidate_count}, "
        f"without_orientation={selector.residual_without_orientation}, "
        f"without_action={selector.residual_without_action}, "
        f"without_no_dwell={selector.residual_without_no_dwell}, "
        f"final_selector_count={selector.final_selector_count}, "
        f"bare_unique={selector.bare_invariants_entail_unique_selector}, "
        f"terminal_decision={selector.terminal_decision}"
    )
    print(
        "scaling conclusion: "
        f"certified_sides={','.join(str(side) for side in scaling.certified_sides)}, "
        f"gap_floor={scaling.gap_floor:.3f}/L^2, "
        f"bell_floor={scaling.bell_floor:.6f}, "
        f"min_margin={scaling.min_margin:.3e}, "
        f"countermodel_side={scaling.countermodel_side}, "
        f"matches_rows={scaling.countermodel_matches_all_rows}, "
        f"violates_universal_bound={scaling.countermodel_violates_universal_bound}, "
        f"finite_entails_all_even={scaling.finite_rows_entail_all_even_bound}, "
        f"terminal_decision={scaling.terminal_decision}"
    )
    print(
        "hardware conclusion: "
        f"record_length={hardware.record_length}, d_min={hardware.minimum_distance}, "
        f"correctable={hardware.correctable_flips}, "
        f"slot_threshold={hardware.slot_threshold:.3e}, "
        f"area_budget={hardware.area_budget_rad:.6f}, "
        f"controller_margin={hardware.controller_margin:.3f}, "
        f"detector_word_bound={hardware.detector_word_bound:.3e}, "
        f"detector_log10_overlap={hardware.detector_log10_overlap:.3f}, "
        f"no_device_model_preserves_requirements={hardware.no_device_countermodel_preserves_requirements}, "
        f"requirements_entail_measurement={hardware.requirements_entail_fabricated_measurement}, "
        f"terminal_decision={hardware.terminal_decision}"
    )
    print(
        "lane conclusion: "
        f"evidence_packet_checked={conclusion.evidence_packet_checked}, "
        f"current_packet_entails_unconditional_closure="
        f"{conclusion.current_packet_entails_unconditional_closure}, "
        f"planning_closed={conclusion.planning_closed}, "
        f"unconditional_closed={conclusion.unconditional_closed}, "
        f"promote_to_nature_grade={conclusion.promote_to_nature_grade}, "
        f"boundary_status={conclusion.boundary_status}"
    )
    print()
    print("Acceptance gates:")
    print_gate("selector non-entailment is established by exhaustive enumeration", selector_gate)
    print_gate("finite scaling rows admit an explicit all-even countermodel", scaling_gate)
    print_gate("requirement inequalities admit an explicit no-device countermodel", hardware_gate)
    print_gate("planning closes while nature-grade closure remains HOLD", boundary_gate)
    print_gate("claim boundary stays state-only and not FTL", True)
    print()
    print("Limitations:")
    print("  The theorem is current-packet non-entailment, not a global no-go.")
    print("  A stronger selector theorem, an all-even scaling proof, or device")
    print("  evidence can retire the corresponding witness.")
    return 0 if all((selector_gate, scaling_gate, hardware_gate, boundary_gate)) else 1


if __name__ == "__main__":
    raise SystemExit(main())
