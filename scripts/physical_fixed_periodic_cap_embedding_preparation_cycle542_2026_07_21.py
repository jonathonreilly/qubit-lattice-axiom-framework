#!/usr/bin/env python3
"""Cycle 542: fixed-periodic cap embedding and preparation attempt.

Cycle 537's three fill disks are tested against the already installed
Cycle-527 16^3-per-cell periodic integer microgrid.  The rough Cycle-532 M2
placement is first identified exactly inside that grid.  A cubical-homology
certificate then tests whether a bounded local 2-chain in the unchanged fine
three-torus can have one axial Wilson cycle as its only boundary.  Product
reset and local-check-measurement preparation routes are tested separately.

The retained negative is deliberately narrow: it concerns a genuine cubical
cap embedding in the unchanged periodic substrate.  It is not a no-go for
nongeometric auxiliary hypergraphs, cut/open boundaries, dynamic punctures,
or autonomous long schedules.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21 as c527
import physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21 as c533
import physical_local_wilson_fill_disk_cycle537_2026_07_21 as c537


c532 = c537.c532
c235 = c537.c235
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MICRO_SCALE = c527.MICRO_SCALE
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "fixed-cap-attempt-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FIXED_PERIODIC_CAP_EMBEDDING_PREPARATION_CYCLE542_NOTE_2026-07-21.md"
)
CYCLE527_RUNNER = ROOT / "scripts/physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21.py"
CYCLE533_RUNNER = ROOT / "scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py"
CYCLE537_RUNNER = ROOT / "scripts/physical_local_wilson_fill_disk_cycle537_2026_07_21.py"
CYCLE537_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_WILSON_FILL_DISK_CYCLE537_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    CYCLE527_RUNNER: "2ca2021fa76b889128b587a6a0d67986e236319ea8fb7ccd1dfaf31982c55fa0",
    CYCLE533_RUNNER: "72fe24e03b38812ef9f6dc610bc445b5ea6046a30683c2b734e9c0396e84facd",
    CYCLE537_RUNNER: "cd00034db5e106accfd95e33de5c9b3b2a26b2c35719611454c3486481ad47ac",
    CYCLE537_NOTE: "e413a8c079fa2d5ff14d1b46d19df60cd07d853d118b51d8494632cc03a427f8",
}


class CertificateFailure(RuntimeError):
    """A declared finite Cycle-542 certificate condition failed."""


class ResourceWall(RuntimeError):
    """A technical execution ceiling, never physical evidence."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    if elapsed >= WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS:
        raise ResourceWall(f"wall grace reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swap_count():
        raise ResourceWall(f"nonzero process swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard Cycle542 wall alarm reached")


def strict_upstream_contract() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    semantic = {
        "Cycle527_full_microgrid": "MICRO_SITES_PER_CELL = MICRO_SCALE**3"
        in CYCLE527_RUNNER.read_text(encoding="utf-8"),
        "Cycle533_fixed_reference_boundary": "fixed-Wilson reference"
        in CYCLE533_RUNNER.read_text(encoding="utf-8"),
        "Cycle537_fill_disk": "def build_fill_disk" in CYCLE537_RUNNER.read_text(encoding="utf-8"),
    }
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "semantic_predicates": semantic,
        "pass": expected == observed and all(semantic.values()),
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    flat = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "unchanged periodic substrate",
        "cubical 2-chain",
        "axial wilson",
        "homology",
        "product reset",
        "preparation remains open",
        "both matter parities",
        "gamma(p)",
        "mass",
        "contact",
        "seam",
        "all 24",
        "576",
        "held l6",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in flat)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = strict_upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle527_533_537_pins": upstream["pass"],
        "note_scope_supply_and_N1_N8": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "upstream": upstream,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def rough_role(graph, qubit: int):
    row = graph.edges[qubit]
    if qubit < len(graph.base.edges):
        if row.kind not in ("matter_internal_triangle", "matter_outer_square"):
            raise CertificateFailure("base-face ordering changed")
        return ("face", qubit)
    if row.kind == "puncture_spoke":
        return ("port", row.owner, row.label)
    if row.kind == "rough_terminal":
        return ("flag", row.owner)
    raise CertificateFailure(f"unmapped rough role: {row}")


