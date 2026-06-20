#!/usr/bin/env python3
"""Firewall for the distance-law finite-table diagnostic split.

This verifier is intentionally fast. It checks that the source note, runner
text, and cached heavy-runner output all present the distance-law packet as a
bounded finite-table diagnostic rather than a continuum inverse-square closure.
"""

from __future__ import annotations

from pathlib import Path

import runner_cache


ROOT = Path(__file__).resolve().parent.parent
NOTE = ROOT / "docs" / "DISTANCE_LAW_DEFINITIVE_NOTE.md"
RUNNER = ROOT / "scripts" / "frontier_distance_law_definitive.py"
CACHE = ROOT / "logs" / "runner-cache" / "frontier_distance_law_definitive.txt"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(name: str, ok: bool, detail: str, results: list[tuple[str, bool]]) -> None:
    results.append((name, ok))
    status = "PASS" if ok else "FAIL"
    print(f"{status}: {name} -- {detail}")


def contains_all(text: str, needles: list[str]) -> tuple[bool, list[str]]:
    missing = [needle for needle in needles if needle not in text]
    return not missing, missing


def main() -> int:
    results: list[tuple[str, bool]] = []
    note = read(NOTE)
    runner = read(RUNNER)
    cache = read(CACHE)

    note_needles = [
        "# Distance Law Finite-Table Diagnostic",
        "**Status:** bounded support note -- finite ordered-cubic distance-law diagnostic",
        "## Finite-table diagnostic split (2026-06-17)",
        "the selected `N >= 56` weighted-mean diagnostic",
        "`alpha = -1.00104 +/- 0.00416`",
        "does **not** add an estimator-selection theorem",
        "not as a continuum estimator",
        "bounded finite-table support only",
        "selected scaled-window weighted mean is a diagnostic",
    ]
    ok, missing = contains_all(note, note_needles)
    check("note finite-table diagnostic boundary", ok, f"missing={missing}", results)

    note_banned = [
        "# Definitive Distance Law Closure",
        "**Status:** bounded review candidate -- high-precision ordered-cubic distance-law closure",
        "The weighted mean of converged large-N values is the correct estimator",
        "architecture-independent closure by itself",
    ]
    present = [needle for needle in note_banned if needle in note]
    check("note removes old closure wording", not present, f"present={present}", results)

    runner_needles = [
        "Finite-table distance-law diagnostic on ordered-cubic Dirichlet lattices.",
        "Boundary: the weighted mean of scaled-fit values for N>=56 is a selected",
        "DISTANCE LAW FINITE-TABLE DIAGNOSTIC",
        "finite-table diagnostics",
        "Selected diagnostic estimator",
        "DIAGNOSTIC MATCH",
        "BOUNDED DIAGNOSTIC CLAIMS",
        "a retained inverse-square law, continuum theorem, or estimator-selection theorem",
    ]
    ok, missing = contains_all(runner, runner_needles)
    check("runner diagnostic firewall text", ok, f"missing={missing}", results)

    runner_banned = [
        "DEFINITIVE DISTANCE LAW CLOSURE",
        "Closes the gravitational force exponent",
        "Best estimate (",
        "PASS: alpha consistent",
        "SAFE CLAIMS",
        "Gravitational force F ~ 1/r^2 in 3D.",
        "emerges from\n   valley-linear path summation in 3D with sub-percent precision",
    ]
    present = [needle for needle in runner_banned if needle in runner]
    check("runner removes old retained-style output", not present, f"present={present}", results)

    cache_status = runner_cache.cache_status("scripts/frontier_distance_law_definitive.py")
    check("heavy runner cache is fresh", cache_status == "fresh", f"status={cache_status}", results)

    cache_needles = [
        "DISTANCE LAW FINITE-TABLE DIAGNOSTIC",
        "All extrapolation estimates:",
        "Full b, all N                    -0.93474",
        "Core b=4..8, all N               -0.88860",
        "Scaled b=4..N/6, all N           -0.94102",
        "Weighted mean alpha_scaled (N>=56): -1.00104 +/- 0.00416",
        "Selected diagnostic estimator (Selected weighted mean scaled (N>=56)):",
        "DIAGNOSTIC MATCH: selected alpha is consistent with -1.0 to sub-1% precision.",
        "BOUNDED DIAGNOSTIC CLAIMS",
        "Boundary: this is bounded finite-table numerical support.",
    ]
    ok, missing = contains_all(cache, cache_needles)
    check("cache carries diagnostic values and caveats", ok, f"missing={missing}", results)

    cache_banned = [
        "DEFINITIVE DISTANCE LAW CLOSURE",
        "Best estimate (Weighted mean scaled (N>=56)):",
        "PASS: alpha consistent with -1.0 to sub-1% precision.",
        "SAFE CLAIMS",
        "Combined evidence: the inverse-square force law",
    ]
    present = [needle for needle in cache_banned if needle in cache]
    check("cache removes old closure output", not present, f"present={present}", results)

    passed = sum(1 for _, ok in results if ok)
    failed = len(results) - passed
    print()
    print(f"TOTAL PASS: {passed}")
    print(f"TOTAL FAIL: {failed}")
    print(
        "Verdict: finite-table diagnostic split verified; no estimator-selection "
        "or retained inverse-square closure is claimed."
    )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
