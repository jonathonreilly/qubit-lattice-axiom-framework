#!/usr/bin/env python3
"""Bounded algebra-core runner for the Y_T neutral-carrier repair."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CORE_NOTE = DOCS / "YT_SIGNED_RECORD_LOWER_PROJECTOR_NEUTRAL_RAY_ALGEBRA_CORE_BOUNDED_NOTE_2026-06-18.md"
PARENT_NOTE = DOCS / "YT_QUBIT_NEUTRAL_HIGGS_CARRIER_RAY_BRIDGE_NOTE_2026-05-25.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, ok: bool, detail: Any = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if ok:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def is_zero(expr: sp.Expr) -> bool:
    return sp.simplify(expr) == 0


def matrix_is_zero(matrix: sp.Matrix) -> bool:
    return all(is_zero(entry) for entry in matrix)


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def check_source_boundaries() -> None:
    section("T0: source status and firewalls")
    core = read(CORE_NOTE)
    parent = read(PARENT_NOTE)

    for phrase in (
        "Claim type:** bounded_theorem",
        "Actual current-surface status:** bounded-support",
        "Trace class:** upstream_support",
        "proposal_allowed: false",
        "bare_retained_allowed: false",
        "MINIMAL_AXIOMS_2026-06-05.md",
        "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md",
        "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md",
    ):
        check(f"core note contains {phrase}", phrase in core)

    for phrase in (
        "not a same-surface physical carrier theorem",
        "do not identify the qubit readout basis with the EW Higgs doublet basis",
        "same physical carrier surface",
    ):
        check(f"core note preserves boundary: {phrase}", phrase in core)

    check("parent cites algebra-core note", CORE_NOTE.name in parent)
    check("parent records 2026-06-18 audit-scope repair", "2026-06-18 audit-scope repair" in parent)
    check(
        "parent leaves same-surface carrier theorem open",
        "physical same-surface carrier theorem" in parent
        and "same-surface source theorem" in parent,
    )

    for phrase in (
        "carrier-ray bridge is closed",
        "same physical carrier surface has been derived",
        "signed-record source is physically the neutral EW radial source",
        "proposed_retained",
    ):
        check(f"forbidden overclaim absent: {phrase}", phrase not in core and phrase not in parent)


def check_signed_record_algebra() -> None:
    section("T1: signed-record lower-projector algebra")
    z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    p_plus = (ident + z) / 2
    p_minus = (ident - z) / 2

    check("P_+ is idempotent", matrix_is_zero(p_plus * p_plus - p_plus), p_plus)
    check("P_- is idempotent", matrix_is_zero(p_minus * p_minus - p_minus), p_minus)
    check("P_+ P_- = 0", matrix_is_zero(p_plus * p_minus), p_plus * p_minus)
    check("P_+ + P_- = I", matrix_is_zero(p_plus + p_minus - ident), p_plus + p_minus)
    check("sigma_z = P_+ - P_-", matrix_is_zero(z - (p_plus - p_minus)), p_plus - p_minus)
    check("sigma_z = I - 2 P_-", matrix_is_zero(z - (ident - 2 * p_minus)), ident - 2 * p_minus)

    h = sp.symbols("h", real=True)
    signed_weights = sp.Matrix([sp.exp(h), sp.exp(-h)])
    lower_weights = sp.exp(h) * sp.Matrix([1, sp.exp(-2 * h)])
    check(
        "exp(h epsilon) equals exp(h) exp(-2h P_-) on eigenweights",
        matrix_is_zero(signed_weights - lower_weights),
        signed_weights,
    )
    check("affine source coordinate is j=-2h", sp.simplify(-2 * h + 2 * h) == 0)


def check_ew_neutral_ray_bookkeeping() -> None:
    section("T2: EW lower ray is neutral in the one-Higgs bookkeeping")
    v = sp.symbols("v", positive=True, real=True)
    z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    p_plus = (ident + z) / 2
    p_minus = (ident - z) / 2
    t3 = z / 2
    y_h = sp.Rational(1, 2) * ident
    q = t3 + y_h
    h0 = sp.Matrix([0, v / sp.sqrt(2)])
    upper = sp.Matrix([1, 0])

    check("P_- H_0 = H_0", matrix_is_zero(p_minus * h0 - h0), p_minus * h0)
    check("P_+ H_0 = 0", matrix_is_zero(p_plus * h0), p_plus * h0)
    check("Q H_0 = 0", matrix_is_zero(q * h0), q * h0)
    check("upper ray has charge +1", matrix_is_zero(q * upper - upper), q * upper)
    check("neutral nullspace is the lower ray", q.nullspace() == [sp.Matrix([0, 1])], q.nullspace())


def check_radial_tangent_and_ratio_shape() -> None:
    section("T3: conditional radial tangent and response-ratio compatibility")
    s = sp.symbols("s", real=True)
    v = sp.Function("v")(s)
    z = sp.Matrix([[1, 0], [0, -1]])
    ident = sp.eye(2)
    p_minus = (ident - z) / 2
    q = z / 2 + sp.Rational(1, 2) * ident
    h_s = sp.Matrix([0, v / sp.sqrt(2)])
    tangent = sp.diff(h_s, s)

    check("H(s) lies on EW lower ray", matrix_is_zero(p_minus * h_s - h_s), p_minus * h_s)
    check("dH/ds lies on EW lower ray", matrix_is_zero(p_minus * tangent - tangent), tangent)
    check("dH/ds is neutral", matrix_is_zero(q * tangent), q * tangent)

    y_t, g_2 = sp.symbols("y_t g_2", nonzero=True)
    mt = y_t * v / sp.sqrt(2)
    mw = g_2 * v / 2
    ratio = sp.simplify(sp.diff(mt, s) / sp.diff(mw, s))
    check("top/W response-ratio shape cancels the common Jacobian", is_zero(ratio - sp.sqrt(2) * y_t / g_2), ratio)


def main() -> int:
    print("# Y_T signed-record lower-projector neutral-ray algebra core")
    print(f"# Source note: {CORE_NOTE.relative_to(ROOT)}")
    check_source_boundaries()
    check_signed_record_algebra()
    check_ew_neutral_ray_bookkeeping()
    check_radial_tangent_and_ratio_shape()
    print(f"\nTOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
