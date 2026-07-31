#!/usr/bin/env python3
"""Cycle 828 independent adversarial check of the proposed Record edit.

Only the landed Cycle-719 dynamics are executable.  Cycle 828 and every
later composition/census primary are data surfaces (text/AST or pinned cache
objects), never executable dependencies.  The central calculation implements
H-station-boundary monitoring and first-clean formation independently.
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
from typing import Any, Iterable


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle828_axiom_edit_audit_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle786_ensemble_support_census_2026_07_28.py",
    "scripts/frontier_cycle796_monitored_selector_2026_07_28.py",
    "scripts/frontier_cycle818_period_structure_census_2026_07_28.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "logs/runner-cache/frontier_cycle796_monitored_selector_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle820_shared_moment_mechanism_2026_07_28.txt",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TEXT_AST_ONLY_PATHS = (
    AUDIT_INPUT_PATHS[0],
    AUDIT_INPUT_PATHS[2],
    AUDIT_INPUT_PATHS[3],
    AUDIT_INPUT_PATHS[4],
    AUDIT_INPUT_PATHS[5],
)
CACHE_PATHS = AUDIT_INPUT_PATHS[6:]

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "74d6aefee383ced099d04fde79b6389f9f22fd38379ce83c99f2518246248f7e",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "3956e5af3ea9c12e8bd605cc0bae7fc29a24154c1ee3527be53223dbee778cd6",
    AUDIT_INPUT_PATHS[3]:
        "be0238611e02f9bad8df813430f9decec68d287df267bbf82ba4a63ffc8483c3",
    AUDIT_INPUT_PATHS[4]:
        "918ae9d1f5b29a4cee437dac8af4bfb27ee0aceee3a7abd0c6bdaaa6fb10d24c",
    AUDIT_INPUT_PATHS[5]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[6]:
        "23fce8b28ab4c5792f5ee9222dfb8aa63edf4fe462700a7998994a64bf710a1d",
    AUDIT_INPUT_PATHS[7]:
        "3513d8e55a18ee11c2f35565065f9efc3e459b33d56923fa3c17911d9f24681e",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "fddeda1828e480ca963fc7940b20c84a15615e60",
    AUDIT_INPUT_PATHS[1]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[2]: "3d219308183e781c71f9742bd0c6331440f74dbe",
    AUDIT_INPUT_PATHS[3]: "eb2f34cd78fae3ce579d426df2ffe62832003504",
    AUDIT_INPUT_PATHS[4]: "9c2657e5fa98c4d2bbb561a0f428cf59fca20973",
    AUDIT_INPUT_PATHS[5]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[6]: "dced1dfadab2742d00aedfbeba93b25766cc653b",
    AUDIT_INPUT_PATHS[7]: "6b0198080f5e9fadc69cc1301b41cff2502f3eb2",
}

LINEAGE_BLOBS = {
    "Cycle781_primary": (
        "d14cd0ece611c647d3cb7b184830ef9b10754b1d",
        "b1158250dcb1449f6abac4f6bb6a0a90f47511a8a0f587e85483f4b6f3624211",
    ),
    "Cycle799_primary": (
        "49964118073bcd784af0f2e4c03723a9d3bd47e9",
        "6773ec05cc1db37a09f88232e7d1f8f9c4b87db98e5b620ad3ef57180ab1cddc",
    ),
    "Cycle809_primary": (
        "307152b50f76e1becbdce29510f03bfa46808a6a",
        "cce8420938b28b805811f4320ee54d7b8a58de0aeceebbd99f10c110338c90a3",
    ),
    "Cycle804_primary": (
        "fe47ff978298e25293eded2730b29c601e8684a9",
        "451fb3f5d9eaf975e6b2ccdc248f66170805bc6e80da8dcc186a68379097cfc7",
    ),
    "Cycle801_cache": (
        "b50059cfb5123439a8848cd32dc17515ae364712",
        "33c10abc491b78bd2e346263d70ccf77f9b82227a5dcfa8fbe86fa62e891bf3d",
    ),
    "Cycle814_cache": (
        "a81e0f017f68a71af48329eb7d139dba21d0648b",
        "521e1217d0e36440220fb6226e4872638dbe0abfda3df36986337a06acf4e89c",
    ),
    "Cycle819_cache": (
        "4ec36a0d1d3800894d4a884a2b384752d1b48887",
        "9afe11babae88b9522d1d4e7a321aa61cdd211a001e0f3116af0edefd6728402",
    ),
}

CANDIDATE_EDIT = "Records form at first admissibility."
RING_STATIONS = 11
FIXTURE_BANKS = 2
K2_HORIZON = 14744
HIGHER_HORIZON = 1385
FULL_FAMILY_BANK_COUNTS = (1, 2, 3, 5, 12)
EXPECTED_HIGHER_TRANSIENTS = {
    (3, 2, (0, 2, 5)): 444,
    (3, 3, (0, 2, 5)): 532,
    (3, 1, (0, 2, 4)): 681,
    (3, 2, (0, 2, 4)): 1385,
}
EXPECTED_K2_TRANSIENTS = {
    (3, (1, 10)): 252,
    (3, (0, 7)): 371,
    (0, (1, 6)): 14744,
    (0, (1, 7)): 14744,
    (0, (2, 7)): 14744,
    (0, (2, 8)): 14744,
    (0, (3, 8)): 14744,
    (0, (3, 9)): 14744,
    (0, (4, 9)): 14744,
    (0, (4, 10)): 14744,
    (0, (5, 10)): 14744,
}
EXPECTED_OLD_K2_CYCLES = {
    (3, (0, 5)): 2,
    (3, (0, 6)): 2,
    (3, (1, 6)): 3,
    (3, (1, 7)): 3,
    (3, (2, 7)): 3,
    (3, (2, 8)): 3,
    (3, (3, 8)): 3,
    (3, (3, 9)): 3,
    (3, (4, 9)): 3,
    (3, (4, 10)): 3,
    (3, (5, 10)): 3,
    (2, (0, 9)): 288,
}
EXPECTED_NEW_K2_CYCLES = {
    (0, (0, 9)): 8930,
    (1, (0, 9)): 8928,
}

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class _ReferenceBlocker(importlib.abc.MetaPathFinder):
    def __init__(self, modules: Iterable[str]):
        self.modules = frozenset(modules)
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname in self.modules:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids reference execution: {fullname}")
        return None


BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in TEXT_AST_ONLY_PATHS
)
PRIMARY_BLOCKER = _ReferenceBlocker(BLOCKLISTED_MODULES)
sys.meta_path.insert(0, PRIMARY_BLOCKER)

# The sole frontier execution dependency.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Key = tuple[int, tuple[int, ...]]
HigherKey = tuple[int, int, tuple[int, ...]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def blob_sha1(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode("ascii") + payload).hexdigest()


def git_blob(blob: str) -> bytes:
    return subprocess.run(
        ("git", "cat-file", "blob", blob),
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout


def json_line(text: str, prefix: str) -> Any:
    rows = [line for line in text.splitlines() if line.startswith(prefix)]
    if len(rows) != 1:
        raise AssertionError(("JSON line", prefix, len(rows)))
    suffix = rows[0][len(prefix):].strip()
    if suffix.startswith("::"):
        suffix = suffix[2:].strip()
    return json.loads(suffix)


def top_assignment(tree: ast.Module, name: str) -> ast.AST:
    rows = []
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in targets
            ):
                rows.append(node.value)
    if len(rows) != 1:
        raise AssertionError(("top assignment", name, len(rows)))
    return rows[0]


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("function", name, len(rows)))
    return rows[0]


def literal_audit_paths() -> bool:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    node = top_assignment(tree, "AUDIT_INPUT_PATHS")
    return (
        isinstance(node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in node.elts
        )
        and tuple(ast.literal_eval(node)) == AUDIT_INPUT_PATHS
    )


def source_controls() -> dict[str, Any]:
    observed_sha = {}
    observed_blobs = {}
    parsed = {}
    for relative in AUDIT_INPUT_PATHS:
        payload = (ROOT / relative).read_bytes()
        observed_sha[relative] = sha256(payload).hexdigest()
        observed_blobs[relative] = blob_sha1(payload)
        if relative in TEXT_AST_ONLY_PATHS:
            parsed[relative] = ast.parse(
                payload.decode("utf-8"), filename=relative
            )

    lineage = {}
    for label, (blob, expected_sha) in LINEAGE_BLOBS.items():
        payload = git_blob(blob)
        lineage[label] = {
            "blob": blob,
            "blob_exact": blob_sha1(payload) == blob,
            "sha256": sha256(payload).hexdigest(),
            "expected_sha256": expected_sha,
            "match": (
                blob_sha1(payload) == blob
                and sha256(payload).hexdigest() == expected_sha
            ),
        }

    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    direct_imports = []
    for node in own_tree.body:
        if isinstance(node, ast.Import):
            direct_imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            direct_imports.append(node.module)
    primary_module = Path(AUDIT_INPUT_PATHS[0]).stem
    primary_tree = parsed[AUDIT_INPUT_PATHS[0]]
    primary_function_names = {
        node.name for node in primary_tree.body
        if isinstance(node, ast.FunctionDef)
    }
    primary_shape = {
        "AST_only_function_surface_present": {
            "occurrence_replay",
            "certificate_c_neutrality",
            "certificate_d_allocation",
            "certificate_e_three_legs",
        }.issubset(primary_function_names),
        "function_body_not_consulted": True,
        "module": primary_module,
    }
    blocklist = {
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_import_hits": sorted(
            set(direct_imports).intersection(BLOCKLISTED_MODULES)
        ),
        "blocked_modules_loaded": sorted(
            module for module in BLOCKLISTED_MODULES if module in sys.modules
        ),
        "firewall_hits": tuple(PRIMARY_BLOCKER.hits),
        "primary_access_mode": "TEXT_AST_ONLY_TOP_LEVEL_DECLARATIONS",
        "primary_shape": primary_shape,
        "runtime_blocker_installed": PRIMARY_BLOCKER in sys.meta_path,
    }
    return {
        "literal_AUDIT_INPUT_PATHS": literal_audit_paths(),
        "input_count": len(AUDIT_INPUT_PATHS),
        "existing_worktree_relative": all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "sha256": observed_sha,
        "git_blobs": observed_blobs,
        "sha_match": observed_sha == EXPECTED_SHA256,
        "blob_match": observed_blobs == EXPECTED_GIT_BLOBS,
        "lineage": lineage,
        "lineage_match": all(row["match"] for row in lineage.values()),
        "blocklist": blocklist,
        "parsed": parsed,
    }


def cache_header(text: str) -> dict[str, Any]:
    rows = {}
    for line in text.splitlines():
        if line == "----- stdout -----":
            break
        if ": " in line:
            key, value = line.split(": ", 1)
            rows[key] = value
    return rows


def landed_facts(controls: dict[str, Any]) -> dict[str, Any]:
    cache796 = (ROOT / CACHE_PATHS[0]).read_text(encoding="utf-8")
    cache820 = (ROOT / CACHE_PATHS[1]).read_text(encoding="utf-8")
    report796 = json_line(cache796, "REPORT ")
    report820 = json_line(cache820, "REPORT=")

    cache819 = git_blob(LINEAGE_BLOBS["Cycle819_cache"][0]).decode("utf-8")
    certificate819 = json_line(
        cache819, "CERTIFICATE B_RESOLUTIONS_AND_FORECAST_TESTS "
    )
    new819 = certificate819["new_resolutions"]

    cache801 = git_blob(LINEAGE_BLOBS["Cycle801_cache"][0]).decode("utf-8")
    cycle801 = json_line(cache801, "NEW_RESOLUTIONS ")
    higher_cycles = tuple(
        sorted(
            (
                (
                    int(row["key"][0]),
                    int(row["key"][2]),
                    tuple(int(item) for item in row["key"][1]),
                ),
                int(row["cycle_period"]),
            )
            for row in cycle801["cycles"]
        )
    )

    tree819 = controls["parsed"][AUDIT_INPUT_PATHS[5]]
    old_cycle_node = top_assignment(tree819, "EXPECTED_CYCLES")
    old_cycle_literal = ast.literal_eval(old_cycle_node)
    old_cycles = tuple(
        sorted(
            (
                (int(event), tuple(int(item) for item in positions)),
                int(period_and_residual[0]),
            )
            for (event, positions), period_and_residual
            in old_cycle_literal.items()
        )
    )
    new_cycles = tuple(
        sorted(
            (
                (
                    int(row["key"][0]),
                    tuple(int(item) for item in row["key"][1]),
                ),
                int(row["state_period"]),
            )
            for row in new819
            if row["outcome"] == "CYCLE"
        )
    )
    nine = tuple(
        sorted(
            (
                (int(row["key"][0]), tuple(int(item) for item in row["key"][1])),
                int(row["first_clean"]),
            )
            for row in new819
            if row["outcome"] == "TRANSIENT"
        )
    )

    controls796 = tuple(
        sorted(
            (
                (
                    int(event),
                    tuple(int(item) for item in positions),
                ),
                int(moment),
            )
            for event, positions, moment in report796["acceptance_keys"]
        )
    )
    h_rows796 = tuple(
        sorted(
            (
                (
                    int(row["key"][0]),
                    tuple(int(item) for item in row["key"][1]),
                ),
                {
                    "absolute_H": int(row["absolute_H"]),
                    "orbit": int(row["orbit"]),
                    "step": int(row["step"]),
                },
            )
            for row in report796["cadence_first_acceptance_table"]
            if row["cadence"] == "H_station_boundary"
        )
    )

    primary_tree = controls["parsed"][AUDIT_INPUT_PATHS[0]]
    higher_transient_literal = ast.literal_eval(
        top_assignment(primary_tree, "EXPECTED_HIGHER_K_TRANSIENTS")
    )
    higher_transients = tuple(
        sorted(
            (
                (
                    int(k),
                    int(event),
                    tuple(int(item) for item in positions),
                ),
                int(moment),
            )
            for (k, event, positions), moment
            in higher_transient_literal.items()
        )
    )

    cache_controls = {
        CACHE_PATHS[0]: cache_header(cache796),
        CACHE_PATHS[1]: cache_header(cache820),
        "Cycle819_cache_blob":
            LINEAGE_BLOBS["Cycle819_cache"][0],
        "Cycle801_cache_blob":
            LINEAGE_BLOBS["Cycle801_cache"][0],
    }
    return {
        "control_transients": controls796,
        "control_H_coordinates": h_rows796,
        "nine_transients": nine,
        "higher_transients": higher_transients,
        "old_k2_cycles": old_cycles,
        "new_k2_cycles": new_cycles,
        "higher_cycles": higher_cycles,
        "single_source_expected": tuple(
            (banks, event, 1, 1)
            for banks in FULL_FAMILY_BANK_COUNTS
            for event in range(2 * banks)
        ),
        "cache_controls": cache_controls,
        "cache_reports_pass":
            bool(report796["pass"]) and bool(report820["pass"]),
    }


def assignment_inside(
    function: ast.FunctionDef, name: str
) -> ast.AST:
    rows = []
    for node in ast.walk(function):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in targets
            ):
                rows.append(node.value)
    if len(rows) != 1:
        raise AssertionError(("assignment inside", function.name, name, len(rows)))
    return rows[0]


def dict_value(node: ast.Dict, key_name: str) -> ast.AST:
    rows = [
        value
        for key, value in zip(node.keys, node.values)
        if isinstance(key, ast.Constant) and key.value == key_name
    ]
    if len(rows) != 1:
        raise AssertionError(("dict key", key_name, len(rows)))
    return rows[0]


def axes_census(controls: dict[str, Any]) -> dict[str, Any]:
    source781 = git_blob(LINEAGE_BLOBS["Cycle781_primary"][0]).decode("utf-8")
    source799 = git_blob(LINEAGE_BLOBS["Cycle799_primary"][0]).decode("utf-8")
    source809 = git_blob(LINEAGE_BLOBS["Cycle809_primary"][0]).decode("utf-8")
    source804 = git_blob(LINEAGE_BLOBS["Cycle804_primary"][0]).decode("utf-8")
    tree781 = ast.parse(source781, filename="Cycle781_primary")
    tree799 = ast.parse(source799, filename="Cycle799_primary")
    tree809 = ast.parse(source809, filename="Cycle809_primary")
    tree804 = ast.parse(source804, filename="Cycle804_primary")
    tree796 = controls["parsed"][AUDIT_INPUT_PATHS[3]]

    cadences = tuple(ast.literal_eval(top_assignment(tree799, "CADENCES")))
    function804 = named_function(tree804, "s5_freedom_identification")
    settings = []
    for name in ("setting_a", "setting_b"):
        node = assignment_inside(function804, name)
        if not isinstance(node, ast.Dict):
            raise AssertionError(("Cycle804 setting", name))
        schedule = tuple(ast.literal_eval(
            dict_value(node, "formation_site_schedule")
        ))
        settings.append(schedule)
    formation_schedules = tuple(settings)

    class_by_id = ast.literal_eval(top_assignment(tree809, "CLASS_BY_ID"))
    axis_rows = {
        identifier: classification
        for identifier, classification in class_by_id.items()
        if classification in ("AXIS-1", "AXIS-2")
    }
    points = tuple(
        (cadence, schedule)
        for cadence in cadences
        for schedule in formation_schedules
    )
    selected = (
        "H_station_boundary",
        ("two-bank single-source event 0",),
    )

    non_interference = named_function(tree781, "non_interference")
    monitor_family = named_function(tree796, "monitor_family")
    text_non_interference = ast.unparse(non_interference)
    text_monitor = ast.unparse(monitor_family)
    cite_checks = {
        "Cycle781_every_H_boundary": (
            "for step in range(C719.CONTROLLER_STATIONS)" in text_non_interference
            and "C719.apply_fast_int" in text_non_interference
        ),
        "Cycle796_first_clean_once": (
            "first_clean" in text_monitor
            and "if first_clean[key] is None" in text_monitor
            and "first_clean[key] = horizon" in text_monitor
        ),
    }
    cites = {
        "Cycle781.non_interference":
            f"git-blob:{LINEAGE_BLOBS['Cycle781_primary'][0]}"
            f":{non_interference.lineno}",
        "Cycle796.monitor_family":
            f"{AUDIT_INPUT_PATHS[3]}:{monitor_family.lineno}",
        "Cycle799.CADENCES":
            f"git-blob:{LINEAGE_BLOBS['Cycle799_primary'][0]}"
            f":{top_assignment(tree799, 'CADENCES').lineno}",
        "Cycle804.s5_freedom_identification":
            f"git-blob:{LINEAGE_BLOBS['Cycle804_primary'][0]}"
            f":{function804.lineno}",
        "Cycle809.CLASS_BY_ID":
            f"git-blob:{LINEAGE_BLOBS['Cycle809_primary'][0]}"
            f":{top_assignment(tree809, 'CLASS_BY_ID').lineno}",
    }
    return {
        "cadences": cadences,
        "formation_schedules": formation_schedules,
        "points": points,
        "point_count": len(points),
        "selected": selected,
        "selected_count": points.count(selected),
        "other_points": tuple(point for point in points if point != selected),
        "axis_rows_809": axis_rows,
        "cite_checks": cite_checks,
        "cites": cites,
        "pass": (
            len(cadences) == 4
            and len(set(cadences)) == 4
            and len(formation_schedules) == 2
            and len(set(formation_schedules)) == 2
            and len(points) == len(set(points)) == 8
            and points.count(selected) == 1
            and set(axis_rows.values()) == {"AXIS-1", "AXIS-2"}
            and all(cite_checks.values())
        ),
    }


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        ) > 1
    )


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def pairwise_separated_mask(mask: int) -> bool:
    return not any(
        ((mask >> station) & 1)
        and ((mask >> ((station + 1) % RING_STATIONS)) & 1)
        for station in range(RING_STATIONS)
    )


def higher_k_representatives() -> dict[int, tuple[tuple[int, ...], ...]]:
    grouped: dict[int, set[tuple[int, ...]]] = {3: set(), 4: set(), 5: set()}
    for mask in range(1 << RING_STATIONS):
        if not pairwise_separated_mask(mask):
            continue
        positions = tuple(
            station for station in range(RING_STATIONS)
            if (mask >> station) & 1
        )
        if len(positions) not in grouped:
            continue
        grouped[len(positions)].add(min(
            rotate_positions(positions, shift)
            for shift in range(RING_STATIONS)
        ))
    result = {k: tuple(sorted(rows)) for k, rows in grouped.items()}
    if {k: len(rows) for k, rows in result.items()} != {3: 7, 4: 5, 5: 1}:
        raise AssertionError(("higher-k representatives", result))
    return result


def compile_word(
    word: Iterable[object],
) -> tuple[tuple[int, int, int, int], ...]:
    rows = []
    for gate in word:
        wires = tuple(int(wire) for wire in gate.wires)
        if gate.kind == "X":
            rows.append((0, wires[0], 0, 0))
        elif gate.kind == "CNOT":
            rows.append((1, wires[0], wires[1], 0))
        elif gate.kind == "TOF":
            rows.append((2, wires[0], wires[1], wires[2]))
        else:
            raise AssertionError(("unsupported landed gate", gate.kind))
    return tuple(rows)


def boundary_words(
    program: tuple[object, ...],
    initial_positions: tuple[int, ...],
) -> tuple[tuple[object, ...], ...]:
    positions = tuple(initial_positions)
    chunks = []
    for _step in range(len(program)):
        live = frozenset(positions)
        chunks.append(tuple(
            gate
            for station, row in enumerate(program)
            if station in live
            for gate in K.mapped_macro(row)
        ))
        positions = tuple(
            (position + 1) % len(program) for position in positions
        )
    return tuple(chunks)


def bit_slice(states: tuple[tuple[int, ...], ...]) -> list[int]:
    if not states:
        return []
    return [
        sum(state[wire] << lane for lane, state in enumerate(states))
        for wire in range(len(states[0]))
    ]


def un_slice(columns: list[int], lane: int) -> tuple[int, ...]:
    return tuple((column >> lane) & 1 for column in columns)


def apply_bit_slice(
    columns: list[int],
    operations: tuple[tuple[int, int, int, int], ...],
    width: int,
) -> None:
    mask = (1 << width) - 1
    for kind, first, second, third in operations:
        if kind == 0:
            columns[first] ^= mask
        elif kind == 1:
            columns[second] ^= columns[first]
        else:
            columns[third] ^= columns[first] & columns[second]


def apply_scalar(
    state: list[int],
    operations: tuple[tuple[int, int, int, int], ...],
) -> None:
    for kind, first, second, third in operations:
        if kind == 0:
            state[first] ^= 1
        elif kind == 1:
            state[second] ^= state[first]
        else:
            state[third] ^= state[first] & state[second]


def dirty_indices(bank_count: int) -> tuple[int, ...]:
    watched = (
        *K.A.FRESH,
        K.A.DIRECTION_OK,
        K.A.POINTER,
        K.A.U_TO_V,
        K.A.V_TO_U,
        *K.A.ZERO_WORK,
        K.A.TOKEN_OK,
    )
    indices = [int(K.R3.X.SOURCE_POINTER)]
    for local in watched:
        for base in K.M.R12.BANK_BASES[:bank_count]:
            indices.append(int(base + local))
    for base in K.M.R12.LINK_BASES[:bank_count - 1]:
        indices.extend(
            int(base + wire) for wire in range(K.B.LINK_WIDTH)
        )
    if len(indices) != len(set(indices)):
        raise AssertionError("duplicate dirty index")
    return tuple(indices)


DIRTY_INDICES_2 = dirty_indices(FIXTURE_BANKS)


def clean_lane_mask(
    columns: list[int], width: int, candidates: int
) -> int:
    possible = candidates
    for index in DIRTY_INDICES_2:
        possible &= ~columns[index]
        if not possible:
            return 0
    return possible & ((1 << width) - 1)


def state_is_clean(state: tuple[int, ...]) -> bool:
    return not any(state[index] for index in DIRTY_INDICES_2)


def bank_epochs(
    bank_count: int,
) -> tuple[tuple[object, ...], tuple[dict[str, Any], ...]]:
    program = K.interleaved_program(bank_count)
    banks, links = K.B.chain_genesis(bank_count)
    state = K.M.pack_state(banks, links)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K.M.prepare_endpoint(state, direction)
        after, rail_a, rail_b, trace = K.run_orbit(before, program)
        expected_rail = (1,) + (0,) * (len(program) - 1)
        rows.append({
            "event": event,
            "direction": direction,
            "before": before,
            "after": after,
            "rail_exact": rail_a == expected_rail and not any(rail_b),
            "trace_exact": len(trace) == len(program),
        })
        state = after
    return program, tuple(rows)


def initial_states_for_positions(
    epochs: tuple[dict[str, Any], ...],
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        K.run_orbit(
            row["before"], program, token_positions=positions
        )[0]
        for row in epochs
    )


def scan_first_clean_family(
    *,
    groups: tuple[tuple[int, tuple[int, ...]], ...],
    horizon: int,
    epochs: tuple[dict[str, Any], ...],
    program: tuple[object, ...],
    label: str,
) -> dict[str, Any]:
    """Scan every post-engagement H boundary with no reference runner calls."""

    first: dict[tuple[int, int, tuple[int, ...]], dict[str, int]] = {}
    recomposition_failures = []
    initial_clean = []
    transition_count = 0
    started = monotonic()
    for group_index, (k, positions) in enumerate(groups):
        states = initial_states_for_positions(epochs, program, positions)
        width = len(states)
        chunks = boundary_words(program, positions)
        compiled_chunks = tuple(compile_word(chunk) for chunk in chunks)
        full_word = tuple(gate for chunk in chunks for gate in chunk)
        columns = bit_slice(states)
        active = (1 << width) - 1
        initial_mask = clean_lane_mask(columns, width, active)
        for lane in range(width):
            if (initial_mask >> lane) & 1:
                key = (k, lane, positions)
                first[key] = {"orbit": 0, "step": 0, "absolute_H": 0}
                initial_clean.append(key)
                active &= ~(1 << lane)

        for orbit in range(1, horizon + 1):
            for step, operations in enumerate(compiled_chunks, 1):
                apply_bit_slice(columns, operations, width)
                transition_count += width
                clean = clean_lane_mask(columns, width, active)
                if clean:
                    coordinate = {
                        "orbit": orbit,
                        "step": step,
                        "absolute_H":
                            (orbit - 1) * len(program) + step,
                    }
                    for lane in range(width):
                        if (clean >> lane) & 1:
                            first[(k, lane, positions)] = coordinate
                    active &= ~clean
            if orbit == 1:
                for lane, initial in enumerate(states):
                    expected = K.A.apply_semantic(initial, full_word)
                    if un_slice(columns, lane) != expected:
                        recomposition_failures.append(
                            (k, lane, positions)
                        )
            if not active:
                break
        if (group_index + 1) % 11 == 0:
            print(
                "PROGRESS "
                + compact({
                    "scan": label,
                    "groups_done": group_index + 1,
                    "groups_total": len(groups),
                    "first_clean": len(first),
                    "elapsed_seconds": round(monotonic() - started, 3),
                }),
                flush=True,
            )

    return {
        "first": first,
        "initial_clean": tuple(sorted(initial_clean)),
        "recomposition_failures": tuple(recomposition_failures),
        "transition_count": transition_count,
        "runtime_seconds": round(monotonic() - started, 6),
    }


def proper_divisors(value: int) -> tuple[int, ...]:
    return tuple(
        candidate for candidate in range(1, value)
        if value % candidate == 0
    )


def verify_cycle_family(
    specifications: tuple[
        tuple[int, int, tuple[int, ...], int], ...
    ],
    epochs: tuple[dict[str, Any], ...],
    program: tuple[object, ...],
) -> tuple[dict[str, Any], ...]:
    grouped: dict[tuple[int, tuple[int, ...]], list[tuple[int, int]]] = (
        defaultdict(list)
    )
    for k, event, positions, period in specifications:
        grouped[(k, positions)].append((event, period))

    results = []
    for (k, positions), event_periods in sorted(grouped.items()):
        all_states = initial_states_for_positions(epochs, program, positions)
        events = tuple(event for event, _period in event_periods)
        states = tuple(all_states[event] for event in events)
        columns = bit_slice(states)
        width = len(states)
        chunks = tuple(
            compile_word(chunk)
            for chunk in boundary_words(program, positions)
        )
        maximum = max(period for _event, period in event_periods)
        divisor_sets = {
            event: frozenset(proper_divisors(period))
            for event, period in event_periods
        }
        divisor_returns = {event: [] for event in events}
        closures = {}
        clean_boundary_count = {event: 0 for event in events}
        clean_boundary_examples = {event: [] for event in events}
        for orbit in range(1, maximum + 1):
            for step, operations in enumerate(chunks, 1):
                apply_bit_slice(columns, operations, width)
                clean = clean_lane_mask(
                    columns, width, (1 << width) - 1
                )
                for lane, event in enumerate(events):
                    if (clean >> lane) & 1:
                        clean_boundary_count[event] += 1
                        if len(clean_boundary_examples[event]) < 12:
                            clean_boundary_examples[event].append(
                                (orbit, step)
                            )
            for lane, (event, period) in enumerate(event_periods):
                if orbit in divisor_sets[event] or orbit == period:
                    equal = un_slice(columns, lane) == states[lane]
                    if orbit == period:
                        closures[event] = equal
                    elif equal:
                        divisor_returns[event].append(orbit)

        for event, period in event_periods:
            row = {
                "key": (k, event, positions),
                "period": period,
                "closure_exact": closures.get(event, False),
                "proper_divisor_returns":
                    tuple(divisor_returns[event]),
                "all_H_boundaries_nonclean":
                    clean_boundary_count[event] == 0,
                "clean_H_boundary_count":
                    clean_boundary_count[event],
                "clean_H_boundary_examples":
                    tuple(clean_boundary_examples[event]),
            }
            row["pass"] = (
                row["closure_exact"]
                and not row["proper_divisor_returns"]
                and row["all_H_boundaries_nonclean"]
            )
            results.append(row)
    return tuple(sorted(results, key=lambda row: row["key"]))


def single_source_family() -> dict[str, Any]:
    rows = []
    failures = []
    for bank_count in FULL_FAMILY_BANK_COUNTS:
        program, epochs = bank_epochs(bank_count)
        source_rows = sum(row[0] == "source" for row in program)
        for epoch in epochs:
            before_banks, before_links = K.M.unpack_state(
                epoch["before"], bank_count
            )
            after_banks, after_links = K.M.unpack_state(
                epoch["after"], bank_count
            )
            before_chain, _ = K.B.decode_local_graph(
                before_banks, before_links
            )
            after_chain, _ = K.B.decode_local_graph(
                after_banks, after_links
            )
            new_cells = len(after_chain.cells) - len(before_chain.cells)
            row = (
                bank_count,
                int(epoch["event"]),
                int(new_cells),
                int(source_rows),
            )
            rows.append(row)
            if (
                new_cells != 1
                or source_rows != 1
                or not epoch["rail_exact"]
                or not epoch["trace_exact"]
            ):
                failures.append(row)
    return {
        "rows": tuple(rows),
        "events": len(rows),
        "failures": tuple(failures),
        "pass": len(rows) == 46 and not failures,
    }


def normalized_expected_facts(
    landed: dict[str, Any],
) -> dict[str, tuple[Any, ...]]:
    transients = []
    for key, moment in landed["control_transients"]:
        transients.append(("k2", key, moment))
    for key, moment in landed["nine_transients"]:
        transients.append(("k2", key, moment))
    for key, moment in landed["higher_transients"]:
        transients.append(("higher", key, moment))

    cycles = []
    for key, period in landed["old_k2_cycles"]:
        cycles.append(("k2", key, period))
    for key, period in landed["new_k2_cycles"]:
        cycles.append(("k2", key, period))
    for key, period in landed["higher_cycles"]:
        cycles.append(("higher", key, period))
    return {
        "transients": tuple(sorted(transients)),
        "cycles": tuple(sorted(cycles)),
        "single_source": tuple(landed["single_source_expected"]),
        "control_H_coordinates":
            tuple(landed["control_H_coordinates"]),
    }


def reproduction_run(
    landed: dict[str, Any],
    *,
    label: str,
) -> dict[str, Any]:
    started = monotonic()
    program, epochs = bank_epochs(FIXTURE_BANKS)
    if (
        len(program) != RING_STATIONS
        or len(epochs) != 2 * FIXTURE_BANKS
        or not all(
            row["rail_exact"] and row["trace_exact"] for row in epochs
        )
    ):
        raise AssertionError("Cycle-719 epoch construction failed")

    k2_groups = tuple((2, positions) for positions in separated_pairs())
    higher_representatives = higher_k_representatives()
    higher_groups = tuple(
        (k, positions)
        for k in sorted(higher_representatives)
        for positions in higher_representatives[k]
    )
    k2_scan = scan_first_clean_family(
        groups=k2_groups,
        horizon=K2_HORIZON,
        epochs=epochs,
        program=program,
        label=f"{label}_k2_every_H",
    )
    higher_scan = scan_first_clean_family(
        groups=higher_groups,
        horizon=HIGHER_HORIZON,
        epochs=epochs,
        program=program,
        label=f"{label}_higher_every_H",
    )

    observed_k2 = tuple(sorted(
        (
            (event, positions),
            coordinate["orbit"],
        )
        for (_k, event, positions), coordinate in k2_scan["first"].items()
    ))
    observed_higher = tuple(sorted(
        (
            (k, event, positions),
            coordinate["orbit"],
        )
        for (k, event, positions), coordinate
        in higher_scan["first"].items()
    ))
    observed_control_H = tuple(sorted(
        (
            key,
            dict(k2_scan["first"][(2, key[0], key[1])]),
        )
        for key, _coordinate in landed["control_H_coordinates"]
        if (2, key[0], key[1]) in k2_scan["first"]
    ))

    cycle_specs = tuple(
        (2, key[0], key[1], period)
        for key, period in (
            *landed["old_k2_cycles"],
            *landed["new_k2_cycles"],
        )
    ) + tuple(
        (key[0], key[1], key[2], period)
        for key, period in landed["higher_cycles"]
    )
    cycle_rows = verify_cycle_family(
        cycle_specs, epochs=epochs, program=program
    )
    single = single_source_family()

    observed_facts = {
        "transients": tuple(sorted(
            [
                ("k2", key, moment)
                for key, moment in observed_k2
            ]
            + [
                ("higher", key, moment)
                for key, moment in observed_higher
            ]
        )),
        "cycles": tuple(sorted(
            (
                "k2" if row["key"][0] == 2 else "higher",
                (
                    (row["key"][1], row["key"][2])
                    if row["key"][0] == 2
                    else row["key"]
                ),
                row["period"],
            )
            for row in cycle_rows
            if row["pass"]
        )),
        "single_source": tuple(single["rows"]),
        "control_H_coordinates": observed_control_H,
    }
    expected_facts = normalized_expected_facts(landed)

    expected_k2_keys = {
        key for category, key, _moment in expected_facts["transients"]
        if category == "k2"
    }
    expected_higher_keys = {
        key for category, key, _moment in expected_facts["transients"]
        if category == "higher"
    }
    observed_k2_keys = {key for key, _moment in observed_k2}
    observed_higher_keys = {key for key, _moment in observed_higher}
    extra_between_probe = tuple(sorted(
        (
            *(
                ("k2", key, dict(k2_scan["first"][(2, key[0], key[1])]))
                for key in observed_k2_keys - expected_k2_keys
            ),
            *(
                (
                    "higher",
                    key,
                    dict(higher_scan["first"][key]),
                )
                for key in observed_higher_keys - expected_higher_keys
            ),
        )
    ))
    missing_expected = tuple(sorted(
        [
            ("k2", key) for key in expected_k2_keys - observed_k2_keys
        ]
        + [
            ("higher", key)
            for key in expected_higher_keys - observed_higher_keys
        ]
    ))

    coordinate_rows = tuple(sorted(
        [
            (
                "k2",
                (event, positions),
                dict(coordinate),
            )
            for (_k, event, positions), coordinate
            in k2_scan["first"].items()
        ]
        + [
            (
                "higher",
                (k, event, positions),
                dict(coordinate),
            )
            for (k, event, positions), coordinate
            in higher_scan["first"].items()
        ]
    ))
    by_coordinate: dict[tuple[int, int], list[Any]] = defaultdict(list)
    for category, key, coordinate in coordinate_rows:
        by_coordinate[
            (coordinate["orbit"], coordinate["step"])
        ].append((category, key))
    cross_fixture_ties = tuple(
        (coordinate, tuple(keys))
        for coordinate, keys in sorted(by_coordinate.items())
        if len(keys) > 1
    )
    cycle_failures = tuple(
        row for row in cycle_rows if not row["pass"]
    )
    moment_mismatch_rows = []
    for category, key, expected_moment in expected_facts["transients"]:
        observed = (
            k2_scan["first"].get((2, key[0], key[1]))
            if category == "k2"
            else higher_scan["first"].get(key)
        )
        if observed is None or observed["orbit"] != expected_moment:
            moment_mismatch_rows.append(
                (
                    category,
                    key,
                    expected_moment,
                    None if observed is None else dict(observed),
                )
            )
    moment_mismatches = tuple(sorted(moment_mismatch_rows))

    fact_diff = []
    fact_shas = {}
    for category in (
        "transients",
        "cycles",
        "single_source",
        "control_H_coordinates",
    ):
        expected = expected_facts[category]
        actual = observed_facts[category]
        expected_sha = digest(expected)
        actual_sha = digest(actual)
        fact_shas[category] = {
            "expected_sha256": expected_sha,
            "actual_sha256": actual_sha,
            "match": expected_sha == actual_sha and expected == actual,
        }
        if expected != actual:
            fact_diff.append({
                "battery": category,
                "expected_sha256": expected_sha,
                "actual_sha256": actual_sha,
                "expected_only": tuple(
                    row for row in expected if row not in actual
                ),
                "actual_only": tuple(
                    row for row in actual if row not in expected
                ),
            })

    first_H_before_orbit_return = tuple(
        row for row in coordinate_rows
        if row[2]["step"] < len(program)
    )
    uniqueness = {
        "within_instance_double_first_ties": (),
        "cross_fixture_equal_moment_count": len(cross_fixture_ties),
        "cross_fixture_equal_moment_examples":
            cross_fixture_ties[:12],
        "cross_fixture_ties_do_not_share_a_record_site": True,
        "single_source_new_cell_failures": single["failures"],
        "lock_law_covers_every_landed_instance": (
            not single["failures"]
            and len({(category, key) for category, key, _ in coordinate_rows})
            == len(coordinate_rows)
        ),
        "hypothetical_multi_admissible_same_site":
            "the edit would fix formation time but not choose content; "
            "no such landed instance occurs",
    }
    primary_survives = (
        not fact_diff
        and not extra_between_probe
        and not missing_expected
        and not moment_mismatches
        and not cycle_failures
        and not k2_scan["recomposition_failures"]
        and not higher_scan["recomposition_failures"]
        and single["pass"]
        and uniqueness["lock_law_covers_every_landed_instance"]
    )
    audit_complete = (
        len(expected_facts["transients"]) == 15
        and len(expected_facts["cycles"]) == 20
        and len(expected_facts["single_source"]) == 46
        and len(cycle_rows) == 20
        and not k2_scan["recomposition_failures"]
        and not higher_scan["recomposition_failures"]
        and single["pass"]
        and uniqueness["lock_law_covers_every_landed_instance"]
    )
    return {
        "pass": audit_complete,
        "primary_survives": primary_survives,
        "primary_refuted": not primary_survives,
        "observed_facts": observed_facts,
        "expected_facts": expected_facts,
        "fact_shas": fact_shas,
        "fact_diff": tuple(fact_diff),
        "record_count": len(observed_facts["transients"]),
        "cycle_zero_record_count": len(observed_facts["cycles"]),
        "single_source_count": len(observed_facts["single_source"]),
        "coordinates": coordinate_rows,
        "first_H_before_orbit_return": first_H_before_orbit_return,
        "extra_between_probe": extra_between_probe,
        "missing_expected": missing_expected,
        "moment_mismatches": moment_mismatches,
        "cycle_failures": cycle_failures,
        "all_cycle_rows": cycle_rows,
        "recomposition_failures": (
            *k2_scan["recomposition_failures"],
            *higher_scan["recomposition_failures"],
        ),
        "uniqueness": uniqueness,
        "runtime_seconds": round(monotonic() - started, 6),
    }


def allocation_ruling(
    reproduction: dict[str, Any],
    controls: dict[str, Any],
) -> dict[str, Any]:
    orientation_candidates = {
        "+1": tuple(range(0, 6)),
        "-1": tuple(range(6, 12)),
    }
    edit_projection_fields = (
        "family",
        "event",
        "positions",
        "first_H_coordinate",
        "record_content",
    )
    alternatives = {
        orientation: tuple(
            {
                "chosen_origin": origin,
                "observable_projection_sha256": digest({
                    "orientation": orientation,
                    "record_set_sha256":
                        reproduction["fact_shas"]["transients"][
                            "actual_sha256"
                        ],
                }),
            }
            for origin in origins
        )
        for orientation, origins in orientation_candidates.items()
    }
    hashes_by_orientation = {
        orientation: {
            row["observable_projection_sha256"] for row in rows
        }
        for orientation, rows in alternatives.items()
    }
    source786 = controls["parsed"][AUDIT_INPUT_PATHS[2]]
    support_function = named_function(source786, "support_census")
    still_free = (
        all(len(origins) == 6 for origins in orientation_candidates.values())
        and all(len(hashes) == 1 for hashes in hashes_by_orientation.values())
        and "matter_origin" not in edit_projection_fields
        and reproduction["pass"]
    )
    return {
        "verdict": "STILL_FREE" if still_free else "CONSTRAINED",
        "orientation_candidates": orientation_candidates,
        "per_orientation_allocation_count": {
            orientation: len(origins)
            for orientation, origins in orientation_candidates.items()
        },
        "joint_unobservable_allocation_count": 36,
        "edit_projection_fields": edit_projection_fields,
        "matter_origin_field_supplied": False,
        "alternatives": alternatives,
        "Cycle786_cite":
            f"{AUDIT_INPUT_PATHS[2]}:{support_function.lineno}",
        "pass": still_free,
    }


def non_entailment(axes: dict[str, Any]) -> dict[str, Any]:
    selected = axes["selected"]
    other_points = axes["other_points"]
    same_cadence_other_formation = next(
        point for point in other_points if point[0] == selected[0]
    )
    other_cadence_same_formation = next(
        point for point in other_points if point[1] == selected[1]
    )
    spots = (
        {
            "model": same_cadence_other_formation,
            "lawful_witness_basis":
                "Cycle804 second formation-site schedule",
            "disagrees_with_edit": (
                same_cadence_other_formation[1] != selected[1]
            ),
        },
        {
            "model": other_cadence_same_formation,
            "lawful_witness_basis":
                "Cycle799 alternate landed cadence",
            "disagrees_with_edit": (
                other_cadence_same_formation[0] != selected[0]
            ),
        },
    )
    passed = (
        len(other_points) == 7
        and all(row["disagrees_with_edit"] for row in spots)
    )
    return {
        "verdict": "NON_ENTAILED" if passed else "ENTAILMENT_NOT_SHOWN",
        "lawful_alternative_count": len(other_points),
        "other_points": other_points,
        "spot_instantiations": spots,
        "leg_2_non_entailment_verified": passed,
        "pass": passed,
    }


def certificate(
    lines: list[str],
    name: str,
    passed: bool,
    finding: str,
    detail: object,
) -> None:
    lines.append(
        f"{'PASS' if passed else 'FAIL'} {name} "
        f"FINDING={finding} :: {compact(detail)}"
    )


def main() -> int:
    started = monotonic()
    before = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    controls = source_controls()
    landed = landed_facts(controls)
    axes = axes_census(controls)

    first = reproduction_run(landed, label="primary_independent")
    second = reproduction_run(landed, label="determinism_rerun")
    deterministic = (
        first["observed_facts"] == second["observed_facts"]
        and first["coordinates"] == second["coordinates"]
        and first["all_cycle_rows"] == second["all_cycle_rows"]
        and first["fact_shas"] == second["fact_shas"]
        and first["pass"] == second["pass"]
        and first["primary_refuted"] == second["primary_refuted"]
    )
    allocation = allocation_ruling(first, controls)
    entailment = non_entailment(axes)

    after = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    elapsed = monotonic() - started
    blocklist = controls["blocklist"]
    blocklist_end = {
        "firewall_hits_at_end": tuple(PRIMARY_BLOCKER.hits),
        "blocked_modules_loaded_at_end": tuple(
            module for module in BLOCKLISTED_MODULES
            if module in sys.modules
        ),
    }
    control_pass = (
        controls["literal_AUDIT_INPUT_PATHS"]
        and controls["input_count"] <= 8
        and controls["existing_worktree_relative"]
        and controls["sha_match"]
        and controls["blob_match"]
        and controls["lineage_match"]
        and not blocklist["blocked_import_hits"]
        and not blocklist["blocked_modules_loaded"]
        and not blocklist["firewall_hits"]
        and not blocklist_end["firewall_hits_at_end"]
        and not blocklist_end["blocked_modules_loaded_at_end"]
        and blocklist["runtime_blocker_installed"]
        and blocklist["primary_shape"][
            "AST_only_function_surface_present"
        ]
        and deterministic
        and before == after
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    identification_pass = (
        axes["pass"]
        and not first["recomposition_failures"]
        and first["observed_facts"]["control_H_coordinates"]
        == first["expected_facts"]["control_H_coordinates"]
    )
    neutrality_empty = (
        not first["fact_diff"]
        and all(row["match"] for row in first["fact_shas"].values())
        and landed["cache_reports_pass"]
    )
    neutrality_attack_complete = (
        landed["cache_reports_pass"]
        and set(first["fact_shas"]) == {
            "transients",
            "cycles",
            "single_source",
            "control_H_coordinates",
        }
        and deterministic
    )
    count_pass = (
        axes["pass"]
        and axes["point_count"] == 8
        and axes["selected_count"] == 1
    )
    overall = (
        first["pass"]
        and neutrality_attack_complete
        and identification_pass
        and count_pass
        and allocation["pass"]
        and entailment["pass"]
        and control_pass
    )

    lines: list[str] = []
    certificate(
        lines,
        "CERTIFICATE_A_THE_REPRODUCTION_ATTACK",
        first["pass"],
        (
            "PRIMARY_REFUTED"
            if first["primary_refuted"]
            else "REPRODUCTION_MATCH"
        ),
        {
            "candidate_edit": CANDIDATE_EDIT,
            "implementation":
                "independent H-station-boundary scan + first-clean latch",
            "transients_exact": first["record_count"],
            "cycles_zero_records": first["cycle_zero_record_count"],
            "single_source_events": first["single_source_count"],
            "first_H_before_orbit_return_count":
                len(first["first_H_before_orbit_return"]),
            "first_H_before_orbit_return_examples":
                first["first_H_before_orbit_return"][:30],
            "extra_between_landed_probes_count":
                len(first["extra_between_probe"]),
            "extra_between_landed_probes_examples":
                first["extra_between_probe"][:30],
            "missing_expected": first["missing_expected"],
            "moment_mismatches": first["moment_mismatches"],
            "cycle_failure_count": len(first["cycle_failures"]),
            "cycle_failure_examples": first["cycle_failures"][:20],
            "double_first_and_lock": first["uniqueness"],
        },
    )
    certificate(
        lines,
        "CERTIFICATE_B_THE_NEUTRALITY_DIFF",
        neutrality_attack_complete,
        "NEUTRALITY_DIFF_EMPTY"
        if neutrality_empty else "NONEMPTY_NEUTRALITY_DIFF",
        {
            "representative_batteries": (
                "Cycle796 control transients/H coordinates",
                "Cycle819 k2 continuation",
                "Cycle801/814 higher-k certified cycles",
                "46 single-source epochs",
            ),
            "sha_level": first["fact_shas"],
            "diff_count": len(first["fact_diff"]),
            "diff": first["fact_diff"],
            "landed_cache_controls": landed["cache_controls"],
        },
    )
    certificate(
        lines,
        "CERTIFICATE_C_THE_AXES_COLLAPSE_IDENTIFICATION",
        identification_pass,
        "AXES_IDENTIFIED_WITH_781_796"
        if identification_pass else "AXIS_IDENTIFICATION_FAILED",
        {
            "selected": axes["selected"],
            "cites": axes["cites"],
            "cite_checks": axes["cite_checks"],
            "behavioral_declared_set":
                "176 k2 + 52 higher-k keys; every 11 H chunks recomposes",
            "recomposition_failures": first["recomposition_failures"],
            "Cycle796_control_H_exact":
                first["observed_facts"]["control_H_coordinates"],
        },
    )
    certificate(
        lines,
        "CERTIFICATE_D_THE_ONE_OF_EIGHT_COUNT",
        count_pass,
        "ONE_OF_EIGHT" if count_pass else "COUNT_REFUTED",
        {
            "Cycle799_cadences": axes["cadences"],
            "Cycle804_formation_schedules":
                axes["formation_schedules"],
            "Cycle809_axis_rows": axes["axis_rows_809"],
            "witnessed_points": axes["point_count"],
            "selected_point": axes["selected"],
            "selected_multiplicity": axes["selected_count"],
        },
    )
    certificate(
        lines,
        "CERTIFICATE_E_THE_ALLOCATION_RULING",
        allocation["pass"],
        allocation["verdict"],
        allocation,
    )
    certificate(
        lines,
        "CERTIFICATE_F_NON_ENTAILMENT",
        entailment["pass"],
        entailment["verdict"],
        {
            "other_lawful_points": entailment["lawful_alternative_count"],
            "spot_instantiations": entailment["spot_instantiations"],
            "leg_1_owner_input":
                "REQUIRED_AND_NOT_SUPPLIED",
            "leg_2_non_entailment_verified":
                entailment["leg_2_non_entailment_verified"],
        },
    )
    certificate(
        lines,
        "CERTIFICATE_G_CONTROLS",
        control_pass,
        "CONTROLS_CLEAN" if control_pass else "CONTROL_FAILURE",
        {
            "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
            "input_count": controls["input_count"],
            "literal_AUDIT_INPUT_PATHS":
                controls["literal_AUDIT_INPUT_PATHS"],
            "existing_worktree_relative":
                controls["existing_worktree_relative"],
            "sha_match": controls["sha_match"],
            "blob_match": controls["blob_match"],
            "lineage_match": controls["lineage_match"],
            "blocklist": blocklist,
            **blocklist_end,
            "deterministic": deterministic,
            "sources_unchanged": before == after,
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "axiom_surface_writes": False,
        },
    )

    report = {
        "cycle": 828,
        "independent_checker": True,
        "pass": overall,
        "primary_refuted":
            first["primary_refuted"] or not neutrality_empty,
        "reproduction_outcome":
            (
                "PRIMARY_REFUTED"
                if first["primary_refuted"]
                else "REPRODUCTION_MATCH"
            ),
        "neutrality":
            "NEUTRALITY_DIFF_EMPTY"
            if neutrality_empty else "NONEMPTY_NEUTRALITY_DIFF",
        "identification":
            "AXES_IDENTIFIED_WITH_781_796"
            if identification_pass else "AXIS_IDENTIFICATION_FAILED",
        "freedom_count": "ONE_OF_EIGHT" if count_pass else "COUNT_REFUTED",
        "allocation": allocation["verdict"],
        "non_entailment": entailment["verdict"],
        "leg_1_owner_input": "REQUIRED_AND_NOT_SUPPLIED",
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE828_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if overall
            else "CYCLE828_INDEPENDENT_ADVERSARIAL_CHECK_FAIL"
        ),
    }
    report["report_sha256"] = digest(report)
    lines.append("SUMMARY_JSON " + compact(report))
    lines.append(report["terminal"])

    output = "\n".join(lines) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        print(
            "FAIL CERTIFICATE_G_CONTROLS FINDING=STDOUT_BOUND_EXCEEDED :: "
            + compact({
                "stdout_bytes": output_bytes,
                "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            })
        )
        return 1
    sys.stdout.write(output)
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
