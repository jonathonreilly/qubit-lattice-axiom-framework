#!/usr/bin/env python3
"""Independent check of the Cycle-756 C35 finite combinatorics result.

The primary is parsed as inert source and executed only in a fresh subprocess;
it is never imported. This checker recomputes C35 by a first/last-state dynamic
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
    "docs/CYCLE_GRAPH_C35_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md"
)
PRIMARY_PATH = (
    "scripts/frontier_cycle756_c35_independent_set_census_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle756_c35_independent_set_census_2026_07_28.py",
    "docs/CYCLE_GRAPH_C35_INDEPENDENT_SET_CENSUS_"
    "NARROW_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

STATIONS = 35
EXPECTED_STRATA = (
    1,
    35,
    560,
    5_425,
    35_525,
    166_257,
    573_300,
    1_480_050,
    2_877_875,
    4_206_125,
    4_576_264,
    3_640_210,
    2_057_510,
    791_350,
    193_800,
    27_132,
    1_785,
    35,
)
EXPECTED_TOTAL = 20_633_239
EXPECTED_PAIR_MASKS = 35
EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES = 70
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


def literal_assignment(tree: ast.Module, name: str) -> object:
    rows: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
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

    c35_dp = cycle_strata_state_dp(STATIONS)
    c35_formula = closed_formula(STATIONS)
    check("independent_c35_state_dp_matches_declared_strata", c35_dp == EXPECTED_STRATA)
    check("independent_c35_formula_matches_state_dp", c35_formula == c35_dp)
    check("independent_c35_total_is_exact", sum(c35_dp) == EXPECTED_TOTAL)

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
        "independent_occupied_endpoint_incidence_total_is_seventy",
        all(incidences == 2 for _, incidences in pair_rows)
        and sum(incidences for _, incidences in pair_rows)
        == EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES,
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
        == "CYCLE756_C35_INDEPENDENT_SET_CENSUS_PASS",
    )
    check(
        "fresh_primary_report_matches_independent_recount",
        primary_report.get("strata") == list(c35_dp)
        and primary_report.get("independent_set_total") == EXPECTED_TOTAL
        and primary_report.get("adjacent_pair_masks") == EXPECTED_PAIR_MASKS
        and primary_report.get("occupied_endpoint_incidences")
        == EXPECTED_OCCUPIED_ENDPOINT_INCIDENCES,
    )
    check(
        "note_preserves_narrow_unaudited_scope",
        "finite graph-combinatorics support result only" in note_text
        and "Authority: none" in note_text
        and "Audit: unset" in note_text
        and "Independent claim audit remains required." in note_text,
    )

    report = {
        "cycle": 756,
        "claim": "independent_c35_census_check",
        "stations": STATIONS,
        "strata": list(c35_dp),
        "independent_set_total": sum(c35_dp),
        "small_cycle_exhaustive_range": [3, 18],
        "small_cycle_masks_checked": sum(1 << n for n in range(3, 19)),
        "adjacent_pair_masks": len(pair_rows),
        "occupied_endpoint_incidences": sum(row[1] for row in pair_rows),
        "primary_imported": False,
        "passed": sum(CHECKS.values()),
        "failed": len(CHECKS) - sum(CHECKS.values()),
        "runtime_sec": round(perf_counter() - started, 6),
    }
    terminal = (
        "CYCLE756_C35_INDEPENDENT_SET_CENSUS_INDEPENDENT_PASS"
        if report["failed"] == 0
        else "CYCLE756_C35_INDEPENDENT_SET_CENSUS_INDEPENDENT_FAIL"
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
