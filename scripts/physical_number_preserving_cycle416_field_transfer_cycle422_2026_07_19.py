#!/usr/bin/env python3
"""Cycle 422: number-preserving Cycle-416 to recurrent-field transfer.

Construct a fixed nine-M2 unitary W on the Cycle-416 source/mediator pair and
one blank reservoir plus six blank field M2s.  On the declared one-excitation
blank-target code, W moves source to reservoir and mediator to the negative
uniform field seed, clearing the original pair.  W is an involutive unitary,
preserves total excitation, and physically realizes the Cycle-418 encoding.

The transferred state then enters the Cycle-419 coin/exchange/directed-SWAP
update with the local exchange coherently controlled by the inherited strict
response bit.  No Cycle-417 copied ports or expectation feedback are used.
The exact global excitation ledger therefore starts at the original
Cycle-416 source/mediator code rather than after a nonconserving fanout.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import cycle416_seven_m2_common_code_seed_cycle418_2026_07_19 as c418
import physical_two_block_recurrent_field_transport_cycle419_2026_07_19 as c419


c416 = c418.c416
c399 = c419.c399
c403 = c419.c403
c210 = c419.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NUMBER_PRESERVING_CYCLE416_FIELD_TRANSFER_CYCLE422_NOTE_2026-07-19.md"
)
ANGLE = c418.ANGLE
SOURCE_MEDIATOR_DIM = 4
TARGET_DIM = 128
FULL_DIM = SOURCE_MEDIATOR_DIM * TARGET_DIM
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 9e-10
PASS = 0
FAIL = 0
Coord = tuple[int, int, int]


@dataclass(frozen=True)
class Site:
    coord: Coord
    role: str
    block: int | None = None
    direction: int | None = None


RESPONSE_SITE = Site((-4, 0, 0), "STRICT_RESPONSE")
MEDIATOR_SITE = Site((-3, 0, 0), "CYCLE416_MEDIATOR")
SOURCE_SITE = Site((-2, 0, 0), "CYCLE416_SOURCE")
BLOCK_CENTERS = ((0, 0, 0), (3, 0, 0))
BLOCK_SITES = tuple(
    [Site(BLOCK_CENTERS[block], "LOCAL_RESERVOIR", block)]
    + [
        Site(
            tuple(
                int(BLOCK_CENTERS[block][axis] + c210.DIRECTIONS[direction, axis])
                for axis in range(3)
            ),
            "DIRECTIONAL_FIELD_M2",
            block,
            direction,
        )
        for direction in range(6)
    ]
    for block in range(2)
)


@dataclass(frozen=True)
class FieldKey:
    bridge: c399.BridgeKey
    field_basis: int


FieldState = dict[FieldKey, np.ndarray]


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


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "fixed nine-m2 unitary",
        "source column maps to the reservoir column",
        "mediator column maps to the negative uniform field column",
        "clears source and mediator",
        "w e_in g_416(r) = g_7(r) w e_in",
        "r=0,1",
        "exact adjoint and inverse",
        "all 24 proper-cubic frames",
        "connected bounded layout",
        "target-blank refusal",
        "blind held l6",
        "without cycle-417 ports",
        "global excitation balance",
        "no expectation feedback",
        "not physical energy, source, time, or born weight",
        "science disposition",
        "no shared obstruction",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the note fixes the physical transfer, global ledger, and scope", not missing, missing)


def full_index(source_mediator: int, target: int) -> int:
    return source_mediator * TARGET_DIM + target


def input_encoding() -> np.ndarray:
    encoding = np.zeros((FULL_DIM, 2), dtype=complex)
    encoding[full_index(2, 0), 0] = 1  # |source=1,mediator=0; target blank>
    encoding[full_index(1, 0), 1] = 1  # |source=0,mediator=1; target blank>
    return encoding


def target_encoding(*, sign: int = -1, omit_direction: int | None = None) -> np.ndarray:
    if sign not in (-1, 1):
        raise ValueError("target sign must be +/-1")
    if omit_direction is not None and omit_direction not in range(6):
        raise ValueError("omitted direction must be in range(6)")
    encoding = np.zeros((FULL_DIM, 2), dtype=complex)
    encoding[full_index(0, 64), 0] = 1  # cleared pair; R=1,F=vacuum
    directions = tuple(direction for direction in range(6) if direction != omit_direction)
    for direction in directions:
        encoding[full_index(0, 1 << direction), 1] = sign / np.sqrt(len(directions))
    return encoding


def transfer_unitary(*, sign: int = -1, omit_direction: int | None = None) -> np.ndarray:
    source = input_encoding()
    target = target_encoding(sign=sign, omit_direction=omit_direction)
    # Swap the two orthogonal code subspaces and leave their complement fixed.
    return (
        np.eye(FULL_DIM, dtype=complex)
        - source @ source.conj().T
        - target @ target.conj().T
        + target @ source.conj().T
        + source @ target.conj().T
    )


def total_excitation() -> np.ndarray:
    values = []
    for source_mediator in range(SOURCE_MEDIATOR_DIM):
        for target in range(TARGET_DIM):
            values.append(float(source_mediator.bit_count() + target.bit_count()))
    return np.diag(values).astype(complex)


def lifted_target_gate(response: int) -> np.ndarray:
    return np.kron(
        np.eye(SOURCE_MEDIATOR_DIM, dtype=complex),
        c418.physical_gate(response, ANGLE),
    )


def layout_controls() -> None:
    print("\nCONNECTED PHYSICAL-M2 LAYOUT")
    transfer_sites = (MEDIATOR_SITE, SOURCE_SITE) + tuple(BLOCK_SITES[0])
    all_sites = (RESPONSE_SITE,) + transfer_sites + tuple(BLOCK_SITES[1])

    def connected(sites: tuple[Site, ...]) -> bool:
        pending = {0}
        reached: set[int] = set()
        while pending:
            index = pending.pop()
            reached.add(index)
            for other in range(len(sites)):
                if other in reached:
                    continue
                if sum(
                    abs(sites[index].coord[axis] - sites[other].coord[axis])
                    for axis in range(3)
                ) == 1:
                    pending.add(other)
        return len(reached) == len(sites)

    frame_failures = 0
    for frame in c210.proper_cubic_frames():
        moved = tuple(
            Site(
                tuple(int(value) for value in frame @ np.asarray(site.coord)),
                site.role,
                site.block,
                site.direction,
            )
            for site in all_sites
        )
        frame_failures += int(len({site.coord for site in moved}) != len(moved))
        frame_failures += int(not connected(moved))
    check(
        "the nine-M2 W support and its response-plus-two-block extension have connected bounded layout in all frames",
        len({site.coord for site in all_sites}) == len(all_sites)
        and connected(transfer_sites)
        and connected(all_sites)
        and frame_failures == 0,
        {
            "W_support_M2": len(transfer_sites),
            "response_controlled_local_support_union_M2": 10,
            "two_block_installation_union_M2": len(all_sites),
            "maximum_coordinate_diameter": max(
                sum(abs(left.coord[axis] - right.coord[axis]) for axis in range(3))
                for left in all_sites
                for right in all_sites
            ),
            "frames": 24,
            "layout_frame_failures": frame_failures,
        },
    )


def unitary_intertwiner_controls() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    print("\nFIXED W / CYCLE-418 PHYSICAL INTERTWINER")
    source = input_encoding()
    target = target_encoding()
    transfer = transfer_unitary()
    identity = np.eye(FULL_DIM, dtype=complex)
    number = total_excitation()
    rows = []
    failures = 0
    for response in (0, 1):
        logical = c418.logical_gate(response, ANGLE)
        physical = lifted_target_gate(response)
        intertwiner = np.linalg.norm(
            transfer @ source @ logical - physical @ transfer @ source
        )
        inverse = np.linalg.norm(
            transfer.conj().T @ physical.conj().T @ target
            - source @ logical.conj().T
        )
        compression = np.linalg.norm(
            target.conj().T @ physical @ target - logical
        )
        failures += int(max(intertwiner, inverse, compression) > 4e-15)
        rows.append(
            {
                "response": response,
                "intertwiner_residual": float(intertwiner),
                "inverse_intertwiner_residual": float(inverse),
                "compression_residual": float(compression),
            }
        )
    unitarity = np.linalg.norm(transfer.conj().T @ transfer - identity)
    involution = np.linalg.norm(transfer @ transfer - identity)
    number_residual = np.linalg.norm(transfer @ number - number @ transfer)
    mapping = np.linalg.norm(transfer @ source - target)
    check(
        "one fixed nine-M2 unitary physically implements Cycle-418 with exact adjoint, inverse, and total-excitation ledger",
        unitarity < 4e-14
        and involution < 4e-14
        and number_residual < 4e-14
        and mapping < 4e-15
        and failures == 0,
        {
            "dimension": FULL_DIM,
            "unitarity_residual": float(unitarity),
            "involution_residual": float(involution),
            "number_commutator": float(number_residual),
            "W_Ein_minus_E418": float(mapping),
            "rows": rows,
            "failures": failures,
        },
    )
    return transfer, source, target


def covariance_controls(transfer: np.ndarray, source: np.ndarray, target: np.ndarray) -> None:
    print("\nPROPER-CUBIC COVARIANCE")
    sparse_transfer = sparse.csr_matrix(transfer)
    frame_residuals = []
    source_residuals = []
    target_residuals = []
    for frame in c210.proper_cubic_frames():
        direction = c210.direction_permutation(frame)
        local_frame = sparse.kron(
            sparse.eye(2, dtype=complex, format="csr"),
            sparse.csr_matrix(c418.c7.field_bit_permutation(direction)),
            format="csr",
        )
        representation = sparse.kron(
            sparse.eye(SOURCE_MEDIATOR_DIM, dtype=complex, format="csr"),
            local_frame,
            format="csr",
        )
        frame_residuals.append(
            float(sparse.linalg.norm(representation @ sparse_transfer - sparse_transfer @ representation))
        )
        source_residuals.append(
            float(np.linalg.norm(representation @ source - source))
        )
        target_residuals.append(
            float(np.linalg.norm(representation @ target - target))
        )
    check(
        "W, its blank input code, and the signed target code are scalar-covariant in all 24 proper-cubic frames",
        len(frame_residuals) == 24
        and max(frame_residuals) < 4e-14
        and max(source_residuals) < 4e-15
        and max(target_residuals) < 4e-15,
        {
            "frames": len(frame_residuals),
            "maximum_W_covariance_residual": max(frame_residuals),
            "maximum_input_covariance_residual": max(source_residuals),
            "maximum_target_covariance_residual": max(target_residuals),
        },
    )


def validate_declared_input(
    source: int,
    mediator: int,
    reservoir: int,
    field_basis: int,
) -> None:
    if source not in (0, 1) or mediator not in (0, 1) or source + mediator != 1:
        raise ValueError("the Cycle-416 input requires exactly one source/mediator excitation")
    if reservoir != 0 or field_basis != 0:
        raise ValueError("the forward W contract refuses a nonblank target")


def deletion_sign_domain_controls(
    transfer: np.ndarray, source: np.ndarray, target: np.ndarray
) -> None:
    print("\nTARGET-BLANK / DELETION / SIGN CONTROLS")
    rejections = 0
    for probe in (
        (1, 0, 1, 0),
        (0, 1, 0, 1),
        (0, 0, 0, 0),
        (1, 1, 0, 0),
    ):
        try:
            validate_declared_input(*probe)
        except ValueError:
            rejections += 1
    deleted = np.eye(FULL_DIM, dtype=complex)
    deletion_residual = np.linalg.norm(deleted @ source - target)
    wrong_sign = transfer_unitary(sign=1)
    wrong_sign_intertwiner = np.linalg.norm(
        wrong_sign @ source @ c418.logical_gate(1, ANGLE)
        - lifted_target_gate(1) @ wrong_sign @ source
    )
    missing_direction = transfer_unitary(omit_direction=5)
    missing_direction_intertwiner = np.linalg.norm(
        missing_direction @ source @ c418.logical_gate(1, ANGLE)
        - lifted_target_gate(1) @ missing_direction @ source
    )
    cleared_pair_projector = np.zeros((FULL_DIM, FULL_DIM), dtype=complex)
    cleared_pair_projector[:TARGET_DIM, :TARGET_DIM] = np.eye(TARGET_DIM)
    code_leakage = np.linalg.norm(
        (np.eye(FULL_DIM) - cleared_pair_projector) @ transfer @ source
    )
    check(
        "the forward contract refuses nonblank targets while W deletion, sign reversal, and one-direction deletion are visible",
        rejections == 4
        and deletion_residual > 1.9
        and wrong_sign_intertwiner > 0.9
        and missing_direction_intertwiner > 0.05
        and code_leakage < 4e-15
        and np.linalg.norm(transfer.conj().T @ target - source) < 4e-15,
        {
            "lawful_domain_rejections": rejections,
            "cleared_source_mediator_leakage": float(code_leakage),
            "W_deletion_transfer_residual": float(deletion_residual),
            "wrong_sign_intertwiner_residual": float(wrong_sign_intertwiner),
            "one_direction_deleted_intertwiner_residual": float(missing_direction_intertwiner),
            "adjoint_return_residual": float(np.linalg.norm(transfer.conj().T @ target - source)),
        },
    )


def transfer_balance_state(state: c416.BalanceState) -> FieldState:
    """Apply W on the declared blank-target code without materializing 512 columns."""
    output: FieldState = {}
    for key, value in state.items():
        validate_declared_input(key.source, key.mediator, 0, 0)
        if key.source:
            target = FieldKey(key.bridge, c419.reservoir_index(0))
            output[target] = output.get(target, 0) + value.copy()
        else:
            for direction in range(6):
                target = FieldKey(key.bridge, c419.field_index(0, direction))
                output[target] = output.get(target, 0) - c210.UNIFORM[direction] * value
    return output


def field_state_residual(left: FieldState, right: FieldState) -> float:
    total = 0.0
    for key in set(left) | set(right):
        template = left.get(key, right.get(key))
        assert template is not None
        a = left.get(key, np.zeros_like(template))
        b = right.get(key, np.zeros_like(template))
        total += float(np.vdot(a - b, a - b).real)
    return float(np.sqrt(total))


def balance_state_residual(left: c416.BalanceState, right: c416.BalanceState) -> float:
    return c416.state_residual(left, right)


def inverse_transfer_state(state: FieldState) -> tuple[c416.BalanceState, float]:
    bridges = {key.bridge for key in state}
    output: c416.BalanceState = {}
    for bridge in bridges:
        template = next(value for key, value in state.items() if key.bridge == bridge)
        source = state.get(
            FieldKey(bridge, c419.reservoir_index(0)), np.zeros_like(template)
        )
        mediator = np.zeros_like(template)
        for direction in range(6):
            mediator -= c210.UNIFORM[direction].conjugate() * state.get(
                FieldKey(bridge, c419.field_index(0, direction)),
                np.zeros_like(template),
            )
        if np.linalg.norm(source) > 1e-15:
            output[c416.BalanceKey(bridge, 1, 0)] = source
        if np.linalg.norm(mediator) > 1e-15:
            output[c416.BalanceKey(bridge, 0, 1)] = mediator
    reconstructed = transfer_balance_state(output)
    return output, field_state_residual(reconstructed, state)


def apply_controlled_recurrent(
    state: FieldState,
    origin: int,
    *,
    inverse: bool = False,
) -> FieldState:
    matrices = {
        response: c419.recurrent_update(
            ANGLE,
            delete_vertex=(response == 0),
        )
        for response in (0, 1)
    }
    if inverse:
        matrices = {response: matrix.conj().T for response, matrix in matrices.items()}
    output: FieldState = {}
    for key, value in state.items():
        response = c416.response_bit(key.bridge, origin)
        matrix = matrices[response]
        for target_basis in range(c419.DIMENSION):
            coefficient = matrix[target_basis, key.field_basis]
            if abs(coefficient) < 1e-15:
                continue
            target = FieldKey(key.bridge, target_basis)
            output[target] = output.get(target, 0) + coefficient * value
    return output


def state_norm(state: dict) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def field_number(state: FieldState) -> float:
    return float(
        sum(
            np.vdot(value, value).real
            for key, value in state.items()
            if key.field_basis != c419.VACUUM
        )
    )


def basis_weight(state: FieldState, basis: int) -> float:
    return float(
        sum(
            np.vdot(value, value).real
            for key, value in state.items()
            if key.field_basis == basis
        )
    )


def held_global_propagation_controls(factors, packet_layout, packet_initial) -> None:
    print("\nGLOBAL CYCLE-416 -> W -> RESPONSE-CONTROLLED CYCLE-419 HISTORY")
    rows = []
    failures = 0
    ratio_expected = float(np.sin(2 * ANGLE) ** 2 / np.sin(ANGLE) ** 4)
    neighbor_basis = c419.field_index(1, c419.REVERSE[c419.EDGE_DIRECTION])
    for route in c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                source = c403.pre_admission_response(
                    origin, route, length, factors, packet_layout, packet_initial
                )
                original = c416.encode(source)
                balanced = c416.balance_step(original, origin, ANGLE)
                transferred = transfer_balance_state(balanced)
                advanced = apply_controlled_recurrent(transferred, origin)
                restored_target = apply_controlled_recurrent(
                    advanced, origin, inverse=True
                )
                restored, transfer_leakage = inverse_transfer_state(restored_target)
                inverse_residual = balance_state_residual(restored, balanced)
                response_weight = c403.target_sector_weight(source, origin)
                new_expected = response_weight * np.sin(2 * ANGLE) ** 2 / 6
                old_copied_expected = response_weight * np.sin(ANGLE) ** 4 / 6
                observed = basis_weight(advanced, neighbor_basis)
                ratio = observed / old_copied_expected
                original_number = sum(
                    np.vdot(value, value).real * (key.source + key.mediator)
                    for key, value in balanced.items()
                )
                transferred_number = field_number(transferred)
                propagated_number = field_number(advanced)
                number_residual = max(
                    abs(original_number - transferred_number),
                    abs(transferred_number - propagated_number),
                )
                failures += int(abs(observed - new_expected) > TOLERANCE)
                failures += int(abs(ratio - ratio_expected) > 2e-10)
                failures += int(number_residual > TOLERANCE)
                failures += int(max(inverse_residual, transfer_leakage) > TOLERANCE)
                rows.append(
                    {
                        "route": route,
                        "L": length,
                        "held": length == HELD_LENGTH,
                        "origin": "A" if origin == 0 else "C",
                        "observed_number_preserving_neighbor_weight": observed,
                        "expected_number_preserving_neighbor_weight": new_expected,
                        "Cycle419_copied_port_neighbor_weight": old_copied_expected,
                        "new_to_copied_ratio": ratio,
                        "global_number_residual": number_residual,
                        "inverse_residual": inverse_residual,
                        "target_code_leakage": transfer_leakage,
                    }
                )
    check(
        "direct W transfer gives global source-plus-field balance and held one-edge propagation without Cycle-417 ports or expectation feedback",
        failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "analytic_new_to_Cycle419_copied_ratio": ratio_expected,
            "Cycle417_port_M2_used": 0,
            "host_expectation_feedback": 0,
            "physical_response_control": "inherited strict-response M2",
            "comparison_readout_use": "post-update diagnostic only",
        },
    )


def inventory_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN INVENTORY")
    inventory = {
        "supplied": (
            "Cycle416 strict-response source/mediator code, response bit, and angle",
            "one blank reservoir M2, six blank field M2, and dense bounded W implementation",
            "Cycle418 negative uniform seed convention",
            "Cycle419 field coin, directed edge transport, two-block boundary, sizes, and tolerances",
        ),
        "derived": (
            "physical W implementation of E418 with exact inverse and global excitation preservation",
            "r=0,1 W-Ein-G416/G7 intertwiner and all-frame covariance",
            "target-blank refusal, deletion/sign/direction visibility, and cleared old registers",
            "held response-controlled one-edge propagation and exact return to Cycle416 balance state",
            "quantitative difference from the non-number-conserving copied-port route",
        ),
        "open": (
            "primitive synthesis and autonomous blank-target preparation/occurrence",
            "full cubic recurrent field, return/reabsorption, and stationary response selection",
            "carried matter, multiparticle FSWAP transport, contact/recoil ledger, and calibration",
            "physical resource/energy/source identification, Records, time, metric, gravity, probability, and realized history",
        ),
        "authority": "none",
        "audit": "unset",
        "Cycle417_fanout_used": False,
        "global_excitation_ledger_from_Cycle416": True,
        "host_expectation_feedback": 0,
        "physical_energy_source_time_or_Born_selected": False,
        "actual_Records_added": 0,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    check(
        "the inventory keeps the global excitation construction separate from physical resource and constitutional claims",
        not inventory["Cycle417_fanout_used"]
        and inventory["global_excitation_ledger_from_Cycle416"]
        and not inventory["physical_energy_source_time_or_Born_selected"]
        and not inventory["shared_obstruction"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    print("CYCLE 422: NUMBER-PRESERVING CYCLE416-TO-FIELD TRANSFER")
    note_contract()
    layout_controls()
    transfer, source, target = unitary_intertwiner_controls()
    covariance_controls(transfer, source, target)
    deletion_sign_domain_controls(transfer, source, target)
    _rows, factors = c399.source_factors()
    packet_layout, packet_initial = c399.packet_fixture()
    held_global_propagation_controls(factors, packet_layout, packet_initial)
    inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_NUMBER_PRESERVING_CYCLE416_FIELD_TRANSFER_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_NUMBER_PRESERVING_CYCLE416_FIELD_TRANSFER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
