#!/usr/bin/env python3
"""Cycle 827: parity-safe fixed-type atlas for the Cycle-719 controller."""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
from itertools import product
from pathlib import Path
import time

import numpy as np

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as H719
import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/CYCLE719_PARITY_SAFE_TYPED_CONTROLLER_ATLAS_"
    "CYCLE827_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
RUNNER_PATH = (
    "scripts/frontier_cycle827_cycle719_parity_safe_typed_controller_"
    "atlas_2026_07_30.py"
)
RECEIPT_PATH = (
    "outputs/cycle719_parity_safe_typed_controller_atlas_"
    "cycle827_receipt_2026_07_30.json"
)
AUDIT_INPUT_PATHS = (
    NOTE_PATH,
    RUNNER_PATH,
    RECEIPT_PATH,
    "docs/COMPANION_ENDPOINT_CYCLE719_HISTORY_INTERFACE_"
    "CYCLE826_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_"
    "CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle719_recurrent_matter_history_"
    "controller_2026_07_26.py",
    "docs/ROUTEC_STAGGERED_RADIUS_ONE_PARITY_EVEN_TRANSPORT_"
    "CYCLE822_BOUNDED_THEOREM_NOTE_2026-07-30.md",
    "scripts/frontier_cycle822_routec_staggered_radius_one_parity_even_"
    "transport_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
CHARGED_WIRES = frozenset(range(12))
NEIGHBOURS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def lift_matrix(matrix: np.ndarray, wires: tuple[int, ...], total: int) -> np.ndarray:
    output = np.zeros((1 << total, 1 << total), dtype=complex)
    for source in range(1 << total):
        local_source = sum(
            ((source >> wire) & 1) << index
            for index, wire in enumerate(wires)
        )
        for local_target in range(1 << len(wires)):
            amplitude = matrix[local_target, local_source]
            if abs(amplitude) < 1.0e-15:
                continue
            target = source
            for index, wire in enumerate(wires):
                target = (
                    (target & ~(1 << wire))
                    | (((local_target >> index) & 1) << wire)
                )
            output[target, source] += amplitude
    return output


def normalized_gate(gate):
    if gate.kind != "TOF":
        return gate, False
    first, second, target = gate.wires
    if second in CHARGED_WIRES and first not in CHARGED_WIRES:
        return H719.A.Gate("TOF", (second, first, target)), True
    return gate, False


def normalize_word(word):
    output = []
    swaps = 0
    equivalence_failures = 0
    for gate in word:
        fixed, changed = normalized_gate(gate)
        swaps += changed
        if gate.kind == "TOF":
            equivalence_failures += not (
                frozenset(gate.wires[:2]) == frozenset(fixed.wires[:2])
                and gate.wires[2] == fixed.wires[2]
            )
        else:
            equivalence_failures += gate != fixed
        output.append(fixed)
    return tuple(output), swaps, equivalence_failures


def factor_parity_violation(kind: str, wires: tuple[int, ...]) -> bool:
    charged = tuple(wire in CHARGED_WIRES for wire in wires)
    if kind in ("T", "TD"):
        return False
    if kind == "H":
        return bool(charged[0])
    if kind == "X":
        return bool(charged[0])
    if kind == "CNOT":
        return bool(charged[1])
    raise ValueError(kind)


def prefix_parity_certificate(word):
    """Track the conjugated global parity Pauli after every elementary prefix."""
    initial_z = set(CHARGED_WIRES)
    x_support: set[int] = set()
    z_support = set(initial_z)
    negative = False
    noncommuting_prefixes = 0
    for kind, wires in H719.A.expanded(word):
        if kind == "CNOT":
            control, target = wires
            x_control = control in x_support
            x_target = target in x_support
            z_control = control in z_support
            z_target = target in z_support
            negative ^= x_control and z_target and (x_target ^ z_control ^ True)
            if x_control:
                x_support.symmetric_difference_update((target,))
            if z_target:
                z_support.symmetric_difference_update((control,))
        elif kind == "H":
            (wire,) = wires
            x_bit = wire in x_support
            z_bit = wire in z_support
            negative ^= x_bit and z_bit
            if x_bit != z_bit:
                x_support.symmetric_difference_update((wire,))
                z_support.symmetric_difference_update((wire,))
        elif kind == "X":
            (wire,) = wires
            negative ^= wire in z_support
        elif kind in ("T", "TD"):
            (wire,) = wires
            if wire in x_support:
                raise AssertionError("non-Pauli T conjugation entered parity tracker")
        else:
            raise ValueError(kind)
        noncommuting_prefixes += bool(
            negative or x_support or z_support != initial_z
        )
    return {
        "noncommuting_prefixes": noncommuting_prefixes,
        "terminal_parity_returns": bool(
            not negative and not x_support and z_support == initial_z
        ),
    }


def toffoli_decomposition_residual() -> float:
    word = H719.A.expanded((H719.A.Gate("TOF", (0, 1, 2)),))
    actual = np.zeros((8, 8), dtype=complex)
    expected = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        for target, amplitude in H719.A.sparse_apply(
            {source: 1.0 + 0.0j}, word
        ).items():
            actual[target, source] = amplitude
        target = source ^ ((((source >> 0) & 1) & ((source >> 1) & 1)) << 2)
        expected[target, source] = 1.0
    return float(np.linalg.norm(actual - expected))


def expanded_certificate(original, normalized):
    original_counts = Counter()
    normalized_counts = Counter()
    original_violations = normalized_violations = 0
    mutation_trials = mutation_detected = 0
    for gate, fixed in zip(original, normalized):
        original_factors = H719.A.expanded((gate,))
        fixed_factors = H719.A.expanded((fixed,))
        original_counts.update(kind for kind, _wires in original_factors)
        normalized_counts.update(kind for kind, _wires in fixed_factors)
        original_violations += sum(
            factor_parity_violation(kind, wires)
            for kind, wires in original_factors
        )
        normalized_violations += sum(
            factor_parity_violation(kind, wires)
            for kind, wires in fixed_factors
        )
        if gate != fixed:
            mutation_trials += 1
            mutation_detected += (
                sum(
                    factor_parity_violation(kind, wires)
                    for kind, wires in original_factors
                ) > 0
                and not any(
                    factor_parity_violation(kind, wires)
                    for kind, wires in fixed_factors
                )
            )
    original_prefix = prefix_parity_certificate(original)
    normalized_prefix = prefix_parity_certificate(normalized)
    return {
        "original_factor_counts": dict(sorted(original_counts.items())),
        "normalized_factor_counts": dict(sorted(normalized_counts.items())),
        "expanded_factors": sum(normalized_counts.values()),
        "original_elementary_parity_violations": original_violations,
        "normalized_elementary_parity_violations": normalized_violations,
        "original_noncommuting_prefixes": original_prefix[
            "noncommuting_prefixes"
        ],
        "normalized_noncommuting_prefixes": normalized_prefix[
            "noncommuting_prefixes"
        ],
        "original_terminal_parity_returns": original_prefix[
            "terminal_parity_returns"
        ],
        "normalized_terminal_parity_returns": normalized_prefix[
            "terminal_parity_returns"
        ],
        "control_order_mutation_trials": mutation_trials,
        "control_order_mutations_detected": mutation_detected,
        "toffoli_decomposition_maximum_residual": toffoli_decomposition_residual(),
    }


def normalized_run_orbit(data, program, *, reverse=False):
    stations = len(program)
    a = tuple(int(index == 0) for index in range(stations))
    b = (0,) * stations
    steps = range(stations)
    for _step in steps:
        al = list(a)
        bl = list(b)
        if not reverse:
            for station in range(stations):
                if al[station]:
                    word, _swaps, _failures = normalize_word(
                        H719.K.mapped_macro(program[station])
                    )
                    data = H719.A.apply_semantic(data, word)
            for station in range(stations):
                al[station], bl[station] = bl[station], al[station]
            for station in range(stations):
                target = (station + 1) % stations
                bl[station], al[target] = al[target], bl[station]
        else:
            for station in reversed(range(stations)):
                target = (station + 1) % stations
                bl[station], al[target] = al[target], bl[station]
            for station in reversed(range(stations)):
                al[station], bl[station] = bl[station], al[station]
            for station in reversed(range(stations)):
                if al[station]:
                    word, _swaps, _failures = normalize_word(
                        H719.K.mapped_macro(program[station])
                    )
                    data = H719.A.apply_semantic(data, tuple(reversed(word)))
        a, b = tuple(al), tuple(bl)
    return data, a, b


def semantic_controller_certificate(normalized):
    rows = failures = inverse_failures = 0
    for left in (0, 1):
        for right in (0, 1):
            banks, links = H719.B.chain_genesis(H719.BANKS)
            bits = list(H719.M.pack_state(banks, links))
            bits[H719.M.R3.X.LEFT_ENDPOINT] = left
            bits[H719.M.R3.X.RIGHT_ENDPOINT] = right
            bits[H719.R3_SOURCE_POINTER()] = left ^ right
            before = tuple(bits)
            landed, landed_a, landed_b, _trace = H719.K.run_orbit(
                before, H719.PROGRAM
            )
            observed, a_tokens, b_tokens = normalized_run_orbit(
                before, H719.PROGRAM
            )
            restored, ra_tokens, rb_tokens = normalized_run_orbit(
                observed, H719.PROGRAM, reverse=True
            )
            rows += 1
            failures += not (
                observed == landed
                and a_tokens == landed_a
                and b_tokens == landed_b
            )
            inverse_failures += not (
                restored == before
                and tuple(index for index, value in enumerate(ra_tokens) if value)
                == (0,)
                and not any(rb_tokens)
            )
    return {
        "endpoint_truth_rows": rows,
        "normalized_vs_landed_failures": failures,
        "normalized_inverse_failures": inverse_failures,
        "normalized_semantic_gates": len(normalized),
    }


def bfs_path(start, target, blocked, minima, maxima):
    queue = deque((start,))
    predecessor = {start: None}
    while queue:
        site = queue.popleft()
        if site == target:
            break
        for direction in NEIGHBOURS:
            candidate = add(site, direction)
            if candidate in predecessor or candidate in blocked:
                continue
            if any(
                candidate[axis] < minima[axis]
                or candidate[axis] > maxima[axis]
                for axis in range(3)
            ):
                continue
            predecessor[candidate] = site
            queue.append(candidate)
    if target not in predecessor:
        return None
    output = []
    site = target
    while site is not None:
        output.append(site)
        site = predecessor[site]
    return tuple(reversed(output))


def route_structure(path):
    nearest = len(set(path)) != len(path)
    nearest += sum(R822.S789.manhattan(a, b) != 1 for a, b in zip(path, path[1:]))
    labels = list(path)
    for index in range(len(path) - 2):
        labels[index], labels[index + 1] = labels[index + 1], labels[index]
    operand_failure = labels[-2:] != [path[0], path[-1]]
    for index in reversed(range(len(path) - 2)):
        labels[index], labels[index + 1] = labels[index + 1], labels[index]
    return_failure = labels != list(path)
    deletion_detected = False
    if len(path) > 2:
        damaged = list(path)
        for index in range(1, len(path) - 2):
            damaged[index], damaged[index + 1] = damaged[index + 1], damaged[index]
        deletion_detected = damaged[-2:] != [path[0], path[-1]]
    return nearest, operand_failure, return_failure, deletion_detected


def typed_atlas(normalized, wire_sites):
    pair_frequency = Counter()
    for gate in normalized:
        for _kind, wires in H719.A.expanded((gate,)):
            if len(wires) == 2:
                pair_frequency[tuple(wires)] += 1
    charged_pairs = tuple(sorted(
        pair for pair in pair_frequency if pair[0] in CHARGED_WIRES
    ))
    neutral_pairs = tuple(sorted(
        pair for pair in pair_frequency if pair[0] not in CHARGED_WIRES
    ))
    charged_persistent = {wire_sites[wire] for wire in CHARGED_WIRES}
    persistent = set(wire_sites)
    minima = tuple(min(site[axis] for site in wire_sites) - 8 for axis in range(3))
    maxima = tuple(max(site[axis] for site in wire_sites) + 8 for axis in range(3))
    legacy = H719.C713.C712.c707.c655

    charged_paths = {}
    charged_failures = 0
    charged_corridor = set()
    for pair in charged_pairs:
        start, target = (wire_sites[wire] for wire in pair)
        path = bfs_path(
            start, target, persistent - {start, target}, minima, maxima
        )
        charged_failures += path is None
        if path is not None:
            charged_paths[pair] = path
            charged_corridor.update(path[1:-1])

    fixed_charged = charged_persistent | charged_corridor
    neutral_paths = {}
    affected = neutral_failures = 0
    for pair in neutral_pairs:
        start, target = (wire_sites[wire] for wire in pair)
        path = legacy.manhattan_path(start, target)
        if set(path[1:-1]) & fixed_charged:
            affected += 1
            path = bfs_path(
                start, target, fixed_charged - {start, target}, minima, maxima
            )
        neutral_failures += path is None
        if path is not None:
            neutral_paths[pair] = path

    neutral_corridor = {
        site for path in neutral_paths.values() for site in path[1:-1]
    }
    fixed_neutral = (persistent - charged_persistent) | neutral_corridor
    all_paths = {**charged_paths, **neutral_paths}
    nearest = operand = returned = deletions = 0
    maximum_distance = routed_gates = 0
    nonlocal_occurrences = nonlocal_unique_routes = 0
    for pair, path in all_paths.items():
        row = route_structure(path)
        nearest += row[0]
        operand += row[1]
        returned += row[2]
        frequency = pair_frequency[pair]
        distance = len(path) - 1
        maximum_distance = max(maximum_distance, distance)
        routed_gates += frequency * (2 * distance - 1)
        if distance > 1:
            nonlocal_unique_routes += 1
            nonlocal_occurrences += frequency
            deletions += row[3]

    legacy_charged_corridor = set()
    legacy_neutral_corridor = set()
    for pair in charged_pairs:
        legacy_charged_corridor.update(
            legacy.manhattan_path(
                wire_sites[pair[0]], wire_sites[pair[1]]
            )[1:-1]
        )
    for pair in neutral_pairs:
        legacy_neutral_corridor.update(
            legacy.manhattan_path(
                wire_sites[pair[0]], wire_sites[pair[1]]
            )[1:-1]
        )

    one_site_factors = sum(
        1 for gate in normalized
        for _kind, wires in H719.A.expanded((gate,)) if len(wires) == 1
    )
    route_exchange_parity_violations = sum(
        any(site not in fixed_charged for site in path[:-1])
        for path in charged_paths.values()
    ) + sum(
        any(site not in fixed_neutral for site in path)
        for path in neutral_paths.values()
    )
    fswap = R822.primitive_matrix("FSWAP")
    swap = R822.primitive_matrix("SWAP")
    blank_corridor_fswap_residual = float(
        np.linalg.norm((fswap - swap)[:, (0, 1, 2)])
    )
    cnot = R822.primitive_matrix("data_CNOT_work")
    routed_remote_cnot = (
        lift_matrix(fswap, (0, 1), 3)
        @ lift_matrix(cnot, (1, 2), 3)
        @ lift_matrix(fswap, (0, 1), 3)
    )
    ideal_remote_cnot = lift_matrix(cnot, (0, 2), 3)
    blank_corridor_columns = tuple(
        source for source in range(8) if not ((source >> 1) & 1)
    )
    blank_corridor_returned_cnot_residual = float(
        np.linalg.norm(
            (routed_remote_cnot - ideal_remote_cnot)[:, blank_corridor_columns]
        )
    )
    return {
        "paths": all_paths,
        "fixed_charged": frozenset(fixed_charged),
        "fixed_neutral": frozenset(fixed_neutral),
        "semantic_gates": len(normalized),
        "unique_two_M2_pairs": len(pair_frequency),
        "two_M2_factor_occurrences": sum(pair_frequency.values()),
        "one_M2_factor_occurrences": one_site_factors,
        "charged_unique_pairs": len(charged_pairs),
        "charged_pair_occurrences": sum(pair_frequency[p] for p in charged_pairs),
        "charged_control_paths_failed": charged_failures,
        "charged_corridor_sites": len(charged_corridor),
        "charged_corridor_persistent_hits": len(charged_corridor & persistent),
        "neutral_unique_pairs_rerouted": affected,
        "neutral_pair_occurrences_rerouted": sum(
            pair_frequency[pair]
            for pair in neutral_pairs
            if neutral_paths.get(pair) != legacy.manhattan_path(
                wire_sites[pair[0]], wire_sites[pair[1]]
            )
        ),
        "neutral_paths_failed": neutral_failures,
        "charged_neutral_fixed_type_overlap": len(fixed_charged & fixed_neutral),
        "nearest_neighbour_or_repeated_site_failures": nearest,
        "operand_order_failures": operand,
        "route_return_failures": returned,
        "nonlocal_unique_route_deletions_detected": deletions,
        "nonlocal_unique_routes": nonlocal_unique_routes,
        "nonlocal_route_occurrences": nonlocal_occurrences,
        "maximum_route_distance": maximum_distance,
        "routed_two_M2_gates": routed_gates,
        "routed_total_gates": routed_gates + one_site_factors,
        "full_130_H_orbit_routed_controller_gates": (
            130 * (routed_gates + one_site_factors)
        ),
        "charged_route_exchange": "FSWAP",
        "neutral_route_exchange": "SWAP",
        "route_exchange_prefix_parity_violations": route_exchange_parity_violations,
        "blank_corridor_FSWAP_vs_SWAP_residual": blank_corridor_fswap_residual,
        "blank_corridor_returned_FSWAP_CNOT_FSWAP_residual": (
            blank_corridor_returned_cnot_residual
        ),
        "legacy_charged_corridor_neutral_persistent_hits": len(
            legacy_charged_corridor & (persistent - charged_persistent)
        ),
        "legacy_charged_neutral_corridor_overlaps": len(
            legacy_charged_corridor & legacy_neutral_corridor
        ),
        "legacy_neutral_corridor_charged_persistent_hits": len(
            legacy_neutral_corridor & charged_persistent
        ),
    }


def covariance_certificate(atlas):
    frames = tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in R822.B.V.T.proper_cubic_frames()
    )
    charged = atlas["fixed_charged"]
    neutral = atlas["fixed_neutral"]
    edges = {
        tuple(sorted((left, right)))
        for path in atlas["paths"].values()
        for left, right in zip(path, path[1:])
    }
    type_failures = nearest_failures = 0
    for frame in frames:
        mapped_charged = {R822.S789.matvec(frame, site) for site in charged}
        mapped_neutral = {R822.S789.matvec(frame, site) for site in neutral}
        type_failures += (
            len(mapped_charged) != len(charged)
            or len(mapped_neutral) != len(neutral)
            or bool(mapped_charged & mapped_neutral)
        )
        nearest_failures += sum(
            R822.S789.manhattan(
                R822.S789.matvec(frame, left),
                R822.S789.matvec(frame, right),
            ) != 1
            for left, right in edges
        )
    samples = tuple(sorted(charged | neutral))[:256]
    product_failures = product_closure_failures = 0
    for left in frames:
        for right in frames:
            combined = R822.S789.matmul(left, right)
            product_closure_failures += combined not in frames
            product_failures += any(
                R822.S789.matvec(left, R822.S789.matvec(right, site))
                != R822.S789.matvec(combined, site)
                for site in samples
            )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "unique_route_edges": len(edges),
        "transported_type_partition_failures": type_failures,
        "transported_nearest_neighbour_failures": nearest_failures,
        "coordinate_product_failures": product_failures,
        "proper_cubic_product_closure_failures": product_closure_failures,
        "coordinate_product_sites_tested": len(samples),
        "covariance_scope": (
            "passive signed-permutation transport of the fixed atlas; "
            "intrinsic atlas generation remains supplied"
        ),
    }


