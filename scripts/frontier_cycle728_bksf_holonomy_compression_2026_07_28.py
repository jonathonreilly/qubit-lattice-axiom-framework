#!/usr/bin/env python3
"""Bounded finite-ring check of a declared marked-edge GF(2) row system.

The local rows checked here are exactly

    L_s    = A_s XOR B_s XOR ref_s XOR ref_(s+1),       s != s*
    L_{s*} = A_s XOR B_s XOR ref_s XOR ref_(s+1) XOR h.

Here s* is the lexicographically first ring edge and h is one declared supplied
auxiliary bit.  The original chained-agreement proposal remains below as a
correction record: on a closed ring it is the state-independent affine
constant ``n mod 2``, not a variable reference degree of freedom.  The edge
choice and any "holonomy" or controller-level interpretation are not derived.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import random
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md"
K_INPUT_PATH = "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py"
G703_INPUT_PATH = "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py"
AUDIT_INPUT_PATHS = (
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
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
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
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle703_local_gauss_reference_adversary_2026_07_25 as G703


# Freeze-then-verify constants.  These are source literals, not populated from
# the runtime results.
FROZEN_PROGRAM_CENSUS = (
    (
        "bank2_unpadded",
        2,
        11,
        (
            ("bank", 2),
            ("cross", 1),
            ("finalizer", 1),
            ("handoff", 2),
            ("relay", 4),
            ("source", 1),
        ),
    ),
    (
        "bank5_unpadded",
        5,
        35,
        (
            ("bank", 5),
            ("cross", 4),
            ("finalizer", 1),
            ("handoff", 8),
            ("relay", 16),
            ("source", 1),
        ),
    ),
    (
        "bank12_padded130",
        12,
        130,
        (
            ("bank", 12),
            ("cross", 11),
            ("finalizer", 1),
            ("handoff", 22),
            ("identity", 39),
            ("relay", 44),
            ("source", 1),
        ),
    ),
)
FROZEN_SUPPORT_CENSUS = (
    ("bank2_unpadded", 11, 11, 4, 4, 1),
    ("bank5_unpadded", 35, 35, 4, 4, 1),
    ("bank12_padded130", 130, 130, 4, 4, 1),
)
FROZEN_AMENDED_SUPPORT_CENSUS = (
    ("bank2_unpadded", 11, 11, 4, 5, 1, (0,), (0, 1)),
    ("bank5_unpadded", 35, 35, 4, 5, 1, (0,), (0, 1)),
    ("bank12_padded130", 130, 130, 4, 5, 1, (0,), (0, 1)),
)
FROZEN_CONTROL_CENSUS = (
    ("bank2_unpadded", 11, 2, 1),
    ("bank5_unpadded", 35, 2, 1),
    ("bank12_padded130", 130, 2, 1),
)
FROZEN_TWIST_CONTROL_CENSUS = (
    ("bank2_unpadded", 11, (0, 1), 1, 1),
    ("bank5_unpadded", 35, (0, 1), 1, 1),
    ("bank12_padded130", 130, (0, 1), 1, 1),
)
FROZEN_ENUMERATION_CENSUS = (
    ("ring_stations", 11),
    ("rail_bits", 22),
    ("rail_states", 4194304),
    ("method", "exhaustive_all_2^(2*11)_rail_states"),
)
FROZEN_EXHAUSTIVE_RESULT_CENSUS = (
    ("telescope_failures", 0),
    ("local_satisfied_states", 2048),
    ("local_satisfied_even_token_states", 2048),
    ("local_satisfied_token_agreement_expression_matches", 0),
    ("token_parity_equals_agreement_expression_states", 2097152),
    ("exact_sector_separation_failures", 2099200),
)
FROZEN_AMENDED_H_SECTOR_CENSUS = (
    (
        ("h", 0),
        ("rail_states", 4194304),
        ("twist_telescope_failures", 0),
        ("fixed_ref_satisfied_states", 2048),
        ("fixed_ref_matching_states", 2048),
        ("compression_a_failures", 0),
        ("token_parity_sector_states", 2097152),
        ("projected_satisfied_states", 2097152),
        ("projected_exact_separation_failures", 0),
        ("canonical_extension_failures", 0),
        ("complement_extension_failures", 0),
        ("satisfying_reference_extensions", 4194304),
    ),
    (
        ("h", 1),
        ("rail_states", 4194304),
        ("twist_telescope_failures", 0),
        ("fixed_ref_satisfied_states", 2048),
        ("fixed_ref_matching_states", 2048),
        ("compression_a_failures", 0),
        ("token_parity_sector_states", 2097152),
        ("projected_satisfied_states", 2097152),
        ("projected_exact_separation_failures", 0),
        ("canonical_extension_failures", 0),
        ("complement_extension_failures", 0),
        ("satisfying_reference_extensions", 4194304),
    ),
)
FROZEN_CHAINED_REFERENCE_CENSUS = (
    (
        ("stations", 10),
        ("reference_states", 1024),
        ("agreement_value_census", (("0", 1024),)),
        ("disagreement_value_census", (("0", 1024),)),
    ),
    (
        ("stations", 11),
        ("reference_states", 2048),
        ("agreement_value_census", (("1", 2048),)),
        ("disagreement_value_census", (("0", 2048),)),
    ),
)
FROZEN_R1_PULLBACK = (
    ("A", 0),
    ("B", 0),
    ("ref", 0),
    ("ref", 1),
)
FROZEN_R2_PULLBACK = (
    ("B", -1),
    ("A", 1),
    ("ref", 0),
    ("ref", 1),
)
FROZEN_R_PULLBACK = (
    ("A", -1),
    ("B", 1),
    ("ref", 0),
    ("ref", 1),
)
FROZEN_R_ROW_SET_PERMUTED = False
FROZEN_R_COUNTEREXAMPLE = (
    ("ring_stations", 11),
    ("A_before_mask", 1),
    ("B_before_mask", 1),
    ("refs_mask", 0),
    ("syndrome_before_mask", 0),
    ("syndrome_after_mask", 1026),
)
FROZEN_WITNESS_PAIR = (
    (
        ("ring_stations", 11),
        ("A_mask", 0),
        ("B_mask", 0),
        ("refs_mask", 0),
    ),
    (
        ("ring_stations", 11),
        ("A_mask", 0),
        ("B_mask", 0),
        ("refs_mask", 2047),
    ),
)
FROZEN_MARKED_EDGE_WITNESS_PAIR = (
    (
        ("ring_stations", 11),
        ("A_mask", 0),
        ("B_mask", 0),
        ("refs_mask", 0),
        ("h", 0),
    ),
    (
        ("ring_stations", 11),
        ("A_mask", 4),
        ("B_mask", 0),
        ("refs_mask", 6),
        ("h", 1),
    ),
)
FROZEN_RADIUS1_WINDOW_CENSUS = (
    ("ring_stations", 11),
    ("marked_edge", (0, 1)),
    ("radius", 1),
    ("windows_excluding_marked_edge", 9),
    ("windows_with_window_specific_indistinguishable_witness", 9),
    ("rail_ref_bits_per_window", 9),
    ("maximum_observed_bit_differences", 0),
    ("minimum_token_flip_distance", 2),
    ("representative_window_center", 8),
    ("representative_window_sites", (7, 8, 9)),
    ("representative_pair_indistinguishable_windows", 7),
)
EXHAUSTIVE_SEED = b"cycle728-bksf-holonomy-compression-ring11"
STDOUT_LIMIT_BYTES = 20_000


OUTPUT_LINES: list[str] = []
CHECKS: dict[str, bool] = {}
CHECK_DETAILS: dict[str, object] = {}


def compact(value: object, limit: int = 180) -> str:
    rendered = json.dumps(value, sort_keys=True, default=str, separators=(",", ":"))
    if len(rendered) <= limit:
        return rendered
    digest = sha256(rendered.encode()).hexdigest()
    return json.dumps(
        {"bounded_digest_sha256": digest, "unbounded_characters": len(rendered)},
        sort_keys=True,
        separators=(",", ":"),
    )


def emit(line: str = "") -> None:
    OUTPUT_LINES.append(line)


def check(label: str, condition: bool, detail: object = "") -> None:
    if label in CHECKS:
        raise AssertionError(f"duplicate check label: {label}")
    passed = bool(condition)
    CHECKS[label] = passed
    CHECK_DETAILS[label] = detail
    emit(f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}")


def parity_tuple(bits: tuple[int, ...]) -> int:
    """Use the public Cycle-703 prefix-parity machinery at full width."""

    return G703.parity_before(bits, len(bits))


def mask_to_tuple(value: int, width: int) -> tuple[int, ...]:
    return tuple((value >> station) & 1 for station in range(width))


def tuple_to_mask(bits: tuple[int, ...]) -> int:
    return sum(bit << station for station, bit in enumerate(bits))


def rotate_to_next_source(value: int, stations: int) -> int:
    """Bit s of the result is input bit s+1 (indices modulo stations)."""

    mask = (1 << stations) - 1
    return (value >> 1) | ((value & 1) << (stations - 1)) & mask


def rotate_from_previous_source(value: int, stations: int) -> int:
    """Bit s of the result is input bit s-1 (indices modulo stations)."""

    mask = (1 << stations) - 1
    return ((value << 1) & mask) | (value >> (stations - 1))


def local_syndrome_mask(a: int, b: int, refs: int, stations: int) -> int:
    mask = (1 << stations) - 1
    next_refs = rotate_to_next_source(refs, stations)
    return (a ^ b ^ refs ^ next_refs) & mask


def lexicographically_first_edge(stations: int) -> tuple[int, int]:
    """The supplied marking convention, derived rather than special-cased."""

    return min((station, (station + 1) % stations) for station in range(stations))


def marked_station(stations: int) -> int:
    return lexicographically_first_edge(stations)[0]


def twisted_local_syndrome_mask(
    a: int,
    b: int,
    refs: int,
    h: int,
    stations: int,
) -> int:
    """Amended rows, with h entering exactly the lexicographically first edge."""

    if h not in (0, 1):
        raise ValueError(h)
    return local_syndrome_mask(a, b, refs, stations) ^ (
        h << marked_station(stations)
    )


def token_parity(a: int, b: int) -> int:
    return (a ^ b).bit_count() & 1


def chained_agreement_expression(refs: int, stations: int) -> int:
    """XOR of XNOR(ref_s, ref_(s+1)) around the ring."""

    mask = (1 << stations) - 1
    disagreements = refs ^ rotate_to_next_source(refs, stations)
    agreements = (~disagreements) & mask
    return agreements.bit_count() & 1


def closed_ring_difference_coboundary(refs: int, stations: int) -> int:
    """XOR of ref_s XOR ref_(s+1), included to close terminology ambiguity."""

    disagreements = refs ^ rotate_to_next_source(refs, stations)
    return disagreements.bit_count() & 1


def candidate_reference_global_bit(refs: int) -> int:
    """A nonlocal candidate distinguished by the frozen complement witness.

    This is reported only as a diagnostic.  It is not substituted for the
    proposed consecutive-agreement expression.
    """

    return refs.bit_count() & 1


def r1_state(a: int, b: int, stations: int) -> tuple[int, int]:
    del stations
    return b, a


def r2_state(a: int, b: int, stations: int) -> tuple[int, int]:
    return (
        rotate_from_previous_source(b, stations),
        rotate_to_next_source(a, stations),
    )


def r_state(a: int, b: int, stations: int) -> tuple[int, int]:
    after_a, after_b = r1_state(a, b, stations)
    return r2_state(after_a, after_b, stations)


def row_value(
    a: int,
    b: int,
    refs: int,
    station: int,
    stations: int,
) -> int:
    return (
        ((a >> station) & 1)
        ^ ((b >> station) & 1)
        ^ ((refs >> station) & 1)
        ^ ((refs >> ((station + 1) % stations)) & 1)
    )


def pullback_value(
    a: int,
    b: int,
    refs: int,
    station: int,
    stations: int,
    frozen_law: tuple[tuple[str, int], ...],
) -> int:
    values = {"A": a, "B": b, "ref": refs}
    output = 0
    for kind, offset in frozen_law:
        output ^= (values[kind] >> ((station + offset) % stations)) & 1
    return output


def derive_pullback_offsets(
    layer,
    stations: int,
) -> frozenset[tuple[str, int]]:
    """Derive the pullback of L_0 from all single-variable basis inputs."""

    influences = set()
    for kind in ("A", "B", "ref"):
        for source in range(stations):
            a = 1 << source if kind == "A" else 0
            b = 1 << source if kind == "B" else 0
            refs = 1 << source if kind == "ref" else 0
            after_a, after_b = layer(a, b, stations)
            if row_value(after_a, after_b, refs, 0, stations):
                signed_offset = source if source <= stations // 2 else source - stations
                influences.add((kind, signed_offset))
    return frozenset(influences)


def verify_pullback_law(
    layer,
    stations: int,
    frozen_law: tuple[tuple[str, int], ...],
) -> int:
    """Basis-exact verification; all checked expressions are GF(2)-linear."""

    failures = 0
    for kind in ("A", "B", "ref"):
        for source in range(stations):
            a = 1 << source if kind == "A" else 0
            b = 1 << source if kind == "B" else 0
            refs = 1 << source if kind == "ref" else 0
            after_a, after_b = layer(a, b, stations)
            for station in range(stations):
                observed = row_value(
                    after_a, after_b, refs, station, stations
                )
                expected = pullback_value(
                    a, b, refs, station, stations, frozen_law
                )
                failures += observed != expected
    return failures


def toggle(symbols: set[tuple[str, int]], symbol: tuple[str, int]) -> None:
    if symbol in symbols:
        symbols.remove(symbol)
    else:
        symbols.add(symbol)


def pullback_row_symbols(
    station: int,
    stations: int,
    frozen_law: tuple[tuple[str, int], ...],
) -> frozenset[tuple[str, int]]:
    return frozenset(
        (kind, (station + offset) % stations)
        for kind, offset in frozen_law
    )


def telescope_symbols(
    stations: int,
    frozen_law: tuple[tuple[str, int], ...],
) -> frozenset[tuple[str, int]]:
    symbols: set[tuple[str, int]] = set()
    for station in range(stations):
        for symbol in pullback_row_symbols(station, stations, frozen_law):
            toggle(symbols, symbol)
    return frozenset(symbols)


def expected_global_symbols(stations: int) -> frozenset[tuple[str, int]]:
    return frozenset(
        [(kind, station) for kind in ("A", "B") for station in range(stations)]
    )


def amended_telescope_symbols(
    stations: int,
    frozen_law: tuple[tuple[str, int], ...],
) -> frozenset[tuple[str, int]]:
    symbols = set(telescope_symbols(stations, frozen_law))
    toggle(symbols, ("h", marked_station(stations)))
    return frozenset(symbols)


def expected_amended_global_symbols(
    stations: int,
) -> frozenset[tuple[str, int]]:
    return expected_global_symbols(stations) | {
        ("h", marked_station(stations))
    }


def canonical_reference_extension(
    a: int,
    b: int,
    h: int,
    stations: int,
) -> tuple[int, int]:
    """Return the ref_0=0 recurrence and its ring-closure obstruction.

    The obstruction is token_parity XOR h.  When it vanishes, the returned
    chain and its global complement are the two satisfying ref extensions.
    """

    mask = (1 << stations) - 1
    prefix = (a ^ b) & mask
    shift = 1
    while shift < stations:
        prefix ^= (prefix << shift) & mask
        shift <<= 1
    refs = (prefix << 1) & mask
    if h:
        refs ^= mask ^ 1
    closure_obstruction = token_parity(a, b) ^ h
    return refs, closure_obstruction


def row_family_is_permuted(
    stations: int,
    frozen_law: tuple[tuple[str, int], ...],
) -> tuple[bool, tuple[int | None, ...]]:
    original = tuple(
        pullback_row_symbols(station, stations, FROZEN_R1_PULLBACK)
        for station in range(stations)
    )
    transformed = tuple(
        pullback_row_symbols(station, stations, frozen_law)
        for station in range(stations)
    )
    permutation = []
    for row in transformed:
        matches = tuple(index for index, candidate in enumerate(original) if row == candidate)
        permutation.append(matches[0] if len(matches) == 1 else None)
    return all(index is not None for index in permutation), tuple(permutation)


def program_rows() -> tuple[tuple[str, int, tuple[object, ...]], ...]:
    return (
        ("bank2_unpadded", 2, K.interleaved_program(2)),
        ("bank5_unpadded", 5, K.interleaved_program(5)),
        (
            "bank12_padded130",
            12,
            K.interleaved_program(12, physical_padding=True),
        ),
    )


def observed_program_census(
    programs: tuple[tuple[str, int, tuple[object, ...]], ...],
) -> tuple[object, ...]:
    rows = []
    for name, banks, program in programs:
        kinds = tuple(sorted(Counter(row[0] for row in program).items()))
        rows.append((name, banks, len(program), kinds))
    return tuple(rows)


def mode_graph_table(
    programs: tuple[tuple[str, int, tuple[object, ...]], ...],
) -> tuple[str, ...]:
    rows = (
        "MODE_GRAPH_TABLE",
        "program | station | vertex | mode_pair | ring_edge | reference_chain",
    )
    body = []
    for name, _banks, program in programs:
        stations = len(program)
        for station in range(stations):
            neighbor = (station + 1) % stations
            body.append(
                f"{name} | {station} | v_{station} | "
                f"(A_{station},B_{station}) | ({station},{neighbor}) | "
                f"(ref_{station},ref_{neighbor})"
            )
    return rows + tuple(body)


def support_census(
    programs: tuple[tuple[str, int, tuple[object, ...]], ...],
) -> tuple[object, ...]:
    rows = []
    for name, _banks, program in programs:
        stations = len(program)
        weights = []
        radii = []
        for station in range(stations):
            support = (
                ("A", station),
                ("B", station),
                ("ref", station),
                ("ref", (station + 1) % stations),
            )
            weights.append(len(set(support)))
            radii.append(
                max(
                    min(
                        (site - station) % stations,
                        (station - site) % stations,
                    )
                    for _kind, site in support
                )
            )
        rows.append(
            (
                name,
                stations,
                len(weights),
                min(weights),
                max(weights),
                max(radii),
            )
        )
    return tuple(rows)


def amended_support_census(
    programs: tuple[tuple[str, int, tuple[object, ...]], ...],
) -> tuple[object, ...]:
    rows = []
    for name, _banks, program in programs:
        stations = len(program)
        marked = marked_station(stations)
        marked_edge = lexicographically_first_edge(stations)
        weights = []
        radii = []
        h_read_rows = []
        for station in range(stations):
            support: tuple[tuple[str, object], ...] = (
                ("A", station),
                ("B", station),
                ("ref", station),
                ("ref", (station + 1) % stations),
            )
            if station == marked:
                support += (("h", marked_edge),)
                h_read_rows.append(station)
            weights.append(len(set(support)))
            radii.append(
                max(
                    0
                    if kind == "h"
                    else min(
                        (int(site) - station) % stations,
                        (station - int(site)) % stations,
                    )
                    for kind, site in support
                )
            )
        rows.append(
            (
                name,
                stations,
                len(weights),
                min(weights),
                max(weights),
                max(radii),
                tuple(h_read_rows),
                marked_edge,
            )
        )
    return tuple(rows)


def seeded_refs(stations: int) -> int:
    digest = sha256(EXHAUSTIVE_SEED).digest()
    return int.from_bytes(digest, "big") & ((1 << stations) - 1)


def exhaustive_ring11() -> dict[str, object]:
    stations = 11
    mask = (1 << stations) - 1
    marked = marked_station(stations)
    refs = seeded_refs(stations)
    ref_boundary = refs ^ rotate_to_next_source(refs, stations)
    agreement_value = chained_agreement_expression(refs, stations)
    total = 1 << (2 * stations)
    telescope_failures = 0
    local_satisfied = 0
    local_satisfied_even_token = 0
    local_satisfied_agreement_matches = 0
    exact_sector_separation_failures = 0
    parity_agreement_states = 0
    amended_by_h = [
        {
            "h": h,
            "rail_states": total,
            "twist_telescope_failures": 0,
            "fixed_ref_satisfied_states": 0,
            "fixed_ref_matching_states": 0,
            "compression_a_failures": 0,
            "token_parity_sector_states": 0,
            "projected_satisfied_states": 0,
            "projected_exact_separation_failures": 0,
            "canonical_extension_failures": 0,
            "complement_extension_failures": 0,
            "satisfying_reference_extensions": 0,
        }
        for h in (0, 1)
    ]
    for packed in range(total):
        a = packed & mask
        b = (packed >> stations) & mask
        syndrome = a ^ b ^ ref_boundary
        observed_telescope = syndrome.bit_count() & 1
        expected_telescope = token_parity(a, b)
        telescope_failures += observed_telescope != expected_telescope
        all_local = syndrome == 0
        lawful_parity = expected_telescope == agreement_value
        local_satisfied += all_local
        local_satisfied_even_token += all_local and expected_telescope == 0
        local_satisfied_agreement_matches += all_local and lawful_parity
        parity_agreement_states += lawful_parity
        exact_sector_separation_failures += all_local != lawful_parity
        canonical_refs, closure_obstruction = canonical_reference_extension(
            a, b, expected_telescope, stations
        )
        complement_refs = canonical_refs ^ mask
        for h in (0, 1):
            row = amended_by_h[h]
            twisted_syndrome = syndrome ^ (h << marked)
            observed_twist_telescope = twisted_syndrome.bit_count() & 1
            expected_twist_telescope = expected_telescope ^ h
            row["twist_telescope_failures"] += (
                observed_twist_telescope != expected_twist_telescope
            )
            amended_all_local = twisted_syndrome == 0
            token_in_sector = expected_telescope == h
            row["fixed_ref_satisfied_states"] += amended_all_local
            row["fixed_ref_matching_states"] += (
                amended_all_local and token_in_sector
            )
            row["compression_a_failures"] += (
                amended_all_local and not token_in_sector
            )
            row["token_parity_sector_states"] += token_in_sector

            # Project over the declared supplied ref chain.  Closure is the
            # necessary telescope obstruction; the canonical chain and its
            # complement construct the two solutions whenever it vanishes.
            projected_satisfied = closure_obstruction == 0 and h == expected_telescope
            if token_in_sector:
                canonical_failure = (
                    twisted_local_syndrome_mask(
                        a, b, canonical_refs, h, stations
                    )
                    != 0
                )
                complement_failure = (
                    twisted_local_syndrome_mask(
                        a, b, complement_refs, h, stations
                    )
                    != 0
                )
                row["canonical_extension_failures"] += canonical_failure
                row["complement_extension_failures"] += complement_failure
                projected_satisfied = not (
                    canonical_failure or complement_failure
                )
                row["satisfying_reference_extensions"] += (
                    2 if projected_satisfied else 0
                )
            row["projected_satisfied_states"] += projected_satisfied
            row["projected_exact_separation_failures"] += (
                projected_satisfied != token_in_sector
            )
    return {
        "enumeration": dict(FROZEN_ENUMERATION_CENSUS),
        "seed_sha256": sha256(EXHAUSTIVE_SEED).hexdigest(),
        "refs_mask": refs,
        "chained_agreement_expression": agreement_value,
        "telescope_failures": telescope_failures,
        "local_satisfied_states": local_satisfied,
        "local_satisfied_even_token_states": local_satisfied_even_token,
        "local_satisfied_token_agreement_expression_matches": (
            local_satisfied_agreement_matches
        ),
        "token_parity_equals_agreement_expression_states": parity_agreement_states,
        "exact_sector_separation_failures": exact_sector_separation_failures,
        "amended_by_h": tuple(amended_by_h),
    }


def verify_k_r_semantics(stations: int) -> dict[str, int]:
    identity_program = tuple(("identity", 0, ()) for _ in range(stations))
    basis_failures = 0
    for rail in ("A", "B"):
        for source in range(stations):
            a = 1 << source if rail == "A" else 0
            b = 1 << source if rail == "B" else 0
            _data, observed_a, observed_b = K.apply_controller_step(
                (),
                identity_program,
                mask_to_tuple(a, stations),
                mask_to_tuple(b, stations),
            )
            expected_a, expected_b = r_state(a, b, stations)
            basis_failures += (
                tuple_to_mask(observed_a) != expected_a
                or tuple_to_mask(observed_b) != expected_b
            )
    return {"stations": stations, "rail_basis_cases": 2 * stations, "failures": basis_failures}


def control_census(
    programs: tuple[tuple[str, int, tuple[object, ...]], ...],
) -> tuple[tuple[object, ...], ...]:
    rows = []
    for name, _banks, program in programs:
        stations = len(program)
        mask = (1 << stations) - 1
        digest = sha256((name + ":controls").encode()).digest()
        a = int.from_bytes(digest, "big") & mask
        b = int.from_bytes(digest[::-1], "big") & mask
        refs = int.from_bytes(sha256(digest).digest(), "big") & mask
        baseline = local_syndrome_mask(a, b, refs, stations)
        ref_counts = []
        a_counts = []
        for station in range(stations):
            ref_counts.append(
                (
                    baseline
                    ^ local_syndrome_mask(
                        a, b, refs ^ (1 << station), stations
                    )
                ).bit_count()
            )
            a_counts.append(
                (
                    baseline
                    ^ local_syndrome_mask(
                        a ^ (1 << station), b, refs, stations
                    )
                ).bit_count()
            )
        rows.append((name, stations, min(ref_counts), min(a_counts)))
        if set(ref_counts) != {2} or set(a_counts) != {1}:
            rows[-1] = (
                name,
                stations,
                tuple(sorted(Counter(ref_counts).items())),
                tuple(sorted(Counter(a_counts).items())),
            )
    return tuple(rows)


def twist_control_census(
    programs: tuple[tuple[str, int, tuple[object, ...]], ...],
) -> tuple[tuple[object, ...], ...]:
    rows = []
    for name, _banks, program in programs:
        stations = len(program)
        mask = (1 << stations) - 1
        digest = sha256((name + ":twist-control").encode()).digest()
        a = int.from_bytes(digest, "big") & mask
        b = int.from_bytes(digest[::-1], "big") & mask
        refs = int.from_bytes(sha256(digest).digest(), "big") & mask
        h_flip_mask = twisted_local_syndrome_mask(
            a, b, refs, 0, stations
        ) ^ twisted_local_syndrome_mask(a, b, refs, 1, stations)
        rows.append(
            (
                name,
                stations,
                lexicographically_first_edge(stations),
                h_flip_mask,
                h_flip_mask.bit_count(),
            )
        )
    return tuple(rows)


def permuted_telescope_control(stations: int) -> dict[str, object]:
    refs = seeded_refs(stations)
    mask = (1 << stations) - 1
    a = int.from_bytes(sha256(b"cycle728-order-A").digest(), "big") & mask
    b = int.from_bytes(sha256(b"cycle728-order-B").digest(), "big") & mask
    syndrome = local_syndrome_mask(a, b, refs, stations)
    rows = tuple((syndrome >> station) & 1 for station in range(stations))
    order = list(range(stations))
    random.Random(72820260728).shuffle(order)
    direct = parity_tuple(rows)
    shuffled = parity_tuple(tuple(rows[index] for index in order))
    return {
        "stations": stations,
        "direct_telescope": direct,
        "permuted_telescope": shuffled,
        "token_parity": token_parity(a, b),
        "permutation_sha256": sha256(repr(tuple(order)).encode()).hexdigest(),
        "invariant": direct == shuffled == token_parity(a, b),
    }


def frozen_witness_result() -> dict[str, object]:
    derived = (
        (
            ("ring_stations", 11),
            ("A_mask", 0),
            ("B_mask", 0),
            ("refs_mask", 0),
        ),
        (
            ("ring_stations", 11),
            ("A_mask", 0),
            ("B_mask", 0),
            ("refs_mask", (1 << 11) - 1),
        ),
    )
    rows = []
    for item in derived:
        state = dict(item)
        stations = state["ring_stations"]
        rows.append(
            {
                **state,
                "local_syndrome_mask": local_syndrome_mask(
                    state["A_mask"],
                    state["B_mask"],
                    state["refs_mask"],
                    stations,
                ),
                "token_parity": token_parity(state["A_mask"], state["B_mask"]),
                "chained_agreement_expression": chained_agreement_expression(
                    state["refs_mask"], stations
                ),
                "candidate_reference_global_bit": candidate_reference_global_bit(
                    state["refs_mask"]
                ),
            }
        )
    return {
        "derived_pair_matches_frozen_literal": derived == FROZEN_WITNESS_PAIR,
        "states": rows,
        "every_local_row_identical": rows[0]["local_syndrome_mask"]
        == rows[1]["local_syndrome_mask"],
        "every_local_row_satisfied": all(row["local_syndrome_mask"] == 0 for row in rows),
        "chained_agreement_expression_differs": rows[0][
            "chained_agreement_expression"
        ]
        != rows[1]["chained_agreement_expression"],
        "candidate_reference_global_bit_differs": rows[0]["candidate_reference_global_bit"]
        != rows[1]["candidate_reference_global_bit"],
    }


def radius_one_sites(center: int, stations: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            {
                (center - 1) % stations,
                center,
                (center + 1) % stations,
            }
        )
    )


def ring_distance(left: int, right: int, stations: int) -> int:
    return min((left - right) % stations, (right - left) % stations)


def radius_one_window_witness(center: int, stations: int) -> dict[str, object]:
    """Find a satisfying h-pair invisible on one window excluding s*."""

    sites = radius_one_sites(center, stations)
    edge = lexicographically_first_edge(stations)
    if set(edge) <= set(sites):
        raise ValueError(("window contains marked edge", center, sites, edge))
    window_mask = sum(1 << site for site in sites)
    full_mask = (1 << stations) - 1
    for token_site in range(stations):
        if token_site in edge or ring_distance(
            token_site, center, stations
        ) <= 1:
            continue
        a = 1 << token_site
        canonical_refs, obstruction = canonical_reference_extension(
            a, 0, 1, stations
        )
        if obstruction:
            continue
        for refs in (canonical_refs, canonical_refs ^ full_mask):
            observed_difference_mask = (a | refs) & window_mask
            if observed_difference_mask:
                continue
            if twisted_local_syndrome_mask(a, 0, refs, 1, stations):
                continue
            return {
                "center": center,
                "sites": sites,
                "token_flip_site": token_site,
                "token_flip_distance": ring_distance(
                    token_site, center, stations
                ),
                "A_mask": a,
                "B_mask": 0,
                "refs_mask": refs,
                "h": 1,
                "rail_ref_bits_observed": 3 * len(sites),
                "observed_bit_differences": 0,
                "marked_edge_excluded": True,
                "all_rows_satisfied": True,
            }
    raise AssertionError(("no radius-one witness", center, stations))


def marked_edge_witness_result() -> dict[str, object]:
    stations = 11
    edge = lexicographically_first_edge(stations)
    window_rows = tuple(
        radius_one_window_witness(center, stations)
        for center in range(stations)
        if not set(edge) <= set(radius_one_sites(center, stations))
    )
    representative = next(row for row in window_rows if row["center"] == 8)
    derived_pair = (
        (
            ("ring_stations", stations),
            ("A_mask", 0),
            ("B_mask", 0),
            ("refs_mask", 0),
            ("h", 0),
        ),
        (
            ("ring_stations", stations),
            ("A_mask", representative["A_mask"]),
            ("B_mask", representative["B_mask"]),
            ("refs_mask", representative["refs_mask"]),
            ("h", representative["h"]),
        ),
    )
    states = []
    for item in derived_pair:
        state = dict(item)
        states.append(
            {
                **state,
                "token_parity": token_parity(
                    state["A_mask"], state["B_mask"]
                ),
                "twisted_syndrome_mask": twisted_local_syndrome_mask(
                    state["A_mask"],
                    state["B_mask"],
                    state["refs_mask"],
                    state["h"],
                    stations,
                ),
            }
        )
    representative_differences = (
        states[0]["A_mask"] ^ states[1]["A_mask"],
        states[0]["B_mask"] ^ states[1]["B_mask"],
        states[0]["refs_mask"] ^ states[1]["refs_mask"],
    )
    representative_window_rows = tuple(
        {
            "center": row["center"],
            "sites": row["sites"],
            "observed_bit_differences": sum(
                (difference & sum(1 << site for site in row["sites"])).bit_count()
                for difference in representative_differences
            ),
        }
        for row in window_rows
    )
    representative_indistinguishable_windows = sum(
        row["observed_bit_differences"] == 0
        for row in representative_window_rows
    )
    window_census = (
        ("ring_stations", stations),
        ("marked_edge", edge),
        ("radius", 1),
        ("windows_excluding_marked_edge", len(window_rows)),
        (
            "windows_with_window_specific_indistinguishable_witness",
            sum(row["observed_bit_differences"] == 0 for row in window_rows),
        ),
        (
            "rail_ref_bits_per_window",
            min(row["rail_ref_bits_observed"] for row in window_rows),
        ),
        (
            "maximum_observed_bit_differences",
            max(row["observed_bit_differences"] for row in window_rows),
        ),
        (
            "minimum_token_flip_distance",
            min(row["token_flip_distance"] for row in window_rows),
        ),
        ("representative_window_center", representative["center"]),
        ("representative_window_sites", representative["sites"]),
        (
            "representative_pair_indistinguishable_windows",
            representative_indistinguishable_windows,
        ),
    )
    return {
        "derived_pair_matches_frozen_literal": (
            derived_pair == FROZEN_MARKED_EDGE_WITNESS_PAIR
        ),
        "states": states,
        "marked_edge": edge,
        "representative_window": representative,
        "representative_pair_window_census": representative_window_rows,
        "window_census": window_census,
        "window_census_matches_frozen_literal": (
            window_census == FROZEN_RADIUS1_WINDOW_CENSUS
        ),
        "every_radius1_window_excluding_marked_edge_has_its_own_witness": all(
            row["marked_edge_excluded"]
            and row["all_rows_satisfied"]
            and row["observed_bit_differences"] == 0
            and row["token_flip_distance"] > 1
            for row in window_rows
        ),
        "representative_pair_satisfies_all_rows": all(
            row["twisted_syndrome_mask"] == 0 for row in states
        ),
        "representative_pair_differs_in_h": states[0]["h"] != states[1]["h"],
        "representative_pair_differs_in_token_parity": (
            states[0]["token_parity"] != states[1]["token_parity"]
        ),
        "representative_pair_indistinguishable_windows": (
            representative_indistinguishable_windows
        ),
    }


def chained_reference_census(stations: int) -> dict[str, object]:
    agreement_counts = Counter(
        chained_agreement_expression(refs, stations)
        for refs in range(1 << stations)
    )
    disagreement_counts = Counter(
        closed_ring_difference_coboundary(refs, stations)
        for refs in range(1 << stations)
    )
    return {
        "stations": stations,
        "reference_states": 1 << stations,
        "agreement_value_census": {
            str(key): value for key, value in sorted(agreement_counts.items())
        },
        "disagreement_value_census": {
            str(key): value for key, value in sorted(disagreement_counts.items())
        },
        "agreement_equals_station_parity_for_every_reference_state": agreement_counts
        == Counter({stations & 1: 1 << stations}),
        "disagreement_is_zero_for_every_reference_state": disagreement_counts
        == Counter({0: 1 << stations}),
    }


def frozen_chained_reference_census_shape(
    row: dict[str, object],
) -> tuple[tuple[str, object], ...]:
    return (
        ("stations", row["stations"]),
        ("reference_states", row["reference_states"]),
        (
            "agreement_value_census",
            tuple(sorted(row["agreement_value_census"].items())),
        ),
        (
            "disagreement_value_census",
            tuple(sorted(row["disagreement_value_census"].items())),
        ),
    )


def render_with_exact_size(report: dict[str, object]) -> tuple[str, int]:
    report["stdout_bytes"] = 0
    for _ in range(20):
        compact_report = json.dumps(
            report,
            sort_keys=True,
            default=str,
            separators=(",", ":"),
        )
        text = "\n".join(OUTPUT_LINES) + "\n" + compact_report + "\n"
        size = len(text.encode())
        if report["stdout_bytes"] == size:
            return text, size
        report["stdout_bytes"] = size
    raise AssertionError("stdout byte-count fixed point did not converge")


def main() -> int:
    started = perf_counter()
    programs = program_rows()
    observed_programs = observed_program_census(programs)
    table = mode_graph_table(programs)

    check(
        "declared_mode_graph_matches_frozen_program_census",
        observed_programs == FROZEN_PROGRAM_CENSUS,
        {"observed": observed_programs},
    )

    observed_support = support_census(programs)
    check(
        "original_untwisted_row_support_census_remains_frozen",
        observed_support == FROZEN_SUPPORT_CENSUS,
        {"observed": observed_support},
    )
    observed_amended_support = amended_support_census(programs)
    check(
        "amended_locality_radius_at_most_one_and_only_marked_row_reads_h",
        observed_amended_support == FROZEN_AMENDED_SUPPORT_CENSUS,
        {
            "marked_edge_convention": "lexicographically_first_ring_edge",
            "observed": observed_amended_support,
        },
    )

    parity_helper_cases = tuple(
        (
            bits,
            parity_tuple(bits),
            sum(bits) & 1,
        )
        for bits in ((), (0,), (1,), (1, 0, 1), (1, 1, 1, 1, 1))
    )
    check(
        "cycle703_public_parity_machinery_reused",
        all(observed == expected for _bits, observed, expected in parity_helper_cases),
        parity_helper_cases,
    )

    stations_tested = tuple(len(program) for _name, _banks, program in programs)
    telescope_algebra = {
        str(stations): {
            "row_xor": sorted(telescope_symbols(stations, FROZEN_R1_PULLBACK)),
            "equals_global_token_parity": telescope_symbols(
                stations, FROZEN_R1_PULLBACK
            )
            == expected_global_symbols(stations),
        }
        for stations in stations_tested
    }
    check(
        "original_untwisted_telescope_identity_remains_frozen",
        all(row["equals_global_token_parity"] for row in telescope_algebra.values()),
        {
            "rings": stations_tested,
            "large_symbol_tables": "retained by digest in final report",
        },
    )
    twist_telescope_algebra = {
        str(stations): {
            "marked_edge": lexicographically_first_edge(stations),
            "row_xor": sorted(
                amended_telescope_symbols(stations, FROZEN_R1_PULLBACK)
            ),
            "equals_token_parity_xor_h": amended_telescope_symbols(
                stations, FROZEN_R1_PULLBACK
            )
            == expected_amended_global_symbols(stations),
        }
        for stations in stations_tested
    }
    check(
        "twist_telescope_is_exact_boolean_identity_on_11_35_130",
        all(
            row["equals_token_parity_xor_h"]
            for row in twist_telescope_algebra.values()
        ),
        {
            "rings": stations_tested,
            "marked_edges": {
                key: row["marked_edge"]
                for key, row in twist_telescope_algebra.items()
            },
            "identity": "XOR_s L_s = token_parity XOR h",
        },
    )

    exhaustive = exhaustive_ring11()
    exhaustive_result_census = tuple(
        (key, exhaustive[key]) for key, _expected in FROZEN_EXHAUSTIVE_RESULT_CENSUS
    )
    check(
        "original_exhaustive_census_is_frozen_as_self_correction_evidence",
        exhaustive["enumeration"] == dict(FROZEN_ENUMERATION_CENSUS)
        and exhaustive_result_census == FROZEN_EXHAUSTIVE_RESULT_CENSUS,
        exhaustive,
    )
    check(
        "self_correction_original_rows_exactly_force_even_token_parity",
        exhaustive["local_satisfied_states"]
        == exhaustive["local_satisfied_even_token_states"]
        == 2048,
        {
            "local_satisfied_states": exhaustive["local_satisfied_states"],
            "even_token_states": exhaustive[
                "local_satisfied_even_token_states"
            ],
            "algebra": "XOR_s L_s=token parity, so L_s=0 for all s implies parity 0",
        },
    )
    amended_sector_census = tuple(
        tuple(
            (key, row[key])
            for key, _expected in FROZEN_AMENDED_H_SECTOR_CENSUS[h]
        )
        for h, row in enumerate(exhaustive["amended_by_h"])
    )
    check(
        "twist_telescope_ring11_and_h_sector_censuses_are_exhaustively_frozen",
        exhaustive["enumeration"] == dict(FROZEN_ENUMERATION_CENSUS)
        and amended_sector_census == FROZEN_AMENDED_H_SECTOR_CENSUS,
        {
            "enumeration": exhaustive["enumeration"],
            "amended_by_h": exhaustive["amended_by_h"],
        },
    )
    compression_a = all(
        row["fixed_ref_satisfied_states"] > 0
        and row["fixed_ref_matching_states"]
        == row["fixed_ref_satisfied_states"]
        and row["compression_a_failures"] == 0
        for row in exhaustive["amended_by_h"]
    )
    check(
        "compression_a_all_amended_local_rows_pin_token_parity_to_h",
        compression_a,
        {
            "fixed_reference_chain": exhaustive["refs_mask"],
            "h_censuses": exhaustive["amended_by_h"],
        },
    )
    compression_b = all(
        row["projected_satisfied_states"]
        == row["token_parity_sector_states"]
        == 2097152
        and row["projected_exact_separation_failures"] == 0
        and row["canonical_extension_failures"] == 0
        and row["complement_extension_failures"] == 0
        and row["satisfying_reference_extensions"] == 4194304
        for row in exhaustive["amended_by_h"]
    )
    check(
        "compression_b_projected_satisfied_set_exactly_separates_h0_h1",
        compression_b,
        {
            "projection": (
                "rail states admitting a supplied reference-chain extension"
            ),
            "h_censuses": exhaustive["amended_by_h"],
            "exact_solution_multiplicity": (
                "two reference chains per matching rail state: canonical "
                "ref_0=0 and its global complement"
            ),
        },
    )

    derived_r1 = derive_pullback_offsets(r1_state, 11)
    r1_failures = sum(
        verify_pullback_law(r1_state, stations, FROZEN_R1_PULLBACK)
        for stations in stations_tested
    )
    check(
        "R1_row_pullback_law_frozen_and_rowwise_invariant",
        derived_r1 == frozenset(FROZEN_R1_PULLBACK) and r1_failures == 0,
        {
            "frozen_pullback_offsets": FROZEN_R1_PULLBACK,
            "derived_pullback_offsets": sorted(derived_r1),
            "basis_identity_failures": r1_failures,
        },
    )

    derived_r2 = derive_pullback_offsets(r2_state, 11)
    derived_r = derive_pullback_offsets(r_state, 11)
    r2_law_failures = sum(
        verify_pullback_law(r2_state, stations, FROZEN_R2_PULLBACK)
        for stations in stations_tested
    )
    r_law_failures = sum(
        verify_pullback_law(r_state, stations, FROZEN_R_PULLBACK)
        for stations in stations_tested
    )
    r_law_algebra = {}
    row_permutation_results = {}
    for stations in stations_tested:
        r2_global = telescope_symbols(stations, FROZEN_R2_PULLBACK)
        r_global = telescope_symbols(stations, FROZEN_R_PULLBACK)
        permuted, permutation = row_family_is_permuted(
            stations, FROZEN_R_PULLBACK
        )
        r_law_algebra[str(stations)] = {
            "R2_global_token_symbols_preserved": r2_global
            == expected_global_symbols(stations),
            "R_global_token_symbols_preserved": r_global
            == expected_global_symbols(stations),
        }
        row_permutation_results[str(stations)] = {
            "row_set_permuted": permuted,
            "explicit_row_image_indices": permutation,
        }
    check(
        "R2_and_R_true_pullback_laws_match_frozen_offsets",
        derived_r2 == frozenset(FROZEN_R2_PULLBACK)
        and derived_r == frozenset(FROZEN_R_PULLBACK)
        and r2_law_failures == 0
        and r_law_failures == 0
        and all(
            row["R2_global_token_symbols_preserved"]
            and row["R_global_token_symbols_preserved"]
            for row in r_law_algebra.values()
        ),
        {
            "R2_frozen_pullback_offsets": FROZEN_R2_PULLBACK,
            "R2_derived_pullback_offsets": sorted(derived_r2),
            "R2_basis_identity_failures": r2_law_failures,
            "R_frozen_pullback_offsets": FROZEN_R_PULLBACK,
            "R_derived_pullback_offsets": sorted(derived_r),
            "R_basis_identity_failures": r_law_failures,
        },
    )

    k_semantics = tuple(verify_k_r_semantics(stations) for stations in stations_tested)
    check(
        "K_semantic_R_matches_frozen_rail_permutation",
        all(row["failures"] == 0 for row in k_semantics),
        k_semantics,
    )

    observed_row_set_permuted = all(
        row["row_set_permuted"] for row in row_permutation_results.values()
    )
    check(
        "true_nonpermutation_of_declared_row_set_is_frozen",
        observed_row_set_permuted == FROZEN_R_ROW_SET_PERMUTED,
        {
            "frozen": FROZEN_R_ROW_SET_PERMUTED,
            "observed_by_ring": {
                key: value["row_set_permuted"]
                for key, value in row_permutation_results.items()
            },
        },
    )
    check(
        "self_correction_original_D3_row_set_nonpermutation_is_frozen",
        not observed_row_set_permuted,
        {
            "refuted_original_claim": "R permutes the declared local-row set",
            "actual_L_s_after_R": "A_(s-1) XOR B_(s+1) XOR ref_s XOR ref_(s+1)",
            "explicit_row_image_indices": row_permutation_results,
        },
    )

    counterexample = dict(FROZEN_R_COUNTEREXAMPLE)
    counter_a, counter_b = r_state(
        counterexample["A_before_mask"],
        counterexample["B_before_mask"],
        counterexample["ring_stations"],
    )
    observed_counterexample = {
        **counterexample,
        "syndrome_before_mask": local_syndrome_mask(
            counterexample["A_before_mask"],
            counterexample["B_before_mask"],
            counterexample["refs_mask"],
            counterexample["ring_stations"],
        ),
        "syndrome_after_mask": local_syndrome_mask(
            counter_a,
            counter_b,
            counterexample["refs_mask"],
            counterexample["ring_stations"],
        ),
    }
    counterexample_frozen = tuple(observed_counterexample.items()) == FROZEN_R_COUNTEREXAMPLE
    rows_preserved = (
        observed_counterexample["syndrome_before_mask"]
        == observed_counterexample["syndrome_after_mask"]
    )
    check(
        "frozen_R_counterexample_reproduced",
        counterexample_frozen,
        observed_counterexample,
    )
    check(
        "self_correction_original_D3_rowwise_R_commutation_counterexample_is_frozen",
        counterexample_frozen and not rows_preserved,
        {
            "refuted_original_claim": (
                "every local row commutes with H for static refs"
            ),
            "Q_rail_action": "identity by K.apply_controller_step API",
            "R_counterexample": observed_counterexample,
        },
    )
    check(
        "telescoped_global_token_parity_is_invariant_under_H",
        all(
            row["R_global_token_symbols_preserved"]
            for row in r_law_algebra.values()
        )
        and token_parity(
            counterexample["A_before_mask"], counterexample["B_before_mask"]
        )
        == token_parity(counter_a, counter_b),
        {
            "reason": "Q acts on data only; R is a permutation of all rail bits",
            "rings": stations_tested,
        },
    )
    amended_r_compatibility = all(
        amended_telescope_symbols(stations, FROZEN_R_PULLBACK)
        == expected_amended_global_symbols(stations)
        for stations in stations_tested
    ) and all(
        (token_parity(counterexample["A_before_mask"], counterexample["B_before_mask"]) ^ h)
        == (token_parity(counter_a, counter_b) ^ h)
        for h in (0, 1)
    )
    check(
        "amended_token_parity_xor_h_is_R_invariant_with_static_h",
        amended_r_compatibility,
        {
            "frozen_actual_R_pullback": FROZEN_R_PULLBACK,
            "h_action_under_R": "static",
            "rings": stations_tested,
            "identity": "token_parity XOR h is invariant",
        },
    )

    chained_10 = chained_reference_census(10)
    chained_11 = chained_reference_census(11)
    chained_census_frozen = (
        frozen_chained_reference_census_shape(chained_10),
        frozen_chained_reference_census_shape(chained_11),
    ) == FROZEN_CHAINED_REFERENCE_CENSUS
    check(
        "chained_reference_expression_census_matches_frozen_literal",
        chained_census_frozen,
        {"ring10": chained_10, "ring11": chained_11},
    )
    check(
        "chained_agreement_is_affine_size_parity_and_difference_is_coboundary",
        chained_census_frozen
        and chained_10[
            "agreement_equals_station_parity_for_every_reference_state"
        ]
        and chained_11[
            "agreement_equals_station_parity_for_every_reference_state"
        ]
        and chained_10["disagreement_is_zero_for_every_reference_state"]
        and chained_11["disagreement_is_zero_for_every_reference_state"],
        {
            "refuted_original_claim": (
                "the chained-agreement expression is a variable reference bit"
            ),
            "ring10": chained_10,
            "ring11": chained_11,
            "conclusion": (
                "agreement is an affine ring-size-parity constant; only the "
                "chained difference is the zero coboundary"
            ),
        },
    )

    check(
        "self_correction_original_compression_a_has_zero_matching_states_frozen",
        exhaustive["local_satisfied_states"] == 2048
        and exhaustive[
            "local_satisfied_token_agreement_expression_matches"
        ]
        == 0,
        {
            "refuted_original_claim": (
                "untwisted local rows pin token parity to chained agreement"
            ),
            "original_chained_agreement": exhaustive[
                "chained_agreement_expression"
            ],
            "local_satisfied_states": exhaustive["local_satisfied_states"],
            "matching_states": exhaustive[
                "local_satisfied_token_agreement_expression_matches"
            ],
        },
    )

    check(
        "self_correction_original_compression_b_failure_census_is_frozen",
        exhaustive["exact_sector_separation_failures"] == 2099200
        and exhaustive[
            "token_parity_equals_agreement_expression_states"
        ]
        == 2097152
        and chained_11["agreement_value_census"] == {"1": 2048},
        {
            "refuted_original_claim": (
                "untwisted satisfied set exactly separates two chained "
                "agreement sectors"
            ),
            "ring11_agreement_value_census": chained_11[
                "agreement_value_census"
            ],
            "exact_sector_separation_failures": exhaustive[
                "exact_sector_separation_failures"
            ],
            "token_parity_equals_agreement_expression_states": exhaustive[
                "token_parity_equals_agreement_expression_states"
            ],
        },
    )

    witness = frozen_witness_result()
    check(
        "self_correction_original_witness_pair_is_frozen_and_satisfies_rows",
        witness["derived_pair_matches_frozen_literal"]
        and witness["every_local_row_identical"]
        and witness["every_local_row_satisfied"],
        witness,
    )
    check(
        "self_correction_original_witness_does_not_vary_chained_agreement",
        not witness["chained_agreement_expression_differs"]
        and witness["candidate_reference_global_bit_differs"],
        {
            "refuted_original_claim": (
                "the frozen complement witness varies chained agreement"
            ),
            "literal_agreement_holonomies": tuple(
                row["chained_agreement_expression"] for row in witness["states"]
            ),
            "candidate_XOR_all_refs_differs": witness[
                "candidate_reference_global_bit_differs"
            ],
            "boundary": (
                "XOR_all_refs is distinguished, but it is not the requested "
                "XOR-of-consecutive-agreements formula and is not pinned to token parity."
            ),
        },
    )
    marked_witness = marked_edge_witness_result()
    check(
        "each_radius1_window_has_its_own_counterpair_and_representative_is_7_of_9",
        marked_witness["derived_pair_matches_frozen_literal"]
        and marked_witness["window_census_matches_frozen_literal"]
        and marked_witness[
            "every_radius1_window_excluding_marked_edge_has_its_own_witness"
        ]
        and marked_witness["representative_pair_satisfies_all_rows"]
        and marked_witness["representative_pair_differs_in_h"]
        and marked_witness["representative_pair_differs_in_token_parity"]
        and marked_witness["representative_pair_indistinguishable_windows"] == 7,
        marked_witness,
    )

    observed_controls = control_census(programs)
    check(
        "controls_ref_flip_two_rows_A_flip_one_row_match_frozen_census",
        observed_controls == FROZEN_CONTROL_CENSUS,
        {"observed": observed_controls},
    )
    observed_twist_controls = twist_control_census(programs)
    check(
        "control_flip_h_flips_exactly_the_marked_row_only",
        observed_twist_controls == FROZEN_TWIST_CONTROL_CENSUS,
        {"observed": observed_twist_controls},
    )
    order_control = permuted_telescope_control(11)
    check(
        "permuted_row_order_does_not_change_telescope",
        order_control["invariant"],
        order_control,
    )

    claim_boundary = {
        "one_auxiliary_bit_suffices_for_declared_row_family": (
            compression_a and compression_b
        ),
        "converse_is_existential_reference_projection": True,
        "each_tested_radius1_window_individually_fails_to_determine_h": (
            marked_witness[
                "every_radius1_window_excluding_marked_edge_has_its_own_witness"
            ]
        ),
        "proposed_agreement_expression_is_state_independent": (
            chained_census_frozen
        ),
        "agreement_expression_is_itself_a_coboundary": False,
        "refs_are_new_supplied_clean_registers": True,
        "marked_edge_ref_chain_and_h_are_declared_conditions": True,
        "controller_holonomy_identification_claim": False,
        "representation_independent_minimality_claim": False,
        "arbitrary_bounded_window_claim": False,
        "controller_completion_claim": False,
        "occurrence_claim": False,
        "autonomous_preparation_claim": False,
        "enforcement_claim": False,
        "rows_integrated_into_refusal_wrap": False,
        "next_step": (
            "The declared rows remain a conditional algebraic construction "
            "and are not integrated into the refusal wrapper."
        ),
    }
    check(
        "claim_boundary_is_conditional_and_excludes_controller_or_minimality_claims",
        claim_boundary["one_auxiliary_bit_suffices_for_declared_row_family"]
        and claim_boundary["converse_is_existential_reference_projection"]
        and claim_boundary[
            "each_tested_radius1_window_individually_fails_to_determine_h"
        ]
        and claim_boundary["proposed_agreement_expression_is_state_independent"]
        and claim_boundary["agreement_expression_is_itself_a_coboundary"] is False
        and claim_boundary["refs_are_new_supplied_clean_registers"] is True
        and claim_boundary[
            "marked_edge_ref_chain_and_h_are_declared_conditions"
        ]
        is True
        and claim_boundary["controller_holonomy_identification_claim"] is False
        and claim_boundary["representation_independent_minimality_claim"] is False
        and claim_boundary["arbitrary_bounded_window_claim"] is False
        and claim_boundary["controller_completion_claim"] is False
        and claim_boundary["occurrence_claim"] is False
        and claim_boundary["autonomous_preparation_claim"] is False
        and claim_boundary["enforcement_claim"] is False
        and claim_boundary["rows_integrated_into_refusal_wrap"] is False,
        claim_boundary,
    )

    mode_table_text = "\n".join(table)
    telescope_digest = sha256(
        json.dumps(telescope_algebra, sort_keys=True, default=str).encode()
    ).hexdigest()
    twist_telescope_digest = sha256(
        json.dumps(
            twist_telescope_algebra, sort_keys=True, default=str
        ).encode()
    ).hexdigest()
    all_pass = all(CHECKS.values())
    runtime_seconds = round(perf_counter() - started, 6)
    report: dict[str, object] = {
        "audit": "unset",
        "authority": "none",
        "bounded": True,
        "claim_boundary": claim_boundary,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not passed for passed in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "compression": {
            "full_assignment_implication": compression_a,
            "existential_reference_projection_converse": compression_b,
            "amended_h_sector_census": exhaustive["amended_by_h"],
            "projection_over_declared_reference_chain": True,
            "reference_extensions_per_matching_rail_state": 2,
        },
        "controls": {
            "original_flip_census": observed_controls,
            "h_flip_census": observed_twist_controls,
            "row_order": order_control,
        },
        "enumeration": exhaustive,
        "imports": {
            "K": K_INPUT_PATH,
            "G703": G703_INPUT_PATH,
            "G703_public_helper": "parity_before",
            "flattened_mutable_input_count": len(AUDIT_INPUT_PATHS),
        },
        "local_rows": {
            "unmarked_formula": (
                "L_s=A_s XOR B_s XOR ref_s XOR ref_(s+1)"
            ),
            "marked_formula": (
                "L_s*=A_s* XOR B_s* XOR ref_s* XOR ref_(s*+1) XOR h"
            ),
            "marked_edge_convention": "lexicographically_first_ring_edge",
            "marked_edges": {
                str(stations): lexicographically_first_edge(stations)
                for stations in stations_tested
            },
            "satisfied_value": 0,
            "support_census": observed_amended_support,
        },
        "mode_graph": {
            "convention": (
                "station s is vertex (A_s,B_s); ring edge (s,s+1); "
                "one new clean supplied ref_s per station; h is supplied "
                "at the lexicographically first edge"
            ),
            "program_census": observed_programs,
            "full_table_rows_not_emitted": len(table) - 2,
            "full_table_sha256": sha256(mode_table_text.encode()).hexdigest(),
        },
        "run_result": "pass" if all_pass else "fail",
        "R_law": {
            "R1_pullback": FROZEN_R1_PULLBACK,
            "R2_pullback": FROZEN_R2_PULLBACK,
            "R_pullback": FROZEN_R_PULLBACK,
            "row_set_permuted": observed_row_set_permuted,
            "row_permutation_results": row_permutation_results,
            "counterexample": observed_counterexample,
            "K_semantics": k_semantics,
            "global_token_parity_invariant": True,
            "h_static": True,
            "token_parity_xor_h_invariant": amended_r_compatibility,
        },
        "formula_correction_record": {
            "proposed_chained_agreement_is_state_independent": True,
            "agreement_is_affine_translate_of_difference_coboundary": True,
            "chained_agreement_ring10": chained_10,
            "chained_agreement_ring11": chained_11,
            "original_exhaustive_census": {
                key: exhaustive[key]
                for key, _expected in FROZEN_EXHAUSTIVE_RESULT_CENSUS
            },
            "R_row_set_counterexample": row_permutation_results,
            "R_rowwise_counterexample": observed_counterexample,
            "frozen_original_witness": witness,
        },
        "runtime_seconds": runtime_seconds,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "telescope": {
            "exact_boolean_algebra_identity": True,
            "formula": "XOR_s L_s = token_parity XOR h",
            "numeric_exhaustive_ring11": all(
                row["twist_telescope_failures"] == 0
                for row in exhaustive["amended_by_h"]
            ),
            "amended_algebra_table_sha256": twist_telescope_digest,
            "original_algebra_table_sha256": telescope_digest,
            "rings": stations_tested,
        },
        "witness": marked_witness,
    }

    # The full mode table is retained by row count and digest instead of being
    # emitted.  The compact report must fit the audit transport budget without
    # clipping; render_with_exact_size then solves stdout_bytes exactly.
    preliminary = (
        "\n".join(OUTPUT_LINES)
        + "\n"
        + json.dumps(
            report,
            sort_keys=True,
            default=str,
            separators=(",", ":"),
        )
        + "\n"
    )
    check(
        "stdout_complete_and_bounded_under_20000_characters",
        len(preliminary.encode()) < STDOUT_LIMIT_BYTES,
        {
            "preliminary_bytes": len(preliminary.encode()),
            "limit_bytes": STDOUT_LIMIT_BYTES,
            "final_exact_count_in_JSON": True,
        },
    )
    all_pass = all(CHECKS.values())
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not passed for passed in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["run_result"] = "pass" if all_pass else "fail"
    text, exact_size = render_with_exact_size(report)
    if exact_size >= STDOUT_LIMIT_BYTES:
        raise AssertionError((exact_size, STDOUT_LIMIT_BYTES))
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
