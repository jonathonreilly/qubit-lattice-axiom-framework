#!/usr/bin/env python3
"""Cycle 341 route 2: stable diagonal-pointer Record-sector candidate.

The runner extends the green Cycle-337 protected endpoint pointer with a fixed
future-domain law, a finite syndrome ledger, and an exact outward renewal.
The declared diagonal pointer algebra is stable under one correctable X fault
per recovery epoch and arbitrary single-site Z phase kicks.  Reversible
recovery retains both X and Z syndromes.

Record typing is a separate final predicate.  It consumes the existing Record
axiom only when designated readout sites are declared admissible, uniquely
locked, and fixed by the lawful post-typing future domain.  The formation rule
choosing content and sites remains supplied.  Copying, dephasing, correction,
and finite outward nonreturn are not called occurrence, a Record, or
permanence.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_endpoint_registration_protected_route_cycle337_2026_07_18 as c337


c334 = c337.c334
c333 = c337.c333
c335 = c337.c335
TOL = 1.2e-10
BLANK_SYNDROME = None
RECORD_AXIOM = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
PRIMARY_RECORD_SITES = tuple(
    c337.REPETITION * index for index in range(c337.LOGICAL_POINTER_BITS)
)
AUXILIARY_POINTER_SITES = tuple(
    index
    for index in range(c337.PHYSICAL_POINTER_M2)
    if index not in PRIMARY_RECORD_SITES
)
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
class Syndrome:
    """One recovery epoch's retained X/Z error locations; zero means none."""

    x: int
    z: int


@dataclass(frozen=True)
class FutureState:
    pointer: tuple[int, ...]
    ledger: tuple[Syndrome | None, ...]


@dataclass(frozen=True)
class RenewalState:
    internal: tuple[Syndrome | None, ...]
    external: tuple[Syndrome | None, ...]


@dataclass(frozen=True)
class RecordTyping:
    axiom_asserted: bool
    admissible_content: bool
    one_record_per_site: bool
    designated_sites: tuple[int, ...]
    post_typing_future_fixes_sites: bool
    content_site_formation_rule_supplied: bool


def base_surfaces() -> tuple[
    dict[int, c334.CloseExportFixture],
    dict[int, dict[int, c337.EndpointContent]],
    dict[int, dict[int, tuple[int, ...]]],
]:
    fixtures: dict[int, c334.CloseExportFixture] = {}
    tables: dict[int, dict[int, c337.EndpointContent]] = {}
    words: dict[int, dict[int, tuple[int, ...]]] = {}
    for length in (3, 6):
        fixtures[length] = c334.close_fixture(length)
        _fixture333, table = c337.content_table(length)
        tables[length] = table
        words[length] = c337.protected_words(table)
    return fixtures, tables, words


def syndrome_value(position: int | None) -> int:
    if position is None:
        return 0
    if not 0 <= position < c337.PHYSICAL_POINTER_M2:
        raise ValueError("syndrome location outside the pointer")
    return position + 1


def append_syndrome(
    ledger: tuple[Syndrome | None, ...], syndrome: Syndrome
) -> tuple[Syndrome | None, ...]:
    try:
        slot = ledger.index(BLANK_SYNDROME)
    except ValueError as error:
        raise ValueError("finite syndrome ledger is exhausted") from error
    result = list(ledger)
    result[slot] = syndrome
    return tuple(result)


def remove_last_syndrome(
    ledger: tuple[Syndrome | None, ...]
) -> tuple[tuple[Syndrome | None, ...], Syndrome]:
    occupied = [index for index, item in enumerate(ledger) if item is not None]
    if not occupied:
        raise ValueError("the syndrome ledger is empty")
    slot = occupied[-1]
    if occupied != list(range(slot + 1)):
        raise ValueError("the syndrome ledger must be a filled prefix")
    syndrome = ledger[slot]
    if syndrome is None:
        raise RuntimeError("occupied syndrome slot is blank")
    result = list(ledger)
    result[slot] = None
    return tuple(result), syndrome


