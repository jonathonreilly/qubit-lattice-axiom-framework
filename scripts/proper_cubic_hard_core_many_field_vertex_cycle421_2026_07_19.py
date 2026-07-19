#!/usr/bin/env python3
"""Cycle 421: proper-cubic hard-core many-field reservoir vertex.

Replace the vacuum-only source creation used by the Cycle-418 seed with the
hard-core scalar ladder A^dagger=(1/sqrt(6)) sum_d sigma_d^+.  The fixed
seven-M2 Hermitian generator sigma_R^- A^dagger + sigma_R^+ A acts on every
computational occupation where hard-core creation or annihilation is possible.

The conserved coordinate is reservoir-plus-field excitation number, not
energy, stress, a gravity source, a rate, or a Record.  Authority is none and
audit is unset.
"""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
from scipy import linalg, sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import cycle416_seven_m2_common_code_seed_cycle418_2026_07_19 as c418


c7 = c418.c7
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PROPER_CUBIC_HARD_CORE_MANY_FIELD_VERTEX_CYCLE421_NOTE_2026-07-19.md"
)
ANGLE = c418.ANGLE
FIELD_DIM = 64
LOCAL_DIM = 128
MATTER_DIM = 64
FULL_DIM = MATTER_DIM * LOCAL_DIM
PRIOR_TWO_FIELD_WEIGHT = 0.002201473975253681
PRIOR_MISSING_SOURCE_COORDINATE = -0.15248255286187232
TOLERANCE = 2e-12
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
        "hard-core scalar ladder",
        "every nonsaturated computational field occupation",
        "fixed seven-m2 hermitian generator",
        "reservoir-plus-field excitation number",
        "all 128 basis states",
        "cycle-418 vacuum seed",
        "all 24 proper-cubic frames",
        "saturation",
        "coupling deletion",
        "genuine two-field sector",
        "0.002201473975253681",
        "-0.15248255286187232",
        "m64 matter spectator",
        "not energy, stress, or a gravity source",
        "no negative, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-421 note states the many-field construction and exact boundary", not missing, missing)


def hard_core_raising(*, omit_direction: int | None = None) -> np.ndarray:
    if omit_direction is not None and omit_direction not in range(6):
        raise ValueError("omitted direction must be in range(6)")
    raising = np.zeros((FIELD_DIM, FIELD_DIM), dtype=complex)
    for state in range(FIELD_DIM):
        for direction in range(6):
            if direction == omit_direction or (state >> direction) & 1:
                continue
            raising[state | (1 << direction), state] += 1 / np.sqrt(6)
    return raising


def operators(*, omit_direction: int | None = None) -> dict[str, np.ndarray]:
    raising_field = hard_core_raising(omit_direction=omit_direction)
    lowering_field = raising_field.conj().T
    lowering_reservoir = np.asarray(((0, 1), (0, 0)), dtype=complex)
    raising_reservoir = lowering_reservoir.conj().T
    generator = np.kron(lowering_reservoir, raising_field) + np.kron(
        raising_reservoir, lowering_field
    )
    field_number = np.diag(
        np.asarray([state.bit_count() for state in range(FIELD_DIM)], dtype=float)
    ).astype(complex)
    reservoir_number = np.diag((0.0, 1.0)).astype(complex)
    field_lift = np.kron(np.eye(2), field_number)
    reservoir_lift = np.kron(reservoir_number, np.eye(FIELD_DIM))
    return {
        "raising": raising_field,
        "lowering": lowering_field,
        "H": generator,
        "F": field_lift,
        "R": reservoir_lift,
        "Q": field_lift + reservoir_lift,
    }


def vertex(angle: float = ANGLE, *, omit_direction: int | None = None) -> np.ndarray:
    return linalg.expm(-1j * angle * operators(omit_direction=omit_direction)["H"])


def basis(reservoir: int, field: int) -> np.ndarray:
    if reservoir not in (0, 1) or field not in range(FIELD_DIM):
        raise ValueError("basis labels outside M2 x M64")
    state = np.zeros(LOCAL_DIM, dtype=complex)
    state[reservoir * FIELD_DIM + field] = 1
    return state


def expectation(state: np.ndarray, observable: np.ndarray) -> float:
    return float(np.vdot(state, observable @ state).real)


