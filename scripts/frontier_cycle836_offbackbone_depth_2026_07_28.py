#!/usr/bin/env python3
"""Cycle 836: continue all 133 off-backbone k=2 keys to T=131072.

Cycle 831 and Cycle 833 are SHA-pinned source primaries.  They are read only
as text/AST controls and are blocked from import.  Dynamics are rebuilt from
the landed Cycle-719 controller core.

The S0' watch uses a sound two-stage exact window at every integer moment:
selected target bits admit every possible full-state match, then every
survivor is compared on all 5,815 bits and SHA-256 verified.  Thus windowing
can create false positives, which are counted, but cannot hide a visit.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "624dad4d841e10e24891810dbc500cc4d6ebe871d6f09dd96f89e3189e52e2ff",
    AUDIT_INPUT_PATHS[2]:
        "bd08f5f503e532c724e6ae28915ba2f0b4202360bbe01458924d689e27c79174",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[2]: "b3512e0c3e8acdec7bc3f1cfb4e5bf1a236f8fda",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if either text/AST-only source primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, int]]
Lane = tuple[Key, str]
State = tuple[int, ...]
MaskedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
BASELINE_HORIZON = 65536
TARGET_HORIZON = 131072
BOUNDARIES = (BASELINE_HORIZON, TARGET_HORIZON)
DETERMINISM_SLICE_SIZE = 8
EXPECTED_BASELINE_OPEN_COUNT = 133
EXPECTED_BASELINE_OPEN_SHA256 = (
    "967a68cd833008d9ecb68a42df3b993e3d257fdfd881961a082723c5dd959131"
)
EXPECTED_S0_PRIME_SHA256 = (
    "d874aeeb1d4e5ca29b806886314c796ac32e6658b21f888d8e2aa01044905c12"
)
EXPECTED_S0_PRIME_WEIGHT = 47
S1_ENTRY_MOMENT = 51110
S1_SOURCE_KEY: Key = (1, (1, 6))
BACKBONE_PAIRS: tuple[tuple[int, int], ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
PERIOD_LAW_ROWS = (
    (0, False, 8930),
    (0, True, 8930),
    (1, False, 8928),
    (1, True, 8928),
    (2, False, 288),
    (2, True, 288),
    (3, False, 3),
    (3, True, 2),
)
PERIOD_LAW = {
    (event, contains_zero): period
    for event, contains_zero, period in PERIOD_LAW_ROWS
}
BASELINE_RESOLVED_ROWS: tuple[tuple[Key, str, int], ...] = (
    ((3, (0, 5)), "CYCLE", 2),
    ((3, (0, 6)), "CYCLE", 2),
    ((3, (1, 6)), "CYCLE", 3),
    ((3, (1, 7)), "CYCLE", 3),
    ((3, (2, 7)), "CYCLE", 3),
    ((3, (2, 8)), "CYCLE", 3),
    ((3, (3, 8)), "CYCLE", 3),
    ((3, (3, 9)), "CYCLE", 3),
    ((3, (4, 9)), "CYCLE", 3),
    ((3, (4, 10)), "CYCLE", 3),
    ((3, (5, 10)), "CYCLE", 3),
    ((3, (1, 10)), "TRANSIENT", 252),
    ((2, (0, 9)), "CYCLE", 288),
    ((3, (0, 7)), "TRANSIENT", 371),
    ((1, (0, 9)), "CYCLE", 8928),
    ((0, (0, 9)), "CYCLE", 8930),
    ((0, (1, 6)), "TRANSIENT", 14744),
    ((0, (1, 7)), "TRANSIENT", 14744),
    ((0, (2, 7)), "TRANSIENT", 14744),
    ((0, (2, 8)), "TRANSIENT", 14744),
    ((0, (3, 8)), "TRANSIENT", 14744),
    ((0, (3, 9)), "TRANSIENT", 14744),
    ((0, (4, 9)), "TRANSIENT", 14744),
    ((0, (4, 10)), "TRANSIENT", 14744),
    ((0, (5, 10)), "TRANSIENT", 14744),
    ((2, (1, 6)), "TRANSIENT", 33195),
    ((2, (1, 7)), "TRANSIENT", 33195),
    ((2, (2, 7)), "TRANSIENT", 33195),
    ((2, (2, 8)), "TRANSIENT", 33195),
    ((2, (3, 8)), "TRANSIENT", 33195),
    ((2, (3, 9)), "TRANSIENT", 33195),
    ((2, (4, 9)), "TRANSIENT", 33195),
    ((2, (4, 10)), "TRANSIENT", 33195),
    ((2, (5, 10)), "TRANSIENT", 33195),
    ((1, (1, 6)), "TRANSIENT", 51115),
    ((1, (1, 7)), "TRANSIENT", 51115),
    ((1, (2, 7)), "TRANSIENT", 51115),
    ((1, (2, 8)), "TRANSIENT", 51115),
    ((1, (3, 8)), "TRANSIENT", 51115),
    ((1, (3, 9)), "TRANSIENT", 51115),
    ((1, (4, 9)), "TRANSIENT", 51115),
    ((1, (4, 10)), "TRANSIENT", 51115),
    ((1, (5, 10)), "TRANSIENT", 51115),
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: State | bytes) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


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


def top_level_functions(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    markers = {
        AUDIT_INPUT_PATHS[0]:
            {"interleaved_program", "mapped_macro", "run_orbit"},
        AUDIT_INPUT_PATHS[1]:
            {"build_family", "masked_schedule", "boundary_snapshot"},
        AUDIT_INPUT_PATHS[2]:
            {"fourth_candidate_certificate", "candidate_reach_certificate"},
    }
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "sha256": sha_rows,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "blocked_AST_markers": tuple(
            (path, tuple(sorted(names))) for path, names in markers.items()
        ),
        "blocked_AST_markers_present": all(
            names <= top_level_functions(trees[path])
            for path, names in markers.items()
        ),
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 6,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 6
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and result["blocked_AST_markers_present"]
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def cyclic_separation(key: Key) -> int:
    left, right = key[1]
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def unified_backbone_predicate(key: Key) -> bool:
    return (
        0 not in key[1]
        and cyclic_separation(key) == RING_STATIONS // 2
    )


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
    positions = positions0
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(word)


def build_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
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
        epochs.append((event, before))
        state = after

    positions = separated_pairs()
    words = {
        pair: synchronous_word(program, pair) for pair in positions
    }
    states: dict[Key, State] = {}
    composition_failures = 0
    rail_failures = 0
    for event, before in epochs:
        for pair in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=pair
            )
            expected_rail = tuple(
                int(station in pair) for station in range(RING_STATIONS)
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[pair])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            states[(event, pair)] = after
    summary = {
        "events": len(epochs),
        "pairs": len(positions),
        "keys": len(states),
        "state_bits": len(next(iter(states.values()))),
        "allocator_gates": len(allocator),
        "word_gate_counts": tuple(sorted({
            len(word) for word in words.values()
        })),
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "catalog_sha256": digest(tuple(
            (key, state_sha256(states[key])) for key in sorted(states)
        )),
    }
    summary["pass"] = (
        summary["events"] == 4
        and summary["pairs"] == 44
        and summary["keys"] == FAMILY_SIZE
        and summary["state_bits"] == STATE_BITS
        and summary["allocator_gates"] == 3106
        and summary["word_gate_counts"] == (6212,)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "summary": summary,
    }


def bit_slice(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int], lane: int) -> State:
    return tuple((column >> lane) & 1 for column in columns)


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
) -> tuple[MaskedGate, ...]:
    rows: list[MaskedGate] = []
    for step in range(len(program)):
        for station, program_row in enumerate(program):
            lane_mask = sum(
                1 << lane
                for lane, (key, _role) in enumerate(lanes)
                if station in {
                    (key[1][0] + step) % len(program),
                    (key[1][1] + step) % len(program),
                }
            )
            if not lane_mask:
                continue
            for gate in K.mapped_macro(program_row):
                if gate.kind == "X":
                    rows.append((0, gate.wires[0], 0, 0, lane_mask))
                elif gate.kind == "CNOT":
                    rows.append(
                        (1, gate.wires[0], gate.wires[1], 0, lane_mask)
                    )
                elif gate.kind == "TOF":
                    rows.append((
                        2, gate.wires[0], gate.wires[1],
                        gate.wires[2], lane_mask,
                    ))
                else:
                    raise AssertionError(("non-reversible landed gate", gate))
                if len(set(gate.wires)) != len(gate.wires):
                    raise AssertionError(("repeated landed gate wire", gate))
    return tuple(rows)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def reconstruct_s0_prime(family: dict[str, object]) -> tuple[State, dict[str, object]]:
    lane: Lane = (S1_SOURCE_KEY, "S1_source")
    columns = bit_slice((family["states"][S1_SOURCE_KEY],))
    schedule = masked_schedule(family["program"], (lane,))
    one_step = columns.copy()
    advance(one_step, schedule)
    one_step_exact = (
        un_slice(one_step, 0)
        == K.A.apply_semantic(
            family["states"][S1_SOURCE_KEY],
            family["words"][S1_SOURCE_KEY[1]],
        )
    )
    started = monotonic()
    for _moment in range(1, S1_ENTRY_MOMENT + 1):
        advance(columns, schedule)
    s1 = un_slice(columns, 0)
    candidate = list(s1)
    target_wire = K.M.R12.BANK_BASES[0] + K.A.HEAD[1]
    candidate[target_wire] ^= 1
    s0_prime = tuple(candidate)
    certificate = {
        "source_primary":
            "scripts/frontier_cycle833_funnel_family_2026_07_28.py",
        "source_primary_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[2]],
        "construction":
            "S1 at t=51110 for key (1,(1,6)), then XOR bank0.HEAD[1]",
        "source_key": S1_SOURCE_KEY,
        "source_moment": S1_ENTRY_MOMENT,
        "one_step_scalar_equivalence": one_step_exact,
        "source_weight": sum(s1),
        "candidate_weight": sum(s0_prime),
        "candidate_sha256": state_sha256(s0_prime),
        "expected_candidate_sha256": EXPECTED_S0_PRIME_SHA256,
        "target_wire": target_wire,
        "target_field": "bank0.HEAD[1]",
        "seconds": round(monotonic() - started, 6),
    }
    certificate["pass"] = (
        one_step_exact
        and certificate["source_weight"] == 46
        and certificate["candidate_weight"] == EXPECTED_S0_PRIME_WEIGHT
        and certificate["candidate_sha256"] == EXPECTED_S0_PRIME_SHA256
    )
    return s0_prime, certificate


def watched_residual_rows() -> tuple[tuple[str, int], ...]:
    bank_named = (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *((f"FRESH_{index}", wire)
          for index, wire in enumerate(K.A.FRESH)),
        *((f"ZERO_WORK_{index}", wire)
          for index, wire in enumerate(K.A.ZERO_WORK)),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )
    rows = [("source.SOURCE_POINTER", K.R3.X.SOURCE_POINTER)]
    for bank_index, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        rows.extend(
            (f"bank{bank_index}.{name}", base + wire)
            for name, wire in bank_named
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", base + wire)
            for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(rows)


def nonclean_mask(
    columns: list[int],
    residual_rows: tuple[tuple[str, int], ...],
) -> int:
    mask = 0
    for _name, wire in residual_rows:
        mask |= columns[wire]
    return mask


def equality_to_initial_mask(
    columns: list[int],
    initial_columns: list[int],
    candidates: int,
) -> int:
    matches = candidates
    for current, initial in zip(columns, initial_columns):
        matches &= candidates ^ ((current ^ initial) & candidates)
        if not matches:
            return 0
    return matches


def equality_to_target_mask(
    columns: list[int],
    target: State,
    candidates: int,
    wires: tuple[int, ...] | None = None,
) -> int:
    matches = candidates
    selected = range(len(columns)) if wires is None else wires
    for wire in selected:
        matches &= (
            columns[wire]
            if target[wire]
            else candidates ^ (columns[wire] & candidates)
        )
        if not matches:
            return 0
    return matches


def support_at_lane(
    columns: list[int],
    lane: int,
    residual_rows: tuple[tuple[str, int], ...],
) -> tuple[str, ...]:
    return tuple(
        name for name, wire in residual_rows
        if (columns[wire] >> lane) & 1
    )


def boundary_snapshot(
    horizon: int,
    active_mask: int,
    primary_keys: tuple[Key, ...],
    columns: list[int],
    initial_columns: list[int],
    residual_rows: tuple[tuple[str, int], ...],
    nonclean_prefix_counts: list[int],
    initial_inequality_counts: list[int],
    records: dict[Key, dict[str, object]],
) -> dict[str, object]:
    lanes = lane_numbers(active_mask)
    open_keys = tuple(primary_keys[lane] for lane in lanes)
    nonclean = nonclean_mask(columns, residual_rows)
    recurrence = equality_to_initial_mask(
        columns, initial_columns, active_mask
    )
    state_rows = tuple(
        (
            primary_keys[lane],
            support_at_lane(columns, lane, residual_rows),
            state_sha256(un_slice(columns, lane)),
        )
        for lane in lanes
    )
    result = {
        "horizon": horizon,
        "open_count": len(open_keys),
        "new_transient_count": sum(
            row["outcome"] == "TRANSIENT"
            and int(row["resolution_moment"]) <= horizon
            for row in records.values()
        ),
        "new_cycle_count": sum(
            row["outcome"] == "CYCLE"
            and int(row["resolution_moment"]) <= horizon
            for row in records.values()
        ),
        "population_accounting":
            len(open_keys) + len(records) == EXPECTED_BASELINE_OPEN_COUNT,
        "open_key_sha256": digest(open_keys),
        "landed_boundary_tests_executed": len(lanes),
        "landed_state_rows_sha256": digest(state_rows),
        "open_support_weight_census": dict(sorted(Counter(
            len(row[1]) for row in state_rows
        ).items())),
        "all_open_landed_nonclean":
            active_mask & ~nonclean == 0,
        "no_open_state_equals_t0_at_boundary": recurrence == 0,
        "all_earlier_cleanliness_tests_certified": all(
            nonclean_prefix_counts[lane] == horizon + 1
            for lane in lanes
        ),
        "all_earlier_cycle_returns_excluded": all(
            initial_inequality_counts[lane] == horizon
            for lane in lanes
        ),
    }
    result["pass"] = (
        result["population_accounting"]
        and result["landed_boundary_tests_executed"] == len(open_keys)
        and result["all_open_landed_nonclean"]
        and result["no_open_state_equals_t0_at_boundary"]
        and result["all_earlier_cleanliness_tests_certified"]
        and result["all_earlier_cycle_returns_excluded"]
    )
    return result


def determinism_boundary(
    horizon: int,
    keys: tuple[Key, ...],
    primary_index: dict[Key, int],
    duplicate_index: dict[Key, int],
    columns: list[int],
) -> dict[str, object]:
    rows = tuple({
        "key": key,
        "primary_sha256":
            state_sha256(un_slice(columns, primary_index[key])),
        "duplicate_sha256":
            state_sha256(un_slice(columns, duplicate_index[key])),
        "exact_tuple_equal":
            un_slice(columns, primary_index[key])
            == un_slice(columns, duplicate_index[key]),
    } for key in keys)
    return {
        "horizon": horizon,
        "rows": rows,
        "rows_sha256": digest(rows),
        "all_exact": all(row["exact_tuple_equal"] for row in rows),
    }


def cohort_certificate(
    new_resolutions: tuple[dict[str, object], ...],
    resolution_states: dict[Key, bytes],
) -> dict[str, object]:
    pair_tests = []
    shared_moment_pairs = []
    shared_state_pairs = []
    shared_both_pairs = []
    for left, right in combinations(new_resolutions, 2):
        left_key = left["key"]
        right_key = right["key"]
        same_moment = (
            left["resolution_moment"] == right["resolution_moment"]
        )
        same_state = (
            resolution_states[left_key] == resolution_states[right_key]
        )
        row = (
            left_key,
            right_key,
            same_moment,
            same_state,
            same_moment and same_state,
        )
        pair_tests.append(row)
        if same_moment:
            shared_moment_pairs.append((left_key, right_key))
        if same_state:
            shared_state_pairs.append((left_key, right_key))
        if same_moment and same_state:
            shared_both_pairs.append((left_key, right_key))

    grouped: dict[
        tuple[int, str, int, bool, int],
        list[dict[str, object]],
    ] = {}
    for row in new_resolutions:
        key = row["key"]
        group = (
            int(row["resolution_moment"]),
            str(row["outcome"]),
            key[0],
            0 in key[1],
            cyclic_separation(key),
        )
        grouped.setdefault(group, []).append(row)
    separation_rows = []
    for group, rows in sorted(grouped.items()):
        moment, outcome, event, contains_zero, separation = group
        keys = tuple(row["key"] for row in rows)
        states = tuple(resolution_states[key] for key in keys)
        separation_rows.append({
            "resolution_moment": moment,
            "outcome": outcome,
            "event": event,
            "contains_zero": contains_zero,
            "cyclic_separation": separation,
            "count": len(keys),
            "keys": keys,
            "all_exact_same_state_at_resolution":
                len(set(states)) == 1,
            "resolution_state_sha256s":
                tuple(state_sha256(state) for state in states),
        })

    cyclic_rows = tuple(row for row in new_resolutions
                        if row["outcome"] == "CYCLE")
    period_tests = tuple({
        "key": row["key"],
        "event": row["key"][0],
        "contains_zero": 0 in row["key"][1],
        "observed_minimal_state_period": row["state_period"],
        "Cycle831_period_law_expected": PERIOD_LAW[
            (row["key"][0], 0 in row["key"][1])
        ],
        "law_outcome": (
            "HOLDS"
            if row["state_period"] == PERIOD_LAW[
                (row["key"][0], 0 in row["key"][1])
            ]
            else "FALSIFIED_BY_NEW_CYCLE"
        ),
    } for row in cyclic_rows)
    expected_pair_count = (
        len(new_resolutions) * (len(new_resolutions) - 1) // 2
    )
    result = {
        "new_resolution_count": len(new_resolutions),
        "pairwise_shared_moment_state_test": {
            "tested_pair_count": len(pair_tests),
            "expected_pair_count": expected_pair_count,
            "test_rows_sha256": digest(tuple(pair_tests)),
            "shared_moment_pairs": tuple(shared_moment_pairs),
            "shared_exact_state_pairs": tuple(shared_state_pairs),
            "shared_moment_and_exact_state_pairs":
                tuple(shared_both_pairs),
        },
        "separation_class_census": tuple(separation_rows),
        "separation_class_population_accounting":
            sum(row["count"] for row in separation_rows)
            == len(new_resolutions),
        "unified_backbone_predicate":
            "origin absent AND max cyclic separation=5",
        "all_new_resolutions_fail_unified_backbone_predicate":
            all(
                not unified_backbone_predicate(row["key"])
                for row in new_resolutions
            ),
        "cyclic_period_law_tests": period_tests,
        "cyclic_period_test_accounting":
            len(period_tests) == len(cyclic_rows),
    }
    result["pass"] = (
        len(pair_tests) == expected_pair_count
        and result["separation_class_population_accounting"]
        and result[
            "all_new_resolutions_fail_unified_backbone_predicate"
        ]
        and result["cyclic_period_test_accounting"]
    )
    return result


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
    loud_hits: tuple[str, ...],
) -> str:
    lines = list(loud_hits)
    lines.extend(
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    )
    lines.extend(
        f"CERTIFICATE {name} {compact(value)}"
        for name, value in certificates.items()
    )
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(str(report["terminal"]))
    return "\n".join(lines) + "\n"


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
    loud_hits: tuple[str, ...],
) -> str:
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE836_OFFBACKBONE_DEPTH_PASS"
            if report["pass"]
            else "CYCLE836_OFFBACKBONE_DEPTH_HONEST_FAIL"
        )
        output = render(checks, certificates, report, loud_hits)
        size = len(output.encode("utf-8"))
        controls = certificates["E_CONTROLS"]
        if report["stdout_bytes"] == size and controls["stdout_bytes"] == size:
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    script_started = monotonic()
    sources = source_controls()
    family = build_family()
    s0_prime, s0_construction = reconstruct_s0_prime(family)
    catalog = tuple(sorted(family["states"]))
    baseline_resolved_keys = {
        key for key, _outcome, _moment in BASELINE_RESOLVED_ROWS
    }
    baseline_open = tuple(
        key for key in catalog if key not in baseline_resolved_keys
    )
    backbone_catalog = tuple(
        key for key in catalog if unified_backbone_predicate(key)
    )
    resolved_backbone = tuple(
        key for key in baseline_resolved_keys
        if unified_backbone_predicate(key)
    )
    resolved_offbackbone = tuple(
        key for key in baseline_resolved_keys
        if not unified_backbone_predicate(key)
    )
    baseline_package = {
        "source": "SHA-pinned Cycle-833 T=65536 package",
        "resolved_count": len(BASELINE_RESOLVED_ROWS),
        "resolved_transient_count": sum(
            outcome == "TRANSIENT"
            for _key, outcome, _moment in BASELINE_RESOLVED_ROWS
        ),
        "resolved_cycle_count": sum(
            outcome == "CYCLE"
            for _key, outcome, _moment in BASELINE_RESOLVED_ROWS
        ),
        "unique_resolved_keys":
            len(baseline_resolved_keys) == len(BASELINE_RESOLVED_ROWS),
        "backbone_catalog_count": len(backbone_catalog),
        "resolved_backbone_count": len(resolved_backbone),
        "resolved_offbackbone_count": len(resolved_offbackbone),
        "open_count": len(baseline_open),
        "open_key_sha256": digest(baseline_open),
        "expected_open_key_sha256": EXPECTED_BASELINE_OPEN_SHA256,
        "all_open_fail_unified_backbone_predicate":
            all(not unified_backbone_predicate(key) for key in baseline_open),
    }
    baseline_package["pass"] = (
        baseline_package["resolved_count"] == 43
        and baseline_package["resolved_transient_count"] == 29
        and baseline_package["resolved_cycle_count"] == 14
        and baseline_package["unique_resolved_keys"]
        and baseline_package["backbone_catalog_count"] == 36
        and baseline_package["resolved_backbone_count"] == 36
        and baseline_package["resolved_offbackbone_count"] == 7
        and baseline_package["open_count"] == EXPECTED_BASELINE_OPEN_COUNT
        and baseline_package["open_key_sha256"]
        == EXPECTED_BASELINE_OPEN_SHA256
        and baseline_package[
            "all_open_fail_unified_backbone_predicate"
        ]
    )

    determinism_keys = baseline_open[:DETERMINISM_SLICE_SIZE]
    primary_lanes: tuple[Lane, ...] = tuple(
        (key, "primary") for key in baseline_open
    )
    duplicate_lanes: tuple[Lane, ...] = tuple(
        (key, "determinism_duplicate") for key in determinism_keys
    )
    lanes = primary_lanes + duplicate_lanes
    primary_keys = tuple(key for key, _role in primary_lanes)
    primary_index = {
        key: lane for lane, key in enumerate(primary_keys)
    }
    duplicate_index = {
        key: len(primary_lanes) + offset
        for offset, key in enumerate(determinism_keys)
    }
    initial_states = tuple(
        family["states"][key] for key, _role in lanes
    )
    columns = bit_slice(initial_states)
    initial_columns = columns.copy()
    schedule = masked_schedule(family["program"], lanes)
    primary_mask = (1 << len(primary_lanes)) - 1
    residual_rows = watched_residual_rows()
    duplicate_initial_exact = all(
        initial_states[primary_index[key]]
        == initial_states[duplicate_index[key]]
        for key in determinism_keys
    )
    duplicate_masks_identical = all(
        ((mask >> primary_index[key]) & 1)
        == ((mask >> duplicate_index[key]) & 1)
        for _kind, _first, _second, _third, mask in schedule
        for key in determinism_keys
    )
    one_step = columns.copy()
    advance(one_step, schedule)
    one_step_scalar_equivalence = all(
        un_slice(one_step, lane)
        == K.A.apply_semantic(
            family["states"][key], family["words"][key[1]]
        )
        for lane, (key, _role) in enumerate(lanes)
    )

    active_mask = primary_mask
    previous_nonclean = nonclean_mask(columns, residual_rows)
    nonclean_prefix_counts = [
        int(bool(previous_nonclean & (1 << lane)))
        for lane in range(len(primary_lanes))
    ]
    initial_inequality_counts = [0] * len(primary_lanes)
    records: dict[Key, dict[str, object]] = {}
    resolution_states: dict[Key, bytes] = {}

    target_active_wires = tuple(
        wire for wire, bit in enumerate(s0_prime) if bit
    )
    projection_wires = tuple(sorted(set(
        wire * (STATE_BITS - 1) // 255 for wire in range(256)
    )))
    s0_window_wires = tuple(sorted(
        set(target_active_wires) | set(projection_wires)
    ))
    s0_hits: list[dict[str, object]] = []
    s0_moments_scanned = 0
    s0_trajectory_moments_tested = 0
    s0_window_survivors = 0
    s0_full_survivors = 0

    def scan_s0_prime(moment: int) -> None:
        nonlocal s0_moments_scanned
        nonlocal s0_trajectory_moments_tested
        nonlocal s0_window_survivors
        nonlocal s0_full_survivors
        s0_moments_scanned += 1
        s0_trajectory_moments_tested += len(primary_lanes)
        window_matches = equality_to_target_mask(
            columns, s0_prime, primary_mask, s0_window_wires
        )
        s0_window_survivors += window_matches.bit_count()
        full_matches = (
            equality_to_target_mask(
                columns, s0_prime, window_matches
            )
            if window_matches else 0
        )
        s0_full_survivors += full_matches.bit_count()
        for lane in lane_numbers(full_matches):
            state = un_slice(columns, lane)
            observed_sha = state_sha256(state)
            s0_hits.append({
                "trajectory": primary_keys[lane],
                "time": moment,
                "full_5815_bit_equality": state == s0_prime,
                "observed_sha256": observed_sha,
                "expected_sha256": EXPECTED_S0_PRIME_SHA256,
                "hash_verified": observed_sha == EXPECTED_S0_PRIME_SHA256,
            })

    def record_resolution(
        key: Key,
        outcome: str,
        moment: int,
        nonclean: int,
    ) -> None:
        lane = primary_index[key]
        state = un_slice(columns, lane)
        if outcome == "TRANSIENT":
            verification = {
                "method":
                    "ONLINE_EXACT_PER_MOMENT_LANDED_SUPPORT_MONITOR",
                "earlier_moments_checked": moment,
                "earlier_moments_all_nonclean":
                    nonclean_prefix_counts[lane] == moment,
                "landed_veto_at_t_minus_1":
                    bool(previous_nonclean & (1 << lane)),
                "event_is_clean": not bool(nonclean & (1 << lane)),
                "observed_state_sha256": state_sha256(state),
            }
            verification["pass"] = (
                verification["earlier_moments_all_nonclean"]
                and verification["landed_veto_at_t_minus_1"]
                and verification["event_is_clean"]
            )
        else:
            verification = {
                "method":
                    "EXACT_RETURN_TO_T0_AT_EVERY_MOMENT_PLUS_REVERSIBILITY",
                "entry": 0,
                "closure": moment,
                "exact_recurrence_to_initial":
                    state == family["states"][key],
                "earlier_return_moments_checked": moment - 1,
                "every_earlier_return_rejected":
                    initial_inequality_counts[lane] == moment - 1,
                "minimal_period":
                    initial_inequality_counts[lane] == moment - 1,
                "all_cycle_phases_nonclean":
                    nonclean_prefix_counts[lane] == moment,
                "reversibility_basis":
                    "each landed update is a composition solely of "
                    "distinct-wire X/CNOT/TOF gates",
                "observed_state_sha256": state_sha256(state),
            }
            verification["pass"] = (
                verification["exact_recurrence_to_initial"]
                and verification["every_earlier_return_rejected"]
                and verification["minimal_period"]
                and verification["all_cycle_phases_nonclean"]
            )
        row: dict[str, object] = {
            "key": key,
            "outcome": outcome,
            "resolution_moment": moment,
            "first_clean": moment if outcome == "TRANSIENT" else None,
            "cycle_entry": 0 if outcome == "CYCLE" else None,
            "state_period": moment if outcome == "CYCLE" else None,
            "off_backbone":
                not unified_backbone_predicate(key),
            "verification": verification,
        }
        records[key] = row
        resolution_states[key] = bytes(state)

    def evolve_phase(start: int, stop: int) -> dict[str, object]:
        nonlocal active_mask, previous_nonclean
        phase_started = monotonic()
        start_active = active_mask
        logical_transitions = 0
        phase_keys: list[Key] = []
        physical_updates = 0
        for moment in range(start + 1, stop + 1):
            advance(columns, schedule)
            physical_updates += 1
            logical_transitions += active_mask.bit_count()
            scan_s0_prime(moment)
            nonclean = nonclean_mask(columns, residual_rows)
            clean_hits = active_mask & ~nonclean
            recurrence_hits = equality_to_initial_mask(
                columns,
                initial_columns,
                active_mask & ~clean_hits,
            )
            for lane in lane_numbers(clean_hits):
                key = primary_keys[lane]
                record_resolution(key, "TRANSIENT", moment, nonclean)
                phase_keys.append(key)
            for lane in lane_numbers(recurrence_hits):
                key = primary_keys[lane]
                record_resolution(key, "CYCLE", moment, nonclean)
                phase_keys.append(key)
            active_mask &= ~(clean_hits | recurrence_hits)
            for lane in lane_numbers(active_mask):
                nonclean_prefix_counts[lane] += int(
                    bool(nonclean & (1 << lane))
                )
                initial_inequality_counts[lane] += 1
            previous_nonclean = nonclean
        upper = start_active.bit_count() * (stop - start)
        expected_savings = sum(
            stop - int(records[key]["resolution_moment"])
            for key in phase_keys
        )
        return {
            "start_horizon": start,
            "end_horizon": stop,
            "active_keys_before": start_active.bit_count(),
            "active_keys_after": active_mask.bit_count(),
            "resolutions_in_phase": len(phase_keys),
            "resolved_keys": tuple(phase_keys),
            "logical_transitions_executed": logical_transitions,
            "logical_transition_upper_if_no_terminals": upper,
            "logical_transitions_saved_by_terminals":
                upper - logical_transitions,
            "expected_savings_from_resolution_moments":
                expected_savings,
            "transition_accounting_exact":
                upper - logical_transitions == expected_savings,
            "physical_global_updates": physical_updates,
            "expected_physical_global_updates": stop - start,
            "population_accounting":
                active_mask.bit_count() + len(phase_keys)
                == start_active.bit_count(),
            "complete_population":
                physical_updates == stop - start,
            "seconds": round(monotonic() - phase_started, 6),
        }

    scan_s0_prime(0)
    baseline_phase = evolve_phase(0, BASELINE_HORIZON)
    baseline_boundary = boundary_snapshot(
        BASELINE_HORIZON,
        active_mask,
        primary_keys,
        columns,
        initial_columns,
        residual_rows,
        nonclean_prefix_counts,
        initial_inequality_counts,
        records,
    )
    baseline_determinism = determinism_boundary(
        BASELINE_HORIZON,
        determinism_keys,
        primary_index,
        duplicate_index,
        columns,
    )
    deep_phase = evolve_phase(BASELINE_HORIZON, TARGET_HORIZON)
    final_boundary = boundary_snapshot(
        TARGET_HORIZON,
        active_mask,
        primary_keys,
        columns,
        initial_columns,
        residual_rows,
        nonclean_prefix_counts,
        initial_inequality_counts,
        records,
    )
    final_determinism = determinism_boundary(
        TARGET_HORIZON,
        determinism_keys,
        primary_index,
        duplicate_index,
        columns,
    )

    prebaseline_resolutions = tuple(
        row for row in records.values()
        if int(row["resolution_moment"]) <= BASELINE_HORIZON
    )
    new_resolutions = tuple(sorted(
        (
            row for row in records.values()
            if int(row["resolution_moment"]) > BASELINE_HORIZON
        ),
        key=lambda row: (row["resolution_moment"], row["key"]),
    ))
    cohorts = cohort_certificate(new_resolutions, resolution_states)
    null_applies = not new_resolutions
    null_certificate = {
        "applies": null_applies,
        "statement": (
            f"NO KEY RESOLVED FROM T={BASELINE_HORIZON + 1} THROUGH "
            f"COMPLETE T={TARGET_HORIZON}; ALL 133 REMAIN OPEN"
            if null_applies else
            "NULL DOES NOT APPLY; CERTIFICATE C PRINTS EVERY NEW "
            "RESOLUTION AND ITS COHORT TESTS"
        ),
        "continuation_transition_accounting": deep_phase,
        "expected_null_logical_transitions":
            EXPECTED_BASELINE_OPEN_COUNT
            * (TARGET_HORIZON - BASELINE_HORIZON),
        "observed_logical_transitions":
            deep_phase["logical_transitions_executed"],
    }
    null_certificate["pass"] = (
        not null_applies
        or (
            deep_phase["resolutions_in_phase"] == 0
            and final_boundary["open_count"] == EXPECTED_BASELINE_OPEN_COUNT
            and null_certificate["observed_logical_transitions"]
            == null_certificate["expected_null_logical_transitions"]
            and deep_phase["complete_population"]
            and deep_phase["transition_accounting_exact"]
        )
    )

    s0_watch = {
        "candidate_sha256": EXPECTED_S0_PRIME_SHA256,
        "candidate_weight": EXPECTED_S0_PRIME_WEIGHT,
        "method":
            "at every integer moment, exact selected-bit window with no "
            "false negatives; every survivor gets full 5815-bit equality "
            "and SHA-256 verification",
        "window_soundness":
            "every full-state equality necessarily agrees on every selected "
            "wire; the full comparison removes all window false positives",
        "window_wire_count": len(s0_window_wires),
        "inclusive_moment_bounds": (0, TARGET_HORIZON),
        "moments_scanned": s0_moments_scanned,
        "trajectory_count": len(primary_lanes),
        "trajectory_moments_tested": s0_trajectory_moments_tested,
        "window_survivor_count": s0_window_survivors,
        "full_equality_survivor_count": s0_full_survivors,
        "window_false_positive_count":
            s0_window_survivors - s0_full_survivors,
        "exact_hit_count": len(s0_hits),
        "exact_hits": tuple(s0_hits),
        "all_hits_hash_verified":
            all(row["hash_verified"] for row in s0_hits),
        "outcome": (
            "DISCOVERY: S0' VISITED; FAMILY-MAP PREDICTION CONFIRMED"
            if s0_hits else
            "NO S0' VISIT THROUGH COMPLETE T=131072; PREDICTION STANDS DEEPER"
        ),
    }
    s0_watch["pass"] = (
        s0_construction["pass"]
        and s0_moments_scanned == TARGET_HORIZON + 1
        and s0_trajectory_moments_tested
        == EXPECTED_BASELINE_OPEN_COUNT * (TARGET_HORIZON + 1)
        and s0_full_survivors == len(s0_hits)
        and s0_watch["all_hits_hash_verified"]
    )

    baseline_exact = (
        baseline_phase["resolutions_in_phase"] == 0
        and baseline_phase["complete_population"]
        and baseline_phase["transition_accounting_exact"]
        and baseline_boundary["pass"]
        and baseline_boundary["open_count"] == EXPECTED_BASELINE_OPEN_COUNT
        and baseline_boundary["open_key_sha256"]
        == EXPECTED_BASELINE_OPEN_SHA256
        and not prebaseline_resolutions
    )
    resolution_verifications_pass = all(
        row["verification"]["pass"] for row in new_resolutions
    )
    certificate_a = {
        "continuation":
            "all 133 Cycle-833-open off-backbone keys, evolved independently "
            "from their landed t=0 states",
        "baseline_horizon": BASELINE_HORIZON,
        "target_horizon": TARGET_HORIZON,
        "deepest_complete_power_of_two": TARGET_HORIZON,
        "partial_horizon_reported": False,
        "baseline_package": baseline_package,
        "family_rebuild": family["summary"],
        "masked_schedule": {
            "primary_lanes": len(primary_lanes),
            "determinism_duplicate_lanes": len(duplicate_lanes),
            "instructions_per_global_update": len(schedule),
            "one_step_scalar_equivalence": one_step_scalar_equivalence,
            "reversibility_basis": "distinct-wire X/CNOT/TOF only",
        },
        "phase_rows": (baseline_phase, deep_phase),
        "complete_boundaries":
            (baseline_boundary, final_boundary),
        "baseline_exact": baseline_exact,
        "new_resolution_verifications_pass":
            resolution_verifications_pass,
        "final_population_accounting":
            43 + len(new_resolutions) + int(final_boundary["open_count"])
            == FAMILY_SIZE,
    }
    certificate_a["pass"] = (
        sources["pass"]
        and family["summary"]["pass"]
        and baseline_package["pass"]
        and one_step_scalar_equivalence
        and baseline_exact
        and deep_phase["complete_population"]
        and deep_phase["transition_accounting_exact"]
        and final_boundary["pass"]
        and resolution_verifications_pass
        and certificate_a["final_population_accounting"]
    )
    certificate_c = {
        "new_resolution_count": len(new_resolutions),
        "new_transient_count": sum(
            row["outcome"] == "TRANSIENT" for row in new_resolutions
        ),
        "new_cycle_count": sum(
            row["outcome"] == "CYCLE" for row in new_resolutions
        ),
        "new_resolutions": new_resolutions,
        "cohort_tests": cohorts,
    }
    certificate_c["pass"] = (
        resolution_verifications_pass and cohorts["pass"]
    )

    deterministic = (
        duplicate_initial_exact
        and duplicate_masks_identical
        and baseline_determinism["all_exact"]
        and final_determinism["all_exact"]
    )
    elapsed = monotonic() - script_started
    controls_base = (
        sources["pass"]
        and deterministic
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificate_e = {
        **sources,
        "determinism_scope": {
            "declaration":
                "first eight lexicographic Cycle-833-open keys carried as "
                "independent duplicate lanes from t=0 through both complete "
                "boundaries",
            "keys": determinism_keys,
            "initial_states_exact": duplicate_initial_exact,
            "identical_schedule_masks": duplicate_masks_identical,
            "boundary_rows":
                (baseline_determinism, final_determinism),
            "deterministic": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
    }
    checks = {
        "A_DEEP_CONTINUATION_COMPLETE_BOUNDARIES":
            bool(certificate_a["pass"]),
        "B_S0_PRIME_EVERY_STEP_HASH_WATCH":
            bool(s0_watch["pass"]),
        "C_RESOLUTIONS_VERIFIED_AND_COHORT_TESTED":
            bool(certificate_c["pass"]),
        "D_NULL_WITH_ACCOUNTING_IF_APPLICABLE":
            bool(null_certificate["pass"]),
        "E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT":
            controls_base,
    }
    certificates = {
        "A_DEEP_CONTINUATION": certificate_a,
        "B_S0_PRIME_WATCH": {
            "construction": s0_construction,
            "watch": s0_watch,
            "pass": s0_watch["pass"],
        },
        "C_RESOLUTIONS_AND_COHORTS": certificate_c,
        "D_NULL_BRANCH": null_certificate,
        "E_CONTROLS": certificate_e,
    }
    report = {
        "cycle": 836,
        "horizon_reached": TARGET_HORIZON,
        "horizon_complete": True,
        "baseline_open_count": EXPECTED_BASELINE_OPEN_COUNT,
        "S0_prime_outcome": s0_watch["outcome"],
        "S0_prime_hits": len(s0_hits),
        "new_resolution_count": len(new_resolutions),
        "new_transient_count": certificate_c["new_transient_count"],
        "new_cycle_count": certificate_c["new_cycle_count"],
        "null_applies": null_applies,
        "final_open_count": final_boundary["open_count"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE836_OFFBACKBONE_DEPTH_HONEST_FAIL",
    }
    loud_hits = tuple(
        "!!! S0_PRIME_DISCOVERY "
        f"trajectory={compact(row['trajectory'])} "
        f"time={row['time']} sha256={row['observed_sha256']} "
        "FULL_TUPLE_AND_HASH_VERIFIED !!!"
        for row in s0_hits
    )
    output = stable_render(checks, certificates, report, loud_hits)
    stdout_ok = len(output.encode("utf-8")) < STDOUT_LIMIT_BYTES
    checks["E_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
        controls_base and stdout_ok
    )
    output = stable_render(checks, certificates, report, loud_hits)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE836_OFFBACKBONE_DEPTH_HONEST_FAIL",
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode("utf-8")),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE836_OFFBACKBONE_DEPTH_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