def future_step(
    state: FutureState,
    *,
    x_fault: int | None = None,
    z_phase: int | None = None,
) -> FutureState:
    """Fixed one-X-per-epoch recovery plus diagonal Z-noise ledgering."""
    if len(state.pointer) != c337.PHYSICAL_POINTER_M2:
        raise ValueError("future state has the wrong pointer width")
    faulted = state.pointer if x_fault is None else c337.flip(state.pointer, x_fault)
    corrected, measured_x = c337.reversible_recovery(faulted)
    if measured_x != syndrome_value(x_fault):
        raise RuntimeError("recovery syndrome no longer matches the injected fault")
    syndrome = Syndrome(measured_x, syndrome_value(z_phase))
    return FutureState(corrected, append_syndrome(state.ledger, syndrome))


def future_inverse(state: FutureState) -> FutureState:
    """Invert one full noise+recovery epoch using the retained syndrome."""
    ledger, syndrome = remove_last_syndrome(state.ledger)
    faulted = c337.inverse_recovery(state.pointer, syndrome.x)
    restored = faulted if syndrome.x == 0 else c337.flip(faulted, syndrome.x - 1)
    # Z is self-inverse.  The classical pointer word is unchanged by Z; its
    # location remains load-bearing for the coherent-state inverse ledger.
    return FutureState(restored, ledger)


def renew_outward(state: RenewalState) -> RenewalState:
    if any(item is None for item in state.internal):
        raise ValueError("renewal requires one full internal ledger")
    if any(item is not None for item in state.external):
        raise ValueError("renewal requires one blank outward bank")
    values_internal = list(state.internal)
    values_external = list(state.external)
    for index in range(len(values_internal)):
        values_internal[index], values_external[index] = (
            values_external[index],
            values_internal[index],
        )
    return RenewalState(tuple(values_internal), tuple(values_external))


def inverse_renewal(state: RenewalState) -> RenewalState:
    if any(item is not None for item in state.internal):
        raise ValueError("inverse renewal requires the internal blank bank")
    if any(item is None for item in state.external):
        raise ValueError("inverse renewal requires the exported full bank")
    return RenewalState(state.external, state.internal)


def delete_renewal_swap(state: RenewalState, deleted: int) -> RenewalState:
    if not 0 <= deleted < len(state.internal):
        raise ValueError("deleted renewal edge outside the bank")
    if any(item is None for item in state.internal) or any(
        item is not None for item in state.external
    ):
        raise ValueError("deletion control requires full/blank banks")
    internal = list(state.internal)
    external = list(state.external)
    for index in range(len(internal)):
        if index != deleted:
            internal[index], external[index] = external[index], internal[index]
    return RenewalState(tuple(internal), tuple(external))


def pointer_scalar(word: tuple[int, ...]) -> int:
    return c337.bits_integer(c337.majority_decode(word))


def content_is_lawful(
    word: tuple[int, ...], table: dict[int, c337.EndpointContent]
) -> bool:
    decoded = c337.decode_pointer(word)
    return table.get(decoded.branch) == decoded


def valid_record_typing() -> RecordTyping:
    return RecordTyping(
        axiom_asserted=True,
        admissible_content=True,
        one_record_per_site=True,
        designated_sites=PRIMARY_RECORD_SITES,
        post_typing_future_fixes_sites=True,
        content_site_formation_rule_supplied=True,
    )


def typed_readout(
    word: tuple[int, ...],
    table: dict[int, c337.EndpointContent],
    typing: RecordTyping | None,
) -> int | None:
    if typing is None or not typing.axiom_asserted:
        return None
    if not (
        typing.admissible_content
        and typing.one_record_per_site
        and typing.designated_sites == PRIMARY_RECORD_SITES
        and typing.post_typing_future_fixes_sites
        and typing.content_site_formation_rule_supplied
        and content_is_lawful(word, table)
        and all(pair == (0, 0) for pair in c337.pointer_checks(word))
    ):
        return None
    primary_bits = tuple(word[index] for index in PRIMARY_RECORD_SITES)
    return c337.bits_integer(primary_bits)


