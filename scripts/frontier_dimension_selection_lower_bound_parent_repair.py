#!/usr/bin/env python3
"""Parent-row repair runner for DIMENSION_SELECTION_NOTE.md.

The runner verifies the 2026-05-27 lower-bound scope repair by reusing the
finite-k derivative machinery from the bridge row. It checks that the parent
row now claims only the finite-runner lower-bound surface.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "DIMENSION_SELECTION_NOTE.md"
BRIDGE_NOTE = ROOT / "docs" / "DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md"
BRIDGE_RUNNER = ROOT / "scripts" / "frontier_dimension_selection_finite_k_centroid_sign_bridge.py"

PASS = 0
FAIL = 0
DIMS = (1, 2, 3, 4, 5)
EXPECTED = {1: -1, 2: -1, 3: 1, 4: 1, 5: 1}


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def one_line(text: str) -> str:
    return " ".join(text.split())


def sign(value: float) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def load_bridge_runner():
    spec = importlib.util.spec_from_file_location("finite_k_bridge", BRIDGE_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load finite-k bridge runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    print("# Dimension-selection parent lower-bound repair")
    note = read(NOTE)
    flat_note = one_line(note)
    bridge_note = read(BRIDGE_NOTE)

    for phrase in [
        "finite-runner lower-bound support only",
        "does not claim",
        "not a unique-dimension theorem",
        "DIMENSION_SELECTION_FINITE_K_CENTROID_SIGN_BRIDGE_NOTE_2026-05-25.md",
        "does not authorize any framework-baseline rewrite",
        "This row does not claim:",
        "framework-internal upper-bound derivation",
    ]:
        check(f"parent note contains boundary phrase: {phrase}", phrase in flat_note)

    for phrase in [
        "Exact Finite-k Derivative",
        "d <= 2  ->  negative centroid response",
        "d >= 3  ->  positive centroid response",
        "does not close the upper-bound side",
    ]:
        check(f"bridge note contains support phrase: {phrase}", phrase in bridge_note)

    bridge = load_bridge_runner()
    derivative_results: dict[int, float] = {}
    finite_probe_results: dict[int, float] = {}
    for d in DIMS:
        derivative = float(bridge.finite_k_centroid_derivative(d)["dC_dM_at_zero"])
        finite_probe = float(
            bridge.propagate_centroid_for_mass(d, bridge.FINITE_M)
            - bridge.propagate_centroid_for_mass(d, 0.0)
        )
        derivative_results[d] = derivative
        finite_probe_results[d] = finite_probe
        check(f"d={d} exact finite-k derivative has lower-bound sign", sign(derivative) == EXPECTED[d], derivative)
        check(f"d={d} parent finite-M replay has lower-bound sign", sign(finite_probe) == EXPECTED[d], finite_probe)

    passes = [d for d in DIMS if derivative_results[d] > 0 and finite_probe_results[d] > 0]
    fails = [d for d in DIMS if derivative_results[d] < 0 and finite_probe_results[d] < 0]
    check("finite-k lower-bound pass set is d=3,4,5", passes == [3, 4, 5], passes)
    check("finite-k lower-bound fail set is d=1,2", fails == [1, 2], fails)

    forbidden = [
        "self-consistency uniquely selects d = 3",
        "the Z^3 spatial substrate has been derived",
        "repo-wide framework-baseline rewrite is authorized",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
