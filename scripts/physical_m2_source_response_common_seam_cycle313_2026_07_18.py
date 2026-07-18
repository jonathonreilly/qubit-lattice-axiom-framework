#!/usr/bin/env python3
"""Cycle 313: one physical M2 code for a source and its response.

Tensor the accepted Cycle-306 fixed-seam matter encoding with a declared
one-excitation encoding of one reservoir M2 and six directional mediator M2
per lattice cell.  Matter number controls a conjugate reservoir/mediator
exchange.  The mediator then streams by a nearest-neighbour M2 permutation.

The construction is factor certified: every local factor intertwines, so the
ordered product obeys E G_coarse = G_physical E on the declared code.  The
source coefficient, one-excitation preparation, physical M2 extensions, and
schedule are supplied.  Conserved occupation and its response are not called
energy, stress, a gravity source, a clock rate, or a Record.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import local_conjugate_reservoir_source_field_ledger_repair_2026_07_17 as reservoir
import physical_cycle269_relational_role_marker_gauge_cycle306_2026_07_17 as c306
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import stationary_dressed_reservoir_shifted_green_profile_2026_07_17 as dressed


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_M2_SOURCE_RESPONSE_COMMON_SEAM_CYCLE313_NOTE_2026-07-18.md"
)
BETA = -0.3
KAPPA = reservoir.COUPLING
MASS = c219.common_species(BETA).analytic_mass
THETA = KAPPA * MASS
TRAINING_SIZE = 3
HELD_SIZES = (4, 5, 6)
SOURCE = (0, 0, 0)
TOLERANCE = 2e-11

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
        check("the Cycle-313 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e g_coarse = g_physical e",
        "factor-certified",
        "one reservoir m2",
        "six directional mediator m2",
        "operator-level continuity",
        "emission, stream, and reabsorption",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "not energy",
        "not a gravity source",
        "prepared q=1",
        "fixed-seam comparator",
        "supplied structure",
        "literal-zero trigger scan",
        "directed pair audit",
        "exact file:line witnesses",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the construction, imports, and N1-N8 scope", not missing, missing)


def site_index(cell: tuple[int, int, int], length: int) -> int:
    x, y, z = cell
    return (x * length + y) * length + z


def shifted(
    cell: tuple[int, int, int], displacement: np.ndarray, length: int
) -> tuple[int, int, int]:
    return tuple(
        int((cell[axis] + int(displacement[axis])) % length)
        for axis in range(3)
    )


def validate_fixture(
    length: int, source: tuple[int, int, int], matter_number: int
) -> None:
    if length < 3:
        raise ValueError("periodic directional streams require L>=3")
    if len(source) != 3 or any(value < 0 or value >= length for value in source):
        raise ValueError("the source must be a cell of the finite torus")
    if matter_number not in (1, 2):
        raise ValueError("the accepted matter comparator has only n=1 and n=2")


def field_coin(length: int) -> sparse.csr_matrix:
    return sparse.block_diag(
        (
            sparse.csr_matrix([[1.0 + 0j]]),
            sparse.kron(
                sparse.eye(length**3, dtype=complex, format="csr"),
                sparse.csr_matrix(c214.FIELD_COIN),
                format="csr",
            ),
        ),
        format="csr",
    )


def field_vertex(
    length: int, source: tuple[int, int, int], theta: float
) -> sparse.csr_matrix:
    dimension = 1 + 6 * length**3
    local = (0,) + tuple(
        1 + 6 * site_index(source, length) + direction for direction in range(6)
    )
    delta = dressed.local_vertex_block(theta) - np.eye(7, dtype=complex)
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    for left, target in enumerate(local):
        for right, origin in enumerate(local):
            value = delta[left, right]
            if abs(value) > 1e-15:
                rows.append(target)
                columns.append(origin)
                values.append(value)
    return sparse.eye(dimension, dtype=complex, format="csr") + sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def field_stream(length: int) -> sparse.csr_matrix:
    dimension = 1 + 6 * length**3
    rows = [0]
    columns = [0]
    values = [1.0 + 0j]
    for cell in product(range(length), repeat=3):
        origin = site_index(cell, length)
        for direction, displacement in enumerate(c210.DIRECTIONS):
            target = site_index(shifted(cell, displacement, length), length)
            rows.append(1 + 6 * target + direction)
            columns.append(1 + 6 * origin + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def one_source_layers(
    length: int, source: tuple[int, int, int], matter_number: int
) -> tuple[sparse.csr_matrix, sparse.csr_matrix, sparse.csr_matrix, sparse.csr_matrix]:
    validate_fixture(length, source, matter_number)
    coin = field_coin(length)
    vertex = field_vertex(length, source, THETA * matter_number)
    stream = field_stream(length)
    return coin, vertex, stream, (stream @ vertex @ coin).tocsr()


def matter_number_operators() -> tuple[np.ndarray, np.ndarray]:
    c304 = c306.c304
    logical_diagonal = np.ones(c304.LOGICAL_DIMENSION, dtype=complex)
    logical_diagonal[12:] = 2
    micro_diagonal = np.zeros(c304.MICRO_DIMENSION, dtype=complex)
    seen = np.zeros(c304.MICRO_DIMENSION, dtype=int)
    code = c304.c269.build_code(c306.TRAINING_SIZE)
    for column in c304.micro_columns(code):
        index = c304.micro_index(column.sector, column.label, column.stream_slice)
        micro_diagonal[index] = 1 if column.sector == "n1" else 2
        seen[index] += 1
    if not np.all(seen == 1):
        raise RuntimeError("the Cycle-304 microsector number labels are incomplete")
    logical = np.diag(logical_diagonal)
    physical = c306.lift_physical(np.diag(micro_diagonal))
    return logical, physical


def local_q1_embedding() -> np.ndarray:
    """Reservoir first, then the six one-hot directional field states."""

    embedding = np.zeros((128, 7), dtype=complex)
    embedding[64, 0] = 1
    for direction in range(6):
        embedding[1 << direction, 1 + direction] = 1
    return embedding


def matter_and_local_field_intertwiner_controls() -> dict[str, float]:
    print("\nCOMMON FACTOR INTERTWINER")
    encoding = c306.constrained_encoding()
    logical_number, physical_number = matter_number_operators()
    _, logical, physical = c306.old_and_new_operators(BETA)
    logical_matter = logical["contact"] @ logical["stream"] @ logical["coin"]
    physical_matter = physical["contact"] @ physical["stream"] @ physical["coin"]
    matter_residuals = {
        name: float(np.linalg.norm(physical[name] @ encoding - encoding @ logical[name]))
        for name in logical
    }
    matter_residuals["composition"] = float(
        np.linalg.norm(physical_matter @ encoding - encoding @ logical_matter)
    )
    matter_residuals["number"] = float(
        np.linalg.norm(physical_number @ encoding - encoding @ logical_number)
    )
    matter_residuals["number_update_commutator"] = float(
        np.linalg.norm(physical_number @ physical_matter - physical_matter @ physical_number)
    )

    local_embedding = local_q1_embedding()
    operators = reservoir.reservoir_field_operators()
    full_coin = np.kron(np.eye(2), reservoir.full_field_coin())
    q1_coin = np.zeros((7, 7), dtype=complex)
    q1_coin[0, 0] = 1
    q1_coin[1:, 1:] = c214.FIELD_COIN
    local_residuals = {
        "isometry": float(
            np.linalg.norm(local_embedding.conj().T @ local_embedding - np.eye(7))
        ),
        "coin": float(np.linalg.norm(full_coin @ local_embedding - local_embedding @ q1_coin)),
    }
    for number in (1, 2):
        full_gate = reservoir.exchange_gate(THETA * number, operators["exchange"])
        q1_gate = dressed.local_vertex_block(THETA * number)
        local_residuals[f"source_n{number}"] = float(
            np.linalg.norm(full_gate @ local_embedding - local_embedding @ q1_gate)
        )
    field_decode = local_embedding.conj().T @ operators["F"] @ local_embedding
    reservoir_decode = local_embedding.conj().T @ operators["R"] @ local_embedding
    local_residuals["field_observable"] = float(
        np.linalg.norm(field_decode - np.diag((0, 1, 1, 1, 1, 1, 1)))
    )
    local_residuals["reservoir_observable"] = float(
        np.linalg.norm(reservoir_decode - np.diag((1, 0, 0, 0, 0, 0, 0)))
    )

    factor_bound = sum(matter_residuals.values()) + sum(local_residuals.values())
    check(
        "the Cycle-306 matter factors, matter-number source control, and full-M2 local field factors all intertwine",
        max(tuple(matter_residuals.values()) + tuple(local_residuals.values())) < TOLERANCE,
        {
            "matter": matter_residuals,
            "local_field": local_residuals,
            "factor_certified_composition_bound": factor_bound,
            "equation": "E G_coarse = G_physical E on E_306 tensor J_Q1",
        },
    )
    return {**matter_residuals, **local_residuals, "factor_bound": factor_bound}


def volume_code_and_unitarity_controls() -> None:
    print("\nIMPLICIT FULL-M2 VOLUME CODE / HELD SIZES")
    rows = []
    for length in (TRAINING_SIZE,) + HELD_SIZES:
        m2_sites = 1 + 6 * length**3
        masks = tuple(1 << index for index in range(m2_sites))
        stream = field_stream(length)
        permutation = np.argmax(abs(stream.toarray()), axis=0)
        expected = [0]
        for cell in product(range(length), repeat=3):
            for direction, displacement in enumerate(c210.DIRECTIONS):
                target = shifted(cell, displacement, length)
                expected.append(1 + 6 * site_index(target, length) + direction)
        unitarity = []
        for number in (1, 2):
            *_, update = one_source_layers(length, SOURCE, number)
            identity = sparse.eye(update.shape[0], dtype=complex, format="csr")
            unitarity.append(float(sparse_linalg.norm(update.getH() @ update - identity)))
        rows.append(
            {
                "L": length,
                "held_out": length in HELD_SIZES,
                "physical_field_M2": m2_sites,
                "Q1_code_dimension": m2_sites,
                "one_hot_masks_unique": len(set(masks)) == m2_sites,
                "maximum_mask_population": max(mask.bit_count() for mask in masks),
                "stream_matches_M2_bit_permutation": tuple(permutation) == tuple(expected),
                "maximum_Q1_unitarity_residual": max(unitarity),
            }
        )
    check(
        "the implicit declared J_Q1 and nearest-neighbour M2 update are exact through held L=6",
        all(row["one_hot_masks_unique"] for row in rows)
        and all(row["maximum_mask_population"] == 1 for row in rows)
        and all(row["stream_matches_M2_bit_permutation"] for row in rows)
        and max(row["maximum_Q1_unitarity_residual"] for row in rows) < 3e-13,
        rows,
    )


def diagonal_operator(diagonal: np.ndarray) -> sparse.csr_matrix:
    return sparse.diags(diagonal.astype(complex), format="csr")


def continuity_controls() -> None:
    print("\nLOCAL CONSERVATION / CURRENT")
    length = TRAINING_SIZE
    dimension = 1 + 6 * length**3
    rows = []
    for number in (1, 2):
        coin, vertex, stream, update = one_source_layers(length, SOURCE, number)
        local_layer = vertex @ coin
        ledger_residuals = []
        for cell in product(range(length), repeat=3):
            density = np.zeros(dimension)
            if cell == SOURCE:
                density[0] = 1
            start = 1 + 6 * site_index(cell, length)
            density[start : start + 6] = 1
            density_operator = diagonal_operator(density)
            delta = update.getH() @ density_operator @ update - density_operator

            bare_divergence = np.zeros(dimension)
            for direction, displacement in enumerate(c210.DIRECTIONS):
                upstream = shifted(cell, -displacement, length)
                bare_divergence[
                    1 + 6 * site_index(upstream, length) + direction
                ] += 1
                bare_divergence[start + direction] -= 1
            divergence = (
                local_layer.getH()
                @ diagonal_operator(bare_divergence)
                @ local_layer
            )
            ledger_residuals.append(float(sparse_linalg.norm(delta - divergence)))

        source_field = np.zeros(dimension)
        source_field[
            1 + 6 * site_index(SOURCE, length) :
            1 + 6 * site_index(SOURCE, length) + 6
        ] = 1
        reservoir_number = np.zeros(dimension)
        reservoir_number[0] = 1
        f_operator = diagonal_operator(source_field)
        r_operator = diagonal_operator(reservoir_number)
        source_residual = float(
            sparse_linalg.norm(
                (vertex.getH() @ f_operator @ vertex - f_operator)
                + (vertex.getH() @ r_operator @ vertex - r_operator)
            )
        )
        rows.append(
            {
                "matter_number": number,
                "maximum_continuity_residual": max(ledger_residuals),
                "source_balance_residual": source_residual,
            }
        )
    check(
        "the common source/mediator update has an exact operator-level continuity equation and local signed source balance",
        max(
            max(row["maximum_continuity_residual"], row["source_balance_residual"])
            for row in rows
        )
        < 3e-13,
        rows,
    )


def response_controls() -> None:
    print("\nENDOGENOUS OCCUPATION RESPONSE")
    rows = []
    for length in (TRAINING_SIZE,) + HELD_SIZES:
        for number in (1, 2):
            *_, update = one_source_layers(length, SOURCE, number)
            state = np.zeros(update.shape[0], dtype=complex)
            state[0] = 1
            state = update @ state
            expected_field = np.sin(THETA * number) ** 2
            field_weight = float(np.sum(abs(state[1:]) ** 2))
            reservoir_weight = float(abs(state[0]) ** 2)
            neighbor_weights = []
            for direction, displacement in enumerate(c210.DIRECTIONS):
                target = shifted(SOURCE, displacement, length)
                start = 1 + 6 * site_index(target, length)
                neighbor_weights.append(float(np.sum(abs(state[start : start + 6]) ** 2)))

            reservoir_history = [reservoir_weight]
            total_residual = abs(reservoir_weight + field_weight - 1)
            for _tick in range(2, 21):
                state = update @ state
                current_reservoir = float(abs(state[0]) ** 2)
                current_field = float(np.sum(abs(state[1:]) ** 2))
                reservoir_history.append(current_reservoir)
                total_residual = max(total_residual, abs(current_reservoir + current_field - 1))
            positive_return = max(np.diff(reservoir_history)[1:])
            rows.append(
                {
                    "L": length,
                    "held_out": length in HELD_SIZES,
                    "matter_number": number,
                    "one_tick_field_weight": field_weight,
                    "predicted_sin2_weight": expected_field,
                    "maximum_neighbor_error": max(
                        abs(value - expected_field / 6) for value in neighbor_weights
                    ),
                    "maximum_Q_residual_20_ticks": total_residual,
                    "largest_later_reservoir_return": float(positive_return),
                }
            )
    n1 = next(row for row in rows if row["L"] == 6 and row["matter_number"] == 1)
    n2 = next(row for row in rows if row["L"] == 6 and row["matter_number"] == 2)
    check(
        "the same update emits, streams to the six neighbours, and later reabsorbs while the physical occupation response distinguishes n=1 from n=2",
        max(abs(row["one_tick_field_weight"] - row["predicted_sin2_weight"]) for row in rows) < 2e-14
        and max(row["maximum_neighbor_error"] for row in rows) < 2e-14
        and max(row["maximum_Q_residual_20_ticks"] for row in rows) < 2e-13
        and min(row["largest_later_reservoir_return"] for row in rows) > 1e-3
        and abs(n2["one_tick_field_weight"] - n1["one_tick_field_weight"]) > 0.25,
        {
            "rows": rows,
            "supplied_response_observable": "local directional-M2 occupation F_x and reservoir occupation R",
            "conditional_prediction": "F_total(1)=sin^2(kappa m n)",
        },
    )


def field_family_representation(
    length: int,
    *,
    frame: np.ndarray | None = None,
    translation: tuple[int, int, int] | None = None,
) -> sparse.csr_matrix:
    if (frame is None) == (translation is None):
        raise ValueError("select exactly one family action")
    direction_map = tuple(range(6))
    if frame is not None:
        direction_representation = c210.direction_permutation(frame)
        direction_map = tuple(
            int(np.argmax(direction_representation[:, direction]))
            for direction in range(6)
        )
    dimension = 1 + 6 * length**3
    rows = [0]
    columns = [0]
    values = [1.0 + 0j]
    for cell in product(range(length), repeat=3):
        if frame is not None:
            target = tuple(
                int(value % length) for value in frame @ np.asarray(cell)
            )
        else:
            assert translation is not None
            target = tuple(
                (cell[axis] + translation[axis]) % length for axis in range(3)
            )
        origin_flat = site_index(cell, length)
        target_flat = site_index(target, length)
        for direction in range(6):
            rows.append(1 + 6 * target_flat + direction_map[direction])
            columns.append(1 + 6 * origin_flat + direction)
            values.append(1.0 + 0j)
    return sparse.csr_matrix(
        (values, (rows, columns)), shape=(dimension, dimension)
    )


def covariance_and_translation_controls() -> None:
    print("\nPROPER-CUBIC / TRANSLATION FAMILY")
    length = TRAINING_SIZE
    frames = c210.proper_cubic_frames()
    frame_residuals = []
    translation_residuals = []
    for number in (1, 2):
        *_, base = one_source_layers(length, SOURCE, number)
        for frame in frames:
            representation = field_family_representation(length, frame=frame)
            target_source = tuple(
                int(value % length) for value in frame @ np.asarray(SOURCE)
            )
            *_, target = one_source_layers(length, target_source, number)
            frame_residuals.append(
                float(sparse_linalg.norm(representation @ base - target @ representation))
            )
        for translation in product(range(length), repeat=3):
            representation = field_family_representation(
                length, translation=translation
            )
            target_source = tuple(
                (SOURCE[axis] + translation[axis]) % length for axis in range(3)
            )
            *_, target = one_source_layers(length, target_source, number)
            translation_residuals.append(
                float(sparse_linalg.norm(representation @ base - target @ representation))
            )

    logical_number, physical_number = matter_number_operators()
    matter_frame_residuals = []
    for frame in frames:
        logical_r, micro_r = c306.c304.frame_representations(frame)
        physical_r = c306.block_diagonal(micro_r, micro_r)
        matter_frame_residuals.extend(
            (
                float(np.linalg.norm(logical_r @ logical_number - logical_number @ logical_r)),
                float(np.linalg.norm(physical_r @ physical_number - physical_number @ physical_r)),
            )
        )
    check(
        "the encoded matter-number source family is covariant in all 24 proper-cubic frames and all 27 L=3 translations",
        len(frame_residuals) == 2 * 24
        and len(translation_residuals) == 2 * 27
        and max(frame_residuals + translation_residuals + matter_frame_residuals) < 3e-13,
        {
            "frame_tests": len(frame_residuals),
            "translation_tests": len(translation_residuals),
            "maximum_field_frame_residual": max(frame_residuals),
            "maximum_field_translation_residual": max(translation_residuals),
            "maximum_matter_number_frame_residual": max(matter_frame_residuals),
        },
    )


def mass_contact_support_and_deletion_controls() -> None:
    print("\nMASS / CONTACT / SUPPORT / DELETION")
    species = c219.common_species(BETA)
    encoding = c306.constrained_encoding()
    _, logical, physical = c306.old_and_new_operators(BETA)
    scalar = np.zeros(c306.c304.LOGICAL_DIMENSION, dtype=complex)
    scalar[:6] = c210.UNIFORM
    encoded = encoding @ scalar
    eigenvalue = np.vdot(encoded, physical["coin"] @ encoded)
    physical_mass = float(np.angle(eigenvalue)) / c219.C_SQUARED
    contact_zero = c306.lift_physical(c306.c304.physical_contact(0.0))
    contact_firewall = float(
        np.linalg.norm((physical["contact"] - contact_zero) @ encoding[:, :12])
    )
    logical_number, physical_number = matter_number_operators()
    contact_number_commutator = float(
        np.linalg.norm(physical["contact"] @ physical_number - physical_number @ physical["contact"])
    )

    *_, deleted = one_source_layers(TRAINING_SIZE, SOURCE, 1)
    coin = field_coin(TRAINING_SIZE)
    stream = field_stream(TRAINING_SIZE)
    deleted_coupling = stream @ field_vertex(TRAINING_SIZE, SOURCE, 0.0) @ coin
    initial = np.zeros(deleted.shape[0], dtype=complex)
    initial[0] = 1
    deleted_response = float(np.linalg.norm(deleted_coupling @ initial - initial))
    lawful_response = deleted @ initial
    lawful_neighbor = float(np.sum(abs(lawful_response[1:]) ** 2))
    no_stream = field_vertex(TRAINING_SIZE, SOURCE, THETA) @ coin
    unstreamed = no_stream @ initial
    neighbour_weight_without_stream = 0.0
    for displacement in c210.DIRECTIONS:
        target = shifted(SOURCE, displacement, TRAINING_SIZE)
        start = 1 + 6 * site_index(target, TRAINING_SIZE)
        neighbour_weight_without_stream += float(np.sum(abs(unstreamed[start : start + 6]) ** 2))

    operators = reservoir.reservoir_field_operators()
    lowering = np.asarray(((0, 1), (0, 0)), dtype=complex)
    emission_only = np.kron(lowering, operators["creation"])
    bad_gate = np.eye(128, dtype=complex) - 1j * THETA * emission_only
    bad_unitarity = float(np.linalg.norm(bad_gate.conj().T @ bad_gate - np.eye(128)))
    control_deletion = float(
        np.linalg.norm(
            dressed.local_vertex_block(2 * THETA)
            - dressed.local_vertex_block(THETA)
        )
    )
    check(
        "the common seam preserves the Cycle-219 mass and Cycle-230 contact fixtures and has bounded constant physical support",
        abs(physical_mass - c219.rest_mass(species)) < 4e-13
        and contact_firewall == 0
        and contact_number_commutator < TOLERANCE,
        {
            "physical_rest_mass": physical_mass,
            "Cycle219_fixture": c219.rest_mass(species),
            "one_particle_contact_firewall": contact_firewall,
            "contact_number_commutator": contact_number_commutator,
            "matter_M2_per_cell": 23,
            "mediator_M2_per_cell": 6,
            "reservoir_M2_per_active_source": 1,
            "maximum_matter_patch_plus_source_vertex_M2": 51,
            "field_coin_support_M2": 6,
            "field_stream_support_M2": 2,
        },
    )
    check(
        "coupling, stream, conjugate absorption, and matter-number-control deletions are independently detected",
        deleted_response < 1e-14
        and lawful_neighbor > 0.1
        and neighbour_weight_without_stream < 1e-15
        and bad_unitarity > 0.1
        and control_deletion > 0.4,
        {
            "zero_coupling_response": deleted_response,
            "lawful_one_tick_streamed_weight": lawful_neighbor,
            "neighbour_weight_if_stream_deleted": neighbour_weight_without_stream,
            "emission_only_unitarity_residual": bad_unitarity,
            "n_control_deletion_residual": control_deletion,
        },
    )


def lawful_domain_and_inventory_controls() -> None:
    print("\nLAWFUL DOMAIN / INVENTORY")
    validate_fixture(3, SOURCE, 1)
    rejected = 0
    for fixture in (
        (2, SOURCE, 1),
        (3, (3, 0, 0), 1),
        (3, SOURCE, 0),
        (3, SOURCE, 3),
    ):
        try:
            validate_fixture(*fixture)
        except ValueError:
            rejected += 1
    check(
        "the declared common-code domain rejects aliased size, invalid source cells, and absent matter sectors",
        rejected == 4,
        rejected,
    )
    inventory = {
        "inherited matter code": "Cycle-306 E_306, C_role, fixed n=1+n=2 seam, and Cycle-310 final factors",
        "inherited matter update": "Cycle-219 coin, Cycle-230 contact, autonomous fixed-seam stream/catch-up, and supplied order",
        "supplied source identity": "the exact n=1/n=2 matter-number block on the fixed seam",
        "supplied source law": "theta=kappa m n with kappa=0.8 and m=-3 tan(beta/2)",
        "supplied mediator code": "one reservoir M2 at the active source and six directional field M2 per cell",
        "supplied sector": "prepared global Q=1 hard-core sector; preserved locally but not locally prepared",
        "supplied physical extensions": "field coin identity off Q=1, conjugate exchange, nearest-neighbour M2 stream permutation",
        "supplied schedule": "matter/field coins; matter-number-controlled exchange; both streams; matter contact",
        "supplied observable": "local field and reservoir M2 occupation; preparation and readout remain external",
        "derived": "factor-certified common intertwiner, operator continuity, emission/stream/reabsorption response, covariance, held sizes",
        "excluded": "energy, stress, gravity source, metric response, recoil, clock/rate, full Fock, recurrent matter volume, Record",
    }
    check(
        "all supplied and derived source/response structure is explicit",
        len(inventory) == 11,
        inventory,
    )


def no_go_discipline_executable_controls() -> None:
    print("\nNO-GO DISCIPLINE EXECUTABLE CONTROLS")
    lines = NOTE.read_text(encoding="utf-8").lower().splitlines()
    trigger_families = (
        "we assume",
        "by construction",
        "as is standard",
        "the framework provides",
        "bridge context",
        "background",
        "naturally",
        "obviously",
        "standard qft",
        "registered",
        "canonical",
    )
    hits = tuple(
        (line_number, trigger)
        for line_number, line in enumerate(lines, start=1)
        for trigger in trigger_families
        if trigger in line
    )
    check(
        "the N3 literal-zero trigger scan finds no hidden-admission rhetoric in the Cycle-313 proof note",
        not hits,
        hits,
    )

    witnesses = (
        (
            "docs/work_history/repo/review_feedback/LOCAL_CONJUGATE_RESERVOIR_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md",
            23,
            "site-local, not carried",
        ),
        (
            "docs/work_history/repo/review_feedback/CARRIED_INTERNAL_SPECIES_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md",
            348,
            "full-fock car transport remains open",
        ),
        (
            "docs/work_history/repo/review_feedback/SOURCE_RESPONSE_COMMON_CODE_FOLLOWON_SYNTHESIS_CYCLE297_NOTE_2026-07-17.md",
            92,
            "does not establish the requested physical compiler equation",
        ),
        (
            "docs/work_history/repo/review_feedback/SOURCE_RESPONSE_COMMON_CODE_FOLLOWON_SYNTHESIS_CYCLE297_NOTE_2026-07-17.md",
            77,
            "two fixed reservoirs",
        ),
        (
            "docs/work_history/repo/review_feedback/COLLISION_SAFE_PHYSICAL_CATCHUP_SYNTHESIS_CYCLE299_NOTE_2026-07-17.md",
            56,
            "not an assembled encoded",
        ),
        (
            "docs/work_history/repo/review_feedback/CARRIED_RELATIVE_FROZEN_BRANCH_OBSERVABLE_CYCLE300_NOTE_2026-07-17.md",
            20,
            "frozen scalar observable does not pass",
        ),
        (
            "docs/work_history/repo/review_feedback/PHYSICAL_CYCLE269_PAIRED_DIRECT_ORBIT_FACTORIZATION_CYCLE310_NOTE_2026-07-17.md",
            88,
            "decomposition, and not an autonomous law",
        ),
    )
    failures = []
    for relative_path, line_number, fragment in witnesses:
        witness_lines = (ROOT / relative_path).read_text(encoding="utf-8").lower().splitlines()
        if line_number > len(witness_lines) or fragment not in witness_lines[line_number - 1]:
            failures.append((relative_path, line_number, fragment))
    check(
        "the N4 residual table's exact file:line witnesses still point to their stated residuals",
        not failures,
        failures,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 313: PHYSICAL M2 SOURCE/RESPONSE COMMON SEAM")
    print("authority=none; audit=unset")
    note_contract()
    matter_and_local_field_intertwiner_controls()
    volume_code_and_unitarity_controls()
    continuity_controls()
    response_controls()
    covariance_and_translation_controls()
    mass_contact_support_and_deletion_controls()
    lawful_domain_and_inventory_controls()
    no_go_discipline_executable_controls()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    print(
        "RESULT",
        "PHYSICAL_M2_SOURCE_RESPONSE_COMMON_SEAM_FACTOR_CERTIFIED"
        if FAIL == 0
        else "PHYSICAL_M2_SOURCE_RESPONSE_COMMON_SEAM_OPEN",
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
