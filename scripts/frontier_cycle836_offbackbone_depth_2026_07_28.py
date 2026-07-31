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


def main() -> int:
    sys.stdout.write(compact({
        "cycle": 836,
        "pass": False,
        "terminal": "CYCLE836_SCAFFOLD_INCOMPLETE",
    }) + "\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
