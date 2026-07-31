#!/usr/bin/env python3
"""Cycle 837 independent adversarial check: separation five and the (3,3) tie.

The Cycle-837 primary and all landed Python sources are SHA-pinned text/AST
inputs only.  This checker independently enumerates the landed catalog,
partitions every resolved key from the landed resolution records, and derives
the C11 propagation and positional controls with stdlib-only exact arithmetic.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1200
STDOUT_LIMIT_BYTES = 150 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle837_why_sep5_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle822_basin_independent_check_2026_07_28.py",
    "scripts/frontier_cycle832_cohort_moment_law_2026_07_28.py",
    "logs/runner-cache/frontier_cycle818_period_structure_census_2026_07_28.txt",
    "logs/runner-cache/frontier_cycle832_cohort_moment_law_2026_07_28.txt",
)

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
CORE_PATH = AUDIT_INPUT_PATHS[1]
BASIN_PATH = AUDIT_INPUT_PATHS[2]
COHORT_PATH = AUDIT_INPUT_PATHS[3]
PERIOD_LOG_PATH = AUDIT_INPUT_PATHS[4]
COHORT_LOG_PATH = AUDIT_INPUT_PATHS[5]
PYTHON_TEXT_AST_PATHS = AUDIT_INPUT_PATHS[:4]
PRIMARY_MODULE = Path(PRIMARY_PATH).stem

EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "f210ebc75909977eaa468a20b45f9a75ab9ad2e2ac0e48d0c4aab04d3a0a9a9f",
    CORE_PATH:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    BASIN_PATH:
        "c2fd23a7bb47caff70e9561fc9da46feef422c053954fa1af925901a1884ed0b",
    COHORT_PATH:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    PERIOD_LOG_PATH:
        "94bc32640518f097cb09060f9c378d26d73e263539573e3b8e75ed2aab1b857e",
    COHORT_LOG_PATH:
        "89640947e097728e73cbd58a0039364e684dc2e81d840a087fdddd69598bd450",
}
EXPECTED_GIT_BLOBS = {
    PRIMARY_PATH: "8889e129f006bdaf4d3a3d7dd7bb3f1cac595ca7",
    CORE_PATH: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    BASIN_PATH: "6d48f5d86006a5f6718b5993eaecd5ec69d86112",
    COHORT_PATH: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    PERIOD_LOG_PATH: "3544e3beada65b3480d352e2701f6e21b3f9ae2d",
    COHORT_LOG_PATH: "86d14cac924d71a6d4702ffac3dbeacc5c5d0f52",
}

RING_STATIONS = 11
EVENTS = (0, 1, 2, 3)

Pair = tuple[int, int]
Key = tuple[int, Pair]


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    """Fail closed if any code path tries to import the Cycle-837 primary."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname == PRIMARY_MODULE:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


def assignment_node(tree: ast.Module, name: str) -> ast.expr:
    matches = tuple(
        node.value
        for node in tree.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and (
            (
                isinstance(node, ast.Assign)
                and any(
                    isinstance(target, ast.Name) and target.id == name
                    for target in node.targets
                )
            )
            or (
                isinstance(node, ast.AnnAssign)
                and isinstance(node.target, ast.Name)
                and node.target.id == name
            )
        )
    )
    if len(matches) != 1:
        raise AssertionError(("assignment count", name, len(matches)))
    return matches[0]


def literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assignment_node(tree, name))


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = tuple(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(matches) != 1:
        raise AssertionError(("function count", name, len(matches)))
    return matches[0]


def one_json_line(payload: bytes, prefix: str) -> dict[str, object]:
    matches = tuple(
        json.loads(line[len(prefix):])
        for line in payload.decode().splitlines()
        if line.startswith(prefix)
    )
    if len(matches) != 1:
        raise AssertionError(("JSON line count", prefix, len(matches)))
    return matches[0]


def json_lines(payload: bytes, prefix: str) -> tuple[dict[str, object], ...]:
    return tuple(
        json.loads(line[len(prefix):])
        for line in payload.decode().splitlines()
        if line.startswith(prefix)
    )


def freeze_key(value: object) -> Key:
    event, pair = value
    return int(event), (int(pair[0]), int(pair[1]))


def freeze_pair(value: object) -> Pair:
    return int(value[0]), int(value[1])


def cyclic_distance(pair: Pair) -> int:
    left, right = pair
    clockwise = (right - left) % RING_STATIONS
    counterclockwise = (left - right) % RING_STATIONS
    return min(clockwise, counterclockwise)


def geometric_pairs(separation: int) -> tuple[Pair, ...]:
    return tuple(
        pair
        for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_distance(pair) == separation
    )


def landed_pairs() -> tuple[Pair, ...]:
    """Independent catalog definition: unordered pairs at distance > 1."""
    return tuple(
        pair
        for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_distance(pair) > 1
    )


def source_packet() -> tuple[
    dict[str, bytes],
    dict[str, ast.Module],
    dict[str, object],
]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payloads[path], filename=path)
        for path in PYTHON_TEXT_AST_PATHS
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
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
    expected_stdlib_imports = (
        "ast", "collections", "hashlib", "importlib.abc", "itertools",
        "json", "pathlib", "sys", "time",
    )
    primary_function_names = {
        node.name for node in trees[PRIMARY_PATH].body
        if isinstance(node, ast.FunctionDef)
    }
    source_rows = tuple({
        "path": path,
        "exists": (ROOT / path).is_file(),
        "worktree_relative": not Path(path).is_absolute(),
        "sha256": sha_rows[path],
        "expected_sha256": EXPECTED_SHA256[path],
        "sha256_exact": sha_rows[path] == EXPECTED_SHA256[path],
        "git_blob": blob_rows[path],
        "expected_git_blob": EXPECTED_GIT_BLOBS[path],
        "git_blob_exact": blob_rows[path] == EXPECTED_GIT_BLOBS[path],
        "access": (
            "TEXT_AST_ONLY_BLOCKLISTED"
            if path == PRIMARY_PATH
            else (
                "TEXT_AST_ONLY"
                if path in PYTHON_TEXT_AST_PATHS
                else "TEXT_JSON_LINES_ONLY"
            )
        ),
    } for path in AUDIT_INPUT_PATHS)
    controls = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "all_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"]
            for row in source_rows
        ),
        "source_rows": source_rows,
        "primary_path": PRIMARY_PATH,
        "primary_module": PRIMARY_MODULE,
        "primary_access": "TEXT_AST_ONLY_BLOCKLISTED",
        "primary_AST_markers_present": {
            "separation_census_certificate",
            "dynamics_probe_certificate",
            "candidate_law_certificate",
        } <= primary_function_names,
        "primary_loaded": PRIMARY_MODULE in sys.modules,
        "firewall_hits": tuple(FIREWALL.hits),
        "direct_imports": direct_imports,
        "expected_stdlib_imports": expected_stdlib_imports,
        "stdlib_only": direct_imports == expected_stdlib_imports,
    }
    controls["source_pass"] = (
        controls["AUDIT_INPUT_PATHS_literal"]
        and controls["named_input_count"] == controls["read_cap"]
        and controls["all_paths_existing_worktree_relative"]
        and all(
            row["sha256_exact"] and row["git_blob_exact"]
            for row in source_rows
        )
        and controls["primary_AST_markers_present"]
        and not controls["primary_loaded"]
        and not controls["firewall_hits"]
        and controls["stdlib_only"]
    )
    return payloads, trees, controls


def explicit_earlier_resolved(tree: ast.Module) -> frozenset[Key]:
    """Extract only the literal keys in EARLIER_RESOLVED, not its star."""
    value = assignment_node(tree, "EARLIER_RESOLVED")
    if (
        not isinstance(value, ast.Call)
        or not isinstance(value.func, ast.Name)
        or value.func.id != "frozenset"
        or len(value.args) != 1
        or not isinstance(value.args[0], ast.Set)
    ):
        raise AssertionError("EARLIER_RESOLVED does not have expected AST")
    return frozenset(
        freeze_key(ast.literal_eval(element))
        for element in value.args[0].elts
        if not isinstance(element, ast.Starred)
    )


