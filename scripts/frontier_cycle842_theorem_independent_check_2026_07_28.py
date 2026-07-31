#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-842 partial theorem.

The source primary and the pinned fixture primary are text/AST inputs only.
Neither is imported or executed.  Gate evolution is reimplemented here with
bit-sliced Python integers and an independently constructed station schedule.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle842_local_causal_theorem_2026_07_28.py",
)

import ast
import base64
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import gcd
from pathlib import Path
import struct
import subprocess
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_SHA256 = (
    "65ced87db73db177c561e0dd293ae88963c15929d820f6dd99417a27ba647def"
)
PRIMARY_GIT_BLOB = "a1836d84d8dda74c4f79cc1bbc60ef798d86a2e3"
FIXTURE_COMMIT = "2bc4c4d6111a0e260b8b6107cd82e57dcbaa1744"
FIXTURE_PATH = "scripts/frontier_cycle830_sstar_preimage_tree_2026_07_28.py"
FIXTURE_SPEC = f"{FIXTURE_COMMIT}:{FIXTURE_PATH}"
FIXTURE_SHA256 = (
    "40d8cfb99b65fa251599bbf07f6a4399fd5bda9ad1e9e12e24db9395c4737d58"
)
FIXTURE_GIT_BLOB = "98b1571228ad0902301b6853208ef249ea2c2973"
GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
TARGET_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)
EXPECTED_WIRE_DERIVATION_DIGEST = (
    "2a80b39d4eb1b9d7fd3e0999865595178064b57077f87aa2e2eae8510c9d6c86"
)

RING_STATIONS = 11
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
GATE_COUNT = 3106
MOVEMENT_GATE_COUNT = 6212
MEET_TICK = 3
BOUND_B = 162126
FINAL_TICK = MEET_TICK + BOUND_B
WIRES = (40, 81, 105)
MARK_PATTERNS = ((0, 0, 0), (0, 1, 1), (1, 0, 0))
MARKED_KEYS = (
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
CONTROL_SAMPLE_SIZE = 6
COUNTER_WINDOW_END = 64

Pair = tuple[int, int]
Key = tuple[int, Pair]
Gate = tuple[int, int, int, int]
ScheduledGate = tuple[int, int, int, int, int, int]

BLOCKLISTED_MODULES = (
    Path(PRIMARY_PATH).stem,
    Path(FIXTURE_PATH).stem,
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
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
            raise ImportError(f"BLOCKLIST forbids importing {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def object_digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_bytes(*args: str) -> bytes:
    return subprocess.run(
        ("git", *args),
        cwd=ROOT,
        check=True,
        capture_output=True,
        timeout=30,
    ).stdout


def git_text(*args: str) -> str:
    return git_bytes(*args).decode().strip()


def blob_id(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    nodes: list[ast.expr] = []
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


def integer_expression(node: ast.expr, values: dict[str, int]) -> int:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if isinstance(node, ast.Name) and node.id in values:
        return values[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -integer_expression(node.operand, values)
    if isinstance(node, ast.BinOp):
        left = integer_expression(node.left, values)
        right = integer_expression(node.right, values)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.FloorDiv):
            return left // right
    raise ValueError("expression is not a closed integer constant")


def integer_assignments(tree: ast.Module) -> dict[str, int]:
    values: dict[str, int] = {}
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            try:
                values[node.targets[0].id] = integer_expression(
                    node.value, values
                )
            except ValueError:
                pass
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.value is not None
        ):
            try:
                values[node.target.id] = integer_expression(
                    node.value, values
                )
            except ValueError:
                pass
    return values


def cyclic_separation(pair: Pair) -> int:
    left, right = pair
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def lawful_pairs() -> tuple[Pair, ...]:
    return tuple(
        pair
        for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) > 1
    )


def decode_fixture() -> dict[str, object]:
    source = git_bytes("show", FIXTURE_SPEC)
    tree = ast.parse(source, filename=FIXTURE_SPEC)
    encoded = tuple(
        literal_assignment(tree, name)
        for name in (
            "GATE_CONSTANTS_B85",
            "FAMILY_STATES_B85",
            "SSTAR_PACKED_B85",
        )
    )
    if not all(isinstance(value, str) for value in encoded):
        raise AssertionError("pinned fixture literals are missing")
    gate_raw, family_raw, target_raw = (
        zlib.decompress(base64.b85decode(value)) for value in encoded
    )
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros: list[tuple[Gate, ...]] = []
    for length in lengths:
        rows: list[Gate] = []
        for _ in range(length):
            rows.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(rows))
    pairs = lawful_pairs()
    keys = tuple(
        sorted(
            (event, pair)
            for event in range(4)
            for pair in pairs
        )
    )
    states = {
        key: int.from_bytes(
            family_raw[index * STATE_BYTES:(index + 1) * STATE_BYTES],
            "little",
        )
        for index, key in enumerate(keys)
    }
    target = int.from_bytes(target_raw, "little")
    exact = (
        sha256(source).hexdigest() == FIXTURE_SHA256
        and git_text("rev-parse", FIXTURE_SPEC) == FIXTURE_GIT_BLOB
        and sha256(gate_raw).hexdigest() == GATE_RAW_SHA256
        and sha256(family_raw).hexdigest() == FAMILY_RAW_SHA256
        and sha256(target_raw).hexdigest() == TARGET_PACKED_SHA256
        and len(lengths) == RING_STATIONS
        and sum(lengths) == GATE_COUNT
        and offset == len(gate_raw)
        and len(keys) == len(states) == 176
        and len(family_raw) == 176 * STATE_BYTES
        and len(target_raw) == STATE_BYTES
        and target.bit_count() == 44
    )
    return {
        "macros": tuple(macros),
        "keys": keys,
        "states": states,
        "target": target,
        "source_sha256": sha256(source).hexdigest(),
        "source_git_blob": git_text("rev-parse", FIXTURE_SPEC),
        "macro_lengths": lengths,
        "pass": exact,
    }


def source_controls() -> dict[str, object]:
    primary_payload = (ROOT / PRIMARY_PATH).read_bytes()
    primary_tree = ast.parse(primary_payload, filename=PRIMARY_PATH)
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    direct_imports = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in self_tree.body
        if isinstance(node, ast.ImportFrom)
        and node.module != "__future__"
    }
    primary_integers = integer_assignments(primary_tree)
    primary_claim_literals = {
        "DISCRIMINATOR_WIRES":
            literal_assignment(primary_tree, "DISCRIMINATOR_WIRES"),
        "DISCRIMINATOR_PATTERNS":
            literal_assignment(primary_tree, "DISCRIMINATOR_PATTERNS"),
        "EXPECTED_REACHING_KEYS":
            literal_assignment(primary_tree, "EXPECTED_REACHING_KEYS"),
        "SSTAR_BOUND_MOVEMENTS":
            literal_assignment(primary_tree, "SSTAR_BOUND_MOVEMENTS"),
        "SSTAR_BOUND_CONTROLLER_TICKS":
            primary_integers.get("SSTAR_BOUND_CONTROLLER_TICKS"),
        "MEET_CONTROLLER_TICK":
            literal_assignment(primary_tree, "MEET_CONTROLLER_TICK"),
    }
    literal_claims_exact = (
        primary_claim_literals["DISCRIMINATOR_WIRES"] == WIRES
        and primary_claim_literals["DISCRIMINATOR_PATTERNS"]
        == MARK_PATTERNS
        and primary_claim_literals["EXPECTED_REACHING_KEYS"]
        == MARKED_KEYS
        and primary_claim_literals["SSTAR_BOUND_MOVEMENTS"] == 14739
        and primary_claim_literals["SSTAR_BOUND_CONTROLLER_TICKS"]
        == FINAL_TICK
        and primary_claim_literals["MEET_CONTROLLER_TICK"] == MEET_TICK
    )
    worktree_rows = tuple(
        {
            "path": path,
            "exists": (ROOT / path).is_file(),
            "worktree_relative": not Path(path).is_absolute(),
        }
        for path in AUDIT_INPUT_PATHS
    )
    primary_sha = sha256(primary_payload).hexdigest()
    primary_blob = blob_id(primary_payload)
    blocked_loaded = tuple(
        sorted(
            name
            for name in sys.modules
            if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
        )
    )
    exact = (
        literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
        == AUDIT_INPUT_PATHS
        and all(
            row["exists"] and row["worktree_relative"]
            for row in worktree_rows
        )
        and primary_sha == PRIMARY_SHA256
        and primary_blob == PRIMARY_GIT_BLOB
        and literal_claims_exact
        and not (set(BLOCKLISTED_MODULES) & direct_imports)
        and not blocked_loaded
        and not FIREWALL.hits
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — Controls source intake is SHA-pinned, literal-path, "
            "text/AST-only, and BLOCKLIST-clean."
            if exact
            else
            "FAIL — Controls source intake or primary-version binding failed."
        ),
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "input_path_rows": worktree_rows,
        "declared_source_primary_count": 2,
        "read_cap": 6,
        "primary": {
            "path": PRIMARY_PATH,
            "access": "WORKTREE_TEXT_AST_ONLY_BLOCKLISTED",
            "sha256": primary_sha,
            "expected_sha256": PRIMARY_SHA256,
            "git_blob": primary_blob,
            "expected_git_blob": PRIMARY_GIT_BLOB,
        },
        "fixture_primary": {
            "spec": FIXTURE_SPEC,
            "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
            "expected_sha256": FIXTURE_SHA256,
            "expected_git_blob": FIXTURE_GIT_BLOB,
        },
        "primary_claim_literals": primary_claim_literals,
        "primary_claim_literals_exact": literal_claims_exact,
        "blocked_modules_loaded": blocked_loaded,
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_imports": tuple(sorted(direct_imports)),
        "git_head": git_text("rev-parse", "HEAD"),
        "git_branch": git_text("branch", "--show-current"),
        "pass": exact,
    }