def hard_core_ladder_controls() -> None:
    ops = operators()
    raising = ops["raising"]
    lowering = ops["lowering"]
    creation_rows = []
    annihilation_rows = []
    failures = 0
    for occupation in range(7):
        creation_norms = []
        annihilation_norms = []
        for state in range(FIELD_DIM):
            if state.bit_count() != occupation:
                continue
            ket = np.eye(FIELD_DIM, dtype=complex)[:, state]
            creation_norms.append(float(np.linalg.norm(raising @ ket)))
            annihilation_norms.append(float(np.linalg.norm(lowering @ ket)))
        creation_rows.append((occupation, min(creation_norms), max(creation_norms)))
        annihilation_rows.append((occupation, min(annihilation_norms), max(annihilation_norms)))
        if occupation < 6:
            failures += sum(norm <= 1e-15 for norm in creation_norms)
        else:
            failures += sum(norm != 0 for norm in creation_norms)
        if occupation > 0:
            failures += sum(norm <= 1e-15 for norm in annihilation_norms)
        else:
            failures += sum(norm != 0 for norm in annihilation_norms)
    check(
        "the scalar hard-core ladder creates from every nonsaturated computational field occupation and annihilates from every nonvacuum occupation",
        failures == 0
        and np.linalg.norm(lowering - raising.conj().T) == 0
        and np.linalg.norm(ops["H"] - ops["H"].conj().T) == 0,
        {
            "raising_nonzero_matrix_elements": int(np.count_nonzero(raising)),
            "expected_directed_hypercube_edges": 6 * 32,
            "creation_norm_ranges_by_occupation": creation_rows,
            "annihilation_norm_ranges_by_occupation": annihilation_rows,
            "generator_Hermiticity_residual": float(
                np.linalg.norm(ops["H"] - ops["H"].conj().T)
            ),
            "failures": failures,
        },
    )


def seed_intertwiner_controls() -> None:
    encoding = c418.seed()
    gate = vertex()
    logical = c418.logical_gate(1)
    projector = encoding @ encoding.conj().T
    intertwiner = float(np.linalg.norm(encoding @ logical - gate @ encoding))
    inverse = float(
        np.linalg.norm(encoding @ logical.conj().T - gate.conj().T @ encoding)
    )
    leakage = float(
        np.linalg.norm((np.eye(LOCAL_DIM) - projector) @ gate @ encoding)
    )
    source = encoding[:, 0]
    output = gate @ source
    ops = operators()
    transfer = expectation(output, ops["F"])
    check(
        "the genuine many-field vertex preserves the signed Cycle-418 vacuum seed, inverse, leakage, and transfer",
        intertwiner < 3e-15
        and inverse < 3e-15
        and leakage < 3e-15
        and abs(transfer - np.sin(ANGLE) ** 2) < 3e-14,
        {
            "angle": ANGLE,
            "seed_intertwiner_residual": intertwiner,
            "inverse_intertwiner_residual": inverse,
            "seed_leakage": leakage,
            "field_transfer": transfer,
            "Cycle418_transfer": float(np.sin(ANGLE) ** 2),
        },
    )


def all_basis_number_inverse_controls() -> None:
    ops = operators()
    gate = vertex()
    identity = np.eye(LOCAL_DIM, dtype=complex)
    inverse_error = gate.conj().T @ gate - identity
    basis_inverse = np.linalg.norm(inverse_error, axis=0)
    field_after = gate.conj().T @ ops["F"] @ gate
    reservoir_after = gate.conj().T @ ops["R"] @ gate
    ledger = field_after - ops["F"] + reservoir_after - ops["R"]
    check(
        "the fixed seven-M2 vertex is unitary on all 128 states and exactly conserves reservoir-plus-field number",
        np.linalg.norm(gate.conj().T @ gate - identity) < 5e-13
        and np.max(basis_inverse) < 8e-14
        and np.linalg.norm(gate @ ops["Q"] - ops["Q"] @ gate) < 3e-13
        and np.linalg.norm(ledger) < 8e-13,
        {
            "basis_states": LOCAL_DIM,
            "unitarity_Frobenius_residual": float(np.linalg.norm(inverse_error)),
            "maximum_basis_inverse_residual": float(np.max(basis_inverse)),
            "number_commutator": float(
                np.linalg.norm(gate @ ops["Q"] - ops["Q"] @ gate)
            ),
            "operator_number_ledger_residual": float(np.linalg.norm(ledger)),
        },
    )


