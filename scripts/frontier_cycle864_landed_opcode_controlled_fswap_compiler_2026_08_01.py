#!/usr/bin/env python3
"""Cycle 864 exact landed-opcode compiler for controlled charged FSWAP.

The primary result is an eleven-factor, ancilla-free word drawn only from
opcodes actually emitted by the landed Cycle-822/823 grammar.  It implements
neutral-controlled FSWAP on two charged modes in one fixed three-site
nearest-neighbour motif.  The executable certifies the local semantic gate;
it does not claim that the motif has been inserted into the complete Route-B
or Route-C recurrent schedule.

Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import time

import numpy as np

import frontier_cycle821_local_parity_exchange_carrier_recurrent_bell_2026_07_30 as C821
import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822
import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as I823
import frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30 as C827


CONTROL = 0          # neutral
FIRST = 1            # charged
SECOND = 2           # charged
WORK = 3             # clean neutral
WIDTH = 4
TOL = 3.0e-11

# One simultaneous physical motif for every factor in the direct word.  The
# unused WORK wire is listed only because the independent 16-by-16 test keeps
# it as a spectator; no direct-route factor touches it.
FIXED_LOCAL_LAYOUT = {
    CONTROL: (0, 1, 0),
    FIRST: (0, 0, 0),
    SECOND: (1, 0, 0),
    WORK: (0, 0, 1),
}


def lift(matrix, wires):
    return C827.lift_matrix(matrix, tuple(wires), WIDTH)


def phase_residual(left, right):
    overlap = np.vdot(right, left)
    phase = overlap / abs(overlap) if abs(overlap) > 1.0e-14 else 1.0 + 0.0j
    return float(np.linalg.norm(left - phase * right)), phase


def canonical_key(matrix):
    flat = matrix.ravel()
    pivot = next(index for index, value in enumerate(flat) if abs(value) > 1.0e-10)
    normalized = matrix / (flat[pivot] / abs(flat[pivot]))
    return (
        tuple(np.round(normalized.real, 11).ravel())
        + tuple(np.round(normalized.imag, 11).ravel())
    )


def landed_census():
    private = R822.B.P.build_private_atlases()
    context = I823.augment_context(R822.local_site_maps((2, 1, 1), private))
    context, routes, words, *_rest = R822.fixed_typed_compile(context)
    route_list = list(routes)
    before, after = I823.instrument_words(context, route_list)
    all_words = words + before + after
    counts = Counter(
        primitive.kind
        for word in all_words
        for primitive in word.primitives
    )
    support = {}
    for word in all_words:
        for primitive in word.primitives:
            row = support.setdefault(primitive.kind, {
                "occurrences": 0,
                "arities": set(),
                "maximum_two_site_manhattan_distance": 0,
                "nonlocal_two_site_occurrences": 0,
                "exemplar_sites": primitive.sites,
            })
            row["occurrences"] += 1
            row["arities"].add(len(primitive.sites))
            if len(primitive.sites) == 2:
                distance = R822.S789.manhattan(*primitive.sites)
                row["maximum_two_site_manhattan_distance"] = max(
                    row["maximum_two_site_manhattan_distance"], distance
                )
                row["nonlocal_two_site_occurrences"] += distance != 1
    for row in support.values():
        row["arities"] = tuple(sorted(row["arities"]))
    return {
        "counts": counts,
        "support": support,
        "pair_kinds": tuple(sorted(
            kind for kind, count in counts.items()
            if kind.startswith("PAIR_R_") and count
        )),
        "required_neutral_opcode_counts": {
            kind: counts[kind] for kind in (
                "endpoint_CNOT", "endpoint_H", "endpoint_T", "endpoint_Tdg"
            )
        },
    }


def pair_clifford_group(pair_names):
    matrices = {name: R822.primitive_matrix(name) for name in pair_names}
    identity = np.eye(4, dtype=complex)
    queue = deque(((identity, ()),))
    seen = {canonical_key(identity): (identity, ())}
    depth_census = Counter({0: 1})
    while queue:
        matrix, word = queue.popleft()
        for name in pair_names:
            candidate = matrices[name] @ matrix
            key = canonical_key(candidate)
            if key in seen:
                continue
            candidate_word = word + (name,)
            seen[key] = (candidate, candidate_word)
            depth_census[len(candidate_word)] += 1
            queue.append((candidate, candidate_word))
    return tuple(seen.values()), dict(sorted(depth_census.items()))


def shortest_pair_fswap(pair_names):
    target = R822.primitive_matrix("FSWAP")
    matrices = {name: R822.primitive_matrix(name) for name in pair_names}
    identity = np.eye(4, dtype=complex)
    queue = deque(((identity, ()),))
    seen = {canonical_key(identity)}
    depth_frontiers = {}
    best_by_depth = {}
    exact = None
    while queue and exact is None:
        depth = len(queue[0][1])
        level = []
        while queue and len(queue[0][1]) == depth:
            level.append(queue.popleft())
        depth_frontiers[depth] = len(level)
        best = math.inf
        for matrix, word in level:
            residual, phase = phase_residual(matrix, target)
            best = min(best, residual)
            if residual < TOL:
                exact = (word, residual, phase, matrix)
                break
            for name in pair_names:
                candidate = matrices[name] @ matrix
                key = canonical_key(candidate)
                if key in seen:
                    continue
                seen.add(key)
                queue.append((candidate, word + (name,)))
        best_by_depth[depth] = best
    if exact is None:
        raise AssertionError("actual pair Clifford group did not contain FSWAP")
    word, residual, phase, matrix = exact
    return {
        "word": word,
        "residual_up_to_phase": residual,
        "phase_relative_to_FSWAP": phase,
        "matrix": matrix,
        "distinct_projective_group_elements_seen": len(seen),
        "depth_frontiers": depth_frontiers,
        "best_residual_by_depth": best_by_depth,
    }


def pair_pauli(letters):
    return C821.product((
        R822.B.pauli_letter(0, letters[0]),
        R822.B.pauli_letter(1, letters[1]),
    ))


def mapping_rotation(letters, emitted_pair_names):
    # PAIR_R_AB is named for the even Pauli A in Cycle821, but its actual
    # rotation generator is K=-i A Z_pivot.  Control the landed K, not the
    # mnemonic Pauli letters.
    target = R822.B.dense_pauli(C821.pair_rotation_generator(
        0, letters[0], 1, letters[1]
    ), 2)
    z_rows = (
        R822.B.dense_pauli(R822.Pauli(z=1), 2),
        R822.B.dense_pauli(R822.Pauli(z=2), 2),
    )
    rows = []
    for pivot in (0, 1):
        for name in emitted_pair_names:
            unitary = R822.primitive_matrix(name)
            residual = float(np.linalg.norm(
                unitary @ z_rows[pivot] @ unitary.conj().T - target
            ))
            inverse_name = min(
                emitted_pair_names,
                key=lambda other: np.linalg.norm(
                    R822.primitive_matrix(other) - unitary.conj().T
                ),
            )
            inverse_residual = float(np.linalg.norm(
                R822.primitive_matrix(inverse_name) - unitary.conj().T
            ))
            rows.append((residual + inverse_residual, residual, inverse_residual,
                         pivot, name, inverse_name, unitary))
    row = min(rows, key=lambda item: item[:6])
    if row[1] > TOL or row[2] > TOL:
        raise AssertionError(("no actual mapping rotation", letters, row[:6]))
    return {
        "letters": letters,
        "pivot": row[3],
        "unitary_name": row[4],
        "inverse_name": row[5],
        "conjugacy_residual": row[1],
        "inverse_opcode_residual": row[2],
        "unitary": row[6],
    }


def factor(name, matrix, wires, family, opcode=None):
    return {
        "name": name,
        "opcode": opcode or name.split(":", 1)[0].replace(
            "endpoint_T_clean", "endpoint_T"
        ).replace(
            "endpoint_Tdg_clean", "endpoint_Tdg"
        ).replace(
            "endpoint_T_control", "endpoint_T"
        ).replace(
            "endpoint_Tdg_control", "endpoint_Tdg"
        ),
        "matrix": lift(matrix, wires),
        "wires": tuple(wires),
        "family": family,
    }


def controlled_pair_rotation(name, emitted_pair_names):
    # Landed pair names end in _+1 or _-1.
    prefix, sign_text = name.rsplit("_", 1)
    letters = prefix.removeprefix("PAIR_R_")
    sign = int(sign_text)
    mapping = mapping_rotation(letters, emitted_pair_names)
    pivot_wire = (FIRST, SECOND)[mapping["pivot"]]
    endpoint_cnot = I823.primitive_matrix("endpoint_CNOT")
    neutral_t = I823.primitive_matrix("endpoint_T")
    neutral_tdg = I823.primitive_matrix("endpoint_Tdg")
    phase_on_work = neutral_t if sign == 1 else neutral_tdg
    inverse_phase_on_control = neutral_tdg if sign == 1 else neutral_t
    output = [factor(
        mapping["inverse_name"],
        R822.primitive_matrix(mapping["inverse_name"]),
        (FIRST, SECOND), "charged_pair_mapping_inverse",
    )]
    output.extend((
        factor("endpoint_CNOT:pivot->clean", endpoint_cnot,
               (pivot_wire, WORK), "charged_control_neutral_target"),
        factor("endpoint_T_clean" if sign == 1 else "endpoint_Tdg_clean",
               phase_on_work, (WORK,), "neutral_phase_kickback"),
        factor("endpoint_CNOT:pivot->clean", endpoint_cnot,
               (pivot_wire, WORK), "charged_control_neutral_target"),
        factor("endpoint_CNOT:pivot->control", endpoint_cnot,
               (pivot_wire, CONTROL), "charged_control_neutral_target"),
        factor("endpoint_Tdg_control" if sign == 1 else "endpoint_T_control",
               inverse_phase_on_control, (CONTROL,), "neutral_control_phase"),
        factor("endpoint_CNOT:pivot->control", endpoint_cnot,
               (pivot_wire, CONTROL), "charged_control_neutral_target"),
        factor(
            mapping["unitary_name"],
            R822.primitive_matrix(mapping["unitary_name"]),
            (FIRST, SECOND), "charged_pair_mapping_forward",
        ),
    ))

    actual = np.eye(1 << WIDTH, dtype=complex)
    for row in output:
        actual = row["matrix"] @ actual
    pair_gate = R822.primitive_matrix(name)
    pair_lift = lift(pair_gate, (FIRST, SECOND))
    control_one = np.diag(tuple(
        (basis >> CONTROL) & 1 for basis in range(1 << WIDTH)
    )).astype(complex)
    desired = np.eye(1 << WIDTH, dtype=complex) + control_one @ (
        pair_lift - np.eye(1 << WIDTH, dtype=complex)
    )
    clean_columns = tuple(
        basis for basis in range(1 << WIDTH) if not ((basis >> WORK) & 1)
    )
    residual = float(np.linalg.norm(
        (actual - desired)[:, clean_columns]
    ))
    leakage = float(np.linalg.norm(
        actual[np.ix_(
            tuple(basis for basis in range(1 << WIDTH) if (basis >> WORK) & 1),
            clean_columns,
        )]
    ))
    return output, {
        "target_pair_rotation": name,
        "mapping": {key: value for key, value in mapping.items() if key != "unitary"},
        "elementary_factors": len(output),
        "clean_ancilla_controlled_rotation_residual": residual,
        "clean_ancilla_return_leakage": leakage,
    }


def controlled_fswap_synthesis(skeleton, emitted_pair_names):
    factors = []
    blocks = []
    for name in skeleton["word"]:
        start = len(factors)
        block, certificate = controlled_pair_rotation(name, emitted_pair_names)
        factors.extend(block)
        blocks.append((start, len(factors), certificate))
    # Correct the projective phase only on the control-one block.  For the
    # deterministic shortest word below the landed product is -i*FSWAP, so
    # two neutral T gates supply +i.  Keep this branch explicit so a changed
    # enumeration order cannot silently reverse the phase.
    skeleton_phase = skeleton["phase_relative_to_FSWAP"]
    if abs(skeleton_phase + 1j) < TOL:
        phase_kind = "endpoint_T"
        phase_gate = I823.primitive_matrix(phase_kind)
        phase_count = 2
    elif abs(skeleton_phase - 1j) < TOL:
        phase_kind = "endpoint_Tdg"
        phase_gate = I823.primitive_matrix(phase_kind)
        phase_count = 2
    elif abs(skeleton_phase + 1) < TOL:
        phase_kind = "endpoint_T"
        phase_gate = I823.primitive_matrix(phase_kind)
        phase_count = 4
    elif abs(skeleton_phase - 1) < TOL:
        phase_kind = "endpoint_T"
        phase_gate = I823.primitive_matrix(phase_kind)
        phase_count = 0
    else:
        raise AssertionError(("unsupported FSWAP projective phase", skeleton_phase))
    for ordinal in range(phase_count):
        factors.append(factor(
            f"{phase_kind}_control:phase_correction_{ordinal + 1}",
            phase_gate, (CONTROL,), "neutral_relative_phase_correction",
        ))

    parity_local = np.diag(tuple(
        (-1) ** (((basis >> FIRST) & 1) + ((basis >> SECOND) & 1))
        for basis in range(1 << WIDTH)
    )).astype(complex)
    prefix = np.eye(1 << WIDTH, dtype=complex)
    factor_commutators = []
    prefix_commutators = []
    for row in factors:
        factor_commutators.append(float(np.linalg.norm(
            row["matrix"] @ parity_local - parity_local @ row["matrix"]
        )))
        prefix = row["matrix"] @ prefix
        prefix_commutators.append(float(np.linalg.norm(
            prefix @ parity_local - parity_local @ prefix
        )))
    actual = prefix
    fswap = R822.primitive_matrix("FSWAP")
    fswap_lift = lift(fswap, (FIRST, SECOND))
    control_one = np.diag(tuple(
        (basis >> CONTROL) & 1 for basis in range(1 << WIDTH)
    )).astype(complex)
    target = np.eye(1 << WIDTH, dtype=complex) + control_one @ (
        fswap_lift - np.eye(1 << WIDTH, dtype=complex)
    )
    clean_columns = tuple(
        basis for basis in range(1 << WIDTH) if not ((basis >> WORK) & 1)
    )
    dirty_columns = tuple(
        basis for basis in range(1 << WIDTH) if (basis >> WORK) & 1
    )
    clean_residual = float(np.linalg.norm(
        (actual - target)[:, clean_columns]
    ))
    dirty_residual = float(np.linalg.norm(
        (actual - target)[:, dirty_columns]
    ))
    leakage_rows = tuple(
        basis for basis in range(1 << WIDTH) if (basis >> WORK) & 1
    )
    clean_leakage = float(np.linalg.norm(
        actual[np.ix_(leakage_rows, clean_columns)]
    ))
    unitarity = float(np.linalg.norm(
        actual.conj().T @ actual - np.eye(1 << WIDTH)
    ))

    deletion_rows = []
    for deleted in range(len(factors)):
        damaged = np.eye(1 << WIDTH, dtype=complex)
        for index, row in enumerate(factors):
            if index != deleted:
                damaged = row["matrix"] @ damaged
        difference = (damaged - target)[:, clean_columns]
        singular = np.linalg.svd(difference, compute_uv=False)
        deletion_rows.append({
            "ordinal": deleted,
            "name": factors[deleted]["name"],
            "family": factors[deleted]["family"],
            "residual": float(np.linalg.norm(difference)),
            "rank": int(sum(value > 1.0e-10 for value in singular)),
            "singular_values": tuple(float(value) for value in singular),
        })
    block_deletions = []
    for block_index, (start, stop, certificate) in enumerate(blocks):
        damaged = np.eye(1 << WIDTH, dtype=complex)
        for index, row in enumerate(factors):
            if not start <= index < stop:
                damaged = row["matrix"] @ damaged
        block_deletions.append({
            "block": block_index,
            "target": certificate["target_pair_rotation"],
            "residual": float(np.linalg.norm(
                (damaged - target)[:, clean_columns]
            )),
        })
    return {
        "factors": factors,
        "block_certificates": tuple(row[2] for row in blocks),
        "elementary_factors": len(factors),
        "projective_phase_correction_opcode": phase_kind,
        "projective_phase_correction_count": phase_count,
        "factor_family_census": dict(sorted(Counter(
            row["family"] for row in factors
        ).items())),
        "clean_ancilla_target_residual": clean_residual,
        "clean_ancilla_return_leakage": clean_leakage,
        "dirty_ancilla_target_residual": dirty_residual,
        "unitarity_residual": unitarity,
        "maximum_factor_P_ext_commutator": max(factor_commutators),
        "maximum_prefix_P_ext_commutator": max(prefix_commutators),
        "target_P_ext_commutator": float(np.linalg.norm(
            target @ parity_local - parity_local @ target
        )),
        "single_factor_deletions_tested": len(deletion_rows),
        "single_factor_deletions_detected": sum(
            row["residual"] > 1.0e-8 for row in deletion_rows
        ),
        "minimum_single_factor_deletion_residual": min(
            row["residual"] for row in deletion_rows
        ),
        "maximum_single_factor_deletion_residual": max(
            row["residual"] for row in deletion_rows
        ),
        "minimum_single_factor_deletion_rank": min(
            row["rank"] for row in deletion_rows
        ),
        "block_deletions": tuple(block_deletions),
        "deletion_rows": tuple(deletion_rows),
        "factor_word": tuple(row["name"] for row in factors),
        "factor_word_sha256": sha256(repr(tuple(
            row["name"] for row in factors
        )).encode()).hexdigest(),
    }


def opcode_word_matrix(word):
    output = np.eye(4, dtype=complex)
    for name in word:
        output = R822.primitive_matrix(name) @ output
    return output


def givens_routes(pair_group):
    catalog = R822.nonseam_opcode_catalog()
    givens = tuple(
        (row["opcode"], R822.primitive_matrix(row["opcode"]))
        for row in catalog["opcodes"]
        if row["landed_kind"] == "coin_coin_givens"
    )
    fswap = R822.primitive_matrix("FSWAP")
    z_first = R822.B.dense_pauli(R822.Pauli(z=1), 2)

    best = (math.inf, (), None)
    exact = 0
    frontier = ((np.eye(4, dtype=complex), ()),)
    depth_rows = []
    for depth in range(1, 5):
        next_frontier = []
        depth_best = (math.inf, ())
        for matrix, word in frontier:
            for name, gate in givens:
                candidate = gate @ matrix
                candidate_word = word + (name,)
                residual = float(np.linalg.norm(
                    candidate @ z_first @ candidate.conj().T - fswap
                ))
                if residual < depth_best[0]:
                    depth_best = (residual, candidate_word)
                if residual < best[0]:
                    best = (residual, candidate_word, candidate)
                exact += residual < TOL
                next_frontier.append((candidate, candidate_word))
        depth_rows.append({
            "depth": depth,
            "words": len(next_frontier),
            "best_conjugacy_residual": depth_best[0],
            "best_word": depth_best[1],
        })
        frontier = tuple(next_frontier)

    # Stronger one-Givens route: arbitrary actual pair-Clifford dressing on
    # both sides.  This is finite because the emitted pair group has 192
    # projective elements.
    dressed_best = (math.inf, (), None)
    dressed_exact = 0
    selected_dagger = None
    for left, left_word in pair_group:
        for name, gate in givens:
            left_gate = left @ gate
            for right, right_word in pair_group:
                candidate = left_gate @ right
                candidate_word = right_word + (name,) + left_word
                residual = float(np.linalg.norm(
                    candidate @ z_first @ candidate.conj().T - fswap
                ))
                if residual < dressed_best[0]:
                    dressed_best = (
                        residual, candidate_word, candidate
                    )
                if residual < TOL:
                    dressed_exact += 1
                    key = (len(candidate_word), residual, candidate_word)
                    if selected_dagger is None or key < selected_dagger[0]:
                        selected_dagger = (key, candidate_word, candidate)

    if selected_dagger is None:
        raise AssertionError("dressed landed-Givens grammar lost its conjugator")
    _dagger_key, dagger_word, dagger_matrix = selected_dagger

    # Search the same finite forward grammar for an exact matrix inverse,
    # rather than assuming the inverse of a landed Givens is a primitive.
    inverse_target = dagger_matrix.conj().T
    inverse_best = (math.inf, (), None)
    inverse_exact = 0
    selected_w = None
    for left, left_word in pair_group:
        for name, gate in givens:
            left_gate = left @ gate
            for right, right_word in pair_group:
                candidate = left_gate @ right
                candidate_word = right_word + (name,) + left_word
                residual = float(np.linalg.norm(candidate - inverse_target))
                if residual < inverse_best[0]:
                    inverse_best = (residual, candidate_word, candidate)
                if residual < TOL:
                    inverse_exact += 1
                    key = (len(candidate_word), residual, candidate_word)
                    if selected_w is None or key < selected_w[0]:
                        selected_w = (key, candidate_word, candidate)
    if selected_w is None:
        raise AssertionError("no exact forward landed-opcode inverse word")
    _w_key, w_word, w_matrix = selected_w

    inverse_projective_residual, inverse_phase = phase_residual(
        dagger_matrix, w_matrix.conj().T
    )
    return {
        "landed_givens": len(givens),
        "landed_givens_names": tuple(name for name, _matrix in givens),
        "forward_only_depth_search": tuple(depth_rows),
        "forward_only_words_tested": sum(row["words"] for row in depth_rows),
        "forward_only_exact_conjugators": exact,
        "forward_only_best_residual": best[0],
        "forward_only_best_word": best[1],
        "one_givens_pair_clifford_dressed_words_tested": (
            len(pair_group) * len(givens) * len(pair_group)
        ),
        "one_givens_pair_clifford_dressed_exact_conjugators": dressed_exact,
        "one_givens_pair_clifford_dressed_best_residual": dressed_best[0],
        "one_givens_pair_clifford_dressed_best_word": dressed_best[1],
        "exact_inverse_forward_words_tested": (
            len(pair_group) * len(givens) * len(pair_group)
        ),
        "exact_inverse_forward_matches": inverse_exact,
        "exact_inverse_best_residual": inverse_best[0],
        "selected_W_word_application_order": w_word,
        "selected_W_dagger_word_application_order": dagger_word,
        "selected_W_factors": len(w_word),
        "selected_W_dagger_factors": len(dagger_word),
        "selected_W_matrix": w_matrix,
        "selected_W_dagger_matrix": dagger_matrix,
        "W_dagger_exact_inverse_residual": float(np.linalg.norm(
            dagger_matrix - w_matrix.conj().T
        )),
        "W_dagger_inverse_projective_residual": inverse_projective_residual,
        "W_dagger_inverse_relative_phase": inverse_phase,
        "W_dagger_Z_W_literal_FSWAP_residual": float(np.linalg.norm(
            dagger_matrix @ z_first @ w_matrix - fswap
        )),
        "W_dagger_W_identity_residual": float(np.linalg.norm(
            dagger_matrix @ w_matrix - np.eye(4)
        )),
        "boundary": (
            "Positive finite-grammar result: W and its exact matrix adjoint "
            "are both forward words in the landed dictionary."
        ),
    }


def givens_controlled_fswap_synthesis(givens, census):
    factors = []
    for name in givens["selected_W_word_application_order"]:
        factors.append(factor(
            name, R822.primitive_matrix(name), (FIRST, SECOND),
            "W_charged_pair_conjugator", opcode=name,
        ))

    endpoint_h = I823.primitive_matrix("endpoint_H")
    endpoint_cnot = I823.primitive_matrix("endpoint_CNOT")
    core_start = len(factors)
    factors.extend((
        factor("endpoint_H_control:CZ_pre", endpoint_h, (CONTROL,),
               "neutral_H_for_CZ", opcode="endpoint_H"),
        factor("endpoint_CNOT:charged_first_to_neutral_control", endpoint_cnot,
               (FIRST, CONTROL), "charged_control_neutral_target",
               opcode="endpoint_CNOT"),
        factor("endpoint_H_control:CZ_post", endpoint_h, (CONTROL,),
               "neutral_H_for_CZ", opcode="endpoint_H"),
    ))
    core_stop = len(factors)

    for name in givens["selected_W_dagger_word_application_order"]:
        factors.append(factor(
            name, R822.primitive_matrix(name), (FIRST, SECOND),
            "W_dagger_charged_pair_conjugator", opcode=name,
        ))

    parity_local = np.diag(tuple(
        (-1) ** (((basis >> FIRST) & 1) + ((basis >> SECOND) & 1))
        for basis in range(1 << WIDTH)
    )).astype(complex)
    prefix = np.eye(1 << WIDTH, dtype=complex)
    factor_commutators = []
    prefix_commutators = []
    for row in factors:
        factor_commutators.append(float(np.linalg.norm(
            row["matrix"] @ parity_local - parity_local @ row["matrix"]
        )))
        prefix = row["matrix"] @ prefix
        prefix_commutators.append(float(np.linalg.norm(
            prefix @ parity_local - parity_local @ prefix
        )))
    actual = prefix

    literal_fswap = R822.primitive_matrix("FSWAP")
    fswap_lift = lift(literal_fswap, (FIRST, SECOND))
    control_one = np.diag(tuple(
        (basis >> CONTROL) & 1 for basis in range(1 << WIDTH)
    )).astype(complex)
    target = np.eye(1 << WIDTH, dtype=complex) + control_one @ (
        fswap_lift - np.eye(1 << WIDTH, dtype=complex)
    )
    logical_columns = tuple(
        basis for basis in range(1 << WIDTH) if not ((basis >> WORK) & 1)
    )
    column_residuals = tuple(float(np.linalg.norm(
        (actual - target)[:, source]
    )) for source in logical_columns)
    control_return_leakages = []
    ancilla_return_leakages = []
    for source in logical_columns:
        control_value = (source >> CONTROL) & 1
        control_rows = tuple(
            row for row in range(1 << WIDTH)
            if ((row >> CONTROL) & 1) != control_value
        )
        work_rows = tuple(
            row for row in range(1 << WIDTH) if (row >> WORK) & 1
        )
        control_return_leakages.append(float(np.linalg.norm(
            actual[control_rows, source]
        )))
        ancilla_return_leakages.append(float(np.linalg.norm(
            actual[work_rows, source]
        )))

    core = np.eye(1 << WIDTH, dtype=complex)
    for row in factors[core_start:core_stop]:
        core = row["matrix"] @ core
    cz = np.diag(tuple(
        -1.0 if (
            ((basis >> CONTROL) & 1) and ((basis >> FIRST) & 1)
        ) else 1.0
        for basis in range(1 << WIDTH)
    )).astype(complex)

    deletion_rows = []
    for deleted in range(len(factors)):
        damaged = np.eye(1 << WIDTH, dtype=complex)
        for index, row in enumerate(factors):
            if index != deleted:
                damaged = row["matrix"] @ damaged
        difference = (damaged - target)[:, logical_columns]
        singular = np.linalg.svd(difference, compute_uv=False)
        per_column = tuple(float(np.linalg.norm(
            difference[:, column]
        )) for column in range(len(logical_columns)))
        deletion_rows.append({
            "ordinal": deleted,
            "name": factors[deleted]["name"],
            "opcode": factors[deleted]["opcode"],
            "family": factors[deleted]["family"],
            "residual_over_all_8_columns": float(np.linalg.norm(difference)),
            "changed_logical_columns": sum(value > 1.0e-8 for value in per_column),
            "minimum_column_residual": min(per_column),
            "maximum_column_residual": max(per_column),
            "difference_rank": int(sum(
                value > 1.0e-10 for value in singular
            )),
            "singular_values": tuple(float(value) for value in singular),
        })

    unique_opcodes = tuple(dict.fromkeys(row["opcode"] for row in factors))
    landed_rows = {
        opcode: census["support"].get(opcode, {
            "occurrences": 0,
            "arities": (),
            "maximum_two_site_manhattan_distance": math.inf,
            "nonlocal_two_site_occurrences": math.inf,
            "exemplar_sites": (),
        })
        for opcode in unique_opcodes
    }
    control_zero = tuple(
        basis for basis in logical_columns if not ((basis >> CONTROL) & 1)
    )
    control_one_rows = tuple(
        basis for basis in logical_columns if (basis >> CONTROL) & 1
    )
    control_zero_block = actual[np.ix_(control_zero, control_zero)]
    control_one_block = actual[np.ix_(control_one_rows, control_one_rows)]

    w = givens["selected_W_matrix"]
    w_dagger = givens["selected_W_dagger_matrix"]
    z_first = R822.B.dense_pauli(R822.Pauli(z=1), 2)
    layout_distances = tuple(
        0 if len(row["wires"]) == 1 else sum(
            abs(a - b) for a, b in zip(
                FIXED_LOCAL_LAYOUT[row["wires"][0]],
                FIXED_LOCAL_LAYOUT[row["wires"][1]],
            )
        )
        for row in factors
    )
    return {
        "factors": factors,
        "factor_word_application_order": tuple(row["name"] for row in factors),
        "factor_opcode_word_application_order": tuple(
            row["opcode"] for row in factors
        ),
        "factor_word_sha256": sha256(repr(tuple(
            row["name"] for row in factors
        )).encode()).hexdigest(),
        "elementary_factors": len(factors),
        "factor_family_census": dict(sorted(Counter(
            row["family"] for row in factors
        ).items())),
        "W_word_application_order": givens[
            "selected_W_word_application_order"
        ],
        "W_dagger_word_application_order": givens[
            "selected_W_dagger_word_application_order"
        ],
        "W_dagger_exact_inverse_residual": float(np.linalg.norm(
            w_dagger - w.conj().T
        )),
        "W_dagger_inverse_relative_phase": phase_residual(
            w_dagger, w.conj().T
        )[1],
        "W_dagger_Z_W_literal_FSWAP_residual": float(np.linalg.norm(
            w_dagger @ z_first @ w - literal_fswap
        )),
        "W_dagger_W_identity_residual": float(np.linalg.norm(
            w_dagger @ w - np.eye(4)
        )),
        "CZ_core_H_CNOT_H_residual": float(np.linalg.norm(core - cz)),
        "literal_Cycle822_FSWAP_matrix_sha256": (
            R822.U720.c707.c655.matrix_digest(literal_fswap)
        ),
        "all_8_controlled_FSWAP_column_residuals": column_residuals,
        "maximum_8_column_residual": max(column_residuals),
        "residual_over_all_8_columns": float(np.linalg.norm(
            (actual - target)[:, logical_columns]
        )),
        "full_16_by_16_spectator_work_target_residual": float(np.linalg.norm(
            actual - target
        )),
        "control_zero_identity_block_residual": float(np.linalg.norm(
            control_zero_block - np.eye(4)
        )),
        "control_one_literal_FSWAP_block_residual": float(np.linalg.norm(
            control_one_block - literal_fswap
        )),
        "maximum_control_return_leakage": max(control_return_leakages),
        "maximum_unused_ancilla_return_leakage": max(ancilla_return_leakages),
        "unitarity_residual": float(np.linalg.norm(
            actual.conj().T @ actual - np.eye(1 << WIDTH)
        )),
        "synthesis_square_identity_residual": float(np.linalg.norm(
            actual @ actual - np.eye(1 << WIDTH)
        )),
        "synthesis_self_inverse_residual": float(np.linalg.norm(
            actual.conj().T - actual
        )),
        "literal_target_square_identity_residual": float(np.linalg.norm(
            target @ target - np.eye(1 << WIDTH)
        )),
        "maximum_factor_P_ext_commutator": max(factor_commutators),
        "maximum_prefix_P_ext_commutator": max(prefix_commutators),
        "target_P_ext_commutator": float(np.linalg.norm(
            target @ parity_local - parity_local @ target
        )),
        "landed_actual_emission_support": landed_rows,
        "all_factor_opcodes_actually_emitted": all(
            row["occurrences"] > 0 for row in landed_rows.values()
        ),
        "all_emitted_two_site_exemplars_nearest_neighbour_and_onsite_local": all(
            row["nonlocal_two_site_occurrences"] == 0
            and set(row["arities"]) <= {1, 2}
            for row in landed_rows.values()
        ),
        "semantic_factor_supports": tuple({
            "ordinal": ordinal,
            "opcode": row["opcode"],
            "logical_wires": row["wires"],
            "arity": len(row["wires"]),
        } for ordinal, row in enumerate(factors)),
        "fixed_simultaneous_local_layout": {
            "neutral_control": FIXED_LOCAL_LAYOUT[CONTROL],
            "charged_first": FIXED_LOCAL_LAYOUT[FIRST],
            "charged_second": FIXED_LOCAL_LAYOUT[SECOND],
            "unused_spectator_work": FIXED_LOCAL_LAYOUT[WORK],
        },
        "fixed_layout_factor_distances": layout_distances,
        "maximum_fixed_layout_factor_distance": max(layout_distances),
        "all_direct_factors_onsite_or_nearest_neighbour_in_one_layout": all(
            distance <= 1 for distance in layout_distances
        ),
        "single_factor_deletions_tested": len(deletion_rows),
        "single_factor_deletions_detected": sum(
            row["residual_over_all_8_columns"] > 1.0e-8
            for row in deletion_rows
        ),
        "minimum_single_factor_deletion_residual": min(
            row["residual_over_all_8_columns"] for row in deletion_rows
        ),
        "deletion_rows": tuple(deletion_rows),
    }


def sanitize(value):
    if isinstance(value, dict):
        return {
            str(key): sanitize(item)
            for key, item in value.items()
            if key not in ("matrix", "unitary", "factors")
            and not str(key).endswith("_matrix")
        }
    if isinstance(value, (tuple, list)):
        return [sanitize(item) for item in value]
    if isinstance(value, complex):
        return (float(value.real), float(value.imag))
    if isinstance(value, np.generic):
        return sanitize(value.item())
    if isinstance(value, np.ndarray):
        return sanitize(value.tolist())
    return value


def main():
    started = time.time()
    census = landed_census()
    emitted_pair_names = census["pair_kinds"]
    pair_group, group_depths = pair_clifford_group(emitted_pair_names)
    skeleton = shortest_pair_fswap(emitted_pair_names)
    synthesis = controlled_fswap_synthesis(skeleton, emitted_pair_names)
    givens = givens_routes(pair_group)
    direct = givens_controlled_fswap_synthesis(givens, census)
    checks = {
        "only_emitted_pair_opcodes_are_used": all(
            name in emitted_pair_names for name in skeleton["word"]
        ),
        "neutral_T_Tdg_CNOT_are_actually_emitted": all(
            census["required_neutral_opcode_counts"][name] > 0
            for name in census["required_neutral_opcode_counts"]
        ),
        "six_pair_word_is_FSWAP_up_to_an_exact_quarter_phase": (
            len(skeleton["word"]) == 6
            and skeleton["residual_up_to_phase"] < TOL
            and min(
                abs(skeleton["phase_relative_to_FSWAP"] - phase)
                for phase in (1, -1, 1j, -1j)
            ) < TOL
        ),
        "clean_phase_kickback_synthesis_is_exact_and_returns_work": (
            synthesis["clean_ancilla_target_residual"] < TOL
            and synthesis["clean_ancilla_return_leakage"] < TOL
            and synthesis["unitarity_residual"] < TOL
        ),
        "every_factor_and_prefix_commutes_with_same_P_ext": (
            synthesis["maximum_factor_P_ext_commutator"] < TOL
            and synthesis["maximum_prefix_P_ext_commutator"] < TOL
            and synthesis["target_P_ext_commutator"] < TOL
        ),
        "every_single_factor_and_controlled_block_deletion_is_active": (
            synthesis["single_factor_deletions_detected"]
            == synthesis["single_factor_deletions_tested"]
            and all(row["residual"] > 1.0e-8 for row in synthesis["block_deletions"])
        ),
        "landed_Givens_W_and_W_dagger_are_exact_forward_words": (
            direct["W_dagger_exact_inverse_residual"] < TOL
            and direct["W_dagger_Z_W_literal_FSWAP_residual"] < TOL
            and direct["W_dagger_W_identity_residual"] < TOL
            and abs(direct["W_dagger_inverse_relative_phase"] - 1) < TOL
        ),
        "eleven_factor_ancilla_free_controlled_FSWAP_matches_all_8_columns": (
            direct["elementary_factors"] == 11
            and direct["maximum_8_column_residual"] < TOL
            and direct["full_16_by_16_spectator_work_target_residual"] < TOL
            and direct["control_zero_identity_block_residual"] < TOL
            and direct["control_one_literal_FSWAP_block_residual"] < TOL
        ),
        "direct_route_returns_control_and_unused_ancilla_and_is_self_inverse": (
            direct["maximum_control_return_leakage"] < TOL
            and direct["maximum_unused_ancilla_return_leakage"] < TOL
            and direct["synthesis_square_identity_residual"] < TOL
            and direct["synthesis_self_inverse_residual"] < TOL
        ),
        "direct_route_every_factor_is_landed_and_has_local_NN_exemplars": (
            direct["all_factor_opcodes_actually_emitted"]
            and direct[
                "all_emitted_two_site_exemplars_nearest_neighbour_and_onsite_local"
            ]
        ),
        "direct_route_has_one_fixed_three_site_NN_layout": (
            direct[
                "all_direct_factors_onsite_or_nearest_neighbour_in_one_layout"
            ]
            and direct["maximum_fixed_layout_factor_distance"] == 1
            and all(WORK not in row["logical_wires"] for row in direct[
                "semantic_factor_supports"
            ])
        ),
        "direct_route_every_factor_and_prefix_commutes_with_same_P_ext": (
            direct["maximum_factor_P_ext_commutator"] < TOL
            and direct["maximum_prefix_P_ext_commutator"] < TOL
            and direct["target_P_ext_commutator"] < TOL
        ),
        "direct_route_delete_each_of_11_factors_is_active": (
            direct["single_factor_deletions_detected"]
            == direct["single_factor_deletions_tested"]
            == 11
        ),
    }
    report = {
        "status": (
            "cycle864-landed-opcode-neutral-controlled-charged-FSWAP-positive"
            if all(checks.values()) else "cycle864-controlled-FSWAP-failed"
        ),
        "target": (
            "neutral control and two charged target modes; direct route uses no "
            "ancilla, alternate route uses one clean neutral work M2; same "
            "P_ext=Z_first Z_second at every prefix"
        ),
        "landed_dictionary": {
            "pair_kind_census": {
                kind: census["counts"][kind] for kind in emitted_pair_names
            },
            "required_neutral_opcode_counts": census[
                "required_neutral_opcode_counts"
            ],
            "nonseam_opcode_dictionary_sha256": R822.nonseam_opcode_catalog()[
                "opcode_dictionary_sha256"
            ],
        },
        "source_file_sha256": {
            "Cycle821": sha256(Path(C821.__file__).read_bytes()).hexdigest(),
            "Cycle822": sha256(Path(R822.__file__).read_bytes()).hexdigest(),
            "Cycle823": sha256(Path(I823.__file__).read_bytes()).hexdigest(),
            "Cycle827_lift_helper": sha256(Path(C827.__file__).read_bytes()).hexdigest(),
            "Cycle864_probe": sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "pair_clifford_group": {
            "projective_elements": len(pair_group),
            "shortest_word_depth_census": group_depths,
        },
        "uncontrolled_FSWAP_pair_identity": skeleton,
        "clean_ancilla_phase_kickback_synthesis": synthesis,
        "landed_coin_givens_search": givens,
        "landed_Givens_ancilla_free_controlled_FSWAP_synthesis": direct,
        "checks": checks,
        "inventory": {
            "direct_11_factor_route_used": (
                "actually emitted Cycle822 PAIR_R_XX/XY/YX opcodes",
                "actually emitted landed coin Givens G_coin_coin_givens_b45094ee4507a094",
                "actual Cycle823 endpoint_H and charged-control/neutral-target endpoint_CNOT",
                "no work ancilla",
            ),
            "clean_50_factor_route_used": (
                "actually emitted Cycle822 PAIR_R_XX/XY/YX with both signs",
                "actual Cycle823 neutral T/T-dagger and charged-control/neutral-target CNOT",
                "one supplied clean neutral work M2",
            ),
            "not_used": (
                "PAIR_R_YY (algebraically available in Cycle821 but absent from the emitted base word)",
                "arbitrary Givens or H_dual",
                "neutral-control/charged-target CNOT",
            ),
            "semantic_substitution_now_closed": (
                "the neutral-controlled charged FSWAP matrix required by Routes B/C has an exact forward landed-opcode word",
                "the direct word has no ancilla premise and preserves one fixed P_ext at every elementary prefix",
                "all eleven factors fit one three-site charged-charged-neutral nearest-neighbour motif",
            ),
            "remaining_route_B_C_placement_and_schedule_work_not_claimed_here": (
                "bind a copy of the certified three-site motif into each complete Route B/C physical atlas",
                "insert/validate returned-label FSWAP or SWAP transport when those three modes are not already adjacent",
                "re-colour the expanded 11-factor word against the full Route B/C schedule and collision constraints",
                "rerun whole-box prefix parity, endpoint availability, and resource census after substitution",
            ),
        },
        "runtime_seconds": time.time() - started,
    }
    print("REPORT_JSON", json.dumps(sanitize(report), sort_keys=True))
    for label, passed in checks.items():
        print("CHECK", label, "PASS" if passed else "FAIL")
    if not all(checks.values()):
        raise SystemExit(1)
    print("ACTUAL_LANDED_OPCODE_NEUTRAL_CONTROLLED_CHARGED_FSWAP_DIRECT_AND_CLEAN_WORK_PASS")


if __name__ == "__main__":
    main()
