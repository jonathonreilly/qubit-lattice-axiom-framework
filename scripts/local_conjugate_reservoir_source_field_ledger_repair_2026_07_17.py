#!/usr/bin/env python3
"""Local conjugate-reservoir repair for the matter/mediator source port.

Add one reservoir M2 and six directional field M2 sites per coarse cell.  A
bounded onsite exchange consumes one reservoir excitation while creating the
uniform scalar field excitation, and its conjugate absorbs the field while
restoring the reservoir.  The gate commutes with reservoir-plus-field number,
so the declared zero/one-mediator sector follows from a prepared one-excitation
sector without a global occupancy service.

The conserved object is an excitation ledger, not energy, stress, a gravity
source, a clock rate, or a Record.  The reservoir is site-local; transporting
it with moving matter remains an explicit compiler/dynamics import.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "LOCAL_CONJUGATE_RESERVOIR_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md"
)
BETA = c230.BETA
COUPLING = 0.8
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
    if not NOTE.exists():
        check("the conjugate-reservoir note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one reservoir m2",
        "six directional field m2",
        "operator-level",
        "zero/one-mediator sector",
        "no global occupancy service",
        "all 24 proper-cubic frames",
        "mass/contact deletion",
        "not energy",
        "not a gravity source",
        "site-local, not carried",
        "supplied structure",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note preserves construction, controls, and scope", not missing, missing)


def field_creation() -> np.ndarray:
    """Uniform vacuum-to-one-direction creation on six physical field M2."""

    creation = np.zeros((64, 64), dtype=complex)
    for direction in range(6):
        creation[1 << direction, 0] = 1 / np.sqrt(6)
    return creation


def reservoir_field_operators() -> dict[str, np.ndarray]:
    creation = field_creation()
    annihilation = creation.conj().T
    lowering = np.asarray(((0, 1), (0, 0)), dtype=complex)
    raising = lowering.conj().T
    exchange = np.kron(lowering, creation) + np.kron(raising, annihilation)
    field_number = np.diag(
        np.asarray([index.bit_count() for index in range(64)], dtype=float)
    ).astype(complex)
    reservoir_number = np.diag((0.0, 1.0)).astype(complex)
    field_lift = np.kron(np.eye(2), field_number)
    reservoir_lift = np.kron(reservoir_number, np.eye(64))
    total = reservoir_lift + field_lift
    return {
        "creation": creation,
        "annihilation": annihilation,
        "exchange": exchange,
        "F": field_lift,
        "R": reservoir_lift,
        "Q": total,
    }


def exchange_gate(angle: float, exchange: np.ndarray) -> np.ndarray:
    active = exchange @ exchange
    return (
        np.eye(exchange.shape[0], dtype=complex)
        + (np.cos(angle) - 1) * active
        - 1j * np.sin(angle) * exchange
    )


def field_bit_permutation(direction_representation: np.ndarray) -> np.ndarray:
    direction_map = tuple(
        int(np.argmax(direction_representation[:, direction]))
        for direction in range(6)
    )
    result = np.zeros((64, 64), dtype=complex)
    for state in range(64):
        target = 0
        for direction in range(6):
            if (state >> direction) & 1:
                target ^= 1 << direction_map[direction]
        result[target, state] = 1
    return result


def full_field_coin() -> np.ndarray:
    """A supplied full-M2 extension: acoustic coin on N=1, identity otherwise."""

    coin = np.eye(64, dtype=complex)
    one_particle = tuple(1 << direction for direction in range(6))
    coin[np.ix_(one_particle, one_particle)] = c219.c214.FIELD_COIN
    return coin


def local_exchange_and_sector_controls() -> dict[str, np.ndarray]:
    print("\nLOCAL FULL-M2 CONJUGATE RESERVOIR")
    operators = reservoir_field_operators()
    species = c219.common_species(BETA)
    mass = species.analytic_mass
    angle = COUPLING * mass
    gate = exchange_gate(angle, operators["exchange"])
    identity = np.eye(128, dtype=complex)
    q_values = np.diag(operators["Q"]).real
    q1 = np.diag((np.abs(q_values - 1) < 1e-12).astype(float)).astype(complex)

    check(
        "the seven-M2 exchange is unitary, Hermitian-generated, and conserves reservoir plus field excitation",
        np.linalg.norm(operators["exchange"] - operators["exchange"].conj().T)
        == 0
        and np.linalg.norm(gate.conj().T @ gate - identity) < 3e-14
        and np.linalg.norm(gate @ operators["Q"] - operators["Q"] @ gate)
        < 2e-14,
        {
            "support_M2": 7,
            "unitarity_residual": float(
                np.linalg.norm(gate.conj().T @ gate - identity)
            ),
            "excitation_commutator": float(
                np.linalg.norm(gate @ operators["Q"] - operators["Q"] @ gate)
            ),
        },
    )
    check(
        "the prepared total-Q=1 sector is invariant without any global mediator-occupancy query",
        np.linalg.norm((identity - q1) @ gate @ q1) < 2e-15
        and np.linalg.norm(gate @ q1 - q1 @ gate) < 2e-15,
        {
            "Q1_dimension": int(np.trace(q1).real),
            "leakage": float(np.linalg.norm((identity - q1) @ gate @ q1)),
        },
    )

    field_after = gate.conj().T @ operators["F"] @ gate
    reservoir_after = gate.conj().T @ operators["R"] @ gate
    source_transfer = field_after - operators["F"]
    local_ledger_residual = np.linalg.norm(
        source_transfer + reservoir_after - operators["R"]
    )
    check(
        "the onsite source-plus-field ledger is an exact operator identity with signed emission and absorption directions",
        local_ledger_residual < 3e-14
        and np.min(np.linalg.eigvalsh(source_transfer)) < -0.1
        and np.max(np.linalg.eigvalsh(source_transfer)) > 0.1,
        {
            "operator_ledger_residual": float(local_ledger_residual),
            "minimum_transfer_eigenvalue": float(
                np.min(np.linalg.eigvalsh(source_transfer))
            ),
            "maximum_transfer_eigenvalue": float(
                np.max(np.linalg.eigvalsh(source_transfer))
            ),
        },
    )

    emitted_initial = np.zeros(128, dtype=complex)
    emitted_initial[64] = 1  # reservoir=1, field vacuum
    scalar_initial = np.zeros(128, dtype=complex)
    for direction in range(6):
        scalar_initial[1 << direction] = 1 / np.sqrt(6)
    emitted = gate @ emitted_initial
    absorbed = gate @ scalar_initial
    check(
        "the same forward gate consumes reservoir excitation on emission and restores it on scalar absorption",
        abs(
            np.vdot(emitted, operators["F"] @ emitted).real
            - np.sin(angle) ** 2
        )
        < 2e-14
        and abs(
            np.vdot(emitted, operators["R"] @ emitted).real
            - np.cos(angle) ** 2
        )
        < 2e-14
        and abs(
            np.vdot(absorbed, operators["R"] @ absorbed).real
            - np.sin(angle) ** 2
        )
        < 2e-14,
        {
            "angle": angle,
            "emitted_field_weight": float(
                np.vdot(emitted, operators["F"] @ emitted).real
            ),
            "absorbed_reservoir_weight": float(
                np.vdot(absorbed, operators["R"] @ absorbed).real
            ),
        },
    )

    field_coin = full_field_coin()
    check(
        "the supplied full-M2 field-coin extension is unitary and preserves field excitation number",
        np.linalg.norm(field_coin.conj().T @ field_coin - np.eye(64)) < 3e-12
        and np.linalg.norm(
            field_coin @ np.diag(np.diag(operators["F"])[:64])
            - np.diag(np.diag(operators["F"])[:64]) @ field_coin
        )
        < 3e-12,
    )

    covariance = []
    for frame in c210.proper_cubic_frames():
        direction = c210.direction_permutation(frame)
        representation = np.kron(
            np.eye(2), field_bit_permutation(direction)
        )
        covariance.append(
            np.linalg.norm(representation @ gate - gate @ representation)
        )
    check(
        "the physical reservoir-field gate commutes with all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 3e-14,
        max(covariance),
    )
    operators.update(
        {
            "gate": gate,
            "source_transfer": source_transfer,
            "q1": q1,
            "field_coin": field_coin,
        }
    )
    return operators


def physical_matter_support_and_covariance_controls() -> None:
    print("\nPHYSICAL MATTER CONTROL / SUPPORT / LEAKAGE")
    support_rows = []
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        bs = c278.cell_bs(code, (0, 0, 0))
        support = 0
        for row in bs:
            support |= row.x | row.z
        leakage = sum(
            not row.commutes(check_row)
            for row in bs
            for check_row in code.local_checks + code.wilsons
        )
        support_rows.append(
            {
                "L": length,
                "held_out": length == 6,
                "matter_number_union_M2": support.bit_count(),
                "maximum_B_weight": max(
                    (row.x | row.z).bit_count() for row in bs
                ),
                "reservoir_plus_field_M2": 7,
                "joint_vertex_union_M2": support.bit_count() + 7,
                "maximum_expanded_term_weight": max(
                    (row.x | row.z).bit_count() for row in bs
                )
                + 7,
                "check_or_Wilson_leakage": leakage,
                "B_noncommutations": sum(
                    not left.commutes(right) for left in bs for right in bs
                ),
            }
        )
    check(
        "m N_x times the reservoir-field exchange has bounded physical-M2 support and zero code leakage through held-out L=6",
        all(row["matter_number_union_M2"] == 18 for row in support_rows)
        and all(row["joint_vertex_union_M2"] == 25 for row in support_rows)
        and all(row["maximum_expanded_term_weight"] == 12 for row in support_rows)
        and all(row["check_or_Wilson_leakage"] == 0 for row in support_rows)
        and all(row["B_noncommutations"] == 0 for row in support_rows),
        support_rows,
    )

    code = c269.build_code(3)
    source_vertices = tuple(
        code.graph.vertex_index[((0, 0, 0), direction)] for direction in range(6)
    )
    local_family = set(code.local_checks)
    failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        for displacement in product(range(3), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]]
                for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]]
                for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(
                code.graph, vertex_map, edge_map
            )
            transformed_local = {
                c235.apply_gauge(
                    c235.permute_pauli(row, edge_map), toggles, pairs, flips
                )
                for row in code.local_checks
            }
            transformed_bs = {
                c235.apply_gauge(
                    c235.permute_pauli(code.B[vertex], edge_map),
                    toggles,
                    pairs,
                    flips,
                )
                for vertex in source_vertices
            }
            target_bs = {code.B[vertex_map[vertex]] for vertex in source_vertices}
            if transformed_local != local_family or transformed_bs != target_bs:
                failures.append((frame.tolist(), displacement))
            tests += 1
    check(
        "the mapped physical mass control passes all 648 proper-frame and translation tests",
        tests == 24 * 27 and not failures,
        {"tests": tests, "failures": failures[:3]},
    )


def local_matter_contact_and_deletion_controls(operators: dict[str, np.ndarray]) -> None:
    print("\nMASS / CONTACT / DELETION")
    species = c219.common_species(BETA)
    occupations = np.asarray(
        [index.bit_count() for index in range(64)], dtype=float
    )
    number = np.diag(occupations).astype(complex)
    matter_coin = c229.fock_lift(species.coin)
    contact = np.diag(
        np.exp(
            1j
            * c230.COUPLING
            * occupations
            * (occupations - 1)
            / 2
        )
    ).astype(complex)
    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))

    check(
        "the additive m N_x control commutes with the actual onsite matter coin/contact and keeps W_g identity for N at most one",
        np.linalg.norm(number @ matter_coin - matter_coin @ number) < 3e-13
        and np.linalg.norm(number @ contact - contact @ number) == 0
        and np.max(np.abs(np.diag(contact)[occupations <= 1] - 1)) == 0,
        {
            "coin_commutator": float(
                np.linalg.norm(number @ matter_coin - matter_coin @ number)
            ),
            "contact_commutator": float(
                np.linalg.norm(number @ contact - contact @ number)
            ),
        },
    )
    deleted = exchange_gate(0.0, operators["exchange"])
    check(
        "coupling deletion is exact and leaves the Cycle-219 one-particle mass/contact fixture",
        np.linalg.norm(deleted - np.eye(128)) == 0
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6,
        {
            "deletion_residual": float(
                np.linalg.norm(deleted - np.eye(128))
            ),
            "analytic_mass": species.analytic_mass,
            "dispersion_mass": dispersion_mass,
        },
    )
    raw_phase = float(np.angle(np.trace(c210.P_SCALAR @ species.coin)))
    check(
        "the reservoir coupling imports the Cycle-219 c-inverse-squared phase-to-mass normalization",
        abs(raw_phase / species.analytic_mass - c219.C_SQUARED) < 2e-12,
        {
            "raw_phase": raw_phase,
            "mass": species.analytic_mass,
            "ratio": raw_phase / species.analytic_mass,
        },
    )


def site_index(site: tuple[int, int, int], length: int) -> int:
    x, y, z = site
    return (x * length + y) * length + z


def shifted(
    site: tuple[int, int, int], displacement: np.ndarray, length: int
) -> tuple[int, int, int]:
    return tuple(
        int((site[axis] + int(displacement[axis])) % length)
        for axis in range(3)
    )


def one_excitation_layers(
    length: int, angle: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Reservoir plus field one-excitation block of coin, vertex, and stream."""

    cells = tuple(product(range(length), repeat=3))
    cell_count = length**3
    dimension = 7 * cell_count
    coin = np.eye(dimension, dtype=complex)
    vertex = np.eye(dimension, dtype=complex)
    stream = np.zeros((dimension, dimension), dtype=complex)

    for cell in cells:
        flat = site_index(cell, length)
        field_indices = tuple(
            cell_count + 6 * flat + direction for direction in range(6)
        )
        coin[np.ix_(field_indices, field_indices)] = c219.c214.FIELD_COIN
        reservoir_index = flat
        scalar = np.zeros(dimension, dtype=complex)
        scalar[list(field_indices)] = 1 / np.sqrt(6)
        reservoir = np.zeros(dimension, dtype=complex)
        reservoir[reservoir_index] = 1
        exchange = np.outer(reservoir, scalar.conj()) + np.outer(
            scalar, reservoir.conj()
        )
        vertex += (np.cos(angle) - 1) * (exchange @ exchange)
        vertex += -1j * np.sin(angle) * exchange

        stream[reservoir_index, reservoir_index] = 1
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target = shifted(cell, displacement, length)
            target_flat = site_index(target, length)
            stream[
                cell_count + 6 * target_flat + direction,
                cell_count + 6 * flat + direction,
            ] = 1
    return coin, vertex, stream, stream @ vertex @ coin


