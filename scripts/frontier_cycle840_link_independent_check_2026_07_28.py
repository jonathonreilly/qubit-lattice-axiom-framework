#!/usr/bin/env python3
"""Independent adversarial check of Cycle 840 v2's representation claim.

The Cycle-840 and Cycle-839 primaries are BLOCKLISTED: they are read only as
text/AST and are never imported or executed.  The Boolean census is rebuilt
from the SHA-pinned Cycle-830 literal fixture with a separately written
station-mask engine.  The v1 minimality and stability attacks are retained:
v2 passes only by adopting their exact witness and reduction.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle840_missing_link_2026_07_28.py",
)

import ast
import base64
from collections import defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_840 = AUDIT_INPUT_PATHS[1]
PRIMARY_839 = "scripts/frontier_cycle839_meeting_derivation_2026_07_28.py"
FIXTURE_830 = "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py"
PIN_839 = "863c268dd1"
PIN_830 = "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744"

EXPECTED_WORKTREE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "6b87eea4bf26e3c261b84597512d2177406c5875a8c0b6ad5af549f208fd7f19",
}
EXPECTED_WORKTREE_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "0b7375692320b50b68516af61ecbc53526f47145",
}
EXPECTED_HISTORICAL = {
    (PIN_839, PRIMARY_839): (
        "bba2ce68e34bb6c502681c201ba83666e9f674aea2606ced4e3f894fdadfe4fa",
        "9289962e4cdd24732a9c5d1ea53b360d236948f8",
    ),
    (PIN_830, FIXTURE_830): (
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
        "98b1571228ad0902301b6853208ef249ea2c2973",
    ),
}

RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
DISCRIMINATOR_SEARCH_SCOPE = (0, 172)
SEARCH_TICKS = 14739 * RING_STATIONS
EXPECTED_DISCRIMINATOR_WIRES = (40, 81, 105)
EXPECTED_DISCRIMINATOR_PATTERNS = (
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 0),
)
EXPECTED_REPRESENTATION_FUNCTION = (
    "event==0 AND origin_member==False AND separation==5"
)
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_TARGET_RAW_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]


class _BlockedPrimaryFinder(importlib.abc.MetaPathFinder):
    """Fail closed if either 840 or 839 is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        blocked = {Path(PRIMARY_840).stem, Path(PRIMARY_839).stem}
        if fullname.rsplit(".", 1)[-1] in blocked:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _BlockedPrimaryFinder()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        timeout=30,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode().strip()