def gate_semantics(
    gate: Gate,
) -> tuple[str, tuple[int, ...], int, str]:
    kind, first, second, third = gate
    if kind == 0:
        return "X", (), first, f"x[{first}] ^= 1"
    if kind == 1:
        return (
            "CNOT",
            (first,),
            second,
            f"x[{second}] ^= x[{first}]",
        )
    if kind == 2:
        return (
            "TOFFOLI",
            (first, second),
            third,
            f"x[{third}] ^= x[{first}] & x[{second}]",
        )
    raise AssertionError(("unknown gate kind", kind))


def derive_wire_dynamics(
    fixture: dict[str, object],
) -> dict[str, object]:
    macros = fixture["macros"]
    assert isinstance(macros, tuple)
    rows_by_wire: dict[int, tuple[dict[str, object], ...]] = {}
    details = []
    gates_well_formed = True
    for station, macro in enumerate(macros):
        for gate in macro:
            kind, controls, target, _formula = gate_semantics(gate)
            used = controls + (target,)
            gates_well_formed &= (
                kind in {"X", "CNOT", "TOFFOLI"}
                and all(0 <= wire < STATE_BITS for wire in used)
                and target not in controls
                and len(set(controls)) == len(controls)
            )
    for wire in WIRES:
        rows: list[dict[str, object]] = []
        for station, macro in enumerate(macros):
            for clause_index, gate in enumerate(macro):
                kind, controls, target, formula = gate_semantics(gate)
                roles = tuple(
                    role
                    for role, present in (
                        ("READ_CONTROL", wire in controls),
                        ("WRITE_TARGET", wire == target),
                    )
                    if present
                )
                if roles:
                    rows.append(
                        {
                            "station": station,
                            "clause_index_zero_based": clause_index,
                            "kind": kind,
                            "controls": controls,
                            "target": target,
                            "roles": roles,
                            "exact_update": formula,
                        }
                    )
        read_targets = tuple(
            sorted(
                {
                    int(row["target"])
                    for row in rows
                    if "READ_CONTROL" in row["roles"]
                }
            )
        )
        write_controls = tuple(
            sorted(
                {
                    int(control)
                    for row in rows
                    if "WRITE_TARGET" in row["roles"]
                    for control in row["controls"]
                }
            )
        )
        row_tuple = tuple(rows)
        rows_by_wire[wire] = row_tuple
        details.append(
            {
                "wire": wire,
                "read_clause_count": sum(
                    "READ_CONTROL" in row["roles"] for row in rows
                ),
                "write_clause_count": sum(
                    "WRITE_TARGET" in row["roles"] for row in rows
                ),
                "writable": any(
                    "WRITE_TARGET" in row["roles"] for row in rows
                ),
                "read_influence_targets": read_targets,
                "write_dependency_controls": write_controls,
                "one_macro_orbit_neighborhood": tuple(
                    sorted({wire, *read_targets, *write_controls})
                ),
                "touching_clause_applications_per_complete_movement":
                    2 * len(rows),
                "touching_rule_clauses": row_tuple,
            }
        )
    derivation_digest = object_digest(tuple(details))
    digest_exact = (
        not EXPECTED_WIRE_DERIVATION_DIGEST
        or derivation_digest == EXPECTED_WIRE_DERIVATION_DIGEST
    )
    exact = (
        fixture["pass"]
        and gates_well_formed
        and sum(len(macro) for macro in macros) == GATE_COUNT
        and all(row["writable"] for row in details)
        and all(row["touching_rule_clauses"] for row in details)
        and digest_exact
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — THE WIRE DYNAMICS: wires 40/81/105 are all writable; "
            "every read/write clause and its exact one-macro neighborhood "
            "was independently re-derived from all 3,106 gates."
            if exact
            else
            "FAIL — THE WIRE DYNAMICS: an exact clause, writability, "
            "neighborhood, or frozen-derivation check disagreed."
        ),
        "gate_semantics": (
            "X target ^= 1",
            "CNOT target ^= control",
            "TOFFOLI target ^= control_0 & control_1",
        ),
        "all_gates_well_formed": gates_well_formed,
        "macro_gate_count": sum(len(macro) for macro in macros),
        "two_token_gate_applications_per_complete_movement":
            2 * sum(len(macro) for macro in macros),
        "per_wire": tuple(details),
        "derivation_digest": derivation_digest,
        "expected_derivation_digest":
            EXPECTED_WIRE_DERIVATION_DIGEST or "TO_BE_FROZEN",
        "pass": exact,
    }


