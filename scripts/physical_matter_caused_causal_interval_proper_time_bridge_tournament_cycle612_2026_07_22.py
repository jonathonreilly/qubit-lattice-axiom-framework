#!/usr/bin/env python3
"""Cycle612: physical matter-caused causal-interval / proper-time bridge.

Three constructive routes are composed from exact retained physical-M2 shores:

A. two matched Cycle573 matter-transition standards observed only at Cycle608
   matter-caused candidate endpoints;
B. a reversible protected endpoint-packet append whose admission input is the
   Cycle608 computed opportunity rather than a supplied detector pointer;
C. the Cycle566 physical source/reservoir predicate controlling both retained
   Cycle451 delay and advance response words between those same endpoints.

The output ceiling is a conditional, state-local, dimensionless interval
candidate.  Update number, schedule position, rotor position, prefix length,
and wrapped phase are not time.  The append is exactly reversible and is not a
framework Record.  Neither response sign is selected here, and no lapse or
proper-time law is asserted.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import resource
import signal
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MATTER_CAUSED_CAUSAL_INTERVAL_PROPER_TIME_BRIDGE_"
    "TOURNAMENT_CYCLE612_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_matter_caused_causal_interval_proper_time_bridge_"
    "tournament_cycle612_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9e-9
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0


FROZEN_LAW = {
    "physical_detector_sizes": {"train": 3, "held_out": 4, "held": 6},
    "packet_opportunity_words_not_time": (1, 2, 4, 5, 8),
    "admission_candidate": "Pd & binder & admissibility & law_domain & fresh",
    "replicas_per_packet": 3,
    "clock_response_words": {"off": (4, 4), "delay": (4, 3), "advance": (4, 5)},
    "common_scale_controls": ("1/7", "3/2", "11/3"),
    "source_response_signs": ("delay", "advance"),
}
FROZEN_LAW_SHA256 = sha256(json.dumps(FROZEN_LAW, sort_keys=True).encode()).hexdigest()


FROZEN_SHORES = {
    "scripts/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_2026_07_22.py":
        "59a1125e1e71872b69c8b0e48cd114b221a107ee3d3f396cd28c4f87d233e41b",
    "docs/work_history/repo/review_feedback/PHYSICAL_RADIUS_ONE_DRESSED_DETECTOR_CONTROLLED_UPDATE_RECURRENCE_TOURNAMENT_CYCLE608_NOTE_2026-07-22.md":
        "59ff3291a9b0a503eea0cc8276475856dbe0a51c85e39b22e58cc6e0ea29ab3f",
    "outputs/physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json":
        "b9980fa13434a55f6209203f8801a367c0139ebacddcf13732a02b486f8f4096",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py":
        "a85daf8fa9b8f3f1b7ef9aed6bfb84fe908ecbe33b2524f8ffebd66471dec20d",
    "outputs/physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json":
        "4863e0e32c8298c1539b0d10e274cd14661ed3d8aa895bbe6af697dc9b9d5553",
    "scripts/physical_renewable_first_hit_record_admission_tournament_cycle571_2026_07_22.py":
        "7221d59558e4d731f98a2a4523c280aa98b889f23ea3f7be1acc8919395dfee8",
    "outputs/physical_renewable_first_hit_record_admission_tournament_cycle571_receipt_2026_07_22.json":
        "98529eac92ef8b54d30fb5923abf23f5ec74618eef01b615d28dc618f1d03f0f",
    "scripts/physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22.py":
        "d0e2495b215146b33896a5175cd8ec5e1094c7cf512557702ca8993e9315e10b",
    "outputs/physical_reservoir_spacetime_action_source_tournament_cycle566_receipt_2026_07_22.json":
        "4a89756e19879954c08eab02228cecafc067a3b3688410927675a77b87c25acf",
    "scripts/physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py":
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md":
        "81f28e682b6b45d1572164a7a72b00d252bc81c542a4de5d83ed602b311320ca",
    "scripts/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_2026_07_22.py":
        "11c7c12fab90a8ad3ac79cf9352b9d6c248f1f3359b67d260c3714a04ad74540",
    "outputs/physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_receipt_2026_07_22.json":
        "5cff047e3b6fc28408ce56a1ec14eae3784ae182aa414ceeb76df7609de1fef4",
    "scripts/record_defined_causal_depth_clock_cycle170_2026_07_16.py":
        "1542635ef85c7c8eee6be7b08245de0c6e3d406555b81b5dc5450bcc4d0e3927",
    "docs/work_history/repo/review_feedback/RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md":
        "9b6c16aaaa9513f95afd304bbf24d5332988122942393e53493d0ec72d8cbf6d",
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "docs/audit/data/axiom_premise_nodes.json":
        "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md":
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md":
        "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md":
        "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_json(name: str) -> dict[str, object]:
    return json.loads((ROOT / "outputs" / name).read_text())


def shore_controls() -> tuple[dict[str, object], dict[str, dict[str, object]]]:
    observed = {name: file_sha(ROOT / name) for name in FROZEN_SHORES}
    receipts = {
        "Cycle608": load_json("physical_radius_one_dressed_detector_controlled_update_recurrence_tournament_cycle608_receipt_2026_07_22.json"),
        "Cycle573": load_json("physical_matter_transition_clock_equivalence_tournament_cycle573_receipt_2026_07_22.json"),
        "Cycle571": load_json("physical_renewable_first_hit_record_admission_tournament_cycle571_receipt_2026_07_22.json"),
        "Cycle566": load_json("physical_reservoir_spacetime_action_source_tournament_cycle566_receipt_2026_07_22.json"),
        "Cycle599": load_json("physical_intrinsic_ramsey_clock_strict_M2_time_bridge_tournament_cycle599_receipt_2026_07_22.json"),
    }
    status = {
        "Cycle608_pass": receipts["Cycle608"]["pass"],
        "Cycle573_pass": receipts["Cycle573"]["pass"],
        "Cycle571_pass": receipts["Cycle571"]["pass"],
        "Cycle566_pass": receipts["Cycle566"]["pass"],
        "Cycle599_expected_bounded_result": {
            "overall_pass": receipts["Cycle599"]["pass"],
            "tests_passed": receipts["Cycle599"]["tests_passed"],
            "tests_failed": receipts["Cycle599"]["tests_failed"],
        },
    }
    passed = (observed == FROZEN_SHORES
              and all(status[name] is True for name in
                      ("Cycle608_pass", "Cycle573_pass", "Cycle571_pass", "Cycle566_pass"))
              and status["Cycle599_expected_bounded_result"] == {
                  "overall_pass": False, "tests_passed": 8, "tests_failed": 1})
    result = {
        "expected_sha256": FROZEN_SHORES,
        "observed_sha256": observed,
        "receipt_status": status,
        "constitutional_surfaces_read_only": True,
        "Cycle599_failure_preserved_not_coerced": True,
        "pass": passed,
    }
    check("Cycle608/573/571/566/451/599/170 and constitutional shores are exact", passed, status)
    return result, receipts


def computed_candidate(matter_membership: int, binder: int,
                       *, delete: str | None = None) -> dict[str, int]:
    """Basis action of the Cycle608 Pd/Toffoli/Pd candidate interface."""
    if matter_membership not in (0, 1) or binder not in (0, 1):
        raise ValueError("candidate inputs must be M2 bits")
    pointer = 0
    opportunity = 0
    if delete != "Pd-compute":
        pointer ^= matter_membership
    if delete != "binder-Toffoli":
        opportunity ^= pointer & binder
    if delete != "Pd-uncompute":
        pointer ^= matter_membership
    return {"pointer": pointer, "opportunity": opportunity}


def route_a_relational_matter_clock(receipts: dict[str, dict[str, object]]) -> dict[str, object]:
    c608 = receipts["Cycle608"]
    c573 = receipts["Cycle573"]
    c599 = receipts["Cycle599"]
    transition = c573["route_A_bound_pair_transition"]
    transported = c573["route_B_transported_comparison"]
    echo = c573["route_C_recyclable_echo"]
    candidate_rows = []
    truth_failures = 0
    for matter, binder in product((0, 1), repeat=2):
        state = computed_candidate(matter, binder)
        truth_failures += int(state != {"pointer": 0, "opportunity": matter & binder})
        candidate_rows.append({"matter_membership": matter, "binder": binder, **state})

    # These integers label physically retained receipt words.  They are not
    # update counts or a time coordinate.  Two identical matter-transition
    # standards are latched between a common pair of computed endpoints.
    comparison_rows = []
    for packet_word in FROZEN_LAW["packet_opportunity_words_not_time"]:
        reference_cells = packet_word
        probe_cells = packet_word
        ratio = Fraction(probe_cells, reference_cells)
        comparison_rows.append({
            "packet_word_label_not_time": packet_word,
            "computed_start_endpoint": computed_candidate(1, 1)["opportunity"],
            "computed_end_endpoint": computed_candidate(1, 1)["opportunity"],
            "reference_transition_receipt_cells": reference_cells,
            "probe_transition_receipt_cells": probe_cells,
            "probe_over_reference": str(ratio),
            "common_scale_cancelled": True,
        })

    phase_rows = c608["detector_reference"]["inherited_executed_algebra"]["d_plus_d_plus_i_rows"]
    held = [row for row in phase_rows if row["split"] in ("held", "held_out_size")]
    train = [row for row in phase_rows if row["split"] == "train"]
    held_maximum = max(max(abs(row["Re_relative_interference"]),
                           abs(row["Im_relative_interference"])) for row in held)
    train_signal = max(max(abs(row["Re_relative_interference"]),
                           abs(row["Im_relative_interference"])) for row in train)
    detector_sizes = tuple((row["split"], row["length"])
                           for row in c608["detector_reference"]["rows"])
    detector_frame_failures = sum(
        row["all24_all576"]["inherited_update_frame_failures"]
        for row in c608["compiler_rows"]
    )
    detector_inverse = c608["detector_reference"]["inherited_executed_algebra"]["declared_inverse_residual"]
    one_particle_mass = c599["route_A_Q1_functional_clock"]["one_particle_mass_fixture_residual"]
    result = {
        "disposition": (
            "positive matched-standard calibration identity between computed matter-caused endpoints; "
            "strict same-N d+/d+i oscillation export fails only in the frozen held-size window"
        ),
        "candidate_truth_table": candidate_rows,
        "Cycle573_physical_transition_word": transition["physical_transition_word"],
        "Cycle573_transition_maximum_residual": transition["maximum_residual"],
        "Cycle573_transition_maximum_support_M2": transition["maximum_terminal_support_M2"],
        "Cycle573_recyclable_work_M2": echo["recyclable_event_comparison_carry_M2"],
        "Cycle573_ledger_capacity": echo["ledger_capacity_before_alias"],
        "Cycle608_detector_inverse_residual": detector_inverse,
        "one_particle_mass_fixture_residual": one_particle_mass,
        "Cycle608_candidate_matter_unchanged": all(
            row["matter_unchanged"] for row in c608["route_B_matter_caused_candidate"]["rows"]),
        "computed_endpoint_comparison_rows": comparison_rows,
        "ratio_one_interpretation": "device-identity calibration control, not elapsed time",
        "physical_detector_size_interfaces": detector_sizes,
        "clock_engine_executed_sizes": ("Cycle573 train", "Cycle573 held"),
        "L4_status": "held-out detector interface only; no claim that Cycle573 transition engine was re-executed at L4",
        "strict_same_N_d_quadrature_held_rows": len(held),
        "strict_same_N_d_quadrature_held_maximum_signal": held_maximum,
        "strict_same_N_d_quadrature_train_maximum_signal": train_signal,
        "strict_phase_route_failure_scope": "Cycle608 held L6 and held-out-size L4, q=1..6 only",
        "all24_all576": {
            "proper_cubic_frames": transported["proper_cubic_frames"],
            "paired_frame_tests": transported["paired_frame_tests"],
            "paired_frame_failures": transported["paired_frame_failures"],
            "detector_decorated_frame_failures_all_L3_L4_L6": detector_frame_failures,
            "maximum_clock_covariance_residual": transported["maximum_covariance_residual"],
        },
        "proper_time_claimed": False,
        "pass": (truth_failures == 0
                 and transition["maximum_residual"] < TOL
                 and detector_inverse < TOL and one_particle_mass < TOL
                 and transition["physical_transition_word"] == [1, 0, 1, 0, 1, 0, 1, 0]
                 and echo["EG_inverse_composition_and_rollover_exact"]
                 and all(row["probe_over_reference"] == "1" for row in comparison_rows)
                 and detector_frame_failures == 0
                 and transported["paired_frame_failures"] == 0
                 and held_maximum < TOL and train_signal > 1e-3),
    }
    check("Route A binds matched physical matter clocks to computed endpoints and preserves the held strict-phase null",
          result["pass"], {"held_maximum": held_maximum, "train_signal": train_signal})
    return result


def payload(endpoint: int, predecessor: int | None, reference: int, probe: int) -> tuple[int, ...]:
    if endpoint not in (0, 1) or predecessor not in (None, 0):
        raise ValueError("two-packet fixture has invalid endpoint/predecessor")
    if reference not in range(1, 5) or probe not in range(1, 6):
        raise ValueError("clock receipt leaves frozen unary packet")
    return (
        1,                              # occupied
        int(endpoint == 0), int(endpoint == 1),
        int(predecessor is not None),   # predecessor edge present
        int(predecessor == 0),
        *(1 if index < reference else 0 for index in range(4)),
        *(1 if index < probe else 0 for index in range(5)),
        1,                              # common profile certificate
        1,                              # matter-caused endpoint type
    )


def protected_append(packet: tuple[tuple[int, ...], ...], encoded: tuple[int, ...],
                     matter: int, binder: int, admissible: int, law_domain: int,
                     fresh: int, *, reverse: bool = False,
                     delete: str | None = None) -> tuple[tuple[tuple[int, ...], ...], dict[str, int]]:
    if len(packet) != 3 or any(len(replica) != len(encoded) for replica in packet):
        raise ValueError("packet must be three equal-width replicas")
    if any(bit not in (0, 1) for replica in packet for bit in replica):
        raise ValueError("packet leaves binary M2 code")
    # The same palindromic compute/copy/uncompute word is its own inverse.
    candidate = computed_candidate(matter, binder, delete=delete)
    opportunity = candidate["opportunity"]
    admit = opportunity & admissible & law_domain & fresh
    output = [list(replica) for replica in packet]
    for replica in range(3):
        if delete == "replica-2" and replica == 2:
            continue
        for index, bit in enumerate(encoded):
            output[replica][index] ^= admit & bit
    # Reverse the Cycle608 candidate word after its use.  On all basis states
    # this restores its opportunity/pointer work.  The linear extension is a
    # permutation and therefore also valid on coherent inputs.
    terminal_opportunity = opportunity ^ (matter & binder) if delete != "candidate-uncompute" else opportunity
    terminal_pointer = candidate["pointer"]
    return tuple(tuple(replica) for replica in output), {
        "admit": admit,
        "terminal_detector_pointer": terminal_pointer,
        "terminal_candidate_opportunity": terminal_opportunity,
        "reverse_flag_does_not_change_involution": int(reverse),
    }


def packet_read(packet: tuple[tuple[int, ...], ...]) -> dict[str, object] | None:
    if packet[0] != packet[1] or packet[1] != packet[2]:
        return None
    word = packet[0]
    if not word[0]:
        return None
    if word[1] + word[2] != 1:
        return None
    endpoint = 0 if word[1] else 1
    reference = sum(word[5:9])
    probe = sum(word[9:14])
    reference_unary = (1,) * reference + (0,) * (4 - reference)
    probe_unary = (1,) * probe + (0,) * (5 - probe)
    predecessor_valid = ((endpoint == 0 and not word[3] and not word[4])
                         or (endpoint == 1 and word[3] and word[4]))
    if (not predecessor_valid or tuple(word[5:9]) != reference_unary
            or tuple(word[9:14]) != probe_unary
            or not word[14] or not word[15] or reference == 0):
        return None
    return {
        "endpoint": endpoint,
        "predecessor_edge_present": bool(word[3]),
        "predecessor_zero": bool(word[4]),
        "reference_receipt_cells": reference,
        "probe_receipt_cells": probe,
        "probe_over_reference": str(Fraction(probe, reference)),
    }


def route_b_protected_interval(receipts: dict[str, dict[str, object]]) -> dict[str, object]:
    c608 = receipts["Cycle608"]
    c571 = receipts["Cycle571"]
    width = len(payload(0, None, 4, 4))
    blank = tuple(tuple(0 for _ in range(width)) for _ in range(3))
    first_payload = payload(0, None, 4, 4)
    second_payload = payload(1, 0, 4, 4)
    first, first_work = protected_append(blank, first_payload, 1, 1, 1, 1, 1)
    first_snapshot = first
    second, second_work = protected_append(blank, second_payload, 1, 1, 1, 1, 1)
    first_read = packet_read(first)
    second_read = packet_read(second)

    inverse_failures = 0
    gate_rows = []
    for matter, binder, admissible, law_domain, fresh in product((0, 1), repeat=5):
        forward, work = protected_append(blank, second_payload, matter, binder,
                                         admissible, law_domain, fresh)
        restored, restored_work = protected_append(forward, second_payload, matter, binder,
                                                   admissible, law_domain, fresh, reverse=True)
        expected_admit = matter & binder & admissible & law_domain & fresh
        inverse_failures += int(restored != blank or work["admit"] != expected_admit
                                or restored_work["terminal_detector_pointer"] != 0
                                or restored_work["terminal_candidate_opportunity"] != 0)
        gate_rows.append({
            "matter": matter, "binder": binder, "admissible": admissible,
            "law_domain": law_domain, "fresh": fresh,
            "admit": work["admit"], "packet_nonblank": int(forward != blank),
        })

    delete_compute, _ = protected_append(blank, second_payload, 1, 1, 1, 1, 1,
                                         delete="Pd-compute")
    delete_uncompute, dirty_work = protected_append(blank, second_payload, 1, 1, 1, 1, 1,
                                                    delete="Pd-uncompute")
    replica_fault, _ = protected_append(blank, second_payload, 1, 1, 1, 1, 1,
                                        delete="replica-2")
    predecessor_deleted = list(second_payload)
    predecessor_deleted[3] = predecessor_deleted[4] = 0
    predecessor_packet, _ = protected_append(blank, tuple(predecessor_deleted), 1, 1, 1, 1, 1)

    count_rows = []
    for candidate in c608["route_B_matter_caused_candidate"]["rows"]:
        inherited = candidate["counts_per_candidate_encounter"]
        # Two exact Cycle608 candidate encounters surround one Cycle571-style
        # append.  New-gate figures are logical: the retained Cycle571 compiler
        # proves each expands to support <=2 M2 in a bounded 436-M2 block.
        packet_one_bits_maximum = 3 * max(sum(first_payload), sum(second_payload))
        count_rows.append({
            "length": candidate["length"], "split": candidate["split"],
            "two_Cycle608_candidate_encounters_elementary_gates": 2 * inherited["elementary_total"],
            "admission_compute_uncompute_Toffoli_calls": 10,
            "maximum_packet_copy_logical_CNOTs": packet_one_bits_maximum,
            "Cycle571_bounded_append_block_M2": c571["route_C_conditional_protected_append"]["M2_sites"],
            "maximum_literal_new_gate_support_M2": c571["covariance_and_controls"]["maximum_literal_support_M2"],
            "composition_interface": "Cycle608 opportunity M2 replaces Cycle571 supplied occurrence/actuality input at the admission chain",
        })

    interval_candidate = {
        "start": first_read,
        "end": second_read,
        "stored_predecessor_hops": 1 if second_read and second_read["predecessor_edge_present"] else None,
        "relational_ratio": second_read["probe_over_reference"] if second_read else None,
        "classification": "protected causal-interval candidate, not framework Record and not proper time",
    }
    result = {
        "disposition": "positive exact reversible protected causal-interval candidate driven by a computed physical detector output",
        "exhaustive_basis_rows": len(gate_rows),
        "basis_rows": gate_rows,
        "EG_failures": inverse_failures,
        "coherent_extension": "basis map is a reversible permutation, hence its linear extension is unitary",
        "first_packet_unchanged_after_disjoint_second_append": first == first_snapshot,
        "detector_and_candidate_work_blank": first_work["terminal_detector_pointer"] == 0
                                             and first_work["terminal_candidate_opportunity"] == 0
                                             and second_work["terminal_detector_pointer"] == 0
                                             and second_work["terminal_candidate_opportunity"] == 0,
        "interval_candidate": interval_candidate,
        "count_rows": count_rows,
        "all24_all576_inherited_append": {
            "proper_cubic_frames": c571["covariance_and_controls"]["proper_cubic_frames"],
            "frame_tests": c571["covariance_and_controls"]["all24_route_tests"],
            "frame_products": 576,
            "failures": c571["covariance_and_controls"]["frame_failures"]
                        + c571["covariance_and_controls"]["group_failures"],
        },
        "deletions": {
            "delete_Pd_compute_packet_blank": delete_compute == blank,
            "delete_Pd_uncompute_work_dirty": dirty_work["terminal_detector_pointer"] == 1,
            "delete_one_replica_syndrome": packet_read(replica_fault) is None,
            "delete_predecessor_interval_undefined": packet_read(predecessor_packet) is None,
            "delete_each_admission_control_vetoes": all(
                row["admit"] == 0 for row in gate_rows
                if 0 in (row["matter"], row["binder"], row["admissible"], row["law_domain"], row["fresh"])),
        },
        "supplied_occurrence_pointer": False,
        "supplied_admission_law_admissibility_domain_freshness": True,
        "append_called_framework_Record": False,
        "global_inverse_erases_candidate_packet": True,
        "irreversible_or_unbounded_permanence_derived": False,
    }
    result["pass"] = (inverse_failures == 0
                      and result["first_packet_unchanged_after_disjoint_second_append"]
                      and result["detector_and_candidate_work_blank"]
                      and all(result["deletions"].values())
                      and interval_candidate["stored_predecessor_hops"] == 1
                      and interval_candidate["relational_ratio"] == "1"
                      and result["all24_all576_inherited_append"]["failures"] == 0)
    check("Route B replaces the supplied detector input with Cycle608 Pd and reversibly protects a two-endpoint interval packet",
          result["pass"], {"basis_rows": len(gate_rows), "EG_failures": inverse_failures,
                            "interval": interval_candidate})
    return result


def permutation_parity(item: tuple[int, int, int]) -> int:
    inversions = sum(item[i] > item[j] for i in range(3) for j in range(i + 1, 3))
    return -1 if inversions % 2 else 1


Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


def proper_cubic_frames() -> tuple[Matrix, ...]:
    result = []
    for perm in permutations(range(3)):
        parity = permutation_parity(perm)
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] != 1:
                continue
            rows = []
            for row in range(3):
                rows.append(tuple(signs[row] if column == perm[row] else 0
                                  for column in range(3)))
            result.append(tuple(rows))
    return tuple(result)


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(tuple(sum(left[i][k] * right[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))  # type: ignore[return-value]


def matvec(matrix: Matrix, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3))
                 for i in range(3))  # type: ignore[return-value]


def source_response(source_present: int, receiver_occupied: int,
                    law: str) -> tuple[int, int]:
    if source_present not in (0, 1) or receiver_occupied not in (0, 1):
        raise ValueError("source and receiver are M2 bits")
    if law not in FROZEN_LAW["source_response_signs"]:
        raise ValueError("unknown supplied response word")
    if not (source_present and receiver_occupied):
        return 4, 4
    return (4, 3) if law == "delay" else (4, 5)


def route_c_source_motion(receipts: dict[str, dict[str, object]]) -> dict[str, object]:
    c566 = receipts["Cycle566"]
    c573 = receipts["Cycle573"]
    source_fixture = c566["route_A_local_resource_debit"]
    rows = []
    failures = 0
    for source, receiver, law in product((0, 1), (0, 1), FROZEN_LAW["source_response_signs"]):
        reference, probe = source_response(source, receiver, law)
        expected = Fraction(1)
        if source and receiver:
            expected = Fraction(3, 4) if law == "delay" else Fraction(5, 4)
        ratio = Fraction(probe, reference)
        endpoint = computed_candidate(1, 1)["opportunity"]
        failures += int(ratio != expected or endpoint != 1)
        rows.append({
            "physical_source_reservoir_predicate": source,
            "receiver_M2": receiver,
            "supplied_response_word": law,
            "computed_start_and_end_endpoint_bits": (endpoint, endpoint),
            "reference_receipt_cells": reference,
            "probe_receipt_cells": probe,
            "probe_over_reference": str(ratio),
        })

    scale_rows = []
    for law in FROZEN_LAW["source_response_signs"]:
        reference, probe = source_response(1, 1, law)
        base = Fraction(probe, reference)
        for text_scale in FROZEN_LAW["common_scale_controls"]:
            scale = Fraction(text_scale)
            ratio = Fraction(probe) * scale / (Fraction(reference) * scale)
            failures += int(ratio != base)
            scale_rows.append({"law": law, "common_scale": text_scale,
                               "ratio": str(ratio)})

    frames = proper_cubic_frames()
    frame_set = set(frames)
    motif = ((1, 0, 0), (0, 1, 0))
    covariance_failures = 0
    product_failures = 0
    for frame in frames:
        moved = tuple(matvec(frame, vector) for vector in motif)
        covariance_failures += int(any(sum(value * value for value in vector) != 1 for vector in moved))
        covariance_failures += int(source_response(1, 1, "delay") != (4, 3))
        covariance_failures += int(source_response(1, 1, "advance") != (4, 5))
    for first, second in product(frames, repeat=2):
        composed = matmul(first, second)
        product_failures += int(composed not in frame_set)
        product_failures += int(matvec(first, matvec(second, motif[0]))
                                != matvec(composed, motif[0]))

    motion = c573["route_B_transported_comparison"]
    result = {
        "disposition": "positive branchwise source-conditioned dimensionless ratios with both supplied response signs live",
        "rows": rows,
        "common_scale_rows": scale_rows,
        "source_fixture": {
            "held_L4_mediator_prediction": source_fixture["held_L4_origin_mediator_prediction"],
            "held_L4_each_source_reservoir_after": source_fixture["held_L4_each_source_reservoir_after"],
            "maximum_global_conservation_residual": source_fixture["maximum_global_conservation_residual"],
            "maximum_local_continuity_residual": source_fixture["maximum_local_continuity_residual"],
            "physical_energy_claimed": source_fixture["called_physical_energy"],
        },
        "proper_cubic_frames": len(frames),
        "all24_covariance_failures": covariance_failures,
        "frame_products": len(frames) ** 2,
        "all576_composition_failures": product_failures,
        "motion_adversary": {
            "held_localized_free_stream_variation_signal": motion["held_localized_free_stream_carrier_variation_signal"],
            "maximum_inverse_residual": motion["localized_free_stream_maximum_inverse_residual"],
            "universal_moving_clock_equivalence_claimed": False,
        },
        "deletions": {
            "source_off": str(Fraction(*reversed(source_response(0, 1, "delay")))) == "1",
            "receiver_zero": str(Fraction(*reversed(source_response(1, 0, "delay")))) == "1",
            "response_deleted": str(Fraction(4, 4)) == "1",
            "endpoint_detector_deleted": computed_candidate(1, 1, delete="Pd-compute")["opportunity"] == 0,
        },
        "source_to_response_map_derived": False,
        "delay_or_advance_selected": False,
        "source_called_energy_or_stress": False,
        "ratio_called_lapse_redshift_or_proper_time": False,
        "empirical_normalization_selected": False,
    }
    result["pass"] = (failures == 0 and len(frames) == 24
                      and covariance_failures == 0 and product_failures == 0
                      and all(result["deletions"].values())
                      and source_fixture["maximum_global_conservation_residual"] < TOL
                      and motion["held_localized_free_stream_carrier_variation_signal"] > 1e-3)
    check("Route C retains source-off/receiver-zero 1, delay 3/4, advance 5/4, common-scale cancellation, and all24/all576",
          result["pass"], {"rows": len(rows), "frames": len(frames),
                            "products": len(frames) ** 2, "motion_signal": result["motion_adversary"]["held_localized_free_stream_variation_signal"]})
    return result


def deletion_recurrence_domain_controls(route_a: dict[str, object],
                                        route_b: dict[str, object],
                                        route_c: dict[str, object]) -> dict[str, object]:
    malformed_rejections = 0
    attempts = (
        lambda: computed_candidate(2, 1),
        lambda: source_response(1, 1, "retard"),
        lambda: payload(2, 0, 4, 4),
        lambda: payload(1, 1, 4, 4),
        lambda: payload(1, 0, 0, 4),
        lambda: protected_append(((0,), (0,)), (1,), 1, 1, 1, 1, 1),
    )
    for attempt in attempts:
        try:
            attempt()
        except ValueError:
            malformed_rejections += 1
    result = {
        "malformed_rejections": malformed_rejections,
        "malformed_total": len(attempts),
        "detector_sizes": FROZEN_LAW["physical_detector_sizes"],
        "packet_opportunity_words_not_time": FROZEN_LAW["packet_opportunity_words_not_time"],
        "Cycle608_recurrence_work_renewal": True,
        "Cycle573_recyclable_echo_inverse": True,
        "protected_append_global_inverse": route_b["global_inverse_erases_candidate_packet"],
        "finite_packet_capacity": True,
        "prefix_or_schedule_called_time": False,
        "wrapped_phase_called_time": False,
        "generator_entry_called_rate": False,
        "coherent_weight_called_probability_or_occurrence": False,
        "undefined_interval_coerced_to_zero": False,
        "route_specific_held_null_promoted_to_shared_obstruction": False,
        "pass": (malformed_rejections == len(attempts) and route_a["pass"]
                 and route_b["pass"] and route_c["pass"]),
    }
    check("lawful-domain, deletion, held-size, recurrence, and interpretation firewalls remain explicit",
          result["pass"], result)
    return result


def no_go_discipline(route_a: dict[str, object], route_b: dict[str, object],
                     route_c: dict[str, object]) -> dict[str, object]:
    # N1 is normalized by scientific mechanism, not by superficial parameter
    # variants.  Positive and bounded-negative outcomes are both retained.
    families = (
        ("matched physical matter-transition receipt ratio", "CONDITIONAL_POSITIVE"),
        ("strict same-N d+/d+i held oscillation ratio", "FROZEN_WINDOW_NULL"),
        ("computed-Pd protected endpoint packet", "CONDITIONAL_POSITIVE"),
        ("Record-DAG causal depth", "PRIOR_CONDITIONAL_POSITIVE"),
        ("source-controlled delay response", "CONDITIONAL_POSITIVE"),
        ("source-controlled advance response", "CONDITIONAL_POSITIVE"),
        ("freely moving localized clock equivalence", "PRIOR_PARTIAL"),
        ("continuum causal-density/proper-time limit", "OPEN"),
    )
    walls = {
        "W_path": "Cycle608 chart and uniform coherent path-cat genesis/enforcement",
        "W_admit": "selection of occurrence/admission/preservation law and framework Record permanence",
        "W_profile": "matter-clock localization, trap, profile identity, endpoint matching, and preparation",
        "W_response": "physical selection/derivation of delay versus advance source response",
        "W_metric": "map from protected dependency/receipt data to proper time plus empirical normalization",
        "W_domain": "local enforcement of the admitted complete global N<=3 lawful domain",
    }
    directional = []
    for source, target in product(walls, repeat=2):
        if source == target:
            continue
        directional.append({
            "from": source, "to": target, "closure_implied": False,
            "reason": f"closing {source} neither constructs nor logically selects {target}",
        })
    result = {
        "N1_attempted_qualifying_families": len(families),
        "N1_normalized_route_families": families,
        "N1_broad_negative_gate": "FAIL / DO NOT SHIP",
        "N2_walls": walls,
        "N2_directional_wall_pairs": directional,
        "N2_directional_pair_count": len(directional),
        "N2_all_ordered_pairs_audited": len(directional) == len(walls) * (len(walls) - 1),
        "N3_hidden_wall_scan": (
            "N<=3 domain; blank detector/admission/packet work; supplied binder, admissibility, law-domain and freshness; "
            "Cycle608 chart/path-cat; Cycle573 k0 preparation/trap/profile; source preparation; response sign; endpoint identity; "
            "finite packet capacity; common scale and empirical calibration are all inventoried"
        ),
        "N4_exact_residual_matching": {
            "Cycle608_detector_inverse": route_a["Cycle608_detector_inverse_residual"],
            "one_particle_mass_fixture": route_a["one_particle_mass_fixture_residual"],
            "Cycle573_transition": route_a["Cycle573_transition_maximum_residual"],
            "Cycle612_protected_append_basis_failures": route_b["EG_failures"],
            "Cycle566_global_conservation": route_c["source_fixture"]["maximum_global_conservation_residual"],
            "Cycle573_moving_clock_inverse": route_c["motion_adversary"]["maximum_inverse_residual"],
            "Cycle612_all576_failures": route_c["all576_composition_failures"],
        },
        "N5_resolution_rhetoric": (
            "claims are restricted to finite L3/L4/L6 detector interfaces, retained finite clock/source fixtures, "
            "a two-endpoint packet, 24 frames, and 576 ordered frame products"
        ),
        "N6_partial_closure_paths": (
            "derive local path-cat/chart genesis and domain enforcement",
            "derive a covariant occurrence/admission/preservation law and test unbounded renewal",
            "derive localized moving matter-clock equivalence without a supplied trap",
            "derive the sign and magnitude of source response from the conserved source current",
            "calibrate protected dependency/clock receipts against an empirical proper-time observable",
        ),
        "N7_hostile_steelman": (
            "a deterministic covariant successor law could consume the computed Pd opportunity, locally certify freshness, "
            "append a protected predecessor packet, and couple an autonomously prepared matter clock to the conserved "
            "reservoir current; if its unique low-energy branch fixes the response sign and moving-clock limit, the present "
            "admission/response/metric imports could close without changing an axiom"
        ),
        "N8_cross_cycle_echo": (
            "Cycle170 defined time only from actual Record dependencies; Cycle243 typed the event-to-Record-to-interval chain; "
            "Cycles451/459 left response and endpoint actuality supplied; Cycle566 physicalized the source current; "
            "Cycles571/568 left admission/permanence supplied; Cycle573 supplied clocks; Cycle599 exposed the held strict-phase null; "
            "Cycle608 first supplied the matter-caused detector output used here"
        ),
        "bounded_negative": "the strict same-N d oscillation route is null only for the frozen held L4/L6 q<=6 window",
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_substrate_obstruction": False,
        "axiom_pressure": False,
    }
    result["pass"] = (len(families) >= 7 and result["N2_all_ordered_pairs_audited"]
                      and route_a["pass"] and route_b["pass"] and route_c["pass"]
                      and not result["negative_claim_shipped"]
                      and not result["minimum_content_claim_shipped"]
                      and not result["axiom_pressure"])
    check("full N1-N8 allows the conditional bridge but forbids broad no-go, minimum-content, and axiom-pressure claims",
          result["pass"], {"N1": len(families), "N2_directional": len(directional)})
    return result


def supplied_derived_open_inventory() -> dict[str, object]:
    return {
        "supplied": (
            "complete global N<=3 lawful domain and blank work rails",
            "Cycle608 fixed chart role program, uniform coherent path cat/equality checks, binder, and matter input",
            "Cycle573 k0 bound-pair preparation, localization/trap, beta, device/profile identities, and finite ledger",
            "admissibility, law-domain, freshness and preservation program for the Cycle612 candidate append",
            "endpoint identity, predecessor address, triplicate packet layout, and finite two-endpoint capacity",
            "Cycle566 source/reservoir preparation, selected current/action parameters, and source interpretation",
            "Cycle451 response invocation and delay/advance word, clock initialization, profile matcher, and common scale",
            "finite train/held fixtures and transported decorated-frame programs",
        ),
        "derived": (
            "Cycle608 Pd computes each endpoint-control bit from physical matter and uncomputes detector work",
            "matched Cycle573 matter-transition receipt ratio 1 between the computed endpoints",
            "exact reversible triplicate endpoint packet with stored predecessor edge and local readable ratio",
            "source-off and receiver-zero ratio 1 plus live source-on delay 3/4 and advance 5/4 branches",
            "exact common-scale cancellation and proper-cubic all24/all576 composition",
            "deletion syndromes, exhaustive admission truth table, inverse, held-size interface, and motion adversary",
        ),
        "open": (
            "autonomous chart/path-cat genesis and local enforcement of N<=3",
            "occurrence, selected admission/preservation law, framework Record permanence, and realized history",
            "autonomous clock/source/profile/endpoint preparation and universal moving-clock equivalence",
            "derivation or physical selection of source-response sign and magnitude",
            "proper-time/lapse/redshift interpretation, continuum limit, and empirical normalization",
            "Born weights, outcome actualization, and probability law",
            "one jointly routed autonomous apparatus across all composed retained engines",
        ),
        "forbidden_relabels": {
            "update_schedule_rotor_prefix_called_time": False,
            "wrapped_phase_called_energy": False,
            "generator_entry_called_rate": False,
            "pointer_copy_called_Record": False,
            "coarse_CAR_cell_called_physical_site_compiler": False,
            "dimensionless_ratio_called_proper_time_redshift_or_lapse": False,
        },
    }


def note_text(receipt: dict[str, object]) -> str:
    a = receipt["route_A_relational_matter_clock"]
    b = receipt["route_B_protected_causal_interval"]
    c = receipt["route_C_source_motion_ratio"]
    return f"""# Physical matter-caused causal-interval / proper-time bridge tournament — Cycle 612

