#!/usr/bin/env python3
"""Finite-premise support calculator for the teleportation planning boundary.

This runner checks exact combinatorics and arithmetic conditional on the
planning literals documented in TELEPORTATION_CONCLUSION_BOUNDARY_NOTE.md.
It does not derive a physical selector, continue five signed-resource rows to
all even sides, or infer a fabricated device from requirement inequalities.
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
class SelectorCalculation:
    bare_candidate_count: int
    residual_without_orientation: int
    residual_without_action: int
    residual_without_no_dwell: int
    final_selector_count: int
    clauses_are_minimal_on_defined_family: bool


@dataclasses.dataclass(frozen=True)
class ScalingCalculation:
    certified_sides: tuple[int, ...]
    gap_floor: float
    bell_floor: float
    min_margin: float
    scaled_gap_monotone_on_supplied_rows: bool
    bell_monotone_on_supplied_rows: bool


@dataclasses.dataclass(frozen=True)
class ControllerCalculation:
    record_length: int
    minimum_distance: int
    correctable_flips: int
    slot_threshold: float
    area_budget_rad: float
    controller_margin: float
    threshold_residual: float


@dataclasses.dataclass(frozen=True)
class DetectorCalculation:
    domain_side: int
    defect_probability: float
    detector_word_bound: float
    detector_log10_overlap: float


# Explicit planning inputs. Their source and classification are recorded in the
# paired note; none is treated here as framework-derived or measured evidence.
SIGNED_RESOURCE_ROWS = (
    ResourceRow(4, 0.0244025, 0.999702),
    ResourceRow(6, 0.0120618, 0.999709),
    ResourceRow(8, 0.00704654, 0.999711),
    ResourceRow(10, 0.00459031, 0.999711069),
    ResourceRow(12, 0.00321872568895, 0.999711313114),
)
TARGET_WORD_FAILURE = 1e-6
LEAKAGE_BUDGET = 1e-5
CROSSTALK_BUDGET = 2e-5
IMPLEMENTED_AREA_COMPARATOR_RAD = 0.023
DOMAIN_SIDE = 5
DEFECT_PROBABILITY = 0.002
THERMAL_DEFECT_FACTOR = math.exp(-12.0)


def selector_calculation() -> SelectorCalculation:
    """Enumerate the supplied 2 x 8 x 4 label family and its three filters."""

    orientations = ("causal-positive", "causal-negative")
    windings = tuple(range(8))
    carriers = (
        "nearest-neighbor-no-dwell",
        "on-site-dwell",
        "next-nearest-neighbor",
        "non-cubic-nearest-neighbor",
    )
    candidates = tuple(product(orientations, windings, carriers))

    def orientation_clause(candidate: tuple[str, int, str]) -> bool:
        return candidate[0] == "causal-positive"

    def action_clause(candidate: tuple[str, int, str]) -> bool:
        return candidate[1] == 0

    def no_dwell_clause(candidate: tuple[str, int, str]) -> bool:
        return candidate[2] == "nearest-neighbor-no-dwell"

    without_orientation = tuple(
        candidate
        for candidate in candidates
        if action_clause(candidate) and no_dwell_clause(candidate)
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
        if orientation_clause(candidate)
        and action_clause(candidate)
        and no_dwell_clause(candidate)
    )
    residuals = (
        len(without_orientation),
        len(without_action),
        len(without_no_dwell),
    )
    return SelectorCalculation(
        bare_candidate_count=len(candidates),
        residual_without_orientation=residuals[0],
        residual_without_action=residuals[1],
        residual_without_no_dwell=residuals[2],
        final_selector_count=len(final),
        clauses_are_minimal_on_defined_family=(
            all(count > 1 for count in residuals) and len(final) == 1
        ),
    )


def scaling_calculation(gap_floor: float, bell_floor: float) -> ScalingCalculation:
    """Recompute summaries only on the five supplied signed-resource rows."""

    sides = tuple(row.side for row in SIGNED_RESOURCE_ROWS)
    margins = tuple(
        row.gap - gap_floor / (row.side * row.side)
        for row in SIGNED_RESOURCE_ROWS
    )
    scaled_gaps = tuple(
        row.gap * row.side * row.side for row in SIGNED_RESOURCE_ROWS
    )
    bells = tuple(row.bell for row in SIGNED_RESOURCE_ROWS)
    return ScalingCalculation(
        certified_sides=sides,
        gap_floor=gap_floor,
        bell_floor=bell_floor,
        min_margin=min(margins),
        scaled_gap_monotone_on_supplied_rows=all(
            later >= earlier
            for earlier, later in zip(scaled_gaps, scaled_gaps[1:])
        ),
        bell_monotone_on_supplied_rows=all(
            later >= earlier for earlier, later in zip(bells, bells[1:])
        ),
    )


def record_codeword(z_bit: int, x_bit: int) -> tuple[int, ...]:
    parity = z_bit ^ x_bit
    return (z_bit, z_bit, z_bit, x_bit, x_bit, x_bit, parity, parity)


def minimum_hamming_distance() -> int:
    codewords = tuple(
        record_codeword(*outcome) for outcome in product((0, 1), repeat=2)
    )
    return min(
        sum(a != b for a, b in zip(first, second))
        for index, first in enumerate(codewords)
        for second in codewords[index + 1 :]
    )


def word_failure_tail(
    record_length: int,
    correctable_flips: int,
    slot_error: float,
) -> float:
    return sum(
        math.comb(record_length, flips)
        * slot_error**flips
        * (1.0 - slot_error) ** (record_length - flips)
        for flips in range(correctable_flips + 1, record_length + 1)
    )


def solve_slot_threshold(
    record_length: int,
    correctable_flips: int,
    target: float,
) -> float:
    low, high = 0.0, 0.5
    for _ in range(80):
        mid = 0.5 * (low + high)
        if word_failure_tail(record_length, correctable_flips, mid) <= target:
            low = mid
        else:
            high = mid
    return low


def controller_calculation() -> ControllerCalculation:
    """Evaluate the supplied record-code controller envelope."""

    record_length = len(record_codeword(0, 0))
    distance = minimum_hamming_distance()
    correctable = (distance - 1) // 2
    slot_threshold = solve_slot_threshold(
        record_length,
        correctable,
        TARGET_WORD_FAILURE,
    )
    area_budget = math.asin(
        math.sqrt(slot_threshold - LEAKAGE_BUDGET - CROSSTALK_BUDGET)
    )
    return ControllerCalculation(
        record_length=record_length,
        minimum_distance=distance,
        correctable_flips=correctable,
        slot_threshold=slot_threshold,
        area_budget_rad=area_budget,
        controller_margin=area_budget / IMPLEMENTED_AREA_COMPARATOR_RAD,
        threshold_residual=abs(
            word_failure_tail(record_length, correctable, slot_threshold)
            - TARGET_WORD_FAILURE
        ),
    )


def kl_half_against(probability: float) -> float:
    return 0.5 * math.log(0.5 / probability) + 0.5 * math.log(
        0.5 / (1.0 - probability)
    )


def detector_calculation() -> DetectorCalculation:
    """Evaluate the supplied finite-domain detector envelope."""

    spins_per_slot = DOMAIN_SIDE**3
    per_spin_probability = DEFECT_PROBABILITY + THERMAL_DEFECT_FACTOR
    record_length = len(record_codeword(0, 0))
    distance = minimum_hamming_distance()
    detector_word_bound = min(
        1.0,
        record_length
        * math.exp(-spins_per_slot * kl_half_against(per_spin_probability)),
    )
    single_spin_overlap = 2.0 * math.sqrt(
        per_spin_probability * (1.0 - per_spin_probability)
    )
    return DetectorCalculation(
        domain_side=DOMAIN_SIDE,
        defect_probability=DEFECT_PROBABILITY,
        detector_word_bound=detector_word_bound,
        detector_log10_overlap=(
            math.log10(single_spin_overlap) * spins_per_slot * distance
        ),
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
    if not 0.0 < args.tolerance < 1e-3:
        raise ValueError("--tolerance must be in (0, 1e-3)")
    if args.gap_floor <= 0.0:
        raise ValueError("--gap-floor must be positive")
    if not 0.0 < args.bell_floor <= 1.0:
        raise ValueError("--bell-floor must be in (0, 1]")

    selector = selector_calculation()
    scaling = scaling_calculation(args.gap_floor, args.bell_floor)
    controller = controller_calculation()
    detector = detector_calculation()

    candidate_product_gate = selector.bare_candidate_count == 64
    selector_filter_gate = (
        selector.residual_without_orientation == 2
        and selector.residual_without_action == 8
        and selector.residual_without_no_dwell == 4
        and selector.final_selector_count == 1
        and selector.clauses_are_minimal_on_defined_family
    )
    finite_resource_gate = (
        scaling.certified_sides == (4, 6, 8, 10, 12)
        and scaling.min_margin > args.tolerance
        and scaling.scaled_gap_monotone_on_supplied_rows
        and scaling.bell_monotone_on_supplied_rows
        and min(row.bell for row in SIGNED_RESOURCE_ROWS)
        + args.tolerance
        >= args.bell_floor
    )
    controller_gate = (
        controller.record_length == 8
        and controller.minimum_distance == 5
        and controller.correctable_flips == 2
        and controller.threshold_residual <= args.tolerance
        and controller.area_budget_rad > IMPLEMENTED_AREA_COMPARATOR_RAD
        and controller.controller_margin > 2.0
    )
    detector_gate = (
        detector.domain_side == DOMAIN_SIDE
        and math.isclose(
            detector.defect_probability,
            DEFECT_PROBABILITY,
            rel_tol=0.0,
            abs_tol=args.tolerance,
        )
        and detector.detector_word_bound < TARGET_WORD_FAILURE
        and detector.detector_log10_overlap < -12.0
    )
    gates = (
        candidate_product_gate,
        selector_filter_gate,
        finite_resource_gate,
        controller_gate,
        detector_gate,
    )

    print("TELEPORTATION CONCLUSION BOUNDARY")
    print(
        "Status: conditional finite-premise support; "
        "the physical open gate is unchanged"
    )
    print(
        "Claim boundary: finite combinatorics and requirement-envelope "
        "arithmetic only"
    )
    print()
    print(
        "selector calculation: "
        f"bare_candidates={selector.bare_candidate_count}, "
        f"without_orientation={selector.residual_without_orientation}, "
        f"without_action={selector.residual_without_action}, "
        f"without_no_dwell={selector.residual_without_no_dwell}, "
        f"final_selector_count={selector.final_selector_count}, "
        "physical_completeness=not tested"
    )
    print(
        "scaling calculation: "
        f"certified_sides={','.join(str(side) for side in scaling.certified_sides)}, "
        f"gap_floor={scaling.gap_floor:.3f}/L^2, "
        f"bell_floor={scaling.bell_floor:.6f}, "
        f"min_margin={scaling.min_margin:.3e}, "
        "scope=supplied_rows_only"
    )
    print(
        "hardware calculation: "
        f"record_length={controller.record_length}, "
        f"d_min={controller.minimum_distance}, "
        f"correctable={controller.correctable_flips}, "
        f"slot_threshold={controller.slot_threshold:.9e}, "
        f"area_budget={controller.area_budget_rad:.11f}, "
        f"controller_margin={controller.controller_margin:.9f}, "
        f"detector_word_bound={detector.detector_word_bound:.3e}, "
        f"detector_log10_overlap={detector.detector_log10_overlap:.3f}, "
        "device_evidence=not tested"
    )
    print()
    print("Acceptance gates:")
    print_gate("defined candidate product is enumerated exhaustively", gates[0])
    print_gate("defined selector filters have the stated residual counts", gates[1])
    print_gate("five supplied resource rows satisfy the finite checks", gates[2])
    print_gate("controller envelope arithmetic is internally consistent", gates[3])
    print_gate("detector envelope arithmetic is internally consistent", gates[4])
    print()
    print("Limitations:")
    print("  The supplied selector family is not proved physically complete.")
    print("  No all-even continuation or fabricated-device evidence is tested.")
    print("  The live audit repair target remains open.")
    return 0 if all(gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