def fixture_digest(fixture: dict[str, object]) -> str:
    macros = fixture["macros"]
    keys = fixture["keys"]
    states = fixture["states"]
    target = fixture["target"]
    assert isinstance(macros, tuple)
    assert isinstance(keys, tuple)
    assert isinstance(states, dict)
    assert isinstance(target, int)
    hasher = sha256()
    for macro in macros:
        hasher.update(len(macro).to_bytes(2, "little"))
        for gate in macro:
            hasher.update(struct.pack("<BHHH", *gate))
    for key in keys:
        hasher.update(compact(key).encode())
        hasher.update(states[key].to_bytes(STATE_BYTES, "little"))
    hasher.update(target.to_bytes(STATE_BYTES, "little"))
    return hasher.hexdigest()


def bit_columns(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane, state in enumerate(states):
        remainder = state
        while remainder:
            bit = remainder & -remainder
            columns[bit.bit_length() - 1] |= 1 << lane
            remainder ^= bit
    return columns


def build_schedules(
    macros: tuple[tuple[Gate, ...], ...],
    lane_keys: tuple[Key, ...],
    target: int,
) -> tuple[tuple[ScheduledGate, ...], ...]:
    schedules = []
    for phase in range(RING_STATIONS):
        station_masks = [0] * RING_STATIONS
        for lane, (_event, pair) in enumerate(lane_keys):
            for source in pair:
                station_masks[(source + phase) % RING_STATIONS] |= 1 << lane
        rows: list[ScheduledGate] = []
        for station, mask in enumerate(station_masks):
            if not mask:
                continue
            for kind, first, second, third in macros[station]:
                target_wire = (
                    first if kind == 0 else second if kind == 1 else third
                )
                rows.append(
                    (
                        kind,
                        first,
                        second,
                        third,
                        mask,
                        (target >> target_wire) & 1,
                    )
                )
        schedules.append(tuple(rows))
    return tuple(schedules)


def unit_table(lane_count: int) -> tuple[int, ...]:
    units = [0] * (1 << lane_count)
    lane_units = tuple(1 << (16 * lane) for lane in range(lane_count))
    for mask in range(1, 1 << lane_count):
        bit = mask & -mask
        lane = bit.bit_length() - 1
        units[mask] = units[mask ^ bit] + lane_units[lane]
    return tuple(units)


def pack_counts(values: tuple[int, ...]) -> int:
    if any(not 0 <= value < (1 << 16) for value in values):
        raise AssertionError(("count outside packed field", values))
    return sum(value << (16 * lane) for lane, value in enumerate(values))


def unpack_counts(packed: int, lane_count: int) -> tuple[int, ...]:
    return tuple(
        (packed >> (16 * lane)) & 0xFFFF
        for lane in range(lane_count)
    )


def apply_schedule(
    columns: list[int],
    schedule: tuple[ScheduledGate, ...],
    tracked_mask: int,
    units: tuple[int, ...],
    packed_missing: int,
    packed_extra: int,
) -> tuple[int, int]:
    for kind, first, second, third, mask, target_bit in schedule:
        if kind == 0:
            target_wire = first
            toggles = mask
        elif kind == 1:
            target_wire = second
            toggles = columns[first] & mask
        elif kind == 2:
            target_wire = third
            toggles = columns[first] & columns[second] & mask
        else:
            raise AssertionError(("unknown gate kind", kind))
        tracked_toggles = toggles & tracked_mask
        if tracked_toggles:
            old_ones = columns[target_wire] & tracked_toggles
            new_ones = tracked_toggles ^ old_ones
            if target_bit:
                packed_missing += units[old_ones] - units[new_ones]
            else:
                packed_extra += units[new_ones] - units[old_ones]
        columns[target_wire] ^= toggles
    return packed_missing, packed_extra


def predicate_mask(columns: list[int], lane_mask: int) -> int:
    result = 0
    for pattern in MARK_PATTERNS:
        matches = lane_mask
        for wire, expected in zip(WIRES, pattern):
            ones = columns[wire] & lane_mask
            matches &= ones if expected else lane_mask ^ ones
        result |= matches
    return result


def lane_pattern(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((columns[wire] >> lane) & 1 for wire in WIRES)


def feature_mask(
    columns: list[int],
    support: tuple[int, ...],
    lane_mask: int,
) -> int:
    value = 0
    for wire in support:
        value ^= columns[wire]
    return value & lane_mask


def exact_match_mask(
    columns: list[int],
    target: int,
    lane_mask: int,
    signature: tuple[int, ...],
) -> int:
    candidates = lane_mask
    for wire in signature:
        ones = columns[wire] & lane_mask
        candidates &= ones if (target >> wire) & 1 else lane_mask ^ ones
        if not candidates:
            return 0
    for wire in range(STATE_BITS):
        ones = columns[wire] & lane_mask
        candidates &= ones if (target >> wire) & 1 else lane_mask ^ ones
        if not candidates:
            return 0
    return candidates


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def derive_local_neighborhood(
    wire_certificate: dict[str, object],
) -> tuple[int, ...]:
    per_wire = wire_certificate["per_wire"]
    assert isinstance(per_wire, tuple)
    return tuple(
        sorted(
            {
                int(wire)
                for row in per_wire
                for wire in row["one_macro_orbit_neighborhood"]
            }
        )
    )


def run_evolution(
    fixture: dict[str, object],
    wire_certificate: dict[str, object],
) -> dict[str, object]:
    macros = fixture["macros"]
    all_keys = fixture["keys"]
    state_map = fixture["states"]
    target = fixture["target"]
    assert isinstance(macros, tuple)
    assert isinstance(all_keys, tuple)
    assert isinstance(state_map, dict)
    assert isinstance(target, int)

    s5_keys = tuple(
        key for key in all_keys if cyclic_separation(key[1]) == 5
    )
    controls = tuple(key for key in s5_keys if key not in MARKED_KEYS)
    lane_keys = MARKED_KEYS + controls
    lane_count = len(lane_keys)
    if lane_count != 44 or len(controls) != 35:
        raise AssertionError(("unexpected s=5 census", lane_count, controls))
    control_sample = controls[:CONTROL_SAMPLE_SIZE]
    tracked_count = len(MARKED_KEYS) + len(control_sample)
    tracked_mask = (1 << tracked_count) - 1
    primary_mask = (1 << lane_count) - 1
    duplicate_mask = primary_mask << lane_count
    marked_mask = (1 << len(MARKED_KEYS)) - 1
    control_mask = primary_mask ^ marked_mask

    doubled_keys = lane_keys + lane_keys
    doubled_states = tuple(state_map[key] for key in doubled_keys)
    columns = bit_columns(doubled_states)
    schedules = build_schedules(macros, doubled_keys, target)
    schedule_duplicate_exact = all(
        ((mask & duplicate_mask) >> lane_count)
        == (mask & primary_mask)
        for schedule in schedules
        for _kind, _first, _second, _third, mask, _target_bit in schedule
    )
    per_lane_movement_rows = tuple(
        sum(
            len(macros[(source + phase) % RING_STATIONS])
            for phase in range(RING_STATIONS)
            for source in pair
        )
        for _event, pair in lane_keys
    )
    if set(per_lane_movement_rows) != {MOVEMENT_GATE_COUNT}:
        raise AssertionError(
            ("per-lane movement gate count", set(per_lane_movement_rows))
        )

    tracked_states = doubled_states[:tracked_count]
    missing_values = tuple(
        (target & ~state).bit_count() for state in tracked_states
    )
    extra_values = tuple(
        (state & ~target).bit_count() for state in tracked_states
    )
    packed_missing = pack_counts(missing_values)
    packed_extra = pack_counts(extra_values)
    units = unit_table(tracked_count)

    target_ones = tuple(
        wire for wire in range(STATE_BITS) if (target >> wire) & 1
    )
    signature = tuple(
        sorted(
            set(target_ones)
            | {
                index * (STATE_BITS - 1) // 127
                for index in range(128)
            }
        )
    )
    hit_ticks: dict[Key, list[int]] = {key: [] for key in lane_keys}
    duplicate_checkpoints = []
    meet_patterns: tuple[tuple[int, ...], ...] | None = None
    meet_predicate: int | None = None
    first_pattern_counterexample: dict[str, object] | None = None
    first_predicate_counterexample: dict[str, object] | None = None
    first_marked_hamming_counterexample: dict[str, object] | None = None
    first_control_hamming_counterexample: dict[str, object] | None = None
    previous_missing: tuple[int, ...] | None = None
    previous_extra: tuple[int, ...] | None = None
    active_marked_mask = marked_mask

    local_neighborhood = derive_local_neighborhood(wire_certificate)
    parity_initial: tuple[tuple[int, ...], ...] = ()
    parity_survivors: list[tuple[int, ...]] = []
    parity_meet_values: dict[tuple[int, ...], int] = {}
    parity_first_elimination: dict[str, object] | None = None

    weight_initial = tuple(
        (left, right)
        for left in range(1, 17)
        for right in range(1, 17)
        if gcd(left, right) == 1
    )
    weight_survivors = list(weight_initial)
    weight_first_elimination: dict[str, object] | None = None
    weight_control_violation_masks = {
        weight: 0 for weight in weight_initial
    }

    for tick in range(1, FINAL_TICK + 1):
        packed_missing, packed_extra = apply_schedule(
            columns,
            schedules[(tick - 1) % RING_STATIONS],
            tracked_mask,
            units,
            packed_missing,
            packed_extra,
        )
        matches = exact_match_mask(
            columns, target, primary_mask, signature
        )
        for lane in lane_numbers(matches):
            hit_ticks[lane_keys[lane]].append(tick)

        if tick in (MEET_TICK, COUNTER_WINDOW_END, FINAL_TICK):
            duplicate_checkpoints.append(
                {
                    "controller_tick": tick,
                    "all_44_exact": all(
                        (column & primary_mask)
                        == ((column & duplicate_mask) >> lane_count)
                        for column in columns
                    ),
                }
            )

        current_missing = unpack_counts(packed_missing, tracked_count)
        current_extra = unpack_counts(packed_extra, tracked_count)
        if tick == MEET_TICK:
            meet_patterns = tuple(
                lane_pattern(columns, lane) for lane in range(lane_count)
            )
            meet_predicate = predicate_mask(columns, primary_mask)
            previous_missing = current_missing
            previous_extra = current_extra
            supports = tuple((wire,) for wire in local_neighborhood) + tuple(
                combinations(local_neighborhood, 2)
            )
            selected = []
            for support in supports:
                value = feature_mask(columns, support, primary_mask)
                marked_value = value & marked_mask
                control_value = value & control_mask
                marked_constant = marked_value in (0, marked_mask)
                control_constant = control_value in (0, control_mask)
                opposite = bool(marked_value) != bool(control_value)
                if marked_constant and control_constant and opposite:
                    selected.append(support)
                    parity_meet_values[support] = value
            parity_initial = tuple(selected)
            parity_survivors = list(selected)
            continue

        if tick < MEET_TICK:
            continue
        if (
            meet_patterns is None
            or meet_predicate is None
            or previous_missing is None
            or previous_extra is None
        ):
            raise AssertionError("meet snapshot not initialized")

        current_predicate = predicate_mask(columns, primary_mask)
        if first_pattern_counterexample is None:
            for lane in range(len(MARKED_KEYS)):
                pattern = lane_pattern(columns, lane)
                if pattern != meet_patterns[lane]:
                    first_pattern_counterexample = {
                        "key": lane_keys[lane],
                        "controller_tick": tick,
                        "from": meet_patterns[lane],
                        "to": pattern,
                    }
                    break
        if first_predicate_counterexample is None:
            changed = (current_predicate ^ meet_predicate) & marked_mask
            if changed:
                lane = lane_numbers(changed)[0]
                first_predicate_counterexample = {
                    "key": lane_keys[lane],
                    "controller_tick": tick,
                    "from": bool((meet_predicate >> lane) & 1),
                    "to": bool((current_predicate >> lane) & 1),
                    "pattern": lane_pattern(columns, lane),
                }

        for lane in range(tracked_count):
            before = previous_missing[lane] + previous_extra[lane]
            after = current_missing[lane] + current_extra[lane]
            if after <= before:
                continue
            row = {
                "key": lane_keys[lane],
                "from_tick": tick - 1,
                "to_tick": tick,
                "from_distance": before,
                "to_distance": after,
                "increase": after - before,
            }
            if (
                lane < len(MARKED_KEYS)
                and first_marked_hamming_counterexample is None
            ):
                first_marked_hamming_counterexample = row
            elif (
                lane >= len(MARKED_KEYS)
                and first_control_hamming_counterexample is None
            ):
                first_control_hamming_counterexample = row

        active_for_invariant = control_mask | active_marked_mask
        if parity_survivors:
            retained = []
            for support in parity_survivors:
                value = feature_mask(columns, support, primary_mask)
                if (
                    (value ^ parity_meet_values[support])
                    & active_for_invariant
                ) == 0:
                    retained.append(support)
                elif parity_first_elimination is None:
                    parity_first_elimination = {
                        "support": support,
                        "controller_tick": tick,
                    }
            parity_survivors = retained

        if weight_survivors:
            retained_weights = []
            for weight in weight_survivors:
                left, right = weight
                monotone_on_active_marked = all(
                    left * (
                        current_missing[lane] - previous_missing[lane]
                    )
                    + right * (
                        current_extra[lane] - previous_extra[lane]
                    )
                    <= 0
                    for lane in lane_numbers(active_marked_mask)
                )
                if monotone_on_active_marked:
                    retained_weights.append(weight)
                    violations = weight_control_violation_masks[weight]
                    for lane in range(
                        len(MARKED_KEYS), tracked_count
                    ):
                        delta = (
                            left
                            * (
                                current_missing[lane]
                                - previous_missing[lane]
                            )
                            + right
                            * (
                                current_extra[lane]
                                - previous_extra[lane]
                            )
                        )
                        if delta > 0:
                            violations |= 1 << (
                                lane - len(MARKED_KEYS)
                            )
                    weight_control_violation_masks[weight] = violations
                elif weight_first_elimination is None:
                    weight_first_elimination = {
                        "weight_missing": left,
                        "weight_extra": right,
                        "controller_tick": tick,
                    }
            weight_survivors = retained_weights

        active_marked_mask &= ~matches
        previous_missing = current_missing
        previous_extra = current_extra

    if meet_patterns is None or meet_predicate is None:
        raise AssertionError("meet snapshot absent")
    return {
        "lane_keys": lane_keys,
        "controls": controls,
        "control_sample": control_sample,
        "hit_ticks": {
            key: tuple(ticks) for key, ticks in hit_ticks.items()
        },
        "meet_patterns": meet_patterns,
        "meet_predicate": meet_predicate,
        "first_pattern_counterexample": first_pattern_counterexample,
        "first_predicate_counterexample": first_predicate_counterexample,
        "first_marked_hamming_counterexample":
            first_marked_hamming_counterexample,
        "first_control_hamming_counterexample":
            first_control_hamming_counterexample,
        "schedules": schedules,
        "schedule_duplicate_exact": schedule_duplicate_exact,
        "duplicate_checkpoints": tuple(duplicate_checkpoints),
        "per_lane_movement_gate_rows":
            tuple(sorted(set(per_lane_movement_rows))),
        "local_neighborhood": local_neighborhood,
        "parity_initial": parity_initial,
        "parity_survivors": tuple(parity_survivors),
        "parity_first_elimination": parity_first_elimination,
        "weight_initial": weight_initial,
        "weight_survivors": tuple(weight_survivors),
        "weight_first_elimination": weight_first_elimination,
        "weight_control_violation_masks": {
            weight: weight_control_violation_masks[weight]
            for weight in weight_survivors
        },
    }


def bounded_theorem_certificate(
    evolution: dict[str, object],
) -> dict[str, object]:
    hit_ticks = evolution["hit_ticks"]
    controls = evolution["controls"]
    meet_predicate = evolution["meet_predicate"]
    assert isinstance(hit_ticks, dict)
    assert isinstance(controls, tuple)
    assert isinstance(meet_predicate, int)
    marked_rows = tuple(
        {
            "key": key,
            "meet_pattern":
                evolution["meet_patterns"][lane],
            "exact_Sstar_hit_ticks": hit_ticks[key],
            "first_hit_distance_from_meet": (
                hit_ticks[key][0] - MEET_TICK
                if hit_ticks[key] else None
            ),
        }
        for lane, key in enumerate(MARKED_KEYS)
    )
    control_rows = tuple(
        {
            "key": key,
            "meet_pattern":
                evolution["meet_patterns"][len(MARKED_KEYS) + lane],
            "exact_Sstar_hit_ticks": hit_ticks[key],
        }
        for lane, key in enumerate(controls)
    )
    marked_predicate_exact = (
        meet_predicate & ((1 << len(MARKED_KEYS)) - 1)
    ) == ((1 << len(MARKED_KEYS)) - 1)
    controls_predicate_exact = (
        meet_predicate >> len(MARKED_KEYS)
    ) == 0
    all_marked_reach = all(
        row["first_hit_distance_from_meet"] is not None
        and 0 <= row["first_hit_distance_from_meet"] <= BOUND_B
        for row in marked_rows
    )
    no_control_reaches = all(
        not row["exact_Sstar_hit_ticks"] for row in control_rows
    )
    exact = (
        marked_predicate_exact
        and controls_predicate_exact
        and all_marked_reach
        and no_control_reaches
        and len(marked_rows) == 9
        and len(control_rows) == 35
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — THE BOUNDED THEOREM: all 9 declared marked meets reach "
            "exact S* within B=162126, while all 35 declared controls do not."
            if exact
            else
            "FAIL — THE BOUNDED THEOREM: the independent 9/35 census "
            "contains a predicate, reachability, exact-target, or bound "
            "disagreement."
        ),
        "declared_marked_sample": {
            "rule": "all nine primary-declared marked s=5 meet keys",
            "size": len(marked_rows),
            "rows": marked_rows,
        },
        "declared_control_sample": {
            "rule": "all remaining 35 members of the landed s=5 census",
            "size": len(control_rows),
            "rows": control_rows,
        },
        "antecedent_exact_on_sample": (
            marked_predicate_exact and controls_predicate_exact
        ),
        "target_definition": {
            "state_bits": STATE_BITS,
            "hamming_weight": 44,
            "packed_sha256": TARGET_PACKED_SHA256,
        },
        "meet_controller_tick": MEET_TICK,
        "bound_B_controller_ticks": BOUND_B,
        "final_controller_tick": FINAL_TICK,
        "comparison": "exact packed 5815-bit equality at every tick",
        "all_marked_reach": all_marked_reach,
        "no_control_reaches": no_control_reaches,
        "pass": exact,
    }


def failure_verification_certificate(
    evolution: dict[str, object],
) -> dict[str, object]:
    pattern_counterexample = evolution["first_pattern_counterexample"]
    predicate_counterexample = evolution["first_predicate_counterexample"]
    hamming_counterexample = (
        evolution["first_marked_hamming_counterexample"]
    )
    exact = (
        pattern_counterexample is not None
        and predicate_counterexample is not None
        and hamming_counterexample is not None
    )
    return {
        "status": "PASS" if exact else "FAIL",
        "finding": (
            "PASS — THE FAILURE VERIFICATION: the three-wire word and "
            "Boolean predicate both change after the meet, and Hamming "
            "distance to exact S* has a marked-lane one-tick increase."
            if exact
            else
            "FAIL — THE FAILURE VERIFICATION: at least one claimed "
            "conservation/monotonicity failure was not reproduced."
        ),
        "three_wire_word_conservation_counterexample":
            pattern_counterexample,
        "Boolean_D_conservation_counterexample":
            predicate_counterexample,
        "marked_Hamming_monotonicity_counterexample":
            hamming_counterexample,
        "control_Hamming_monotonicity_counterexample":
            evolution["first_control_hamming_counterexample"],
        "Hamming_counterexample_search_window": (
            MEET_TICK,
            FINAL_TICK,
        ),
        "pass": exact,
    }


def constructive_hunt_certificate(
    evolution: dict[str, object],
) -> dict[str, object]:
    parity_survivors = evolution["parity_survivors"]
    weight_survivors = evolution["weight_survivors"]
    assert isinstance(parity_survivors, tuple)
    assert isinstance(weight_survivors, tuple)
    local_find = bool(parity_survivors)
    global_find = bool(weight_survivors)
    outcome = (
        "FIND_LOCAL_AFFINE_PARITY_INVARIANT"
        if local_find
        else (
            "FIND_GLOBAL_WEIGHTED_DEFECT_MONOTONE"
            if global_find
            else "BOTH_DECLARED_CLASSES_EXHAUSTED"
        )
    )
    if local_find:
        finding = (
            "PASS — THE CONSTRUCTIVE HUNT: FIND; a support-1/2 affine "
            "parity separator from the exact one-macro neighborhood survives "
            "the full 44-lane bounded census, upgrading the partial theorem."
        )
    elif global_find:
        finding = (
            "PASS — THE CONSTRUCTIVE HUNT: FIND; a positive weighted "
            "(missing-target, extra-target) defect is nonincreasing on all "
            "9 marked trajectories through first S*, upgrading the bounded "
            "theorem while leaving strict locality open."
        )
    else:
        finding = (
            "PASS — THE CONSTRUCTIVE HUNT: both declared classes are "
            "exhausted on their exact finite domains; no new invariant or "
            "monotone was found, tightening but not closing the open link."
        )
    negative_scope_gate = {
        "status": "UNIVERSAL_NO_GO_FAIL__HONEST_OPEN_SCOPE_PASS",
        "N1_alternative_routes": (
            {
                "family": "three-wire Boolean predicate conservation",
                "marker": "ATTEMPTED",
                "result":
                    "falsified by the reproduced Boolean-D counterexample",
            },
            {
                "family": "raw exact-target Hamming descent",
                "marker": "ATTEMPTED",
                "result":
                    "falsified by the reproduced one-tick increase",
            },
            {
                "family": "support-1/2 local affine GF(2) separator",
                "marker": "ATTEMPTED",
                "result":
                    "exhausted exactly on the declared finite domain",
            },
            {
                "family": "positive asymmetric weighted target defect",
                "marker": "ATTEMPTED",
                "result":
                    "exhausted exactly for weights 1..16 on all marked lanes",
            },
            {
                "family":
                    "higher-degree nonlinear light-cone predicate or "
                    "phase-lifted local Lyapunov function",
                "marker": "UNTESTED",
                "result":
                    "concrete reopen route; forbids a universal no-go",
            },
        ),
        "N2_wall_independence":
            "one open link only; no inflated independent-wall count",
        "N3_hidden_wall_scan":
            "candidate degree, support, weight, and finite-domain limits are "
            "explicit rather than hidden",
        "N4_residual_matching":
            "no prior no-go witness is used to close the present residual",
        "N5_rhetoric_audit":
            "no resolution-independent impossibility claim is made",
        "N6_partial_closure":
            "no new-axiom claim is made; computational candidate routes "
            "remain admissible",
        "N7_steelman":
            "A nonlinear Boolean observable on a deeper causal cone, or a "
            "phase-lifted potential that permits within-phase backtracking, "
            "could still connect the meet flag to S* without lookahead.",
        "N8_cross_cycle_echo":
            "not used as negative evidence under the six-file cap; the "
            "universal negative is expressly withheld",
        "conclusion":
            "The two exact exhaustion results tighten only their declared "
            "classes.  They do not establish that no non-lookahead local "
            "causal link exists.",
    }
    return {
        "status": "PASS",
        "finding": finding,
        "outcome": outcome,
        "candidate_class_1": {
            "name":
                "support-1/2 affine GF(2) parity separators on the union "
                "of the three exact one-macro orbit neighborhoods",
            "domain":
                "all 44 s=5 trajectories, meet tick through marked first "
                "hit or control bound",
            "local_neighborhood": evolution["local_neighborhood"],
            "initial_separator_count": len(evolution["parity_initial"]),
            "survivor_count": len(parity_survivors),
            "survivors": parity_survivors,
            "first_elimination": evolution["parity_first_elimination"],
            "result": "FIND" if local_find else "EXHAUSTED",
        },
        "candidate_class_2": {
            "name":
                "positive coprime weighted target-defect potentials "
                "a*missing_target_ones+b*extra_ones, 1<=a,b<=16",
            "domain":
                "all 9 marked trajectories at every controller tick from "
                "meet through first exact S* hit",
            "candidate_count": len(evolution["weight_initial"]),
            "survivor_count": len(weight_survivors),
            "survivors": tuple(
                {
                    "weight_missing": weight[0],
                    "weight_extra": weight[1],
                    "sampled_control_increase_mask":
                        evolution["weight_control_violation_masks"][weight],
                }
                for weight in weight_survivors
            ),
            "first_elimination": evolution["weight_first_elimination"],
            "result": "FIND" if global_find else "EXHAUSTED",
        },
        "upgrade_scope": (
            "exact finite local separator on the full 44-member census"
            if local_find
            else (
                "exact finite global non-lookahead monotone on all nine "
                "marked trajectories; not a local causal derivation"
                if global_find
                else "none; exhaustion is class- and domain-bounded"
            )
        ),
        "negative_scope_gate": negative_scope_gate,
        "pass": True,
    }


def scientific_disposition(
    wire: dict[str, object],
    bounded: dict[str, object],
    failures: dict[str, object],
    hunt: dict[str, object],
) -> tuple[str, bool]:
    primary_core = (
        wire["pass"] and bounded["pass"] and failures["pass"]
    )
    if not primary_core:
        failed = tuple(
            name
            for name, certificate in (
                ("THE WIRE DYNAMICS", wire),
                ("THE BOUNDED THEOREM", bounded),
                ("THE FAILURE VERIFICATION", failures),
            )
            if not certificate["pass"]
        )
        return (
            "PRIMARY_REFUTED_BY_" + "_AND_".join(
                name.replace(" ", "_") for name in failed
            ),
            True,
        )
    if hunt["outcome"] == "FIND_LOCAL_AFFINE_PARITY_INVARIANT":
        return (
            "PRIMARY_PARTIAL_OPEN_LINK_UPGRADED_BY_EXACT_LOCAL_"
            "INVARIANT_CANDIDATE",
            False,
        )
    if hunt["outcome"] == "FIND_GLOBAL_WEIGHTED_DEFECT_MONOTONE":
        return (
            "PRIMARY_BOUNDED_THEOREM_UPGRADED_BY_EXACT_GLOBAL_MONOTONE_"
            "CANDIDATE_LOCAL_LINK_STILL_OPEN",
            False,
        )
    return (
        "PRIMARY_NOT_REFUTED_EXACT_FINITE_CLAIMS_CONFIRMED_"
        "OPEN_LINK_REMAINS_CLASS_BOUNDED",
        False,
    )


def controls_certificate(
    source: dict[str, object],
    fixture: dict[str, object],
    replay: dict[str, object],
    evolution: dict[str, object],
    elapsed: float,
) -> dict[str, object]:
    blocked_loaded = tuple(
        sorted(
            name
            for name in sys.modules
            if name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
        )
    )
    first_digest = fixture_digest(fixture)
    replay_digest = fixture_digest(replay)
    replay_exact = (
        first_digest == replay_digest
        and fixture["macro_lengths"] == replay["macro_lengths"]
        and fixture["source_sha256"] == replay["source_sha256"]
        and fixture["source_git_blob"] == replay["source_git_blob"]
    )
    duplicate_exact = (
        evolution["schedule_duplicate_exact"]
        and all(
            row["all_44_exact"]
            for row in evolution["duplicate_checkpoints"]
        )
    )
    base_pass = (
        source["pass"]
        and fixture["pass"]
        and replay["pass"]
        and replay_exact
        and duplicate_exact
        and not blocked_loaded
        and not FIREWALL.hits
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    return {
        "status": "PASS" if base_pass else "FAIL",
        "finding": (
            "PASS — Controls: source SHAs and literal paths are exact; "
            "primaries stayed BLOCKLISTED; duplicate replay is deterministic; "
            "runtime and stdout are bounded."
            if base_pass
            else
            "FAIL — Controls: provenance, BLOCKLIST, determinism, runtime, "
            "or output accounting failed."
        ),
        "source_controls": source,
        "fixture": {
            "source_sha256": fixture["source_sha256"],
            "source_git_blob": fixture["source_git_blob"],
            "decoded_fixture_digest": first_digest,
            "replay_fixture_digest": replay_digest,
            "exact_replay": replay_exact,
        },
        "BLOCKLIST": {
            "modules": BLOCKLISTED_MODULES,
            "policy": "TEXT_AST_ONLY; NEVER IMPORT OR EXECUTE",
            "loaded_at_end": blocked_loaded,
            "firewall_hits": tuple(FIREWALL.hits),
        },
        "determinism": {
            "duplicate_schedule_masks_exact":
                evolution["schedule_duplicate_exact"],
            "duplicate_state_checkpoints":
                evolution["duplicate_checkpoints"],
            "duplicate_replay_exact": duplicate_exact,
        },
        "per_lane_gate_rows_per_complete_movement":
            evolution["per_lane_movement_gate_rows"],
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "observed_runtime_seconds": round(elapsed, 6),
        "runtime_below_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "observed_stdout_bytes": 0,
        "stdout_below_limit": False,
        "base_pass_before_stdout_check": base_pass,
        "pass": False,
    }


def stable_render(report: dict[str, object]) -> str:
    controls = report["certificates"]["Controls"]
    assert isinstance(controls, dict)
    prior_size = -1
    for _ in range(12):
        rendered = compact(report)
        size = len(rendered.encode()) + 1
        controls["observed_stdout_bytes"] = size
        controls["stdout_below_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = (
            controls["base_pass_before_stdout_check"]
            and controls["stdout_below_limit"]
        )
        controls["status"] = "PASS" if controls["pass"] else "FAIL"
        report["overall_pass"] = controls["pass"]
        if size == prior_size:
            break
        prior_size = size
    final = compact(report)
    if len(final.encode()) + 1 != controls["observed_stdout_bytes"]:
        raise AssertionError("stdout accounting did not stabilize")
    return final


def run() -> int:
    started = monotonic()
    source = source_controls()
    fixture = decode_fixture()
    wire = derive_wire_dynamics(fixture)
    evolution = run_evolution(fixture, wire)
    bounded = bounded_theorem_certificate(evolution)
    failures = failure_verification_certificate(evolution)
    hunt = constructive_hunt_certificate(evolution)
    disposition, primary_refuted = scientific_disposition(
        wire, bounded, failures, hunt
    )
    replay = decode_fixture()
    elapsed = monotonic() - started
    controls = controls_certificate(
        source, fixture, replay, evolution, elapsed
    )
    report = {
        "cycle": 842,
        "checker": "INDEPENDENT ADVERSARIAL CHECKER — honest bounds",
        "scientific_disposition": disposition,
        "primary_refuted": primary_refuted,
        "certificates": {
            "THE WIRE DYNAMICS": wire,
            "THE BOUNDED THEOREM": bounded,
            "THE FAILURE VERIFICATION": failures,
            "THE CONSTRUCTIVE HUNT": hunt,
            "Controls": controls,
        },
        "scope_statement":
            "Exact full 9/35 landed s=5 finite census for reachability; "
            "constructive conclusions remain limited to the two explicitly "
            "enumerated candidate classes and their declared domains.",
        "overall_pass": False,
    }
    rendered = stable_render(report)
    if len(rendered.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    print(rendered)
    return 0 if report["overall_pass"] else 1


def main() -> int:
    started = monotonic()
    code = run()
    if monotonic() - started >= AUDIT_TIMEOUT_SEC:
        raise AssertionError("runtime limit exceeded")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