def blob_sha(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def literal(tree: ast.Module, name: str) -> object | None:
    nodes = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            nodes.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            nodes.append(node.value)
    if len(nodes) != 1:
        return None
    try:
        return ast.literal_eval(nodes[0])
    except (TypeError, ValueError):
        return None


def source_controls() -> tuple[dict[str, object], ast.Module, ast.Module]:
    worktree_payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    primary_tree = ast.parse(
        worktree_payloads[PRIMARY_840], filename=PRIMARY_840
    )
    controller_tree = ast.parse(
        worktree_payloads[AUDIT_INPUT_PATHS[0]],
        filename=AUDIT_INPUT_PATHS[0],
    )
    historical_payloads = {
        (commit, path): git_bytes("show", f"{commit}:{path}")
        for commit, path in EXPECTED_HISTORICAL
    }
    historical_trees = {
        key: ast.parse(payload, filename=f"{key[0]}:{key[1]}")
        for key, payload in historical_payloads.items()
    }
    worktree_rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": (
            "TEXT_AST_ONLY_BLOCKLISTED"
            if path == PRIMARY_840 else "TEXT_AST_PROVENANCE_ONLY"
        ),
        "sha256": sha256(payload).hexdigest(),
        "expected_sha256": EXPECTED_WORKTREE_SHA256[path],
        "git_blob": blob_sha(payload),
        "expected_git_blob": EXPECTED_WORKTREE_BLOBS[path],
        "exact": (
            sha256(payload).hexdigest() == EXPECTED_WORKTREE_SHA256[path]
            and blob_sha(payload) == EXPECTED_WORKTREE_BLOBS[path]
        ),
    } for path, payload in worktree_payloads.items())
    historical_rows = tuple({
        "spec": f"{commit}:{path}",
        "access": (
            "PINNED_TEXT_AST_ONLY_BLOCKLISTED"
            if path == PRIMARY_839 else "PINNED_LITERAL_FIXTURE_TEXT_AST_ONLY"
        ),
        "sha256": sha256(payload).hexdigest(),
        "expected_sha256": EXPECTED_HISTORICAL[(commit, path)][0],
        "git_blob": git_text("rev-parse", f"{commit}:{path}"),
        "expected_git_blob": EXPECTED_HISTORICAL[(commit, path)][1],
        "exact": (
            sha256(payload).hexdigest()
            == EXPECTED_HISTORICAL[(commit, path)][0]
            and git_text("rev-parse", f"{commit}:{path}")
            == EXPECTED_HISTORICAL[(commit, path)][1]
        ),
    } for (commit, path), payload in historical_payloads.items())
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    direct_imports = tuple(sorted({
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in self_tree.body
        if isinstance(node, ast.ImportFrom)
        and node.module != "__future__"
    }))
    expected_stdlib = (
        "ast", "base64", "collections", "hashlib", "importlib.abc",
        "itertools", "json", "pathlib", "struct", "subprocess", "sys",
        "time", "zlib",
    )
    controller_functions = {
        node.name for node in controller_tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    controller_strings = {
        node.value for node in ast.walk(controller_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    primary_functions = {
        node.name for node in primary_tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    fixture_tree = historical_trees[(PIN_830, FIXTURE_830)]
    ast_provenance = {
        "Cycle719_mapped_macro_landed":
            "mapped_macro" in controller_functions,
        "Cycle719_source_bank_program_labels":
            {"source", "bank"} <= controller_strings,
        "Cycle830_state_bit_ordinal_surface_landed":
            literal(fixture_tree, "STATE_BITS") == STATE_BITS,
        "Cycle830_literal_fixture_landed": all(
            isinstance(literal(fixture_tree, name), str)
            for name in (
                "GATE_CONSTANTS_B85",
                "FAMILY_STATES_B85",
                "SSTAR_PACKED_B85",
            )
        ),
        "Cycle840_v2_functions_present": {
            "discriminator_pattern",
            "discriminator_d",
            "reconstruct_minimal_discriminator",
            "certificate_b_representation",
        } <= primary_functions,
        "Cycle840_v2_literals_exact": (
            literal(primary_tree, "DISCRIMINATOR_SEARCH_SCOPE")
            == DISCRIMINATOR_SEARCH_SCOPE
            and literal(primary_tree, "EXPECTED_DISCRIMINATOR_WIRES")
            == EXPECTED_DISCRIMINATOR_WIRES
            and literal(primary_tree, "EXPECTED_DISCRIMINATOR_PATTERNS")
            == EXPECTED_DISCRIMINATOR_PATTERNS
            and literal(primary_tree, "EXPECTED_REPRESENTATION_FUNCTION")
            == EXPECTED_REPRESENTATION_FUNCTION
            and literal(primary_tree, "V1_LINK_FRAMING_RETRACTED") is True
            and literal(primary_tree, "CAUSAL_MECHANISM_CLAIMED") is False
        ),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "read_cap": 6,
        "source_primary_count": (
            len(worktree_rows) + len(historical_rows)
        ),
        "worktree_rows": worktree_rows,
        "historical_rows": historical_rows,
        "all_literal_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in worktree_rows
        ),
        "direct_imports": direct_imports,
        "expected_stdlib": expected_stdlib,
        "stdlib_only": direct_imports == expected_stdlib,
        "AST_provenance": ast_provenance,
        "blocked_modules_loaded_at_start": tuple(sorted(
            name for name in sys.modules
            if name.rsplit(".", 1)[-1]
            in {Path(PRIMARY_840).stem, Path(PRIMARY_839).stem}
        )),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["source_primary_count"] <= result["read_cap"]
        and result["all_literal_paths_existing_worktree_relative"]
        and all(row["exact"] for row in worktree_rows)
        and all(row["exact"] for row in historical_rows)
        and ast_provenance["Cycle719_mapped_macro_landed"]
        and ast_provenance["Cycle719_source_bank_program_labels"]
        and ast_provenance[
            "Cycle830_state_bit_ordinal_surface_landed"
        ]
        and ast_provenance["Cycle830_literal_fixture_landed"]
        and ast_provenance["Cycle840_v2_functions_present"]
        and ast_provenance["Cycle840_v2_literals_exact"]
        and result["stdlib_only"]
        and not result["blocked_modules_loaded_at_start"]
        and not result["firewall_hits_at_start"]
    )
    return (
        result,
        primary_tree,
        historical_trees[(PIN_830, FIXTURE_830)],
    )


def lawful_pairs() -> tuple[Pair, ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def cyclic_separation(pair: Pair) -> int:
    left, right = pair
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def decode_fixture(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(
        literal(tree, name)
        for name in (
            "GATE_CONSTANTS_B85",
            "FAMILY_STATES_B85",
            "SSTAR_PACKED_B85",
        )
    )
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("Cycle-830 fixture literals unavailable")
    gate_raw, family_raw, target_raw = tuple(
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    counts = struct.unpack("<11H", gate_raw[:22])
    macros = []
    offset = 22
    for count in counts:
        macro = []
        for _row in range(count):
            macro.append(struct.unpack(
                "<BHHH", gate_raw[offset:offset + 7]
            ))
            offset += 7
        macros.append(tuple(macro))
    pairs = lawful_pairs()
    keys = tuple(sorted(
        (event, pair) for event in range(4) for pair in pairs
    ))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little"
        )
    target = int.from_bytes(target_raw, "little")
    public = {
        "fixture_source": f"{PIN_830}:{FIXTURE_830}",
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "target_raw_sha256": sha256(target_raw).hexdigest(),
        "macro_gate_counts": counts,
        "macro_gate_total": sum(counts),
        "family_count": len(states),
        "target_hamming_weight": target.bit_count(),
    }
    public["pass"] = (
        offset == len(gate_raw)
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and public["target_raw_sha256"] == EXPECTED_TARGET_RAW_SHA256
        and len(macros) == RING_STATIONS
        and sum(counts) == 3106
        and len(pairs) == 44
        and len(states) == 176
        and target.bit_count() == 44
    )
    return {
        "macros": tuple(macros),
        "states": states,
        "target": target,
        "public": public,
    }


def to_columns(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        value = state
        while value:
            bit = value & -value
            columns[bit.bit_length() - 1] |= 1 << lane
            value ^= bit
    return columns


def from_columns(
    columns: list[int],
    lane_count: int,
) -> tuple[int, ...]:
    states = [0] * lane_count
    for wire, column in enumerate(columns):
        value = column & ((1 << lane_count) - 1)
        while value:
            bit = value & -value
            states[bit.bit_length() - 1] |= 1 << wire
            value ^= bit
    return tuple(states)


def phase_actions(
    macros: tuple[tuple[Gate, ...], ...],
    lane_keys: tuple[Key, ...],
) -> tuple[tuple[tuple[int, tuple[Gate, ...]], ...], ...]:
    """Group by live station, unlike Cycle 840's flattened masked rows."""
    phases = []
    for phase in range(RING_STATIONS):
        actions = []
        for station, macro in enumerate(macros):
            mask = 0
            for lane, (_event, pair) in enumerate(lane_keys):
                if station in {
                    (pair[0] + phase) % RING_STATIONS,
                    (pair[1] + phase) % RING_STATIONS,
                }:
                    mask |= 1 << lane
            if mask:
                actions.append((mask, macro))
        phases.append(tuple(actions))
    return tuple(phases)


def apply_phase(
    columns: list[int],
    actions: tuple[tuple[int, tuple[Gate, ...]], ...],
) -> None:
    for mask, macro in actions:
        for kind, first, second, third in macro:
            if kind == 0:
                columns[first] ^= mask
            elif kind == 1:
                columns[second] ^= columns[first] & mask
            elif kind == 2:
                columns[third] ^= (
                    columns[first] & columns[second] & mask
                )
            else:
                raise AssertionError(("unknown gate", kind))


def candidate_target_lanes(
    columns: list[int],
    target: int,
    lane_mask: int,
    prefilter: tuple[int, ...],
) -> int:
    candidates = lane_mask
    for wire in prefilter:
        column = columns[wire] & lane_mask
        candidates &= (
            column if (target >> wire) & 1 else lane_mask ^ column
        )
        if not candidates:
            return 0
    for wire, column0 in enumerate(columns):
        column = column0 & lane_mask
        candidates &= (
            column if (target >> wire) & 1 else lane_mask ^ column
        )
        if not candidates:
            return 0
    return candidates


def lane_indices(mask: int) -> tuple[int, ...]:
    lanes = []
    while mask:
        bit = mask & -mask
        lanes.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(lanes)


def evolve_census(fixtures: dict[str, object]) -> dict[str, object]:
    macros = fixtures["macros"]
    states = fixtures["states"]
    target = fixtures["target"]
    assert isinstance(macros, tuple)
    assert isinstance(states, dict)
    assert isinstance(target, int)
    keys = tuple(
        key for key in sorted(states)
        if cyclic_separation(key[1]) == 5
    )
    replay_keys = tuple(reversed(keys))
    lane_keys = keys + replay_keys
    columns = to_columns(tuple(states[key] for key in lane_keys))
    actions = phase_actions(macros, lane_keys)
    primary_mask = (1 << len(keys)) - 1
    replay_mask = ((1 << len(keys)) - 1) << len(keys)
    active_target_wires = tuple(
        wire for wire in range(STATE_BITS) if (target >> wire) & 1
    )
    spread = tuple(
        index * (STATE_BITS - 1) // 95 for index in range(96)
    )
    prefilter = tuple(sorted(set(active_target_wires + spread)))
    snapshots = {0: from_columns(columns, len(keys))[:len(keys)]}
    primary_hits = []
    replay_hits = []
    for tick in range(1, SEARCH_TICKS + 1):
        apply_phase(columns, actions[(tick - 1) % RING_STATIONS])
        if tick <= 3:
            snapshots[tick] = from_columns(
                columns, len(lane_keys)
            )[:len(keys)]
        primary = candidate_target_lanes(
            columns, target, primary_mask, prefilter
        )
        replay = candidate_target_lanes(
            columns, target, replay_mask, prefilter
        )
        primary_hits.extend(
            (tick, keys[lane]) for lane in lane_indices(primary)
        )
        replay_hits.extend(
            (tick, lane_keys[lane]) for lane in lane_indices(replay)
        )
    final_states = from_columns(columns, len(lane_keys))
    primary_final = final_states[:len(keys)]
    replay_final = {
        key: final_states[len(keys) + index]
        for index, key in enumerate(replay_keys)
    }
    duplicate_final = all(
        state == replay_final[key]
        for key, state in zip(keys, primary_final)
    )
    duplicate_hits = tuple(primary_hits) == tuple(sorted(replay_hits))
    return {
        "keys": keys,
        "snapshots": snapshots,
        "hits": tuple(primary_hits),
        "public": {
            "scope": "all 44 s=5 keys, ticks 1 through 162129",
            "engine":
                "independent station-mask phase groups with reversed-key "
                "duplicate lanes",
            "lane_count": len(lane_keys),
            "prefilter_wire_count": len(prefilter),
            "exact_hits": tuple(primary_hits),
            "duplicate_hits_exact": duplicate_hits,
            "duplicate_final_states_exact": duplicate_final,
            "pass": (
                len(keys) == 44
                and set(snapshots) == {0, 1, 2, 3}
                and duplicate_hits
                and duplicate_final
            ),
        },
    }


def projection_pattern(
    state: int,
    wires: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in wires)


def primary_claim(primary_tree: ast.Module) -> dict[str, object]:
    wires = literal(primary_tree, "EXPECTED_DISCRIMINATOR_WIRES")
    patterns = literal(primary_tree, "EXPECTED_DISCRIMINATOR_PATTERNS")
    scope = literal(primary_tree, "DISCRIMINATOR_SEARCH_SCOPE")
    expected_keys = literal(primary_tree, "EXPECTED_REACHING_KEYS")
    provenance = literal(primary_tree, "DISCRIMINATOR_WIRE_PROVENANCE")
    representation = literal(
        primary_tree, "EXPECTED_REPRESENTATION_FUNCTION"
    )
    retracted = literal(primary_tree, "V1_LINK_FRAMING_RETRACTED")
    causal_claimed = literal(primary_tree, "CAUSAL_MECHANISM_CLAIMED")
    if not (
        isinstance(wires, tuple)
        and
        isinstance(patterns, tuple)
        and isinstance(expected_keys, tuple)
        and isinstance(provenance, tuple)
        and scope == DISCRIMINATOR_SEARCH_SCOPE
    ):
        raise AssertionError("Cycle-840 literal claim surface drift")
    return {
        "wires": wires,
        "patterns": patterns,
        "search_scope": scope,
        "expected_reaching_keys": expected_keys,
        "wire_provenance": provenance,
        "representation_function": representation,
        "v1_link_framing_retracted": retracted,
        "causal_mechanism_claimed": causal_claimed,
    }


def entry_predicate(key: Key) -> bool:
    event, pair = key
    return (
        event == 0
        and 0 not in pair
        and cyclic_separation(pair) == 5
    )


def p_census(
    claim: dict[str, object],
    dynamics: dict[str, object],
) -> dict[str, object]:
    patterns = claim["patterns"]
    wires = claim["wires"]
    keys = dynamics["keys"]
    snapshots = dynamics["snapshots"]
    hits = dynamics["hits"]
    assert isinstance(patterns, tuple)
    assert isinstance(wires, tuple)
    assert isinstance(keys, tuple)
    assert isinstance(snapshots, dict)
    assert isinstance(hits, tuple)
    hit_keys = tuple(sorted({key for _tick, key in hits}))
    meet_states = snapshots[3]
    d_keys = tuple(
        key for key, state in zip(keys, meet_states)
        if projection_pattern(state, wires) in patterns
    )
    station0_keys = tuple(
        key for key in keys
        if key[0] in (0, 1, 2) and key[1] in ((0, 5), (0, 6))
    )
    approach = []
    for tick in range(4):
        tick_states = snapshots[tick]
        keys_at_d = tuple(
            key for key, state in zip(keys, tick_states)
            if projection_pattern(state, wires) in patterns
        )
        approach.append({
            "tick": tick,
            "D_keys": keys_at_d,
            "D_count": len(keys_at_d),
            "equals_entry_predicate": keys_at_d == tuple(
                key for key in keys if entry_predicate(key)
            ),
            "projected_pattern_count": len({
                projection_pattern(state, wires) for state in tick_states
            }),
            "projected_pattern_digest": digest(tuple(
                projection_pattern(state, wires) for state in tick_states
            )),
        })
    pattern_uses = tuple(sorted(
        (
            pattern,
            sum(
                projection_pattern(state, wires) == pattern
                for state in meet_states
            ),
        )
        for pattern in patterns
    ))
    expected_reaching = claim["expected_reaching_keys"]
    entry_keys = tuple(key for key in keys if entry_predicate(key))
    return {
        "partition": f"{len(hit_keys)}-vs-{len(keys) - len(hit_keys)}",
        "hit_keys": hit_keys,
        "D_keys": d_keys,
        "expected_reaching_keys": expected_reaching,
        "D_implies_reach": set(d_keys) <= set(hit_keys),
        "reach_implies_D": set(hit_keys) <= set(d_keys),
        "station0_keys": station0_keys,
        "station0_D_absent": all(key not in d_keys for key in station0_keys),
        "entry_predicate_keys": entry_keys,
        "D_meet_equals_entry_predicate": d_keys == entry_keys,
        "pattern_uses": pattern_uses,
        "approach": tuple(approach),
        "pass": (
            len(keys) == 44
            and len(hit_keys) == 9
            and len(keys) - len(hit_keys) == 35
            and hit_keys == expected_reaching
            and d_keys == hit_keys
            and len(d_keys) == 9
            and len(pattern_uses) == 3
            and all(count > 0 for _pattern, count in pattern_uses)
            and len(station0_keys) == 6
            and all(key not in d_keys for key in station0_keys)
        ),
    }


def field_literal(wire: int, value: int) -> str:
    start, stop = DISCRIMINATOR_SEARCH_SCOPE
    if not start <= wire < stop:
        raise AssertionError(("wire outside audited projection scope", wire))
    return f"Cycle830_packed_5815_bit_data_wire[{wire}]={value}"


def exact_projection(
    states: tuple[int, ...],
    labels: tuple[bool, ...],
    wires: tuple[int, ...],
) -> tuple[bool, tuple[tuple[int, ...], ...]]:
    positives = {
        tuple((state >> wire) & 1 for wire in wires)
        for state, label in zip(states, labels) if label
    }
    negatives = {
        tuple((state >> wire) & 1 for wire in wires)
        for state, label in zip(states, labels) if not label
    }
    return not (positives & negatives), tuple(sorted(positives))


def minimum_separating_wires(
    states: tuple[int, ...],
    labels: tuple[bool, ...],
) -> dict[str, object]:
    positives = tuple(
        state for state, label in zip(states, labels) if label
    )
    negatives = tuple(
        state for state, label in zip(states, labels) if not label
    )
    pair_count = len(positives) * len(negatives)
    full = (1 << pair_count) - 1
    raw = []
    for wire in range(*DISCRIMINATOR_SEARCH_SCOPE):
        cover = 0
        index = 0
        for positive in positives:
            positive_bit = (positive >> wire) & 1
            for negative in negatives:
                if positive_bit != ((negative >> wire) & 1):
                    cover |= 1 << index
                index += 1
        if cover:
            raw.append((wire, cover))
    # Equal cross-pair coverage is interchangeable for exact separation.
    by_cover = {}
    for wire, cover in raw:
        by_cover.setdefault(cover, wire)
    candidates = tuple(
        (wire, cover) for cover, wire in by_cover.items()
    )
    pair_options = [[] for _index in range(pair_count)]
    for candidate, (_wire, cover) in enumerate(candidates):
        value = cover
        while value:
            bit = value & -value
            pair_options[bit.bit_length() - 1].append(candidate)
            value ^= bit
    tested_states = 0

    def solve(
        uncovered: int,
        depth: int,
        memo: set[tuple[int, int]],
    ) -> tuple[int, ...] | None:
        nonlocal tested_states
        tested_states += 1
        if not uncovered:
            return ()
        if depth == 0:
            return None
        maximum = max(
            (cover & uncovered).bit_count()
            for _wire, cover in candidates
        )
        if maximum == 0 or (
            uncovered.bit_count() + maximum - 1
        ) // maximum > depth:
            return None
        marker = (uncovered, depth)
        if marker in memo:
            return None
        memo.add(marker)
        live_pairs = lane_indices(uncovered)
        pivot = min(
            live_pairs,
            key=lambda pair: sum(
                bool(candidates[index][1] & uncovered)
                for index in pair_options[pair]
            ),
        )
        choices = sorted(
            pair_options[pivot],
            key=lambda index: (
                -(candidates[index][1] & uncovered).bit_count(),
                candidates[index][0],
            ),
        )
        for candidate in choices:
            wire, cover = candidates[candidate]
            tail = solve(uncovered & ~cover, depth - 1, memo)
            if tail is not None:
                return (wire,) + tail
        return None

    solution = None
    proved_impossible_below = []
    for depth in range(1, 13):
        solution = solve(full, depth, set())
        if solution is not None:
            break
        proved_impossible_below.append(depth)
    if solution is None:
        raise AssertionError(
            "no source+bank0 bit projection found through width 12"
        )
    wires = tuple(sorted(set(solution)))
    exact, patterns = exact_projection(states, labels, wires)
    return {
        "cross_class_pairs": pair_count,
        "candidate_wires_with_nonzero_coverage": len(raw),
        "unique_cross_pair_coverages": len(candidates),
        "search_states": tested_states,
        "proved_no_exact_projection_at_widths":
            tuple(proved_impossible_below),
        "minimum_wire_count": len(wires),
        "wires": wires,
        "named_wires": tuple(
            (
                field_literal(wire, (positives[0] >> wire) & 1)
                if len({(state >> wire) & 1 for state in positives}) == 1
                else f"Cycle830_packed_5815_bit_data_wire[{wire}]"
            )
            for wire in wires
        ),
        "positive_pattern_set": patterns,
        "positive_pattern_count": len(patterns),
        "exact": exact,
    }


def overfit_attack(
    claim: dict[str, object],
    dynamics: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    keys = dynamics["keys"]
    states = dynamics["snapshots"][3]
    d_keys = set(census["D_keys"])
    wires = claim["wires"]
    patterns = claim["patterns"]
    assert isinstance(keys, tuple)
    assert isinstance(states, tuple)
    assert isinstance(wires, tuple)
    assert isinstance(patterns, tuple)
    labels = tuple(key in d_keys for key in keys)
    projection = minimum_separating_wires(states, labels)
    adopted_minimum = (
        projection["exact"]
        and projection["proved_no_exact_projection_at_widths"] == (1, 2)
        and projection["minimum_wire_count"] == len(wires) == 3
        and projection["wires"] == wires == EXPECTED_DISCRIMINATOR_WIRES
        and projection["positive_pattern_set"]
        == patterns == EXPECTED_DISCRIMINATOR_PATTERNS
    )
    approach = census["approach"]
    entry_reduces_d = census["D_meet_equals_entry_predicate"]
    patterns_pre_meet = tuple(
        row["tick"] for row in approach[:-1] if row["D_count"]
    )
    representation_adopted = (
        claim["representation_function"]
        == EXPECTED_REPRESENTATION_FUNCTION
        and claim["v1_link_framing_retracted"] is True
        and claim["causal_mechanism_claimed"] is False
    )
    minimality_pass = adopted_minimum
    stability_pass = entry_reduces_d and representation_adopted
    return {
        "MINIMALITY": {
            "verdict": "PASS" if minimality_pass else "FAIL",
            "primary_pattern_count": len(patterns),
            "exact_projected_bit_pattern_enumeration": projection,
            "primary_adopts_independent_minimum": adopted_minimum,
            "strictly_simpler_exact_discriminator_found": False,
            "adopted_discriminator_name":
                "3 Cycle830-packed-wire / 3-pattern discriminator",
            "finding": (
                "V2 adopts the independently reconstructed width-3 minimum; "
                "the exhaustive attack again proves widths 1 and 2 "
                "impossible in the audited 172-wire prefix."
                if minimality_pass else
                "V2 does not exactly adopt the independently reconstructed "
                "minimum discriminator."
            ),
        },
        "STABILITY": {
            "verdict": "PASS" if stability_pass else "FAIL",
            "approach_ticks_0_through_3": approach,
            "D_patterns_appear_before_meet_at_ticks": patterns_pre_meet,
            "D_meet_equals_function_of_event_origin_separation":
                entry_reduces_d,
            "entry_function": EXPECTED_REPRESENTATION_FUNCTION,
            "primary_adopts_representation_reading":
                representation_adopted,
            "independent_dynamical_content_claimed": False,
            "finding": (
                "V2 agrees that the discriminator is the entry predicate "
                "wearing register clothes and retracts the causal/link "
                "reading."
                if stability_pass else
                "The finite reduction persists but v2 does not adopt its "
                "required representation-only reading."
            ),
        },
        "law_candidate": (
            "ADOPTED_MINIMAL_REGISTER_REPRESENTATION_NOT_CAUSAL_LAW"
            if minimality_pass and stability_pass
            else "V2_AGREEMENT_FAILED"
        ),
        "pass": minimality_pass and stability_pass,
    }


def chain_audit(primary_tree: ast.Module) -> dict[str, object]:
    strings = tuple(
        node.value for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    prose = "\n".join(strings)
    required_boundaries = (
        "REGISTER-LOCALLY READABLE",
        "LOCALITY / REPRESENTATION result, not a causal mechanism",
        "The local causal theorem remains open",
        "V1's finite 'link' framing is retracted",
    )
    boundary_hits = tuple(
        phrase for phrase in required_boundaries if phrase in prose
    )
    statuses = tuple(sorted({
        value for value in strings
        if value in {
            "OPEN",
            "PARTIAL",
            "REGISTER_LOCALLY_READABLE",
            "REGISTER_LOCAL_REPRESENTATION_EXACT_CAUSAL_THEOREM_OPEN",
        }
    }))
    exact = (
        len(boundary_hits) == len(required_boundaries)
        and "REGISTER_LOCALLY_READABLE" in statuses
        and "REGISTER_LOCAL_REPRESENTATION_EXACT_CAUSAL_THEOREM_OPEN"
        in statuses
        and "CAUSAL_CHAIN_CLOSED" not in prose
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "AST_status_literals": statuses,
        "boundary_phrases_found": boundary_hits,
        "reading":
            "V2 claims only exact finite register-local readability, "
            "expressly retracts link language, and leaves the local causal "
            "theorem open.",
        "causal_mechanism_overclaim": False if exact else None,
        "pass": exact,
    }


def vocabulary_audit(
    controls: dict[str, object],
    claim: dict[str, object],
) -> dict[str, object]:
    basis = controls["AST_provenance"]
    assert isinstance(basis, dict)
    provenance = claim["wire_provenance"]
    wires = claim["wires"]
    assert isinstance(provenance, tuple)
    assert isinstance(wires, tuple)
    fixture_spec = f"{PIN_830}:{FIXTURE_830}"
    rows_exact = (
        len(provenance) == 3
        and tuple(row[0] for row in provenance) == wires
        and all(
            len(row) == 5
            and row[1]
            == f"Cycle830_packed_5815_bit_data_wire[{row[0]}]"
            and row[2] == fixture_spec
            and "state=int.from_bytes(chunk,'little')" in row[3]
            and row[4] == EXPECTED_FAMILY_RAW_SHA256
            for row in provenance
        )
    )
    landed_ordinal_surface = (
        basis["Cycle830_state_bit_ordinal_surface_landed"]
        and basis["Cycle830_literal_fixture_landed"]
        and all(0 <= wire < STATE_BITS for wire in wires)
    )
    neutral_vocabulary = all(
        "source_register" not in row[1]
        and "bank0_register" not in row[1]
        for row in provenance
    )
    exact = bool(
        rows_exact
        and landed_ordinal_surface
        and neutral_vocabulary
        and wires == EXPECTED_DISCRIMINATOR_WIRES
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "wire_names": tuple(row[1] for row in provenance),
        "wire_ordinals": wires,
        "neutral_global_data_wire_vocabulary": neutral_vocabulary,
        "Cycle830_binds_5815_bit_ordinal_surface":
            landed_ordinal_surface,
        "per_wire_provenance_exact": rows_exact,
        "provenance": {
            "Cycle719_worktree_sha256":
                EXPECTED_WORKTREE_SHA256[AUDIT_INPUT_PATHS[0]],
            "Cycle830_fixture_spec": fixture_spec,
            "Cycle830_family_raw_sha256": EXPECTED_FAMILY_RAW_SHA256,
            "Cycle840_local_field_map_sha256":
                EXPECTED_WORKTREE_SHA256[PRIMARY_840],
        },
        "finding": (
            "V2 names all three wires as zero-based bits of the landed, "
            "SHA-pinned Cycle830 5815-bit little-endian packed fixture; it "
            "makes no unsupported source/bank numeric-range claim."
            if exact else
            "V2's three-wire names are not fully bound to the landed "
            "Cycle830 packed-state ordinal surface."
        ),
        "pass": exact,
    }


def render(certificates: dict[str, object], report: dict[str, object]) -> str:
    rows = []
    for name, certificate in certificates.items():
        verdict = certificate.get("verdict", "PASS")
        rows.append(
            f"CERTIFICATE {name} {verdict} {compact(certificate)}"
        )
    for finding in report["findings_verbatim"]:
        rows.append(f"FINDING {finding}")
    rows.append("SUMMARY_JSON " + compact(report))
    rows.append(str(report["terminal"]))
    return "\n".join(rows) + "\n"


def run() -> int:
    started = monotonic()
    controls, primary_tree, fixture_tree = source_controls()
    claim = primary_claim(primary_tree)
    fixtures = decode_fixture(fixture_tree)
    dynamics = evolve_census(fixtures)
    census = p_census(claim, dynamics)
    attack = overfit_attack(claim, dynamics, census)
    chain = chain_audit(primary_tree)
    vocabulary = vocabulary_audit(controls, claim)
    elapsed = monotonic() - started
    controls.update({
        "fixture": fixtures["public"],
        "dynamics": dynamics["public"],
        "blocked_modules_loaded_at_end": tuple(sorted(
            name for name in sys.modules
            if name.rsplit(".", 1)[-1]
            in {Path(PRIMARY_840).stem, Path(PRIMARY_839).stem}
        )),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": {
            "reversed_key_duplicate_hits_exact":
                dynamics["public"]["duplicate_hits_exact"],
            "reversed_key_duplicate_final_states_exact":
                dynamics["public"]["duplicate_final_states_exact"],
        },
        "self_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "user_runtime_ceiling_seconds": 1400,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    })
    controls_base = (
        controls["pass"]
        and fixtures["public"]["pass"]
        and dynamics["public"]["pass"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < 1400
    )
    d_exact = {
        "verdict": "PASS" if census["pass"] else "FAIL",
        **census,
    }
    certificates = {
        "D_BOTH_DIRECTIONS": d_exact,
        "MINIMALITY": attack["MINIMALITY"],
        "STABILITY": attack["STABILITY"],
        "VOCABULARY": vocabulary,
        "CHAIN_AUDIT": chain,
        "CONTROLS": controls,
    }
    findings = (
        attack["MINIMALITY"]["finding"],
        attack["STABILITY"]["finding"],
        vocabulary["finding"],
        (
            "D is extensionally exact on the finite 44-configuration census "
            "and register-locally reads the entry predicate; it is not an "
            "independent dynamical law."
        ),
    )
    report = {
        "cycle": 840,
        "version": 2,
        "checker": "INDEPENDENT_ADVERSARIAL_V1_ATTACKS_RETAINED",
        "partition": census["partition"],
        "D_both_directions": census["pass"],
        "station0_D_absent": census["station0_D_absent"],
        "overfit_ruling": attack["law_candidate"],
        "claim_status":
            "REGISTER_LOCAL_REPRESENTATION_EXACT_CAUSAL_THEOREM_OPEN",
        "findings_verbatim": findings,
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": bool(
            census["pass"]
            and attack["pass"]
            and attack["MINIMALITY"]["verdict"] == "PASS"
            and attack["STABILITY"]["verdict"] == "PASS"
            and vocabulary["pass"]
            and chain["pass"]
            and controls_base
            and attack["law_candidate"]
            == "ADOPTED_MINIMAL_REGISTER_REPRESENTATION_NOT_CAUSAL_LAW"
        ),
        "terminal": "CYCLE840_V2_INDEPENDENT_CHECK_HONEST_FAIL",
    }
    report["terminal"] = (
        "CYCLE840_V2_INDEPENDENT_CHECK_AGREEMENT_PASS"
        if report["pass"] else
        "CYCLE840_V2_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    for _attempt in range(12):
        controls["pass"] = (
            controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        output = render(certificates, report)
        size = len(output.encode())
        if controls["stdout_bytes"] == size and report["stdout_bytes"] == size:
            break
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    else:
        raise AssertionError("stdout size fixed point did not converge")
    output = render(certificates, report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE840_V2_INDEPENDENT_CHECK_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