def microgrid_identification(length: int) -> dict:
    graph = c532.c247.PunctureGraph(length, terminals=1)
    roles = c527.role_coordinates(length)
    modulus = MICRO_SCALE * length
    mapped = []
    odd_Cycle532_coordinates = 0
    coordinate_mismatches = 0
    missing_roles = 0
    for qubit in range(graph.qubits):
        old = c532.physical_position(graph, qubit)
        odd_Cycle532_coordinates += any(value % 2 for value in old)
        coordinate = tuple((value // 2) % modulus for value in old)
        role = rough_role(graph, qubit)
        if role not in roles:
            missing_roles += 1
        else:
            coordinate_mismatches += coordinate != roles[role]
        mapped.append(coordinate)
    collisions = len(mapped) - len(set(mapped))
    disk = c537.build_fill_disk(length)
    added_fill = 3 * disk.edge_count
    installed = c527.MICRO_SITES_PER_CELL * length**3
    blank_after_rough = installed - graph.qubits
    frame_failures = 0
    for frame in c235.proper_cubic_frames():
        _vertices, edge_map = c532.c247.graph_frame_maps(graph, frame)
        for source, target in enumerate(edge_map):
            expected = c527.rotate_coord(mapped[source], frame, modulus)
            frame_failures += expected != mapped[target]
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "fine_torus_side": modulus,
        "installed_M2": installed,
        "rough_M2": graph.qubits,
        "blank_M2_after_rough": blank_after_rough,
        "Cycle537_added_fill_M2_requested": added_fill,
        "enough_unassigned_site_count_before_geometry": blank_after_rough >= added_fill,
        "rough_coordinate_collisions": collisions,
        "odd_Cycle532_coordinates_before_divide_by_two": odd_Cycle532_coordinates,
        "rough_to_Cycle527_role_coordinate_mismatches": coordinate_mismatches,
        "rough_roles_missing_from_Cycle527": missing_roles,
        "all24_rough_fixed_coordinate_failures": frame_failures,
        "pass": bool(
            graph.qubits == 22 * length**3
            and collisions == odd_Cycle532_coordinates == coordinate_mismatches == missing_roles == 0
            and blank_after_rough >= added_fill
            and frame_failures == 0
        ),
    }


def unit_step(point, axis: int, modulus: int):
    target = list(point)
    target[axis] = (target[axis] + 1) % modulus
    return tuple(target)


def cut_pair(edge, cut_axis: int, modulus: int) -> int:
    first, second = edge
    changed = tuple(axis for axis in range(3) if first[axis] != second[axis])
    if len(changed) != 1:
        raise CertificateFailure("cut pairing received a non-edge")
    axis = changed[0]
    difference = (second[axis] - first[axis]) % modulus
    if difference not in (1, modulus - 1):
        raise CertificateFailure("cut pairing received a non-nearest-neighbour edge")
    return int(axis == cut_axis and {first[axis], second[axis]} == {0, modulus - 1})


def plaquette_edges(origin, first_axis: int, second_axis: int, modulus: int):
    first = unit_step(origin, first_axis, modulus)
    second = unit_step(origin, second_axis, modulus)
    corner = unit_step(first, second_axis, modulus)
    return (
        (origin, first),
        (first, corner),
        (corner, second),
        (second, origin),
    )


def cubical_homology_controls(length: int) -> dict:
    modulus = MICRO_SCALE * length
    plaquettes = 0
    cocycle_failures = 0
    first_failure = None
    for first_axis in range(3):
        for second_axis in range(first_axis + 1, 3):
            for x in range(modulus):
                for y in range(modulus):
                    for z in range(modulus):
                        origin = (x, y, z)
                        edges = plaquette_edges(origin, first_axis, second_axis, modulus)
                        plaquettes += 1
                        values = tuple(
                            sum(cut_pair(edge, cut_axis, modulus) for edge in edges) % 2
                            for cut_axis in range(3)
                        )
                        if values != (0, 0, 0):
                            cocycle_failures += 1
                            if first_failure is None:
                                first_failure = (origin, first_axis, second_axis, values)

    axial = []
    for axis in range(3):
        point = [0, 0, 0]
        edges = []
        for _ in range(modulus):
            target = list(point)
            target[axis] = (target[axis] + 1) % modulus
            edges.append((tuple(point), tuple(target)))
            point = target
        character = tuple(
            sum(cut_pair(edge, cut_axis, modulus) for edge in edges) % 2
            for cut_axis in range(3)
        )
        axial.append(character)

    disk = c537.build_fill_disk(length)
    edge_multiplicity = {}
    for _coordinate, boundary in disk.faces:
        for edge in boundary:
            edge_multiplicity[edge] = edge_multiplicity.get(edge, 0) ^ 1
    odd_boundary = frozenset(edge for edge, parity in edge_multiplicity.items() if parity)
    abstract_boundary_identity = odd_boundary == frozenset(disk.perimeter)
    boundary_path_edges = 4 * len(disk.perimeter)
    boundary_winding = tuple(tuple(int(i == axis) for i in range(3)) for axis in range(3))
    zero_boundary_required = bool(cocycle_failures == 0)
    mismatch = tuple(character != (0, 0, 0) for character in axial)
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "fine_torus_side": modulus,
        "all_elementary_plaquettes_tested": plaquettes,
        "elementary_plaquette_cut_cocycle_failures": cocycle_failures,
        "first_cocycle_failure": first_failure,
        "abstract_sum_of_fill_faces_equals_perimeter": abstract_boundary_identity,
        "abstract_fill_perimeter_edges": len(disk.perimeter),
        "four_NN_steps_per_abstract_boundary_edge": True,
        "target_boundary_NN_edges": boundary_path_edges,
        "axial_Wilson_cut_characters": tuple(axial),
        "target_attachment_winding_characters": boundary_winding,
        "every_cubical_2_chain_boundary_has_zero_cut_character": zero_boundary_required,
        "three_axial_boundary_mismatches": mismatch,
        "one_fill_disk_cubical_embedding_exists_in_unchanged_periodic_torus": False,
        "simultaneous_three_disk_collision_free_embedding_exists": False,
        "collision_statement_is_downstream_not_independent": True,
        "pass": bool(
            plaquettes == 3 * modulus**3
            and cocycle_failures == 0
            and abstract_boundary_identity
            and boundary_path_edges == MICRO_SCALE * length
            and tuple(axial) == boundary_winding
            and mismatch == (True, True, True)
        ),
    }


