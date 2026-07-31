#!/usr/bin/env python3
"""Cycle 854 independent adversarial checker: the free braid.

This checker never imports or executes the Cycle-830, Cycle-848, or Cycle-854
sources.  It extracts the fixture bank and declared census constants from
SHA/blob-pinned source text with ``ast.literal_eval`` and independently builds
the generator toggle table, inverse reachable census, braid types, and affine
inheritance ranks through weight three.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py",
    "scripts/frontier_cycle848_braid_derivation_2026_07_28.py",
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
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR27-20260729"
EXPECTED_BASE = "e07dc8e094abd7d2633a805139ae100585e03d62"
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58",
    AUDIT_INPUT_PATHS[1]:
        "a9fdefbffe16495e62258804d3abbddb48aaa500e365f56c739c24959162ca48",
    AUDIT_INPUT_PATHS[2]:
        "348c78729f97cb8f5b7c1da53bbf4ee18e8a89a5860a622721a937d36196f754",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "98b1571228ad0902301b6853208ef249ea2c2973",
    AUDIT_INPUT_PATHS[1]: "c55036475e2389565b1c4b69e96595db99e03779",
    AUDIT_INPUT_PATHS[2]: "d59753105863646fbd443e74ebe5406224b95c67",
}
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_TARGET_RAW_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)
EXPECTED_EVENT_SIGNATURE_SHA256 = (
    "7ae45bbd8b6e688b9abdadd0e33dcfd300e2649b4776386a5b8ec48eb62e064a"
)

RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
FAMILY_SIZE = 176
MACRO_GATE_COUNT = 3106
GENERATOR_GATE_COUNT = 6212
NORMALIZED_DEPTH = 64
BACKBONE = (
    (1, 6), (1, 7), (2, 7), (2, 8), (3, 8),
    (3, 9), (4, 9), (4, 10), (5, 10),
)
PREDICATE_WIRES = (40, 81, 105)
EXPECTED_EVENTS = 20
EXPECTED_TYPES = 16
EXPECTED_WIRES = 5320
EXPECTED_PAIRS = 14148540
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

FINDING_FAMILY = (
    "5,320 wires; 14,148,540 pair parities; {56,58} reappears as a special case"
)
FINDING_FREE = "0 inherited / 0 mixed / 16 FREE"
FINDING_THIRD = "no braid type is entailed at the third level"
FINDING_CONTROLS = (
    "shas; BLOCKLIST source primary (text/AST only); determinism; literal "
    "AUDIT_INPUT_PATHS existing worktree-relative; runtime < 1400s; stdout < 150KB"
)


class SourceFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None,
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = SourceFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def literal(tree: ast.Module, name: str) -> object | None:
    matches: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def source_controls() -> tuple[dict[str, object], dict[str, ast.Module]]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    imports: set[str] = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    hashes = {path: sha256(data).hexdigest() for path, data in payloads.items()}
    blobs = {path: git_blob(data) for path, data in payloads.items()}
    literal_paths = literal(self_tree, "AUDIT_INPUT_PATHS")
    declared = trees[AUDIT_INPUT_PATHS[1]]
    declared_constants = {
        "BACKBONE": literal(declared, "BACKBONE") == BACKBONE,
        "NINE_PREDICATE_WIRES":
            literal(declared, "NINE_PREDICATE_WIRES") == PREDICATE_WIRES,
        "EXPECTED_GENERATED_EVENT_COUNT":
            literal(declared, "EXPECTED_GENERATED_EVENT_COUNT") == EXPECTED_EVENTS,
    }
    branch = subprocess.run(
        ("git", "branch", "--show-current"), cwd=ROOT, check=True,
        capture_output=True, text=True, timeout=20,
    ).stdout.strip()
    base_ok = subprocess.run(
        ("git", "merge-base", "--is-ancestor", EXPECTED_BASE, "HEAD"),
        cwd=ROOT, timeout=20,
    ).returncode == 0
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal": literal_paths == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": hashes,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "declared_census_constants": declared_constants,
        "primary_source": AUDIT_INPUT_PATHS[2],
        "primary_policy": "BLOCKLIST source primary (text/AST only)",
        "blocklist": BLOCKLISTED_MODULES,
        "direct_blocklisted_imports": tuple(sorted(
            name for name in imports if name in BLOCKLISTED_MODULES
        )),
        "firewall_hits_at_start": tuple(FIREWALL.hits),
        "expected_branch": EXPECTED_BRANCH,
        "actual_branch": branch,
        "base_is_ancestor": base_ok,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and hashes == EXPECTED_SHA256
        and blobs == EXPECTED_GIT_BLOBS
        and all(declared_constants.values())
        and not result["direct_blocklisted_imports"]
        and not FIREWALL.hits
        and branch == EXPECTED_BRANCH
        and base_ok
    )
    return result, trees


def cyclic_distance(pair: tuple[int, int]) -> int:
    clockwise = (pair[1] - pair[0]) % RING_STATIONS
    counterclockwise = (pair[0] - pair[1]) % RING_STATIONS
    return min(clockwise, counterclockwise)


def fixture_keys() -> tuple[tuple[int, tuple[int, int]], ...]:
    separated = tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_distance(pair) > 1
    )
    return tuple((event, pair) for event in range(4) for pair in separated)


def decode_literal_bank(tree: ast.Module) -> dict[str, object]:
    names = ("GATE_CONSTANTS_B85", "FAMILY_STATES_B85", "SSTAR_PACKED_B85")
    encoded = tuple(literal(tree, name) for name in names)
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("literal fixture bank absent")
    raw_gate, raw_family, raw_target = tuple(
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    lengths = struct.unpack("<11H", raw_gate[:22])
    cursor = 22
    station_macros = []
    for length in lengths:
        macro = []
        for _ in range(length):
            macro.append(struct.unpack("<BHHH", raw_gate[cursor:cursor + 7]))
            cursor += 7
        station_macros.append(tuple(macro))
    keys = fixture_keys()
    seeds = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        seeds[key] = int.from_bytes(
            raw_family[start:start + STATE_BYTES], "little",
        )
    public = {
        "station_macro_lengths": lengths,
        "macro_gate_count": sum(lengths),
        "family_count": len(seeds),
        "gate_raw_sha256": sha256(raw_gate).hexdigest(),
        "family_raw_sha256": sha256(raw_family).hexdigest(),
        "target_raw_sha256": sha256(raw_target).hexdigest(),
    }
    public["pass"] = (
        len(lengths) == RING_STATIONS
        and sum(lengths) == MACRO_GATE_COUNT
        and cursor == len(raw_gate)
        and len(raw_family) == FAMILY_SIZE * STATE_BYTES
        and len(raw_target) == STATE_BYTES
        and len(seeds) == FAMILY_SIZE
        and public["gate_raw_sha256"] == EXPECTED_GATE_RAW_SHA256
        and public["family_raw_sha256"] == EXPECTED_FAMILY_RAW_SHA256
        and public["target_raw_sha256"] == EXPECTED_TARGET_RAW_SHA256
    )
    return {
        "macros": tuple(station_macros),
        "keys": keys,
        "seeds": seeds,
        "target": int.from_bytes(raw_target, "little"),
        "public": public,
    }


def generator_rows(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
) -> dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]]:
    generators = {}
    for generator in BACKBONE:
        rows = []
        for phase in range(RING_STATIONS):
            active = {
                (generator[0] + phase) % RING_STATIONS,
                (generator[1] + phase) % RING_STATIONS,
            }
            for station in sorted(active):
                rows.extend(macros[station])
        if len(rows) != GENERATOR_GATE_COUNT:
            raise AssertionError(("generator length drift", generator, len(rows)))
        generators[generator] = tuple(rows)
    return generators


def executable_rows(
    raw: tuple[tuple[int, int, int, int], ...],
) -> tuple[tuple[int, int], ...]:
    plan = []
    for kind, first, second, third in raw:
        if kind == 0:
            plan.append((0, 1 << first))
        elif kind == 1:
            plan.append((1 << first, 1 << second))
        elif kind == 2:
            plan.append(((1 << first) | (1 << second), 1 << third))
        else:
            raise AssertionError(("unknown primitive", kind))
    return tuple(plan)


def transform(
    state: int, plan: tuple[tuple[int, int], ...], *, inverse: bool = False,
) -> int:
    operations = reversed(plan) if inverse else plan
    for controls, target in operations:
        if controls == 0 or state & controls == controls:
            state ^= target
    return state


def target_wire(row: tuple[int, int, int, int]) -> int:
    kind, first, second, third = row
    if kind == 0:
        return first
    if kind == 1:
        return second
    if kind == 2:
        return third
    raise AssertionError(("unknown primitive", kind))


def toggle_table(
    generators: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
) -> dict[str, object]:
    x_counts = [[0] * STATE_BITS for _ in BACKBONE]
    conditional = [[0] * STATE_BITS for _ in BACKBONE]
    target_kind_counts = [
        [[0, 0, 0] for _ in range(STATE_BITS)] for _ in BACKBONE
    ]
    for generator_index, generator in enumerate(BACKBONE):
        for row in generators[generator]:
            kind = row[0]
            wire = target_wire(row)
            target_kind_counts[generator_index][wire][kind] += 1
            if kind == 0:
                x_counts[generator_index][wire] += 1
            else:
                conditional[generator_index][wire] += 1
    signatures: list[int | None] = []
    for wire in range(STATE_BITS):
        if any(conditional[index][wire] for index in range(len(BACKBONE))):
            signatures.append(None)
        else:
            signature = sum(
                (x_counts[index][wire] & 1) << index
                for index in range(len(BACKBONE))
            )
            signatures.append(signature)
    groups: dict[int, list[int]] = defaultdict(list)
    for wire, signature in enumerate(signatures):
        if signature is not None:
            groups[signature].append(wire)
    wire_family = tuple(groups.get(0, ()))
    pair_count = sum(len(group) * (len(group) - 1) // 2 for group in groups.values())
    return {
        "x_counts": x_counts,
        "conditional": conditional,
        "target_kind_counts": target_kind_counts,
        "signatures": tuple(signatures),
        "signature_groups": {
            signature: tuple(group) for signature, group in groups.items()
        },
        "wire_family": wire_family,
        "pair_count": pair_count,
    }


def partition(states: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    buckets: dict[int, list[int]] = {}
    for lane, state in enumerate(states):
        buckets.setdefault(state, []).append(lane)
    return tuple(tuple(group) for group in buckets.values())


def inverse_reachable_census(
    target: int,
    plans: dict[tuple[int, int], tuple[tuple[int, int], ...]],
) -> tuple[tuple[int, ...], ...]:
    """Build depths 0..65 by reversing each lane's declared generator."""
    by_depth = [tuple(target for _ in BACKBONE)]
    for _depth in range(1, NORMALIZED_DEPTH + 2):
        previous = by_depth[-1]
        predecessor = tuple(
            transform(previous[lane], plans[generator], inverse=True)
            for lane, generator in enumerate(BACKBONE)
        )
        if any(
            transform(predecessor[lane], plans[generator]) != previous[lane]
            for lane, generator in enumerate(BACKBONE)
        ):
            raise AssertionError("inverse/forward reachable-census mismatch")
        by_depth.append(predecessor)
    return tuple(by_depth)


