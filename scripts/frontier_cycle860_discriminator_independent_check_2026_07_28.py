#!/usr/bin/env python3
"""Cycle 860 independent adversarial checker: the readout discriminator.

The Cycle-852 and Cycle-860 primaries are SHA-pinned text/AST provenance
surfaces only.  Dynamics are rebuilt from the Cycle-719 core.  This checker
uses an aggregate clean mask and integer snapshot encoding, neither of which
is the primary's coordinate-by-coordinate predicate/snapshot machinery.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Callable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle852_selection_tournament_2026_07_28.py",
    "scripts/frontier_cycle860_readout_discriminator_2026_07_28.py",
)
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "fcb1e5ad22e48dc865754bc0a0f5357cdef8e78b477c21f48b74e5971eaa8419",
    AUDIT_INPUT_PATHS[2]:
        "28a62fb0bc83ec7a46c18901158693344a84cc1eff8c0c9537b40d9004d8b926",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "d584154f32ead0a03a9661c6f176d52b2a1a77dc",
    AUDIT_INPUT_PATHS[2]: "b48450fbe70f152bfeaab561a12591a2ec7d48c0",
}

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
TRAJECTORY_HORIZON = 51_115
EXPECTED_PRIMARY_CONTENT_DIGEST = (
    "f77c04f33b5c596a0bb5f80e3fa685ddee8b4497069470da6cc34a23a4616150"
)
EXPECTED_PRIMARY_WITNESS_KEY = (2, 0, (0, 2))

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _TextOnlyFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST text/AST-only source: {fullname}")
        return None


FIREWALL = _TextOnlyFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]
Content = int


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(t, ast.Name) and t.id == name for t in node.targets):
                values.append(node.value)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                values.append(node.value)
    if len(values) != 1:
        return None
    try:
        return ast.literal_eval(values[0])
    except (TypeError, ValueError):
        return None


def function_source(text: str, tree: ast.Module, name: str) -> str:
    nodes = [
        node for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == name
    ]
    if len(nodes) != 1:
        return ""
    return ast.get_source_segment(text, nodes[0]) or ""


def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    texts = {
        path: payload.decode("utf-8") for path, payload in payloads.items()
    }
    trees = {
        path: ast.parse(text, filename=path) for path, text in texts.items()
    }
    self_text = Path(__file__).read_text(encoding="utf-8")
    self_tree = ast.parse(self_text, filename=Path(__file__).name)
    primary_tree = trees[AUDIT_INPUT_PATHS[2]]
    primary_content_digest_nodes = [
        value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Dict)
        for key, value in zip(node.keys, node.values)
        if isinstance(key, ast.Constant) and key.value == "content_digest"
        and isinstance(value, ast.Call)
        and isinstance(value.func, ast.Name) and value.func.id == "digest"
    ]
    primary_cert_c = function_source(
        texts[AUDIT_INPUT_PATHS[2]], primary_tree, "certificate_c"
    )
    core_held = function_source(
        texts[CORE_PATH], trees[CORE_PATH], "held_certificate"
    )
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    sha_rows = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_input_paths":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "parsed_top_level_counts": {
            path: len(tree.body) for path, tree in trees.items()
        },
        "blocked_modules_loaded": tuple(
            module for module in BLOCKLISTED_MODULES if module in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "primary_declared_inputs": literal_assignment(
            primary_tree, "AUDIT_INPUT_PATHS"
        ),
        "primary_content_digest_AST_count": len(primary_content_digest_nodes),
        "primary_witness_rule_AST": "key = e1_only[0]" in primary_cert_c,
        "core_direction_convention_AST": (
            "direction = (1, 0) if event % 2 == 0 else (0, 1)" in core_held
            and "orientation=1 if direction == (1, 0) else -1" in core_held
        ),
    }
    result["pass"] = bool(
        result["literal_input_paths"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and all(result["parsed_top_level_counts"].values())
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and result["primary_declared_inputs"] == AUDIT_INPUT_PATHS[:2]
        and len(primary_content_digest_nodes) == 1
        and result["primary_witness_rule_AST"]
        and result["core_direction_convention_AST"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def nonadjacent_cycle(positions: tuple[int, ...], stations: int) -> bool:
    mask = sum(1 << position for position in positions)
    rotated = ((mask << 1) | (mask >> (stations - 1))) & ((1 << stations) - 1)
    return not (mask & rotated)


def event_seeds(program) -> tuple[tuple[int, State], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    seeds = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if after != K.A.apply_semantic(before, allocator):
            raise AssertionError(("event seed semantic mismatch", event))
        if rail_a != (1,) + (0,) * (len(program) - 1) or any(rail_b):
            raise AssertionError(("event seed rail mismatch", event))
        if len(trace) != len(program):
            raise AssertionError(("event seed trace mismatch", event))
        seeds.append((event, before))
        state = after
    return tuple(seeds)


def census_fixture():
    program = K.interleaved_program(FIXTURE_BANKS)
    seeds = event_seeds(program)
    placements = tuple(
        positions
        for count in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(len(program)), count)
        if nonadjacent_cycle(positions, len(program))
    )
    keys = tuple(sorted(
        (len(positions), event, positions)
        for positions in placements
        for event, _state in seeds
    ))
    if len(keys) != len(set(keys)):
        raise AssertionError("duplicate census key")
    return program, seeds, keys


def synchronous_action(program, positions: tuple[int, ...]):
    moving = positions
    gates = []
    for _ in program:
        live = set(moving)
        gates.extend(
            gate
            for station, row in enumerate(program)
            if station in live
            for gate in K.mapped_macro(row)
        )
        moving = tuple((station + 1) % len(program) for station in moving)
    return tuple(gates)


def initial_states(program, seeds, census):
    by_event = dict(seeds)
    word_by_positions = {
        positions: synchronous_action(program, positions)
        for _count, _event, positions in census
    }
    states = []
    failures = 0
    for count, event, positions in census:
        before = by_event[event]
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(station in positions) for station in range(len(program))
        )
        failures += int(
            after != K.A.apply_semantic(before, word_by_positions[positions])
        )
        failures += int(rail_a != expected_rail or any(rail_b))
        restored, inverse_a, inverse_b, _trace = K.run_orbit(
            after, program, token_positions=positions, reverse=True
        )
        failures += int(
            restored != before or inverse_a != rail_a or inverse_b != rail_b
        )
        failures += int(count != len(positions))
        states.append(after)
    return tuple(states), failures


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


def aggregate_dirty_coordinates() -> tuple[int, ...]:
    """Assemble the clean predicate in one structural pack.

    The primary separately marks every local coordinate and differences it
    against a baseline.  Here all forbidden bank and link fields are set at
    once, packed once, and checked by an independent population invariant.
    """

    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    dirty_banks = []
    for bank in banks0:
        row = [0] * len(bank)
        for wire in watched_bank_wires():
            row[wire] = 1
        dirty_banks.append(tuple(row))
    dirty_links = tuple(tuple(1 for _bit in link) for link in links0)
    aggregate = K.M.pack_state(tuple(dirty_banks), dirty_links)
    coordinates = {
        index for index, value in enumerate(aggregate) if value
    } | {K.R3.X.SOURCE_POINTER}
    expected_population = (
        FIXTURE_BANKS * len(set(watched_bank_wires()))
        + sum(map(len, links0))
        + 1
    )
    if len(coordinates) != expected_population:
        raise AssertionError((
            "aggregate clean-coordinate population",
            len(coordinates),
            expected_population,
        ))
    return tuple(sorted(coordinates))


def pack_columns(states: tuple[State, ...]) -> list[int]:
    columns = [0] * len(states[0])
    for lane, state in enumerate(states):
        lane_bit = 1 << lane
        for wire, value in enumerate(state):
            if value:
                columns[wire] |= lane_bit
    return columns


def compiled_schedules(program, keys: tuple[Key, ...]) -> tuple[Callable, ...]:
    functions = []
    for step in range(len(program)):
        rows: list[tuple[str, tuple[int, ...], int]] = []
        for station, program_row in enumerate(program):
            active = sum(
                1 << lane
                for lane, (_count, _event, positions) in enumerate(keys)
                if (station - step) % len(program) in positions
            )
            if active:
                rows.extend(
                    (gate.kind, gate.wires, active)
                    for gate in K.mapped_macro(program_row)
                )
        source = ["def advance(columns):"]
        for kind, wires, active in rows:
            if kind == "X":
                source.append(f" columns[{wires[0]}] ^= {active}")
            elif kind == "CNOT":
                source.append(
                    f" columns[{wires[1]}] ^= columns[{wires[0]}] & {active}"
                )
            elif kind == "TOF":
                source.append(
                    f" columns[{wires[2]}] ^= "
                    f"columns[{wires[0]}] & columns[{wires[1]}] & {active}"
                )
            else:
                raise ValueError(("unsupported core gate", kind, wires))
        namespace: dict[str, object] = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        functions.append(namespace["advance"])
    return tuple(functions)


def clean_lanes(columns: list[int], dirty: tuple[int, ...], lane_mask: int) -> int:
    occupied = 0
    for coordinate in dirty:
        occupied |= columns[coordinate]
    return lane_mask & ~occupied


def lanes(mask: int) -> tuple[int, ...]:
    result = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


def integer_snapshot(columns: list[int], lane: int) -> Content:
    lane_bit = 1 << lane
    value = 0
    for wire, column in enumerate(columns):
        if column & lane_bit:
            value |= 1 << wire
    return value


def primary_snapshot_sha(content: Content, width: int) -> str:
    primary_bytes = bytes((content >> wire) & 1 for wire in range(width))
    return sha256(primary_bytes).hexdigest()


def replay(program, seeds, census) -> dict[str, object]:
    started = monotonic()
    base_states, initial_failures = initial_states(program, seeds, census)
    duplicate_keys = (census[0], census[-1])
    duplicate_lanes = (len(census), len(census) + 1)
    simulation_keys = census + duplicate_keys
    simulation_states = base_states + (base_states[0], base_states[-1])
    columns = pack_columns(simulation_states)
    schedules = compiled_schedules(program, simulation_keys)
    dirty = aggregate_dirty_coordinates()
    census_mask = (1 << len(census)) - 1
    simulation_mask = (1 << len(simulation_keys)) - 1

    e1_moment: dict[Key, int] = {}
    e2_moment: dict[Key, int] = {}
    e1_content: dict[Key, Content] = {}
    e2_content: dict[Key, Content] = {}
    determinism_mismatches = 0

    def check_duplicates(clean: int) -> None:
        nonlocal determinism_mismatches
        for original, duplicate in zip((0, len(census) - 1), duplicate_lanes):
            determinism_mismatches += int(
                bool(clean & (1 << original)) != bool(clean & (1 << duplicate))
            )

    clean_all = clean_lanes(columns, dirty, simulation_mask)
    check_duplicates(clean_all)
    initially_clean = clean_all & census_mask
    for lane in lanes(initially_clean):
        key = census[lane]
        content = integer_snapshot(columns, lane)
        e1_moment[key] = 0
        e2_moment[key] = 0
        e1_content[key] = content
        e2_content[key] = content
    e1_found = initially_clean
    e2_found = initially_clean

    for orbit in range(1, TRAJECTORY_HORIZON + 1):
        for step, advance in enumerate(schedules, 1):
            advance(columns)
            clean_all = clean_lanes(columns, dirty, simulation_mask)
            check_duplicates(clean_all)
            new_e1 = (clean_all & census_mask) & ~e1_found
            for lane in lanes(new_e1):
                key = census[lane]
                e1_moment[key] = (orbit - 1) * len(program) + step
                e1_content[key] = integer_snapshot(columns, lane)
            e1_found |= new_e1
        orbit_clean = clean_all & census_mask
        new_e2 = orbit_clean & ~e2_found
        for lane in lanes(new_e2):
            key = census[lane]
            e2_moment[key] = orbit
            e2_content[key] = integer_snapshot(columns, lane)
        e2_found |= new_e2

    full_state_duplicate_mismatches = sum(
        bool(column & (1 << original))
        != bool(column & (1 << duplicate))
        for column in columns
        for original, duplicate in zip((0, len(census) - 1), duplicate_lanes)
    )
    return {
        "e1_moment": e1_moment,
        "e2_moment": e2_moment,
        "e1_content": e1_content,
        "e2_content": e2_content,
        "state_width": len(columns),
        "dirty_coordinate_count": len(dirty),
        "initial_failures": initial_failures,
        "determinism_boundary_mismatches": determinism_mismatches,
        "determinism_final_state_mismatches": full_state_duplicate_mismatches,
        "runtime_seconds": round(monotonic() - started, 6),
    }


def stamp_analysis(scan: dict[str, object]) -> dict[str, object]:
    e1_moment = scan["e1_moment"]
    e2_moment = scan["e2_moment"]
    e1_content = scan["e1_content"]
    e2_content = scan["e2_content"]
    e1_keys = set(e1_moment)
    e2_keys = set(e2_moment)
    same_moment = []
    later_equal = []
    split = []
    for key in sorted(e2_keys):
        if e1_moment[key] == 11 * e2_moment[key]:
            same_moment.append(key)
        elif e1_content[key] == e2_content[key]:
            later_equal.append(key)
        else:
            split.append(key)
    e1_only = tuple(sorted(e1_keys - e2_keys))
    contents = set(e1_content.values()) | set(e2_content.values())
    primary_sha = {
        content: primary_snapshot_sha(content, scan["state_width"])
        for content in contents
    }
    primary_content_digest = digest({
        "e1": tuple(sorted(
            (compact(key), primary_sha[content])
            for key, content in e1_content.items()
        )),
        "e2": tuple(sorted(
            (compact(key), primary_sha[content])
            for key, content in e2_content.items()
        )),
    })
    own_content_digest = digest({
        "encoding": "exact integer; bit i is packed-state wire i",
        "e1": tuple(sorted(
            (compact(key), format(content, "x"))
            for key, content in e1_content.items()
        )),
        "e2": tuple(sorted(
            (compact(key), format(content, "x"))
            for key, content in e2_content.items()
        )),
    })
    return {
        "e1_keys": e1_keys,
        "e2_keys": e2_keys,
        "e1_only": e1_only,
        "same_moment": tuple(same_moment),
        "later_equal": tuple(later_equal),
        "split": tuple(split),
        "contents": contents,
        "primary_content_digest": primary_content_digest,
        "integer_snapshot_digest": own_content_digest,
        "distinct_content_classes": len(contents),
    }


class UnionFind:
    def __init__(self, values) -> None:
        self.parent = {value: value for value in values}
        self.rank = {value: 0 for value in values}

    def find(self, value):
        root = value
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[value] != value:
            value, self.parent[value] = self.parent[value], root
        return root

    def union(self, left, right) -> None:
        left = self.find(left)
        right = self.find(right)
        if left == right:
            return
        if self.rank[left] < self.rank[right]:
            left, right = right, left
        self.parent[right] = left
        if self.rank[left] == self.rank[right]:
            self.rank[left] += 1


def constraint_closure(scan, analysis) -> dict[str, object]:
    e1_content = scan["e1_content"]
    e2_content = scan["e2_content"]
    closure = UnionFind(analysis["contents"])
    for key in analysis["split"]:
        closure.union(e1_content[key], e2_content[key])
    zero_roots = {
        closure.find(e1_content[key]) for key in analysis["e1_only"]
    }
    e2_contents = set(e2_content.values())
    forced = {
        content for content in e2_contents
        if closure.find(content) in zero_roots
    }
    free = e2_contents - forced
    component_histogram = Counter(
        closure.find(content) for content in analysis["contents"]
    )
    witness_key = analysis["e1_only"][0] if analysis["e1_only"] else None
    return {
        "e2_content_count": len(e2_contents),
        "forced_zero_e2_count": len(forced),
        "surviving_free_e2_count": len(free),
        "split_equality_constraint_count": len(analysis["split"]),
        "e1_only_zero_constraint_count": len(analysis["e1_only"]),
        "closure_component_count": len(component_histogram),
        "closure_component_size_histogram": dict(sorted(Counter(
            component_histogram.values()
        ).items())),
        "witness_key": witness_key,
        "witness_content_sha_prefix": (
            primary_snapshot_sha(
                e1_content[witness_key], scan["state_width"]
            )[:16]
            if witness_key is not None else None
        ),
    }


def candidate_constraint_test(name, values, scan, analysis) -> dict[str, object]:
    zero_violations = tuple(
        key for key in analysis["e1_only"]
        if values[scan["e1_content"][key]] != 0
    )
    equality_violations = tuple(
        key for key in analysis["split"]
        if values[scan["e1_content"][key]]
        != values[scan["e2_content"][key]]
    )
    return {
        "candidate": name,
        "content_determined_extension": True,
        "zero_constraints_tested": len(analysis["e1_only"]),
        "zero_constraint_violations": len(zero_violations),
        "split_equalities_tested": len(analysis["split"]),
        "split_equality_violations": len(equality_violations),
        "first_zero_violation": zero_violations[0] if zero_violations else None,
        "first_equality_violation": (
            equality_violations[0] if equality_violations else None
        ),
        "inside_kernel": not zero_violations and not equality_violations,
    }


def content_state(content: Content, width: int) -> State:
    return tuple((content >> wire) & 1 for wire in range(width))


def payload_weight(content: Content, width: int) -> int:
    banks, _links = K.M.unpack_state(
        content_state(content, width), FIXTURE_BANKS
    )
    declared_payload = tuple(sorted({
        wire for cell in K.A.CELLS for wire in cell["payload"]
    }))
    return sum(bank[wire] for bank in banks for wire in declared_payload)


def kernel_naturalness_probe(scan, analysis) -> dict[str, object]:
    contents = analysis["contents"]
    width = scan["state_width"]
    candidates = {}
    candidates["hamming_weight"] = candidate_constraint_test(
        "v = Hamming weight of full record content",
        {content: content.bit_count() for content in contents},
        scan,
        analysis,
    )
    candidates["declared_payload_weight"] = candidate_constraint_test(
        "v = weight of A.CELLS[*]['payload'] in every bank",
        {content: payload_weight(content, width) for content in contents},
        scan,
        analysis,
    )

    direction_values: dict[Content, set[int]] = defaultdict(set)
    for reading in ("e1_content", "e2_content"):
        for key, content in scan[reading].items():
            direction_values[content].add(1 if key[1] % 2 == 0 else -1)
    direction_conflicts = {
        content: values
        for content, values in direction_values.items()
        if len(values) != 1
    }
    if direction_conflicts:
        candidates["single_source_direction"] = {
            "candidate": (
                "v = core single-source direction value: (1,0)->+1, "
                "(0,1)->-1, extended by landed content"
            ),
            "content_determined_extension": False,
            "extension_conflicting_content_count": len(direction_conflicts),
            "zero_constraints_tested": 0,
            "zero_constraint_violations": None,
            "split_equalities_tested": 0,
            "split_equality_violations": None,
            "inside_kernel": False,
            "finding": (
                "DOES_NOT_EXTEND: at least one identical landed content is "
                "associated with both core direction values"
            ),
        }
    else:
        direction_test = candidate_constraint_test(
            (
                "v = core single-source direction value: (1,0)->+1, "
                "(0,1)->-1, extended by landed content"
            ),
            {content: next(iter(values)) for content, values in direction_values.items()},
            scan,
            analysis,
        )
        direction_test["extension_conflicting_content_count"] = 0
        direction_test["finding"] = "content-determined extension exists"
        candidates["single_source_direction"] = direction_test

    candidates["constant_one"] = candidate_constraint_test(
        "v = constant 1 (record counting)",
        {content: 1 for content in contents},
        scan,
        analysis,
    )
    inside = tuple(
        name for name, row in candidates.items() if row["inside_kernel"]
    )
    return {
        "declared_payload_register": (
            "for each of the two banks, union of the two core-declared "
            "A.CELLS cell['payload'] wire tuples (68 local bits per bank)"
        ),
        "single_source_convention_derivation": (
            "Cycle-719 held_certificate sets event-even direction (1,0) and "
            "orientation +1; event-odd direction (0,1) and orientation -1"
        ),
        "candidates": candidates,
        "natural_candidates_inside_kernel": inside,
        "reversal_grade_finding": bool(inside),
        "finding": (
            "REVERSAL_GRADE_NATURAL_AGREEING_READOUT_EXISTS: " + ",".join(inside)
            if inside else
            "ALL_NATURAL_CANDIDATES_OUTSIDE_KERNEL_TIGHTENS_GENERIC_SEPARATION"
        ),
    }


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, seeds, census = census_fixture()
    scan = replay(program, seeds, census)
    analysis = stamp_analysis(scan)
    closure = constraint_closure(scan, analysis)
    naturalness = kernel_naturalness_probe(scan, analysis)

    stamp_payload = {
        "census_size": len(census),
        "horizon_orbits_inclusive": TRAJECTORY_HORIZON,
        "e1_stamped": len(analysis["e1_keys"]),
        "e2_stamped": len(analysis["e2_keys"]),
        "e2_subset_e1": analysis["e2_keys"] <= analysis["e1_keys"],
        "same_moment": len(analysis["same_moment"]),
        "different_moment_equal_content": len(analysis["later_equal"]),
        "different_content": len(analysis["split"]),
        "e1_only": len(analysis["e1_only"]),
        "distinct_content_classes": analysis["distinct_content_classes"],
        "primary_content_digest": analysis["primary_content_digest"],
        "expected_primary_content_digest": EXPECTED_PRIMARY_CONTENT_DIGEST,
        "integer_snapshot_digest": analysis["integer_snapshot_digest"],
        "initial_state_failures": scan["initial_failures"],
    }
    stamp_pass = bool(
        len(census) == 748
        and stamp_payload["e1_stamped"] == 182
        and stamp_payload["e2_stamped"] == 114
        and stamp_payload["e2_subset_e1"]
        and stamp_payload["same_moment"] == 34
        and stamp_payload["different_moment_equal_content"] == 49
        and stamp_payload["different_content"] == 31
        and stamp_payload["e1_only"] == 68
        and stamp_payload["distinct_content_classes"] == 76
        and stamp_payload["primary_content_digest"]
            == EXPECTED_PRIMARY_CONTENT_DIGEST
        and scan["initial_failures"] == 0
    )
    closure_pass = bool(
        closure["e2_content_count"] == 48
        and closure["forced_zero_e2_count"] == 6
        and closure["surviving_free_e2_count"] == 42
        and closure["witness_key"] == EXPECTED_PRIMARY_WITNESS_KEY
        and closure["split_equality_constraint_count"] == 31
        and closure["e1_only_zero_constraint_count"] == 68
    )
    naturalness_pass = (
        set(naturalness["candidates"])
        == {
            "hamming_weight",
            "declared_payload_weight",
            "single_source_direction",
            "constant_one",
        }
        and all(
            row["inside_kernel"] in (True, False)
            for row in naturalness["candidates"].values()
        )
    )
    runtime = round(monotonic() - started, 6)
    controls_payload = {
        **controls,
        "determinism_duplicate_keys": (census[0], census[-1]),
        "determinism_boundary_mismatches":
            scan["determinism_boundary_mismatches"],
        "determinism_final_state_mismatches":
            scan["determinism_final_state_mismatches"],
        "runtime_seconds": runtime,
        "runtime_under_1400s": runtime < AUDIT_TIMEOUT_SEC,
        "stdout_under_150KB": None,
    }
    controls_pass = bool(
        controls["pass"]
        and scan["determinism_boundary_mismatches"] == 0
        and scan["determinism_final_state_mismatches"] == 0
        and runtime < AUDIT_TIMEOUT_SEC
        and not FIREWALL.hits
    )
    checks = {
        "THE_STAMP_AND_SNAPSHOT_REPLAY": stamp_pass,
        "THE_CONSTRAINT_CLOSURE": closure_pass,
        "THE_KERNEL_NATURALNESS_PROBE": naturalness_pass,
        "CONTROLS": controls_pass,
    }
    verdict = (
        "PRIMARY_REFUTED_BY_NATURAL_AGREEING_KERNEL"
        if naturalness["reversal_grade_finding"] else
        "PRIMARY_NOT_REFUTED_ALL_NATURAL_PROBES_OUTSIDE_KERNEL"
    )
    report = {
        "checks": checks,
        "THE_STAMP_AND_SNAPSHOT_REPLAY": stamp_payload,
        "THE_CONSTRAINT_CLOSURE": closure,
        "THE_KERNEL_NATURALNESS_PROBE": naturalness,
        "CONTROLS": controls_payload,
        "verdict": verdict,
        "pass": all(checks.values()),
    }

    def finding_lines() -> tuple[str, ...]:
        candidate_summary = "; ".join(
            f"{name}={'INSIDE' if row['inside_kernel'] else 'OUTSIDE'}"
            + (
                f"(zero={row['zero_constraint_violations']},"
                f"eq={row['split_equality_violations']})"
                if row["content_determined_extension"] else
                f"(NO_EXTENSION conflicts="
                f"{row['extension_conflicting_content_count']})"
            )
            for name, row in naturalness["candidates"].items()
        )
        return (
            f"{'PASS' if checks['THE_STAMP_AND_SNAPSHOT_REPLAY'] else 'FAIL'} "
            "THE_STAMP_AND_SNAPSHOT_REPLAY :: "
            f"stamped={stamp_payload['e1_stamped']}/{stamp_payload['e2_stamped']}; "
            f"split={stamp_payload['same_moment']}/"
            f"{stamp_payload['different_moment_equal_content']}/"
            f"{stamp_payload['different_content']}; "
            f"E1-only={stamp_payload['e1_only']}; classes="
            f"{stamp_payload['distinct_content_classes']}; content_digest="
            f"{stamp_payload['primary_content_digest']}",
            f"{'PASS' if checks['THE_CONSTRAINT_CLOSURE'] else 'FAIL'} "
            "THE_CONSTRAINT_CLOSURE :: "
            f"E2 contents={closure['e2_content_count']}; forced-zero="
            f"{closure['forced_zero_e2_count']}; surviving-free="
            f"{closure['surviving_free_e2_count']}; witness key="
            f"{closure['witness_key']}",
            f"{'PASS' if checks['THE_KERNEL_NATURALNESS_PROBE'] else 'FAIL'} "
            "THE_KERNEL_NATURALNESS_PROBE :: " + candidate_summary + "; "
            + naturalness["finding"],
            f"{'PASS' if checks['CONTROLS'] else 'FAIL'} CONTROLS :: "
            "SHA/Git-blob pinned; Cycle-852/Cycle-860 BLOCKLIST text/AST only; "
            f"determinism mismatches={scan['determinism_boundary_mismatches']}/"
            f"{scan['determinism_final_state_mismatches']}; runtime={runtime}s; "
            "stdout<150KB",
            "VERDICT :: " + verdict,
        )

    preliminary = "\n".join(finding_lines()) + "\nSUMMARY_JSON " + compact(report) + "\n"
    stdout_ok = len(preliminary.encode("utf-8")) < STDOUT_LIMIT_BYTES
    controls_payload["stdout_under_150KB"] = stdout_ok
    checks["CONTROLS"] = checks["CONTROLS"] and stdout_ok
    report["pass"] = all(checks.values())
    report["report_sha256"] = digest(report)
    output = "\n".join(finding_lines()) + "\nSUMMARY_JSON " + compact(report) + "\n"
    output += (
        "CYCLE860_DISCRIMINATOR_INDEPENDENT_CHECK_PASS\n"
        if report["pass"] else
        "CYCLE860_DISCRIMINATOR_INDEPENDENT_CHECK_HONEST_FAIL\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