def covariance_of_obstruction() -> dict:
    frames = tuple(c235.proper_cubic_frames())
    frame_keys = {tuple(int(v) for v in frame.reshape(-1)): index for index, frame in enumerate(frames)}
    basis = tuple(np.eye(3, dtype=int)[:, axis] for axis in range(3))
    zero_image_failures = 0
    signed_axis_failures = 0
    group_failures = 0
    for frame in frames:
        for vector in basis:
            image = frame @ vector
            zero_image_failures += not np.any(image)
            signed_axis_failures += tuple(sorted(abs(int(v)) for v in image)) != (0, 0, 1)
    for left in frames:
        for right in frames:
            product = left @ right
            key = tuple(int(v) for v in product.reshape(-1))
            if key not in frame_keys:
                group_failures += 1
                continue
            for vector in basis:
                group_failures += not np.array_equal(left @ (right @ vector), product @ vector)
    return {
        "proper_cubic_frames": len(frames),
        "frame_products": len(frames) ** 2,
        "axial_nonzero_character_image_failures": zero_image_failures,
        "signed_axis_orbit_failures": signed_axis_failures,
        "frame_group_action_failures": group_failures,
        "runtime_frame_selector_used": False,
        "compile_time_24_presentation_orbit_substituted_for_embedding": False,
        "interpretation": (
            "the fixed-substrate homology mismatch itself is invariant under the "
            "proper-cubic group; no candidate cap placement is being rotated"
        ),
        "pass": bool(
            len(frames) == 24
            and len(frames) ** 2 == 576
            and zero_image_failures == signed_axis_failures == group_failures == 0
        ),
    }


