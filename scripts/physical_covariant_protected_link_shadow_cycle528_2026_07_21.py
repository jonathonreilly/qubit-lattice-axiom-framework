#!/usr/bin/env python3
"""Cycle 528: covariant protected-link shadow attack on the Cycle-523 B wall.

Build a concrete locally prepared Bell-link comparator to the Cycle-236
one-link Majorana sector, keep it live through the B layer, and compose it
with Cycle 523's exact 100-call/cell onsite schedule.  Exact L5 and held-L6
one-/two-particle censuses then distinguish the one-link success from the
simultaneous-matching failure.  A GF(2) solve tests the larger class of
translation-equivariant products of arbitrary endpoint-cell diagonal link
responses.  A separate Cycle-260 prefix-field construction distinguishes an
exact bounded-support runtime phase from size-growing preparation/recode.

The negative results are route-class-specific.  Correlated link-sector
preparation and non-diagonal/stateful local gauge transitions remain open.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from hashlib import sha256
from itertools import combinations, product
import io
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17 as c231
import FARRELLY_SHORT_AUXILIARY_MAJORANA_CAR_COMPILER_CYCLE236_2026_07_17 as c236
import genuine_staggered_parity_shuttle_cycle260_2026_07_17 as c260
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523


c210 = c219.c210
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 5e-12
PERTURBATION = 1e-4
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "protected-link-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_COVARIANT_PROTECTED_LINK_SHADOW_CYCLE528_NOTE_2026-07-21.md"
)
CYCLE219_RUNNER = ROOT / "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py"
CYCLE230_RUNNER = ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py"
CYCLE231_RUNNER = ROOT / "scripts/ROUTE1_DIRECT_CAR_COMPILER_CYCLE231_2026_07_17.py"
CYCLE236_RUNNER = ROOT / "scripts/FARRELLY_SHORT_AUXILIARY_MAJORANA_CAR_COMPILER_CYCLE236_2026_07_17.py"
CYCLE260_RUNNER = ROOT / "scripts/genuine_staggered_parity_shuttle_cycle260_2026_07_17.py"
CYCLE523_RUNNER = ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py"
STRICT_FILE_HASHES = {
    CYCLE219_RUNNER: "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    CYCLE230_RUNNER: "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    CYCLE231_RUNNER: "5adb6dc52f6352a5367a2b56da94854e511f9dd174688029f1841e5004a91c32",
    CYCLE236_RUNNER: "e491464d1c096ddbe624ef90d23f97c155fc16ac15c974199aad6f0e46364b2b",
    CYCLE260_RUNNER: "eb872bf2efd5f8c5a9a67c44cbe3cd6052f94ebe44dc8e7efc4bcd10928196c3",
    CYCLE523_RUNNER: "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
}


class CertificateFailure(RuntimeError):
    """A bounded predicate failed; never promoted automatically to a no-go."""


class ResourceWall(RuntimeError):
    """A technical resource wall; never a physical conclusion."""


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
    if swap_count() != 0:
        raise ResourceWall(f"nonzero swap count at {label}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swap_count(),
    }


def alarm_handler(_signum, _frame) -> None:
    raise ResourceWall("hard 1200-second wall alarm reached")


def kron4(*operators: np.ndarray) -> np.ndarray:
    result = np.asarray(((1,),), dtype=complex)
    for operator in operators:
        result = np.kron(result, operator)
    return result


def covariant_bell_link_controls() -> dict:
    """Build a swap-symmetric local comparator to Cycle236's one-link code."""

    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    phase = np.diag((1, 1j)).astype(complex)

    # Extended mode order [matter-left a, auxiliary-left c,
    # matter-right b, auxiliary-right d].
    a, c, b, d = (c236.annihilation(index, 4) for index in range(4))
    m_oriented = 1j * (c + c.conj().T) @ (d + d.conj().T)
    q_oriented = (
        a.conj().T @ a
        + b.conj().T @ b
        - a.conj().T @ m_oriented @ b
        - b.conj().T @ m_oriented @ a
    )
    u_oriented = expm(1j * np.pi * q_oriented / 2)

    a2, b2 = (c236.annihilation(index, 2) for index in range(2))
    q_coarse = (
        a2.conj().T @ a2
        + b2.conj().T @ b2
        - a2.conj().T @ b2
        - b2.conj().T @ a2
    )
    fswap = expm(1j * np.pi * q_coarse / 2)

    vacuum = np.eye(16, dtype=complex)[:, 0]
    k = (c.conj().T - 1j * d.conj().T) / np.sqrt(2)
    columns = []
    for occupied_left, occupied_right in ((0, 0), (0, 1), (1, 0), (1, 1)):
        vector = vacuum
        if occupied_right:
            vector = b.conj().T @ vector
        if occupied_left:
            vector = a.conj().T @ vector
        columns.append(k @ vector)
    oriented_encoding = np.column_stack(columns)

    # S on the right auxiliary endpoint sends the auxiliary state
    # (|10>-i|01>)/sqrt to psi+=(|10>+|01>)/sqrt.  It does not localize
    # Cycle236's full JW stabilizer, which also crosses the interleaved matter
    # mode.  The physical comparator below therefore declares a new local YY
    # constraint rather than misidentifying the transformed JW operator.
    endpoint_phase = kron4(identity, identity, identity, phase)
    m_symmetric = kron4(identity, y, identity, y)
    odd_parity = -kron4(identity, z, identity, z)

    # Exact three-call local preparation of psi+ from |00>:
    # X_right, H_left, CNOT_left->right.
    hadamard = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    cnot = np.zeros((4, 4), dtype=complex)
    for source in range(4):
        left = (source >> 1) & 1
        right = source & 1
        target = (left << 1) | (right ^ left)
        cnot[target, source] = 1
    aux_vacuum = np.asarray((1, 0, 0, 0), dtype=complex)
    prep = cnot @ np.kron(hadamard, identity) @ np.kron(identity, x)
    prepared = prep @ aux_vacuum
    psi_plus = np.asarray((0, 1, 1, 0), dtype=complex) / np.sqrt(2)

    # Product matter/Bell encoding in physical order [a,c,b,d].
    encoding = np.zeros((16, 4), dtype=complex)
    for column, (occupied_left, occupied_right) in enumerate(
        ((0, 0), (0, 1), (1, 0), (1, 1))
    ):
        for cbit, dbit in ((0, 1), (1, 0)):
            row = (occupied_left << 3) | (cbit << 2) | (occupied_right << 1) | dbit
            encoding[row, column] = 1 / np.sqrt(2)

    matter_fswap = np.zeros((16, 16), dtype=complex)
    for source in range(16):
        bits = tuple((source >> (3 - index)) & 1 for index in range(4))
        matter_source = 2 * bits[0] + bits[2]
        for matter_target in range(4):
            coefficient = fswap[matter_target, matter_source]
            if abs(coefficient) < 1e-16:
                continue
            target_bits = (
                (matter_target >> 1) & 1,
                bits[1],
                matter_target & 1,
                bits[3],
            )
            target = sum(bit << (3 - index) for index, bit in enumerate(target_bits))
            matter_fswap[target, source] = coefficient
    plus = (np.eye(16) + m_symmetric) / 2
    minus = (np.eye(16) - m_symmetric) / 2
    update = matter_fswap @ plus + minus

    swap_pair = np.zeros((16, 16), dtype=complex)
    for source in range(16):
        bits = tuple((source >> (3 - index)) & 1 for index in range(4))
        target_bits = (bits[2], bits[3], bits[0], bits[1])
        target = sum(bit << (3 - index) for index, bit in enumerate(target_bits))
        swap_pair[target, source] = 1

    projector = encoding @ encoding.conj().T
    inverse = update.conj().T
    # A fixed small phase on the doubly occupied matter column is a direct
    # bounded perturbation of the link action.
    perturbation = np.eye(16, dtype=complex)
    for basis in range(16):
        if ((basis >> 3) & 1) and ((basis >> 1) & 1):
            perturbation[basis, basis] = np.exp(1j * PERTURBATION)
    perturbed = perturbation @ update
    deleted_update = plus + minus
    wrong_aux = np.asarray((1, 0, 0, 0), dtype=complex)
    transformed_oriented_encoding = endpoint_phase @ oriented_encoding
    controls = {
        "Cycle236_oriented_K_to_covariant_psi_plus_residual": float(
            np.linalg.norm(prepared - psi_plus)
        ),
        "Cycle236_and_local_comparator_one_link_action_residual": float(
            np.linalg.norm(u_oriented @ oriented_encoding - oriented_encoding @ fswap)
            + np.linalg.norm(update @ encoding - encoding @ fswap)
        ),
        "transformed_Cycle236_code_projector_vs_product_Bell_projector_residual": float(
            np.linalg.norm(
                transformed_oriented_encoding @ transformed_oriented_encoding.conj().T
                - encoding @ encoding.conj().T
            )
        ),
        "encoding_isometry_residual": float(
            np.linalg.norm(encoding.conj().T @ encoding - np.eye(4))
        ),
        "Cycle236_transformed_JW_M_vs_local_YY_residual": float(
            np.linalg.norm(endpoint_phase @ m_oriented @ endpoint_phase.conj().T - m_symmetric)
        ),
        "M_constraint_residual": float(np.linalg.norm(m_symmetric @ encoding - encoding)),
        "odd_link_parity_constraint_residual": float(
            np.linalg.norm(odd_parity @ encoding - encoding)
        ),
        "constraint_commutator_residual": float(
            np.linalg.norm(m_symmetric @ odd_parity - odd_parity @ m_symmetric)
        ),
        "one_link_intertwiner_residual": float(np.linalg.norm(update @ encoding - encoding @ fswap)),
        "terminal_code_leakage_residual": float(
            np.linalg.norm((np.eye(16) - projector) @ update @ encoding)
        ),
        "update_unitarity_residual": float(
            np.linalg.norm(update.conj().T @ update - np.eye(16))
        ),
        "inverse_roundtrip_residual": float(np.linalg.norm(inverse @ update - np.eye(16))),
        "endpoint_reversal_update_residual": float(
            np.linalg.norm(swap_pair @ update @ swap_pair - update)
        ),
        "endpoint_reversal_code_projector_residual": float(
            np.linalg.norm(swap_pair @ projector @ swap_pair - projector)
        ),
        "deleted_update_intertwiner_residual": float(
            np.linalg.norm(deleted_update @ encoding - encoding @ fswap)
        ),
        "perturbed_update_intertwiner_residual": float(
            np.linalg.norm(perturbed @ encoding - encoding @ fswap)
        ),
        "deleted_preparation_M_residual": float(
            np.linalg.norm(np.kron(y, y) @ wrong_aux - wrong_aux)
        ),
        "deleted_preparation_odd_parity_residual": float(
            np.linalg.norm(-np.kron(z, z) @ wrong_aux - wrong_aux)
        ),
        "auxiliary_M2_per_link": 2,
        "B_links_per_cell": 3,
        "auxiliary_M2_per_cell": 6,
        "Cycle523_q_plus_tag_M2_per_cell": 7,
        "combined_active_M2_per_cell": 13,
        "preparation_one_two_M2_calls_per_link": 3,
        "preparation_depth_bound": 3,
        "runtime_dressed_gate_support_M2": 4,
        "runtime_dressed_blocks_per_cell": 3,
        "auxiliary_unprepared_during_B": False,
    }
    controls["pass"] = bool(
        controls["Cycle236_oriented_K_to_covariant_psi_plus_residual"] < TOLERANCE
        and controls["Cycle236_and_local_comparator_one_link_action_residual"] < TOLERANCE
        and controls["transformed_Cycle236_code_projector_vs_product_Bell_projector_residual"] > 1
        and controls["encoding_isometry_residual"] < TOLERANCE
        and controls["Cycle236_transformed_JW_M_vs_local_YY_residual"] > 1
        and controls["M_constraint_residual"] < TOLERANCE
        and controls["odd_link_parity_constraint_residual"] < TOLERANCE
        and controls["constraint_commutator_residual"] < TOLERANCE
        and controls["one_link_intertwiner_residual"] < TOLERANCE
        and controls["terminal_code_leakage_residual"] < TOLERANCE
        and controls["update_unitarity_residual"] < TOLERANCE
        and controls["inverse_roundtrip_residual"] < TOLERANCE
        and controls["endpoint_reversal_update_residual"] < TOLERANCE
        and controls["endpoint_reversal_code_projector_residual"] < TOLERANCE
        and controls["deleted_update_intertwiner_residual"] > 1
        and controls["perturbed_update_intertwiner_residual"] > 1e-5
        and controls["deleted_preparation_M_residual"] > 1
        and controls["deleted_preparation_odd_parity_residual"] > 1
        and controls["combined_active_M2_per_cell"] == 13
    )
    return controls


