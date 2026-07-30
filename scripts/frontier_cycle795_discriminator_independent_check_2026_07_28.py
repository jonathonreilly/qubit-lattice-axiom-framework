#!/usr/bin/env python3
"""Cycle 795 independent adversarial discriminator checker.

The Cycle-795 primary is SHA-pinned text/AST only: it is never imported or
executed here.  The 176-key family and the T=1024 outcomes are reconstructed
from the landed Cycle-736/719 machinery.  Feature construction, separator
counting, exhaustive 2-vs-12 relabeling, and forecast voting are separate
implementations.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter
from hashlib import blake2s, sha256
from itertools import combinations
import json
from math import log2
from pathlib import Path
from statistics import median
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PINNED_TEXT_PATHS = (
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
    "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
)
BLOCKLIST_TEXT_PATHS = (
    "scripts/frontier_cycle795_discriminator_census_2026_07_28.py",
)
TEXT_ONLY_MODULES = (
    "frontier_cycle762_residual_as_content_probe_2026_07_28",
    "frontier_cycle762_residual_probe_independent_check_2026_07_28",
    "frontier_cycle790_horizon_extension_2026_07_28",
    "frontier_cycle791_open_keys_resolution_2026_07_28",
    "frontier_cycle795_discriminator_census_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    PINNED_TEXT_PATHS[0]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    PINNED_TEXT_PATHS[1]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    PINNED_TEXT_PATHS[2]:
        "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
    PINNED_TEXT_PATHS[3]:
        "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    BLOCKLIST_TEXT_PATHS[0]:
        "6a52229e9ac3bf5ab45bd25a4088e354c759fc499b58462aa0c2401f89474e7f",
}

RING_STATIONS = 11
FIXTURE_BANKS = 2
FINAL_HORIZON = 1024
FAMILY_SIZE = 176
RESOLVED_SIZE = 14
OPEN_SIZE = 162
STDOUT_LIMIT_BYTES = 150 * 1024
LANDED_CONSTANTS = (130, 11, 2, 5, 12, 288, 6, 3)
NULL_MATERIALITY_ALPHA = 0.05

EXPECTED_PRIMARY_TABLE_SHA256 = (
    "266dd5f0c36cb79eb88a143c303e31ef1f79b068d6131545962ee38f8d24e705"
)
EXPECTED_RESOLVED_ROWS_SHA256 = (
    "e20fada7571cb8e694374ea57f1d4308bb99346326f187f0c4e8fa662514e340"
)
EXPECTED_PRIMARY_CLEAN_NAMES_SHA256 = (
    "dc265dc602faef161bf1483f95810396fe3c4dfa75e7afb1cf9f871a396e6d91"
)
EXPECTED_PRIMARY_NEAR_NAMES_SHA256 = (
    "8e7b3aa2f350d8ac8fc6c79d8e387e67050d09dcb2272ebfe86278ae2970865b"
)
EXPECTED_VOTE_ROWS_SHA256 = (
    "c5cd44ef1c85ab4a6d3ccb765fb2f0a745c00608f67a93aa6508a4b69d551ab0"
)

EXPECTED_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
EXPECTED_PRIOR_CYCLES = {
    (3, (0, 5)): 2,
    (3, (0, 6)): 2,
    (3, (1, 6)): 3,
    (3, (1, 7)): 3,
    (3, (2, 7)): 3,
    (3, (2, 8)): 3,
    (3, (3, 8)): 3,
    (3, (3, 9)): 3,
    (3, (4, 9)): 3,
    (3, (4, 10)): 3,
    (3, (5, 10)): 3,
}
EXPECTED_CYCLES = {
    **{
        key: (period, period)
        for key, period in EXPECTED_PRIOR_CYCLES.items()
    },
    (2, (0, 9)): (288, 6),
}

Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def top_level_function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def anchor_and_blocklist_certificate() -> dict[str, object]:
    all_paths = AUDIT_INPUT_PATHS + PINNED_TEXT_PATHS + BLOCKLIST_TEXT_PATHS
    payloads = {path: (ROOT / path).read_bytes() for path in all_paths}
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    checker_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    direct_frontier_imports = {
        alias.name
        for node in checker_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    expected_imports = {Path(path).stem for path in AUDIT_INPUT_PATHS}
    checker_imports_text_only = any(
        isinstance(node, ast.Import)
        and any(alias.name in TEXT_ONLY_MODULES for alias in node.names)
        or isinstance(node, ast.ImportFrom)
        and node.module in TEXT_ONLY_MODULES
        for node in checker_tree.body
    )
    audit_tuple = literal_assignment(checker_tree, "AUDIT_INPUT_PATHS")
    cycle790_tree = trees[PINNED_TEXT_PATHS[2]]
    cycle791_tree = trees[PINNED_TEXT_PATHS[3]]
    primary_tree = trees[BLOCKLIST_TEXT_PATHS[0]]
    cycle790_periodic = literal_assignment(
        cycle790_tree, "EXPECTED_PERIODIC_KEYS_T64"
    )
    cycle791_baseline = literal_assignment(
        cycle791_tree, "EXPECTED_BASELINE_CLEAN_KEY"
    )
    cycle791_horizons = literal_assignment(cycle791_tree, "HORIZONS")
    expected_periodic_literal = tuple(
        (event, positions, period)
        for (event, positions), period in EXPECTED_PRIOR_CYCLES.items()
    )
    primary_ast_ok = {
        "feature_table",
        "candidate_result",
        "discrimination_census",
        "run",
    } <= top_level_function_names(primary_tree)
    verdict_ast_ok = (
        {
            "build_family",
            "cycle_census",
            "minimal_phase_period",
        } <= top_level_function_names(cycle790_tree)
        and {
            "build_identity_and_checkpoints",
            "resolution_sweep",
            "run",
        } <= top_level_function_names(cycle791_tree)
    )
    module_paths_exact = (
        Path(M736.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
        and Path(K.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[1]).resolve()
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal_exact": audit_tuple == AUDIT_INPUT_PATHS,
        "input_sha256": actual_sha,
        "direct_landed_imports": tuple(sorted(direct_frontier_imports)),
        "module_paths_exact": module_paths_exact,
        "text_only_modules_loaded": tuple(
            name for name in TEXT_ONLY_MODULES if name in sys.modules
        ),
        "checker_imports_text_only": checker_imports_text_only,
        "primary_AST_only": primary_ast_ok,
        "cycle790_791_verdict_AST": verdict_ast_ok,
        "cycle790_periodic_literal_matches": (
            cycle790_periodic == expected_periodic_literal
        ),
        "cycle791_baseline_literal_matches": (
            cycle791_baseline == (3, (1, 10))
        ),
        "cycle791_horizons_literal_matches": (
            cycle791_horizons == (512, 1024)
        ),
        "guarded_imports_clean": (
            not M736.CHECKS and not M736.OUTPUT_LINES
        ),
    }
    result["pass"] = (
        all((ROOT / path).is_file() for path in all_paths)
        and actual_sha == EXPECTED_SHA256
        and result["AUDIT_INPUT_PATHS_literal_exact"]
        and direct_frontier_imports == expected_imports
        and module_paths_exact
        and not result["text_only_modules_loaded"]
        and not checker_imports_text_only
        and primary_ast_ok
        and verdict_ast_ok
        and result["cycle790_periodic_literal_matches"]
        and result["cycle791_baseline_literal_matches"]
        and result["cycle791_horizons_literal_matches"]
        and result["guarded_imports_clean"]
    )
    return result


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        ) > 1
    )


def closed_synchronous_word(
    program: tuple[object, ...],
    positions: tuple[int, int],
) -> tuple[object, ...]:
    word: list[object] = []
    for step in range(len(program)):
        occupied = {
            (position + step) % len(program)
            for position in positions
        }
        for station, macro in enumerate(program):
            if station in occupied:
                word.extend(K.mapped_macro(macro))
    return tuple(word)


def watched_registers() -> tuple[tuple[str, int], ...]:
    return (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH_{index}", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK_{index}", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )


def residual_coordinates(state: tuple[int, ...]) -> Support:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    coordinates: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        coordinates.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register_name, wire in watched_registers():
            if bank[wire]:
                coordinates.add(("bank", register_name, bank_index))
    for link_index, link in enumerate(links):
        for wire_index, bit in enumerate(link):
            if bit:
                coordinates.add(
                    ("link", f"WIRE_{wire_index}", link_index)
                )
    return frozenset(coordinates)


def canonical_support(support: Support) -> tuple[Coordinate, ...]:
    return tuple(sorted(support))


def construct_family() -> dict[str, object]:
    started = monotonic()
    program = K.interleaved_program(FIXTURE_BANKS)
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks0, links0)
    allocator_word = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs: list[tuple[int, tuple[int, int], tuple[int, ...]]] = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        prepared = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(prepared, program)
        epoch_failures += (
            after != K.A.apply_semantic(prepared, allocator_word)
        )
        epoch_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        epoch_failures += any(rail_b)
        epoch_failures += len(trace) != len(program)
        epochs.append((event, direction, prepared))
        state = after

    positions = separated_pairs()
    landed_positions = {
        M736.occupied_sites(configuration)
        for configuration in M736.configuration_census()["configurations"]
        if sum(configuration) == 2
    }
    words = {
        pair: closed_synchronous_word(program, pair)
        for pair in positions
    }
    word_disagreements = sum(
        words[pair]
        != M736.synchronous_composition_word(program, pair)
        for pair in positions
    )

    states: dict[Key, tuple[int, ...]] = {}
    residues: dict[Key, Support] = {}
    composition_failures = 0
    inverse_failures = 0
    rail_failures = 0
    for event, _direction, prepared in epochs:
        for pair in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                prepared, program, token_positions=pair
            )
            restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
                after, program, token_positions=pair, reverse=True
            )
            expected_rail = tuple(
                int(station in pair)
                for station in range(len(program))
            )
            composition_failures += (
                after != K.A.apply_semantic(prepared, words[pair])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            inverse_failures += (
                restored != prepared
                or inverse_a != rail_a
                or inverse_b != rail_b
            )
            key = (event, pair)
            states[key] = after
            residues[key] = residual_coordinates(after)

    keyset_sha = digest_rows(tuple(sorted(states)))
    residual_rows = tuple(
        (key, canonical_support(residues[key]))
        for key in sorted(residues)
    )
    state_rows = tuple(
        (
            key,
            blake2s(
                bytes(states[key]),
                digest_size=32,
                person=b"C795fam",
            ).hexdigest(),
        )
        for key in sorted(states)
    )
    per_epoch_signatures = tuple(
        len({residues[(event, pair)] for pair in positions})
        for event in range(2 * FIXTURE_BANKS)
    )
    summary = {
        "directions": tuple(direction for _, direction, _ in epochs),
        "program_stations": len(program),
        "positions": len(positions),
        "keys": len(states),
        "position_set_matches_cycle736": set(positions) == landed_positions,
        "cycle736_expected_k2_count": M736.EXPECTED_COUNTS_BY_K[2],
        "word_disagreements": word_disagreements,
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "inverse_failures": inverse_failures,
        "support_classes": len(set(residues.values())),
        "support_classes_by_epoch": per_epoch_signatures,
        "all_initial_residuals_nonzero": all(residues.values()),
        "keyset_sha256": keyset_sha,
        "initial_residual_sha256": digest_rows(residual_rows),
        "initial_state_sha256": digest_rows(state_rows),
        "runtime_seconds": round(monotonic() - started, 6),
    }
    summary["pass"] = (
        summary["directions"] == ((1, 0), (0, 1), (1, 0), (0, 1))
        and summary["program_stations"] == RING_STATIONS
        and summary["positions"]
        == summary["cycle736_expected_k2_count"]
        == 44
        and summary["keys"] == FAMILY_SIZE
        and summary["position_set_matches_cycle736"]
        and summary["word_disagreements"] == 0
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
        and summary["inverse_failures"] == 0
        and summary["support_classes"] == 25
        and summary["support_classes_by_epoch"] == (1, 1, 12, 14)
        and summary["all_initial_residuals_nonzero"]
        and summary["keyset_sha256"]
        == "788e673e0a8f8f46931dd549dbdff0010a21d82f98c3363859e8da2e160bf756"
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "residues": residues,
        "directions": summary["directions"],
        "summary": summary,
    }


def state_fingerprint(state: tuple[int, ...]) -> bytes:
    return blake2s(
        bytes(state), digest_size=32, person=b"C795dyn"
    ).digest()


def evolve_exact(
    initial_state: tuple[int, ...],
    word: tuple[object, ...],
    updates: int,
) -> tuple[int, ...]:
    state = initial_state
    for _ in range(updates):
        state = K.A.apply_semantic(state, word)
    return state


def least_period(phases: tuple[int, ...]) -> int:
    for candidate in range(1, len(phases) + 1):
        if len(phases) % candidate:
            continue
        if all(
            phases[index] == phases[index % candidate]
            for index in range(len(phases))
        ):
            return candidate
    raise AssertionError(("no phase period", len(phases)))


def sweep_to_1024(family: dict[str, object]) -> dict[str, object]:
    started = monotonic()
    support_ids: dict[Support, int] = {frozenset(): 0}
    support_weights = [0]

    def support_id(support: Support) -> int:
        if support not in support_ids:
            support_ids[support] = len(support_ids)
            support_weights.append(len(support))
        return support_ids[support]

    records: dict[Key, dict[str, object]] = {}
    total_collisions = 0
    total_exact_repeats = 0
    for key in sorted(family["states"]):
        initial_state = family["states"][key]
        word = family["words"][key[1]]
        initial_support = residual_coordinates(initial_state)
        phase_ids = [support_id(initial_support)]
        first_digest = state_fingerprint(initial_state)
        seen: dict[bytes, list[int]] = {first_digest: [0]}
        state = initial_state
        first_clean = 0 if not initial_support else None
        cycle_entry = None
        cycle_closure = None
        state_period = None
        residual_period = None
        cycle_nonzero = None
        exact_cycle_equality = None
        collisions = 0
        exact_repeats = 0
        evolved_through = 0
        trajectory = sha256()
        trajectory.update(first_digest)
        trajectory.update(compact(canonical_support(initial_support)).encode())

        for update in range(1, FINAL_HORIZON + 1):
            if first_clean is not None or cycle_closure is not None:
                break
            state = K.A.apply_semantic(state, word)
            support = residual_coordinates(state)
            phase_ids.append(support_id(support))
            fingerprint = state_fingerprint(state)
            evolved_through = update
            trajectory.update(update.to_bytes(2, "big"))
            trajectory.update(fingerprint)
            trajectory.update(compact(canonical_support(support)).encode())

            if not support:
                first_clean = update
                break

            exact_entry = None
            for candidate_entry in seen.get(fingerprint, ()):
                if evolve_exact(
                    initial_state, word, candidate_entry
                ) == state:
                    exact_entry = candidate_entry
                    break
                collisions += 1
                total_collisions += 1
            if exact_entry is not None:
                cycle_entry = exact_entry
                cycle_closure = update
                state_period = update - exact_entry
                phases = tuple(phase_ids[exact_entry:update])
                residual_period = least_period(phases)
                cycle_nonzero = all(
                    support_weights[phase] > 0 for phase in phases
                )
                exact_cycle_equality = (
                    evolve_exact(initial_state, word, exact_entry)
                    == state
                )
                exact_repeats += 1
                total_exact_repeats += 1
                break
            seen.setdefault(fingerprint, []).append(update)

        records[key] = {
            "first_clean": first_clean,
            "cycle_entry": cycle_entry,
            "cycle_closure": cycle_closure,
            "state_period": state_period,
            "residual_period": residual_period,
            "cycle_nonzero": cycle_nonzero,
            "exact_cycle_equality": exact_cycle_equality,
            "evolved_through": evolved_through,
            "phase_ids": tuple(phase_ids),
            "minimum_residual_weight": min(
                support_weights[phase] for phase in phase_ids
            ),
            "distinct_hash_buckets": len(seen),
            "hash_collisions": collisions,
            "exact_repeats": exact_repeats,
            "trajectory_sha256": trajectory.hexdigest(),
        }

    evidence_rows = tuple(
        (
            key,
            *(
                records[key][field]
                for field in (
                    "first_clean",
                    "cycle_entry",
                    "cycle_closure",
                    "state_period",
                    "residual_period",
                    "cycle_nonzero",
                    "exact_cycle_equality",
                    "evolved_through",
                    "minimum_residual_weight",
                    "distinct_hash_buckets",
                    "hash_collisions",
                    "exact_repeats",
                    "trajectory_sha256",
                )
            ),
        )
        for key in sorted(records)
    )
    return {
        "records": records,
        "hash_collisions": total_collisions,
        "exact_repeats": total_exact_repeats,
        "evidence_sha256": digest_rows(evidence_rows),
        "runtime_seconds": round(monotonic() - started, 6),
    }


def classify_labels(
    sweep: dict[str, object],
) -> dict[str, object]:
    records = sweep["records"]
    transient_keys = tuple(
        key
        for key in sorted(records)
        if records[key]["first_clean"] is not None
        and records[key]["first_clean"] <= FINAL_HORIZON
    )
    cycle_keys = tuple(
        key
        for key in sorted(records)
        if records[key]["first_clean"] is None
        and records[key]["cycle_closure"] is not None
        and records[key]["cycle_closure"] <= FINAL_HORIZON
    )
    open_keys = tuple(
        key
        for key in sorted(records)
        if key not in set(transient_keys) | set(cycle_keys)
    )
    observed_transients = {
        key: records[key]["first_clean"]
        for key in transient_keys
    }
    observed_cycles = {
        key: (
            records[key]["state_period"],
            records[key]["residual_period"],
        )
        for key in cycle_keys
    }
    clean_exact = all(
        records[key]["phase_ids"][records[key]["first_clean"]] == 0
        and all(
            phase != 0
            for phase in records[key]["phase_ids"][
                :records[key]["first_clean"]
            ]
        )
        for key in transient_keys
    )
    cycles_exact = all(
        records[key]["cycle_nonzero"] is True
        and records[key]["exact_cycle_equality"] is True
        and records[key]["cycle_entry"] == 0
        for key in cycle_keys
    )
    open_exhausted = all(
        records[key]["first_clean"] is None
        and records[key]["cycle_closure"] is None
        and records[key]["evolved_through"] == FINAL_HORIZON
        and records[key]["minimum_residual_weight"] > 0
        and records[key]["distinct_hash_buckets"] == FINAL_HORIZON + 1
        for key in open_keys
    )
    result = {
        "transient_keys": transient_keys,
        "cycle_keys": cycle_keys,
        "open_keys": open_keys,
        "observed_transients": observed_transients,
        "observed_cycles": observed_cycles,
        "clean_first_hits_exact": clean_exact,
        "cycles_exact_and_nonzero": cycles_exact,
        "open_exhausted_through_1024": open_exhausted,
        "clean_time_census": dict(
            sorted(Counter(observed_transients.values()).items())
        ),
        "state_period_census": dict(
            sorted(Counter(row[0] for row in observed_cycles.values()).items())
        ),
        "residual_period_census": dict(
            sorted(Counter(row[1] for row in observed_cycles.values()).items())
        ),
    }
    result["pass"] = (
        observed_transients == EXPECTED_TRANSIENTS
        and observed_cycles == EXPECTED_CYCLES
        and len(transient_keys) == 2
        and len(cycle_keys) == 12
        and len(open_keys) == OPEN_SIZE
        and clean_exact
        and cycles_exact
        and open_exhausted
        and sweep["hash_collisions"] == 0
        and sweep["exact_repeats"] == 12
    )
    result["label_sha256"] = digest_rows(
        (transient_keys, cycle_keys, open_keys)
    )
    return result


def independent_feature_schema() -> tuple[str, ...]:
    geometric_and_support = (
        "epoch",
        "epoch_parity",
        "epoch_direction",
        "left",
        "right",
        "clockwise_gap",
        "counterclockwise_gap",
        "ring_separation",
        "ring_long_distance",
        "short_orientation",
        "direction_short_alignment",
        "position_sum",
        "position_product",
        "occupancy_mask",
        "chord_midpoint_mod11",
        "short_arc_start",
        "short_arc_end",
        "left_parity",
        "right_parity",
        "parity_code",
        "same_position_parity",
        "epoch_sum_parity",
        "initial_residual_weight",
        "initial_support_size",
        "support_signature_id",
        "support_kind_mask",
        "support_source_count",
        "support_bank_count",
        "support_link_count",
        "support_bank0_count",
        "support_bank1_count",
        "support_bank_imbalance",
        "support_coordinate_index_sum",
    )
    modular_coordinates = tuple(
        f"{coordinate}_mod_{modulus}"
        for modulus in LANDED_CONSTANTS
        for coordinate in (
            "left",
            "right",
            "position_sum",
            "clockwise_gap",
            "ring_separation",
            "epoch",
        )
    )
    equal_residues = tuple(
        f"same_position_residue_mod_{modulus}"
        for modulus in LANDED_CONSTANTS
    )
    return geometric_and_support + modular_coordinates + equal_residues


FEATURE_SCHEMA = independent_feature_schema()
PAIR_FEATURES = (
    "epoch",
    "epoch_parity",
    "epoch_direction",
    "left",
    "right",
    "clockwise_gap",
    "counterclockwise_gap",
    "ring_separation",
    "short_orientation",
    "direction_short_alignment",
    "position_sum",
    "position_product",
    "occupancy_mask",
    "chord_midpoint_mod11",
    "parity_code",
    "same_position_parity",
    "epoch_sum_parity",
    "initial_residual_weight",
    "support_signature_id",
    "support_kind_mask",
    "support_source_count",
    "support_bank_count",
    "support_link_count",
    "support_bank_imbalance",
)


def support_statistics(
    support: tuple[Coordinate, ...],
) -> dict[str, int]:
    source_count = sum(coordinate[0] == "source" for coordinate in support)
    bank_count = sum(coordinate[0] == "bank" for coordinate in support)
    link_count = sum(coordinate[0] == "link" for coordinate in support)
    bank0_count = sum(
        coordinate[0] == "bank" and coordinate[2] == 0
        for coordinate in support
    )
    bank1_count = sum(
        coordinate[0] == "bank" and coordinate[2] == 1
        for coordinate in support
    )
    kind_mask = (
        int(source_count > 0)
        + 2 * int(bank_count > 0)
        + 4 * int(link_count > 0)
    )
    return {
        "source_count": source_count,
        "bank_count": bank_count,
        "link_count": link_count,
        "bank0_count": bank0_count,
        "bank1_count": bank1_count,
        "kind_mask": kind_mask,
        "coordinate_index_sum": sum(
            coordinate[2] for coordinate in support
        ),
    }


def independent_feature_table(
    family: dict[str, object],
) -> dict[str, object]:
    canonical_supports = {
        key: canonical_support(support)
        for key, support in family["residues"].items()
    }
    support_classes = {
        support: identifier
        for identifier, support in enumerate(
            sorted(set(canonical_supports.values()))
        )
    }
    features: dict[Key, tuple[int, ...]] = {}
    rows: list[tuple[int, ...]] = []
    for key in sorted(family["states"]):
        epoch, (left, right) = key
        clockwise = (right - left) % RING_STATIONS
        counterclockwise = (left - right) % RING_STATIONS
        separation = min(clockwise, counterclockwise)
        long_distance = max(clockwise, counterclockwise)
        short_orientation = 1 if clockwise < counterclockwise else -1
        epoch_direction = (
            1 if family["directions"][epoch] == (1, 0) else -1
        )
        short_start, short_end = (
            (left, right)
            if short_orientation == 1
            else (right, left)
        )
        support = canonical_supports[key]
        support_stats = support_statistics(support)

        named: dict[str, int] = {
            "epoch": epoch,
            "epoch_parity": epoch % 2,
            "epoch_direction": epoch_direction,
            "left": left,
            "right": right,
            "clockwise_gap": clockwise,
            "counterclockwise_gap": counterclockwise,
            "ring_separation": separation,
            "ring_long_distance": long_distance,
            "short_orientation": short_orientation,
            "direction_short_alignment":
                epoch_direction * short_orientation,
            "position_sum": left + right,
            "position_product": left * right,
            "occupancy_mask": (1 << left) | (1 << right),
            "chord_midpoint_mod11":
                (6 * (left + right)) % RING_STATIONS,
            "short_arc_start": short_start,
            "short_arc_end": short_end,
            "left_parity": left % 2,
            "right_parity": right % 2,
            "parity_code": 2 * (left % 2) + right % 2,
            "same_position_parity": int(left % 2 == right % 2),
            "epoch_sum_parity": (epoch + left + right) % 2,
            "initial_residual_weight": len(support),
            "initial_support_size": len(support),
            "support_signature_id": support_classes[support],
            "support_kind_mask": support_stats["kind_mask"],
            "support_source_count": support_stats["source_count"],
            "support_bank_count": support_stats["bank_count"],
            "support_link_count": support_stats["link_count"],
            "support_bank0_count": support_stats["bank0_count"],
            "support_bank1_count": support_stats["bank1_count"],
            "support_bank_imbalance":
                support_stats["bank1_count"]
                - support_stats["bank0_count"],
            "support_coordinate_index_sum":
                support_stats["coordinate_index_sum"],
        }
        for modulus in LANDED_CONSTANTS:
            named.update(
                {
                    f"left_mod_{modulus}": left % modulus,
                    f"right_mod_{modulus}": right % modulus,
                    f"position_sum_mod_{modulus}":
                        (left + right) % modulus,
                    f"clockwise_gap_mod_{modulus}":
                        clockwise % modulus,
                    f"ring_separation_mod_{modulus}":
                        separation % modulus,
                    f"epoch_mod_{modulus}": epoch % modulus,
                    f"same_position_residue_mod_{modulus}":
                        int(left % modulus == right % modulus),
                }
            )
        feature_row = tuple(int(named[name]) for name in FEATURE_SCHEMA)
        if len(named) != len(FEATURE_SCHEMA):
            raise AssertionError(
                ("feature names differ", set(named) ^ set(FEATURE_SCHEMA))
            )
        features[key] = feature_row
        rows.append((epoch, left, right, *feature_row))
    return {
        "features": features,
        "rows": tuple(rows),
        "table_sha256": digest_rows(tuple(rows)),
        "support_classes": len(support_classes),
    }


def projection(
    features: dict[Key, tuple[int, ...]],
    key: Key,
    names: tuple[str, ...],
    indices: dict[str, int],
) -> tuple[int, ...]:
    return tuple(features[key][indices[name]] for name in names)


def candidate_analysis(
    names: tuple[str, ...],
    features: dict[Key, tuple[int, ...]],
    transient_keys: tuple[Key, ...],
    cycle_keys: tuple[Key, ...],
    open_keys: tuple[Key, ...],
    indices: dict[str, int],
) -> dict[str, object]:
    transient_values = Counter(
        projection(features, key, names, indices)
        for key in transient_keys
    )
    cycle_values = Counter(
        projection(features, key, names, indices)
        for key in cycle_keys
    )
    overlap = set(transient_values) & set(cycle_values)
    violations = sum(
        min(transient_values[value], cycle_values[value])
        for value in overlap
    )
    margin = min(
        (
            sum(abs(left - right) for left, right in zip(tvalue, cvalue))
            for tvalue in transient_values
            for cvalue in cycle_values
        ),
        default=0,
    )
    forecast: list[str] = []
    for key in open_keys:
        value = projection(features, key, names, indices)
        if value in transient_values and value not in cycle_values:
            forecast.append("TRANSIENT")
        elif value in cycle_values and value not in transient_values:
            forecast.append("CYCLE")
        else:
            forecast.append("UNSEEN")
    implication_counts = {
        label: forecast.count(label)
        for label in ("TRANSIENT", "CYCLE", "UNSEEN")
    }
    return {
        "names": names,
        "dimension": len(names),
        "violations": violations,
        "margin": margin,
        "forecast": tuple(forecast),
        "implication_counts": implication_counts,
        "open_classified": OPEN_SIZE - implication_counts["UNSEEN"],
    }


def separator_census(
    features: dict[Key, tuple[int, ...]],
    labels: dict[str, object],
) -> dict[str, object]:
    indices = {
        name: index for index, name in enumerate(FEATURE_SCHEMA)
    }
    candidate_names = (
        tuple((name,) for name in FEATURE_SCHEMA)
        + tuple(combinations(PAIR_FEATURES, 2))
    )
    candidates = tuple(
        candidate_analysis(
            names,
            features,
            labels["transient_keys"],
            labels["cycle_keys"],
            labels["open_keys"],
            indices,
        )
        for names in candidate_names
    )
    clean = sorted(
        (row for row in candidates if row["violations"] == 0),
        key=lambda row: (
            -row["open_classified"],
            row["dimension"],
            -row["margin"],
            row["names"],
        ),
    )
    near = sorted(
        (row for row in candidates if row["violations"] == 1),
        key=lambda row: (
            -row["open_classified"],
            row["dimension"],
            row["names"],
        ),
    )
    return {
        "candidate_names": candidate_names,
        "candidates": candidates,
        "clean": tuple(clean),
        "near": tuple(near),
        "clean_names_sha256": digest_rows(
            tuple(row["names"] for row in clean)
        ),
        "near_names_sha256": digest_rows(
            tuple(row["names"] for row in near)
        ),
    }


def projection_is_clean(
    values: tuple[tuple[int, ...], ...],
    transient_indices: tuple[int, int],
) -> bool:
    transient_index_set = set(transient_indices)
    transient_values = {
        values[index] for index in transient_indices
    }
    cycle_values = {
        value
        for index, value in enumerate(values)
        if index not in transient_index_set
    }
    return transient_values.isdisjoint(cycle_values)


def exhaustive_null_test(
    features: dict[Key, tuple[int, ...]],
    labels: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    indices = {
        name: index for index, name in enumerate(FEATURE_SCHEMA)
    }
    resolved_keys = tuple(
        sorted(labels["transient_keys"] + labels["cycle_keys"])
    )
    true_pair = tuple(sorted(labels["transient_keys"]))
    candidate_projections = tuple(
        (
            names,
            tuple(
                projection(features, key, names, indices)
                for key in resolved_keys
            ),
        )
        for names in census["candidate_names"]
    )
    labeling_rows = []
    for transient_indices in combinations(range(RESOLVED_SIZE), 2):
        transient_pair = tuple(
            resolved_keys[index] for index in transient_indices
        )
        clean_count = sum(
            projection_is_clean(values, transient_indices)
            for _names, values in candidate_projections
        )
        labeling_rows.append((transient_pair, clean_count))
    true_count = next(
        count for pair, count in labeling_rows if pair == true_pair
    )
    counts = sorted(count for _pair, count in labeling_rows)
    histogram = dict(sorted(Counter(counts).items()))
    lower = sum(count < true_count for count in counts)
    tied = sum(count == true_count for count in counts)
    higher = sum(count > true_count for count in counts)
    upper_tail_numerator = tied + higher
    upper_tail_probability = upper_tail_numerator / len(counts)
    materially_more = upper_tail_probability <= NULL_MATERIALITY_ALPHA
    verdict = (
        "TRUE_LABELING_MATERIALLY_MORE_SEPARATED_THAN_NULL"
        if materially_more
        else "SEPARATORS_UNINFORMATIVE_AT_THIS_SAMPLE"
    )
    return {
        "verdict": verdict,
        "labelings_enumerated": len(labeling_rows),
        "candidate_count_per_labeling": len(candidate_projections),
        "true_transient_pair": true_pair,
        "true_clean_separator_count": true_count,
        "null_min": min(counts),
        "null_median": median(counts),
        "null_max": max(counts),
        "histogram": histogram,
        "labelings_lower_tied_higher": {
            "lower": lower,
            "tied": tied,
            "higher": higher,
        },
        "true_ascending_rank_interval": (
            lower + 1,
            lower + tied,
        ),
        "upper_tail_including_ties": (
            upper_tail_numerator,
            len(counts),
        ),
        "upper_tail_probability": upper_tail_probability,
        "materiality_rule":
            "materially_more iff exact upper-tail including ties <= 0.05",
        "materially_more": materially_more,
        "labeling_rows_sha256": digest_rows(tuple(labeling_rows)),
        "pass": (
            len(labeling_rows) == 91
            and len(set(pair for pair, _count in labeling_rows)) == 91
            and all(
                len(candidate_projections) == 365
                for _pair, _count in labeling_rows
            )
            and sum(histogram.values()) == 91
            and true_count == len(census["clean"]) == 103
            and (min(counts), median(counts), max(counts))
            == (60, 88, 206)
            and (lower, tied, higher) == (69, 3, 19)
            and upper_tail_numerator == 22
            and verdict == "SEPARATORS_UNINFORMATIVE_AT_THIS_SAMPLE"
        ),
    }


def forecast_vote_audit(
    labels: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    clean = census["clean"]
    open_keys = labels["open_keys"]
    forecasts = tuple(row["forecast"] for row in clean)
    vote_rows = []
    for index, key in enumerate(open_keys):
        counts = tuple(
            sum(forecast[index] == label for forecast in forecasts)
            for label in ("TRANSIENT", "CYCLE", "UNSEEN")
        )
        probabilities = [
            count / len(clean) for count in counts if count
        ]
        entropy_bits = -sum(
            probability * log2(probability)
            for probability in probabilities
        )
        vote_rows.append((key, *counts, round(entropy_bits, 9)))

    pairwise_disagreements = tuple(
        sum(left != right for left, right in zip(first, second))
        for first, second in combinations(forecasts, 2)
    )
    coverage = tuple(
        sum(label != "UNSEEN" for label in forecast)
        for forecast in forecasts
    )
    best = clean[0]
    summary = {}
    for offset, label in enumerate(("TRANSIENT", "CYCLE", "UNSEEN"), 1):
        values = [row[offset] for row in vote_rows]
        summary[label] = {
            "min": min(values),
            "median": median(values),
            "max": max(values),
            "total": sum(values),
        }
    summary.update(
        {
            "open_keys_contested": sum(
                sum(count > 0 for count in row[1:4]) > 1
                for row in vote_rows
            ),
            "open_keys_unanimous": sum(
                max(row[1:4]) == len(clean)
                for row in vote_rows
            ),
            "unique_forecast_vectors": len(set(forecasts)),
            "pairwise_disagreement": {
                "pairs": len(pairwise_disagreements),
                "min": min(pairwise_disagreements),
                "median": median(pairwise_disagreements),
                "max": max(pairwise_disagreements),
                "mean":
                    sum(pairwise_disagreements)
                    / len(pairwise_disagreements),
            },
            "separator_open_coverage": {
                "min": min(coverage),
                "median": median(coverage),
                "max": max(coverage),
            },
            "entropy_bits": {
                "min": min(row[4] for row in vote_rows),
                "median": median(row[4] for row in vote_rows),
                "max": max(row[4] for row in vote_rows),
                "mean":
                    sum(row[4] for row in vote_rows) / len(vote_rows),
            },
        }
    )
    return {
        "best": {
            "names": best["names"],
            "margin_L1": best["margin"],
            "implication_counts": best["implication_counts"],
        },
        "summary": summary,
        "vote_rows": tuple(vote_rows),
        "vote_rows_sha256": digest_rows(tuple(vote_rows)),
        "pass": (
            len(clean) == 103
            and len(forecasts) == 103
            and all(len(row) == OPEN_SIZE for row in forecasts)
            and best["names"]
            == (
                "direction_short_alignment",
                "epoch_sum_parity",
            )
            and best["margin"] == 1
            and best["implication_counts"]
            == {"TRANSIENT": 42, "CYCLE": 120, "UNSEEN": 0}
            and len(vote_rows) == OPEN_SIZE
            and all(sum(row[1:4]) == 103 for row in vote_rows)
            and summary["TRANSIENT"]
            == {"min": 0, "median": 3.0, "max": 99, "total": 1156}
            and summary["open_keys_contested"] == 162
            and summary["open_keys_unanimous"] == 0
            and summary["unique_forecast_vectors"] == 46
            and summary["pairwise_disagreement"]["median"] == 40
            and summary["pairwise_disagreement"]["max"] == 162
            and digest_rows(tuple(vote_rows))
            == EXPECTED_VOTE_ROWS_SHA256
        ),
    }


def full_analysis(
    family: dict[str, object],
    labels: dict[str, object],
) -> dict[str, object]:
    table = independent_feature_table(family)
    census = separator_census(table["features"], labels)
    null_test = exhaustive_null_test(
        table["features"], labels, census
    )
    forecasts = forecast_vote_audit(labels, census)
    return {
        "table": table,
        "census": census,
        "null_test": null_test,
        "forecasts": forecasts,
    }


def render_output(
    certificates: dict[str, bool],
    findings: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {label}"
        for label, passed in certificates.items()
    ]
    lines.extend(
        f"FINDING {label} {compact(value)}"
        for label, value in findings.items()
    )
    lines.append(
        "NULL_TEST_VERDICT " + str(report["null_test_verdict"])
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def synchronize_report(
    certificates: dict[str, bool],
    report: dict[str, object],
) -> None:
    report["checks"] = dict(certificates)
    report["pass"] = all(certificates.values())
    report["terminal"] = (
        "CYCLE795_DISCRIMINATOR_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE795_DISCRIMINATOR_INDEPENDENT_CHECK_HONEST_FAIL"
    )


def stable_render(
    certificates: dict[str, bool],
    findings: dict[str, object],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        synchronize_report(certificates, report)
        output = render_output(certificates, findings, report)
        size = len(output.encode("utf-8"))
        if (
            report["controls"]["stdout_bytes"] == size
            and findings["F_CONTROLS"]["stdout_bytes"] == size
        ):
            return output
        report["controls"]["stdout_bytes"] = size
        findings["F_CONTROLS"]["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    certificates: dict[str, bool] = {}
    findings: dict[str, object] = {}

    anchors = anchor_and_blocklist_certificate()
    certificates[
        "A_CONTROLS_SHA_ANCHORS_PRIMARY_BLOCKLIST"
    ] = bool(anchors["pass"])
    findings["A_CONTROLS"] = {
        "finding_verbatim":
            "Cycle-795 primary remained SHA-pinned text/AST only; "
            "only the Cycle-736/719 landed machinery was imported",
        **anchors,
    }

    family = construct_family()
    sweep = sweep_to_1024(family)
    labels = classify_labels(sweep)
    analysis = full_analysis(family, labels)
    table = analysis["table"]
    census = analysis["census"]
    null_test = analysis["null_test"]
    forecasts = analysis["forecasts"]

    resolved_keys = tuple(
        sorted(labels["transient_keys"] + labels["cycle_keys"])
    )
    resolved_rows = tuple(
        (key, *table["features"][key])
        for key in resolved_keys
    )
    resolved_output = tuple(
        {
            "key": key,
            "label": (
                "TRANSIENT"
                if key in labels["transient_keys"]
                else "CYCLE"
            ),
            "first_clean": labels["observed_transients"].get(key),
            "periods": labels["observed_cycles"].get(key),
            "feature_values": table["features"][key],
        }
        for key in resolved_keys
    )
    feature_pass = (
        family["summary"]["pass"]
        and labels["pass"]
        and len(FEATURE_SCHEMA) == len(set(FEATURE_SCHEMA)) == 89
        and len(PAIR_FEATURES) == len(set(PAIR_FEATURES)) == 24
        and set(PAIR_FEATURES) <= set(FEATURE_SCHEMA)
        and len(table["features"]) == len(table["rows"]) == FAMILY_SIZE
        and set(table["features"]) == set(family["states"])
        and all(
            len(row) == 3 + len(FEATURE_SCHEMA)
            for row in table["rows"]
        )
        and table["support_classes"] == 25
        and table["table_sha256"] == EXPECTED_PRIMARY_TABLE_SHA256
        and digest_rows(resolved_rows) == EXPECTED_RESOLVED_ROWS_SHA256
        and len(resolved_rows) == RESOLVED_SIZE
    )
    certificates[
        "B_FEATURE_TABLE_RECOUNT_14_LABELS_2_12"
    ] = feature_pass
    findings["B_FEATURE_TABLE_AND_LABELS"] = {
        "finding_verbatim":
            "Independent landed features match the primary's full "
            "176-row table; the independent T=1024 sweep yields exactly "
            "2 transients and 12 certified cycles",
        "feature_schema": FEATURE_SCHEMA,
        "feature_rows": len(table["rows"]),
        "feature_table_sha256": table["table_sha256"],
        "expected_primary_feature_table_sha256":
            EXPECTED_PRIMARY_TABLE_SHA256,
        "resolved_rows_sha256": digest_rows(resolved_rows),
        "resolved_rows": resolved_output,
        "labels": {
            "transients": tuple(
                {
                    "key": key,
                    "first_clean": first_clean,
                }
                for key, first_clean
                in sorted(labels["observed_transients"].items())
            ),
            "cycles": tuple(
                {
                    "key": key,
                    "state_period": periods[0],
                    "residual_period": periods[1],
                }
                for key, periods
                in sorted(labels["observed_cycles"].items())
            ),
            "open_count": len(labels["open_keys"]),
            "clean_time_census": labels["clean_time_census"],
            "state_period_census": labels["state_period_census"],
            "residual_period_census":
                labels["residual_period_census"],
            "clean_first_hits_exact":
                labels["clean_first_hits_exact"],
            "cycles_exact_and_nonzero":
                labels["cycles_exact_and_nonzero"],
            "open_exhausted_through_1024":
                labels["open_exhausted_through_1024"],
        },
        "family_controls": family["summary"],
        "sweep_controls": {
            "hash_algorithm":
                "BLAKE2s-256 plus exact candidate-state re-evolution",
            "hash_collisions": sweep["hash_collisions"],
            "exact_repeats": sweep["exact_repeats"],
            "evidence_sha256": sweep["evidence_sha256"],
            "runtime_seconds": sweep["runtime_seconds"],
        },
    }

    separator_pass = (
        len(census["candidate_names"]) == 365
        and len(FEATURE_SCHEMA) == 89
        and len(tuple(combinations(PAIR_FEATURES, 2))) == 276
        and len(census["clean"]) == 103
        and len(census["near"]) == 143
        and all(
            row["violations"] == 0 and row["margin"] > 0
            for row in census["clean"]
        )
        and all(
            row["violations"] == 1 and row["margin"] == 0
            for row in census["near"]
        )
        and census["clean_names_sha256"]
        == EXPECTED_PRIMARY_CLEAN_NAMES_SHA256
        and census["near_names_sha256"]
        == EXPECTED_PRIMARY_NEAR_NAMES_SHA256
    )
    certificates[
        "C_SEPARATOR_RECOUNT_103_CLEAN_143_NEAR"
    ] = separator_pass
    findings["C_SEPARATOR_RECOUNT"] = {
        "finding_verbatim":
            "Independent recount: 89 single features plus 276 bounded "
            "pairs produce exactly 103 clean separators and 143 "
            "one-violation near-separators",
        "single_features": len(FEATURE_SCHEMA),
        "pairs": len(tuple(combinations(PAIR_FEATURES, 2))),
        "candidates": len(census["candidate_names"]),
        "clean": len(census["clean"]),
        "near": len(census["near"]),
        "clean_names_sha256": census["clean_names_sha256"],
        "near_names_sha256": census["near_names_sha256"],
        "clean_separator_names": tuple(
            row["names"] for row in census["clean"]
        ),
        "near_separator_names": tuple(
            row["names"] for row in census["near"]
        ),
    }

    certificates[
        "D_EXHAUSTIVE_NULL_TEST_91_LABELINGS"
    ] = bool(null_test["pass"])
    findings["D_NULL_TEST"] = {
        "finding_verbatim":
            "TRUE count 103; exhaustive C(14,2) null "
            "min/median/max 60/88/206; exact upper tail 22/91; "
            "SEPARATORS_UNINFORMATIVE_AT_THIS_SAMPLE",
        **null_test,
    }

    certificates[
        "E_FORECAST_SET_AUDIT_42_120_AND_VOTE_ENTROPY"
    ] = bool(forecasts["pass"])
    vote_output = tuple(
        {
            "key": row[0],
            "transient_votes": row[1],
            "cycle_votes": row[2],
            "unseen_votes": row[3],
            "entropy_bits": row[4],
        }
        for row in forecasts["vote_rows"]
    )
    findings["E_FORECAST_VOTES"] = {
        "finding_verbatim":
            "Best separator independently forecasts 42 transient / "
            "120 cycle / 0 unseen; across all 103 clean separators every "
            "open key is contested and transient votes span 0 to 99",
        "clean_separators_voting": len(census["clean"]),
        "best_separator": forecasts["best"],
        "summary": forecasts["summary"],
        "vote_rows_sha256": forecasts["vote_rows_sha256"],
        "per_open_key_votes": vote_output,
    }

    replay_family = construct_family()
    replay_sweep = sweep_to_1024(replay_family)
    replay_labels = classify_labels(replay_sweep)
    replay_analysis = full_analysis(replay_family, replay_labels)
    family_static_deterministic = all(
        replay_family["summary"][field] == family["summary"][field]
        for field in family["summary"]
        if field != "runtime_seconds"
    )
    deterministic = (
        replay_family["summary"]["pass"]
        and family_static_deterministic
        and replay_sweep["evidence_sha256"]
        == sweep["evidence_sha256"]
        and replay_sweep["hash_collisions"]
        == sweep["hash_collisions"]
        == 0
        and replay_sweep["exact_repeats"]
        == sweep["exact_repeats"]
        == 12
        and replay_labels == labels
        and replay_analysis == analysis
        and not any(
            module_name in sys.modules
            for module_name in TEXT_ONLY_MODULES
        )
    )
    elapsed = monotonic() - started
    controls_base = (
        deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and null_test["verdict"]
        in {
            "SEPARATORS_UNINFORMATIVE_AT_THIS_SAMPLE",
            "TRUE_LABELING_MATERIALLY_MORE_SEPARATED_THAN_NULL",
        }
    )
    certificates[
        "F_DETERMINISM_RUNTIME_STDOUT"
    ] = controls_base
    findings["F_CONTROLS"] = {
        "finding_verbatim":
            "Independent family, labels, table, null distribution, and "
            "forecast votes replay identically within the runtime and "
            "stdout bounds",
        "deterministic": deterministic,
        "first_sweep_sha256": sweep["evidence_sha256"],
        "replay_sweep_sha256": replay_sweep["evidence_sha256"],
        "first_sweep_seconds": sweep["runtime_seconds"],
        "replay_sweep_seconds": replay_sweep["runtime_seconds"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "text_only_modules_loaded_after_replay": tuple(
            module_name
            for module_name in TEXT_ONLY_MODULES
            if module_name in sys.modules
        ),
    }

    report = {
        "cycle": 795,
        "status": "INDEPENDENT_ADVERSARIAL_CHECK_COMPLETE",
        "null_test_verdict": null_test["verdict"],
        "true_clean_separators":
            null_test["true_clean_separator_count"],
        "null_distribution": {
            "min": null_test["null_min"],
            "median": null_test["null_median"],
            "max": null_test["null_max"],
            "upper_tail_including_ties":
                null_test["upper_tail_including_ties"],
            "upper_tail_probability":
                null_test["upper_tail_probability"],
        },
        "separator_recount": {
            "clean": len(census["clean"]),
            "near": len(census["near"]),
        },
        "best_forecast": forecasts["best"],
        "forecast_vote_summary": forecasts["summary"],
        "runtime_seconds": round(elapsed, 6),
        "controls": {
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "stdout_bytes": 0,
            "primary_blocklisted_text_AST_only": True,
        },
        "checks": {},
        "pass": False,
        "terminal":
            "CYCLE795_DISCRIMINATOR_INDEPENDENT_CHECK_HONEST_FAIL",
    }
    output = stable_render(certificates, findings, report)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    certificates[
        "F_DETERMINISM_RUNTIME_STDOUT"
    ] = controls_base and stdout_ok
    output = stable_render(certificates, findings, report)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal":
                "CYCLE795_DISCRIMINATOR_INDEPENDENT_CHECK_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "pass": False,
            "terminal":
                "CYCLE795_DISCRIMINATOR_INDEPENDENT_CHECK_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