def landed_evidence(
    payloads: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    period_rows_all = json_lines(
        payloads[PERIOD_LOG_PATH], "PERIOD_TABLE_ROW "
    )
    strict_k2_rows = tuple(
        row for row in period_rows_all if int(row["k"]) == 2
    )
    preregistration = one_json_line(
        payloads[COHORT_LOG_PATH],
        "V1_HISTORICAL_PRE_REGISTRATION_RETRACTED ",
    )
    backbone_certificate = one_json_line(
        payloads[COHORT_LOG_PATH],
        "CERTIFICATE A_36_KEY_BACKBONE ",
    )
    moment_certificate = one_json_line(
        payloads[COHORT_LOG_PATH],
        "CERTIFICATE C_MOMENT_PREDICTION_RERULING ",
    )
    cohort_summary = one_json_line(
        payloads[COHORT_LOG_PATH], "SUMMARY_JSON "
    )

    catalog_pairs = landed_pairs()
    catalog = frozenset(
        (event, pair) for pair in catalog_pairs for event in EVENTS
    )
    open_keys = frozenset(
        (int(event), freeze_pair(pair))
        for pair, event in preregistration["open_pair_event_keys"]
    )
    resolved_from_complement = catalog - open_keys

    classification_rows = tuple(
        backbone_certificate["classification_rows"]
    )
    transient_cohort_keys = frozenset(
        freeze_key(row["key"])
        for row in classification_rows
        if row["classification"] == "TRANSIENT_COHORT"
    )
    strict_cycle_keys = frozenset(
        (
            int(row["event"]),
            freeze_pair(row["positions"]),
        )
        for row in strict_k2_rows
    )
    literal_earlier = explicit_earlier_resolved(trees[COHORT_PATH])
    earlier_transient_keys = frozenset(
        resolved_from_complement
        - transient_cohort_keys
        - strict_cycle_keys
    )
    resolved_from_lists = frozenset(
        literal_earlier | transient_cohort_keys | strict_cycle_keys
    )
    backbone_pairs = frozenset(
        freeze_pair(pair)
        for pair in backbone_certificate["backbone_pairs"]
    )

    separated_source = ast.unparse(
        function_node(trees[BASIN_PATH], "separated_pairs")
    )
    held_source = ast.unparse(
        function_node(trees[CORE_PATH], "held_certificate")
    )
    catalog_definition_AST_exact = (
        "combinations(range(RING_STATIONS), 2)" in separated_source
        and "> 1" in separated_source
        and "range(2 * bank_count)" in held_source
    )
    period_log_terminal = any(
        line.startswith("FINAL ")
        and json.loads(line[len("FINAL "):]).get("terminal")
        == "CYCLE818_PERIOD_STRUCTURE_CENSUS_PASS"
        for line in payloads[PERIOD_LOG_PATH].decode().splitlines()
    )
    cohort_terminal = "CYCLE832_V2_36_KEY_BACKBONE_EXACT_PASS"
    cohort_log_terminal = (
        cohort_summary["terminal"] == cohort_terminal
        and any(
            line == cohort_terminal
            for line in payloads[COHORT_LOG_PATH].decode().splitlines()
        )
    )

    exact = (
        catalog_definition_AST_exact
        and len(catalog_pairs) == 44
        and len(catalog) == 176
        and len(open_keys) == 133
        and open_keys <= catalog
        and len(resolved_from_complement) == 43
        and len(transient_cohort_keys) == 27
        and len(strict_cycle_keys) == 12
        and len(earlier_transient_keys) == 4
        and earlier_transient_keys
        == literal_earlier - transient_cohort_keys - strict_cycle_keys
        and resolved_from_lists == resolved_from_complement
        and not (
            earlier_transient_keys & transient_cohort_keys
            or earlier_transient_keys & strict_cycle_keys
            or transient_cohort_keys & strict_cycle_keys
        )
        and len(backbone_pairs) == 9
        and len(period_rows_all) == 14
        and all(
            row["pass"]
            and row["minimal_period"]
            and row["full_state_recurrence"]
            for row in strict_k2_rows
        )
        and backbone_certificate["classification_census"]
        == {
            "CERTIFIED_PERIOD_3_CYCLE": 9,
            "TRANSIENT_COHORT": 27,
        }
        and period_log_terminal
        and cohort_log_terminal
    )
    return {
        "catalog_pairs": catalog_pairs,
        "catalog": catalog,
        "open_keys": open_keys,
        "resolved_keys": resolved_from_lists,
        "earlier_transient_keys": earlier_transient_keys,
        "transient_cohort_keys": transient_cohort_keys,
        "strict_cycle_keys": strict_cycle_keys,
        "backbone_pairs": backbone_pairs,
        "moment_certificate": moment_certificate,
        "public": {
            "catalog_definition":
                "all unordered C11 station pairs with cyclic distance > 1; "
                "four event labels 0,1,2,3 per admitted pair",
            "catalog_definition_AST_exact":
                catalog_definition_AST_exact,
            "landed_pair_count": len(catalog_pairs),
            "landed_key_count": len(catalog),
            "open_key_count": len(open_keys),
            "resolved_key_count": len(resolved_from_lists),
            "resolution_partition": {
                "EARLIER_TRANSIENT": len(earlier_transient_keys),
                "TRANSIENT_COHORT": len(transient_cohort_keys),
                "STRICT_CYCLE": len(strict_cycle_keys),
            },
            "earlier_transient_keys":
                tuple(sorted(earlier_transient_keys)),
            "strict_cycle_period_census": dict(sorted(Counter(
                int(row["period"]) for row in strict_k2_rows
            ).items())),
            "period_log_rows_all_k": len(period_rows_all),
            "period_log_rows_k2": len(strict_k2_rows),
            "period_log_terminal_exact": period_log_terminal,
            "cohort_log_terminal_exact": cohort_log_terminal,
            "resolved_lists_equal_catalog_minus_open":
                resolved_from_lists == resolved_from_complement,
            "pass": exact,
        },
        "pass": exact,
    }


def table_certificate(evidence: dict[str, object]) -> dict[str, object]:
    catalog = evidence["catalog"]
    resolved_keys = evidence["resolved_keys"]
    open_keys = evidence["open_keys"]
    earlier = evidence["earlier_transient_keys"]
    cohorts = evidence["transient_cohort_keys"]
    cycles = evidence["strict_cycle_keys"]
    assert all(isinstance(rows, frozenset) for rows in (
        catalog, resolved_keys, open_keys, earlier, cohorts, cycles
    ))

    rows = []
    for separation in range(1, 6):
        geometry = geometric_pairs(separation)
        landed = tuple(
            (event, pair)
            for pair in geometry
            for event in EVENTS
            if (event, pair) in catalog
        )
        resolved = tuple(key for key in landed if key in resolved_keys)
        opened = tuple(key for key in landed if key in open_keys)
        complete = tuple(
            pair for pair in geometry
            if all((event, pair) in resolved_keys for event in EVENTS)
        )
        rows.append({
            "separation": separation,
            "geometric_pair_count": len(geometry),
            "geometric_candidate_key_count": len(geometry) * len(EVENTS),
            "landed_key_count": len(landed),
            "resolved_key_count": len(resolved),
            "open_key_count": len(opened),
            "complete_fiber_count": len(complete),
            "complete_fibers": complete,
            "resolved_classification": {
                "EARLIER_TRANSIENT": sum(key in earlier for key in landed),
                "TRANSIENT_COHORT": sum(key in cohorts for key in landed),
                "STRICT_CYCLE": sum(key in cycles for key in landed),
            },
        })
    expected = (
        (1, 0, 0, 0, 0),
        (2, 44, 4, 40, 0),
        (3, 44, 0, 44, 0),
        (4, 44, 1, 43, 0),
        (5, 44, 38, 6, 9),
    )
    observed = tuple(
        (
            row["separation"],
            row["landed_key_count"],
            row["resolved_key_count"],
            row["open_key_count"],
            row["complete_fiber_count"],
        )
        for row in rows
    )
    expected_classes = {
        1: {"EARLIER_TRANSIENT": 0, "TRANSIENT_COHORT": 0,
            "STRICT_CYCLE": 0},
        2: {"EARLIER_TRANSIENT": 3, "TRANSIENT_COHORT": 0,
            "STRICT_CYCLE": 1},
        3: {"EARLIER_TRANSIENT": 0, "TRANSIENT_COHORT": 0,
            "STRICT_CYCLE": 0},
        4: {"EARLIER_TRANSIENT": 1, "TRANSIENT_COHORT": 0,
            "STRICT_CYCLE": 0},
        5: {"EARLIER_TRANSIENT": 0, "TRANSIENT_COHORT": 27,
            "STRICT_CYCLE": 11},
    }
    exact = (
        evidence["pass"]
        and observed == expected
        and all(
            row["geometric_pair_count"] == 11
            and row["geometric_candidate_key_count"] == 44
            and row["resolved_classification"]
            == expected_classes[row["separation"]]
            for row in rows
        )
        and sum(row["resolved_key_count"] for row in rows) == 43
        and sum(row["open_key_count"] for row in rows) == 133
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "finding": (
            "THE TABLE: PASS — independently enumerated cells are "
            "s=1 (0 landed), s=2 (44 landed, 4 resolved, 40 open), "
            "s=3 (44, 0, 44), s=4 (44, 1, 43), and "
            "s=5 (44, 38, 6, 9 complete fibers)."
            if exact else
            "THE TABLE: FAIL — the independent census differs from the "
            "claimed status-by-separation table."
        ),
        "s1_zero_explanation": (
            "The landed catalog admits an unordered pair only when its "
            "cyclic distance is >1.  Every s=1 pair is adjacent, so the "
            "11 geometric pairs and their 44 candidate event keys are "
            "outside the catalog; zero keys land."
        ),
        "rows": tuple(rows),
        "resolution_partition_source": evidence["public"],
        "pass": exact,
    }


def biconditional_certificate(
    evidence: dict[str, object],
    table: dict[str, object],
) -> dict[str, object]:
    resolved = evidence["resolved_keys"]
    backbone = evidence["backbone_pairs"]
    pairs = evidence["catalog_pairs"]
    assert isinstance(resolved, frozenset)
    assert isinstance(backbone, frozenset)
    assert isinstance(pairs, tuple)
    complete = frozenset(
        pair for pair in pairs
        if all((event, pair) in resolved for event in EVENTS)
    )
    predicate = frozenset(
        pair for pair in pairs
        if cyclic_distance(pair) == 5 and 0 not in pair
    )
    forward_counterexamples = tuple(sorted(complete - predicate))
    reverse_counterexamples = tuple(sorted(predicate - complete))
    exact = (
        table["pass"]
        and len(pairs) == 44
        and len(resolved) + len(evidence["open_keys"]) == 176
        and len(complete) == len(predicate) == len(backbone) == 9
        and complete == predicate == backbone
        and not forward_counterexamples
        and not reverse_counterexamples
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "finding": (
            "THE BICONDITIONAL: PASS — over all 44 landed pair fibers "
            "(176 keys), a fiber is complete iff s=5 and station 0 is "
            "absent; both directions have zero counterexamples."
            if exact else
            "THE BICONDITIONAL: FAIL — at least one implication has a "
            "landed counterexample."
        ),
        "landed_pairs_checked": len(pairs),
        "landed_keys_checked": len(pairs) * len(EVENTS),
        "complete_implies_s5_origin_absent": {
            "antecedent_count": len(complete),
            "counterexamples": forward_counterexamples,
            "pass": not forward_counterexamples,
        },
        "s5_origin_absent_implies_complete": {
            "antecedent_count": len(predicate),
            "counterexamples": reverse_counterexamples,
            "pass": not reverse_counterexamples,
        },
        "complete_fibers": tuple(sorted(complete)),
        "predicate_fibers": tuple(sorted(predicate)),
        "matches_landed_backbone": complete == backbone,
        "pass": exact,
    }


def expand_one_step(stations: frozenset[int]) -> frozenset[int]:
    return frozenset(
        point
        for station in stations
        for point in (
            station,
            (station - 1) % RING_STATIONS,
            (station + 1) % RING_STATIONS,
        )
    )


def first_propagation_overlap(
    pair: Pair,
) -> tuple[int, tuple[int, ...]]:
    left = frozenset((pair[0],))
    right = frozenset((pair[1],))
    for tick in range(RING_STATIONS + 1):
        overlap = left & right
        if overlap:
            return tick, tuple(sorted(overlap))
        left = expand_one_step(left)
        right = expand_one_step(right)
    raise AssertionError(("no propagation overlap", pair))


def first_path_overlap(
    path: tuple[int, ...],
) -> tuple[int, tuple[int, ...]]:
    for tick in range(len(path) + 1):
        left = frozenset(path[:tick + 1])
        right = frozenset(path[-tick - 1:])
        overlap = left & right
        if overlap:
            return tick, tuple(
                station for station in path if station in overlap
            )
    raise AssertionError(("no path overlap", path))


def translated_pair(pair: Pair, tick: int) -> Pair:
    return tuple(sorted((
        (pair[0] + tick) % RING_STATIONS,
        (pair[1] + tick) % RING_STATIONS,
    )))


def tie_certificate(
    evidence: dict[str, object],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    rows = []
    for separation in range(1, 6):
        short_path = tuple(range(separation + 1))
        long_path = tuple(
            (-offset) % RING_STATIONS
            for offset in range(RING_STATIONS - separation + 1)
        )
        short_tick, short_overlap = first_path_overlap(short_path)
        long_tick, long_overlap = first_path_overlap(long_path)
        pair_rows = tuple(
            (tick, len(overlap))
            for tick, overlap in (
                first_propagation_overlap(pair)
                for pair in geometric_pairs(separation)
            )
        )
        representative_tick, representative_overlap = (
            first_propagation_overlap((0, separation))
        )
        formula_ticks = (
            (separation + 1) // 2,
            (RING_STATIONS - separation + 1) // 2,
        )
        rows.append({
            "separation": separation,
            "arc_lengths": (
                separation, RING_STATIONS - separation
            ),
            "arc_meeting_ticks": (short_tick, long_tick),
            "ceil_length_over_2_formula_ticks": formula_ticks,
            "arc_meeting_station_counts": (
                len(short_overlap), len(long_overlap)
            ),
            "representative_arc_meeting_stations": (
                short_overlap, long_overlap
            ),
            "simultaneous_arc_meeting":
                short_tick == long_tick,
            "global_first_overlap_tick": representative_tick,
            "global_first_overlap_stations":
                representative_overlap,
            "global_first_overlap_station_count":
                len(representative_overlap),
            "rotation_uniform_global_meeting":
                len(set(pair_rows)) == 1,
        })
    ties = tuple(
        row["separation"]
        for row in rows if row["simultaneous_arc_meeting"]
    )

    controller_source = ast.unparse(
        function_node(trees[CORE_PATH], "apply_controller_step")
    )
    synchronous_source = ast.unparse(
        function_node(trees[BASIN_PATH], "synchronous_word")
    )
    landed_translation_AST_exact = (
        "target = (station + 1) % stations" in controller_source
        and "b[station], a[target] = (a[target], b[station])"
        in controller_source
        and (
            "positions = tuple(((position + 1) % len(program) "
            "for position in positions))"
        ) in synchronous_source
    )
    literal_rows = []
    for separation in range(1, 6):
        pairs = geometric_pairs(separation)
        collision_count = 0
        separation_failures = 0
        period_failures = 0
        for pair in pairs:
            orbit = tuple(
                translated_pair(pair, tick)
                for tick in range(RING_STATIONS + 1)
            )
            collision_count += sum(
                state[0] == state[1] for state in orbit
            )
            separation_failures += sum(
                cyclic_distance(state) != separation for state in orbit
            )
            period_failures += orbit[-1] != pair
        literal_rows.append({
            "separation": separation,
            "pairs_checked": len(pairs),
            "states_checked":
                len(pairs) * (RING_STATIONS + 1),
            "collision_count": collision_count,
            "separation_failures": separation_failures,
            "period_failures": period_failures,
        })
    literal_sources_never_collide = (
        landed_translation_AST_exact
        and all(
            not row["collision_count"]
            and not row["separation_failures"]
            and not row["period_failures"]
            for row in literal_rows
        )
    )

    s5 = next(row for row in rows if row["separation"] == 5)
    exact = (
        evidence["pass"]
        and tuple(row["arc_lengths"] for row in rows)
        == ((1, 10), (2, 9), (3, 8), (4, 7), (5, 6))
        and tuple(row["arc_meeting_ticks"] for row in rows)
        == ((1, 5), (1, 5), (2, 4), (2, 4), (3, 3))
        and all(
            row["arc_meeting_ticks"]
            == row["ceil_length_over_2_formula_ticks"]
            and row["rotation_uniform_global_meeting"]
            for row in rows
        )
        and ties == (5,)
        and s5["arc_meeting_station_counts"] == (2, 1)
        and s5["global_first_overlap_station_count"] == 3
        and literal_sources_never_collide
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "finding": (
            "THE (3,3) TIE: PASS — the arc-length/tick table is "
            "(1,10)->(1,5), (2,9)->(1,5), (3,8)->(2,4), "
            "(4,7)->(2,4), (5,6)->(3,3); only s=5 ties, with "
            "two meeting stations on the length-5 arc and one on the "
            "length-6 arc."
            if exact else
            "THE (3,3) TIE: FAIL — independent radius-one propagation "
            "does not reproduce the claimed unique tie."
        ),
        "derivation": (
            "On a path of L edges, endpoint radius-one fronts first "
            "overlap at the least integer t with 2t>=L, namely ceil(L/2). "
            "Odd L contributes two central stations and even L one.  "
            "The two complementary C11 paths have lengths s and 11-s."
        ),
        "per_separation_meeting_table": tuple(rows),
        "simultaneous_separations": ties,
        "literal_controller": {
            "AST_common_translation_exact":
                landed_translation_AST_exact,
            "rows": tuple(literal_rows),
            "literal_sources_never_collide":
                literal_sources_never_collide,
            "finding": (
                "LITERAL SOURCES NEVER COLLIDE: PASS — the landed update "
                "common-translates both distinct positions by +1 mod 11, "
                "so cyclic separation is invariant."
                if literal_sources_never_collide else
                "LITERAL SOURCES NEVER COLLIDE: FAIL — a collision or "
                "source-rule mismatch was found."
            ),
        },
        "auxiliary_model_boundary": (
            "The radius-one expanding fronts are an auxiliary undirected "
            "C11 propagation model; the literal landed controller performs "
            "common translation and has no source collision."
        ),
        "pass": exact,
    }


def bank_geometry_certificate(
    evidence: dict[str, object],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    anatomy = function_node(trees[BASIN_PATH], "anatomy")
    source = ast.unparse(anatomy)
    names = {
        node.id for node in ast.walk(anatomy)
        if isinstance(node, ast.Name)
    }
    anatomy_AST_exact = (
        "banks, links = K.M.unpack_state(state, FIXTURE_BANKS)" in source
        and "for bank in banks" in source
        and "for cell in K.A.CELLS" in source
        and "occupancy == ((1, 1), (0, 0))" in source
        and "positions" not in names
        and "pair" not in names
    )
    moment_certificate = evidence["moment_certificate"]
    event0 = next(
        row
        for row in moment_certificate[
            "residual_census_v1_reproduced"
        ]["funnel_anatomies"]["rows"]
        if int(row["event"]) == 0
    )
    exact = (
        anatomy_AST_exact
        and int(event0["full_state_hamming_weight"]) == 44
        and event0["landed_support_component_counts"]
        == {"bank0": 1, "source": 1}
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "finding": (
            "[1,1] IS BANK GEOMETRY: PASS — Cycle-822 defines occupancy "
            "from each unpacked bank's two K.A.CELLS valid bits; the "
            "anatomy function has no ring-pair/position coordinate."
            if exact else
            "[1,1] IS BANK GEOMETRY: FAIL — the anatomy AST or landed "
            "event-0 record does not support the claimed reading."
        ),
        "anatomy_AST_exact": anatomy_AST_exact,
        "occupancy_reading": (
            "((1,1),(0,0)) means the two cell-valid bits of bank 0 are "
            "occupied and those of bank 1 are not; it is not a station pair."
        ),
        "event0_funnel_hamming_weight": event0[
            "full_state_hamming_weight"
        ],
        "event0_landed_support_component_counts":
            event0["landed_support_component_counts"],
        "pass": exact,
    }


def s4_control_certificate(
    evidence: dict[str, object],
    biconditional: dict[str, object],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    representative = (1, 5)
    selector = frozenset(biconditional["predicate_fibers"])
    orbit = tuple(
        translated_pair(representative, tick)
        for tick in range(RING_STATIONS)
    )
    representative_hits = tuple(
        tick for tick, pair in enumerate(orbit)
        if pair in selector
    )
    all_s4_hits = tuple(
        (pair, tick, translated_pair(pair, tick))
        for pair in geometric_pairs(4)
        for tick in range(RING_STATIONS)
        if translated_pair(pair, tick) in selector
    )
    primary_probe_source = ast.unparse(
        function_node(
            trees[PRIMARY_PATH], "dynamics_probe_certificate"
        )
    )
    catalog = evidence["catalog"]
    open_keys = evidence["open_keys"]
    fairness = {
        "primary_representative_exact":
            "s4_pair = (1, 5)" in primary_probe_source,
        "representative_is_landed_event0_key":
            (0, representative) in catalog,
        "representative_event0_key_is_open":
            (0, representative) in open_keys,
        "pairwise_separated_lawful":
            cyclic_distance(representative) > 1,
        "two_source_count": len(set(representative)),
        "origin_absent_initially": 0 not in representative,
        "same_landed_common_translation":
            all(
                orbit[tick]
                == translated_pair(representative, tick)
                for tick in range(RING_STATIONS)
            ),
        "full_translation_period_checked":
            translated_pair(representative, RING_STATIONS)
            == representative,
        "selector_is_data_verified_biconditional":
            biconditional["pass"]
            and selector
            == frozenset(biconditional["complete_fibers"]),
        "all_11_s4_pairs_checked":
            len(geometric_pairs(4)) == 11,
        "scope_is_position_projection_only": True,
        "full_internal_state_unreachability_claimed": False,
    }
    exact = (
        all(
            value is True
            for key, value in fairness.items()
            if key not in {
                "two_source_count",
                "full_internal_state_unreachability_claimed",
            }
        )
        and fairness["two_source_count"] == 2
        and not fairness["full_internal_state_unreachability_claimed"]
        and all(cyclic_distance(pair) == 4 for pair in orbit)
        and not representative_hits
        and not all_s4_hits
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "finding": (
            "THE s=4 CONTROL: PASS — the lawful event-0 key (1,5) and, "
            "more strongly, all 11 s=4 position orbits preserve s=4 for "
            "their full 11-tick period and never reach the verified "
            "s=5-origin-absent selector."
            if exact else
            "THE s=4 CONTROL: FAIL — the control is unlawful, unfair, or "
            "reaches the selector."
        ),
        "representative": {
            "event": 0,
            "pair": representative,
            "orbit_t0_through_t10": orbit,
            "selector_hit_times": representative_hits,
        },
        "all_s4_selector_hits": all_s4_hits,
        "fairness_audit": fairness,
        "strawman_audit": (
            "NOT A STRAWMAN within its stated positional scope: it uses a "
            "real landed/open two-source key, the exact landed translation "
            "rule, a full period, and the selector independently recovered "
            "from complete fibers.  It does not construct a 5815-bit "
            "trajectory and therefore does not claim full-state "
            "unreachability."
        ),
        "full_internal_state_reachability": "OPEN",
        "pass": exact,
    }


def science_certificates(
    payloads: dict[str, bytes],
    trees: dict[str, ast.Module],
) -> dict[str, dict[str, object]]:
    evidence = landed_evidence(payloads, trees)
    table = table_certificate(evidence)
    biconditional = biconditional_certificate(evidence, table)
    tie = tie_certificate(evidence, trees)
    bank = bank_geometry_certificate(evidence, trees)
    s4 = s4_control_certificate(
        evidence, biconditional, trees
    )
    return {
        "THE_TABLE": table,
        "THE_BICONDITIONAL": biconditional,
        "THE_3_3_TIE": tie,
        "BANK_GEOMETRY": bank,
        "THE_S4_CONTROL": s4,
    }


def render(
    certificates: dict[str, dict[str, object]],
    controls: dict[str, object],
    report: dict[str, object],
) -> str:
    lines = []
    for name, certificate in certificates.items():
        lines.append(
            f"CERTIFICATE {name} {certificate['verdict']} "
            + compact(certificate)
        )
        lines.append(f"FINDING {name} {certificate['finding']}")
    lines.extend((
        "CERTIFICATE CONTROLS "
        + ("PASS " if controls["pass"] else "FAIL ")
        + compact(controls),
        "FINDING CONTROLS " + str(controls["finding"]),
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    ))
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: dict[str, dict[str, object]],
    controls: dict[str, object],
    report: dict[str, object],
    controls_base: bool,
) -> str:
    for _attempt in range(20):
        controls["pass"] = (
            controls_base
            and int(controls["stdout_bytes"]) < STDOUT_LIMIT_BYTES
        )
        report["checks"] = {
            **{
                name: bool(certificate["pass"])
                for name, certificate in certificates.items()
            },
            "CONTROLS": bool(controls["pass"]),
        }
        report["pass"] = all(report["checks"].values())
        report["primary_disposition"] = (
            "NOT_REFUTED_WITHIN_DECLARED_BOUNDS"
            if report["pass"] else "REFUTED_OR_CHECK_FAILED"
        )
        report["terminal"] = (
            "CYCLE837_SEP5_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
            if report["pass"]
            else "CYCLE837_SEP5_INDEPENDENT_ADVERSARIAL_CHECK_FAIL"
        )
        output = render(certificates, controls, report)
        size = len(output.encode())
        if (
            int(controls["stdout_bytes"]) == size
            and int(report["stdout_bytes"]) == size
        ):
            return output
        controls["stdout_bytes"] = size
        report["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    payloads, trees, controls = source_packet()
    first = science_certificates(payloads, trees)
    replay = science_certificates(payloads, trees)
    first_digest = digest(first)
    replay_digest = digest(replay)
    deterministic = first == replay and first_digest == replay_digest
    elapsed = monotonic() - started

    controls.update({
        "blocked_primary_loaded_at_end": PRIMARY_MODULE in sys.modules,
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "determinism": {
            "first_certificate_sha256": first_digest,
            "replay_certificate_sha256": replay_digest,
            "certificates_exactly_equal": deterministic,
        },
        "exact_arithmetic": (
            "All catalogs, separations, resolution partitions, propagation "
            "sets, arc ticks, selector tests, SHA-256 values, and equality "
            "checks use exact integers/bytes/sets; only monotonic runtime "
            "is a float."
        ),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "finding": (
            "CONTROLS: PASS — six literal existing worktree-relative "
            "inputs are SHA/blob pinned; the Cycle-837 primary remained "
            "BLOCKLISTED text/AST-only; replay was deterministic; runtime "
            "and stdout stayed within bounds."
        ),
        "pass": False,
    })
    controls_base = (
        bool(controls["source_pass"])
        and deterministic
        and all(certificate["pass"] for certificate in first.values())
        and not controls["blocked_primary_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    if not controls_base:
        controls["finding"] = (
            "CONTROLS: FAIL — a source, blocklist, determinism, scientific, "
            "or runtime control failed."
        )

    report = {
        "cycle": 837,
        "target":
            "independent adversarial check of the biconditional and (3,3) tie",
        "causal_derivation_status": "OPEN",
        "causal_boundary": (
            "The exact catalog biconditional, auxiliary C11 tie, literal "
            "noncollision, bank-geometry reading, and positional s=4 "
            "control do not derive a full internal-state causal selector."
        ),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "primary_disposition": "REFUTED_OR_CHECK_FAILED",
        "terminal": "CYCLE837_SEP5_INDEPENDENT_ADVERSARIAL_CHECK_FAIL",
    }
    output = stable_render(first, controls, report, controls_base)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal":
                "CYCLE837_SEP5_INDEPENDENT_ADVERSARIAL_CHECK_FAIL",
        }) + "\n")
        return 1
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
            "terminal":
                "CYCLE837_SEP5_INDEPENDENT_ADVERSARIAL_CHECK_FAIL",
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