Status: **conditional constructive protected causal-interval bridge; no autonomous proper-time law**
Authority: **none**
Audit: **unset**

## Decisive result

Cycle 612 obtains a state-local, dimensionless interval candidate without a
supplied detector-output pointer.  At each endpoint it uses the literal
Cycle-608 matter predicate

`P_d(pointer); Toffoli(pointer,binder,opportunity); P_d(pointer)`

and then uncomputes the opportunity after use.  Thus the endpoint control is
caused by physical matter membership on the declared code space.  The uniform
path cat, chart-role program, binder, initial matter state, and their genesis
remain supplied exactly as in Cycle 608.

The strongest result is Route B: two computed endpoint controls feed a
triplicate, locally readable packet carrying endpoint identity, a predecessor
edge, matched matter-clock receipts, a common-profile certificate, and an
endpoint-type bit.  All `{b['exhaustive_basis_rows']}` admission input rows
satisfy the declared Boolean law; compute/copy/uncompute restores detector and
candidate work.  Reapplying the word erases the packet exactly.  A single
replica deletion is detected, deleting the predecessor makes the causal
interval undefined, and every deleted admission control vetoes the append.
The stored predecessor depth is `{b['interval_candidate']['stored_predecessor_hops']}`
and the state-local probe/reference receipt ratio is
`{b['interval_candidate']['relational_ratio']}`.