def shifted(cell: tuple[int, int, int], axis: int, amount: int, length: int):
    output = list(cell)
    output[axis] = (output[axis] + amount) % length
    return tuple(output)


def response_equation_mask(
    occupied: tuple[int, ...],
    length: int,
    key_index: dict[tuple[int, int, int], int],
    vacuum_keys: tuple[int, ...],
) -> int:
    """Row for a product of arbitrary endpoint-cell diagonal link phases.

    The unknown f_(axis,left_word,right_word) is an arbitrary bit.  The
    candidate correction exponent is the XOR of f over every positive-axis
    link.  Axis dependence is retained, so this search is more permissive
    than proper-cubic covariance.
    """

    words: dict[tuple[int, int, int], int] = {}
    for mode in occupied:
        cell, direction = c231.index_mode(mode, length)
        words[cell] = words.get(cell, 0) | (1 << direction)

    baseline = 0
    if length**3 % 2:
        for key in vacuum_keys:
            baseline ^= 1 << key
    incident = set()
    for cell in words:
        for axis in range(3):
            incident.add((axis, cell, shifted(cell, axis, 1, length)))
            owner = shifted(cell, axis, -1, length)
            incident.add((axis, owner, cell))
    row = baseline
    for axis, owner, target in incident:
        row ^= 1 << vacuum_keys[axis]
        key = (axis, words.get(owner, 0), words.get(target, 0))
        if key not in key_index:
            key_index[key] = len(key_index)
        row ^= 1 << key_index[key]
    return row


