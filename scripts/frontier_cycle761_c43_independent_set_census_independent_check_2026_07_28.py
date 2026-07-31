#!/usr/bin/env python3
"""Independent check of the Cycle-761 C43 finite combinatorics result.

The primary is parsed as inert source and executed only in a fresh subprocess;
it is never imported. This checker recomputes C43 by a first/last-state dynamic
program and exhaustively enumerates every labelled mask for C3 through C18.
"""
from __future__ import annotations

import ast
from collections import Counter
import json
from math import comb
from pathlib import Path
import subprocess
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = (
    "docs/CYCLE_GRAPH_C43_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md"
)
PRIMARY_PATH = (
    "scripts/frontier_cycle761_c43_independent_set_census_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle761_c43_independent_set_census_2026_07_28.py",
    "docs/CYCLE_GRAPH_C43_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STATIONS = 43
EXPECTED_STRATA = (
    1,
    43,
    860,
    10_621,
    90_687,
    567_987,
    2_701_776,
    9_970_840,
    28_915_436,
    66_335_412,
    120_609_840,
    173_376_645,
    195_747_825,
    171_655_785,
    115_000_920,
    57_500_460,
    20_764_055,
    5_167_525,
    826_804,
    76_153,
    3_311,
    43,
)
EXPECTED_TOTAL = 969_323_029
EXPECTED_PAIR_MASKS = 43
EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES = 86
ONE_EDGE_MIN_OCCUPIED = 12
ONE_EDGE_MAX_OCCUPIED = 21
ONE_EDGE_PHASES = (0, 1)
STDOUT_LIMIT_BYTES = 150 * 1024

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def cycle_strata_state_dp(stations: int) -> tuple[int, ...]:
    """Count by conditioning on the first and last occupancy states."""

    totals: Counter[int] = Counter()
    for first in (0, 1):
        states: Counter[tuple[int, int]] = Counter({(first, first): 1})
        for _ in range(1, stations):
            next_states: Counter[tuple[int, int]] = Counter()
            for (previous, occupied), multiplicity in states.items():
                next_states[(0, occupied)] += multiplicity
                if previous == 0:
                    next_states[(1, occupied + 1)] += multiplicity
            states = next_states
        for (last, occupied), multiplicity in states.items():
            if not (first and last):
                totals[occupied] += multiplicity
    return tuple(totals[index] for index in range(stations // 2 + 1))


def brute_force_cycle_strata(stations: int) -> tuple[int, ...]:
    full = (1 << stations) - 1
    counts = [0] * (stations // 2 + 1)
    for mask in range(1 << stations):
        rotated = ((mask << 1) & full) | (mask >> (stations - 1))
        if not (mask & rotated):
            counts[mask.bit_count()] += 1
    return tuple(counts)


def closed_formula(stations: int) -> tuple[int, ...]:
    return (1,) + tuple(
        stations * comb(stations - occupied, occupied) // (stations - occupied)
        for occupied in range(1, stations // 2 + 1)
    )


def adjacent_pair_incidences(stations: int) -> tuple[tuple[int, int], ...]:
    rows: list[tuple[int, int]] = []
    for start in range(stations):
        mask = (1 << start) | (1 << ((start + 1) % stations))
        incidences = 0
        for occupied in range(stations):
            if not (mask & (1 << occupied)):
                continue
            neighbors = (
                (1 << ((occupied - 1) % stations))
                | (1 << ((occupied + 1) % stations))
            )
            incidences += bool(mask & neighbors)
        rows.append((mask, incidences))
    return tuple(rows)


def one_edge_vertex_rows(
    stations: int,
) -> tuple[tuple[int, int, int, frozenset[int]], ...]:
    rows: list[tuple[int, int, int, frozenset[int]]] = []
    for cardinality in range(ONE_EDGE_MIN_OCCUPIED, ONE_EDGE_MAX_OCCUPIED + 1):
        for edge_start in range(stations):
            for phase in ONE_EDGE_PHASES:
                vertices = {edge_start, (edge_start + 1) % stations}
                vertices.update(
                    (edge_start + 3 + phase + 2 * step) % stations
                    for step in range(cardinality - 2)
                )
                rows.append(
                    (cardinality, edge_start, phase, frozenset(vertices))
                )
    return tuple(rows)


def vertex_set_edges(
    vertices: frozenset[int], stations: int
) -> frozenset[frozenset[int]]:
    return frozenset(
        frozenset((vertex, (vertex + 1) % stations))
        for vertex in vertices
        if (vertex + 1) % stations in vertices
    )


def literal_assignment(tree: ast.Module, name: str) -> object:
    rows: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                rows.append(node.value)
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name) and node.target.id == name:
                rows.append(node.value)
    if len(rows) != 1:
        raise AssertionError(("assignment census", name, len(rows)))
    return ast.literal_eval(rows[0])


def imported_roots(tree: ast.Module) -> set[str]:
    roots: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            roots.add(node.module.split(".", 1)[0])
    return roots


def parse_primary_report(stdout: str) -> dict[str, object]:
    rows = [line for line in stdout.splitlines() if line.startswith("{")]
    if len(rows) != 1:
        raise AssertionError(("primary JSON census", len(rows)))
    value = json.loads(rows[0])
    if not isinstance(value, dict):
        raise AssertionError("primary report is not an object")
    return value


def main() -> int:
    started = perf_counter()
    root = Path(__file__).resolve().parents[1]
    source = (root / PRIMARY_PATH).read_text(encoding="utf-8")
    note_text = (root / NOTE_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)

    allowed_imports = {
        "__future__",
        "hashlib",
        "json",
        "math",
        "pathlib",
        "time",
    }
    check(
        "primary_imports_only_standard_library_modules",
        imported_roots(tree) <= allowed_imports,
    )
    check(
        "primary_declares_only_the_note_as_external_input",
        literal_assignment(tree, "AUDIT_INPUT_PATHS") == (NOTE_PATH,),
    )
    check(
        "primary_source_excludes_rejected_parent_modules",
        "frontier_cycle739" not in source
        and "frontier_cycle740" not in source
        and "frontier_cycle719" not in source
        and "numpy" not in source,
    )

    c43_dp = cycle_strata_state_dp(STATIONS)
    c43_formula = closed_formula(STATIONS)
    check("independent_c43_state_dp_matches_declared_strata", c43_dp == EXPECTED_STRATA)
    check("independent_c43_formula_matches_state_dp", c43_formula == c43_dp)
    check("independent_c43_total_is_exact", sum(c43_dp) == EXPECTED_TOTAL)

    brute_force_rows = {
        stations: brute_force_cycle_strata(stations)
        for stations in range(3, 19)
    }
    check(
        "closed_formula_matches_all_masks_for_c3_through_c18",
        all(
            brute_force_rows[stations] == closed_formula(stations)
            for stations in brute_force_rows
        ),
    )

    pair_rows = adjacent_pair_incidences(STATIONS)
    check(
        "independent_adjacent_pair_mask_census_is_exact",
        len(pair_rows) == EXPECTED_PAIR_MASKS
        and len({mask for mask, _ in pair_rows}) == EXPECTED_PAIR_MASKS,
    )
    check(
        "independent_occupied_endpoint_incidence_total_is_eighty_six",
        all(incidences == 2 for _, incidences in pair_rows)
        and sum(incidences for _, incidences in pair_rows)
        == EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES,
    )

    one_edge_rows = one_edge_vertex_rows(STATIONS)
    structural_one_edge_total = (
        len(range(ONE_EDGE_MIN_OCCUPIED, ONE_EDGE_MAX_OCCUPIED + 1))
        * STATIONS
        * len(ONE_EDGE_PHASES)
    )
    one_edge_sets = tuple(vertices for _, _, _, vertices in one_edge_rows)
    one_edge_edge_sets = tuple(
        vertex_set_edges(vertices, STATIONS) for vertices in one_edge_sets
    )
    check(
        "independent_one_edge_family_size_is_structurally_derived",
        len(one_edge_rows) == structural_one_edge_total
        and structural_one_edge_total == 860,
    )
    check(
        "independent_one_edge_vertex_sets_are_pairwise_distinct",
        len(set(one_edge_sets)) == len(one_edge_sets),
    )
    check(
        "independent_one_edge_rows_have_declared_cardinality",
        all(
            len(vertices) == cardinality
            for cardinality, _, _, vertices in one_edge_rows
        ),
    )
    check(
        "independent_one_edge_rows_have_only_the_labelled_edge",
        all(
            edges
            == frozenset(
                (frozenset((edge_start, (edge_start + 1) % STATIONS)),)
            )
            for (_, edge_start, _, _), edges in zip(
                one_edge_rows, one_edge_edge_sets, strict=True
            )
        ),
    )
    check(
        "independent_one_edge_occupied_endpoint_incidence_total_is_exact",
        sum(2 * len(edges) for edges in one_edge_edge_sets)
        == 2 * structural_one_edge_total
        == 1_720,
    )

    completed = subprocess.run(
        [sys.executable, str(root / PRIMARY_PATH)],
        cwd=root,
        text=True,
        capture_output=True,
        timeout=60,
        check=False,
    )
    primary_report = parse_primary_report(completed.stdout)
    check(
        "fresh_primary_subprocess_passes",
        completed.returncode == 0
        and completed.stderr == ""
        and primary_report.get("terminal")
        == "CYCLE761_C43_INDEPENDENT_SET_CENSUS_PASS",
    )
    check(
        "fresh_primary_report_matches_independent_recount",
        primary_report.get("strata") == list(c43_dp)
        and primary_report.get("independent_set_total") == EXPECTED_TOTAL
        and primary_report.get("adjacent_pair_masks") == EXPECTED_PAIR_MASKS
        and primary_report.get("occupied_endpoint_incidences")
        == EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES
        and primary_report.get("one_edge_masks") == structural_one_edge_total
        and primary_report.get("one_edge_occupied_endpoint_incidences")
        == 2 * structural_one_edge_total,
    )
    check(
        "note_preserves_narrow_unaudited_scope",
        "finite graph-combinatorics support result only" in note_text
        and "Authority: none" in note_text
        and "Audit: unset" in note_text
        and "Independent claim audit remains required" in note_text,
    )

    report = {
        "cycle": 761,
        "claim": "independent_c43_census_check",
        "stations": STATIONS,
        "strata": list(c43_dp),
        "independent_set_total": sum(c43_dp),
        "small_cycle_exhaustive_range": [3, 18],
        "small_cycle_masks_checked": sum(1 << n for n in range(3, 19)),
        "adjacent_pair_masks": len(pair_rows),
        "occupied_endpoint_incidences": sum(row[1] for row in pair_rows),
        "one_edge_occupied_range": [ONE_EDGE_MIN_OCCUPIED, ONE_EDGE_MAX_OCCUPIED],
        "one_edge_phases": list(ONE_EDGE_PHASES),
        "one_edge_masks": len(one_edge_rows),
        "one_edge_occupied_endpoint_incidences": sum(
            2 * len(edges) for edges in one_edge_edge_sets
        ),
        "primary_imported": False,
        "passed": sum(CHECKS.values()),
        "failed": len(CHECKS) - sum(CHECKS.values()),
        "runtime_sec": round(perf_counter() - started, 6),
    }
    terminal = (
        "CYCLE761_C43_INDEPENDENT_SET_CENSUS_INDEPENDENT_PASS"
        if report["failed"] == 0
        else "CYCLE761_C43_INDEPENDENT_SET_CENSUS_INDEPENDENT_FAIL"
    )
    report["terminal"] = terminal
    rendered = OUTPUT_LINES + [
        json.dumps(report, sort_keys=True, separators=(",", ":")),
        terminal,
    ]
    output = "\n".join(rendered) + "\n"
    if len(output.encode()) > STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout budget exceeded")
    print(output, end="")
    return 0 if report["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
