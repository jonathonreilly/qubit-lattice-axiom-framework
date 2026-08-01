#!/usr/bin/env python3
"""Cycle 864 Route-C typed-exchange matrix candidate.

This runner replays an exact eleven-factor charged cFSWAP matrix word and a
returned-routed twenty-one-factor all-neutral Fredkin matrix word through the
repo-native selected Route-C service construction.  Every candidate factor is
bound to its canonical imported opcode matrix, arity, declared local sites,
and an explicitly supplied retyped selected palette.

This is a matrix candidate, not an actual-atlas coordinate-support or
fixed-law promotion claim.
The generic relocation of locally available opcode kinds onto the candidate
palette, the singleton serial factor slots, the rooted two-word boundary, and
the clean successful-admission sector are supplied.  Proper-cubic, product,
translation, and held checks are passive transports of that supplied finite
program only.  Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path

import numpy as np

import frontier_cycle864_two_station_service_token_discriminator_2026_08_01 as C


RUNNER_SOURCE = Path(__file__).resolve()
REPO_ROOT = RUNNER_SOURCE.parent.parent
ROUTE_C_SOURCE = Path(C.__file__).resolve()
TOL = 4.0e-11

R822 = C.R822
I823 = C.I823
H719 = C.H719


W_WORD = (
    "PAIR_R_XX_-1",
    "G_coin_coin_givens_b45094ee4507a094",
    "PAIR_R_XY_+1",
    "PAIR_R_YX_-1",
    "PAIR_R_XX_+1",
)
W_DAGGER_WORD = (
    "PAIR_R_XY_+1",
    "PAIR_R_YX_-1",
    "G_coin_coin_givens_b45094ee4507a094",
)


def core_factor_specs():
    """(label, opcode, matrix, logical wires, family), in application order.

    Local logical wires are control=0, charged-first=1, charged-second=2.
    The physical integration orients charged-first at pair[1], the endpoint
    adjacent to the neutral taxi terminal.
    """
    output = []
    for opcode in W_WORD:
        output.append((opcode, opcode, R822.primitive_matrix(opcode), (1, 2), "W"))
    output.extend((
        (
            "endpoint_H_control:CZ_pre", "endpoint_H",
            I823.primitive_matrix("endpoint_H"), (0,), "CZ_core",
        ),
        (
            "endpoint_CNOT:charged_first_to_neutral_control", "endpoint_CNOT",
            I823.primitive_matrix("endpoint_CNOT"), (1, 0), "CZ_core",
        ),
        (
            "endpoint_H_control:CZ_post", "endpoint_H",
            I823.primitive_matrix("endpoint_H"), (0,), "CZ_core",
        ),
    ))
    for opcode in W_DAGGER_WORD:
        output.append((
            opcode, opcode, R822.primitive_matrix(opcode), (1, 2), "W_dagger"
        ))
    if len(output) != 11:
        raise AssertionError(("charged matrix candidate factor census", len(output)))
    return tuple(output)


CORE_FACTORS = core_factor_specs()


def neutral_fredkin_logical_specs():
    """Exact all-neutral cSWAP for the clean Cycle823 pointer corridor.

    Logical wires are enable control=0, pointer a=1 (adjacent to control), and
    pointer b=2.  CNOT(a,b); Toffoli(control,b,a); CNOT(a,b).
    """
    h = I823.primitive_matrix("endpoint_H")
    t = I823.primitive_matrix("endpoint_T")
    tdg = I823.primitive_matrix("endpoint_Tdg")
    cnot = I823.primitive_matrix("endpoint_CNOT")
    first, second, target = 0, 2, 1
    rows = [
        ("pointer_CNOT_a_to_b:pre", "endpoint_CNOT", cnot, (1, 2)),
        ("pointer_TOF_H", "endpoint_H", h, (target,)),
        ("pointer_TOF_CNOT_second_target_1", "endpoint_CNOT", cnot, (second, target)),
        ("pointer_TOF_Tdg_target_1", "endpoint_Tdg", tdg, (target,)),
        ("pointer_TOF_CNOT_first_target_1", "endpoint_CNOT", cnot, (first, target)),
        ("pointer_TOF_T_target_1", "endpoint_T", t, (target,)),
        ("pointer_TOF_CNOT_second_target_2", "endpoint_CNOT", cnot, (second, target)),
        ("pointer_TOF_Tdg_target_2", "endpoint_Tdg", tdg, (target,)),
        ("pointer_TOF_CNOT_first_target_2", "endpoint_CNOT", cnot, (first, target)),
        ("pointer_TOF_T_second", "endpoint_T", t, (second,)),
        ("pointer_TOF_T_target_2", "endpoint_T", t, (target,)),
        ("pointer_TOF_H_target", "endpoint_H", h, (target,)),
        ("pointer_TOF_CNOT_first_second_1", "endpoint_CNOT", cnot, (first, second)),
        ("pointer_TOF_T_first", "endpoint_T", t, (first,)),
        ("pointer_TOF_Tdg_second", "endpoint_Tdg", tdg, (second,)),
        ("pointer_TOF_CNOT_first_second_2", "endpoint_CNOT", cnot, (first, second)),
        ("pointer_CNOT_a_to_b:post", "endpoint_CNOT", cnot, (1, 2)),
    ]
    if len(rows) != 17:
        raise AssertionError(("neutral Fredkin logical factors", len(rows)))
    return tuple(rows)


NEUTRAL_FREDKIN_FACTORS = neutral_fredkin_logical_specs()


def neutral_fredkin_physical_specs():
    output = []
    swap = R822.primitive_matrix("SWAP")
    for label, opcode, matrix, wires in NEUTRAL_FREDKIN_FACTORS:
        if wires == (0, 2):
            output.extend((
                (f"{label}:route_SWAP_out", "SWAP", swap, (0, 1)),
                (f"{label}:routed_endpoint_CNOT", opcode, matrix, (1, 2)),
                (f"{label}:route_SWAP_return", "SWAP", swap, (0, 1)),
            ))
        else:
            output.append((label, opcode, matrix, wires))
    if len(output) != 21:
        raise AssertionError(("routed neutral Fredkin factors", len(output)))
    return tuple(output)


NEUTRAL_FREDKIN_PHYSICAL_FACTORS = neutral_fredkin_physical_specs()
POINTER_FREDKIN_ROUTES = {}


def compose_opcode_word(word):
    output = np.eye(4, dtype=complex)
    for opcode in word:
        output = R822.primitive_matrix(opcode) @ output
    return output


def actual_atlas_census():
    private = R822.B.P.build_private_atlases()
    context = I823.augment_context(R822.local_site_maps(C.SHAPE, private))
    context, routes, words, *_rest = R822.fixed_typed_compile(context)
    routed_atlas = list(routes)
    before, after = I823.instrument_words(context, routed_atlas)
    all_words = words + before + after
    type_report, actual_charged, actual_neutral = R822.fixed_type_assignment(
        context, tuple(routed_atlas)
    )
    counts = Counter(
        primitive.kind for word in all_words for primitive in word.primitives
    )
    support = {}
    ordered_supports = set()
    unordered_supports = set()
    for word in all_words:
        for primitive in word.primitives:
            ordered_sites = tuple(primitive.sites)
            unordered_sites = (
                tuple(sorted(ordered_sites))
                if len(ordered_sites) == 2 else ordered_sites
            )
            ordered_supports.add((primitive.kind, ordered_sites))
            unordered_supports.add((primitive.kind, unordered_sites))
            type_signature = tuple(
                "charged" if site in actual_charged
                else "neutral" if site in actual_neutral
                else "untyped"
                for site in ordered_sites
            )
            canonical = I823.primitive_matrix(primitive.kind)
            row = support.setdefault(primitive.kind, {
                "occurrences": 0,
                "arities": set(),
                "type_signatures": set(),
                "maximum_two_site_distance": 0,
                "non_NN_two_site_occurrences": 0,
                "exemplar_sites": primitive.sites,
                "canonical_matrix_shape": tuple(canonical.shape),
                "canonical_matrix_sha256": (
                    R822.U720.c707.c655.matrix_digest(canonical)
                ),
            })
            row["occurrences"] += 1
            row["arities"].add(len(primitive.sites))
            row["type_signatures"].add(type_signature)
            if len(primitive.sites) == 2:
                distance = C.l1(*primitive.sites)
                row["maximum_two_site_distance"] = max(
                    row["maximum_two_site_distance"], distance
                )
                row["non_NN_two_site_occurrences"] += distance != 1
    for row in support.values():
        row["arities"] = tuple(sorted(row["arities"]))
        row["type_signatures"] = tuple(sorted(row["type_signatures"]))
    return {
        "atlas_shape": C.SHAPE,
        "counts": counts,
        "support": support,
        "type_report": type_report,
        "actual_charged": actual_charged,
        "actual_neutral": actual_neutral,
        "ordered_supports": frozenset(ordered_supports),
        "unordered_supports": frozenset(unordered_supports),
    }


def ideal_controlled_fswap():
    fswap = R822.primitive_matrix("FSWAP")
    output = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        control = source & 1
        local_source = (source >> 1) & 3
        gate = fswap if control else np.eye(4)
        for local_target in range(4):
            output[(local_target << 1) | control, source] = gate[
                local_target, local_source
            ]
    return output


def charged_exchange_matrix_candidate_certificate(actual_atlas):
    parity = np.diag(tuple(
        (-1) ** (((basis >> 1) & 1) + ((basis >> 2) & 1))
        for basis in range(8)
    )).astype(complex)
    actual = np.eye(8, dtype=complex)
    prefixes = []
    factor_commutators = []
    lifted = []
    for label, opcode, matrix, wires, family in CORE_FACTORS:
        dense = C.lift_matrix(matrix, wires, 3)
        lifted.append(dense)
        factor_commutators.append(float(np.linalg.norm(
            dense @ parity - parity @ dense
        )))
        actual = dense @ actual
        prefixes.append(float(np.linalg.norm(actual @ parity - parity @ actual)))
    target = ideal_controlled_fswap()
    swap = R822.primitive_matrix("SWAP")
    controlled_swap = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        control = source & 1
        local_source = (source >> 1) & 3
        gate = swap if control else np.eye(4)
        for local_target in range(4):
            controlled_swap[(local_target << 1) | control, source] = gate[
                local_target, local_source
            ]
    clean_columns = tuple(source for source in range(8) if ((source >> 1) & 3) != 3)
    dirty_columns = tuple(source for source in range(8) if ((source >> 1) & 3) == 3)
    columns = tuple(float(np.linalg.norm(
        actual[:, source] - target[:, source]
    )) for source in range(8))

    first_two_swapped = np.eye(8, dtype=complex)
    for ordinal in (1, 0, *range(2, len(lifted))):
        first_two_swapped = lifted[ordinal] @ first_two_swapped
    reversed_order = np.eye(8, dtype=complex)
    for dense in reversed(lifted):
        reversed_order = dense @ reversed_order

    w = compose_opcode_word(W_WORD)
    w_dagger = compose_opcode_word(W_DAGGER_WORD)
    z_first = R822.B.dense_pauli(R822.Pauli(z=1), 2)
    fswap = R822.primitive_matrix("FSWAP")
    overlap = np.vdot(w.conj().T, w_dagger)
    relative_phase = overlap / abs(overlap)

    deletions = []
    for deleted in range(len(lifted)):
        damaged = np.eye(8, dtype=complex)
        for ordinal, dense in enumerate(lifted):
            if ordinal != deleted:
                damaged = dense @ damaged
        difference = damaged - target
        per_column = tuple(float(np.linalg.norm(
            difference[:, source]
        )) for source in range(8))
        deletions.append({
            "ordinal": deleted,
            "label": CORE_FACTORS[deleted][0],
            "opcode": CORE_FACTORS[deleted][1],
            "residual": float(np.linalg.norm(difference)),
            "changed_columns": sum(value > 1.0e-8 for value in per_column),
            "minimum_column_residual": min(per_column),
            "maximum_column_residual": max(per_column),
        })

    opcode_counts = Counter(row[1] for row in CORE_FACTORS)
    support = {
        opcode: actual_atlas["support"].get(opcode, {
            "occurrences": 0,
            "arities": (),
            "maximum_two_site_distance": math.inf,
            "non_NN_two_site_occurrences": math.inf,
            "exemplar_sites": (),
        })
        for opcode in opcode_counts
    }
    return {
        "factor_word_application_order": tuple(row[0] for row in CORE_FACTORS),
        "opcode_word_application_order": tuple(row[1] for row in CORE_FACTORS),
        "factor_word_sha256": sha256(repr(tuple(
            row[0] for row in CORE_FACTORS
        )).encode()).hexdigest(),
        "elementary_factors_per_controlled_exchange": len(CORE_FACTORS),
        "per_exchange_opcode_census": dict(sorted(opcode_counts.items())),
        "W_word_application_order": W_WORD,
        "W_dagger_word_application_order": W_DAGGER_WORD,
        "W_dagger_exact_inverse_residual": float(np.linalg.norm(
            w_dagger - w.conj().T
        )),
        "W_dagger_inverse_relative_phase": (
            float(relative_phase.real), float(relative_phase.imag)
        ),
        "W_dagger_Z_first_W_FSWAP_residual": float(np.linalg.norm(
            w_dagger @ z_first @ w - fswap
        )),
        "all_8_column_residuals": columns,
        "maximum_column_residual": max(columns),
        "full_matrix_residual": float(np.linalg.norm(actual - target)),
        "first_two_factor_order_swap_residual": float(np.linalg.norm(
            first_two_swapped - target
        )),
        "reversed_factor_order_residual": float(np.linalg.norm(
            reversed_order - target
        )),
        "cSWAP_clean_domain_residual": float(np.linalg.norm(
            (actual - controlled_swap)[:, clean_columns]
        )),
        "cSWAP_dirty_11_residual": float(np.linalg.norm(
            (actual - controlled_swap)[:, dirty_columns]
        )),
        "unitarity_residual": float(np.linalg.norm(
            actual.conj().T @ actual - np.eye(8)
        )),
        "square_identity_residual": float(np.linalg.norm(
            actual @ actual - np.eye(8)
        )),
        "self_inverse_residual": float(np.linalg.norm(actual.conj().T - actual)),
        "control_return_leakage": max(float(np.linalg.norm(
            actual[
                tuple(row for row in range(8) if (row & 1) != (source & 1)),
                source,
            ]
        )) for source in range(8)),
        "maximum_factor_P_ext_commutator": max(factor_commutators),
        "maximum_prefix_P_ext_commutator": max(prefixes),
        "single_factor_deletions": tuple(deletions),
        "single_factor_deletions_tested": len(deletions),
        "single_factor_deletions_detected": sum(
            row["residual"] > 1.0e-8 for row in deletions
        ),
        "minimum_deletion_residual": min(row["residual"] for row in deletions),
        "actual_atlas_kind_support_examples": support,
        "all_candidate_opcode_kinds_available_somewhere_in_actual_atlas": all(
            row["occurrences"] > 0 for row in support.values()
        ),
        "all_actual_atlas_kind_exemplars_NN_and_onsite_local": all(
            row["non_NN_two_site_occurrences"] == 0
            and set(row["arities"]) <= {1, 2}
            for row in support.values()
        ),
        "literal_FSWAP_sha256": R822.U720.c707.c655.matrix_digest(fswap),
        # Compatibility fields consumed by the original damage reporter.
        "H_dual_fixed_dictionary_match": False,
        "H_dual_requires_supplied_new_local_gate": False,
    }


def neutral_fredkin_matrix_certificate(actual_atlas):
    logical_actual = np.eye(8, dtype=complex)
    for _label, _opcode, matrix, wires in NEUTRAL_FREDKIN_FACTORS:
        dense = C.lift_matrix(matrix, wires, 3)
        logical_actual = dense @ logical_actual
    actual = np.eye(8, dtype=complex)
    lifted = []
    for _label, _opcode, matrix, wires in NEUTRAL_FREDKIN_PHYSICAL_FACTORS:
        dense = C.lift_matrix(matrix, wires, 3)
        lifted.append(dense)
        actual = dense @ actual
    target = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        control = source & 1
        a = (source >> 1) & 1
        b = (source >> 2) & 1
        if control:
            destination = control | (b << 1) | (a << 2)
        else:
            destination = source
        target[destination, source] = 1.0
    columns = tuple(float(np.linalg.norm(
        actual[:, source] - target[:, source]
    )) for source in range(8))
    first_two_swapped = np.eye(8, dtype=complex)
    for ordinal in (1, 0, *range(2, len(lifted))):
        first_two_swapped = lifted[ordinal] @ first_two_swapped
    clean_columns = tuple(
        source for source in range(8) if ((source >> 1) & 3) != 3
    )
    deletions = []
    for deleted in range(len(lifted)):
        damaged = np.eye(8, dtype=complex)
        for ordinal, dense in enumerate(lifted):
            if ordinal != deleted:
                damaged = dense @ damaged
        residual = float(np.linalg.norm(damaged - target))
        clean_residual = float(np.linalg.norm(
            (damaged - target)[:, clean_columns]
        ))
        deletions.append({
            "ordinal": deleted,
            "label": NEUTRAL_FREDKIN_PHYSICAL_FACTORS[deleted][0],
            "opcode": NEUTRAL_FREDKIN_PHYSICAL_FACTORS[deleted][1],
            "residual": residual,
            "clean_pointer_domain_residual": clean_residual,
            "clean_pointer_columns_changed": sum(
                np.linalg.norm(damaged[:, source] - target[:, source])
                > 1.0e-8
                for source in clean_columns
            ),
        })
    opcodes = Counter(row[1] for row in NEUTRAL_FREDKIN_FACTORS)
    physical_opcodes = Counter(
        row[1] for row in NEUTRAL_FREDKIN_PHYSICAL_FACTORS
    )
    support = {
        opcode: actual_atlas["support"].get(opcode, {"occurrences": 0})
        for opcode in physical_opcodes
    }
    neutral_base = max(C.C827.CHARGED_WIRES) + 1
    control_wire, a_wire, b_wire = (
        neutral_base, neutral_base + 1, neutral_base + 2
    )
    semantic_word = (
        H719.A.cn(a_wire, b_wire),
        H719.A.tof(control_wire, b_wire, a_wire),
        H719.A.cn(a_wire, b_wire),
    )
    normalized, normalization_swaps, normalization_failures = C.C827.normalize_word(
        semantic_word
    )
    expanded = tuple(H719.A.expanded(normalized))
    expanded_census = Counter(kind for kind, _wires in expanded)
    parity_violations = sum(
        C.C827.factor_parity_violation(kind, wires)
        for kind, wires in expanded
    )
    prefix_parity = C.C827.prefix_parity_certificate(normalized)
    return {
        "purpose": (
            "all-neutral controlled SWAP on the supplied-clean Cycle823 "
            "pointer corridor; not substituted for charged cFSWAP"
        ),
        "logical_factor_word_application_order": tuple(
            row[0] for row in NEUTRAL_FREDKIN_FACTORS
        ),
        "logical_opcode_census": dict(sorted(opcodes.items())),
        "logical_elementary_factors": len(NEUTRAL_FREDKIN_FACTORS),
        "returned_routed_physical_factor_word": tuple(
            row[0] for row in NEUTRAL_FREDKIN_PHYSICAL_FACTORS
        ),
        "returned_routed_physical_opcode_census": dict(sorted(
            physical_opcodes.items()
        )),
        "returned_routed_physical_factors": len(
            NEUTRAL_FREDKIN_PHYSICAL_FACTORS
        ),
        "Cycle719_semantic_word": tuple(
            (gate.kind, gate.wires) for gate in semantic_word
        ),
        "Cycle719_expanded_factor_census": dict(sorted(expanded_census.items())),
        "Cycle719_expanded_factors": len(expanded),
        "Cycle827_neutral_wire_range": (
            control_wire, a_wire, b_wire
        ),
        "Cycle827_control_normalization_swaps": normalization_swaps,
        "Cycle827_control_normalization_failures": normalization_failures,
        "Cycle827_factor_parity_violations": parity_violations,
        "Cycle827_prefix_parity": prefix_parity,
        "all_8_cSWAP_column_residuals": columns,
        "maximum_cSWAP_column_residual": max(columns),
        "full_matrix_residual": float(np.linalg.norm(actual - target)),
        "first_two_factor_order_swap_residual": float(np.linalg.norm(
            first_two_swapped - target
        )),
        "logical_vs_returned_routed_matrix_residual": float(np.linalg.norm(
            logical_actual - actual
        )),
        "unitarity_residual": float(np.linalg.norm(
            actual.conj().T @ actual - np.eye(8)
        )),
        "square_identity_residual": float(np.linalg.norm(
            actual @ actual - np.eye(8)
        )),
        "physical_single_factor_deletions": tuple(deletions),
        "physical_single_factor_deletions_tested": len(deletions),
        "physical_single_factor_deletions_detected": sum(
            row["residual"] > 1.0e-8 for row in deletions
        ),
        "minimum_physical_deletion_residual": min(
            row["residual"] for row in deletions
        ),
        "clean_pointer_domain_columns": clean_columns,
        "physical_single_factor_clean_domain_deletions_detected": sum(
            row["clean_pointer_domain_residual"] > 1.0e-8
            for row in deletions
        ),
        "minimum_physical_clean_domain_deletion_residual": min(
            row["clean_pointer_domain_residual"] for row in deletions
        ),
        "actual_atlas_kind_support_examples": support,
        "all_candidate_opcode_kinds_available_somewhere_in_actual_atlas": all(
            row["occurrences"] > 0 for row in support.values()
        ),
        "clean_pointer_premise": (
            "the Route-C pointer corridor has at most one pointer occupation; "
            "cSWAP and cFSWAP therefore agree on its admitted domain"
        ),
        "dirty_11_FSWAP_equivalence_claimed": False,
    }


def apply_local_unitary(state, matrix, wires):
    output = defaultdict(complex)
    for basis, amplitude in state.items():
        local_source = sum(
            ((basis >> wire) & 1) << index for index, wire in enumerate(wires)
        )
        for local_target in range(1 << len(wires)):
            coefficient = matrix[local_target, local_source]
            if abs(coefficient) < 1.0e-15:
                continue
            target = basis
            for index, wire in enumerate(wires):
                target = (
                    (target & ~(1 << wire))
                    | (((local_target >> index) & 1) << wire)
                )
            output[target] += coefficient * amplitude
    return C.clean_state(output)


def apply_charged_exchange_matrix_candidate(
    state, control, first, second, *, delete_factor=None,
):
    physical = (control, first, second)
    for ordinal, (_label, _opcode, matrix, logical_wires, _family) in enumerate(
        CORE_FACTORS
    ):
        if ordinal == delete_factor:
            continue
        wires = tuple(physical[wire] for wire in logical_wires)
        state = apply_local_unitary(state, matrix, wires)
    return state


def build_pointer_fredkin_routes(geometry, taxi):
    routes = {}
    failures = Counter()
    for key, taxi_path in taxi["paths"].items():
        _station, path_index, pair = key
        if path_index != 2:
            continue
        control = taxi_path[-1]
        a = pair[1]
        b = pair[0]
        # c-a-b is already a two-edge neutral path.  The only non-NN logical
        # CNOT in the Fredkin decomposition is routed c->b by SWAP(c,a),
        # CNOT(a,b), SWAP(c,a), returning the a label before the next factor.
        route = (control, a, b)
        failures["route_structure"] += not C.path_ok(route)
        failures["charged_coordinate_hits"] += len(
            set(route) & set(geometry["charged"])
        )
        failures["service_coordinate_hits"] += len(
            set(route) & set(geometry["service_sites"])
        )
        failures["neutral_membership"] += sum(
            site not in taxi["neutral"] for site in route
        )
        routes[key] = route
    return routes, dict(sorted(failures.items()))


def apply_neutral_fredkin(
    state, control, a, b, route, *, delete_factor=None,
):
    physical = (control, a, b)
    if tuple(route) != physical:
        raise AssertionError(("pointer Fredkin route bind", route, physical))
    for ordinal, (_label, _opcode, matrix, logical_wires) in enumerate(
        NEUTRAL_FREDKIN_PHYSICAL_FACTORS
    ):
        if ordinal == delete_factor:
            continue
        wires = tuple(physical[wire] for wire in logical_wires)
        state = apply_local_unitary(state, matrix, wires)
    return state


def substituted_taxi_exchange(
    state, taxi_path, pair, site_bits, *, omit_core=False,
    omit_last_return=False, delete_core_factor=None,
    pointer_fredkin_route=None, delete_pointer_factor=None,
):
    for left, right in zip(taxi_path, taxi_path[1:]):
        state = C.apply_swap(state, site_bits[left], site_bits[right])
    if not omit_core:
        if pointer_fredkin_route is None:
            # The taxi terminal is adjacent to pair[1], so pair[1] is the
            # charged control endpoint of the candidate endpoint_CNOT core.
            state = apply_charged_exchange_matrix_candidate(
                state,
                site_bits[taxi_path[-1]],
                site_bits[pair[1]],
                site_bits[pair[0]],
                delete_factor=delete_core_factor,
            )
        else:
            state = apply_neutral_fredkin(
                state,
                site_bits[taxi_path[-1]],
                site_bits[pair[1]],
                site_bits[pair[0]],
                tuple(site_bits[site] for site in pointer_fredkin_route),
                delete_factor=delete_pointer_factor,
            )
    reverse_edges = tuple(reversed(tuple(zip(taxi_path, taxi_path[1:]))))
    if omit_last_return:
        reverse_edges = reverse_edges[:-1]
    for left, right in reverse_edges:
        state = C.apply_swap(state, site_bits[left], site_bits[right])
    return state


def substituted_conditional_route(
    state, station, path_index, path, taxi, site_bits,
    *, runtime=None, damage=None,
):
    runtime = {} if runtime is None else runtime
    for ordinal, pair in enumerate(C.route_sequence(path)):
        key = (station, path_index, pair)
        omit_core = False
        omit_return = False
        delete_factor = None
        delete_pointer_factor = None
        enable_bit = site_bits[C.SERVICE[f"E{station}"]]
        active = any((basis >> enable_bit) & 1 for basis in state)
        if damage == "pointer_adapter_factor" and not runtime.get(
            "pointer_adapter_factor"
        ):
            if active and station == 1 and path_index == 2 and ordinal == 0:
                omit_core = True
                runtime["pointer_adapter_factor"] = True
        if damage == "taxi_return" and not runtime.get("taxi_return"):
            if active and station == 0 and path_index == 0 and ordinal == 0:
                omit_return = True
                runtime["taxi_return"] = True
        if (
            isinstance(damage, tuple)
            and len(damage) == 2
            and damage[0] == "charged_matrix_candidate_factor"
            and not runtime.get("charged_matrix_candidate_factor")
            and active and station == 0 and path_index == 0 and ordinal == 0
        ):
            delete_factor = int(damage[1])
            runtime["charged_matrix_candidate_factor"] = True
        if (
            isinstance(damage, tuple)
            and len(damage) == 2
            and damage[0] == "neutral_fredkin_factor"
            and not runtime.get("neutral_fredkin_factor")
            and active and station == 0 and path_index == 2 and ordinal == 0
        ):
            delete_pointer_factor = int(damage[1])
            runtime["neutral_fredkin_factor"] = True
        state = substituted_taxi_exchange(
            state, taxi["paths"][key], pair, site_bits,
            omit_core=omit_core,
            omit_last_return=omit_return,
            delete_core_factor=delete_factor,
            pointer_fredkin_route=(
                POINTER_FREDKIN_ROUTES[key] if path_index == 2 else None
            ),
            delete_pointer_factor=delete_pointer_factor,
        )
    return state


# Patch the actual construction's late-bound globals.  Its station, Q, rail,
# orbit, lawful, and damage functions otherwise remain byte-for-byte actual.
C.apply_taxi_exchange = substituted_taxi_exchange
C.apply_conditional_route = substituted_conditional_route


def declared_forward_occurrence_sequence(geometry):
    """Exact keyed conditional-route chronology of one supplied Q block."""
    rows = []
    for station in (0, 1):
        paths = geometry["station_paths"][station]
        for path_index in (0, 1, 2, 1, 0):
            rows.extend(
                (station, path_index, pair)
                for pair in C.route_sequence(paths[path_index])
            )
    return tuple(rows)


def factor_dictionary_rows():
    def row(specification):
        label, opcode, matrix, logical_wires = specification[:4]
        return {
            "label": label,
            "opcode": opcode,
            "logical_wires": logical_wires,
            "matrix_shape": tuple(matrix.shape),
            "matrix_sha256": R822.U720.c707.c655.matrix_digest(matrix),
        }

    return {
        "charged_11": tuple(row(specification) for specification in CORE_FACTORS),
        "neutral_pointer_21": tuple(
            row(specification)
            for specification in NEUTRAL_FREDKIN_PHYSICAL_FACTORS
        ),
    }


def candidate_site_type(site, charged, neutral):
    in_charged = site in charged
    in_neutral = site in neutral
    if in_charged and in_neutral:
        return "overlap"
    if in_charged:
        return "charged"
    if in_neutral:
        return "neutral"
    return "untyped"


def validate_candidate_factor(record, actual_atlas, charged, neutral):
    """Authenticate one candidate occurrence without granting relocation."""
    failures = Counter()
    opcode = record["opcode"]
    matrix = record["matrix"]
    logical_wires = tuple(record["logical_wires"])
    sites = tuple(record["sites"])
    physical = tuple(record["physical_triple"])
    support = actual_atlas["support"].get(opcode)

    failures["opcode_kind_absent_from_actual_dictionary_or_instrument"] += (
        support is None
    )
    canonical = None
    try:
        canonical = I823.primitive_matrix(opcode)
    except (KeyError, ValueError):
        failures["canonical_imported_matrix_missing"] += 1

    wire_arity = len(logical_wires)
    site_arity = len(sites)
    failures["declared_wire_site_arity_mismatch"] += wire_arity != site_arity
    expected_dimension = 1 << wire_arity
    failures["matrix_dimension_vs_declared_wire_arity"] += tuple(matrix.shape) != (
        expected_dimension, expected_dimension
    )
    site_dimension = 1 << site_arity
    failures["matrix_dimension_vs_physical_site_arity"] += tuple(matrix.shape) != (
        site_dimension, site_dimension
    )
    expected_sites = tuple(physical[wire] for wire in logical_wires)
    failures["physical_sites_vs_declared_wires"] += sites != expected_sites
    failures["repeated_physical_site"] += len(sites) != len(set(sites))
    failures["unsupported_factor_arity"] += site_arity not in (1, 2)
    failures["one_site_not_onsite"] += site_arity == 1 and len(sites) != 1
    failures["two_site_not_nearest_neighbour"] += (
        site_arity == 2 and C.l1(*sites) != 1
    )

    type_signature = tuple(
        candidate_site_type(site, charged, neutral) for site in sites
    )
    failures["candidate_palette_untyped_or_overlapped"] += any(
        kind not in ("charged", "neutral") for kind in type_signature
    )
    if support is not None:
        failures["opcode_arity_absent_from_actual_support"] += (
            site_arity not in support["arities"]
        )
        failures["opcode_type_signature_absent_from_actual_support"] += (
            type_signature not in support["type_signatures"]
        )
    if canonical is not None:
        same_shape = tuple(matrix.shape) == tuple(canonical.shape)
        failures["factor_matrix_shape_vs_canonical_opcode"] += not same_shape
        failures["factor_matrix_not_exact_canonical_opcode"] += (
            not same_shape or not np.array_equal(matrix, canonical)
        )
    return dict(sorted(failures.items()))


def failure_total(failures):
    return sum(int(value) for value in failures.values())


def support_key(opcode, sites, *, unordered=False):
    sites = tuple(sites)
    if unordered and len(sites) == 2:
        sites = tuple(sorted(sites))
    return opcode, sites


def candidate_factor_trace_certificate(geometry, taxi, actual_atlas):
    candidate_charged = frozenset(geometry["charged"])
    candidate_neutral = frozenset(taxi["neutral"])
    per_q_sequence = declared_forward_occurrence_sequence(geometry)
    expected_counter = Counter(per_q_sequence)
    atlas_counter = Counter(taxi["occurrence_per_Q"])
    keyed_counter_difference = sum(
        abs(expected_counter[key] - atlas_counter[key])
        for key in set(expected_counter) | set(atlas_counter)
    )

    occurrence_blocks = []
    expanded_digest_rows = []
    validation_failures = Counter()
    charged_ordered = set()
    pointer_ordered = set()
    charged_unordered = set()
    pointer_unordered = set()
    factor_slot = 0
    first_record = None
    for application_slot in range(2):
        for occurrence_in_q, key in enumerate(per_q_sequence):
            station, path_index, pair = key
            taxi_path = taxi["paths"][key]
            physical = (taxi_path[-1], pair[1], pair[0])
            if path_index < 2:
                dictionary_name = "charged_11"
                specifications = CORE_FACTORS
                ordered_set = charged_ordered
                unordered_set = charged_unordered
            else:
                dictionary_name = "neutral_pointer_21"
                specifications = NEUTRAL_FREDKIN_PHYSICAL_FACTORS
                ordered_set = pointer_ordered
                unordered_set = pointer_unordered
            occurrence_blocks.append({
                "serial_occurrence_slot": len(occurrence_blocks),
                "service_application_slot": application_slot,
                "occurrence_slot_within_Q": occurrence_in_q,
                "station_block_slot": station,
                "path_index": path_index,
                "route_pair": pair,
                "candidate_physical_triple": physical,
                "factor_dictionary": dictionary_name,
                "first_serial_factor_slot": factor_slot,
                "serial_factor_slots": len(specifications),
            })
            for factor_ordinal, specification in enumerate(specifications):
                label, opcode, matrix, logical_wires = specification[:4]
                sites = tuple(physical[wire] for wire in logical_wires)
                record = {
                    "label": label,
                    "opcode": opcode,
                    "matrix": matrix,
                    "logical_wires": logical_wires,
                    "sites": sites,
                    "physical_triple": physical,
                }
                if first_record is None:
                    first_record = record
                for name, value in validate_candidate_factor(
                    record, actual_atlas, candidate_charged, candidate_neutral
                ).items():
                    validation_failures[name] += value
                ordered_set.add(support_key(opcode, sites))
                unordered_set.add(support_key(opcode, sites, unordered=True))
                expanded_digest_rows.append((
                    factor_slot,
                    application_slot,
                    occurrence_in_q,
                    factor_ordinal,
                    opcode,
                    sites,
                    R822.U720.c707.c655.matrix_digest(matrix),
                ))
                factor_slot += 1

    selected_ordered = charged_ordered | pointer_ordered
    selected_unordered = charged_unordered | pointer_unordered
    actual_ordered = actual_atlas["ordered_supports"]
    actual_unordered = actual_atlas["unordered_supports"]

    actual_charged = actual_atlas["actual_charged"]
    actual_neutral = actual_atlas["actual_neutral"]
    charged_absent = candidate_charged - actual_charged
    neutral_absent = candidate_neutral - actual_neutral
    charged_opposite = candidate_charged & actual_neutral
    neutral_opposite = candidate_neutral & actual_charged

    hostile = {}
    if first_record is None:
        hostile["missing_seed_record"] = True
    else:
        relabelled = dict(first_record)
        relabelled["opcode"] = "endpoint_H"
        hostile["opcode_relabel_failure_census"] = validate_candidate_factor(
            relabelled, actual_atlas, candidate_charged, candidate_neutral
        )
        arity_mutated = dict(first_record)
        arity_mutated["logical_wires"] = first_record["logical_wires"][:1]
        hostile["declared_arity_failure_census"] = validate_candidate_factor(
            arity_mutated, actual_atlas, candidate_charged, candidate_neutral
        )
        matrix_mutated = dict(first_record)
        changed_matrix = np.array(first_record["matrix"], copy=True)
        changed_matrix[0, 0] += 0.125
        matrix_mutated["matrix"] = changed_matrix
        hostile["matrix_mutation_failure_census"] = validate_candidate_factor(
            matrix_mutated, actual_atlas, candidate_charged, candidate_neutral
        )
        hostile["opcode_relabel_detected"] = failure_total(
            hostile["opcode_relabel_failure_census"]
        ) > 0
        hostile["declared_arity_mutation_detected"] = failure_total(
            hostile["declared_arity_failure_census"]
        ) > 0
        hostile["matrix_mutation_detected"] = failure_total(
            hostile["matrix_mutation_failure_census"]
        ) > 0

    four_count_keys = tuple(sorted(
        (key for key, count in expected_counter.items()
         if key[1] < 2 and count == 4),
        key=repr,
    ))
    count_mutation = {
        "candidate_keys_with_count_four": len(four_count_keys),
        "detected": False,
    }
    if len(four_count_keys) >= 2:
        receiver, donor = four_count_keys[:2]
        mutated_sequence = list(per_q_sequence)
        mutated_sequence[mutated_sequence.index(donor)] = receiver
        mutated_counter = Counter(mutated_sequence)
        mutation_difference = sum(
            abs(mutated_counter[key] - atlas_counter[key])
            for key in set(mutated_counter) | set(atlas_counter)
        )
        count_mutation.update({
            "same_total_occurrences": len(mutated_sequence) == len(per_q_sequence),
            "receiver_key": repr(receiver),
            "donor_key": repr(donor),
            "receiver_before_after": (
                expected_counter[receiver], mutated_counter[receiver]
            ),
            "donor_before_after": (
                expected_counter[donor], mutated_counter[donor]
            ),
            "keyed_counter_difference": mutation_difference,
            "sequence_changed": tuple(mutated_sequence) != per_q_sequence,
            "detected": (
                mutation_difference > 0
                and tuple(mutated_sequence) != per_q_sequence
                and len(mutated_sequence) == len(per_q_sequence)
            ),
        })

    adverse = {
        "actual_atlas_shape": actual_atlas["atlas_shape"],
        "selected_ordered_opcode_site_supports": len(selected_ordered),
        "actual_ordered_support_matches": len(selected_ordered & actual_ordered),
        "selected_unique_unordered_opcode_site_supports": len(selected_unordered),
        "actual_unordered_support_matches": len(
            selected_unordered & actual_unordered
        ),
        "charged_candidate_ordered_supports": len(charged_ordered),
        "charged_actual_ordered_support_matches": len(
            charged_ordered & actual_ordered
        ),
        "pointer_candidate_ordered_supports": len(pointer_ordered),
        "pointer_actual_ordered_support_matches": len(
            pointer_ordered & actual_ordered
        ),
        "selected_charged_coordinates": len(candidate_charged),
        "selected_charged_absent_from_actual_atlas": len(charged_absent),
        "selected_charged_opposite_typed_in_actual_atlas": len(charged_opposite),
        "selected_neutral_coordinates": len(candidate_neutral),
        "selected_neutral_absent_from_actual_atlas": len(neutral_absent),
        "selected_neutral_opposite_typed_in_actual_atlas": len(neutral_opposite),
        "actual_coordinate_support_or_palette_mismatches_nonzero": all((
            len(selected_ordered - actual_ordered) > 0,
            len(charged_absent) > 0,
            len(neutral_absent) > 0,
        )),
        "gating_role": (
            "adverse boundary: exact actual-atlas support is not granted; "
            "the candidate requires generic local opcode availability and "
            "an explicitly supplied retyped selected palette"
        ),
    }
    return {
        "trace_scope": (
            "the 20,636 controlled-exchange matrix factors only; taxi, guard, "
            "rail, and imported Cycle719 factors retain their own certificates"
        ),
        "factor_dictionaries": factor_dictionary_rows(),
        "replayable_supplied_occurrence_blocks": tuple(occurrence_blocks),
        "occurrences_per_Q": len(per_q_sequence),
        "two_application_occurrences": len(occurrence_blocks),
        "full_expected_keyed_occurrence_counter_entries": len(expected_counter),
        "full_expected_keyed_occurrence_counter_sha256": sha256(
            repr(tuple(sorted(expected_counter.items(), key=lambda row: repr(row[0])))).encode()
        ).hexdigest(),
        "full_expected_occurrence_sequence_sha256": sha256(
            repr(per_q_sequence).encode()
        ).hexdigest(),
        "keyed_occurrence_counter_difference_from_taxi_atlas": (
            keyed_counter_difference
        ),
        "expanded_candidate_factor_occurrences": factor_slot,
        "expanded_candidate_factor_trace_sha256": sha256(
            repr(tuple(expanded_digest_rows)).encode()
        ).hexdigest(),
        "candidate_factor_validation_failures": dict(sorted(
            validation_failures.items()
        )),
        "candidate_factor_validation_failure_total": sum(
            validation_failures.values()
        ),
        "hostile_factor_mutations": hostile,
        "hostile_same_total_5_3_occurrence_mutation": count_mutation,
        "actual_atlas_adverse_boundary": adverse,
        "generic_local_opcode_availability_supplied": True,
        "selected_palette_retyping_supplied": True,
        "actual_coordinate_opcode_site_support_claimed": False,
        "actual_atlas_palette_reused_claimed": False,
        "supplied_singleton_serial_factor_slots": factor_slot,
        "maximum_factors_per_supplied_serial_slot": 1,
        "parallel_factor_pairs_scheduled": 0,
        "parallel_collision_or_recolouring_claimed": False,
    }


def taxi_and_serial_certificate(
    geometry, taxi, matrix_report, fredkin_report, pointer_routes,
):
    rows = []
    failures = Counter()
    counterfactual = Counter()
    terminal_counts = Counter()
    occurrence_sequence = declared_forward_occurrence_sequence(geometry)

    for key, taxi_path in taxi["paths"].items():
        station, path_index, pair = key
        control = taxi_path[-1]
        first, second = pair[1], pair[0]
        terminal_counts[control] += 1
        failures["taxi_path_structure"] += not C.path_ok(taxi_path)
        failures["target_pair_not_NN"] += C.l1(first, second) != 1
        failures["control_not_adjacent_to_oriented_first"] += C.l1(control, first) != 1
        failures["local_triple_not_distinct"] += len({control, first, second}) != 3
        failures["control_on_charged_palette"] += control in geometry["charged"]
        failures["terminal_on_service_register"] += control in geometry["service_sites"]
        failures["taxi_internal_charged_hits"] += len(
            set(taxi_path[1:]) & set(geometry["charged"])
        )
        factor_nonlocal = factor_type = 0
        physical = (control, first, second)
        if path_index < 2:
            failures["charged_target_missing"] += (
                first not in geometry["charged"] or second not in geometry["charged"]
            )
            for _label, _opcode, _matrix, logical_wires, _family in CORE_FACTORS:
                sites = tuple(physical[wire] for wire in logical_wires)
                factor_nonlocal += len(sites) == 2 and C.l1(*sites) != 1
                if logical_wires == (1, 2):
                    factor_type += any(
                        site not in geometry["charged"] for site in sites
                    )
                elif logical_wires == (1, 0):
                    factor_type += not (
                        sites[0] in geometry["charged"]
                        and sites[1] in taxi["neutral"]
                    )
                elif logical_wires == (0,):
                    factor_type += sites[0] not in taxi["neutral"]
        else:
            # Applying the charged eleven-factor word here is the rejected
            # recolouring: eight charged-pair factors plus its charged-control
            # CNOT are mistyped at every unique pointer pair.
            counterfactual["charged_word_pointer_target_pairs"] += 1
            counterfactual["charged_pair_factor_type_mismatches"] += 8
            counterfactual["charged_control_CNOT_type_mismatches"] += 1
            failures["pointer_targets_not_neutral"] += (
                first not in taxi["neutral"] or second not in taxi["neutral"]
            )
            route = pointer_routes.get(key, ())
            failures["pointer_Fredkin_route_missing"] += not route
            if route:
                failures["pointer_Fredkin_route_structure"] += not C.path_ok(route)
                failures["pointer_Fredkin_route_bind"] += tuple(route) != physical
                failures["pointer_Fredkin_route_charged_hits"] += len(
                    set(route) & set(geometry["charged"])
                )
            for _label, _opcode, _matrix, logical_wires in (
                NEUTRAL_FREDKIN_PHYSICAL_FACTORS
            ):
                sites = tuple(physical[wire] for wire in logical_wires)
                factor_nonlocal += len(sites) == 2 and C.l1(*sites) != 1
                factor_type += any(site not in taxi["neutral"] for site in sites)
        failures["factor_nonlocal"] += factor_nonlocal
        failures["factor_type_mismatch"] += factor_type
        rows.append({
            "key": repr(key),
            "station": station,
            "path_index": path_index,
            "control_terminal": control,
            "oriented_charged_first": first,
            "oriented_charged_second": second,
            "taxi_distance": len(taxi_path) - 1,
        })

    charged_per_q = sum(
        frequency for key, frequency in taxi["occurrence_per_Q"].items()
        if key[1] < 2
    )
    pointer_per_q = sum(
        frequency for key, frequency in taxi["occurrence_per_Q"].items()
        if key[1] == 2
    )
    per_q = charged_per_q + pointer_per_q
    occurrence_counter = Counter(occurrence_sequence)
    atlas_counter = Counter(taxi["occurrence_per_Q"])
    keyed_occurrence_counter_difference = sum(
        abs(occurrence_counter[key] - atlas_counter[key])
        for key in set(occurrence_counter) | set(atlas_counter)
    )
    sequence_failures = (
        len(occurrence_sequence) != per_q
        or keyed_occurrence_counter_difference != 0
    )
    # The candidate supplies a singleton serial slot for every core factor.
    # These ordinals assert no parallel placement and prove no colouring fact.
    supplied_serial_slots = 2 * (
        charged_per_q * len(CORE_FACTORS)
        + pointer_per_q * len(NEUTRAL_FREDKIN_PHYSICAL_FACTORS)
    )
    taxi_return_failures = 0
    for path in taxi["paths"].values():
        labels = list(path)
        for index in range(len(path) - 1):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        for index in reversed(range(len(path) - 1)):
            labels[index], labels[index + 1] = labels[index + 1], labels[index]
        taxi_return_failures += labels != list(path)
    return {
        "unique_control_target_taxis": len(rows),
        "conditional_exchange_occurrences_per_Q": per_q,
        "conditional_exchange_occurrences_two_word_orbit": 2 * per_q,
        "charged_endpoint_exchange_occurrences_per_Q": charged_per_q,
        "charged_endpoint_exchange_occurrences_two_word_orbit": 2 * charged_per_q,
        "neutral_pointer_exchange_occurrences_per_Q": pointer_per_q,
        "neutral_pointer_exchange_occurrences_two_word_orbit": 2 * pointer_per_q,
        "charged_orientation": (
            "neutral taxi terminal is logical control; pair[1] is candidate-CNOT "
            "charged first; pair[0] is charged second"
        ),
        "pointer_orientation": (
            "all three wires neutral; pair[1]=Fredkin b/Toffoli target, "
            "pair[0]=Fredkin c/Toffoli second control"
        ),
        "failure_census": dict(sorted(failures.items())),
        "all_local_placement_failures": sum(failures.values()),
        "rejected_charged_word_on_neutral_pointer_census": dict(sorted(
            counterfactual.items()
        )),
        "occurrence_sequence_census_failure": int(sequence_failures),
        "keyed_occurrence_counter_difference_from_taxi_atlas": (
            keyed_occurrence_counter_difference
        ),
        "declared_occurrence_sequence_sha256": sha256(
            repr(occurrence_sequence).encode()
        ).hexdigest(),
        "taxi_terminal_coordinates_reused_serially": sum(
            count > 1 for count in terminal_counts.values()
        ),
        "same_type_serial_reuse_assessed_under_supplied_order_only": True,
        "charged_factor_slots_per_exchange": len(CORE_FACTORS),
        "pointer_factor_slots_per_exchange": len(
            NEUTRAL_FREDKIN_PHYSICAL_FACTORS
        ),
        "supplied_singleton_serial_factor_slots": supplied_serial_slots,
        "maximum_factors_per_supplied_serial_slot": 1,
        "parallel_factor_pairs_scheduled": 0,
        "parallel_collision_or_recolouring_claimed": False,
        "taxi_return_label_failures": taxi_return_failures,
        "charged_matrix_candidate_control_return_leakage": matrix_report[
            "control_return_leakage"
        ],
        "neutral_Fredkin_matrix_residual": fredkin_report[
            "full_matrix_residual"
        ],
        "sample_local_bindings": tuple(rows[:8]),
    }


def augmented_covariance_and_held(geometry, taxi, taxi_report):
    report = C.covariance_and_held_certificate(geometry, taxi)
    frames = tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in R822.B.V.T.proper_cubic_frames()
    )
    triples = tuple(
        (path[-1], key[2][1], key[2][0])
        for key, path in taxi["paths"].items()
    )
    frame_locality = frame_distinct = 0
    for frame in frames:
        for control, first, second in triples:
            moved = tuple(C.matvec(frame, site) for site in (control, first, second))
            frame_locality += C.l1(moved[0], moved[1]) != 1
            frame_locality += C.l1(moved[1], moved[2]) != 1
            frame_distinct += len(set(moved)) != 3
    product_coordinate = product_locality = 0
    for left in frames:
        for right in frames:
            combined = C.matmul(left, right)
            for triple in triples:
                sequential = tuple(
                    C.matvec(left, C.matvec(right, site)) for site in triple
                )
                direct = tuple(C.matvec(combined, site) for site in triple)
                product_coordinate += sequential != direct
                product_locality += C.l1(direct[0], direct[1]) != 1
                product_locality += C.l1(direct[1], direct[2]) != 1

    held_shift = report["held_embedding_shift"]
    held_triples = tuple(tuple(C.add(site, held_shift) for site in triple) for triple in triples)
    held_locality = sum(
        C.l1(control, first) != 1 or C.l1(first, second) != 1
        for control, first, second in held_triples
    )
    held_charged = {C.add(site, held_shift) for site in geometry["charged"]}
    held_neutral = {C.add(site, held_shift) for site in taxi["neutral"]}
    report.update({
        "matrix_candidate_local_triples": len(triples),
        "matrix_candidate_24_frame_locality_failures": frame_locality,
        "matrix_candidate_24_frame_distinctness_failures": frame_distinct,
        "matrix_candidate_576_product_coordinate_failures": product_coordinate,
        "matrix_candidate_576_product_locality_failures": product_locality,
        "held_matrix_candidate_locality_failures": held_locality,
        "held_shifted_charged_neutral_overlap": len(held_charged & held_neutral),
        "held_supplied_singleton_serial_factor_slots": taxi_report[
            "supplied_singleton_serial_factor_slots"
        ],
        "covariance_role": (
            "passive transport of the supplied finite candidate program; "
            "not an intrinsic placement, colouring, or recurrence law"
        ),
    })
    return report


def full_lawful_service_certificate(geometry, taxi, site_bits):
    """Run the full lawful/cleanup/inverse suite from both token offsets."""
    rows = []
    history_failures = endpoint_failures = pointer_failures = 0
    target_failures = service_failures = controller_return_failures = 0
    phase_failures = inverse_failures = 0
    outputs_a0 = {}
    outputs_a1 = {}
    for endpoint_bits in product((0, 1), repeat=4):
        for start_station, outputs in ((0, outputs_a0), (1, outputs_a1)):
            initial = C.initial_state(
                geometry, site_bits, endpoint_bits,
                service_tokens=(start_station,),
            )
            observed = C.service_orbit(initial, geometry, taxi, site_bits)
            basis = C.singleton_basis(observed)
            amplitude = observed[basis]
            surface = C.surface_rows(basis, geometry, site_bits)
            order = (0, 1) if start_station == 0 else (1, 0)
            expected = C.expected_history(endpoint_bits, order)
            history_failures += surface["history"] != expected
            endpoint_failures += surface["endpoints"] != endpoint_bits
            pointer_failures += surface["source_pointers"] != (0, 0)
            target_failures += surface["target_port_bits"] != (0, 0, 0)
            service_failures += surface["service"] != C.expected_service_register(
                (start_station,)
            )
            controller_return_failures += not (
                surface["controller_A_positions"] == (0,)
                and surface["controller_B_weight"] == 0
                and surface["controller_work_weight"] == 0
            )
            phase_failures += abs(amplitude - 1.0) > TOL
            restored = C.service_orbit(
                observed, geometry, taxi, site_bits, reverse=True
            )
            residual = C.state_residual(initial, restored)
            inverse_failures += residual > TOL
            outputs[endpoint_bits] = observed
            rows.append({
                "service_start_station": start_station,
                "endpoint_bits": endpoint_bits,
                "expected_history": expected,
                "observed_history": surface["history"],
                "inverse_residual": residual,
            })

    order_sensitive_cases = sum(
        C.expected_history(endpoint_bits, (0, 1))
        != C.expected_history(endpoint_bits, (1, 0))
        for endpoint_bits in outputs_a0
    )
    order_output_differences = sum(
        C.state_residual(outputs_a0[endpoint_bits], outputs_a1[endpoint_bits])
        > TOL
        for endpoint_bits in outputs_a0
    )
    decoded_order_differences = sum(
        C.decode_history(C.singleton_basis(outputs_a0[endpoint_bits]))
        != C.decode_history(C.singleton_basis(outputs_a1[endpoint_bits]))
        for endpoint_bits in outputs_a0
    )
    return {
        "lawful_A0_endpoint_rows": 16,
        "lawful_A1_offset_rows": 16,
        "full_check_rows_by_start_station": {"A0": 16, "A1": 16},
        "history_failures": history_failures,
        "endpoint_return_failures": endpoint_failures,
        "source_pointer_cleanup_failures": pointer_failures,
        "controller_target_cleanup_failures": target_failures,
        "service_register_return_failures": service_failures,
        "Cycle719_internal_register_return_failures": controller_return_failures,
        "unexpected_phase_failures": phase_failures,
        "forward_inverse_failures": inverse_failures,
        "order_sensitive_endpoint_cases": order_sensitive_cases,
        "decoded_history_order_differences": decoded_order_differences,
        "whole_state_A0_vs_A1_differences": order_output_differences,
        "maximum_forward_inverse_residual": max(
            row["inverse_residual"] for row in rows
        ),
        "sample_rows": tuple(rows),
    }


def augmented_sector_and_damage(geometry, taxi, site_bits):
    report = C.sector_and_damage_certificate(geometry, taxi, site_bits)
    report.pop("deleted_H_dual_CZ_H_dual_middle_factor_residual", None)
    endpoint_bits = (1, 0, 0, 1)
    initial = C.initial_state(geometry, site_bits, endpoint_bits)
    lawful = C.service_orbit(initial, geometry, taxi, site_bits)
    rows = []
    for ordinal, factor in enumerate(CORE_FACTORS):
        damaged = C.service_orbit(
            initial, geometry, taxi, site_bits,
            damage=("charged_matrix_candidate_factor", ordinal),
        )
        rows.append({
            "ordinal": ordinal,
            "label": factor[0],
            "opcode": factor[1],
            "whole_service_residual": C.state_residual(damaged, lawful),
        })
    pointer_rows = []
    for ordinal, factor in enumerate(NEUTRAL_FREDKIN_PHYSICAL_FACTORS):
        damaged = C.service_orbit(
            initial, geometry, taxi, site_bits,
            damage=("neutral_fredkin_factor", ordinal),
        )
        pointer_rows.append({
            "ordinal": ordinal,
            "label": factor[0],
            "opcode": factor[1],
            "whole_service_residual": C.state_residual(damaged, lawful),
        })
    report.update({
        "deleted_charged_matrix_candidate_factor_rows": tuple(rows),
        "deleted_charged_matrix_candidate_factors_tested": len(rows),
        "deleted_charged_matrix_candidate_factors_detected": sum(
            row["whole_service_residual"] > TOL for row in rows
        ),
        "minimum_deleted_charged_matrix_candidate_whole_service_residual": min(
            row["whole_service_residual"] for row in rows
        ),
        "deleted_pointer_Fredkin_factor_rows": tuple(pointer_rows),
        "deleted_pointer_Fredkin_single_service_seed_endpoint_bits": endpoint_bits,
        "deleted_pointer_Fredkin_factors_tested": len(pointer_rows),
        "deleted_pointer_Fredkin_factors_detected": sum(
            row["whole_service_residual"] > TOL for row in pointer_rows
        ),
        "deleted_pointer_Fredkin_single_service_seed_complete_coverage_claimed": False,
        "minimum_deleted_pointer_Fredkin_whole_service_residual": min(
            row["whole_service_residual"] for row in pointer_rows
        ),
    })
    return report


def elementary_factor_census(
    geometry_report, taxi_report, guard_report, controller_report,
):
    core_occurrences = taxi_report[
        "charged_endpoint_exchange_occurrences_two_word_orbit"
    ]
    pointer_occurrences = taxi_report[
        "neutral_pointer_exchange_occurrences_two_word_orbit"
    ]
    core_per_exchange = Counter(row[1] for row in CORE_FACTORS)
    core_orbit = {
        opcode: count * core_occurrences
        for opcode, count in sorted(core_per_exchange.items())
    }
    pointer_per_exchange = Counter(
        row[1] for row in NEUTRAL_FREDKIN_PHYSICAL_FACTORS
    )
    pointer_orbit = {
        opcode: count * pointer_occurrences
        for opcode, count in sorted(pointer_per_exchange.items())
    }
    guard_forward_expanded = sum(
        row["expanded_factors"] for row in guard_report["rows"]
    )
    guard_forward_routed = sum(
        row["routed_NN_gates"] for row in guard_report["rows"]
    )
    # Each of two station blocks occurs in each of two Q words and applies its
    # guard forward and reverse.  The row sum already includes both stations.
    guard_multiplier = 4
    guard_orbit_expanded = guard_multiplier * guard_forward_expanded
    guard_orbit_routed = guard_multiplier * guard_forward_routed
    taxi_swaps = geometry_report[
        "control_taxi_SWAP_occurrences_two_application_orbit"
    ]
    rail_swaps = 8
    controller_expanded = controller_report[
        "Cycle719_expanded_factor_occurrences_per_service_orbit"
    ]
    selected_accounted = (
        sum(core_orbit.values()) + sum(pointer_orbit.values())
        + taxi_swaps + rail_swaps
        + guard_orbit_routed + controller_expanded
    )
    return {
        "charged_endpoint_exchange_occurrences_two_word_orbit": core_occurrences,
        "neutral_pointer_exchange_occurrences_two_word_orbit": pointer_occurrences,
        "charged_matrix_candidate_factors_per_exchange": len(CORE_FACTORS),
        "charged_matrix_candidate_opcode_census_per_exchange": dict(sorted(
            core_per_exchange.items()
        )),
        "charged_matrix_candidate_opcode_census_two_word_orbit": core_orbit,
        "charged_matrix_candidate_factor_occurrences_two_word_orbit": sum(
            core_orbit.values()
        ),
        "neutral_pointer_Fredkin_factors_per_exchange": len(
            NEUTRAL_FREDKIN_PHYSICAL_FACTORS
        ),
        "neutral_pointer_Fredkin_opcode_census_per_exchange": dict(sorted(
            pointer_per_exchange.items()
        )),
        "neutral_pointer_Fredkin_opcode_census_two_word_orbit": pointer_orbit,
        "neutral_pointer_Fredkin_factor_occurrences_two_word_orbit": sum(
            pointer_orbit.values()
        ),
        "neutral_control_taxi_SWAP_occurrences_two_word_orbit": taxi_swaps,
        "service_rail_SWAP_occurrences_two_word_orbit": rail_swaps,
        "guard_expanded_factor_occurrences_two_word_orbit": guard_orbit_expanded,
        "guard_routed_NN_factor_occurrences_two_word_orbit": guard_orbit_routed,
        "guard_transport_SWAP_overhead_two_word_orbit": (
            guard_orbit_routed - guard_orbit_expanded
        ),
        "Cycle719_expanded_factor_occurrences_two_word_orbit": controller_expanded,
        "selected_program_accounted_factor_occurrences_two_word_orbit": selected_accounted,
        "census_boundary": (
            "Cycle719 count is its imported expanded-factor word; this bounded runner "
            "does not infer a new globally routed Cycle823+Cycle827 atlas count"
        ),
    }


def sanitize(value):
    if isinstance(value, dict):
        return {str(key): sanitize(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [sanitize(item) for item in value]
    if isinstance(value, set):
        return sorted(value)
    if isinstance(value, np.generic):
        return sanitize(value.item())
    if isinstance(value, complex):
        return (float(value.real), float(value.imag))
    return value


def module_source_provenance(module):
    path = Path(module.__file__).resolve()
    return {
        "source": path.relative_to(REPO_ROOT).as_posix(),
        "sha256": sha256(path.read_bytes()).hexdigest(),
    }


def direct_import_provenance():
    return {
        "runner_direct_repo_imports": {
            "Route_C_host": module_source_provenance(C),
        },
        "Route_C_host_direct_repo_imports": {
            "Cycle719_recurrent_controller": module_source_provenance(C.H719),
            "Cycle719_two_rail_core": module_source_provenance(C.K719),
            "Cycle720_companion_geometry": module_source_provenance(C.M720),
            "Cycle789_fixed_coframe_schedule": module_source_provenance(C.S789),
            "Cycle822_typed_transport": module_source_provenance(C.R822),
            "Cycle823_endpoint_instrument": module_source_provenance(C.I823),
            "Cycle826_history_interface": module_source_provenance(C.I826),
            "Cycle827_typed_controller_atlas": module_source_provenance(C.C827),
        },
        "numpy_version": np.__version__,
    }


def main():
    actual_atlas = actual_atlas_census()
    matrix = charged_exchange_matrix_candidate_certificate(actual_atlas)
    fredkin = neutral_fredkin_matrix_certificate(actual_atlas)
    C.controlled_exchange_matrix_certificate = lambda: matrix

    geometry = C.build_port_geometry()
    taxi = C.build_taxi_atlas(geometry)
    pointer_routes, pointer_route_failures = build_pointer_fredkin_routes(
        geometry, taxi
    )
    POINTER_FREDKIN_ROUTES.clear()
    POINTER_FREDKIN_ROUTES.update(pointer_routes)
    site_bits = C.site_bit_map(geometry, taxi)
    geometry_report = C.geometry_certificate(geometry, taxi)
    taxi_report = taxi_and_serial_certificate(
        geometry, taxi, matrix, fredkin, pointer_routes
    )
    taxi_report["pointer_Fredkin_route_failure_census"] = pointer_route_failures
    trace = candidate_factor_trace_certificate(geometry, taxi, actual_atlas)
    geometry_report["controlled_core_elementary_factors_two_application_orbit"] = (
        len(CORE_FACTORS)
        * taxi_report["charged_endpoint_exchange_occurrences_two_word_orbit"]
        + len(NEUTRAL_FREDKIN_PHYSICAL_FACTORS)
        * taxi_report["neutral_pointer_exchange_occurrences_two_word_orbit"]
    )
    geometry_report["controlled_core_factorization"] = (
        "11 canonical matrix factors on charged endpoint paths; 21 "
        "returned-routed canonical matrix factors on supplied-clean neutral "
        "pointer paths, relocated onto an explicitly supplied retyped palette"
    )
    guard = C.guard_physical_certificate(geometry)
    covariance = augmented_covariance_and_held(geometry, taxi, taxi_report)
    lawful = full_lawful_service_certificate(geometry, taxi, site_bits)
    sectors = augmented_sector_and_damage(geometry, taxi, site_bits)
    controller = C.controller_and_schedule_certificate(geometry_report)
    factors = elementary_factor_census(
        geometry_report, taxi_report, guard, controller
    )

    report = {
        "status": "bounded-selected-two-station-routec-typed-exchange-matrix-candidate",
        "authority": "none",
        "audit": "unset",
        "scope": (
            "exact matrix-level selected two-station service candidate on an "
            "explicitly supplied retyped palette and supplied singleton serial "
            "slots; not an actual-atlas opcode-site bind or fixed-law promotion"
        ),
        "source": {
            "Route_C_source": ROUTE_C_SOURCE.relative_to(REPO_ROOT).as_posix(),
            "Route_C_sha256": sha256(ROUTE_C_SOURCE.read_bytes()).hexdigest(),
            "runner_source": RUNNER_SOURCE.relative_to(REPO_ROOT).as_posix(),
            "runner_sha256": sha256(RUNNER_SOURCE.read_bytes()).hexdigest(),
            "direct_import_provenance": direct_import_provenance(),
            "opcode_dictionary_sha256": R822.nonseam_opcode_catalog()[
                "opcode_dictionary_sha256"
            ],
        },
        "charged_exchange_matrix_candidate": matrix,
        "neutral_pointer_matrix_candidate": fredkin,
        "selected_controlled_exchange_candidate_factor_trace": trace,
        "elementary_factor_census": factors,
        "geometry": geometry_report,
        "local_taxis_and_supplied_serial_slots": taxi_report,
        "guard": guard,
        "covariance_and_held": covariance,
        "lawful_service": lawful,
        "sectors_and_damage": sectors,
        "controller_and_schedule": controller,
        "scope_boundaries": {
            "selected_two_station_matrix_candidate_exact": True,
            "selected_two_station_actual_atlas_fixed_law_closed": False,
            "actual_atlas_opcode_site_support_bound": False,
            "actual_atlas_palette_reused": False,
            "generic_local_opcode_availability_supplied": True,
            "selected_palette_retyping_supplied": True,
            "supplied_singleton_serial_slots": True,
            "parallel_collision_or_recolouring_claimed": False,
            "new_H_dual_or_arbitrary_Givens_supplied": False,
            "full_global_Cycle823_Cycle827_atlas_bound": False,
            "autonomous_lattice_recurrence_claimed": False,
            "two_word_host_boundary_retired": False,
            "word_application_ordinals_are_physical_time": False,
            "remaining_dependency": (
                "bind every candidate opcode to exact sites in an actual typed "
                "atlas, reconcile the selected palette, construct parallel "
                "colouring if desired, and retire the hosted boundaries"
            ),
            "minimum_or_no_go_claimed": False,
        },
        "site_bit_width": max(site_bits.values()) + 1,
        "controller_cache": C.controller_map.cache_info()._asdict(),
    }
    checks = {
        "charged_matrix_candidate_exact_and_order_sensitive": (
            matrix["maximum_column_residual"] < TOL
            and matrix["first_two_factor_order_swap_residual"] > TOL
            and matrix["reversed_factor_order_residual"] > TOL
        ),
        "charged_matrix_candidate_preserves_clean_cSWAP_domain": (
            matrix["cSWAP_clean_domain_residual"] < TOL
            and matrix["cSWAP_dirty_11_residual"] > 1.0
        ),
        "charged_matrix_candidate_forward_adjoint_phase_exact": (
            matrix["W_dagger_exact_inverse_residual"] < TOL
            and matrix["W_dagger_Z_first_W_FSWAP_residual"] < TOL
            and abs(complex(*matrix["W_dagger_inverse_relative_phase"]) - 1) < TOL
        ),
        "charged_matrix_candidate_factor_and_prefix_P_ext": (
            matrix["maximum_factor_P_ext_commutator"] < TOL
            and matrix["maximum_prefix_P_ext_commutator"] < TOL
        ),
        "candidate_factor_trace_authenticated_and_adverse_boundary_exposed": (
            trace["candidate_factor_validation_failure_total"] == 0
            and trace["keyed_occurrence_counter_difference_from_taxi_atlas"] == 0
            and trace["expanded_candidate_factor_occurrences"]
            == geometry_report[
                "controlled_core_elementary_factors_two_application_orbit"
            ]
            and trace["hostile_factor_mutations"]["opcode_relabel_detected"]
            and trace["hostile_factor_mutations"][
                "declared_arity_mutation_detected"
            ]
            and trace["hostile_factor_mutations"]["matrix_mutation_detected"]
            and trace["hostile_same_total_5_3_occurrence_mutation"]["detected"]
            and trace["actual_atlas_adverse_boundary"][
                "actual_coordinate_support_or_palette_mismatches_nonzero"
            ]
            and not trace["actual_coordinate_opcode_site_support_claimed"]
            and not trace["actual_atlas_palette_reused_claimed"]
        ),
        "neutral_Fredkin_matrix_candidate_exact_expanded_and_order_sensitive": (
            fredkin["maximum_cSWAP_column_residual"] < TOL
            and fredkin["logical_vs_returned_routed_matrix_residual"] < TOL
            and fredkin["first_two_factor_order_swap_residual"] > TOL
            and fredkin["Cycle719_expanded_factors"] == 17
            and fredkin["Cycle719_expanded_factor_census"]
            == {"CNOT": 8, "H": 2, "T": 4, "TD": 3}
        ),
        "neutral_Fredkin_candidate_kinds_available_and_Cycle827_parity_safe": (
            fredkin[
                "all_candidate_opcode_kinds_available_somewhere_in_actual_atlas"
            ]
            and fredkin["Cycle827_control_normalization_failures"] == 0
            and fredkin["Cycle827_factor_parity_violations"] == 0
            and fredkin["Cycle827_prefix_parity"]["noncommuting_prefixes"] == 0
            and fredkin["Cycle827_prefix_parity"]["terminal_parity_returns"]
        ),
        "candidate_local_taxis_and_oriented_factor_sites_fit_retyped_palette": (
            taxi_report["all_local_placement_failures"] == 0
            and taxi_report["occurrence_sequence_census_failure"] == 0
            and taxi_report["keyed_occurrence_counter_difference_from_taxi_atlas"] == 0
            and sum(pointer_route_failures.values()) == 0
        ),
        "supplied_singleton_serial_slots_and_returned_labels_fit": (
            taxi_report["supplied_singleton_serial_factor_slots"]
            == trace["supplied_singleton_serial_factor_slots"]
            and taxi_report["maximum_factors_per_supplied_serial_slot"] == 1
            and taxi_report["parallel_factor_pairs_scheduled"] == 0
            and not taxi_report["parallel_collision_or_recolouring_claimed"]
            and taxi_report["taxi_return_label_failures"] == 0
            and taxi_report[
                "charged_matrix_candidate_control_return_leakage"
            ] < TOL
        ),
        "guard_lawful_and_inverse": (
            guard["guard_truth_failures"] == 0
            and guard["dirty_B_or_work_refusal_failures"] == 0
            and guard["guard_inverse_cleanup_failures"] == 0
        ),
        "passive_covariant_24_576_and_held_transport": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and covariance["translation_trials"] == 3
            and not any((
                covariance["frame_path_failures"],
                covariance["frame_type_failures"],
                covariance["frame_control_adjacency_failures"],
                covariance["frame_product_closure_failures"],
                covariance["frame_product_anchor_failures"],
                covariance["translation_failures"],
                covariance["held_actual_source_translation_failures"],
                covariance["matrix_candidate_24_frame_locality_failures"],
                covariance["matrix_candidate_24_frame_distinctness_failures"],
                covariance["matrix_candidate_576_product_coordinate_failures"],
                covariance["matrix_candidate_576_product_locality_failures"],
                covariance["held_matrix_candidate_locality_failures"],
                covariance["held_shifted_charged_neutral_overlap"],
            ))
        ),
        "lawful_service_and_full_inverse_exact": not any((
            lawful["history_failures"],
            lawful["endpoint_return_failures"],
            lawful["source_pointer_cleanup_failures"],
            lawful["controller_target_cleanup_failures"],
            lawful["service_register_return_failures"],
            lawful["Cycle719_internal_register_return_failures"],
            lawful["unexpected_phase_failures"],
            lawful["forward_inverse_failures"],
        )),
        "existing_unlawful_and_dirty_controls_preserved": (
            sectors["zero_token_history"] == ()
            and sectors["zero_token_source_pointers_retained"] == (1, 1)
            and sectors["two_token_count_returned"] == 2
            and sectors["two_token_whole_state_differs_from_lawful"]
            and sectors["unlawful_controller_target_patterns_detected"] == 7
            and sectors["dirty_taxi_corridor_transparency_residual"] < TOL
            and all(
                row["whole_state_differs_from_lawful"]
                for row in sectors["dirty_service_rows"].values()
            )
        ),
        "existing_route_guard_controller_deletions_active": all(
            sectors[key] > TOL for key in (
                "deleted_station1_pointer_adapter_factor_residual",
                "deleted_taxi_return_factor_residual",
                "deleted_guard_OR_Toffoli_residual",
                "deleted_Cycle719_finalizer_station_residual",
            )
        ),
        "each_charged_matrix_candidate_factor_deletion_active_in_service": (
            sectors["deleted_charged_matrix_candidate_factors_detected"]
            == sectors["deleted_charged_matrix_candidate_factors_tested"]
            == 11
        ),
        "each_pointer_Fredkin_physical_factor_deletion_active_on_clean_local_domain": (
            fredkin["physical_single_factor_clean_domain_deletions_detected"]
            == fredkin["physical_single_factor_deletions_tested"]
            == len(NEUTRAL_FREDKIN_PHYSICAL_FACTORS)
        ),
        "controller_normalization_preserved": (
            controller["Cycle827_normalization_equivalence_failures"] == 0
            and controller["normalized_vs_original_full_orbit_failures"] == 0
        ),
    }
    report["checks"] = checks
    print("REPORT_JSON", json.dumps(sanitize(report), sort_keys=True), flush=True)
    for label, passed in checks.items():
        print("CHECK", label, "PASS" if passed else "FAIL", flush=True)
    if not all(checks.values()):
        raise SystemExit(1)
    print("CYCLE864_ROUTEC_TYPED_EXCHANGE_MATRIX_CANDIDATE_PASS", flush=True)


if __name__ == "__main__":
    main()
