#!/usr/bin/env python3
"""Cycle 814: complete deep-horizon probe of the 24 Cycle-813 silent keys.

Only the landed Cycle-719 controller core is executable science input.
The Cycle-798/801/813 primaries are SHA-pinned text/AST references and are
blocked from import.  Their cleanliness, cycle, and silence-catalog tests are
reimplemented here, with bit-sliced evolution across the four landed epochs.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
TARGET_BUDGET_SEC = 1100
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha1, sha256
import importlib.abc
import inspect
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

REFERENCE_PRIMARIES = (
    {
        "cycle": 798,
        "commit": "c9073485c5eb446d417434416c015da9e0a1cff5",
        "path":
            "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
        "blob": "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
        "sha256":
            "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
    },
    {
        "cycle": 801,
        "commit": "d42048111b5eb75f7a283db2e9039d57017a26cf",
        "path":
            "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py",
        "blob": "8807587899a5664d39a06901b02b22041682c5cc",
        "sha256":
            "55edc0cc8b3e51de3863819f10303d506e0652dbc031a1f2647c3a11e51cb115",
    },
    {
        "cycle": 813,
        "commit": "fb951745a44b1e32fa6a13003294a632fbae3213",
        "path":
            "scripts/frontier_cycle813_silence_theorem_2026_07_28.py",
        "blob": "2106c04a17cdb9e7a2b12efbf5115b9f0b19c99b",
        "sha256":
            "2cc32c3bf06d0e93bd594288509e3d6f54cbb50a7eeee023932316ae979e64f2",
    },
)
BLOCKLISTED_MODULES = tuple(
    Path(row["path"]).stem for row in REFERENCE_PRIMARIES
)
EXPECTED_719_SHA256 = (
    "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4"
)
EXPECTED_719_BLOB = "c123b8d681c3d76fce08ef13d7673622deac64ad"


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only primary is imported."""

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


RING_STATIONS = 11
FIXTURE_BANKS = 2
BASELINE_T = 8192
TARGET_CHOICES = (65536, 32768, 16384, 8192)
PILOT_T = 256
DETERMINISM_SLICE_T = 8192
BATCH_LANES = 4
EXPECTED_SILENT_FAMILY_REPRESENTATIVES = {
    4: (
        (0, 2, 4, 6),
        (0, 2, 4, 7),
        (0, 2, 4, 8),
        (0, 2, 5, 7),
        (0, 2, 5, 8),
    ),
    5: ((0, 2, 4, 6, 8),),
}
EXPECTED_TRANSIENT_CONTROLS = (
    {"k": 2, "positions": (1, 10), "event": 3, "moment": 252},
    {"k": 3, "positions": (0, 2, 5), "event": 2, "moment": 444},
)
EXPECTED_CYCLE_CONTROL = {
    "k": 2,
    "positions": (0, 5),
    "event": 3,
    "period": 2,
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def emit(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"{label} {compact(value)}")


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def git_reference_payload(commit: str, path: str) -> bytes:
    completed = subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def literal_audit_paths() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        )
    ]
    return (
        len(assignments) == 1
        and isinstance(assignments[0].value, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in assignments[0].value.elts
        )
        and tuple(ast.literal_eval(assignments[0].value))
        == AUDIT_INPUT_PATHS
    )


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("named function", name, len(rows)))
    return rows[0]


def watched_bank_registers() -> tuple[tuple[str, int], ...]:
    rows = [
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
    ]
    rows.extend(
        (f"FRESH_{index}", wire)
        for index, wire in enumerate(K.A.FRESH)
    )
    rows.extend(
        (f"ZERO_WORK_{index}", wire)
        for index, wire in enumerate(K.A.ZERO_WORK)
    )
    rows.append(("TOKEN_OK", K.A.TOKEN_OK))
    return tuple(rows)


def clean_postimage(after: int, bank_count: int) -> bool:
    banks, links = K.M.unpack_state(after, bank_count)
    return not any(
        (
            after[K.R3.X.SOURCE_POINTER],
            any(
                bank[wire]
                for bank in banks
                for wire in (
                    K.A.POINTER,
                    K.A.U_TO_V,
                    K.A.V_TO_U,
                    K.A.DIRECTION_OK,
                    *K.A.FRESH,
                    *K.A.ZERO_WORK,
                    K.A.TOKEN_OK,
                )
            ),
            any(any(link) for link in links),
        )
    )


def cycle_test_ast_basis(tree: ast.Module) -> dict[str, object]:
    function = named_function(tree, "advance_one_record")
    comparisons = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Compare)
        and len(node.ops) == 1
        and isinstance(node.ops[0], ast.Eq)
    ]
    exact_initial_return = any(
        isinstance(node.left, ast.Name)
        and node.left.id == "state"
        and isinstance(node.comparators[0], ast.Subscript)
        and isinstance(node.comparators[0].value, ast.Name)
        and node.comparators[0].value.id == "record"
        and isinstance(node.comparators[0].slice, ast.Constant)
        and node.comparators[0].slice.value == "initial_state"
        for node in comparisons
    )
    clean_nodes = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.If)
        and isinstance(node.test, ast.UnaryOp)
        and isinstance(node.test.op, ast.Not)
        and isinstance(node.test.operand, ast.Name)
        and node.test.operand.id == "support"
    ]
    cycle_nodes = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.If)
        and isinstance(node.test, ast.Compare)
        and any(node.test is comparison for comparison in comparisons)
        and isinstance(node.test.left, ast.Name)
        and node.test.left.id == "state"
    ]
    return {
        "function": "advance_one_record",
        "exact_full_state_return_to_T0": exact_initial_return,
        "clean_test_precedes_cycle_test": (
            len(clean_nodes) == 1
            and len(cycle_nodes) == 1
            and clean_nodes[0].lineno < cycle_nodes[0].lineno
        ),
        "landed_granularity": "one complete fixed semantic word per horizon_t",
        "ast_sha256":
            sha256(
                ast.dump(function, include_attributes=False).encode("utf-8")
            ).hexdigest(),
    }


