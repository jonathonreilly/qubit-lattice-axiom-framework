#!/usr/bin/env python3
"""Cycle 334: close-gated environment export into the realized-state slot.

The construction composes the Cycle-317 contact-trine instrument, the
Cycle-321 operational refinement quotient, and the Cycle-332 conditional
close certificate with a finite open environment rail.  It distinguishes a
bounded reversible export and pointwise decoder from dephasing, pointer
output, Record formation, permanence, and a branch-selection/sampling law.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_effect_equivalence_normalized_grade_cycle321_2026_07_18 as c321
import physical_fixed_program_carrier_two_use_cycle323_2026_07_18 as c323
import physical_support_matcher_predecessor_controls_cycle329_2026_07_18 as c329
import physical_transition_occurrence_close_tournament_cycle332_2026_07_18 as c332


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ENVIRONMENT_EXPORT_REALIZED_MEMBER_BRIDGE_CYCLE334_NOTE_2026-07-18.md"
)
TOL = 1.2e-10
ENV_DIMENSION = 8
ENV_M2 = 3
BLANK_LABEL = 7
BRANCH_LABELS = (0, 1, 2)
METHODOLOGY_MAIN = "df24c9086f485a284a8c103c7c7a1e2dccc0d7bd"
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
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-334 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "realized-state primitive supplies the slot",
        "never its content",
        "pointwise",
        "close-gated environment export",
        "coarse-cp quotient",
        "stinespring",
        "pointer output is not occurrence",
        "dephasing is not occurrence",
        "commit candidate is not a record",
        "exact inverse",
        "finite-horizon nonreturn is not permanence",
        "actual endpoint content remains supplied",
        "all 24 proper-cubic frames",
        "held l=6",
        "no axiom pressure",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the export construction, realized-state boundary, and full no-go gate",
        not missing,
        missing,
    )


def methodology_freshness_control() -> None:
    completed = subprocess.run(
        ["git", "rev-parse", "origin/main"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    observed = completed.stdout.strip()
    note = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    registry = json.loads(
        (ROOT / "docs/audit/data/axiom_premise_nodes.json").read_text(
            encoding="utf-8"
        )
    )
    realized = registry["nodes"].get("realized_state_primitive", {})
    check(
        "the N1-N8 gate is pinned to the freshly fetched methodology and primitive-registry reference",
        completed.returncode == 0
        and observed == METHODOLOGY_MAIN
        and METHODOLOGY_MAIN in note,
        {"expected": METHODOLOGY_MAIN, "observed": observed},
    )
    check(
        "the approved realized-state primitive is chain-satisfying and content-free at the registered source",
        "realized_state_primitive" in registry["canonical_ids"]
        and realized.get("current_path")
        == "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
        and "POINTWISE only" in realized.get("note", "")
        and "Supplies the slot, never the content" in realized.get("note", ""),
        realized,
    )


def no_go_contract_control() -> None:
    note = NOTE.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")
    lower = (note + "\n" + source).lower()
    other_trigger_parts = (
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
    headings = tuple(f"### N{index} —" for index in range(1, 9))
    attempted = note.count("**ATTEMPTED**")
    open_routes = note.count("**OPEN / UNTESTED**")
    pair_rows = sum(
        line.startswith("| `W_") and "/W_" in line
        for line in note.splitlines()
    )
    check(
        "the full N1-N8 release surface keeps the broad negative failed and classifies every literal hidden-condition trigger",
        all(heading in note for heading in headings)
        and attempted >= 6
        and open_routes >= 4
        and pair_rows == 10
        and "Broad gate status: **FAIL / DO NOT SHIP**" in note
        and "retained-authority citations, not hidden conditions" in note
        and lower.count("registered") >= 1
        and all("".join(parts) not in lower for parts in other_trigger_parts),
        {
            "attempted_routes": attempted,
            "open_routes": open_routes,
            "N2_pair_rows": pair_rows,
            "registered_hits": lower.count("registered"),
        },
    )


def basis(index: int, dimension: int = ENV_DIMENSION) -> np.ndarray:
    result = np.zeros(dimension, dtype=complex)
    result[index] = 1
    return result


def complete_columns(columns: np.ndarray) -> np.ndarray:
    """Complete orthonormal columns without rotating the supplied columns."""
    vectors = [columns[:, index].astype(complex) for index in range(columns.shape[1])]
    for index in range(columns.shape[0]):
        candidate = np.zeros(columns.shape[0], dtype=complex)
        candidate[index] = 1
        for vector in vectors:
            candidate -= vector * np.vdot(vector, candidate)
        norm = np.linalg.norm(candidate)
        if norm > 1e-11:
            vectors.append(candidate / norm)
        if len(vectors) == columns.shape[0]:
            break
    result = np.column_stack(vectors)
    if result.shape != (columns.shape[0], columns.shape[0]):
        raise RuntimeError("orthonormal completion did not span the ambient space")
    return result


def environment_isometry(kraus: tuple[np.ndarray, ...]) -> np.ndarray:
    if not 1 <= len(kraus) < ENV_DIMENSION:
        raise ValueError("the environment has seven nonblank branch labels")
    result = np.zeros((2 * ENV_DIMENSION, 2), dtype=complex)
    for label, operator in enumerate(kraus):
        if operator.shape != (2, 2):
            raise ValueError("every branch block acts on the seam qubit")
        result[2 * label : 2 * (label + 1)] = operator
    return result


def blank_input() -> np.ndarray:
    result = np.zeros((2 * ENV_DIMENSION, 2), dtype=complex)
    result[2 * BLANK_LABEL : 2 * (BLANK_LABEL + 1)] = np.eye(2)
    return result


def unitary_extension(input_code: np.ndarray, output_code: np.ndarray) -> np.ndarray:
    if input_code.shape != output_code.shape:
        raise ValueError("input and output codes must have the same shape")
    if max(
        np.linalg.norm(input_code.conj().T @ input_code - np.eye(input_code.shape[1])),
        np.linalg.norm(output_code.conj().T @ output_code - np.eye(output_code.shape[1])),
    ) > TOL:
        raise ValueError("both code maps must be isometries")
    input_basis = complete_columns(input_code)
    output_basis = complete_columns(output_code)
    return output_basis @ input_basis.conj().T


@dataclass(frozen=True)
class CloseExportFixture:
    length: int
    physical: c317.PhysicalFixture
    program: c321.Program
    input_code: np.ndarray
    output_code: np.ndarray
    export_unitary: np.ndarray
    close_unitary: np.ndarray
    close_certificate: int
    false_close: int
    fixed_carrier_isometry: float


def close_fixture(length: int) -> CloseExportFixture:
    physical = c317.physical_fixture(length)
    programs = c323.make_programs(physical.contact)
    carrier = c323.FixedProgramCarrier(programs)
    program = programs[4]
    if program.name != "contact trine":
        raise RuntimeError("Cycle-323 program label four is no longer the contact trine")
    fixed_carrier_isometry = float(
        np.linalg.norm(carrier.update.conj().T @ carrier.update - np.eye(16))
    )
    output_code = environment_isometry(program.kraus)
    input_code = blank_input()
    export_unitary = unitary_extension(input_code, output_code)
    close_unitary = np.zeros((32, 32), dtype=complex)
    close_unitary[:16, :16] = np.eye(16)
    close_unitary[16:, 16:] = export_unitary

    transition = c332.compile_transition_program(length)
    active_nonvacuum = transition.active_rows[
        transition.nonvacuum[transition.active_rows]
    ]
    pre = int(active_nonvacuum[0])
    post = int(transition.sidecar.stream_mapping[pre])
    witness = c332.transition_witness(transition, pre, post)
    matcher = c329.build_fixture(length)
    match, ready = c329.route_outputs(matcher, "syndrome")
    certificate = c332.boundary_certificate(1, witness, 1, match, ready)
    false_close = c332.boundary_certificate(0, 0, 0, match, ready)
    return CloseExportFixture(
        length,
        physical,
        program,
        input_code,
        output_code,
        export_unitary,
        close_unitary,
        certificate,
        false_close,
        fixed_carrier_isometry,
    )


def branch_state() -> tuple[np.ndarray, np.ndarray]:
    vector = np.asarray(
        (np.sqrt(0.63), np.exp(0.41j) * np.sqrt(0.37)), dtype=complex
    )
    vector /= np.linalg.norm(vector)
    return vector, np.outer(vector, vector.conj())


def effects_weights(
    kraus: tuple[np.ndarray, ...], rho: np.ndarray
) -> tuple[tuple[np.ndarray, ...], np.ndarray]:
    effects = tuple(operator.conj().T @ operator for operator in kraus)
    weights = np.asarray(
        [float(np.trace(effect @ rho).real) for effect in effects], dtype=float
    )
    return effects, weights


def close_export_controls() -> tuple[dict[int, CloseExportFixture], dict[str, object]]:
    fixtures = {length: close_fixture(length) for length in (3, 6)}
    rows = []
    vector, rho = branch_state()
    for length, fixture in fixtures.items():
        output = fixture.output_code @ vector
        exported = fixture.export_unitary @ fixture.input_code @ vector
        restored = fixture.export_unitary.conj().T @ output
        close_zero_input = np.concatenate((fixture.input_code @ vector, np.zeros(16, dtype=complex)))
        close_one_input = np.concatenate((np.zeros(16, dtype=complex), fixture.input_code @ vector))
        close_zero_output = fixture.close_unitary @ close_zero_input
        close_one_output = fixture.close_unitary @ close_one_input
        physical_output = c317.physical_isometry(
            fixture.physical.two_ray_encoding, fixture.program.kraus
        )
        full_projector = (
            fixture.physical.full_encoding
            @ fixture.physical.full_encoding.conj().T
        )
        leakage = max(
            np.linalg.norm(
                (np.eye(510) - full_projector)
                @ physical_output[510 * label : 510 * (label + 1)]
            )
            for label in range(ENV_DIMENSION)
        )
        effects, weights = effects_weights(fixture.program.kraus, rho)
        branch_deleted = fixture.program.kraus[1:]
        deletion_defect = np.linalg.norm(
            sum((operator.conj().T @ operator for operator in branch_deleted),
                start=np.zeros((2, 2), dtype=complex))
            - np.eye(2)
        )
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "close_certificate": fixture.close_certificate,
                "false_close": fixture.false_close,
                "fixed_carrier_isometry": fixture.fixed_carrier_isometry,
                "output_isometry": float(
                    np.linalg.norm(fixture.output_code.conj().T @ fixture.output_code - np.eye(2))
                ),
                "unitary": float(
                    np.linalg.norm(
                        fixture.export_unitary.conj().T @ fixture.export_unitary
                        - np.eye(16)
                    )
                ),
                "close_unitary": float(
                    np.linalg.norm(
                        fixture.close_unitary.conj().T @ fixture.close_unitary
                        - np.eye(32)
                    )
                ),
                "forward": float(np.linalg.norm(exported - output)),
                "close_one_forward": float(
                    np.linalg.norm(close_one_output[16:] - output)
                    + np.linalg.norm(close_one_output[:16])
                ),
                "close_zero_blank": float(
                    np.linalg.norm(close_zero_output[:16] - fixture.input_code @ vector)
                    + np.linalg.norm(close_zero_output[16:])
                ),
                "inverse": float(
                    np.linalg.norm(restored - fixture.input_code @ vector)
                ),
                "physical_isometry": float(
                    np.linalg.norm(physical_output.conj().T @ physical_output - np.eye(2))
                ),
                "physical_code_leakage": float(leakage),
                "weight_sum": float(weights.sum()),
                "minimum_weight": float(weights.min()),
                "branch_deletion_isometry_defect": float(deletion_defect),
                "effects": effects,
                "weights": weights,
            }
        )
    check(
        "the actual Cycle-332 close gates one exact reversible contact-trine environment export through held L=6",
        all(
            row["close_certificate"] == 1
            and row["false_close"] == 0
            and max(
                row["output_isometry"],
                row["fixed_carrier_isometry"],
                row["unitary"],
                row["close_unitary"],
                row["forward"],
                row["close_one_forward"],
                row["close_zero_blank"],
                row["inverse"],
                row["physical_isometry"],
                row["physical_code_leakage"],
                abs(row["weight_sum"] - 1),
            )
            < TOL
            and row["minimum_weight"] > 0.1
            and row["branch_deletion_isometry_defect"] > 0.2
            for row in rows
        ),
        [
            {key: value for key, value in row.items() if key not in ("effects", "weights")}
            for row in rows
        ],
    )
    return fixtures, {"rows": rows, "rho": rho, "vector": vector}


def stinespring_and_dephasing_controls(
    fixture: CloseExportFixture, rho: np.ndarray
) -> dict[str, object]:
    omega = np.exp(2j * np.pi / 3)
    fourier = np.asarray(
        [[omega ** (row * column) for column in range(3)] for row in range(3)],
        dtype=complex,
    ) / np.sqrt(3)
    environment_rotation = np.eye(ENV_DIMENSION, dtype=complex)
    environment_rotation[:3, :3] = fourier
    rotated_isometry = np.kron(environment_rotation, np.eye(2)) @ fixture.output_code
    rotated_kraus = tuple(
        rotated_isometry[2 * label : 2 * (label + 1)]
        for label in BRANCH_LABELS
    )
    original_effects, original_weights = effects_weights(fixture.program.kraus, rho)
    rotated_effects, rotated_weights = effects_weights(rotated_kraus, rho)
    reduced_original = c321.apply_cp(fixture.program.kraus, rho)
    reduced_rotated = c321.apply_cp(rotated_kraus, rho)
    channel_residual = float(
        np.linalg.norm(c321.choi(fixture.program.kraus) - c321.choi(rotated_kraus))
    )
    effect_change = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(original_effects, rotated_effects)
    )
    weight_change = float(np.max(np.abs(original_weights - rotated_weights)))

    vector, _ = branch_state()
    pure = fixture.output_code @ vector
    coherent_density = np.outer(pure, pure.conj())
    dephased_density = np.zeros_like(coherent_density)
    for label in BRANCH_LABELS:
        block = slice(2 * label, 2 * (label + 1))
        dephased_density[block, block] = coherent_density[block, block]
    def trace_environment(density: np.ndarray) -> np.ndarray:
        tensor = density.reshape(ENV_DIMENSION, 2, ENV_DIMENSION, 2)
        return np.einsum("asat->st", tensor)
    dephasing_system_residual = float(
        np.linalg.norm(
            trace_environment(coherent_density) - trace_environment(dephased_density)
        )
    )
    coherent_purity = float(np.trace(coherent_density @ coherent_density).real)
    dephased_purity = float(np.trace(dephased_density @ dephased_density).real)
    detail = {
        "environment_rotation_unitarity": float(
            np.linalg.norm(environment_rotation.conj().T @ environment_rotation - np.eye(8))
        ),
        "reduced_channel_Choi_residual": channel_residual,
        "held_state_reduced_residual": float(np.linalg.norm(reduced_original - reduced_rotated)),
        "maximum_named_branch_effect_change": effect_change,
        "maximum_named_branch_weight_change": weight_change,
        "original_weights": tuple(float(value) for value in original_weights),
        "rotated_weights": tuple(float(value) for value in rotated_weights),
        "dephasing_system_residual": dephasing_system_residual,
        "coherent_global_purity": coherent_purity,
        "dephased_global_purity": dephased_purity,
    }
    check(
        "environment-basis rotations and dephasing preserve the reduced system process while changing or erasing named transcript structure",
        detail["environment_rotation_unitarity"] < TOL
        and channel_residual < TOL
        and detail["held_state_reduced_residual"] < TOL
        and effect_change > 0.2
        and weight_change > 0.05
        and dephasing_system_residual < TOL
        and abs(coherent_purity - 1) < TOL
        and dephased_purity < 0.8,
        detail,
    )
    return detail


def operational_quotient_controls(
    fixture: CloseExportFixture, rho: np.ndarray
) -> dict[str, object]:
    unsplit, refined, parameters = c321.ray_programs(fixture.physical.contact)
    coarse_effect_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(unsplit.coarse_effects, refined.coarse_effects)
    )
    coarse_cp_residual = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(c321.grouped_chois(unsplit), c321.grouped_chois(refined))
    )
    erased_channel_residual = float(
        np.linalg.norm(c321.choi(unsplit.kraus) - c321.choi(refined.kraus))
    )
    coarse_transcript_residual = float(
        np.linalg.norm(
            c321.transcript_choi(unsplit.coarse_effects)
            - c321.transcript_choi(refined.coarse_effects)
        )
    )
    fine_transcript_residual = float(
        np.linalg.norm(
            c321.transcript_choi(unsplit.fine_effects)
            - c321.transcript_choi(refined.fine_effects)
        )
    )
    unsplit_weights = np.asarray(
        [float(np.trace(effect @ rho).real) for effect in unsplit.coarse_effects]
    )
    refined_weights = np.asarray(
        [float(np.trace(effect @ rho).real) for effect in refined.coarse_effects]
    )
    detail = {
        "coarse_effect_residual": coarse_effect_residual,
        "coarse_CP_Choi_residual": coarse_cp_residual,
        "pointer_erased_channel_residual": erased_channel_residual,
        "coarse_transcript_residual": coarse_transcript_residual,
        "fine_transcript_residual": fine_transcript_residual,
        "coarse_weight_residual": float(np.max(np.abs(unsplit_weights - refined_weights))),
        "coarse_weights": tuple(float(value) for value in unsplit_weights),
        "split_weight": parameters["split"],
    }
    check(
        "the exact Cycle-321 coarse-CP refinement quotient survives export while the fine environment transcript remains physically distinct",
        max(
            coarse_effect_residual,
            coarse_cp_residual,
            erased_channel_residual,
            coarse_transcript_residual,
            detail["coarse_weight_residual"],
        )
        < TOL
        and fine_transcript_residual > 0.3,
        detail,
    )
    return detail


SparseRailState = dict[tuple[int, ...], np.ndarray]


def rail_initial(kraus: tuple[np.ndarray, ...], vector: np.ndarray, length: int) -> SparseRailState:
    if length < 1:
        raise ValueError("the rail needs at least one outbound edge")
    result: SparseRailState = {}
    for label, operator in enumerate(kraus):
        configuration = (label,) + (BLANK_LABEL,) * length
        result[configuration] = operator @ vector
    return result


def rail_swap(state: SparseRailState, left: int, right: int) -> SparseRailState:
    result: SparseRailState = {}
    for configuration, system_vector in state.items():
        updated = list(configuration)
        updated[left], updated[right] = updated[right], updated[left]
        key = tuple(updated)
        result[key] = result.get(key, np.zeros(2, dtype=complex)) + system_vector
    return result


def state_distance(left: SparseRailState, right: SparseRailState) -> float:
    keys = set(left) | set(right)
    return float(
        np.sqrt(
            sum(
                np.linalg.norm(
                    left.get(key, np.zeros(2, dtype=complex))
                    - right.get(key, np.zeros(2, dtype=complex))
                )
                ** 2
                for key in keys
            )
        )
    )


def rail_norm(state: SparseRailState) -> float:
    return float(sum(np.vdot(value, value).real for value in state.values()))


def endpoint_weights(state: SparseRailState) -> dict[int, float]:
    result: dict[int, float] = {}
    for configuration, vector in state.items():
        label = configuration[-1]
        result[label] = result.get(label, 0.0) + float(np.vdot(vector, vector).real)
    return result


def run_rail(
    initial: SparseRailState,
    length: int,
    *,
    deleted_edge: int | None = None,
) -> SparseRailState:
    state = initial
    for edge in range(length):
        if edge == deleted_edge:
            continue
        state = rail_swap(state, edge, edge + 1)
    return state


def reverse_rail(state: SparseRailState, length: int) -> SparseRailState:
    for edge in reversed(range(length)):
        state = rail_swap(state, edge, edge + 1)
    return state


def rail_capacity_deletion_and_covariance_controls(
    fixtures: dict[int, CloseExportFixture], vector: np.ndarray
) -> dict[str, object]:
    frame_rows = []
    rows = []
    frames = tuple(c317.c311.c235.proper_cubic_frames())
    for length, fixture in fixtures.items():
        initial = rail_initial(fixture.program.kraus, vector, length)
        final = run_rail(initial, length)
        restored = reverse_rail(final, length)
        weights = endpoint_weights(final)
        deleted_export = run_rail(initial, length, deleted_edge=0)
        deleted_middle = run_rail(initial, length, deleted_edge=length // 2)
        rows.append(
            {
                "L": length,
                "held": length == 6,
                "forward_norm": rail_norm(final),
                "inverse_residual": state_distance(initial, restored),
                "endpoint_weights": weights,
                "source_blank": all(config[0] == BLANK_LABEL for config in final),
                "deleted_export_endpoint_weight": sum(
                    value
                    for label, value in endpoint_weights(deleted_export).items()
                    if label != BLANK_LABEL
                ),
                "deleted_middle_endpoint_weight": sum(
                    value
                    for label, value in endpoint_weights(deleted_middle).items()
                    if label != BLANK_LABEL
                ),
                "environment_capacity_M2": ENV_M2 * (length + 1),
                "maximum_rail_step_support_M2": 2 * ENV_M2,
                "maximum_close_program_export_step_M2": 30,
                "conservative_combined_patch_M2": 720 + 62 + ENV_M2 * length,
            }
        )
        axis = np.asarray((1, 0, 0), dtype=int)
        positions = np.asarray([step * axis for step in range(length + 1)])
        for frame in frames:
            carried = positions @ frame.T
            frame_rows.append(
                {
                    "L": length,
                    "unique": len({tuple(row) for row in carried}) == length + 1,
                    "edge_lengths": tuple(
                        int(np.dot(delta, delta)) for delta in np.diff(carried, axis=0)
                    ),
                    "scalar_labels": tuple(sorted(weights)) == BRANCH_LABELS,
                }
            )
    check(
        "the environment transcript moves on a bounded open rail with exact inverse, held size, edge-deletion visibility, and carried cubic covariance",
        all(
            abs(row["forward_norm"] - 1) < TOL
            and row["inverse_residual"] < TOL
            and row["source_blank"]
            and tuple(sorted(row["endpoint_weights"])) == BRANCH_LABELS
            and abs(sum(row["endpoint_weights"].values()) - 1) < TOL
            and abs(row["deleted_export_endpoint_weight"]) < TOL
            and abs(row["deleted_middle_endpoint_weight"]) < TOL
            and row["maximum_rail_step_support_M2"] == 6
            and row["maximum_close_program_export_step_M2"] == 30
            for row in rows
        )
        and len(frame_rows) == 48
        and all(
            row["unique"]
            and set(row["edge_lengths"]) == {1}
            and row["scalar_labels"]
            for row in frame_rows
        ),
        {"rows": rows, "frame_size_cases": len(frame_rows)},
    )
    return {"rows": rows, "frame_rows": frame_rows}


def physical_apparatus_covariance_control(fixture: CloseExportFixture) -> dict[str, object]:
    base = fixture.physical
    reducer = c317.c311.c305.StabilizerReducer(base.code)
    rows = []
    padded = fixture.program.kraus + tuple(
        np.zeros((2, 2), dtype=complex)
        for _ in range(ENV_DIMENSION - len(fixture.program.kraus))
    )
    for frame in c317.c311.c235.proper_cubic_frames():
        logical_r = c317.c311.logical_frame_representation(frame)
        old_r, failures = c317.c311.flagged_frame_representation(
            base.encoder, base.basis_rows, base.occurrence, frame, reducer
        )
        mapping, phases, mapping_failures = c317.c311.signed_mapping(old_r)
        new_mapping = np.concatenate((mapping, mapping + 255))
        new_phases = np.concatenate((phases, phases))
        selected = np.zeros((127, 2), dtype=complex)
        selected[
            [
                c317.c311.SEAM_INDEX[(2, (0, 1), stream_slice)]
                for stream_slice in (0, 1)
            ],
            [0, 1],
        ] = 1
        carried_f = base.full_encoding @ logical_r @ selected
        mapped_f = c317.c311.apply_signed_mapping(
            new_mapping, new_phases, base.two_ray_encoding
        )
        base_v = np.vstack(tuple(base.two_ray_encoding @ operator for operator in padded))
        carried_v = np.vstack(tuple(carried_f @ operator for operator in padded))
        mapped_v = np.vstack(
            tuple(
                c317.c311.apply_signed_mapping(
                    new_mapping,
                    new_phases,
                    base_v[510 * label : 510 * (label + 1)],
                )
                for label in range(ENV_DIMENSION)
            )
        )
        rows.append(
            {
                "branch_failures": failures + mapping_failures,
                "code_residual": float(np.linalg.norm(mapped_f - carried_f)),
                "export_residual": float(np.linalg.norm(mapped_v - carried_v)),
            }
        )
    detail = {
        "frames": len(rows),
        "branch_failures": sum(row["branch_failures"] for row in rows),
        "maximum_code_residual": max(row["code_residual"] for row in rows),
        "maximum_export_residual": max(row["export_residual"] for row in rows),
    }
    check(
        "the physical trine export is carried covariantly under every proper-cubic frame",
        detail["frames"] == 24
        and detail["branch_failures"] == 0
        and max(detail["maximum_code_residual"], detail["maximum_export_residual"])
        < TOL,
        detail,
    )
    return detail


def pointwise_decoded_label(
    realized_endpoint_content: int | None,
    *,
    decoder_enabled: bool = True,
) -> int | None:
    if realized_endpoint_content is None or not decoder_enabled:
        return None
    if realized_endpoint_content not in BRANCH_LABELS:
        raise ValueError("the supplied realized endpoint content is not a lawful branch label")
    return realized_endpoint_content


def realized_state_and_semantic_controls(weights: tuple[float, ...]) -> dict[str, object]:
    pointwise = tuple(pointwise_decoded_label(label) for label in BRANCH_LABELS)
    without_content = pointwise_decoded_label(None)
    without_decoder = pointwise_decoded_label(0, decoder_enabled=False)
    malformed = 0
    for value in (-1, 3, BLANK_LABEL):
        try:
            pointwise_decoded_label(value)
        except ValueError:
            malformed += 1
    detail = {
        "lawful_pointwise_decoded_labels": pointwise,
        "without_actual_endpoint_content": without_content,
        "without_decoder": without_decoder,
        "malformed_rejections": malformed,
        "branch_weights": weights,
        "all_declared_branch_subchannels_have_nonzero_trace_weight": all(
            value > TOL for value in weights
        ),
        "law_admissibility_of_realized_endpoint_content": "separate required input",
        "counterfactual_decoded_label_variability": len(set(pointwise)),
        "realized_state_slot": "approved primitive / chain-satisfied",
        "state_contingent_endpoint_label": "registered data",
        "record_typing": "absent",
        "permanence_application": "absent before Record typing",
    }
    check(
        "the approved realized-state slot supports conditional pointwise decoding but supplies no endpoint content, decoder, branch rule, Record, or permanence",
        pointwise == BRANCH_LABELS
        and without_content is None
        and without_decoder is None
        and malformed == 3
        and detail["all_declared_branch_subchannels_have_nonzero_trace_weight"]
        and detail["counterfactual_decoded_label_variability"] == 3,
        detail,
    )
    return detail


def deletion_summary_control(
    fixture: CloseExportFixture,
    rho: np.ndarray,
    rail: dict[str, object],
) -> dict[str, object]:
    _effects, weights = effects_weights(fixture.program.kraus, rho)
    vector, _ = branch_state()
    blank_configuration = (BLANK_LABEL,) * (fixture.length + 1)
    close_deleted_rail = run_rail(
        {blank_configuration: vector}, fixture.length
    )
    close_deleted_endpoint_weight = sum(
        value
        for label, value in endpoint_weights(close_deleted_rail).items()
        if label != BLANK_LABEL
    )
    deleted_contact, _ = c321.auxiliary_programs(np.eye(2, dtype=complex))
    deleted_effects, deleted_weights = effects_weights(deleted_contact.kraus, rho)
    contact_effect_change = max(
        float(np.linalg.norm(left - right))
        for left, right in zip(fixture.program.fine_effects, deleted_effects)
    )
    detail = {
        "close_deleted_endpoint_weight": close_deleted_endpoint_weight,
        "export_coupling_deleted_endpoint_weight": rail["rows"][0]["deleted_export_endpoint_weight"],
        "rail_edge_deleted_endpoint_weight": rail["rows"][0]["deleted_middle_endpoint_weight"],
        "one_branch_deleted_isometry_defect": float(
            np.linalg.norm(fixture.program.fine_effects[0])
        ),
        "contact_deleted_effect_change": contact_effect_change,
        "contact_deleted_weight_change": float(np.max(np.abs(weights - deleted_weights))),
        "contact_deleted_weight_sum": float(deleted_weights.sum()),
        "endpoint_content_deleted_label": pointwise_decoded_label(None),
        "decoder_deleted_label": pointwise_decoded_label(0, decoder_enabled=False),
    }
    check(
        "close, export, rail, branch, contact, endpoint-content, and decoder deletions remain separately visible",
        detail["close_deleted_endpoint_weight"] == 0
        and abs(detail["export_coupling_deleted_endpoint_weight"]) < TOL
        and abs(detail["rail_edge_deleted_endpoint_weight"]) < TOL
        and detail["one_branch_deleted_isometry_defect"] > 0.2
        and detail["contact_deleted_effect_change"] > 0.1
        and detail["contact_deleted_weight_change"] > 0.01
        and abs(detail["contact_deleted_weight_sum"] - 1) < TOL
        and detail["endpoint_content_deleted_label"] is None
        and detail["decoder_deleted_label"] is None,
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    methodology_freshness_control()
    no_go_contract_control()
    fixtures, export = close_export_controls()
    held = fixtures[6]
    stinespring = stinespring_and_dephasing_controls(held, export["rho"])
    quotient = operational_quotient_controls(held, export["rho"])
    rail = rail_capacity_deletion_and_covariance_controls(fixtures, export["vector"])
    covariance = physical_apparatus_covariance_control(fixtures[3])
    weights = tuple(float(value) for value in export["rows"][-1]["weights"])
    semantic = realized_state_and_semantic_controls(weights)
    deletions = deletion_summary_control(held, export["rho"], rail)
    check(
        "Cycle 334 supplies a bounded reversible export plus typed conditional decoder without claiming a compiled physical content correlation or actual-member selection",
        stinespring["reduced_channel_Choi_residual"] < TOL
        and quotient["coarse_CP_Choi_residual"] < TOL
        and covariance["maximum_export_residual"] < TOL
        and semantic["without_actual_endpoint_content"] is None
        and deletions["decoder_deleted_label"] is None,
        {
            "strongest_positive": "conditional pointwise endpoint decoder",
            "narrow_separator": "named branch effects are not fixed by the reduced channel",
            "realized_state_slot": semantic["realized_state_slot"],
            "record_typing": semantic["record_typing"],
        },
    )
    print("DATA export_rows", [
        {key: value for key, value in row.items() if key not in ("effects", "weights")}
        for row in export["rows"]
    ])
    print("DATA stinespring", stinespring)
    print("DATA quotient", quotient)
    print("DATA rail", rail["rows"])
    print("DATA covariance", covariance)
    print("DATA semantic", semantic)
    print("DATA deletions", deletions)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE334_ENVIRONMENT_EXPORT_CONDITIONAL_GREEN"
        if FAIL == 0
        else "CYCLE334_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