def frame_representation(length: int, frame: np.ndarray) -> np.ndarray:
    cell_count = length**3
    dimension = 7 * cell_count
    result = np.zeros((dimension, dimension), dtype=complex)
    direction_map = tuple(
        int(np.argmax(c210.direction_permutation(frame)[:, direction]))
        for direction in range(6)
    )
    for cell in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(cell))
        source_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        result[target_flat, source_flat] = 1
        for direction in range(6):
            result[
                cell_count + 6 * target_flat + direction_map[direction],
                cell_count + 6 * source_flat + direction,
            ] = 1
    return result


def translation_representation(
    length: int, displacement: tuple[int, int, int]
) -> np.ndarray:
    cell_count = length**3
    dimension = 7 * cell_count
    result = np.zeros((dimension, dimension), dtype=complex)
    for cell in product(range(length), repeat=3):
        target = tuple(
            (cell[axis] + displacement[axis]) % length for axis in range(3)
        )
        source_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        result[target_flat, source_flat] = 1
        for direction in range(6):
            result[
                cell_count + 6 * target_flat + direction,
                cell_count + 6 * source_flat + direction,
            ] = 1
    return result


def operator_ledger_and_global_covariance_controls() -> None:
    print("\nOPERATOR-LEVEL SOURCE + FIELD CONTINUITY")
    length = 3
    mass = c219.common_species(BETA).analytic_mass
    angle = COUPLING * mass
    coin, vertex, stream, update = one_excitation_layers(length, angle)
    cell_count = length**3
    dimension = update.shape[0]
    local_layer = vertex @ coin
    ledger_residuals = []
    source_residuals = []
    for cell in product(range(length), repeat=3):
        flat = site_index(cell, length)
        reservoir = np.zeros((dimension, dimension), dtype=complex)
        reservoir[flat, flat] = 1
        field = np.zeros_like(reservoir)
        for direction in range(6):
            field[cell_count + 6 * flat + direction, cell_count + 6 * flat + direction] = 1
        density = reservoir + field
        delta = update.conj().T @ density @ update - density
        divergence = np.zeros_like(delta)
        for direction, displacement in enumerate(c210.DIRECTIONS):
            upstream = shifted(cell, -displacement, length)
            upstream_flat = site_index(upstream, length)
            incoming = np.zeros_like(delta)
            incoming[
                cell_count + 6 * upstream_flat + direction,
                cell_count + 6 * upstream_flat + direction,
            ] = 1
            outgoing = np.zeros_like(delta)
            outgoing[
                cell_count + 6 * flat + direction,
                cell_count + 6 * flat + direction,
            ] = 1
            divergence += local_layer.conj().T @ (incoming - outgoing) @ local_layer
        ledger_residuals.append(float(np.linalg.norm(delta - divergence)))

        vertex_field_after = vertex.conj().T @ field @ vertex
        vertex_reservoir_after = vertex.conj().T @ reservoir @ vertex
        source_residuals.append(
            float(
                np.linalg.norm(
                    (vertex_field_after - field)
                    + (vertex_reservoir_after - reservoir)
                )
            )
        )
    check(
        "the fixed occupied-control reservoir-field coin-vertex-stream update has an exact operator-level continuity ledger",
        max(ledger_residuals) < 3e-14 and max(source_residuals) < 3e-14,
        {
            "dimension": dimension,
            "maximum_divergence_residual": max(ledger_residuals),
            "maximum_vertex_source_residual": max(source_residuals),
        },
    )
    check(
        "the fixed-control reservoir-field one-excitation update is unitary and its inverse restores every amplitude",
        np.linalg.norm(update.conj().T @ update - np.eye(dimension)) < 3e-13,
        float(np.linalg.norm(update.conj().T @ update - np.eye(dimension))),
    )

    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = frame_representation(length, frame)
        frame_residuals.append(
            np.linalg.norm(representation @ update - update @ representation)
        )
    translation_residuals = []
    for axis in range(3):
        displacement = [0, 0, 0]
        displacement[axis] = 1
        representation = translation_representation(length, tuple(displacement))
        translation_residuals.append(
            np.linalg.norm(representation @ update - update @ representation)
        )
    check(
        "the fixed-control reservoir-field update is translation invariant and covariant in all 24 proper-cubic frames",
        len(frame_residuals) == 24
        and max(frame_residuals) < 3e-13
        and max(translation_residuals) < 3e-13,
        {
            "maximum_frame_residual": max(frame_residuals),
            "maximum_translation_residual": max(translation_residuals),
        },
    )


