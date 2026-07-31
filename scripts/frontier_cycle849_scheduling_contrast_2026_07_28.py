#!/usr/bin/env python3
"""Cycle 849: exact k=3 meet geometry and scheduling-mark contrast.

The named predecessor runners are source primaries only.  This runner reads
them as SHA-pinned text/AST, decodes the Cycle-830 literal fixture bank, and
independently applies the landed Boolean X/CNOT/Toffoli rules with integers.
No predecessor is imported or executed.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle840_missing_link_2026_07_28.py",
)

import ast
import base64
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
EXPECTED_BRANCH = "physics-loop/proof-grade-blockF20-20260729"
EXPECTED_BASE = "293c666cd22da9cfa6352fafd73a57bbe5492f05"
RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
K2_MEET_DISCRIMINATOR_WIRES = (40, 81, 105)
K2_MEET_POSITIVE_PATTERNS = ((0, 0, 0), (0, 1, 1), (1, 0, 0))
K2_EXTENSION_WIRES = (88, 124, 125)
EXPECTED_K3_NATIVE_WIRES = (256, 262)
EXPECTED_K3_TRIO_PATTERNS = ((0, 0), (1, 1))
EXPECTED_K3_NONTRIO_PATTERNS = ((0, 1), (1, 0))

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
HISTORICAL_SOURCES = (
    (
        "cycle839_meeting_primary",
        "863c268dd10ed18b09a5d5c33f54a6f118c4083c",
        "scripts/frontier_cycle839_meeting_derivation_2026_07_28.py",
        "bba2ce68e34bb6c502681c201ba83666e9f674aea2606ced4e3f894fdadfe4fa",
        "9289962e4cdd24732a9c5d1ea53b360d236948f8",
    ),
    (
        "cycle838_k3_primary",
        "da8484ced3926203ef8da76015988e6f858a4008",
        "scripts/frontier_cycle838_k3_trio_forecast_2026_07_28.py",
        "ea668b4d0be960622cd10d4e16b3cd1056d343db80ee6845407ca6ddb3e604c0",
        "2f89c8eb911375bed58b1126e9f5f7b860ead20a",
    ),
    (
        "cycle830_fixture_primary",
        "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744",
        "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
        "98b1571228ad0902301b6853208ef249ea2c2973",
    ),
    (
        "cycle846_three_wire_primary",
        "7af6f39f9f2714a5a836af8b1bd3170b2afd4715",
        "scripts/frontier_cycle846_reduced_braids_delay_law_2026_07_28.py",
        "172313524341e958d36e1028f0cec5e64e81c4efd915c009073049998c37fc45",
        "2e0eb1848b92ab3f43a5ada64664ab45b58f5bb1",
    ),
)
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)

Key = tuple[int, tuple[int, ...], int]
PairKey = tuple[int, tuple[int, int]]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]

K3_OPEN_KEYS: tuple[Key, ...] = (
    (3, (0, 2, 6), 2),
    (3, (0, 2, 6), 3),
    (3, (0, 2, 7), 2),
    (3, (0, 2, 7), 3),
    (3, (0, 2, 8), 2),
    (3, (0, 2, 8), 3),
    (3, (0, 3, 6), 2),
    (3, (0, 3, 6), 3),
    (3, (0, 3, 7), 2),
    (3, (0, 3, 7), 3),
)
TRIO_KEYS = tuple(key for key in K3_OPEN_KEYS if key[1][1] == 2)
NONTRIO_KEYS = tuple(key for key in K3_OPEN_KEYS if key not in TRIO_KEYS)
EXPECTED_TRIO_GEOMETRY = {
    (0, 2, 6): (
        (0, 2, 2, 1, (1,)),
        (2, 6, 4, 2, (4,)),
        (6, 0, 5, 3, (8, 9)),
    ),
    (0, 2, 7): (
        (0, 2, 2, 1, (1,)),
        (2, 7, 5, 3, (4, 5)),
        (7, 0, 4, 2, (9,)),
    ),
    (0, 2, 8): (
        (0, 2, 2, 1, (1,)),
        (2, 8, 6, 3, (5,)),
        (8, 0, 3, 2, (9, 10)),
    ),
}
EXPECTED_COMMON_MEETS = {
    (0, 2, 6): (3, (3,)),
    (0, 2, 7): (3, (10,)),
    (0, 2, 8): (3, (0, 10)),
}


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a source primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(sorted({
    *(Path(path).stem for path in AUDIT_INPUT_PATHS),
    *(Path(path).stem for _name, _commit, path, _sha, _blob
      in HISTORICAL_SOURCES),
}))
FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, check=True, capture_output=True,
        timeout=20,
    ).stdout


def git_text(*arguments: str) -> str:
    return git_bytes(*arguments).decode().strip()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
        ):
            values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    historical_payloads = {}
    historical_trees = {}
    historical_rows = []
    for name, commit, path, expected_sha, expected_blob in HISTORICAL_SOURCES:
        spec = f"{commit}:{path}"
        payload = git_bytes("show", spec)
        tree = ast.parse(payload, filename=spec)
        historical_payloads[name] = payload
        historical_trees[name] = tree
        historical_rows.append({
            "name": name,
            "spec": spec,
            "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": expected_sha,
            "sha256_exact": sha256(payload).hexdigest() == expected_sha,
            "git_blob": git_text("rev-parse", spec),
            "expected_git_blob": expected_blob,
            "git_blob_exact": git_text("rev-parse", spec) == expected_blob,
        })
    worktree_rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "access": "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED",
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_WORKTREE_SHA256[path],
        "sha256_exact": (
            sha256(payloads[path]).hexdigest()
            == EXPECTED_WORKTREE_SHA256[path]
        ),
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_WORKTREE_BLOBS[path],
        "git_blob_exact": (
            git_blob(payloads[path]) == EXPECTED_WORKTREE_BLOBS[path]
        ),
    } for path in AUDIT_INPUT_PATHS)
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
    markers = {
        AUDIT_INPUT_PATHS[0]: {"interleaved_program", "run_orbit"},
        AUDIT_INPUT_PATHS[1]: {
            "reconstruct_minimal_discriminator", "meeting_theorem_certificate",
        },
        "cycle839_meeting_primary": {
            "theorem_arc_meeting", "meeting_theorem_certificate",
        },
        "cycle838_k3_primary": {"make_engine", "forecast_certificate"},
        "cycle830_fixture_primary": {"run"},
        "cycle846_three_wire_primary": {
            "register_accounting_rows", "certificate_c_weight_law",
        },
    }
    marker_exact = (
        all(markers[path] <= function_names(trees[path])
            for path in AUDIT_INPUT_PATHS)
        and all(markers[name] <= function_names(historical_trees[name])
                for name in historical_trees)
        and b"(88, 124, 125)" in historical_payloads[
            "cycle846_three_wire_primary"
        ]
    )
    landed_keys = literal_assignment(
        historical_trees["cycle838_k3_primary"],
        "K3_OPEN_THROUGH_T65536",
    )
    branch = git_text("branch", "--show-current")
    base = git_text(
        "merge-base", "HEAD", "physics-loop/proof-grade-blockF19-20260729"
    )
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": (
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS
        ),
        "named_worktree_input_count": len(AUDIT_INPUT_PATHS),
        "total_source_primary_count": (
            len(AUDIT_INPUT_PATHS) + len(HISTORICAL_SOURCES)
        ),
        "maximum_source_primary_count": 7,
        "all_AUDIT_INPUT_PATHS_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in worktree_rows
        ),
        "worktree_source_rows": worktree_rows,
        "historical_source_rows": tuple(historical_rows),
        "source_AST_markers_exact": marker_exact,
        "Cycle838_literal_k3_keys": landed_keys,
        "literal_k3_catalog_exact": landed_keys == K3_OPEN_KEYS,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(sorted(
            name for name in sys.modules
            if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
        )),
        "firewall_hits": tuple(FIREWALL.hits),
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "git_branch_exact": branch == EXPECTED_BRANCH,
        "git_base": base,
        "expected_git_base": EXPECTED_BASE,
        "git_base_exact": base == EXPECTED_BASE,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["total_source_primary_count"] <= 7
        and result["all_AUDIT_INPUT_PATHS_existing_worktree_relative"]
        and all(row["sha256_exact"] and row["git_blob_exact"]
                for row in worktree_rows)
        and all(row["sha256_exact"] and row["git_blob_exact"]
                for row in historical_rows)
        and marker_exact
        and result["literal_k3_catalog_exact"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["git_branch_exact"]
        and result["git_base_exact"]
    )
    return result, historical_trees


def arc_vertices(start: int, end: int) -> tuple[int, ...]:
    length = (end - start) % RING_STATIONS
    return tuple((start + offset) % RING_STATIONS for offset in range(length + 1))


def enumerated_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    for tick in range(length + 1):
        left = set(vertices[:tick + 1])
        right = set(vertices[max(0, length - tick):])
        overlap = left & right
        if overlap:
            return tick, tuple(vertex for vertex in vertices if vertex in overlap)
    raise AssertionError(("wavefronts did not meet", vertices))


def theorem_arc_meeting(
    vertices: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    length = len(vertices) - 1
    tick = (length + 1) // 2
    return tick, tuple(vertices[length - tick:tick + 1])


def trio_geometry(positions: tuple[int, ...]) -> dict[str, object]:
    ordered = tuple(sorted(positions))
    arcs = []
    for index, start in enumerate(ordered):
        end = ordered[(index + 1) % len(ordered)]
        vertices = arc_vertices(start, end)
        formula = theorem_arc_meeting(vertices)
        enumerated = enumerated_arc_meeting(vertices)
        arcs.append({
            "adjacent_sources_clockwise": (start, end),
            "arc_vertices": vertices,
            "gap_length": len(vertices) - 1,
            "first_meeting_tick": formula[0],
            "meeting_centers": formula[1],
            "center_count": len(formula[1]),
            "parity_center_law_exact": (
                len(formula[1]) == (1 if (len(vertices) - 1) % 2 == 0 else 2)
            ),
            "formula_equals_enumeration": formula == enumerated,
        })
    adjacent_completion_tick = max(
        int(row["first_meeting_tick"]) for row in arcs
    )
    common_tick = None
    common_centers: tuple[int, ...] = ()
    for tick in range(RING_STATIONS):
        centers = tuple(
            station for station in range(RING_STATIONS)
            if all(
                min(
                    (station - source) % RING_STATIONS,
                    (source - station) % RING_STATIONS,
                ) <= tick
                for source in ordered
            )
        )
        if centers:
            common_tick = tick
            common_centers = centers
            break
    if common_tick is None:
        raise AssertionError(("no common three-source meet", positions))
    return {
        "sources": ordered,
        "clockwise_gap_lengths": tuple(row["gap_length"] for row in arcs),
        "adjacent_arc_meetings": tuple(arcs),
        "meeting_time_multiset": tuple(sorted(
            int(row["first_meeting_tick"]) for row in arcs
        )),
        "all_adjacent_meets_completed_tick": adjacent_completion_tick,
        "first_common_three_source_meeting_tick": common_tick,
        "first_common_three_source_meeting_centers": common_centers,
        "common_meeting_minimax_radius_exact": all(
            max(
                min(
                    (station - source) % RING_STATIONS,
                    (source - station) % RING_STATIONS,
                )
                for source in ordered
            ) == common_tick
            for station in common_centers
        ) and all(
            any(
                min(
                    (station - source) % RING_STATIONS,
                    (source - station) % RING_STATIONS,
                ) > common_tick - 1
                for source in ordered
            )
            for station in range(RING_STATIONS)
        ),
        "first_center_union": tuple(sorted({
            center for row in arcs for center in row["meeting_centers"]
        })),
        "landed_A_positions_at_common_meet": tuple(
            (source + common_tick) % RING_STATIONS for source in ordered
        ),
        "landed_B_positions_at_common_meet": (),
        "gap_partition_exact": sum(int(row["gap_length"]) for row in arcs)
        == RING_STATIONS,
        "formula_equals_enumeration": all(
            bool(row["formula_equals_enumeration"]) for row in arcs
        ),
    }


def certificate_a_meets() -> dict[str, object]:
    position_rows = tuple(
        trio_geometry(positions) for positions in sorted({key[1] for key in TRIO_KEYS})
    )
    key_rows = tuple({
        "key": key,
        "event": key[2],
        **trio_geometry(key[1]),
    } for key in TRIO_KEYS)
    compact_geometry = tuple(
        (row["sources"], tuple(
            (
                arc["adjacent_sources_clockwise"][0],
                arc["adjacent_sources_clockwise"][1],
                arc["gap_length"],
                arc["first_meeting_tick"],
                arc["meeting_centers"],
            )
            for arc in row["adjacent_arc_meetings"]
        ))
        for row in position_rows
    )
    expected_compact_geometry = tuple(sorted(EXPECTED_TRIO_GEOMETRY.items()))
    common_meets = {
        row["sources"]: (
            row["first_common_three_source_meeting_tick"],
            row["first_common_three_source_meeting_centers"],
        )
        for row in position_rows
    }
    exact = (
        len(TRIO_KEYS) == 6
        and len(position_rows) == 3
        and compact_geometry == expected_compact_geometry
        and common_meets == EXPECTED_COMMON_MEETS
        and all(row["clockwise_gap_lengths"] in ((2, 4, 5), (2, 5, 4), (2, 6, 3))
                for row in position_rows)
        and all(row["meeting_time_multiset"] == (1, 2, 3)
                for row in position_rows)
        and all(row["all_adjacent_meets_completed_tick"] == 3
                for row in position_rows)
        and all(row["first_common_three_source_meeting_tick"] == 3
                and row["common_meeting_minimax_radius_exact"]
                for row in position_rows)
        and all(row["gap_partition_exact"] and row["formula_equals_enumeration"]
                for row in position_rows)
        and all(
            arc["parity_center_law_exact"]
            for row in position_rows for arc in row["adjacent_arc_meetings"]
        )
    )
    return {
        "verdict": "MEET" if exact else "NO_MEET",
        "certificate_role": "A_EXACT_THREE_SOURCE_MEETING_STRUCTURE",
        "theorem": (
            "For clockwise-adjacent sources bounding a gap of d edges on C11, "
            "the two radius-one wavefronts first meet at ceil(d/2); the center "
            "set is one vertex for even d and the two middle vertices for odd d. "
            "The three source gaps partition C11, so the triple meeting structure "
            "is the three exact adjacent-gap meetings."
        ),
        "common_meet_theorem": (
            "The first common meeting of all three graph balls is the exact "
            "minimax radius min_v max_i dist(v,source_i).  For (0,2,6), "
            "(0,2,7), and (0,2,8) it is tick 3 with center sets (3), (10), "
            "and (0,10), respectively."
        ),
        "six_trio_keys": TRIO_KEYS,
        "position_geometry": position_rows,
        "per_key_geometry": key_rows,
        "expected_compact_geometry": expected_compact_geometry,
        "computed_compact_geometry": compact_geometry,
        "expected_common_meets": tuple(sorted(EXPECTED_COMMON_MEETS.items())),
        "computed_common_meets": tuple(sorted(common_meets.items())),
        "pass": exact,
    }


def cyclic_separation(pair: tuple[int, int]) -> int:
    return min(
        (pair[1] - pair[0]) % RING_STATIONS,
        (pair[0] - pair[1]) % RING_STATIONS,
    )


def lawful_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def decode_cycle830_fixtures(
    tree: ast.Module,
) -> dict[str, object]:
    gate_encoded = literal_assignment(tree, "GATE_CONSTANTS_B85")
    family_encoded = literal_assignment(tree, "FAMILY_STATES_B85")
    if not isinstance(gate_encoded, str) or not isinstance(family_encoded, str):
        raise AssertionError("Cycle-830 literal fixtures missing")
    gate_raw = zlib.decompress(base64.b85decode(gate_encoded))
    family_raw = zlib.decompress(base64.b85decode(family_encoded))
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros = []
    for length in lengths:
        rows = []
        for _index in range(length):
            rows.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(rows))
    pairs = lawful_pairs()
    pair_keys: tuple[PairKey, ...] = tuple(sorted(
        (event, pair) for event in range(4) for pair in pairs
    ))
    states = {}
    for index, key in enumerate(pair_keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little"
        )
    exact = (
        len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and sha256(gate_raw).hexdigest() == EXPECTED_GATE_RAW_SHA256
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and sha256(family_raw).hexdigest() == EXPECTED_FAMILY_RAW_SHA256
        and len(pairs) == 44
        and len(pair_keys) == len(states) == FAMILY_SIZE
    )
    return {
        "macros": tuple(macros),
        "pair_keys": pair_keys,
        "states": states,
        "public": {
            "source_access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "macro_gate_counts": lengths,
            "macro_gate_count": sum(lengths),
            "gate_raw_sha256": sha256(gate_raw).hexdigest(),
            "family_raw_sha256": sha256(family_raw).hexdigest(),
            "family_key_count": len(states),
            "pass": exact,
        },
    }


def phase_word(
    macros: tuple[tuple[Gate, ...], ...],
    positions: tuple[int, ...],
    phase: int,
) -> tuple[Gate, ...]:
    live = {(position + phase) % RING_STATIONS for position in positions}
    return tuple(
        gate for station, macro in enumerate(macros) if station in live
        for gate in macro
    )


def synchronous_word(
    macros: tuple[tuple[Gate, ...], ...],
    positions: tuple[int, ...],
) -> tuple[Gate, ...]:
    return tuple(
        gate for phase in range(RING_STATIONS)
        for gate in phase_word(macros, positions, phase)
    )


def apply_word(state: int, word: tuple[Gate, ...]) -> int:
    for kind, first, second, third in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        elif kind == 2:
            state ^= (
                ((state >> first) & 1) & ((state >> second) & 1)
            ) << third
        else:
            raise AssertionError(("unsupported gate kind", kind))
    return state


def recover_event_fixtures(fixtures: dict[str, object]) -> dict[str, object]:
    macros = fixtures["macros"]
    pair_keys = fixtures["pair_keys"]
    states = fixtures["states"]
    assert isinstance(macros, tuple)
    assert isinstance(pair_keys, tuple)
    assert isinstance(states, dict)
    recovered_by_key = {}
    replay_exact = True
    for key in pair_keys:
        event, pair = key
        word = synchronous_word(macros, pair)
        before = apply_word(states[key], tuple(reversed(word)))
        recovered_by_key[key] = before
        replay_exact = replay_exact and apply_word(before, word) == states[key]
    before_by_event = {}
    event_rows = []
    for event in range(4):
        values = {
            recovered_by_key[key] for key in pair_keys if key[0] == event
        }
        before = min(values)
        before_by_event[event] = before
        event_rows.append({
            "event": event,
            "pair_reconstruction_count": sum(
                key[0] == event for key in pair_keys
            ),
            "unique_recovered_fixture_count": len(values),
            "recovered_fixture_packed_sha256": sha256(
                before.to_bytes(STATE_BYTES, "little")
            ).hexdigest(),
        })
    exact = (
        fixtures["public"]["pass"]
        and replay_exact
        and all(row["pair_reconstruction_count"] == 44
                and row["unique_recovered_fixture_count"] == 1
                for row in event_rows)
    )
    return {
        "before_by_event": before_by_event,
        "public": {
            "method": (
                "Invert every pair synchronous word in reverse gate order; "
                "X, CNOT, and Toffoli are self-inverse."
            ),
            "event_rows": tuple(event_rows),
            "all_176_pair_states_replay_exact": replay_exact,
            "pass": exact,
        },
    }


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def wire_pattern(state: int, wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in wires)


def evolve_k3_to_meets(
    fixtures: dict[str, object], recovered: dict[str, object]
) -> dict[str, object]:
    macros = fixtures["macros"]
    before_by_event = recovered["before_by_event"]
    assert isinstance(macros, tuple)
    assert isinstance(before_by_event, dict)
    lane_keys = K3_OPEN_KEYS + K3_OPEN_KEYS
    states = tuple(
        apply_word(
            before_by_event[key[2]], synchronous_word(macros, key[1])
        )
        for key in lane_keys
    )
    snapshots: dict[int, tuple[int, ...]] = {0: states}
    current = list(states)
    maximum_common_meet_tick = max(
        int(trio_geometry(key[1])[
            "first_common_three_source_meeting_tick"
        ]) for key in K3_OPEN_KEYS
    )
    for tick in range(1, maximum_common_meet_tick + 1):
        for lane, key in enumerate(lane_keys):
            current[lane] = apply_word(
                current[lane], phase_word(macros, key[1], tick - 1)
            )
        snapshots[tick] = tuple(current)
    duplicate_rows = tuple({
        "controller_tick": tick,
        "all_10_duplicate_lanes_exact": all(
            snapshots[tick][lane]
            == snapshots[tick][lane + len(K3_OPEN_KEYS)]
            for lane in range(len(K3_OPEN_KEYS))
        ),
    } for tick in range(maximum_common_meet_tick + 1))
    construction_rows = tuple({
        "key": key,
        "initial_packed_sha256": packed_sha256(snapshots[0][lane]),
        "first_common_three_source_meet_tick": trio_geometry(key[1])[
            "first_common_three_source_meeting_tick"
        ],
        "meet_packed_sha256": packed_sha256(
            snapshots[int(trio_geometry(key[1])[
                "first_common_three_source_meeting_tick"
            ])][lane]
        ),
    } for lane, key in enumerate(K3_OPEN_KEYS))
    exact = (
        fixtures["public"]["pass"]
        and recovered["public"]["pass"]
        and len(states) == 2 * len(K3_OPEN_KEYS)
        and all(row["all_10_duplicate_lanes_exact"] for row in duplicate_rows)
    )
    return {
        "snapshots": snapshots,
        "meet_states": tuple(
            snapshots[int(trio_geometry(key[1])[
                "first_common_three_source_meeting_tick"
            ])][lane]
            for lane, key in enumerate(K3_OPEN_KEYS)
        ),
        "public": {
            "scope": (
                "all ten literal k=3 open keys, independent scalar landed "
                "Boolean replay through each key's first common three-source "
                "meet tick"
            ),
            "maximum_common_meet_tick": maximum_common_meet_tick,
            "key_rows": construction_rows,
            "duplicate_determinism_checks": duplicate_rows,
            "pass": exact,
        },
    }


def named_wire_test(
    states: tuple[int, ...], wires: tuple[int, ...]
) -> dict[str, object]:
    rows = tuple({
        "key": key,
        "class": "TRIO" if key in TRIO_KEYS else "NONTRIO",
        "pattern": wire_pattern(state, wires),
    } for key, state in zip(K3_OPEN_KEYS, states))
    positive_patterns = tuple(sorted({
        row["pattern"] for row in rows if row["class"] == "TRIO"
    }))
    negative_patterns = tuple(sorted({
        row["pattern"] for row in rows if row["class"] == "NONTRIO"
    }))
    return {
        "wires": wires,
        "rows": rows,
        "trio_pattern_set": positive_patterns,
        "nontrio_pattern_set": negative_patterns,
        "pattern_sets_disjoint": not (
            set(positive_patterns) & set(negative_patterns)
        ),
    }


def reconstruct_minimal_discriminator(
    states: tuple[int, ...], labels: tuple[bool, ...]
) -> dict[str, object]:
    """Cycle-840 set-cover method over all landed data wires through width 3."""
    cross_pairs = tuple(
        (positive, negative)
        for positive, label in enumerate(labels) if label
        for negative, other in enumerate(labels) if not other
    )
    full = (1 << len(cross_pairs)) - 1
    cover_to_wire: dict[int, int] = {}
    candidate_wire_count = 0
    for wire in range(STATE_BITS):
        cover = 0
        for index, (positive, negative) in enumerate(cross_pairs):
            if ((states[positive] >> wire) ^ (states[negative] >> wire)) & 1:
                cover |= 1 << index
        if cover:
            candidate_wire_count += 1
            cover_to_wire[cover] = min(wire, cover_to_wire.get(cover, wire))
    candidates = tuple(sorted(
        ((wire, cover) for cover, wire in cover_to_wire.items()),
        key=lambda row: row[0],
    ))
    tested_width1 = len(candidates)
    width1 = tuple((wire,) for wire, cover in candidates if cover == full)
    tested_width2 = 0
    width2 = []
    if not width1:
        for (left_wire, left), (right_wire, right) in combinations(candidates, 2):
            tested_width2 += 1
            if left | right == full:
                width2.append((left_wire, right_wire))
    width3_witness: tuple[int, ...] | None = None
    tested_width3_pairs = 0
    tested_width3_completions = 0
    if not width1 and not width2:
        covers_by_bit = tuple(
            tuple(index for index, (_wire, cover) in enumerate(candidates)
                  if (cover >> bit) & 1)
            for bit in range(len(cross_pairs))
        )
        for left_index in range(len(candidates)):
            left_wire, left = candidates[left_index]
            if width3_witness is not None:
                break
            for right_index in range(left_index + 1, len(candidates)):
                tested_width3_pairs += 1
                right_wire, right = candidates[right_index]
                missing = full & ~(left | right)
                if not missing:
                    raise AssertionError("width-2 witness omitted")
                missing_bits = tuple(
                    bit for bit in range(len(cross_pairs)) if (missing >> bit) & 1
                )
                pivot = min(
                    missing_bits,
                    key=lambda bit: sum(
                        index > right_index for index in covers_by_bit[bit]
                    ),
                )
                for third_index in covers_by_bit[pivot]:
                    if third_index <= right_index:
                        continue
                    tested_width3_completions += 1
                    third_wire, third = candidates[third_index]
                    if (left | right | third) == full:
                        width3_witness = (
                            left_wire, right_wire, third_wire
                        )
                        break
                if width3_witness is not None:
                    break
    if width1:
        minimum_width = 1
        witness = min(width1)
    elif width2:
        minimum_width = 2
        witness = min(width2)
    elif width3_witness is not None:
        minimum_width = 3
        witness = width3_witness
    else:
        minimum_width = None
        witness = None
    positive_patterns = tuple(sorted({
        wire_pattern(state, witness) for state, label in zip(states, labels)
        if label
    })) if witness else ()
    negative_patterns = tuple(sorted({
        wire_pattern(state, witness) for state, label in zip(states, labels)
        if not label
    })) if witness else ()
    exact = (
        len(cross_pairs) == len(TRIO_KEYS) * len(NONTRIO_KEYS) == 24
        and minimum_width is not None
        and witness is not None
        and not set(positive_patterns) & set(negative_patterns)
        and (minimum_width == 1 or not width1)
        and (minimum_width <= 2 or not width2)
    )
    return {
        "method": (
            "Cycle-840 cross-class set cover: a wire covers every trio/nontrio "
            "pair on which its bit differs; selected wires discriminate exactly "
            "iff their cover union is all cross-class pairs."
        ),
        "search_scope": "all zero-based landed data wires 0 through 5814",
        "search_scope_half_open": (0, STATE_BITS),
        "cross_class_pair_count": len(cross_pairs),
        "candidate_wire_count": candidate_wire_count,
        "distinct_nonzero_cover_count": len(candidates),
        "identical_cover_reduction_exact": (
            "Only the least wire per identical cross-pair cover is needed: "
            "two equal covers cannot improve a set-cover union."
        ),
        "tested_width1_cover_classes": tested_width1,
        "tested_width2_cover_class_pairs": tested_width2,
        "tested_width3_prefix_pairs_until_witness": tested_width3_pairs,
        "tested_width3_completion_candidates_until_witness":
            tested_width3_completions,
        "proved_no_exact_projection_at_widths": tuple(
            width for width, solutions in ((1, width1), (2, width2))
            if not solutions and minimum_width is not None and width < minimum_width
        ),
        "minimum_wire_count": minimum_width,
        "wires": witness,
        "trio_pattern_set": positive_patterns,
        "nontrio_pattern_set": negative_patterns,
        "pattern_sets_disjoint": not (
            set(positive_patterns) & set(negative_patterns)
        ) if witness else False,
        "exact": exact,
    }


def certificate_b_mark(
    dynamics: dict[str, object]
) -> dict[str, object]:
    states = dynamics["meet_states"]
    snapshots = dynamics["snapshots"]
    assert isinstance(states, tuple)
    assert isinstance(snapshots, dict)
    labels = tuple(key in TRIO_KEYS for key in K3_OPEN_KEYS)
    k2_meet = named_wire_test(states, K2_MEET_DISCRIMINATOR_WIRES)
    k2_extension = named_wire_test(states, K2_EXTENSION_WIRES)
    native = reconstruct_minimal_discriminator(states, labels)
    native_wires = native["wires"]
    tick_rows = tuple({
        "key": key,
        "class": "TRIO" if key in TRIO_KEYS else "NONTRIO",
        "first_common_three_source_meet_tick": trio_geometry(key[1])[
            "first_common_three_source_meeting_tick"
        ],
        "patterns_by_controller_tick": tuple({
            "tick": tick,
            "k2_40_81_105": wire_pattern(
                snapshots[tick][lane], K2_MEET_DISCRIMINATOR_WIRES
            ),
            "k2_40_81_105_D": wire_pattern(
                snapshots[tick][lane], K2_MEET_DISCRIMINATOR_WIRES
            ) in K2_MEET_POSITIVE_PATTERNS,
            "k2_88_124_125": wire_pattern(
                snapshots[tick][lane], K2_EXTENSION_WIRES
            ),
            "k3_native": (
                wire_pattern(snapshots[tick][lane], native_wires)
                if isinstance(native_wires, tuple) else None
            ),
        } for tick in range(
            1, int(dynamics["public"]["maximum_common_meet_tick"]) + 1
        )),
    } for lane, key in enumerate(K3_OPEN_KEYS))
    mark_exists = bool(
        native["exact"]
        and native["minimum_wire_count"] is not None
        and int(native["minimum_wire_count"]) <= 3
    )
    verdict = "MARKED" if mark_exists else "UNMARKED"
    expected_native_exact = (
        native["minimum_wire_count"] == 2
        and native_wires == EXPECTED_K3_NATIVE_WIRES
        and native["trio_pattern_set"] == EXPECTED_K3_TRIO_PATTERNS
        and native["nontrio_pattern_set"] == EXPECTED_K3_NONTRIO_PATTERNS
    )
    exact = (
        dynamics["public"]["pass"]
        and native["exact"]
        and expected_native_exact
        and mark_exists
        and not k2_meet["pattern_sets_disjoint"]
        and not k2_extension["pattern_sets_disjoint"]
    )
    return {
        "verdict": verdict,
        "certificate_role": "B_K3_MEET_MARK_TEST",
        "meet_snapshot_definition": (
            "For each key, the landed 5815-bit state at the first nonempty "
            "intersection of all three graph balls.  This is tick 3 for the "
            "six trios and the (0,3,6) controls, and tick 4 for the (0,3,7) "
            "controls."
        ),
        "tested_k2_wire_triples": {
            "Cycle840_meet_predicate_40_81_105": {
                **k2_meet,
                "Cycle840_positive_patterns": K2_MEET_POSITIVE_PATTERNS,
                "Cycle840_D_true_on_trio_keys": all(
                    wire_pattern(state, K2_MEET_DISCRIMINATOR_WIRES)
                    in K2_MEET_POSITIVE_PATTERNS
                    for key, state in zip(K3_OPEN_KEYS, states)
                    if key in TRIO_KEYS
                ),
                "Cycle840_D_false_on_nontrio_keys": all(
                    wire_pattern(state, K2_MEET_DISCRIMINATOR_WIRES)
                    not in K2_MEET_POSITIVE_PATTERNS
                    for key, state in zip(K3_OPEN_KEYS, states)
                    if key in NONTRIO_KEYS
                ),
            },
            "Cycle846_extension_88_124_125": k2_extension,
        },
        "k3_native_minimality": native,
        "k3_wires": native_wires,
        "k3_predicate": "D3(x)=1 iff bit[256] == bit[262]",
        "k3_predicate_exact_on_ten_meet_states": expected_native_exact,
        "three_wire_hunt_disposition": (
            "The requested width-3 hunt terminates earlier: exhaustive widths "
            "1 then 2 find the exact minimum pair (256,262).  Any added third "
            "wire is redundant, so no nonminimal triple is presented as the "
            "native minimum."
        ),
        "all_ticks_named_and_native_patterns": tick_rows,
        "reading": (
            "The two-wire equality predicate on landed wires 256 and 262 "
            "separates every trio meet state from every nontrio k=3 meet "
            "state; this is stronger than a width-3 witness."
            if mark_exists else
            "No exact three-wire Boolean register projection was found at the "
            "completed k=3 meets."
        ),
        "causal_precision": (
            "MARKED is a finite register-local representation result.  It does "
            "not claim that the three wires cause a later resolution."
        ),
        "pass": exact,
    }


def certificate_c_contrast(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
) -> dict[str, object]:
    if certificate_a["verdict"] == "NO_MEET":
        verdict = "NO_MEET"
        stall_location = "BEFORE_MEETING"
        statement = (
            "The k=3 common wavefront meeting is absent, so the stall precedes "
            "the structural stage at which k=2 carries its meet mark."
        )
    elif certificate_b["verdict"] == "UNMARKED":
        verdict = "UNMARKED"
        stall_location = "AT_MARK"
        statement = (
            "The k=3 sources meet but no at-most-three-wire local predicate "
            "separates trio from nontrio meet states, unlike the k=2 meet mark."
        )
    else:
        verdict = "MARKED"
        stall_location = "AFTER_MARK_PURE_SCHEDULING"
        statement = (
            "At the same structural stage—first common all-source wavefront "
            "meeting—k=2 has its locally readable Cycle-840 predicate on wires "
            "(40,81,105), while k=3 has its own exact, smaller equality mark on "
            "wires (256,262).  Since all k=2 s=5 keys resolve by t=1,142,432 "
            "but the six k=3 backbone trios have not started resolution by "
            "T=1,048,576, the k=3 stall is after the mark: the mark is present "
            "and the scheduled resolution moment is absent through that horizon."
        )
    exact = (
        certificate_a["pass"]
        and certificate_b["pass"]
        and verdict == "MARKED"
        and certificate_b["k3_wires"] == EXPECTED_K3_NATIVE_WIRES
    )
    return {
        "verdict": verdict,
        "certificate_role": "C_CROSS_STRATUM_SCHEDULING_CONTRAST",
        "stall_location": stall_location,
        "same_structural_stage": "FIRST_COMMON_ALL_SOURCE_WAVEFRONT_MEET",
        "k2_at_meet": {
            "meeting_tick": 3,
            "mark_wires": K2_MEET_DISCRIMINATOR_WIRES,
            "mark_reading": (
                "Cycle-840 finite entry predicate is register-locally readable"
            ),
            "all_s5_keys_resolved_by_controller_time": 1_142_432,
        },
        "k3_at_meet": {
            "six_trio_meeting_tick": 3,
            "mark_wires": EXPECTED_K3_NATIVE_WIRES,
            "mark_reading": "D3(x)=1 iff bit[256] == bit[262]",
            "backbone_trio_resolution_not_started_through": 1_048_576,
        },
        "named_k2_triple_transfer_result": (
            "Neither (40,81,105) nor (88,124,125) transfers as an exact "
            "trio/nontrio classifier at the k=3 common meets; the k=3 mark is "
            "native to wires (256,262)."
        ),
        "horizon_facts_role": (
            "Supplied landed context, used for scheduling contrast and not "
            "re-derived by this bounded meet/mark runner."
        ),
        "exact_contrast_statement": statement,
        "causal_precision": (
            "MARKED certifies finite register-local readability, not a local "
            "update-rule mechanism or an eventual k=3 resolution theorem."
        ),
        "pass": exact,
    }


def render(certificates: dict[str, object], report: dict[str, object]) -> str:
    return "\n".join((
        *(f"CERTIFICATE {name} {compact(value)}"
          for name, value in certificates.items()),
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    )) + "\n"


def stable_render(
    certificates: dict[str, object],
    checks: dict[str, bool],
    report: dict[str, object],
    controls_base: bool,
) -> str:
    controls = certificates["D_CONTROLS"]
    assert isinstance(controls, dict)
    for _attempt in range(20):
        controls["pass"] = bool(
            controls_base and controls["stdout_bytes"] < STDOUT_LIMIT_BYTES
        )
        checks["D_CONTROLS"] = bool(controls["pass"])
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE849_MARKED_SCHEDULING_CONTRAST_PASS"
            if report["pass"] and report["verdict"] == "MARKED"
            else "CYCLE849_HONEST_FAIL"
        )
        output = render(certificates, report)
        size = len(output.encode())
        if controls["stdout_bytes"] == size and report["stdout_bytes"] == size:
            return output
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    controls, historical_trees = source_controls()
    source_controls_pass = bool(controls["pass"])
    fixtures = decode_cycle830_fixtures(
        historical_trees["cycle830_fixture_primary"]
    )
    recovered = recover_event_fixtures(fixtures)
    dynamics = evolve_k3_to_meets(fixtures, recovered)
    certificate_a = certificate_a_meets()
    certificate_b = certificate_b_mark(dynamics)
    certificate_c = certificate_c_contrast(certificate_a, certificate_b)

    replay_fixtures = decode_cycle830_fixtures(
        historical_trees["cycle830_fixture_primary"]
    )
    replay_recovered = recover_event_fixtures(replay_fixtures)
    replay_dynamics = evolve_k3_to_meets(
        replay_fixtures, replay_recovered
    )
    replay_a = certificate_a_meets()
    replay_b = certificate_b_mark(replay_dynamics)
    replay_c = certificate_c_contrast(replay_a, replay_b)
    deterministic = (
        fixtures["public"] == replay_fixtures["public"]
        and recovered["public"] == replay_recovered["public"]
        and dynamics["public"] == replay_dynamics["public"]
        and dynamics["meet_states"] == replay_dynamics["meet_states"]
        and certificate_a == replay_a
        and certificate_b == replay_b
        and certificate_c == replay_c
        and all(
            row["all_10_duplicate_lanes_exact"]
            for row in dynamics["public"]["duplicate_determinism_checks"]
        )
    )
    elapsed = monotonic() - started
    controls.update({
        "source_controls_pass": source_controls_pass,
        "fixture_provenance": fixtures["public"],
        "event_fixture_reconstruction": recovered["public"],
        "landed_k3_reimplementation": dynamics["public"],
        "blocked_modules_loaded_at_end": tuple(sorted(
            name for name in sys.modules
            if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
        )),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": {
            "method": (
                "Independent full fixture/dynamics/certificate replay plus "
                "duplicate lanes for all ten k=3 keys at ticks 0 through 4."
            ),
            "full_replay_exact": deterministic,
            "duplicate_lane_checks": dynamics["public"][
                "duplicate_determinism_checks"
            ],
            "exact": deterministic,
        },
        "exact_arithmetic": (
            "C11 distances, arc wavefront sets, Boolean X/CNOT/Toffoli gates, "
            "5815-bit states, exhaustive cross-class covers, counts, and SHA "
            "digests use exact Python integers/bytes/sets.  Only monotonic wall "
            "runtime is floating point."
        ),
        "certificate_digest_sha256": digest((
            certificate_a, certificate_b, certificate_c,
            fixtures["public"], recovered["public"], dynamics["public"],
        )),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "user_runtime_ceiling_seconds": 1400,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    })
    controls_base = (
        source_controls_pass
        and fixtures["public"]["pass"]
        and recovered["public"]["pass"]
        and dynamics["public"]["pass"]
        and certificate_a["pass"]
        and certificate_b["pass"]
        and certificate_c["pass"]
        and deterministic
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC <= 1400
    )
    certificates = {
        "A_K3_MEETS": certificate_a,
        "B_K3_MARK_TEST": certificate_b,
        "C_SCHEDULING_CONTRAST": certificate_c,
        "D_CONTROLS": controls,
    }
    checks = {
        "A_EXACT_K3_MEETS": bool(
            certificate_a["pass"] and certificate_a["verdict"] == "MEET"
        ),
        "B_MARKED_NATIVE_REGISTER": bool(
            certificate_b["pass"]
            and certificate_b["verdict"] == "MARKED"
            and certificate_b["k3_wires"] == EXPECTED_K3_NATIVE_WIRES
        ),
        "C_AFTER_MARK_SCHEDULING_CONTRAST": bool(
            certificate_c["pass"]
            and certificate_c["stall_location"]
            == "AFTER_MARK_PURE_SCHEDULING"
        ),
        "D_CONTROLS": False,
        "FULL_REPLAY_AND_DUPLICATE_DETERMINISM": deterministic,
        "RUNTIME_BOUND": elapsed < AUDIT_TIMEOUT_SEC,
    }
    report = {
        "cycle": 849,
        "stage": "certificates-A-B-C-D",
        "meeting_verdict": certificate_a["verdict"],
        "verdict": certificate_b["verdict"],
        "stall_location": certificate_c["stall_location"],
        "k3_wires": certificate_b["k3_wires"],
        "k3_predicate": certificate_b["k3_predicate"],
        "native_minimum_wire_count": certificate_b[
            "k3_native_minimality"
        ]["minimum_wire_count"],
        "runtime_seconds": round(elapsed, 6),
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE849_HONEST_FAIL",
    }
    output = stable_render(certificates, checks, report, controls_base)
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
            "terminal": "CYCLE849_HONEST_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
