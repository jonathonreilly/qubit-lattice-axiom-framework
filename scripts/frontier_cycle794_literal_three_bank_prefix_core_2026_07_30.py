#!/usr/bin/env python3
"""Cycle-794 core for the literal local three-bank input prefix.

Only the public Cycle-789 algebra and fixed-coframe schedule surfaces are used.
The core emits the Bell-measurement/correction prefix on supplied O/I/L banks,
orders rows by transported local colour/slot data, and appends the routed local
inversion-CZ cocycle needed when that order reverses anticommuting private
corrections.  It proves the resulting signed Choi graph against the canonical
Cycle-789 channel.  Schedule labels are not physical time.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product

import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S788
import frontier_cycle789_three_register_even_car_channel_2026_07_30 as C788


AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    "scripts/frontier_cycle789_three_register_even_car_channel_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


def fields(row) -> tuple[int, int, int]:
    return C788.B.fields(row)


def normalized_frames():
    return tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in S788.B.V.T.proper_cubic_frames()
    )


def order_for(scratch, frame, shift=(0, 0, 0)) -> tuple[int, ...]:
    def key(index):
        owner, slot = scratch["owners_slots"][index]
        mapped = S788.add(S788.matvec(frame, owner), shift)
        return (
            tuple(value % S788.COLOR_MODULUS for value in mapped),
            slot,
            index,
        )

    return tuple(sorted(range(len(scratch["corrections"])), key=key))


def inversion_pairs(scratch, order) -> tuple[tuple[int, int], ...]:
    position = {row: index for index, row in enumerate(order)}
    return tuple(
        (left, right)
        for left, right in scratch["anti_pairs"]
        if position[left] > position[right]
    )


def measurement_block(obj, index: int) -> tuple[tuple, ...]:
    q = obj["q"]
    ancilla = 4 * q + index
    row = obj["bell_rows"][index]
    return (
        (("H", ancilla),)
        + tuple(
            ("CP", ancilla, qubit, C788.B.letter_at(row, qubit))
            for qubit in C788.B.supported_qubits(row)
        )
        + (("H", ancilla),)
    )


def correction_block(obj, index: int) -> tuple[tuple, ...]:
    q = obj["q"]
    ancilla = 4 * q + index
    row = obj["corrections"][index]
    return tuple(
        ("CP", ancilla, qubit, C788.B.letter_at(row, qubit))
        for qubit in C788.B.supported_qubits(row)
    )


def abstract_prefix_word(obj, scratch, order, *, repair=True):
    word = tuple(
        gate for index in order for gate in measurement_block(obj, index)
    ) + tuple(
        gate for index in order for gate in correction_block(obj, index)
    )
    inversions = inversion_pairs(scratch, order)
    if repair:
        q = obj["q"]
        word += tuple(
            ("CP", 4 * q + left, 4 * q + right, "Z")
            for left, right in inversions
        )
    return word, inversions


def bell_words_by_index(scratch):
    tag_to_index = {
        tuple(tag): index for index, tag in enumerate(scratch["tags"])
    }
    output = {"bell_measure": {}, "bell_correction": {}}
    for word in scratch["words"]:
        if word["stage"] in output:
            output[word["stage"]][tag_to_index[tuple(word["tag"])]] = word
    return output


def firewall_lookup(scratch):
    output = {}
    for macro, _owner, _slot in scratch["phase_firewall"]:
        if macro.stage != "bell_phase_firewall":
            continue
        output[(macro.control, macro.target)] = macro
    return output


def selected_firewall_macros(scratch, inversions):
    lookup = firewall_lookup(scratch)
    output = []
    for left, right in inversions:
        left_owner, left_slot = scratch["owners_slots"][left]
        right_owner, right_slot = scratch["owners_slots"][right]
        left_site = S788.ancilla_site(
            scratch["centers"][left_owner], left_slot, "bell"
        )
        right_site = S788.ancilla_site(
            scratch["centers"][right_owner], right_slot, "bell"
        )
        macro = lookup.get((left_site, right_site))
        if macro is None:
            macro = lookup.get((right_site, left_site))
        if macro is None:
            raise AssertionError(("missing Bell firewall macro", left, right))
        output.append(macro)
    return tuple(output)


def physical_prefix(scratch, order):
    by_index = bell_words_by_index(scratch)
    inversions = inversion_pairs(scratch, order)
    firewalls = selected_firewall_macros(scratch, inversions)
    words = tuple(by_index["bell_measure"][index] for index in order) + tuple(
        by_index["bell_correction"][index] for index in order
    )
    primitives = tuple(
        primitive for word in words for primitive in word["primitives"]
    ) + tuple(
        primitive for macro in firewalls for primitive in macro.primitives
    )
    macros = tuple(
        macro for word in words for macro in word["macros"]
    ) + firewalls
    return {
        "words": words,
        "macros": macros,
        "firewall_macros": firewalls,
        "inversions": inversions,
        "primitives": primitives,
    }

def physical_structure_failures(scratch, order, physical) -> int:
    by_index = bell_words_by_index(scratch)
    failures = 0
    for index in order:
        measurement = by_index["bell_measure"][index]
        expected = (
            (S788.Primitive("H", (measurement["ancilla"],)),)
            + tuple(
                primitive
                for macro in measurement["macros"]
                for primitive in macro.primitives
            )
            + (S788.Primitive("H", (measurement["ancilla"],)),)
        )
        failures += tuple(measurement["primitives"]) != expected
        correction = by_index["bell_correction"][index]
        expected = tuple(
            primitive
            for macro in correction["macros"]
            for primitive in macro.primitives
        )
        failures += tuple(correction["primitives"]) != expected
    for macro in physical["macros"]:
        controlled = tuple(
            primitive for primitive in macro.primitives
            if primitive.kind.startswith("CP_")
        )
        failures += len(controlled) != 1
        if controlled:
            failures += controlled[0].kind != "CP_" + macro.letter
            failures += controlled[0].sites != (
                macro.path[-2], macro.path[-1]
            )
        failures += macro.path[0] != macro.control
        failures += macro.path[-1] != macro.target
    expected_all = tuple(
        primitive
        for index in order
        for primitive in by_index["bell_measure"][index]["primitives"]
    ) + tuple(
        primitive
        for index in order
        for primitive in by_index["bell_correction"][index]["primitives"]
    ) + tuple(
        primitive
        for macro in physical["firewall_macros"]
        for primitive in macro.primitives
    )
    failures += tuple(physical["primitives"]) != expected_all
    return int(failures)


def semantic_signature_from_abstract(word, q):
    return tuple(tuple(gate) for gate in word)


def semantic_signature_from_physical(obj, scratch, order, physical):
    q = obj["q"]
    tag_to_index = {
        tuple(tag): index for index, tag in enumerate(scratch["tags"])
    }
    o_sites = tuple(S788.U.placement(scratch["fixture"])["sites_by_qubit"])
    i_sites = S788.bank_sites(
        scratch["fixture"], scratch["centers"], 1, S788.I_PAIRS
    )
    l_sites = S788.bank_sites(
        scratch["fixture"], scratch["centers"], 2, S788.L_PAIRS
    )
    site_to_wire = {
        **{site: index for index, site in enumerate(o_sites)},
        **{site: q + index for index, site in enumerate(i_sites)},
        **{site: 2 * q + index for index, site in enumerate(l_sites)},
    }
    output = []
    by_index = bell_words_by_index(scratch)
    for index in order:
        word = by_index["bell_measure"][index]
        if tag_to_index[tuple(word["tag"])] != index:
            raise AssertionError("tag/index drift")
        ancilla = 4 * q + index
        output.append(("H", ancilla))
        output.extend(
            ("CP", ancilla, site_to_wire[macro.target], macro.letter)
            for macro in word["macros"]
        )
        output.append(("H", ancilla))
    for index in order:
        word = by_index["bell_correction"][index]
        ancilla = 4 * q + index
        output.extend(
            ("CP", ancilla, site_to_wire[macro.target], macro.letter)
            for macro in word["macros"]
        )
    output.extend(
        ("CP", 4 * q + left, 4 * q + right, "Z")
        for left, right in physical["inversions"]
    )
    return tuple(output)


def graph_and_tableau_certificate(obj, scratch, order):
    canonical = tuple(obj["gates"])
    repaired, inversions = abstract_prefix_word(obj, scratch, order, repair=True)
    bare, _ = abstract_prefix_word(obj, scratch, order, repair=False)
    initial = obj["resource"] + obj["live_reference"] + obj["ancilla_z"]
    canonical_final = C788.conjugate_basis(initial, canonical)
    repaired_final = C788.conjugate_basis(initial, repaired)
    bare_final = C788.conjugate_basis(initial, bare)
    repaired_binary, repaired_signed = C788.signed_span_failures(
        obj["output_reference"], repaired_final, obj["width"]
    )
    bare_binary, bare_signed = C788.signed_span_failures(
        obj["output_reference"], bare_final, obj["width"]
    )
    generators = tuple(
        row
        for qubit in range(obj["width"])
        for row in (
            C788.Pauli(x=1 << qubit), C788.Pauli(z=1 << qubit)
        )
    )
    canonical_tableau = C788.conjugate_basis(generators, canonical)
    repaired_tableau = C788.conjugate_basis(generators, repaired)
    bare_tableau = C788.conjugate_basis(generators, bare)
    return {
        "inversion_CZs": len(inversions),
        "repaired_output_binary_span_failures": repaired_binary,
        "repaired_output_signed_span_failures": repaired_signed,
        "bare_output_binary_span_failures": bare_binary,
        "bare_output_signed_span_failures": bare_signed,
        "repaired_full_tableau_differences_from_canonical": sum(
            fields(left) != fields(right)
            for left, right in zip(canonical_tableau, repaired_tableau)
        ),
        "bare_full_tableau_differences_from_canonical": sum(
            fields(left) != fields(right)
            for left, right in zip(canonical_tableau, bare_tableau)
        ),
        "canonical_final_graph_sha256": sha256(repr(tuple(
            fields(row) for row in canonical_final
        )).encode()).hexdigest(),
        "repaired_final_graph_sha256": sha256(repr(tuple(
            fields(row) for row in repaired_final
        )).encode()).hexdigest(),
    }


def context_graph_certificate(obj, scratch):
    frames = normalized_frames()
    origins = tuple(product((0, 1), repeat=3))
    initial = obj["resource"] + obj["live_reference"] + obj["ancilla_z"]
    generators = tuple(
        row
        for qubit in range(obj["width"])
        for row in (
            C788.Pauli(x=1 << qubit), C788.Pauli(z=1 << qubit)
        )
    )
    canonical_tableau = C788.conjugate_basis(generators, tuple(obj["gates"]))
    rows = []
    binary = signed = tableau = 0
    inversion_counts = []
    for frame_id, frame in enumerate(frames):
        for origin in origins:
            order = order_for(scratch, frame, origin)
            repaired, inversions = abstract_prefix_word(
                obj, scratch, order, repair=True
            )
            final = C788.conjugate_basis(initial, repaired)
            context_binary, context_signed = C788.signed_span_failures(
                obj["output_reference"], final, obj["width"]
            )
            repaired_tableau = C788.conjugate_basis(generators, repaired)
            context_tableau = sum(
                fields(left) != fields(right)
                for left, right in zip(canonical_tableau, repaired_tableau)
            )
            binary += context_binary
            signed += context_signed
            tableau += context_tableau
            inversion_counts.append(len(inversions))
            rows.append((
                frame_id, origin, sha256(repr(order).encode()).hexdigest(),
                len(inversions), context_binary, context_signed,
                context_tableau,
            ))
    product_failures = 0
    checked_order_digests = {row[2] for row in rows}
    for left in frames:
        for right in frames:
            order = order_for(scratch, S788.matmul(left, right))
            product_failures += (
                sha256(repr(order).encode()).hexdigest()
                not in checked_order_digests
            )
    return {
        "proper_cubic_frames": len(frames),
        "translation_origins": len(origins),
        "frame_origin_contexts": len(rows),
        "ordered_frame_products": len(frames) ** 2,
        "minimum_inversion_CZs": min(inversion_counts, default=0),
        "maximum_inversion_CZs": max(inversion_counts, default=0),
        "repaired_output_binary_span_failures": binary,
        "repaired_output_signed_span_failures": signed,
        "repaired_full_tableau_differences_from_canonical": tableau,
        "frame_product_order_outside_checked_contexts": product_failures,
        "context_sha256": sha256(repr(tuple(rows)).encode()).hexdigest(),
    }


def firewall_path_covariance_certificate(scratch):
    frames = normalized_frames()
    origins = tuple(product((0, 1), repeat=3))
    macros = tuple(
        macro for macro, _owner, _slot in scratch["phase_firewall"]
        if macro.stage == "bell_phase_firewall"
    )
    context_NN_failures = 0
    context_endpoint_failures = 0
    for frame in frames:
        for origin in origins:
            for macro in macros:
                mapped = tuple(
                    S788.transform(site, frame, origin) for site in macro.path
                )
                context_NN_failures += sum(
                    S788.manhattan(left, right) != 1
                    for left, right in zip(mapped, mapped[1:])
                )
                context_endpoint_failures += (
                    mapped[0] != S788.transform(macro.control, frame, origin)
                    or mapped[-1]
                    != S788.transform(macro.target, frame, origin)
                )
    product_coordinate_failures = 0
    sites = tuple({site for macro in macros for site in macro.path})
    for left in frames:
        for right in frames:
            product_frame = S788.matmul(left, right)
            product_coordinate_failures += any(
                S788.matvec(left, S788.matvec(right, site))
                != S788.matvec(product_frame, site)
                for site in sites
            )
    return {
        "Bell_firewall_macros": len(macros),
        "proper_cubic_frames": len(frames),
        "translation_origins": len(origins),
        "frame_origin_contexts": len(frames) * len(origins),
        "ordered_frame_products": len(frames) ** 2,
        "context_NN_failures": context_NN_failures,
        "context_endpoint_failures": context_endpoint_failures,
        "product_coordinate_failures": product_coordinate_failures,
    }