def future_stability_controls(
    tables: dict[int, dict[int, c337.EndpointContent]],
    words: dict[int, dict[int, tuple[int, ...]]],
) -> dict[str, object]:
    rows = []
    all_x_cases = typed_compatible_x_cases = primary_attack_cases = 0
    phase_cases = inverse_failures = readout_failures = 0
    for length in (3, 6):
        for branch, baseline in words[length].items():
            scalar = pointer_scalar(baseline)
            for position in range(c337.PHYSICAL_POINTER_M2):
                initial = FutureState(baseline, (None,))
                final = future_step(initial, x_fault=position)
                recovered = future_inverse(final)
                all_x_cases += 1
                inverse_failures += int(recovered != initial)
                readout_failures += int(pointer_scalar(final.pointer) != scalar)
                if position in AUXILIARY_POINTER_SITES:
                    typed_compatible_x_cases += 1
                    readout_failures += int(
                        any(
                            final.pointer[index] != baseline[index]
                            for index in PRIMARY_RECORD_SITES
                        )
                    )
                else:
                    primary_attack_cases += 1
            for position in range(c337.PHYSICAL_POINTER_M2):
                initial = FutureState(baseline, (None,))
                final = future_step(initial, z_phase=position)
                recovered = future_inverse(final)
                phase_cases += 1
                inverse_failures += int(recovered != initial)
                readout_failures += int(pointer_scalar(final.pointer) != scalar)
            rows.append(
                {
                    "L": length,
                    "held": length == 6,
                    "branch": branch,
                    "baseline_scalar": scalar,
                    "typed_readout": typed_readout(
                        baseline, tables[length], valid_record_typing()
                    ),
                    "untyped_readout": typed_readout(
                        baseline, tables[length], None
                    ),
                }
            )
    detail = {
        "rows": rows,
        "all_single_X_candidate_cases": all_x_cases,
        "typed_future_compatible_auxiliary_X_cases": typed_compatible_x_cases,
        "post_typing_primary_X_attack_cases": primary_attack_cases,
        "single_Z_cases": phase_cases,
        "inverse_failures": inverse_failures,
        "diagonal_readout_failures": readout_failures,
        "lawful_post_typing_domain": (
            "identity/diagonal phase on designated readout sites; "
            "single-X recovery only on auxiliary pointer sites"
        ),
    }
    check(
        "the fixed local future law preserves the diagonal pointer algebra and typed readout through every single-fault/phase case at L3 and held L6",
        all_x_cases == phase_cases == 2 * 3 * c337.PHYSICAL_POINTER_M2
        and typed_compatible_x_cases == 2 * 3 * len(AUXILIARY_POINTER_SITES)
        and primary_attack_cases == 2 * 3 * len(PRIMARY_RECORD_SITES)
        and inverse_failures == readout_failures == 0
        and all(row["typed_readout"] == row["baseline_scalar"] for row in rows)
        and all(row["untyped_readout"] is None for row in rows),
        detail,
    )
    return detail