def exact_residual_bit(permutation: np.ndarray, occupied: tuple[int, ...]) -> int:
    exact = c231.exterior_permutation_action(permutation, occupied)
    endpoint = c231.endpoint_fswap_action(permutation, occupied)
    if exact[0] != endpoint[0]:
        raise AssertionError("B actions disagree on the target occupation")
    return int(exact[1] != endpoint[1])


def minimum_link_response_certificate(length: int) -> dict:
    """Complete N<=2 row scan and retain the minimum 1/2-row contradiction."""

    permutation = c231.edge_permutation(length)
    key_index = {(axis, 0, 0): axis for axis in range(3)}
    vacuum_keys = (0, 1, 2)
    representatives: dict[int, tuple[int, tuple[int, ...]]] = {}
    one_row = None
    two_rows = None
    equation_count = 0
    unique_row_rhs = set()

    occupations = [()] + [(mode,) for mode in range(len(permutation))]
    occupations.extend(combinations(range(len(permutation)), 2))
    for occupied in occupations:
        occupied = tuple(occupied)
        row = response_equation_mask(occupied, length, key_index, vacuum_keys)
        rhs = exact_residual_bit(permutation, occupied)
        equation_count += 1
        unique_row_rhs.add((row, rhs))
        if row == 0 and rhs == 1 and one_row is None:
            one_row = (occupied,)
        if row in representatives and representatives[row][0] != rhs and two_rows is None:
            two_rows = (representatives[row][1], occupied)
        representatives.setdefault(row, (rhs, occupied))

    certificate = one_row or two_rows
    if certificate is None:
        raise CertificateFailure(f"no inconsistent one/two-row certificate at L={length}")
    certificate_rows = []
    xor_row = 0
    xor_rhs = 0
    for occupied in certificate:
        row = response_equation_mask(occupied, length, key_index, vacuum_keys)
        rhs = exact_residual_bit(permutation, occupied)
        xor_row ^= row
        xor_rhs ^= rhs
        certificate_rows.append(
            {
                "occupied_modes": occupied,
                "occupied_labels": tuple(c231.index_mode(mode, length) for mode in occupied),
                "equation_nonzero_unknowns": row.bit_count(),
                "equation_rhs": rhs,
                "equation_mask_hex": hex(row),
            }
        )
    return {
        "length": length,
        "equations_complete_vacuum_one_two": equation_count,
        "unknown_endpoint_response_bits_seen": len(key_index),
        "distinct_equation_masks": len(representatives),
        "distinct_row_rhs_pairs": len(unique_row_rhs),
        "minimum_inconsistent_certificate_rows": len(certificate),
        "no_one_row_contradiction": one_row is None,
        "certificate": tuple(certificate_rows),
        "certificate_equation_mask_XOR": hex(xor_row),
        "certificate_rhs_XOR": xor_rhs,
        "axis_specific_response_allowed": True,
        "proper_cubic_covariance_imposed": False,
        "translation_equivariant": True,
        "response_scope": "product of arbitrary diagonal phases f_axis(left_M64_word,right_M64_word)",
        "pass": bool(
            len(certificate) in (1, 2)
            and (len(certificate) == 1 or one_row is None)
            and xor_row == 0
            and xor_rhs == 1
        ),
    }


