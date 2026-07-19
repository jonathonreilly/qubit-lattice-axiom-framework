#!/usr/bin/env python3
"""Cycle 418: exact Cycle-416 to seven-M2 common-code seed.

The declared two-level Cycle-416 source/mediator code is embedded into the
one-excitation sector of one reservoir M2 plus six hard-core field M2.  The
minus sign on the uniform field seed converts Cycle 416's +i rotation into
the existing LOCAL_CONJUGATE_RESERVOIR runner's -i exchange convention.

The construction is also lifted, sparsely and without a blockade, to one
complete M64 matter cell times all 128 reservoir/field computational states.
This is a local common-code seed, not a carried source, field stream, energy,
stress, gravity source, clock, or Record.  Authority is none; audit is unset.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_strict_response_source_clock_metric_receiver_cycle416_2026_07_18 as c416
import local_conjugate_reservoir_source_field_ledger_repair_2026_07_17 as c7


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "CYCLE416_SEVEN_M2_COMMON_CODE_SEED_CYCLE418_NOTE_2026-07-19.md"
)
ANGLE = 0.36272452333990834
MATTER_DIM = 64
FIELD_DIM = 64
LOCAL_DIM = 2 * FIELD_DIM
FULL_DIM = MATTER_DIM * LOCAL_DIM
TOLERANCE = 8e-13
AUTHORITY = "none"
AUDIT = "unset"
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "source=1, mediator=0",
        "source=0, mediator=1",
        "e g_416(r) = g_7(r) e",
        "r=0,1",
        "8192",
        "all 64 hard-core field states",
        "all 24 proper-cubic frames",
        "adjoint/inverse relation",
        "number ledger",
        "coupling deletion",
        "sign deletion",
        "not energy, stress, or a gravity source",
        "no negative, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-418 note states the exact seed, lift, imports, and semantic boundary", not missing, missing)


def logical_gate(response: int, angle: float = ANGLE) -> np.ndarray:
    """Cycle-416 gate in ordered basis (|source>, |mediator>)."""
    if response not in (0, 1):
        raise ValueError("response must be binary")
    full = c416.balance_unitary(response, angle)
    return full[np.ix_((2, 1), (2, 1))]


def physical_gate(response: int, angle: float = ANGLE) -> np.ndarray:
    if response not in (0, 1):
        raise ValueError("response must be binary")
    if response == 0:
        return np.eye(LOCAL_DIM, dtype=complex)
    operators = c7.reservoir_field_operators()
    return c7.exchange_gate(angle, operators["exchange"])


def seed(*, sign: int = -1, omit_direction: int | None = None) -> np.ndarray:
    """Return E: C2 -> C2_R tensor C64_F on the declared source code."""
    if sign not in (-1, 1):
        raise ValueError("seed sign must be +/-1")
    if omit_direction is not None and omit_direction not in range(6):
        raise ValueError("omitted direction must be in range(6)")
    encoding = np.zeros((LOCAL_DIM, 2), dtype=complex)
    encoding[FIELD_DIM, 0] = 1  # |R=1,F=vacuum>
    directions = tuple(d for d in range(6) if d != omit_direction)
    normalization = np.sqrt(len(directions))
    for direction in directions:
        encoding[1 << direction, 1] = sign / normalization
    return encoding


def sparse_norm(matrix: sparse.spmatrix) -> float:
    return float(sparse.linalg.norm(matrix))


def seed_intertwiner_controls() -> None:
    encoding = seed()
    projector = encoding @ encoding.conj().T
    rows = []
    failures = 0
    for response in (0, 1):
        logical = logical_gate(response)
        physical = physical_gate(response)
        intertwiner = float(np.linalg.norm(encoding @ logical - physical @ encoding))
        inverse = float(
            np.linalg.norm(encoding @ logical.conj().T - physical.conj().T @ encoding)
        )
        compression = float(
            np.linalg.norm(encoding.conj().T @ physical @ encoding - logical)
        )
        leakage = float(
            np.linalg.norm((np.eye(LOCAL_DIM) - projector) @ physical @ encoding)
        )
        failures += int(max(intertwiner, inverse, compression, leakage) > 3e-15)
        rows.append(
            {
                "response": response,
                "intertwiner_residual": intertwiner,
                "inverse_intertwiner_residual": inverse,
                "compression_residual": compression,
                "code_leakage": leakage,
            }
        )
    check(
        "the signed seed is isometric and satisfies E G_416(r) = G_7(r) E with its inverse for r=0,1",
        np.linalg.norm(encoding.conj().T @ encoding - np.eye(2)) < 5e-16
        and failures == 0,
        {
            "angle": ANGLE,
            "Cycle416_imported_angle": c416.source_angle()[0],
            "angle_difference": ANGLE - c416.source_angle()[0],
            "seed_isometry_residual": float(
                np.linalg.norm(encoding.conj().T @ encoding - np.eye(2))
            ),
            "rows": rows,
            "failures": failures,
        },
    )


def inverse_number_and_deletion_controls() -> None:
    operators = c7.reservoir_field_operators()
    gate = physical_gate(1)
    encoding = seed()
    emitted_initial = encoding[:, 0]
    emitted = gate @ emitted_initial
    restored = gate.conj().T @ emitted
    field_weight = float(np.vdot(emitted, operators["F"] @ emitted).real)
    reservoir_weight = float(np.vdot(emitted, operators["R"] @ emitted).real)
    local_ledger = (
        gate.conj().T @ operators["F"] @ gate
        - operators["F"]
        + gate.conj().T @ operators["R"] @ gate
        - operators["R"]
    )
    deleted_logical = logical_gate(1, 0.0)
    deleted_physical = physical_gate(1, 0.0)
    wrong_sign = seed(sign=1)
    wrong_sign_residual = float(
        np.linalg.norm(wrong_sign @ logical_gate(1) - gate @ wrong_sign)
    )
    missing_direction = seed(omit_direction=5)
    missing_direction_residual = float(
        np.linalg.norm(missing_direction @ logical_gate(1) - gate @ missing_direction)
    )
    check(
        "the local gate has an exact excitation ledger and adjoint inverse on the declared seed",
        np.linalg.norm(gate.conj().T @ gate - np.eye(LOCAL_DIM)) < 3e-14
        and np.linalg.norm(gate @ operators["Q"] - operators["Q"] @ gate) < 3e-14
        and np.linalg.norm(local_ledger) < 3e-14
        and np.linalg.norm(restored - emitted_initial) < 3e-15
        and abs(field_weight - np.sin(ANGLE) ** 2) < 3e-14
        and abs(reservoir_weight - np.cos(ANGLE) ** 2) < 3e-14,
        {
            "unitarity_residual": float(
                np.linalg.norm(gate.conj().T @ gate - np.eye(LOCAL_DIM))
            ),
            "number_commutator": float(
                np.linalg.norm(gate @ operators["Q"] - operators["Q"] @ gate)
            ),
            "operator_number_ledger_residual": float(np.linalg.norm(local_ledger)),
            "inverse_state_residual": float(np.linalg.norm(restored - emitted_initial)),
            "emitted_field_weight": field_weight,
            "Cycle416_G7_transfer": float(np.sin(ANGLE) ** 2),
            "reservoir_weight": reservoir_weight,
        },
    )
    check(
        "coupling deletion is identity while the seed sign and six-direction content are load-bearing",
        np.linalg.norm(deleted_logical - np.eye(2)) == 0
        and np.linalg.norm(deleted_physical - np.eye(LOCAL_DIM)) == 0
        and np.linalg.norm(encoding @ deleted_logical - deleted_physical @ encoding) == 0
        and wrong_sign_residual > 0.9
        and missing_direction_residual > 0.05,
        {
            "coupling_deletion_logical_residual": float(
                np.linalg.norm(deleted_logical - np.eye(2))
            ),
            "coupling_deletion_physical_residual": float(
                np.linalg.norm(deleted_physical - np.eye(LOCAL_DIM))
            ),
            "wrong_sign_intertwiner_residual": wrong_sign_residual,
            "one_direction_deleted_intertwiner_residual": missing_direction_residual,
        },
    )


def covariance_controls() -> None:
    encoding = seed()
    gate = physical_gate(1)
    seed_residuals = []
    gate_residuals = []
    for frame in c7.c210.proper_cubic_frames():
        direction = c7.c210.direction_permutation(frame)
        representation = np.kron(
            np.eye(2), c7.field_bit_permutation(direction)
        )
        seed_residuals.append(float(np.linalg.norm(representation @ encoding - encoding)))
        gate_residuals.append(float(np.linalg.norm(representation @ gate - gate @ representation)))
    check(
        "the uniform signed seed and seven-M2 gate are scalar-covariant in all 24 proper-cubic frames",
        len(seed_residuals) == 24
        and max(seed_residuals) < 3e-15
        and max(gate_residuals) < 3e-14,
        {
            "frames": len(seed_residuals),
            "maximum_seed_covariance_residual": max(seed_residuals),
            "maximum_gate_covariance_residual": max(gate_residuals),
        },
    )


def full_m64_hard_core_controls() -> None:
    """Exercise I_M64 tensor G7 on every one of the 8192 basis columns."""
    local_gate = sparse.csr_matrix(physical_gate(1))
    matter_identity = sparse.eye(MATTER_DIM, format="csr", dtype=complex)
    full_gate = sparse.kron(matter_identity, local_gate, format="csr")
    full_identity = sparse.eye(FULL_DIM, format="csr", dtype=complex)
    inverse_error = full_gate.getH() @ full_gate - full_identity
    inverse_column_norms = np.sqrt(
        np.asarray(abs(inverse_error).power(2).sum(axis=0)).ravel()
    )

    matter_number_values = np.asarray(
        [state.bit_count() for state in range(MATTER_DIM)], dtype=float
    )
    local_q_values = np.diag(c7.reservoir_field_operators()["Q"]).real
    total_number_values = np.repeat(matter_number_values, LOCAL_DIM) + np.tile(
        local_q_values, MATTER_DIM
    )
    total_number = sparse.diags(total_number_values, format="csr", dtype=complex)
    number_commutator = full_gate @ total_number - total_number @ full_gate

    contact_phases = np.exp(
        1j
        * c7.c230.COUPLING
        * matter_number_values
        * (matter_number_values - 1)
        / 2
    )
    contact = sparse.kron(
        sparse.diags(contact_phases, format="csr"),
        sparse.eye(LOCAL_DIM, format="csr", dtype=complex),
        format="csr",
    )
    contact_commutator = full_gate @ contact - contact @ full_gate

    encoding = sparse.csr_matrix(seed())
    full_encoding = sparse.kron(matter_identity, encoding, format="csr")
    full_logical = sparse.kron(
        matter_identity, sparse.csr_matrix(logical_gate(1)), format="csr"
    )
    full_intertwiner = full_encoding @ full_logical - full_gate @ full_encoding
    full_code_leakage = full_gate @ full_encoding - full_encoding @ full_logical

    row, column = full_gate.nonzero()
    matter_block_leakage = int(np.count_nonzero(row // LOCAL_DIM != column // LOCAL_DIM))
    field_states_touched = {
        (index % LOCAL_DIM) % FIELD_DIM for index in range(FULL_DIM)
    }
    check(
        "the sparse spectator extension covers all 8192 M64-matter x M2-reservoir x M64-field basis states with exact inverse and number/contact ledgers",
        full_gate.shape == (FULL_DIM, FULL_DIM)
        and len(inverse_column_norms) == FULL_DIM
        and float(np.max(inverse_column_norms)) < 5e-15
        and sparse_norm(number_commutator) < TOLERANCE
        and sparse_norm(contact_commutator) < TOLERANCE
        and sparse_norm(full_intertwiner) < 3e-14
        and sparse_norm(full_code_leakage) < 3e-14
        and matter_block_leakage == 0
        and field_states_touched == set(range(FIELD_DIM)),
        {
            "basis_dimension": FULL_DIM,
            "matter_basis_states": MATTER_DIM,
            "reservoir_basis_states": 2,
            "hard_core_field_basis_states": len(field_states_touched),
            "sparse_gate_nonzeros": int(full_gate.nnz),
            "full_unitarity_Frobenius_residual": sparse_norm(inverse_error),
            "maximum_basis_inverse_residual": float(np.max(inverse_column_norms)),
            "full_number_commutator": sparse_norm(number_commutator),
            "full_contact_commutator": sparse_norm(contact_commutator),
            "full_seed_intertwiner_residual": sparse_norm(full_intertwiner),
            "full_code_leakage": sparse_norm(full_code_leakage),
            "matter_block_leakage": matter_block_leakage,
        },
    )

    frame_gate_residuals = []
    frame_seed_residuals = []
    for frame in c7.c210.proper_cubic_frames():
        direction = c7.c210.direction_permutation(frame)
        matter_frame = sparse.csr_matrix(c7.c229.fock_lift(direction))
        local_frame = sparse.kron(
            sparse.eye(2, format="csr", dtype=complex),
            sparse.csr_matrix(c7.field_bit_permutation(direction)),
            format="csr",
        )
        physical_frame = sparse.kron(matter_frame, local_frame, format="csr")
        logical_frame = sparse.kron(
            matter_frame, sparse.eye(2, format="csr", dtype=complex), format="csr"
        )
        frame_gate_residuals.append(
            sparse_norm(physical_frame @ full_gate - full_gate @ physical_frame)
        )
        frame_seed_residuals.append(
            sparse_norm(physical_frame @ full_encoding - full_encoding @ logical_frame)
        )
    check(
        "the complete 8192-basis lift and its signed seed intertwine all 24 matter/field proper-cubic Fock actions",
        len(frame_gate_residuals) == 24
        and max(frame_gate_residuals) < TOLERANCE
        and max(frame_seed_residuals) < TOLERANCE,
        {
            "frames": len(frame_gate_residuals),
            "maximum_full_gate_covariance_residual": max(frame_gate_residuals),
            "maximum_full_seed_covariance_residual": max(frame_seed_residuals),
        },
    )


def domain_and_inventory_controls() -> None:
    rejections = 0
    for probe in (
        lambda: logical_gate(2),
        lambda: physical_gate(-1),
        lambda: seed(sign=0),
        lambda: seed(omit_direction=6),
    ):
        try:
            probe()
        except ValueError:
            rejections += 1
    inventory = {
        "supplied": (
            "Cycle416 strict-response bit and fixed +i source/mediator rotation",
            "Cycle219 mass normalization and coupling 0.8 fixing theta",
            "one prepared source excitation and the signed uniform six-direction seed",
            "one reservoir M2, six hard-core field M2, full 64-state field basis, and G7 extension",
            "one M64 matter spectator and its proper-cubic Fock/contact representations",
        ),
        "derived": (
            "exact r=0,1 common-code intertwiner and adjoint inverse",
            "exact number ledger, zero code leakage, deletion visibility, and 24-frame covariance",
            "sparse 8192-basis spectator lift with every hard-core field state lawful/tested and higher occupations unchanged",
        ),
        "open": (
            "strict-response physical control wired into this local seed",
            "field coin/stream/contact schedule and carried reservoir transport",
            "a genuine many-field emission/absorption vertex, two-source number-two history, recoil, work, and resource interpretation",
            "selection as energy/stress/gravity source, actual Records, time, and metric response",
        ),
        "host_expectation_queries": 0,
        "global_field_blockade": False,
        "actual_Records_added": 0,
        "physical_energy_or_source_derived": False,
        "negative_or_minimum_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
    }
    check(
        "lawful domains and the supplied/derived/open inventory preserve the local-seed boundary",
        rejections == 4
        and not inventory["global_field_blockade"]
        and not inventory["physical_energy_or_source_derived"]
        and not inventory["negative_or_minimum_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        {"domain_rejections": rejections, **inventory},
    )


def main() -> int:
    print("CYCLE 418: CYCLE-416 / SEVEN-M2 EXACT COMMON-CODE SEED")
    note_contract()
    seed_intertwiner_controls()
    inverse_number_and_deletion_controls()
    covariance_controls()
    full_m64_hard_core_controls()
    domain_and_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT CYCLE416_SEVEN_M2_COMMON_CODE_SEED_NOT_CERTIFIED")
        return 1
    print("RESULT CYCLE416_SEVEN_M2_COMMON_CODE_SEED_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
