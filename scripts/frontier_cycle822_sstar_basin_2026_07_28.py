#!/usr/bin/env python3
"""Cycle 822: exact S* basin census and k=2 domain-law attempt.

The Cycle-819 and Cycle-820 primaries are SHA-pinned text/AST-only
references.  They are blocklisted from import and execution.  This single
runner imports only the landed Cycle-719 controller core, reconstructs the
176-key family, reconstructs S* along two independent key trajectories, and
performs a complete exact sweep through T=24576.

The population sweep bit-slices keys, not physics: at each controller
station, the landed X/CNOT/TOF gate is applied under the exact mask of keys
whose token occupies that station.  A scalar one-step comparison certifies
the representation before the sweep.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
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
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[2]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[2]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
}


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if either text/AST-only predecessor is imported."""

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
Lane = tuple[Key, str]
MaskedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
MECHANISM_ENTRY = 14739
SELECTION_MOMENT = 14744
FIXED_LAG = 5
TARGET_HORIZON = 24576
CHECKPOINTS = (
    0, 4096, 8192, 12288, 14738, 14739, 14740, 16384, 20480,
    TARGET_HORIZON,
)
DETERMINISM_SLICE_SIZE = 8
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
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


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


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


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
    functions819 = function_names(trees[AUDIT_INPUT_PATHS[1]])
    functions820 = function_names(trees[AUDIT_INPUT_PATHS[2]])
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
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "cycle819_AST_basis": {
            "build_family",
            "advance_population",
            "verify_transient",
            "verify_cycle",
        } <= functions819,
        "cycle820_AST_basis": {
            "build_family",
            "evolve_nine",
            "population_state_at_entry",
            "mechanism_candidates",
        } <= functions820,
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
        and result["cycle819_AST_basis"]
        and result["cycle820_AST_basis"]
        and direct_frontier_imports == {
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

    summary = {
        "epochs": len(epochs),
        "program_stations": len(program),
        "positions": len(positions),
        "keys": len(states),
        "state_bits": len(next(iter(states.values()))),
        "allocator_gates": len(allocator),
        "synchronous_word_gate_counts":
            tuple(sorted({len(word) for word in words.values()})),
        "unique_initial_supports": len(set(supports.values())),
        "unique_initial_supports_by_epoch": tuple(
            len({
                supports[(event, positions0)]
                for positions0 in positions
            })
            for event in range(2 * FIXTURE_BANKS)
        ),
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
        and summary["state_bits"] == 5815
        and summary["allocator_gates"] == 3106
        and summary["synchronous_word_gate_counts"] == (6212,)
        and summary["unique_initial_supports"] == 25
        and summary["unique_initial_supports_by_epoch"] == (1, 1, 12, 14)
        and summary["epoch_failures"] == 0
        and summary["composition_failures"] == 0
        and summary["rail_failures"] == 0
    )
    return {
        "program": program,
        "positions": positions,
        "words": words,
        "states": states,
        "supports": supports,
        "summary": summary,
    }


def bit_slice(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(state[wire] << index for index, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int], index: int) -> tuple[int, ...]:
    return tuple((column >> index) & 1 for column in columns)


def masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
) -> tuple[MaskedGate, ...]:
    rows: list[MaskedGate] = []
    for step in range(len(program)):
        for station, program_row in enumerate(program):
            lane_mask = sum(
                1 << lane_index
                for lane_index, (key, _replica) in enumerate(lanes)
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
                    raise ValueError(("unsupported landed gate", gate))
    return tuple(rows)


def apply_masked(
    columns: list[int],
    schedule: tuple[MaskedGate, ...],
) -> None:
    for kind, first, second, third, lane_mask in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )


def scalar_equivalence(
    family: dict[str, object],
    keys: tuple[Key, ...],
) -> dict[str, object]:
    lanes = tuple((key, "primary") for key in keys)
    initial = tuple(family["states"][key] for key in keys)
    columns = bit_slice(initial)
    schedule = masked_schedule(family["program"], lanes)
    apply_masked(columns, schedule)
    sliced = tuple(un_slice(columns, index) for index in range(len(keys)))
    scalar = tuple(
        K.A.apply_semantic(state, family["words"][key[1]])
        for key, state in zip(keys, initial)
    )
    result = {
        "scope": "one exact update on eight lexicographic family keys",
        "keys": keys,
        "masked_gate_rows": len(schedule),
        "exact_tuple_equal": sliced == scalar,
        "sliced_sha256": digest(tuple(map(state_sha256, sliced))),
        "scalar_sha256": digest(tuple(map(state_sha256, scalar))),
    }
    result["pass"] = result["exact_tuple_equal"]
    return result