def global_stream_controls() -> dict:
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        permutation = c231.edge_permutation(length)
        mismatch, total, witness = c231.two_particle_mismatch(length)
        if witness is None:
            raise CertificateFailure(f"missing stream witness at L={length}")
        exact = c231.exterior_permutation_action(permutation, witness)
        endpoint = c231.endpoint_fswap_action(permutation, witness)
        one_failures = sum(
            exact_residual_bit(permutation, (mode,))
            for mode in range(len(permutation))
        )
        response = minimum_link_response_certificate(length)
        rows.append(
            {
                "length": length,
                "modes": len(permutation),
                "vacuum_failures": exact_residual_bit(permutation, ()),
                "one_particle_tests": len(permutation),
                "one_particle_failures": one_failures,
                "complete_two_particle_pairs": total,
                "two_particle_exchange_sign_mismatches": mismatch,
                "first_witness": witness,
                "exact_witness_phase": exact[1],
                "Bell_link_physical_witness_phase": endpoint[1],
                "basis_witness_residual": abs(exact[1] - endpoint[1]),
                "operator_norm_residual": 2,
                "endpoint_response_solve": response,
            }
        )
    return {
        "rows": tuple(rows),
        "global_product_Bell_encoding": "E7 per cell tensor psi+ per B link",
        "physical_B_action_on_code": "product of disjoint endpoint FSWAPs",
        "auxiliary_constraints_live_through_B": True,
        "global_Jordan_Wigner_order_used_by_physical_candidate": False,
        "nonlocal_parity_service_used": False,
        "host_side_runtime_choice_used": False,
        "correlated_link_sector_tested": False,
        "non_diagonal_stateful_link_transition_tested": False,
        "general_local_gauge_no_go": False,
        "pass": bool(
            rows[0]["vacuum_failures"] == rows[1]["vacuum_failures"] == 0
            and rows[0]["one_particle_failures"] == rows[1]["one_particle_failures"] == 0
            and rows[0]["complete_two_particle_pairs"] == 280_875
            and rows[0]["two_particle_exchange_sign_mismatches"] == 60_600
            and rows[1]["complete_two_particle_pairs"] == 839_160
            and rows[1]["two_particle_exchange_sign_mismatches"] == 154_800
            and all(row["basis_witness_residual"] == 2 for row in rows)
            and rows[0]["endpoint_response_solve"]["pass"]
            and rows[0]["endpoint_response_solve"]["minimum_inconsistent_certificate_rows"] == 2
            and rows[1]["endpoint_response_solve"]["minimum_inconsistent_certificate_rows"] == 1
            and rows[1]["endpoint_response_solve"]["certificate_rhs_XOR"] == 1
        ),
    }


