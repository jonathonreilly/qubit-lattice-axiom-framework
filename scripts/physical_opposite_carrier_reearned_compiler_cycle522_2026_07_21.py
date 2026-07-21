#!/usr/bin/env python3
"""Cycle 522: zero-new-M2 opposite-carrier algebraic compiler.

The odd local M64 branch grammar retains precisely those complement carriers
whose opposite direction is occupied and renormalizes the retained set.  The
runner rechecks the local M64 shell, the adjacent-twelve-cell N<=2 Gram, the
seven-cell all-order shell, and one full two-cell all-Fock seam.

The physical coin used by the positive result is rebuilt as a bounded dense
on-shell lift.  The inherited Cycle-311 dense coin is tested separately and
fails to preserve the selected subspace.  Nothing here is primitive gate
synthesis or a recurrent multi-edge update.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import replace
from fractions import Fraction
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_adjacent_two_star_seam_tag_preservation_cycle519_2026_07_21 as c519
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle330_all_order_isometry_bridge_cycle515_2026_07_20 as c515


AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 4.0e-11
WALL_LIMIT_SECONDS = 600.0
RSS_GUARD_BYTES = 3_000_000_000

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OPPOSITE_CARRIER_REEARNED_COMPILER_CYCLE522_NOTE_2026-07-21.md"
)

PASS = 0
FAIL = 0


class ResourceWall(RuntimeError):
    """Technical execution ceiling, never a physical conclusion."""


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    swaps = int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))
    if elapsed >= WALL_LIMIT_SECONDS:
        raise ResourceWall(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swaps != 0:
        raise ResourceWall(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard wall alarm reached")


def check(label: str, condition: bool, detail: object) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def semantic_upstream_contract() -> dict:
    common_source = (ROOT / "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py").read_text()
    overlap_source = (ROOT / "scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py").read_text()
    gram_source = (ROOT / "scripts/physical_adjacent_two_star_compressed_gram_cycle518_2026_07_21.py").read_text()
    predicates = {
        "Cycle311_odd_complement_loop": "for carrier_direction in sorted(set(range(6)) - set(label))" in common_source,
        "Cycle311_odd_sqrt_normalization": "/ np.sqrt(6 - number)" in common_source,
        "Cycle315_two_gauge_terms": overlap_source.count("branch.amplitude / np.sqrt(2)") >= 2,
        "Cycle315_dense_ambient_formula": "E U E^dagger + I - E E^dagger" in overlap_source,
        "Cycle518_GF2_quotient": "def gf2_reduce" in gram_source,
        "Cycle519_native_doubletons": c519.EXPECTED_NATIVE_DOUBLETONS == 24,
        "Cycle519_native_Gram": c519.EXPECTED_NATIVE_GRAM_RESIDUAL == Fraction(1, 400),
    }
    return {"predicates": predicates, "pass": all(predicates.values())}


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing": (str(NOTE),), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "opposite-carrier",
        "10,768,384",
        "115,712",
        "25,088",
        "inherited coin",
        "rebuilt dense coin",
        "primitive",
        "recurrent multi-edge",
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
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def selected_carriers(number: int, label: tuple[int, ...]) -> tuple[int, ...]:
    if number not in range(7) or label not in c311.LABEL_INDEX[number]:
        raise ValueError("selected carriers require one ordered six-mode occupation label")
    if number % 2 == 0:
        return ()
    selected = tuple(
        direction
        for direction in range(6)
        if direction not in label and (direction ^ 1) in label
    )
    if not selected:
        raise ValueError("every odd six-mode label must expose an opposite carrier")
    return selected


def selected_common_branches(code, body, number: int, label, stream_slice: int):
    native = c311.common_branches(code, body, number, label, stream_slice)
    if number % 2 == 0:
        return native
    carriers = selected_carriers(number, label)
    kept = tuple(branch for branch in native if branch.carrier_direction in carriers)
    if len(kept) != len(carriers):
        raise ValueError("the native complement shell did not expose the selected carrier")
    scale = math.sqrt((6 - number) / len(kept))
    return tuple(replace(branch, amplitude=branch.amplitude * scale) for branch in kept)


def selected_gauge_terms(code, body, number: int, label):
    terms = []
    for branch in selected_common_branches(code, body, number, label, 0):
        terms.append(
            c315.GaugeTerm(
                number,
                c311.branch_representative(code, body, branch, 0),
                branch.amplitude / math.sqrt(2),
            )
        )
        target_slice = 0 if number == 0 else 1
        target = next(
            candidate
            for candidate in selected_common_branches(
                code, body, number, label, target_slice
            )
            if candidate.carrier_direction == branch.carrier_direction
        )
        terms.append(
            c315.GaugeTerm(
                number,
                c311.branch_representative(code, body, target, 1),
                branch.amplitude / math.sqrt(2),
            )
        )
    return tuple(terms)


def selected_local_encoder(code, body=(0, 0, 0)):
    columns = tuple(
        c311.CommonColumn(
            number,
            label,
            stream_slice,
            selected_common_branches(code, body, number, label, stream_slice),
        )
        for number, label, stream_slice in c311.SEAM_LABELS
    )
    encoder = c311.CommonEncoder(code, tuple(body), columns)
    basis = tuple(branch for column in columns for branch in column.branches)
    occurrence = {}
    encoding = np.zeros((len(basis), c311.SEAM_DIMENSION), dtype=complex)
    offset = 0
    for column_index, column in enumerate(columns):
        for branch in column.branches:
            occurrence[
                (
                    branch.number,
                    branch.label,
                    branch.stream_slice,
                    branch.carrier_direction,
                )
            ] = offset
            encoding[offset, column_index] = branch.amplitude
            offset += 1
    exchange = np.zeros((len(basis), len(basis)), dtype=complex)
    for source, branch in enumerate(basis):
        target_slice = 0 if branch.number == 0 else 1 - branch.stream_slice
        target = occurrence[
            (branch.number, branch.label, target_slice, branch.carrier_direction)
        ]
        exchange[target, source] = 1
    return encoder, basis, occurrence, encoding, exchange


def selected_frame_representation(encoder, basis, occurrence, frame):
    reducer = c311.c305.StabilizerReducer(encoder.code)
    vertex_map, edge_map = c311.c235.graph_frame_maps(encoder.code.graph, frame)
    toggles, repair_pairs, flips = c311.c269.repair_data(
        encoder.code.graph, vertex_map, edge_map
    )
    representation = np.zeros((len(basis), len(basis)), dtype=complex)
    failures = 0
    for source, branch in enumerate(basis):
        mapped_label = tuple(
            sorted(c311.direction_map(frame, direction) for direction in branch.label)
        )
        mapped_carrier = (
            None
            if branch.carrier_direction is None
            else c311.direction_map(frame, branch.carrier_direction)
        )
        target = occurrence.get(
            (branch.number, mapped_label, branch.stream_slice, mapped_carrier)
        )
        if target is None:
            failures += 1
            continue
        target_branch = basis[target]
        transformed = c311.local.transform_pauli(
            encoder.code,
            branch.face_pauli,
            edge_map,
            toggles,
            repair_pairs,
            flips,
        )
        phase = reducer.relative_phase(transformed, target_branch.face_pauli)
        failures += phase is None
        if phase is not None:
            representation[target, source] = c311.c308.phase_scalar(phase)
        failures += (
            c311.ports.permute_bits(branch.tags, vertex_map) != target_branch.tags
        )
    return representation, failures


def embedded_selected_encoding(native_encoder, native_encoding, occurrence):
    selected = np.zeros_like(native_encoding)
    for column_index, column in enumerate(native_encoder.columns):
        if column.number % 2 == 0:
            kept = column.branches
            scale = 1.0
        else:
            carriers = selected_carriers(column.number, column.label)
            kept = tuple(
                branch
                for branch in column.branches
                if branch.carrier_direction in carriers
            )
            scale = math.sqrt((6 - column.number) / len(kept))
        for branch in kept:
            row = occurrence[
                (
                    branch.number,
                    branch.label,
                    branch.stream_slice,
                    branch.carrier_direction,
                )
            ]
            selected[row, column_index] = native_encoding[row, column_index] * scale
    return selected


def local_shell_controls(length: int) -> tuple[dict, tuple]:
    code = c311.c269.build_code(length)
    encoder, basis, occurrence, encoding, exchange = selected_local_encoder(code)
    dimension = len(basis)
    identity = np.eye(c311.SEAM_DIMENSION)
    micro_identity = np.eye(dimension)
    selected_gram = float(np.linalg.norm(encoding.conj().T @ encoding - identity))
    constrained = np.vstack((encoding, exchange @ encoding)) / math.sqrt(2)
    zero = np.zeros_like(exchange)
    role_constraint = np.block([[zero, exchange], [exchange, zero]])
    raw = c311.raw_unflagged_encoding(
        encoder, c311.c305.StabilizerReducer(code)
    )

    logical_coin = c311.logical_coin(c311.c219.common_species(-0.3).coin)
    selected_projector = encoding @ encoding.conj().T
    rebuilt_coin = (
        encoding @ logical_coin @ encoding.conj().T
        + micro_identity
        - selected_projector
    )
    stream = exchange
    contact = c311.flagged_contact(encoder, basis, c311.COUPLING)
    logical_stream = c311.logical_stream()
    logical_contact = c311.logical_contact(c311.COUPLING)
    update = contact @ stream @ rebuilt_coin
    logical_update = logical_contact @ logical_stream @ logical_coin

    native_encoder = c311.common_encoder(code)
    native_basis, native_encoding, native_occurrence = c311.flagged_basis_and_encoding(
        native_encoder
    )
    native_exchange = c311.exchange_matrix(native_encoder, native_occurrence)
    _native_gauge_coin, inherited_coin = c311.physical_coin(
        native_encoding, logical_coin, native_exchange
    )
    selected_in_native = embedded_selected_encoding(
        native_encoder, native_encoding, native_occurrence
    )
    selected_native_projector = selected_in_native @ selected_in_native.conj().T
    inherited_intertwiner = float(
        np.linalg.norm(inherited_coin @ selected_in_native - selected_in_native @ logical_coin)
    )
    inherited_leakage = float(
        np.linalg.norm(
            (np.eye(len(native_basis)) - selected_native_projector)
            @ inherited_coin
            @ selected_in_native,
            2,
        )
    )
    rebuilt_native_ambient = (
        selected_in_native @ logical_coin @ selected_in_native.conj().T
        + np.eye(len(native_basis))
        - selected_native_projector
    )

    representatives = [
        c311.branch_representative(code, encoder.body, branch, 0)
        for branch in basis
    ]
    active = number_changing = constraint_failures = sector_failures = 0
    maximum_transition_support = 0
    for target, source in np.argwhere(abs(rebuilt_coin) > c311.TOLERANCE):
        if target == source:
            continue
        active += 1
        number_changing += basis[int(target)].number != basis[int(source)].number
        transition = representatives[int(target)] @ c311.local.pauli_dagger(
            representatives[int(source)]
        )
        maximum_transition_support = max(
            maximum_transition_support, (transition.x | transition.z).bit_count()
        )
        constraint_failures += sum(
            not transition.commutes(c311.c305.constraint_pauli(code, vertex))
            for vertex in range(len(code.graph.vertices))
        )
        sector_failures += sum(
            not transition.commutes(row)
            for row in code.local_checks + code.wilsons
        )

    contact_failures = 0
    for column in encoder.columns:
        expected = (
            np.exp(1j * math.comb(column.number, 2) * c311.COUPLING)
            if column.stream_slice == 0
            else 1
        )
        contact_failures += sum(
            abs(c311.contact_phase(code, branch, c311.COUPLING) - expected)
            > c311.TOLERANCE
            for branch in column.branches
        )

    deletion_rows = {}
    for number in (1, 3):
        residuals = []
        for column_index, column in enumerate(encoder.columns):
            if column.number != number or column.stream_slice != 0:
                continue
            rows = np.flatnonzero(abs(encoding[:, column_index]) > 1e-14)
            deleted = encoding.copy()
            deleted[rows[0], column_index] = 0
            residuals.append(
                float(np.linalg.norm(deleted.conj().T @ deleted - identity, 2))
            )
        deletion_rows[number] = {
            "minimum": min(residuals),
            "maximum": max(residuals),
            "histogram": dict(Counter(round(value, 12) for value in residuals)),
        }

    branch_histogram = Counter(
        (branch.number, branch.stream_slice) for branch in basis
    )
    result = {
        "L": length,
        "held": length == HELD_LENGTH,
        "flagged_microsectors": dimension,
        "branch_histogram": {
            f"n{number}_s{stream_slice}": count
            for (number, stream_slice), count in sorted(branch_histogram.items())
        },
        "selected_Gram_residual": selected_gram,
        "selected_rank": int(np.linalg.matrix_rank(encoding, tol=1e-10)),
        "raw_rows_without_cell_role": raw.shape[0],
        "raw_rank_without_cell_role": int(np.linalg.matrix_rank(raw, tol=1e-10)),
        "raw_Gram_operator_residual": float(
            np.linalg.norm(raw.conj().T @ raw - identity, 2)
        ),
        "role_constrained_rank": int(np.linalg.matrix_rank(constrained, tol=1e-10)),
        "role_constraint_eigen_residual": float(
            np.linalg.norm(role_constraint @ constrained - constrained)
        ),
        "rebuilt_coin_intertwiner_residual": float(
            np.linalg.norm(rebuilt_coin @ encoding - encoding @ logical_coin)
        ),
        "rebuilt_coin_unitarity_residual": float(
            np.linalg.norm(rebuilt_coin.conj().T @ rebuilt_coin - micro_identity)
        ),
        "stream_intertwiner_residual": float(
            np.linalg.norm(stream @ encoding - encoding @ logical_stream)
        ),
        "contact_intertwiner_residual": float(
            np.linalg.norm(contact @ encoding - encoding @ logical_contact)
        ),
        "composed_intertwiner_residual": float(
            np.linalg.norm(update @ encoding - encoding @ logical_update)
        ),
        "composed_unitarity_residual": float(
            np.linalg.norm(update.conj().T @ update - micro_identity)
        ),
        "inherited_native_coin_intertwiner_residual": inherited_intertwiner,
        "inherited_native_coin_leakage_operator_norm": inherited_leakage,
        "rebuilt_vs_inherited_coin_operator_norm": float(
            np.linalg.norm(rebuilt_native_ambient - inherited_coin, 2)
        ),
        "rebuilt_active_offdiagonal_microterms": active,
        "number_changing_microterms": number_changing,
        "port_constraint_commutator_failures": constraint_failures,
        "fixed_sector_commutator_failures": sector_failures,
        "maximum_rebuilt_coin_transition_support_M2": maximum_transition_support,
        "physical_contact_failures": contact_failures,
        "carrier_deletions": deletion_rows,
        "unrescaled_n1_column_Gram_deficit": Fraction(4, 5),
    }
    result["pass"] = (
        dimension == 159
        and result["selected_rank"] == 127
        and selected_gram < TOLERANCE
        and result["raw_rank_without_cell_role"] == 121
        and abs(result["raw_Gram_operator_residual"] - 1) < TOLERANCE
        and result["role_constrained_rank"] == 127
        and result["role_constraint_eigen_residual"] < TOLERANCE
        and max(
            result["rebuilt_coin_intertwiner_residual"],
            result["rebuilt_coin_unitarity_residual"],
            result["stream_intertwiner_residual"],
            result["contact_intertwiner_residual"],
            result["composed_intertwiner_residual"],
            result["composed_unitarity_residual"],
        )
        < TOLERANCE
        and inherited_intertwiner > 5
        and inherited_leakage > 0.9
        and active == 1608
        and number_changing == constraint_failures == sector_failures == 0
        and maximum_transition_support <= 27
        and contact_failures == 0
        and deletion_rows[1]["minimum"] > 0.99
        and deletion_rows[3]["minimum"] > 0.32
    )
    return result, (
        code,
        encoder,
        basis,
        occurrence,
        encoding,
        exchange,
        rebuilt_coin,
        contact,
        update,
    )


def frame_controls(local_objects: tuple) -> dict:
    (
        _code,
        encoder,
        basis,
        occurrence,
        encoding,
        exchange,
        rebuilt_coin,
        contact,
        update,
    ) = local_objects
    frames = c311.c235.proper_cubic_frames()
    maximum = Counter()
    branch_failures = 0
    for frame in frames:
        representation, failures = selected_frame_representation(
            encoder, basis, occurrence, frame
        )
        mapping, phases, mapping_failures = c311.signed_mapping(representation)
        logical = c311.logical_frame_representation(frame)
        branch_failures += failures + mapping_failures
        maximum["isometry"] = max(
            maximum["isometry"],
            float(
                np.linalg.norm(
                    c311.apply_signed_mapping(mapping, phases, encoding)
                    - encoding @ logical
                )
            ),
        )
        maximum["stream"] = max(
            maximum["stream"],
            c311.conjugation_residual(exchange, mapping, phases),
        )
        maximum["coin"] = max(
            maximum["coin"],
            c311.conjugation_residual(rebuilt_coin, mapping, phases),
        )
        maximum["contact"] = max(
            maximum["contact"],
            c311.conjugation_residual(contact, mapping, phases),
        )
        maximum["composition"] = max(
            maximum["composition"],
            c311.conjugation_residual(update, mapping, phases),
        )

    lookup = {tuple(frame.flatten()): index for index, frame in enumerate(frames)}
    logical_representations = [
        c311.logical_frame_representation(frame) for frame in frames
    ]
    group_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            target = lookup[tuple((left @ right).flatten())]
            group_failures += (
                np.linalg.norm(
                    logical_representations[left_index]
                    @ logical_representations[right_index]
                    - logical_representations[target]
                )
                > c311.TOLERANCE
            )

    selector_tests = selector_failures = normalization_failures = 0
    for frame in frames:
        for number in (1, 3, 5):
            for label in c311.LABELS[number]:
                source = selected_carriers(number, label)
                target_label = tuple(
                    sorted(c311.direction_map(frame, direction) for direction in label)
                )
                mapped = tuple(
                    sorted(c311.direction_map(frame, direction) for direction in source)
                )
                target = tuple(sorted(selected_carriers(number, target_label)))
                selector_tests += 1
                selector_failures += mapped != target
                normalization_failures += len(source) != len(target)
    return {
        "L": encoder.code.length,
        "proper_frames": len(frames),
        "physical_branch_failures": branch_failures,
        "maximum_covariance_residuals": dict(maximum),
        "frame_group_products": len(frames) ** 2,
        "frame_group_failures": int(group_failures),
        "odd_label_selector_tests": selector_tests,
        "odd_label_selector_failures": selector_failures,
        "normalization_orbit_failures": normalization_failures,
        "pass": (
            len(frames) == 24
            and branch_failures == 0
            and max(maximum.values(), default=0) < TOLERANCE
            and group_failures == 0
            and selector_tests == 768
            and selector_failures == normalization_failures == 0
        ),
    }


def adjacent_twelve_census(length: int) -> dict:
    _code, _cells, cache = c519.build_cache(length)
    vacuum = tuple(cache[cell, 0][0]["auxiliary"] for cell in range(12))
    toggles = tuple(
        cache[cell, 0][0]["auxiliary"] ^ cache[cell, 0][1]["auxiliary"]
        for cell in range(12)
    )
    quotient_basis = c519.c518.gf2_basis(toggles)
    seen = Counter()
    sectors = Counter()

    def add(choices, sector: str) -> None:
        delta = 0
        for cell, number, term_index in choices:
            delta ^= cache[cell, number][term_index]["auxiliary"] ^ vacuum[cell]
        quotient, _coefficient = c519.c518.gf2_reduce(delta, quotient_basis)
        seen[quotient] += 1
        sectors[sector] += 1

    add((), "n0")
    selected_one = {}
    for cell in range(12):
        selected_one[cell] = tuple(
            (index, term)
            for index, term in enumerate(cache[cell, 1])
            if term["carrier"] == (term["label"][0] ^ 1)
        )
        for term_index, _term in selected_one[cell]:
            add(((cell, 1, term_index),), "n1")
        for term_index, _term in enumerate(cache[cell, 2]):
            add(((cell, 2, term_index),), "n2_same_cell")
    for first, second in combinations(range(12), 2):
        for first_index, _first in selected_one[first]:
            for second_index, _second in selected_one[second]:
                add(
                    (
                        (first, 1, first_index),
                        (second, 1, second_index),
                    ),
                    "n2_split_cells",
                )

    fiber_histogram = Counter(seen.values())
    expanded_sectors = {
        "n0": sectors["n0"] * 2**12,
        "n1": sectors["n1"] * 2**11,
        "n2_same_cell": sectors["n2_same_cell"] * 2**11,
        "n2_split_cells": sectors["n2_split_cells"] * 2**10,
    }
    result = {
        "L": length,
        "held": length == HELD_LENGTH,
        "seed_sectors": dict(sectors),
        "seeds": sum(sectors.values()),
        "quotient_fibers": len(seen),
        "fiber_histogram": dict(fiber_histogram),
        "maximum_fiber": max(seen.values()),
        "expanded_sector_rows": expanded_sectors,
        "expanded_rows": sum(expanded_sectors.values()),
        "logical_columns": c519.EXPECTED_LOGICAL_DIMENSION,
        "branches_per_column": 4096,
        "exact_squared_branch_weight": (1, 4096),
        "exact_column_norm": (1, 1),
        "new_tag_M2": 0,
        "native_comparator_doubletons": c519.EXPECTED_NATIVE_DOUBLETONS,
        "native_comparator_Gram_residual": (1, 400),
    }
    result["pass"] = (
        sectors
        == Counter(
            {
                "n0": 1,
                "n1": 144,
                "n2_same_cell": 360,
                "n2_split_cells": 9504,
            }
        )
        and result["seeds"] == result["quotient_fibers"] == 10009
        and fiber_histogram == Counter({1: 10009})
        and result["expanded_rows"] == 10_768_384
        and result["expanded_rows"]
        == result["logical_columns"] * result["branches_per_column"]
    )
    return result


def seven_star_controls(length: int) -> dict:
    c330 = c515.c330
    code = c330.c269.build_code(length)
    reducer = c330.c315.RayReducer(code)
    cache = {}
    total_branches = row_reuses = 0
    branch_histogram = Counter()
    mask_histogram = Counter()
    maximum_support = 0
    maximum_norm_residual = 0.0
    labels = c330.seven_cell_labels()
    for label in labels:
        terms_by_cell = []
        for cell, (number, local_label) in zip(c330.CELLS, c330.label_specs(label)):
            key = (cell, number, local_label)
            if key not in cache:
                cache[key] = selected_gauge_terms(code, cell, number, local_label)
            terms_by_cell.append(cache[key])
        column_branches = 0
        norm = 0.0
        for term_tuple in product(*terms_by_cell):
            representatives = tuple(term.representative for term in term_tuple)
            physical = c330.multiply_order(representatives, tuple(range(7)))
            before = len(reducer.row_by_aux)
            reducer.reduce(physical)
            row_reuses += len(reducer.row_by_aux) != before + 1
            coefficient = math.prod(term.amplitude for term in term_tuple)
            norm += abs(coefficient) ** 2
            total_branches += 1
            column_branches += 1
            mask_histogram[c330.branch_anticommutation_mask(representatives)] += 1
            maximum_support = max(
                maximum_support, (physical.x | physical.z).bit_count()
            )
        branch_histogram[column_branches] += 1
        maximum_norm_residual = max(maximum_norm_residual, abs(norm - 1))
    result = {
        "L": length,
        "held": length == HELD_LENGTH,
        "logical_columns": len(labels),
        "structural_branches": total_branches,
        "physical_rows": len(reducer.row_by_aux),
        "row_reuses": int(row_reuses),
        "branches_per_column_histogram": dict(branch_histogram),
        "maximum_column_norm_residual": maximum_norm_residual,
        "anticommutation_mask_support": tuple(sorted(mask_histogram)),
        "maximum_base_branch_support_M2": maximum_support,
        "maximum_branch_support_with_thirteen_order_M2": maximum_support + 13,
        "all_cell_factor_orders": math.factorial(7),
        "all_order_isometry_reason": "each order multiplies every unique physical row by one exact anticommutation character",
    }
    result["pass"] = (
        len(labels) == 904
        and total_branches == len(reducer.row_by_aux) == 115_712
        and row_reuses == 0
        and branch_histogram == Counter({128: 904})
        and maximum_norm_residual < TOLERANCE
        and tuple(sorted(mask_histogram)) == (0, 1, 2, 4, 8, 16, 32)
        and maximum_support <= 33
    )
    return result


def two_cell_support(code) -> dict:
    local_terms = {}
    union = 0
    maximum_single = maximum_joint = 0
    constraint_failures = sector_failures = 0
    for body in (c315.LEFT, c315.RIGHT):
        for number, label in c311.FOCK_LABELS:
            terms = selected_gauge_terms(code, body, number, label)
            local_terms[(body, number, label)] = terms
            for term in terms:
                word = term.representative.x | term.representative.z
                union |= word
                maximum_single = max(maximum_single, word.bit_count())
                constraint_failures += sum(
                    not term.representative.commutes(
                        c311.c305.constraint_pauli(code, vertex)
                    )
                    for vertex in range(len(code.graph.vertices))
                )
                sector_failures += sum(
                    not term.representative.commutes(row)
                    for row in code.local_checks + code.wilsons
                )
    for left_number, left_label, right_number, right_label in c315.joint_labels():
        for left, right in product(
            local_terms[(c315.LEFT, left_number, left_label)],
            local_terms[(c315.RIGHT, right_number, right_label)],
        ):
            combined = left.representative @ right.representative
            maximum_joint = max(
                maximum_joint, (combined.x | combined.z).bit_count()
            )
    vertices = len(code.graph.vertices)
    cells = code.length**3
    face_mask = (1 << code.qubits) - 1
    port_mask = ((1 << vertices) - 1) << code.qubits
    flag_mask = ((1 << cells) - 1) << (code.qubits + vertices)
    r_mask = ((1 << cells) - 1) << (code.qubits + vertices + cells)
    return {
        "face_M2_union": (union & face_mask).bit_count(),
        "port_M2_union": (union & port_mask).bit_count(),
        "cell_flag_M2_union": (union & flag_mask).bit_count(),
        "cell_r_M2_union": (union & r_mask).bit_count(),
        "edge_flag_and_r_M2": 2,
        "total_patch_union_M2": union.bit_count() + 2,
        "maximum_single_cell_branch_M2": maximum_single,
        "maximum_joint_branch_with_edge_roles_M2": maximum_joint + 2,
        "port_constraint_commutator_failures": constraint_failures,
        "fixed_sector_commutator_failures": sector_failures,
        "installed_M2_per_cell_with_edge_roles": 29,
    }


def two_cell_controls(length: int, execute_update: bool) -> tuple[dict, dict | None]:
    labels = c315.joint_labels()
    code = c315.c269.build_code(length)
    reducer = c315.RayReducer(code)
    forward = c315.joint_encoding(
        code,
        labels,
        reducer,
        False,
        term_builder=selected_gauge_terms,
    )
    if forward.shape[0] < len(reducer.row_by_aux):
        forward.resize((len(reducer.row_by_aux), len(labels)))
    identity = sparse.eye(len(labels), format="csc")
    gram = (forward.conj().T @ forward).tocsc()
    result = {
        "L": length,
        "held": length == HELD_LENGTH,
        "logical_columns": len(labels),
        "physical_rays": forward.shape[0],
        "matrix_nonzeros": forward.nnz,
        "Gram_operator_residual": c315.largest_singular(gram - identity),
        "Gram_raw_maximum": c315.raw_maximum_abs(gram - identity),
        "minimum_Gram_eigenvalue": float(
            eigsh(
                gram,
                k=1,
                which="SA",
                return_eigenvectors=False,
                tol=2e-10,
            )[0]
        ),
    }
    update_result = None
    if execute_update:
        reverse = c315.joint_encoding(
            code,
            labels,
            reducer,
            True,
            term_builder=selected_gauge_terms,
        )
        forward, reverse = c315.align_rows(
            forward, reverse, len(reducer.row_by_aux)
        )
        logical_coin, logical_stream, logical_contact, logical_update, logical = (
            c315.logical_update_controls(labels)
        )
        edge = c315.edge_role_gauge_controls(forward, reverse, logical_update)
        ambient = c315.ambient_completion_controls(forward, logical_update)
        covariance = c315.covariance_translation_controls(
            labels, logical_coin, logical_contact, logical_update
        )

        deleted_stream = logical_stream.tolil(copy=True)
        deleted_stream[:, 0] = 0
        deleted_stream = deleted_stream.tocsc()
        deleted_stream_residual = c315.largest_singular(
            deleted_stream.conj().T @ deleted_stream - identity
        )
        coin_coo = logical_coin.tocoo()
        offdiagonal = np.flatnonzero(coin_coo.row != coin_coo.col)
        selected = int(offdiagonal[np.argmax(abs(coin_coo.data[offdiagonal]))])
        mutated = coin_coo.data.copy()
        deleted_coin_coefficient = complex(mutated[selected])
        mutated[selected] = 0
        deleted_coin = sparse.coo_matrix(
            (mutated, (coin_coo.row, coin_coo.col)), shape=coin_coo.shape
        ).tocsc()
        deleted_coin.eliminate_zeros()
        deleted_coin_residual = c315.largest_singular(
            deleted_coin.conj().T @ deleted_coin - identity
        )
        deleted_contact_residual = c315.largest_singular(
            logical_contact - identity
        )
        support = two_cell_support(code)
        update_result = {
            "logical_update": logical,
            "edge_role_gauge": edge,
            "ambient_completion": ambient,
            "covariance": covariance,
            "support": support,
            "deletions": {
                "deleted_FSWAP_column_unitarity_residual": deleted_stream_residual,
                "deleted_coin_coefficient": (
                    deleted_coin_coefficient.real,
                    deleted_coin_coefficient.imag,
                ),
                "deleted_coin_unitarity_residual": deleted_coin_residual,
                "deleted_contact_residual": deleted_contact_residual,
            },
        }
    result["pass"] = (
        result["logical_columns"] == 4096
        and result["physical_rays"] == 25_088
        and result["matrix_nonzeros"] == 25_600
        and result["Gram_operator_residual"] == 0
        and result["Gram_raw_maximum"] < TOLERANCE
        and abs(result["minimum_Gram_eigenvalue"] - 1) < TOLERANCE
    )
    return result, update_result


def update_pass(update: dict) -> bool:
    logical = update["logical_update"]
    edge = update["edge_role_gauge"]
    ambient = update["ambient_completion"]
    covariance = update["covariance"]
    support = update["support"]
    deletions = update["deletions"]
    return (
        max(
            logical["coin_unitarity"],
            logical["FSWAP_unitarity"],
            logical["contact_unitarity"],
            logical["composed_unitarity"],
        )
        == 0
        and abs(logical["two_cell_rest_mass"] - logical["Cycle219_mass_fixture"])
        < TOLERANCE
        and logical["two_cell_uniform_one_particle_residual"] < TOLERANCE
        and max(
            edge["flagged_physical_Gram_residual"],
            edge["constrained_Gram_residual"],
            edge["constraint_involution_residual"],
            edge["constraint_eigen_residual"],
            edge["gauge_lift_constraint_commutator"],
            edge["gauge_lift_intertwining_residual"],
            edge["seam_update_unitarity"],
        )
        == 0
        and edge["unordered_without_edge_r_Gram_residual"] > 0.99
        and ambient["intertwining_residual"] == 0
        and ambient["maximum_randomized_ambient_inverse_residual"] < TOLERANCE
        and covariance["proper_cubic_frames"] == 24
        and covariance["maximum_update_covariance_residual"] == 0
        and covariance["edge_role_group_law_failures"] == 0
        and support["total_patch_union_M2"] == 83
        and support["maximum_joint_branch_with_edge_roles_M2"] == 65
        and support["port_constraint_commutator_failures"] == 0
        and support["fixed_sector_commutator_failures"] == 0
        and deletions["deleted_FSWAP_column_unitarity_residual"] > 0.99
        and deletions["deleted_coin_unitarity_residual"] > 0.5
        and deletions["deleted_contact_residual"] > 1
    )


def domain_controls() -> dict:
    failures = 0
    for bad in (
        lambda: selected_carriers(7, ()),
        lambda: selected_carriers(1, (0, 0)),
        lambda: selected_carriers(2, (0,)),
    ):
        try:
            bad()
        except ValueError:
            continue
        failures += 1
    try:
        c519.c517.rotated_patch(c519.c517.IDENTITY, 4)
    except ValueError:
        pass
    else:
        failures += 1
    reflection = np.diag((-1, 1, 1))
    determinant_minus_one_rejected = round(np.linalg.det(reflection)) == -1
    return {
        "malformed_selector_cases": 3,
        "malformed_selector_failures": failures,
        "L4_adjacent_patch_rejected": True,
        "determinant_minus_one_not_in_proper_frame_domain": determinant_minus_one_rejected,
        "lawful_adjacent_domain": "L=5 and held L=6; twelve distinct cells; global N<=2",
        "lawful_local_domain": "complete local n=0,...,6 M64",
        "lawful_two_cell_domain": "complete 4096-dimensional two-cell Fock space",
        "pass": failures == 0 and determinant_minus_one_rejected,
    }


def dry_contract() -> dict:
    semantic = semantic_upstream_contract()
    note = note_contract()
    counts = {
        "selected_carrier_counts": {
            number: sorted(
                Counter(
                    len(selected_carriers(number, label))
                    for label in c311.LABELS[number]
                ).items()
            )
            for number in (1, 3, 5)
        },
        "expected_local_microsectors": 159,
        "expected_adjacent_seeds": 10_009,
        "expected_adjacent_rows": 10_768_384,
        "expected_seven_star_rows": 115_712,
        "expected_two_cell_rays": 25_088,
    }
    counts_pass = counts["selected_carrier_counts"] == {
        1: [(1, 6)],
        3: [(1, 12), (3, 8)],
        5: [(1, 6)],
    }
    return {
        "schema": "cycle522-opposite-carrier-dry-contract-v1",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "semantic_upstream": semantic,
        "note_contract": note,
        "counts": counts,
        "pass": semantic["pass"] and note["pass"] and counts_pass,
    }


def certificate() -> dict:
    started = time.monotonic()
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    checkpoints = []
    try:
        dry = dry_contract()
        local_train, train_objects = local_shell_controls(TRAIN_LENGTH)
        local_held, held_objects = local_shell_controls(HELD_LENGTH)
        checkpoints.append(checkpoint(started, "local-shells"))
        frames_train = frame_controls(train_objects)
        frames_held = frame_controls(held_objects)
        checkpoints.append(checkpoint(started, "all-frames"))
        adjacent_train = adjacent_twelve_census(TRAIN_LENGTH)
        adjacent_held = adjacent_twelve_census(HELD_LENGTH)
        checkpoints.append(checkpoint(started, "adjacent-gram"))
        seven_train = seven_star_controls(TRAIN_LENGTH)
        seven_held = seven_star_controls(HELD_LENGTH)
        checkpoints.append(checkpoint(started, "seven-star"))
        two_train, update = two_cell_controls(TRAIN_LENGTH, True)
        checkpoints.append(checkpoint(started, "two-cell-update"))
        two_held, _held_update = two_cell_controls(HELD_LENGTH, False)
        checkpoints.append(checkpoint(started, "held-two-cell"))
        domain = domain_controls()
        update_ok = update is not None and update_pass(update)

        tests = {
            "dry_contract": dry["pass"],
            "complete_local_M64_L5": local_train["pass"],
            "complete_local_M64_held_L6": local_held["pass"],
            "all24_physical_frames_L5": frames_train["pass"],
            "all24_physical_frames_held_L6": frames_held["pass"],
            "adjacent12_exact_Gram_L5": adjacent_train["pass"],
            "adjacent12_exact_Gram_held_L6": adjacent_held["pass"],
            "seven_cell_all_order_shell_L5": seven_train["pass"],
            "seven_cell_all_order_shell_held_L6": seven_held["pass"],
            "two_cell_full_Fock_Gram_L5": two_train["pass"],
            "two_cell_full_Fock_Gram_held_L6": two_held["pass"],
            "two_cell_dense_free_contact_update_and_mass": update_ok,
            "lawful_domain_and_deletions": domain["pass"],
        }
        for label, condition in tests.items():
            check(label.replace("_", " "), bool(condition), condition)
        final_resource = checkpoint(started, "complete")
        result = {
            "schema": "cycle522-opposite-carrier-reearned-compiler-v1",
            "status": "PASS" if all(tests.values()) else "FAIL",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "claim_boundary": "zero-new-M2 algebraic compiler with rebuilt supplied dense coefficients; not primitive synthesis or recurrent multi-edge dynamics",
            "tests": tests,
            "dry_contract": dry,
            "local_shells": (local_train, local_held),
            "frame_controls": (frames_train, frames_held),
            "adjacent_twelve": (adjacent_train, adjacent_held),
            "seven_star": (seven_train, seven_held),
            "two_cell_Gram": (two_train, two_held),
            "two_cell_update": update,
            "domain_controls": domain,
            "resources": checkpoints + [final_resource],
            "supplied": {
                "fixed_reference_and_preparation": True,
                "opposite_carrier_selector_and_normalization": True,
                "rebuilt_dense_coin_coefficients": True,
                "dense_off_code_identity_completion": True,
                "cell_and_edge_role_constraints_and_preparation": True,
                "primitive_gate_genesis_and_schedule": True,
                "recurrent_multi_edge_application": True,
                "beta_and_contact_coupling": True,
            },
            "not_claimed": (
                "primitive M2 synthesis",
                "simultaneous recurrent multi-edge constraint closure",
                "physical time or rate",
                "Record formation",
                "Born probability",
                "source, stress, gravity, or backreaction",
                "continuum or thermodynamic limit",
            ),
        }
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
        print(f"SUMMARY PASS={PASS} FAIL={FAIL}")
        return result
    finally:
        signal.alarm(0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode", choices=("dry-contract", "certificate"), default="certificate"
    )
    args = parser.parse_args()
    if args.mode == "dry-contract":
        result = dry_contract()
        print(json.dumps(result, indent=2, sort_keys=True, default=str))
        return 0 if result["pass"] else 1
    result = certificate()
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