def evolve_sstar_pair(
    family: dict[str, object],
) -> dict[str, object]:
    # Use distinct left-position classes so the two-key witness also
    # witnesses the nine-trajectory inequality on both adjacent ticks.
    keys = (NINE_KEYS[0], NINE_KEYS[-1])
    lanes = tuple((key, "certificate_A") for key in keys)
    columns = bit_slice(tuple(family["states"][key] for key in keys))
    schedule = masked_schedule(family["program"], lanes)
    snapshots: dict[int, tuple[tuple[int, ...], ...]] = {}
    for update in range(MECHANISM_ENTRY + 2):
        if update in {
            MECHANISM_ENTRY - 1,
            MECHANISM_ENTRY,
            MECHANISM_ENTRY + 1,
        }:
            snapshots[update] = tuple(
                un_slice(columns, index) for index in range(len(keys))
            )
        if update <= MECHANISM_ENTRY:
            apply_masked(columns, schedule)
    before = snapshots[MECHANISM_ENTRY - 1]
    entry = snapshots[MECHANISM_ENTRY]
    after = snapshots[MECHANISM_ENTRY + 1]
    sstar = entry[0]
    result = {
        "trajectory_keys": keys,
        "evolution_updates": MECHANISM_ENTRY + 1,
        "masked_gate_rows_per_update": len(schedule),
        "t14738_state_sha256": tuple(map(state_sha256, before)),
        "t14738_exact_tuple_unequal": before[0] != before[1],
        "t14739_state_sha256": tuple(map(state_sha256, entry)),
        "t14739_exact_tuple_equal": entry[0] == entry[1],
        "t14740_state_sha256": tuple(map(state_sha256, after)),
        "t14740_exact_tuple_unequal": after[0] != after[1],
        "sstar_sha256": state_sha256(sstar),
        "sstar_full_state_bits": len(sstar),
        "sstar_full_state_hamming_weight": sum(sstar),
        "sstar": sstar,
    }
    result["pass"] = (
        result["t14738_exact_tuple_unequal"]
        and result["t14739_exact_tuple_equal"]
        and result["t14740_exact_tuple_unequal"]
        and len(sstar) == 5815
    )
    return result


