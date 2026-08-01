#!/usr/bin/env python3
"""Cycle 861: exact confirmation-ladder identification audit.

The owner-supplied N6 model sets a record possibility at its first clean
post-engagement H boundary, confirms it at every later clean H-boundary
revisit, and locks the record at a chosen rung.  This runner reconstructs the
complete Cycle-852 census and horizon directly from the Cycle-719 core.  The
Cycle-852/856/860 primaries, plus the historical Cycle-849 trio-mark source,
are SHA-pinned text/AST provenance only and are never imported.

This is a model-layer audit.  It changes no axiom surface and treats the lock
threshold as a dial unless the computed threshold structure forces one.
"""
from __future__ import annotations

import ast
from collections import Counter, defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Callable


AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle852_selection_tournament_2026_07_28.py",
    "scripts/frontier_cycle856_record_covariance_2026_07_28.py",
    "scripts/frontier_cycle860_readout_discriminator_2026_07_28.py",
)
CORE_PATH = AUDIT_INPUT_PATHS[0]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
HISTORICAL_AST_PROVENANCE = (
    "655dd678aa",
    "scripts/frontier_cycle849_scheduling_contrast_2026_07_28.py",
    "0f1d15c444514f81ac007e2c122b3b47c917bec9a01de8b4e5fef358ef910818",
    "f2e842dbdbc04df27ddd078424a5cd9bc9455af5",
)
BLOCKLISTED_MODULES = tuple(sorted({
    *(Path(path).stem for path in TEXT_AST_ONLY_PATHS),
    Path(HISTORICAL_AST_PROVENANCE[1]).stem,
}))
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "fcb1e5ad22e48dc865754bc0a0f5357cdef8e78b477c21f48b74e5971eaa8419",
    AUDIT_INPUT_PATHS[2]:
        "20bce7f6dab9d7755ddefc6e2000d501acb8572dc15f50981b65ba9f6e2a4f2b",
    AUDIT_INPUT_PATHS[3]:
        "28a62fb0bc83ec7a46c18901158693344a84cc1eff8c0c9537b40d9004d8b926",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "d584154f32ead0a03a9661c6f176d52b2a1a77dc",
    AUDIT_INPUT_PATHS[2]: "fc873d0b1947866b238bbe5456ffe89fcd072a21",
    AUDIT_INPUT_PATHS[3]: "b48450fbe70f152bfeaab561a12591a2ec7d48c0",
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any cited text/AST-only primary is imported."""

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
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, PRIMARY_FIREWALL)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, int, tuple[int, ...]]
State = tuple[int, ...]
Selection = frozenset[Key]

FIXTURE_BANKS = 2
MIN_SOURCES = 2
MAX_SOURCES = 5
TRAJECTORY_HORIZON = 51_115
LANDED_E1_STAMPED = 182
LANDED_E2_STAMPED = 114
E2_LANDED_RULE = "record set = first-clean orbit-return selection-event set"
K3_TRIOS: tuple[Key, ...] = (
    (3, 2, (0, 2, 6)),
    (3, 3, (0, 2, 6)),
    (3, 2, (0, 2, 7)),
    (3, 3, (0, 2, 7)),
    (3, 2, (0, 2, 8)),
    (3, 3, (0, 2, 8)),
)
K3_MARK_WIRES = (256, 262)


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


def function_names(tree: ast.Module) -> frozenset[str]:
    return frozenset(
        node.name for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    )


def historical_payload() -> bytes:
    commit, path, _expected_sha, _expected_blob = HISTORICAL_AST_PROVENANCE
    return subprocess.run(
        ("git", "show", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    ).stdout


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
    historical = historical_payload()
    historical_tree = ast.parse(
        historical, filename=HISTORICAL_AST_PROVENANCE[1]
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
    primary_markers = {
        AUDIT_INPUT_PATHS[1]: {
            "derive_census", "dirty_global_indices", "trajectory_census",
        },
        AUDIT_INPUT_PATHS[2]: {
            "monitor_stamp_sets", "monitor_dependence_report",
        },
        AUDIT_INPUT_PATHS[3]: {"lane_snapshot_sha", "stamp_scan"},
    }
    marker_exact = all(
        markers <= function_names(trees[path])
        for path, markers in primary_markers.items()
    )
    historical_keys = literal_assignment(historical_tree, "K3_OPEN_KEYS")
    expected_historical_trios = tuple(
        (k, event, positions)
        for k, positions, event in (historical_keys or ())
        if positions[1] == 2
    )
    historical_facts = {
        "sha256": sha256(historical).hexdigest(),
        "git_blob": git_blob(historical),
        "K3_OPEN_KEYS": historical_keys,
        "EXPECTED_K3_NATIVE_WIRES": literal_assignment(
            historical_tree, "EXPECTED_K3_NATIVE_WIRES"
        ),
        "certificate_markers": tuple(sorted(
            {"certificate_b_mark", "certificate_c_contrast"}
            & function_names(historical_tree)
        )),
        "trio_mapping_exact": expected_historical_trios == K3_TRIOS,
    }
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
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": blob_rows,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "historical_text_AST_only": {
            "commit": HISTORICAL_AST_PROVENANCE[0],
            "path": HISTORICAL_AST_PROVENANCE[1],
            **historical_facts,
        },
        "parsed_top_level_counts": {
            **{path: len(tree.body) for path, tree in trees.items()},
            f"{HISTORICAL_AST_PROVENANCE[0]}:{HISTORICAL_AST_PROVENANCE[1]}":
                len(historical_tree.body),
        },
        "AST_semantic_markers_exact": marker_exact,
        "blocked_modules": BLOCKLISTED_MODULES,
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
        and all(result["parsed_top_level_counts"].values())
        and marker_exact
        and historical_facts["sha256"] == HISTORICAL_AST_PROVENANCE[2]
        and historical_facts["git_blob"] == HISTORICAL_AST_PROVENANCE[3]
        and historical_facts["EXPECTED_K3_NATIVE_WIRES"] == K3_MARK_WIRES
        and historical_facts["certificate_markers"]
            == ("certificate_b_mark", "certificate_c_contrast")
        and historical_facts["trio_mapping_exact"]
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


def derive_event_seeds(program: tuple[object, ...]) -> tuple[tuple[int, State], ...]:
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


def frame_map(key: Key, shift: int, stations: int) -> Key:
    k, event, positions = key
    moved = tuple(sorted((station + shift) % stations for station in positions))
    return k, event, moved


def derive_scope() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    stations = len(program)
    event_seeds = derive_event_seeds(program)
    census = tuple(sorted(
        (k, event, positions)
        for k in range(MIN_SOURCES, MAX_SOURCES + 1)
        for positions in combinations(range(stations), k)
        if pairwise_separated(positions, stations)
        for event, _state in event_seeds
    ))
    remaining = set(census)
    orbits = []
    while remaining:
        representative = min(remaining)
        orbit = tuple(sorted({
            frame_map(representative, shift, stations)
            for shift in range(stations)
        }))
        if not set(orbit) <= set(census):
            raise AssertionError(("frame closure", representative))
        orbits.append(orbit)
        remaining.difference_update(orbit)
    result = {
        "program": program,
        "event_seeds": event_seeds,
        "census": census,
        "orbits": tuple(sorted(orbits, key=lambda row: row[0])),
        "stations": stations,
        "population": len(census),
        "per_k_populations": dict(sorted(Counter(key[0] for key in census).items())),
    }
    result["pass"] = (
        stations == 11
        and len(event_seeds) == 4
        and len(census) == 748
        and len(result["orbits"]) == 68
        and all(len(orbit) == 11 for orbit in result["orbits"])
        and set(K3_TRIOS) <= set(census)
    )
    return result


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


def synchronous_word(
    program: tuple[object, ...], positions0: tuple[int, ...]
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


def build_initial_states(scope: dict[str, object]) -> tuple[tuple[State, ...], int]:
    program = scope["program"]
    census = scope["census"]
    seed_by_event = dict(scope["event_seeds"])
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


def pack_states(states: tuple[State, ...]) -> list[int]:
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def compile_masked_gate(gate: object, mask: int) -> tuple[int, int, int, int, int]:
    if gate.kind == "X":
        return (0, gate.wires[0], 0, 0, mask)
    if gate.kind == "CNOT":
        return (1, gate.wires[0], gate.wires[1], 0, mask)
    if gate.kind == "TOF":
        return (2, gate.wires[0], gate.wires[1], gate.wires[2], mask)
    raise ValueError(("unsupported landed gate", gate))


def masked_h_schedules(
    program: tuple[object, ...], census: tuple[Key, ...]
) -> tuple[tuple[tuple[int, int, int, int, int], ...], ...]:
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


def compile_fast_schedules(
    schedules: tuple[tuple[tuple[int, int, int, int, int], ...], ...]
) -> tuple[Callable[[list[int]], None], ...]:
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
    return tuple(functions)  # type: ignore[return-value]


def clean_mask(columns: list[int], dirty_indices: tuple[int, ...], all_mask: int) -> int:
    dirty = 0
    for wire in dirty_indices:
        dirty |= columns[wire]
    return all_mask & ~dirty


def equality_mask(
    columns: list[int], reference: list[int], candidate_mask: int
) -> int:
    differences = 0
    for left, right in zip(columns, reference):
        differences |= left ^ right
    return candidate_mask & ~differences


def lane_numbers(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


if __name__ == "__main__":
    raise SystemExit("Cycle 861 runner scaffold: certificates not yet installed")