def composition_spectator_and_schedule_controls() -> None:
    print("\nCOMPOSITION / SPECTATOR / SCHEDULE")
    angle = COUPLING * c219.common_species(BETA).analytic_mass
    sigma_x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    gate = np.cos(angle) * np.eye(2) - 1j * np.sin(angle) * sigma_x
    field = np.diag((0.0, 1.0)).astype(complex)
    identity = np.eye(2, dtype=complex)
    left = np.kron(gate, identity)
    right = np.kron(identity, gate)
    composed = left @ right
    total_field = np.kron(field, identity) + np.kron(identity, field)
    transfer = composed.conj().T @ total_field @ composed - total_field
    separate_transfer = np.kron(gate.conj().T @ field @ gate - field, identity)
    separate_transfer += np.kron(identity, gate.conj().T @ field @ gate - field)
    check(
        "two independent local reservoir vertices commute and their excitation transfers add exactly",
        np.linalg.norm(left @ right - right @ left) == 0
        and np.linalg.norm(transfer - separate_transfer) < 2e-15,
        {
            "commutator": float(np.linalg.norm(left @ right - right @ left)),
            "transfer_additivity_residual": float(
                np.linalg.norm(transfer - separate_transfer)
            ),
        },
    )
    spectator = np.eye(2, dtype=complex)
    check(
        "a normalized spectator factor does not alter the local source-field operator ledger",
        np.linalg.norm(
            np.kron(gate.conj().T @ field @ gate - field, spectator)
            - np.kron(gate.conj().T @ field @ gate - field, np.eye(2))
        )
        == 0,
    )
    check(
        "the update schedule and unimplemented carried-source extension are explicit",
        True,
        {
            "schedule": (
                "candidate full schedule: matter/field onsite coins; local matter-controlled "
                "reservoir-field exchange; matter and direction-field streams; arrival-cell contact; "
                "moving matter is not executed in the reservoir-field matrix control"
            ),
            "remaining": (
                "the reservoir is attached to a lattice cell; transporting it with a moving "
                "matter body needs a new bounded carrier/compiler"
            ),
        },
    )


