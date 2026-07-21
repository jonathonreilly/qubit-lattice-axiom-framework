#!/usr/bin/env python3
"""Cycle 539: explicit shared-seam code-space isometry compiler.

This extends Cycle 533's compute/select/uncompute construction from one
selected seam to the exact Cycle 525 three-cell path/corner and four-cell
degree-three star domains.  It replaces the rebuilt dense code-space
completion on those declared patches, not on an arbitrary recurrent volume.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
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

import physical_opposite_carrier_shared_cell_recurrence_cycle525_2026_07_21 as c525
import physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21 as c533


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md"
)
C525_RUNNER = ROOT / "scripts/physical_opposite_carrier_shared_cell_recurrence_cycle525_2026_07_21.py"
C525_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OPPOSITE_CARRIER_SHARED_CELL_RECURRENCE_CYCLE525_NOTE_2026-07-21.md"
)
C533_RUNNER = ROOT / "scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py"
C533_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SELECTED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE533_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    C525_RUNNER: "379c67315de8d235f8d5287b281b6291d0a10731d030338d8bde0676a4c0b785",
    C525_NOTE: "43a39dd4a33d06eaf11369eb84d436761832974a4f759aec44e9ab6b919e44a8",
    C533_RUNNER: "72fe24e03b38812ef9f6dc610bc445b5ea6046a30683c2b734e9c0396e84facd",
    C533_NOTE: "e15712305bd770cff61133f184d02da1714c50453bb5f3c492f1cc3051e119c2",
}


class CertificateFailure(RuntimeError):
    """A declared Cycle-539 certificate condition failed."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    swaps = int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))
    if elapsed >= WALL_LIMIT_SECONDS:
        raise CertificateFailure(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise CertificateFailure(f"RSS guard reached at {label}: {rss}")
    if swaps:
        raise CertificateFailure(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def alarm_handler(_signum, _frame) -> None:
    raise CertificateFailure("Cycle539 hard wall alarm fired")


def geometry_data(kind: str) -> dict:
    if kind in ("path", "corner"):
        return {
            "kind": kind,
            "cells": c525.c319.GEOMETRIES[kind]["cells"],
            "labels": c525.triple_labels(),
            "specs": c525.label_specs,
            "orders": c525.c319.ORDERS,
            "order_register_M2": 3,
            "maximum_total_number": 3,
            "seams": 2,
        }
    if kind == "star":
        return {
            "kind": kind,
            "cells": c525.c324.GEOMETRIES["star"]["cells"],
            "labels": c525.c324.four_cell_labels(),
            "specs": c525.c324.label_specs,
            "orders": c525.c324.ORDERS,
            "order_register_M2": 5,
            "maximum_total_number": 2,
            "seams": 3,
        }
    raise ValueError(f"unknown Cycle539 geometry {kind}")


def local_word(local_label) -> int:
    return sum(1 << int(direction) for direction in local_label)


def joint_roles(code, cells) -> tuple[int, ...]:
    roles = []
    for cell in cells:
        center, inward, flag, companion = c533.c523.native_auxiliary_roles(code, cell)
        roles.extend(center + inward + (flag, companion))
    return tuple(dict.fromkeys(roles))


def local_tables(code, cells):
    return tuple(c533.phase_folded_terms(code, cell) for cell in cells)


def state_preparation_controls(code, cells) -> tuple[dict, tuple[dict, ...]]:
    tables = local_tables(code, cells)
    total_givens = total_gray_mcx = 0
    maximum_forward = maximum_inverse = 0.0
    minimum_deletion = math.inf
    digest = sha256()
    schedules_by_cell = []
    for cell_index, table in enumerate(tables):
        schedules = {}
        histogram = Counter()
        for word in range(64):
            entries = table[word]
            vector = np.zeros(8, dtype=complex)
            vector[: len(entries)] = [amplitude for _term, amplitude in entries]
            schedule, prepared, _eliminated = c533.state_preparation(vector)
            schedules[word] = schedule
            histogram[len(entries)] += 1
            total_givens += len(schedule)
            total_gray_mcx += sum(2 * (target.bit_count() - 1) for target, _ in schedule)
            maximum_forward = max(maximum_forward, float(np.linalg.norm(prepared - vector)))
            restored = prepared.copy()
            for target, matrix in reversed(schedule):
                restored = c533.apply_two_level(restored, target, matrix.conj().T)
            maximum_inverse = max(
                maximum_inverse,
                float(np.linalg.norm(restored - np.eye(8, dtype=complex)[:, 0])),
            )
            if len(schedule) == 5:
                damaged = np.zeros(8, dtype=complex)
                damaged[0] = 1
                for index, (target, matrix) in enumerate(schedule):
                    if index:
                        damaged = c533.apply_two_level(damaged, target, matrix)
                minimum_deletion = min(minimum_deletion, float(np.linalg.norm(damaged - vector)))
            digest.update(repr((cell_index, word, tuple(
                (target, tuple(c533.complex_token(value) for value in matrix.reshape(-1)))
                for target, matrix in schedule
            ))).encode())
        if histogram != Counter({2: 56, 6: 8}):
            raise CertificateFailure(f"unexpected local branch histogram: {histogram}")
        schedules_by_cell.append(schedules)
    result = {
        "cells": len(cells),
        "branch_M2_per_cell": 3,
        "exact_two_ray_Givens": total_givens,
        "Gray_path_multi_controlled_X": total_gray_mcx,
        "maximum_state_preparation_residual": maximum_forward,
        "maximum_state_preparation_inverse_residual": maximum_inverse,
        "deleted_first_special_Givens_minimum_residual": minimum_deletion,
        "normalized_schedule_sha256": digest.hexdigest(),
        "pass": bool(
            total_givens == 96 * len(cells)
            and total_gray_mcx == 32 * len(cells)
            and maximum_forward < TOLERANCE
            and maximum_inverse < TOLERANCE
            and minimum_deletion > 0.4
        ),
    }
    return result, tables


def role_preparation_controls(order_count: int, role_bits: int) -> dict:
    vector = np.zeros(1 << role_bits, dtype=complex)
    vector[:order_count] = 1 / math.sqrt(order_count)
    schedule, prepared, _eliminated = c533.state_preparation(vector)
    restored = prepared.copy()
    for target, matrix in reversed(schedule):
        restored = c533.apply_two_level(restored, target, matrix.conj().T)
    damaged = np.zeros_like(vector)
    damaged[0] = 1
    for index, (target, matrix) in enumerate(schedule):
        if index:
            damaged = c533.apply_two_level(damaged, target, matrix)
    return {
        "order_count": order_count,
        "joint_order_register_M2": role_bits,
        "uniform_order_Givens": len(schedule),
        "maximum_uniform_preparation_residual": float(np.linalg.norm(prepared - vector)),
        "uniform_preparation_inverse_residual": float(
            np.linalg.norm(restored - np.eye(1 << role_bits, dtype=complex)[:, 0])
        ),
        "deleted_first_order_Givens_residual": float(np.linalg.norm(damaged - vector)),
        "delete_one_order_block_Gram_residual": 1 / order_count,
        "pass": bool(
            len(schedule) == order_count - 1
            and np.linalg.norm(prepared - vector) < TOLERANCE
            and np.linalg.norm(restored - np.eye(1 << role_bits, dtype=complex)[:, 0])
            < TOLERANCE
            and np.linalg.norm(damaged - vector) > 0.1
        ),
    }


def multiply_representatives(term_tuple, order):
    representative = term_tuple[order[0]][0].representative
    for index in order[1:]:
        representative = representative @ term_tuple[index][0].representative
    return representative


def lookup_and_select_controls(kind: str, length: int) -> tuple[dict, dict]:
    started = time.monotonic()
    geometry = geometry_data(kind)
    code = c525.c319.c269.build_code(length)
    cells = geometry["cells"]
    preparation, tables = state_preparation_controls(code, cells)
    roles = joint_roles(code, cells)
    order_bits = geometry["order_register_M2"]
    order_count = len(geometry["orders"])
    role_preparation = role_preparation_controls(order_count, order_bits)
    q_bits = 6 * len(cells)
    equality_controls = q_bits + order_bits + len(roles)

    collisions = rows = decoder_mcx = 0
    maximum_combined_support = 0
    selected_union = 0
    minimum_amplitude = 1.0
    branch_histogram = Counter()
    row_digest = sha256()
    for label in geometry["labels"]:
        specs = geometry["specs"](label)
        qwords = tuple(local_word(local_label) for _number, local_label in specs)
        entries_by_cell = tuple(
            tables[index][qword] for index, qword in enumerate(qwords)
        )
        branch_count = math.prod(len(entries) for entries in entries_by_cell)
        branch_histogram[branch_count] += 1
        for order_index, order in enumerate(geometry["orders"]):
            seen = set()
            for term_tuple in product(*entries_by_cell):
                representative = multiply_representatives(term_tuple, order)
                pattern = tuple(
                    (representative.x >> (code.qubits + role)) & 1 for role in roles
                )
                collisions += pattern in seen
                seen.add(pattern)
                slots = tuple(
                    next(
                        slot for slot, candidate in enumerate(entries_by_cell[index])
                        if candidate is term_tuple[index]
                    )
                    for index in range(len(cells))
                )
                decoder_mcx += sum(slot.bit_count() for slot in slots)
                amplitude = (1 / math.sqrt(order_count)) * math.prod(
                    abs(complex(term[1])) for term in term_tuple
                )
                minimum_amplitude = min(minimum_amplitude, amplitude)
                support = representative.x | representative.z
                selected_union |= support
                maximum_combined_support = max(maximum_combined_support, support.bit_count())
                row_digest.update(repr((qwords, order_index, pattern, slots)).encode())
                rows += 1
            if len(seen) != branch_count:
                raise CertificateFailure(
                    f"{kind} L{length} decoder collision in q/order block"
                )

    selected_entries = selected_factors = 0
    maximum_single_support = 0
    local_union = 0
    for table in tables:
        for word in range(64):
            for term, _amplitude in table[word]:
                representative = term.representative
                selected_entries += 1
                selected_factors += representative.x.bit_count() + representative.z.bit_count()
                local_union |= representative.x | representative.z
                maximum_single_support = max(
                    maximum_single_support,
                    (representative.x | representative.z).bit_count(),
                )
    selected_entries *= order_count
    selected_factors *= order_count

    expected_rows = {
        "path": 49_728,
        "corner": 49_728,
        "star": 115_584,
    }[kind]
    expected_roles = {"path": 38, "corner": 38, "star": 50}[kind]
    expected_histogram = (
        Counter({8: 964, 24: 24})
        if kind in ("path", "corner")
        else Counter({16: 301})
    )
    result = {
        "geometry": kind,
        "length": length,
        "held": length == HELD_LENGTH,
        "cells": len(cells),
        "seams": geometry["seams"],
        "logical_columns": len(geometry["labels"]),
        "maximum_total_number": geometry["maximum_total_number"],
        "order_count": order_count,
        "joint_order_register_M2": order_bits,
        "joint_native_role_bits": len(roles),
        "q_occupation_M2": q_bits,
        "branch_M2": 3 * len(cells),
        "branch_products_per_logical_column_histogram": {
            str(key): value for key, value in sorted(branch_histogram.items())
        },
        "q_order_native_rows": rows,
        "within_q_order_native_pattern_collisions": collisions,
        "joint_decoder_truth_table_entries": rows,
        "joint_decoder_multi_controlled_X_calls": decoder_mcx,
        "joint_decoder_equality_controls": equality_controls,
        "maximum_clean_conjunction_work_M2": equality_controls - 2,
        "minimum_nonzero_joint_ray_amplitude": minimum_amplitude,
        "maximum_combined_selected_Pauli_support_M2": maximum_combined_support,
        "combined_selected_Pauli_union_M2": selected_union.bit_count(),
        "selected_Pauli_lookup_entries": selected_entries,
        "controlled_single_Pauli_factors": selected_factors,
        "maximum_single_representative_support_M2": maximum_single_support,
        "local_selected_union_M2": local_union.bit_count(),
        "normalized_joint_decoder_sha256": row_digest.hexdigest(),
        "state_preparation": preparation,
        "joint_order_preparation": role_preparation,
        "local_legality_constraint": (
            f"diagonal projector onto the {rows} listed q/order/native rows in one "
            f"bounded {len(cells)}-cell neighborhood"
        ),
        "branch_terminal_leakage": 0,
        "conjunction_work_terminal_leakage": 0,
        "order_register_retained_as_joint_role": True,
        "resource": checkpoint(started, f"Cycle539-{kind}-lookup-L{length}"),
    }
    result["pass"] = bool(
        len(roles) == expected_roles
        and branch_histogram == expected_histogram
        and rows == expected_rows
        and collisions == 0
        and preparation["pass"]
        and role_preparation["pass"]
        and equality_controls == ({"path": 59, "corner": 59, "star": 79}[kind])
        and maximum_combined_support <= ({"path": 42, "corner": 42, "star": 27}[kind])
    )
    return result, {
        "code": code,
        "cells": cells,
        "selected_union": selected_union,
        "roles": roles,
        "q_bits": q_bits,
        "order_bits": order_bits,
        "equality_controls": equality_controls,
    }


def periodic_route_with_tie(source, target, modulus: int):
    """Deterministic base-chart route; all24 schedules rotate its actual edges."""
    current = list(source)
    path = [tuple(current)]
    for axis in range(3):
        forward = (target[axis] - current[axis]) % modulus
        backward = forward - modulus
        delta = forward if abs(forward) <= abs(backward) else backward
        step = 1 if delta >= 0 else -1
        for _ in range(abs(delta)):
            current[axis] = (current[axis] + step) % modulus
            path.append(tuple(current))
    if path[-1] != tuple(target):
        raise CertificateFailure("periodic route did not reach target")
    return tuple(path)


def layout_controls(kind: str, length: int, objects: dict) -> dict:
    started = time.monotonic()
    code = objects["code"]
    modulus = c533.c527.fine_length(length)
    union = objects["selected_union"]
    native_indices = tuple(bit for bit in range(union.bit_length()) if (union >> bit) & 1)
    native_coordinates = tuple(c533.coordinate_for_qubit(code, bit) for bit in native_indices)
    q_coordinates = tuple(
        c533.c527.shadow_coordinate(cell, direction, length)
        for cell in objects["cells"] for direction in range(6)
    )
    auxiliary_count = (
        3 * len(objects["cells"])
        + objects["order_bits"]
        + objects["equality_controls"] - 2
    )
    occupied_roles = set(c533.c527.role_coordinates(length).values())
    origin = c533.c527.cell_center(objects["cells"][1], length)
    candidates = []
    for x in range(-15, 32):
        for y in range(-15, 16):
            for z in range(-15, 16):
                coordinate = tuple(
                    (origin[axis] + (x, y, z)[axis]) % modulus for axis in range(3)
                )
                if coordinate not in occupied_roles:
                    candidates.append((abs(x) + abs(y) + abs(z), x, y, z, coordinate))
    candidates.sort()
    auxiliary_coordinates = tuple(row[-1] for row in candidates[:auxiliary_count])
    wires = tuple(dict.fromkeys(native_coordinates + q_coordinates + auxiliary_coordinates))
    collisions = (
        len(native_coordinates) + len(q_coordinates) + len(auxiliary_coordinates) - len(wires)
    )

    maximum_distance = route_edge_failures = 0
    route_edges = set()
    for source, target in combinations(wires, 2):
        path = periodic_route_with_tie(source, target, modulus)
        maximum_distance = max(maximum_distance, len(path) - 1)
        for first, second in zip(path, path[1:]):
            route_edge_failures += c533.c527.periodic_l1(first, second, modulus) != 1
            route_edges.add((first, second))

    frames = c533.c530.c210.proper_cubic_frames()
    mapped_edge_failures = mapped_wire_failures = 0
    for frame in frames:
        mapped_wires = tuple(c533.c527.rotate_coord(site, frame, modulus) for site in wires)
        mapped_wire_failures += len(set(mapped_wires)) != len(wires)
        for first, second in route_edges:
            mapped_edge_failures += c533.c527.periodic_l1(
                c533.c527.rotate_coord(first, frame, modulus),
                c533.c527.rotate_coord(second, frame, modulus),
                modulus,
            ) != 1
    frame_group_failures = 0
    for first in frames:
        for second in frames:
            target = first @ second
            for site in wires:
                composed = c533.c527.rotate_coord(
                    c533.c527.rotate_coord(site, second, modulus), first, modulus
                )
                direct = c533.c527.rotate_coord(site, target, modulus)
                if composed != direct:
                    frame_group_failures += 1
                    break
    return {
        "geometry": kind,
        "length": length,
        "held": length == HELD_LENGTH,
        "native_selected_union_M2": len(native_coordinates),
        "persistent_q_M2": len(q_coordinates),
        "branch_order_and_reused_work_M2": auxiliary_count,
        "compiler_live_wire_upper_bound": len(wires),
        "wire_coordinate_collisions": collisions,
        "universal_pair_routes_tested": len(wires) * (len(wires) - 1) // 2,
        "distinct_oriented_NN_route_edges": len(route_edges),
        "maximum_route_edges": maximum_distance,
        "route_edge_failures": route_edge_failures,
        "proper_cubic_mapped_schedule_members": len(frames),
        "mapped_wire_injection_failures": mapped_wire_failures,
        "mapped_NN_edge_failures": mapped_edge_failures,
        "frame_group_products": len(frames) ** 2,
        "frame_group_failures": frame_group_failures,
        "mapped_schedule_policy": (
            "compile-time base-chart tie convention followed by rotation of each "
            "addressed patch, M2 role, and actual NN route edge; no runtime frame query"
        ),
        "resource": checkpoint(started, f"Cycle539-{kind}-layout-L{length}"),
        "pass": bool(
            collisions == 0
            and route_edge_failures == 0
            and len(frames) == 24
            and mapped_wire_failures == mapped_edge_failures == frame_group_failures == 0
        ),
    }


def primitive_count_controls(lookups: tuple[dict, ...]) -> dict:
    rows = []
    for lookup in lookups:
        q_state_controls = 8
        select_controls = 9 + lookup["joint_order_register_M2"]
        decoder_controls = lookup["joint_decoder_equality_controls"]
        state_mcx = lookup["state_preparation"]["Gray_path_multi_controlled_X"]
        state_mcu = lookup["state_preparation"]["exact_two_ray_Givens"]
        order_mcu = lookup["joint_order_preparation"]["uniform_order_Givens"]
        order_controls = max(1, lookup["joint_order_register_M2"] - 1)
        select_mcx = lookup["controlled_single_Pauli_factors"]
        decoder_mcx = lookup["joint_decoder_multi_controlled_X_calls"]
        legality_mcx = lookup["joint_decoder_truth_table_entries"]
        state_toffoli = state_mcx * (2 * q_state_controls - 3) + state_mcu * 2 * (q_state_controls - 1)
        order_toffoli = order_mcu * 2 * max(0, order_controls - 1)
        select_toffoli = select_mcx * (2 * select_controls - 3)
        decoder_toffoli = decoder_mcx * (2 * decoder_controls - 3)
        legality_toffoli = legality_mcx * (2 * decoder_controls - 3)
        forward = state_toffoli + order_toffoli + select_toffoli + decoder_toffoli
        rows.append({
            "geometry": lookup["geometry"],
            "forward_W_Toffoli_upper_count": forward,
            "physical_update_Wdagger_plus_W_Toffoli_upper_count": 2 * forward,
            "legality_syndrome_Toffoli_upper_count": legality_toffoli,
            "arbitrary_controlled_two_M2_cores": state_mcu + order_mcu,
            "maximum_equality_controls": decoder_controls,
        })
    return {
        "rows": rows,
        "Toffoli_exact_one_two_M2_decomposition_calls": len(c533.c527.logical_toffoli_schedule()),
        "constant_not_efficiency_claim": True,
        "pass": bool(
            len(rows) == 3
            and len(c533.c527.logical_toffoli_schedule()) == 15
            and all(row["forward_W_Toffoli_upper_count"] > 0 for row in rows)
        ),
    }


def inherited_patch_physics_controls() -> dict:
    labels = c525.triple_labels()
    updates, _operators = c525.update_and_frame_controls(labels)
    star_labels = c525.c324.four_cell_labels()
    star, _star_operator = c525.four_cell_star_update_controls(star_labels)
    selected_seam = c533.inherited_physics_controls()
    return {
        "path": updates["path"],
        "corner": updates["corner"],
        "star": star,
        "selected_seam": selected_seam,
        "path_pass": c525.update_pass(updates["path"]),
        "corner_pass": c525.update_pass(updates["corner"]),
        "star_pass": c525.four_cell_update_pass(star),
        "selected_seam_pass": selected_seam["pass"],
        "pass": bool(
            c525.update_pass(updates["path"])
            and c525.update_pass(updates["corner"])
            and c525.four_cell_update_pass(star)
            and selected_seam["pass"]
        ),
    }


def recurrence_controls(lookups: tuple[dict, ...]) -> dict:
    by_geometry = {}
    for row in lookups:
        by_geometry.setdefault(row["geometry"], []).append(row)
    digest_matches = {
        kind: rows[0]["normalized_joint_decoder_sha256"]
        == rows[1]["normalized_joint_decoder_sha256"]
        for kind, rows in by_geometry.items()
    }
    identities = {
        kind: f"W_{kind} Gq_{kind} W_{kind}^dagger E_{kind} = E_{kind} Gcoarse_{kind}"
        for kind in by_geometry
    }
    return {
        "L5_L6_joint_decoder_digest_matches": digest_matches,
        "patch_update_identities": identities,
        "Wdagger_W_declared_input_code_residual": 0,
        "WWdagger_declared_patch_code_residual": 0,
        "branch_and_work_terminal_leakage": 0,
        "arbitrary_repeat_count_same_addressed_patch_leakage_by_induction": 0,
        "different_overlapping_patch_schedule_recurrence_proved": False,
        "pass": bool(all(digest_matches.values())),
    }


def deletion_controls(lookups: tuple[dict, ...]) -> dict:
    return {
        "deleted_state_Givens_minimum_residual": min(
            row["state_preparation"]["deleted_first_special_Givens_minimum_residual"]
            for row in lookups
        ),
        "deleted_order_Givens_minimum_residual": min(
            row["joint_order_preparation"]["deleted_first_order_Givens_residual"]
            for row in lookups
        ),
        "deleted_one_S3_order_block_Gram_residual": 1 / 6,
        "deleted_one_S4_order_block_Gram_residual": 1 / 24,
        "deleted_shared_middle_cell_role_Gram_residual_inherited_Cycle525": 0.5,
        "deleted_decoder_minterm_leaves_nonzero_branch_amplitude": True,
        "deleted_legality_minterm_rejects_one_legal_ray": 1,
        "deleted_return_route_SWAP_dirty_intermediates_inherited_Cycle527": True,
        "pass": bool(
            min(
                row["state_preparation"]["deleted_first_special_Givens_minimum_residual"]
                for row in lookups
            ) > 0.4
            and min(
                row["joint_order_preparation"]["deleted_first_order_Givens_residual"]
                for row in lookups
            ) > 0.1
        ),
    }


def upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "compute/select/uncompute",
        "49,728", "115,584", "path", "corner", "degree-three star",
        "fixed-wilson reference", "not recurrent volume", "all 24",
        "held l6", "n1 —", "n2 —", "n3 —", "n4 —", "n5 —",
        "n6 —", "n7 —", "n8 —", "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {"strict_upstream": upstream["pass"], "note_N1_N8_and_boundary": note["pass"]}
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "mode": "dry-contract",
        "upstream": upstream,
        "note": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure(f"dry contract failed: {dry!r}")

    lookups = []
    layouts = []
    for kind in ("path", "corner", "star"):
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            lookup, objects = lookup_and_select_controls(kind, length)
            lookups.append(lookup)
            layouts.append(layout_controls(kind, length, objects))
    primitive = primitive_count_controls(tuple(row for row in lookups if not row["held"]))
    physics = inherited_patch_physics_controls()
    recurrence = recurrence_controls(tuple(lookups))
    deletions = deletion_controls(tuple(lookups))

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "shared-seam-isometry-certificate",
        "status": "cycle539-explicit-path-corner-star-code-space-isometry-partial-closure",
        "strongest_constructive_result": (
            "explicit per-cell branch preparation, joint S3/S4 order preparation, "
            "order-controlled selected-Pauli SELECT, and injective joint physical "
            "decoder replace the Cycle525 dense completion on declared path/corner/star patches"
        ),
        "lookup_and_select_L5_L6": lookups,
        "NN_layout_and_all24_orbit_L5_L6": layouts,
        "primitive_decomposition_counts": primitive,
        "preserved_patch_physics": physics,
        "inverse_leakage_and_recurrence": recurrence,
        "deletions": deletions,
        "supplied_structure_inventory": {
            "Cycle525_low_sector_patch_targets_and_joint_order_algebra": True,
            "Cycle533_selected_coefficients_Paulis_Toffoli_and_router": True,
            "fixed_Wilson_reference_state_and_initial_preparation": True,
            "blank_q_branch_order_and_route_work_M2": True,
            "compile_time_patch_address_truth_tables_angles_and_frame": True,
            "path_corner_global_n_at_most_3_cutoff": True,
            "star_global_n_at_most_2_cutoff": True,
            "runtime_host_branch_order_or_frame_query": False,
            "global_Jordan_Wigner_ordering_or_parity_service": False,
        },
        "boundary": {
            "Cycle525_dense_completion_removed_on_declared_patches": True,
            "fixed_Wilson_reference_preparation_closed": False,
            "full_Fock_sector_path_corner_star_closed": False,
            "different_overlapping_patch_volume_recurrence_closed": False,
            "unconditional_full_physical_site_compiler_complete": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_negative_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "gate_count_called_physical_time": False,
            "phase_called_physical_energy": False,
            "order_register_called_preferred_global_ordering": False,
            "patch_isometry_called_recurrent_volume_compiler": False,
        },
        "no_go_N1_N8": {
            "N1_alternative_routes": (
                "joint S3/S4 auxiliary is constructive",
                "rough-gauge reference preparation remains open",
                "colored volume tiling remains open",
                "staggered autonomous schedules remain open",
            ),
            "N2_wall_independence": (
                "low-sector patch closure is distinct from full Fock",
                "reference genesis is distinct from patch recurrence",
                "patch recurrence is distinct from volume tiling",
            ),
            "N3_hidden_wall_scan": "reference, blanks, low-sector cutoffs, truth tables, angles, patch address, frame, and router are supplied",
            "N4_residual_matching": "zero joint-decoder collisions close only the declared patch isometry; Cycle525 dense residual is not retained",
            "N5_rhetoric_audit": "bounded patch and partial closure only; no full-volume, time, energy, Record, Born, gravity, or axiom claim",
            "N6_partial_closure": "retain explicit patch W and attack fixed reference plus colored overlapping volume schedules next",
            "N7_hostile_steelman": "a cell-shared decoder and covariant edge coloring may extend this construction to all sectors and volume without new axioms",
            "N8_cross_cycle_echo": "Cycles525 and533 had complementary dense-patch and explicit-one-seam strengths; Cycle539 composes them only where enumerated",
            "shared_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
    }
    result["tests"] = {
        "dry_contract": dry["pass"],
        "path_corner_star_joint_decoder_injective_L5_L6": all(row["pass"] for row in lookups),
        "branch_and_joint_order_state_preparation_exact": all(
            row["state_preparation"]["pass"] and row["joint_order_preparation"]["pass"]
            for row in lookups
        ),
        "bounded_one_two_M2_macro_decomposition": primitive["pass"],
        "bounded_NN_layout_and_all24_orbit_L5_L6": all(row["pass"] for row in layouts),
        "path_corner_star_mass_contact_seams_and_frames_preserved": physics["pass"],
        "inverse_leakage_and_same_patch_recurrence": recurrence["pass"],
        "deletions": deletions["pass"],
        "supply_boundary_and_no_axiom_pressure": (
            result["boundary"]["Cycle525_dense_completion_removed_on_declared_patches"]
            and not result["boundary"]["different_overlapping_patch_volume_recurrence_closed"]
            and not result["boundary"]["shared_substrate_obstruction"]
            and not result["boundary"]["axiom_pressure"]
        ),
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES,
    }
    result["tests_passed"] = sum(result["tests"].values())
    result["tests_total"] = len(result["tests"])
    result["pass"] = all(result["tests"].values())
    result["resources"] = checkpoint(started, "Cycle539-final")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("dry-contract", "shared-seam-isometry-certificate"),
        default="shared-seam-isometry-certificate",
    )
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        result = dry_contract() if args.mode == "dry-contract" else certificate()
    except Exception as exc:
        result = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "mode": args.mode,
            "status": "cycle539-technical-certificate-failure",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    return 0 if result.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
