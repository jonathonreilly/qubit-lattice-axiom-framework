#!/usr/bin/env python3
"""Cycle 783: cross-test invariant physical functionals at the W2 wall.

This bounded runner reconstructs the Cycle-752 adjacent-start battery and
then replaces its fixed station permutation only at active Q contests.  The
declared functional family is the Cycle-775/780 construction stated in the
task: first-Q-layer physical gate count and initial station occupancy, with
ascending and descending mirrors always tested together.

An equal-valued pair is not secretly completed with station index.  Both
orders are propagated; if they differ, the functional has failed to supply
an order at that boundary.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import perf_counter
import types
from typing import Callable


AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle752_adjacency_independent_check_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
)

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "cfff6c6c8acf971c78682caec55f2bd70d661cd21e70d619ef1e1087fc412fd2",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[3]:
        "2bfc05e703ab75663360361296fe3f816884faf5397ac04a3e55e277244e5ce7",
}
RING_STATIONS = 11
FIXTURE_BANKS = 2
EXPECTED_COUNT = 2
ROUTE3_FIXED_Q_ORDER = (1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2)
STDOUT_LIMIT_BYTES = 150 * 1024
RUNTIME_LIMIT_SEC = 1500.0

# The Cycle-752 checker uses these exact inert shims to keep its held-fixture
# entry point inside the bounded input set.  Neither supplies an attribute.
for _shim_name in (
    "frontier_cycle734_paired_excitation_genesis_2026_07_28",
    "frontier_cycle731_token_count_certificate_2026_07_28",
):
    sys.modules.setdefault(_shim_name, types.ModuleType(_shim_name))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle735_separated_pair_lawful_control_2026_07_28 as S735


ROOT = Path(__file__).resolve().parents[1]
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def emit(label: str, value: object) -> None:
    OUTPUT_LINES.append(
        f"{label}={json.dumps(value, sort_keys=True, separators=(',', ':'))}"
    )


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: "
        f"{json.dumps(detail, sort_keys=True, separators=(',', ':'))}"
    )
    return passed


def digest_bits(bits: tuple[int, ...]) -> str:
    return sha256(bytes(bits)).hexdigest()


def apply_pair(
    data: tuple[int, ...],
    macros: tuple[tuple[object, ...], ...],
    order: tuple[int, int],
) -> tuple[int, ...]:
    output = data
    for station in order:
        output = K.A.apply_semantic(output, macros[station])
    return output


def command_output(arguments: tuple[str, ...]) -> str:
    completed = subprocess.run(
        arguments,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def source_certificate() -> dict[str, object]:
    observed = {
        relative: sha256((ROOT / relative).read_bytes()).hexdigest()
        for relative in AUDIT_INPUT_PATHS
    }
    provenance = {}
    for relative in AUDIT_INPUT_PATHS:
        provenance[relative] = {
            "source": "present in bounded worktree; no copy performed",
            "head_blob": command_output(
                ("git", "ls-tree", "HEAD", relative)
            ).split()[2],
            "last_commit": command_output(
                ("git", "log", "-1", "--format=%H", "--", relative)
            ),
        }
    return {
        "audit_input_paths_literal": AUDIT_INPUT_PATHS,
        "observed_sha256": observed,
        "expected_sha256": EXPECTED_SHA256,
        "anchors_match": observed == EXPECTED_SHA256,
        "head": command_output(("git", "rev-parse", "HEAD")),
        "provenance": provenance,
        "copied_modules": (),
        "reimplementation_basis": {
            "external_basis": (
                "Cycle-783 task statement's Cycle-775/780 construction; "
                "no blockP file was read"
            ),
            "gate_item_value": (
                "g_s=len(K.controlled_macro(K.mapped_macro(program[s]),"
                " A_s, work_s))"
            ),
            "gate_configuration_value": (
                "F_gate(p)=g_p+g_{p+1} for initially occupied stations"
            ),
            "occupancy_item_value": (
                "n_p(s)=1 iff s is one of initial stations p,p+1"
            ),
            "mirror_rule": "compare item values ascending and descending",
            "tie_rule": (
                "propagate both orders; a differing pair is unresolved, "
                "with no station-index completion"
            ),
        },
    }


def fixture() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    data = S735.held_fixture_data()
    macros = tuple(K.mapped_macro(row) for row in program)
    data_width = len(data)
    physical_counts = tuple(
        len(
            K.controlled_macro(
                macros[station],
                data_width + station,
                data_width + 2 * RING_STATIONS + station,
            )
        )
        for station in range(RING_STATIONS)
    )
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    expected = K.A.apply_semantic(
        K.A.apply_semantic(data, allocator), allocator
    )
    if len(program) != RING_STATIONS:
        raise AssertionError(("held program width", len(program)))
    return {
        "program": program,
        "data": data,
        "macros": macros,
        "physical_counts": physical_counts,
        "expected": expected,
    }


def run_fixed_order(
    fixed: dict[str, object],
    start: int,
    order: tuple[int, ...],
) -> tuple[int, ...]:
    rank = {station: index for index, station in enumerate(order)}
    data = fixed["data"]
    macros = fixed["macros"]
    for step in range(RING_STATIONS):
        left = (start + step) % RING_STATIONS
        right = (left + 1) % RING_STATIONS
        active_order = (
            (left, right)
            if rank[left] < rank[right]
            else (right, left)
        )
        data = apply_pair(data, macros, active_order)
    return data


def sampled_fixed_order_table(
    fixed: dict[str, object],
) -> tuple[dict[str, object], ...]:
    witness = ROUTE3_FIXED_Q_ORDER
    specifications = [
        (
            f"sequence_rotation_{offset}",
            "rotation_class",
            witness[offset:] + witness[:offset],
        )
        for offset in range(RING_STATIONS)
    ]
    specifications.extend(
        (
            ("ascending", "structured", tuple(range(RING_STATIONS))),
            (
                "descending",
                "structured",
                tuple(reversed(range(RING_STATIONS))),
            ),
            (
                "even_then_odd",
                "structured",
                tuple(range(0, RING_STATIONS, 2))
                + tuple(range(1, RING_STATIONS, 2)),
            ),
            (
                "odd_then_even",
                "structured",
                tuple(range(1, RING_STATIONS, 2))
                + tuple(range(0, RING_STATIONS, 2)),
            ),
            (
                "witness_reverse",
                "structured",
                tuple(reversed(witness)),
            ),
            (
                "zigzag",
                "structured",
                (0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5),
            ),
        )
    )
    rows = []
    for name, family, order in specifications:
        correct = tuple(
            start
            for start in range(RING_STATIONS)
            if run_fixed_order(fixed, start, order) == fixed["expected"]
        )
        rows.append(
            {
                "name": name,
                "family": family,
                "order": order,
                "correct_positions": correct,
                "passes": len(correct),
            }
        )
    return tuple(rows)


def exhaustive_fixed_order_classes(
    fixed: dict[str, object],
) -> dict[str, object]:
    """Enumerate the 2^11 adjacent-edge orientations.

    A total station order induces one orientation on every edge of C_11.
    Conversely every orientation other than the two directed cycles is a
    DAG and hence has a topological total order.  Thus the 2046 retained
    masks are exactly all fixed-order behavior classes on this battery.
    """

    size = 1 << RING_STATIONS
    start_mask_by_orientation = [0] * size
    macros = fixed["macros"]
    for start in range(RING_STATIONS):
        states = [fixed["data"]]
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            next_states = []
            for data in states:
                next_states.append(
                    apply_pair(data, macros, (left, right))
                )
                next_states.append(
                    apply_pair(data, macros, (right, left))
                )
            states = next_states
        for local_mask, output in enumerate(states):
            if output != fixed["expected"]:
                continue
            absolute_mask = 0
            for step in range(RING_STATIONS):
                decision = (
                    local_mask >> (RING_STATIONS - 1 - step)
                ) & 1
                edge = (start + step) % RING_STATIONS
                absolute_mask |= decision << edge
            start_mask_by_orientation[absolute_mask] |= 1 << start

    realizable = range(1, size - 1)
    histogram = Counter(
        start_mask_by_orientation[mask].bit_count()
        for mask in realizable
    )
    local_successes = tuple(
        sum(
            bool(start_mask_by_orientation[mask] & (1 << start))
            for mask in range(size)
        )
        for start in range(RING_STATIONS)
    )
    return {
        "edge_orientation_classes": size,
        "fixed_total_order_classes": size - 2,
        "excluded_directed_cycle_classes": (0, size - 1),
        "pass_count_histogram": dict(sorted(histogram.items())),
        "best_fixed_order_passes": max(histogram),
        "position_uniform_fixed_orders": sum(
            start_mask_by_orientation[mask] == size - 1
            for mask in realizable
        ),
        "all_local_orientation_success_counts_by_start":
            local_successes,
    }


def baseline(fixed: dict[str, object]) -> dict[str, object]:
    table = sampled_fixed_order_table(fixed)
    witness = table[0]
    rotations = tuple(row for row in table if row["family"] == "rotation_class")
    structured = tuple(row for row in table if row["family"] == "structured")
    exhaustive = exhaustive_fixed_order_classes(fixed)
    return {
        "witness_order": ROUTE3_FIXED_Q_ORDER,
        "witness_correct_positions": witness["correct_positions"],
        "witness_passes": witness["passes"],
        "sampled_fixed_order_table": table,
        "rotation_orders_with_any_success": sum(
            bool(row["passes"]) for row in rotations
        ),
        "rotation_allocator_correct_cases": sum(
            row["passes"] for row in rotations
        ),
        "structured_orders_with_any_success": sum(
            bool(row["passes"]) for row in structured
        ),
        "structured_allocator_correct_cases": sum(
            row["passes"] for row in structured
        ),
        "sampled_position_uniform_orders": sum(
            row["passes"] == RING_STATIONS for row in table
        ),
        "exhaustive": exhaustive,
    }


def functional_battery(
    fixed: dict[str, object],
    name: str,
    value_kind: str,
    descending: bool,
) -> dict[str, object]:
    macros = fixed["macros"]
    physical_counts = fixed["physical_counts"]
    rows = []
    for start in range(RING_STATIONS):
        initial_occupancy = tuple(
            int(station in (start, (start + 1) % RING_STATIONS))
            for station in range(RING_STATIONS)
        )
        states = {fixed["data"]}
        unresolved = []
        for step in range(RING_STATIONS):
            left = (start + step) % RING_STATIONS
            right = (left + 1) % RING_STATIONS
            if value_kind == "physical_gate_count":
                values = (
                    physical_counts[left],
                    physical_counts[right],
                )
            elif value_kind == "initial_station_occupancy":
                values = (
                    initial_occupancy[left],
                    initial_occupancy[right],
                )
            else:
                raise AssertionError(("functional kind", value_kind))

            if values[0] != values[1]:
                lower = (
                    (left, right)
                    if values[0] < values[1]
                    else (right, left)
                )
                order = tuple(reversed(lower)) if descending else lower
                states = {
                    apply_pair(data, macros, order) for data in states
                }
                continue

            next_states = set()
            differing_inputs = 0
            for data in states:
                forward = apply_pair(data, macros, (left, right))
                reverse = apply_pair(data, macros, (right, left))
                differing_inputs += forward != reverse
                next_states.add(forward)
                next_states.add(reverse)
            if differing_inputs:
                unresolved.append(
                    {
                        "step": step,
                        "items": (left, right),
                        "tied_value": values[0],
                        "differing_input_branches": differing_inputs,
                    }
                )
            states = next_states

        defined = not unresolved
        all_outputs_correct = states == {fixed["expected"]}
        possible_output_digests = tuple(
            sorted(digest_bits(state) for state in states)
        )
        rows.append(
            {
                "start": start,
                "passes": defined and all_outputs_correct,
                "order_defined": defined,
                "all_outputs_correct": all_outputs_correct,
                "possible_outputs": len(states),
                "possible_output_digests": possible_output_digests,
                "unresolved_order_sensitive_ties": tuple(unresolved),
            }
        )
    correct_positions = tuple(
        row["start"] for row in rows if row["passes"]
    )
    return {
        "name": name,
        "value_kind": value_kind,
        "mirror": "descending" if descending else "ascending",
        "passes": len(correct_positions),
        "correct_positions": correct_positions,
        "starts_with_total_order": sum(
            row["order_defined"] for row in rows
        ),
        "rows": tuple(rows),
    }


FUNCTIONAL_SPECS = (
    (
        "first_Q_physical_gate_count_ASC",
        "physical_gate_count",
        False,
    ),
    (
        "first_Q_physical_gate_count_DESC",
        "physical_gate_count",
        True,
    ),
    (
        "initial_station_occupancy_ASC",
        "initial_station_occupancy",
        False,
    ),
    (
        "initial_station_occupancy_DESC",
        "initial_station_occupancy",
        True,
    ),
)


def functional_mapping(fixed: dict[str, object]) -> dict[str, object]:
    station_rows = []
    for station, (program_row, macro, count) in enumerate(
        zip(
            fixed["program"],
            fixed["macros"],
            fixed["physical_counts"],
        )
    ):
        station_rows.append(
            {
                "station": station,
                "program_kind": program_row[0],
                "program_index": program_row[1],
                "landed_semantic_macro_gates": len(macro),
                "first_Q_physical_gates": count,
            }
        )
    start_rows = []
    for start in range(RING_STATIONS):
        items = (start, (start + 1) % RING_STATIONS)
        item_values = tuple(
            fixed["physical_counts"][station] for station in items
        )
        occupancy = tuple(
            int(station in items) for station in range(RING_STATIONS)
        )
        start_rows.append(
            {
                "start": start,
                "contended_items_initially": items,
                "gate_item_values": item_values,
                "gate_configuration_sum": sum(item_values),
                "initial_station_occupancies": occupancy,
                "occupancy_configuration_sum": sum(occupancy),
            }
        )
    return {
        "station_item_mapping": tuple(station_rows),
        "initial_configuration_mapping": tuple(start_rows),
        "adjacent_gate_value_ties": sum(
            fixed["physical_counts"][station]
            == fixed["physical_counts"][
                (station + 1) % RING_STATIONS
            ]
            for station in range(RING_STATIONS)
        ),
    }


def translate_fixture(
    fixed: dict[str, object], shift: int
) -> dict[str, object]:
    translated_program: list[object] = [None] * RING_STATIONS
    translated_macros: list[object] = [None] * RING_STATIONS
    translated_counts = [0] * RING_STATIONS
    for old in range(RING_STATIONS):
        new = (old + shift) % RING_STATIONS
        translated_program[new] = fixed["program"][old]
        translated_macros[new] = fixed["macros"][old]
        translated_counts[new] = fixed["physical_counts"][old]
    return {
        "program": tuple(translated_program),
        "data": fixed["data"],
        "macros": tuple(translated_macros),
        "physical_counts": tuple(translated_counts),
        "expected": fixed["expected"],
    }


def covariance_control(
    fixed: dict[str, object],
    original_results: tuple[dict[str, object], ...],
) -> dict[str, object]:
    """Check the lawful C_11 label action with all physical data carried."""

    comparisons = 0
    failures = []
    for shift in range(RING_STATIONS):
        translated = translate_fixture(fixed, shift)
        for spec, original in zip(FUNCTIONAL_SPECS, original_results):
            name, value_kind, descending = spec
            rerun = functional_battery(
                translated, name, value_kind, descending
            )
            for old_start in range(RING_STATIONS):
                new_start = (old_start + shift) % RING_STATIONS
                before = original["rows"][old_start]
                after = rerun["rows"][new_start]
                comparisons += 1
                invariant_fields = (
                    "passes",
                    "order_defined",
                    "all_outputs_correct",
                    "possible_outputs",
                    "possible_output_digests",
                )
                if any(
                    before[field] != after[field]
                    for field in invariant_fields
                ):
                    failures.append(
                        {
                            "shift": shift,
                            "functional": name,
                            "old_start": old_start,
                            "new_start": new_start,
                        }
                    )
    return {
        "lawful_relabeling": (
            "cyclic C_11 station-label translation s->s+k, carrying "
            "program rows/macros, gate weights, initial A occupancy, "
            "and token positions; successor transport is preserved"
        ),
        "scope": (
            "cyclic translations only; reflections are not asserted "
            "because s->s+1 transport would require a direction reversal"
        ),
        "partial_order_note": (
            "occupancy mirrors are covariant preorders but fail to become "
            "orders at order-sensitive equal-occupancy contests"
        ),
        "comparisons": comparisons,
        "expected_comparisons":
            RING_STATIONS * len(FUNCTIONAL_SPECS) * RING_STATIONS,
        "failures": tuple(failures),
        "passes": not failures,
    }


def core_experiment() -> dict[str, object]:
    fixed = fixture()
    base = baseline(fixed)
    mapping = functional_mapping(fixed)
    functionals = tuple(
        functional_battery(fixed, name, value_kind, descending)
        for name, value_kind, descending in FUNCTIONAL_SPECS
    )
    best = max(row["passes"] for row in functionals)
    full = tuple(
        row["name"]
        for row in functionals
        if row["passes"] == RING_STATIONS
    )
    fixed_best = base["exhaustive"]["best_fixed_order_passes"]
    if full:
        outcome = "ORDER_FOUND"
    elif best > fixed_best:
        outcome = "ORDER_PARTIAL"
    else:
        outcome = "NO_ORDER"
    return {
        "baseline": base,
        "mapping": mapping,
        "functionals": functionals,
        "outcome": outcome,
        "best_functional_passes": best,
        "position_uniform_functionals": full,
        "bounded_conclusion": (
            f"{outcome} at the Cycle-752 held ring-11 fixture only; "
            "this is an input to W2 and is not a W2-closure claim"
        ),
        "covariance": covariance_control(fixed, functionals),
        "expected_output_sha256": digest_bits(fixed["expected"]),
    }


def compact_functional_table(
    functionals: tuple[dict[str, object], ...],
) -> tuple[dict[str, object], ...]:
    return tuple(
        {
            "name": functional["name"],
            "passes": functional["passes"],
            "correct_positions": functional["correct_positions"],
            "starts_with_total_order":
                functional["starts_with_total_order"],
            "start_table": tuple(
                {
                    "start": row["start"],
                    "pass": row["passes"],
                    "order_defined": row["order_defined"],
                    "all_outputs_correct": row["all_outputs_correct"],
                    "possible_outputs": row["possible_outputs"],
                    "unresolved_ties": len(
                        row["unresolved_order_sensitive_ties"]
                    ),
                }
                for row in functional["rows"]
            ),
        }
        for functional in functionals
    )


def main() -> int:
    started = perf_counter()
    source = source_certificate()
    first = core_experiment()
    second = core_experiment()
    deterministic = first == second
    elapsed = perf_counter() - started

    baseline_result = first["baseline"]
    sampled = baseline_result["sampled_fixed_order_table"]
    observed_fixed_table = tuple(
        (row["name"], row["correct_positions"]) for row in sampled
    )
    expected_fixed_table = (
        ("sequence_rotation_0", (0,)),
        ("sequence_rotation_1", ()),
        ("sequence_rotation_2", ()),
        ("sequence_rotation_3", (0,)),
        ("sequence_rotation_4", (0,)),
        ("sequence_rotation_5", (0,)),
        ("sequence_rotation_6", (0,)),
        ("sequence_rotation_7", (0,)),
        ("sequence_rotation_8", (0,)),
        ("sequence_rotation_9", (0,)),
        ("sequence_rotation_10", (0,)),
        ("ascending", ()),
        ("descending", ()),
        ("even_then_odd", ()),
        ("odd_then_even", (0,)),
        ("witness_reverse", ()),
        ("zigzag", ()),
    )
    exhaustive = baseline_result["exhaustive"]
    mapping = first["mapping"]
    functional_table = compact_functional_table(first["functionals"])
    functional_counts = {
        row["name"]: row["passes"] for row in first["functionals"]
    }

    emit("CYCLE783_AUDIT_INPUT_PATHS", AUDIT_INPUT_PATHS)
    emit("CYCLE783_PROVENANCE", source["provenance"])
    emit(
        "CYCLE783_FUNCTIONAL_REIMPLEMENTATION_BASIS",
        source["reimplementation_basis"],
    )
    check(
        "CERTIFICATE_A_ANCHORS_PROVENANCE_FUNCTIONAL_BASIS",
        source["anchors_match"]
        and not source["copied_modules"]
        and len(source["provenance"]) == len(AUDIT_INPUT_PATHS),
        {
            "anchors_match": source["anchors_match"],
            "head": source["head"],
            "copied_modules": source["copied_modules"],
            "observed_sha256": source["observed_sha256"],
        },
    )

    emit("CYCLE783_FIXED_ORDER_FAILURE_TABLE", sampled)
    emit("CYCLE783_FIXED_ORDER_EXHAUSTIVE_CONTROL", exhaustive)
    baseline_pass = (
        observed_fixed_table == expected_fixed_table
        and baseline_result["witness_passes"] == 1
        and baseline_result["witness_correct_positions"] == (0,)
        and baseline_result["rotation_orders_with_any_success"] == 9
        and baseline_result["rotation_allocator_correct_cases"] == 9
        and baseline_result["structured_orders_with_any_success"] == 1
        and baseline_result["structured_allocator_correct_cases"] == 1
        and baseline_result["sampled_position_uniform_orders"] == 0
        and exhaustive["fixed_total_order_classes"] == 2046
        and exhaustive["pass_count_histogram"] == {0: 1535, 1: 511}
        and exhaustive["best_fixed_order_passes"] == 1
        and exhaustive["position_uniform_fixed_orders"] == 0
    )
    check(
        "CERTIFICATE_B_CYCLE752_BASELINE_EXACT",
        baseline_pass,
        {
            "witness": (
                baseline_result["witness_passes"],
                RING_STATIONS,
            ),
            "sampled_orders": len(sampled),
            "sampled_uniform": 0,
            "exhaustive_fixed_classes": 2046,
            "exhaustive_uniform": 0,
            "best_fixed": exhaustive["best_fixed_order_passes"],
        },
    )

    emit("CYCLE783_FUNCTIONAL_ITEM_MAPPING", mapping)
    construction_pass = (
        tuple(
            row["first_Q_physical_gates"]
            for row in mapping["station_item_mapping"]
        )
        == (9, 1146, 1512, 755, 20, 1146, 1, 20, 749, 1215, 29)
        and mapping["adjacent_gate_value_ties"] == 0
        and all(
            row["occupancy_configuration_sum"] == EXPECTED_COUNT
            for row in mapping["initial_configuration_mapping"]
        )
        and tuple(spec[2] for spec in FUNCTIONAL_SPECS)
        == (False, True, False, True)
    )
    check(
        "CERTIFICATE_C_FUNCTIONAL_ORDER_CONSTRUCTION_MAPPING",
        construction_pass,
        {
            "family": tuple(spec[0] for spec in FUNCTIONAL_SPECS),
            "adjacent_gate_value_ties":
                mapping["adjacent_gate_value_ties"],
            "mapping_rows":
                len(mapping["initial_configuration_mapping"]),
        },
    )

    emit("CYCLE783_FUNCTIONAL_11_START_TABLE", functional_table)
    emit(
        "CYCLE783_FROZEN_OUTCOME",
        {
            "outcome": first["outcome"],
            "counts": functional_counts,
            "position_uniform_functionals":
                first["position_uniform_functionals"],
            "bounded_conclusion": first["bounded_conclusion"],
        },
    )
    outcome_pass = (
        functional_counts
        == {
            "first_Q_physical_gate_count_ASC": 0,
            "first_Q_physical_gate_count_DESC": 0,
            "initial_station_occupancy_ASC": 0,
            "initial_station_occupancy_DESC": 0,
        }
        and first["outcome"] == "NO_ORDER"
        and first["best_functional_passes"]
        <= exhaustive["best_fixed_order_passes"]
        and not first["position_uniform_functionals"]
    )
    check(
        "CERTIFICATE_D_FULL_BATTERY_FROZEN_OUTCOME",
        outcome_pass,
        {
            "counts": functional_counts,
            "outcome": first["outcome"],
            "fixed_baseline_best":
                exhaustive["best_fixed_order_passes"],
            "W2_closure_claim": False,
        },
    )

    emit("CYCLE783_COVARIANCE_CONTROL", first["covariance"])
    before_e_bytes = len(("\n".join(OUTPUT_LINES) + "\n").encode())
    bounds_pass = (
        first["covariance"]["passes"]
        and first["covariance"]["comparisons"]
        == first["covariance"]["expected_comparisons"]
        == 484
        and deterministic
        and elapsed < RUNTIME_LIMIT_SEC
        and before_e_bytes < STDOUT_LIMIT_BYTES - 4096
    )
    check(
        "CERTIFICATE_E_COVARIANCE_DETERMINISM_BOUNDS",
        bounds_pass,
        {
            "covariance_comparisons":
                first["covariance"]["comparisons"],
            "covariance_failures":
                len(first["covariance"]["failures"]),
            "deterministic_full_rerun": deterministic,
            "runtime_sec": round(elapsed, 6),
            "runtime_limit_sec": RUNTIME_LIMIT_SEC,
            "stdout_bytes_before_E": before_e_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    emit(
        "CYCLE783_FINAL",
        {
            "status": "PASS" if all(CHECKS.values()) else "FAIL",
            "baseline": "witness 1/11; fixed uniform 0",
            "functional_counts": functional_counts,
            "outcome": first["outcome"],
            "runtime_sec": round(elapsed, 6),
            "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        },
    )

    stdout = "\n".join(OUTPUT_LINES) + "\n"
    if len(stdout.encode()) > STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout limit", len(stdout.encode()), STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(stdout)
    return 0 if all(CHECKS.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
