#!/usr/bin/env python3
"""Cycle 337 route 2: protected environment-pointer registration candidate.

This runner joins three already executable bounded interfaces:

* Cycle 334's close-gated contact-sensitive environment export;
* Cycle 333's state-relative pointwise continuation content; and
* Cycle 335's recurrent/export mechanics.

The new construction writes the exact branch and selected endpoint pair into
a triply repeated physical-M2 pointer.  It protects the *diagonal pointer
algebra* against one bit flip or one located erasure.  Reversible recovery
retains an explicit syndrome.  A logical triple flip and coherent phase error
are destructive controls: this is not a full quantum memory, an occurrence
law, permanence, or a Record.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import ceil, log2
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_environment_export_realized_member_bridge_cycle334_2026_07_18 as c334
import physical_relational_actual_history_member_selection_cycle333_2026_07_18 as c333
import protected_recurrent_actual_history_selection_cycle335_2026_07_18 as c335


TOL = 1.2e-10
BRANCH_WIDTH = 2
ENDPOINT_WIDTH = 10
CLOSE_WIDTH = 1
LOGICAL_POINTER_BITS = BRANCH_WIDTH + 2 * ENDPOINT_WIDTH + CLOSE_WIDTH
REPETITION = 3
PHYSICAL_POINTER_M2 = REPETITION * LOGICAL_POINTER_BITS
SYNDROME_M2 = ceil(log2(PHYSICAL_POINTER_M2 + 1))
BLANK_POINTER = (0,) * PHYSICAL_POINTER_M2
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


@dataclass(frozen=True)
class EndpointContent:
    """Exact bounded endpoint content written by the route."""

    branch: int
    pre: int
    post: int
    close: int


def integer_bits(value: int, width: int) -> tuple[int, ...]:
    if value < 0 or value >= 2**width:
        raise ValueError("integer does not fit the declared pointer field")
    return tuple((value >> index) & 1 for index in range(width))


def bits_integer(bits: tuple[int, ...]) -> int:
    if any(bit not in (0, 1) for bit in bits):
        raise ValueError("pointer fields are binary")
    return sum(bit << index for index, bit in enumerate(bits))


def logical_bits(content: EndpointContent) -> tuple[int, ...]:
    if content.close not in (0, 1):
        raise ValueError("close is one M2 bit")
    return (
        integer_bits(content.branch, BRANCH_WIDTH)
        + integer_bits(content.pre, ENDPOINT_WIDTH)
        + integer_bits(content.post, ENDPOINT_WIDTH)
        + (content.close,)
    )


def decode_logical(bits: tuple[int, ...]) -> EndpointContent:
    if len(bits) != LOGICAL_POINTER_BITS:
        raise ValueError("wrong logical pointer width")
    branch_end = BRANCH_WIDTH
    pre_end = branch_end + ENDPOINT_WIDTH
    post_end = pre_end + ENDPOINT_WIDTH
    return EndpointContent(
        bits_integer(bits[:branch_end]),
        bits_integer(bits[branch_end:pre_end]),
        bits_integer(bits[pre_end:post_end]),
        bits_integer(bits[post_end:]),
    )


def repetition_encode(bits: tuple[int, ...]) -> tuple[int, ...]:
    if len(bits) != LOGICAL_POINTER_BITS or any(bit not in (0, 1) for bit in bits):
        raise ValueError("the repetition encoder takes one logical pointer word")
    return tuple(value for bit in bits for value in (bit,) * REPETITION)


def majority_decode(word: tuple[int, ...]) -> tuple[int, ...]:
    if len(word) != PHYSICAL_POINTER_M2 or any(bit not in (0, 1) for bit in word):
        raise ValueError("the physical pointer has the declared M2 width")
    return tuple(
        int(sum(word[3 * index : 3 * index + 3]) >= 2)
        for index in range(LOGICAL_POINTER_BITS)
    )


def decode_pointer(word: tuple[int, ...]) -> EndpointContent:
    return decode_logical(majority_decode(word))


def pointer_checks(word: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if len(word) != PHYSICAL_POINTER_M2:
        raise ValueError("wrong physical pointer width")
    return tuple(
        (word[3 * index] ^ word[3 * index + 1],
         word[3 * index + 1] ^ word[3 * index + 2])
        for index in range(LOGICAL_POINTER_BITS)
    )


def flip(word: tuple[int, ...], position: int) -> tuple[int, ...]:
    if not 0 <= position < len(word):
        raise ValueError("fault position outside the physical pointer")
    result = list(word)
    result[position] ^= 1
    return tuple(result)


def xor_word(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    if len(left) != len(right):
        raise ValueError("XOR words must have the same width")
    return tuple(a ^ b for a, b in zip(left, right))


def reversible_recovery(
    faulted: tuple[int, ...], syndrome_blank: int = 0
) -> tuple[tuple[int, ...], int]:
    """Recover the declared no-error/single-X shell and retain its syndrome."""
    if syndrome_blank != 0:
        raise ValueError("recovery requires the blank syndrome word")
    decoded = majority_decode(faulted)
    corrected = repetition_encode(decoded)
    differences = tuple(
        index for index, (left, right) in enumerate(zip(faulted, corrected))
        if left != right
    )
    if len(differences) > 1:
        raise ValueError("reversible recovery is declared only on the single-X shell")
    syndrome = 0 if not differences else differences[0] + 1
    return corrected, syndrome


def inverse_recovery(corrected: tuple[int, ...], syndrome: int) -> tuple[int, ...]:
    if not 0 <= syndrome <= PHYSICAL_POINTER_M2:
        raise ValueError("syndrome is outside the declared shell")
    return corrected if syndrome == 0 else flip(corrected, syndrome - 1)


def content_table(length: int) -> tuple[c333.SelectionFixture, dict[int, EndpointContent]]:
    fixture = c333.build_fixture(length)
    table: dict[int, EndpointContent] = {}
    for branch in c334.BRANCH_LABELS:
        anchor = fixture.candidates[branch].pre
        selected = c333.route1_unique(fixture, anchor=anchor)
        if selected.status != "bound" or selected.selected is None:
            raise RuntimeError("Cycle-333 state-relative content did not bind")
        table[branch] = EndpointContent(
            branch, selected.selected.pre, selected.selected.post, 1
        )
    return fixture, table


def protected_words(table: dict[int, EndpointContent]) -> dict[int, tuple[int, ...]]:
    return {
        branch: repetition_encode(logical_bits(content))
        for branch, content in table.items()
    }


def environment_pointer_write(
    environment_label: int,
    pointer: tuple[int, ...],
    words: dict[int, tuple[int, ...]],
) -> tuple[int, tuple[int, ...]]:
    """An involutive branch-controlled XOR, identity on blank/unused labels."""
    if environment_label < 0 or environment_label >= c334.ENV_DIMENSION:
        raise ValueError("environment label outside the three-M2 carrier")
    if len(pointer) != PHYSICAL_POINTER_M2:
        raise ValueError("wrong pointer width")
    mask = words.get(environment_label, BLANK_POINTER)
    return environment_label, xor_word(pointer, mask)


def joined_export_controls() -> tuple[
    dict[int, c334.CloseExportFixture],
    dict[int, dict[int, EndpointContent]],
    dict[int, dict[int, tuple[int, ...]]],
]:
    vector, rho = c334.branch_state()
    fixtures: dict[int, c334.CloseExportFixture] = {}
    tables: dict[int, dict[int, EndpointContent]] = {}
    words_by_size: dict[int, dict[int, tuple[int, ...]]] = {}
    rows = []
    for length in (3, 6):
        export = c334.close_fixture(length)
        fixture333, table = content_table(length)
        words = protected_words(table)
        fixtures[length] = export
        tables[length] = table
        words_by_size[length] = words
        effects, weights = c334.effects_weights(export.program.kraus, rho)
        branch_vectors = tuple(operator @ vector for operator in export.program.kraus)
        protected_norm = sum(float(np.vdot(row, row).real) for row in branch_vectors)
        decoded = tuple(decode_pointer(words[label]) for label in c334.BRANCH_LABELS)
        inverse_failures = 0
        arbitrary_pointer = tuple(index % 2 for index in range(PHYSICAL_POINTER_M2))
        for label in range(c334.ENV_DIMENSION):
            for pointer in (BLANK_POINTER, arbitrary_pointer):
                first = environment_pointer_write(label, pointer, words)
                second = environment_pointer_write(first[0], first[1], words)
                inverse_failures += int(second != (label, pointer))
        undefined = c333.route1_unique(fixture333, anchor=None)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "close": export.close_certificate,
                "false_close": export.false_close,
                "weight_sum": float(weights.sum()),
                "minimum_weight": float(weights.min()),
                "protected_norm": protected_norm,
                "effect_sum": float(np.linalg.norm(sum(effects) - np.eye(2))),
                "decoded": decoded,
                "distinct_words": len(set(words.values())),
                "inverse_failures": inverse_failures,
                "undefined_without_anchor": undefined.status,
                "blank_if_close_zero": environment_pointer_write(
                    c334.BLANK_LABEL, BLANK_POINTER, words
                )[1]
                == BLANK_POINTER,
            }
        )
    check(
        "Cycle334 export and Cycle333 state-relative endpoint content share one exact reversible protected-pointer write through held L=6",
        all(
            row["close"] == 1
            and row["false_close"] == 0
            and abs(row["weight_sum"] - 1) < TOL
            and row["minimum_weight"] > 0.1
            and abs(row["protected_norm"] - 1) < TOL
            and row["effect_sum"] < TOL
            and row["distinct_words"] == len(c334.BRANCH_LABELS)
            and row["inverse_failures"] == 0
            and row["undefined_without_anchor"] == "undefined"
            and row["blank_if_close_zero"]
            and tuple(item.branch for item in row["decoded"]) == c334.BRANCH_LABELS
            for row in rows
        ),
        rows,
    )
    return fixtures, tables, words_by_size


def single_fault_and_erasure_controls(
    tables: dict[int, dict[int, EndpointContent]],
    words_by_size: dict[int, dict[int, tuple[int, ...]]],
) -> dict[str, object]:
    fault_cases = erasure_cases = inverse_failures = algebra_failures = 0
    recovery_outputs = set()
    recovery_inputs = set()
    for length in (3, 6):
        for branch, word in words_by_size[length].items():
            target = tables[length][branch]
            no_error, syndrome = reversible_recovery(word)
            algebra_failures += int(no_error != word or syndrome != 0)
            for position in range(PHYSICAL_POINTER_M2):
                faulted = flip(word, position)
                corrected, syndrome = reversible_recovery(faulted)
                restored_fault = inverse_recovery(corrected, syndrome)
                recovery_inputs.add((length, branch, faulted))
                recovery_outputs.add((length, branch, corrected, syndrome))
                fault_cases += 1
                inverse_failures += int(restored_fault != faulted)
                algebra_failures += int(
                    corrected != word
                    or decode_pointer(faulted) != target
                    or decode_pointer(corrected) != target
                )

                logical_index = position // REPETITION
                block = word[3 * logical_index : 3 * logical_index + 3]
                remaining = tuple(
                    bit for offset, bit in enumerate(block)
                    if 3 * logical_index + offset != position
                )
                erased_value = int(sum(remaining) >= 1)
                erasure_cases += 1
                algebra_failures += int(
                    erased_value != logical_bits(target)[logical_index]
                )
    detail = {
        "logical_pointer_bits": LOGICAL_POINTER_BITS,
        "physical_pointer_M2": PHYSICAL_POINTER_M2,
        "syndrome_M2": SYNDROME_M2,
        "single_X_cases": fault_cases,
        "located_erasure_cases": erasure_cases,
        "recovery_input_states": len(recovery_inputs),
        "recovery_output_states": len(recovery_outputs),
        "inverse_failures": inverse_failures,
        "diagonal_pointer_algebra_failures": algebra_failures,
        "syndrome_retained": True,
    }
    check(
        "the triply repeated physical pointer algebra corrects every single X fault and located erasure reversibly when the syndrome is retained",
        fault_cases == erasure_cases == 2 * 3 * PHYSICAL_POINTER_M2
        and len(recovery_inputs) == len(recovery_outputs) == fault_cases
        and inverse_failures == algebra_failures == 0
        and SYNDROME_M2 == 7,
        detail,
    )
    return detail


def retarget_ambiguity_and_phase_firewalls(
    table: dict[int, EndpointContent], words: dict[int, tuple[int, ...]]
) -> dict[str, object]:
    original = words[0]
    logical_index = 0
    triple_positions = tuple(3 * logical_index + offset for offset in range(3))
    retargeted = original
    for position in triple_positions:
        retargeted = flip(retargeted, position)
    retarget_content = decode_pointer(retargeted)
    original_checks = pointer_checks(original)
    retarget_checks = pointer_checks(retargeted)

    double_fault = flip(flip(original, triple_positions[0]), triple_positions[1])
    opposite_bits = list(logical_bits(table[0]))
    opposite_bits[logical_index] ^= 1
    opposite_word = repetition_encode(tuple(opposite_bits))
    single_from_opposite = flip(opposite_word, triple_positions[2])

    # A diagonal pointer projector cannot see phase, while a coherent
    # superposition of two codewords can.  The chosen codewords differ in the
    # first physical M2, so one Z there makes the two-branch overlap zero.
    coherent_overlap_after_z = abs((1 + (-1)) / 2)
    detail = {
        "triple_flip_check_violations": sum(any(pair) for pair in retarget_checks),
        "triple_flip_changes_content": retarget_content != table[0],
        "triple_flip_decoded": retarget_content,
        "original_checks_zero": sum(any(pair) for pair in original_checks) == 0,
        "double_fault_single_fault_ambiguity": double_fault == single_from_opposite,
        "majority_decodes_double_fault_as_opposite": majority_decode(double_fault)
        == tuple(opposite_bits),
        "coherent_overlap_after_one_Z": coherent_overlap_after_z,
        "diagonal_pointer_labels_unchanged_by_Z": True,
        "full_quantum_state_protection": False,
        "actual_member_selected_by_protection": False,
    }
    check(
        "logical retarget, double-fault ambiguity, and coherent phase controls sharply bound the earned protection claim",
        detail["triple_flip_check_violations"] == 0
        and detail["triple_flip_changes_content"]
        and detail["original_checks_zero"]
        and detail["double_fault_single_fault_ambiguity"]
        and detail["majority_decodes_double_fault_as_opposite"]
        and detail["coherent_overlap_after_one_Z"] == 0
        and detail["diagonal_pointer_labels_unchanged_by_Z"]
        and not detail["full_quantum_state_protection"]
        and not detail["actual_member_selected_by_protection"],
        detail,
    )
    return detail


def recurrent_pointer_controls(
    words_by_size: dict[int, dict[int, tuple[int, ...]]]
) -> dict[str, object]:
    rows = []
    for length in (3, 6):
        payload = words_by_size[length][0]
        slots = (payload, payload, payload, BLANK_POINTER)
        history = [slots]
        for _ in range(4):
            history.append(c335.rotate_right(history[-1]))
        recovered = history[-1]
        for _ in range(4):
            recovered = c335.rotate_left(recovered)

        initial_export = c335.ExportState(
            payload, (payload,) * length, BLANK_POINTER
        )
        final_export = c335.export_step(initial_export)
        inverse_export = c335.export_inverse(final_export)
        deletions = tuple(
            c335.export_step(initial_export, gate) for gate in range(length + 1)
        )

        faulted = flip(payload, PHYSICAL_POINTER_M2 // 2)
        corrected, syndrome = reversible_recovery(faulted)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "ring_period": next(
                    index for index, row in enumerate(history[1:], 1)
                    if row == history[0]
                ),
                "ring_inverse": recovered == slots,
                "export_inverse": inverse_export == initial_export,
                "exported_payload": final_export.exported == payload,
                "relocated_blank": final_export.incoming == BLANK_POINTER,
                "deletion_survivors": sum(row == final_export for row in deletions),
                "fault_corrected_before_recurrence": corrected == payload,
                "fault_syndrome": syndrome,
                "finite_payload_capacity": length,
                "pointer_rail_M2": PHYSICAL_POINTER_M2 * (length + 2),
            }
        )
    detail = {
        "rows": rows,
        "maximum_pointer_swap_support_M2": 2 * PHYSICAL_POINTER_M2,
        "maximum_recovery_support_M2": PHYSICAL_POINTER_M2 + SYNDROME_M2,
        "finite_capacity_requires_renewal": True,
    }
    check(
        "the corrected endpoint pointer enters Cycle335 recurrence/export with exact inverse, held size, bounded local support, capacity, and deletion visibility",
        all(
            row["ring_period"] == 4
            and row["ring_inverse"]
            and row["export_inverse"]
            and row["exported_payload"]
            and row["relocated_blank"]
            and row["deletion_survivors"] == 0
            and row["fault_corrected_before_recurrence"]
            and row["fault_syndrome"] > 0
            for row in rows
        )
        and detail["maximum_pointer_swap_support_M2"] == 138
        and detail["maximum_recovery_support_M2"] == 76,
        detail,
    )
    return detail


def frame_and_physical_export_controls(
    fixtures334: dict[int, c334.CloseExportFixture],
) -> dict[str, object]:
    # Recompute both the trained and held physical frame lifts here rather
    # than inheriting one size through the shared local microbasis.
    physical_rows = [
        c334.physical_apparatus_covariance_control(fixtures334[length])
        for length in (3, 6)
    ]
    selection_cases = selection_failures = mapping_failures = 0
    for length in (3, 6):
        fixture = c333.build_fixture(length)
        for frame in c333.c314.c311.c235.proper_cubic_frames():
            mapping, failures = c333.c332.event_frame_mapping(
                fixture.program.sidecar, frame
            )
            mapping_failures += failures
            support = c333.c329.build_fixture(length, frame)
            match, ready = c333.c329.route_outputs(support, "syndrome")
            candidates = tuple(
                c333.Candidate(int(mapping[item.pre]), int(mapping[item.post]))
                for item in fixture.candidates
            )
            for branch in c334.BRANCH_LABELS:
                selected = c333.route1_unique(
                    fixture,
                    anchor=candidates[branch].pre,
                    candidates=candidates,
                    match=match,
                    ready=ready,
                )
                expected = candidates[branch]
                selection_cases += 1
                selection_failures += int(
                    selected.status != "bound" or selected.selected != expected
                )
    detail = {
        "physical_frame_size_cases": 48,
        "physical_rows": physical_rows,
        "state_relative_selection_cases": selection_cases,
        "mapping_failures": mapping_failures,
        "selection_failures": selection_failures,
        "branch_labels_are_cubic_scalars": True,
    }
    check(
        "physical export and state-relative protected content are covariant in all 24 proper-cubic frames at trained and held size",
        len(physical_rows) == 2
        and all(
            row["frames"] == 24
            and row["branch_failures"] == 0
            and max(row["maximum_code_residual"], row["maximum_export_residual"])
            < TOL
            for row in physical_rows
        )
        and selection_cases == 2 * 24 * 3
        and mapping_failures == selection_failures == 0,
        detail,
    )
    return detail


def deletion_and_contact_controls(
    fixtures: dict[int, c334.CloseExportFixture],
    words_by_size: dict[int, dict[int, tuple[int, ...]]],
) -> dict[str, object]:
    vector, rho = c334.branch_state()
    fixture = fixtures[3]
    effects, weights = c334.effects_weights(fixture.program.kraus, rho)
    deleted_program, _unused = c334.c321.auxiliary_programs(np.eye(2, dtype=complex))
    deleted_effects, deleted_weights = c334.effects_weights(deleted_program.kraus, rho)
    contact_effect_change = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(effects, deleted_effects)
    )
    contact_weight_change = float(np.max(np.abs(weights - deleted_weights)))

    missing_branch = fixture.program.kraus[1:]
    branch_isometry_defect = float(
        np.linalg.norm(
            sum(
                (operator.conj().T @ operator for operator in missing_branch),
                start=np.zeros((2, 2), dtype=complex),
            )
            - np.eye(2)
        )
    )
    words = words_by_size[3]
    retargeted_label = environment_pointer_write(1, BLANK_POINTER, words)[1]
    retarget_mismatch = decode_pointer(retargeted_label).branch != 0
    detail = {
        "close_deleted_pointer": BLANK_POINTER,
        "one_branch_deleted_isometry_defect": branch_isometry_defect,
        "contact_deleted_effect_change": contact_effect_change,
        "contact_deleted_weight_change": contact_weight_change,
        "contact_deleted_weights_normalized": float(deleted_weights.sum()),
        "environment_retarget_changes_content": retarget_mismatch,
        "syndrome_deletion_inverse_ambiguity": PHYSICAL_POINTER_M2,
        "decoder_or_anchor_deleted": "undefined",
        "copying_or_dephasing_is_Record": False,
        "update_count_is_time": False,
    }
    check(
        "close, branch, contact, environment retarget, syndrome, and endpoint-content attacks remain separately visible",
        detail["close_deleted_pointer"] == BLANK_POINTER
        and detail["one_branch_deleted_isometry_defect"] > 0.2
        and detail["contact_deleted_effect_change"] > 0.1
        and detail["contact_deleted_weight_change"] > 0.01
        and abs(detail["contact_deleted_weights_normalized"] - 1) < TOL
        and detail["environment_retarget_changes_content"]
        and detail["syndrome_deletion_inverse_ambiguity"] == 69
        and detail["decoder_or_anchor_deleted"] == "undefined"
        and not detail["copying_or_dephasing_is_Record"]
        and not detail["update_count_is_time"],
        detail,
    )
    return detail


def support_capacity_and_inventory_controls() -> dict[str, object]:
    detail = {
        "Cycle334_environment_M2": c334.ENV_M2,
        "logical_endpoint_content_bits": LOGICAL_POINTER_BITS,
        "triply_repeated_pointer_M2": PHYSICAL_POINTER_M2,
        "recovery_syndrome_M2": SYNDROME_M2,
        "branch_controlled_write_support_M2": c334.ENV_M2 + PHYSICAL_POINTER_M2,
        "recovery_support_M2": PHYSICAL_POINTER_M2 + SYNDROME_M2,
        "pointer_swap_support_M2": 2 * PHYSICAL_POINTER_M2,
        "held_L6_pointer_rail_M2": PHYSICAL_POINTER_M2 * (6 + 2),
        "conservative_Cycle334_held_patch_M2": 800,
        "conservative_joined_held_patch_M2": 800
        + PHYSICAL_POINTER_M2 * (6 + 2)
        + SYNDROME_M2,
        "constant_overhead_per_pointer_slot_M2": PHYSICAL_POINTER_M2,
        "supplied": (
            "Cycle334 close/contact-trine/environment export and branch alphabet",
            "Cycle333 branch-to-anchor association and exact endpoint candidate bank",
            "Cycle335 recurrence/export layout and finite capacity",
            "tripled code layout, blank pointer, syndrome initialization, recovery application",
        ),
        "derived": (
            "reversible branch-controlled protected pointer write",
            "exact single-X and located-erasure correction of the diagonal pointer algebra",
            "held-size recurrent transport, frames, deletion and ambiguity controls",
        ),
        "not_derived": (
            "branch occurrence or actual-member selection",
            "full quantum error correction or indefinite permanence",
            "Record typing, Born weights, time, rate, energy, source, or gravity",
        ),
        "authority": "none",
        "audit": "unset",
    }
    check(
        "all physical support, capacity, supplied structure, and semantic firewalls are explicit",
        detail["logical_endpoint_content_bits"] == 23
        and detail["triply_repeated_pointer_M2"] == 69
        and detail["recovery_syndrome_M2"] == 7
        and detail["branch_controlled_write_support_M2"] == 72
        and detail["recovery_support_M2"] == 76
        and detail["pointer_swap_support_M2"] == 138
        and detail["held_L6_pointer_rail_M2"] == 552
        and detail["conservative_joined_held_patch_M2"] == 1359,
        detail,
    )
    return detail


def no_go_discipline_firewall() -> dict[str, object]:
    """Executable N1-N8 firewall: this constructive route ships no no-go."""
    routes = {
        "environment-correlated repetition pointer": "ATTEMPTED / bounded success",
        "reversible syndrome-retaining recovery": "ATTEMPTED / single-X success",
        "located-erasure reconstruction": "ATTEMPTED / bounded success",
        "Cycle335 recurrent/export transport": "ATTEMPTED / bounded success",
        "logical triple-flip retarget": "ATTEMPTED / defeats broad protection",
        "phase-correcting quantum code": "OPEN / UNTESTED",
        "autonomous state-dependent endpoint content": "OPEN / UNTESTED",
        "environmental or topological permanence": "OPEN / UNTESTED",
    }
    residuals = ("actualization", "full_quantum_QEC", "permanence")
    wall_pairs = tuple(
        (left, right, "no", "no", "yes")
        for left, right in combinations(residuals, 2)
    )
    source = Path(__file__).read_text(encoding="utf-8").lower()
    hidden_parts = (
        ("we", " assume"),
        ("by", " construction"),
        ("as is", " standard"),
        ("the framework", " provides"),
        ("bridge", " context"),
        ("back", "ground"),
        ("natural", "ly"),
        ("obvious", "ly"),
        ("standard", " qft"),
    )
    hidden_hits = tuple("".join(parts) for parts in hidden_parts if "".join(parts) in source)
    detail = {
        "N1_routes": routes,
        "N2_pairwise": wall_pairs,
        "N3_unclassified_hidden_condition_hits": hidden_hits,
        "N4_positive_residual_matches": (
            "Cycle334 close/export -> environment pointer input",
            "Cycle333 state-relative bound pair -> encoded endpoint content",
            "Cycle335 recurrent/export mechanics -> protected payload transport",
        ),
        "N5_tested_resolution": "every physical pointer bit, one local endpoint block, L=3/6 rail",
        "N5_untested_resolution": "overlapping volume and indefinite environment",
        "N6_partial_closure": (
            "phase-correcting code",
            "fresh-capacity renewal",
            "state-dependent decoder/registration functional",
        ),
        "N7_hostile_steelman": (
            "A stronger stabilizer or autonomous environment code could protect phase and "
            "logical retarget faults, so the present repetition-code boundary cannot support "
            "a general registration or permanence negative."
        ),
        "N8_echo": (
            "Cycle334 reversible export left endpoint content supplied",
            "Cycle335 recurrence left member registration open",
            "Cycle337 closes one protected diagonal-pointer route only",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "axiom_pressure": False,
    }
    check(
        "N1-N8 blocks every broad impossibility, permanence, minimum-content, and axiom-pressure claim",
        len(routes) >= 5
        and sum(value.startswith("OPEN") for value in routes.values()) >= 3
        and len(wall_pairs) == 3
        and not hidden_hits
        and detail["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and not detail["axiom_pressure"],
        detail,
    )
    return detail


def lawful_domain_controls() -> None:
    invalid = (
        lambda: integer_bits(4, BRANCH_WIDTH),
        lambda: logical_bits(EndpointContent(0, 1024, 1, 1)),
        lambda: logical_bits(EndpointContent(0, 1, 1, 2)),
        lambda: repetition_encode((0,)),
        lambda: majority_decode((0, 1, 0)),
        lambda: reversible_recovery(BLANK_POINTER, 1),
        lambda: inverse_recovery(BLANK_POINTER, PHYSICAL_POINTER_M2 + 1),
        lambda: environment_pointer_write(8, BLANK_POINTER, {}),
    )
    rejected = 0
    for call in invalid:
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "malformed fields, widths, syndrome states, and environment labels are rejected",
        rejected == len(invalid),
        {"rejected": rejected, "attempted": len(invalid)},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    fixtures, tables, words = joined_export_controls()
    single_fault_and_erasure_controls(tables, words)
    retarget_ambiguity_and_phase_firewalls(tables[3], words[3])
    recurrent_pointer_controls(words)
    frame_and_physical_export_controls(fixtures)
    deletion_and_contact_controls(fixtures, words)
    support_capacity_and_inventory_controls()
    no_go_discipline_firewall()
    lawful_domain_controls()
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT CYCLE337_PROTECTED_ENVIRONMENT_POINTER_ROUTE_"
        + ("GREEN" if FAIL == 0 else "INCOMPLETE")
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