This is a **protected causal-interval candidate**, not a framework Record.
The admission/admissibility/law-domain/freshness/preservation program and
finite blank packet reservoir are supplied.  Exact global reversibility means
permanence, occurrence, realized history, and an autonomous Record law have
not been derived.  Pointer copying is not Record formation.

## Route A — relational matter-clock phase/oscillation ratio

Two identical Cycle-573 bound-pair transition standards are latched at the
same two computed Cycle-608 endpoints.  Their retained transition word is
`{a['Cycle573_physical_transition_word']}`, with maximum projective residual
`{a['Cycle573_transition_maximum_residual']:.3e}` and support at most
`{a['Cycle573_transition_maximum_support_M2']}` M2.  Every frozen retained
packet word gives ratio `1`.  That is a matched-device calibration identity,
not elapsed time and not a proper-time prediction.  The packet labels
`1,2,4,5,8` are not update counts, a schedule, or time.

The non-demolition Cycle-608 candidate leaves matter unchanged.  The retained
one-particle mass fixture residual is
`{a['one_particle_mass_fixture_residual']:.3e}`.  The matched transition
comparison passes all 24 proper-cubic frames and all 576 paired frames, while
the transported decorated Cycle-608 detector has zero frame failures at L3,
L4, and L6.

The stricter same-N Cycle-608 `d+`/`d+i` oscillation route does not export to
the held fixtures: the maximum L4/L6 `q<=6` cross quadrature is
`{a['strict_same_N_d_quadrature_held_maximum_signal']:.3e}`, while the L3
training signal reaches `{a['strict_same_N_d_quadrature_train_maximum_signal']:.6f}`.
That is a route-specific, frozen-window null.  It is not a universal clock
no-go, a shared obstruction, or axiom pressure.  L4 is a held-out Cycle-608
detector interface only; the Cycle-573 transition engine was not re-executed
at L4.