def occupancy_saturation_deletion_controls() -> None:
    ops = operators()
    gate = vertex()
    rows = []
    failures = 0
    for occupation in range(7):
        emission_weights = []
        absorption_weights = []
        number_residuals = []
        for field in range(FIELD_DIM):
            if field.bit_count() != occupation:
                continue
            emitted = gate @ basis(1, field)
            absorbed = gate @ basis(0, field)
            emission_weights.append(
                1 - expectation(emitted, ops["R"])
            )
            absorption_weights.append(expectation(absorbed, ops["R"]))
            number_residuals.extend((
                abs(expectation(emitted, ops["Q"]) - (occupation + 1)),
                abs(expectation(absorbed, ops["Q"]) - occupation),
            ))
        if occupation < 6:
            failures += sum(weight <= 1e-15 for weight in emission_weights)
        else:
            failures += sum(abs(weight) > 2e-14 for weight in emission_weights)
        if occupation > 0:
            failures += sum(weight <= 1e-15 for weight in absorption_weights)
        else:
            failures += sum(abs(weight) > 2e-14 for weight in absorption_weights)
        failures += sum(residual > 5e-13 for residual in number_residuals)
        rows.append({
            "field_occupation": occupation,
            "computational_states": len(emission_weights),
            "emission_weight_range": (min(emission_weights), max(emission_weights)),
            "absorption_weight_range": (min(absorption_weights), max(absorption_weights)),
            "maximum_number_residual": max(number_residuals),
        })

    deleted = vertex(0.0)
    damaged = vertex(omit_direction=5)
    frame = next(
        frame for frame in c7.c210.proper_cubic_frames()
        if int(np.argmax(c7.c210.direction_permutation(frame)[:, 5])) != 5
    )
    representation = np.kron(
        np.eye(2), c7.field_bit_permutation(c7.c210.direction_permutation(frame))
    )
    damaged_covariance = float(
        np.linalg.norm(representation @ damaged - damaged @ representation)
    )
    damaged_seed = float(
        np.linalg.norm(c418.seed() @ c418.logical_gate(1) - damaged @ c418.seed())
    )
    check(
        "occupation, saturation, vacuum-absorption, and coupling/direction deletion controls are explicit",
        failures == 0
        and np.linalg.norm(deleted - np.eye(LOCAL_DIM)) == 0
        and damaged_covariance > 0.1
        and damaged_seed > 0.05,
        {
            "rows": rows,
            "failures": failures,
            "coupling_deletion_residual": float(
                np.linalg.norm(deleted - np.eye(LOCAL_DIM))
            ),
            "one_direction_deleted_covariance_residual": damaged_covariance,
            "one_direction_deleted_seed_residual": damaged_seed,
        },
    )


def covariance_controls() -> None:
    ops = operators()
    gate = vertex()
    generator_residuals = []
    gate_residuals = []
    for frame in c7.c210.proper_cubic_frames():
        representation = np.kron(
            np.eye(2),
            c7.field_bit_permutation(c7.c210.direction_permutation(frame)),
        )
        generator_residuals.append(
            float(np.linalg.norm(representation @ ops["H"] - ops["H"] @ representation))
        )
        gate_residuals.append(
            float(np.linalg.norm(representation @ gate - gate @ representation))
        )
    check(
        "the hard-core scalar generator and finite vertex commute with all 24 proper-cubic frames",
        len(generator_residuals) == 24
        and max(generator_residuals) < 3e-14
        and max(gate_residuals) < 5e-13,
        {
            "frames": len(generator_residuals),
            "maximum_generator_covariance_residual": max(generator_residuals),
            "maximum_gate_covariance_residual": max(gate_residuals),
        },
    )


def two_vertex_controls() -> None:
    gate = vertex()
    ops = operators()
    local_initial = basis(1, 0)
    local_output = gate @ local_initial
    joint_initial = np.outer(local_initial, local_initial)
    joint_output = np.outer(local_output, local_output)
    restored = gate.conj().T @ joint_output @ gate.conj()
    field_counts = np.diag(ops["F"]).real
    reservoir_counts = np.diag(ops["R"]).real
    probabilities = abs(joint_output) ** 2
    two_field_mask = (
        field_counts[:, None] + field_counts[None, :]
    ) == 2
    total_q = (
        field_counts[:, None]
        + field_counts[None, :]
        + reservoir_counts[:, None]
        + reservoir_counts[None, :]
    )
    two_field_weight = float(np.sum(probabilities[two_field_mask]))
    q2_leakage = float(np.sum(probabilities[abs(total_q - 2) > 1e-12]))
    expected = float(np.sin(ANGLE) ** 4)
    comparison = {
        "current_two_independent_vertex_weight": two_field_weight,
        "prior_two_tick_weight": PRIOR_TWO_FIELD_WEIGHT,
        "difference": two_field_weight - PRIOR_TWO_FIELD_WEIGHT,
        "ratio": two_field_weight / PRIOR_TWO_FIELD_WEIGHT,
        "prior_missing_source_coordinate": PRIOR_MISSING_SOURCE_COORDINATE,
        "missing_source_coordinate_closed_here": False,
        "comparison_semantics": "different supplied schedule and initial condition; diagnostic comparison, not a target match",
    }
    check(
        "two independent Q_total=2 reservoir vertices produce a genuine two-field sector with exact inverse and no blockade",
        abs(two_field_weight - expected) < 5e-14
        and two_field_weight > 0
        and q2_leakage < 3e-15
        and np.linalg.norm(restored - joint_initial) < 8e-14,
        {
            "joint_dimension": LOCAL_DIM**2,
            "two_field_weight": two_field_weight,
            "expected_sin4": expected,
            "Q_total_2_leakage": q2_leakage,
            "joint_inverse_residual": float(np.linalg.norm(restored - joint_initial)),
            "prior_comparison": comparison,
        },
    )