def prefix_bits(bits: tuple[int, ...]) -> tuple[int, ...]:
    shadow = [0]
    for bit in bits[:-1]:
        shadow.append(shadow[-1] ^ bit)
    return tuple(shadow)


def prefix_constraint_failures(bits: tuple[int, ...], shadow: tuple[int, ...]) -> int:
    failures = int(shadow[0] != 0)
    failures += sum(
        shadow[index + 1] != (shadow[index] ^ bits[index])
        for index in range(len(bits) - 1)
    )
    return failures


def prefix_phase(bits: tuple[int, ...], shadow: tuple[int, ...]) -> int:
    rest_parity = shadow[-1] ^ bits[0] ^ bits[-1]
    return -1 if bits[0] and rest_parity else 1


def edge_phase_swap(bits: tuple[int, ...]) -> tuple[int, ...]:
    output = list(bits)
    length = len(bits)
    for left in range(1, length, 2):
        right = (left + 1) % length
        output[left], output[right] = output[right], output[left]
    return tuple(output)


def distributed_prefix_controls() -> dict:
    rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        cycle_length = 2 * length
        exact_failures = 0
        constraint_failures = 0
        stale_recode_words = 0
        maximum_stale_constraints = 0
        for bits in product((0, 1), repeat=cycle_length):
            shadow = prefix_bits(bits)
            constraint_failures += prefix_constraint_failures(bits, shadow)
            exact_failures += prefix_phase(bits, shadow) != c260.phase_sign(bits)
            moved = edge_phase_swap(bits)
            stale = prefix_constraint_failures(moved, shadow)
            stale_recode_words += stale > 0
            maximum_stale_constraints = max(maximum_stale_constraints, stale)

        remote = length - 1
        witness = [0] * cycle_length
        witness[0] = 1
        witness[remote] = 1
        exact_shadow = prefix_bits(tuple(witness))
        deleted = list(exact_shadow)
        for index in range(remote + 1, cycle_length):
            deleted[index] ^= 1
        deletion_residual = abs(
            prefix_phase(tuple(witness), exact_shadow)
            - prefix_phase(tuple(witness), tuple(deleted))
        )

        # Preparation lightcone witness: blank auxiliaries with vacuum matter
        # versus one matter bit at position 0 look identical inside radius
        # L-1 around output s_L, but the required s_L values are 0 and 1.
        prep_output = length
        prep_remote = 0
        prep_vacuum = (0,) * cycle_length
        prep_single = (1,) + (0,) * (cycle_length - 1)
        prep_target_pair = (
            prefix_bits(prep_vacuum)[prep_output],
            prefix_bits(prep_single)[prep_output],
        )
        prep_distance = min(
            (prep_output - prep_remote) % cycle_length,
            (prep_remote - prep_output) % cycle_length,
        )

        # Recode lightcone witness includes the *old valid shadow*: vacuum and
        # a single bit at the last site have identical old shadows and are
        # identical inside radius L-1 around output L-1.  After the B matching
        # the last bit moves to site 0, so the required new prefixes differ.
        recode_output = length - 1
        recode_remote = cycle_length - 1
        recode_vacuum = prep_vacuum
        recode_single = (0,) * (cycle_length - 1) + (1,)
        recode_old_shadow_pair = (
            prefix_bits(recode_vacuum),
            prefix_bits(recode_single),
        )
        recode_target_pair = (
            prefix_bits(edge_phase_swap(recode_vacuum))[recode_output],
            prefix_bits(edge_phase_swap(recode_single))[recode_output],
        )
        recode_distance = min(
            (recode_output - recode_remote) % cycle_length,
            (recode_remote - recode_output) % cycle_length,
        )
        rows.append(
            {
                "length": length,
                "alternating_cycles": len(c260.alternating_cycles(length)),
                "cycle_length": cycle_length,
                "complete_cycle_basis_words": 1 << cycle_length,
                "prefix_constraint_failures": constraint_failures,
                "local_phase_failures": exact_failures,
                "runtime_phase_support_M2": 3,
                "runtime_phase_graph_radius": 1,
                "stale_shadow_words_after_B": stale_recode_words,
                "maximum_stale_local_constraints": maximum_stale_constraints,
                "explicit_sequential_preparation_depth": cycle_length - 1,
                "radius_one_preparation_depth_lower_bound": length,
                "radius_one_recode_depth_lower_bound": length,
                "preparation_lightcone_witness": {
                    "output_shadow_position": prep_output,
                    "remote_matter_position": prep_remote,
                    "cyclic_distance": prep_distance,
                    "radius_L_minus_1_inputs_identical": prep_distance == length,
                    "required_output_pair": prep_target_pair,
                },
                "recode_lightcone_witness": {
                    "output_shadow_position": recode_output,
                    "remote_matter_position": recode_remote,
                    "cyclic_distance": recode_distance,
                    "old_shadow_words_identical": recode_old_shadow_pair[0]
                    == recode_old_shadow_pair[1],
                    "radius_L_minus_1_inputs_identical": recode_distance == length,
                    "required_output_pair": recode_target_pair,
                },
                "named_remote_deletion_position": remote,
                "named_remote_deletion_state_residual": deletion_residual,
            }
        )
    return {
        "rows": tuple(rows),
        "encoding": "s_0=0; s_(i+1)=s_i XOR n_i on each opened alternating cycle",
        "local_constraints": "one anchor plus nearest-neighbor prefix checks",
        "runtime_phase": "(-1)^[n_0(s_last XOR n_0 XOR n_last)] at the seam",
        "preparation_and_recode": "exact sequential prefix ladder",
        "selected_seam_anchor_supplied": True,
        "constant_depth_preparation_or_recode_claimed": False,
        "runtime_phase_impossibility_claimed": False,
        "pass": bool(
            all(row["prefix_constraint_failures"] == 0 for row in rows)
            and all(row["local_phase_failures"] == 0 for row in rows)
            and all(row["stale_shadow_words_after_B"] > 0 for row in rows)
            and [row["explicit_sequential_preparation_depth"] for row in rows] == [9, 11]
            and [row["radius_one_preparation_depth_lower_bound"] for row in rows] == [5, 6]
            and all(
                row["preparation_lightcone_witness"]["radius_L_minus_1_inputs_identical"]
                and row["preparation_lightcone_witness"]["required_output_pair"] == (0, 1)
                and row["recode_lightcone_witness"]["old_shadow_words_identical"]
                and row["recode_lightcone_witness"]["radius_L_minus_1_inputs_identical"]
                and row["recode_lightcone_witness"]["required_output_pair"] == (0, 1)
                for row in rows
            )
            and all(row["named_remote_deletion_state_residual"] == 2 for row in rows)
        ),
    }


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    permutation = c210.direction_permutation(frame)
    return tuple(int(np.argmax(permutation[:, source])) for source in range(6))


