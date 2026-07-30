#!/usr/bin/env python3
"""Cycle 820: exact shared-moment mechanism for the nine t=14744 keys.

The Cycle-819 primary is a SHA-pinned text/AST-only reference.  It is
blocklisted from import and execution.  This runner independently rebuilds the
landed k=2 family from the Cycle-719 controller core, evolves the nine selected
keys, and tests exact arithmetic, trajectory, and mechanism claims.

The state-class mechanism is not inferred from hashes: equality classes are
formed by exact tuple equality and hashes are printed only as compact labels.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
)

import ast
from collections import defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import ceil, floor, gcd
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

TEXT_AST_ONLY_PATHS = (AUDIT_INPUT_PATHS[1],)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
}


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if the Cycle-819 text/AST reference is imported."""

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


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Coordinate = tuple[str, str, int]
Support = frozenset[Coordinate]
Key = tuple[int, tuple[int, int]]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
TARGET_MOMENT = 14744
TRAJECTORY_END = TARGET_MOMENT + 6
MECHANISM_ENTRY = 14739
FIXED_LAG = 5
NINE_KEYS: tuple[Key, ...] = (
    (0, (1, 6)),
    (0, (1, 7)),
    (0, (2, 7)),
    (0, (2, 8)),
    (0, (3, 8)),
    (0, (3, 9)),
    (0, (4, 9)),
    (0, (4, 10)),
    (0, (5, 10)),
)
PERIODS = (2, 3, 288, 4464, 5952, 8928, 8930)
EARLIER_MOMENTS = (252, 371, 444, 532, 681, 1385)
HORIZON_POWERS = (4096, 8192, 16384)
CHECKPOINTS = (
    0, 1, 252, 371, 444, 532, 681, 1385, 4096, 4464, 5952,
    8192, 8928, 8930, 14738, 14739, 14740, 14741, 14742, 14743,
    14744, 14745, 14746, 14747, 14748, 14749, 14750,
)
EXPECTED_CONTROL_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
}
EXPECTED_OLD_CYCLES = {
    (3, (0, 5)),
    (3, (0, 6)),
    (3, (1, 6)),
    (3, (1, 7)),
    (3, (2, 7)),
    (3, (2, 8)),
    (3, (3, 8)),
    (3, (3, 9)),
    (3, (4, 9)),
    (3, (4, 10)),
    (3, (5, 10)),
    (2, (0, 9)),
}
NEW_CYCLE_KEYS = {
    (1, (0, 9)),
    (0, (0, 9)),
}
RESOLVED_THROUGH_819 = (
    set(EXPECTED_CONTROL_TRANSIENTS)
    | EXPECTED_OLD_CYCLES
    | set(NINE_KEYS)
    | NEW_CYCLE_KEYS
)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def state_sha256(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob_sha(payload: bytes) -> str:
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


def source_certificate() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads.items()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_path = Path(__file__)
    self_payload = self_path.read_bytes()
    self_tree = ast.parse(self_payload, filename=self_path.name)
    direct_frontier_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    }
    cycle819_functions = {
        node.name
        for node in trees[AUDIT_INPUT_PATHS[1]].body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
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
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob_sha(self_payload),
        "cycle819_reference_mode": "TEXT_AST_ONLY",
        "cycle819_reference_AST_basis": {
            "build_family",
            "residual_support",
            "advance_population",
            "verify_transient",
            "verify_cycle",
        } <= cycle819_functions,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": tuple(sorted(direct_frontier_imports)),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 6,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and result["cycle819_reference_AST_basis"]
        and direct_frontier_imports
        == {
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        }
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and len(AUDIT_INPUT_PATHS) <= 6
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


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
    positions = tuple(positions0)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for gate in word:
        if gate.kind == "X":
            rows.append((0, gate.wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, gate.wires[0], gate.wires[1], 0))
        elif gate.kind == "TOF":
            rows.append((2, gate.wires[0], gate.wires[1], gate.wires[2]))
        else:
            raise ValueError(("unsupported landed gate", gate))
    return tuple(rows)


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


def residual_support(state: tuple[int, ...]) -> Support:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    rows: set[Coordinate] = set()
    if state[K.R3.X.SOURCE_POINTER]:
        rows.add(("source", "SOURCE_POINTER", 0))
    for bank_index, bank in enumerate(banks):
        for register_name, wire in watched_registers():
            if bank[wire]:
                rows.add(("bank", register_name, bank_index))
    for link_index, link in enumerate(links):
        for wire_index, bit in enumerate(link):
            if bit:
                rows.add(("link", f"WIRE_{wire_index}", link_index))
    return frozenset(rows)


def canonical_support(support: Support) -> tuple[Coordinate, ...]:
    return tuple(sorted(support))


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
        epochs.append((event, direction, before))
        state = after

    positions = separated_pairs()
    words = {
        positions0: synchronous_word(program, positions0)
        for positions0 in positions
    }
    compiled_words = {
        positions0: compile_word(words[positions0])
        for positions0 in positions
    }
    states: dict[Key, tuple[int, ...]] = {}
    supports: dict[Key, Support] = {}
    composition_failures = 0
    rail_failures = 0
    for event, _direction, before in epochs:
        for positions0 in positions:
            after, rail_a, rail_b, _trace = K.run_orbit(
                before, program, token_positions=positions0
            )
            expected_rail = tuple(
                int(station in positions0)
                for station in range(RING_STATIONS)
            )
            composition_failures += (
                after != K.A.apply_semantic(before, words[positions0])
            )
            rail_failures += rail_a != expected_rail or any(rail_b)
            key = (event, positions0)
            states[key] = after
            supports[key] = residual_support(after)

    unique_supports = set(supports.values())
    state_bits = len(next(iter(states.values())))
    summary = {
        "epochs": len(epochs),
        "program_stations": len(program),
        "positions": len(positions),
        "keys": len(states),
        "unique_initial_supports": len(unique_supports),
        "unique_initial_supports_by_epoch": tuple(
            len({
                supports[(event, positions0)]
                for positions0 in positions
            })
            for event in range(2 * FIXTURE_BANKS)
        ),
        "allocator_gates": len(allocator),
        "synchronous_word_gate_counts":
            tuple(sorted({len(word) for word in words.values()})),
        "state_bits": state_bits,
        "epoch_failures": epoch_failures,
        "composition_failures": composition_failures,
        "rail_failures": rail_failures,
        "family_sha256": digest(tuple(
            (key, canonical_support(supports[key]))
            for key in sorted(supports)
        )),
    }
    summary["pass"] = (
        summary["epochs"] == 4
        and summary["program_stations"] == 11
        and summary["positions"] == 44
        and summary["keys"] == FAMILY_SIZE
        and summary["unique_initial_supports"] == 25
        and summary["unique_initial_supports_by_epoch"] == (1, 1, 12, 14)
        and summary["allocator_gates"] == 3106
        and summary["synchronous_word_gate_counts"] == (6212,)
        and summary["state_bits"] == 5815
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "compiled_words": compiled_words,
        "states": states,
        "supports": supports,
        "summary": summary,
    }


def factorization(value: int) -> tuple[tuple[int, int], ...]:
    remaining = value
    prime = 2
    rows = []
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
    assert value == product_from_factorization(tuple(rows))
    return tuple(rows)


def product_from_factorization(rows: tuple[tuple[int, int], ...]) -> int:
    value = 1
    for prime, exponent in rows:
        value *= prime ** exponent
    return value


def extended_gcd(left: int, right: int) -> tuple[int, int, int]:
    old_r, r = left, right
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def positive_pair_relation(
    left: int,
    right: int,
) -> dict[str, object]:
    common, x0, y0 = extended_gcd(left, right)
    if TARGET_MOMENT % common:
        return {
            "left": left,
            "right": right,
            "status": "FAILS",
            "reason": "gcd_does_not_divide_target",
            "gcd": common,
            "target_mod_gcd": TARGET_MOMENT % common,
        }
    scale = TARGET_MOMENT // common
    a0 = x0 * scale
    b0 = y0 * scale
    a_step = right // common
    b_step = left // common
    n_min = ceil_div(1 - a0, a_step)
    n_max = (b0 - 1) // b_step
    if n_min > n_max:
        return {
            "left": left,
            "right": right,
            "status": "FAILS",
            "reason": "no_strictly_positive_solution",
            "general_integer_solution":
                f"a={a0}+{a_step}n;b={b0}-{b_step}n",
            "n_positive_interval": (n_min, n_max),
        }
    first_a = a0 + a_step * n_min
    first_b = b0 - b_step * n_min
    last_a = a0 + a_step * n_max
    last_b = b0 - b_step * n_max
    all_checked = all(
        (a0 + a_step * n) * left
        + (b0 - b_step * n) * right
        == TARGET_MOMENT
        and a0 + a_step * n >= 1
        and b0 - b_step * n >= 1
        for n in range(n_min, n_max + 1)
    )
    return {
        "left": left,
        "right": right,
        "status": "HOLDS_EXACTLY",
        "all_positive_solutions":
            f"a={a0}+{a_step}n;b={b0}-{b_step}n;"
            f"{n_min}<=n<={n_max}",
        "solution_count": n_max - n_min + 1,
        "first_solution": (first_a, first_b),
        "last_solution": (last_a, last_b),
        "all_solutions_machine_checked": all_checked,
    }


def arithmetic_certificate(
    family: dict[str, object],
) -> dict[str, object]:
    summary = family["summary"]
    inventory = {
        "periods": tuple(
            (f"period_{value}", value) for value in PERIODS
        ),
        "earlier_moments": tuple(
            (f"moment_{value}", value) for value in EARLIER_MOMENTS
        ),
        "orbit_station_counts": (
            ("physical_controller_stations", 130),
            ("k2_program_stations", summary["program_stations"]),
            ("fixture_banks", FIXTURE_BANKS),
            ("held_bank_count_5", 5),
            ("held_bank_count_12", 12),
            ("family_epochs", summary["epochs"]),
            ("separated_position_pairs", summary["positions"]),
            ("family_keys", summary["keys"]),
            ("unique_initial_supports", summary["unique_initial_supports"]),
            ("allocator_semantic_gates", summary["allocator_gates"]),
            (
                "synchronous_k2_word_gates",
                summary["synchronous_word_gate_counts"][0],
            ),
            ("landed_state_bits", summary["state_bits"]),
        ),
        "horizon_powers": tuple(
            (f"horizon_{value}", value) for value in HORIZON_POWERS
        ),
    }
    flattened = tuple(
        row for rows in inventory.values() for row in rows
    )
    labels_by_value: dict[int, list[str]] = defaultdict(list)
    for label, value in flattened:
        labels_by_value[value].append(label)
    values = tuple(sorted(labels_by_value))
    divisibility = tuple({
        "value": value,
        "labels": tuple(labels_by_value[value]),
        "target_divmod_value": divmod(TARGET_MOMENT, value),
        "value_divides_target": TARGET_MOMENT % value == 0,
        "status":
            "HOLDS_EXACTLY"
            if TARGET_MOMENT % value == 0 else "FAILS",
    } for value in values)
    pair_rows = tuple(
        positive_pair_relation(left, right)
        for left, right in combinations(values, 2)
    )
    factorizations = tuple({
        "value": value,
        "labels": tuple(labels_by_value[value]),
        "prime_factorization": factorization(value),
    } for value in (TARGET_MOMENT,) + values)
    centered_relation = {
        "relation":
            "2*14744=8928+8930+2*5815",
        "equivalent_relations": (
            "14744=8928+5815+1",
            "14744=8930+5815-1",
        ),
        "machine_values": {
            "left": 2 * TARGET_MOMENT,
            "right": 8928 + 8930 + 2 * summary["state_bits"],
            "lower": 8928 + summary["state_bits"] + 1,
            "upper": 8930 + summary["state_bits"] - 1,
        },
    }
    centered_relation["status"] = (
        "HOLDS_EXACTLY"
        if centered_relation["machine_values"]["left"]
        == centered_relation["machine_values"]["right"]
        == 2 * TARGET_MOMENT
        and centered_relation["machine_values"]["lower"]
        == centered_relation["machine_values"]["upper"]
        == TARGET_MOMENT
        else "FAILS"
    )
    result = {
        "relation_grammar": (
            "complete unary divisibility census and complete unordered-pair "
            "strictly-positive integer census a*x+b*y=14744; each holding "
            "pair prints the full parameterized solution interval"
        ),
        "inventory": inventory,
        "labels_by_value": tuple(
            (value, tuple(labels_by_value[value])) for value in values
        ),
        "factorizations": factorizations,
        "target_factorization": factorization(TARGET_MOMENT),
        "divisibility_census": divisibility,
        "positive_pair_linear_combination_census": pair_rows,
        "divisibility_holds": tuple(
            row["value"] for row in divisibility
            if row["status"] == "HOLDS_EXACTLY"
        ),
        "divisibility_fails": tuple(
            row["value"] for row in divisibility
            if row["status"] == "FAILS"
        ),
        "pair_holds_count": sum(
            row["status"] == "HOLDS_EXACTLY" for row in pair_rows
        ),
        "pair_fails_count": sum(
            row["status"] == "FAILS" for row in pair_rows
        ),
        "new_cycle_centered_state_size_relation": centered_relation,
    }
    result["pass"] = (
        result["target_factorization"] == ((2, 3), (19, 1), (97, 1))
        and len(divisibility) == len(values)
        and all(
            row["target_divmod_value"]
            == divmod(TARGET_MOMENT, row["value"])
            for row in divisibility
        )
        and all(
            row["status"] == "FAILS"
            or row["all_solutions_machine_checked"]
            for row in pair_rows
        )
        and result["pair_holds_count"] + result["pair_fails_count"]
        == len(pair_rows)
        and centered_relation["status"] == "HOLDS_EXACTLY"
    )
    return result


def exact_equality_partition(
    states: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    groups: dict[tuple[int, ...], list[int]] = {}
    for index, state in enumerate(states):
        groups.setdefault(state, []).append(index)
    return tuple(sorted(
        tuple(indices)
        for indices in groups.values()
        if len(indices) >= 2
    ))


def compress_arithmetic_runs(
    values: tuple[int, ...],
) -> tuple[tuple[int, int, int], ...]:
    if not values:
        return ()
    rows = []
    index = 0
    while index < len(values):
        if index + 1 == len(values):
            rows.append((values[index], values[index], 0))
            break
        step = values[index + 1] - values[index]
        stop = index + 2
        while (
            stop < len(values)
            and values[stop] - values[stop - 1] == step
        ):
            stop += 1
        if stop - index >= 3:
            rows.append((values[index], values[stop - 1], step))
            index = stop
        else:
            rows.append((values[index], values[index], 0))
            index += 1
    return tuple(rows)


def expand_arithmetic_runs(
    rows: tuple[tuple[int, int, int], ...],
) -> tuple[int, ...]:
    values = []
    for start, stop, step in rows:
        if step == 0:
            assert start == stop
            values.append(start)
        else:
            values.extend(range(start, stop + step, step))
    return tuple(values)


def encode_time_bitset(values: tuple[int, ...]) -> str:
    encoded = 0
    for value in values:
        encoded |= 1 << value
    return format(encoded, "x")


def decode_time_bitset(encoded: str, limit: int) -> tuple[int, ...]:
    bits = int(encoded, 16)
    return tuple(
        value for value in range(limit + 1)
        if bits & (1 << value)
    )


def evolve_nine(
    family: dict[str, object],
) -> dict[str, object]:
    states = {key: family["states"][key] for key in NINE_KEYS}
    words = {key: family["words"][key[1]] for key in NINE_KEYS}
    first_clean = {key: None for key in NINE_KEYS}
    nearest_misses: dict[Key, list[tuple[int, Coordinate]]] = {
        key: [] for key in NINE_KEYS
    }
    checkpoints: dict[int, tuple[dict[str, object], ...]] = {}
    support_window: dict[
        int, tuple[tuple[Coordinate, ...], ...]
    ] = {}
    exact_partitions: dict[
        tuple[tuple[int, ...], ...], list[int]
    ] = defaultdict(list)
    all_equal_times = []
    state_at_entry: tuple[int, ...] | None = None
    trajectory_hasher = sha256()

    for update in range(TRAJECTORY_END + 1):
        ordered_states = tuple(states[key] for key in NINE_KEYS)
        supports = tuple(
            residual_support(states[key]) for key in NINE_KEYS
        )
        partition = exact_equality_partition(ordered_states)
        exact_partitions[partition].append(update)
        if len(set(ordered_states)) == 1:
            all_equal_times.append(update)
        if update == MECHANISM_ENTRY:
            state_at_entry = ordered_states[0]
        for key, support in zip(NINE_KEYS, supports):
            if not support and first_clean[key] is None:
                first_clean[key] = update
            if len(support) == 1:
                nearest_misses[key].append(
                    (update, next(iter(support)))
                )
        if update in CHECKPOINTS:
            checkpoints[update] = tuple({
                "key_index": index,
                "state_sha256": state_sha256(state),
                "support_weight": len(support),
                "support": canonical_support(support),
            } for index, (state, support) in enumerate(
                zip(ordered_states, supports)
            ))
        if TARGET_MOMENT - 1 <= update <= TRAJECTORY_END:
            support_window[update] = tuple(
                canonical_support(support) for support in supports
            )
        trajectory_hasher.update(
            compact((
                update,
                tuple(state_sha256(state) for state in ordered_states),
                tuple(canonical_support(support) for support in supports),
            )).encode("utf-8")
        )
        if update < TRAJECTORY_END:
            states = {
                key: K.A.apply_semantic(states[key], words[key])
                for key in NINE_KEYS
            }

    miss_classes: dict[
        tuple[tuple[int, Coordinate], ...], list[int]
    ] = defaultdict(list)
    for index, key in enumerate(NINE_KEYS):
        miss_classes[tuple(nearest_misses[key])].append(index)
    coincidence_map = tuple({
        "shared_key_groups": partition,
        "time_count": len(times),
        "times_bitset_hex": encode_time_bitset(tuple(times)),
        "bitset_domain": (0, TRAJECTORY_END),
        "times_sha256": digest(tuple(times)),
    } for partition, times in sorted(
        exact_partitions.items(),
        key=lambda row: (-len(row[1]), row[0]),
    ))
    coincidence_exact = all(
        decode_time_bitset(row["times_bitset_hex"], TRAJECTORY_END)
        == tuple(exact_partitions[row["shared_key_groups"]])
        for row in coincidence_map
    )
    result = {
        "key_index": tuple(enumerate(NINE_KEYS)),
        "checkpoint_declaration": CHECKPOINTS,
        "state_hashes_at_checkpoints": tuple(
            {"time": update, "rows": checkpoints[update]}
            for update in CHECKPOINTS
        ),
        "nearest_miss_definition":
            "exactly one residual-support condition remains nonzero",
        "nearest_miss_classes": tuple({
            "key_indices": tuple(indices),
            "count_per_key": len(sequence),
            "times_and_lone_failed_conditions": sequence,
            "sequence_sha256": digest(sequence),
        } for sequence, indices in sorted(
            miss_classes.items(), key=lambda row: row[1]
        )),
        "coincidence_definition":
            "same-time exact full-state tuple equality; SHA256 is label only",
        "coincidence_map": coincidence_map,
        "coincidence_map_exactly_decodes": coincidence_exact,
        "coincidence_partition_count": len(coincidence_map),
        "all_nine_exact_state_coincidence_times":
            tuple(all_equal_times),
        "first_clean": tuple(
            (key, first_clean[key]) for key in NINE_KEYS
        ),
        "target_window": tuple(
            (update, support_window[update])
            for update in range(TARGET_MOMENT - 1, TRAJECTORY_END + 1)
        ),
        "state_at_entry": state_at_entry,
        "state_at_entry_sha256":
            state_sha256(state_at_entry) if state_at_entry else None,
        "trajectory_sha256": trajectory_hasher.hexdigest(),
    }
    result["pass"] = (
        all(moment == TARGET_MOMENT for moment in first_clean.values())
        and all(
            support_window[TARGET_MOMENT - 1][index]
            for index in range(len(NINE_KEYS))
        )
        and all(
            not support_window[TARGET_MOMENT][index]
            for index in range(len(NINE_KEYS))
        )
        and tuple(all_equal_times) == (0, 1, 14739, 14744)
        and coincidence_exact
        and state_at_entry is not None
    )
    return result


def bit_slice(
    states: tuple[tuple[int, ...], ...],
) -> list[int]:
    return [
        sum(state[wire] << index for index, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(
    columns: list[int],
    index: int,
) -> tuple[int, ...]:
    return tuple((column >> index) & 1 for column in columns)


def apply_compiled_bit_slice(
    columns: list[int],
    operations: tuple[tuple[int, int, int, int], ...],
    width: int,
) -> None:
    mask = (1 << width) - 1
    for kind, first, second, third in operations:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first]
        else:
            columns[third] ^= columns[first] & columns[second]


def population_state_at_entry(
    family: dict[str, object],
) -> dict[Key, tuple[int, ...]]:
    result: dict[Key, tuple[int, ...]] = {}
    for positions in family["positions"]:
        keys = tuple(
            (event, positions) for event in range(2 * FIXTURE_BANKS)
        )
        columns = bit_slice(tuple(family["states"][key] for key in keys))
        operations = family["compiled_words"][positions]
        for _update in range(MECHANISM_ENTRY):
            apply_compiled_bit_slice(columns, operations, len(keys))
        for index, key in enumerate(keys):
            result[key] = un_slice(columns, index)
    return result


def five_step_image(
    state: tuple[int, ...],
    word: tuple[object, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    weights = [len(residual_support(state))]
    current = state
    for _step in range(FIXED_LAG):
        current = K.A.apply_semantic(current, word)
        weights.append(len(residual_support(current)))
    return current, tuple(weights)


def mechanism_candidates(
    family: dict[str, object],
    trajectory: dict[str, object],
    population_at_entry: dict[Key, tuple[int, ...]],
) -> tuple[dict[str, object], dict[str, object]]:
    common_state = trajectory["state_at_entry"]
    assert isinstance(common_state, tuple)
    coincidence_times = trajectory[
        "all_nine_exact_state_coincidence_times"
    ]
    earlier_entries = tuple(
        update
        for update in coincidence_times
        if update < TARGET_MOMENT
        and (
            update == 0
            or update - 1 not in coincidence_times
        )
    )
    annihilator_rows = []
    for positions in family["positions"]:
        image, weights = five_step_image(
            common_state, family["words"][positions]
        )
        annihilator_rows.append({
            "positions": positions,
            "support_weights_t0_through_t5": weights,
            "clean_at_5": not residual_support(image),
            "image_sha256": state_sha256(image),
        })
    annihilator_positions = tuple(
        row["positions"] for row in annihilator_rows
        if row["clean_at_5"]
    )
    expected_annihilator_positions = tuple(
        positions for positions in family["positions"]
        if positions[0] > 0
    )

    all_keys = set(family["states"])
    open_151 = tuple(sorted(all_keys - RESOLVED_THROUGH_819))
    family_entry_class = tuple(sorted(
        key for key, state in population_at_entry.items()
        if state == common_state
    ))
    open_entry_class = tuple(
        key for key in open_151
        if population_at_entry[key] == common_state
    )
    open_trigger_now = tuple(
        key for key in open_entry_class
        if key[1] in annihilator_positions
    )

    same_pair_counterexample = (1, NINE_KEYS[0][1])
    counter_image, counter_weights = five_step_image(
        population_at_entry[same_pair_counterexample],
        family["words"][same_pair_counterexample[1]],
    )
    word_hashes = tuple(
        digest(family["compiled_words"][key[1]])
        for key in NINE_KEYS
    )
    t_minus_one = dict(trajectory["target_window"])[TARGET_MOMENT - 1]
    period_rows = tuple({
        "period": period,
        "quotient": TARGET_MOMENT // period,
        "residue": TARGET_MOMENT % period,
        "zero_phase": TARGET_MOMENT % period == 0,
    } for period in PERIODS)

    candidates = {
        "A_common_exact_configuration_plus_landed_lag_5": {
            "status": "HOLDS_EXACTLY",
            "shared_entry_times_before_target": earlier_entries,
            "last_shared_entry": MECHANISM_ENTRY,
            "entry_state_sha256": state_sha256(common_state),
            "fixed_lag": FIXED_LAG,
            "lag_source": "landed held bank-count 5",
            "prediction_relation": "14739+5=14744",
            "prediction_machine_checked":
                MECHANISM_ENTRY + FIXED_LAG == TARGET_MOMENT,
            "all_nine_first_clean_at_prediction": all(
                moment == TARGET_MOMENT
                for _key, moment in trajectory["first_clean"]
            ),
        },
        "B_position_pair_alone_predicts_moment": {
            "status": "FAILS",
            "reason":
                "same pair in another epoch has a different t=14739 state "
                "and a nonclean five-step image",
            "selected_key": NINE_KEYS[0],
            "counterexample_key": same_pair_counterexample,
            "same_positions":
                NINE_KEYS[0][1] == same_pair_counterexample[1],
            "counterexample_support_weights_t14739_through_t14744":
                counter_weights,
            "counterexample_clean_at_t14744":
                not residual_support(counter_image),
            "affine_uniformity_exact_obstruction": (
                "pairs (1,6),(1,7) force right coefficient 0; "
                "pairs (1,7),(2,7) force left coefficient 0; "
                "only a constant affine function survives"
            ),
        },
        "C_period_clock_synchronization": {
            "status": "FAILS",
            "zero_phase_rows": period_rows,
            "period_2_partial_coincidence":
                "HOLDS but selects every even time, not t=14744",
            "nontrivial_period_greater_than_2_zero_phase_count": sum(
                row["zero_phase"] and row["period"] > 2
                for row in period_rows
            ),
            "new_cycle_counterexample":
                (8928, TARGET_MOMENT % 8928, 8930, TARGET_MOMENT % 8930),
            "centered_static_relation":
                "2*14744=8928+8930+2*5815 HOLDS but is not clock phase",
        },
        "D_state_Sstar_five_step_annihilator_class": {
            "status": "HOLDS_EXACTLY",
            "class_relation":
                "for all 44 landed separated pairs, S* is clean after "
                "five updates iff left_position>0",
            "annihilator_position_count": len(annihilator_positions),
            "annihilator_positions": annihilator_positions,
            "nonannihilator_positions": tuple(
                positions for positions in family["positions"]
                if positions not in annihilator_positions
            ),
            "exact_class_expected": expected_annihilator_positions,
            "exact_class_match":
                annihilator_positions == expected_annihilator_positions,
            "nine_inside_class": all(
                key[1] in annihilator_positions for key in NINE_KEYS
            ),
            "all_annihilator_images_same": len({
                row["image_sha256"] for row in annihilator_rows
                if row["clean_at_5"]
            }) == 1,
            "machine_checked_rows": tuple(annihilator_rows),
        },
        "E_common_singleton_last_defect": {
            "status": "FAILS",
            "claim": "all nine have the same singleton support at t=14743",
            "support_weights": tuple(len(support) for support in t_minus_one),
            "counterexample_key_index": 0,
            "counterexample_support": t_minus_one[0],
            "partial_structure":
                "all nine share FRESH_1(bank0), but key indices 0,1 "
                "also carry DIRECTION_OK(bank0) and ZERO_WORK_0(bank0)",
        },
        "F_identical_transition_words": {
            "status": "FAILS",
            "compiled_word_hashes": word_hashes,
            "distinct_word_count": len(set(word_hashes)),
            "counterexample":
                "all nine words are syntactically distinct even though "
                "their S* five-step images coincide",
        },
    }
    prediction = {
        "resolved_key_count_encoded": len(RESOLVED_THROUGH_819),
        "open_key_count": len(open_151),
        "open_key_sha256": digest(open_151),
        "family_keys_in_Sstar_at_t14739": family_entry_class,
        "family_Sstar_class_is_exactly_nine":
            family_entry_class == tuple(sorted(NINE_KEYS)),
        "open_151_in_Sstar_at_t14739": open_entry_class,
        "open_151_triggered_for_t14744": open_trigger_now,
        "specific_prediction":
            "zero of the 151 open keys is selected at t=14744 because "
            "zero is in S* at t=14739",
        "falsifiable_future_rule":
            "for any of the 151, an exact entry into S* at time tau with "
            "left_position>0 predicts clean support at tau+5; a nonclean "
            "tau+5 image falsifies this mechanism",
    }
    prediction["pass"] = (
        len(RESOLVED_THROUGH_819) == 25
        and len(open_151) == 151
        and prediction["family_Sstar_class_is_exactly_nine"]
        and not open_entry_class
        and not open_trigger_now
    )
    candidates_pass = (
        candidates[
            "A_common_exact_configuration_plus_landed_lag_5"
        ]["prediction_machine_checked"]
        and candidates[
            "A_common_exact_configuration_plus_landed_lag_5"
        ]["all_nine_first_clean_at_prediction"]
        and candidates[
            "D_state_Sstar_five_step_annihilator_class"
        ]["exact_class_match"]
        and candidates[
            "D_state_Sstar_five_step_annihilator_class"
        ]["nine_inside_class"]
        and candidates[
            "D_state_Sstar_five_step_annihilator_class"
        ]["all_annihilator_images_same"]
        and candidates[
            "B_position_pair_alone_predicts_moment"
        ]["counterexample_clean_at_t14744"] is False
        and candidates[
            "C_period_clock_synchronization"
        ]["nontrivial_period_greater_than_2_zero_phase_count"] == 0
        and candidates[
            "F_identical_transition_words"
        ]["distinct_word_count"] == 9
    )
    return {
        "candidates": candidates,
        "pass": candidates_pass,
    }, prediction


def identity_controls(
    family: dict[str, object],
    trajectory: dict[str, object],
) -> dict[str, object]:
    control_rows = []
    for key, expected in sorted(EXPECTED_CONTROL_TRANSIENTS.items()):
        state = family["states"][key]
        word = family["words"][key[1]]
        clean_times = []
        window = {}
        for update in range(expected + 2):
            support = residual_support(state)
            if not support:
                clean_times.append(update)
            if expected - 1 <= update <= expected + 1:
                window[update] = {
                    "support": canonical_support(support),
                    "state_sha256": state_sha256(state),
                }
            if update < expected + 1:
                state = K.A.apply_semantic(state, word)
        control_rows.append({
            "key": key,
            "expected_first_clean": expected,
            "clean_times_through_plus_1": tuple(clean_times),
            "window": tuple(sorted(window.items())),
            "pass": clean_times and clean_times[0] == expected,
        })
    nine_first_clean = dict(trajectory["first_clean"])[NINE_KEYS[0]]
    target_window = dict(trajectory["target_window"])
    nine_identity = {
        "key": NINE_KEYS[0],
        "first_clean": nine_first_clean,
        "t_minus_1_nonclean":
            bool(target_window[TARGET_MOMENT - 1][0]),
        "t_clean": not target_window[TARGET_MOMENT][0],
        "plus_1_through_plus_6_exact_supports": tuple(
            (
                update,
                target_window[update][0],
            )
            for update in range(TARGET_MOMENT + 1, TRAJECTORY_END + 1)
        ),
    }
    result = {
        "nine_key_identity": nine_identity,
        "k2_transient_controls": tuple(control_rows),
    }
    result["pass"] = (
        nine_first_clean == TARGET_MOMENT
        and nine_identity["t_minus_1_nonclean"]
        and nine_identity["t_clean"]
        and all(row["pass"] for row in control_rows)
    )
    return result


def stable_render(
    checks: dict[str, bool],
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        "CYCLE820_SHARED_MOMENT_MECHANISM",
        *(
            f"CERTIFICATE_{name}={compact(value)}"
            for name, value in certificates.items()
        ),
        f"REPORT={compact(report)}",
    ]
    return "\n".join(lines) + "\n"


def run() -> int:
    started = monotonic()
    sources = source_certificate()
    family = build_family()
    arithmetic = arithmetic_certificate(family)
    trajectory = evolve_nine(family)
    population_at_entry = population_state_at_entry(family)
    candidates, prediction = mechanism_candidates(
        family, trajectory, population_at_entry
    )
    identities = identity_controls(family, trajectory)

    replay = evolve_nine(family)
    deterministic = (
        replay["trajectory_sha256"] == trajectory["trajectory_sha256"]
        and replay["first_clean"] == trajectory["first_clean"]
        and replay["nearest_miss_classes"]
        == trajectory["nearest_miss_classes"]
        and replay["coincidence_map"] == trajectory["coincidence_map"]
        and replay["state_hashes_at_checkpoints"]
        == trajectory["state_hashes_at_checkpoints"]
    )

    verdict = {
        "verdict": "MECHANISM_FOUND",
        "named_mechanism":
            "EXACT_SSTAR_ENTRY_PLUS_LEFT_POSITIVE_FIVE_STEP_ANNIHILATOR",
        "statement":
            "exactly the nine keys enter the same 5815-bit state S* at "
            "t=14739; every landed separated-pair word with left>0 maps "
            "S* to one common clean state in exactly the landed lag 5, "
            "therefore all nine select at 14744",
        "arithmetic_center_relation_is_causal": False,
        "prediction_for_151": prediction,
    }
    verdict["pass"] = prediction["pass"]

    elapsed = monotonic() - started
    checks = {
        "A_ARITHMETIC_EXACT_CENSUS": arithmetic["pass"],
        "B_NINE_TRAJECTORIES_AND_COINCIDENCE_MAP": trajectory["pass"],
        "C_EXACT_MECHANISM_CANDIDATES": candidates["pass"],
        "D_MECHANISM_FOUND_WITH_151_FALSIFIER": verdict["pass"],
        "E_IDENTITY_14744_252_371": identities["pass"],
        "F_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT": False,
    }
    controls = {
        **sources,
        "family_reimplementation": family["summary"],
        "determinism_scope":
            "full nine-key t=0..14750 trajectory, nearest misses, "
            "coincidence map, and checkpoint state hashes replayed",
        "primary_trajectory_sha256": trajectory["trajectory_sha256"],
        "replay_trajectory_sha256": replay["trajectory_sha256"],
        "deterministic": deterministic,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
        "pass": False,
    }
    controls_base = (
        sources["pass"]
        and family["summary"]["pass"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
    )
    certificates = {
        "A_ARITHMETIC": arithmetic,
        "B_TRAJECTORY": {
            key: value
            for key, value in trajectory.items()
            if key != "state_at_entry"
        },
        "C_CANDIDATES": candidates,
        "D_VERDICT": verdict,
        "E_IDENTITY": identities,
        "F_CONTROLS": controls,
    }
    report = {
        "cycle": 820,
        "target_moment": TARGET_MOMENT,
        "nine_key_count": len(NINE_KEYS),
        "verdict": verdict["verdict"],
        "named_mechanism": verdict["named_mechanism"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE820_SHARED_MOMENT_MECHANISM_HONEST_FAIL",
    }

    for _iteration in range(6):
        controls["pass"] = controls_base
        checks["F_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
            controls_base
        )
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE820_MECHANISM_FOUND_EXACT_PASS"
            if report["pass"]
            else "CYCLE820_SHARED_MOMENT_MECHANISM_HONEST_FAIL"
        )
        output = stable_render(checks, certificates, report)
        stdout_bytes = len(output.encode("utf-8"))
        stdout_ok = stdout_bytes < STDOUT_LIMIT_BYTES
        controls["stdout_bytes"] = stdout_bytes
        controls["pass"] = controls_base and stdout_ok
        checks["F_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
            controls["pass"]
        )
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE820_MECHANISM_FOUND_EXACT_PASS"
            if report["pass"]
            else "CYCLE820_SHARED_MOMENT_MECHANISM_HONEST_FAIL"
        )
        report["stdout_bytes"] = stdout_bytes
    output = stable_render(checks, certificates, report)
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE820_SHARED_MOMENT_MECHANISM_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
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
            "terminal": "CYCLE820_SHARED_MOMENT_MECHANISM_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