def paired_receipt_certificate(swaps, factors, semantics, atlas, covariance):
    payload = json.loads((ROOT / RECEIPT_PATH).read_text())
    expected = {
        "artifact": Path(RUNNER_PATH).name,
        "audit": "unset",
        "authority": "none",
        "artifact_provenance_sha256": {
            "note": digest(ROOT / NOTE_PATH),
            "runner": digest(ROOT / RUNNER_PATH),
        },
        "checks_passed": 7,
        "checks_total": 7,
        "claim_scope": (
            "fixed finite parity-safe one/two-M2 recompile and typed route atlas "
            "for the landed 12-bank Cycle719 controller; Cycle823 same-chart "
            "port placement and intrinsic atlas generation remain open"
        ),
        "semantic_recompile": {
            "semantic_gates": semantics["normalized_semantic_gates"],
            "control_order_swaps": swaps,
            "endpoint_truth_rows": semantics["endpoint_truth_rows"],
            "normalized_vs_landed_failures": semantics[
                "normalized_vs_landed_failures"
            ],
            "normalized_inverse_failures": semantics[
                "normalized_inverse_failures"
            ],
        },
        "elementary_factors": {
            "total": factors["expanded_factors"],
            "CNOT": factors["normalized_factor_counts"]["CNOT"],
            "H": factors["normalized_factor_counts"]["H"],
            "T": factors["normalized_factor_counts"]["T"],
            "T_dagger": factors["normalized_factor_counts"]["TD"],
            "original_elementary_parity_violations": factors[
                "original_elementary_parity_violations"
            ],
            "normalized_elementary_parity_violations": factors[
                "normalized_elementary_parity_violations"
            ],
            "original_noncommuting_prefixes": factors[
                "original_noncommuting_prefixes"
            ],
            "normalized_noncommuting_prefixes": factors[
                "normalized_noncommuting_prefixes"
            ],
            "original_terminal_parity_returns": factors[
                "original_terminal_parity_returns"
            ],
            "normalized_terminal_parity_returns": factors[
                "normalized_terminal_parity_returns"
            ],
            "toffoli_decomposition_maximum_residual": factors[
                "toffoli_decomposition_maximum_residual"
            ],
        },
        "typed_atlas": {
            "unique_two_M2_pairs": atlas["unique_two_M2_pairs"],
            "two_M2_factor_occurrences": atlas["two_M2_factor_occurrences"],
            "charged_unique_pairs": atlas["charged_unique_pairs"],
            "charged_pair_occurrences": atlas["charged_pair_occurrences"],
            "charged_corridor_sites": atlas["charged_corridor_sites"],
            "charged_route_exchange": atlas["charged_route_exchange"],
            "neutral_route_exchange": atlas["neutral_route_exchange"],
            "blank_corridor_FSWAP_vs_SWAP_residual": atlas[
                "blank_corridor_FSWAP_vs_SWAP_residual"
            ],
            "blank_corridor_returned_FSWAP_CNOT_FSWAP_residual": atlas[
                "blank_corridor_returned_FSWAP_CNOT_FSWAP_residual"
            ],
            "neutral_unique_pairs_rerouted": atlas[
                "neutral_unique_pairs_rerouted"
            ],
            "neutral_pair_occurrences_rerouted": atlas[
                "neutral_pair_occurrences_rerouted"
            ],
            "maximum_route_distance": atlas["maximum_route_distance"],
            "routed_gates_per_H": atlas["routed_total_gates"],
            "routed_gates_per_130_H_orbit": atlas[
                "full_130_H_orbit_routed_controller_gates"
            ],
            "missing_or_structural_route_failures": sum(
                atlas[label]
                for label in (
                    "charged_control_paths_failed",
                    "neutral_paths_failed",
                    "charged_corridor_persistent_hits",
                    "nearest_neighbour_or_repeated_site_failures",
                    "operand_order_failures",
                    "route_return_failures",
                )
            ),
            "charged_neutral_fixed_type_overlap": atlas[
                "charged_neutral_fixed_type_overlap"
            ],
        },
        "legacy_active_control": {
            "charged_corridor_neutral_persistent_hits": atlas[
                "legacy_charged_corridor_neutral_persistent_hits"
            ],
            "charged_neutral_corridor_overlaps": atlas[
                "legacy_charged_neutral_corridor_overlaps"
            ],
            "neutral_corridor_charged_persistent_hits": atlas[
                "legacy_neutral_corridor_charged_persistent_hits"
            ],
            "control_order_mutations_detected": factors[
                "control_order_mutations_detected"
            ],
            "nonlocal_unique_routes": atlas["nonlocal_unique_routes"],
            "nonlocal_unique_route_deletions_detected": atlas[
                "nonlocal_unique_route_deletions_detected"
            ],
        },
        "covariance": {
            "proper_cubic_frames": covariance["proper_cubic_frames"],
            "ordered_frame_products": covariance["ordered_frame_products"],
            "unique_route_edges": covariance["unique_route_edges"],
            "transported_type_partition_failures": covariance[
                "transported_type_partition_failures"
            ],
            "transported_nearest_neighbour_failures": covariance[
                "transported_nearest_neighbour_failures"
            ],
            "coordinate_product_failures": covariance[
                "coordinate_product_failures"
            ],
            "proper_cubic_product_closure_failures": covariance[
                "proper_cubic_product_closure_failures"
            ],
            "coordinate_product_sites_tested": covariance[
                "coordinate_product_sites_tested"
            ],
        },
        "open_boundary": [
            "same-chart Cycle823 endpoint-to-controller physical port placement",
            "intrinsic query-free atlas generation and local type/genesis enforcement",
            "autonomous token/bank genesis, admission, renewal, and multi-source arbitration",
            "physical time, permanent Record, Born/history, source/gravity, and prediction bridge",
        ],
        "status": (
            "cycle827-cycle719-parity-safe-typed-controller-atlas-bounded-positive"
        ),
    }
    section_matches = {
        key: payload.get(key) == value for key, value in expected.items()
    }
    section_matches["no_unpinned_receipt_sections"] = set(payload) == set(expected)
    section_matches["all"] = all(section_matches.values())
    return section_matches