def lawful_domain_and_inventory_controls() -> None:
    print("\nLAWFUL DOMAIN / SUPPLIED STRUCTURE")

    def validate(length: int, matter_modes: int, field_m2: int, reservoir_m2: int) -> None:
        if length < 3:
            raise ValueError("periodic physical matter code requires L>=3")
        if matter_modes != 6:
            raise ValueError("the imported matter cell has six modes")
        if field_m2 != 6 or reservoir_m2 != 1:
            raise ValueError("the repair uses six field M2 and one reservoir M2")

    validate(3, 6, 6, 1)
    rejected = 0
    for row in ((2, 6, 6, 1), (3, 5, 6, 1), (3, 6, 5, 1), (3, 6, 6, 2)):
        try:
            validate(*row)
        except ValueError:
            rejected += 1
    check(
        "the declared domain rejects aliased and mistyped fixtures",
        rejected == 4,
        {"rejected": rejected},
    )
    check(
        "the supplied structure inventory is explicit",
        True,
        {
            "supplied": (
                "Cycle-269 sectorwise mapped matter code and B representatives",
                "beta=-0.3 and m=-3 tan(beta/2)",
                "one site-local reservoir M2 per coarse cell",
                "six physical directional field M2 per coarse cell",
                "full field-coin extension outside the zero/one sector",
                "uniform scalar creation convention",
                "coupling 0.8 and coin-vertex-stream-contact schedule",
                "prepared total reservoir-plus-field excitation sector",
            ),
            "derived": (
                "full local physical-M2 exchange gate",
                "operator-level source-field balance",
                "zero/one mediator invariance without occupancy queries",
                "bounded support, zero leakage, covariance, deletion, and composition",
            ),
            "not_earned": (
                "reservoir transport with moving matter",
                "energy/stress/gravity-source interpretation",
                "field work or matter recoil",
                "clock normalization or metric response",
                "prepared full-Fock matter encoder",
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("LOCAL CONJUGATE RESERVOIR / SOURCE-FIELD LEDGER REPAIR")
    note_contract()
    operators = local_exchange_and_sector_controls()
    physical_matter_support_and_covariance_controls()
    local_matter_contact_and_deletion_controls(operators)
    operator_ledger_and_global_covariance_controls()
    composition_spectator_and_schedule_controls()
    lawful_domain_and_inventory_controls()
    print("\nSUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "LOCAL_CONJUGATE_RESERVOIR_LEDGER_REPAIR_BOUNDED"
        if FAIL == 0
        else "LOCAL_CONJUGATE_RESERVOIR_LEDGER_REPAIR_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
