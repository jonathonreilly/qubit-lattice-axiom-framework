#!/usr/bin/env python3
"""Cycle 814 independent adversarial checker.

The Cycle-814, Cycle-798, and Cycle-801 primaries are text/AST-only evidence
and are blocked from import.  The only executable science input is the landed
Cycle-719 controller core.  This checker supplies its own Boolean gate
evaluator, synchronous-word evolution, landed-cleanliness reimplementation,
cycle/minimal-period checks, and a declared eight-key null spot sweep.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha1, sha256
import importlib
import importlib.abc
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
        "cycle": 814,
        "module": "frontier_cycle814_deep_silence_probe_2026_07_28",
        "source": "worktree",
        "path":
            "scripts/frontier_cycle814_deep_silence_probe_2026_07_28.py",
        "sha256":
            "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
        "git_blob": "19ba617ad1f6be9f8fdc637b764dc7b38cae8d7b",
        "required_function": "verify_terminal_event",
    },
    {
        "cycle": 798,
        "module": "frontier_cycle798_higher_k_horizon_scan_2026_07_28",
        "source": "git",
        "commit": "c9073485c5eb446d417434416c015da9e0a1cff5",
        "path":
            "scripts/frontier_cycle798_higher_k_horizon_scan_2026_07_28.py",
        "sha256":
            "f6ec49636ecb7ec09808eed7d38f2085f6145cd383c306370502c547741942b1",
        "git_blob": "9de34ad5adcbf484d4f0c7e6aec13375ed465aab",
        "required_function": "clean_postimage",
    },
    {
        "cycle": 801,
        "module": "frontier_cycle801_silent_strata_deep_scan_2026_07_28",
        "source": "git",
        "commit": "d42048111b5eb75f7a283db2e9039d57017a26cf",
        "path":
            "scripts/frontier_cycle801_silent_strata_deep_scan_2026_07_28.py",
        "sha256":
            "55edc0cc8b3e51de3863819f10303d506e0652dbc031a1f2647c3a11e51cb115",
        "git_blob": "8807587899a5664d39a06901b02b22041682c5cc",
        "required_function": "advance_one_record",
    },
)
BLOCKLISTED_MODULES = tuple(
    str(row["module"]) for row in REFERENCE_PRIMARIES
)
EXPECTED_INPUT_ANCHORS = {
    AUDIT_INPUT_PATHS[0]: {
        "sha256":
            "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
        "git_blob": "c123b8d681c3d76fce08ef13d7673622deac64ad",
    },
    AUDIT_INPUT_PATHS[1]: {
        "sha256":
            "f023d10784506e0c9ffbb39b17c3f120af78f377f27c5dab93de9a9aebaa98c0",
        "git_blob": "19ba617ad1f6be9f8fdc637b764dc7b38cae8d7b",
    },
}


class PrimaryBlocklist(importlib.abc.MetaPathFinder):
    """Fail closed if any attacked primary is imported."""

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
            raise ImportError(f"BLOCKLIST text/AST-only primary: {fullname}")
        return None


FIREWALL = PrimaryBlocklist()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
BANK_COUNT = 2
TARGET_T = 65536
CLAIMED_PERIOD = 4464
DETERMINISM_SLICE_T = 4096
CLAIMED_CYCLE_KEYS = (
    (4, (0, 2, 4, 7), 1),
    (4, (0, 2, 4, 8), 1),
)
DECLARED_NULL_KEYS = (
    (4, (0, 2, 4, 6), 0),
    (4, (0, 2, 4, 6), 1),
    (4, (0, 2, 4, 6), 2),
    (4, (0, 2, 4, 6), 3),
    (4, (0, 2, 4, 7), 0),
    (4, (0, 2, 4, 7), 2),
    (4, (0, 2, 4, 8), 0),
    (4, (0, 2, 4, 8), 2),
)
TRANSIENT_CONTROL = (3, (0, 2, 5), 2, 444)
CYCLE_CONTROL = (2, (0, 5), 3, 2)

CERTIFICATES: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload
    ).hexdigest()


def certificate(name: str, passed: bool, finding: object) -> None:
    if name in CERTIFICATES:
        raise AssertionError(("duplicate certificate", name))
    CERTIFICATES[name] = bool(passed)
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {name} :: {compact(finding)}"
    )


def literal_audit_input_paths() -> bool:
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


def reference_payload(row: dict[str, object]) -> bytes:
    if row["source"] == "worktree":
        return (ROOT / str(row["path"])).read_bytes()
    completed = subprocess.run(
        (
            "git",
            "show",
            f"{row['commit']}:{row['path']}",
        ),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout


def source_controls() -> dict[str, object]:
    input_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        payload = path.read_bytes() if path.is_file() else b""
        observed = {
            "path": relative,
            "exists": path.is_file(),
            "worktree_relative": not Path(relative).is_absolute(),
            "sha256": sha256(payload).hexdigest(),
            "git_blob": git_blob(payload),
        }
        expected = EXPECTED_INPUT_ANCHORS[relative]
        observed["anchor_match"] = (
            observed["sha256"] == expected["sha256"]
            and observed["git_blob"] == expected["git_blob"]
        )
        input_rows.append(observed)

    reference_rows = []
    for reference in REFERENCE_PRIMARIES:
        payload = reference_payload(reference)
        tree = ast.parse(
            payload.decode("utf-8"), filename=str(reference["path"])
        )
        function_names = tuple(
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        )
        reference_rows.append(
            {
                "cycle": reference["cycle"],
                "module": reference["module"],
                "path": reference["path"],
                "source": reference["source"],
                "sha256": sha256(payload).hexdigest(),
                "git_blob": git_blob(payload),
                "sha_match": (
                    sha256(payload).hexdigest() == reference["sha256"]
                    and git_blob(payload) == reference["git_blob"]
                ),
                "AST_parse": True,
                "required_function": reference["required_function"],
                "required_function_found":
                    reference["required_function"] in function_names,
                "TEXT_AST_ONLY": True,
            }
        )

    checker_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    forbidden_runtime_calls = tuple(
        sorted(
            {
                node.attr
                for node in ast.walk(checker_tree)
                if isinstance(node, ast.Attribute)
                and node.attr in {"apply_semantic", "run_orbit"}
            }
        )
    )
    blocked_messages = []
    for module in BLOCKLISTED_MODULES:
        try:
            importlib.import_module(module)
        except ImportError as error:
            blocked_messages.append(str(error))

    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_AUDIT_INPUT_PATHS": literal_audit_input_paths(),
        "input_rows": tuple(input_rows),
        "reference_rows": tuple(reference_rows),
        "blocked_modules": BLOCKLISTED_MODULES,
        "block_messages": tuple(blocked_messages),
        "firewall_hits": tuple(FIREWALL.hits),
        "blocked_absent_from_runtime_modules": all(
            module not in sys.modules for module in BLOCKLISTED_MODULES
        ),
        "forbidden_landed_evaluator_calls": forbidden_runtime_calls,
        "own_evolution_only": not forbidden_runtime_calls,
    }
    result["pass"] = (
        result["literal_AUDIT_INPUT_PATHS"]
        and all(
            row["exists"]
            and row["worktree_relative"]
            and row["anchor_match"]
            for row in input_rows
        )
        and all(
            row["sha_match"] and row["required_function_found"]
            for row in reference_rows
        )
        and tuple(FIREWALL.hits) == BLOCKLISTED_MODULES
        and len(blocked_messages) == len(BLOCKLISTED_MODULES)
        and result["blocked_absent_from_runtime_modules"]
        and result["own_evolution_only"]
    )
    return result


CompiledGate = tuple[tuple[int, ...], int]


def tuple_to_int(state: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(state))


def int_to_tuple(state: int, width: int) -> tuple[int, ...]:
    return tuple((state >> index) & 1 for index in range(width))


def full_state_sha256(state: int, width: int) -> str:
    payload = state.to_bytes((width + 7) // 8, "little")
    return sha256(payload).hexdigest()


def watched_bank_wires() -> tuple[int, ...]:
    return (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )


def landed_clean_reimplementation(state: int, width: int) -> bool:
    """Structural reimplementation of the landed Cycle-798 predicate."""

    packed = int_to_tuple(state, width)
    banks, links = K.M.unpack_state(packed, BANK_COUNT)
    return (
        not packed[K.R3.X.SOURCE_POINTER]
        and not any(
            bank[wire]
            for bank in banks
            for wire in watched_bank_wires()
        )
        and not any(bit for link in links for bit in link)
    )


def one_changed_coordinate(
    left: tuple[int, ...], right: tuple[int, ...]
) -> int:
    changed = tuple(
        index
        for index, pair in enumerate(zip(left, right))
        if pair[0] != pair[1]
    )
    if len(left) != len(right) or len(changed) != 1:
        raise AssertionError(("not one coordinate", len(changed)))
    return changed[0]


def watched_coordinate_basis() -> dict[str, object]:
    """Reconstruct the exact cleanliness mask from structural perturbations."""

    banks, links = K.B.chain_genesis(BANK_COUNT)
    packed = K.M.pack_state(banks, links)
    unpacked_banks, unpacked_links = K.M.unpack_state(packed, BANK_COUNT)
    labels: dict[int, tuple[str, int, int]] = {
        K.R3.X.SOURCE_POINTER: ("source", 0, K.R3.X.SOURCE_POINTER)
    }

    for bank_index in range(BANK_COUNT):
        for wire in watched_bank_wires():
            changed_banks = [list(bank) for bank in unpacked_banks]
            changed_banks[bank_index][wire] ^= 1
            changed = K.M.pack_state(
                tuple(tuple(bank) for bank in changed_banks),
                unpacked_links,
            )
            coordinate = one_changed_coordinate(packed, changed)
            if coordinate in labels:
                raise AssertionError(("duplicate watched bit", coordinate))
            labels[coordinate] = ("bank", bank_index, wire)

    for link_index, link in enumerate(unpacked_links):
        for wire in range(len(link)):
            changed_links = [list(row) for row in unpacked_links]
            changed_links[link_index][wire] ^= 1
            changed = K.M.pack_state(
                unpacked_banks,
                tuple(tuple(row) for row in changed_links),
            )
            coordinate = one_changed_coordinate(packed, changed)
            if coordinate in labels:
                raise AssertionError(("duplicate watched bit", coordinate))
            labels[coordinate] = ("link", link_index, wire)

    width = len(packed)
    indices = tuple(sorted(labels))
    index_set = frozenset(indices)
    disagreements = []
    for coordinate in range(width):
        direct = landed_clean_reimplementation(1 << coordinate, width)
        compiled = coordinate not in index_set
        if direct != compiled:
            disagreements.append(coordinate)
    zero_clean = landed_clean_reimplementation(0, width)
    return {
        "state_width": width,
        "indices": indices,
        "labels": labels,
        "watched_count": len(indices),
        "zero_clean": zero_clean,
        "coordinate_rows_checked": width,
        "coordinate_disagreements": tuple(disagreements),
        "pass": (
            zero_clean
            and len(indices) == 477
            and not disagreements
        ),
    }


def compile_gates(gates: tuple[object, ...]) -> tuple[CompiledGate, ...]:
    expected_arity = {"X": 1, "CNOT": 2, "TOF": 3}
    compiled = []
    for gate in gates:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind not in expected_arity or len(wires) != expected_arity[kind]:
            raise AssertionError(("unsupported gate", kind, wires))
        if len(set(wires)) != len(wires):
            raise AssertionError(("repeated gate wire", kind, wires))
        compiled.append((wires[:-1], wires[-1]))
    return tuple(compiled)


def apply_scalar_word(state: int, word: tuple[CompiledGate, ...]) -> int:
    """Apply a Boolean reversible word without the landed evaluator."""

    for controls, target in word:
        if all((state >> control) & 1 for control in controls):
            state ^= 1 << target
    return state


def apply_sliced_word(
    wire_values: list[int],
    word: tuple[CompiledGate, ...],
    live_lane_mask: int,
) -> None:
    """Apply the same word to all selected lanes with local Boolean logic."""

    for controls, target in word:
        enabled = live_lane_mask
        for control in controls:
            enabled &= wire_values[control]
        wire_values[target] ^= enabled


def bit_slice(states: tuple[int, ...], width: int) -> list[int]:
    return [
        sum(((state >> coordinate) & 1) << lane
            for lane, state in enumerate(states))
        for coordinate in range(width)
    ]


def lane_int(wire_values: list[int] | tuple[int, ...], lane: int) -> int:
    lane_mask = 1 << lane
    return sum(
        int(bool(value & lane_mask)) << coordinate
        for coordinate, value in enumerate(wire_values)
    )


def dirty_lane_mask(
    wire_values: list[int] | tuple[int, ...],
    watched_indices: tuple[int, ...],
) -> int:
    dirty = 0
    for coordinate in watched_indices:
        dirty |= wire_values[coordinate]
    return dirty


def synchronous_word(
    program: tuple[object, ...], positions: tuple[int, ...]
) -> tuple[CompiledGate, ...]:
    """Compose one full orbit directly from rotating occupied stations."""

    live = tuple(positions)
    gates = []
    for _step in range(len(program)):
        live_set = frozenset(live)
        for station, row in enumerate(program):
            if station in live_set:
                gates.extend(K.mapped_macro(row))
        live = tuple((station + 1) % len(program) for station in live)
    return compile_gates(tuple(gates))


def rotate(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def separated(positions: tuple[int, ...]) -> bool:
    occupied = frozenset(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in occupied
    )


def configuration_families() -> dict[
    int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
]:
    grouped: dict[int, dict[tuple[int, ...], set[tuple[int, ...]]]] = {}
    for mask in range(1 << RING_STATIONS):
        positions = tuple(
            station
            for station in range(RING_STATIONS)
            if mask & (1 << station)
        )
        if not separated(positions):
            continue
        representative = (
            min(rotate(positions, shift) for shift in range(RING_STATIONS))
            if positions
            else ()
        )
        grouped.setdefault(len(positions), {}).setdefault(
            representative, set()
        ).add(positions)
    return {
        k: {
            representative: tuple(sorted(configurations))
            for representative, configurations in sorted(rows.items())
        }
        for k, rows in sorted(grouped.items())
    }


def build_fixtures(width: int) -> dict[int, dict[str, object]]:
    """Build all four event inputs using the independent evaluator."""

    banks, links = K.B.chain_genesis(BANK_COUNT)
    state = tuple_to_int(K.M.pack_state(banks, links))
    allocator = compile_gates(
        tuple(K.M.global_allocator_word(BANK_COUNT))
    )
    fixtures = {}
    for event in range(2 * BANK_COUNT):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before_tuple = K.M.prepare_endpoint(
            int_to_tuple(state, width), direction
        )
        before = tuple_to_int(before_tuple)
        fixtures[event] = {
            "event": event,
            "direction": direction,
            "before": before,
        }
        state = apply_scalar_word(before, allocator)
    return fixtures


def proper_divisors(value: int) -> tuple[int, ...]:
    return tuple(
        candidate
        for candidate in range(1, value)
        if value % candidate == 0
    )


def make_group(
    positions: tuple[int, ...],
    events: tuple[int, ...],
    program: tuple[object, ...],
    fixtures: dict[int, dict[str, object]],
    width: int,
    watched_indices: tuple[int, ...],
) -> dict[str, object]:
    word = synchronous_word(program, positions)
    initial_states = tuple(
        apply_scalar_word(int(fixtures[event]["before"]), word)
        for event in events
    )
    wire_values = bit_slice(initial_states, width)
    initial_dirty = dirty_lane_mask(wire_values, watched_indices)
    records = []
    for lane, (event, initial) in enumerate(zip(events, initial_states)):
        compiled_clean = not bool(initial_dirty & (1 << lane))
        direct_clean = landed_clean_reimplementation(initial, width)
        records.append(
            {
                "key": (len(positions), positions, event),
                "lane": lane,
                "initial_state": initial,
                "initial_state_sha256":
                    full_state_sha256(initial, width),
                "first_clean_t": 0 if compiled_clean else None,
                "clean_boundaries_checked": 1,
                "nonclean_boundaries": int(not compiled_clean),
                "period_clean_moments": (
                    [0] if compiled_clean and 0 < CLAIMED_PERIOD else []
                ),
                "period_nonclean_boundaries": int(not compiled_clean),
                "captures": {
                    0: {
                        "state_sha256": full_state_sha256(initial, width),
                        "clean": compiled_clean,
                        "direct_clean":
                            direct_clean,
                        "direct_clean_agreement":
                            compiled_clean == direct_clean,
                    }
                },
            }
        )
    return {
        "positions": positions,
        "events": events,
        "word": word,
        "wire_values": wire_values,
        "initial_wire_values": tuple(wire_values),
        "records": records,
        "last_t": 0,
        "checkpoint_wires": {},
        "gate_count": len(word),
    }


def capture_group(
    group: dict[str, object],
    horizon_t: int,
    width: int,
    watched_indices: tuple[int, ...],
) -> None:
    wire_values = group["wire_values"]
    dirty = dirty_lane_mask(wire_values, watched_indices)
    for record in group["records"]:
        lane = int(record["lane"])
        state = lane_int(wire_values, lane)
        compiled_clean = not bool(dirty & (1 << lane))
        direct_clean = landed_clean_reimplementation(state, width)
        record["captures"][horizon_t] = {
            "state_sha256": full_state_sha256(state, width),
            "clean": compiled_clean,
            "direct_clean": direct_clean,
            "direct_clean_agreement": compiled_clean == direct_clean,
            "equals_anchor": state == record["initial_state"],
        }


def advance_group(
    group: dict[str, object],
    end_t: int,
    width: int,
    watched_indices: tuple[int, ...],
    capture_times: frozenset[int],
    checkpoint_times: frozenset[int] = frozenset(),
) -> dict[str, object]:
    """Advance one family word completely with independent bit-sliced gates."""

    if group["last_t"] != 0:
        raise AssertionError(("group already advanced", group["last_t"]))
    started = monotonic()
    if 0 in capture_times:
        capture_group(group, 0, width, watched_indices)
    live_lane_mask = (1 << len(group["records"])) - 1
    for horizon_t in range(1, end_t + 1):
        apply_sliced_word(
            group["wire_values"], group["word"], live_lane_mask
        )
        dirty = dirty_lane_mask(group["wire_values"], watched_indices)
        for record in group["records"]:
            lane = int(record["lane"])
            clean = not bool(dirty & (1 << lane))
            record["clean_boundaries_checked"] += 1
            if clean and record["first_clean_t"] is None:
                record["first_clean_t"] = horizon_t
            if not clean:
                record["nonclean_boundaries"] += 1
            if horizon_t < CLAIMED_PERIOD:
                if clean:
                    record["period_clean_moments"].append(horizon_t)
                else:
                    record["period_nonclean_boundaries"] += 1
        if horizon_t in capture_times:
            capture_group(
                group, horizon_t, width, watched_indices
            )
        if horizon_t in checkpoint_times:
            group["checkpoint_wires"][horizon_t] = tuple(
                group["wire_values"]
            )
    group["last_t"] = end_t
    return {
        "positions": group["positions"],
        "events": group["events"],
        "start_t": 0,
        "end_t": end_t,
        "lane_count": len(group["records"]),
        "key_transitions": len(group["records"]) * end_t,
        "word_applications": end_t,
        "gate_evaluations": len(group["word"]) * end_t,
        "seconds": round(monotonic() - started, 6),
    }


def record_by_key(
    groups: tuple[dict[str, object], ...]
) -> dict[tuple[int, tuple[int, ...], int], dict[str, object]]:
    rows = {}
    for group in groups:
        for record in group["records"]:
            key = record["key"]
            if key in rows:
                raise AssertionError(("duplicate key", key))
            rows[key] = record
    return rows


def catalog_attack(
    families: dict[
        int, dict[tuple[int, ...], tuple[tuple[int, ...], ...]]
    ],
) -> dict[str, object]:
    all_keys = tuple(
        (k, representative, event)
        for k in (4, 5)
        for representative in families[k]
        for event in range(2 * BANK_COUNT)
    )
    open_keys = tuple(
        key for key in all_keys if key not in CLAIMED_CYCLE_KEYS
    )
    configuration_counts = {
        k: sum(len(rows) for rows in families[k].values())
        for k in families
    }
    family_counts = {k: len(rows) for k, rows in families.items()}
    return {
        "all_silent_keys": all_keys,
        "open_keys": open_keys,
        "configuration_counts": configuration_counts,
        "family_counts": family_counts,
        "declared_null_keys": DECLARED_NULL_KEYS,
        "declared_null_count": len(DECLARED_NULL_KEYS),
        "declared_subset_of_22_open": (
            len(open_keys) == 22
            and set(DECLARED_NULL_KEYS).issubset(open_keys)
        ),
        "pass": (
            configuration_counts
            == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
            and family_counts
            == {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
            and len(all_keys) == 24
            and len(open_keys) == 22
            and len(DECLARED_NULL_KEYS) >= 6
            and len(set(DECLARED_NULL_KEYS)) == len(DECLARED_NULL_KEYS)
            and set(DECLARED_NULL_KEYS).issubset(open_keys)
        ),
    }


def cycle_attacks(
    rows: dict[
        tuple[int, tuple[int, ...], int], dict[str, object]
    ],
) -> tuple[dict[str, object], dict[str, object]]:
    divisors = proper_divisors(CLAIMED_PERIOD)
    certifications = []
    minimal_rows = []
    for key in CLAIMED_CYCLE_KEYS:
        record = rows[key]
        captures = record["captures"]
        anchor = captures[0]
        closure = captures[CLAIMED_PERIOD]
        divisor_rows = tuple(
            {
                "divisor": divisor,
                "state_sha256": captures[divisor]["state_sha256"],
                "equals_anchor": captures[divisor]["equals_anchor"],
            }
            for divisor in divisors
        )
        period_clean_moments = tuple(record["period_clean_moments"])
        direct_capture_agreement = all(
            capture["direct_clean_agreement"]
            for capture in captures.values()
        )
        certification = {
            "key": key,
            "anchor_t": 0,
            "anchor_full_state_sha256": anchor["state_sha256"],
            "closure_t": CLAIMED_PERIOD,
            "closure_full_state_sha256": closure["state_sha256"],
            "exact_full_state_recurrence":
                closure["equals_anchor"]
                and closure["state_sha256"] == anchor["state_sha256"],
            "claimed_period": CLAIMED_PERIOD,
            "period_boundaries_checked": CLAIMED_PERIOD,
            "period_nonclean_boundaries":
                record["period_nonclean_boundaries"],
            "period_clean_moments": period_clean_moments,
            "every_phase_in_one_full_period_nonclean": (
                record["period_nonclean_boundaries"] == CLAIMED_PERIOD
                and not period_clean_moments
            ),
            "closure_nonclean": not closure["clean"],
            "preperiod_start_t": 0,
            "preperiod_end_exclusive_t": 0,
            "preperiod_length": 0,
            "preperiod_nonclean": True,
            "preperiod_vacuous_because_anchor_is_T0": True,
            "anchor_nonclean": not anchor["clean"],
            "direct_landed_test_capture_agreement":
                direct_capture_agreement,
            "first_clean_through_T65536": record["first_clean_t"],
        }
        certification["forever_nonclean_follows"] = (
            certification["exact_full_state_recurrence"]
            and certification["every_phase_in_one_full_period_nonclean"]
            and certification["closure_nonclean"]
            and certification["preperiod_nonclean"]
            and certification["anchor_nonclean"]
        )
        certification["pass"] = (
            certification["forever_nonclean_follows"]
            and certification["direct_landed_test_capture_agreement"]
            and certification["first_clean_through_T65536"] is None
        )
        certifications.append(certification)

        divisor_returns = tuple(
            row["divisor"]
            for row in divisor_rows
            if row["equals_anchor"]
        )
        minimal = {
            "key": key,
            "period": CLAIMED_PERIOD,
            "proper_divisors": divisors,
            "proper_divisor_count": len(divisors),
            "divisor_state_rows": divisor_rows,
            "returning_proper_divisors": divisor_returns,
            "no_proper_divisor_is_period": not divisor_returns,
            "period_recurrence_verified":
                certification["exact_full_state_recurrence"],
        }
        minimal["minimal_period_4464"] = (
            minimal["period_recurrence_verified"]
            and minimal["no_proper_divisor_is_period"]
        )
        minimal["pass"] = minimal["minimal_period_4464"]
        minimal_rows.append(minimal)
    certification_result = {
        "claimed_cycle_count": len(CLAIMED_CYCLE_KEYS),
        "rows": tuple(certifications),
        "pass": (
            len(certifications) == 2
            and all(row["pass"] for row in certifications)
        ),
    }
    minimal_result = {
        "method": (
            "A minimal state period must divide every exact return time; "
            "4464 recurs and every proper divisor is tested against the "
            "complete Boolean state."
        ),
        "rows": tuple(minimal_rows),
        "pass": (
            len(minimal_rows) == 2
            and all(row["pass"] for row in minimal_rows)
        ),
    }
    return certification_result, minimal_result


def null_spot_attack(
    rows: dict[
        tuple[int, tuple[int, ...], int], dict[str, object]
    ],
    catalog: dict[str, object],
) -> dict[str, object]:
    findings = []
    for key in DECLARED_NULL_KEYS:
        record = rows[key]
        captures = record["captures"]
        direct_capture_agreement = all(
            capture["direct_clean_agreement"]
            for capture in captures.values()
        )
        finding = {
            "key": key,
            "declared_open_key": key in catalog["open_keys"],
            "horizon_t": TARGET_T,
            "first_clean_t": record["first_clean_t"],
            "clean_boundaries_checked":
                record["clean_boundaries_checked"],
            "nonclean_boundaries": record["nonclean_boundaries"],
            "T0_full_state_sha256":
                captures[0]["state_sha256"],
            "T65536_full_state_sha256":
                captures[TARGET_T]["state_sha256"],
            "direct_landed_test_capture_agreement":
                direct_capture_agreement,
        }
        finding["pass"] = (
            finding["declared_open_key"]
            and finding["first_clean_t"] is None
            and finding["clean_boundaries_checked"] == TARGET_T + 1
            and finding["nonclean_boundaries"] == TARGET_T + 1
            and finding["direct_landed_test_capture_agreement"]
        )
        findings.append(finding)
    missed = tuple(
        row for row in findings if row["first_clean_t"] is not None
    )
    return {
        "declared_choice": DECLARED_NULL_KEYS,
        "declared_choice_count": len(DECLARED_NULL_KEYS),
        "claimed_open_population": 22,
        "target_t": TARGET_T,
        "key_transitions": len(DECLARED_NULL_KEYS) * TARGET_T,
        "first_clean_events_found": missed,
        "rows": tuple(findings),
        "REFUTES_NULL_IF_NONEMPTY": missed,
        "pass": (
            catalog["pass"]
            and len(findings) >= 6
            and not missed
            and all(row["pass"] for row in findings)
        ),
    }


def scalar_trajectory(
    initial: int,
    word: tuple[CompiledGate, ...],
    end_t: int,
    watched_mask: int,
    width: int,
    capture_times: frozenset[int],
) -> dict[str, object]:
    state = initial
    clean_moments = []
    return_moments = []
    captures = {}
    direct_disagreements = []
    for horizon_t in range(end_t + 1):
        compiled_clean = not bool(state & watched_mask)
        if compiled_clean:
            clean_moments.append(horizon_t)
        if horizon_t > 0 and state == initial:
            return_moments.append(horizon_t)
        if horizon_t in capture_times:
            direct_clean = landed_clean_reimplementation(state, width)
            if direct_clean != compiled_clean:
                direct_disagreements.append(horizon_t)
            captures[horizon_t] = {
                "state_sha256": full_state_sha256(state, width),
                "clean": compiled_clean,
                "direct_clean": direct_clean,
                "direct_clean_agreement":
                    direct_clean == compiled_clean,
                "equals_anchor": state == initial,
            }
        if horizon_t < end_t:
            state = apply_scalar_word(state, word)
    return {
        "end_t": end_t,
        "clean_moments": tuple(clean_moments),
        "return_moments": tuple(return_moments),
        "captures": captures,
        "direct_disagreements": tuple(direct_disagreements),
        "boundary_count": end_t + 1,
    }


def identity_controls(
    program: tuple[object, ...],
    fixtures: dict[int, dict[str, object]],
    watched_indices: tuple[int, ...],
    width: int,
) -> dict[str, object]:
    watched_mask = sum(1 << coordinate for coordinate in watched_indices)

    transient_k, transient_positions, transient_event, transient_t = (
        TRANSIENT_CONTROL
    )
    transient_word = synchronous_word(program, transient_positions)
    transient_initial = apply_scalar_word(
        int(fixtures[transient_event]["before"]), transient_word
    )
    transient_walk = scalar_trajectory(
        transient_initial,
        transient_word,
        transient_t,
        watched_mask,
        width,
        frozenset({0, transient_t - 1, transient_t}),
    )
    transient = {
        "key": (
            transient_k, transient_positions, transient_event
        ),
        "claimed_first_clean_t": transient_t,
        "observed_clean_moments": transient_walk["clean_moments"],
        "first_clean_t": (
            transient_walk["clean_moments"][0]
            if transient_walk["clean_moments"]
            else None
        ),
        "all_earlier_boundaries_nonclean": (
            transient_walk["clean_moments"] == (transient_t,)
        ),
        "T443_clean":
            transient_walk["captures"][transient_t - 1]["clean"],
        "T444_clean":
            transient_walk["captures"][transient_t]["clean"],
        "captures": transient_walk["captures"],
        "direct_disagreements":
            transient_walk["direct_disagreements"],
    }
    transient["pass"] = (
        transient["first_clean_t"] == transient_t
        and transient["all_earlier_boundaries_nonclean"]
        and not transient["T443_clean"]
        and transient["T444_clean"]
        and not transient["direct_disagreements"]
    )

    cycle_k, cycle_positions, cycle_event, cycle_period = CYCLE_CONTROL
    control_word = synchronous_word(program, cycle_positions)
    control_initial = apply_scalar_word(
        int(fixtures[cycle_event]["before"]), control_word
    )
    control_walk = scalar_trajectory(
        control_initial,
        control_word,
        cycle_period,
        watched_mask,
        width,
        frozenset(range(cycle_period + 1)),
    )
    control_divisors = proper_divisors(cycle_period)
    cycle = {
        "key": (cycle_k, cycle_positions, cycle_event),
        "claimed_period": cycle_period,
        "anchor_full_state_sha256":
            control_walk["captures"][0]["state_sha256"],
        "closure_full_state_sha256":
            control_walk["captures"][cycle_period]["state_sha256"],
        "exact_recurrence": (
            control_walk["captures"][cycle_period]["equals_anchor"]
            and control_walk["captures"][0]["state_sha256"]
            == control_walk["captures"][cycle_period]["state_sha256"]
        ),
        "proper_divisors": control_divisors,
        "returning_proper_divisors": tuple(
            divisor
            for divisor in control_divisors
            if control_walk["captures"][divisor]["equals_anchor"]
        ),
        "clean_moments": control_walk["clean_moments"],
        "all_cycle_phases_nonclean":
            not control_walk["clean_moments"],
        "return_moments": control_walk["return_moments"],
        "captures": control_walk["captures"],
        "direct_disagreements":
            control_walk["direct_disagreements"],
    }
    cycle["pass"] = (
        cycle["exact_recurrence"]
        and not cycle["returning_proper_divisors"]
        and cycle["all_cycle_phases_nonclean"]
        and cycle["return_moments"] == (cycle_period,)
        and not cycle["direct_disagreements"]
    )
    return {
        "known_k3_transient_444": transient,
        "known_k_le_3_cycle": cycle,
        "pass": transient["pass"] and cycle["pass"],
    }


def determinism_attack(
    deep_group: dict[str, object],
    program: tuple[object, ...],
    fixtures: dict[int, dict[str, object]],
    width: int,
    watched_indices: tuple[int, ...],
) -> dict[str, object]:
    positions = tuple(deep_group["positions"])
    events = tuple(deep_group["events"])
    deep_checkpoint = deep_group["checkpoint_wires"][
        DETERMINISM_SLICE_T
    ]
    replay = make_group(
        positions,
        events,
        program,
        fixtures,
        width,
        watched_indices,
    )
    replay_timing = advance_group(
        replay,
        DETERMINISM_SLICE_T,
        width,
        watched_indices,
        frozenset({0, DETERMINISM_SLICE_T}),
        frozenset({DETERMINISM_SLICE_T}),
    )
    replay_checkpoint = replay["checkpoint_wires"][
        DETERMINISM_SLICE_T
    ]
    deep_lane_hashes = tuple(
        record["captures"][DETERMINISM_SLICE_T]["state_sha256"]
        for record in deep_group["records"]
    )
    replay_lane_hashes = tuple(
        record["captures"][DETERMINISM_SLICE_T]["state_sha256"]
        for record in replay["records"]
    )
    return {
        "declared_slice": {
            "k": len(positions),
            "positions": positions,
            "events": events,
            "start_t": 0,
            "end_t": DETERMINISM_SLICE_T,
        },
        "deep_checkpoint_sha256": digest(deep_checkpoint),
        "replay_checkpoint_sha256": digest(replay_checkpoint),
        "deep_lane_full_state_sha256": deep_lane_hashes,
        "replay_lane_full_state_sha256": replay_lane_hashes,
        "exact_bit_sliced_state_match":
            deep_checkpoint == replay_checkpoint,
        "all_lane_hashes_match":
            deep_lane_hashes == replay_lane_hashes,
        "replay_timing": replay_timing,
        "pass": (
            deep_checkpoint == replay_checkpoint
            and deep_lane_hashes == replay_lane_hashes
        ),
    }


def science_run() -> dict[str, object]:
    watched = watched_coordinate_basis()
    width = int(watched["state_width"])
    watched_indices = tuple(watched["indices"])
    program = K.interleaved_program(BANK_COUNT)
    fixtures = build_fixtures(width)
    families = configuration_families()
    catalog = catalog_attack(families)

    selected_keys = CLAIMED_CYCLE_KEYS + DECLARED_NULL_KEYS
    events_by_positions: dict[tuple[int, ...], set[int]] = {}
    for _k, positions, event in selected_keys:
        events_by_positions.setdefault(positions, set()).add(event)
    groups = tuple(
        make_group(
            positions,
            tuple(sorted(events)),
            program,
            fixtures,
            width,
            watched_indices,
        )
        for positions, events in sorted(events_by_positions.items())
    )
    if sum(len(group["records"]) for group in groups) != len(
        set(selected_keys)
    ):
        raise AssertionError("selected-key grouping mismatch")

    divisor_captures = frozenset(
        {0, CLAIMED_PERIOD - 1, CLAIMED_PERIOD, TARGET_T}
        | set(proper_divisors(CLAIMED_PERIOD))
    )
    timings = []
    determinism_group = None
    for group in groups:
        positions = tuple(group["positions"])
        if positions == (0, 2, 4, 6):
            captures = frozenset(
                {0, DETERMINISM_SLICE_T, TARGET_T}
            )
            checkpoints = frozenset({DETERMINISM_SLICE_T})
            determinism_group = group
        else:
            captures = divisor_captures
            checkpoints = frozenset()
        timings.append(
            advance_group(
                group,
                TARGET_T,
                width,
                watched_indices,
                captures,
                checkpoints,
            )
        )
    if determinism_group is None:
        raise AssertionError("declared determinism family absent")

    rows = record_by_key(groups)
    certifications, periods = cycle_attacks(rows)
    null_spot = null_spot_attack(rows, catalog)
    identities = identity_controls(
        program, fixtures, watched_indices, width
    )
    determinism = determinism_attack(
        determinism_group,
        program,
        fixtures,
        width,
        watched_indices,
    )
    capture_disagreements = tuple(
        {
            "key": key,
            "time": horizon_t,
        }
        for key, record in rows.items()
        for horizon_t, capture in record["captures"].items()
        if not capture["direct_clean_agreement"]
    )
    accounting = {
        "selected_key_count": len(rows),
        "selected_cycle_key_count": len(CLAIMED_CYCLE_KEYS),
        "declared_null_key_count": len(DECLARED_NULL_KEYS),
        "horizon_t": TARGET_T,
        "expected_selected_key_transitions":
            len(rows) * TARGET_T,
        "observed_selected_key_transitions": sum(
            row["key_transitions"] for row in timings
        ),
        "expected_family_word_applications":
            len(groups) * TARGET_T,
        "observed_family_word_applications": sum(
            row["word_applications"] for row in timings
        ),
        "bit_sliced_gate_evaluations": sum(
            row["gate_evaluations"] for row in timings
        ),
        "capture_direct_clean_disagreements":
            capture_disagreements,
        "timings": tuple(timings),
    }
    accounting["pass"] = (
        accounting["selected_key_count"] == 10
        and accounting["observed_selected_key_transitions"]
        == accounting["expected_selected_key_transitions"]
        and accounting["observed_family_word_applications"]
        == accounting["expected_family_word_applications"]
        and not capture_disagreements
    )
    return {
        "watched": {
            "state_width": watched["state_width"],
            "watched_count": watched["watched_count"],
            "zero_clean": watched["zero_clean"],
            "coordinate_rows_checked":
                watched["coordinate_rows_checked"],
            "coordinate_disagreements":
                watched["coordinate_disagreements"],
            "pass": watched["pass"],
        },
        "catalog": catalog,
        "certifications": certifications,
        "periods": periods,
        "null_spot": null_spot,
        "identities": identities,
        "determinism": determinism,
        "accounting": accounting,
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    science = science_run()

    certification_finding = {
        "landed_cleanliness_reimplementation": science["watched"],
        "selected_sweep_accounting": science["accounting"],
        "certifications": science["certifications"],
    }
    certification_pass = (
        science["watched"]["pass"]
        and science["accounting"]["pass"]
        and science["certifications"]["pass"]
    )
    certificate(
        "THE_TWO_CERTIFICATIONS",
        certification_pass,
        certification_finding,
    )

    null_finding = {
        "catalog": {
            "configuration_counts":
                science["catalog"]["configuration_counts"],
            "family_counts": science["catalog"]["family_counts"],
            "all_silent_key_count":
                len(science["catalog"]["all_silent_keys"]),
            "open_key_count": len(science["catalog"]["open_keys"]),
            "declared_subset_of_22_open":
                science["catalog"]["declared_subset_of_22_open"],
        },
        "coverage": science["null_spot"],
        "selected_sweep_accounting": science["accounting"],
    }
    null_pass = (
        science["catalog"]["pass"]
        and science["accounting"]["pass"]
        and science["null_spot"]["pass"]
    )
    certificate(
        "NULL_SPOT_COVERAGE",
        null_pass,
        null_finding,
    )

    certificate(
        "PERIOD_CROSS_CHECK",
        bool(science["periods"]["pass"]),
        science["periods"],
    )

    certificate(
        "IDENTITY_CONTROLS",
        (
            science["watched"]["pass"]
            and science["identities"]["pass"]
        ),
        science["identities"],
    )

    elapsed_before_controls = monotonic() - started
    preliminary_control_detail = {
        "source_controls": controls,
        "determinism": science["determinism"],
        "runtime_seconds_before_terminal":
            round(elapsed_before_controls, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(compact(preliminary_control_detail).encode("utf-8"))
        + 8192
    )
    control_detail = {
        **preliminary_control_detail,
        "projected_stdout_bytes": projected_stdout_bytes,
        "literal_AUDIT_INPUT_PATHS":
            controls["literal_AUDIT_INPUT_PATHS"],
        "existing_worktree_relative_inputs": all(
            row["exists"] and row["worktree_relative"]
            for row in controls["input_rows"]
        ),
    }
    controls_pass = (
        controls["pass"]
        and science["determinism"]["pass"]
        and elapsed_before_controls < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    certificate(
        "CONTROLS_SHA_BLOCKLIST_DETERMINISM_PATHS_RUNTIME_STDOUT",
        controls_pass,
        control_detail,
    )

    science_certificates = (
        "THE_TWO_CERTIFICATIONS",
        "NULL_SPOT_COVERAGE",
        "PERIOD_CROSS_CHECK",
        "IDENTITY_CONTROLS",
    )
    primary_refuted = any(
        not CERTIFICATES[name] for name in science_certificates
    )
    if primary_refuted:
        overall = "REFUTED"
    elif not controls_pass:
        overall = "INCONCLUSIVE_CHECKER_CONTROL_FAILURE"
    else:
        overall = "CONFIRMED_ON_DECLARED_INDEPENDENT_SCOPE"
    terminal = {
        "terminal": (
            "CYCLE814_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if all(CERTIFICATES.values())
            else "CYCLE814_INDEPENDENT_ADVERSARIAL_CHECK_HONEST_FAIL"
        ),
        "pass": all(CERTIFICATES.values()),
        "overall": overall,
        "claimed_cycle_keys": CLAIMED_CYCLE_KEYS,
        "cycle_period": CLAIMED_PERIOD,
        "declared_null_keys": DECLARED_NULL_KEYS,
        "null_keys_checked": len(DECLARED_NULL_KEYS),
        "null_horizon_t": TARGET_T,
        "missed_first_clean_events":
            science["null_spot"]["first_clean_events_found"],
        "identity_controls_pass": science["identities"]["pass"],
        "determinism_sha256": digest(science["determinism"]),
        "runtime_seconds": round(monotonic() - started, 6),
    }
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout limit exceeded", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if terminal["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