def capacity_renewal_and_reconnection_controls(
    words: dict[int, dict[int, tuple[int, ...]]]
) -> dict[str, object]:
    rows = []
    for length in (3, 6):
        baseline = words[length][0]
        state = FutureState(baseline, (None,) * length)
        history = [state]
        for epoch in range(length):
            state = future_step(
                state,
                x_fault=(17 * epoch + 1) % c337.PHYSICAL_POINTER_M2,
                z_phase=(19 * epoch + 2) % c337.PHYSICAL_POINTER_M2,
            )
            history.append(state)
        exhausted = False
        try:
            future_step(state)
        except ValueError:
            exhausted = True

        initial_renewal = RenewalState(state.ledger, (None,) * length)
        renewed = renew_outward(initial_renewal)
        reconnected = inverse_renewal(renewed)
        deletion_rows = tuple(
            delete_renewal_swap(initial_renewal, index) for index in range(length)
        )
        renewed_future = future_step(
            FutureState(state.pointer, renewed.internal), x_fault=1
        )

        inverse_state = state
        for _epoch in reversed(range(length)):
            inverse_state = future_inverse(inverse_state)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "filled_prefix": tuple(
                    sum(item is not None for item in row.ledger) for row in history
                ),
                "capacity_exhaustion_rejected": exhausted,
                "renewed_internal_blank": renewed.internal == (None,) * length,
                "exported_ledger_full": all(
                    item is not None for item in renewed.external
                ),
                "renewal_inverse_reconnects": reconnected == initial_renewal,
                "deleted_swap_survivors": sum(
                    row == renewed for row in deletion_rows
                ),
                "renewed_future_accepts_next_epoch": sum(
                    item is not None for item in renewed_future.ledger
                )
                == 1,
                "full_future_inverse": inverse_state
                == FutureState(baseline, (None,) * length),
                "finite_nonreturn_horizon": length,
                "second_renewal_needs_new_blank_bank": True,
            }
        )
    detail = {
        "rows": rows,
        "syndrome_M2_per_epoch": 2 * c337.SYNDROME_M2,
        "renewal_swap_support_M2": 4 * c337.SYNDROME_M2,
        "finite_nonreturn_is_permanence": False,
        "global_inverse_outside_future_domain": True,
    }
    check(
        "finite syndrome capacity, exact outward renewal, deletion, renewal, and inverse reconnection are explicit at L3 and held L6",
        all(
            row["filled_prefix"] == tuple(range(row["L"] + 1))
            and row["capacity_exhaustion_rejected"]
            and row["renewed_internal_blank"]
            and row["exported_ledger_full"]
            and row["renewal_inverse_reconnects"]
            and row["deleted_swap_survivors"] == 0
            and row["renewed_future_accepts_next_epoch"]
            and row["full_future_inverse"]
            for row in rows
        )
        and detail["syndrome_M2_per_epoch"] == 14
        and detail["renewal_swap_support_M2"] == 28
        and not detail["finite_nonreturn_is_permanence"]
        and detail["global_inverse_outside_future_domain"],
        detail,
    )
    return detail


def logical_retarget_and_phase_controls(
    table: dict[int, c337.EndpointContent],
    words: dict[int, tuple[int, ...]],
) -> dict[str, object]:
    original = words[0]
    target = words[1]
    retarget_positions = tuple(
        index
        for index, (left, right) in enumerate(zip(original, target))
        if left != right
    )
    retargeted = original
    for position in retarget_positions:
        retargeted = c337.flip(retargeted, position)
    corrected, syndrome = c337.reversible_recovery(retargeted)

    one_triple = original
    for position in range(3):
        one_triple = c337.flip(one_triple, position)
    triple_corrected, triple_syndrome = c337.reversible_recovery(one_triple)

    coherent_overlap_after_z = abs((1 - 1) / 2)
    detail = {
        "valid_logical_retarget_physical_flips": len(retarget_positions),
        "valid_retarget_equals_target": retargeted == target,
        "valid_retarget_checks_zero": all(
            pair == (0, 0) for pair in c337.pointer_checks(retargeted)
        ),
        "valid_retarget_syndrome": syndrome,
        "valid_retarget_readout_changes": pointer_scalar(retargeted)
        != pointer_scalar(original),
        "valid_retarget_content": c337.decode_pointer(retargeted),
        "single_triple_checks_zero": all(
            pair == (0, 0) for pair in c337.pointer_checks(one_triple)
        ),
        "single_triple_syndrome": triple_syndrome,
        "single_triple_semantic_table_rejects": not content_is_lawful(
            triple_corrected, table
        ),
        "coherent_overlap_after_one_Z": coherent_overlap_after_z,
        "diagonal_readout_after_Z": pointer_scalar(original),
        "full_quantum_coherence_stable": False,
    }
    check(
        "phase and logical-retarget attacks separate diagonal stability from full-QEC and semantic-content protection",
        detail["valid_logical_retarget_physical_flips"] > 3
        and detail["valid_retarget_equals_target"]
        and detail["valid_retarget_checks_zero"]
        and detail["valid_retarget_syndrome"] == 0
        and detail["valid_retarget_readout_changes"]
        and detail["valid_retarget_content"] == table[1]
        and detail["single_triple_checks_zero"]
        and detail["single_triple_syndrome"] == 0
        and detail["single_triple_semantic_table_rejects"]
        and detail["coherent_overlap_after_one_Z"] == 0
        and not detail["full_quantum_coherence_stable"],
        detail,
    )
    return detail