def support(mask: int) -> tuple[int, ...]:
    wires = []
    while mask:
        bit = mask & -mask
        wires.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(wires)


def structural_events(
    by_depth: tuple[tuple[int, ...], ...],
    plans: dict[tuple[int, int], tuple[tuple[int, int], ...]],
) -> tuple[dict[str, object], ...]:
    events = []
    for depth in range(NORMALIZED_DEPTH, -1, -1):
        inputs = by_depth[depth + 1]
        outputs = by_depth[depth]
        predecessor_blocks = partition(inputs)
        for output_block in partition(outputs):
            incoming = tuple(
                tuple(lane for lane in block if lane in output_block)
                for block in predecessor_blocks
                if any(lane in output_block for lane in block)
            )
            if len(incoming) < 2:
                continue
            lanes = tuple(output_block)
            states = tuple(inputs[lane] for lane in lanes)
            common = outputs[lanes[0]]
            if not all(outputs[lane] == common for lane in lanes):
                raise AssertionError("output block is not coincident")
            if not all(
                transform(states[index], plans[BACKBONE[lane]]) == common
                for index, lane in enumerate(lanes)
            ):
                raise AssertionError("event generator replay mismatch")
            variation = 0
            for state in states[1:]:
                variation |= states[0] ^ state
            variation_wires = support(variation)
            patterns = tuple(
                tuple((state >> wire) & 1 for wire in PREDICATE_WIRES)
                for state in states
            )
            structural_type = {
                "incoming_block_sizes": tuple(len(block) for block in incoming),
                "participant_count": len(lanes),
                "predecessor_variation_support_count": len(variation_wires),
                "predecessor_pattern_multiset":
                    tuple(sorted(Counter(patterns).items())),
                "known_three_wire_local":
                    set(variation_wires) <= set(PREDICATE_WIRES),
                "all_patterns_in_landed_nine_family": all(
                    pattern in ((0, 0, 0), (0, 1, 1), (1, 0, 0))
                    for pattern in patterns
                ),
            }
            events.append({
                "event_index": len(events),
                "depth": depth,
                "incoming": incoming,
                "lanes": lanes,
                "keys": tuple(BACKBONE[lane] for lane in lanes),
                "states": states,
                "variation_wires": variation_wires,
                "component_wires": tuple(sorted(
                    set(variation_wires) | set(PREDICATE_WIRES)
                )),
                "structural_type": structural_type,
                "type_sha256": digest(structural_type),
            })
    signature = tuple(
        (event["depth"], event["incoming"], event["lanes"])
        for event in events
    )
    if len(events) != EXPECTED_EVENTS:
        raise AssertionError(("event count", len(events)))
    if digest(signature) != EXPECTED_EVENT_SIGNATURE_SHA256:
        raise AssertionError(("event signature", digest(signature)))
    return tuple(events)