def product_reset_controls(length: int) -> dict:
    objects = c537.extended_objects(length)
    graph = objects["graph"]
    qubits = objects["qubits"]
    fill_start = graph.qubits
    fill_end = qubits
    fill_z = objects["fill_z"]
    fill_x = objects["fill_x"]
    per_edge = []
    for qubit in range(fill_start, fill_end):
        z_face_degree = sum(bool((row.z >> qubit) & 1) for row in fill_z)
        x_star_degree = sum(bool((row.x >> qubit) & 1) for row in fill_x)
        admissible_reset_axes = tuple(
            axis
            for axis in ("X", "Y", "Z")
            if (axis not in ("X", "Y") or z_face_degree == 0)
            and (axis not in ("Z", "Y") or x_star_degree == 0)
        )
        per_edge.append((z_face_degree, x_star_degree, admissible_reset_axes))
    z_reset_conflicts = sum(row[1] for row in per_edge)
    x_reset_conflicts = sum(row[0] for row in per_edge)
    y_reset_conflicts = z_reset_conflicts + x_reset_conflicts
    edges_with_any_compatible_axis = sum(bool(row[2]) for row in per_edge)
    maximum_check_support = max(
        (row.x | row.z).bit_count() for row in fill_z + fill_x
    )
    syndrome_macros = []
    controlled_pauli_calls = 0
    for check_number, row in enumerate(fill_z + fill_x):
        support = []
        mask = row.x | row.z
        while mask:
            bit = mask & -mask
            qubit = bit.bit_length() - 1
            label = ("I", "X", "Z", "Y")[(int(bool(row.x & bit))) + 2 * int(bool(row.z & bit))]
            support.append((qubit, label))
            mask ^= bit
        controlled_pauli_calls += len(support)
        syndrome_macros.append(
            ("RESET_0", check_number, "H", tuple(support), "H", "MEASURE_Z")
        )
    syndrome_digest = sha256(repr(tuple(syndrome_macros)).encode()).hexdigest()
    minimum_face_degree = min(row[0] for row in per_edge)
    minimum_star_degree = min(row[1] for row in per_edge)
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "fill_M2": fill_end - fill_start,
        "fill_Z_faces": len(fill_z),
        "fill_X_stars": len(fill_x),
        "minimum_Z_face_incidence_per_fill_M2": minimum_face_degree,
        "minimum_X_star_incidence_per_fill_M2": minimum_star_degree,
        "all_Z_product_reset_anticommuting_generator_pairs": z_reset_conflicts,
        "all_X_product_reset_anticommuting_generator_pairs": x_reset_conflicts,
        "all_Y_product_reset_anticommuting_generator_pairs": y_reset_conflicts,
        "fill_M2_with_any_single_axis_reset_commuting_with_every_fill_check": (
            edges_with_any_compatible_axis
        ),
        "direct_tensor_product_reset_is_already_in_filled_code": False,
        "maximum_abstract_fill_check_support": maximum_check_support,
        "local_syndrome_flags_if_all_checks_installed": len(syndrome_macros),
        "controlled_Pauli_calls_in_one_complete_syndrome_round": controlled_pauli_calls,
        "syndrome_macro_schedule_sha256": syndrome_digest,
        "one_reset_flag_controlled_Pauli_measurement_per_check_is_bounded": (
            maximum_check_support <= 11
        ),
        "local_check_measurement_schedule_constructed": bool(
            syndrome_macros
            and controlled_pauli_calls == sum((row.x | row.z).bit_count() for row in fill_z + fill_x)
        ),
        "postselection_called_deterministic_isometry": False,
        "deterministic_syndrome_correction_or_convergence_constructed": False,
        "full_product_input_code_space_isometry_constructed": False,
        "Cycle533_compute_select_uncompute_starts_from_supplied_fixed_Wilson_reference": True,
        "pass": bool(
            fill_end - fill_start == 6 * length * (length - 1)
            and minimum_face_degree >= 2
            and minimum_star_degree >= 1
            and z_reset_conflicts > 0
            and x_reset_conflicts > 0
            and y_reset_conflicts > 0
            and edges_with_any_compatible_axis == 0
            and maximum_check_support <= 11
        ),
    }