def layout_and_covariance_controls() -> dict:
    frames = c210.proper_cubic_frames()
    directions = tuple(tuple(int(value) for value in row) for row in c210.DIRECTIONS)
    q_offsets = {tuple(-np.asarray(direction)) for direction in directions}
    aux_offsets = {tuple(3 * np.asarray(direction)) for direction in directions}
    active = q_offsets | aux_offsets | {(0, 0, 0)}
    frame_layout_failures = 0
    for frame in frames:
        moved = {
            tuple(int(value) for value in frame @ np.asarray(offset))
            for offset in active
        }
        frame_layout_failures += moved != active

    patch_rows = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        period = 8 * length
        positions = set()
        for cell in product(range(length), repeat=3):
            center = 8 * np.asarray(cell)
            for offset in active:
                positions.add(
                    tuple(
                        int(value % period)
                        for value in center + np.asarray(offset)
                    )
                )
        patch_rows.append(
            {
                "length": length,
                "active_M2": len(positions),
                "expected_active_M2": 13 * length**3,
                "placement_collisions": 13 * length**3 - len(positions),
            }
        )

    frame_lookup = {tuple(frame.reshape(-1)): frame for frame in frames}
    frame_product_failures = 0
    direction_product_failures = 0
    for first in frames:
        for second in frames:
            target = first @ second
            frame_product_failures += tuple(target.reshape(-1)) not in frame_lookup
            first_map = direction_map(first)
            second_map = direction_map(second)
            target_map = direction_map(target)
            direction_product_failures += any(
                first_map[second_map[index]] != target_map[index]
                for index in range(6)
            )

    # Along a canonical positive-axis coarse link, the four active carriers
    # lie at 1,3,5,7 in an eight-site macro interval.
    link_chain_coordinates = (1, 3, 5, 7)
    controls = {
        "macro_spacing": 8,
        "active_M2_offsets_per_cell": len(active),
        "q_face_offsets": len(q_offsets),
        "auxiliary_radial_offsets": len(aux_offsets),
        "center_tag_offsets": 1,
        "q_to_center_physical_L1": 1,
        "canonical_B_block_coordinates": link_chain_coordinates,
        "canonical_B_block_diameter": max(link_chain_coordinates) - min(link_chain_coordinates),
        "auxiliary_pair_physical_L1": 2,
        "proper_cubic_frames": len(frames),
        "frame_layout_failures": frame_layout_failures,
        "frame_products": len(frames) ** 2,
        "frame_product_failures": frame_product_failures,
        "direction_product_failures": direction_product_failures,
        "L5_L6_recurrent_patch_placements": tuple(patch_rows),
        "Bell_constraints_endpoint_swap_symmetric": True,
        "dressed_update_endpoint_swap_symmetric": True,
    }
    controls["pass"] = bool(
        len(active) == 13
        and len(q_offsets) == len(aux_offsets) == 6
        and controls["canonical_B_block_diameter"] == 6
        and controls["proper_cubic_frames"] == 24
        and controls["frame_products"] == 576
        and frame_layout_failures == frame_product_failures == direction_product_failures == 0
        and all(row["placement_collisions"] == 0 for row in patch_rows)
    )
    return controls