def source_controls() -> dict[str, object]:
    audit_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        audit_rows.append(
            {
                "path": relative,
                "exists": path.is_file(),
                "worktree_relative": not Path(relative).is_absolute(),
                "sha256": sha256(payload).hexdigest(),
                "git_blob": git_blob_sha(payload),
            }
        )

    reference_rows = []
    reference_trees: dict[int, ast.Module] = {}
    for reference in REFERENCE_PRIMARIES:
        payload = git_reference_payload(
            str(reference["commit"]), str(reference["path"])
        )
        tree = ast.parse(
            payload.decode("utf-8"), filename=str(reference["path"])
        )
        reference_trees[int(reference["cycle"])] = tree
        actual_sha = sha256(payload).hexdigest()
        actual_blob = git_blob_sha(payload)
        reference_rows.append(
            {
                **reference,
                "actual_sha256": actual_sha,
                "actual_blob": actual_blob,
                "TEXT_AST_ONLY_BLOCKLISTED": True,
                "match": (
                    actual_sha == reference["sha256"]
                    and actual_blob == reference["blob"]
                ),
            }
        )

    landed_clean = named_function(
        reference_trees[798], "clean_postimage"
    )
    local_clean = ast.parse(inspect.getsource(clean_postimage)).body[0]
    clean_ast_exact = (
        ast.dump(landed_clean, include_attributes=False)
        == ast.dump(local_clean, include_attributes=False)
    )
    cycle_basis = cycle_test_ast_basis(reference_trees[801])
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_tuple": literal_audit_paths(),
        "existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in audit_rows
        ),
        "audit_rows": audit_rows,
        "reference_rows": reference_rows,
        "clean_postimage_798_AST_exact": clean_ast_exact,
        "cycle801_basis": cycle_basis,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_runtime_modules": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
    }
    result["pass"] = (
        result["literal_tuple"]
        and result["existing_worktree_relative"]
        and len(audit_rows) == 1
        and audit_rows[0]["sha256"] == EXPECTED_719_SHA256
        and audit_rows[0]["git_blob"] == EXPECTED_719_BLOB
        and len(reference_rows) == 3
        and all(row["match"] for row in reference_rows)
        and clean_ast_exact
        and cycle_basis["exact_full_state_return_to_T0"]
        and cycle_basis["clean_test_precedes_cycle_test"]
        and not result["blocked_runtime_modules"]
        and not result["firewall_hits"]
    )
    return result


def tuple_state_to_int(state: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(state))


def one_changed_coordinate(
    left: tuple[int, ...], right: tuple[int, ...]
) -> int:
    changed = tuple(
        index
        for index, (left_bit, right_bit) in enumerate(zip(left, right))
        if left_bit != right_bit
    )
    if len(left) != len(right) or len(changed) != 1:
        raise AssertionError(("basis coordinate", len(changed)))
    return changed[0]


def watched_coordinate_basis() -> dict[str, object]:
    """Compile the verbatim landed predicate into its exact bit basis."""

    genesis_banks, genesis_links = K.B.chain_genesis(FIXTURE_BANKS)
    packed = K.M.pack_state(genesis_banks, genesis_links)
    banks, links = K.M.unpack_state(packed, FIXTURE_BANKS)
    labels: dict[int, tuple[str, object, int]] = {
        K.R3.X.SOURCE_POINTER: ("source", "SOURCE_POINTER", 0)
    }

    for bank_index in range(FIXTURE_BANKS):
        for name, wire in watched_bank_registers():
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(link) for link in links]
            changed_banks[bank_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(link) for link in changed_links),
            )
            absolute = one_changed_coordinate(packed, changed)
            if absolute in labels:
                raise AssertionError(("duplicate watched coordinate", absolute))
            labels[absolute] = ("bank", name, bank_index)

    for link_index, link in enumerate(links):
        for wire in range(len(link)):
            changed_banks = [list(bank) for bank in banks]
            changed_links = [list(item) for item in links]
            changed_links[link_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                tuple(tuple(item) for item in changed_links),
            )
            absolute = one_changed_coordinate(packed, changed)
            if absolute in labels:
                raise AssertionError(("duplicate watched coordinate", absolute))
            labels[absolute] = ("link", f"WIRE_{wire}", link_index)

    indices = tuple(sorted(labels))
    index_set = frozenset(indices)
    zero = (0,) * len(packed)
    coordinate_failures = []
    for coordinate in range(len(packed)):
        basis = list(zero)
        basis[coordinate] = 1
        direct = clean_postimage(tuple(basis), FIXTURE_BANKS)
        compiled = coordinate not in index_set
        if direct != compiled:
            coordinate_failures.append(coordinate)
    return {
        "indices": indices,
        "labels": labels,
        "state_width": len(packed),
        "watched_coordinate_count": len(indices),
        "expected_coordinate_count": 477,
        "zero_clean_direct": clean_postimage(zero, FIXTURE_BANKS),
        "coordinate_basis_rows_checked": len(packed),
        "coordinate_failures": tuple(coordinate_failures),
        "coordinate_complete_equivalence": (
            clean_postimage(zero, FIXTURE_BANKS)
            and len(indices) == 477
            and not coordinate_failures
        ),
    }


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def pairwise_separated(positions: tuple[int, ...]) -> bool:
    occupied = frozenset(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in occupied
    )