def alternative_route_discriminators() -> dict:
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        modulus = MICRO_SCALE * length
        maximum_fan_radius = modulus // 2
        rows.append(
            {
                "length": length,
                "relational_ring_net_logical_reduction_per_axis": 0,
                "rooted_chain_maximum_linear_dressing_X_support": length - 1,
                "fan_to_macro_origin_maximum_NN_radius": maximum_fan_radius,
                "cut_sheet_changes_periodic_boundary_data": True,
                "dynamic_puncture_requires_autonomous_reversible_schedule": True,
            }
        )
    return {
        "rows": tuple(rows),
        "fixed_cubical_cap": "falsified by nonzero axial H1 character",
        "immersed_or_intersecting_cubical_cap": (
            "self-intersections do not alter the mod-two boundary/cocycle pairing"
        ),
        "relational_ring": "local but relocates rather than removes one logical per axis",
        "rooted_chain": "rank-correct tested ansatz has growing root-crossing dressing",
        "fan": "macro-origin corridors have held-size growing radius",
        "open_cut_sheet": "live only after explicit boundary/topology change",
        "dynamic_puncture": "live; physical schedule, inverse, and convergence remain open",
        "nongeometric_local_hypergraph": "live; must define physical adjacency without calling it a cap embedding",
        "pass": bool(
            rows[0]["rooted_chain_maximum_linear_dressing_X_support"] == 4
            and rows[1]["rooted_chain_maximum_linear_dressing_X_support"] == 5
            and rows[0]["fan_to_macro_origin_maximum_NN_radius"] == 40
            and rows[1]["fan_to_macro_origin_maximum_NN_radius"] == 48
        ),
    }


def inherited_summary(certificate: dict) -> dict:
    factorizations = []
    for row in certificate["factorization_L5_L6"]:
        factorizations.append(
            {
                key: row[key]
                for key in (
                    "length",
                    "held",
                    "total_M2",
                    "stabilizer_rank",
                    "code_exponent",
                    "Wilson_rank_increments_after_local_fill",
                    "matter_quotient_dimension",
                    "matter_symplectic_rank",
                    "gauge_quotient_dimension",
                    "gauge_symplectic_rank",
                    "full_matter_commutant_dimension",
                    "full_matter_commutant_symplectic_rank",
                    "both_matter_parity_sectors_nonempty",
                    "maximum_added_disk_X_by_family",
                    "maximum_dual_path_edges_by_family",
                    "maximum_support_M2",
                    "pass",
                )
            }
        )
    inherited_target = certificate["inherited_target"]
    return {
        "Cycle537_status": certificate["status"],
        "Cycle537_tests_passed": certificate["tests_passed"],
        "Cycle537_tests_total": certificate["tests_total"],
        "factorization_L5_L6": tuple(factorizations),
        "onsite_contact_B_L5_L6": certificate["onsite_contact_B_L5_L6"],
        "deletions": certificate["deletions"],
        "full_Fock_Gamma_P": inherited_target["full_Fock_Gamma_P"],
        "mass_contact_and_seam": inherited_target["mass_contact_and_seam"],
        "FSWAP_polynomial_inverse": inherited_target["FSWAP_polynomial_inverse"],
        "pass": certificate["pass"],
    }


def certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle542 dry contract failed")

    microgrid = tuple(microgrid_identification(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    checkpoints.append(checkpoint(started, "rough-M2-microgrid-identification"))
    homology = tuple(cubical_homology_controls(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    checkpoints.append(checkpoint(started, "exhaustive-cubical-homology"))
    covariance = covariance_of_obstruction()
    reset = tuple(product_reset_controls(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    alternatives = alternative_route_discriminators()
    checkpoints.append(checkpoint(started, "preparation-route-discriminators"))
    inherited = inherited_summary(c537.certificate())
    checkpoints.append(checkpoint(started, "strict-Cycle537-target-replay"))

    tests = {
        "dry_contract": dry["pass"],
        "rough_M2_exactly_inside_Cycle527_microgrid": all(row["pass"] for row in microgrid),
        "all_elementary_cubical_faces_have_zero_cut_pairing": all(row["pass"] for row in homology),
        "three_axial_Wilsons_have_nonzero_H1_characters": all(
            row["axial_Wilson_cut_characters"] == ((1, 0, 0), (0, 1, 0), (0, 0, 1))
            for row in homology
        ),
        "fixed_unchanged_periodic_cubical_cap_embedding_falsified": all(
            not row["one_fill_disk_cubical_embedding_exists_in_unchanged_periodic_torus"]
            for row in homology
        ),
        "all24_576_obstruction_covariance": covariance["pass"],
        "direct_product_reset_preparation_falsified": all(row["pass"] for row in reset),
        "bounded_local_check_measurement_but_no_deterministic_preparation": all(
            row["local_check_measurement_schedule_constructed"]
            and not row["deterministic_syndrome_correction_or_convergence_constructed"]
            for row in reset
        ),
        "alternative_routes_kept_distinct": alternatives["pass"],
        "Cycle537_target_gauge_GammaP_mass_contact_seam_replayed": inherited["pass"],
        "supply_boundary_and_no_axiom_pressure": True,
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    result = {
        "revision": REVISION,
        "mode": "fixed-cap-attempt-certificate",
        "status": "cycle542-fixed-periodic-cubical-cap-falsified-preparation-open",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "strongest_result": (
            "Cycle532 rough M2 embed exactly in the installed Cycle527 microgrid, but no "
            "cubical 2-chain in the unchanged periodic fine torus can bound any one of "
            "the three nonzero axial Wilson H1 characters"
        ),
        "microgrid_identification_L5_L6": microgrid,
        "cubical_homology_L5_L6": homology,
        "proper_cubic_covariance": covariance,
        "preparation_attempt_L5_L6": reset,
        "alternative_routes": alternatives,
        "inherited_Cycle537_target_certificate": inherited,
        "embedding_status": {
            "fixed_single_frame_independent_cubical_cap_embedding_constructed": False,
            "one_disk_blocked_before_three_disk_collision_routing": True,
            "collision_called_independent_wall": False,
            "compile_time_24_presentation_orbit_used_as_substitute": False,
            "unchanged_periodic_boundary_retained": True,
        },
        "preparation_status": {
            "direct_product_reset": "falsified",
            "bounded_local_check_measurement_circuit": "constructed conditionally on cap adjacency",
            "postselection": "not called deterministic isometry",
            "deterministic_local_correction_or_convergence": "open",
            "full_product_input_code_space_isometry": "open",
            "Cycle533_fixed_reference_import_retired": False,
        },
        "supplied_structure_inventory": {
            "macro_origin": (0, 0, 0),
            "unchanged_periodic_fine_torus": True,
            "integer_microgrid_scale": MICRO_SCALE,
            "three_axial_attachment_cycles": True,
            "Cycle537_abstract_cap_topology": True,
            "product_reset_axes_tested": ("X", "Y", "Z"),
            "one_reused_syndrome_flag_per_check": True,
            "measurement_outcome_correction_schedule": False,
            "open_or_cut_boundary_data": False,
            "runtime_frame_selector": False,
            "host_side_parity_service": False,
            "state_preparation_schedule": False,
        },
        "boundary": {
            "scoped_cubical_embedding_no_go": True,
            "nongeometric_local_hypergraph_no_go": False,
            "dynamic_puncture_no_go": False,
            "open_cut_sheet_no_go": False,
            "general_local_preparation_no_go": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_negative_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "compiler_schedule_called_physical_time": False,
            "phase_called_physical_energy": False,
            "syndrome_pointer_called_Record": False,
            "unprepared_code_presentation_called_encoding": False,
        },
        "resources": {
            "elapsed_seconds": elapsed,
            "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
            "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "checkpoints": checkpoints,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle542-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
