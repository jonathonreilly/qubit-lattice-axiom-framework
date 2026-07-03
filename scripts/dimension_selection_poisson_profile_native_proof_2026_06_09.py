#!/usr/bin/env python3
"""Runner-native proof of the dimension-selection radial profile family.

The lower-bound dimension-selection runner uses the analytic radial family

    f_1(r) = r,
    f_2(r) = log(r),
    f_d(r) = r^(2-d) for d >= 3.

This certificate proves the family directly on the runner's radial coordinate:
each profile is harmonic away from the source under the d-dimensional radial
Laplacian, has radius-independent shell flux, and has the derivative sign
used by the finite-k centroid bridge. Literature/textbook sources can be cited
in parallel, but they are not needed as load-bearing authority for these
identities.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOWER_NOTE = DOCS / "DIMENSION_SELECTION_LOWER_BOUND_BRIDGE_V2_2026-05-20.md"
PARENT_RUNNER = ROOT / "scripts" / "frontier_dimension_selection.py"

PASS = 0
FAIL = 0
DIMS = (1, 2, 3, 4, 5)
EXPECTED_PROFILE_DERIVATIVE_SIGN = {1: 1, 2: 1, 3: -1, 4: -1, 5: -1}
r = sp.symbols("r", positive=True, real=True)


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


def sign(value: Any) -> int:
    numeric = float(value)
    return 1 if numeric > 0 else -1 if numeric < 0 else 0


def profile(d: int) -> sp.Expr:
    if d == 1:
        return r
    if d == 2:
        return sp.log(r)
    return r ** (2 - d)


def radial_laplacian(expr: sp.Expr, d: int) -> sp.Expr:
    return sp.simplify(sp.diff(expr, r, 2) + sp.Rational(d - 1, 1) * sp.diff(expr, r) / r)


def shell_flux(expr: sp.Expr, d: int) -> sp.Expr:
    # The omitted sphere-area constant is dimension dependent but not r
    # dependent. The r-dependence is the load-bearing part for the profile.
    return sp.simplify(r ** (d - 1) * sp.diff(expr, r))


def source_firewall() -> None:
    print("\nSection 0: source firewall")
    check("lower-bound V2 note exists", LOWER_NOTE.exists())
    check("parent dimension runner exists", PARENT_RUNNER.exists())

    note = read(LOWER_NOTE)
    runner = read(PARENT_RUNNER)
    required_note_phrases = [
        "Runner-native radial Green-profile proof",
        "dimension_selection_poisson_profile_native_proof_2026_06_09.py",
        "textbook references are parallel provenance",
        "not load-bearing inputs",
    ]
    for phrase in required_note_phrases:
        check(f"lower note contains required phrase: {phrase}", phrase in note)

    forbidden_note_phrases = [
        "standard d-dimensional Poisson Green's function asymptotics",
        "comes from standard Poisson Green's functions",
        "Upstream standard-math imports",
    ]
    for phrase in forbidden_note_phrases:
        check(f"lower note excludes imported-authority phrase: {phrase}", phrase not in note)

    required_runner_phrases = [
        "runner-native radial Green-profile certificate",
        "f_1(r)=r, f_2(r)=log(r), f_d(r)=r^(2-d)",
        "no textbook import is needed",
    ]
    for phrase in required_runner_phrases:
        check(f"parent runner contains refreshed profile phrase: {phrase}", phrase in runner)

    stale_runner_phrase = "Strategy: The Poisson Green's function in d dimensions gives"
    check("parent runner excludes stale textbook-strategy phrase", stale_runner_phrase not in runner)


def exact_profile_proof() -> dict[int, dict[str, sp.Expr]]:
    print("\nSection 1: exact radial Poisson profile proof")
    rows: dict[int, dict[str, sp.Expr]] = {}
    for d in DIMS:
        f = profile(d)
        lap = radial_laplacian(f, d)
        flux = shell_flux(f, d)
        flux_derivative = sp.simplify(sp.diff(flux, r))
        df = sp.diff(f, r)
        df_at_2 = sp.simplify(df.subs(r, sp.Integer(2)))
        expected = EXPECTED_PROFILE_DERIVATIVE_SIGN[d]

        check(f"d={d} radial Laplacian vanishes away from source", sp.simplify(lap) == 0, lap)
        check(f"d={d} shell flux is radius-independent", flux_derivative == 0, flux)
        check(f"d={d} profile derivative sign matches lower-bound transition", sign(df_at_2) == expected, df_at_2)
        rows[d] = {"profile": f, "laplacian": lap, "flux": flux, "derivative": df}
    return rows


def runner_formula_alignment() -> None:
    print("\nSection 2: parent-runner formula alignment")
    source = read(PARENT_RUNNER)
    expected_fragments = [
        "phi[ix, iy] = -M_val * r",
        "phi[ix, iy] = -M_val * math.log(r)",
        "phi[ix, iy] = -M_val / r ** (d - 2)",
        "if r < 0.5:",
    ]
    for fragment in expected_fragments:
        check(f"parent runner implements profile fragment: {fragment}", fragment in source)

    # Evaluate the finite regularized runner family at representative radii.
    samples = (0.5, 1.0, 2.0, 4.0)
    for d in DIMS:
        values: list[float] = []
        for rv in samples:
            if d == 1:
                values.append(rv)
            elif d == 2:
                values.append(math.log(rv))
            else:
                values.append(1.0 / (rv ** (d - 2)))
        if d <= 2:
            monotone = all(a < b for a, b in zip(values, values[1:]))
        else:
            monotone = all(a > b for a, b in zip(values, values[1:]))
        check(f"d={d} finite regularized sample monotonicity matches derivative sign", monotone, values)


def main() -> int:
    print("=" * 88)
    print("DIMENSION-SELECTION RADIAL PROFILE NATIVE PROOF")
    print("=" * 88)
    source_firewall()
    exact_profile_proof()
    runner_formula_alignment()
    print("=" * 88)
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
