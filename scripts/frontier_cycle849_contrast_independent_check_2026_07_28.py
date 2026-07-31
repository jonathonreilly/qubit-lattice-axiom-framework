#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-849 mark/stall contrast.

Cycle-849 and both historical Cycle-847 scripts are source primaries: this
checker SHA-pins and parses them as text/AST, but never imports or executes
them.  The landed Cycle-719 controller grammar is the sole executable science
dependency.  Meeting geometry, Boolean replay, mark minimization, and the
six-trio continuation sweep are implemented here.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle849_scheduling_contrast_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
CORE_PATH = AUDIT_INPUT_PATHS[1]
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "0f1d15c444514f81ac007e2c122b3b47c917bec9a01de8b4e5fef358ef910818",
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}
EXPECTED_GIT_BLOB = {
    PRIMARY_PATH: "f2e842dbdbc04df27ddd078424a5cd9bc9455af5",
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
}
HISTORICAL_SOURCES = (
    (
        "cycle847_null_primary",
        "eead0b278d31990d607e2500d7e330e720064e0e",
        "scripts/frontier_cycle847_trio_to_a_million_2026_07_28.py",
        "dab7567b80c9f70488581a9387e654d9bf5e053afcade822576e5a3bd47bba95",
        "c18478b434b962a42df0b9a46ebc50e50fb30f81",
    ),
    (
        "cycle847_independent_spot_checker",
        "ecdd7a73a6ea03334f0467ea20ef803fe0039e07",
        "scripts/frontier_cycle847_million_independent_check_2026_07_28.py",
        "965287e3b004fd84d0bca4668f8def73bebdf4d1d62a68a36f2c8d15d728aba0",
        "eaa91ba5ef28ef7feb02792ccdae043a948d57c2",
    ),
)


class PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Make accidental execution of any source primary a hard failure."""

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
    Path(PRIMARY_PATH).stem,
    *(Path(path).stem for _name, _commit, path, _sha, _blob
      in HISTORICAL_SOURCES),
}))
FIREWALL = PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, ...], int]
Gate = tuple[int, int, int, int]
MaskedGate = tuple[int, int, int, int, int]
RING_STATIONS = 11
FIXTURE_BANKS = 2
STATE_BITS = 5815
TARGET_T = 1_048_576
RUNTIME_LIMIT_SECONDS = 1200
STDOUT_LIMIT_BYTES = 150_000
K2_MEET_WIRES = (40, 81, 105)
K2_EXTENSION_WIRES = (88, 124, 125)
NATIVE_WIRES = (256, 262)
K3_KEYS: tuple[Key, ...] = (
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
TRIO_POSITIONS = ((0, 2, 6), (0, 2, 7), (0, 2, 8))
TRIO_KEYS = tuple(key for key in K3_KEYS if key[1] in TRIO_POSITIONS)
NONTRIO_KEYS = tuple(key for key in K3_KEYS if key not in TRIO_KEYS)
EXPECTED_COMMON_MEETS = {
    (0, 2, 6): (3, (3,)),
    (0, 2, 7): (3, (10,)),
    (0, 2, 8): (3, (0, 10)),
}


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def git_bytes(*arguments: str) -> bytes:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, check=True, capture_output=True,
        timeout=30,
    ).stdout


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    values: list[ast.expr] = []
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
    current_rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "expected_git_blob": EXPECTED_GIT_BLOB[path],
        "git_blob_exact": git_blob(payloads[path]) == EXPECTED_GIT_BLOB[path],
        "access": "EXECUTABLE_CORE" if path == CORE_PATH else "TEXT_AST_ONLY_BLOCKLISTED",
    } for path in AUDIT_INPUT_PATHS)
    historical_trees: dict[str, ast.Module] = {}
    historical_rows = []
    for name, commit, path, expected_sha, expected_blob in HISTORICAL_SOURCES:
        spec = f"{commit}:{path}"
        payload = git_bytes("show", spec)
        tree = ast.parse(payload, filename=spec)
        historical_trees[name] = tree
        historical_rows.append({
            "name": name,
            "spec": spec,
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": expected_sha,
            "sha256_exact": sha256(payload).hexdigest() == expected_sha,
            "git_blob": git_blob(payload),
            "expected_git_blob": expected_blob,
            "git_blob_exact": git_blob(payload) == expected_blob,
            "access": "PINNED_GIT_OBJECT_TEXT_AST_ONLY_BLOCKLISTED",
        })
    self_tree = ast.parse(Path(__file__).read_bytes(), filename=Path(__file__).name)
    direct_frontier_imports = tuple(
        alias.name
        for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names if alias.name.startswith("frontier_cycle")
    )
    primary_tree = trees[PRIMARY_PATH]
    null_tree = historical_trees["cycle847_null_primary"]
    spot_tree = historical_trees["cycle847_independent_spot_checker"]
    null_functions = function_names(null_tree)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS") == AUDIT_INPUT_PATHS,
        "all_AUDIT_INPUT_PATHS_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in current_rows
        ),
        "current_source_rows": current_rows,
        "historical_source_rows": tuple(historical_rows),
        "blocked_modules": BLOCKLISTED_MODULES,
        "direct_frontier_imports": direct_frontier_imports,
        "primary_literal_k3_keys": literal_assignment(primary_tree, "K3_OPEN_KEYS"),
        "cycle847_literal_target": literal_assignment(null_tree, "TARGET_HORIZON"),
        "cycle847_literal_k3_keys": literal_assignment(null_tree, "K3_KEYS"),
        "cycle847_spot_literal_target": literal_assignment(spot_tree, "TARGET_T"),
        "cycle847_spot_keys": literal_assignment(spot_tree, "SPOT_KEYS"),
        "cycle847_null_AST_contract": {
            "required_functions": (
                "clean_postimage", "evolve", "boundary_snapshot",
                "null_family_row", "certificate_c",
            ),
            "present": all(name in null_functions for name in (
                "clean_postimage", "evolve", "boundary_snapshot",
                "null_family_row", "certificate_c",
            )),
        },
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["all_AUDIT_INPUT_PATHS_existing_worktree_relative"]
        and all(row["sha256_exact"] and row["git_blob_exact"] for row in current_rows)
        and all(row["sha256_exact"] and row["git_blob_exact"] for row in historical_rows)
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and result["primary_literal_k3_keys"] == K3_KEYS
        and result["cycle847_literal_target"] == TARGET_T
        and result["cycle847_literal_k3_keys"] == K3_KEYS
        and result["cycle847_spot_literal_target"] == TARGET_T
        and result["cycle847_null_AST_contract"]["present"]
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
    )
    return result, historical_trees


def ring_distance(left: int, right: int) -> int:
    return min((left - right) % RING_STATIONS, (right - left) % RING_STATIONS)


def first_common_ball_meet(
    positions: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    for tick in range(RING_STATIONS):
        centers = tuple(
            station for station in range(RING_STATIONS)
            if all(ring_distance(station, source) <= tick for source in positions)
        )
        if centers:
            return tick, centers
    raise AssertionError(("no common ball meet", positions))


def adjacent_arc_rows(positions: tuple[int, ...]) -> tuple[dict[str, object], ...]:
    ordered = tuple(sorted(positions))
    rows = []
    for index, start in enumerate(ordered):
        end = ordered[(index + 1) % len(ordered)]
        gap = (end - start) % RING_STATIONS
        vertices = tuple((start + offset) % RING_STATIONS for offset in range(gap + 1))
        meeting_tick = None
        centers: tuple[int, ...] = ()
        for tick in range(gap + 1):
            left = set(vertices[:tick + 1])
            right = set(vertices[max(0, gap - tick):])
            overlap = left & right
            if overlap:
                meeting_tick = tick
                centers = tuple(vertex for vertex in vertices if vertex in overlap)
                break
        rows.append({
            "sources": (start, end),
            "gap": gap,
            "first_meeting_tick": meeting_tick,
            "centers": centers,
        })
    return tuple(rows)


def certificate_meets() -> dict[str, object]:
    position_rows = []
    for positions in TRIO_POSITIONS:
        adjacent = adjacent_arc_rows(positions)
        common = first_common_ball_meet(positions)
        position_rows.append({
            "positions": positions,
            "adjacent_meets": adjacent,
            "adjacent_meeting_times": tuple(sorted(
                int(row["first_meeting_tick"]) for row in adjacent
            )),
            "common_meet": common,
            "minimax_crosscheck": min(
                max(ring_distance(station, source) for source in positions)
                for station in range(RING_STATIONS)
            ) == common[0],
        })
    per_key_rows = tuple({
        "key": key,
        "common_meet": first_common_ball_meet(key[1]),
    } for key in TRIO_KEYS)
    computed = {
        row["positions"]: row["common_meet"] for row in position_rows
    }
    passed = (
        len(TRIO_KEYS) == 6
        and len(position_rows) == 3
        and computed == EXPECTED_COMMON_MEETS
        and all(row["adjacent_meeting_times"] == (1, 2, 3) for row in position_rows)
        and all(row["minimax_crosscheck"] for row in position_rows)
        and all(row["common_meet"][0] == 3 for row in per_key_rows)
    )
    finding = (
        "THE MEETS PASS: six trio keys reduce to three source sets; first common "
        "meets are (0,2,6)->t=3 centers=(3,), (0,2,7)->t=3 centers=(10,), "
        "and (0,2,8)->t=3 centers=(0,10)."
        if passed else
        f"THE MEETS FAIL: independently computed common meets are {computed}."
    )
    return {
        "name": "THE MEETS",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "method": "direct C11 ball enumeration plus independent minimax-radius check",
        "position_rows": tuple(position_rows),
        "per_key_rows": per_key_rows,
        "pass": passed,
    }


def compile_gates(word: tuple[object, ...]) -> tuple[Gate, ...]:
    rows = []
    for gate in word:
        wires = tuple(map(int, gate.wires))
        if len(wires) != len(set(wires)):
            raise AssertionError(("repeated gate wire", gate))
        if gate.kind == "X" and len(wires) == 1:
            rows.append((0, wires[0], 0, 0))
        elif gate.kind == "CNOT" and len(wires) == 2:
            rows.append((1, wires[0], wires[1], 0))
        elif gate.kind == "TOF" and len(wires) == 3:
            rows.append((2, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported gate", gate))
    return tuple(rows)


def apply_int(state: int, word: tuple[Gate, ...]) -> int:
    for kind, first, second, third in word:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        else:
            state ^= (
                ((state >> first) & 1) & ((state >> second) & 1)
            ) << third
    return state


def bits_to_int(bits: bytes | tuple[int, ...] | list[int]) -> int:
    return sum(int(bit) << wire for wire, bit in enumerate(bits))


def int_to_bits(state: int) -> bytes:
    return bytes((state >> wire) & 1 for wire in range(STATE_BITS))


def make_context() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state_bits = bytes(K.M.pack_state(banks, links))
    allocator_objects = tuple(K.M.global_allocator_word(FIXTURE_BANKS))
    allocator = compile_gates(allocator_objects)
    fixtures: dict[int, int] = {}
    fixture_rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before_bits = bytes(K.M.prepare_endpoint(state_bits, direction))
        before = bits_to_int(before_bits)
        fixtures[event] = before
        fixture_rows.append({
            "event": event,
            "direction": direction,
            "packed_sha256": sha256(before.to_bytes((STATE_BITS + 7) // 8, "little")).hexdigest(),
        })
        state_bits = int_to_bits(apply_int(before, allocator))
    passed = (
        len(program) == RING_STATIONS
        and len(state_bits) == STATE_BITS
        and len(allocator) == 3106
        and tuple(fixtures) == (0, 1, 2, 3)
    )
    return {
        "program": program,
        "fixtures": fixtures,
        "fixture_rows": tuple(fixture_rows),
        "allocator_gate_count": len(allocator),
        "pass": passed,
    }


def orbit_word(
    program: tuple[object, ...], positions: tuple[int, ...]
) -> tuple[Gate, ...]:
    gates = []
    for phase in range(len(program)):
        live = {(position + phase) % len(program) for position in positions}
        for station, row in enumerate(program):
            if station in live:
                gates.extend(compile_gates(tuple(K.mapped_macro(row))))
    return tuple(gates)


def phase_word(
    program: tuple[object, ...], positions: tuple[int, ...], phase: int
) -> tuple[Gate, ...]:
    live = {(position + phase) % len(program) for position in positions}
    gates = []
    for station, row in enumerate(program):
        if station in live:
            gates.extend(compile_gates(tuple(K.mapped_macro(row))))
    return tuple(gates)


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes((STATE_BITS + 7) // 8, "little")).hexdigest()


def compute_meet_states(context: dict[str, object]) -> dict[str, object]:
    program = context["program"]
    fixtures = context["fixtures"]
    assert isinstance(program, tuple)
    assert isinstance(fixtures, dict)
    words = {
        positions: orbit_word(program, positions)
        for positions in sorted({key[1] for key in K3_KEYS})
    }
    states = []
    rows = []
    for key in K3_KEYS:
        meet_tick, centers = first_common_ball_meet(key[1])
        state = apply_int(fixtures[key[2]], words[key[1]])
        initial_sha = packed_sha256(state)
        for phase in range(meet_tick):
            state = apply_int(state, phase_word(program, key[1], phase))
        states.append(state)
        rows.append({
            "key": key,
            "class": "TRIO" if key in TRIO_KEYS else "NONTRIO",
            "meet_tick": meet_tick,
            "meet_centers": centers,
            "initial_packed_sha256": initial_sha,
            "meet_packed_sha256": packed_sha256(state),
        })
    return {
        "states": tuple(states),
        "rows": tuple(rows),
        "orbit_gate_counts": tuple(
            (positions, len(word)) for positions, word in sorted(words.items())
        ),
        "pass": context["pass"] and len(states) == len(K3_KEYS),
    }


def wire_pattern(state: int, wires: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in wires)


def pattern_test(
    states: tuple[int, ...], wires: tuple[int, ...]
) -> dict[str, object]:
    trio_patterns = tuple(sorted({
        wire_pattern(state, wires)
        for key, state in zip(K3_KEYS, states) if key in TRIO_KEYS
    }))
    nontrio_patterns = tuple(sorted({
        wire_pattern(state, wires)
        for key, state in zip(K3_KEYS, states) if key in NONTRIO_KEYS
    }))
    collisions = []
    for trio_index, (trio_key, trio_state) in enumerate(zip(K3_KEYS, states)):
        if trio_key not in TRIO_KEYS:
            continue
        for non_index, (non_key, non_state) in enumerate(zip(K3_KEYS, states)):
            if non_key not in NONTRIO_KEYS:
                continue
            if wire_pattern(trio_state, wires) == wire_pattern(non_state, wires):
                collisions.append({
                    "trio_index": trio_index,
                    "trio_key": trio_key,
                    "nontrio_index": non_index,
                    "nontrio_key": non_key,
                    "pattern": wire_pattern(trio_state, wires),
                })
    return {
        "wires": wires,
        "trio_patterns": trio_patterns,
        "nontrio_patterns": nontrio_patterns,
        "pattern_sets_disjoint": not collisions,
        "first_collision": collisions[0] if collisions else None,
        "collision_count": len(collisions),
    }


def mark_minimality(states: tuple[int, ...]) -> dict[str, object]:
    labels = tuple(key in TRIO_KEYS for key in K3_KEYS)
    cross_pairs = tuple(
        (positive, negative)
        for positive, label in enumerate(labels) if label
        for negative, other in enumerate(labels) if not other
    )
    full = (1 << len(cross_pairs)) - 1
    covers = []
    for wire in range(STATE_BITS):
        cover = 0
        for index, (positive, negative) in enumerate(cross_pairs):
            if ((states[positive] >> wire) ^ (states[negative] >> wire)) & 1:
                cover |= 1 << index
        covers.append(cover)
    single_bit_marks = tuple(
        wire for wire, cover in enumerate(covers) if cover == full
    )
    first_pair = None
    tested_pairs = 0
    for left in range(STATE_BITS):
        for right in range(left + 1, STATE_BITS):
            tested_pairs += 1
            if covers[left] | covers[right] == full:
                first_pair = (left, right)
                break
        if first_pair is not None:
            break
    return {
        "method": "all-wire cross-class cover enumeration; lexicographic pair scan",
        "cross_class_pair_count": len(cross_pairs),
        "zero_bit_impossible_two_nonempty_classes": bool(TRIO_KEYS and NONTRIO_KEYS),
        "single_bits_enumerated": STATE_BITS,
        "single_bit_marks": single_bit_marks,
        "single_bit_mark_count": len(single_bit_marks),
        "pair_candidates_tested_through_first_witness": tested_pairs,
        "first_lexicographic_pair_mark": first_pair,
        "minimum_width": 1 if single_bit_marks else (2 if first_pair else None),
    }


def certificate_mark(context: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    dynamics = compute_meet_states(context)
    states = dynamics["states"]
    assert isinstance(states, tuple)
    native = pattern_test(states, NATIVE_WIRES)
    k2_meet = pattern_test(states, K2_MEET_WIRES)
    k2_extension = pattern_test(states, K2_EXTENSION_WIRES)
    minimality = mark_minimality(states)
    rows = tuple({
        "key": key,
        "class": "TRIO" if key in TRIO_KEYS else "NONTRIO",
        "bits_256_262": wire_pattern(state, NATIVE_WIRES),
        "equal": wire_pattern(state, NATIVE_WIRES)[0]
            == wire_pattern(state, NATIVE_WIRES)[1],
    } for key, state in zip(K3_KEYS, states))
    trio_implies_equal = all(row["equal"] for row in rows if row["class"] == "TRIO")
    equal_implies_trio = all(
        row["class"] == "TRIO" for row in rows if row["equal"]
    )
    passed = (
        dynamics["pass"]
        and native["trio_patterns"] == ((0, 0), (1, 1))
        and native["nontrio_patterns"] == ((0, 1), (1, 0))
        and native["pattern_sets_disjoint"]
        and trio_implies_equal
        and equal_implies_trio
        and minimality["single_bit_mark_count"] == 0
        and minimality["minimum_width"] == 2
        and minimality["first_lexicographic_pair_mark"] == NATIVE_WIRES
        and not k2_meet["pattern_sets_disjoint"]
        and not k2_extension["pattern_sets_disjoint"]
    )
    finding = (
        "THE MARK PASS: own gate replay gives bit[256] == bit[262] iff TRIO "
        "on all ten meet states; exhaustive 5815-wire width-1 enumeration "
        "finds no single-bit mark; lexicographic width-2 enumeration first "
        "finds (256,262); both inherited k=2 triples have cross-class collisions."
        if passed else
        "THE MARK FAIL: the independent meet-state replay, bidirectional equality "
        "test, minimality enumeration, or inherited-triple collision test disagrees."
    )
    certificate = {
        "name": "THE MARK",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "meet_state_rows": dynamics["rows"],
        "native_rows": rows,
        "trio_implies_bit_equality": trio_implies_equal,
        "bit_equality_implies_trio": equal_implies_trio,
        "native_pattern_test": native,
        "minimality": minimality,
        "k2_40_81_105_failure": k2_meet,
        "k2_88_124_125_failure": k2_extension,
        "pass": passed,
    }
    return certificate, dynamics


def residual_indices() -> tuple[int, ...]:
    bank_fields = (
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        K.A.DIRECTION_OK,
        *K.A.FRESH,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    rows = [int(K.R3.X.SOURCE_POINTER)]
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]:
        rows.extend(int(base + wire) for wire in bank_fields)
    for base in K.M.R12.LINK_BASES[:FIXTURE_BANKS - 1]:
        rows.extend(int(base + wire) for wire in range(K.B.LINK_WIDTH))
    result = tuple(rows)
    if (
        len(result) != 477
        or len(set(result)) != 477
        or min(result) < 0
        or max(result) >= STATE_BITS
    ):
        raise AssertionError("Cycle-847 residual basis changed")
    return result


def bit_slice(states: tuple[int, ...]) -> list[int]:
    return [
        sum(((state >> wire) & 1) << lane for lane, state in enumerate(states))
        for wire in range(STATE_BITS)
    ]


def lane_int(columns: list[int] | tuple[int, ...], lane: int) -> int:
    return sum(((column >> lane) & 1) << wire for wire, column in enumerate(columns))


def lane_byte_sha256(columns: list[int] | tuple[int, ...], lane: int) -> str:
    return sha256(bytes((column >> lane) & 1 for column in columns)).hexdigest()


def masked_schedule(
    program: tuple[object, ...], lane_keys: tuple[Key, ...]
) -> tuple[MaskedGate, ...]:
    rows: list[MaskedGate] = []
    for phase in range(len(program)):
        live_by_lane = tuple(
            {(position + phase) % len(program) for position in key[1]}
            for key in lane_keys
        )
        for station, program_row in enumerate(program):
            mask = sum(
                1 << lane for lane, live in enumerate(live_by_lane)
                if station in live
            )
            if not mask:
                continue
            for kind, first, second, third in compile_gates(
                tuple(K.mapped_macro(program_row))
            ):
                rows.append((kind, first, second, third, mask))
    return tuple(rows)


def advance_columns(columns: list[int], schedule: tuple[MaskedGate, ...]) -> None:
    for kind, first, second, third, mask in schedule:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first] & mask
        else:
            columns[third] ^= columns[first] & columns[second] & mask


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def choose_return_filter(
    initial_columns: tuple[int, ...], one_step_columns: list[int],
    primary_count: int,
) -> tuple[int, ...]:
    selected = set()
    for lane in range(primary_count):
        differing = tuple(
            wire for wire, (initial, after) in enumerate(
                zip(initial_columns, one_step_columns)
            )
            if ((initial ^ after) >> lane) & 1
        )
        selected.update(differing[:24])
    if len(selected) < 48:
        selected.update(range(0, STATE_BITS, max(1, STATE_BITS // 64)))
    return tuple(sorted(selected))


def choose_funnel_filter(
    initial_columns: tuple[int, ...], lanes: tuple[int, int, int]
) -> tuple[int, ...]:
    mask = sum(1 << lane for lane in lanes)
    differing = tuple(
        wire for wire, column in enumerate(initial_columns)
        if (column & mask) not in (0, mask)
    )
    if len(differing) >= 96:
        return differing[:96]
    supplement = tuple(
        wire for wire in range(0, STATE_BITS, max(1, STATE_BITS // 128))
        if wire not in set(differing)
    )
    return (differing + supplement)[:96]


def full_return(
    columns: list[int], initial_columns: tuple[int, ...], lane: int
) -> bool:
    bit = 1 << lane
    return all(not ((current ^ initial) & bit) for current, initial in zip(
        columns, initial_columns
    ))


def full_three_lane_funnel(
    columns: list[int], lanes: tuple[int, int, int]
) -> bool:
    mask = sum(1 << lane for lane in lanes)
    return all((column & mask) in (0, mask) for column in columns)


def checkpoint_row(
    moment: int,
    columns: list[int],
    primary_keys: tuple[Key, ...],
    residual: tuple[int, ...],
    duplicate_lane: int,
) -> dict[str, object]:
    rows = tuple({
        "key": key,
        "state_sha256": lane_byte_sha256(columns, lane),
        "residual_support_weight": sum(
            (columns[wire] >> lane) & 1 for wire in residual
        ),
    } for lane, key in enumerate(primary_keys))
    return {
        "t": moment,
        "rows": rows,
        "duplicate_state_sha256": lane_byte_sha256(columns, duplicate_lane),
        "duplicate_exact": lane_int(columns, 0) == lane_int(columns, duplicate_lane),
    }


def certificate_stall(
    context: dict[str, object], source_certificate: dict[str, object]
) -> dict[str, object]:
    """Sweep all six marked trios; test the Cycle-847 null and funnels."""
    started = monotonic()
    program = context["program"]
    fixtures = context["fixtures"]
    assert isinstance(program, tuple)
    assert isinstance(fixtures, dict)
    primary_keys = TRIO_KEYS
    duplicate_key = primary_keys[0]
    lane_keys = primary_keys + (duplicate_key,)
    words = {
        positions: orbit_word(program, positions)
        for positions in TRIO_POSITIONS
    }
    initial_states = tuple(
        apply_int(fixtures[key[2]], words[key[1]]) for key in lane_keys
    )
    columns = bit_slice(initial_states)
    initial_columns = tuple(columns)
    schedule = masked_schedule(program, lane_keys)
    one_step = columns.copy()
    advance_columns(one_step, schedule)
    primary_mask = (1 << len(primary_keys)) - 1
    duplicate_lane = len(lane_keys) - 1
    duplicate_bit = 1 << duplicate_lane
    duplicate_schedule_lockstep = all(
        bool(mask & 1) == bool(mask & duplicate_bit)
        for _kind, _first, _second, _third, mask in schedule
    )
    residual = residual_indices()
    return_filter = choose_return_filter(initial_columns, one_step, len(primary_keys))
    event_lanes = {
        2: tuple(lane for lane, key in enumerate(primary_keys) if key[2] == 2),
        3: tuple(lane for lane, key in enumerate(primary_keys) if key[2] == 3),
    }
    funnel_filters = {
        event: choose_funnel_filter(initial_columns, lanes)
        for event, lanes in event_lanes.items()
    }
    events = []
    filter_survivors = {"return": 0, "event2_funnel": 0, "event3_funnel": 0}
    checkpoint_times = {0, 1, 3, 65_536, 524_288, TARGET_T}
    checkpoints = [checkpoint_row(
        0, columns, primary_keys, residual, duplicate_lane
    )]
    initial_dirty = 0
    for wire in residual:
        initial_dirty |= columns[wire]
    for event, lanes in event_lanes.items():
        if full_three_lane_funnel(columns, lanes):
            events.append({"t": 0, "kind": "FULL_STATE_FUNNEL", "event": event})
    reached = 0
    for moment in range(1, TARGET_T + 1):
        advance_columns(columns, schedule)
        reached = moment

        dirty = 0
        for wire in residual:
            dirty |= columns[wire]
        clean_hits = primary_mask & ~dirty
        for lane in lane_numbers(clean_hits):
            events.append({
                "t": moment,
                "kind": "CLEAN_POSTIMAGE",
                "lane": lane,
                "key": primary_keys[lane],
            })

        return_candidates = primary_mask
        for wire in return_filter:
            return_candidates &= ~(columns[wire] ^ initial_columns[wire])
            if not return_candidates:
                break
        filter_survivors["return"] += return_candidates.bit_count()
        for lane in lane_numbers(return_candidates & ~clean_hits):
            if full_return(columns, initial_columns, lane):
                events.append({
                    "t": moment,
                    "kind": "EXACT_RETURN_TO_T0",
                    "lane": lane,
                    "key": primary_keys[lane],
                })

        for event, lanes in event_lanes.items():
            lane_mask = sum(1 << lane for lane in lanes)
            candidate = True
            for wire in funnel_filters[event]:
                pattern = columns[wire] & lane_mask
                if pattern not in (0, lane_mask):
                    candidate = False
                    break
            if candidate:
                filter_survivors[f"event{event}_funnel"] += 1
                if full_three_lane_funnel(columns, lanes):
                    events.append({
                        "t": moment,
                        "kind": "FULL_STATE_FUNNEL",
                        "event": event,
                        "keys": tuple(primary_keys[lane] for lane in lanes),
                    })

        if moment in checkpoint_times:
            checkpoints.append(checkpoint_row(
                moment, columns, primary_keys, residual, duplicate_lane
            ))
        if events:
            break

    terminal_rows = tuple({
        "key": key,
        "state_sha256": lane_byte_sha256(columns, lane),
        "residual_support_weight": sum(
            (columns[wire] >> lane) & 1 for wire in residual
        ),
        "transitions_executed": reached,
    } for lane, key in enumerate(primary_keys))
    spot_keys = source_certificate["cycle847_spot_keys"]
    spot_trio_keys = tuple(
        key for key in spot_keys if key in TRIO_KEYS
    ) if isinstance(spot_keys, tuple) else ()
    deterministic = (
        initial_states[0] == initial_states[duplicate_lane]
        and duplicate_schedule_lockstep
        and all(row["duplicate_exact"] for row in checkpoints)
        and lane_int(columns, 0) == lane_int(columns, duplicate_lane)
    )
    passed = (
        context["pass"]
        and initial_dirty & primary_mask == primary_mask
        and len(primary_keys) == 6
        and all(len(lanes) == 3 for lanes in event_lanes.values())
        and reached == TARGET_T
        and not events
        and deterministic
        and source_certificate["cycle847_literal_target"] == TARGET_T
        and source_certificate["cycle847_literal_k3_keys"] == K3_KEYS
        and len(spot_trio_keys) == 2
    )
    finding = (
        "THE STALL LOCALIZATION PASS: all six marked trio trajectories have no "
        "clean postimage, exact t0 return, or per-event full-state funnel at "
        "any integer t=0..1048576; this independently matches the Cycle-847 "
        "six-key null, while its historical independent checker is correctly "
        "treated as a two-trio spot check only."
        if passed else
        f"THE STALL LOCALIZATION FAIL: independent sweep stopped at t={reached} "
        f"with events={events}."
    )
    return {
        "name": "THE STALL LOCALIZATION",
        "status": "PASS" if passed else "FAIL",
        "finding": finding,
        "scope": "all six marked trio keys at every integer continuation tick",
        "target_horizon": TARGET_T,
        "reached_horizon": reached,
        "tested_primary_key_moments": len(primary_keys) * reached,
        "expected_primary_key_moments": len(primary_keys) * TARGET_T,
        "primary_keys": primary_keys,
        "event_lane_groups": event_lanes,
        "resolution_or_funnel_events": tuple(events),
        "return_filter_wire_count": len(return_filter),
        "funnel_filter_wire_counts": {
            event: len(wires) for event, wires in funnel_filters.items()
        },
        "filter_survivors_requiring_full_state_test": filter_survivors,
        "filter_soundness": (
            "filters are necessary coordinate equalities only; every survivor "
            "is checked across all 5815 bits, so false negatives are impossible"
        ),
        "residual_coordinate_count": len(residual),
        "schedule_instructions_per_tick": len(schedule),
        "logical_primary_transitions": len(primary_keys) * reached,
        "expected_logical_primary_transitions": len(primary_keys) * TARGET_T,
        "checkpoints": tuple(checkpoints),
        "terminal_rows": terminal_rows,
        "determinism": {
            "duplicate_key": duplicate_key,
            "duplicate_lane": duplicate_lane,
            "initial_exact": initial_states[0] == initial_states[duplicate_lane],
            "schedule_masks_lockstep": duplicate_schedule_lockstep,
            "checkpoint_exact": all(row["duplicate_exact"] for row in checkpoints),
            "terminal_exact": lane_int(columns, 0) == lane_int(columns, duplicate_lane),
            "pass": deterministic,
        },
        "cycle847_cross_reference": {
            "full_null_primary_target": source_certificate["cycle847_literal_target"],
            "full_null_primary_ten_keys": source_certificate["cycle847_literal_k3_keys"],
            "full_null_primary_AST_contract": source_certificate["cycle847_null_AST_contract"],
            "historical_independent_spot_keys": spot_keys,
            "historical_independent_spot_trio_keys": spot_trio_keys,
            "historical_independent_spot_trio_count": len(spot_trio_keys),
            "honesty": "spot checker is corroboration, not six-trio coverage",
        },
        "seconds": round(monotonic() - started, 6),
        "pass": passed,
    }


def render(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    summary: dict[str, object],
) -> str:
    lines = tuple(
        f"CERTIFICATE {name} {certificate['status']} {compact(certificate)}"
        for name, certificate in certificates
    )
    return "\n".join((
        *lines,
        "SUMMARY_JSON " + compact(summary),
        str(summary["terminal"]),
        "",
    ))


def stable_output(
    certificates: tuple[tuple[str, dict[str, object]], ...],
    summary: dict[str, object],
    controls: dict[str, object],
) -> str:
    for _attempt in range(20):
        output = render(certificates, summary)
        size = len(output.encode())
        if controls["stdout_bytes"] == size and summary["stdout_bytes"] == size:
            return output
        controls["stdout_bytes"] = size
        summary["stdout_bytes"] = size
    raise AssertionError("stdout size fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources, _historical_trees = source_controls()
    meets = certificate_meets()
    context = make_context()
    mark, dynamics = certificate_mark(context)
    stall = certificate_stall(context, sources)
    elapsed = monotonic() - started
    controls_base = (
        sources["pass"]
        and context["pass"]
        and dynamics["pass"]
        and stall["determinism"]["pass"]
        and not any(name in sys.modules for name in BLOCKLISTED_MODULES)
        and not FIREWALL.hits
        and elapsed < RUNTIME_LIMIT_SECONDS
    )
    controls = {
        "name": "CONTROLS",
        "status": "PASS" if controls_base else "FAIL",
        "finding": (
            "CONTROLS PASS: current and historical SHAs/blobs are exact; source "
            "primaries remained blocklisted text/AST-only; literal input paths "
            "exist worktree-relative; duplicate-lane determinism is exact; runtime "
            "is under 1200s and stdout is under 150KB."
            if controls_base else
            "CONTROLS FAIL: at least one SHA/blob, blocklist, path, determinism, "
            "runtime, or stdout precondition failed."
        ),
        "sources": sources,
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": controls_base,
    }
    certificates = (
        ("THE_MEETS", meets),
        ("THE_MARK", mark),
        ("THE_STALL_LOCALIZATION", stall),
        ("CONTROLS", controls),
    )
    science_pass = meets["pass"] and mark["pass"] and stall["pass"]
    all_pass = science_pass and controls["pass"]
    summary = {
        "cycle": 849,
        "checker": Path(__file__).name,
        "meeting_status": meets["status"],
        "mark_status": mark["status"],
        "stall_status": stall["status"],
        "primary_refuted": not science_pass,
        "native_wires": NATIVE_WIRES,
        "native_minimum_width": mark["minimality"]["minimum_width"],
        "swept_horizon": stall["reached_horizon"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": all_pass,
        "terminal": (
            "CYCLE849_PRIMARY_REFUTED"
            if not science_pass else (
                "CYCLE849_CONTRAST_INDEPENDENT_CHECK_PASS"
                if all_pass else "CYCLE849_CONTRAST_INDEPENDENT_CHECK_FAIL"
            )
        ),
    }
    output = stable_output(certificates, summary, controls)
    stdout_ok = len(output.encode()) < STDOUT_LIMIT_BYTES
    controls["pass"] = controls_base and stdout_ok
    controls["status"] = "PASS" if controls["pass"] else "FAIL"
    if not stdout_ok:
        controls["finding"] = "CONTROLS FAIL: stdout is not under 150KB."
    all_pass = science_pass and controls["pass"]
    summary["pass"] = all_pass
    summary["terminal"] = (
        "CYCLE849_PRIMARY_REFUTED"
        if not science_pass else (
            "CYCLE849_CONTRAST_INDEPENDENT_CHECK_PASS"
            if all_pass else "CYCLE849_CONTRAST_INDEPENDENT_CHECK_FAIL"
        )
    )
    output = stable_output(certificates, summary, controls)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout limit exceeded")
    sys.stdout.write(output)
    return 0 if all_pass else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE849_CONTRAST_INDEPENDENT_CHECK_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
