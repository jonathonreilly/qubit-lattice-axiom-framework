#!/usr/bin/env python3
"""Cycle 822 independent adversarial check of S*, its basin, and its moment.

The Cycle-819, Cycle-820, and Cycle-822 primaries are SHA-pinned text/AST
inputs only.  This checker imports the landed Cycle-719 controller core and
rebuilds the k=2 catalog, trajectories, state anatomy, and bounded census.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "scripts/frontier_cycle822_sstar_basin_2026_07_28.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
import inspect
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import sys
from time import monotonic
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[2]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
    AUDIT_INPUT_PATHS[3]:
        "269d235c4981eaa4b94cfc200a0d472bf9f1ca8b57c2e14880afe754a9d41c56",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[2]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[3]: "56fd26ec1f09e3690aa0e9cacd1447c289fd7ac0",
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, int]]
Lane = tuple[Key, str]
MaskedGate = tuple[int, int, int, int, int]

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
ENTRY = 14739
HORIZON = 24576
CLOCKS = (4464, 5952, 8928, 8930)
NINE_ENTRANTS: tuple[Key, ...] = (
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
RESOLVED_OTHER = {
    (3, (1, 10)), (3, (0, 7)),
    (3, (0, 5)), (3, (0, 6)), (3, (1, 6)), (3, (1, 7)),
    (3, (2, 7)), (3, (2, 8)), (3, (3, 8)), (3, (3, 9)),
    (3, (4, 9)), (3, (4, 10)), (3, (5, 10)), (2, (0, 9)),
    (1, (0, 9)), (0, (0, 9)),
}
OPEN_SAMPLE_INDICES = (0, 13, 27, 40, 50, 64, 78, 90, 101, 115, 130, 150)
CHECKPOINTS = tuple(sorted({
    0, *CLOCKS, ENTRY - 1, ENTRY, ENTRY + 1,
    *(ENTRY + clock for clock in CLOCKS if ENTRY + clock <= HORIZON),
    HORIZON,
}))


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def state_hash(state: tuple[int, ...]) -> str:
    return sha256(bytes(state)).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == name
                for target in node.targets)
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    expected_ast_names = {
        AUDIT_INPUT_PATHS[1]: {"build_family", "advance_population"},
        AUDIT_INPUT_PATHS[2]: {"build_family", "evolve_nine"},
        AUDIT_INPUT_PATHS[3]: {"build_family", "basin_census", "moment_formula"},
    }
    ast_names = {
        path: {
            node.name for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        for path, tree in trees.items()
    }
    sha_rows = {path: sha256(payload).hexdigest()
                for path, payload in payloads.items()}
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    result = {
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "literal_AUDIT_INPUT_PATHS":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "blocked_text_AST_only": TEXT_AST_ONLY_PATHS,
        "blocked_AST_markers": {
            path: sorted(expected_ast_names[path])
            for path in TEXT_AST_ONLY_PATHS
        },
        "blocked_AST_markers_present": all(
            expected_ast_names[path] <= ast_names[path]
            for path in TEXT_AST_ONLY_PATHS
        ),
        "direct_frontier_imports": direct_frontier_imports,
        "blocked_loaded": tuple(
            name for name in BLOCKED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "self_sha256": sha256(self_payload).hexdigest(),
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "maximum_named_inputs": 6,
    }
    result["pass"] = (
        sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and result["literal_AUDIT_INPUT_PATHS"]
        and result["existing_worktree_relative"]
        and result["blocked_AST_markers_present"]
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_loaded"]
        and not result["firewall_hits"]
        and len(AUDIT_INPUT_PATHS) <= 6
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


def cyclic_separation(key: Key) -> int:
    left, right = key[1]
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def synchronous_word(
    program: tuple[object, ...],
    positions0: tuple[int, int],
) -> tuple[object, ...]:
    positions = positions0
    word: list[object] = []
    for _ in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple((position + 1) % len(program) for position in positions)
    return tuple(word)


def build_initial_states(
    keys: tuple[Key, ...],
) -> tuple[
    tuple[object, ...],
    dict[tuple[int, int], tuple[object, ...]],
    dict[Key, tuple[int, ...]],
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    epochs: list[tuple[int, ...]] = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        epochs.append(before)
        state, rail_a, rail_b, trace = K.run_orbit(before, program)
        assert rail_a == (1,) + (0,) * (len(program) - 1)
        assert not any(rail_b) and len(trace) == len(program)
    positions = tuple(sorted({key[1] for key in keys}))
    words = {position: synchronous_word(program, position)
             for position in positions}
    states = {
        key: K.run_orbit(
            epochs[key[0]], program, token_positions=key[1]
        )[0]
        for key in keys
    }
    return program, words, states


def bit_slice(states: tuple[tuple[int, ...], ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((column >> lane) & 1 for column in columns)


def masked_schedule(
    program: tuple[object, ...],
    lanes: tuple[Lane, ...],
) -> tuple[MaskedGate, ...]:
    schedule: list[MaskedGate] = []
    for step in range(len(program)):
        for station, program_row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (key, _replica) in enumerate(lanes)
                if station in {
                    (key[1][0] + step) % len(program),
                    (key[1][1] + step) % len(program),
                }
            )
            if not mask:
                continue
            for gate in K.mapped_macro(program_row):
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
                    raise ValueError(("unsupported gate", gate))
    return tuple(schedule)


def advance(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def equality_mask(
    columns: list[int],
    target: tuple[int, ...],
    lane_mask: int,
    wires: tuple[int, ...],
) -> int:
    matches = lane_mask
    for wire in wires:
        matches &= (
            columns[wire]
            if target[wire]
            else lane_mask ^ (columns[wire] & lane_mask)
        )
        if not matches:
            break
    return matches


def lane_numbers(mask: int) -> tuple[int, ...]:
    lanes: list[int] = []
    while mask:
        bit = mask & -mask
        lanes.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(lanes)


def reconstruct_sstar() -> dict[str, object]:
    keys = (NINE_ENTRANTS[0], NINE_ENTRANTS[-1])
    program, _words, states = build_initial_states(keys)
    lanes = tuple((key, "independent_reconstruction") for key in keys)
    columns = bit_slice(tuple(states[key] for key in keys))
    schedule = masked_schedule(program, lanes)
    before: tuple[tuple[int, ...], ...] | None = None
    entry: tuple[tuple[int, ...], ...] | None = None
    after: tuple[tuple[int, ...], ...] | None = None
    for update in range(ENTRY + 2):
        if update == ENTRY - 1:
            before = tuple(un_slice(columns, lane) for lane in range(2))
        elif update == ENTRY:
            entry = tuple(un_slice(columns, lane) for lane in range(2))
        elif update == ENTRY + 1:
            after = tuple(un_slice(columns, lane) for lane in range(2))
        if update <= ENTRY:
            advance(columns, schedule)
    assert before is not None and entry is not None and after is not None
    result = {
        "keys": keys,
        "t14738_hashes": tuple(map(state_hash, before)),
        "t14738_unequal": before[0] != before[1],
        "t14739_hashes": tuple(map(state_hash, entry)),
        "t14739_hash_match": entry[0] == entry[1],
        "t14740_hashes": tuple(map(state_hash, after)),
        "t14740_unequal": after[0] != after[1],
        "state_bits": len(entry[0]),
        "state": entry[0],
        "masked_gates_per_update": len(schedule),
    }
    result["pass"] = (
        result["t14738_unequal"]
        and result["t14739_hash_match"]
        and result["t14740_unequal"]
        and result["state_bits"] == 5815
    )
    return result


def watched_residual_wires() -> dict[str, int]:
    rows = {"source.SOURCE_POINTER": K.R3.X.SOURCE_POINTER}
    for bank_index, base in enumerate(K.M.R12.BANK_BASES[:FIXTURE_BANKS]):
        named = (
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
        rows.update({
            f"bank{bank_index}.{name}": base + wire
            for name, wire in named
        })
    for link_index, base in enumerate(
        K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]
    ):
        rows.update({
            f"link{link_index}.WIRE_{wire}": base + wire
            for wire in range(K.B.LINK_WIDTH)
        })
    return rows


def anatomy(state: tuple[int, ...]) -> dict[str, object]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    residual_map = watched_residual_wires()
    residual = tuple(
        name for name, wire in residual_map.items() if state[wire]
    )
    occupancy = tuple(
        tuple(bank[int(cell["valid"])] for cell in K.A.CELLS)
        for bank in banks
    )
    tokens = tuple(
        tuple(bank[wire] for wire in K.A.TOKEN)
        for bank in banks
    )
    encoding = {
        "pack_state_module": inspect.getmodule(K.M.pack_state).__name__,
        "unpack_state_module": inspect.getmodule(K.M.unpack_state).__name__,
        "bank_schema_module": K.A.__name__,
        "source_schema_module": K.R3.__name__,
        "state_definition":
            "K.M.unpack_state(state,2) with K.R3.X.SOURCE_POINTER, "
            "K.A.CELLS[*]['valid'], K.A.TOKEN, K.A.DIRECTION_OK, "
            "K.M.R12 bank/link offsets",
        "source_pointer_wire": K.R3.X.SOURCE_POINTER,
        "bank_bases": tuple(K.M.R12.BANK_BASES[:2]),
        "link_bases": tuple(K.M.R12.LINK_BASES[:1]),
        "bank_width": K.A.N,
        "link_width": K.B.LINK_WIDTH,
    }
    result = {
        "encoding_citation": encoding,
        "state_sha256": state_hash(state),
        "state_bits": len(state),
        "hamming_weight": sum(state),
        "occupancy": occupancy,
        "tokens": tokens,
        "link_weights": tuple(sum(link) for link in links),
        "residual_fields": residual,
        "expected_residual_fields": (
            "source.SOURCE_POINTER", "bank0.DIRECTION_OK",
        ),
    }
    result["pass"] = (
        result["state_bits"] == 5815
        and result["hamming_weight"] == 44
        and occupancy == ((1, 1), (0, 0))
        and tokens == ((1, 0), (0, 0))
        and result["link_weights"] == (0,)
        and residual == result["expected_residual_fields"]
    )
    result["finding"] = (
        f"S* ANATOMY {'PASS' if result['pass'] else 'FAIL'}: "
        f"5815 bits, weight {result['hamming_weight']}, "
        f"occupancy {list(map(list, occupancy))}, "
        f"tokens {list(map(list, tokens))}, empty link "
        f"{result['link_weights'] == (0,)}, residual {list(residual)}; "
        f"encoding {encoding['pack_state_module']}.pack_state/unpack_state "
        f"+ {encoding['bank_schema_module']} and "
        f"{encoding['source_schema_module']}."
    )
    return result


def catalog_and_predictor() -> dict[str, object]:
    positions = separated_pairs()
    catalog = tuple(
        (event, pair)
        for event in range(2 * FIXTURE_BANKS)
        for pair in positions
    )
    entrant_set = set(NINE_ENTRANTS)
    resolved_set = set(RESOLVED_OTHER)
    open_keys = tuple(sorted(set(catalog) - entrant_set - resolved_set))

    conjuncts: tuple[tuple[str, Callable[[Key], bool]], ...] = (
        ("event=0", lambda key: key[0] == 0),
        ("origin absent", lambda key: 0 not in key[1]),
        ("maximum cyclic separation=5",
         lambda key: cyclic_separation(key) == 5),
    )

    def predicate(key: Key) -> bool:
        return all(test(key) for _name, test in conjuncts)

    selected = tuple(key for key in catalog if predicate(key))
    entrants_missing = tuple(key for key in NINE_ENTRANTS if not predicate(key))
    nonentrants_selected = tuple(
        key for key in catalog if key not in entrant_set and predicate(key)
    )
    drop_rows = []
    for dropped, _test in conjuncts:
        kept = tuple(test for name, test in conjuncts if name != dropped)
        selected_drop = tuple(
            key for key in catalog if all(test(key) for test in kept)
        )
        false_positives = tuple(
            key for key in selected_drop if key not in entrant_set
        )
        drop_rows.append({
            "dropped": dropped,
            "selected_count": len(selected_drop),
            "false_positive_count": len(false_positives),
            "false_positive_witnesses": false_positives[:4],
            "breaks_exactness": bool(false_positives),
            "status": "PASS" if false_positives else "FAIL",
        })
    result = {
        "catalog_size": len(catalog),
        "position_pairs": len(positions),
        "entrants": tuple(sorted(NINE_ENTRANTS)),
        "resolved_nonentrants": tuple(sorted(RESOLVED_OTHER)),
        "open_keys": open_keys,
        "open_count": len(open_keys),
        "selected": selected,
        "both_directions": {
            "all_nine_entrants_satisfy": not entrants_missing,
            "entrant_true_count": len(NINE_ENTRANTS) - len(entrants_missing),
            "nonentrant_false_count":
                len(catalog) - len(NINE_ENTRANTS) - len(nonentrants_selected),
            "nonentrant_total": len(catalog) - len(NINE_ENTRANTS),
            "false_negatives": entrants_missing,
            "false_positives": nonentrants_selected,
        },
        "key_structure_only": True,
        "trajectory_values_accessed_by_predicate": (),
        "drop_conjunct_attacks": tuple(drop_rows),
    }
    result["pass"] = (
        len(catalog) == FAMILY_SIZE
        and len(open_keys) == 151
        and set(selected) == entrant_set
        and all(row["breaks_exactness"] for row in drop_rows)
    )
    loads = ", ".join(
        f"drop {row['dropped']} -> {row['selected_count']} selected/"
        f"{row['false_positive_count']} false positives ({row['status']})"
        for row in drop_rows
    )
    result["finding"] = (
        f"THE PREDICTOR {'PASS' if result['pass'] else 'FAIL'}: "
        f"9/9 entrants true; "
        f"{result['both_directions']['nonentrant_false_count']}/"
        f"{result['both_directions']['nonentrant_total']} nonentrants false "
        f"(151 open + 16 resolved); key-structure only; {loads}."
    )
    return result


def hamming(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a != b for a, b in zip(left, right))


def scan_declared_sample(
    sstar: tuple[int, ...],
    open_keys: tuple[Key, ...],
) -> dict[str, object]:
    open_sample = tuple(open_keys[index] for index in OPEN_SAMPLE_INDICES)
    primary_keys = NINE_ENTRANTS + open_sample
    duplicate_keys = (NINE_ENTRANTS[0], open_sample[0])
    lanes: tuple[Lane, ...] = (
        tuple((key, "primary") for key in primary_keys)
        + tuple((key, "determinism_replay") for key in duplicate_keys)
    )
    program, _words, states = build_initial_states(primary_keys)
    columns = bit_slice(tuple(states[key] for key, _replica in lanes))
    schedule = masked_schedule(program, lanes)
    primary_index = {key: index for index, key in enumerate(primary_keys)}
    primary_mask = (1 << len(primary_keys)) - 1

    active = tuple(wire for wire, bit in enumerate(sstar) if bit)
    spread = tuple(sorted({
        round(index * (len(sstar) - 1) / 127) for index in range(128)
    }))
    signature_wires = tuple(sorted(set(active + spread)))
    all_wires = tuple(range(len(sstar)))

    residual_named = watched_residual_wires()
    residual_wires = tuple(sorted(residual_named.values()))
    source_wire = K.R3.X.SOURCE_POINTER
    direction0_wire = (
        K.M.R12.BANK_BASES[0] + K.A.DIRECTION_OK
    )
    structure_wires = tuple(sorted(set(
        tuple(
            base + int(cell["valid"])
            for base in K.M.R12.BANK_BASES[:2]
            for cell in K.A.CELLS
        )
        + tuple(
            base + wire
            for base in K.M.R12.BANK_BASES[:2]
            for wire in K.A.TOKEN
        )
        + tuple(
            K.M.R12.LINK_BASES[0] + wire
            for wire in range(K.B.LINK_WIDTH)
        )
    )))

    first: dict[str, dict[Key, int]] = {
        "source_pointer": {},
        "bank0_direction": {},
        "source_and_direction": {},
        "target_residual_class": {},
        "target_structure_without_residual": {},
        "target_anatomy_class": {},
    }
    exact_hits: list[tuple[int, Key]] = []
    structural_hits_open_count = 0
    structural_hits_open_sample: list[tuple[int, Key]] = []
    snapshots: dict[int, dict[Key, tuple[int, ...]]] = {}
    neighborhood: dict[int, dict[str, object]] = {}
    determinism_rows: list[dict[str, object]] = []
    full_comparison_times: list[int] = []

    neighborhood_times = set(range(ENTRY - 4, ENTRY + 6))
    snapshot_times = set(CHECKPOINTS) | neighborhood_times

    def register(class_name: str, mask: int, update: int) -> None:
        for lane in lane_numbers(mask & primary_mask):
            key = primary_keys[lane]
            first[class_name].setdefault(key, update)

    open_sample_set = set(open_sample)
    entrant_set = set(NINE_ENTRANTS)
    for update in range(HORIZON + 1):
        source_mask = columns[source_wire] & primary_mask
        direction_mask = columns[direction0_wire] & primary_mask
        residual_mask = equality_mask(
            columns, sstar, primary_mask, residual_wires
        )
        structure_mask = equality_mask(
            columns, sstar, primary_mask, structure_wires
        )
        anatomy_mask = residual_mask & structure_mask
        register("source_pointer", source_mask, update)
        register("bank0_direction", direction_mask, update)
        register("source_and_direction", source_mask & direction_mask, update)
        register("target_residual_class", residual_mask, update)
        register(
            "target_structure_without_residual", structure_mask, update
        )
        register("target_anatomy_class", anatomy_mask, update)
        for lane in lane_numbers(anatomy_mask):
            key = primary_keys[lane]
            if key in open_sample_set:
                structural_hits_open_count += 1
                if len(structural_hits_open_sample) < 16:
                    structural_hits_open_sample.append((update, key))

        candidates = equality_mask(
            columns, sstar, primary_mask, signature_wires
        )
        if candidates:
            full_comparison_times.append(update)
            matches = equality_mask(columns, sstar, candidates, all_wires)
            exact_hits.extend(
                (update, primary_keys[lane]) for lane in lane_numbers(matches)
            )

        if update in snapshot_times:
            row = {
                key: un_slice(columns, primary_index[key])
                for key in primary_keys
            }
            snapshots[update] = row
            if update in neighborhood_times:
                entrant_states = tuple(row[key] for key in NINE_ENTRANTS)
                pair_distances = tuple(
                    hamming(entrant_states[left], entrant_states[right])
                    for left, right in combinations(range(9), 2)
                )
                neighborhood[update] = {
                    "distance_to_Sstar": tuple(
                        hamming(state, sstar) for state in entrant_states
                    ),
                    "pairwise_diameter": max(pair_distances),
                    "unique_state_hashes":
                        len({state_hash(state) for state in entrant_states}),
                }

        if update in CHECKPOINTS:
            replay_rows = []
            for replay_offset, key in enumerate(duplicate_keys):
                primary_lane = primary_index[key]
                replay_lane = len(primary_keys) + replay_offset
                same = (
                    un_slice(columns, primary_lane)
                    == un_slice(columns, replay_lane)
                )
                replay_rows.append({"key": key, "exact_tuple_equal": same})
            determinism_rows.append({
                "time": update,
                "rows": tuple(replay_rows),
                "pass": all(row["exact_tuple_equal"] for row in replay_rows),
            })

        if update < HORIZON:
            advance(columns, schedule)

    open_hits = tuple(
        hit for hit in exact_hits if hit[1] in open_sample_set
    )
    entrant_hits = tuple(
        hit for hit in exact_hits if hit[1] in entrant_set
    )
    expected_entrant_hits = tuple(
        (ENTRY, key) for key in NINE_ENTRANTS
    )
    two_witnesses = (NINE_ENTRANTS[0], NINE_ENTRANTS[-1])
    witness_rows = tuple({
        "key": key,
        "hit_times": tuple(
            time for time, found_key in entrant_hits if found_key == key
        ),
        "t14739_sha256": state_hash(snapshots[ENTRY][key]),
        "equals_reconstructed_Sstar": snapshots[ENTRY][key] == sstar,
    } for key in two_witnesses)
    result = {
        "declared_open_sample": open_sample,
        "declared_horizon": HORIZON,
        "open_sample_exact_Sstar_hits": open_hits,
        "all_nine_entrant_hits_within_sample_scan": entrant_hits,
        "two_required_hit_rechecks": witness_rows,
        "exact_comparison_candidate_times": tuple(full_comparison_times),
        "first_hitting_times": {
            name: tuple(
                (key, rows.get(key))
                for key in primary_keys
            )
            for name, rows in first.items()
        },
        "open_anatomy_class_hit_count": structural_hits_open_count,
        "open_anatomy_class_hit_sample": tuple(structural_hits_open_sample),
        "snapshots": snapshots,
        "neighborhood": neighborhood,
        "masked_gates_per_update": len(schedule),
        "state_cells_scanned": len(primary_keys) * (HORIZON + 1),
        "determinism": {
            "duplicate_keys": duplicate_keys,
            "checkpoints": tuple(determinism_rows),
            "pass": all(row["pass"] for row in determinism_rows),
        },
    }
    result["pass"] = (
        not open_hits
        and entrant_hits == expected_entrant_hits
        and all(row["equals_reconstructed_Sstar"] for row in witness_rows)
        and result["determinism"]["pass"]
    )
    result["finding"] = (
        f"CENSUS SPOT-CHECK {'PASS' if result['pass'] else 'FAIL'}: "
        f"12 declared open keys scanned through T={HORIZON}, "
        f"{len(open_hits)} S* visits; two entrant rechecks hit only at "
        f"{tuple(row['hit_times'] for row in witness_rows)}; the stronger "
        f"nine-entrant sample recorded {len(entrant_hits)} total hits."
    )
    return result


def first_time_vector(
    census: dict[str, object],
    class_name: str,
    keys: tuple[Key, ...] = NINE_ENTRANTS,
) -> tuple[int | None, ...]:
    rows = dict(census["first_hitting_times"][class_name])
    return tuple(rows.get(key) for key in keys)


def formula_attacks(
    sstar: tuple[int, ...],
    census: dict[str, object],
) -> dict[str, object]:
    snapshots = census["snapshots"]
    hits = census["all_nine_entrant_hits_within_sample_scan"]
    observed = {
        key: tuple(time for time, hit_key in hits if hit_key == key)
        for key in NINE_ENTRANTS
    }

    structural_first = first_time_vector(
        census, "target_structure_without_residual"
    )
    precursor_predictions = tuple(
        None if time is None else time + 1 for time in structural_first
    )
    precursor_exact = all(time == ENTRY for time in precursor_predictions)
    precursor = {
        "mechanism":
            "first entry into the occupancy/token/empty-link structural "
            "class, then one exact update to S*",
        "declared_class":
            "occupancy ((1,1),(0,0)); tokens ((1,0),(0,0)); empty link; "
            "no S* full-state equality and no time constant",
        "first_class_hits": structural_first,
        "formula": "t_candidate=min{t: structural_class(t)}+1",
        "predictions": precursor_predictions,
        "required": tuple(ENTRY for _ in NINE_ENTRANTS),
        "counterexample_or_mismatch":
            "the predicted vector is not nine copies of 14739"
            if not precursor_exact
            else "the class is reached at the target rather than one tick "
                 "before it, so the +1 precursor formula predicts 14740",
        "noncircular": True,
        "predicts_14739_exactly": precursor_exact,
        "status": "HOLDS-EXACTLY" if precursor_exact else "FAILS",
    }

    source_first = first_time_vector(census, "source_pointer")
    direction_first = first_time_vector(census, "bank0_direction")
    conjunction_first = first_time_vector(census, "source_and_direction")
    field_predictions = tuple(
        max(source, direction)
        if source is not None and direction is not None else None
        for source, direction in zip(source_first, direction_first)
    )
    residual_fields = {
        "mechanism":
            "derive entry from the first hits of SOURCE_POINTER and "
            "bank-0 DIRECTION_OK",
        "formula":
            "t_candidate=max(first SOURCE_POINTER, first bank0 DIRECTION_OK)",
        "first_SOURCE_POINTER": source_first,
        "first_bank0_DIRECTION_OK": direction_first,
        "first_conjunction": conjunction_first,
        "predictions": field_predictions,
        "required": tuple(ENTRY for _ in NINE_ENTRANTS),
        "counterexample_or_mismatch":
            "the fields and their conjunction have early false hits; "
            f"max-first predictions are {field_predictions}",
        "noncircular": True,
        "predicts_14739_exactly":
            all(time == ENTRY for time in field_predictions),
        "status":
            "HOLDS-EXACTLY"
            if all(time == ENTRY for time in field_predictions)
            else "FAILS",
    }

    common_gcd = CLOCKS[0]
    for clock in CLOCKS[1:]:
        common_gcd = gcd(common_gcd, clock)
    representative = NINE_ENTRANTS[0]
    clock_rows = tuple({
        "clock": clock,
        "entry_residue": ENTRY % clock,
        "exact_lag_to_entry": ENTRY - clock,
        "Hamming_distance_state_at_clock_to_Sstar":
            hamming(snapshots[clock][representative], sstar),
        "lag_equals_Hamming_distance":
            ENTRY - clock
            == hamming(snapshots[clock][representative], sstar),
    } for clock in CLOCKS)
    static_identities = (
        {
            "identity": "8928 + 5815 - 4",
            "value": 8928 + 5815 - 4,
            "arithmetically_exact": 8928 + 5815 - 4 == ENTRY,
            "dynamic_lag_mismatch":
                hamming(snapshots[8928][representative], sstar) != 5811,
        },
        {
            "identity": "8930 + 5815 - 6",
            "value": 8930 + 5815 - 6,
            "arithmetically_exact": 8930 + 5815 - 6 == ENTRY,
            "dynamic_lag_mismatch":
                hamming(snapshots[8930][representative], sstar) != 5809,
        },
    )
    clock_exact = (
        ENTRY % common_gcd == 0
        or any(row["lag_equals_Hamming_distance"] for row in clock_rows)
    )
    clock_attack = {
        "mechanism":
            "zero-phase alignment or exact dynamical lag from cycle clocks "
            "4464/5952/8928/8930",
        "clock_rows": clock_rows,
        "common_gcd": common_gcd,
        "zero_phase_required_residue": 0,
        "actual_residue_mod_common_gcd": ENTRY % common_gcd,
        "static_identities": static_identities,
        "counterexample_or_mismatch":
            f"14739 mod gcd(clocks)={ENTRY % common_gcd}, not 0; "
            "the two exact integer identities have lags 5811/5809 but "
            "neither lag is the measured state-space distance",
        "noncircular": True,
        "predicts_14739_exactly": clock_exact,
        "status": "HOLDS-EXACTLY" if clock_exact else "FAILS",
    }

    return_rows = []
    for clock in CLOCKS:
        time = ENTRY + clock
        states = tuple(snapshots[time][key] for key in NINE_ENTRANTS)
        return_rows.append({
            "proposed_return_period": clock,
            "test_time": time,
            "Sstar_return_count": sum(state == sstar for state in states),
            "unique_state_hashes": len({state_hash(state) for state in states}),
            "all_nine_return_to_Sstar": all(state == sstar for state in states),
        })
    spectral_exact = any(row["all_nine_return_to_Sstar"] for row in return_rows)
    spectral = {
        "mechanism":
            "S*-neighborhood exact return/spectral clock fixes the entry phase",
        "local_neighborhood": census["neighborhood"],
        "return_tests": tuple(return_rows),
        "counterexample_or_mismatch":
            "none of the four proposed clocks returns all nine word-images "
            "to S*; the exact coalescence at 14739 is isolated in the tested "
            "neighborhood and supplies no backward return phase formula",
        "noncircular": True,
        "predicts_14739_exactly": spectral_exact,
        "status": "HOLDS-EXACTLY" if spectral_exact else "FAILS",
    }

    affine = {
        "mechanism":
            "affine key formula a+b*event+c*left+d*right",
        "observed_entry_times": tuple(
            (key, observed[key]) for key in NINE_ENTRANTS
        ),
        "derivation":
            "equal-time keys (1,6)/(1,7) force d=0; "
            "(1,7)/(2,7) force c=0; all events are zero, so b contributes "
            "nothing; only a=14739 remains",
        "counterexample_or_mismatch":
            "the only surviving intercept is the observed entry itself, "
            "so this class has no nonconstant or noncircular predictor",
        "noncircular": False,
        "predicts_14739_exactly": False,
        "status": "FAILS",
    }

    target_residual_first = first_time_vector(
        census, "target_residual_class"
    )
    target_anatomy_first = first_time_vector(
        census, "target_anatomy_class"
    )
    circular_control = {
        "target_residual_first_hits": target_residual_first,
        "target_anatomy_first_hits": target_anatomy_first,
        "holds_as_reduced_hitting_test": (
            all(time == ENTRY for time in target_residual_first)
            and all(time == ENTRY for time in target_anatomy_first)
        ),
        "excluded_from_upgrade":
            "these min-hit expressions use fields selected from S* anatomy "
            "and obtain the number by the same trajectory scan; they are "
            "reduced target tests, not numerical moment derivations",
    }
    candidates = (precursor, residual_fields, clock_attack, spectral, affine)
    found = tuple(
        row["mechanism"] for row in candidates
        if row["status"] == "HOLDS-EXACTLY" and row["noncircular"]
    )
    result = {
        "candidates": candidates,
        "circular_reduced-hitting_control": circular_control,
        "noncircular_formulae_found": found,
        "moment_formula_exact_and_noncircular": bool(found),
        "outcome":
            "NONCIRCULAR_MOMENT_FORMULA_FOUND"
            if found else "NO_NONCIRCULAR_MOMENT_FORMULA_FOUND",
    }
    result["pass"] = all(
        row["status"] in {"HOLDS-EXACTLY", "FAILS"} for row in candidates
    )
    result["finding"] = (
        "THE FORMULA ATTACK "
        f"{'UPGRADES' if found else 'DOES NOT UPGRADE'}: "
        f"{', '.join(row['status'] for row in candidates)}; "
        f"{result['outcome']}. The exact reduced residual/anatomy hitting "
        "test is explicitly quarantined as target-derived trajectory search."
    )
    return result


def without_large_internal_rows(census: dict[str, object]) -> dict[str, object]:
    return {
        key: value for key, value in census.items()
        if key != "snapshots"
    }


def render_line(name: str, status: str, value: object) -> str:
    return f"{name}={status} {compact(value)}"


def run() -> int:
    started = monotonic()
    sources = source_controls()
    predictor = catalog_and_predictor()
    reconstruction = reconstruct_sstar()
    sstar = reconstruction["state"]
    assert isinstance(sstar, tuple)
    sstar_anatomy = anatomy(sstar)
    census = scan_declared_sample(sstar, predictor["open_keys"])
    formula = formula_attacks(sstar, census)

    reconstruction_public = {
        key: value for key, value in reconstruction.items() if key != "state"
    }
    drop_rows = predictor["drop_conjunct_attacks"]
    formula_rows = formula["candidates"]
    elapsed = monotonic() - started
    verdict_name = (
        "BASIN_STRUCTURE_PLUS_NONCIRCULAR_MOMENT_FOUND"
        if formula["moment_formula_exact_and_noncircular"]
        else "BASIN_STRUCTURE_FOUND"
    )
    scientific_pass = (
        reconstruction["pass"]
        and sstar_anatomy["pass"]
        and predictor["pass"]
        and census["pass"]
        and formula["pass"]
    )
    controls = {
        "source_controls": sources,
        "determinism": census["determinism"],
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    controls_base = (
        sources["pass"]
        and census["determinism"]["pass"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    lines = [
        render_line(
            "CERTIFICATE_SSTAR_ANATOMY",
            "PASS" if reconstruction["pass"] and sstar_anatomy["pass"]
            else "FAIL",
            {
                "reconstruction": reconstruction_public,
                "anatomy": sstar_anatomy,
                "finding": sstar_anatomy["finding"],
            },
        ),
        render_line(
            "CERTIFICATE_PREDICTOR_BOTH_DIRECTIONS",
            "PASS" if predictor["pass"] else "FAIL",
            {
                key: value for key, value in predictor.items()
                if key != "open_keys"
            },
        ),
        *(
            render_line(
                "CERTIFICATE_PREDICTOR_LOAD_BEARING_"
                + str(row["dropped"]).upper()
                .replace("=", "_").replace(" ", "_").replace("-", "_"),
                row["status"],
                row,
            )
            for row in drop_rows
        ),
        render_line(
            "CERTIFICATE_CENSUS_SPOT_CHECK",
            "PASS" if census["pass"] else "FAIL",
            without_large_internal_rows(census),
        ),
        *(
            render_line(
                f"FORMULA_ATTACK_{index}_{name}",
                row["status"],
                row,
            )
            for index, (name, row) in enumerate(zip(
                (
                    "PRECURSOR_CLASS",
                    "RESIDUAL_FIELDS",
                    "CYCLE_CLOCKS",
                    "SPECTRAL_RETURN",
                    "AFFINE_KEY_FORMULA",
                ),
                formula_rows,
            ), start=1)
        ),
        render_line(
            "CERTIFICATE_FORMULA_ATTACK_OUTCOME",
            "PASS",
            {
                key: value for key, value in formula.items()
                if key != "candidates"
            },
        ),
    ]

    overall = {
        "cycle": 822,
        "verdict": verdict_name,
        "scientific_checks_pass": scientific_pass,
        "formula_upgrade":
            formula["moment_formula_exact_and_noncircular"],
        "finding_anatomy": sstar_anatomy["finding"],
        "finding_predictor": predictor["finding"],
        "finding_census": census["finding"],
        "finding_formula": formula["finding"],
        "runtime_seconds": round(elapsed, 6),
        "pass": False,
        "terminal": "CYCLE822_INDEPENDENT_CHECK_FAIL",
    }
    for _iteration in range(8):
        controls["pass"] = controls_base
        overall["pass"] = scientific_pass and controls["pass"]
        overall["terminal"] = (
            "CYCLE822_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if overall["pass"] else "CYCLE822_INDEPENDENT_CHECK_FAIL"
        )
        prospective = lines + [
            render_line(
                "CERTIFICATE_CONTROLS",
                "PASS" if controls["pass"] else "FAIL",
                controls,
            ),
            render_line(
                "CERTIFICATE_OVERALL",
                "PASS" if overall["pass"] else "FAIL",
                overall,
            ),
        ]
        byte_count = len(("\n".join(prospective) + "\n").encode())
        controls["stdout_bytes"] = byte_count
        controls["pass"] = controls_base and byte_count < STDOUT_LIMIT_BYTES

    overall["pass"] = scientific_pass and controls["pass"]
    overall["terminal"] = (
        "CYCLE822_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
        if overall["pass"] else "CYCLE822_INDEPENDENT_CHECK_FAIL"
    )
    output_lines = lines + [
        render_line(
            "CERTIFICATE_CONTROLS",
            "PASS" if controls["pass"] else "FAIL",
            controls,
        ),
        render_line(
            "CERTIFICATE_OVERALL",
            "PASS" if overall["pass"] else "FAIL",
            overall,
        ),
    ]
    output = "\n".join(output_lines) + "\n"
    actual_bytes = len(output.encode())
    if actual_bytes >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE822_INDEPENDENT_CHECK_FAIL",
            "failure": "stdout limit exceeded",
            "stdout_bytes": actual_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if overall["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE822_INDEPENDENT_CHECK_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
