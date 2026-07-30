#!/usr/bin/env python3
"""Cycle 797 independent adversarial continuation checker.

The Cycle-797/791/790 primaries are blocklisted: their bytes are used only
for SHA and AST controls and their modules are never imported or executed.
The 176-key family, landed cleanliness projection, controller words, and
evolution are rebuilt from the landed Cycle-736/719 modules.

The main attack starts every key at t=0, independently recovers the 162 keys
open at T=1024, and sweeps every one through T=4096.  Cycle candidates use a
SHA3-256 digest of an independently bit-packed full state and are certified
only by exact state re-evolution.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from collections import Counter
from hashlib import sha256, sha3_256
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


TEXT_ANCHOR_PATHS = (
    "scripts/frontier_cycle762_residual_as_content_probe_2026_07_28.py",
    "scripts/frontier_cycle762_residual_probe_independent_check_2026_07_28.py",
    "scripts/frontier_cycle795_discriminator_census_2026_07_28.py",
)
BLOCKLIST_TEXT_PATHS = (
    "scripts/frontier_cycle797_deep_horizon_continuation_2026_07_28.py",
    "scripts/frontier_cycle791_open_keys_resolution_2026_07_28.py",
    "scripts/frontier_cycle790_horizon_extension_2026_07_28.py",
)
BLOCKLIST_MODULES = (
    "frontier_cycle797_deep_horizon_continuation_2026_07_28",
    "frontier_cycle791_open_keys_resolution_2026_07_28",
    "frontier_cycle790_horizon_extension_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    TEXT_ANCHOR_PATHS[0]:
        "cb5f80cf5d0e169e01561bd9a8665fc8492036398bc0f3eeebe2e326497dbd0d",
    TEXT_ANCHOR_PATHS[1]:
        "c8d43dc2c65b851554393c493d016f6341ba9eb8c3a35bb9f361d77a2f16c619",
    TEXT_ANCHOR_PATHS[2]:
        "6a52229e9ac3bf5ab45bd25a4088e354c759fc499b58462aa0c2401f89474e7f",
    BLOCKLIST_TEXT_PATHS[0]:
        "7ece6f7c818a4dcffb3019c610ca0861998f19cfae0287e23fe98562c1a09698",
    BLOCKLIST_TEXT_PATHS[1]:
        "3380b3f0820a74e0f538b54144bb926a2a4be9041ed21ae5181216f481c8a98a",
    BLOCKLIST_TEXT_PATHS[2]:
        "bc1a47b591e4b308ef3e57ea7776a56223c76c0eca3867816d408f5021e86ac6",
}

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
FINAL_HORIZON = 4096
BOUNDARIES = (256, 1024, 2048, 4096)
EXPECTED_SEPARATOR_COUNT = 103
EXPECTED_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
EXPECTED_CYCLES = {
    (3, (0, 5)): (2, 2),
    (3, (0, 6)): (2, 2),
    (3, (1, 6)): (3, 3),
    (3, (1, 7)): (3, 3),
    (3, (2, 7)): (3, 3),
    (3, (2, 8)): (3, 3),
    (3, (3, 8)): (3, 3),
    (3, (3, 9)): (3, 3),
    (3, (4, 9)): (3, 3),
    (3, (4, 10)): (3, 3),
    (3, (5, 10)): (3, 3),
    (2, (0, 9)): (288, 6),
}
EXPECTED_KEYSET_SHA256 = {
    "family":
        "788e673e0a8f8f46931dd549dbdff0010a21d82f98c3363859e8da2e160bf756",
    "T256_clean":
        "ab0b2a632f6deee4329f02df4834ff3ecc8cd4d885f59459f7dee46fd5dc5bed",
    "T256_cycles":
        "f7fd5f12d3705e30d5dacbf45013d2c4bec743f6e8b72d85df60a6aa8c51b2ae",
    "T256_open":
        "fe07a7b4ffdc2587b01db029d5afe4550d0987eb32fa8873f3afd917d916d947",
}
EXPECTED_FULL_STEP_ACCOUNTING = {
    "T1025_T2048": 162 * (2048 - 1024),
    "T2049_T4096": 162 * (4096 - 2048),
    "total": (
        162 * (2048 - 1024)
        + 162 * (4096 - 2048)
    ),
}
ORIGINAL_TRANSIENT_POSITIONS = ((1, 10), (0, 7))

Key = tuple[int, tuple[int, int]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest_rows(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def keyset_digest(keys: object) -> str:
    return sha256(
        compact(tuple(sorted(keys))).encode("utf-8")
    ).hexdigest()


def literal_tuple_assignment(
    path: Path,
    name: str,
) -> tuple[str, ...] | None:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    matches: list[ast.AST] = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
    if (
        len(matches) != 1
        or not isinstance(matches[0], ast.Tuple)
        or not all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in matches[0].elts
        )
    ):
        return None
    return ast.literal_eval(matches[0])


def top_level_literal(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("top-level assignment count", name, len(matches)))
    return ast.literal_eval(matches[0])


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function count", name, len(matches)))
    return matches[0]


def imported_frontier_modules(tree: ast.Module) -> set[str]:
    result = set()
    for node in tree.body:
        if isinstance(node, ast.Import):
            result.update(
                alias.name
                for alias in node.names
                if alias.name.startswith("frontier_cycle")
            )
        elif (
            isinstance(node, ast.ImportFrom)
            and node.module
            and node.module.startswith("frontier_cycle")
        ):
            result.add(node.module)
    return result


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def text_anchor_and_blocklist_certificate() -> dict[str, object]:
    paths = AUDIT_INPUT_PATHS + TEXT_ANCHOR_PATHS + BLOCKLIST_TEXT_PATHS
    payloads = {path: (ROOT / path).read_bytes() for path in paths}
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
    expected_direct_imports = {
        Path(path).stem for path in AUDIT_INPUT_PATHS
    }
    actual_direct_imports = imported_frontier_modules(checker_tree)
    blocklisted_in_checker_ast = bool(
        actual_direct_imports & set(BLOCKLIST_MODULES)
    )
    requirements = {
        TEXT_ANCHOR_PATHS[0]: {
            "held_two_bank_epochs",
            "k2_positions",
            "continuation_census",
        },
        TEXT_ANCHOR_PATHS[1]: {
            "separated_k2_positions",
            "synchronous_word",
            "watched_bank_registers",
            "residual_support",
            "build_family",
            "asymptotic_census",
        },
        TEXT_ANCHOR_PATHS[2]: {
            "feature_table",
            "discrimination_census",
            "candidate_result",
        },
        BLOCKLIST_TEXT_PATHS[0]: {
            "run_continuation",
            "resolution_rows",
            "hypothesis_table",
            "selection_pattern_check",
            "run",
        },
        BLOCKLIST_TEXT_PATHS[1]: {
            "build_identity_and_checkpoints",
            "advance_one_key",
            "advance_batches",
            "resolution_sweep",
        },
        BLOCKLIST_TEXT_PATHS[2]: {
            "build_family",
            "cycle_census",
            "residual_support",
            "minimal_phase_period",
        },
    }
    ast_shapes_ok = all(
        required <= function_names(trees[path])
        for path, required in requirements.items()
    )
    module_paths_exact = (
        Path(M736.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[0]).resolve()
        and Path(K.__file__).resolve()
        == (ROOT / AUDIT_INPUT_PATHS[1]).resolve()
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal_exact":
            literal_tuple_assignment(Path(__file__), "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "all_anchor_paths_exist":
            all((ROOT / path).is_file() for path in paths),
        "input_sha256": actual_sha,
        "direct_landed_imports": tuple(sorted(actual_direct_imports)),
        "expected_direct_landed_imports":
            tuple(sorted(expected_direct_imports)),
        "module_paths_exact": module_paths_exact,
        "anchored_AST_shapes": ast_shapes_ok,
        "blocklist_text_only": (
            not blocklisted_in_checker_ast
            and not any(name in sys.modules for name in BLOCKLIST_MODULES)
        ),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal_exact"]
        and result["all_anchor_paths_exist"]
        and actual_sha == EXPECTED_SHA256
        and actual_direct_imports == expected_direct_imports
        and module_paths_exact
        and ast_shapes_ok
        and result["blocklist_text_only"]
    )
    return result


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        )
        > 1
    )


def independent_word(
    program: tuple[object, ...],
    initial_positions: tuple[int, int],
) -> tuple[object, ...]:
    word: list[object] = []
    stations = len(program)
    for step in range(stations):
        live = {
            (position + step) % stations
            for position in initial_positions
        }
        for station in range(stations):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
    return tuple(word)


def watched_bank_registers() -> tuple[int, ...]:
    return (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )


def landed_residual_mask(state: tuple[int, ...]) -> int:
    """Independent integer encoding of the exact landed clean projection."""

    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    values = [state[K.R3.X.SOURCE_POINTER]]
    values.extend(
        bank[wire]
        for bank in banks
        for wire in watched_bank_registers()
    )
    values.extend(
        value
        for link in links
        for value in link
    )
    if any(value not in (0, 1) for value in values):
        raise AssertionError("landed residual projection is not binary")
    result = 0
    for index, value in enumerate(values):
        result |= value << index
    return result


def build_family_independently() -> dict[str, object]:
    started = monotonic()
    program = K.interleaved_program(FIXTURE_BANKS)
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks0, links0)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epochs = []
    epoch_failures = 0
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        epoch_failures += after != K.A.apply_semantic(before, allocator)
        epoch_failures += rail_a != (1,) + (0,) * (len(program) - 1)
        epoch_failures += any(rail_b)
        epoch_failures += len(trace) != len(program)
        epochs.append((event, direction, before))
        state = after

    positions = separated_pairs()
    m736_positions = {
        M736.occupied_sites(configuration)
        for configuration in M736.configuration_census()["configurations"]
        if sum(configuration) == 2
    }
    words = {
        pair: independent_word(program, pair)
        for pair in positions
    }
    word_disagreements = sum(
        words[pair]
        != M736.synchronous_composition_word(program, pair)
        for pair in positions
    )
    states: dict[Key, tuple[int, ...]] = {}
    initial_masks: dict[Key, int] = {}
    composition_failures = 0
    inverse_failures = 0
    rail_failures = 0
    for event, _direction, before in epochs:
        for pair in positions:
            after, rail_a, rail_b, _ = K.run_orbit(
                before, program, token_positions=pair
            )
            restored, inverse_a, inverse_b, _ = K.run_orbit(
                after, program, token_positions=pair, reverse=True
            )
            expected_rail = tuple(
                int(station in pair)
                for station in range(len(program))
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[pair])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            inverse_failures += (
                restored != before
                or inverse_a != rail_a
                or inverse_b != rail_b
            )
            key = (event, pair)
            states[key] = after
            initial_masks[key] = landed_residual_mask(after)

    signature_counts = tuple(
        len({
            initial_masks[(event, pair)]
            for pair in positions
        })
        for event in range(2 * FIXTURE_BANKS)
    )
    summary = {
        "epochs": len(epochs),
        "directions": tuple(row[1] for row in epochs),
        "program_stations": len(program),
        "position_count": len(positions),
        "M736_position_set_agrees": set(positions) == m736_positions,
        "M736_expected_k2_count": M736.EXPECTED_COUNTS_BY_K[2],
        "word_disagreements": word_disagreements,
        "key_count": len(states),
        "unique_initial_masks": len(set(initial_masks.values())),
        "unique_initial_masks_by_epoch": signature_counts,
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "inverse_failures": inverse_failures,
        "all_initial_masks_nonzero": all(initial_masks.values()),
        "family_keyset_sha256": keyset_digest(states),
        "initial_mask_sha256": digest_rows(tuple(sorted(initial_masks.items()))),
        "runtime_seconds": round(monotonic() - started, 6),
    }
    summary["pass"] = (
        summary["epochs"] == 4
        and summary["directions"]
        == ((1, 0), (0, 1), (1, 0), (0, 1))
        and summary["program_stations"] == RING_STATIONS
        and summary["position_count"]
        == summary["M736_expected_k2_count"]
        == 44
        and summary["M736_position_set_agrees"]
        and summary["word_disagreements"] == 0
        and summary["key_count"] == FAMILY_SIZE
        and summary["unique_initial_masks"] == 25
        and summary["unique_initial_masks_by_epoch"] == (1, 1, 12, 14)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
        and summary["inverse_failures"] == 0
        and summary["all_initial_masks_nonzero"]
        and summary["family_keyset_sha256"]
        == EXPECTED_KEYSET_SHA256["family"]
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "initial_masks": initial_masks,
        "summary": summary,
    }


def packed_state_bytes(state: tuple[int, ...]) -> bytes:
    """Length-delimited bit packing independent of the primaries' bytes(state)."""

    packed = bytearray((len(state) + 7) // 8)
    for index, value in enumerate(state):
        if value not in (0, 1):
            raise AssertionError(("non-binary state", index, value))
        packed[index // 8] |= value << (index % 8)
    return len(state).to_bytes(4, "big") + bytes(packed)


def recurrence_hash(state: tuple[int, ...]) -> bytes:
    return sha3_256(packed_state_bytes(state)).digest()


def encoded_mask(mask: int) -> bytes:
    payload = mask.to_bytes(max(1, (mask.bit_length() + 7) // 8), "big")
    return len(payload).to_bytes(2, "big") + payload


def evolve_exact(
    initial_state: tuple[int, ...],
    word: tuple[object, ...],
    updates: int,
) -> tuple[int, ...]:
    state = initial_state
    for _ in range(updates):
        state = K.A.apply_semantic(state, word)
    return state


def least_mask_period(masks: tuple[int, ...]) -> int:
    length = len(masks)
    for candidate in range(1, length + 1):
        if length % candidate:
            continue
        if all(
            masks[index] == masks[index % candidate]
            for index in range(length)
        ):
            return candidate
    raise AssertionError(("no finite mask period", length))


def record_signature(record: dict[str, object]) -> dict[str, object]:
    return {
        name: record[name]
        for name in (
            "first_clean",
            "cycle_entry",
            "state_period",
            "residual_period",
            "cycle_closure",
            "cycle_nonzero",
            "exact_cycle_equality",
            "evolved_through",
            "minimum_residual_weight",
            "hash_observations",
            "distinct_hash_buckets",
            "hash_collisions",
            "exact_repeats",
            "trajectory_sha256",
        )
    }


def sweep_keys(
    family: dict[str, object],
    keys: tuple[Key, ...],
    horizon: int,
) -> dict[str, object]:
    """Sweep each key from t=0, stopping only on clean or exact recurrence."""

    started = monotonic()
    records: dict[Key, dict[str, object]] = {}
    total_hash_collisions = 0
    total_exact_repeats = 0
    total_transitions = 0
    for key in keys:
        initial_state = family["states"][key]
        word = family["words"][key[1]]
        initial_mask = landed_residual_mask(initial_state)
        masks = [initial_mask]
        state = initial_state
        initial_digest = recurrence_hash(initial_state)
        seen: dict[bytes, list[int]] = {initial_digest: [0]}
        trajectory = sha256()
        trajectory.update((0).to_bytes(4, "big"))
        trajectory.update(initial_digest)
        trajectory.update(encoded_mask(initial_mask))
        first_clean = 0 if initial_mask == 0 else None
        cycle_entry = None
        state_period = None
        residual_period = None
        cycle_closure = None
        cycle_nonzero = None
        exact_cycle_equality = None
        hash_collisions = 0
        exact_repeats = 0
        evolved_through = 0

        for update in range(1, horizon + 1):
            if first_clean is not None or cycle_closure is not None:
                break
            state = K.A.apply_semantic(state, word)
            total_transitions += 1
            evolved_through = update
            mask = landed_residual_mask(state)
            masks.append(mask)
            state_hash = recurrence_hash(state)
            trajectory.update(update.to_bytes(4, "big"))
            trajectory.update(state_hash)
            trajectory.update(encoded_mask(mask))

            if mask == 0:
                first_clean = update
                break

            exact_entry = None
            for candidate_entry in seen.get(state_hash, ()):
                candidate_state = evolve_exact(
                    initial_state, word, candidate_entry
                )
                if candidate_state == state:
                    exact_entry = candidate_entry
                    break
                hash_collisions += 1
                total_hash_collisions += 1
            if exact_entry is not None:
                cycle_entry = exact_entry
                state_period = update - exact_entry
                cycle_closure = update
                phase_masks = tuple(masks[exact_entry:update])
                residual_period = least_mask_period(phase_masks)
                cycle_nonzero = all(phase_masks)
                exact_cycle_equality = (
                    evolve_exact(initial_state, word, exact_entry) == state
                )
                exact_repeats += 1
                total_exact_repeats += 1
                break
            seen.setdefault(state_hash, []).append(update)

        records[key] = {
            "first_clean": first_clean,
            "cycle_entry": cycle_entry,
            "state_period": state_period,
            "residual_period": residual_period,
            "cycle_closure": cycle_closure,
            "cycle_nonzero": cycle_nonzero,
            "exact_cycle_equality": exact_cycle_equality,
            "evolved_through": evolved_through,
            "phase_masks": tuple(masks),
            "minimum_residual_weight": min(mask.bit_count() for mask in masks),
            "hash_algorithm":
                "SHA3-256(length-delimited independently bit-packed full state)"
                "+exact-state-re-evolution",
            "hash_observations": evolved_through + 1,
            "distinct_hash_buckets": len(seen),
            "hash_collisions": hash_collisions,
            "exact_repeats": exact_repeats,
            "trajectory_sha256": trajectory.hexdigest(),
        }

    deterministic_rows = tuple(
        {"key": key, **record_signature(records[key])}
        for key in keys
    )
    return {
        "records": records,
        "keys": keys,
        "horizon": horizon,
        "transitions": total_transitions,
        "hash_collisions": total_hash_collisions,
        "exact_repeats": total_exact_repeats,
        "deterministic_sha256": digest_rows(deterministic_rows),
        "runtime_seconds": round(monotonic() - started, 6),
    }


def partition_at(
    records: dict[Key, dict[str, object]],
    horizon: int,
) -> dict[str, tuple[Key, ...]]:
    clean = []
    cycles = []
    open_keys = []
    for key in sorted(records):
        record = records[key]
        if (
            record["first_clean"] is not None
            and record["first_clean"] <= horizon
        ):
            clean.append(key)
        elif (
            record["cycle_closure"] is not None
            and record["cycle_closure"] <= horizon
        ):
            cycles.append(key)
        else:
            open_keys.append(key)
    return {
        "clean": tuple(clean),
        "cycles": tuple(cycles),
        "open": tuple(open_keys),
    }


def segment_transition_count(
    records: dict[Key, dict[str, object]],
    keys: tuple[Key, ...],
    start: int,
    end: int,
) -> int:
    transitions = 0
    for key in keys:
        record = records[key]
        terminal = (
            record["first_clean"]
            if record["first_clean"] is not None
            else record["cycle_closure"]
        )
        last = end if terminal is None or terminal > end else terminal
        if last > start:
            transitions += last - start
    return transitions


def transient_nonreappearance(
    family: dict[str, object],
    key: Key,
    expected_moment: int,
) -> dict[str, object]:
    initial_state = family["states"][key]
    state = initial_state
    word = family["words"][key[1]]
    zero_times = []
    clean_state = None
    clean_state_reappearances = []
    exact_state_recurrences = []
    initial_hash = recurrence_hash(state)
    seen: dict[bytes, list[int]] = {initial_hash: [0]}
    requested_spots = {
        0,
        expected_moment - 1,
        expected_moment,
        expected_moment + 1,
        512,
        1024,
        2048,
        4096,
    }
    spots = {}
    for update in range(FINAL_HORIZON + 1):
        mask = landed_residual_mask(state)
        if update:
            state_hash = recurrence_hash(state)
            for candidate_entry in seen.get(state_hash, ()):
                if evolve_exact(
                    initial_state, word, candidate_entry
                ) == state:
                    exact_state_recurrences.append(
                        (candidate_entry, update)
                    )
                    break
            seen.setdefault(state_hash, []).append(update)
        if update in requested_spots:
            spots[update] = mask.bit_count()
        if mask == 0:
            zero_times.append(update)
        if update == expected_moment:
            clean_state = state
        elif (
            update > expected_moment
            and clean_state is not None
            and state == clean_state
        ):
            clean_state_reappearances.append(update)
        if update < FINAL_HORIZON:
            state = K.A.apply_semantic(state, word)
    return {
        "key": key,
        "expected_first_clean": expected_moment,
        "zero_residual_times": tuple(zero_times),
        "later_zero_projection_times":
            tuple(update for update in zero_times if update > expected_moment),
        "exact_full_state_recurrences_through_4096":
            tuple(exact_state_recurrences),
        "clean_state_reappearances_after_event":
            tuple(clean_state_reappearances),
        "spot_residual_weights": dict(sorted(spots.items())),
        "pass": (
            bool(zero_times)
            and zero_times[0] == expected_moment
            and not exact_state_recurrences
            and not clean_state_reappearances
            and spots[expected_moment] == 0
        ),
    }


def cycle_persistence(
    family: dict[str, object],
    key: Key,
    expected_state_period: int,
    expected_residual_period: int,
) -> dict[str, object]:
    word = family["words"][key[1]]
    state = family["states"][key]
    template_states = [state]
    template_masks = [landed_residual_mask(state)]
    for _update in range(1, expected_state_period):
        state = K.A.apply_semantic(state, word)
        template_states.append(state)
        template_masks.append(landed_residual_mask(state))

    mismatches = 0
    zero_residual_updates = 0
    state = family["states"][key]
    horizon_hash = sha256()
    for update in range(FINAL_HORIZON + 1):
        expected_state = template_states[update % expected_state_period]
        mismatches += state != expected_state
        zero_residual_updates += landed_residual_mask(state) == 0
        if update in (0, 1024, 2048, 4096):
            horizon_hash.update(update.to_bytes(4, "big"))
            horizon_hash.update(recurrence_hash(state))
        if update < FINAL_HORIZON:
            state = K.A.apply_semantic(state, word)
    residual_period = least_mask_period(tuple(template_masks))
    return {
        "key": key,
        "entry": 0,
        "state_period": expected_state_period,
        "observed_residual_period": residual_period,
        "expected_residual_period": expected_residual_period,
        "exact_periodic_state_mismatches_through_4096": mismatches,
        "zero_residual_updates_through_4096": zero_residual_updates,
        "horizon_state_sha256": horizon_hash.hexdigest(),
        "pass": (
            mismatches == 0
            and zero_residual_updates == 0
            and residual_period == expected_residual_period
        ),
    }


def rotation_representative(
    positions: tuple[int, int],
) -> tuple[int, int]:
    return min(
        tuple(
            sorted(
                (
                    (positions[0] + shift) % RING_STATIONS,
                    (positions[1] + shift) % RING_STATIONS,
                )
            )
        )
        for shift in range(RING_STATIONS)
    )


def two_for_two_control(family: dict[str, object]) -> dict[str, object]:
    representatives = tuple(sorted({
        rotation_representative(pair)
        for pair in family["positions"]
    }))
    battery = tuple(
        sorted(set(representatives) | set(ORIGINAL_TRANSIENT_POSITIONS))
    )
    requested = {251, 252, 370, 371}
    clean: dict[tuple[tuple[int, int], int], bool] = {}
    for pair in battery:
        state = family["states"][(3, pair)]
        word = family["words"][pair]
        for update in range(max(requested) + 1):
            if update in requested:
                clean[(pair, update)] = landed_residual_mask(state) == 0
            if update < max(requested):
                state = K.A.apply_semantic(state, word)

    rows = []
    for key, moment in sorted(EXPECTED_TRANSIENTS.items()):
        pair = key[1]
        survivors = tuple(
            candidate
            for candidate in battery
            if clean[(candidate, moment)]
        )
        rows.append({
            "key": key,
            "moment": moment,
            "dirty_one_tick_before": not clean[(pair, moment - 1)],
            "survivors_at_moment": survivors,
            "unique_one_tick_selection": (
                not clean[(pair, moment - 1)]
                and survivors == (pair,)
            ),
        })
    return {
        "rotation_representatives": representatives,
        "battery": battery,
        "rows": tuple(rows),
        "pass": all(row["unique_one_tick_selection"] for row in rows),
    }


def qualified_call_name(call: ast.Call) -> str:
    parts = []
    node: ast.AST = call.func
    while isinstance(node, ast.Attribute):
        parts.append(node.attr)
        node = node.value
    if isinstance(node, ast.Name):
        parts.append(node.id)
    return ".".join(reversed(parts))


def dict_constant_keys(node: ast.AST) -> set[str]:
    if not isinstance(node, ast.Dict):
        return set()
    return {
        key.value
        for key in node.keys
        if isinstance(key, ast.Constant) and isinstance(key.value, str)
    }


def primary_coverage_ast_contract() -> dict[str, object]:
    primary_path = ROOT / BLOCKLIST_TEXT_PATHS[0]
    c791_path = ROOT / BLOCKLIST_TEXT_PATHS[1]
    primary_tree = ast.parse(
        primary_path.read_bytes(),
        filename=BLOCKLIST_TEXT_PATHS[0],
    )
    c791_tree = ast.parse(
        c791_path.read_bytes(),
        filename=BLOCKLIST_TEXT_PATHS[1],
    )
    continuation = function_node(primary_tree, "run_continuation")
    continuation_calls = [
        node for node in ast.walk(continuation)
        if isinstance(node, ast.Call)
        and qualified_call_name(node) == "M791.advance_batches"
    ]
    call_arguments = tuple(
        tuple(ast.unparse(argument) for argument in call.args)
        for call in continuation_calls
    )
    advance_call_shape = (
        len(call_arguments) == 2
        and len(call_arguments[0]) == 5
        and len(call_arguments[1]) == 5
        and call_arguments[0][3:] == ("open1024", "HORIZONS[0]")
        and call_arguments[1][3:] == ("covered4096", "HORIZONS[1]")
    )
    covered_assignments = [
        node.value
        for node in continuation.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "covered4096"
            for target in node.targets
        )
    ]
    covered_prefix_shape = (
        len(covered_assignments) == 1
        and ast.unparse(covered_assignments[0])
        == "remaining2048[:prefix_count]"
    )
    continuation_text = ast.unparse(continuation)
    transition_count_wiring = all(
        fragment in continuation_text
        for fragment in (
            "'T1025_T2048': transitions2048",
            "'T2049_T4096': transitions4096",
            "'total': transitions2048 + transitions4096",
        )
    )
    chooser_text = ast.unparse(
        function_node(primary_tree, "choose_t4096_prefix")
    )
    full_flag_exact = (
        "'full_T4096_coverage': selected == len(remaining_open)"
        in chooser_text
    )

    primary_run = function_node(primary_tree, "run")
    printed_calls = []
    for node in ast.walk(primary_run):
        if (
            isinstance(node, ast.Call)
            and qualified_call_name(node) == "data"
            and len(node.args) == 2
            and isinstance(node.args[0], ast.Constant)
            and node.args[0].value == "C_COVERAGE"
        ):
            printed_calls.append(node)
    printed_keys = (
        dict_constant_keys(printed_calls[0].args[1])
        if len(printed_calls) == 1
        else set()
    )
    printed_accounting_wired = (
        len(printed_calls) == 1
        and {
            "T2048_population_covered",
            "T4096_prefix_sha256",
            "T4096_uncovered_keys",
            "transition_counts",
            "phase_seconds",
        } <= printed_keys
        and isinstance(printed_calls[0].args[1], ast.Dict)
        and any(key is None for key in printed_calls[0].args[1].keys)
    )

    advance_batches = function_node(c791_tree, "advance_batches")
    advance_one = function_node(c791_tree, "advance_one_key")
    batch_text = ast.unparse(advance_batches)
    one_text = ast.unparse(advance_one)
    counter_semantics = all(
        fragment in batch_text
        for fragment in (
            "transitions += advance_one_key(",
            "for key in batch:",
        )
    ) and all(
        fragment in one_text
        for fragment in (
            "for update in range(record['last_evolved'] + 1, end_update + 1):",
            "transitions += 1",
            "state = M790.K.A.apply_semantic(record['state'], word)",
            "record['last_evolved'] = update",
        )
    )
    snapshot_text = ast.unparse(
        function_node(c791_tree, "resolution_snapshot")
    )
    status_text = ast.unparse(
        function_node(c791_tree, "record_status")
    )
    uncovered_semantics = all(
        fragment in snapshot_text
        for fragment in (
            "status = record_status(record, horizon)",
            "uncovered.append(key)",
        )
    ) and all(
        fragment in status_text
        for fragment in (
            "if record['last_evolved'] >= horizon:",
            "return f'OPEN_THROUGH_T={horizon}'",
            "return f'UNMEASURED_AFTER_T=",
        )
    )
    constants_exact = (
        top_level_literal(primary_tree, "HORIZONS") == (2048, 4096)
        and top_level_literal(primary_tree, "T1024_OPEN_SIZE") == 162
        and top_level_literal(primary_tree, "FAMILY_SIZE") == 176
        and top_level_literal(primary_tree, "EXPECTED_SEPARATOR_COUNT")
        == EXPECTED_SEPARATOR_COUNT
    )
    result = {
        "primary_constants_exact": constants_exact,
        "advance_batch_call_arguments": call_arguments,
        "two_boundary_advance_calls_exact": advance_call_shape,
        "T4096_population_is_declared_prefix": covered_prefix_shape,
        "full_coverage_flag_is_prefix_equals_population": full_flag_exact,
        "transition_counts_live_wired": transition_count_wiring,
        "C_COVERAGE_printed_keys": tuple(sorted(printed_keys)),
        "printed_accounting_live_wired": printed_accounting_wired,
        "Cycle791_counter_counts_each_semantic_transition":
            counter_semantics,
        "Cycle791_uncovered_test_uses_last_evolved_boundary":
            uncovered_semantics,
        "important_caveat":
            "A-E PASS alone permits a partial adaptive prefix; FULL is valid "
            "only when the printed prefix/full flag/uncovered list and exact "
            "transition counts equal the complete-population accounting.",
    }
    result["pass"] = all(
        result[name]
        for name in (
            "primary_constants_exact",
            "two_boundary_advance_calls_exact",
            "T4096_population_is_declared_prefix",
            "full_coverage_flag_is_prefix_equals_population",
            "transition_counts_live_wired",
            "printed_accounting_live_wired",
            "Cycle791_counter_counts_each_semantic_transition",
            "Cycle791_uncovered_test_uses_last_evolved_boundary",
        )
    )
    return result


def render_output(
    certificates: dict[str, bool],
    findings: dict[str, object],
    report: dict[str, object],
    loud_refutations: tuple[str, ...],
) -> str:
    lines = list(loud_refutations)
    lines.extend(
        f"{'PASS' if passed else 'FAIL'} {label}"
        for label, passed in certificates.items()
    )
    lines.extend(
        f"FINDING {label} {compact(value)}"
        for label, value in findings.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stabilize_output(
    certificates: dict[str, bool],
    findings: dict[str, object],
    report: dict[str, object],
    loud_refutations: tuple[str, ...],
) -> str:
    for _attempt in range(16):
        output = render_output(
            certificates, findings, report, loud_refutations
        )
        size = len(output.encode("utf-8"))
        finding_size = findings["F_CONTROLS"].get("stdout_bytes")
        report_size = report["controls"].get("stdout_bytes")
        if finding_size == size and report_size == size:
            return output
        findings["F_CONTROLS"]["stdout_bytes"] = size
        report["controls"]["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    certificates: dict[str, bool] = {}
    findings: dict[str, object] = {}
    loud_refutations: list[str] = []

    anchors = text_anchor_and_blocklist_certificate()
    certificates[
        "A_SHA_ANCHORS_AND_797_791_790_TEXT_ONLY_BLOCKLIST"
    ] = bool(anchors["pass"])
    findings["A_CONTROLS"] = {
        "finding_verbatim":
            "Cycle-797, Cycle-791, and Cycle-790 primaries remained "
            "SHA-anchored AST text and were never imported or executed.",
        **anchors,
    }

    family = build_family_independently()
    full = sweep_keys(
        family,
        tuple(sorted(family["states"])),
        FINAL_HORIZON,
    )
    records = full["records"]
    partitions = {
        horizon: partition_at(records, horizon)
        for horizon in BOUNDARIES
    }
    t256 = partitions[256]
    t1024 = partitions[1024]
    t2048 = partitions[2048]
    t4096 = partitions[4096]
    open1024 = t1024["open"]

    new_clean = tuple(
        key for key in t4096["clean"] if key in set(open1024)
    )
    new_cycles = tuple(
        key for key in t4096["cycles"] if key in set(open1024)
    )
    missed_resolution_rows = tuple(
        sorted(
            (
                *(
                    {
                        "key": key,
                        "outcome": "TRANSIENT",
                        "first_clean": records[key]["first_clean"],
                    }
                    for key in new_clean
                ),
                *(
                    {
                        "key": key,
                        "outcome": "CYCLE",
                        "entry": records[key]["cycle_entry"],
                        "state_period": records[key]["state_period"],
                        "residual_period": records[key]["residual_period"],
                        "closure": records[key]["cycle_closure"],
                        "exact_state_equality":
                            records[key]["exact_cycle_equality"],
                    }
                    for key in new_cycles
                ),
            ),
            key=lambda row: row["key"],
        )
    )
    for row in missed_resolution_rows:
        loud_refutations.append(
            "!!! MISSED RESOLUTION REFUTES CYCLE-797 PRIMARY !!! "
            + compact(row)
        )

    all_open1024_fully_disposed = all(
        (
            records[key]["first_clean"] is not None
            and 1024 < records[key]["first_clean"] <= FINAL_HORIZON
        )
        or (
            records[key]["cycle_closure"] is not None
            and 1024 < records[key]["cycle_closure"] <= FINAL_HORIZON
            and records[key]["exact_cycle_equality"] is True
            and records[key]["cycle_nonzero"] is True
        )
        or (
            records[key]["first_clean"] is None
            and records[key]["cycle_closure"] is None
            and records[key]["evolved_through"] == FINAL_HORIZON
            and records[key]["hash_observations"] == FINAL_HORIZON + 1
            and records[key]["distinct_hash_buckets"]
            == FINAL_HORIZON + 1
            and records[key]["minimum_residual_weight"] > 0
        )
        for key in open1024
    )
    hunt_executed_cleanly = (
        len(open1024) == 162
        and all_open1024_fully_disposed
        and full["hash_collisions"] == 0
    )
    certificates[
        "B_MISSED_RESOLUTION_HUNT_ALL_162_THROUGH_T4096"
    ] = hunt_executed_cleanly
    hunt_verbatim = (
        "REFUTED: at least one Cycle-797 T=1024-open key resolves by "
        "T=4096."
        if missed_resolution_rows
        else
        "CONFIRMED alternative: all 162 T=1024-open keys remain nonclean "
        "and without an exact certified cycle through T=4096."
    )
    findings["B_MISSED_RESOLUTION_HUNT"] = {
        "finding_verbatim": hunt_verbatim,
        "hash_granularity":
            "SHA3-256 over length-delimited independently bit-packed full "
            "state; every digest hit exact-state re-evolved",
        "T1024_open_keys": len(open1024),
        "coverage": (
            f"{sum(1 for key in open1024 if (
                records[key]['evolved_through'] == FINAL_HORIZON
                or records[key]['first_clean'] is not None
                or records[key]['cycle_closure'] is not None
            ))}/162"
        ),
        "new_clean_events": tuple(
            row for row in missed_resolution_rows
            if row["outcome"] == "TRANSIENT"
        ),
        "new_certified_cycles": tuple(
            row for row in missed_resolution_rows
            if row["outcome"] == "CYCLE"
        ),
        "open_at_T2048": len(t2048["open"]),
        "open_at_T4096": len(t4096["open"]),
        "hash_observations": sum(
            records[key]["hash_observations"] for key in open1024
        ),
        "digest_collisions": sum(
            records[key]["hash_collisions"] for key in open1024
        ),
        "independent_sweep_sha256": full["deterministic_sha256"],
        "sweep_runtime_seconds": full["runtime_seconds"],
    }

    transient_rows = tuple(
        transient_nonreappearance(family, key, moment)
        for key, moment in sorted(EXPECTED_TRANSIENTS.items())
    )
    cycle_rows = tuple(
        cycle_persistence(family, key, periods[0], periods[1])
        for key, periods in sorted(EXPECTED_CYCLES.items())
    )
    observed_transients = {
        key: records[key]["first_clean"]
        for key in t1024["clean"]
    }
    observed_cycles = {
        key: (
            records[key]["state_period"],
            records[key]["residual_period"],
        )
        for key in t1024["cycles"]
    }
    counts = {
        horizon: {
            "clean": len(partition["clean"]),
            "cycles": len(partition["cycles"]),
            "open": len(partition["open"]),
        }
        for horizon, partition in partitions.items()
    }
    t256_keyset_sha = {
        label: keyset_digest(t256[label])
        for label in ("clean", "cycles", "open")
    }
    identity_pass = (
        family["summary"]["pass"]
        and counts[256] == {"clean": 1, "cycles": 11, "open": 164}
        and counts[1024] == {"clean": 2, "cycles": 12, "open": 162}
        and observed_transients == EXPECTED_TRANSIENTS
        and observed_cycles == EXPECTED_CYCLES
        and all(row["pass"] for row in transient_rows)
        and all(row["pass"] for row in cycle_rows)
        and t256_keyset_sha == {
            "clean": EXPECTED_KEYSET_SHA256["T256_clean"],
            "cycles": EXPECTED_KEYSET_SHA256["T256_cycles"],
            "open": EXPECTED_KEYSET_SHA256["T256_open"],
        }
    )
    certificates[
        "C_IDENTITY_2_TRANSIENTS_12_PERSISTENT_CYCLES_AND_FRACTIONS"
    ] = identity_pass
    findings["C_IDENTITY_CONTROLS"] = {
        "finding_verbatim":
            "The first-clean moments are exactly 252 and 371 with no exact "
            "full-state recurrence through T=4096; all 12 cycles persist "
            "exactly through T=4096; T=1024 is 2/12/162.",
        "boundary_counts": counts,
        "T1024_fractions": {
            "clean_transients": "2/176",
            "certified_cycles": "12/176",
            "open": "162/176",
        },
        "observed_transients": tuple(
            {"key": key, "first_clean": moment}
            for key, moment in sorted(observed_transients.items())
        ),
        "transient_nonreappearance_controls": transient_rows,
        "observed_cycles": tuple(
            {
                "key": key,
                "state_period": periods[0],
                "residual_period": periods[1],
            }
            for key, periods in sorted(observed_cycles.items())
        ),
        "cycle_persistence_controls": cycle_rows,
        "T256_keyset_sha256": t256_keyset_sha,
        "T1024_open_key_sha256": keyset_digest(open1024),
        "family": family["summary"],
    }

    ast_coverage = primary_coverage_ast_contract()
    independent_accounting = {
        "T1025_T2048": segment_transition_count(
            records, open1024, 1024, 2048
        ),
        "T2049_T4096": segment_transition_count(
            records, t2048["open"], 2048, 4096
        ),
    }
    independent_accounting["total"] = (
        independent_accounting["T1025_T2048"]
        + independent_accounting["T2049_T4096"]
    )
    every_boundary_fully_evaluated = (
        all(
            records[key]["evolved_through"] >= 2048
            for key in open1024
        )
        and all(
            records[key]["evolved_through"] >= 4096
            for key in t2048["open"]
        )
    )
    coverage_pass = (
        ast_coverage["pass"]
        and len(open1024) == len(t2048["open"]) == len(t4096["open"]) == 162
        and every_boundary_fully_evaluated
        and independent_accounting == EXPECTED_FULL_STEP_ACCOUNTING
    )
    certificates[
        "D_PRIMARY_COVERAGE_AST_AND_PRINTED_STEP_ACCOUNTING"
    ] = coverage_pass
    findings["D_COVERAGE_AUDIT"] = {
        "finding_verbatim": (
            "CONFIRMED FULL coverage: 162/162 keys reach T=2048 and "
            "162/162 reach T=4096; exact continuation accounting is "
            "165888 + 331776 = 497664 semantic transitions."
            if coverage_pass
            else
            "INVALID FULL coverage: the AST/accounting/full-boundary "
            "requirements do not all close."
        ),
        "coverage_verdict": "CONFIRMED" if coverage_pass else "INVALID",
        "primary_AST_contract": ast_coverage,
        "expected_primary_printed_step_accounting":
            EXPECTED_FULL_STEP_ACCOUNTING,
        "independently_measured_full_step_accounting":
            independent_accounting,
        "T2048_population_covered": len(open1024),
        "T4096_population_covered": len(t2048["open"]),
        "T4096_uncovered_keys": tuple(
            key for key in t2048["open"]
            if records[key]["evolved_through"] < 4096
        ),
        "every_boundary_fully_evaluated":
            every_boundary_fully_evaluated,
    }

    selector = two_for_two_control(family)
    no_new_data = not missed_resolution_rows
    hypothesis_control_pass = (
        selector["pass"]
        and (
            no_new_data
            or bool(missed_resolution_rows)
        )
        and top_level_literal(
            ast.parse(
                (ROOT / BLOCKLIST_TEXT_PATHS[0]).read_bytes(),
                filename=BLOCKLIST_TEXT_PATHS[0],
            ),
            "EXPECTED_SEPARATOR_COUNT",
        ) == EXPECTED_SEPARATOR_COUNT
    )
    certificates[
        "E_103_SEPARATOR_SURVIVAL_AND_TWO_FOR_TWO_PIN"
    ] = hypothesis_control_pass
    findings["E_HYPOTHESES_AND_SELECTOR"] = {
        "finding_verbatim": (
            "All 103 separator hypotheses survive because the full "
            "continuation produced zero new resolution data; TWO_FOR_TWO "
            "remains independently pinned."
            if no_new_data
            else
            "A missed resolution exists, so the primary is refuted before "
            "any separator-survival claim can be retained; TWO_FOR_TWO "
            "baseline was still independently checked."
        ),
        "new_resolution_data_rows": len(missed_resolution_rows),
        "separator_count": EXPECTED_SEPARATOR_COUNT,
        "surviving_separator_count":
            EXPECTED_SEPARATOR_COUNT if no_new_data else None,
        "survival_basis":
            "VACUOUS_NO_NEW_RESOLUTION_DATA"
            if no_new_data else "PRIMARY_ALREADY_REFUTED",
        "two_for_two": selector,
    }

    slice_indices = (0, 1, 23, 54, 81, 108, 160, 161)
    declared_slice = tuple(open1024[index] for index in slice_indices)
    replay_family = build_family_independently()
    replay = sweep_keys(replay_family, declared_slice, FINAL_HORIZON)
    slice_deterministic = (
        replay_family["summary"]["pass"]
        and replay_family["summary"]["initial_mask_sha256"]
        == family["summary"]["initial_mask_sha256"]
        and all(
            record_signature(replay["records"][key])
            == record_signature(records[key])
            for key in declared_slice
        )
        and replay["hash_collisions"] == 0
    )
    elapsed = monotonic() - started
    control_base = (
        slice_deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not any(name in sys.modules for name in BLOCKLIST_MODULES)
    )
    certificates[
        "F_DECLARED_SLICE_DETERMINISM_RUNTIME_AND_STDOUT"
    ] = control_base
    findings["F_CONTROLS"] = {
        "finding_verbatim":
            "Declared-slice replay is deterministic; runtime and stdout "
            "remain inside their hard bounds; all three primaries remain "
            "absent from sys.modules.",
        "declared_slice_indices": slice_indices,
        "declared_slice_keys": declared_slice,
        "slice_replay_sha256": replay["deterministic_sha256"],
        "slice_primary_rows_sha256": digest_rows(tuple(
            {"key": key, **record_signature(records[key])}
            for key in declared_slice
        )),
        "deterministic": slice_deterministic,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocklisted_modules_imported":
            tuple(name for name in BLOCKLIST_MODULES if name in sys.modules),
    }

    checker_completed = all(certificates.values())
    refuted = bool(missed_resolution_rows)
    terminal = (
        "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL"
        if not checker_completed
        else (
            "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_REFUTES_PRIMARY"
            if refuted
            else
            "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_CONFIRMED_COVERAGE"
        )
    )
    report = {
        "cycle": 797,
        "role": "INDEPENDENT_ADVERSARIAL_CHECKER",
        "certificates": certificates,
        "hunt_outcome": "MISSED_RESOLUTION_FOUND" if refuted else "NULL_SURVIVES",
        "missed_resolution_count": len(missed_resolution_rows),
        "identity": "2/12/162",
        "coverage_verdict": "CONFIRMED" if coverage_pass else "INVALID",
        "separator_hypotheses_surviving":
            EXPECTED_SEPARATOR_COUNT if no_new_data else None,
        "two_for_two_pinned": selector["pass"],
        "pass": checker_completed,
        "terminal": terminal,
        "controls": {
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "deterministic_slice": slice_deterministic,
        },
    }
    output = stabilize_output(
        certificates, findings, report, tuple(loud_refutations)
    )
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    certificates[
        "F_DECLARED_SLICE_DETERMINISM_RUNTIME_AND_STDOUT"
    ] = control_base and stdout_ok
    findings["F_CONTROLS"]["stdout_under_150KB"] = stdout_ok
    checker_completed = all(certificates.values())
    report["certificates"] = certificates
    report["pass"] = checker_completed
    report["terminal"] = (
        "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL"
        if not checker_completed
        else (
            "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_REFUTES_PRIMARY"
            if refuted
            else
            "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_CONFIRMED_COVERAGE"
        )
    )
    report["controls"]["stdout_under_150KB"] = stdout_ok
    output = stabilize_output(
        certificates, findings, report, tuple(loud_refutations)
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal":
                "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
        sys.stdout.write(
            "FAIL F_DECLARED_SLICE_DETERMINISM_RUNTIME_AND_STDOUT\n"
        )
        sys.stdout.write(compact(failure) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if checker_completed else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        failure = {
            "pass": False,
            "terminal":
                "CYCLE797_INDEPENDENT_ADVERSARIAL_CHECK_CONTROL_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write("FAIL UNCAUGHT_CHECKER_EXCEPTION\n")
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
