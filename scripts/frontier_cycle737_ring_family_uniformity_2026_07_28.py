#!/usr/bin/env python3
"""Cycle 737: bounded ring-family uniformity of the separated sector.

The Cycle-719 non-padded program constructor has N(b)=8b-5 stations for a
positive supplied bank count b.  This runner exhausts the first four members,
N in {3, 11, 19, 27}.  It checks the Cycle-736 template, marked-edge charge
law, count certificate, controller orbit, and adjacency wall at each member.
This is a finite-family theorem, not a theorem for arbitrary N.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb
import sys
from time import perf_counter

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RING_FAMILY_UNIFORMITY_CYCLE737_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

RING_FAMILY = (3, 11, 19, 27)
BANK_FAMILY = (1, 2, 3, 4)
SUGGESTED_CANDIDATES = (5, 7, 9, 13)
STDOUT_LIMIT_BYTES = 150 * 1024
BITPLANE_BATCH = 32_768

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def digest_json(value: object) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def tuple_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def mask_to_config(mask: int, stations: int) -> tuple[int, ...]:
    return tuple((mask >> station) & 1 for station in range(stations))


def occupied_sites(mask: int, stations: int) -> tuple[int, ...]:
    return tuple(
        station for station in range(stations) if (mask >> station) & 1
    )


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    full = (1 << stations) - 1
    normalized = shift % stations
    if normalized == 0:
        return mask & full
    return (
        ((mask << normalized) & full)
        | (mask >> (stations - normalized))
    )


def has_adjacent_pair(mask: int, stations: int) -> bool:
    return bool(mask & rotate_mask(mask, 1, stations))


def independent_masks(stations: int) -> tuple[int, ...]:
    """Generate every independent A-mask of C_n without scanning 2**n."""

    masks: list[int] = []

    def extend(
        station: int, first: int, previous: int, mask: int
    ) -> None:
        if station == stations:
            if not (first and previous):
                masks.append(mask)
            return
        extend(station + 1, first, 0, mask)
        if not previous and not (station == stations - 1 and first):
            extend(station + 1, first or int(station == 0), 1, mask | (1 << station))

    extend(0, 0, 0, 0)
    if len(masks) != len(set(masks)):
        raise AssertionError(("duplicate independent masks", stations))
    return tuple(masks)


def independent_cycle_closed_form(stations: int, count: int) -> int:
    if count == 0:
        return 1
    if count > stations // 2:
        return 0
    numerator = stations * comb(stations - count, count)
    denominator = stations - count
    if numerator % denominator:
        raise AssertionError(("nonintegral cycle census", stations, count))
    return numerator // denominator


def lucas_number(index: int) -> int:
    if index == 0:
        return 2
    if index == 1:
        return 1
    previous, current = 2, 1
    for _ in range(2, index + 1):
        previous, current = current, previous + current
    return current


def census_certificate(
    stations: int,
) -> tuple[dict[str, object], tuple[int, ...]]:
    masks = independent_masks(stations)
    maximum = stations // 2
    direct = tuple(
        sum(mask.bit_count() == count for mask in masks)
        for count in range(maximum + 1)
    )
    closed = tuple(
        independent_cycle_closed_form(stations, count)
        for count in range(maximum + 1)
    )
    total = len(masks)
    lucas = lucas_number(stations)
    report = {
        "ring": stations,
        "maximum_k": maximum,
        "direct_counts_by_k": direct,
        "closed_form_counts_by_k": closed,
        "direct_total": total,
        "closed_form_total": sum(closed),
        "lucas_total": lucas,
        "closed_form": "|Ind_k(C_n)|=n/(n-k)*binomial(n-k,k)",
        "lucas_recurrence": "L_0=2,L_1=1,L_n=L_(n-1)+L_(n-2)",
        "mask_table_sha256": digest_json(masks),
        "exact": (
            direct == closed
            and total == sum(closed) == lucas
            and not any(has_adjacent_pair(mask, stations) for mask in masks)
        ),
    }
    return report, masks


def reference_mask(mask: int, stations: int) -> int:
    refs = C731.canonical_refs(
        mask, 0, mask.bit_count() & 1, stations
    )
    return tuple_to_int(refs)


def source_from_masks(
    layout: dict[str, int],
    a_mask: int,
    refs_mask: int,
    parity: int,
) -> int:
    return (
        (a_mask << layout["a_base"])
        | (refs_mask << layout["ref_base"])
        | (int(parity) << layout["h_wire"])
    )


def marked_edge_law(
    a_mask: int, refs_mask: int, parity: int, stations: int
) -> bool:
    marked = int(C731.E730.F728.marked_station(stations))
    return all(
        (
            ((refs_mask >> station) & 1)
            ^ ((a_mask >> station) & 1)
            ^ ((refs_mask >> ((station + 1) % stations)) & 1)
            ^ (int(parity) if station == marked else 0)
        )
        == 0
        for station in range(stations)
    )


def pure_x_apply(word: tuple[object, ...]) -> tuple[int, bool, bool]:
    value = 0
    targets: list[int] = []
    pure = True
    for gate in word:
        pure &= gate.kind == "X" and len(gate.wires) == 1
        if gate.kind != "X" or len(gate.wires) != 1:
            continue
        target = int(gate.wires[0])
        targets.append(target)
        value ^= 1 << target
    return value, pure, len(targets) == len(set(targets))


def first_mask_by_k(
    masks: tuple[int, ...], maximum: int
) -> dict[int, int]:
    output: dict[int, int] = {}
    for mask in masks:
        output.setdefault(mask.bit_count(), mask)
    if tuple(sorted(output)) != tuple(range(maximum + 1)):
        raise AssertionError(("missing count sector", tuple(sorted(output))))
    return output


def template_and_covariance_certificate(
    stations: int,
    masks: tuple[int, ...],
    refs_masks: tuple[int, ...],
    layout: dict[str, int],
) -> dict[str, object]:
    maximum = stations // 2
    first_by_k = first_mask_by_k(masks, maximum)
    exact_failures = 0
    charge_failures = 0
    literal_sample_failures = 0
    rows_hasher = sha256()
    ring_mask = (1 << stations) - 1
    data_mask = (1 << layout["data_width"]) - 1
    allowed_support = (
        (ring_mask << layout["a_base"])
        | (ring_mask << layout["ref_base"])
        | (1 << layout["h_wire"])
    )

    for mask, refs_mask in zip(masks, refs_masks):
        config = mask_to_config(mask, stations)
        parity = mask.bit_count() & 1
        word = M736.multisource_creation_word(layout, config)
        observed, pure, unique = pure_x_apply(word)
        expected = M736.template_expected_value(layout, config)
        supplied = source_from_masks(layout, mask, refs_mask, parity)
        lawful = marked_edge_law(mask, refs_mask, parity, stations)
        conditions = (
            observed == expected == supplied,
            pure,
            unique,
            (observed & data_mask) == 0,
            ((observed >> layout["a_base"]) & ring_mask) == mask,
            ((observed >> layout["b_base"]) & ring_mask) == 0,
            ((observed >> layout["work_base"]) & ring_mask) == 0,
            ((observed >> layout["ref_base"]) & ring_mask) == refs_mask,
            ((observed >> layout["h_wire"]) & 1) == parity,
            (observed & ~allowed_support) == 0,
            len(word)
            == mask.bit_count() + refs_mask.bit_count() + parity,
        )
        exact_failures += not all(conditions)
        charge_failures += not lawful
        if first_by_k[mask.bit_count()] == mask:
            literal = C731.literal_apply(
                (0,), word, layout["full_width"], 1
            )[0]
            literal_sample_failures += literal != observed
        rows_hasher.update(
            (
                f"{mask}:{refs_mask}:{len(word)}:"
                f"{int(all(conditions))}:{int(lawful)};"
            ).encode()
        )

    covariance_masks = {
        mask for mask in masks if mask.bit_count() <= 2
    }
    covariance_masks.update(first_by_k.values())
    covariance_failures = 0
    covariance_identities = 0
    covariance_hasher = sha256()
    for mask in sorted(covariance_masks):
        config = mask_to_config(mask, stations)
        word = M736.multisource_creation_word(layout, config)
        for shift in range(stations):
            shifted_mask = rotate_mask(mask, shift, stations)
            conjugated = M736.conjugate_template_by_translation(
                word, layout, shift
            )
            target = M736.multisource_creation_word(
                layout, mask_to_config(shifted_mask, stations)
            )
            exact = conjugated == target
            covariance_identities += 1
            covariance_failures += not exact
            covariance_hasher.update(
                f"{mask}:{shift}:{shifted_mask}:{int(exact)};".encode()
            )

    k_le_2 = sum(mask.bit_count() <= 2 for mask in masks)
    ast_audit = M736.template_ast_audit()
    expected_covariance = len(covariance_masks) * stations
    return {
        "ring": stations,
        "template_cases": len(masks),
        "template_exactness_failures": exact_failures,
        "marked_edge_charge_failures": charge_failures,
        "marked_station": int(C731.E730.F728.marked_station(stations)),
        "literal_samples": maximum + 1,
        "literal_sample_failures": literal_sample_failures,
        "template_table_sha256": rows_hasher.hexdigest(),
        "covariance_scope": "all k<=2 plus one declared sample per k",
        "all_k_le_2_configurations": k_le_2,
        "covariance_sample_masks_sha256":
            digest_json(tuple(sorted(covariance_masks))),
        "one_declared_sample_per_k": tuple(
            first_by_k[count] for count in range(maximum + 1)
        ),
        "covariance_configurations": len(covariance_masks),
        "shifts_per_configuration": stations,
        "covariance_identities": covariance_identities,
        "expected_covariance_identities": expected_covariance,
        "covariance_failures": covariance_failures,
        "covariance_table_sha256": covariance_hasher.hexdigest(),
        "config_parameter_ast_anchor": ast_audit["audit_pass"],
        "exact": (
            exact_failures == charge_failures == literal_sample_failures == 0
            and covariance_failures == 0
            and covariance_identities == expected_covariance
            and ast_audit["audit_pass"]
        ),
    }


def count_enforcement_certificate(
    program: tuple[object, ...],
    stations: int,
    masks: tuple[int, ...],
    refs_masks: tuple[int, ...],
    counts: tuple[int, ...],
) -> dict[str, object]:
    maximum = stations // 2
    prefixes: list[tuple[tuple[object, ...], dict[str, int]]] = []
    layouts_equal = True
    canonical_layout: dict[str, int] | None = None
    prefix_gate_counts: list[int] = []
    prefix_digests: list[str] = []

    for expected_count in range(maximum + 1):
        word, layout, _blocks, metadata = (
            C731.count_certified_controller_build(
                program, C731.DATA_WIDTH, expected_count
            )
        )
        if canonical_layout is None:
            canonical_layout = layout
        else:
            layouts_equal &= layout == canonical_layout
        stop = int(metadata["comparison_compute_stop"])
        prefix = word[:stop]
        prefixes.append((prefix, layout))
        prefix_gate_counts.append(len(prefix))
        prefix_digests.append(K.gate_digest(prefix))
        C731.count_certified_controller_build.cache_clear()

    if canonical_layout is None:
        raise AssertionError("count constructor did not produce a layout")
    accepted = [
        [0 for _ in range(maximum + 1)]
        for _ in range(maximum + 1)
    ]
    refused = [
        [0 for _ in range(maximum + 1)]
        for _ in range(maximum + 1)
    ]
    reverse_failures = 0
    preservation_failures = 0
    counter_failures = 0
    refusal_failures = 0
    first_failure: dict[str, object] | None = None
    table_hasher = sha256()

    for start in range(0, len(masks), BITPLANE_BATCH):
        stop = min(start + BITPLANE_BATCH, len(masks))
        batch_masks = masks[start:stop]
        batch_refs = refs_masks[start:stop]
        sources = tuple(
            source_from_masks(
                canonical_layout,
                mask,
                refs_mask,
                mask.bit_count() & 1,
            )
            for mask, refs_mask in zip(batch_masks, batch_refs)
        )
        for expected_count, (prefix, layout) in enumerate(prefixes):
            compared = C731.literal_apply(
                sources, prefix, layout["full_width"], 1
            )
            restored = C731.literal_apply(
                compared,
                tuple(reversed(prefix)),
                layout["full_width"],
                1,
            )
            counter_mask = (1 << layout["counter_width"]) - 1
            ring_mask = (1 << stations) - 1
            for mask, refs_mask, source, value, recovered in zip(
                batch_masks, batch_refs, sources, compared, restored
            ):
                true_count = mask.bit_count()
                observed_count = (
                    value >> layout["counter_base"]
                ) & counter_mask
                observed_refusal = (
                    value >> layout["refusal_latch"]
                ) & 1
                expected_refusal = int(true_count != expected_count)
                observed_a = (
                    value >> layout["a_base"]
                ) & ring_mask
                observed_refs = (
                    value >> layout["ref_base"]
                ) & ring_mask
                observed_h = (value >> layout["h_wire"]) & 1
                accepted[expected_count][true_count] += (
                    observed_refusal == 0
                )
                refused[expected_count][true_count] += (
                    observed_refusal == 1
                )
                counter_bad = observed_count != true_count
                refusal_bad = observed_refusal != expected_refusal
                preservation_bad = (
                    observed_a != mask
                    or observed_refs != refs_mask
                    or observed_h != (true_count & 1)
                )
                reverse_bad = recovered != source
                counter_failures += counter_bad
                refusal_failures += refusal_bad
                preservation_failures += preservation_bad
                reverse_failures += reverse_bad
                if (
                    first_failure is None
                    and (
                        counter_bad
                        or refusal_bad
                        or preservation_bad
                        or reverse_bad
                    )
                ):
                    first_failure = {
                        "expected_count": expected_count,
                        "mask": mask,
                        "true_count": true_count,
                        "observed_count": observed_count,
                        "observed_refusal": observed_refusal,
                        "expected_refusal": expected_refusal,
                        "preservation_bad": preservation_bad,
                        "reverse_bad": reverse_bad,
                    }
                table_hasher.update(
                    (
                        f"{expected_count}:{mask}:{observed_count}:"
                        f"{observed_refusal};"
                    ).encode()
                )

    expected_accepted = tuple(
        tuple(
            counts[true_count] if expected_count == true_count else 0
            for true_count in range(maximum + 1)
        )
        for expected_count in range(maximum + 1)
    )
    expected_refused = tuple(
        tuple(
            0 if expected_count == true_count else counts[true_count]
            for true_count in range(maximum + 1)
        )
        for expected_count in range(maximum + 1)
    )
    accepted_tuple = tuple(tuple(row) for row in accepted)
    refused_tuple = tuple(tuple(row) for row in refused)
    diagonal = sum(
        accepted[count][count] for count in range(maximum + 1)
    )
    cross = sum(
        refused[expected][true]
        for expected in range(maximum + 1)
        for true in range(maximum + 1)
        if expected != true
    )
    return {
        "ring": stations,
        "constructor": (
            "C731.count_certified_controller_build("
            "K.interleaved_program(b),DATA_WIDTH,expected_count=k)"
        ),
        "counter_width": canonical_layout["counter_width"],
        "counter_width_formula": "ceil(log2(n+1)) = n.bit_length()",
        "expected_counter_width": stations.bit_length(),
        "expected_count_domain": tuple(range(maximum + 1)),
        "true_count_domain": tuple(range(maximum + 1)),
        "accepted_grid": accepted_tuple,
        "refused_grid": refused_tuple,
        "expected_accepted_grid": expected_accepted,
        "expected_refused_grid": expected_refused,
        "acceptance_diagonal": diagonal,
        "expected_acceptance_diagonal": len(masks),
        "cross_refusal_off_diagonal": cross,
        "expected_cross_refusal_off_diagonal": len(masks) * maximum,
        "constructor_layouts_equal": layouts_equal,
        "constructor_prefix_gate_counts": tuple(prefix_gate_counts),
        "constructor_prefix_sha256": tuple(prefix_digests),
        "counter_failures": counter_failures,
        "refusal_failures": refusal_failures,
        "rail_preservation_failures": preservation_failures,
        "prefix_reverse_failures": reverse_failures,
        "first_failure": first_failure,
        "cross_census_sha256": table_hasher.hexdigest(),
        "exact": (
            accepted_tuple == expected_accepted
            and refused_tuple == expected_refused
            and diagonal == len(masks)
            and cross == len(masks) * maximum
            and layouts_equal
            and canonical_layout["counter_width"] == stations.bit_length()
            and counter_failures
            == refusal_failures
            == preservation_failures
            == reverse_failures
            == 0
            and first_failure is None
        ),
    }


def circular_distance(
    left: int, right: int, stations: int
) -> int:
    return min(
        (right - left) % stations, (left - right) % stations
    )


def invariant_census(
    stations: int,
    masks: tuple[int, ...],
    counts: tuple[int, ...],
) -> dict[str, int]:
    boundary_steps = 0
    adjacency_violations = 0
    translation_failures = 0
    rail_closure_failures = 0
    for mask in masks:
        live = mask
        for step in range(stations):
            boundary_steps += 1
            translation_failures += (
                live != rotate_mask(mask, step, stations)
            )
            adjacency_violations += has_adjacent_pair(live, stations)
            live = rotate_mask(live, 1, stations)
        rail_closure_failures += live != mask

    isometry_failures = 0
    for left in range(stations):
        for right in range(left + 1, stations):
            baseline = circular_distance(left, right, stations)
            for shift in range(stations):
                isometry_failures += (
                    circular_distance(
                        (left + shift) % stations,
                        (right + shift) % stations,
                        stations,
                    )
                    != baseline
                )
    pair_count = sum(
        comb(count, 2) * counts[count]
        for count in range(len(counts))
    )
    return {
        "boundary_steps": boundary_steps,
        "expected_boundary_steps": len(masks) * stations,
        "station_checks": boundary_steps * stations,
        "adjacency_ownership_violations": adjacency_violations,
        "common_translation_failures": translation_failures,
        "rail_closure_failures": rail_closure_failures,
        "pairwise_distance_checks": pair_count * stations,
        "translation_isometry_basis_checks":
            comb(stations, 2) * stations,
        "translation_isometry_failures": isometry_failures,
    }


def controller_orbit_certificate(
    banks: int,
    program: tuple[object, ...],
    stations: int,
    masks: tuple[int, ...],
    counts: tuple[int, ...],
) -> dict[str, object]:
    genesis_banks, links = K.B.chain_genesis(banks)
    data = K.M.prepare_endpoint(
        K.M.pack_state(genesis_banks, links), (1, 0)
    )
    data_wires = len(data)
    data_value = tuple_to_int(data)
    controller = K.controller_word(program, data_wires)
    inverse_controller = tuple(reversed(controller))
    width = data_wires + 3 * stations
    ring_mask = (1 << stations) - 1
    data_mask = (1 << data_wires) - 1
    data_bytes = (data_wires + 7) // 8
    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations

    register_failures = 0
    exact_register_closures = 0
    orbit_hasher = sha256()
    samples = first_mask_by_k(masks, stations // 2)
    sample_outputs: dict[int, int] = {}

    for start in range(0, len(masks), BITPLANE_BATCH):
        batch_masks = masks[start:start + BITPLANE_BATCH]
        sources = tuple(
            data_value | (mask << a_base) for mask in batch_masks
        )
        observed = C731.literal_apply(
            sources, controller, width, stations
        )
        for mask, output in zip(batch_masks, observed):
            output_a = (output >> a_base) & ring_mask
            output_b = (output >> b_base) & ring_mask
            output_work = (output >> work_base) & ring_mask
            register_bad = (
                output_a != mask
                or output_b != 0
                or output_work != 0
            )
            register_failures += register_bad
            exact_register_closures += not register_bad
            output_data = output & data_mask
            orbit_hasher.update(mask.to_bytes(4, "little"))
            orbit_hasher.update(
                output_data.to_bytes(data_bytes, "little")
            )
            count = mask.bit_count()
            if samples[count] == mask:
                sample_outputs[count] = output

    allowed_gate_kinds = {"X", "CNOT", "TOF"}
    inverse_structure_failures = sum(
        gate.kind not in allowed_gate_kinds for gate in controller
    )
    sample_source_values = tuple(
        data_value | (mask << a_base)
        for _count, mask in sorted(samples.items())
    )
    sample_output_values = tuple(
        sample_outputs[count] for count in sorted(samples)
    )
    inverse_sample_values = C731.literal_apply(
        sample_output_values, inverse_controller, width, stations
    )
    inverse_sample_failures = sum(
        recovered != source
        for recovered, source in zip(
            inverse_sample_values, sample_source_values
        )
    )
    inverse_certified_configurations = (
        len(masks)
        if inverse_structure_failures == inverse_sample_failures == 0
        else 0
    )
    exact_closures = (
        len(masks)
        if exact_register_closures == len(masks)
        and inverse_certified_configurations == len(masks)
        else 0
    )

    sample_semantic_failures = 0
    sample_composition_failures = 0
    sample_trace_failures = 0
    for count, mask in sorted(samples.items()):
        sites = occupied_sites(mask, stations)
        semantic_output, final_a, final_b, trace = K.run_orbit(
            data, program, token_positions=sites
        )
        expected_composition = K.A.apply_semantic(
            data, M736.synchronous_composition_word(program, sites)
        )
        literal = sample_outputs[count]
        literal_data = literal & data_mask
        literal_a = (literal >> a_base) & ring_mask
        literal_b = (literal >> b_base) & ring_mask
        sample_semantic_failures += (
            literal_data != tuple_to_int(semantic_output)
            or literal_a != tuple_to_int(final_a)
            or literal_b != tuple_to_int(final_b)
        )
        sample_composition_failures += (
            semantic_output != expected_composition
        )
        sample_trace_failures += len(trace) != stations

    held = K.held_certificate(banks)
    held_failures = sum(
        int(held[key])
        for key in (
            "logical_failures",
            "fixed_word_failures",
            "inverse_failures",
            "postimage_failures",
            "token_return_failures",
        )
    )
    invariants = invariant_census(stations, masks, counts)
    failure_census = {
        "adjacency_ownership_violations":
            invariants["adjacency_ownership_violations"],
        "common_translation_failures":
            invariants["common_translation_failures"],
        "translation_isometry_failures":
            invariants["translation_isometry_failures"],
        "rail_closure_failures":
            invariants["rail_closure_failures"],
        "literal_register_failures": register_failures,
        "inverse_structure_failures": inverse_structure_failures,
        "inverse_sample_failures": inverse_sample_failures,
        "sample_semantic_failures": sample_semantic_failures,
        "sample_composition_failures": sample_composition_failures,
        "sample_trace_failures": sample_trace_failures,
        "Cycle719_held_baseline_failures": held_failures,
    }
    return {
        "ring": stations,
        "banks": banks,
        "program_stations": len(program),
        "program_nonidentity_stations":
            sum(bool(K.mapped_macro(row)) for row in program),
        "controller_semantic_gates": len(controller),
        "controller_word_sha256": K.gate_digest(controller),
        "orbit_configurations": len(masks),
        "steps_per_orbit": stations,
        "exhausted_literal_controller_steps": len(masks) * stations,
        "invariants": invariants,
        "exact_register_and_inverse_closures": exact_closures,
        "expected_exact_closures": len(masks),
        "literal_inverse_samples": len(samples),
        "inverse_certified_configurations":
            inverse_certified_configurations,
        "inverse_certificate": (
            "reverse(W)^n is the exact inverse of W^n because every "
            "emitted X/CNOT/TOF gate is self-inverse; the reversed "
            "full orbit is additionally executed once in every k sector"
        ),
        "semantic_composition_samples": len(samples),
        "sample_counts": tuple(sorted(samples)),
        "failure_census": failure_census,
        "orbit_output_table_sha256": orbit_hasher.hexdigest(),
        "literal_execution": (
            "K.controller_word(program,DATA_WIDTH) iterated n times "
            "forward over every independent configuration in bitplane "
            "batches"
        ),
        "distance_argument": (
            "every boundary A-mask was checked as the common rotation; "
            "circular-distance isometry was checked for every site pair "
            "and every shift"
        ),
        "exact": (
            exact_closures == len(masks)
            and invariants["boundary_steps"] == len(masks) * stations
            and invariants["pairwise_distance_checks"]
            == sum(
                comb(count, 2) * counts[count]
                for count in range(len(counts))
            )
            * stations
            and all(value == 0 for value in failure_census.values())
        ),
    }


def near_miss_certificate(stations: int) -> dict[str, object]:
    rows = []
    first_failure: dict[str, object] | None = None
    total_violating_stations = 0
    total_reason_incidences = 0
    for left in range(stations):
        right = (left + 1) % stations
        mask = (1 << left) | (1 << right)
        config = mask_to_config(mask, stations)
        violations = M736.S735.P734.ownership_violations(
            config, (0,) * stations, (0,) * stations
        )
        observed_sites = tuple(
            int(row["station"]) for row in violations
        )
        expected_sites = tuple(sorted((left, right)))
        reasons = tuple(
            reason
            for row in violations
            for reason in row["reasons"]
            if reason in ("left_A", "right_A")
        )
        exact = (
            observed_sites == expected_sites
            and len(violations) == 2
            and len(reasons) == 2
        )
        if not exact and first_failure is None:
            first_failure = {
                "edge": (left, right),
                "observed_sites": observed_sites,
                "expected_sites": expected_sites,
                "reasons": reasons,
            }
        total_violating_stations += len(violations)
        total_reason_incidences += len(reasons)
        rows.append(
            (left, right, observed_sites, reasons, exact)
        )
    return {
        "ring": stations,
        "adjacent_pairs": stations,
        "violating_stations": total_violating_stations,
        "expected_violating_stations": 2 * stations,
        "neighbor_reason_incidences": total_reason_incidences,
        "expected_neighbor_reason_incidences": 2 * stations,
        "wall": "ownership_uniqueness_at_adjacent_Q_sites",
        "first_failure": first_failure,
        "near_miss_table_sha256": digest_json(rows),
        "exact": (
            first_failure is None
            and total_violating_stations
            == total_reason_incidences
            == 2 * stations
        ),
    }


def admissibility_certificate() -> dict[str, object]:
    programs = tuple(
        K.interleaved_program(banks) for banks in BANK_FAMILY
    )
    observed = tuple(len(program) for program in programs)
    formula = tuple(8 * banks - 5 for banks in BANK_FAMILY)
    excluded = []
    for stations in SUGGESTED_CANDIDATES:
        numerator = stations + 5
        bank_count = numerator // 8 if numerator % 8 == 0 else None
        if bank_count is None or bank_count < 1:
            excluded.append(
                {
                    "ring": stations,
                    "reason": (
                        "no positive integer bank count b solves "
                        "n=8b-5"
                    ),
                }
            )
    padded = K.interleaved_program(12, physical_padding=True)
    return {
        "ring_family": RING_FAMILY,
        "bank_family": BANK_FAMILY,
        "observed_program_lengths": observed,
        "derived_program_lengths": formula,
        "derivation": (
            "non-padded K.interleaved_program(b): source + b banks + "
            "(b-1) crosses + 3(b-1) forward link rows + 3(b-1) "
            "reverse link rows + finalizer = 8b-5, for supplied b>=1"
        ),
        "membership_rule": "n=8b-5 for declared positive integer b",
        "suggested_candidates": SUGGESTED_CANDIDATES,
        "excluded_suggested_candidates": tuple(excluded),
        "K_n11_status": (
            "not hard-coded in the non-padded constructor; n=11 is "
            "the derived b=2 member"
        ),
        "physical_padding_frozen_dependence": {
            "constructor": "K.interleaved_program",
            "argument": "physical_padding=True",
            "required_bank_count": 12,
            "fixed_program_stations": len(padded),
            "source_constant": 130,
            "used_by_sector_family": False,
        },
        "exact": (
            observed == formula == RING_FAMILY
            and len(RING_FAMILY) >= 4
            and 11 in RING_FAMILY
            and len(tuple(n for n in RING_FAMILY if n != 11)) >= 3
            and len(excluded) == len(SUGGESTED_CANDIDATES)
            and len(padded) == 130
        ),
    }


def cycle736_anchor() -> dict[str, object]:
    program = K.interleaved_program(2)
    _word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, 0
        )
    )
    anchor = M736.cycle735_regression_anchor(layout)
    frozen = M736.configuration_census()
    configurations = frozen.pop("configurations")
    C731.count_certified_controller_build.cache_clear()
    return {
        "ring": 11,
        "frozen_counts_by_k": frozen["direct_counts_by_k"],
        "frozen_total": frozen["direct_total"],
        "frozen_lucas_total": frozen["lucas_recurrence_total_L11"],
        "one_orbit": anchor["one_orbit_rerun"],
        "Cycle735_regression_anchor": anchor["regression_pass"],
        "configuration_rows_rerun": len(configurations),
        "exact": (
            frozen["agreement"]
            and frozen["direct_counts_by_k"]
            == M736.EXPECTED_COUNTS_BY_K
            and frozen["direct_total"]
            == frozen["lucas_recurrence_total_L11"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and anchor["regression_pass"]
        ),
    }


def main() -> int:
    started = perf_counter()
    check(
        "INPUT_declared_literal_paths",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
            "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
        and NOTE_PATH
        == "docs/RING_FAMILY_UNIFORMITY_CYCLE737_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )

    anchor = cycle736_anchor()
    check("A_Cycle736_anchor_n11", anchor["exact"])

    admissibility = admissibility_certificate()
    check("B_admissibility_derivation", admissibility["exact"])

    census_reports: dict[int, dict[str, object]] = {}
    template_reports: dict[int, dict[str, object]] = {}
    enforcement_reports: dict[int, dict[str, object]] = {}
    orbit_reports: dict[int, dict[str, object]] = {}
    near_miss_reports: dict[int, dict[str, object]] = {}

    for banks, stations in zip(BANK_FAMILY, RING_FAMILY):
        program = K.interleaved_program(banks)
        census, masks = census_certificate(stations)
        counts = tuple(census["direct_counts_by_k"])
        refs_masks = tuple(
            reference_mask(mask, stations) for mask in masks
        )
        census_reports[stations] = census
        check(
            f"C_census_lucas_agreement_n{stations}",
            census["exact"]
            and census["direct_total"]
            == census["closed_form_total"]
            == census["lucas_total"],
        )

        _word, layout, _blocks, _metadata = (
            C731.count_certified_controller_build(
                program, C731.DATA_WIDTH, 0
            )
        )
        C731.count_certified_controller_build.cache_clear()
        template = template_and_covariance_certificate(
            stations, masks, refs_masks, layout
        )
        template_reports[stations] = template
        check(
            f"D_template_exactness_covariance_n{stations}",
            template["exact"]
            and template["template_cases"] == census["direct_total"]
            and template["all_k_le_2_configurations"]
            == sum(counts[:3]),
        )

        enforcement = count_enforcement_certificate(
            program, stations, masks, refs_masks, counts
        )
        enforcement_reports[stations] = enforcement
        check(
            f"E_enforcement_grid_n{stations}",
            enforcement["exact"]
            and enforcement["counter_width"] == stations.bit_length()
            and enforcement["acceptance_diagonal"]
            == census["direct_total"]
            and enforcement["cross_refusal_off_diagonal"]
            == census["direct_total"] * (stations // 2),
        )

        orbit = controller_orbit_certificate(
            banks, program, stations, masks, counts
        )
        orbit_reports[stations] = orbit
        check(
            f"F_invariant_full_orbit_n{stations}",
            orbit["exact"]
            and orbit["orbit_configurations"] == census["direct_total"]
            and orbit["exhausted_literal_controller_steps"]
            == census["direct_total"] * stations
            and orbit["exact_register_and_inverse_closures"]
            == census["direct_total"],
        )

        near_miss = near_miss_certificate(stations)
        near_miss_reports[stations] = near_miss
        check(
            f"G_near_miss_controls_n{stations}",
            near_miss["exact"]
            and near_miss["violating_stations"]
            == near_miss["expected_violating_stations"]
            == 2 * stations,
        )
        del masks
        del refs_masks

    family_component_pass = all(
        report["exact"]
        for reports in (
            census_reports,
            template_reports,
            enforcement_reports,
            orbit_reports,
            near_miss_reports,
        )
        for report in reports.values()
    )
    frozen_n_dependence = None if family_component_pass else {
        "outcome": "one or more declared family components failed",
        "supplied_program_family": "n=8b-5",
    }
    boundary = {
        "ring_family": list(RING_FAMILY),
        "sector_theorem_uniform_over_family": bool(
            admissibility["exact"] and family_component_pass
        ),
        "frozen_n_dependence": frozen_n_dependence,
        "family_membership_declared": True,
        "general_n_theorem_claimed": False,
        "per_n_geometry_supplied": True,
        "per_n_program_supplied": True,
        "per_n_genesis_supplied": True,
        "canonical_reference_gauge_cut_supplied": True,
        "expected_count_grid_supplied": True,
        "supplies": (
            "positive bank count b and non-padded K program with n=8b-5",
            "finite oriented per-n ring geometry and marked reference cut",
            "per-n clean K chain genesis and direction-(1,0) endpoint",
            "external independent configuration parameter",
            "blank B/work rails and clean controller auxiliaries",
            "expected_count=k for every per-n enforcement-grid row",
        ),
        "uniformity_statement": (
            "Each declared family member is exhaustive.  Passing all "
            "members proves ring-uniformity only over [3,11,19,27], "
            "not for arbitrary n."
        ),
    }
    check(
        "H_honest_boundary_keys",
        boundary["ring_family"] == list(RING_FAMILY)
        and boundary["sector_theorem_uniform_over_family"]
        and boundary["frozen_n_dependence"] is None
        and boundary["family_membership_declared"]
        and not boundary["general_n_theorem_claimed"]
        and boundary["per_n_geometry_supplied"]
        and boundary["per_n_program_supplied"]
        and boundary["per_n_genesis_supplied"],
    )

    elapsed = perf_counter() - started
    check(
        "TIMEOUT_runtime_under_900_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
    )
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "admissibility_derivation": admissibility,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "Cycle736_anchor": anchor,
        "census_lucas_agreement": census_reports,
        "template_exactness_covariance": template_reports,
        "enforcement_grid": enforcement_reports,
        "invariant_full_orbit": orbit_reports,
        "near_miss_controls": near_miss_reports,
        "honest_boundary": boundary,
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE737_RING_FAMILY_UNIFORMITY_PASS"
            if all(CHECKS.values())
            else "CYCLE737_RING_FAMILY_UNIFORMITY_HONEST_FAIL"
        ),
    }
    provisional = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional.encode())
        + len("\n".join(OUTPUT_LINES).encode())
        + 4096
        < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE737_RING_FAMILY_UNIFORMITY_PASS"
        if report["pass"]
        else "CYCLE737_RING_FAMILY_UNIFORMITY_HONEST_FAIL"
    )
    report["report_sha256"] = digest_json(report)
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
