#!/usr/bin/env python3
"""Cycle 855: exact reachable reduction to the Cycle-854 free sector.

The Cycle-854 inheritance family is recomputed from Cycle-830 primitive gate
fixtures.  Cited scientific primaries are SHA/blob pinned, parsed as text/AST
only, and blocked from import.  Closure is tested on the complete Cycle-853
boundary census, generator by generator, before any reduced machine is named.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle848_braid_derivation_2026_07_28.py",
    "scripts/frontier_cycle853_generator_usage_census_2026_07_28.py",
    "scripts/frontier_cycle854_braid_inheritance_2026_07_28.py",
)

import ast
import base64
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR28-20260729"
EXPECTED_BASE = "eaa53c423ee6f7d854ad35cd2bc0f240c7fee0dc"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[1]:
        "a9fdefbffe16495e62258804d3abbddb48aaa500e365f56c739c24959162ca48",
    AUDIT_INPUT_PATHS[2]:
        "946a2ffcbb3ddad19ff2213831593f7ea93a97d9a680fec50a674391592863b7",
    AUDIT_INPUT_PATHS[3]:
        "348c78729f97cb8f5b7c1da53bbf4ee18e8a89a5860a622721a937d36196f754",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[1]: "c55036475e2389565b1c4b69e96595db99e03779",
    AUDIT_INPUT_PATHS[2]: "b28e895ffa847973a5a8ae594d3eb7796b0bc018",
    AUDIT_INPUT_PATHS[3]: "d59753105863646fbd443e74ebe5406224b95c67",
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_SSTAR_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)

RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
EVENTS = (0, 2, 1)
RESOLUTION_MOMENTS = {0: 14744, 2: 33195, 1: 51115}
FULL_REACHABLE_STATES = 891513
FULL_LANDED_TRANSITIONS = 891486
NINE_FUNNEL_MOVEMENT = 14739
NORMALIZED_DEPTH = 64
PREDECESSOR_DEPTH = NORMALIZED_DEPTH + 1
PREDICATE_WIRES = (40, 81, 105)
K3_MARK_BITS = (256, 262)
EXPECTED_EVENT_COUNT = 20
EXPECTED_TYPE_COUNT = 16
EXPECTED_INHERITED_WIRE_COUNT = 5320
EXPECTED_INHERITED_PAIR_COUNT = 14148540
EXPECTED_FREE_WIRE_COUNT = STATE_BITS - EXPECTED_INHERITED_WIRE_COUNT
EXPECTED_EVENT_SIGNATURE_SHA256 = (
    "7ae45bbd8b6e688b9abdadd0e33dcfd300e2649b4776386a5b8ec48eb62e064a"
)
EXPECTED_NORMALIZED_PARTITION_SHA256 = (
    "726b74aefc7afa6e1790c7dc73a59eacdadeec72246e19ac01104be09d49829d"
)
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
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
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    bases = {
        "cycle830_literal_fixture_basis": {
            "decode_fixtures", "build_words", "apply_word",
        } <= function_names(trees[AUDIT_INPUT_PATHS[0]]),
        "cycle848_braid_basis": {
            "evolve_nine", "transition_rows", "certificate_b_schema_hunt",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle853_reachable_census_basis": {
            "build_masked_schedule", "write_kernel_inputs", "execute_kernel",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle854_inheritance_basis": {
            "inheritance_census", "precondition_entailment", "decomposition",
        } <= function_names(trees[AUDIT_INPUT_PATHS[3]]),
        "cycle848_constants_exact": (
            literal_assignment(trees[AUDIT_INPUT_PATHS[1]], "BACKBONE")
            == BACKBONE
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[1]], "NINE_PREDICATE_WIRES"
            ) == PREDICATE_WIRES
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[1]], "EXPECTED_GENERATED_EVENT_COUNT"
            ) == EXPECTED_EVENT_COUNT
        ),
        "cycle853_constants_exact": (
            literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "EVENTS") == EVENTS
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[2]], "RESOLUTION_MOMENTS"
            ) == RESOLUTION_MOMENTS
            and literal_assignment(trees[AUDIT_INPUT_PATHS[2]], "STATE_BITS")
            == STATE_BITS
        ),
        "cycle854_counts_exact": (
            literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "EXPECTED_INHERITED_WIRE_COUNT"
            ) == EXPECTED_INHERITED_WIRE_COUNT
            and literal_assignment(
                trees[AUDIT_INPUT_PATHS[3]], "EXPECTED_INHERITED_PAIR_COUNT"
            ) == EXPECTED_INHERITED_PAIR_COUNT
        ),
    }
    actual_sha = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    actual_blobs = {path: git_blob(payload) for path, payload in payloads.items()}
    branch = subprocess.run(
        ("git", "branch", "--show-current"), cwd=ROOT, check=True,
        capture_output=True, text=True, timeout=20,
    ).stdout.strip()
    base_is_ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", EXPECTED_BASE, "HEAD"),
        cwd=ROOT, timeout=20,
    ).returncode == 0
    public = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "AST_basis": bases,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "text_AST_only": AUDIT_INPUT_PATHS,
        "cycle854_certificate_parsed": False,
        "direct_frontier_imports": tuple(sorted(
            name for name in imports if name.startswith("frontier_cycle")
        )),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "expected_branch": EXPECTED_BRANCH,
        "actual_branch": branch,
        "branch_exact": branch == EXPECTED_BRANCH,
        "expected_base": EXPECTED_BASE,
        "expected_base_is_ancestor": base_is_ancestor,
    }
    public["pass"] = (
        public["AUDIT_INPUT_PATHS_literal"]
        and public["existing_worktree_relative"]
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(bases.values())
        and not public["direct_frontier_imports"]
        and not FIREWALL.hits
        and public["branch_exact"]
        and base_is_ancestor
    )
    return public, trees


def lawful_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if min(
            (pair[1] - pair[0]) % RING_STATIONS,
            (pair[0] - pair[1]) % RING_STATIONS,
        ) > 1
    )


def decode_fixtures(tree: ast.Module) -> dict[str, object]:
    encoded = tuple(literal_assignment(tree, name) for name in (
        "GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85",
    ))
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("Cycle-830 literal fixture bank missing")
    gate_raw, family_raw, target_raw = tuple(
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros = []
    for length in lengths:
        rows = []
        for _index in range(length):
            rows.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(rows))
    keys = tuple(sorted(
        (event, pair) for event in range(2 * FIXTURE_BANKS)
        for pair in lawful_pairs()
    ))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little",
        )
    public = {
        "macro_gate_counts": lengths,
        "macro_gate_count": sum(lengths),
        "family_key_count": len(states),
        "gate_raw_sha256": sha256(gate_raw).hexdigest(),
        "family_raw_sha256": sha256(family_raw).hexdigest(),
        "target_raw_sha256": sha256(target_raw).hexdigest(),
    }
    public["pass"] = (
        len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and len(family_raw) == FAMILY_SIZE * STATE_BYTES
        and len(target_raw) == STATE_BYTES
        and len(states) == FAMILY_SIZE
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and public["target_raw_sha256"] == EXPECTED_SSTAR_PACKED_SHA256
    )
    return {
        "macros": tuple(macros), "states": states,
        "target": int.from_bytes(target_raw, "little"), "public": public,
    }


def build_gate_words(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
) -> dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]]:
    words = {}
    for pair in BACKBONE:
        rows = []
        for phase in range(RING_STATIONS):
            live = {
                (pair[0] + phase) % RING_STATIONS,
                (pair[1] + phase) % RING_STATIONS,
            }
            for station, macro in enumerate(macros):
                if station in live:
                    rows.extend(macro)
        if len(rows) != WORD_GATE_COUNT:
            raise AssertionError(("word gate count drift", pair, len(rows)))
        words[pair] = tuple(rows)
    return words


def gate_target(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    return first if kind == 0 else second if kind == 1 else third


def ranges(values: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    if not values:
        return ()
    result = []
    start = previous = values[0]
    for value in values[1:]:
        if value != previous + 1:
            result.append((start, previous))
            start = value
        previous = value
    result.append((start, previous))
    return tuple(result)


def inheritance_reconstruction(
    words: dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]],
) -> tuple[dict[str, object], dict[str, object]]:
    target_counts = []
    for pair in BACKBONE:
        counts: dict[int, list[int]] = defaultdict(lambda: [0, 0, 0])
        for row in words[pair]:
            counts[gate_target(row)][row[0]] += 1
        target_counts.append(counts)
    profiles = {
        wire: tuple(tuple(counts[wire]) for counts in target_counts)
        for wire in range(STATE_BITS)
    }

    def x_signature(profile: tuple[tuple[int, int, int], ...]) -> tuple[int, ...] | None:
        if any(cnot or toffoli for _x, cnot, toffoli in profile):
            return None
        return tuple(x_count % 2 for x_count, _cnot, _toffoli in profile)

    signature_by_wire = {
        wire: signature for wire, profile in profiles.items()
        if (signature := x_signature(profile)) is not None
    }
    signature_groups: dict[tuple[int, ...], list[int]] = defaultdict(list)
    for wire, signature in signature_by_wire.items():
        signature_groups[signature].append(wire)
    zero_signature = (0,) * len(BACKBONE)
    inherited = tuple(
        wire for wire in range(STATE_BITS)
        if signature_by_wire.get(wire) == zero_signature
    )
    inherited_set = set(inherited)
    free = tuple(wire for wire in range(STATE_BITS) if wire not in inherited_set)
    free_set = set(free)
    pair_count = sum(
        len(group) * (len(group) - 1) // 2
        for group in signature_groups.values()
    )

    support_rows = []
    for pair in BACKBONE:
        free_targets = set()
        free_controls = set()
        inherited_controls = set()
        inherited_to_free = set()
        free_to_free = set()
        channels = Counter()
        for kind, first, second, third in words[pair]:
            target = first if kind == 0 else second if kind == 1 else third
            controls = () if kind == 0 else (first,) if kind == 1 else (first, second)
            if target in free_set:
                free_targets.add(target)
                for control in controls:
                    if control in inherited_set:
                        inherited_controls.add(control)
                        inherited_to_free.add((control, target))
                        channels[f"{kind}:INHERITED_CONTROL_TO_FREE_TARGET"] += 1
                    else:
                        free_controls.add(control)
                        free_to_free.add((control, target))
                        channels[f"{kind}:FREE_CONTROL_TO_FREE_TARGET"] += 1
        support_rows.append({
            "generator": pair,
            "free_target_count": len(free_targets),
            "free_target_ranges": ranges(tuple(sorted(free_targets))),
            "free_control_count": len(free_controls),
            "free_control_ranges": ranges(tuple(sorted(free_controls))),
            "inherited_control_count": len(inherited_controls),
            "inherited_control_ranges": ranges(tuple(sorted(inherited_controls))),
            "inherited_to_free_channel_count": len(inherited_to_free),
            "free_to_free_channel_count": len(free_to_free),
            "primitive_channel_counts": tuple(sorted(channels.items())),
        })

    private = {
        "profiles": profiles,
        "signature_by_wire": signature_by_wire,
        "signature_groups": {
            key: tuple(value) for key, value in signature_groups.items()
        },
        "inherited_wires": inherited,
        "free_wires": free,
    }
    certificate = {
        "reconstruction_basis": (
            "Independent primitive-target census of all 6,212 gates in each "
            "BACKBONE generator; no Cycle-854 result row is parsed."
        ),
        "inherited_wire_count": len(inherited),
        "inherited_wire_ranges": ranges(inherited),
        "inherited_pair_parity_count": pair_count,
        "free_wire_count": len(free),
        "free_wire_ranges": ranges(free),
        "free_wire_sha256": digest(free),
        "support_map": tuple(support_rows),
        "finding": "FREE_COMPLEMENT_RECOMPUTED",
        "pass": (
            len(inherited) == EXPECTED_INHERITED_WIRE_COUNT
            and pair_count == EXPECTED_INHERITED_PAIR_COUNT
            and len(free) == EXPECTED_FREE_WIRE_COUNT
            and set(inherited).isdisjoint(free)
            and len(inherited) + len(free) == STATE_BITS
        ),
    }
    return certificate, private


def main() -> int:
    raise SystemExit("Cycle 855 scaffold: reduced-census kernel not yet installed")


if __name__ == "__main__":
    raise SystemExit(main())