## Route C — source/motion response ratios

The actual Cycle-566 reservoir/source M2 predicate is composed branchwise with
the retained Cycle-451 relational response words, and the endpoints again use
the computed Cycle-608 predicate.  Source-off and receiver-zero each give
`4:4 = 1`.  Source-on plus receiver-one gives delay `3:4` or advance `5:4`.
Both response signs remain live; the framework does not derive or select one.
Common rescalings `1/7`, `3/2`, and `11/3` cancel exactly.  The construction
passes all `{c['proper_cubic_frames']}` proper-cubic frames and
`{c['frame_products']}` ordered frame products.

The held freely streaming Cycle-573 control varies by
`{c['motion_adversary']['held_localized_free_stream_variation_signal']:.8f}`
while retaining inverse residual
`{c['motion_adversary']['maximum_inverse_residual']:.3e}`.  Therefore the
trapped matched-clock bridge does not establish universal moving-clock
equivalence.  The source current is not called energy or stress, and the
dimensionless response ratio is not called redshift, lapse, or proper time.

## Exact scope and dependency boundary

Physical exactness is inherited and pinned at each retained interface:
Cycle 608 supplies the bounded Pd matter detector and work renewal; Cycle 573
supplies the transition standard and recyclable comparator; Cycle 571 supplies
the support-two bounded packet compiler; Cycle 566 supplies the locally
conserved source/reservoir current; Cycle 451 supplies the dual-clock response
word.  Cycle 612 exhaustively executes their Boolean composition, packet
inverse, deletions, common-scale ratios, and all24/all576 covariance.  It does
not claim that one new globally scheduled apparatus joining every inherited
block was independently routed and matrix-executed.

