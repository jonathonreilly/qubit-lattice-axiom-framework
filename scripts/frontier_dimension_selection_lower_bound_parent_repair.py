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
PARENT_RUNNER = ROOT / "scripts" / "frontier_dimension_selection.py"

PASS = 0
FAIL = 0
DIMS = (1, 2, 3, 4, 5)
EXPECTED = {1: -1, 2: -1, 3: 1, 4: 1, 5: 1}
EXPECTED_ATTRACTIVE = {1: False, 2: False, 3: True, 4: True, 5: True}
EXPECTED_BETA_2DP = {1: 0.18, 2: 0.27, 3: 1.01, 4: 1.05, 5: 1.03}
EXPECTED_ALPHA_2DP = {1: 0.42, 2: -0.17, 3: 1.32, 4: 3.30, 5: 5.01}


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


def load_parent_runner():
    spec = importlib.util.spec_from_file_location("dimension_parent", PARENT_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load parent dimension runner")
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

    for path in [PARENT_RUNNER, BRIDGE_RUNNER]:
        text = read(path)
        check(f"load-bearing runner source exists: {path.relative_to(ROOT)}", path.exists())
        check(
            f"load-bearing runner source is untruncated: {path.relative_to(ROOT)}",
            len(text.splitlines()) > 80 and "if __name__" in text,
            f"{len(text.splitlines())} lines",
        )

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

    parent = load_parent_runner()
    i3_value = float(parent.measure_I3(k=4.0))
    check("parent runner I_3 table value is <1e-10", i3_value < 1e-10, i3_value)
    check("parent note table exposes alpha approx column", "alpha approx" in note)
    for d in DIMS:
        row = parent.measure_gravity_2d_with_d_potential(d, k=6.0)
        beta_2dp = round(float(row["beta"]), 2)
        alpha_2dp = round(float(row["alpha"]), 2)
        attractive = bool(row["attractive"])
        table_fragment = (
            f"| {d} | {'yes' if EXPECTED_ATTRACTIVE[d] else 'no'} | "
            f"{EXPECTED_BETA_2DP[d]:.2f} | {EXPECTED_ALPHA_2DP[d]:.2f} | "
            "`<1e-10`"
        )
        check(
            f"d={d} parent runner attractive table entry matches",
            attractive == EXPECTED_ATTRACTIVE[d],
            attractive,
        )
        check(
            f"d={d} parent runner beta table entry matches",
            beta_2dp == EXPECTED_BETA_2DP[d],
            beta_2dp,
        )
        check(
            f"d={d} parent runner alpha table entry matches",
            alpha_2dp == EXPECTED_ALPHA_2DP[d],
            alpha_2dp,
        )
        check(f"d={d} source note table row matches replayed values", table_fragment in note)

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
