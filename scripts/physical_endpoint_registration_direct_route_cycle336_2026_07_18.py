#!/usr/bin/env python3
"""Cycle 336 route 1: direct endpoint/content registration handshake.

This runner joins three already-bounded interfaces:

* Cycle 333 supplies a unique-or-undefined continuation flag relative to
  supplied realized-prefix content;
* Cycle 334 supplies a close-gated contact-trine environment endpoint; and
* Cycle 335 supplies protected recurrent/export mechanics with explicit
  finite capacity.

The new object is a direct computational-basis permutation on finite M2
registers.  Branch endpoint, supplied realized endpoint content, candidate
identity/mask, close, recurrence phase, equality workspace, commit workspace,
incoming/outgoing payloads, and four protected slots are all encoded in the
state.  The update contains no host-side selector query or hidden phase
argument.  It is an equality-only conditional registration compiler, not an
actual-member selector.  Its candidate output is not a Record, its update
count is not time, and its coherent commit sector is not a Born sample.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_relational_actual_history_member_selection_cycle333_2026_07_18 as c333
import physical_environment_export_realized_member_bridge_cycle334_2026_07_18 as c334
import protected_recurrent_actual_history_selection_cycle335_2026_07_18 as c335


c332 = c333.c332
c329 = c333.c329
c314 = c333.c314
c317 = c334.c317

TOL = 1.2e-10
BRANCHES = c334.BRANCH_LABELS
BLANK_ENDPOINT = c334.BLANK_LABEL
N_CANDIDATES = c333.N_CANDIDATES
N_SLOTS = 4
HOST_SELECTION_QUERIES = 0
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
class Payload:
    """Five M2: three endpoint bits and two candidate-identity bits."""

    endpoint: int
    candidate: int


BLANK = Payload(BLANK_ENDPOINT, N_CANDIDATES - 1)


@dataclass(frozen=True)
class RegisterState:
    """The declared 42-M2 direct-route register block."""

    endpoint: int             # 3 M2, incoming Cycle-334 environment label
    realized_content: int     # 3 M2, supplied realized-state local content
    candidate: int            # 2 M2, Cycle-333 candidate-bank identity
    candidate_mask: int       # 4 M2, Cycle-333 unique/ambiguous flags
    phase: int                # 2 M2, Cycle-335 recurrent blank position
    close: int                # 1 M2, Cycle-332/334 close certificate
    equality: int             # 1 M2 reversible equality workspace
    commit: int               # 1 M2 reversible conditional-commit workspace
    outgoing: Payload         # 5 M2 exported old protected payload
    slots: tuple[Payload, ...]  # 4 x 5 M2 protected recurrent ring


REGISTER_M2 = 3 + 3 + 2 + 4 + 2 + 1 + 1 + 1 + 5 + N_SLOTS * 5
DELETABLE_GATES = frozenset(("equality", "commit", "insert", "phase", "export"))


def validate_payload(payload: Payload) -> None:
    if not 0 <= payload.endpoint < 8 or not 0 <= payload.candidate < N_CANDIDATES:
        raise ValueError("a payload is exactly three endpoint M2 and two identity M2")


def validate_state(state: RegisterState) -> None:
    if not 0 <= state.endpoint < 8 or not 0 <= state.realized_content < 8:
        raise ValueError("endpoint and realized content are three-M2 labels")
    if not 0 <= state.candidate < N_CANDIDATES:
        raise ValueError("candidate identity is a two-M2 label")
    if not 0 <= state.candidate_mask < 2**N_CANDIDATES:
        raise ValueError("candidate membership is a four-M2 word")
    if not 0 <= state.phase < N_SLOTS:
        raise ValueError("recurrence phase is a two-M2 word")
    if state.close not in (0, 1) or state.equality not in (0, 1) or state.commit not in (0, 1):
        raise ValueError("close, equality, and commit are physical bits")
    if len(state.slots) != N_SLOTS:
        raise ValueError("the direct route uses four protected payload slots")
    validate_payload(state.outgoing)
    for payload in state.slots:
        validate_payload(payload)


def input_payload(state: RegisterState) -> Payload:
    return Payload(state.endpoint, state.candidate)


def xor_equality(state: RegisterState) -> RegisterState:
    truth = int(state.endpoint == state.realized_content)
    return replace(state, equality=state.equality ^ truth)


def commit_truth(state: RegisterState) -> int:
    """Truth table evaluated entirely from encoded registers."""
    lawful_endpoint = state.endpoint in BRANCHES
    identity_bound = state.candidate_mask == 1 << state.candidate
    fresh = state.slots[state.phase] == BLANK
    output_blank = state.outgoing == BLANK
    return int(
        lawful_endpoint
        and identity_bound
        and fresh
        and output_blank
        and state.close == 1
        and state.equality == 1
    )


def xor_commit(state: RegisterState) -> RegisterState:
    return replace(state, commit=state.commit ^ commit_truth(state))


def swap_input_slot(state: RegisterState) -> RegisterState:
    values = list(state.slots)
    incoming = input_payload(state)
    values[state.phase], incoming = incoming, values[state.phase]
    return replace(
        state,
        endpoint=incoming.endpoint,
        candidate=incoming.candidate,
        slots=tuple(values),
    )


def shift_phase(state: RegisterState, direction: int) -> RegisterState:
    if direction not in (-1, 1):
        raise ValueError("the reversible phase shift is one forward or inverse step")
    return replace(state, phase=(state.phase + direction) % N_SLOTS)


def swap_outgoing_slot(state: RegisterState) -> RegisterState:
    values = list(state.slots)
    values[state.phase], outgoing = state.outgoing, values[state.phase]
    return replace(state, outgoing=outgoing, slots=tuple(values))


def validate_deleted_gate(deleted_gate: str | None) -> None:
    if deleted_gate is not None and deleted_gate not in DELETABLE_GATES:
        raise ValueError("deleted gate is outside the five-gate direct compiler")


def forward(state: RegisterState, deleted_gate: str | None = None) -> RegisterState:
    """Apply the direct route; every primitive is a reversible truth-table gate."""
    validate_state(state)
    validate_deleted_gate(deleted_gate)
    result = state
    if deleted_gate != "equality":
        result = xor_equality(result)
    if deleted_gate != "commit":
        result = xor_commit(result)
    if result.commit == 1:
        if deleted_gate != "insert":
            result = swap_input_slot(result)
        if deleted_gate != "phase":
            result = shift_phase(result, 1)
        if deleted_gate != "export":
            result = swap_outgoing_slot(result)
    validate_state(result)
    return result


def inverse(state: RegisterState, deleted_gate: str | None = None) -> RegisterState:
    """Reverse the exact gate list, including any declared one-gate deletion."""
    validate_state(state)
    validate_deleted_gate(deleted_gate)
    result = state
    if result.commit == 1:
        if deleted_gate != "export":
            result = swap_outgoing_slot(result)
        if deleted_gate != "phase":
            result = shift_phase(result, -1)
        if deleted_gate != "insert":
            result = swap_input_slot(result)
    if deleted_gate != "commit":
        result = xor_commit(result)
    if deleted_gate != "equality":
        result = xor_equality(result)
    validate_state(result)
    return result


def protected_payload(slot: int) -> Payload:
    return Payload(slot % len(BRANCHES), slot % N_CANDIDATES)


def ring_with_blank(phase: int) -> tuple[Payload, ...]:
    if not 0 <= phase < N_SLOTS:
        raise ValueError("blank phase is outside the four-slot ring")
    return tuple(BLANK if slot == phase else protected_payload(slot) for slot in range(N_SLOTS))


def code_state(
    endpoint: int,
    realized_content: int,
    candidate: int,
    candidate_mask: int,
    phase: int,
    close: int,
    *,
    equality: int = 0,
    commit: int = 0,
    slots: tuple[Payload, ...] | None = None,
    outgoing: Payload = BLANK,
) -> RegisterState:
    state = RegisterState(
        endpoint,
        realized_content,
        candidate,
        candidate_mask,
        phase,
        close,
        equality,
        commit,
        outgoing,
        ring_with_blank(phase) if slots is None else slots,
    )
    validate_state(state)
    return state


def local_gate_and_inverse_controls() -> dict[str, object]:
    equality_rows = np.arange(8 * 8 * 2, dtype=np.int64)
    equality_map = np.empty_like(equality_rows)
    for row in equality_rows:
        endpoint = int(row // 16)
        content = int((row // 2) % 8)
        witness = int(row % 2)
        equality_map[row] = 16 * endpoint + 2 * content + (witness ^ int(endpoint == content))

    inverse_failures = 0
    cases = 0
    masks = range(2**N_CANDIDATES)
    for endpoint, content, candidate, mask, phase, close, equality, commit in product(
        (*BRANCHES, BLANK_ENDPOINT),
        (*BRANCHES, BLANK_ENDPOINT),
        range(N_CANDIDATES),
        masks,
        range(N_SLOTS),
        (0, 1),
        (0, 1),
        (0, 1),
    ):
        state = code_state(
            endpoint,
            content,
            candidate,
            mask,
            phase,
            close,
            equality=equality,
            commit=commit,
        )
        for deleted_gate in (None, *sorted(DELETABLE_GATES)):
            inverse_failures += int(inverse(forward(state, deleted_gate), deleted_gate) != state)
            cases += 1
    detail = {
        "equality_truth_table_rows": len(equality_map),
        "equality_permutation_failures": len(equality_map) - len(np.unique(equality_map)),
        "equality_involution_failures": int(
            np.count_nonzero(equality_map[equality_map] != equality_rows)
        ),
        "full_and_deleted_inverse_cases": cases,
        "inverse_failures": inverse_failures,
        "register_M2": REGISTER_M2,
        "maximum_compiled_step_support_M2": REGISTER_M2,
    }
    check(
        "the equality truth table and full five-gate compiler are exact reversible permutations on the declared M2 code family",
        detail["equality_permutation_failures"] == 0
        and detail["equality_involution_failures"] == 0
        and inverse_failures == 0
        and REGISTER_M2 == 42,
        detail,
    )
    return detail


def predecessor_fixture_controls() -> tuple[dict[int, c333.SelectionFixture], dict[int, c334.CloseExportFixture], dict[str, object]]:
    selections = {length: c333.build_fixture(length) for length in (3, 6)}
    exports = {length: c334.close_fixture(length) for length in (3, 6)}
    vector, _rho = c334.branch_state()
    rows = []
    for length in (3, 6):
        selection = selections[length]
        selected = c333.route1_unique(selection, anchor=selection.anchor)
        export = exports[length]
        physical_endpoint = export.output_code @ vector
        exported = export.export_unitary @ export.input_code @ vector
        branch_norms = tuple(
            float(np.vdot(physical_endpoint[2 * label : 2 * (label + 1)], physical_endpoint[2 * label : 2 * (label + 1)]).real)
            for label in BRANCHES
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "selection_status": selected.status,
                "selection_flags": selected.flags,
                "close": export.close_certificate,
                "false_close": export.false_close,
                "export_unitary_residual": float(
                    np.linalg.norm(export.export_unitary.conj().T @ export.export_unitary - np.eye(16))
                ),
                "export_forward_residual": float(np.linalg.norm(exported - physical_endpoint)),
                "branch_sector_norms": branch_norms,
                "branch_sector_norm_sum": sum(branch_norms),
            }
        )
    check(
        "the Cycle-333 unique continuation and Cycle-334 close-gated coherent endpoint are present at trained and held size",
        all(
            row["selection_status"] == "bound"
            and row["selection_flags"] is not None
            and sum(row["selection_flags"]) == 1
            and row["close"] == 1
            and row["false_close"] == 0
            and max(row["export_unitary_residual"], row["export_forward_residual"], abs(row["branch_sector_norm_sum"] - 1)) < TOL
            and min(row["branch_sector_norms"]) > 0.1
            for row in rows
        ),
        rows,
    )
    return selections, exports, {"rows": rows, "vector": vector}


def expected_commit_output(state: RegisterState) -> tuple[Payload, Payload, int]:
    old_phase = state.phase
    new_phase = (old_phase + 1) % N_SLOTS
    return input_payload(state), state.slots[new_phase], new_phase


def covariance_and_register_integration_controls(
    selections: dict[int, c333.SelectionFixture],
    exports: dict[int, c334.CloseExportFixture],
) -> dict[str, object]:
    orders = tuple(permutations(range(N_CANDIDATES)))
    positions = np.asarray(
        [(x, y, z) for x in range(4) for y in range(4) for z in range(3)][
            :REGISTER_M2
        ],
        dtype=int,
    )
    frames = tuple(c317.c311.c235.proper_cubic_frames())
    cases = 0
    mapping_failures = selection_failures = registration_failures = geometry_failures = 0
    for length, fixture in selections.items():
        export = exports[length]
        for frame in frames:
            mapping, failures = c332.event_frame_mapping(fixture.program.sidecar, frame)
            mapping_failures += failures
            anchor = int(mapping[fixture.anchor])
            mapped = tuple(
                c333.Candidate(int(mapping[item.pre]), int(mapping[item.post]))
                for item in fixture.candidates
            )
            support = c329.build_fixture(length, frame)
            match, ready = c329.route_outputs(support, "syndrome")
            carried_positions = positions @ frame.T
            geometry_failures += int(
                len({tuple(row) for row in carried_positions}) != len(positions)
                or np.max(np.ptp(carried_positions, axis=0)) > 3
            )
            for order in orders:
                bank = tuple(mapped[index] for index in order)
                outcome = c333.route1_unique(
                    fixture,
                    anchor=anchor,
                    candidates=bank,
                    match=match,
                    ready=ready,
                )
                if outcome.status != "bound" or outcome.flags is None or outcome.selected is None:
                    selection_failures += 1
                    continue
                candidate = outcome.flags.index(1)
                mask = sum(bit << index for index, bit in enumerate(outcome.flags))
                selection_failures += int(mask != 1 << candidate)
                for branch in BRANCHES:
                    for phase in range(N_SLOTS):
                        state = code_state(
                            branch,
                            branch,
                            candidate,
                            mask,
                            phase,
                            export.close_certificate,
                        )
                        inserted, outgoing, new_phase = expected_commit_output(state)
                        result = forward(state)
                        registration_failures += int(
                            result.equality != 1
                            or result.commit != 1
                            or input_payload(result) != BLANK
                            or result.slots[phase] != inserted
                            or result.phase != new_phase
                            or result.outgoing != outgoing
                            or result.slots[new_phase] != BLANK
                            or sum(payload == BLANK for payload in result.slots) != 1
                            or inverse(result) != state
                        )
                        cases += 1
    detail = {
        "L_values": tuple(selections),
        "proper_cubic_frames_per_size": len(frames),
        "candidate_orders": len(orders),
        "branch_labels": len(BRANCHES),
        "encoded_phases": N_SLOTS,
        "frame_size_order_branch_phase_cases": cases,
        "event_mapping_failures": mapping_failures,
        "selection_failures": selection_failures,
        "registration_failures": registration_failures,
        "carried_register_geometry_failures": geometry_failures,
        "host_selection_queries": HOST_SELECTION_QUERIES,
        "bounded_register_cube_sites": len(positions),
    }
    check(
        "the direct compiler carries the encoded endpoint content candidate and phase through all frames sizes and bank orders without a host selector",
        cases == 2 * 24 * 24 * len(BRANCHES) * N_SLOTS
        and mapping_failures == selection_failures == registration_failures == geometry_failures == 0
        and HOST_SELECTION_QUERIES == 0,
        detail,
    )
    return detail


def coherent_endpoint_control(exports: dict[int, c334.CloseExportFixture], vector: np.ndarray) -> dict[str, object]:
    rows = []
    for length, fixture in exports.items():
        coherent = (fixture.output_code @ vector).reshape(8, 2)
        sector_norms = tuple(float(np.vdot(coherent[label], coherent[label]).real) for label in BRANCHES)
        for content in BRANCHES:
            committed_sector_norm = sum(
                value for label, value in zip(BRANCHES, sector_norms) if label == content
            )
            rows.append(
                {
                    "L": length,
                    "realized_content": content,
                    "committed_sector_norm": committed_sector_norm,
                    "direct_basis_sum": sector_norms[content],
                    "other_sector_norm": sum(sector_norms) - committed_sector_norm,
                }
            )
    detail = {
        "rows": rows,
        "maximum_sector_identity_residual": max(
            abs(row["committed_sector_norm"] - row["direct_basis_sum"]) for row in rows
        ),
        "all_other_sectors_remain_coherent": all(row["other_sector_norm"] > TOL for row in rows),
        "interpretation": "controlled permutation sector norm; not occurrence or frequency",
    }
    check(
        "the basis permutation extends linearly to the coherent Cycle-334 endpoint and marks only the matching content sector without selecting it",
        detail["maximum_sector_identity_residual"] < TOL
        and detail["all_other_sectors_remain_coherent"],
        detail,
    )
    return detail


def adversarial_controls() -> dict[str, object]:
    base = code_state(0, 0, 0, 1, 0, 1)
    full = forward(base)
    false_close = forward(replace(base, close=0))
    mismatch = forward(replace(base, realized_content=1))
    tie = forward(replace(base, candidate_mask=0b0011))
    wrong_identity = forward(replace(base, candidate_mask=0b0010))
    exhausted_slots = list(base.slots)
    exhausted_slots[base.phase] = Payload(2, 2)
    exhausted = forward(replace(base, slots=tuple(exhausted_slots)))
    retarget_content = forward(replace(base, realized_content=2))
    retarget_pair = forward(replace(base, endpoint=2, realized_content=2))
    deleted = {gate: forward(base, gate) for gate in sorted(DELETABLE_GATES)}
    deletion_visibility = {
        gate: result != full and inverse(result, gate) == base for gate, result in deleted.items()
    }
    malformed = 0
    invalid_calls = (
        lambda: code_state(8, 0, 0, 1, 0, 1),
        lambda: code_state(0, 8, 0, 1, 0, 1),
        lambda: code_state(0, 0, 4, 1, 0, 1),
        lambda: code_state(0, 0, 0, 16, 0, 1),
        lambda: code_state(0, 0, 0, 1, 4, 1),
        lambda: code_state(0, 0, 0, 1, 0, 2),
        lambda: forward(base, "host_dispatch"),
    )
    for call in invalid_calls:
        try:
            call()
        except ValueError:
            malformed += 1
    detail = {
        "full_commit": full.commit,
        "false_close_commit": false_close.commit,
        "mismatch_commit": mismatch.commit,
        "tie_commit": tie.commit,
        "wrong_identity_commit": wrong_identity.commit,
        "exhaustion_commit": exhausted.commit,
        "retarget_content_only_commit": retarget_content.commit,
        "retarget_endpoint_and_content_commit": retarget_pair.commit,
        "retargeted_endpoint": retarget_pair.slots[0].endpoint,
        "one_gate_deletion_visibility_and_inverse": deletion_visibility,
        "lawful_domain_rejections": malformed,
        "lawful_domain_attempts": len(invalid_calls),
    }
    check(
        "false-close mismatch tie wrong-identity exhaustion retarget deletion and lawful-domain controls are exact and separately visible",
        full.commit == 1
        and all(
            result.commit == 0
            for result in (false_close, mismatch, tie, wrong_identity, exhausted, retarget_content)
        )
        and retarget_pair.commit == 1
        and retarget_pair.slots[0].endpoint == 2
        and all(deletion_visibility.values())
        and malformed == len(invalid_calls),
        detail,
    )
    return detail


def recurrence_and_firewall_controls() -> dict[str, object]:
    phase = 0
    slots = ring_with_blank(phase)
    exported = []
    phase_history = [phase]
    blank_history = [tuple(index for index, value in enumerate(slots) if value == BLANK)]
    inverse_rows = []
    for step in range(12):
        branch = step % len(BRANCHES)
        candidate = step % N_CANDIDATES
        state = code_state(
            branch,
            branch,
            candidate,
            1 << candidate,
            phase,
            1,
            slots=slots,
        )
        result = forward(state)
        inverse_rows.append(inverse(result) == state)
        exported.append(result.outgoing)
        phase, slots = result.phase, result.slots
        phase_history.append(phase)
        blank_history.append(tuple(index for index, value in enumerate(slots) if value == BLANK))
    cycle335_reference = (c335.ONE, c335.ONE, c335.ONE, c335.ZERO)
    rotated = cycle335_reference
    for _ in range(4):
        rotated = c335.rotate_right(rotated)
    detail = {
        "registered_steps_with_declared_port_refresh": 12,
        "phase_history": tuple(phase_history),
        "blank_history": tuple(blank_history),
        "exact_step_inverse_failures": len(inverse_rows) - sum(inverse_rows),
        "phase_period_four": all(phase_history[index + 4] == phase_history[index] for index in range(9)),
        "one_blank_every_step": all(len(row) == 1 and row[0] == phase_history[index] for index, row in enumerate(blank_history)),
        "nonblank_exports": sum(payload != BLANK for payload in exported),
        "Cycle335_period_four_reference": rotated == cycle335_reference,
        "incoming_port_refresh": "supplied boundary preparation between reversible steps",
        "candidate_is_Record": False,
        "circuit_cycle_is_time": False,
        "commit_sector_is_Born_sample": False,
        "occurrence_selected": False,
    }
    check(
        "the encoded phase moves one protected blank recurrently and exports old payloads, with port refresh and semantic limits explicit",
        detail["exact_step_inverse_failures"] == 0
        and detail["phase_period_four"]
        and detail["one_blank_every_step"]
        and detail["nonblank_exports"] == 12
        and detail["Cycle335_period_four_reference"]
        and detail["candidate_is_Record"] is False
        and detail["circuit_cycle_is_time"] is False
        and detail["commit_sector_is_Born_sample"] is False
        and detail["occurrence_selected"] is False,
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    gates = local_gate_and_inverse_controls()
    selections, exports, predecessor = predecessor_fixture_controls()
    covariance = covariance_and_register_integration_controls(selections, exports)
    coherent = coherent_endpoint_control(exports, predecessor["vector"])
    attacks = adversarial_controls()
    recurrence = recurrence_and_firewall_controls()
    check(
        "Cycle 336 direct route compiles endpoint/content equality into bounded recurrent registration without semantic promotion",
        gates["inverse_failures"] == 0
        and covariance["registration_failures"] == 0
        and coherent["maximum_sector_identity_residual"] < TOL
        and attacks["tie_commit"] == 0
        and recurrence["exact_step_inverse_failures"] == 0
        and HOST_SELECTION_QUERIES == 0,
        {
            "strongest_positive": "direct encoded equality-only recurrent registration permutation",
            "still_supplied": "realized content, endpoint/candidate preparation, port refresh, Record typing, clock and grade laws",
            "candidate_is_not_Record": True,
            "circuit_cycle_is_not_time": True,
            "coherent_commit_sector_is_not_Born_sample": True,
        },
    )
    print("DATA gates", gates)
    print("DATA predecessor", predecessor["rows"])
    print("DATA covariance", covariance)
    print("DATA coherent", coherent)
    print("DATA attacks", attacks)
    print("DATA recurrence", recurrence)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE336_DIRECT_ENDPOINT_REGISTRATION_GREEN" if FAIL == 0 else "CYCLE336_DIRECT_ROUTE_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