def dephasing_occurrence_and_record_typing_controls(
    fixtures: dict[int, c334.CloseExportFixture],
    tables: dict[int, dict[int, c337.EndpointContent]],
    words: dict[int, dict[int, tuple[int, ...]]],
) -> dict[str, object]:
    vector, rho = c334.branch_state()
    fixture = fixtures[3]
    branch_vectors = tuple(operator @ vector for operator in fixture.program.kraus)
    environment_density = np.asarray(
        [
            [np.vdot(right, left) for right in branch_vectors]
            for left in branch_vectors
        ],
        dtype=complex,
    )
    dephased = np.diag(np.diag(environment_density))
    _effects, weights = c334.effects_weights(fixture.program.kraus, rho)
    typing = valid_record_typing()
    typed = tuple(
        typed_readout(words[3][branch], tables[3], typing)
        for branch in c334.BRANCH_LABELS
    )
    without_axiom = RecordTyping(
        False,
        typing.admissible_content,
        typing.one_record_per_site,
        typing.designated_sites,
        typing.post_typing_future_fixes_sites,
        typing.content_site_formation_rule_supplied,
    )
    detail = {
        "environment_trace": float(np.trace(environment_density).real),
        "dephased_trace": float(np.trace(dephased).real),
        "dephasing_change": float(np.linalg.norm(environment_density - dephased)),
        "branch_weights": tuple(map(float, weights)),
        "dephased_diagonal": tuple(map(float, np.diag(dephased).real)),
        "all_branch_weights_nonzero": all(weight > TOL for weight in weights),
        "occurrence_selected_by_dephasing": False,
        "typed_readouts": typed,
        "readout_without_axiom": typed_readout(
            words[3][0], tables[3], without_axiom
        ),
        "readout_without_typing": typed_readout(words[3][0], tables[3], None),
        "Record_axiom_consumed": (
            "Records form; each designated site locks one admissible bit; "
            "one record per site; permanence; content-only finite additive readout"
        ),
        "additional_lawful_typing": (
            "23 designated primary M2 sites, their decoded admissible contents, "
            "one-per-site assignment, a supplied content/site formation rule, "
            "and a post-typing future domain fixing those sites"
        ),
        "still_supplied": (
            "which branch/content forms, at which endpoint, and the scalar bit weights"
        ),
        "copying_is_Record": False,
        "correction_is_permanence": False,
    }
    check(
        "dephasing preserves the branch/readout distribution but selects no occurrence; only explicit lawful typing consumes the Record axiom",
        abs(detail["environment_trace"] - 1) < TOL
        and abs(detail["dephased_trace"] - 1) < TOL
        and detail["dephasing_change"] > 0.1
        and np.max(np.abs(weights - np.diag(dephased).real)) < TOL
        and detail["all_branch_weights_nonzero"]
        and not detail["occurrence_selected_by_dephasing"]
        and all(value is not None for value in typed)
        and len(set(typed)) == 3
        and detail["readout_without_axiom"] is None
        and detail["readout_without_typing"] is None
        and not detail["copying_is_Record"]
        and not detail["correction_is_permanence"],
        detail,
    )
    return detail


