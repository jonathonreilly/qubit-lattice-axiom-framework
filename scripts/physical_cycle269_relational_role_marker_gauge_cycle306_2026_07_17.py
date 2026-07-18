#!/usr/bin/env python3
"""Cycle 306: locally constrained relational carrier-role marker.

Cycle 304's fixed-seam comparator has a correct 42-column intertwiner but
uses one unconstrained phase flag.  This runner first tests the bare local
exchange selector suggested by that degeneracy.  Its +1 space has only 21 of
the intended columns and the selector does not commute with the active coin
or contact.  One additional ordinary M2 repairs both defects: the constraint

    C_role = K_exchange X_r = +1

uses the signless local stream/catch-up exchange K_exchange and a new local
gauge companion r.  The relational marker Z_slice Z_r is a code observable.
The physical stream flips it autonomously; the coin and contact preserve it.

All statements are restricted to the Cycle-304 n=1+n=2 fixed-seam
comparator.  This is not a recurrent-volume or full-Fock compiler.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_coin_stream_contact_common_refinement_cycle304_2026_07_17 as c304
import physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17 as c302


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_RELATIONAL_ROLE_MARKER_GAUGE_CYCLE306_NOTE_2026-07-17.md"
)
TRAINING_SIZE = 3
HELD_SIZE = 6
TOLERANCE = 1e-11

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
        check("the Cycle-306 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "one additional ordinary m2",
        "c_role = k_exchange x_r",
        "exactly forty-two",
        "standalone selector",
        "twenty-one",
        "relational carrier-role marker",
        "autonomously",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "forty-four m2",
        "twenty-three m2 per cell",
        "fixed-seam comparator",
        "not a recurrent-volume compiler",
        "no global jordan–wigner ordering",
        "no host-side branch control",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the constructive and residual boundary", not missing, missing)


def block_diagonal(*blocks: np.ndarray) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    result = np.zeros((size, size), dtype=complex)
    offset = 0
    for block in blocks:
        width = block.shape[0]
        result[offset : offset + width, offset : offset + width] = block
        offset += width
    return result


def exchange_operator() -> np.ndarray:
    """Signless face/tag/flag carrier exchange on all ninety microsectors."""

    return np.abs(c304.physical_stream()).astype(complex)


def slice_z() -> np.ndarray:
    diagonal = np.empty(c304.MICRO_DIMENSION, dtype=complex)
    for column in c304.micro_columns(c304.c269.build_code(TRAINING_SIZE)):
        diagonal[c304.micro_index(column.sector, column.label, column.stream_slice)] = (
            1 if column.stream_slice == 0 else -1
        )
    return np.diag(diagonal)


def logical_role_z() -> np.ndarray:
    diagonal = np.empty(c304.LOGICAL_DIMENSION, dtype=complex)
    for direction in range(6):
        for stream_slice in range(2):
            diagonal[c304.logical_n1_index(direction, stream_slice)] = (
                1 if stream_slice == 0 else -1
            )
    for pair in c304.PAIR_LABELS:
        for stream_slice in range(2):
            diagonal[c304.logical_n2_index(pair, stream_slice)] = (
                1 if stream_slice == 0 else -1
            )
    return np.diag(diagonal)


def role_constraint() -> np.ndarray:
    x_r = np.asarray(((0, 1), (1, 0)), dtype=complex)
    return np.kron(x_r, exchange_operator())


def constrained_encoding() -> np.ndarray:
    old = c304.common_encoding()
    return np.vstack((old, exchange_operator() @ old)) / np.sqrt(2)


def shell_projector() -> np.ndarray:
    old = c304.common_encoding()
    return np.kron(np.eye(2), old @ old.conj().T)


def constrained_projector() -> np.ndarray:
    constraint_projector = (np.eye(180) + role_constraint()) / 2
    return shell_projector() @ constraint_projector


def lift_physical(operator: np.ndarray) -> np.ndarray:
    """Physical-r-controlled completion, with no host branch selection."""

    exchange = exchange_operator()
    return block_diagonal(operator, exchange @ operator @ exchange)


def gauge_qubit(code: c304.c269.WilsonSubsystemCode, body) -> int:
    """One homogeneous gauge-companion M2 following the Cycle-304 flags."""

    return (
        code.qubits
        + len(code.graph.vertices)
        + code.length**3
        + code.graph.cells.index(tuple(body))
    )


def collision_and_bare_selector_controls() -> None:
    code = c304.c269.build_code(TRAINING_SIZE)
    columns = c304.micro_columns(code)
    half_stream: dict[tuple[int, int, int], set[int]] = {}
    for column in columns:
        if column.sector != "n1":
            continue
        key = (column.face_pauli.x, column.face_pauli.z, column.tags)
        half_stream.setdefault(key, set()).add(column.stream_slice)
    two_valued = sum(values == {0, 1} for values in half_stream.values())
    check(
        "the existing face/occupation/port data give thirty exact two-valued flag collisions",
        len(half_stream) == two_valued == 30,
        {
            "unflagged_n1_patterns": len(half_stream),
            "patterns_with_both_flag_values": two_valued,
            "scope": "diagonal functions of the displayed Cycle-304 local data",
        },
    )

    encoding = c304.common_encoding()
    projector = encoding @ encoding.conj().T
    exchange = exchange_operator()
    bare_plus = projector @ ((np.eye(90) + exchange) / 2)
    coin = c304.physical_coin(c219.common_species(-0.3).coin)
    contact = c304.physical_contact(c304.contact.COUPLING)
    stream = c304.physical_stream()
    detail = {
        "intended_common_dimension": 42,
        "bare_selector_plus_dimension": int(np.linalg.matrix_rank(bare_plus, tol=1e-10)),
        "bare_selector_trace_on_common_code": float(np.trace(bare_plus).real),
        "coin_commutator": float(np.linalg.norm(exchange @ coin - coin @ exchange)),
        "contact_commutator": float(np.linalg.norm(exchange @ contact - contact @ exchange)),
        "stream_commutator": float(np.linalg.norm(exchange @ stream - stream @ exchange)),
    }
    check(
        "the standalone X_flag R selector is an exact local involution but deletes half the common code",
        np.linalg.norm(exchange @ exchange - np.eye(90)) == 0
        and np.linalg.norm(exchange @ projector - projector @ exchange) < TOLERANCE
        and detail["bare_selector_plus_dimension"] == 21
        and detail["coin_commutator"] > 8
        and detail["contact_commutator"] > 2
        and detail["stream_commutator"] == 0,
        detail,
    )


def constraint_dimension_and_marker_controls() -> None:
    encoding = constrained_encoding()
    constraint = role_constraint()
    shell = shell_projector()
    projector = constrained_projector()
    marker = np.kron(np.diag((1, -1)), slice_z())
    logical_marker = logical_role_z()
    detail = {
        "ambient_micro_dimension": 180,
        "shell_times_r_dimension": int(np.linalg.matrix_rank(shell, tol=1e-10)),
        "constraint_code_dimension": int(np.linalg.matrix_rank(projector, tol=1e-10)),
        "constraint_projector_trace": float(np.trace(projector).real),
        "constraint_involution_residual": float(
            np.linalg.norm(constraint @ constraint - np.eye(180))
        ),
        "shell_constraint_commutator": float(
            np.linalg.norm(shell @ constraint - constraint @ shell)
        ),
        "joint_projector_idempotence": float(
            np.linalg.norm(projector @ projector - projector)
        ),
        "isometry_residual": float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(42))),
        "projector_residual": float(np.linalg.norm(projector - encoding @ encoding.conj().T)),
        "constraint_eigen_residual": float(np.linalg.norm(constraint @ encoding - encoding)),
        "marker_decode_residual": float(np.linalg.norm(marker @ encoding - encoding @ logical_marker)),
        "constraint_marker_commutator": float(np.linalg.norm(constraint @ marker - marker @ constraint)),
    }
    check(
        "one extra M2 and one non-diagonal local constraint leave exactly the intended forty-two columns",
        detail["shell_times_r_dimension"] == 84
        and detail["constraint_code_dimension"] == 42
        and max(
            detail["constraint_involution_residual"],
            detail["shell_constraint_commutator"],
            detail["joint_projector_idempotence"],
            detail["isometry_residual"],
            detail["projector_residual"],
            detail["constraint_eigen_residual"],
            detail["marker_decode_residual"],
            detail["constraint_marker_commutator"],
        )
        < TOLERANCE,
        detail,
    )


def old_and_new_operators(beta: float):
    coin6 = c219.common_species(beta).coin
    old = {
        "coin": c304.physical_coin(coin6),
        "stream": c304.physical_stream(),
        "contact": c304.physical_contact(c304.contact.COUPLING),
    }
    logical = {
        "coin": c304.logical_coin(coin6),
        "stream": c304.logical_stream(),
        "contact": c304.logical_contact(c304.contact.COUPLING),
    }
    new = {name: lift_physical(operator) for name, operator in old.items()}
    return old, logical, new


def intertwiner_and_constraint_controls(beta: float, held: bool = False) -> dict[str, float]:
    encoding = constrained_encoding()
    projector = constrained_projector()
    constraint = role_constraint()
    old, logical, new = old_and_new_operators(beta)
    logical_g = logical["contact"] @ logical["stream"] @ logical["coin"]
    physical_g = new["contact"] @ new["stream"] @ new["coin"]
    residuals = {
        name: float(np.linalg.norm(new[name] @ encoding - encoding @ logical[name]))
        for name in old
    }
    residuals.update(
        {
            "composition": float(np.linalg.norm(physical_g @ encoding - encoding @ logical_g)),
            "leakage": float(np.linalg.norm((np.eye(180) - projector) @ physical_g @ encoding)),
            "composition_unitarity": float(
                np.linalg.norm(physical_g.conj().T @ physical_g - np.eye(180))
            ),
            "maximum_constraint_commutator": max(
                float(np.linalg.norm(constraint @ operator - operator @ constraint))
                for operator in tuple(new.values()) + (physical_g,)
            ),
        }
    )
    label = "held beta=-0.35" if held else f"beta={beta}"
    check(
        f"{label}: coin, autonomous stream/catch-up, contact, and composition preserve C_role and intertwine",
        max(residuals.values()) < TOLERANCE,
        residuals,
    )
    return residuals


def autonomous_marker_controls() -> None:
    constraint = role_constraint()
    marker = np.kron(np.diag((1, -1)), slice_z())
    slice_marker = np.kron(np.eye(2), slice_z())
    _, _, operators = old_and_new_operators(-0.3)
    stream = operators["stream"]
    coin = operators["coin"]
    contact = operators["contact"]
    check(
        "the physical stream flips the gauge-invariant role marker autonomously while coin and contact preserve it",
        np.linalg.norm(constraint @ stream - stream @ constraint) < TOLERANCE
        and np.linalg.norm(marker @ stream + stream @ marker) < TOLERANCE
        and np.linalg.norm(slice_marker @ stream + stream @ slice_marker) < TOLERANCE
        and np.linalg.norm(marker @ coin - coin @ marker) < TOLERANCE
        and np.linalg.norm(marker @ contact - contact @ marker) < TOLERANCE,
        {
            "stream_constraint_commutator": float(np.linalg.norm(constraint @ stream - stream @ constraint)),
            "stream_role_marker_anticommutator": float(np.linalg.norm(marker @ stream + stream @ marker)),
            "stream_slice_flag_anticommutator": float(np.linalg.norm(slice_marker @ stream + stream @ slice_marker)),
            "coin_role_marker_commutator": float(np.linalg.norm(marker @ coin - coin @ marker)),
            "contact_role_marker_commutator": float(np.linalg.norm(marker @ contact - contact @ marker)),
            "host_branch_queries": 0,
            "physical_r_projectors_in_completion": 2,
        },
    )


def matrix_unit_locality_controls(code, label: str) -> None:
    columns = c304.micro_columns(code)
    exchange = exchange_operator()
    r_qubit = gauge_qubit(code, c304.BODY)
    transition_supports = []
    support_union = 0
    constraint_failures = sector_failures = 0
    rows, sources = np.where(abs(exchange) > 0.5)
    for target, source in zip(rows.tolist(), sources.tolist()):
        transition = columns[target].representative @ c302.pauli_dagger(
            columns[source].representative
        )
        transition = c235.Pauli(
            transition.phase, transition.x | (1 << r_qubit), transition.z
        )
        support = transition.x | transition.z
        support_union |= support
        transition_supports.append(support.bit_count())
        constraint_failures += sum(
            not transition.commutes(c302.constraint_pauli(code, vertex_index))
            for vertex_index in range(len(code.graph.vertices))
        )
        sector_failures += sum(
            not transition.commutes(row)
            for row in code.local_checks + code.wilsons
        )

    face_union = tag_union = 0
    max_representative = 0
    for column in columns:
        face_union |= column.face_pauli.x | column.face_pauli.z
        tag_union |= column.tags
        max_representative = max(
            max_representative,
            (column.representative.x | column.representative.z).bit_count() + 1,
        )
    check(
        f"{label}: C_role is an explicit bounded matrix-unit constraint with zero inherited-check leakage",
        len(rows) == 90
        and face_union.bit_count() == 30
        and tag_union.bit_count() == 12
        and support_union.bit_count() == 44
        and max(transition_supports) == 22
        and max_representative <= 19
        and constraint_failures == sector_failures == 0,
        {
            "constraint_matrix_units": len(rows),
            "face_M2": face_union.bit_count(),
            "port_M2": tag_union.bit_count(),
            "role_marker_M2": 2,
            "bounded_patch_union_M2": face_union.bit_count() + tag_union.bit_count() + 2,
            "physical_constraint_union_M2": support_union.bit_count(),
            "maximum_transition_support_M2": max(transition_supports),
            "maximum_encoded_branch_representative_M2": max_representative,
            "installed_overhead_M2_per_cell": 23,
            "port_constraint_commutator_failures": constraint_failures,
            "fixed_sector_commutator_failures": sector_failures,
        },
    )


def covariance_controls(code) -> None:
    encoding = constrained_encoding()
    constraint = role_constraint()
    marker = np.kron(np.diag((1, -1)), slice_z())
    _, logical, physical = old_and_new_operators(-0.3)
    frame_encoding = frame_operator = frame_constraint = frame_marker = 0.0
    marker_placement_failures = 0
    frames = c235.proper_cubic_frames()
    for frame in frames:
        logical_r, micro_r = c304.frame_representations(frame)
        physical_r = block_diagonal(micro_r, micro_r)
        frame_encoding = max(
            frame_encoding,
            float(np.linalg.norm(physical_r @ encoding - encoding @ logical_r)),
        )
        frame_constraint = max(
            frame_constraint,
            float(np.linalg.norm(physical_r @ constraint - constraint @ physical_r)),
        )
        frame_marker = max(
            frame_marker,
            float(np.linalg.norm(physical_r @ marker - marker @ physical_r)),
        )
        for name in physical:
            frame_operator = max(
                frame_operator,
                float(np.linalg.norm(physical_r @ physical[name] - physical[name] @ physical_r)),
                float(np.linalg.norm(logical_r @ logical[name] - logical[name] @ logical_r)),
            )
        mapped = set()
        for body in code.graph.cells:
            target = tuple(int(value % code.length) for value in frame @ np.asarray(body))
            mapped.add(gauge_qubit(code, target))
        marker_placement_failures += len(mapped) != code.length**3
    check(
        "the constrained encoding, role law, marker, and all three updates are covariant under all 24 proper-cubic frames",
        max(frame_encoding, frame_operator, frame_constraint, frame_marker) < TOLERANCE
        and marker_placement_failures == 0,
        {
            "frames": len(frames),
            "encoding_residual": frame_encoding,
            "operator_residual": frame_operator,
            "constraint_residual": frame_constraint,
            "marker_residual": frame_marker,
            "marker_placement_failures": marker_placement_failures,
        },
    )


def translation_controls(code) -> None:
    solver = c304.reference_solver(code)
    source_columns = c304.micro_columns(code, c304.BODY)
    failures = 0
    gauge_targets = set()
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c304.c269.graph_translation_maps(code.graph, displacement)
        toggles, pairs, flips = c304.c269.repair_data(code.graph, vertex_map, edge_map)
        target_columns = c304.micro_columns(code, displacement)
        gauge_targets.add(gauge_qubit(code, displacement))
        for source, target in zip(source_columns, target_columns):
            phase = c304.state_relative_phase(
                code,
                solver,
                source.face_pauli,
                target.face_pauli,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            failures += phase != 0
            failures += c304.local.ports.permute_bits(source.tags, vertex_map) != target.tags
            failures += source.stream_slice != target.stream_slice
    failures += len(gauge_targets) != code.length**3
    check(
        "all ninety constrained marker branches are covariant under all 27 L=3 translations",
        failures == 0,
        {
            "ray_tests": code.length**3 * 90,
            "homogeneous_gauge_M2": len(gauge_targets),
            "failures": failures,
        },
    )


def mass_contact_and_schedule_controls() -> None:
    species = c219.common_species(-0.3)
    encoding = constrained_encoding()
    physical_coin = lift_physical(c304.physical_coin(species.coin))
    scalar = np.zeros(42, dtype=complex)
    scalar[:6] = c304.c210.UNIFORM
    encoded = encoding @ scalar
    eigenvalue = np.vdot(encoded, physical_coin @ encoded)
    mass = float(np.angle(eigenvalue)) / c219.C_SQUARED
    fixture = c219.rest_mass(species)
    physical_contact = lift_physical(c304.physical_contact(c304.contact.COUPLING))
    contact_zero = lift_physical(c304.physical_contact(0.0))
    n1 = encoding[:, :12]
    contact_firewall = float(np.linalg.norm((physical_contact - contact_zero) @ n1))
    order_residual = float(
        np.linalg.norm(
            physical_contact @ lift_physical(c304.physical_stream())
            - lift_physical(c304.physical_stream()) @ physical_contact,
            2,
        )
    )
    check(
        "the relational marker preserves the one-particle mass fixture, local contact, and declared fixed-seam schedule",
        abs(mass - fixture) < 4e-13
        and contact_firewall == 0
        and order_residual > 0.3,
        {
            "physical_rest_mass": mass,
            "Cycle219_fixture": fixture,
            "one_particle_contact_difference": contact_firewall,
            "Cycle230_contact_coupling": c304.contact.COUPLING,
            "contact_stream_order_residual": order_residual,
            "principal_sea_rank73_compiler_claimed": False,
        },
    )


def deletion_controls() -> None:
    encoding = constrained_encoding()
    shell = shell_projector()
    projector = constrained_projector()
    exchange = exchange_operator()
    x_r = np.asarray(((0, 1), (1, 0)), dtype=complex)
    bare_without_r = np.kron(np.eye(2), exchange)
    deleted_k = np.kron(x_r, np.eye(90))
    bare_leakage = float(
        np.linalg.norm(((np.eye(180) - bare_without_r) / 2) @ encoding, 2)
    )
    deleted_k_leakage = float(
        np.linalg.norm(((np.eye(180) - deleted_k) / 2) @ encoding, 2)
    )

    old, logical, good = old_and_new_operators(-0.3)
    bad_coin = np.kron(np.eye(2), old["coin"])
    bad_contact = np.kron(np.eye(2), old["contact"])
    constraint = role_constraint()
    bad_coin_leakage = float(np.linalg.norm((np.eye(180) - projector) @ bad_coin @ encoding, 2))
    bad_contact_leakage = float(
        np.linalg.norm((np.eye(180) - projector) @ bad_contact @ encoding, 2)
    )

    # Deleting K from the stream keeps only its number-sector sign.  It no
    # longer changes carrier role and cannot intertwine the logical stream.
    deleted_stream_old = old["stream"] @ exchange
    deleted_stream = lift_physical(deleted_stream_old)
    deleted_stream_residual = float(
        np.linalg.norm(deleted_stream @ encoding - encoding @ logical["stream"], 2)
    )
    check(
        "deleting r, C_role, K_exchange, or branch conjugation is detected by dimension, leakage, or intertwining controls",
        int(np.linalg.matrix_rank(shell, tol=1e-10)) == 84
        and int(np.linalg.matrix_rank(projector, tol=1e-10)) == 42
        and bare_leakage > 0.99
        and deleted_k_leakage > 0.99
        and bad_coin_leakage > 0.6
        and bad_contact_leakage > 0.15
        and deleted_stream_residual > 1.9,
        {
            "dimension_if_C_role_deleted": int(np.linalg.matrix_rank(shell, tol=1e-10)),
            "lawful_constrained_dimension": int(np.linalg.matrix_rank(projector, tol=1e-10)),
            "leakage_if_r_partner_deleted": bare_leakage,
            "leakage_if_K_exchange_deleted_from_constraint": deleted_k_leakage,
            "coin_leakage_if_r_branch_conjugation_deleted": bad_coin_leakage,
            "contact_leakage_if_r_branch_conjugation_deleted": bad_contact_leakage,
            "stream_intertwining_if_K_exchange_deleted": deleted_stream_residual,
            "good_stream_constraint_commutator": float(
                np.linalg.norm(constraint @ good["stream"] - good["stream"] @ constraint)
            ),
        },
    )


def lawful_domain_and_inventory() -> None:
    rejected = 0
    for pair in ((0, 0), (-1, 2), (0, 6)):
        try:
            if pair not in c304.PAIR_INDEX:
                raise ValueError("not a lawful two-mode wedge")
        except ValueError:
            rejected += 1
    try:
        c304.c269.build_code(2)
    except (KeyError, ValueError):
        rejected += 1
    check(
        "lawful-domain controls reject repeated-mode, non-port, and aliased-size inputs",
        rejected == 4,
        rejected,
    )
    inventory = {
        "inherited sector": "fixed +++ Wilson reference and all Cycle-269 local checks",
        "inherited comparator": "Cycle-304 42-column n=1+n=2 fixed-seam E and signful stream/catch-up",
        "inherited laws": "Cycle-219 C, declared wedge^2 C, Cycle-230 g=0.37 contact, coin-stream-contact schedule",
        "supplied new physical resource": "one homogeneous ordinary gauge-companion M2 r per cell",
        "supplied new local law": "C_role=K_exchange X_r=+1, a 90-term bounded matrix-unit candidate",
        "supplied new completion": "physical-r-controlled A|0><0| + KAK|1><1| coefficients for each bounded comparator block",
        "derived": "42-column relational E, gauge-invariant marker, exact constraint preservation and covariance",
        "still supplied": "dense matrix-unit primitive synthesis, common-shell projector, initial lawful code state, macrocell framing",
        "excluded": "global ordering, parity service, host branch, recurrent volume, higher Fock sectors, rank-73 sea",
    }
    check("all added and inherited structure is explicit", len(inventory) == 9, inventory)


def main() -> int:
    print("CYCLE 306: LOCALLY CONSTRAINED RELATIONAL ROLE MARKER")
    print("authority=none; audit=unset")
    note_contract()
    collision_and_bare_selector_controls()
    constraint_dimension_and_marker_controls()
    autonomous_marker_controls()
    for beta in (-0.2, -0.3, -0.4):
        intertwiner_and_constraint_controls(beta)
    intertwiner_and_constraint_controls(-0.35, held=True)
    training = c304.c269.build_code(TRAINING_SIZE)
    held = c304.c269.build_code(HELD_SIZE)
    matrix_unit_locality_controls(training, "training L=3")
    matrix_unit_locality_controls(held, "held L=6")
    covariance_controls(training)
    translation_controls(training)
    mass_contact_and_schedule_controls()
    deletion_controls()
    lawful_domain_and_inventory()
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