def main() -> None:
    started = time.time()
    declared = (
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and NOTE_PATH in AUDIT_INPUT_PATHS
        and RUNNER_PATH in AUDIT_INPUT_PATHS
        and all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        )
    )
    block = H719.physical_controller_block(H719.BANKS)
    original = block["semantic"]
    normalized, swaps, equivalence_failures = normalize_word(original)
    factors = expanded_certificate(original, normalized)
    semantics = semantic_controller_certificate(normalized)
    atlas = typed_atlas(normalized, block["wire_sites"])
    covariance = covariance_certificate(atlas)
    paths = atlas.pop("paths")
    atlas.pop("fixed_charged")
    atlas.pop("fixed_neutral")
    receipt = paired_receipt_certificate(
        swaps, factors, semantics, atlas, covariance
    )
    checks = {
        "declared_inputs_are_unique_existing_repo_relative_files": declared,
        "six_control_swaps_preserve_the_semantic_controller": (
            swaps == 6
            and equivalence_failures == 0
            and semantics["endpoint_truth_rows"] == 4
            and semantics["normalized_vs_landed_failures"] == 0
            and semantics["normalized_inverse_failures"] == 0
        ),
        "normalized_elementary_word_is_prefix_parity_safe": (
            factors["expanded_factors"] == 740226
            and factors["normalized_factor_counts"] == {
                "CNOT": 303942,
                "H": 96952,
                "T": 193904,
                "TD": 145428,
            }
            and factors["original_elementary_parity_violations"] == 12
            and factors["normalized_elementary_parity_violations"] == 0
            and factors["original_noncommuting_prefixes"] == 18
            and factors["normalized_noncommuting_prefixes"] == 0
            and factors["original_terminal_parity_returns"]
            and factors["normalized_terminal_parity_returns"]
            and factors["control_order_mutation_trials"]
            == factors["control_order_mutations_detected"] == 6
            and factors["toffoli_decomposition_maximum_residual"] < 3.0e-11
        ),
        "fixed_type_route_atlas_is_complete_and_collision_free": (
            atlas["unique_two_M2_pairs"] == 41717
            and atlas["two_M2_factor_occurrences"] == 303942
            and atlas["charged_unique_pairs"] == 8
            and atlas["charged_pair_occurrences"] == 24
            and atlas["charged_control_paths_failed"] == 0
            and atlas["neutral_paths_failed"] == 0
            and atlas["charged_corridor_sites"] == 84
            and atlas["charged_corridor_persistent_hits"] == 0
            and atlas["charged_neutral_fixed_type_overlap"] == 0
            and atlas["nearest_neighbour_or_repeated_site_failures"] == 0
            and atlas["operand_order_failures"] == 0
            and atlas["route_return_failures"] == 0
            and atlas["charged_route_exchange"] == "FSWAP"
            and atlas["neutral_route_exchange"] == "SWAP"
            and atlas["route_exchange_prefix_parity_violations"] == 0
            and atlas["blank_corridor_FSWAP_vs_SWAP_residual"] < 3.0e-11
            and atlas["blank_corridor_returned_FSWAP_CNOT_FSWAP_residual"]
            < 3.0e-11
            and atlas["neutral_unique_pairs_rerouted"] == 1297
            and atlas["neutral_pair_occurrences_rerouted"] == 7700
            and atlas["maximum_route_distance"] == 45
            and atlas["routed_total_gates"] == 13315498
            and atlas["full_130_H_orbit_routed_controller_gates"]
            == 1731014740
        ),
        "legacy_failures_are_repaired_by_active_route_changes": (
            atlas["legacy_charged_corridor_neutral_persistent_hits"] == 10
            and atlas["legacy_charged_neutral_corridor_overlaps"] == 34
            and atlas["legacy_neutral_corridor_charged_persistent_hits"] == 12
            and atlas["neutral_unique_pairs_rerouted"] > 0
            and atlas["nonlocal_unique_route_deletions_detected"]
            == atlas["nonlocal_unique_routes"] == 41056
        ),
        "proper_cubic_transport_and_products_preserve_the_typed_atlas": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and covariance["unique_route_edges"] == 27740
            and covariance["transported_type_partition_failures"] == 0
            and covariance["transported_nearest_neighbour_failures"] == 0
            and covariance["coordinate_product_failures"] == 0
            and covariance["proper_cubic_product_closure_failures"] == 0
        ),
        "paired_receipt_is_current_and_all_values_are_pinned": receipt["all"],
    }
    report = {
        "cycle": 827,
        "status": (
            "cycle827-cycle719-parity-safe-typed-controller-atlas-bounded-positive"
            if all(checks.values()) else "cycle827-failed"
        ),
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "fixed finite parity-safe one/two-M2 recompile and typed route atlas "
            "for the landed 12-bank Cycle719 controller; Cycle823 same-chart "
            "port placement and intrinsic atlas generation remain open"
        ),
        "control_order_swaps": swaps,
        "semantic_equivalence_failures": equivalence_failures,
        "factors": factors,
        "semantic_controller": semantics,
        "atlas": atlas,
        "covariance": covariance,
        "paired_receipt": receipt,
        "checks": checks,
        "inventory": {
            "derived": (
                "six parity-safe Toffoli control reorderings",
                "740226-factor prefix-even one/two-M2 controller word",
                "complete fixed charged/neutral route atlas for 41717 pairs",
                "proper-cubic transported atlas covariance",
            ),
            "supplied": (
                "Cycle719 finite 12-bank program, unique token, bank genesis, and occurrence",
                "fixed laboratory atlas and coframe",
                "blank route workspace inside the declared atlas bounds",
            ),
            "open": (
                "same-chart Cycle823 endpoint-to-controller physical port placement",
                "intrinsic query-free atlas generation and local type enforcement",
                "autonomous token/bank genesis, admission, renewal, and multi-source arbitration",
                "physical time, permanent Record, Born/history, source/gravity, and prediction bridge",
            ),
        },
        "source_sha256": {
            path: digest(ROOT / path) for path in AUDIT_INPUT_PATHS
        } if declared else {},
        "runtime_seconds": time.time() - started,
        "atlas_path_digest": sha256(repr(tuple(sorted(paths.items()))).encode()).hexdigest(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    for label, passed in checks.items():
        print(f"CHECK {label}: {'PASS' if passed else 'FAIL'}")
    if not all(checks.values()):
        raise SystemExit(1)
    print("CYCLE827_CYCLE719_PARITY_SAFE_TYPED_CONTROLLER_ATLAS_BOUNDED_PASS")


if __name__ == "__main__":
    main()