def bit_tuple(state: tuple[int, ...], wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(state[wire] for wire in wires)


def integer_bits(bits: tuple[int, ...]) -> int:
    return sum(bit << index for index, bit in enumerate(bits))


def packet_row(
    bank: tuple[int, ...],
    cell_index: int,
) -> dict[str, object]:
    layout = K.A.CELLS[cell_index]
    fields = {}
    for name in (
        "pred", "rotor_before", "rotor_after", "carry", "delta",
        "endpoint", "binder", "valid", "orientation", "actual",
        "admiss", "law",
    ):
        wires = layout[name]
        wire_tuple = (int(wires),) if isinstance(wires, int) else tuple(wires)
        bits = bit_tuple(bank, wire_tuple)
        fields[name] = {
            "bits_little_endian": bits,
            "integer": integer_bits(bits),
        }
    return fields


def anatomy_signature(state: tuple[int, ...]) -> tuple[object, ...]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    return (
        tuple(index for index in range(41) if state[index]),
        tuple(
            (
                bit_tuple(bank, tuple(
                    int(wire)
                    for layout in K.A.CELLS
                    for name in (
                        "pred", "rotor_before", "rotor_after", "carry",
                        "delta", "endpoint", "binder", "valid",
                        "orientation", "actual", "admiss", "law",
                    )
                    for wire in (
                        (layout[name],)
                        if isinstance(layout[name], int)
                        else layout[name]
                    )
                )),
                bit_tuple(bank, K.A.HEAD),
                bit_tuple(bank, K.A.ROTOR),
                bit_tuple(bank, K.A.TOKEN),
                bit_tuple(bank, K.A.FRESH),
                tuple(bank[wire] for _name, wire in watched_registers()),
                bank[K.A.BINDER],
                bank[K.A.ACTUAL],
                bank[K.A.ADMISS],
                bank[K.A.LAW],
            )
            for bank in banks
        ),
        links,
    )


def sstar_anatomy(
    family: dict[str, object],
    reconstruction: dict[str, object],
) -> dict[str, object]:
    state = reconstruction["sstar"]
    assert isinstance(state, tuple)
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    bank_rows = []
    for bank_index, bank in enumerate(banks):
        bank_rows.append({
            "bank": bank_index,
            "hamming_weight": sum(bank),
            "occupancy_valid_row": tuple(
                bank[int(layout["valid"])] for layout in K.A.CELLS
            ),
            "packet_rows": tuple(
                packet_row(bank, cell_index)
                for cell_index in range(len(K.A.CELLS))
            ),
            "head_bits_little_endian": bit_tuple(bank, K.A.HEAD),
            "head_integer": integer_bits(bit_tuple(bank, K.A.HEAD)),
            "rotor_bits_little_endian": bit_tuple(bank, K.A.ROTOR),
            "rotor_integer": integer_bits(bit_tuple(bank, K.A.ROTOR)),
            "token_row": bit_tuple(bank, K.A.TOKEN),
            "token_count": sum(bank[wire] for wire in K.A.TOKEN),
            "fresh_row": bit_tuple(bank, K.A.FRESH),
            "interface_registers": {
                "POINTER": bank[K.A.POINTER],
                "U_TO_V": bank[K.A.U_TO_V],
                "V_TO_U": bank[K.A.V_TO_U],
                "DIRECTION_OK": bank[K.A.DIRECTION_OK],
                "BINDER": bank[K.A.BINDER],
                "ACTUAL": bank[K.A.ACTUAL],
                "ADMISS": bank[K.A.ADMISS],
                "LAW": bank[K.A.LAW],
                "TOKEN_OK": bank[K.A.TOKEN_OK],
                "ENABLE_TARGET": bank[K.A.ENABLE_TARGET],
            },
            "zero_work_active_indices": tuple(
                index for index, wire in enumerate(K.A.ZERO_WORK)
                if bank[wire]
            ),
            "all_active_local_wire_indices": tuple(
                index for index, bit in enumerate(bank) if bit
            ),
        })
    source_active = tuple(index for index in range(41) if state[index])
    anatomy = {
        "identity": {
            "full_state_sha256": state_sha256(state),
            "full_state_bits": len(state),
            "hamming_weight": sum(state),
            "second_trajectory_hash_verified":
                reconstruction["t14739_exact_tuple_equal"],
        },
        "source_matter_row": {
            "matter_bits_0_through_11": tuple(state[:12]),
            "active_matter_indices": tuple(
                index for index in range(12) if state[index]
            ),
            "left_endpoint": state[K.R3.X.LEFT_ENDPOINT],
            "right_endpoint": state[K.R3.X.RIGHT_ENDPOINT],
            "source_pointer": state[K.R3.X.SOURCE_POINTER],
            "active_source_register_indices_0_through_40": source_active,
        },
        "banks": tuple(bank_rows),
        "links": tuple({
            "link": link_index,
            "hamming_weight": sum(link),
            "active_wire_indices": tuple(
                index for index, bit in enumerate(link) if bit
            ),
        } for link_index, link in enumerate(links)),
        "residual_support": canonical_support(residual_support(state)),
        "residual_support_weight": len(residual_support(state)),
        "bank_exact_symmetry": banks[0] == banks[1],
        "named_charge_register_present": False,
        "charge_label_policy":
            "the landed schema names no charge register; no proxy is invented",
        "anatomy_signature_sha256": digest(anatomy_signature(state)),
    }
    anatomy["pass"] = (
        anatomy["identity"]["second_trajectory_hash_verified"]
        and anatomy["identity"]["full_state_bits"] == 5815
        and anatomy["identity"]["hamming_weight"] == sum(state)
        and anatomy["residual_support_weight"] > 0
    )
    return anatomy


def cyclic_separation(key: Key) -> int:
    left, right = key[1]
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def predictor_row(
    name: str,
    predicate: Callable[[Key], bool],
    entrants: tuple[Key, ...],
    open_keys: tuple[Key, ...],
    resolved_other: tuple[Key, ...],
    statement: str,
) -> dict[str, object]:
    universe = tuple(sorted(entrants + open_keys + resolved_other))
    selected = tuple(key for key in universe if predicate(key))
    entrant_set = set(entrants)
    false_negatives = tuple(
        key for key in entrants if not predicate(key)
    )
    false_positives_open = tuple(
        key for key in open_keys if predicate(key)
    )
    false_positives_resolved = tuple(
        key for key in resolved_other if predicate(key)
    )
    result = {
        "candidate": name,
        "exact_claim": statement,
        "entrant_true": sum(predicate(key) for key in entrants),
        "entrant_total": len(entrants),
        "open_nonentrant_true": len(false_positives_open),
        "open_nonentrant_total": len(open_keys),
        "resolved_other_true": len(false_positives_resolved),
        "resolved_other_total": len(resolved_other),
        "selected_count": len(selected),
        "selected_sha256": digest(selected),
        "false_negatives": false_negatives,
        "false_positives_open": false_positives_open,
        "false_positives_resolved": false_positives_resolved,
        "status": (
            "HOLDS_EXACTLY"
            if set(selected) == entrant_set else "FAILS"
        ),
    }
    return result


def entry_predictors(
    family: dict[str, object],
) -> dict[str, object]:
    all_keys = tuple(sorted(family["states"]))
    entrants = tuple(sorted(NINE_KEYS))
    open_keys = tuple(sorted(
        set(all_keys) - RESOLVED_THROUGH_819
    ))
    resolved_other = tuple(sorted(
        RESOLVED_THROUGH_819 - set(NINE_KEYS)
    ))
    predicates: tuple[
        tuple[str, Callable[[Key], bool], str], ...
    ] = (
        (
            "position_spacing_maximal_ring_only",
            lambda key: cyclic_separation(key) == 5,
            "cyclic separation is the maximum value 5 on the 11-ring",
        ),
        (
            "position_pair_arithmetic_event0_gap5or6",
            lambda key: (
                key[0] == 0
                and key[1][1] - key[1][0] in (5, 6)
            ),
            "event=0 and ordinary sorted-position difference is 5 or 6",
        ),
        (
            "event_index_zero_only",
            lambda key: key[0] == 0,
            "event index equals zero",
        ),
        (
            "position_membership_no_origin_maximal",
            lambda key: (
                0 not in key[1] and cyclic_separation(key) == 5
            ),
            "origin is absent and cyclic separation is maximal",
        ),
        (
            "pair_sum_band_with_event",
            lambda key: (
                key[0] == 0 and 7 <= sum(key[1]) <= 15
            ),
            "event=0 and 7<=left+right<=15",
        ),
        (
            "exact_natural_domain_maxsep_event0_no_origin",
            lambda key: (
                key[0] == 0
                and 0 not in key[1]
                and cyclic_separation(key) == 5
            ),
            "event=0, origin absent, and maximum cyclic separation 5",
        ),
        (
            "exact_arithmetic_domain",
            lambda key: (
                key[0] == 0
                and key[1][0] > 0
                and key[1][1] - key[1][0] in (5, 6)
            ),
            "event=0, left>0, and sorted-position difference in {5,6}",
        ),
    )
    rows = tuple(
        predictor_row(
            name, predicate, entrants, open_keys, resolved_other, statement
        )
        for name, predicate, statement in predicates
    )
    spacing_sequence = tuple(
        right - left for _event, (left, right) in entrants
    )
    exact_rows = tuple(
        row["candidate"] for row in rows
        if row["status"] == "HOLDS_EXACTLY"
    )
    failed_rows = tuple(
        row["candidate"] for row in rows
        if row["status"] == "FAILS"
    )
    result = {
        "class_partition": {
            "entrants": entrants,
            "entrant_count": len(entrants),
            "open_nonentrants_count": len(open_keys),
            "open_nonentrants_sha256": digest(open_keys),
            "resolved_other_count": len(resolved_other),
            "resolved_other": resolved_other,
            "partition_exact":
                len(entrants) + len(open_keys) + len(resolved_other)
                == FAMILY_SIZE,
        },
        "alternating_sorted_gap_observation": {
            "sequence": spacing_sequence,
            "equals_5_6_alternation":
                spacing_sequence == (5, 6, 5, 6, 5, 6, 5, 6, 5),
            "predictor_status":
                "FAILS without event=0 and origin-exclusion",
        },
        "candidate_rows": rows,
        "exact_predictors_found": exact_rows,
        "failed_candidates": failed_rows,
        "natural_exact_predictor":
            "event=0 AND origin absent AND cyclic separation=5",
        "scope":
            "exact truth table over nine entrants, 151 open nonentrants, "
            "and 16 other resolved transient/cycle keys",
    }
    result["pass"] = (
        result["class_partition"]["partition_exact"]
        and result[
            "alternating_sorted_gap_observation"
        ]["equals_5_6_alternation"]
        and exact_rows == (
            "exact_natural_domain_maxsep_event0_no_origin",
            "exact_arithmetic_domain",
        )
        and len(failed_rows) == 5
    )
    result["open_keys"] = open_keys
    return result


def residual_wire_indices() -> tuple[int, ...]:
    wires = [K.R3.X.SOURCE_POINTER]
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        wires.extend(base + wire for _name, wire in watched_registers())
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        wires.extend(range(base, base + K.B.LINK_WIDTH))
    return tuple(sorted(set(wires)))


def matching_mask(
    columns: list[int],
    target: tuple[int, ...],
    lane_mask: int,
    signature_wires: tuple[int, ...],
) -> tuple[int, bool]:
    candidates = lane_mask
    for wire in signature_wires:
        candidates &= (
            columns[wire]
            if target[wire]
            else lane_mask ^ (columns[wire] & lane_mask)
        )
        if not candidates:
            return 0, False
    matches = candidates
    for wire, target_bit in enumerate(target):
        matches &= (
            columns[wire]
            if target_bit
            else lane_mask ^ (columns[wire] & lane_mask)
        )
        if not matches:
            break
    return matches, True


def lane_indices(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def checkpoint_distances(
    columns: list[int],
    sstar: tuple[int, ...],
    key_indices: tuple[tuple[Key, int], ...],
) -> tuple[tuple[Key, int], ...]:
    rows = []
    for key, index in key_indices:
        state = un_slice(columns, index)
        rows.append((key, sum(a != b for a, b in zip(state, sstar))))
    return tuple(rows)


def five_step_closure(
    family: dict[str, object],
    sstar: tuple[int, ...],
) -> dict[str, object]:
    rows = []
    clean_images = []
    for positions in family["positions"]:
        current = sstar
        weights = [len(residual_support(current))]
        for _step in range(FIXED_LAG):
            current = K.A.apply_semantic(current, family["words"][positions])
            weights.append(len(residual_support(current)))
        clean = not residual_support(current)
        if clean:
            clean_images.append(current)
        rows.append({
            "positions": positions,
            "support_weights_entry_through_plus5": tuple(weights),
            "nonclean_through_plus4": all(weights[index] > 0 for index in range(5)),
            "clean_at_plus5": clean,
            "image_sha256": state_sha256(current),
        })
    clean_positions = tuple(
        row["positions"] for row in rows if row["clean_at_plus5"]
    )
    expected = tuple(
        positions for positions in family["positions"]
        if positions[0] > 0
    )
    result = {
        "exact_rule":
            "S* is residual-clean at +5 iff the canonical left position >0",
        "fixed_lag": FIXED_LAG,
        "rows": tuple(rows),
        "clean_positions": clean_positions,
        "expected_clean_positions": expected,
        "class_exact": clean_positions == expected,
        "all_clean_images_exact_tuple_equal": (
            bool(clean_images)
            and all(image == clean_images[0] for image in clean_images[1:])
        ),
        "all_left_positive_nonclean_through_plus4": all(
            row["nonclean_through_plus4"]
            for row in rows if row["positions"][0] > 0
        ),
    }
    result["pass"] = (
        result["class_exact"]
        and result["all_clean_images_exact_tuple_equal"]
        and result["all_left_positive_nonclean_through_plus4"]
    )
    return result


def emit_line(
    name: str,
    value: object,
    emitted: list[str],
) -> None:
    line = f"{name}={compact(value)}"
    emitted.append(line)
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def basin_census(
    family: dict[str, object],
    sstar: tuple[int, ...],
    open_keys: tuple[Key, ...],
    emitted: list[str],
) -> dict[str, object]:
    primary_keys = tuple(sorted(family["states"]))
    determinism_keys = open_keys[:DETERMINISM_SLICE_SIZE]
    lanes: tuple[Lane, ...] = (
        tuple((key, "primary") for key in primary_keys)
        + tuple((key, "replay") for key in determinism_keys)
    )
    columns = bit_slice(tuple(
        family["states"][key] for key, _replica in lanes
    ))
    schedule = masked_schedule(family["program"], lanes)
    primary_index = {key: index for index, key in enumerate(primary_keys)}
    open_index_rows = tuple(
        (key, primary_index[key]) for key in open_keys
    )
    primary_mask = (1 << len(primary_keys)) - 1
    open_mask = sum(1 << primary_index[key] for key in open_keys)
    residual_wires = residual_wire_indices()
    active_sstar = tuple(
        index for index, bit in enumerate(sstar) if bit
    )
    spread = tuple(
        sorted(set(
            round(index * (len(sstar) - 1) / 191)
            for index in range(192)
        ))
    )
    signature_wires = tuple(sorted(set(active_sstar + spread)))
    prior_matches = 0
    exact_hits: list[tuple[int, Key]] = []
    open_entries: list[tuple[int, Key]] = []
    full_comparison_times = []
    first_clean: dict[Key, int | None] = {
        key: None for key in open_keys
    }
    checkpoint_rows = []
    determinism_rows = []
    pending: dict[tuple[Key, int], dict[str, object]] = {}
    prediction_verifications = []
    t14739_signature_class: tuple[Key, ...] = ()

    for update in range(TARGET_HORIZON + 1):
        match_bits, full_tested = matching_mask(
            columns, sstar, primary_mask, signature_wires
        )
        if full_tested:
            full_comparison_times.append(update)
        for index in lane_indices(match_bits):
            exact_hits.append((update, primary_keys[index]))
        new_open_bits = (match_bits & open_mask) & ~prior_matches
        for index in lane_indices(new_open_bits):
            key = primary_keys[index]
            open_entries.append((update, key))
            if key[1][0] > 0:
                prediction = {
                    "key": key,
                    "exact_Sstar_entry": update,
                    "predicted_first_clean_moment": update + FIXED_LAG,
                    "selection_lag": FIXED_LAG,
                    "basis":
                        "pre-verified all-word S* left-positive closure",
                    "printed_before_future_verification": True,
                }
                emit_line(
                    "ENTRY_PREDICTION_PREREGISTERED_BEFORE_VERIFICATION",
                    prediction,
                    emitted,
                )
                state = un_slice(columns, index)
                pending[(key, update)] = {
                    **prediction,
                    "support_weights_entry_through_prediction": [
                        len(residual_support(state))
                    ],
                }
        prior_matches = match_bits & open_mask

        dirty_mask = 0
        for wire in residual_wires:
            dirty_mask |= columns[wire]
        clean_mask = open_mask & ~dirty_mask
        for index in lane_indices(clean_mask):
            key = primary_keys[index]
            if first_clean[key] is None:
                first_clean[key] = update

        for (key, entry), row in tuple(pending.items()):
            if entry < update <= entry + FIXED_LAG:
                state = un_slice(columns, primary_index[key])
                row[
                    "support_weights_entry_through_prediction"
                ].append(len(residual_support(state)))
            if update == entry + FIXED_LAG:
                weights = tuple(
                    row["support_weights_entry_through_prediction"]
                )
                verification = {
                    **row,
                    "support_weights_entry_through_prediction": weights,
                    "predicted_moment_clean": weights[-1] == 0,
                    "nonclean_entry_through_plus4":
                        all(value > 0 for value in weights[:-1]),
                    "is_first_clean":
                        first_clean[key] == entry + FIXED_LAG,
                }
                verification["pass"] = (
                    verification["predicted_moment_clean"]
                    and verification["nonclean_entry_through_plus4"]
                    and verification["is_first_clean"]
                )
                prediction_verifications.append(verification)
                del pending[(key, entry)]

        if update in CHECKPOINTS:
            distances = checkpoint_distances(
                columns, sstar, open_index_rows
            )
            distance_values = tuple(distance for _key, distance in distances)
            minimum = min(distance_values)
            checkpoint_rows.append({
                "time": update,
                "metric":
                    "full 5815-bit tuple Hamming distance to exact S*",
                "distances": distances,
                "minimum": minimum,
                "minimum_keys": tuple(
                    key for key, distance in distances
                    if distance == minimum
                ),
                "maximum": max(distance_values),
                "distance_census": tuple(sorted(Counter(
                    distance_values
                ).items())),
                "rows_sha256": digest(distances),
            })
            duplicate_rows = []
            for replay_offset, key in enumerate(determinism_keys):
                first = primary_index[key]
                second = len(primary_keys) + replay_offset
                duplicate_rows.append({
                    "key": key,
                    "exact_tuple_equal":
                        un_slice(columns, first)
                        == un_slice(columns, second),
                })
            determinism_rows.append({
                "time": update,
                "rows": tuple(duplicate_rows),
                "all_exact": all(
                    row["exact_tuple_equal"] for row in duplicate_rows
                ),
            })
        if update == MECHANISM_ENTRY:
            signature = anatomy_signature(sstar)
            t14739_signature_class = tuple(
                key for key in primary_keys
                if anatomy_signature(
                    un_slice(columns, primary_index[key])
                ) == signature
            )

        if update < TARGET_HORIZON:
            apply_masked(columns, schedule)

    unresolved_predictions = tuple({
        **row,
        "support_weights_entry_through_horizon": tuple(
            row["support_weights_entry_through_prediction"]
        ),
        "verification_status": "BEYOND_DECLARED_HORIZON",
    } for row in pending.values())
    new_transients = tuple(sorted(
        (key, moment)
        for key, moment in first_clean.items()
        if moment is not None and moment > 16384
    ))
    old_horizon_violations = tuple(sorted(
        (key, moment)
        for key, moment in first_clean.items()
        if moment is not None and moment <= 16384
    ))
    open_exact_hits = tuple(
        (update, key) for update, key in exact_hits if key in set(open_keys)
    )
    exact_hit_keys_at_entry = tuple(
        key for update, key in exact_hits if update == MECHANISM_ENTRY
    )
    result = {
        "declared_horizon": TARGET_HORIZON,
        "complete_sweep": True,
        "population_scope": {
            "primary_family_keys": len(primary_keys),
            "required_open_keys": len(open_keys),
            "duplicate_determinism_lanes": len(determinism_keys),
            "total_bit_sliced_lanes": len(lanes),
            "masked_gate_rows_per_update": len(schedule),
        },
        "exact_hit_metric": "exact 5815-bit tuple equality to S*",
        "signature_prefilter_wires": len(signature_wires),
        "signature_prefilter_has_no_false_negative":
            "full equality implies signature equality; every candidate is "
            "then checked on all 5815 bits",
        "full_exact_comparison_candidate_times": tuple(full_comparison_times),
        "all_family_exact_hits": tuple(exact_hits),
        "open_151_exact_hits": open_exact_hits,
        "open_151_exact_entries": tuple(open_entries),
        "entry_class_at_t14739": exact_hit_keys_at_entry,
        "entry_class_is_exactly_nine":
            exact_hit_keys_at_entry == tuple(sorted(NINE_KEYS)),
        "anatomy_signature_class_at_t14739": t14739_signature_class,
        "anatomy_signature_class_is_exactly_nine":
            t14739_signature_class == tuple(sorted(NINE_KEYS)),
        "visited_state_key_cells": len(primary_keys) * (
            TARGET_HORIZON + 1
        ),
        "Sstar_exact_hit_cell_count": len(exact_hits),
        "near_approach_checkpoints": tuple(checkpoint_rows),
        "first_clean_after_T16384": new_transients,
        "contradictions_to_151_open_through_T16384":
            old_horizon_violations,
        "prediction_verifications": tuple(prediction_verifications),
        "unverified_beyond_horizon_predictions": unresolved_predictions,
        "determinism_scope": {
            "description":
                "eight duplicate key lanes, exact full-state equality at "
                "every declared checkpoint through T=24576",
            "keys": determinism_keys,
            "rows": tuple(determinism_rows),
            "pass": all(row["all_exact"] for row in determinism_rows),
        },
    }
    result["pass"] = (
        len(open_keys) == 151
        and not old_horizon_violations
        and result["entry_class_is_exactly_nine"]
        and result["anatomy_signature_class_is_exactly_nine"]
        and all(row["pass"] for row in prediction_verifications)
        and result["determinism_scope"]["pass"]
    )
    return result


def moment_formula(
    census: dict[str, object],
    family: dict[str, object],
) -> dict[str, object]:
    hits = census["all_family_exact_hits"]
    entrant_times = tuple(
        (key, update)
        for update, key in hits if key in set(NINE_KEYS)
    )
    unique_first = {}
    for key, update in entrant_times:
        unique_first.setdefault(key, update)
    observed = tuple(
        (key, unique_first.get(key)) for key in sorted(NINE_KEYS)
    )
    affine_obstruction = {
        "candidate":
            "t=a+b*event+c*left+d*right over integer/rational coefficients",
        "same_left_pair":
            ((0, (1, 6)), (0, (1, 7))),
        "same_left_equal_time_forces": "d=0",
        "same_right_pair":
            ((0, (1, 7)), (0, (2, 7))),
        "same_right_equal_time_forces": "c=0",
        "all_event_zero_forces": "b is unidentifiable and contributes zero",
        "remaining_formula": "t=a=14739",
        "remaining_intercept_is_observed_entry":
            MECHANISM_ENTRY,
        "nonconstant_key_structure_formula_exists_in_this_class": False,
    }
    rows = (
        {
            "name": "observed_constant",
            "formula": "t(key)=14739",
            "values": tuple(MECHANISM_ENTRY for _key in NINE_KEYS),
            "reproduces_all_nine": all(
                update == MECHANISM_ENTRY for _key, update in observed
            ),
            "status": "HOLDS_EXACTLY_BUT_CIRCULAR_OBSERVED_INTERCEPT",
        },
        {
            "name": "static_landed_integer_identity",
            "formula": "t=state_bits+period_8928-family_epochs",
            "machine_values": {
                "state_bits": family["summary"]["state_bits"],
                "period_8928": 8928,
                "family_epochs": family["summary"]["epochs"],
                "result":
                    family["summary"]["state_bits"] + 8928
                    - family["summary"]["epochs"],
            },
            "reproduces_all_nine":
                family["summary"]["state_bits"] + 8928
                - family["summary"]["epochs"] == MECHANISM_ENTRY,
            "status":
                "HOLDS_ARITHMETICALLY_NOT_A_CAUSAL_OR_KEY_DERIVATION",
        },
    )
    result = {
        "observed_exact_entry_times": observed,
        "candidate_formula_rows": rows,
        "affine_key_formula_obstruction": affine_obstruction,
        "reproduction_status":
            "HOLDS_EXACTLY only for a constant observed intercept and a "
            "static integer coincidence",
        "derivation_status":
            "GAP_NO_DYNAMICS_DERIVED_MOMENT_FORMULA",
        "honest_gap":
            "the exact domain predicate does not supply an orbit-phase "
            "invariant or recurrence equation fixing 14739; within the "
            "natural affine key class, equal entrant times erase every "
            "nonconstant key coefficient",
        "moment_formula_exact_and_noncircular": False,
    }
    result["pass"] = (
        len(observed) == 9
        and all(update == MECHANISM_ENTRY for _key, update in observed)
        and all(row["reproduces_all_nine"] for row in rows)
        and not result["moment_formula_exact_and_noncircular"]
    )
    return result


def stable_render(
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = [
        *(
            f"CERTIFICATE_{name}={compact(value)}"
            for name, value in certificates.items()
        ),
        f"REPORT={compact(report)}",
    ]
    return "\n".join(lines) + "\n"


def run() -> int:
    started = monotonic()
    emitted: list[str] = []
    emit_line(
        "CYCLE822_SSTAR_BASIN",
        {
            "phase": "START",
            "verification_not_started": True,
            "target_horizon": TARGET_HORIZON,
        },
        emitted,
    )
    sources = source_certificate()
    family = build_family()
    scalar = scalar_equivalence(
        family, tuple(sorted(family["states"]))[:8]
    )
    reconstruction = evolve_sstar_pair(family)
    anatomy = sstar_anatomy(family, reconstruction)
    predictors = entry_predictors(family)
    closure = five_step_closure(family, reconstruction["sstar"])
    preregistration = {
        "printed_before_basin_verification": True,
        "unconditional_new_key_time_predictions": (),
        "reason_no_unconditional_prediction":
            "the exact domain selector contains only the already observed "
            "nine; no noncircular entry-time formula was derived",
        "conditional_falsifiable_rule":
            "if an open key with left_position>0 first enters exact S* at "
            "tau, it is predicted to be first residual-clean at tau+5",
        "conditional_rule_scope":
            "all 44 separated-pair words were checked before the census; "
            "clean at +5 iff left_position>0",
        "known_nine_not_misreported_as_new_predictions": True,
    }
    emit_line("PREDICTION_REGISTRATION", preregistration, emitted)

    census = basin_census(
        family,
        reconstruction["sstar"],
        predictors["open_keys"],
        emitted,
    )
    formula = moment_formula(census, family)
    verdict = {
        "verdict": "BASIN_STRUCTURE_FOUND",
        "domain_predictor_status":
            "EXACT at k=2 scope: event=0, origin absent, maximum cyclic "
            "separation 5",
        "Sstar_structure_status":
            "exact anatomy, exact nine-key t=14739 class, and exact "
            "left-positive five-step closure",
        "moment_formula_status":
            formula["derivation_status"],
        "why_not_DOMAIN_LAW_DERIVED":
            "the exact entry selector is found, but no noncircular dynamics "
            "formula fixes its entry moment",
        "scope":
            "176-key k=2 family; required 151-key open census through "
            f"T={TARGET_HORIZON}",
    }
    verdict["pass"] = (
        predictors["pass"]
        and census["pass"]
        and formula["pass"]
        and closure["pass"]
    )

    elapsed = monotonic() - started
    reconstruction_public = {
        key: value for key, value in reconstruction.items()
        if key != "sstar"
    }
    checks = {
        "A_SSTAR_EXACT_RECONSTRUCTION_AND_ANATOMY":
            reconstruction["pass"] and anatomy["pass"],
        "B_ENTRY_PREDICTOR_EXACT_CANDIDATE_TABLE":
            predictors["pass"],
        "C_BASIN_CENSUS_COMPLETE_AND_PREDICTIONS_VERIFIED":
            census["pass"],
        "D_MOMENT_FORMULA_HONEST_GAP":
            formula["pass"],
        "E_BASIN_STRUCTURE_FOUND_VERDICT":
            verdict["pass"],
        "F_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT": False,
    }
    controls = {
        **sources,
        "family_reimplementation": family["summary"],
        "masked_bit_slice_scalar_equivalence": scalar,
        "sstar_second_trajectory_exact_verification":
            reconstruction["t14739_exact_tuple_equal"],
        "census_determinism": census["determinism_scope"],
        "predictions_printed_before_verification": True,
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes_including_preregistration": 0,
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
        and scalar["pass"]
        and reconstruction["pass"]
        and census["determinism_scope"]["pass"]
        and elapsed < AUDIT_TIMEOUT_SEC
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
    )
    certificates = {
        "A_SSTAR": {
            "reconstruction": reconstruction_public,
            "anatomy": anatomy,
            "five_step_closure": closure,
        },
        "B_ENTRY_PREDICTOR": {
            key: value for key, value in predictors.items()
            if key != "open_keys"
        },
        "C_BASIN_CENSUS": census,
        "D_MOMENT_FORMULA": formula,
        "E_VERDICT": verdict,
        "F_CONTROLS": controls,
    }
    report = {
        "cycle": 822,
        "target": "S* basin and k=2 domain-law attempt",
        "declared_horizon": TARGET_HORIZON,
        "verdict": verdict["verdict"],
        "new_exact_entries": census["open_151_exact_entries"],
        "new_transients": census["first_clean_after_T16384"],
        "moment_formula_status": formula["derivation_status"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE822_SSTAR_BASIN_HONEST_FAIL",
    }
    emitted_bytes = sum(
        len((line + "\n").encode("utf-8")) for line in emitted
    )
    for _iteration in range(8):
        controls["pass"] = controls_base
        checks["F_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
            controls_base
        )
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE822_BASIN_STRUCTURE_FOUND_EXACT_PASS"
            if report["pass"]
            else "CYCLE822_SSTAR_BASIN_HONEST_FAIL"
        )
        output = stable_render(certificates, report)
        total_bytes = emitted_bytes + len(output.encode("utf-8"))
        stdout_ok = total_bytes < STDOUT_LIMIT_BYTES
        controls["stdout_bytes_including_preregistration"] = total_bytes
        controls["pass"] = controls_base and stdout_ok
        checks["F_SHAS_BLOCKLIST_DETERMINISM_RUNTIME_STDOUT"] = (
            controls["pass"]
        )
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE822_BASIN_STRUCTURE_FOUND_EXACT_PASS"
            if report["pass"]
            else "CYCLE822_SSTAR_BASIN_HONEST_FAIL"
        )
        report["stdout_bytes"] = total_bytes
    output = stable_render(certificates, report)
    final_bytes = emitted_bytes + len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        failure = {
            "pass": False,
            "terminal": "CYCLE822_SSTAR_BASIN_HONEST_FAIL",
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
            "terminal": "CYCLE822_SSTAR_BASIN_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }
        sys.stdout.write(compact(failure) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