def evenly_spaced(values: tuple[int, ...], count: int) -> tuple[int, ...]:
    if len(values) <= count:
        return values
    if count == 1:
        return (values[0],)
    indices = tuple(index * (len(values) - 1) // (count - 1) for index in range(count))
    return tuple(values[index] for index in indices)


def deterministic_samples(table: dict[str, object]) -> dict[str, object]:
    wire_family = table["wire_family"]
    wire_sample = tuple(sorted(set((56, 58) + evenly_spaced(wire_family, 9))))
    pair_sample_members = evenly_spaced(wire_family, 10)
    pair_sample = tuple(sorted(set(
        ((56, 58),) + tuple(
            (pair_sample_members[index], pair_sample_members[-1 - index])
            for index in range(len(pair_sample_members) // 2)
        )
    )))
    return {
        "selection_rule": (
            "end-point-inclusive evenly spaced members/groups in sorted order; "
            "no RNG; force inclusion of wires 56,58 and pair {56,58}"
        ),
        "wires": wire_sample,
        "pairs": pair_sample,
    }


def sample_cancellation(
    table: dict[str, object], samples: dict[str, object],
) -> dict[str, object]:
    kind_counts = table["target_kind_counts"]
    wire_rows = []
    for wire in samples["wires"]:
        per_generator = []
        for index, generator in enumerate(BACKBONE):
            counts = tuple(kind_counts[index][wire])
            per_generator.append({
                "generator": generator,
                "primitive_target_counts_X_CNOT_Toffoli": counts,
                "explicit_X_pair_cancellation_residual": counts[0] & 1,
                "conditional_target_count": counts[1] + counts[2],
            })
        wire_rows.append({"wire": wire, "per_generator": tuple(per_generator)})
    pair_rows = []
    for first, second in samples["pairs"]:
        per_generator = []
        for index, generator in enumerate(BACKBONE):
            first_counts = tuple(kind_counts[index][first])
            second_counts = tuple(kind_counts[index][second])
            per_generator.append({
                "generator": generator,
                "first_target_counts": first_counts,
                "second_target_counts": second_counts,
                "explicit_pair_parity_residual":
                    (first_counts[0] ^ second_counts[0]) & 1,
                "conditional_target_count":
                    sum(first_counts[1:]) + sum(second_counts[1:]),
            })
        pair_rows.append({"pair": (first, second), "per_generator": tuple(per_generator)})
    passed = (
        all(
            row["explicit_X_pair_cancellation_residual"] == 0
            and row["conditional_target_count"] == 0
            for sample in wire_rows for row in sample["per_generator"]
        )
        and all(
            row["explicit_pair_parity_residual"] == 0
            and row["conditional_target_count"] == 0
            for sample in pair_rows for row in sample["per_generator"]
        )
    )
    return {
        "wire_rows": tuple(wire_rows),
        "pair_rows": tuple(pair_rows),
        "pass": passed,
    }


def sample_boundary_constancy(
    fixtures: dict[str, object],
    plans: dict[tuple[int, int], tuple[tuple[int, int], ...]],
    by_depth: tuple[tuple[int, ...], ...],
    samples: dict[str, object],
) -> dict[str, object]:
    sampled_wires = samples["wires"]
    sampled_pairs = samples["pairs"]

    def observations(state: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
        wires = tuple((state >> wire) & 1 for wire in sampled_wires)
        pairs = tuple(
            ((state >> first) ^ (state >> second)) & 1
            for first, second in sampled_pairs
        )
        return wires, pairs

    fixture_checks = 0
    fixture_ok = True
    for state in fixtures["seeds"].values():
        before = observations(state)
        for generator in BACKBONE:
            after = observations(transform(state, plans[generator]))
            fixture_ok &= after == before
            fixture_checks += 1
    ladder_checks = 0
    ladder_ok = True
    for lane in range(len(BACKBONE)):
        baseline = observations(by_depth[0][lane])
        for depth in range(1, len(by_depth)):
            ladder_ok &= observations(by_depth[depth][lane]) == baseline
            ladder_checks += 1
    return {
        "reachable_boundary_census": (
            "all 176 fixture states under each of 9 complete generators, plus "
            "all 9 lanes at inverse-reconstructed depths 0..65"
        ),
        "fixture_generator_checks": fixture_checks,
        "inverse_ladder_checks": ladder_checks,
        "sampled_wire_count": len(sampled_wires),
        "sampled_pair_count": len(sampled_pairs),
        "fixture_generator_constancy": fixture_ok,
        "inverse_ladder_constancy": ladder_ok,
        "pass": fixture_ok and ladder_ok,
    }


def family_certificate(
    fixtures: dict[str, object],
    table: dict[str, object],
    plans: dict[tuple[int, int], tuple[tuple[int, int], ...]],
    by_depth: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    samples = deterministic_samples(table)
    cancellation = sample_cancellation(table, samples)
    constancy = sample_boundary_constancy(fixtures, plans, by_depth, samples)
    signatures = table["signatures"]
    initial_one_counts = {
        wire: sum((state >> wire) & 1 for state in fixtures["seeds"].values())
        for wire in (56, 58)
    }
    special_counts = {
        wire: tuple(
            tuple(table["target_kind_counts"][index][wire])
            for index in range(len(BACKBONE))
        ) for wire in (56, 58)
    }
    special = {
        "wires": (56, 58),
        "both_level_1_members": all(wire in table["wire_family"] for wire in (56, 58)),
        "pair_level_2_member":
            signatures[56] is not None and signatures[56] == signatures[58],
        "all_176_initial_one_counts": initial_one_counts,
        "per_generator_target_counts_X_CNOT_Toffoli": special_counts,
        "reappears": (
            initial_one_counts == {56: 0, 58: 0}
            and all(
                counts == (4, 0, 0)
                for rows in special_counts.values() for counts in rows
            )
        ),
    }
    wire_count = len(table["wire_family"])
    pair_count = table["pair_count"]
    result = {
        "independent_machinery": (
            "raw primitive target histogram -> reject any conditionally targeted "
            "wire -> nine-bit unconditional-X boundary signature"
        ),
        "wire_count": wire_count,
        "wire_family_sha256": digest(table["wire_family"]),
        "x_only_signature_group_count": len(table["signature_groups"]),
        "pair_parity_count": pair_count,
        "compressed_pair_family_sha256": digest(tuple(
            (signature, wires)
            for signature, wires in sorted(table["signature_groups"].items())
            if len(wires) >= 2
        )),
        "random_free_sample": samples,
        "explicit_toggle_cancellation": cancellation,
        "sample_boundary_constancy": constancy,
        "special_56_58": special,
        "finding": FINDING_FAMILY,
    }
    result["pass"] = (
        wire_count == EXPECTED_WIRES
        and pair_count == EXPECTED_PAIRS
        and special["both_level_1_members"]
        and special["pair_level_2_member"]
        and special["reappears"]
        and cancellation["pass"]
        and constancy["pass"]
    )
    return result


def gf2_rank(rows: tuple[int, ...]) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def derived_equations(
    component_wires: tuple[int, ...],
    signatures: tuple[int | None, ...],
    maximum_weight: int,
) -> tuple[dict[str, object], ...]:
    equations = []
    for weight in range(1, maximum_weight + 1):
        for local_indices in combinations(range(len(component_wires)), weight):
            wires = tuple(component_wires[index] for index in local_indices)
            wire_signatures = tuple(signatures[wire] for wire in wires)
            if any(signature is None for signature in wire_signatures):
                continue
            toggle = 0
            for signature in wire_signatures:
                toggle ^= signature
            if toggle == 0:
                equations.append({
                    "weight": weight,
                    "wires": wires,
                    "coefficient_mask": sum(1 << index for index in local_indices),
                    "nine_generator_toggle_residual": toggle,
                })
    return tuple(equations)


def classify_types(
    events: tuple[dict[str, object], ...],
    fixtures: dict[str, object],
    signatures: tuple[int | None, ...],
    maximum_weight: int,
) -> dict[str, object]:
    grouped: dict[str, list[dict[str, object]]] = defaultdict(list)
    for event in events:
        grouped[event["type_sha256"]].append(event)
    per_type = []
    for type_index, type_hash in enumerate(sorted(grouped), 1):
        occurrences = tuple(grouped[type_hash])
        occurrence_rows = []
        total_cells = 0
        total_rank = 0
        all_consistent = True
        supports = set()
        for event in occurrences:
            wires = event["component_wires"]
            supports.add(wires)
            equations = derived_equations(wires, signatures, maximum_weight)
            coefficient_rows = tuple(
                equation["coefficient_mask"] for equation in equations
            )
            rank = gf2_rank(coefficient_rows)
            lane_consistency = True
            for key, state in zip(event["keys"], event["states"]):
                initial = fixtures["seeds"][(0, key)]
                for equation in equations:
                    current_parity = 0
                    initial_parity = 0
                    for wire in equation["wires"]:
                        current_parity ^= (state >> wire) & 1
                        initial_parity ^= (initial >> wire) & 1
                    lane_consistency &= current_parity == initial_parity
            lane_count = len(event["states"])
            total_cells += len(wires) * lane_count
            total_rank += rank * lane_count
            all_consistent &= lane_consistency
            occurrence_rows.append({
                "event_index": event["event_index"],
                "depth": event["depth"],
                "keys": event["keys"],
                "support_wires": wires,
                "raw_derived_equations": tuple(
                    (row["weight"], row["wires"]) for row in equations
                ),
                "raw_equation_count": len(equations),
                "independent_affine_rank_per_lane": rank,
                "inherited_affine_relation_count_per_lane": (1 << rank) - 1,
                "lane_count": lane_count,
                "observed_pattern_satisfies_relations": lane_consistency,
            })
        verdict = (
            "INHERITED" if total_rank == total_cells
            else "FREE" if total_rank == 0
            else "MIXED"
        )
        per_type.append({
            "type_id": f"T{type_index:02d}",
            "type_sha256": type_hash,
            "occurrence_count": len(occurrences),
            "support_sets": tuple(sorted(supports)),
            "component_cell_count": total_cells,
            "inherited_affine_rank": total_rank,
            "free_degree_count": total_cells - total_rank,
            "occurrences": tuple(occurrence_rows),
            "relations_satisfied": all_consistent,
            "verdict": verdict,
        })
    counts = Counter(row["verdict"] for row in per_type)
    return {
        "maximum_equation_weight": maximum_weight,
        "event_count": len(events),
        "type_count": len(per_type),
        "per_type": tuple(per_type),
        "verdict_counts": {
            "INHERITED": counts["INHERITED"],
            "MIXED": counts["MIXED"],
            "FREE": counts["FREE"],
        },
        "all_relations_satisfied": all(row["relations_satisfied"] for row in per_type),
    }


def analyze(tree830: ast.Module) -> dict[str, object]:
    fixtures = decode_literal_bank(tree830)
    raw_generators = generator_rows(fixtures["macros"])
    plans = {
        generator: executable_rows(rows)
        for generator, rows in raw_generators.items()
    }
    table = toggle_table(raw_generators)
    by_depth = inverse_reachable_census(fixtures["target"], plans)
    events = structural_events(by_depth, plans)
    family = family_certificate(fixtures, table, plans, by_depth)

    level_two = classify_types(events, fixtures, table["signatures"], 2)
    level_two_counts = level_two["verdict_counts"]
    free_certificate = {
        "derivation_only": (
            "The equation system comes only from X-only primitive target lists "
            "whose nine-generator toggle XOR is zero. Census states supply only "
            "the pattern being tested and never admit an equation."
        ),
        "census_construction": (
            "independent inverse construction from the pinned terminal state at "
            "depth 0 through predecessor depth 65; every inverse step replayed forward"
        ),
        "event_signature_sha256": digest(tuple(
            (event["depth"], event["incoming"], event["lanes"])
            for event in events
        )),
        "type_partition_sha256": digest(tuple(
            (event["type_sha256"], event["event_index"])
            for event in events
        )),
        "classification": level_two,
        "decomposition": (
            f"{level_two_counts['INHERITED']} inherited / "
            f"{level_two_counts['MIXED']} mixed / "
            f"{level_two_counts['FREE']} FREE"
        ),
        "finding": FINDING_FREE,
    }
    free_certificate["pass"] = (
        level_two["event_count"] == EXPECTED_EVENTS
        and level_two["type_count"] == EXPECTED_TYPES
        and level_two["all_relations_satisfied"]
        and level_two_counts == {"INHERITED": 0, "MIXED": 0, "FREE": 16}
        and free_certificate["decomposition"] == FINDING_FREE
    )

    level_three = classify_types(events, fixtures, table["signatures"], 3)
    level_three_counts = level_three["verdict_counts"]
    distinct_supports = tuple(sorted(set(
        support_set
        for row in level_three["per_type"]
        for support_set in row["support_sets"]
    )))
    triple_candidates = sum(
        sum(1 for _ in combinations(component, 3))
        for component in distinct_supports
    )
    derived_triples = tuple(sorted(set(
        wires
        for row in level_three["per_type"]
        for occurrence in row["occurrences"]
        for weight, wires in occurrence["raw_derived_equations"]
        if weight == 3
    )))
    affine_support_patterns = tuple({
        "support_wires": component,
        "derived_wire_XOR_generator_constant_patterns": tuple(
            (wire, tuple((table["signatures"][wire] >> index) & 1
                         for index in range(len(BACKBONE))))
            for wire in component if table["signatures"][wire] is not None
        ),
        "rejected_conditionally_targeted_wires": tuple(
            wire for wire in component if table["signatures"][wire] is None
        ),
    } for component in distinct_supports)
    rank_deltas = tuple({
        "type_id": row_three["type_id"],
        "level_2_rank": row_two["inherited_affine_rank"],
        "level_3_rank": row_three["inherited_affine_rank"],
        "rank_gain": (
            row_three["inherited_affine_rank"]
            - row_two["inherited_affine_rank"]
        ),
        "level_3_verdict": row_three["verdict"],
    } for row_two, row_three in zip(level_two["per_type"], level_three["per_type"]))
    third_certificate = {
        "declared_extension": (
            "LEVEL_3_BOUNDED_UNORDERED_TRIPLE_PARITY restricted to each exact "
            "braid-type support, followed by GF(2) affine closure of all inherited "
            "weight-1, weight-2, and weight-3 equations on that support"
        ),
        "distinct_braid_supports": distinct_supports,
        "bounded_triple_candidates_examined": triple_candidates,
        "derived_inherited_triples": derived_triples,
        "affine_boundary_rule": (
            "For every X-only support wire, x_out = x_in XOR c(generator), "
            "with c read from its independently derived nine-bit toggle signature; "
            "conditionally targeted wires admit no such input-independent relation."
        ),
        "global_x_only_toggle_signature_groups": tuple(
            (signature, len(wires))
            for signature, wires in sorted(table["signature_groups"].items())
        ),
        "support_affine_wire_patterns": affine_support_patterns,
        "classification": level_three,
        "per_type_rank_delta": rank_deltas,
        "third_level_entailed_types": tuple(
            row["type_id"] for row in level_three["per_type"]
            if row["verdict"] == "INHERITED"
        ),
        "third_level_nonfree_types": tuple(
            row["type_id"] for row in level_three["per_type"]
            if row["verdict"] != "FREE"
        ),
        "finding": FINDING_THIRD,
    }
    third_certificate["pass"] = (
        level_three["event_count"] == EXPECTED_EVENTS
        and level_three["type_count"] == EXPECTED_TYPES
        and level_three["all_relations_satisfied"]
        and level_three_counts == {"INHERITED": 0, "MIXED": 0, "FREE": 16}
        and not third_certificate["third_level_entailed_types"]
        and not third_certificate["third_level_nonfree_types"]
    )
    event_public = tuple({
        "event_index": event["event_index"],
        "depth": event["depth"],
        "incoming": event["incoming"],
        "lanes": event["lanes"],
        "keys": event["keys"],
        "variation_wires": event["variation_wires"],
        "component_wires": event["component_wires"],
        "structural_type": event["structural_type"],
        "type_sha256": event["type_sha256"],
        "predecessor_state_sha256": digest(tuple(
            state.to_bytes(STATE_BYTES, "little").hex()
            for state in event["states"]
        )),
    } for event in events)
    return {
        "fixture_reconstruction": fixtures["public"],
        "THE_INHERITED_FAMILY": family,
        "THE_FREE_VERDICTS": free_certificate,
        "THE_THIRD_LEVEL_HUNT": third_certificate,
        "event_census_sha256": digest(event_public),
        "event_census": event_public,
    }


def run_worker() -> int:
    started = monotonic()
    sources, trees = source_controls()
    first = analyze(trees[AUDIT_INPUT_PATHS[0]])
    second = analyze(trees[AUDIT_INPUT_PATHS[0]])
    deterministic = first == second
    elapsed = monotonic() - started
    blocked_loaded = tuple(sorted(
        name for name in sys.modules
        if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
    ))
    controls_base = (
        sources["pass"]
        and first["fixture_reconstruction"]["pass"]
        and second["fixture_reconstruction"]["pass"]
        and first["THE_INHERITED_FAMILY"]["pass"]
        and first["THE_FREE_VERDICTS"]["pass"]
        and first["THE_THIRD_LEVEL_HUNT"]["pass"]
        and deterministic
        and not blocked_loaded
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls = {
        "source_controls": sources,
        "fixture_reconstruction_first": first["fixture_reconstruction"],
        "fixture_reconstruction_second": second["fixture_reconstruction"],
        "primary_source_never_imported_or_executed": True,
        "primary_source_access": "SHA/blob-pinned bytes parsed as text/AST only",
        "determinism": {
            "exact": deterministic,
            "first_sha256": digest(first),
            "second_sha256": digest(second),
            "first_event_census_sha256": first["event_census_sha256"],
            "second_event_census_sha256": second["event_census_sha256"],
        },
        "blocked_modules_loaded_at_end": blocked_loaded,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_below_limit": False,
        "finding": FINDING_CONTROLS,
        "pass": False,
    }
    certificates = {
        "THE_INHERITED_FAMILY": first["THE_INHERITED_FAMILY"],
        "THE_FREE_VERDICTS": first["THE_FREE_VERDICTS"],
        "THE_THIRD_LEVEL_HUNT": first["THE_THIRD_LEVEL_HUNT"],
        "CONTROLS": controls,
    }
    checks = {
        name: bool(value["pass"]) for name, value in certificates.items()
    }
    report = {
        "cycle": 854,
        "checker": "INDEPENDENT_ADVERSARIAL_CHECKER_THE_FREE_BRAID",
        "primary_status": "UPHELD_BOUNDED_NEGATIVE",
        "decomposition": first["THE_FREE_VERDICTS"]["decomposition"],
        "third_level_entailed_types":
            first["THE_THIRD_LEVEL_HUNT"]["third_level_entailed_types"],
        "runtime_seconds": round(elapsed, 6),
        "checks": {},
        "pass": False,
        "terminal": "CYCLE854_INDEPENDENT_CHECK_HONEST_FAIL",
    }

    def render() -> str:
        lines = []
        for name, certificate in certificates.items():
            lines.append(f"{name}: {'PASS' if checks[name] else 'FAIL'}")
            lines.append(f"{name}_FINDING={certificate['finding']}")
            lines.append(f"{name}_CERTIFICATE={compact(certificate)}")
        lines.append(f"REPORT={compact(report)}")
        return "\n".join(lines) + "\n"

    for _ in range(16):
        controls["pass"] = controls_base and controls["stdout_below_limit"]
        checks["CONTROLS"] = controls["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["primary_status"] = (
            "UPHELD_BOUNDED_NEGATIVE"
            if report["pass"] else "REFUTED_OR_CHECK_FAILED"
        )
        report["terminal"] = (
            "CYCLE854_INDEPENDENT_CHECK_PASS"
            if report["pass"] else "CYCLE854_INDEPENDENT_CHECK_HONEST_FAIL"
        )
        output = render()
        byte_count = len(output.encode())
        controls["stdout_bytes"] = byte_count
        controls["stdout_below_limit"] = byte_count < STDOUT_LIMIT_BYTES
    output = render()
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 854,
            "pass": False,
            "terminal": "CYCLE854_INDEPENDENT_STDOUT_LIMIT_EXCEEDED",
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }))
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--_worker":
        try:
            return run_worker()
        except Exception as error:
            print(compact({
                "cycle": 854,
                "pass": False,
                "terminal": "CYCLE854_INDEPENDENT_CHECK_HONEST_FAIL",
                "exception_type": type(error).__name__,
                "exception": str(error),
            }))
            return 1
    if len(sys.argv) != 1:
        raise SystemExit(
            "usage: frontier_cycle854_inheritance_independent_check_2026_07_28.py"
        )
    try:
        completed = subprocess.run(
            (sys.executable, str(Path(__file__).resolve()), "--_worker"),
            cwd=ROOT, capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        print(compact({
            "cycle": 854,
            "pass": False,
            "terminal": "CYCLE854_INDEPENDENT_TIMEOUT",
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        }))
        return 1
    stdout_bytes = len(completed.stdout.encode())
    if stdout_bytes >= STDOUT_LIMIT_BYTES:
        print(compact({
            "cycle": 854,
            "pass": False,
            "terminal": "CYCLE854_INDEPENDENT_STDOUT_LIMIT_EXCEEDED",
            "stdout_bytes": stdout_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }))
        return 1
    sys.stdout.write(completed.stdout)
    if completed.stderr:
        sys.stderr.write(completed.stderr)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