def m64_spectator_contact_controls() -> None:
    gate = sparse.csr_matrix(vertex())
    matter_identity = sparse.eye(MATTER_DIM, format="csr", dtype=complex)
    full = sparse.kron(matter_identity, gate, format="csr")
    identity = sparse.eye(FULL_DIM, format="csr", dtype=complex)
    inverse_error = full.getH() @ full - identity
    matter_number = np.asarray(
        [state.bit_count() for state in range(MATTER_DIM)], dtype=float
    )
    contact_phases = np.exp(
        1j
        * c7.c230.COUPLING
        * matter_number
        * (matter_number - 1)
        / 2
    )
    contact = sparse.kron(
        sparse.diags(contact_phases, format="csr"),
        sparse.eye(LOCAL_DIM, format="csr", dtype=complex),
        format="csr",
    )
    contact_residual = float(sparse.linalg.norm(full @ contact - contact @ full))
    row, column = full.nonzero()
    matter_leakage = int(np.count_nonzero(row // LOCAL_DIM != column // LOCAL_DIM))
    check(
        "one complete M64 matter cell is an exact spectator and its intrinsic contact commutes with the many-field vertex",
        full.shape == (FULL_DIM, FULL_DIM)
        and float(sparse.linalg.norm(inverse_error)) < 5e-12
        and contact_residual == 0
        and matter_leakage == 0,
        {
            "basis_dimension": FULL_DIM,
            "sparse_nonzeros": int(full.nnz),
            "unitarity_Frobenius_residual": float(sparse.linalg.norm(inverse_error)),
            "contact_commutator": contact_residual,
            "matter_block_leakage": matter_leakage,
            "matter_action": "identity spectator",
        },
    )


def domain_inventory_controls() -> None:
    rejections = 0
    for probe in (
        lambda: hard_core_raising(omit_direction=6),
        lambda: basis(2, 0),
        lambda: basis(1, 64),
    ):
        try:
            probe()
        except ValueError:
            rejections += 1
    inventory = {
        "supplied": (
            "Cycle418 signed vacuum common-code seed and fixed angle",
            "one reservoir M2 and six ordinary hard-core directional field M2",
            "permutation-scalar equal-weight hard-core raising convention",
            "one M64 matter spectator, intrinsic contact phases, and proper-cubic representations",
            "two independent prepared reservoir excitations for the Q_total=2 control",
        ),
        "derived": (
            "fixed Hermitian seven-M2 generator acting on every creatable/annihilable computational occupation",
            "all-128 unitarity/inverse, exact R+F ledger, saturation and deletion controls",
            "Cycle418 vacuum intertwiner/transfer preservation and all-24 covariance",
            "genuine two-field output from two independent local vertices",
        ),
        "open": (
            "normalization or selection of this hard-core ladder as a physical source law",
            "field coin/stream, carried reservoir, repeated same-block history, recoil, and source work",
            "closure of the prior missing source coordinate and reconciliation with its different two-tick schedule",
            "energy/stress/gravity interpretation, actual Records, time, and metric response",
        ),
        "host_expectation_queries": 0,
        "global_field_blockade": False,
        "prior_missing_source_coordinate_closed": False,
        "actual_Records_added": 0,
        "number_called_energy": False,
        "physical_source_selected": False,
        "negative_or_minimum_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
    }
    check(
        "lawful domains and supplied/derived/open inventory keep the many-field vertex separate from source interpretation",
        rejections == 3
        and not inventory["global_field_blockade"]
        and not inventory["prior_missing_source_coordinate_closed"]
        and not inventory["number_called_energy"]
        and not inventory["physical_source_selected"]
        and not inventory["negative_or_minimum_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        {"domain_rejections": rejections, **inventory},
    )


def main() -> int:
    print("CYCLE 421: PROPER-CUBIC HARD-CORE MANY-FIELD RESERVOIR VERTEX")
    note_contract()
    hard_core_ladder_controls()
    seed_intertwiner_controls()
    all_basis_number_inverse_controls()
    occupancy_saturation_deletion_controls()
    covariance_controls()
    two_vertex_controls()
    m64_spectator_contact_controls()
    domain_inventory_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PROPER_CUBIC_HARD_CORE_MANY_FIELD_VERTEX_NOT_CERTIFIED")
        return 1
    print("RESULT PROPER_CUBIC_HARD_CORE_MANY_FIELD_VERTEX_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