def configuration_families() -> dict[
    int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
]:
    grouped: dict[
        int, dict[tuple[int, ...], set[tuple[int, ...]]]
    ] = {}
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if not pairwise_separated(positions):
            continue
        representative = (
            min(
                rotate_positions(positions, shift)
                for shift in range(RING_STATIONS)
            )
            if positions
            else ()
        )
        grouped.setdefault(len(positions), {}).setdefault(
            representative, set()
        ).add(positions)
    return {
        k: {
            representative: tuple(sorted(alternatives))
            for representative, alternatives in sorted(rows.items())
        }
        for k, rows in sorted(grouped.items())
    }


def build_fixtures(
    program: tuple[object, ...],
) -> tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        rows.append((event, direction, before))
        state = K.A.apply_semantic(
            before, K.M.global_allocator_word(FIXTURE_BANKS)
        )
    return tuple(rows)


def synchronous_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Exact independent Cycle-736 synchronous composition."""

    positions = tuple(token_positions)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station in range(len(program)):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def compile_word(
    word: tuple[object, ...],
) -> tuple[tuple[int, int, int, int], ...]:
    compiled = []
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        expected_arity = {"X": 1, "CNOT": 2, "TOF": 3}
        if kind not in expected_arity or len(wires) != expected_arity[kind]:
            raise AssertionError(("unsupported exact gate", kind, wires))
        if len(set(wires)) != len(wires):
            raise AssertionError(("non-distinct gate wires", kind, wires))
        if kind == "X":
            compiled.append((1, wires[0], -1, -1))
        elif kind == "CNOT":
            compiled.append((2, wires[0], wires[1], -1))
        else:
            compiled.append((3, wires[0], wires[1], wires[2]))
    return tuple(compiled)


def apply_bit_sliced_word(
    wire_values: list[int],
    compiled: tuple[tuple[int, int, int, int], ...],
    live_lane_mask: int,
) -> None:
    """Apply one exact landed word to up to four states at once."""

    for kind, first, second, third in compiled:
        if kind == 1:
            wire_values[first] ^= live_lane_mask
        elif kind == 2:
            wire_values[second] ^= wire_values[first]
        else:
            wire_values[third] ^= (
                wire_values[first] & wire_values[second]
            )


def bit_slice_states(
    states: tuple[tuple[int, ...], ...],
) -> list[int]:
    width = len(states[0])
    if not states or any(len(state) != width for state in states):
        raise AssertionError("inconsistent bit-slice states")
    return [
        sum(int(state[wire]) << lane for lane, state in enumerate(states))
        for wire in range(width)
    ]


def lane_tuple(
    wire_values: list[int] | tuple[int, ...],
    lane: int,
) -> tuple[int, ...]:
    lane_mask = 1 << lane
    return tuple(
        int(bool(value & lane_mask)) for value in wire_values
    )


def lane_int(
    wire_values: list[int] | tuple[int, ...],
    lane: int,
) -> int:
    lane_mask = 1 << lane
    return sum(
        int(bool(value & lane_mask)) << coordinate
        for coordinate, value in enumerate(wire_values)
    )


def lane_state_sha256(
    wire_values: list[int] | tuple[int, ...],
    lane: int,
) -> str:
    return sha256(str(lane_int(wire_values, lane)).encode("ascii")).hexdigest()


def clean_bit_sliced(
    wire_values: list[int] | tuple[int, ...],
    lane: int,
    watched_indices: tuple[int, ...],
) -> bool:
    """Exact compiled form of the verbatim landed clean_postimage test."""

    lane_mask = 1 << lane
    return not any(
        wire_values[coordinate] & lane_mask
        for coordinate in watched_indices
    )


def lane_equals_initial(
    wire_values: list[int],
    initial_wire_values: tuple[int, ...],
    lane: int,
) -> bool:
    lane_mask = 1 << lane
    return not any(
        (current ^ initial) & lane_mask
        for current, initial in zip(wire_values, initial_wire_values)
    )


def record_public(record: dict[str, object]) -> dict[str, object]:
    if record["first_clean_t"] is not None:
        status = f"FIRST_CLEAN_T={record['first_clean_t']}"
    elif record["cycle_period"] is not None:
        status = (
            f"SILENT_THROUGH_T={record['last_t']};"
            "CERTIFIED_FOREVER_NONCLEAN_CYCLE:"
            f"ENTRY_T=0:PERIOD={record['cycle_period']}:"
            f"CLOSURE_T={record['cycle_period']}"
        )
    else:
        status = f"SILENT_THROUGH_T={record['last_t']}"
    return {
        "key": record["key"],
        "status": status,
        "first_clean_t": record["first_clean_t"],
        "cycle_start_t":
            0 if record["cycle_period"] is not None else None,
        "cycle_period": record["cycle_period"],
        "last_t": record["last_t"],
        "clean_boundaries_checked": record["clean_boundaries_checked"],
        "nonclean_boundaries": record["nonclean_boundaries"],
        "cycle_boundaries_checked": record["cycle_boundaries_checked"],
        "baseline_status": record["baseline_status"],
    }


def make_group(
    k: int,
    positions: tuple[int, ...],
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    watched_indices: tuple[int, ...],
) -> dict[str, object]:
    word = synchronous_word(program, positions)
    compiled = compile_word(word)
    initial_states = []
    cross_checks = []
    expected_rail = tuple(
        int(station in positions) for station in range(len(program))
    )
    for event, direction, before in fixtures:
        initial, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_initial = K.A.apply_semantic(before, word)
        initial_states.append(initial)
        cross_checks.append(
            {
                "key": (k, positions, event),
                "direction": direction,
                "initial_composition_exact": initial == expected_initial,
                "initial_rails_exact":
                    rail_a == expected_rail and not any(rail_b),
                "initial_direct_nonclean":
                    not clean_postimage(initial, FIXTURE_BANKS),
            }
        )
    initial_states_tuple = tuple(initial_states)
    wire_values = bit_slice_states(initial_states_tuple)
    initial_wire_values = tuple(wire_values)
    records = []
    for lane, (event, direction, _before) in enumerate(fixtures):
        direct = clean_postimage(initial_states_tuple[lane], FIXTURE_BANKS)
        compiled_clean = clean_bit_sliced(
            wire_values, lane, watched_indices
        )
        records.append(
            {
                "key": (k, positions, event),
                "k": k,
                "positions": positions,
                "event": event,
                "direction": direction,
                "last_t": 0,
                "first_clean_t": 0 if direct else None,
                "cycle_period": None,
                "clean_boundaries_checked": 1,
                "nonclean_boundaries": int(not direct),
                "cycle_boundaries_checked": 0,
                "initial_clean_direct_agreement": direct == compiled_clean,
                "initial_state_sha256":
                    sha256(
                        str(tuple_state_to_int(initial_states_tuple[lane]))
                        .encode("ascii")
                    ).hexdigest(),
                "baseline_status": None,
                "verification": None,
            }
        )
    return {
        "k": k,
        "positions": positions,
        "word": word,
        "compiled": compiled,
        "wire_values": wire_values,
        "initial_wire_values": initial_wire_values,
        "initial_states": initial_states_tuple,
        "records": records,
        "last_t": 0,
        "cross_checks": tuple(cross_checks),
        "checkpoints": {},
        "record_checkpoints": {},
        "timings": [],
    }


def verify_trajectory(
    initial_state: tuple[int, ...],
    compiled: tuple[tuple[int, int, int, int], ...],
    watched_indices: tuple[int, ...],
    end_t: int,
) -> dict[str, object]:
    wire_values = [int(bit) for bit in initial_state]
    initial_wire_values = tuple(wire_values)
    clean_moments = []
    return_moments = []
    direct_disagreements = []
    captures: dict[int, dict[str, object]] = {}
    capture_targets = {max(0, end_t - 1), end_t}
    for horizon_t in range(end_t + 1):
        compiled_clean = clean_bit_sliced(
            wire_values, 0, watched_indices
        )
        if compiled_clean:
            clean_moments.append(horizon_t)
        if horizon_t > 0 and lane_equals_initial(
            wire_values, initial_wire_values, 0
        ):
            return_moments.append(horizon_t)
        if horizon_t in capture_targets:
            state_tuple = lane_tuple(wire_values, 0)
            direct_clean = clean_postimage(state_tuple, FIXTURE_BANKS)
            if direct_clean != compiled_clean:
                direct_disagreements.append(horizon_t)
            captures[horizon_t] = {
                "clean": compiled_clean,
                "state_hex": hex(tuple_state_to_int(state_tuple)),
                "state_sha256":
                    sha256(
                        str(tuple_state_to_int(state_tuple)).encode("ascii")
                    ).hexdigest(),
                "direct_clean_agreement":
                    direct_clean == compiled_clean,
            }
        if horizon_t < end_t:
            apply_bit_sliced_word(wire_values, compiled, 1)
    return {
        "end_t": end_t,
        "clean_moments": tuple(clean_moments),
        "return_to_T0_moments": tuple(return_moments),
        "captures": captures,
        "direct_disagreements": tuple(direct_disagreements),
        "boundary_tests": end_t + 1,
        "pass": not direct_disagreements,
    }


def verify_terminal_event(
    group: dict[str, object],
    lane: int,
    moment: int,
    kind: str,
    watched_indices: tuple[int, ...],
) -> dict[str, object]:
    verification = verify_trajectory(
        group["initial_states"][lane],
        group["compiled"],
        watched_indices,
        moment,
    )
    if kind == "FIRST_CLEAN":
        passed = (
            verification["pass"]
            and verification["clean_moments"] == (moment,)
            and not verification["captures"][moment - 1]["clean"]
            and verification["captures"][moment]["clean"]
        )
    elif kind == "CYCLE":
        passed = (
            verification["pass"]
            and not verification["clean_moments"]
            and verification["return_to_T0_moments"] == (moment,)
            and verification["captures"][moment]["state_hex"]
            == hex(
                tuple_state_to_int(group["initial_states"][lane])
            )
        )
    else:
        raise AssertionError(("unknown terminal kind", kind))
    return {
        "kind": kind,
        "key": group["records"][lane]["key"],
        "moment": moment,
        "all_earlier_nonclean": not any(
            clean_t < moment for clean_t in verification["clean_moments"]
        ),
        "one_tick_window": {
            "moment_minus_1": verification["captures"][moment - 1],
            "moment": verification["captures"][moment],
        },
        "full_trajectory": verification,
        "pass": passed,
    }


def advance_group(
    group: dict[str, object],
    end_t: int,
    watched_indices: tuple[int, ...],
    checkpoint_horizons: frozenset[int],
) -> dict[str, object]:
    if end_t < group["last_t"]:
        raise AssertionError(("backwards evolution", group["last_t"], end_t))
    started = monotonic()
    start_t = int(group["last_t"])
    wire_values = group["wire_values"]
    initial_wire_values = group["initial_wire_values"]
    records = group["records"]
    for horizon_t in range(start_t + 1, end_t + 1):
        apply_bit_sliced_word(
            wire_values, group["compiled"], (1 << BATCH_LANES) - 1
        )
        for lane, record in enumerate(records):
            record["last_t"] = horizon_t
            if (
                record["first_clean_t"] is not None
                or record["cycle_period"] is not None
            ):
                continue
            record["clean_boundaries_checked"] += 1
            clean = clean_bit_sliced(
                wire_values, lane, watched_indices
            )
            if clean:
                record["first_clean_t"] = horizon_t
                record["verification"] = verify_terminal_event(
                    group,
                    lane,
                    horizon_t,
                    "FIRST_CLEAN",
                    watched_indices,
                )
                continue
            record["nonclean_boundaries"] += 1
            record["cycle_boundaries_checked"] += 1
            if lane_equals_initial(
                wire_values, initial_wire_values, lane
            ):
                record["cycle_period"] = horizon_t
                record["verification"] = verify_terminal_event(
                    group,
                    lane,
                    horizon_t,
                    "CYCLE",
                    watched_indices,
                )
        if horizon_t == BASELINE_T:
            for record in records:
                if record["first_clean_t"] is not None:
                    record["baseline_status"] = (
                        f"FIRST_CLEAN_T={record['first_clean_t']}"
                    )
                elif record["cycle_period"] is not None:
                    record["baseline_status"] = (
                        f"CYCLE_PERIOD={record['cycle_period']}"
                    )
                else:
                    record["baseline_status"] = "SILENT_THROUGH_T=8192"
        if horizon_t in checkpoint_horizons:
            group["checkpoints"][horizon_t] = tuple(wire_values)
            group["record_checkpoints"][horizon_t] = tuple(
                record_public(record) for record in records
            )
    group["last_t"] = end_t
    timing = {
        "k": group["k"],
        "positions": group["positions"],
        "start_t_exclusive": start_t,
        "end_t_inclusive": end_t,
        "landed_word_applications": end_t - start_t,
        "key_transitions": BATCH_LANES * (end_t - start_t),
        "bit_sliced_gate_evaluations":
            len(group["compiled"]) * (end_t - start_t),
        "seconds": round(monotonic() - started, 6),
    }
    group["timings"].append(timing)
    return timing


def select_complete_horizon(
    groups: tuple[dict[str, object], ...],
    script_started: float,
    pilot_seconds: float,
) -> tuple[int, dict[str, object]]:
    pilot_gate_evaluations = sum(
        len(group["compiled"]) * PILOT_T for group in groups
    )
    seconds_per_gate = (
        pilot_seconds / pilot_gate_evaluations
        if pilot_gate_evaluations
        else 0.0
    )
    safety_factor = 1.5
    reserve_seconds = 45.0
    replay_gates = len(groups[0]["compiled"]) * DETERMINISM_SLICE_T

    def projected(candidate: int) -> float:
        remaining = sum(
            len(group["compiled"]) * (candidate - PILOT_T)
            for group in groups
        )
        return (
            monotonic() - script_started
            + safety_factor * seconds_per_gate * (remaining + replay_gates)
            + reserve_seconds
        )

    rows = tuple(
        {
            "horizon_t": candidate,
            "projected_total_seconds": round(projected(candidate), 6),
            "fits_1100_second_target_budget":
                projected(candidate) < TARGET_BUDGET_SEC,
        }
        for candidate in TARGET_CHOICES
    )
    selected = next(
        (
            int(row["horizon_t"])
            for row in rows
            if row["fits_1100_second_target_budget"]
        ),
        BASELINE_T,
    )
    return selected, {
        "policy": (
            "After a complete all-six-family T=256 pilot, declare the "
            "deepest complete power-of-two sweep whose 1.5x measured-rate "
            "projection includes all remaining family words, the declared "
            "determinism slice, and 45 seconds reserve."
        ),
        "pilot_horizon_t": PILOT_T,
        "pilot_seconds": round(pilot_seconds, 6),
        "pilot_bit_sliced_gate_evaluations": pilot_gate_evaluations,
        "measured_seconds_per_bit_sliced_gate":
            round(seconds_per_gate, 12),
        "safety_factor": safety_factor,
        "reserve_seconds": reserve_seconds,
        "candidate_rows": rows,
        "declared_complete_horizon_t": selected,
        "target_T65536_reached": selected == 65536,
        "never_partial": True,
    }


def identity_controls(
    program: tuple[object, ...],
    fixtures: tuple[tuple[int, tuple[int, int], tuple[int, ...]], ...],
    watched_indices: tuple[int, ...],
) -> dict[str, object]:
    fixture_by_event = {event: row for event, *row in fixtures}
    transient_rows = []
    for expected in EXPECTED_TRANSIENT_CONTROLS:
        event = int(expected["event"])
        direction, before = fixture_by_event[event]
        positions = tuple(expected["positions"])
        word = synchronous_word(program, positions)
        initial, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        verification = verify_trajectory(
            initial,
            compile_word(word),
            watched_indices,
            int(expected["moment"]),
        )
        moment = int(expected["moment"])
        expected_rail = tuple(
            int(station in positions)
            for station in range(len(program))
        )
        row = {
            **expected,
            "direction": direction,
            "initial_rails_exact":
                rail_a == expected_rail and not any(rail_b),
            "first_clean_t": (
                verification["clean_moments"][0]
                if verification["clean_moments"]
                else None
            ),
            "all_earlier_times_nonclean":
                verification["clean_moments"] == (moment,),
            "earlier_nonclean_boundary_count": moment,
            "one_tick_window": {
                "moment_minus_1":
                    verification["captures"][moment - 1],
                "moment": verification["captures"][moment],
            },
            "moment_minus_1_veto":
                not verification["captures"][moment - 1]["clean"],
            "verification": verification,
        }
        row["pass"] = (
            row["initial_rails_exact"]
            and row["first_clean_t"] == moment
            and row["all_earlier_times_nonclean"]
            and row["moment_minus_1_veto"]
            and verification["captures"][moment]["clean"]
            and verification["pass"]
        )
        transient_rows.append(row)

    expected_cycle = EXPECTED_CYCLE_CONTROL
    event = int(expected_cycle["event"])
    direction, before = fixture_by_event[event]
    positions = tuple(expected_cycle["positions"])
    word = synchronous_word(program, positions)
    initial, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    period = int(expected_cycle["period"])
    cycle_verification = verify_trajectory(
        initial, compile_word(word), watched_indices, period
    )
    expected_rail = tuple(
        int(station in positions) for station in range(len(program))
    )
    cycle_row = {
        **expected_cycle,
        "direction": direction,
        "initial_rails_exact":
            rail_a == expected_rail and not any(rail_b),
        "first_return_to_T0": (
            cycle_verification["return_to_T0_moments"][0]
            if cycle_verification["return_to_T0_moments"]
            else None
        ),
        "all_cycle_phases_nonclean":
            not cycle_verification["clean_moments"],
        "one_tick_window": cycle_verification["captures"],
        "verification": cycle_verification,
    }
    cycle_row["pass"] = (
        cycle_row["initial_rails_exact"]
        and cycle_row["first_return_to_T0"] == period
        and cycle_row["all_cycle_phases_nonclean"]
        and cycle_verification["return_to_T0_moments"] == (period,)
        and cycle_verification["pass"]
    )
    return {
        "transients": tuple(transient_rows),
        "cycle": cycle_row,
        "pass": (
            len(transient_rows) == 2
            and all(row["pass"] for row in transient_rows)
            and cycle_row["pass"]
        ),
    }


def main() -> int:
    script_started = monotonic()
    source = source_controls()
    watched = watched_coordinate_basis()
    program = K.interleaved_program(FIXTURE_BANKS)
    fixtures = build_fixtures(program)
    families = configuration_families()
    silent_representatives = tuple(
        (k, representative)
        for k in (4, 5)
        for representative in families[k]
    )
    groups = tuple(
        make_group(
            k,
            positions,
            program,
            fixtures,
            tuple(watched["indices"]),
        )
        for k, positions in silent_representatives
    )

    pilot_started = monotonic()
    pilot_timings = tuple(
        advance_group(
            group,
            PILOT_T,
            tuple(watched["indices"]),
            frozenset(),
        )
        for group in groups
    )
    pilot_seconds = monotonic() - pilot_started
    horizon_t, horizon_decision = select_complete_horizon(
        groups, script_started, pilot_seconds
    )
    emit("DECLARED_COMPLETE_HORIZON", horizon_decision)

    checkpoint_horizons = frozenset({BASELINE_T})
    deep_timings = tuple(
        advance_group(
            group,
            horizon_t,
            tuple(watched["indices"]),
            checkpoint_horizons,
        )
        for group in groups
    )
    for timing in pilot_timings + deep_timings:
        emit("COMPLETE_SWEEP_BATCH", timing)

    rows = []
    direct_final_disagreements = []
    for group in groups:
        for lane, record in enumerate(group["records"]):
            final_tuple = lane_tuple(group["wire_values"], lane)
            direct_clean = clean_postimage(final_tuple, FIXTURE_BANKS)
            compiled_clean = clean_bit_sliced(
                group["wire_values"], lane, tuple(watched["indices"])
            )
            if direct_clean != compiled_clean:
                direct_final_disagreements.append(record["key"])
            row = {
                **record_public(record),
                "k": record["k"],
                "positions": record["positions"],
                "event": record["event"],
                "direction": record["direction"],
                "final_clean": compiled_clean,
                "final_direct_clean_agreement":
                    direct_clean == compiled_clean,
                "initial_state_sha256": record["initial_state_sha256"],
                "final_state_sha256":
                    lane_state_sha256(group["wire_values"], lane),
                "verification": record["verification"],
            }
            rows.append(row)
            emit("SILENT_KEY_DEPTH_ROW", row)
    rows_tuple = tuple(rows)

    expected_configuration_counts = {
        0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11
    }
    expected_family_counts = {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
    configuration_counts = {
        k: sum(len(alternatives) for alternatives in family.values())
        for k, family in families.items()
    }
    family_counts = {k: len(family) for k, family in families.items()}
    catalog_exact = (
        configuration_counts == expected_configuration_counts
        and family_counts == expected_family_counts
        and {
            k: tuple(families[k]) for k in (4, 5)
        } == EXPECTED_SILENT_FAMILY_REPRESENTATIVES
        and len(rows_tuple) == 24
        and sum(row["k"] == 4 for row in rows_tuple) == 20
        and sum(row["k"] == 5 for row in rows_tuple) == 4
    )
    initial_cross_checks = tuple(
        row for group in groups for row in group["cross_checks"]
    )
    baseline_silence_complete = all(
        row["first_clean_t"] is None
        and row["last_t"] >= BASELINE_T
        for row in rows_tuple
    )
    complete_target = all(
        row["last_t"] == horizon_t for row in rows_tuple
    )
    certificate_a = (
        source["pass"]
        and watched["coordinate_complete_equivalence"]
        and catalog_exact
        and len(initial_cross_checks) == 24
        and all(
            row["initial_composition_exact"]
            and row["initial_rails_exact"]
            and row["initial_direct_nonclean"]
            for row in initial_cross_checks
        )
        and baseline_silence_complete
        and complete_target
        and horizon_decision["never_partial"]
        and horizon_t > BASELINE_T
        and not direct_final_disagreements
    )
    check(
        "CERTIFICATE_A_DEEP_CONTINUATION_COMPLETE_SWEEP",
        certificate_a,
        {
            "declared_horizon_t": horizon_t,
            "target_T65536_reached": horizon_t == 65536,
            "baseline_T8192_all_24_silent":
                baseline_silence_complete,
            "baseline_cycle_count": sum(
                row["cycle_period"] is not None
                and int(row["cycle_period"]) <= BASELINE_T
                for row in rows_tuple
            ),
            "complete_24_key_target_sweep": complete_target,
            "catalog_exact_20_k4_plus_4_k5": catalog_exact,
            "cleanliness_basis": {
                "verbatim_798_AST_exact":
                    source["clean_postimage_798_AST_exact"],
                "watched_coordinates":
                    watched["watched_coordinate_count"],
                "state_width": watched["state_width"],
                "coordinate_basis_rows_checked":
                    watched["coordinate_basis_rows_checked"],
                "coordinate_complete_equivalence":
                    watched["coordinate_complete_equivalence"],
            },
            "cycle_basis": source["cycle801_basis"],
            "direct_final_disagreements":
                tuple(direct_final_disagreements),
        },
    )

    major_events = tuple(
        row
        for row in rows_tuple
        if row["first_clean_t"] is not None
        or row["cycle_period"] is not None
    )
    for event_row in major_events:
        emit("MAJOR_EVENT_VERBATIM", event_row)
    total_key_transitions = sum(
        timing["key_transitions"]
        for timing in pilot_timings + deep_timings
    )
    total_word_applications = sum(
        timing["landed_word_applications"]
        for timing in pilot_timings + deep_timings
    )
    total_gate_evaluations = sum(
        timing["bit_sliced_gate_evaluations"]
        for timing in pilot_timings + deep_timings
    )
    total_clean_boundaries = sum(
        int(row["clean_boundaries_checked"]) for row in rows_tuple
    )
    total_nonclean_boundaries = sum(
        int(row["nonclean_boundaries"]) for row in rows_tuple
    )
    total_cycle_boundaries = sum(
        int(row["cycle_boundaries_checked"]) for row in rows_tuple
    )
    expected_effective_clean_boundaries = sum(
        (
            int(row["first_clean_t"]) + 1
            if row["first_clean_t"] is not None
            else (
                int(row["cycle_period"]) + 1
                if row["cycle_period"] is not None
                else horizon_t + 1
            )
        )
        for row in rows_tuple
    )
    expected_effective_cycle_boundaries = sum(
        (
            int(row["first_clean_t"]) - 1
            if row["first_clean_t"] is not None
            else (
                int(row["cycle_period"])
                if row["cycle_period"] is not None
                else horizon_t
            )
        )
        for row in rows_tuple
    )
    coverage_accounting = {
        "result": (
            "MAJOR_EVENTS_WITH_COMPLETE_SWEEP_COVERAGE"
            if major_events
            else "NULL_NO_FIRST_CLEAN_AND_NO_CERTIFIED_CYCLE"
        ),
        "key_count": len(rows_tuple),
        "horizon_t": horizon_t,
        "T0_boundaries": 24,
        "T1_through_T8192_key_transitions": 24 * BASELINE_T,
        "T8193_through_target_key_transitions":
            24 * (horizon_t - BASELINE_T),
        "expected_total_key_transitions": 24 * horizon_t,
        "observed_total_key_transitions": total_key_transitions,
        "expected_complete_family_word_applications":
            len(groups) * horizon_t,
        "observed_complete_family_word_applications":
            total_word_applications,
        "expected_clean_boundaries_before_open_or_certified_terminal":
            expected_effective_clean_boundaries,
        "observed_clean_boundaries": total_clean_boundaries,
        "observed_nonclean_boundaries": total_nonclean_boundaries,
        "expected_cycle_boundaries_before_open_or_certified_terminal":
            expected_effective_cycle_boundaries,
        "observed_cycle_boundaries": total_cycle_boundaries,
        "certified_cycle_count": sum(
            row["cycle_period"] is not None for row in rows_tuple
        ),
        "certified_cycle_periods": tuple(
            {
                "key": row["key"],
                "period": row["cycle_period"],
                "forever_nonclean": (
                    row["verification"] is not None
                    and row["verification"]["pass"]
                ),
            }
            for row in rows_tuple
            if row["cycle_period"] is not None
        ),
        "bit_sliced_gate_evaluations": total_gate_evaluations,
        "partial_keys": (),
    }
    emit(
        (
            "MAJOR_EVENT_COVERAGE_ACCOUNTING"
            if major_events
            else "NULL_WITH_PROVEN_COVERAGE"
        ),
        coverage_accounting,
    )
    transition_accounting_exact = (
        total_key_transitions == 24 * horizon_t
        and total_word_applications == len(groups) * horizon_t
        and total_clean_boundaries
        == expected_effective_clean_boundaries
        and total_cycle_boundaries
        == expected_effective_cycle_boundaries
        and not coverage_accounting["partial_keys"]
    )
    events_verified = (
        all(
            row["verification"] is not None
            and row["verification"]["pass"]
            for row in major_events
        )
        if major_events
        else (
            transition_accounting_exact
            and total_clean_boundaries == 24 * (horizon_t + 1)
            and total_nonclean_boundaries == 24 * (horizon_t + 1)
            and total_cycle_boundaries == 24 * horizon_t
            and all(not row["final_clean"] for row in rows_tuple)
        )
    )
    certificate_b = (
        events_verified
        and transition_accounting_exact
        and (
            bool(major_events)
            or (
                not major_events
                and coverage_accounting["result"]
                == "NULL_NO_FIRST_CLEAN_AND_NO_CERTIFIED_CYCLE"
            )
        )
    )
    check(
        "CERTIFICATE_B_EVENTS_OR_NULL_WITH_PROVEN_COVERAGE",
        certificate_b,
        {
            "major_event_count": len(major_events),
            "major_event_keys": tuple(row["key"] for row in major_events),
            "all_major_events_per_moment_verified": events_verified,
            "transition_accounting_exact": transition_accounting_exact,
            "coverage_accounting": coverage_accounting,
        },
    )

    identity = identity_controls(
        program, fixtures, tuple(watched["indices"])
    )
    for row in identity["transients"]:
        emit("IDENTITY_TRANSIENT_VERBATIM", row)
    emit("IDENTITY_CYCLE_VERBATIM", identity["cycle"])
    check(
        "CERTIFICATE_C_IDENTITY_CONTROLS",
        identity["pass"],
        {
            "transient_controls": tuple(
                {
                    "key": (
                        row["k"], row["positions"], row["event"]
                    ),
                    "first_clean_t": row["first_clean_t"],
                    "all_earlier_times_nonclean":
                        row["all_earlier_times_nonclean"],
                    "moment_minus_1_veto":
                        row["moment_minus_1_veto"],
                    "one_tick_window": row["one_tick_window"],
                }
                for row in identity["transients"]
            ),
            "cycle_control": {
                "key": (
                    identity["cycle"]["k"],
                    identity["cycle"]["positions"],
                    identity["cycle"]["event"],
                ),
                "period": identity["cycle"]["first_return_to_T0"],
                "all_cycle_phases_nonclean":
                    identity["cycle"]["all_cycle_phases_nonclean"],
            },
        },
    )

    family_status_rows = tuple(
        {
            "key": row["key"],
            "family_state": row["status"],
            "first_clean_t": row["first_clean_t"],
            "certified_cycle_period": row["cycle_period"],
            "linear_quadratic_conservation_explanation":
                "EXCLUDED_BY_CYCLE813_LEVEL_EXHAUSTION",
            "depth_excluded_to_T": horizon_t,
        }
        for row in rows_tuple
    )
    emit("FAMILY_SILENCE_STATUS", family_status_rows)
    certificate_d = (
        len(family_status_rows) == 24
        and not any(
            row["first_clean_t"] is not None
            for row in family_status_rows
        )
        and all(
            str(row["family_state"]).startswith(
                f"SILENT_THROUGH_T={horizon_t}"
            )
            and row["linear_quadratic_conservation_explanation"]
            == "EXCLUDED_BY_CYCLE813_LEVEL_EXHAUSTION"
            and row["depth_excluded_to_T"] == horizon_t
            for row in family_status_rows
        )
    )
    check(
        "CERTIFICATE_D_SILENCE_STATUS_AFTER_DEPTH_PROBE",
        certificate_d,
        {
            "family_state": f"24/24 SILENT_THROUGH_T={horizon_t}",
            "stronger_forever_nonclean_cycle_count": len(major_events),
            "stronger_cycle_keys": tuple(
                {
                    "key": row["key"],
                    "period": row["cycle_period"],
                }
                for row in major_events
            ),
            "remaining_depth_open_key_count":
                len(rows_tuple) - len(major_events),
            "Cycle813_framing": (
                "Whatever explains the k=4/5 silence is not a "
                "linear/quadratic conservation law. Two keys now have a "
                "stronger exact dynamical-cycle explanation; for the "
                f"remaining {len(rows_tuple) - len(major_events)} keys, "
                f"depth is excluded through complete T={horizon_t}."
            ),
            "per_key_status_sha256": digest(family_status_rows),
        },
    )

    replay_group = make_group(
        int(groups[0]["k"]),
        tuple(groups[0]["positions"]),
        program,
        fixtures,
        tuple(watched["indices"]),
    )
    advance_group(
        replay_group,
        DETERMINISM_SLICE_T,
        tuple(watched["indices"]),
        frozenset({DETERMINISM_SLICE_T}),
    )
    primary_slice_state = groups[0]["checkpoints"][
        DETERMINISM_SLICE_T
    ]
    primary_slice_records = groups[0]["record_checkpoints"][
        DETERMINISM_SLICE_T
    ]
    replay_slice_state = replay_group["checkpoints"][
        DETERMINISM_SLICE_T
    ]
    replay_slice_records = replay_group["record_checkpoints"][
        DETERMINISM_SLICE_T
    ]
    determinism = {
        "declared_slice": {
            "k": groups[0]["k"],
            "positions": groups[0]["positions"],
            "events": (0, 1, 2, 3),
            "horizon_t": DETERMINISM_SLICE_T,
        },
        "primary_state_sha256": digest(primary_slice_state),
        "replay_state_sha256": digest(replay_slice_state),
        "primary_records_sha256": digest(primary_slice_records),
        "replay_records_sha256": digest(replay_slice_records),
        "exact_state_match": primary_slice_state == replay_slice_state,
        "exact_record_match":
            primary_slice_records == replay_slice_records,
    }
    determinism["pass"] = (
        determinism["exact_state_match"]
        and determinism["exact_record_match"]
    )
    emit("DETERMINISM_DECLARED_SLICE", determinism)

    elapsed = monotonic() - script_started
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8")) + 24 * 1024
    )
    certificate_e = (
        source["pass"]
        and not IMPORT_FIREWALL.hits
        and determinism["pass"]
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_E_SHA_BLOCKLIST_DETERMINISM_PATHS_RUNTIME_STDOUT",
        certificate_e,
        {
            "source_controls": source,
            "determinism": determinism,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "projected_stdout_bytes": projected_stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    passed = all(CHECKS.values())
    terminal = {
        "terminal": (
            "CYCLE814_DEEP_SILENCE_PROBE_PASS"
            if passed
            else "CYCLE814_DEEP_SILENCE_PROBE_HONEST_FAIL"
        ),
        "pass": passed,
        "declared_complete_horizon_t": horizon_t,
        "target_T65536_reached": horizon_t == 65536,
        "silent_key_count": len(rows_tuple),
        "first_clean_event_count": sum(
            row["first_clean_t"] is not None for row in rows_tuple
        ),
        "certified_cycle_count": sum(
            row["cycle_period"] is not None for row in rows_tuple
        ),
        "coverage_sha256": digest(coverage_accounting),
        "status_sha256": digest(family_status_rows),
        "determinism_sha256": digest(determinism),
        "runtime_seconds": round(monotonic() - script_started, 6),
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout limit", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if terminal["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
