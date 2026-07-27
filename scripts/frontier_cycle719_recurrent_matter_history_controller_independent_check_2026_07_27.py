#!/usr/bin/env python3
"""Independent check of the Cycle-719 Cycle713 -> H^130 composition.

Usage:
  python3 this_file.py /path/to/route-a/worktree/scripts

This checker does not accept the host ``run_orbit`` call as execution evidence:
it applies the literal 61,562-gate controller word 130 times to every matter
branch in the frozen origin-0 row.  It also executes compiled deletions.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


SCRIPTS = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as X


K = X.K
P = len(X.PROGRAM)
D = X.M.R12.TOTAL_WIRES
EXPECTED_RUNNER_SHA256 = "063103ae1c6bcfc44aff05200bea0c932a50e018b78f2b67ca90feec28c5aac2"


def apply_word(value, word):
    output = value
    for gate in word:
        if gate.kind == "X":
            output ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            output ^= ((output >> gate.wires[0]) & 1) << gate.wires[1]
        elif gate.kind == "TOF":
            controls = (
                ((output >> gate.wires[0]) & 1)
                & ((output >> gate.wires[1]) & 1)
            )
            output ^= controls << gate.wires[2]
        else:
            raise ValueError(gate.kind)
    return output


def apply_orbit(before, word):
    state = before
    for _ in range(P):
        state = apply_word(state, word)
    return state


def controller_rows():
    full = K.controller_word(X.PROGRAM, D)
    banks, links = X.B.chain_genesis(X.BANKS)
    initial = X.tuple_to_int(X.M.pack_state(banks, links, matter=1))
    matter = X.C713.apply_sparse_word({initial: 1.0 + 0.0j}, X.MATTER_WORD)
    branch_rows = []
    full_outputs = {}
    for basis in matter:
        before = basis | (1 << D)
        actual = apply_orbit(before, full)
        expected, a, b, _trace = K.run_orbit(X.int_to_tuple(basis), X.PROGRAM)
        data_mask = (1 << D) - 1
        a_word = (actual >> D) & ((1 << P) - 1)
        b_word = (actual >> (D + P)) & ((1 << P) - 1)
        work_word = (actual >> (D + 2 * P)) & ((1 << P) - 1)
        row = {
            "pointer": (basis >> X.R3_SOURCE_POINTER()) & 1,
            "data_equal_run_orbit": (actual & data_mask) == X.tuple_to_int(expected),
            "expected_token_return": tuple(i for i, value in enumerate(a) if value) == (0,)
            and not any(b),
            "compiled_A0_return": a_word == 1,
            "compiled_B_vacuum": b_word == 0,
            "compiled_work_clean": work_word == 0,
        }
        branch_rows.append(row)
        full_outputs[basis] = actual

    inverse_failures = sum(
        apply_orbit(full_outputs[basis], tuple(reversed(full)))
        != (basis | (1 << D))
        for basis in matter
    )

    packet_program = list(X.PROGRAM)
    packet_index = next(
        i for i, row in enumerate(packet_program) if row[0] == "bank"
    )
    packet_program[packet_index] = ("identity", 0, ())
    packet_word = K.controller_word(tuple(packet_program), D)
    final_program = list(X.PROGRAM)
    final_index = next(i for i, row in enumerate(final_program) if row[0] == "finalizer")
    final_program[final_index] = ("identity", 0, ())
    final_word = K.controller_word(tuple(final_program), D)
    endpoint_basis = next(basis for basis in matter if (basis >> X.R3_SOURCE_POINTER()) & 1)
    endpoint_before = endpoint_basis | (1 << D)
    endpoint_full = full_outputs[endpoint_basis]
    packet_deleted = apply_orbit(endpoint_before, packet_word)
    final_deleted = apply_orbit(endpoint_before, final_word)
    data_mask = (1 << D) - 1
    return {
        "matter_branches": len(matter),
        "branch_rows": branch_rows,
        "one_H_semantic_gates": len(full),
        "full_orbit_H_applications": P,
        "full_orbit_semantic_gate_applications": P * len(full),
        "actual_inverse_failures": inverse_failures,
        "packet_delete_full_state_changed": packet_deleted != endpoint_full,
        "packet_delete_data_bits_changed": (
            (packet_deleted ^ endpoint_full) & data_mask
        ).bit_count(),
        "finalizer_delete_full_state_changed": final_deleted != endpoint_full,
        "finalizer_delete_data_bits_changed": (
            (final_deleted ^ endpoint_full) & data_mask
        ).bit_count(),
    }


def physical_rows():
    layout = X.M.R12.full_wire_layout()
    caps = X.source_physical_caps(layout)
    controller = K.physical_controller_certificate(X.BANKS)
    source_pointer = layout["source_wire_sites"][X.R3_SOURCE_POINTER()]
    endpoint_pointer = tuple(caps["landed"]["pointer_sites"])[2]
    return {
        "decoded_matter_gates": len(X.MATTER_WORD),
        "source_pointer_index": X.R3_SOURCE_POINTER(),
        "source_pointer_M2": source_pointer,
        "endpoint_pointer_M2": endpoint_pointer,
        "all_pointer_sites_equal": tuple(caps["landed"]["pointer_sites"])
        == tuple(layout["source_wire_sites"][38:41]),
        "pointer_binding_equal": source_pointer == endpoint_pointer,
        "source_cap_physical_primitives": len(caps["word"]),
        "source_cap_routed_NN_gates": len(caps["routed"]),
        "one_H_physical_primitives": controller["forward"]["physical_primitives"],
        "one_H_routed_NN_gates": controller["forward"]["routed_NN_gates"],
        "full_G_physical_primitives": len(caps["word"])
        + P * controller["forward"]["physical_primitives"],
        "full_G_routed_NN_gates": len(caps["routed"])
        + P * controller["forward"]["routed_NN_gates"],
        "route_failures": sum(
            caps[direction][key]
            for direction in ("route", "inverse_route")
            for key in ("non_NN_failures", "operand_order_failures", "route_return_failures")
        ) + sum(
            controller[direction][key]
            for direction in ("forward", "inverse")
            for key in ("non_NN_failures", "operand_order_failures", "route_return_failures")
        ),
        "controller_covariance_scope": "passive coordinate/group/translation roundtrips only",
        "joint_active_covariance_executed": False,
        "route_deletion_opportunities_are_executed_deletions": False,
    }


def main():
    controller = controller_rows()
    physical = physical_rows()
    checks = {
        "actual_92_gate_matter_word": physical["decoded_matter_gates"] == 92,
        "actual_H130_all_six_branches": (
            controller["matter_branches"] == 6
            and all(
                all(value for key, value in row.items() if key != "pointer")
                for row in controller["branch_rows"]
            )
        ),
        "actual_compiled_inverse": controller["actual_inverse_failures"] == 0,
        "actual_compiled_deletions": (
            controller["packet_delete_full_state_changed"]
            and controller["packet_delete_data_bits_changed"] == 35
            and controller["finalizer_delete_full_state_changed"]
            and controller["finalizer_delete_data_bits_changed"] == 3
        ),
        "same_pointer_site_binding": (
            physical["all_pointer_sites_equal"] and physical["pointer_binding_equal"]
        ),
        "literal_routes": physical["route_failures"] == 0,
        "scope_firewall": (
            not physical["joint_active_covariance_executed"]
            and not physical["route_deletion_opportunities_are_executed_deletions"]
        ),
    }
    observed_runner_sha256 = sha256(Path(X.__file__).read_bytes()).hexdigest()
    checks["attacked_runner_pin"] = observed_runner_sha256 == EXPECTED_RUNNER_SHA256
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "controller": controller,
        "physical": physical,
        "attacked_runner": str(Path(X.__file__).resolve()),
        "attacked_runner_sha256": observed_runner_sha256,
        "expected_runner_sha256": EXPECTED_RUNNER_SHA256,
        "boundary": (
            "The composed action survives literal H^130 execution on the frozen six-branch row. "
            "This checker does not upgrade passive controller coordinate covariance to active "
            "law covariance, and does not treat route deletion opportunities as executed deletions."
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    for name, passed in checks.items():
        print("PASS" if passed else "FAIL", name, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE719_RECURRENT_CONTROLLER_INDEPENDENT_PASS" if report["pass"] else "CYCLE719_RECURRENT_CONTROLLER_INDEPENDENT_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
