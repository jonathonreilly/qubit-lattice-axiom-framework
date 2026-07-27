#!/usr/bin/env python3
"""Independent symbolic route replay for the Cycle714 full34 packet word.

This checker deliberately proves only placement/routing statements.  It loads
the candidate packet's *unrouted* semantic word, independently reconstructs
the Cycle-713 endpoint-instrument physical word from landed Cycle-712
components, composes the two at the retained pointer coordinate, and then
tracks immutable logical wire labels through every emitted route SWAP.

No state-vector, phase, occurrence, time, Record, or Born-law conclusion is
drawn from the symbolic label calculation.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26 as P714

AUDIT_TIMEOUT_SEC = 300
NOTE_PATH = (
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_"
    "CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_"
    "CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_"
    "CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/"
    "CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "scripts/frontier_cycle714_full34_fixed_packet_independent_route_replay_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
Coord = tuple[int, int, int]


def one(kind: str, wire: int, matrix: np.ndarray) -> C712.AGate:
    return C712.AGate(kind, (wire,), matrix)


def two(kind: str, left: int, right: int, matrix: np.ndarray) -> C712.AGate:
    return C712.AGate(kind, (left, right), matrix)


def exact_toffoli_word(a: int, b: int, target: int) -> tuple[C712.AGate, ...]:
    """Independent spelling of the standard exact 15-factor H/T/CNOT word."""
    t = np.diag((1.0, np.exp(0.25j * np.pi))).astype(complex)
    tdg = t.conj().T
    h = C712.c707.c655.H
    cnot = C712.c707.c655.CNOT
    return (
        one("endpoint_OR_Toffoli_H", target, h),
        two("endpoint_OR_Toffoli_CNOT", b, target, cnot),
        one("endpoint_OR_Toffoli_Tdg", target, tdg),
        two("endpoint_OR_Toffoli_CNOT", a, target, cnot),
        one("endpoint_OR_Toffoli_T", target, t),
        two("endpoint_OR_Toffoli_CNOT", b, target, cnot),
        one("endpoint_OR_Toffoli_Tdg", target, tdg),
        two("endpoint_OR_Toffoli_CNOT", a, target, cnot),
        one("endpoint_OR_Toffoli_T", b, t),
        one("endpoint_OR_Toffoli_T", target, t),
        one("endpoint_OR_Toffoli_H", target, h),
        two("endpoint_OR_Toffoli_CNOT", a, b, cnot),
        one("endpoint_OR_Toffoli_T", a, t),
        one("endpoint_OR_Toffoli_Tdg", b, tdg),
        two("endpoint_OR_Toffoli_CNOT", a, b, cnot),
    )


def endpoint_register_word(
    left: int, right: int, du: int, dv: int, pointer: int
) -> tuple[tuple[C712.AGate, ...], tuple[C712.AGate, ...], tuple[C712.AGate, ...]]:
    cnot = C712.c707.c655.CNOT
    before = (
        two("endpoint_pre_left", left, du, cnot),
        two("endpoint_pre_right", right, dv, cnot),
    )
    after = (
        two("endpoint_post_left", left, du, cnot),
        two("endpoint_post_right", right, dv, cnot),
        two("endpoint_OR_CNOT", du, pointer, cnot),
        two("endpoint_OR_CNOT", dv, pointer, cnot),
    ) + exact_toffoli_word(du, dv, pointer)
    clean = (
        two("endpoint_clean_left_from_left", left, du, cnot),
        two("endpoint_clean_left_from_right", right, du, cnot),
        two("endpoint_clean_right_from_left", left, dv, cnot),
        two("endpoint_clean_right_from_right", right, dv, cnot),
    )
    return before, after, clean


def instrumented_decoded_word() -> tuple[C712.AGate, ...]:
    decoded, _qr_residual = C712.decoded_word(2)
    first_seam = next(i for i, gate in enumerate(decoded) if gate.kind == "seam_FSWAP")
    first_contact = next(i for i, gate in enumerate(decoded) if gate.kind == "onsite_contact")
    aux_base = C712.C709.G.build_equivalence(((0, 0, 0), (1, 0, 0))).equivalence.qubits
    before, after, clean = endpoint_register_word(1, 6, aux_base, aux_base + 1, aux_base + 2)
    return (
        tuple(decoded[:first_seam])
        + before
        + tuple(decoded[first_seam:first_contact])
        + after
        + clean
        + tuple(decoded[first_contact:])
    )


def word_signature(word):
    return tuple(
        (gate.kind, gate.wires, C712.c707.c655.matrix_digest(gate.matrix))
        for gate in word
    )


def pointer_sites(
    wire_sites: tuple[Coord, ...], occupied: tuple[Coord, ...]
) -> tuple[Coord, Coord, Coord]:
    left, right = wire_sites[1], wire_sites[6]
    candidates = []
    occupied_set = set(occupied)
    for x in range(min(left[0], right[0]) - 2, max(left[0], right[0]) + 3):
        for y in range(min(left[1], right[1]) - 2, max(left[1], right[1]) + 3):
            for z in range(min(left[2], right[2]) - 2, max(left[2], right[2]) + 3):
                site = (x, y, z)
                if site in occupied_set:
                    continue
                dl = sum(abs(site[i] - left[i]) for i in range(3))
                dr = sum(abs(site[i] - right[i]) for i in range(3))
                candidates.append((max(dl, dr), dl + dr, site))
    result = tuple(row[2] for row in sorted(candidates)[:3])
    if len(result) != 3 or len(set(result)) != 3:
        raise AssertionError("failed to allocate endpoint register")
    return result


@dataclass(frozen=True)
class BuiltWord:
    endpoint: tuple[C712.c707.Instruction, ...]
    packet: tuple[C712.c707.Instruction, ...]
    combined: tuple[C712.c707.Instruction, ...]
    matter_sites: tuple[Coord, ...]
    endpoint_sites: tuple[Coord, Coord, Coord]
    packet_sites: tuple[Coord, ...]
    assigned: frozenset[Coord]


def build_word() -> BuiltWord:
    cells = ((0, 0, 0), (1, 0, 0))
    eq = C712.C709.G.build_equivalence(cells).equivalence
    _eq2, graph, site_map, gauges, occupied, collisions = C712.P709.placement_bundle(cells)
    if collisions:
        raise AssertionError(("landed placement collision", collisions))
    carriers = C712.carriers_for(eq, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(i for i, carrier in enumerate(carriers) if len(carrier) == 2)
    endpoint_sites = pointer_sites(wire_sites, occupied)
    extended_sites = wire_sites + endpoint_sites
    target_decode = C712.synthesize_decode(eq.target_w, eq.target_v)
    target_encode = C712.inverse_word(target_decode)
    cnot = C712.c707.c655.CNOT
    endpoint = (
        tuple(
            C712.c707.Instruction("endpoint_repetition_decode_CNOT", carriers[i], cnot)
            for i in repeated
        )
        + C712.abstract_to_physical(target_decode, extended_sites, "endpoint_target_decode_")
        + C712.abstract_to_physical(
            instrumented_decoded_word(), extended_sites, "endpoint_decoded_"
        )
        + C712.abstract_to_physical(target_encode, extended_sites, "endpoint_target_encode_")
        + tuple(
            C712.c707.Instruction("endpoint_repetition_encode_CNOT", carriers[i], cnot)
            for i in reversed(repeated)
        )
    )

    # Independently reproduce the candidate's declared bounded site allocator.
    occupied_all = set(occupied) | set(endpoint_sites)
    candidates: list[Coord] = []
    for radius in range(1, 12):
        for x in range(-radius, radius + 1):
            for y in range(-radius, radius + 1):
                for z in range(-radius, radius + 1):
                    site = (x, y, z)
                    if (
                        max(abs(x), abs(y), abs(z)) == radius
                        and site not in occupied_all
                        and site not in candidates
                    ):
                        candidates.append(site)
                    if len(candidates) >= P714.N:
                        break
                if len(candidates) >= P714.N:
                    break
            if len(candidates) >= P714.N:
                break
        if len(candidates) >= P714.N:
            break
    fresh = iter(candidates)
    packet_sites = tuple(
        endpoint_sites[2] if wire == P714.POINTER else next(fresh)
        for wire in range(P714.N)
    )
    matrix = {
        "H": P714.H,
        "T": P714.T,
        "TD": P714.TD,
        "CNOT": P714.CNOT,
    }
    packet = tuple(
        C712.c707.Instruction(
            "packet_" + kind,
            tuple(packet_sites[wire] for wire in wires),
            matrix[kind],
        )
        for kind, wires in P714.expanded(P714.word())
    )
    assigned = frozenset(occupied_all | set(packet_sites))
    if packet_sites[P714.POINTER] != endpoint_sites[2]:
        raise AssertionError("endpoint and packet do not share pointer M2")
    return BuiltWord(
        endpoint=endpoint,
        packet=packet,
        combined=endpoint + packet,
        matter_sites=tuple(occupied),
        endpoint_sites=endpoint_sites,
        packet_sites=packet_sites,
        assigned=assigned,
    )


def l1(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def macro_lengths(word: tuple[C712.c707.Instruction, ...]) -> tuple[int, ...]:
    output = []
    for instruction in word:
        if len(instruction.sites) == 1:
            output.append(1)
        elif len(instruction.sites) == 2:
            output.append(2 * l1(*instruction.sites) - 1)
        else:
            raise AssertionError(("instruction arity", len(instruction.sites)))
    return tuple(output)


def replay(
    word: tuple[C712.c707.Instruction, ...],
    routed: tuple[C712.c707.c655.Gate, ...],
    *,
    deleted_index: int | None = None,
    check_active: bool = True,
) -> dict[str, object]:
    coordinates = {site for instruction in word for site in instruction.sites}
    coordinates |= {site for gate in routed for site in gate.sites}
    labels = {site: site for site in coordinates}
    cursor = 0
    active_gate_failures = matrix_failures = 0
    route_matrix_failures = arity_failures = adjacency_failures = 0
    lengths = macro_lengths(word)
    for instruction, length in zip(word, lengths):
        macro = routed[cursor:cursor + length]
        if len(macro) != length:
            raise AssertionError("truncated routed macro")
        active_seen = 0
        for local_index, gate in enumerate(macro):
            global_index = cursor + local_index
            arity_failures += len(gate.sites) not in (1, 2)
            adjacency_failures += len(gate.sites) == 2 and l1(*gate.sites) != 1
            if global_index == deleted_index:
                continue
            if gate.kind == "route_swap":
                route_matrix_failures += not np.array_equal(
                    gate.matrix, C712.c707.c655.SWAP
                )
                left, right = gate.sites
                labels[left], labels[right] = labels[right], labels[left]
                continue
            active_seen += 1
            if check_active:
                active_gate_failures += (
                    gate.kind != instruction.kind
                    or tuple(labels[site] for site in gate.sites) != instruction.sites
                )
                matrix_failures += not np.array_equal(gate.matrix, instruction.matrix)
        if deleted_index is None or not (cursor <= deleted_index < cursor + length):
            active_gate_failures += active_seen != 1
        cursor += length
    if cursor != len(routed):
        raise AssertionError(("unconsumed routed gates", cursor, len(routed)))
    changed = tuple(sorted(site for site in coordinates if labels[site] != site))
    return {
        "logical_instructions": len(word),
        "routed_gates": len(routed),
        "active_order_or_kind_failures": active_gate_failures,
        "active_matrix_failures": matrix_failures,
        "route_SWAP_matrix_failures": route_matrix_failures,
        "arity_failures": arity_failures,
        "nearest_neighbor_failures": adjacency_failures,
        "final_permutation_identity": not changed,
        "final_nonidentity_coordinates": changed,
    }


def route_return_deletion(
    word: tuple[C712.c707.Instruction, ...],
    routed: tuple[C712.c707.c655.Gate, ...],
) -> dict[str, object]:
    cursor = 0
    deleted = None
    for instruction, length in zip(word, macro_lengths(word)):
        macro = routed[cursor:cursor + length]
        active = next(i for i, gate in enumerate(macro) if gate.kind != "route_swap")
        returns = [i for i, gate in enumerate(macro) if i > active and gate.kind == "route_swap"]
        if returns:
            deleted = cursor + returns[0]
            break
        cursor += length
    if deleted is None:
        raise AssertionError("no active route-return SWAP found")
    damaged = replay(word, routed, deleted_index=deleted, check_active=False)
    return {
        "deleted_routed_gate_index": deleted,
        "deleted_gate_kind": routed[deleted].kind,
        "final_permutation_nonidentity": not damaged["final_permutation_identity"],
        "nonidentity_coordinate_count": len(damaged["final_nonidentity_coordinates"]),
    }


def transform(frame: np.ndarray, site: Coord) -> Coord:
    value = frame @ np.asarray(site, dtype=int)
    return tuple(int(x) for x in value)


def rotate_instruction(frame: np.ndarray, instruction):
    return C712.c707.Instruction(
        instruction.kind,
        tuple(transform(frame, site) for site in instruction.sites),
        instruction.matrix,
    )


def rotate_gate(frame: np.ndarray, gate):
    return C712.c707.c655.Gate(
        gate.kind,
        tuple(transform(frame, site) for site in gate.sites),
        gate.matrix,
    )


def covariance_certificate(word, routed) -> dict[str, object]:
    frames = C712.C709.F.base.proper_cubic_frames()
    replay_failures = 0
    for frame in frames:
        rotated_word = tuple(rotate_instruction(frame, instruction) for instruction in word)
        rotated_routed = tuple(rotate_gate(frame, gate) for gate in routed)
        row = replay(rotated_word, rotated_routed)
        replay_failures += sum(
            int(row[key])
            for key in (
                "active_order_or_kind_failures",
                "active_matrix_failures",
                "route_SWAP_matrix_failures",
                "arity_failures",
                "nearest_neighbor_failures",
            )
        )
        replay_failures += not row["final_permutation_identity"]
    touched = {site for gate in routed for site in gate.sites}
    composition_failures = 0
    for left in frames:
        for right in frames:
            product = left @ right
            for site in touched:
                composition_failures += (
                    transform(left, transform(right, site)) != transform(product, site)
                )
    return {
        "proper_cubic_frames": len(frames),
        "rotated_routed_word_replay_failures": replay_failures,
        "ordered_frame_products": len(frames) ** 2,
        "coordinate_composition_rows": len(frames) ** 2 * len(touched),
        "coordinate_composition_failures": composition_failures,
        "scope": (
            "passive coordinate transport of the already routed ordered word; "
            "this does not derive active coframes or a covariant route scheduler"
        ),
    }


def main() -> None:
    provenance = P714.provenance_certificate(AUDIT_INPUT_PATHS, __file__)
    source_closure = (
        provenance["baseline_is_ancestor"]
        and provenance["declared_path_failures"] == 0
        and provenance["duplicate_declared_paths"] == 0
        and not provenance["missing_transitive_scripts"]
        and not provenance["missing_dynamic_scripts"]
        and not provenance["untracked_inputs"]
    )
    actual_cycle713_word, _actual_qr = C713.instrumented_decoded_word(2)
    independent_cycle713_word = instrumented_decoded_word()
    endpoint_word_signature_failures = sum(
        left != right for left, right in zip(
            word_signature(actual_cycle713_word),
            word_signature(independent_cycle713_word),
        )
    ) + abs(len(actual_cycle713_word) - len(independent_cycle713_word))
    built = build_word()
    endpoint_routed, endpoint_route = C712.c707.route_word(built.endpoint)
    packet_routed, packet_route = C712.c707.route_word(built.packet)
    routed, route_report = C712.c707.route_word(built.combined)
    independent = replay(built.combined, routed)
    deletion = route_return_deletion(built.combined, routed)
    covariance = covariance_certificate(built.combined, routed)
    touched = set(route_report["touched_coordinates"])
    packet_new = set(built.packet_sites) - {built.endpoint_sites[2]}
    allocation_collision_count = (
        len(built.matter_sites) + len(built.endpoint_sites) + len(packet_new)
        - len(built.assigned)
    )
    combined_digest = sha256(
        "".join(
            gate.kind
            + repr(gate.sites)
            + C712.c707.c655.matrix_digest(gate.matrix)
            for gate in routed
        ).encode()
    ).hexdigest()
    cycle713_pointer_sites = tuple(C713.physical_word_certificate(2)["pointer_sites"])
    report = {
        "declared_inputs": AUDIT_INPUT_PATHS,
        "provenance": provenance,
        "source_closure": source_closure,
        "scientific_scope": (
            "independent symbolic routing/wire-label replay only; the packet candidate's "
            "separate Boolean/action checks carry the semantic claim; the independently reconstructed "
            "endpoint word is required to match the repaired Cycle713 literal word exactly"
        ),
        "independent_endpoint_word_signature_failures": endpoint_word_signature_failures,
        "matter_assigned_M2": len(built.matter_sites),
        "endpoint_register_M2": len(built.endpoint_sites),
        "packet_interface_M2": len(built.packet_sites),
        "packet_new_M2": len(packet_new),
        "combined_assigned_M2": len(built.assigned),
        "allocation_collision_count": allocation_collision_count,
        "shared_pointer_site": built.endpoint_sites[2],
        "Cycle713_pointer_sites": cycle713_pointer_sites,
        "independent_pointer_sites_match_Cycle713": (
            built.endpoint_sites == cycle713_pointer_sites
        ),
        "shared_pointer_exactly_once_in_packet_map": (
            built.packet_sites.count(built.endpoint_sites[2]) == 1
            and built.packet_sites[P714.POINTER] == built.endpoint_sites[2]
        ),
        "endpoint_primitive_gates": len(built.endpoint),
        "packet_primitive_gates": len(built.packet),
        "combined_primitive_gates": len(built.combined),
        "endpoint_routed_gates": len(endpoint_routed),
        "packet_routed_gates": len(packet_routed),
        "combined_routed_gates": len(routed),
        "component_routed_count_additive": (
            len(routed) == len(endpoint_routed) + len(packet_routed)
        ),
        "endpoint_maximum_route_distance": endpoint_route["maximum_route_distance"],
        "packet_maximum_route_distance": packet_route["maximum_route_distance"],
        "combined_maximum_route_distance": route_report["maximum_route_distance"],
        "combined_touched_M2": len(touched),
        "combined_route_only_M2": len(touched - set(built.assigned)),
        "combined_assigned_or_touched_union_M2": len(touched | set(built.assigned)),
        "combined_routed_word_sha256": combined_digest,
        "route_api_digest_matches": combined_digest == route_report["word_sha256"],
        "routed_gate_kinds": dict(Counter(gate.kind for gate in routed)),
        "independent_symbolic_replay": independent,
        "active_route_return_deletion": deletion,
        "proper_cubic_covariance": covariance,
    }
    checks = {
        "source_closure": source_closure,
        "Cycle713_literal_word_match": endpoint_word_signature_failures == 0,
        "recomputed_100_M2": len(built.assigned) == 100 and allocation_collision_count == 0,
        "shared_pointer": report["shared_pointer_exactly_once_in_packet_map"]
        and report["independent_pointer_sites_match_Cycle713"],
        "exact_combined_resources": len(built.combined) == 2118
        and len(routed) == 20396 and len(touched) == 548
        and len(touched - set(built.assigned)) == 454
        and len(touched | set(built.assigned)) == 554
        and route_report["maximum_route_distance"] == 24
        and combined_digest
        == "d197bed4fda6a3d18c65852757478278aec54f3fb19ba8f404fd6d350649f3de",
        "resource_additivity": report["component_routed_count_additive"],
        "route_digest": report["route_api_digest_matches"],
        "ordered_logical_replay": independent["active_order_or_kind_failures"] == 0,
        "gate_matrices": independent["active_matrix_failures"] == 0
        and independent["route_SWAP_matrix_failures"] == 0,
        "bounded_gate_grammar": independent["arity_failures"] == 0
        and independent["nearest_neighbor_failures"] == 0,
        "route_return_identity": independent["final_permutation_identity"],
        "route_return_deletion": deletion["final_permutation_nonidentity"],
        "proper_cubic_24_576": covariance["proper_cubic_frames"] == 24
        and covariance["ordered_frame_products"] == 576
        and covariance["rotated_routed_word_replay_failures"] == 0
        and covariance["coordinate_composition_failures"] == 0,
    }
    report["checks"] = checks
    report["pass"] = all(checks.values())
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, default=str, separators=(",", ":")
    ).encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True))
    print(
        "CYCLE714_FULL34_PACKET_ROUTE_REPLAY_PASS"
        if report["pass"]
        else "CYCLE714_FULL34_PACKET_ROUTE_REPLAY_FAIL"
    )
    if not report["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