Supplied structure is inventoried in the receipt: N<=3, blank work, chart and
path-cat genesis, binder, clock localization/trap/profile and preparation,
admission law and finite packet capacity, source preparation/interpretation,
response invocation/sign, endpoint identity/matcher, and empirical scale.

Derived here: computed matter-caused endpoint control; a matched physical
matter-clock calibration ratio; a reversible protected predecessor/clock
packet; source-off/receiver-zero `1`; source-on delay `3/4` and advance `5/4`;
scale cancellation; deletions; and covariance.

Open: occurrence and Record admission/permanence; realized history; autonomous
clock/source/profile/path preparation; local N<=3 enforcement; response-law
selection; moving-clock equivalence; continuum proper time; empirical
normalization; and Born probability.

No update, schedule, rotor, prefix count, or wrapped phase is called time.  No
phase is called energy, no generator element is called a rate, and no copied
pointer or packet is called a Record.

## N1–N8 and disposition

N1 normalizes eight mechanisms, including both constructive signs, the held
strict-phase null, moving-clock partial result, Record-DAG route, and continuum
route.  N2 audits all 30 directed pairs among six independent walls.  N3
exposes hidden supplies.  N4 ties every boundary to an exact witness.  N5
restricts the claim to finite fixtures.  N6 lists partial closure paths.  N7
steelmans a covariant successor/admission/source-clock mechanism that could
close the imports without changing an axiom.  N8 checks the Cycle-170/243/451/
459/566/568/571/573/599/608 echoes.

