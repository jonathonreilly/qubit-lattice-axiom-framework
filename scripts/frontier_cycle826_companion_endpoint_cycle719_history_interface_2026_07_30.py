#!/usr/bin/env python3
"""Cycle 826: Cycle-823 endpoint output into the Cycle-719 history interface.

This runner composes the exact Cycle-823 full-seam endpoint truth map with
the unchanged Cycle-719 recurrent controller at its declared register
interface.  It does not claim a same-chart physical placement between the
two landed compilers; coordinate co-location/routing remains explicit and
open.
"""

from __future__ import annotations

from hashlib import sha256
import json
import math
from pathlib import Path
import time

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M720
import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as H719
import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as I823


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/COMPANION_ENDPOINT_CYCLE719_HISTORY_INTERFACE_"
    "CYCLE826_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
RUNNER_PATH = (
    "scripts/frontier_cycle826_companion_endpoint_cycle719_history_"
    "interface_2026_07_30.py"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    RUNNER_PATH,
    "docs/COMPANION_FULL_SEAM_ENDPOINT_INSTRUMENT_"
    "CYCLE823_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle823_companion_full_seam_endpoint_"
    "instrument_2026_07_30.py",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_"
    "CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle719_recurrent_matter_history_"
    "controller_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TOL = 3.0e-11


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def controller_input(left: int, right: int, pointer: int) -> tuple[int, ...]:
    banks, links = H719.B.chain_genesis(H719.BANKS)
    bits = list(H719.M.pack_state(banks, links))
    bits[H719.M.R3.X.LEFT_ENDPOINT] = left
    bits[H719.M.R3.X.RIGHT_ENDPOINT] = right
    bits[H719.R3_SOURCE_POINTER()] = pointer
    return tuple(bits)


def decode_history(bits: tuple[int, ...]) -> tuple[int, ...]:
    banks, links = H719.M.unpack_state(bits, H719.BANKS)
    chain, _order = H719.B.decode_local_graph(banks, links)
    return tuple(cell.orientation for cell in chain.cells)


def expected_orientation(left: int, right: int, pointer: int) -> tuple[int, ...]:
    if not pointer:
        return ()
    return (1 if right else -1,)


def controller_truth_table() -> dict[str, object]:
    rows = []
    failures = inverse_failures = token_failures = pointer_failures = 0
    endpoint_failures = history_failures = 0
    deletion_detected = dirty_pointer_detected = 0
    zero_token_detected = two_token_detected = 0
    finalizer_index = next(
        index for index, row in enumerate(H719.PROGRAM)
        if row[0] == "finalizer"
    )
    damaged_program = list(H719.PROGRAM)
    damaged_program[finalizer_index] = ("identity", 0, ())
    damaged_program = tuple(damaged_program)
    for left in (0, 1):
        for right in (0, 1):
            pointer = left ^ right
            before = controller_input(left, right, pointer)
            after, a_tokens, b_tokens, _trace = H719.K.run_orbit(
                before, H719.PROGRAM
            )
            restored, ra_tokens, rb_tokens, _reverse_trace = H719.K.run_orbit(
                after, H719.PROGRAM, reverse=True
            )
            history = decode_history(after)
            expected = expected_orientation(left, right, pointer)
            endpoint_ok = (
                after[H719.M.R3.X.LEFT_ENDPOINT] == left
                and after[H719.M.R3.X.RIGHT_ENDPOINT] == right
            )
            pointer_ok = after[H719.R3_SOURCE_POINTER()] == 0
            tokens_ok = (
                tuple(index for index, value in enumerate(a_tokens) if value)
                == (0,)
                and not any(b_tokens)
                and tuple(index for index, value in enumerate(ra_tokens) if value)
                == (0,)
                and not any(rb_tokens)
            )
            failures += not (
                endpoint_ok and pointer_ok and tokens_ok
                and history == expected and restored == before
            )
            inverse_failures += restored != before
            token_failures += not tokens_ok
            pointer_failures += not pointer_ok
            endpoint_failures += not endpoint_ok
            history_failures += history != expected

            deleted, *_ = H719.K.run_orbit(before, damaged_program)
            if pointer:
                deletion_detected += (
                    deleted != after
                    and deleted[H719.R3_SOURCE_POINTER()] == 1
                )

            dirty = list(before)
            dirty[H719.R3_SOURCE_POINTER()] ^= 1
            dirty_after, *_ = H719.K.run_orbit(tuple(dirty), H719.PROGRAM)
            dirty_pointer_detected += dirty_after != after

            zero, *_ = H719.K.run_orbit(
                before, H719.PROGRAM, token_positions=()
            )
            double, *_ = H719.K.run_orbit(
                before, H719.PROGRAM, token_positions=(0, 1)
            )
            zero_token_detected += zero != after
            two_token_detected += double != after
            rows.append({
                "left": left,
                "right": right,
                "pointer": pointer,
                "history": history,
                "expected_history": expected,
                "pointer_returned_clean": pointer_ok,
                "controller_token_returned": tokens_ok,
                "inverse_exact": restored == before,
            })
    return {
        "rows": tuple(rows),
        "truth_rows": len(rows),
        "failures": failures,
        "inverse_failures": inverse_failures,
        "controller_token_failures": token_failures,
        "source_pointer_cleanup_failures": pointer_failures,
        "endpoint_preservation_failures": endpoint_failures,
        "history_orientation_failures": history_failures,
        "success_finalizer_deletions_detected": deletion_detected,
        "expected_success_rows": 2,
        "dirty_pointer_inputs_detected": dirty_pointer_detected,
        "zero_token_inputs_detected": zero_token_detected,
        "two_token_inputs_detected": two_token_detected,
        "program_stations": len(H719.PROGRAM),
    }


def interface_key(
    matter_basis: int,
    amplitude: complex,
    left: int,
    right: int,
    width: int,
) -> tuple[int, complex, tuple[int, int, int]]:
    pointer_wire = width + 2
    pointer = (matter_basis >> pointer_wire) & 1
    post_left = (matter_basis >> left) & 1
    post_right = (matter_basis >> right) & 1
    clean_matter = matter_basis & ((1 << width) - 1)
    return clean_matter, amplitude, (post_left, post_right, pointer)


def composition_certificate(truth: dict[str, object]) -> dict[str, object]:
    cases = failures = interface_failures = 0
    maximum_residual = 0.0
    histories = {(): 0, (-1,): 0, (1,): 0}
    actual_history = {
        (row["left"], row["right"], row["pointer"]): tuple(row["history"])
        for row in truth["rows"]
    }
    per_shape = []
    for shape in I823.SHAPES:
        fixture = M720.CompanionFixture.build(shape)
        shape_cases = shape_failures = 0
        for edge_index, edge in enumerate(fixture.edges):
            left, right = edge[4], edge[5]
            for family, rows in (
                ("physical", fixture.physical_terms(edge_index)),
                ("target", fixture.target_terms(edge_index)),
            ):
                width = fixture.qubits if family == "physical" else fixture.matter_qubits
                for basis in I823.signature_representatives(rows, left, right):
                    cases += 1
                    shape_cases += 1
                    instrumented = I823.instrument_sparse(
                        rows, basis, left, right, width
                    )
                    seam = I823.apply_full_seam(rows, basis)
                    observed = {}
                    interface_rows = []
                    for output, amplitude in instrumented.items():
                        clean_matter, coefficient, interface = interface_key(
                            output, amplitude, left, right, width
                        )
                        interface_rows.append(interface)
                        post_left, post_right, pointer = interface
                        interface_failures += pointer != (post_left ^ post_right)
                        controller_history = actual_history[
                            (post_left, post_right, pointer)
                        ]
                        key = (clean_matter, controller_history)
                        observed[key] = observed.get(key, 0.0j) + coefficient
                    expected = {}
                    for output, amplitude in seam.items():
                        post_left = (output >> left) & 1
                        post_right = (output >> right) & 1
                        pointer = post_left ^ post_right
                        history = expected_orientation(
                            post_left, post_right, pointer
                        )
                        key = (output, history)
                        expected[key] = expected.get(key, 0.0j) + amplitude
                        histories[history] += 1
                    residual = math.sqrt(sum(
                        abs(observed.get(key, 0.0j) - expected.get(key, 0.0j)) ** 2
                        for key in set(observed) | set(expected)
                    ))
                    maximum_residual = max(maximum_residual, residual)
                    failed = residual > TOL or len(interface_rows) != 1
                    failures += failed
                    shape_failures += failed
        per_shape.append({
            "shape": shape,
            "cases": shape_cases,
            "failures": shape_failures,
        })
    return {
        "held_shapes": len(I823.SHAPES),
        "physical_or_target_phase_classes": cases,
        "composition_failures": failures,
        "interface_xor_failures": interface_failures,
        "maximum_composition_residual": maximum_residual,
        "history_class_counts": {str(key): value for key, value in histories.items()},
        "per_shape": tuple(per_shape),
    }


def main() -> None:
    started = time.time()
    declared_inputs = (
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and NOTE_PATH in AUDIT_INPUT_PATHS
        and RUNNER_PATH in AUDIT_INPUT_PATHS
        and all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        )
    )
    truth = controller_truth_table()
    composition = composition_certificate(truth)
    checks = {
        "declared_inputs_are_unique_existing_repo_relative_files": declared_inputs,
        "cycle719_controller_consumes_all_four_endpoint_rows_exactly": (
            truth["truth_rows"] == 4
            and truth["failures"] == 0
            and truth["inverse_failures"] == 0
            and truth["controller_token_failures"] == 0
            and truth["source_pointer_cleanup_failures"] == 0
            and truth["endpoint_preservation_failures"] == 0
            and truth["history_orientation_failures"] == 0
        ),
        "cycle823_full_seam_composes_with_history_interface_on_all_classes": (
            composition["held_shapes"] == 4
            and composition["physical_or_target_phase_classes"] == 1312
            and composition["composition_failures"] == 0
            and composition["interface_xor_failures"] == 0
            and composition["maximum_composition_residual"] < TOL
        ),
        "success_finalizer_deletion_is_active": (
            truth["success_finalizer_deletions_detected"]
            == truth["expected_success_rows"] == 2
        ),
        "dirty_pointer_and_token_sector_controls_are_active": (
            truth["dirty_pointer_inputs_detected"] == 4
            and truth["zero_token_inputs_detected"] == 2
            and truth["two_token_inputs_detected"] == 2
        ),
    }
    report = {
        "cycle": 826,
        "status": (
            "cycle826-companion-endpoint-cycle719-history-interface-bounded-positive"
            if all(checks.values()) else "cycle826-failed"
        ),
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "exact register-interface composition of the Cycle823 full-seam "
            "opportunity with the landed Cycle719 finite recurrent controller; "
            "same-chart physical port placement remains open"
        ),
        "controller_truth_table": truth,
        "composition": composition,
        "checks": checks,
        "inventory": {
            "derived": (
                "exact four-row endpoint-to-history interface",
                "exact 1312-class coherent composition",
                "source-pointer and controller-token return on success",
                "exact inverse on the finite Cycle719 bank",
            ),
            "supplied": (
                "Cycle823 finite full-seam compiler and clean endpoint registers",
                "Cycle719 unique token, finite program ring, banks, and clean work",
                "wire identification between endpoint occupations/pointer and controller inputs",
                "program occurrence and successful admission sector",
            ),
            "open": (
                "same-chart collision-free physical placement and route between compilers",
                "autonomous unique-token and clean-bank genesis or enforcement",
                "post-capacity renewal and multi-source arbitration",
                "objective admission, physical time, permanent Record, Born/history, and source/gravity",
            ),
        },
        "source_sha256": {
            path: digest(ROOT / path) for path in AUDIT_INPUT_PATHS
        } if declared_inputs else {},
        "runtime_seconds": time.time() - started,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    for label, passed in checks.items():
        print(f"CHECK {label}: {'PASS' if passed else 'FAIL'}")
    if not all(checks.values()):
        raise SystemExit(1)
    print("CYCLE826_COMPANION_ENDPOINT_CYCLE719_HISTORY_INTERFACE_BOUNDED_PASS")


if __name__ == "__main__":
    main()