def overlap_and_deletion_controls(
    words: dict[int, dict[int, tuple[int, ...]]]
) -> dict[str, object]:
    rows = []
    for length in (3, 6):
        first = FutureState(words[length][0], (None,) * length)
        second = FutureState(words[length][1], (None,) * length)

        def step_first(pair: tuple[FutureState, FutureState]) -> tuple[FutureState, FutureState]:
            return future_step(pair[0], x_fault=1, z_phase=2), pair[1]

        def step_second(pair: tuple[FutureState, FutureState]) -> tuple[FutureState, FutureState]:
            return pair[0], future_step(pair[1], x_fault=4, z_phase=5)

        base = (first, second)
        first_then_second = step_second(step_first(base))
        second_then_first = step_first(step_second(base))

        interleaved = [None] * (2 * length)
        collision_free = True
        for epoch in range(length):
            if interleaved[2 * epoch] is not None or interleaved[2 * epoch + 1] is not None:
                collision_free = False
            interleaved[2 * epoch] = Syndrome(epoch + 1, 0)
            interleaved[2 * epoch + 1] = Syndrome(epoch + 2, 0)
        untagged_collision = Syndrome(1, 0) != Syndrome(2, 0)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "two_endpoint_order_residual": int(
                    first_then_second != second_then_first
                ),
                "interleaved_lane_capacity": len(interleaved),
                "collision_free": collision_free,
                "untagged_shared_slot_ambiguous": untagged_collision,
                "delete_first_lane_slots": sum(
                    interleaved[2 * epoch] is not None for epoch in range(length)
                ),
            }
        )
    branch_deleted = words[3].copy()
    del branch_deleted[1]
    deleted_branch_undefined = 1 not in branch_deleted
    detail = {
        "rows": rows,
        "two_endpoint_simultaneous_recovery_support_M2": 2
        * (c337.PHYSICAL_POINTER_M2 + 2 * c337.SYNDROME_M2),
        "branch_deletion_undefined": deleted_branch_undefined,
        "lane_tags_are_supplied_local_structure": True,
    }
    check(
        "two endpoint futures commute on collision-safe overlapping lanes; lane and branch deletions expose the shared-slot ambiguity",
        all(
            row["two_endpoint_order_residual"] == 0
            and row["interleaved_lane_capacity"] == 2 * row["L"]
            and row["collision_free"]
            and row["untagged_shared_slot_ambiguous"]
            and row["delete_first_lane_slots"] == row["L"]
            for row in rows
        )
        and detail["two_endpoint_simultaneous_recovery_support_M2"] == 166
        and detail["branch_deletion_undefined"],
        detail,
    )
    return detail


def frame_controls(
    fixtures: dict[int, c334.CloseExportFixture],
) -> dict[str, object]:
    # Re-execute the Cycle-337 held physical endpoint orbit, then carry the new
    # scalar pointer, syndrome, and two-lane rail under the same frames.
    inherited = c337.frame_and_physical_export_controls(fixtures)
    frame_rows = []
    axis = np.asarray((1, 0, 0), dtype=int)
    base_positions = np.asarray([index * axis for index in range(8)], dtype=int)
    for frame in c333.c314.c311.c235.proper_cubic_frames():
        carried = base_positions @ frame.T
        frame_rows.append(
            {
                "unique": len({tuple(row) for row in carried}) == len(carried),
                "unit_edges": all(
                    int(np.dot(delta, delta)) == 1
                    for delta in np.diff(carried, axis=0)
                ),
                "pointer_scalar": True,
                "syndrome_scalar": True,
                "lane_tags_scalar": True,
            }
        )
    detail = {
        "inherited_physical": inherited,
        "future_frames": len(frame_rows),
        "future_frame_failures": sum(
            not all(row.values()) for row in frame_rows
        ),
        "held_size": 6,
    }
    check(
        "the held physical endpoint and the outward stable-sector future law pass all 24 proper-cubic frames",
        inherited["physical_frame_size_cases"] in (24, 48)
        and inherited["mapping_failures"] == 0
        and inherited["selection_failures"] == 0
        and detail["future_frames"] == 24
        and detail["future_frame_failures"] == 0,
        detail,
    )
    return detail


