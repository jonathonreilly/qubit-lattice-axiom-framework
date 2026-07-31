#!/usr/bin/env python3
"""Cycle 831 independent adversarial check of the claimed cohort structure.

The Cycle-831, Cycle-819, and Cycle-822 primaries are SHA-pinned text/AST
controls only.  They are blocked from import.  All dynamics below are rebuilt
from the landed Cycle-719 core with an independently assembled packed
X/CNOT/TOF schedule and exact tuple comparisons.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle831_deep_k2_forecast_tests_2026_07_28.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle822_basin_independent_check_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


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
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[3]:
        "c2fd23a7bb47caff70e9561fc9da46feef422c053954fa1af925901a1884ed0b",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "ef24edda08118c4e14439b899790fff6c6f94175",
    AUDIT_INPUT_PATHS[2]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[3]: "6d48f5d86006a5f6718b5993eaecd5ec69d86112",
}


class _BlockedPrimaryFinder(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _BlockedPrimaryFinder()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, int]]
Lane = tuple[Key, str]
PackedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
TARGET_HORIZON = 65536
BASELINE_HORIZON = 16384
SSTAR_MOMENT = 14739
ORIGINAL_RESOLUTION = 14744
COHORT_TARGETS = {2: 33195, 1: 51115}
BACKBONE: tuple[tuple[int, int], ...] = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
ORIGINAL_KEYS: tuple[Key, ...] = tuple((0, pair) for pair in BACKBONE)
COHORT_KEYS = {
    event: tuple((event, pair) for pair in BACKBONE)
    for event in COHORT_TARGETS
}
ATTACK_KEYS = COHORT_KEYS[2][:5] + COHORT_KEYS[1][:5]
DETERMINISM_SLICE_SIZE = 4
LANDED_CLOCKS = (4464, 5952, 8928, 8930)

EXPECTED_EARLIER_RESOLVED = frozenset({
    (3, (1, 10)), (3, (0, 7)),
    (3, (0, 5)), (3, (0, 6)),
    (3, (1, 6)), (3, (1, 7)), (3, (2, 7)),
    (3, (2, 8)), (3, (3, 8)), (3, (3, 9)),
    (3, (4, 9)), (3, (4, 10)), (3, (5, 10)),
    (2, (0, 9)), (1, (0, 9)), (0, (0, 9)),
    *ORIGINAL_KEYS,
})


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def state_hash(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    prefix = f"blob {len(payload)}\0".encode()
    return sha1(prefix + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    nodes = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(nodes) != 1:
        return None
    try:
        return ast.literal_eval(nodes[0])
    except (TypeError, ValueError):
        return None


def top_level_functions(tree: ast.Module) -> set[str]:
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
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
    imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    markers = {
        AUDIT_INPUT_PATHS[1]: {"boundary_snapshot", "run"},
        AUDIT_INPUT_PATHS[2]:
            {"advance_population", "verify_cycle", "verify_transient"},
        AUDIT_INPUT_PATHS[3]:
            {"catalog_and_predictor", "masked_schedule", "reconstruct_sstar"},
    }
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
        "direct_frontier_imports": imports,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 7,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and result["blocked_AST_markers_present"]
        and imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_loaded"]
        and not result["firewall_hits"]
        and len(AUDIT_INPUT_PATHS) <= 7
    )
    return result


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


def cyclic_separation(pair: tuple[int, int]) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def orbit_word(
    program: tuple[object, ...],
    pair: tuple[int, int],
) -> tuple[object, ...]:
    rows: list[object] = []
    for step in range(len(program)):
        live = {
            (pair[0] + step) % len(program),
            (pair[1] + step) % len(program),
        }
        for station, macro in enumerate(program):
            if station in live:
                rows.extend(K.mapped_macro(macro))
    return tuple(rows)


def build_seed_family() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    pairs = separated_pairs()
    words = {pair: orbit_word(program, pair) for pair in pairs}
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    epoch_states: list[tuple[int, tuple[int, ...]]] = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        epoch_states.append((event, before))
        state = K.A.apply_semantic(before, allocator)
    states = {
        (event, pair): K.A.apply_semantic(before, words[pair])
        for event, before in epoch_states
        for pair in pairs
    }
    return {
        "program": program,
        "pairs": pairs,
        "words": words,
        "states": states,
        "summary": {
            "events": len(epoch_states),
            "pairs": len(pairs),
            "keys": len(states),
            "state_bits": len(next(iter(states.values()))),
            "allocator_gates": len(allocator),
            "word_gate_counts": tuple(sorted({
                len(word) for word in words.values()
            })),
        },
    }


def watched_residual_wires() -> tuple[tuple[str, int], ...]:
    bank_rows = (
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
            for name, wire in bank_rows
        )
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.extend(
            (f"link{link_index}.WIRE_{wire}", base + wire)
            for wire in range(K.B.LINK_WIDTH)
        )
    return tuple(rows)


def pack_states(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def unpack_lane(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((column >> lane) & 1 for column in columns)


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def packed_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
    included_mask: int,
) -> tuple[PackedGate, ...]:
    schedule: list[PackedGate] = []
    for step in range(len(program)):
        station_masks = [0] * len(program)
        for lane in lane_numbers(included_mask):
            pair = lanes[lane][0][1]
            station_masks[(pair[0] + step) % len(program)] |= 1 << lane
            station_masks[(pair[1] + step) % len(program)] |= 1 << lane
        for station, macro in enumerate(program):
            mask = station_masks[station]
            if not mask:
                continue
            for gate in K.mapped_macro(macro):
                if len(set(gate.wires)) != len(gate.wires):
                    raise AssertionError(("repeated landed gate wire", gate))
                if gate.kind == "X":
                    schedule.append((0, gate.wires[0], 0, 0, mask))
                elif gate.kind == "CNOT":
                    schedule.append(
                        (1, gate.wires[0], gate.wires[1], 0, mask)
                    )
                elif gate.kind == "TOF":
                    schedule.append(
                        (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
                    )
                else:
                    raise AssertionError(("non-reversible gate", gate))
    return tuple(schedule)


def advance(columns: list[int], schedule: tuple[PackedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def nonclean_mask(
    columns: list[int],
    residual_rows: tuple[tuple[str, int], ...],
) -> int:
    mask = 0
    for _name, wire in residual_rows:
        mask |= columns[wire]
    return mask


def exact_initial_mask(
    columns: list[int],
    initial_columns: list[int],
    candidates: int,
) -> int:
    matches = candidates
    for current, initial in zip(columns, initial_columns):
        matches &= candidates ^ ((current ^ initial) & candidates)
        if not matches:
            break
    return matches


def exact_target_mask(
    columns: list[int],
    target: tuple[int, ...],
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
            break
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


def hamming_weight(
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> int:
    return sum(a != b for a, b in zip(left, right))


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    if value < 1:
        raise ValueError(value)
    remaining = value
    rows = []
    prime = 2
    while prime * prime <= remaining:
        exponent = 0
        while remaining % prime == 0:
            remaining //= prime
            exponent += 1
        if exponent:
            rows.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        rows.append((remaining, 1))
    return tuple(rows)


def factor_product(rows: tuple[tuple[int, int], ...]) -> int:
    value = 1
    for prime, exponent in rows:
        value *= prime ** exponent
    return value


def arithmetic_census() -> dict[str, object]:
    moments = (ORIGINAL_RESOLUTION, *COHORT_TARGETS.values())
    subjects = tuple(
        ("moment", value) for value in moments
    ) + tuple(
        (f"difference:{right}-{left}", right - left)
        for left, right in combinations(moments, 2)
    )
    factor_rows = tuple({
        "label": label,
        "value": value,
        "factorization": factorization(value),
        "reconstruction": factor_product(factorization(value)),
    } for label, value in subjects)
    ratio_rows = tuple({
        "left": left,
        "right": right,
        "right_over_left_reduced": (
            Fraction(right, left).numerator,
            Fraction(right, left).denominator,
        ),
        "integer_multiple": right % left == 0,
        "verdict": "HIT" if right % left == 0 else "FAIL",
    } for left, right in combinations(moments, 2))
    clock_rows = tuple({
        "subject": label,
        "value": value,
        "clock": clock,
        "quotient": divmod(value, clock)[0],
        "remainder": divmod(value, clock)[1],
        "exact_multiple": value % clock == 0,
        "verdict": "HIT" if value % clock == 0 else "FAIL",
    } for label, value in subjects for clock in LANDED_CLOCKS)
    clock_pair_rows = tuple({
        "left_clock": left,
        "right_clock": right,
        "right_over_left_reduced": (
            Fraction(right, left).numerator,
            Fraction(right, left).denominator,
        ),
        "integer_multiple": right % left == 0,
        "verdict": "HIT" if right % left == 0 else "FAIL",
    } for left, right in combinations(LANDED_CLOCKS, 2))
    valid = (
        all(row["reconstruction"] == row["value"] for row in factor_rows)
        and all(
            row["value"]
            == row["clock"] * row["quotient"] + row["remainder"]
            and 0 <= row["remainder"] < row["clock"]
            and row["exact_multiple"] == (row["remainder"] == 0)
            for row in clock_rows
        )
        and all(
            Fraction(row["right"], row["left"])
            == Fraction(*row["right_over_left_reduced"])
            for row in ratio_rows
        )
        and any(row["verdict"] == "HIT" for row in clock_pair_rows)
        and any(row["verdict"] == "FAIL" for row in clock_pair_rows)
    )
    return {
        "moments": moments,
        "landed_clocks": LANDED_CLOCKS,
        "factorizations": factor_rows,
        "moment_ratios": ratio_rows,
        "moment_and_difference_clock_divisions": clock_rows,
        "clock_pair_ratios": clock_pair_rows,
        "interpretation":
            "Only exact integer arithmetic is reported; HIT means zero "
            "remainder/integer multiple and FAIL means nonzero remainder.",
        "pass": valid,
    }


def render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    ]
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
) -> str:
    controls = certificates["CONTROLS"]
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["primary_refuted"] = not all(checks.values())
        report["terminal"] = (
            "CYCLE831_COHORTS_INDEPENDENT_CHECK_PASS"
            if report["pass"]
            else "CYCLE831_COHORTS_INDEPENDENT_CHECK_REFUTES_PRIMARY"
        )
        output = render(checks, certificates, report)
        size = len(output.encode())
        if report["stdout_bytes"] == size and controls["stdout_bytes"] == size:
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    family = build_seed_family()
    catalog = tuple(sorted(family["states"]))
    claimed_resolved = (
        set(EXPECTED_EARLIER_RESOLVED)
        | set(COHORT_KEYS[2])
        | set(COHORT_KEYS[1])
    )
    claimed_open = tuple(key for key in catalog if key not in claimed_resolved)
    null_keys = tuple(sorted(
        claimed_open,
        key=lambda key: (sha256(compact(key).encode()).hexdigest(), key),
    )[:10])
    duplicate_keys = null_keys[:DETERMINISM_SLICE_SIZE]

    primary_keys = (
        ORIGINAL_KEYS + COHORT_KEYS[2] + COHORT_KEYS[1] + null_keys
    )
    primary_lanes: tuple[Lane, ...] = tuple(
        (key, "primary") for key in primary_keys
    )
    duplicate_lanes: tuple[Lane, ...] = tuple(
        (key, "determinism_duplicate") for key in duplicate_keys
    )
    lanes = primary_lanes + duplicate_lanes
    primary_index = {
        key: lane for lane, (key, _role) in enumerate(primary_lanes)
    }
    duplicate_index = {
        key: len(primary_lanes) + offset
        for offset, key in enumerate(duplicate_keys)
    }

    initial_states = tuple(
        family["states"][key] for key, _role in lanes
    )
    columns = pack_states(initial_states)
    initial_columns = columns.copy()
    residual_rows = watched_residual_wires()
    residual_wires = tuple(wire for _name, wire in residual_rows)
    primary_mask = (1 << len(primary_lanes)) - 1

    def key_mask(keys: tuple[Key, ...]) -> int:
        return sum(1 << primary_index[key] for key in keys)

    original_mask = key_mask(ORIGINAL_KEYS)
    cohort_masks = {
        event: key_mask(COHORT_KEYS[event]) for event in COHORT_TARGETS
    }
    null_mask = key_mask(null_keys)
    duplicate_mask = sum(1 << duplicate_index[key] for key in duplicate_keys)
    all_lanes_mask = (1 << len(lanes)) - 1
    phase_masks = (
        all_lanes_mask,
        all_lanes_mask ^ original_mask,
        cohort_masks[1] | null_mask | duplicate_mask,
        null_mask | duplicate_mask,
    )
    schedules = tuple(
        packed_schedule(family["program"], lanes, mask)
        for mask in phase_masks
    )

    scalar_one_step = columns.copy()
    advance(scalar_one_step, schedules[0])
    one_step_rows = tuple({
        "key": key,
        "packed_sha256": state_hash(
            unpack_lane(scalar_one_step, primary_index[key])
        ),
        "scalar_sha256": state_hash(K.A.apply_semantic(
            family["states"][key], family["words"][key[1]]
        )),
        "exact": (
            unpack_lane(scalar_one_step, primary_index[key])
            == K.A.apply_semantic(
                family["states"][key], family["words"][key[1]]
            )
        ),
    } for key in primary_keys)
    duplicate_initial_exact = all(
        initial_states[primary_index[key]]
        == initial_states[duplicate_index[key]]
        for key in duplicate_keys
    )
    duplicate_masks_identical = all(
        ((mask >> primary_index[key]) & 1)
        == ((mask >> duplicate_index[key]) & 1)
        for schedule in schedules
        for _kind, _first, _second, _third, mask in schedule
        for key in duplicate_keys
    )

    first_clean: dict[Key, int | None] = {
        key: None for key in primary_keys
    }
    first_recurrence: dict[Key, int | None] = {
        key: None for key in primary_keys
    }
    veto_at_first_clean: dict[Key, bool | None] = {
        key: None for key in primary_keys
    }
    state_at_first_clean: dict[Key, str | None] = {
        key: None for key in primary_keys
    }
    initial_nonclean = nonclean_mask(columns, residual_rows)
    earlier_nonclean_counts = {
        key: int(bool(initial_nonclean & (1 << primary_index[key])))
        for key in primary_keys
    }
    clean_unseen_mask = primary_mask
    recurrence_unseen_mask = primary_mask
    previous_nonclean = initial_nonclean
    windows: dict[Key, list[dict[str, object]]] = {
        key: [] for key in ATTACK_KEYS
    }
    sstar: tuple[int, ...] | None = None
    snapshots: dict[int, dict[Key, tuple[int, ...]]] = {}
    sstar_visits: dict[Key, list[int]] = {
        key: [] for key in COHORT_KEYS[2] + COHORT_KEYS[1]
    }
    determinism_rows: list[dict[str, object]] = []
    phase_rows: list[dict[str, object]] = []

    def determinism_checkpoint(moment: int) -> None:
        rows = tuple({
            "key": key,
            "primary_sha256":
                state_hash(unpack_lane(columns, primary_index[key])),
            "duplicate_sha256":
                state_hash(unpack_lane(columns, duplicate_index[key])),
            "exact_tuple_equal": (
                unpack_lane(columns, primary_index[key])
                == unpack_lane(columns, duplicate_index[key])
            ),
        } for key in duplicate_keys)
        determinism_rows.append({
            "moment": moment,
            "rows": rows,
            "all_exact": all(row["exact_tuple_equal"] for row in rows),
        })

    determinism_checkpoint(0)

    def evolve_segment(
        start: int,
        stop: int,
        schedule: tuple[PackedGate, ...],
        included_mask: int,
    ) -> None:
        nonlocal clean_unseen_mask, recurrence_unseen_mask
        nonlocal previous_nonclean, sstar
        phase_started = monotonic()
        included_primary = included_mask & primary_mask
        for moment in range(start + 1, stop + 1):
            advance(columns, schedule)
            nonclean = nonclean_mask(columns, residual_rows)

            if moment == SSTAR_MOMENT:
                states = {
                    key: unpack_lane(columns, primary_index[key])
                    for key in ORIGINAL_KEYS
                }
                snapshots[moment] = states
                sstar = states[ORIGINAL_KEYS[0]]
            if moment == COHORT_TARGETS[2] - 5:
                snapshots[moment] = {
                    key: unpack_lane(columns, primary_index[key])
                    for key in COHORT_KEYS[2]
                }
            if moment == COHORT_TARGETS[1] - 5:
                snapshots[moment] = {
                    key: unpack_lane(columns, primary_index[key])
                    for key in COHORT_KEYS[1]
                }

            for key in ATTACK_KEYS:
                target = COHORT_TARGETS[key[0]]
                if target - 5 <= moment <= target:
                    lane = primary_index[key]
                    state = unpack_lane(columns, lane)
                    support = support_at_lane(columns, lane, residual_rows)
                    windows[key].append({
                        "moment": moment,
                        "landed_nonclean": bool(support),
                        "landed_support": support,
                        "landed_support_weight": len(support),
                        "state_sha256": state_hash(state),
                    })

            if moment > BASELINE_HORIZON and sstar is not None:
                f1_mask = (
                    (cohort_masks[2] | cohort_masks[1])
                    & clean_unseen_mask
                    & included_primary
                )
                residual_matches = exact_target_mask(
                    columns, sstar, f1_mask, residual_wires
                )
                full_matches = (
                    exact_target_mask(columns, sstar, residual_matches)
                    if residual_matches else 0
                )
                for lane in lane_numbers(full_matches):
                    key = primary_lanes[lane][0]
                    sstar_visits[key].append(moment)

            clean_hits = clean_unseen_mask & included_primary & ~nonclean
            for lane in lane_numbers(clean_hits):
                key = primary_lanes[lane][0]
                first_clean[key] = moment
                veto_at_first_clean[key] = bool(
                    previous_nonclean & (1 << lane)
                )
                state_at_first_clean[key] = state_hash(
                    unpack_lane(columns, lane)
                )
            clean_unseen_mask &= ~clean_hits

            recurrence_candidates = (
                recurrence_unseen_mask & included_primary & ~clean_hits
            )
            recurrence_hits = exact_initial_mask(
                columns, initial_columns, recurrence_candidates
            )
            for lane in lane_numbers(recurrence_hits):
                first_recurrence[primary_lanes[lane][0]] = moment
            recurrence_unseen_mask &= ~recurrence_hits

            for lane in lane_numbers(clean_unseen_mask & included_primary):
                key = primary_lanes[lane][0]
                earlier_nonclean_counts[key] += int(
                    bool(nonclean & (1 << lane))
                )
            previous_nonclean = nonclean
        phase_rows.append({
            "start": start,
            "stop": stop,
            "physical_global_updates": stop - start,
            "included_lanes": included_mask.bit_count(),
            "packed_instructions_per_update": len(schedule),
            "seconds": round(monotonic() - phase_started, 6),
        })
        determinism_checkpoint(stop)

    evolve_segment(0, ORIGINAL_RESOLUTION, schedules[0], phase_masks[0])
    evolve_segment(
        ORIGINAL_RESOLUTION,
        COHORT_TARGETS[2],
        schedules[1],
        phase_masks[1],
    )
    evolve_segment(
        COHORT_TARGETS[2],
        COHORT_TARGETS[1],
        schedules[2],
        phase_masks[2],
    )
    evolve_segment(
        COHORT_TARGETS[1],
        TARGET_HORIZON,
        schedules[3],
        phase_masks[3],
    )

    if sstar is None:
        raise AssertionError("S* moment was not reached")

    def resolution_row(key: Key, target: int) -> dict[str, object]:
        window = tuple(windows.get(key, ()))
        pattern = tuple(row["landed_nonclean"] for row in window)
        result = {
            "key": key,
            "target": target,
            "first_clean_observed": first_clean[key],
            "earlier_moments_checked": target,
            "earlier_nonclean_count": earlier_nonclean_counts[key],
            "every_earlier_moment_nonclean":
                earlier_nonclean_counts[key] == target,
            "landed_veto_at_t_minus_1": veto_at_first_clean[key],
            "event_is_landed_clean": (
                first_clean[key] == target
                and len(window) == 6
                and not window[-1]["landed_nonclean"]
            ),
            "first_recurrence_through_resolution":
                first_recurrence[key],
            "state_at_first_clean_sha256": state_at_first_clean[key],
            "window_t_minus_5_through_t": window,
            "expected_window_cleanliness": (True,) * 5 + (False,),
            "observed_window_cleanliness": pattern,
        }
        result["pass"] = (
            result["first_clean_observed"] == target
            and result["every_earlier_moment_nonclean"]
            and result["landed_veto_at_t_minus_1"] is True
            and result["event_is_landed_clean"]
            and result["first_recurrence_through_resolution"] is None
            and pattern == result["expected_window_cleanliness"]
        )
        return result

    attacked_resolution_rows = tuple(
        resolution_row(key, COHORT_TARGETS[key[0]])
        for key in ATTACK_KEYS
    )
    all_cohort_resolution_rows = tuple({
        "key": key,
        "target": COHORT_TARGETS[key[0]],
        "first_clean_observed": first_clean[key],
        "earlier_nonclean_count": earlier_nonclean_counts[key],
        "landed_veto_at_t_minus_1": veto_at_first_clean[key],
        "first_recurrence_through_resolution": first_recurrence[key],
        "pass": (
            first_clean[key] == COHORT_TARGETS[key[0]]
            and earlier_nonclean_counts[key] == COHORT_TARGETS[key[0]]
            and veto_at_first_clean[key] is True
            and first_recurrence[key] is None
        ),
    } for key in COHORT_KEYS[2] + COHORT_KEYS[1])
    original_resolution_rows = tuple({
        "key": key,
        "first_clean_observed": first_clean[key],
        "earlier_nonclean_count": earlier_nonclean_counts[key],
        "landed_veto_at_t_minus_1": veto_at_first_clean[key],
        "first_recurrence_through_resolution": first_recurrence[key],
        "pass": (
            first_clean[key] == ORIGINAL_RESOLUTION
            and earlier_nonclean_counts[key] == ORIGINAL_RESOLUTION
            and veto_at_first_clean[key] is True
            and first_recurrence[key] is None
        ),
    } for key in ORIGINAL_KEYS)
    resolution_pass = (
        len(attacked_resolution_rows) == 10
        and sum(row["key"][0] == 2 for row in attacked_resolution_rows) == 5
        and sum(row["key"][0] == 1 for row in attacked_resolution_rows) == 5
        and all(row["pass"] for row in attacked_resolution_rows)
        and all(row["pass"] for row in all_cohort_resolution_rows)
        and all(row["pass"] for row in original_resolution_rows)
    )

    original_states = snapshots[SSTAR_MOMENT]
    funnel_states = {
        2: snapshots[COHORT_TARGETS[2] - 5],
        1: snapshots[COHORT_TARGETS[1] - 5],
    }
    original_funnel = original_states[ORIGINAL_KEYS[0]]
    event2_funnel = funnel_states[2][COHORT_KEYS[2][0]]
    event1_funnel = funnel_states[1][COHORT_KEYS[1][0]]
    original_within_equal = all(
        state == original_funnel for state in original_states.values()
    )
    within_equal = {
        event: all(
            state == next(iter(funnel_states[event].values()))
            for state in funnel_states[event].values()
        )
        for event in COHORT_TARGETS
    }
    three_pairwise_diffs = {
        "event2_funnel_vs_event1_funnel":
            hamming_weight(event2_funnel, event1_funnel),
        "event2_funnel_vs_Sstar":
            hamming_weight(event2_funnel, sstar),
        "event1_funnel_vs_Sstar":
            hamming_weight(event1_funnel, sstar),
    }
    tminus5_sstar_rows = tuple({
        "key": key,
        "moment": COHORT_TARGETS[key[0]] - 5,
        "hamming_weight_vs_Sstar": hamming_weight(
            funnel_states[key[0]][key], sstar
        ),
        "differs_from_Sstar":
            funnel_states[key[0]][key] != sstar,
        "Sstar_visit_moments_from_16385_through_resolution":
            tuple(sstar_visits[key]),
        "zero_Sstar_visits": not sstar_visits[key],
    } for key in COHORT_KEYS[2] + COHORT_KEYS[1])
    mergers_pass = (
        original_within_equal
        and all(within_equal.values())
        and all(weight > 0 for weight in three_pairwise_diffs.values())
        and all(
            row["differs_from_Sstar"] and row["zero_Sstar_visits"]
            for row in tminus5_sstar_rows
        )
    )

    expected_pairs = tuple(sorted(BACKBONE))
    observed_original_pairs = tuple(sorted(
        key[1] for key in ORIGINAL_KEYS
        if first_clean[key] == ORIGINAL_RESOLUTION
    ))
    observed_cohort_pairs = {
        event: tuple(sorted(
            key[1] for key in COHORT_KEYS[event]
            if first_clean[key] == COHORT_TARGETS[event]
        ))
        for event in COHORT_TARGETS
    }
    separation_rows = tuple({
        "pair": pair,
        "cyclic_separation": cyclic_separation(pair),
        "max_for_ring_11": cyclic_separation(pair) == 5,
    } for pair in expected_pairs)
    pair_set_pass = (
        observed_original_pairs == expected_pairs
        and all(
            pairs == expected_pairs
            for pairs in observed_cohort_pairs.values()
        )
        and all(row["max_for_ring_11"] for row in separation_rows)
    )

    null_rows = tuple({
        "key": key,
        "first_clean_through_65536": first_clean[key],
        "first_exact_return_to_t0_through_65536": first_recurrence[key],
        "landed_nonclean_moments_count_t0_through_t65536":
            earlier_nonclean_counts[key],
        "final_landed_support":
            support_at_lane(columns, primary_index[key], residual_rows),
        "final_state_sha256":
            state_hash(unpack_lane(columns, primary_index[key])),
        "zero_event": (
            first_clean[key] is None and first_recurrence[key] is None
        ),
    } for key in null_keys)
    null_pass = (
        len(catalog) == 176
        and len(EXPECTED_EARLIER_RESOLVED) == 25
        and len(claimed_resolved) == 43
        and len(claimed_open) == 133
        and len(null_keys) == 10
        and len(set(null_keys)) == 10
        and set(null_keys) <= set(claimed_open)
        and all(row["zero_event"] for row in null_rows)
        and all(
            row["landed_nonclean_moments_count_t0_through_t65536"]
            == TARGET_HORIZON + 1
            for row in null_rows
        )
    )

    arithmetic = arithmetic_census()
    deterministic = (
        duplicate_initial_exact
        and duplicate_masks_identical
        and all(row["all_exact"] for row in determinism_rows)
    )
    elapsed = monotonic() - started
    controls_pass = (
        sources["pass"]
        and family["summary"] == {
            "events": 4,
            "pairs": 44,
            "keys": 176,
            "state_bits": 5815,
            "allocator_gates": 3106,
            "word_gate_counts": (6212,),
        }
        and all(row["exact"] for row in one_step_rows)
        and deterministic
        and not any(
            name in sys.modules for name in BLOCKLISTED_MODULES
        )
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    checks = {
        "RESOLUTION_VERIFICATION": resolution_pass,
        "THE_COHORT_MERGERS": mergers_pass,
        "THE_PAIR_SET_IDENTITY": pair_set_pass,
        "NULL_SPOT_COVERAGE": null_pass,
        "THE_MOMENT_ARITHMETIC": bool(arithmetic["pass"]),
        "CONTROLS": controls_pass,
    }
    certificates: dict[str, object] = {
        "RESOLUTION_VERIFICATION": {
            "method":
                "independent packed X/CNOT/TOF evolution with an exact "
                "landed named-residual test at every moment",
            "detailed_attack_rows_five_per_cohort":
                attacked_resolution_rows,
            "all_eighteen_cohort_census": all_cohort_resolution_rows,
            "original_nine_control": original_resolution_rows,
            "phase_accounting": tuple(phase_rows),
            "pass": resolution_pass,
        },
        "THE_COHORT_MERGERS": {
            "Sstar": {
                "moment": SSTAR_MOMENT,
                "state_sha256": state_hash(sstar),
                "original_nine_exactly_equal": original_within_equal,
                "state_bits": len(sstar),
            },
            "cohorts": tuple({
                "event": event,
                "resolution_moment": COHORT_TARGETS[event],
                "funnel_moment": COHORT_TARGETS[event] - 5,
                "keys": COHORT_KEYS[event],
                "all_nine_exact_tuple_equal_at_funnel":
                    within_equal[event],
                "funnel_state_sha256": state_hash(
                    next(iter(funnel_states[event].values()))
                ),
            } for event in (2, 1)),
            "three_pairwise_diff_weights": three_pairwise_diffs,
            "F1_exact_rows": tminus5_sstar_rows,
            "F1_scan_interval":
                "every moment 16385 through each trajectory's first clean",
            "no_new_cycle_on_all_eighteen":
                all(first_recurrence[key] is None
                    for key in COHORT_KEYS[2] + COHORT_KEYS[1]),
            "pass": mergers_pass,
        },
        "THE_PAIR_SET_IDENTITY": {
            "expected_original_nine_pairs": expected_pairs,
            "observed_original_pairs_resolving_at_14744":
                observed_original_pairs,
            "observed_event2_pairs_resolving_at_33195":
                observed_cohort_pairs[2],
            "observed_event1_pairs_resolving_at_51115":
                observed_cohort_pairs[1],
            "max_cyclic_separation_rows": separation_rows,
            "pass": pair_set_pass,
        },
        "NULL_SPOT_COVERAGE": {
            "selection_rule":
                "lowest ten SHA256(canonical key) ranks from the claimed "
                "133-key post-cohort open population; no outcome selection",
            "family_accounting": {
                "family": len(catalog),
                "resolved_through_819": len(EXPECTED_EARLIER_RESOLVED),
                "new_cohort_transients": 18,
                "claimed_open": len(claimed_open),
            },
            "sample_size": len(null_keys),
            "rows": null_rows,
            "pass": null_pass,
        },
        "THE_MOMENT_ARITHMETIC": arithmetic,
        "CONTROLS": {
            **sources,
            "independent_evolution": {
                "direct_dynamic_imports": (
                    "frontier_cycle719_two_rail_recurrent_controller_core_"
                    "2026_07_26",
                ),
                "primary_outputs_consumed": False,
                "one_step_scalar_equivalence_rows": one_step_rows,
                "phase_schedule_instruction_counts":
                    tuple(len(schedule) for schedule in schedules),
            },
            "determinism_declared_slice": {
                "declaration":
                    "first four keys in the declared SHA-ranked null sample "
                    "are carried as distinct duplicate lanes t=0..65536",
                "keys": duplicate_keys,
                "initial_exact": duplicate_initial_exact,
                "all_schedule_masks_identical": duplicate_masks_identical,
                "checkpoints": tuple(determinism_rows),
                "deterministic": deterministic,
            },
            "blocked_modules_loaded_at_end": tuple(
                name for name in BLOCKLISTED_MODULES
                if name in sys.modules
            ),
            "firewall_hits_at_end": tuple(FIREWALL.hits),
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "pass": controls_pass,
        },
    }
    report = {
        "cycle": 831,
        "checker": "cohorts_independent_check",
        "horizon_reached": TARGET_HORIZON,
        "cohort_transients_verified": 18,
        "null_keys_swept": len(null_keys),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "primary_refuted": False,
        "terminal": "CYCLE831_COHORTS_INDEPENDENT_CHECK_REFUTES_PRIMARY",
    }
    output = stable_render(checks, certificates, report)
    stdout_ok = len(output.encode()) < STDOUT_LIMIT_BYTES
    checks["CONTROLS"] = controls_pass and stdout_ok
    certificates["CONTROLS"]["pass"] = checks["CONTROLS"]
    output = stable_render(checks, certificates, report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "primary_refuted": True,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal":
                "CYCLE831_COHORTS_INDEPENDENT_CHECK_REFUTES_PRIMARY",
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
            "primary_refuted": True,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal":
                "CYCLE831_COHORTS_INDEPENDENT_CHECK_REFUTES_PRIMARY",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
