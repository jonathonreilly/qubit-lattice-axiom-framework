#!/usr/bin/env python3
"""Cycle 837: why separation five?  Exact bounded derivation probe.

This stdlib-only runner reads every landed Python primary as SHA-pinned
text/AST only.  It separates three facts which must not be conflated:
landed key status, literal common-translation controller dynamics, and the
auxiliary undirected radius-one wavefront model on C11.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
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
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
PYTHON_PRIMARY_PATHS = AUDIT_INPUT_PATHS[:4]
TEXT_LOG_PATHS = AUDIT_INPUT_PATHS[4:]
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in PYTHON_PRIMARY_PATHS
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "c2fd23a7bb47caff70e9561fc9da46feef422c053954fa1af925901a1884ed0b",
    AUDIT_INPUT_PATHS[3]:
        "0db01e80084af4dbb52c74a0a055984edf8ab818f2c8ba8a99c1f6a3fc15bb3e",
    AUDIT_INPUT_PATHS[4]:
        "94bc32640518f097cb09060f9c378d26d73e263539573e3b8e75ed2aab1b857e",
    AUDIT_INPUT_PATHS[5]:
        "89640947e097728e73cbd58a0039364e684dc2e81d840a087fdddd69598bd450",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "8ddd84104dc0729107cebfb0d0cd694fe78af1af",
    AUDIT_INPUT_PATHS[2]: "6d48f5d86006a5f6718b5993eaecd5ec69d86112",
    AUDIT_INPUT_PATHS[3]: "d666f5c301ffe6b6508f3636b15814a662bfbe8e",
    AUDIT_INPUT_PATHS[4]: "3544e3beada65b3480d352e2701f6e21b3f9ae2d",
    AUDIT_INPUT_PATHS[5]: "86d14cac924d71a6d4702ffac3dbeacc5c5d0f52",
}
EXPECTED_BASE = "f3ec9213b4b02457bfc8bc092bf25510297e2813"
EXPECTED_BRANCH = "physics-loop/proof-grade-blockR20-20260729"
RING_STATIONS = 11
EVENTS = (0, 1, 2, 3)

Pair = tuple[int, int]
Key = tuple[int, Pair]


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
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


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def git_value(*arguments: str) -> str:
    completed = subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return completed.stdout.strip()


def source_controls() -> tuple[
    dict[str, object],
    dict[str, bytes],
    dict[str, ast.Module],
]:
    payloads = {
        path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS
    }
    trees = {
        path: ast.parse(payloads[path], filename=path)
        for path in PYTHON_PRIMARY_PATHS
    }
    self_tree = ast.parse(
        Path(__file__).read_bytes(), filename=Path(__file__).name
    )
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
        "json", "pathlib", "subprocess", "sys", "time",
    )
    sha_rows = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    blob_rows = {
        path: git_blob(payload) for path, payload in payloads.items()
    }
    branch = git_value("branch", "--show-current")
    head = git_value("rev-parse", "HEAD")
    base = git_value(
        "merge-base",
        "HEAD",
        "physics-loop/proof-grade-blockR19-20260729",
    )
    rows = tuple({
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
            if path in PYTHON_PRIMARY_PATHS
            else "TEXT_JSON_LINES_ONLY"
        ),
    } for path in AUDIT_INPUT_PATHS)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "named_input_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "all_paths_existing_worktree_relative": all(
            row["exists"] and row["worktree_relative"] for row in rows
        ),
        "source_rows": rows,
        "python_primaries": PYTHON_PRIMARY_PATHS,
        "python_primary_access": "TEXT_AST_ONLY_BLOCKLISTED",
        "direct_imports": direct_imports,
        "expected_stdlib_imports": expected_stdlib_imports,
        "stdlib_only": direct_imports == expected_stdlib_imports,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "git_head": head,
        "git_base": base,
        "expected_git_base": EXPECTED_BASE,
        "git_base_exact": base == EXPECTED_BASE,
        "git_branch": branch,
        "expected_git_branch": EXPECTED_BRANCH,
        "git_branch_exact": branch == EXPECTED_BRANCH,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["named_input_count"] <= result["read_cap"]
        and result["all_paths_existing_worktree_relative"]
        and all(
            row["sha256_exact"] and row["git_blob_exact"] for row in rows
        )
        and result["stdlib_only"]
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and result["git_base_exact"]
        and result["git_branch_exact"]
    )
    return result, payloads, trees


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = tuple(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )
    if len(matches) != 1:
        raise AssertionError((name, len(matches)))
    return matches[0]


def json_line(
    payload: bytes,
    prefix: str,
) -> dict[str, object]:
    matches = tuple(
        json.loads(line[len(prefix):])
        for line in payload.decode().splitlines()
        if line.startswith(prefix)
    )
    if len(matches) != 1:
        raise AssertionError((prefix, len(matches)))
    return matches[0]


def period_rows(payload: bytes) -> tuple[dict[str, object], ...]:
    prefix = "PERIOD_TABLE_ROW "
    return tuple(
        json.loads(line[len(prefix):])
        for line in payload.decode().splitlines()
        if line.startswith(prefix)
    )


def cyclic_separation(pair: Pair) -> int:
    left, right = pair
    return min(
        (right - left) % RING_STATIONS,
        (left - right) % RING_STATIONS,
    )


def pairs_at_separation(separation: int) -> tuple[Pair, ...]:
    return tuple(
        pair for pair in combinations(range(RING_STATIONS), 2)
        if cyclic_separation(pair) == separation
    )


def freeze_key(value: object) -> Key:
    event, pair = value
    return int(event), (int(pair[0]), int(pair[1]))


def landed_records(
    payloads: dict[str, bytes],
) -> dict[str, object]:
    cycle832 = payloads[AUDIT_INPUT_PATHS[5]]
    preregistration = json_line(
        cycle832, "V1_HISTORICAL_PRE_REGISTRATION_RETRACTED "
    )
    certificate_a = json_line(
        cycle832, "CERTIFICATE A_36_KEY_BACKBONE "
    )
    certificate_c = json_line(
        cycle832, "CERTIFICATE C_MOMENT_PREDICTION_RERULING "
    )
    summary = json_line(cycle832, "SUMMARY_JSON ")
    strict_rows = period_rows(payloads[AUDIT_INPUT_PATHS[4]])
    return {
        "preregistration": preregistration,
        "cycle832_certificate_a": certificate_a,
        "cycle832_certificate_c": certificate_c,
        "cycle832_summary": summary,
        "cycle818_period_rows": strict_rows,
    }


def separation_census_certificate(
    records: dict[str, object],
) -> dict[str, object]:
    preregistration = records["preregistration"]
    cycle832 = records["cycle832_certificate_a"]
    strict_rows = records["cycle818_period_rows"]
    assert isinstance(preregistration, dict)
    assert isinstance(cycle832, dict)
    assert isinstance(strict_rows, tuple)

    open_keys: set[Key] = {
        (int(event), (int(pair[0]), int(pair[1])))
        for pair, event in preregistration["open_pair_event_keys"]
    }
    lawful_pairs = tuple(
        pair
        for separation in range(2, 6)
        for pair in pairs_at_separation(separation)
    )
    lawful_keys = {
        (event, pair) for pair in lawful_pairs for event in EVENTS
    }
    resolved_keys = lawful_keys - open_keys
    backbone_pairs = {
        (int(pair[0]), int(pair[1]))
        for pair in cycle832["backbone_pairs"]
    }
    backbone_keys = {
        freeze_key(key) for key in cycle832["backbone_keys"]
    }
    transient_rows = tuple(
        row for row in cycle832["classification_rows"]
        if row["classification"] == "TRANSIENT_COHORT"
    )
    transient_moments = {
        freeze_key(row["key"]): int(row["resolution_moment"])
        for row in transient_rows
    }
    periodic = {
        (int(row["event"]),
         (int(row["positions"][0]), int(row["positions"][1]))):
            int(row["period"])
        for row in strict_rows
        if int(row["k"]) == 2
    }

    def status(key: Key) -> str:
        if key in open_keys:
            return "OPEN_OFF_BACKBONE"
        if key in transient_moments:
            return (
                "RESOLVED_TRANSIENT_COHORT_AT_"
                f"{transient_moments[key]}"
            )
        if key in periodic:
            return f"RESOLVED_MINIMAL_PERIOD_{periodic[key]}"
        if key in resolved_keys:
            return "EARLIER_RESOLVED_NONCATALOG"
        raise AssertionError(("unclassified lawful key", key))

    rows = []
    all_status_rows = []
    for separation in range(1, 6):
        pairs = pairs_at_separation(separation)
        candidate_keys = tuple(
            (event, pair) for pair in pairs for event in EVENTS
        )
        if separation == 1:
            status_rows = tuple({
                "key": key,
                "status": "OUTSIDE_PAIRWISE_SEPARATED_K2_FAMILY",
            } for key in candidate_keys)
            resolved = ()
            opened = ()
            complete = ()
            landed_key_count = 0
        else:
            status_rows = tuple({
                "key": key,
                "status": status(key),
            } for key in candidate_keys)
            resolved = tuple(
                key for key in candidate_keys if key in resolved_keys
            )
            opened = tuple(
                key for key in candidate_keys if key in open_keys
            )
            complete = tuple(
                pair for pair in pairs
                if all((event, pair) in resolved_keys for event in EVENTS)
            )
            landed_key_count = len(candidate_keys)
        all_status_rows.extend(status_rows)
        rows.append({
            "separation": separation,
            "pair_count": len(pairs),
            "pairs": pairs,
            "event_label_count": len(EVENTS),
            "candidate_key_count": len(candidate_keys),
            "candidate_keys": candidate_keys,
            "landed_key_count": landed_key_count,
            "resolved_key_count": len(resolved),
            "open_key_count": len(opened),
            "complete_four_event_pair_fiber_count": len(complete),
            "complete_four_event_pair_fibers": complete,
            "backbone_pair_count": len(set(pairs) & backbone_pairs),
            "status_census": dict(sorted(Counter(
                row["status"] for row in status_rows
            ).items())),
            "landed_status_rows": (
                status_rows if separation > 1 else ()
            ),
            "outside_family_status_rows": (
                status_rows if separation == 1 else ()
            ),
        })
    row_by_separation = {
        int(row["separation"]): row for row in rows
    }
    complete_fiber_separations = tuple(
        separation for separation, row in row_by_separation.items()
        if row["complete_four_event_pair_fiber_count"]
    )
    any_resolved_separations = tuple(
        separation for separation, row in row_by_separation.items()
        if row["resolved_key_count"]
    )
    expected_resolved_open = {
        1: (0, 0),
        2: (4, 40),
        3: (0, 44),
        4: (1, 43),
        5: (38, 6),
    }
    expected_complete = {1: 0, 2: 0, 3: 0, 4: 0, 5: 9}
    exact = (
        all(row["pair_count"] == 11 for row in rows)
        and all(row["candidate_key_count"] == 44 for row in rows)
        and row_by_separation[1]["landed_key_count"] == 0
        and all(
            row_by_separation[separation]["landed_key_count"] == 44
            for separation in range(2, 6)
        )
        and all(
            (
                row_by_separation[separation]["resolved_key_count"],
                row_by_separation[separation]["open_key_count"],
            ) == expected_resolved_open[separation]
            for separation in range(1, 6)
        )
        and all(
            row_by_separation[separation][
                "complete_four_event_pair_fiber_count"
            ] == expected_complete[separation]
            for separation in range(1, 6)
        )
        and len(lawful_pairs) == 44
        and len(lawful_keys) == 176
        and len(resolved_keys) == 43
        and len(open_keys) == 133
        and len(backbone_pairs) == 9
        and len(backbone_keys) == 36
        and backbone_keys <= resolved_keys
        and complete_fiber_separations == (5,)
        and any_resolved_separations == (2, 4, 5)
        and records["cycle832_summary"]["terminal"]
        == "CYCLE832_V2_36_KEY_BACKBONE_EXACT_PASS"
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "status_by_separation": tuple(rows),
        "landed_lawful_pair_count": len(lawful_pairs),
        "landed_lawful_key_count": len(lawful_keys),
        "landed_resolved_key_count": len(resolved_keys),
        "landed_open_key_count": len(open_keys),
        "backbone_pair_count": len(backbone_pairs),
        "backbone_key_count": len(backbone_keys),
        "all_backbone_keys_resolved": backbone_keys <= resolved_keys,
        "any_resolved_key_separations": any_resolved_separations,
        "complete_pair_fiber_separations": complete_fiber_separations,
        "only_s5_has_any_resolved_key":
            any_resolved_separations == (5,),
        "only_s5_has_complete_four_event_pair_fibers":
            complete_fiber_separations == (5,),
        "claim_reruling": (
            "'only s=5 resolves' FAILS for individual keys (s=2 and s=4 "
            "also contain resolved keys), but HOLDS EXACTLY for complete "
            "four-event pair fibers: exactly nine, all at s=5."
        ),
        "pass": exact,
    }


def ring_ball(center: int, radius: int) -> frozenset[int]:
    return frozenset(
        station for station in range(RING_STATIONS)
        if min(
            (station - center) % RING_STATIONS,
            (center - station) % RING_STATIONS,
        ) <= radius
    )


def first_ball_meeting(pair: Pair) -> tuple[int, tuple[int, ...]]:
    for tick in range(RING_STATIONS + 1):
        overlap = ring_ball(pair[0], tick) & ring_ball(pair[1], tick)
        if overlap:
            return tick, tuple(sorted(overlap))
    raise AssertionError(("balls never meet", pair))


def translated_pair(pair: Pair, tick: int) -> Pair:
    return (
        (pair[0] + tick) % RING_STATIONS,
        (pair[1] + tick) % RING_STATIONS,
    )


def dynamics_probe_certificate(
    records: dict[str, object],
    trees: dict[str, ast.Module],
) -> dict[str, object]:
    cycle832_a = records["cycle832_certificate_a"]
    cycle832_c = records["cycle832_certificate_c"]
    assert isinstance(cycle832_a, dict)
    assert isinstance(cycle832_c, dict)
    backbone_pairs = {
        (int(pair[0]), int(pair[1]))
        for pair in cycle832_a["backbone_pairs"]
    }
    maximum = RING_STATIONS // 2
    geometric_rows = tuple({
        "separation": separation,
        "pair_count": len(pairs_at_separation(separation)),
        "pairs": pairs_at_separation(separation),
        "is_distance_maximizing": separation == maximum,
    } for separation in range(1, maximum + 1))
    maximum_pairs = set(pairs_at_separation(maximum))
    max_without_origin = {
        pair for pair in maximum_pairs if 0 not in pair
    }
    farthest_by_station = tuple({
        "station": station,
        "farthest_vertices": tuple(
            other for other in range(RING_STATIONS)
            if other != station
            and cyclic_separation(tuple(sorted((station, other))))
            == maximum
        ),
    } for station in range(RING_STATIONS))
    antipodal = {
        "ring_stations": RING_STATIONS,
        "floor_n_over_2": maximum,
        "unique_maximizing_separation_class": (
            tuple(
                row["separation"] for row in geometric_rows
                if row["is_distance_maximizing"]
            ) == (5,)
        ),
        "unordered_maximum_distance_pair_count": len(maximum_pairs),
        "unordered_maximum_distance_pairs": tuple(sorted(maximum_pairs)),
        "farthest_vertices_by_station": farthest_by_station,
        "unique_antipode_per_station": all(
            len(row["farthest_vertices"]) == 1
            for row in farthest_by_station
        ),
        "odd_ring_reading": (
            "C11 has one unique maximum separation value s=5, but no "
            "unique antipodal vertex: every station has two farthest "
            "vertices and there are 11 maximum-distance unordered pairs."
        ),
        "backbone_equals_maximum_pairs_without_station0":
            backbone_pairs == max_without_origin,
        "maximum_pairs_without_station0_count": len(max_without_origin),
        "omitted_maximum_pairs": tuple(
            sorted(maximum_pairs - backbone_pairs)
        ),
        "origin_exclusion_breaks_rotation_invariance": any(
            tuple(sorted(translated_pair(pair, tick)))
            not in backbone_pairs
            for pair in backbone_pairs
            for tick in range(RING_STATIONS)
        ),
    }

    core_source = ast.unparse(function_node(
        trees[AUDIT_INPUT_PATHS[0]], "apply_controller_step"
    ))
    multisource_source = ast.unparse(function_node(
        trees[AUDIT_INPUT_PATHS[1]], "synchronous_composition_word"
    ))
    controller_ast_exact = (
        "target = (station + 1) % stations" in core_source
        and (
            "b[station], a[target] = "
            "(a[target], b[station])"
        ) in core_source
        and (
            "positions = tuple(((station + 1) % stations "
            "for station in positions))"
        ) in multisource_source
    )
    literal_rows = []
    for separation in range(1, 6):
        all_pairs = pairs_at_separation(separation)
        separation_failures = 0
        collision_count = 0
        return_failures = 0
        for pair in all_pairs:
            orbit = tuple(
                translated_pair(pair, tick)
                for tick in range(RING_STATIONS + 1)
            )
            separation_failures += any(
                cyclic_separation(tuple(sorted(state))) != separation
                for state in orbit
            )
            collision_count += sum(
                state[0] == state[1] for state in orbit
            )
            return_failures += orbit[-1] != pair
        representative = all_pairs[0]
        literal_rows.append({
            "separation": separation,
            "pairs_checked": len(all_pairs),
            "representative_pair": representative,
            "representative_orbit_t0_through_t11": tuple(
                translated_pair(representative, tick)
                for tick in range(RING_STATIONS + 1)
            ),
            "separation_failures": separation_failures,
            "source_collision_count": collision_count,
            "return_failures": return_failures,
            "lawful_pairwise_separated_sector": separation > 1,
        })
    literal_controller = {
        "landed_rule": (
            "Both A-rail sources undergo the same nearest-neighbor update "
            "p -> p+1 mod 11 at each controller step."
        ),
        "source_AST_translation_exact": controller_ast_exact,
        "rows": tuple(literal_rows),
        "separation_is_invariant": all(
            not row["separation_failures"] for row in literal_rows
        ),
        "two_sources_never_collide": all(
            not row["source_collision_count"] for row in literal_rows
        ),
        "all_pairs_return_after_11": all(
            not row["return_failures"] for row in literal_rows
        ),
        "interpretation": (
            "Literal landed controller tokens are common-translated, not "
            "counterpropagating expanding wavefronts."
        ),
    }

    wavefront_rows = []
    for separation in range(1, 6):
        pair_rows = []
        for pair in pairs_at_separation(separation):
            first_tick, overlap = first_ball_meeting(pair)
            pair_rows.append((first_tick, len(overlap)))
        short_arc = separation
        long_arc = RING_STATIONS - separation
        arc_ticks = (
            (short_arc + 1) // 2,
            (long_arc + 1) // 2,
        )
        representative = (0, separation)
        first_tick, overlap = first_ball_meeting(representative)
        wavefront_rows.append({
            "separation": separation,
            "arc_lengths": (short_arc, long_arc),
            "per_arc_first_ball_overlap_ticks": arc_ticks,
            "both_arcs_first_overlap_simultaneously":
                arc_ticks[0] == arc_ticks[1],
            "global_first_overlap_tick": first_tick,
            "representative_first_overlap_stations": overlap,
            "representative_first_overlap_station_count": len(overlap),
            "rotation_uniform_tick_and_cardinality":
                len(set(pair_rows)) == 1,
        })
    simultaneous_separations = tuple(
        row["separation"] for row in wavefront_rows
        if row["both_arcs_first_overlap_simultaneously"]
    )
    wavefront = {
        "model": (
            "Auxiliary undirected graph balls B_t(x) on C11, expanding "
            "by graph radius one per tick; this is not the literal "
            "common-translation A-rail motion."
        ),
        "rows": tuple(wavefront_rows),
        "simultaneous_two_arc_first_overlap_separations":
            simultaneous_separations,
        "s5_first_overlap_station_count": next(
            row["representative_first_overlap_station_count"]
            for row in wavefront_rows if row["separation"] == 5
        ),
        "s5_exact_reading": (
            "At s=5 the length-5 and length-6 arcs first overlap together "
            "at tick 3.  The ball intersection has three stations, not "
            "two: two central vertices on the odd arc and one midpoint "
            "on the even arc."
        ),
    }

    residuals = cycle832_c["residual_census_v1_reproduced"]
    anatomies = residuals["funnel_anatomies"]
    event0 = next(
        row for row in anatomies["rows"] if int(row["event"]) == 0
    )
    anatomy_source = ast.unparse(function_node(
        trees[AUDIT_INPUT_PATHS[2]], "anatomy"
    ))
    anatomy_ast_exact = all(fragment in anatomy_source for fragment in (
        "result['state_bits'] == 5815",
        "result['hamming_weight'] == 44",
        "occupancy == ((1, 1), (0, 0))",
        "tokens == ((1, 0), (0, 0))",
        "result['link_weights'] == (0,)",
        "('source.SOURCE_POINTER', 'bank0.DIRECTION_OK')",
    ))
    s4_pair = (1, 5)
    s4_orbit = tuple(
        tuple(sorted(translated_pair(s4_pair, tick)))
        for tick in range(RING_STATIONS)
    )
    s4_selector_hits = tuple(
        tick for tick, pair in enumerate(s4_orbit)
        if cyclic_separation(pair) == 5 and 0 not in pair
    )
    skeleton = {
        "state_bits": 5815,
        "state_sha256": event0["state_sha256"],
        "hamming_weight": event0["full_state_hamming_weight"],
        "occupancy": ((1, 1), (0, 0)),
        "tokens": ((1, 0), (0, 0)),
        "link_weights": (0,),
        "residual_fields": tuple(event0["landed_residual_support"]),
        "residual_component_counts":
            event0["landed_support_component_counts"],
    }
    s4_candidate = {
        "construction_status":
            "ABSTRACT_PRODUCT_CANDIDATE_NOT_A_NEW_5815_BIT_WITNESS",
        "event": 0,
        "pair": s4_pair,
        "controller_A_mask": tuple(
            int(station in s4_pair)
            for station in range(RING_STATIONS)
        ),
        "copied_landed_Sstar_target_anatomy": skeleton,
        "pairwise_separated_lawful": cyclic_separation(s4_pair) > 1,
        "token_count": 2,
        "cyclic_separation": cyclic_separation(s4_pair),
        "origin_absent_initially": 0 not in s4_pair,
        "position_orbit_t0_through_t10": s4_orbit,
        "position_orbit_period": RING_STATIONS,
        "separation_preserved_every_tick": all(
            cyclic_separation(pair) == 4 for pair in s4_orbit
        ),
        "backbone_selector_hit_times": s4_selector_hits,
        "backbone_selector_unreachable_in_position_projection":
            not s4_selector_hits,
        "Sstar_anatomy_contains_pair_coordinate_fields": False,
        "lawfulness_outcome":
            "HOLDS_EXACTLY_FOR_THE_POSITION_SECTOR",
        "reachability_outcome": (
            "The s=4 position orbit never reaches the s=5 selector, for "
            "all ticks by period 11.  Full internal-state reachability of "
            "the copied S* target is OPEN: this abstract product is not a "
            "constructed 5815-bit off-backbone trajectory witness."
        ),
    }
    skeleton_probe = {
        "cycle822_anatomy_AST_exact": anatomy_ast_exact,
        "landed_event0_funnel_anatomy": skeleton,
        "occupancy_1_1_is_bank_cell_geometry": True,
        "occupancy_1_1_is_ring_pair_geometry": False,
        "s4_analogue_candidate": s4_candidate,
        "antipodality_required_by_skeleton_fields": False,
        "antipodality_required_by_full_dynamics": "OPEN",
    }

    exact = (
        antipodal["unique_maximizing_separation_class"]
        and len(maximum_pairs) == 11
        and not antipodal["unique_antipode_per_station"]
        and antipodal[
            "backbone_equals_maximum_pairs_without_station0"
        ]
        and len(max_without_origin) == 9
        and controller_ast_exact
        and literal_controller["separation_is_invariant"]
        and literal_controller["two_sources_never_collide"]
        and literal_controller["all_pairs_return_after_11"]
        and simultaneous_separations == (5,)
        and wavefront["s5_first_overlap_station_count"] == 3
        and all(
            row["rotation_uniform_tick_and_cardinality"]
            for row in wavefront_rows
        )
        and anatomy_ast_exact
        and skeleton["hamming_weight"] == 44
        and skeleton["residual_component_counts"]
        == {"bank0": 1, "source": 1}
        and s4_candidate["pairwise_separated_lawful"]
        and s4_candidate["separation_preserved_every_tick"]
        and not s4_selector_hits
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "A_antipodal_maximum_distance_probe": antipodal,
        "B_literal_controller_collision_probe": literal_controller,
        "B_auxiliary_wavefront_collision_probe": wavefront,
        "C_funnel_skeleton_s4_control": skeleton_probe,
        "sharp_dynamics_outcome": (
            "s=5 is uniquely maximum-distance and uniquely equalizes the "
            "two arc-wise graph-ball meeting ticks (3,3).  But the literal "
            "controller common-translates both sources without collision, "
            "and the weight-44 [1,1] anatomy is bank-register geometry.  "
            "Therefore these exact structures do not yet derive the "
            "backbone selection."
        ),
        "pass": exact,
    }


def candidate_law_certificate(
    certificate_a: dict[str, object],
    certificate_b: dict[str, object],
) -> dict[str, object]:
    rows = certificate_a["status_by_separation"]
    backbone_pairs = set(
        certificate_b["A_antipodal_maximum_distance_probe"][
            "unordered_maximum_distance_pairs"
        ]
    ) - set(
        certificate_b["A_antipodal_maximum_distance_probe"][
            "omitted_maximum_pairs"
        ]
    )
    complete_pairs = {
        tuple(pair)
        for row in rows
        for pair in row["complete_four_event_pair_fibers"]
    }
    all_pairs = tuple(
        pair
        for separation in range(1, 6)
        for pair in pairs_at_separation(separation)
    )
    law_rows = tuple({
        "pair": pair,
        "separation": cyclic_separation(pair),
        "origin_absent": 0 not in pair,
        "predicate_s5_and_origin_absent":
            cyclic_separation(pair) == 5 and 0 not in pair,
        "landed_backbone_pair": pair in backbone_pairs,
        "complete_four_event_resolved_fiber": pair in complete_pairs,
    } for pair in all_pairs)
    selector_exact = all(
        row["predicate_s5_and_origin_absent"]
        == row["landed_backbone_pair"]
        == row["complete_four_event_resolved_fiber"]
        for row in law_rows
    )
    wavefront_s5_pairs = set(pairs_at_separation(5))
    graph_property_false_positives = tuple(sorted(
        wavefront_s5_pairs - backbone_pairs
    ))
    exact = (
        certificate_a["pass"]
        and certificate_b["pass"]
        and selector_exact
        and len(law_rows) == 55
        and len(backbone_pairs) == len(complete_pairs) == 9
        and graph_property_false_positives == ((0, 5), (0, 6))
        and not certificate_a["only_s5_has_any_resolved_key"]
        and certificate_a[
            "only_s5_has_complete_four_event_pair_fibers"
        ]
    )
    return {
        "verdict": "PASS" if exact else "FAIL",
        "actual_current_surface_status": "exact-support",
        "HOLDS_EXACTLY": (
            "On the landed C11 k=2 catalog, an unordered pair carries a "
            "complete resolved four-event fiber iff its cyclic separation "
            "is 5 and station 0 is absent.  Equivalently, the nine-pair "
            "backbone is exactly {pair: separation(pair)=5 and 0 not in "
            "pair}.  Separation 5 alone selects 11 pairs, not nine."
        ),
        "law_table": law_rows,
        "selector_biconditional_exact": selector_exact,
        "backbone_pairs": tuple(sorted(backbone_pairs)),
        "complete_four_event_pairs": tuple(sorted(complete_pairs)),
        "auxiliary_two_arc_wavefront_property_pair_count":
            len(wavefront_s5_pairs),
        "auxiliary_two_arc_wavefront_property_false_positives":
            graph_property_false_positives,
        "individual_key_only_s5_claim": "FAILS",
        "complete_pair_fiber_only_s5_claim": "HOLDS_EXACTLY",
        "causal_derivation_status": "OPEN",
        "conjectural": (
            "It remains conjectural that simultaneous two-arc graph-ball "
            "meeting causes funnel entry, that antipodality is necessary "
            "for the weight-44 S* funnel, or that a lawful s=4 full "
            "internal trajectory cannot reach S*.  The exact graph-ball "
            "property overselects (0,5) and (0,6), while literal landed "
            "tokens never collide."
        ),
        "pass": exact,
    }


def render(
    certificates: dict[str, object],
    checks: dict[str, bool],
    report: dict[str, object],
) -> str:
    lines = tuple(
        f"CERTIFICATE {name} {compact(value)}"
        for name, value in certificates.items()
    ) + tuple(
        f"CHECK {name}={str(value).lower()}"
        for name, value in checks.items()
    ) + (
        "SUMMARY_JSON " + compact(report),
        str(report["terminal"]),
    )
    return "\n".join(lines) + "\n"


def stable_render(
    certificates: dict[str, object],
    checks: dict[str, bool],
    report: dict[str, object],
) -> str:
    for _attempt in range(20):
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE837_WHY_SEP5_EXACT_BOUNDARY_PASS"
            if report["pass"]
            else "CYCLE837_WHY_SEP5_HONEST_FAIL"
        )
        output = render(certificates, checks, report)
        size = len(output.encode())
        controls = certificates["D_CONTROLS"]
        if (
            report["stdout_bytes"] == size
            and controls["stdout_bytes"] == size
        ):
            return output
        report["stdout_bytes"] = size
        controls["stdout_bytes"] = size
    raise AssertionError("stdout byte fixed point did not converge")


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "exception_type": type(error).__name__,
            "exception": str(error),
            "terminal": "CYCLE837_WHY_SEP5_HONEST_FAIL",
        }) + "\n")
        return 1


def run() -> int:
    started = monotonic()
    controls, payloads, trees = source_controls()
    source_pass = bool(controls["pass"])
    records = landed_records(payloads)
    certificate_a = separation_census_certificate(records)
    certificate_b = dynamics_probe_certificate(records, trees)
    certificate_c = candidate_law_certificate(
        certificate_a, certificate_b
    )
    replay_a = separation_census_certificate(records)
    replay_b = dynamics_probe_certificate(records, trees)
    replay_c = candidate_law_certificate(replay_a, replay_b)
    first_digest = digest((certificate_a, certificate_b, certificate_c))
    replay_digest = digest((replay_a, replay_b, replay_c))
    deterministic = (
        first_digest == replay_digest
        and certificate_a == replay_a
        and certificate_b == replay_b
        and certificate_c == replay_c
    )
    elapsed = monotonic() - started
    controls.update({
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(FIREWALL.hits),
        "exact_arithmetic": (
            "All separations, pair/key counts, graph distances, ball "
            "intersections, arc meeting ticks, translations, status "
            "censuses, SHA-256 values, and equality tests use exact Python "
            "integers/bytes/sets; only monotonic runtime is a float."
        ),
        "determinism": {
            "first_certificate_sha256": first_digest,
            "replay_certificate_sha256": replay_digest,
            "certificates_exactly_equal": deterministic,
        },
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    })
    controls_base = (
        source_pass
        and certificate_a["pass"]
        and certificate_b["pass"]
        and certificate_c["pass"]
        and deterministic
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    controls["pass"] = controls_base
    checks = {
        "A_SEPARATION_CENSUS_EXACT": bool(certificate_a["pass"]),
        "B_DYNAMICS_PROBE_EXACT_BOUNDARY": bool(certificate_b["pass"]),
        "C_CANDIDATE_LAW_SHARPEST_EXACT": bool(certificate_c["pass"]),
        "D_CONTROLS": controls_base,
    }
    certificates = {
        "A_SEPARATION_CENSUS": certificate_a,
        "B_DYNAMICS_PROBE": certificate_b,
        "C_CANDIDATE_LAW": certificate_c,
        "D_CONTROLS": controls,
    }
    table_summary = tuple({
        "separation": row["separation"],
        "pairs": row["pair_count"],
        "landed_keys": row["landed_key_count"],
        "resolved": row["resolved_key_count"],
        "open": row["open_key_count"],
        "complete_pair_fibers":
            row["complete_four_event_pair_fiber_count"],
    } for row in certificate_a["status_by_separation"])
    report = {
        "cycle": 837,
        "target": "why max-separation-5",
        "actual_current_surface_status": "exact-support",
        "status_by_separation": table_summary,
        "individual_key_only_s5_claim":
            certificate_c["individual_key_only_s5_claim"],
        "complete_pair_fiber_only_s5_claim":
            certificate_c["complete_pair_fiber_only_s5_claim"],
        "sharpest_exact_claim": certificate_c["HOLDS_EXACTLY"],
        "causal_derivation_status":
            certificate_c["causal_derivation_status"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE837_WHY_SEP5_HONEST_FAIL",
    }
    output = stable_render(certificates, checks, report)
    stdout_ok = len(output.encode()) < STDOUT_LIMIT_BYTES
    checks["D_CONTROLS"] = controls_base and stdout_ok
    controls["pass"] = checks["D_CONTROLS"]
    output = stable_render(certificates, checks, report)
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "failure": "stdout limit exceeded",
            "stdout_bytes": len(output.encode()),
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "terminal": "CYCLE837_WHY_SEP5_HONEST_FAIL",
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