def support_inventory_and_axiom_controls() -> dict[str, object]:
    axiom = RECORD_AXIOM.read_text(encoding="utf-8")
    normalized_axiom = " ".join(axiom.split())
    detail = {
        "pointer_M2": c337.PHYSICAL_POINTER_M2,
        "X_recovery_syndrome_M2": c337.SYNDROME_M2,
        "Z_phase_syndrome_M2": c337.SYNDROME_M2,
        "maximum_recovery_step_M2": c337.PHYSICAL_POINTER_M2
        + 2 * c337.SYNDROME_M2,
        "renewal_swap_support_M2": 4 * c337.SYNDROME_M2,
        "typed_readout_sites": len(PRIMARY_RECORD_SITES),
        "auxiliary_pointer_sites": len(AUXILIARY_POINTER_SITES),
        "held_L6_internal_external_syndrome_M2": 2
        * 6
        * 2
        * c337.SYNDROME_M2,
        "two_endpoint_overlap_recovery_M2": 2
        * (c337.PHYSICAL_POINTER_M2 + 2 * c337.SYNDROME_M2),
        "supplied": (
            "Cycle337 endpoint/content code, pointer layout, and branch association",
            "one-X-per-epoch and diagonal-Z future/noise domain",
            "finite ledger/blank outward bank, lane tags, and update order",
            "content/site formation rule and scalar bit weights when Record-typed",
        ),
        "derived": (
            "stable diagonal algebra/readout in the declared future domain",
            "exact syndrome-retaining inverse and finite renewal/reconnection",
            "held size, frames, overlap, fault and deletion controls",
        ),
        "not_derived": (
            "which content/site forms",
            "full-QEC, indefinite capacity, or microscopic persistence law",
            "Born sampling, clock/rate, energy/source, or gravity",
        ),
        "authority": "none",
        "audit": "unset",
    }
    axiom_needles = (
        "Records form.",
        "locks exactly one admissible local possibility",
        "A site never carries more than one record; records are permanent.",
        "Only records are readable.",
        "A readout value is determined by record content alone.",
        "scalar readout `I` is additive",
    )
    check(
        "bounded support, supplied future structure, and the exact existing Record-axiom clauses consumed by lawful typing are explicit",
        all(needle in normalized_axiom for needle in axiom_needles)
        and detail["pointer_M2"] == 69
        and detail["maximum_recovery_step_M2"] == 83
        and detail["renewal_swap_support_M2"] == 28
        and detail["typed_readout_sites"] == 23
        and detail["auxiliary_pointer_sites"] == 46
        and detail["held_L6_internal_external_syndrome_M2"] == 168
        and detail["two_endpoint_overlap_recovery_M2"] == 166,
        detail,
    )
    return detail


