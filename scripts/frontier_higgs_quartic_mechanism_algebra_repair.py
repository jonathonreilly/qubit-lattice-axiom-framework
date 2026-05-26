#!/usr/bin/env python3
"""Formal quartic-potential algebra repair runner for the Higgs mechanism row."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
NOTE_PATH = ROOT / "docs" / "HIGGS_MECHANISM_NOTE.md"
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
CLAIM_ID = "higgs_mechanism_note"
RUNNER_PATH = "scripts/frontier_higgs_quartic_mechanism_algebra_repair.py"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if ok else "FAIL"
    suffix = f" ({detail})" if detail else ""
    print(f"  [{status}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def check_note_boundary() -> None:
    section("Source-note boundary")
    text = NOTE_PATH.read_text()
    normalized = " ".join(text.split())
    required = [
        "bounded-support formal scalar-potential algebra",
        "That formal quartic-potential mechanism is the entire repaired theorem.",
        "This repair does not supply that missing physical bridge.",
        "The physical bridge from this formal quartic-potential algebra to a framework-native Higgs mechanism remains a separate open science problem.",
    ]
    for needle in required:
        check(f"note contains required boundary: {needle!r}", needle in normalized)

    forbidden = [
        "Higgs mechanism is derived from Cl(3)/Z^3",
        "Coleman-Weinberg effective potential is derived from the framework",
        "physical Higgs mass is predicted",
        "lambda(M_Pl) is derived",
        "bare-parameter substrate is derived",
    ]
    for needle in forbidden:
        check(f"note avoids overclaim phrase: {needle!r}", needle not in normalized)


def check_symbolic_quartic_algebra() -> None:
    section("Symbolic quartic algebra")
    r, m2, lam = sp.symbols("r m2 lambda", positive=True)
    # Use mu2 > 0 for the broken case m2 = -mu2.
    mu2 = sp.symbols("mu2", positive=True)
    v2 = mu2 / lam
    v = sp.sqrt(v2)
    potential = sp.Rational(1, 2) * (-mu2) * r**2 + sp.Rational(1, 4) * lam * r**4
    d1 = sp.diff(potential, r)
    d2 = sp.diff(potential, r, 2)
    check("stationary derivative factorizes as r(-mu2 + lambda r^2)", sp.factor(d1) == r * (-mu2 + lam * r**2))
    check("broken radius solves stationarity", sp.simplify(d1.subs(r, v)) == 0)
    v_value = sp.simplify(potential.subs(r, v))
    check("broken minimum value is -mu2^2/(4 lambda)", v_value == -mu2**2 / (4 * lam), str(v_value))
    curvature = sp.simplify(d2.subs(r, v))
    check("radial curvature at broken radius is 2 mu2", curvature == 2 * mu2, str(curvature))
    check("curvature equals 2 lambda v^2", sp.simplify(curvature - 2 * lam * v2) == 0)

    unbroken_potential = sp.Rational(1, 2) * m2 * r**2 + sp.Rational(1, 4) * lam * r**4
    check("unbroken potential has zero value at origin", unbroken_potential.subs(r, 0) == 0)
    check("unbroken potential derivative vanishes at origin", sp.diff(unbroken_potential, r).subs(r, 0) == 0)
    check("unbroken curvature at origin is m2", sp.diff(unbroken_potential, r, 2).subs(r, 0) == m2)


def check_numeric_global_minima() -> None:
    section("Numeric global-minimum samples")
    samples = [
        (1.0, -0.25),
        (0.75, -1.5),
        (2.0, -3.0),
        (0.5, 0.0),
        (1.5, 0.4),
    ]
    for lam, m2 in samples:
        xs = [i / 100.0 for i in range(0, 801)]
        vals = [0.5 * m2 * x * x + 0.25 * lam * x**4 for x in xs]
        idx = min(range(len(vals)), key=vals.__getitem__)
        grid_min = xs[idx]
        if m2 < 0:
            expected = math.sqrt(-m2 / lam)
            check(
                f"lambda={lam:g}, m2={m2:g}: minimum near broken radius",
                abs(grid_min - expected) < 0.01,
                f"grid_min={grid_min:.3f} expected={expected:.3f}",
            )
            check(
                f"lambda={lam:g}, m2={m2:g}: broken value below origin",
                vals[idx] < 0.0,
                f"Vmin={vals[idx]:.6f}",
            )
        else:
            check(
                f"lambda={lam:g}, m2={m2:g}: minimum at origin",
                grid_min == 0.0,
                f"grid_min={grid_min:.3f}",
            )
            check(
                f"lambda={lam:g}, m2={m2:g}: minimum value equals origin",
                abs(vals[idx]) < 1e-12,
                f"Vmin={vals[idx]:.6f}",
            )


def check_negative_controls() -> None:
    section("Negative controls")
    xs = [i / 100.0 for i in range(0, 1001)]
    unstable_vals = [0.5 * (-1.0) * x * x + 0.25 * (-0.5) * x**4 for x in xs]
    check("lambda < 0 sample is unbounded along larger radius", unstable_vals[-1] < unstable_vals[100], f"V(10)={unstable_vals[-1]:.3f}")

    no_break_vals = [0.5 * 0.7 * x * x + 0.25 * 1.0 * x**4 for x in xs]
    idx = min(range(len(no_break_vals)), key=no_break_vals.__getitem__)
    check("m2 > 0 sample has no nonzero broken minimum", xs[idx] == 0.0, f"argmin={xs[idx]:.3f}")


def check_audit_metadata_after_pipeline() -> None:
    section("Audit metadata after pipeline regeneration")
    if not LEDGER_PATH.exists():
        check("audit ledger exists", False, str(LEDGER_PATH))
        return
    ledger = json.loads(LEDGER_PATH.read_text())
    row = ledger.get("rows", {}).get(CLAIM_ID)
    check(f"{CLAIM_ID} row exists", row is not None)
    if row is None:
        return
    check("claim_type is bounded_theorem", row.get("claim_type") == "bounded_theorem", str(row.get("claim_type")))
    check("audit_status reset to unaudited", row.get("audit_status") == "unaudited", str(row.get("audit_status")))
    check("effective_status reset to unaudited", row.get("effective_status") == "unaudited", str(row.get("effective_status")))
    check("runner path is formal quartic repair runner", row.get("runner_path") == RUNNER_PATH, str(row.get("runner_path")))
    check("direct deps are empty for formal quartic theorem", row.get("deps") == [], str(row.get("deps")))
    check("open dependency paths are empty", row.get("open_dependency_paths") == [], str(row.get("open_dependency_paths")))


def main() -> int:
    print("Higgs formal quartic mechanism algebra repair")
    check_note_boundary()
    check_symbolic_quartic_algebra()
    check_numeric_global_minima()
    check_negative_controls()
    check_audit_metadata_after_pipeline()
    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
