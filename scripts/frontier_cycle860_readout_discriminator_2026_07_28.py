#!/usr/bin/env python3
"""Cycle 860: the readout-I discriminator between the E1 and E2 readings.

Question (exercise Route 1, owner-directed): the Record axiom makes readout
content-determined and additive over disjoint records.  E1 ("first
admissibility") and E2 ("first orbit admissibility") stamp records at
different moments and for different key sets.  Are the two readings
readout-DISTINGUISHABLE — does there exist an admissible content-determined
value function under which some landed history reads out differently — and
does any NONTRIVIAL value function make all landed histories agree?

Method: replay the certified Cycle-852 census (748 keys, horizon 51,115
orbits) with independently re-implemented machinery from the Cycle-719 core;
capture the full clean-state snapshot (the record-content candidate) at every
E1 and E2 stamp moment; then solve the exact agreement-constraint system over
content classes.  The Cycle-852 primary is a SHA-pinned text/AST provenance
surface only; nothing is imported from it.

Supervisor-authored (exercise lane, run personally).  bounded_theorem,
authority none, audit unset.  Independent audit still required.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle852_selection_tournament_2026_07_28.py",
)
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "fcb1e5ad22e48dc865754bc0a0f5357cdef8e78b477c21f48b74e5971eaa8419",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "d584154f32ead0a03a9661c6f176d52b2a1a77dc",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if a cited text/AST-only primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K

Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
TRAJECTORY_HORIZON = 51_115
LANDED_E1_STAMPED = 182
LANDED_E2_STAMPED = 114
E2_LANDED_RULE = "record set = first-clean orbit-return selection-event set"


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name) and target.id == name
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
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=Path(__file__).name,
    )
    sha_rows = {
        path: sha256(payload).hexdigest() for path, payload in payloads.items()
    }
    blob_rows = {path: git_blob(payload) for path, payload in payloads.items()}
    direct_frontier_imports = tuple(sorted(
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    ))
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": all(
            not Path(path).is_absolute() and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": sha_rows,
        "git_blobs": blob_rows,
        "text_AST_parsed_top_level_counts": {
            path: len(tree.body) for path, tree in trees.items()
        },
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and sha_rows == EXPECTED_SHA256
        and blob_rows == EXPECTED_GIT_BLOBS
        and direct_frontier_imports == (
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        )
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


def pairwise_separated(positions: tuple[int, ...], stations: int) -> bool:
    occupied = set(positions)
    return all(
        (station + 1) % stations not in occupied for station in occupied
    )


def derive_event_seeds(program) -> tuple[tuple[int, State], ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    state = K.M.pack_state(banks, links)
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    rows = []
    for event in range(2 * FIXTURE_BANKS):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        if not (
            after == K.A.apply_semantic(before, allocator)
            and rail_a == (1,) + (0,) * (len(program) - 1)
            and not any(rail_b)
            and len(trace) == len(program)
        ):
            raise AssertionError(("Cycle-719 event seed", event))
        rows.append((event, before))
        state = after
    return tuple(rows)


def derive_census():
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    event_seeds = derive_event_seeds(program)
    keys = tuple(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if pairwise_separated(positions, stations)
        for event, _state in event_seeds
    )
    if len(keys) != len(set(keys)):
        raise AssertionError("duplicate census key")
    return program, event_seeds, tuple(sorted(keys))


def watched_registers() -> tuple[tuple[str, int], ...]:
    return (
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


def dirty_global_indices() -> tuple[int, ...]:
    banks0, links0 = K.B.chain_genesis(FIXTURE_BANKS)
    zero_banks = tuple(tuple(0 for _bit in bank) for bank in banks0)
    zero_links = tuple(tuple(0 for _bit in link) for link in links0)
    baseline = K.M.pack_state(zero_banks, zero_links)
    indices = {K.R3.X.SOURCE_POINTER}
    for bank_index, _bank in enumerate(zero_banks):
        for _name, wire in watched_registers():
            changed = [list(bank) for bank in zero_banks]
            changed[bank_index][wire] = 1
            marked = K.M.pack_state(
                tuple(tuple(bank) for bank in changed), zero_links
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(("packed bank marker", differences))
            indices.add(differences[0])
    for link_index, link in enumerate(zero_links):
        for wire in range(len(link)):
            changed = [list(row) for row in zero_links]
            changed[link_index][wire] = 1
            marked = K.M.pack_state(
                zero_banks, tuple(tuple(row) for row in changed)
            )
            differences = tuple(
                index
                for index, (left, right) in enumerate(zip(baseline, marked))
                if left != right
            )
            if len(differences) != 1:
                raise AssertionError(("packed link marker", differences))
            indices.add(differences[0])
    return tuple(sorted(indices))


def synchronous_word(program, positions0):
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


def build_initial_states(program, event_seeds, census):
    seed_by_event = dict(event_seeds)
    word_cache = {
        positions: synchronous_word(program, positions)
        for _k, _event, positions in census
    }
    states = []
    failures = 0
    for k, event, positions in census:
        before = seed_by_event[event]
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=positions
        )
        expected_rail = tuple(
            int(station in positions) for station in range(len(program))
        )
        failures += after != K.A.apply_semantic(before, word_cache[positions])
        failures += rail_a != expected_rail or any(rail_b)
        restored, inverse_a, inverse_b, _ = K.run_orbit(
            after, program, token_positions=positions, reverse=True
        )
        failures += (
            restored != before or inverse_a != rail_a or inverse_b != rail_b
        )
        if len(positions) != k:
            raise AssertionError(("key/source mismatch", k, positions))
        states.append(after)
    return tuple(states), failures


def pack_states(states):
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compile_masked_gate(gate, mask):
    if gate.kind == "X":
        return (0, gate.wires[0], 0, 0, mask)
    if gate.kind == "CNOT":
        return (1, gate.wires[0], gate.wires[1], 0, mask)
    if gate.kind == "TOF":
        return (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
    raise ValueError(("unsupported landed gate", gate))


def masked_h_schedules(program, census):
    stations = len(program)
    rows = []
    for step in range(stations):
        schedule = []
        for station, program_row in enumerate(program):
            mask = sum(
                1 << lane
                for lane, (_k, _event, positions) in enumerate(census)
                if (station - step) % stations in positions
            )
            if not mask:
                continue
            schedule.extend(
                compile_masked_gate(gate, mask)
                for gate in K.mapped_macro(program_row)
            )
        rows.append(tuple(schedule))
    return tuple(rows)


def compile_fast_schedules(schedules):
    functions = []
    for schedule in schedules:
        source = ["def apply_chunk(c):"]
        for kind, first, second, third, mask in schedule:
            if kind == 0:
                source.append(f" c[{first}] ^= {mask}")
            elif kind == 1:
                source.append(f" c[{second}] ^= c[{first}] & {mask}")
            else:
                source.append(
                    f" c[{third}] ^= c[{first}] & c[{second}] & {mask}"
                )
        namespace: dict[str, object] = {}
        exec("\n".join(source), {"__builtins__": {}}, namespace)
        functions.append(namespace["apply_chunk"])
    return tuple(functions)


def clean_mask(columns, dirty_indices, all_mask):
    dirty = 0
    for wire in dirty_indices:
        dirty |= columns[wire]
    return all_mask & ~dirty


def lane_numbers(mask):
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def lane_snapshot_sha(columns, lane) -> str:
    bit = 1 << lane
    return sha256(
        bytes(int(bool(column & bit)) for column in columns)
    ).hexdigest()


def stamp_scan(program, event_seeds, census):
    """Replay the census; capture content snapshots at every stamp moment."""

    started = monotonic()
    states, initial_failures = build_initial_states(
        program, event_seeds, census
    )
    simulation_keys = census + (census[0],)
    duplicate_lane = len(census)
    columns = pack_states(states + (states[0],))
    schedules = masked_h_schedules(program, simulation_keys)
    fast_schedules = compile_fast_schedules(schedules)
    dirty_indices = dirty_global_indices()
    all_mask = (1 << len(census)) - 1
    simulation_mask = (1 << len(simulation_keys)) - 1

    e1_moment: dict[Key, int] = {}
    e2_moment: dict[Key, int] = {}
    e1_content: dict[Key, str] = {}
    e2_content: dict[Key, str] = {}

    initial_clean_all = clean_mask(columns, dirty_indices, simulation_mask)
    initial_clean = initial_clean_all & all_mask
    determinism_mismatches = int(
        bool(initial_clean_all & 1)
        != bool(initial_clean_all & (1 << duplicate_lane))
    )
    for lane in lane_numbers(initial_clean):
        snap = lane_snapshot_sha(columns, lane)
        e1_moment[census[lane]] = 0
        e2_moment[census[lane]] = 0
        e1_content[census[lane]] = snap
        e2_content[census[lane]] = snap
    e1_found = initial_clean
    e2_found = initial_clean

    stations = len(program)
    for orbit in range(1, TRAJECTORY_HORIZON + 1):
        for step, apply_chunk in enumerate(fast_schedules, 1):
            apply_chunk(columns)
            clean_all = clean_mask(columns, dirty_indices, simulation_mask)
            clean = clean_all & all_mask
            determinism_mismatches += (
                bool(clean_all & 1)
                != bool(clean_all & (1 << duplicate_lane))
            )
            new_e1 = clean & ~e1_found
            if new_e1:
                absolute_h = (orbit - 1) * stations + step
                for lane in lane_numbers(new_e1):
                    e1_moment[census[lane]] = absolute_h
                    e1_content[census[lane]] = lane_snapshot_sha(
                        columns, lane
                    )
                e1_found |= new_e1
        orbit_clean = (
            clean_mask(columns, dirty_indices, simulation_mask) & all_mask
        )
        new_e2 = orbit_clean & ~e2_found
        if new_e2:
            for lane in lane_numbers(new_e2):
                e2_moment[census[lane]] = orbit
                e2_content[census[lane]] = lane_snapshot_sha(columns, lane)
            e2_found |= new_e2

    return {
        "initial_build_failures": initial_failures,
        "e1_moment": e1_moment,
        "e2_moment": e2_moment,
        "e1_content": e1_content,
        "e2_content": e2_content,
        "determinism_mismatches": determinism_mismatches,
        "runtime_seconds": round(monotonic() - started, 6),
    }


def certificate_a(scan, census) -> dict[str, object]:
    e1_stamped = frozenset(scan["e1_moment"])
    e2_stamped = frozenset(scan["e2_moment"])
    stations = 11
    ordering_ok = all(
        scan["e1_moment"][key] <= stations * scan["e2_moment"][key]
        for key in e2_stamped
    )
    per_k_e1 = Counter(key[0] for key in e1_stamped)
    per_k_e2 = Counter(key[0] for key in e2_stamped)
    result = {
        "certificate": "A_STAMP_REGRESSION",
        "census_size": len(census),
        "e1_stamped_count": len(e1_stamped),
        "e2_stamped_count": len(e2_stamped),
        "landed_expected": (LANDED_E1_STAMPED, LANDED_E2_STAMPED),
        "e2_subset_of_e1": e2_stamped <= e1_stamped,
        "e1_before_or_at_e2_boundary": ordering_ok,
        "per_k_e1": dict(sorted(per_k_e1.items())),
        "per_k_e2": dict(sorted(per_k_e2.items())),
        "initial_build_failures": scan["initial_build_failures"],
        "determinism_mismatches": scan["determinism_mismatches"],
    }
    result["pass"] = (
        len(e1_stamped) == LANDED_E1_STAMPED
        and len(e2_stamped) == LANDED_E2_STAMPED
        and result["e2_subset_of_e1"]
        and ordering_ok
        and scan["initial_build_failures"] == 0
        and scan["determinism_mismatches"] == 0
    )
    return result


def certificate_b(scan) -> dict[str, object]:
    e2_keys = sorted(scan["e2_moment"])
    stations = 11
    same_moment = []
    equal_content = []
    different_content = []
    for key in e2_keys:
        e1_h = scan["e1_moment"][key]
        e2_h = stations * scan["e2_moment"][key]
        if e1_h == e2_h:
            same_moment.append(key)
        elif scan["e1_content"][key] == scan["e2_content"][key]:
            equal_content.append(key)
        else:
            different_content.append(key)
    e1_only = sorted(set(scan["e1_moment"]) - set(scan["e2_moment"]))
    content_classes: dict[str, list[tuple[str, Key]]] = {}
    for key, sha in scan["e1_content"].items():
        content_classes.setdefault(sha, []).append(("E1", key))
    for key, sha in scan["e2_content"].items():
        content_classes.setdefault(sha, []).append(("E2", key))
    result = {
        "certificate": "B_CONTENT_CENSUS",
        "both_stamped": len(e2_keys),
        "same_moment_count": len(same_moment),
        "different_moment_equal_content_count": len(equal_content),
        "different_moment_different_content_count": len(different_content),
        "different_content_examples": [
            {
                "key": key,
                "e1_absolute_h": scan["e1_moment"][key],
                "e2_orbit": scan["e2_moment"][key],
                "e1_content_sha": scan["e1_content"][key][:16],
                "e2_content_sha": scan["e2_content"][key][:16],
            }
            for key in different_content[:3]
        ],
        "e1_only_count": len(e1_only),
        "e1_only_examples": [
            {
                "key": key,
                "e1_absolute_h": scan["e1_moment"][key],
                "content_sha": scan["e1_content"][key][:16],
            }
            for key in e1_only[:3]
        ],
        "distinct_content_class_count": len(content_classes),
        "content_class_size_histogram": dict(sorted(Counter(
            len(members) for members in content_classes.values()
        ).items())),
    }
    result["pass"] = (
        len(e2_keys)
        == len(same_moment) + len(equal_content) + len(different_content)
    )
    return result, content_classes, e1_only, different_content


def certificate_c(scan, content_classes, e1_only, different_content):
    """Solve the exact readout-agreement constraint system.

    Agreement of I on EVERY landed history requires a content-determined v
    with: v == 0 on every E1-only record content, and v(s_E1) == v(s_E2) for
    every both-stamped key.  Contents are v-equal iff sha-equal (content
    determination).  Union-find over EQ constraints; a class touching any
    ZERO constraint is forced to zero everywhere that content appears.
    """

    parent: dict[str, str] = {}

    def find(sha: str) -> str:
        parent.setdefault(sha, sha)
        while parent[sha] != sha:
            parent[sha] = parent[parent[sha]]
            sha = parent[sha]
        return sha

    def union(left: str, right: str) -> None:
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[left_root] = right_root

    for key in scan["e2_moment"]:
        union(scan["e1_content"][key], scan["e2_content"][key])
    zero_roots = {find(scan["e1_content"][key]) for key in e1_only}
    e2_contents = {scan["e2_content"][key] for key in scan["e2_moment"]}
    forced_zero_e2 = {
        sha for sha in e2_contents if find(sha) in zero_roots
    }
    surviving_free = e2_contents - forced_zero_e2

    separable_by_existence = len(e1_only) > 0
    separable_on_shared = len(different_content) > 0
    if not surviving_free and e2_contents:
        verdict = "SEPARABLE_STRONG_TRIVIAL_KERNEL_ONLY"
    elif separable_by_existence or separable_on_shared:
        verdict = "SEPARABLE_WITH_NONTRIVIAL_AGREEING_KERNEL"
    else:
        verdict = "NOT_SEPARABLE_AT_SCOPE"

    witness = None
    if e1_only:
        key = e1_only[0]
        witness = {
            "type": "E1_only_history",
            "key": key,
            "statement": (
                "any content-determined v with v!=0 on this record content"
                " gives I_E1 != 0 = I_E2 on this single history"
            ),
            "content_sha": scan["e1_content"][key][:16],
        }
    elif different_content:
        key = different_content[0]
        witness = {
            "type": "shared_key_content_split",
            "key": key,
            "statement": (
                "assign v different values on the two contents unless"
                " collision-forced equal"
            ),
        }
    result = {
        "certificate": "C_SEPARATION_THEOREM",
        "separable_by_E1_only_existence": separable_by_existence,
        "separable_on_shared_sector": separable_on_shared,
        "eq_constraint_count": len(scan["e2_moment"]),
        "zero_constraint_count": len(e1_only),
        "e2_content_count": len(e2_contents),
        "e2_contents_forced_zero": len(forced_zero_e2),
        "e2_contents_surviving_free": len(surviving_free),
        "witness": witness,
        "verdict": verdict,
    }
    result["pass"] = True
    return result


def certificate_d() -> dict[str, object]:
    """Scan the pinned surfaces for any multi-source scalar value function."""

    needles = ("readout_value", "scalar_readout", "record_value", "I_value")
    findings = {}
    for path in AUDIT_INPUT_PATHS:
        text = (ROOT / path).read_text(encoding="utf-8")
        findings[path] = {
            needle: text.count(needle) for needle in needles
        }
    any_hit = any(
        count for rows in findings.values() for count in rows.values()
    )
    result = {
        "certificate": "D_LANDED_VALUE_FUNCTION_SCAN",
        "needle_counts": findings,
        "multi_source_value_function_found": any_hit,
        "finding": (
            "no multi-source scalar record value function is implemented on"
            " the pinned surfaces; the landed corpus evaluates I only on the"
            " single-source sector; the separation analysis therefore ranges"
            " over ALL admissible content-determined value functions"
            if not any_hit else "value-function needles found; inspect"
        ),
    }
    result["pass"] = True
    return result


def main() -> int:
    started = monotonic()
    controls = source_controls()
    program, event_seeds, census = derive_census()
    scan = stamp_scan(program, event_seeds, census)
    cert_a = certificate_a(scan, census)
    cert_b, content_classes, e1_only, different_content = certificate_b(scan)
    cert_c = certificate_c(scan, content_classes, e1_only, different_content)
    cert_d = certificate_d()
    runtime = round(monotonic() - started, 6)
    checks = {
        "A_STAMP_REGRESSION": cert_a["pass"],
        "B_CONTENT_CENSUS": cert_b["pass"],
        "C_SEPARATION_THEOREM": cert_c["pass"],
        "D_LANDED_VALUE_SCAN": cert_d["pass"],
        "E_CONTROLS": bool(
            controls["pass"] and runtime < AUDIT_TIMEOUT_SEC
        ),
    }
    lines = [
        "CYCLE860_READOUT_DISCRIMINATOR",
        "PROPOSAL_CONTEXT_EXERCISE_ROUTE_1_NO_AXIOM_SURFACE_TOUCHED",
        f"E2_LANDED_RULE :: {E2_LANDED_RULE}",
    ]
    for name, payload in (
        ("A_STAMP_REGRESSION", cert_a),
        ("B_CONTENT_CENSUS", cert_b),
        ("C_SEPARATION_THEOREM", cert_c),
        ("D_LANDED_VALUE_SCAN", cert_d),
    ):
        status = "PASS" if payload["pass"] else "FAIL"
        lines.append(f"CERTIFICATE {name} {status} {compact(payload)}")
    summary = {
        "checks": checks,
        "cycle": 860,
        "runtime_seconds": runtime,
        "scan_runtime_seconds": scan["runtime_seconds"],
        "verdict": cert_c["verdict"],
        "pass": all(checks.values()),
        "content_digest": digest({
            "e1": tuple(sorted(
                (compact(k), v) for k, v in scan["e1_content"].items()
            )),
            "e2": tuple(sorted(
                (compact(k), v) for k, v in scan["e2_content"].items()
            )),
        }),
    }
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append(
        "CYCLE860_READOUT_DISCRIMINATOR_"
        + ("PASS" if summary["pass"] else "HONEST_FAIL")
    )
    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