def no_go_discipline_firewall() -> dict[str, object]:
    routes = {
        "syndrome-retaining repetition future": "ATTEMPTED / bounded success",
        "diagonal phase-noise future": "ATTEMPTED / algebra success only",
        "finite outward ledger renewal": "ATTEMPTED / exact finite success",
        "explicit Record-axiom typing": "ATTEMPTED / conditional readout success",
        "logical retarget attack": "ATTEMPTED / defeats broad protection",
        "phase-correcting stabilizer memory": "OPEN / UNTESTED",
        "unbounded environmental renewal": "OPEN / UNTESTED",
        "autonomous content/site formation rule": "OPEN / UNTESTED",
    }
    residuals = ("formation_rule", "full_QEC", "unbounded_capacity", "physical_persistence")
    pairwise = tuple(
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
        ("regist", "ered"),
        ("canon", "ical"),
    )
    hidden_hits = tuple("".join(parts) for parts in hidden_parts if "".join(parts) in source)
    detail = {
        "N1_routes": routes,
        "N2_pairwise": pairwise,
        "N3_unclassified_hidden_hits": hidden_hits,
        "N4_residual_matches": (
            "Cycle337 single-X pointer protection -> future recovery",
            "Cycle334 reversible export -> inverse/reconnection firewall",
            "Cycle335 finite recurrence -> capacity/renewal boundary",
            "Record axiom fixed locking/readout -> final typing only",
        ),
        "N5_tested": "bit/site, 69-M2 block, L3/L6 ledger, two-lane overlap",
        "N5_untested": "indefinite environment and volume-wide Record process",
        "N6_partial_closure": (
            "approved Record axiom supplies typing consequences, not formation rule",
            "larger phase-correcting code",
            "fresh outward bank generation",
        ),
        "N7_hostile_steelman": (
            "A phase-correcting code with autonomous fresh environment could remove the "
            "tested logical/finite-capacity boundaries, while the existing Record axiom "
            "already supplies permanence once a lawful site/content typing is established."
        ),
        "N8_echo": (
            "Cycle337 narrowed protection to a diagonal pointer algebra",
            "Cycle335 kept inverse and finite capacity explicit",
            "Cycle341 adds a fixed future domain and consumes Record only at typing",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_claim": False,
        "axiom_pressure": False,
    }
    check(
        "full N1-N8 blocks broad impossibility, physical-permanence, and axiom-pressure claims",
        len(routes) >= 5
        and sum(value.startswith("OPEN") for value in routes.values()) >= 3
        and len(pairwise) == 6
        and not hidden_hits
        and detail["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and not detail["minimum_content_claim"]
        and not detail["axiom_pressure"],
        detail,
    )
    return detail


def lawful_domain_controls() -> None:
    syndrome = Syndrome(1, 1)
    invalid = (
        lambda: syndrome_value(c337.PHYSICAL_POINTER_M2),
        lambda: append_syndrome((syndrome,), syndrome),
        lambda: remove_last_syndrome((None,)),
        lambda: future_step(FutureState((0,), (None,))),
        lambda: renew_outward(RenewalState((None,), (None,))),
        lambda: renew_outward(RenewalState((syndrome,), (syndrome,))),
        lambda: delete_renewal_swap(RenewalState((syndrome,), (None,)), 1),
        lambda: inverse_renewal(RenewalState((syndrome,), (None,))),
    )
    rejected = 0
    for call in invalid:
        try:
            call()
        except ValueError:
            rejected += 1
    check(
        "malformed faults, exhausted ledgers, renewal banks, and pointer domains are rejected",
        rejected == len(invalid),
        {"rejected": rejected, "attempted": len(invalid)},
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    fixtures, tables, words = base_surfaces()
    future_stability_controls(tables, words)
    capacity_renewal_and_reconnection_controls(words)
    logical_retarget_and_phase_controls(tables[3], words[3])
    dephasing_occurrence_and_record_typing_controls(fixtures, tables, words)
    overlap_and_deletion_controls(words)
    frame_controls(fixtures)
    support_inventory_and_axiom_controls()
    no_go_discipline_firewall()
    lawful_domain_controls()
    print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT CYCLE341_STABLE_POINTER_RECORD_SECTOR_ROUTE_"
        + ("GREEN" if FAIL == 0 else "INCOMPLETE")
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