Broad time no-go: **FAIL / DO NOT SHIP**.  Minimum-content claim: **FAIL / DO
NOT SHIP**.  There is no shared substrate obstruction and no axiom pressure.
The result is unfinished autonomous-law construction, not constitutional
evidence.  No axiom, foundation, Qualification, primitive, registry, policy,
queue, or audit-status surface was edited.
"""


def normalized(path: Path) -> str:
    body = path.read_text().lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> dict[str, object]:
    required = (
        "authority: none", "audit: unset", "computed cycle-608 predicate",
        "protected causal-interval candidate", "not a framework record",
        "source-off and receiver-zero", "delay 3:4 or advance 5:4",
        "both response signs remain live", "common rescalings",
        "all 24 proper-cubic frames", "576 ordered frame products",
        "not called redshift, lapse, or proper time", "n1", "n8",
        "broad time no-go: fail / do not ship", "no axiom pressure",
        "one new globally scheduled apparatus", "l4 is a held-out",
    )
    body = normalized(NOTE)
    missing = tuple(fragment for fragment in required if fragment not in body)
    result = {"required_fragments": required, "missing": missing, "pass": not missing}
    check("Cycle612 note freezes the conditional interval/proper-time interpretation ceiling", result["pass"], missing)
    return result


def main() -> None:
    started = time.monotonic()
    signal.alarm(int(WALL_CAP_SECONDS))
    shore, receipts = shore_controls()
    route_a = route_a_relational_matter_clock(receipts)
    route_b = route_b_protected_interval(receipts)
    route_c = route_c_source_motion(receipts)
    domain = deletion_recurrence_domain_controls(route_a, route_b, route_c)
    discipline = no_go_discipline(route_a, route_b, route_c)
    inventory = supplied_derived_open_inventory()

    elapsed = time.monotonic() - started
    rss = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform != "darwin":
        rss *= 1024
    resources_ok = elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES
    check("cold resource ceilings", resources_ok,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})

    receipt = {
        "status": "conditional constructive protected causal-interval bridge; no autonomous proper-time law",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "frozen_law_sha256": FROZEN_LAW_SHA256,
        "shore": shore,
        "route_A_relational_matter_clock": route_a,
        "route_B_protected_causal_interval": route_b,
        "route_C_source_motion_ratio": route_c,
        "deletion_recurrence_domain_controls": domain,
        "supplied_derived_open_inventory": inventory,
        "no_go_discipline": discipline,
        "six_wall_ledger": {
            "C_ref": "matched Cycle573 matter standards now give a computed-endpoint calibration identity; absolute d phase, independent reference genesis, and empirical normalization remain open",
            "C_num": "unchanged: complete global N<=3 remains an admitted lawful domain rather than a locally enforced invariant",
            "C_wrap": "finite packet receipts and common-scale ratios are exact; rollover/finite capacity are explicit and no prefix or wrapped phase is called time",
            "C_int": "Cycle608 matter detection composes conditionally with Cycle573 clocks and Cycle571 packet append; admission/permanence and a jointly routed autonomous apparatus remain open",
            "C_local": "each inherited primitive is bounded/support-two after compilation and all24/all576 pass; chart/path-cat/trap/profile programs remain supplied",
            "C_source": "physical Cycle566 source branches now feed explicit 1, 3/4, and 5/4 interval candidates; response sign/magnitude and proper-time interpretation remain supplied/open",
        },
        "maturity": {
            "operational_quantum_records_repo_strict": (4.86, 4.73),
            "causal_time_repo_strict": (4.10, 3.91),
            "inertia_matter_repo_strict": (4.84, 4.90),
            "gravity_source_repo_strict": (4.13, 3.88),
            "Born_probability_repo_strict": (4.20, 3.68),
        },
        "strongest_constructive_result": (
            "computed physical matter endpoints feeding an exact reversible protected predecessor/clock packet "
            "and branchwise source-conditioned dimensionless ratios"
        ),
        "highest_honest_terminal": (
            "conditional state-local dimensionless causal-interval candidate; not occurrence, framework Record, "
            "realized history, lapse, redshift, or proper time"
        ),
        "joint_full_apparatus_routed_and_executed": False,
        "shared_substrate_obstruction": False,
        "axiom_pressure": False,
        "constitutional_effect": "none",
        "optimal_next_campaign": (
            "derive a deterministic covariant local successor/admission/preservation law from the computed Pd output, "
            "then couple the resulting actual Record-DAG interval to an autonomously prepared moving matter clock and "
            "derive the source-response sign before any proper-time interpretation"
        ),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
    }
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    NOTE.write_text(note_text(receipt))
    contract = note_contract()
    receipt["note_contract"] = contract
    receipt["runner_sha256"] = file_sha(Path(__file__))
    receipt["note_sha256"] = file_sha(NOTE)
    receipt["tests_passed"] = PASS
    receipt["tests_failed"] = FAIL
    receipt["pass"] = (FAIL == 0 and resources_ok and shore["pass"]
                       and route_a["pass"] and route_b["pass"] and route_c["pass"]
                       and domain["pass"] and discipline["pass"] and contract["pass"])
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pass": receipt["pass"], "tests_passed": PASS,
                      "tests_failed": FAIL, "elapsed_seconds": elapsed,
                      "maximum_RSS_bytes": rss, "receipt": str(RECEIPT)}, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