def onsite_and_fixture_controls() -> dict:
    onsite, objects = c523.onsite_compiler_controls()
    layouts = tuple(
        c523.layout_schedule_controls(length, objects["mode_schedule"])
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    c230.PASS = 0
    c230.FAIL = 0
    capture = io.StringIO()
    with redirect_stdout(capture):
        seam = c230.l3_modular_channel_controls()
    singulars = np.linalg.svd(seam, compute_uv=False)
    controls = {
        "Cycle523_onsite_full_M64_pass": onsite["pass"],
        "onsite_EG_intertwiner_residual": onsite["onsite_EG_intertwiner_residual"],
        "terminal_code_leakage_residual": onsite["terminal_code_leakage_residual"],
        "inverse_roundtrip_residual": onsite["inverse_roundtrip_residual"],
        "mass_fixture_residual": onsite["mass_fixture_residual"],
        "contact_active_two_particle_states": onsite["contact_active_two_particle_states"],
        "contact_deletion_residual": onsite["contact_deletion_residual"],
        "logical_onsite_plus_reverse_plus_B_plus_contact_calls_per_cell": tuple(
            row["total_one_two_M2_gate_calls"] // row["coarse_cells"] for row in layouts
        ),
        "Cycle523_layout_pass": all(row["pass"] for row in layouts),
        "Cycle523_proper_frame_edge_set_failures": tuple(
            row["proper_frame_edge_set_failures"] for row in layouts
        ),
        "Cycle523_proper_frame_cell_bijection_failures": tuple(
            row["proper_frame_cell_bijection_failures"] for row in layouts
        ),
        "Bell_dressed_B_blocks_replacing_endpoint_FSWAPs_per_cell": 3,
        "combined_bounded_block_calls_per_cell": 100,
        "maximum_new_B_block_support_M2": 4,
        "four_M2_block_decomposition_to_one_two_M2_primitives_synthesized": False,
        "Cycle230_seam_subchecks": {"pass": c230.PASS, "fail": c230.FAIL},
        "Cycle230_seam_singular_values": tuple(float(value) for value in singulars),
    }
    controls["pass"] = bool(
        onsite["pass"]
        and controls["onsite_EG_intertwiner_residual"] < TOLERANCE
        and controls["terminal_code_leakage_residual"] < TOLERANCE
        and controls["inverse_roundtrip_residual"] < 2e-11
        and controls["mass_fixture_residual"] < TOLERANCE
        and controls["contact_active_two_particle_states"] == 15
        and controls["logical_onsite_plus_reverse_plus_B_plus_contact_calls_per_cell"] == (100, 100)
        and controls["combined_bounded_block_calls_per_cell"] == 100
        and controls["Cycle523_layout_pass"]
        and controls["Cycle523_proper_frame_edge_set_failures"] == (0, 0)
        and controls["Cycle523_proper_frame_cell_bijection_failures"] == (0, 0)
        and c230.FAIL == 0
        and np.linalg.norm(singulars - np.asarray((0.49577141, 0.45566605))) < 2e-8
    )
    return controls


def upstream_evidence() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "authority: none",
        "audit: unset",
        "yy=+1",
        "-zz=+1",
        "60,600",
        "154,800",
        "minimum two-row",
        "100-call/cell",
        "all 24",
        "576",
        "preparation",
        "runtime",
        "correlated link-sector",
        "stateful",
        "broad no-go gate status: **fail / do not ship**",
        "partial-attempt-with-named-untested-routes",
        "proof-search target contract",
        "n1 — alternative-route normalization",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing_fragments": missing, "pass": not missing}


def dry_contract() -> dict:
    evidence = upstream_evidence()
    note = note_contract()
    tests = {
        "strict_predecessor_hashes": evidence["pass"],
        "note_scope_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle528-protected-link-contract-ready" if all(tests.values()) else "cycle528-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "evidence": evidence,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def protected_link_certificate() -> dict:
    started = time.monotonic()
    checkpoints = [checkpoint(started, "initial")]
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle528 dry contract failed")
    local_link = covariant_bell_link_controls()
    checkpoints.append(checkpoint(started, "local-covariant-Bell-link-complete"))
    layout = layout_and_covariance_controls()
    checkpoints.append(checkpoint(started, "layout-all24-576-complete"))
    onsite = onsite_and_fixture_controls()
    checkpoints.append(checkpoint(started, "Cycle523-onsite-and-seam-complete"))
    stream = global_stream_controls()
    checkpoints.append(checkpoint(started, "complete-L5-L6-stream-census-complete"))
    prefix = distributed_prefix_controls()
    checkpoints.append(checkpoint(started, "Cycle260-prefix-comparison-complete"))
    tests = {
        "dry_contract": dry["pass"],
        "exact_covariant_one_link_code_prep_update_inverse_leakage_deletions": local_link["pass"],
        "bounded_layout_all24_and_576_covariance": layout["pass"],
        "Cycle523_100_call_onsite_mass_contact_seam_fixture": onsite["pass"],
        "complete_L5_held_L6_one_two_stream_census_and_minimum_certificate": stream["pass"],
        "Cycle260_runtime_phase_vs_preparation_recode_separation": prefix["pass"],
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    elapsed = time.monotonic() - started
    return {
        "revision": REVISION,
        "mode": "protected-link-certificate",
        "status": (
            "cycle528-one-link-closure-with-global-product-response-falsified"
            if all(tests.values())
            else "cycle528-certificate-failed"
        ),
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "local_covariant_Bell_link": local_link,
        "layout_and_covariance": layout,
        "Cycle523_onsite_and_Cycle230_fixtures": onsite,
        "global_stream": stream,
        "Cycle260_distributed_prefix_comparison": prefix,
        "strongest_constructive_result": {
            "code": "Cycle523 E7 tensor one swap-symmetric psi+ auxiliary pair per B link",
            "local_constraints": "YY=+1 and -ZZ=+1 on each link",
            "preparation": "three fixed one/two-M2 calls per link, constant depth",
            "one_link_intertwiner": "U_link E_link = E_link FSWAP with zero code leakage",
            "runtime": "three disjoint four-M2 dressed B blocks per cell; auxiliary remains live",
            "layout": "13 active M2/cell in an all-frame period-eight bounded neighborhood",
            "protected_shadow_schedule": "Cycle523 exact 100-call/cell schedule retained with B calls replaced one-for-one",
            "full_global_B_intertwiner": False,
        },
        "route_disposition": {
            "Cycle236_one_link_Majorana_comparison": (
                "same exact one-link FSWAP action; distinct full code projector"
            ),
            "product_prepared_Bell_links": "falsified by complete L5/L6 two-particle census",
            "endpoint_cell_diagonal_product_responses": "falsified by minimum two-row GF(2) certificate",
            "Cycle260_distributed_prefix_runtime": "exact bounded-support phase on the already encoded prefix code",
            "Cycle260_prefix_preparation_recode": "explicit depth grows with L; seam anchor supplied",
            "correlated_link_sector_preparation": "open",
            "non_diagonal_stateful_link_gauge_transition": "open",
        },
        "supplied_not_synthesized": {
            "Cycle219_beta_minus_0p3_coin": True,
            "Cycle230_contact_g_0p37_and_factor_order": True,
            "Cycle523_compile_time_QR_schedule": True,
            "period_eight_supercell_origin": True,
            "Cycle260_prefix_seam_anchor": True,
            "physical_duration_or_energy": False,
            "four_M2_dressed_block_one_two_M2_decomposition": False,
            "correlated_link_sector_preparation": False,
            "stateful_gauge_transition": False,
        },
        "no_go_boundary": {
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "bounded_negative": "product-prepared links with endpoint-cell diagonal product responses",
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else protected_link_certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle528-runner-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if payload["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
