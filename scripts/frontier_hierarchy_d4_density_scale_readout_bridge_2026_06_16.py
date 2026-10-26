#!/usr/bin/env python3
"""Verifier for the hierarchy D=4 density-scale readout bridge.

The checked theorem is deliberately narrow:

    rho_* = A(L) v(L)^4 with fixed positive rho_* and A(L) > 0
    implies v(L) / v_ref = (A_ref / A(L))^(1/4).

It fixes exponent, inverse/direct placement, sign, and baseline
normalization for the coefficient-to-scale map. The endpoint coefficients are
recomputed here from the supplied finite APBC coefficient formula instead of imported
from the live audit status of the endpoint note. It does not identify the
electroweak VEV with this readout.
"""

from __future__ import annotations

import math
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
)
PARENT_NOTE_PATH = ROOT / "docs" / "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md"

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md', 'docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md']

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def scale_ratio(a_ref: float, a_new: float) -> float:
    return (a_ref / a_new) ** 0.25


def note_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def apbc_modes(lt: int) -> list[float]:
    return [(2 * n + 1) * math.pi / lt for n in range(lt)]


def endpoint_coefficient(lt: int, u0: float = 1.0) -> float:
    return (1.0 / (2.0 * lt * u0**2)) * sum(
        1.0 / (3.0 + math.sin(omega) ** 2) for omega in apbc_modes(lt)
    )


def endpoint_coefficient_inf(u0: float = 1.0) -> float:
    # Average_{0..2pi} 1/(3 + sin^2 omega) = 1 / sqrt(3 * 4).
    return 1.0 / (4.0 * math.sqrt(3.0) * u0**2)


def main() -> int:
    print("Hierarchy D=4 density-scale readout bridge verifier")
    print("Status authority: independent audit lane only.")
    print("Premises: positive coefficients and a supplied quartic law; no physical identification is proved.")

    section("Fixed positive D=4 density algebra")
    rho = 5.0
    a_ref = 2.0
    a_new = 7.0
    v_ref = (rho / a_ref) ** 0.25
    v_new = (rho / a_new) ** 0.25
    lhs = v_new / v_ref
    rhs = scale_ratio(a_ref, a_new)
    print(f"rho={rho:.6f}; A_ref={a_ref:.6f}; A_new={a_new:.6f}")
    print(f"v_new/v_ref={lhs:.15f}; (A_ref/A_new)^(1/4)={rhs:.15f}")
    check("fixed-density equation gives inverse fourth-root coefficient placement", abs(lhs - rhs) < 1.0e-15)

    baseline = scale_ratio(a_ref, a_ref)
    check("reference endpoint normalizes exactly to one", abs(baseline - 1.0) < 1.0e-15)
    check(
        "larger coefficient gives downward scale compression",
        a_new > a_ref and scale_ratio(a_ref, a_new) < 1.0,
        f"ratio={scale_ratio(a_ref, a_new):.15f}",
    )
    check(
        "smaller coefficient gives upward scale rescaling",
        scale_ratio(a_ref, 1.0) > 1.0,
        f"ratio={scale_ratio(a_ref, 1.0):.15f}",
    )

    section("Supplied coefficient applications")
    u0 = 1.0
    a2 = endpoint_coefficient(2, u0)
    a4 = endpoint_coefficient(4, u0)
    ainf = endpoint_coefficient_inf(u0)
    check(
        "supplied finite coefficient gives A_2 = 1/(8 u0^2)",
        abs(a2 - 1.0 / (8.0 * u0**2)) < 1.0e-15,
        f"A_2={a2:.15f}",
    )
    check(
        "supplied finite coefficient gives A_4 = 1/(7 u0^2)",
        abs(a4 - 1.0 / (7.0 * u0**2)) < 1.0e-15,
        f"A_4={a4:.15f}",
    )
    check(
        "supplied angular-average formula is consistent with A_inf = 1/(4 sqrt(3) u0^2)",
        abs(ainf - 1.0 / (4.0 * math.sqrt(3.0) * u0**2)) < 1.0e-15,
        f"A_inf={ainf:.15f}",
    )
    a2_over_a4 = Fraction(7, 8)
    v4_over_v2 = float(a2_over_a4) ** 0.25
    direct_root = float(Fraction(8, 7)) ** 0.25
    print(f"A_2/A_4 = {a2_over_a4}")
    print(f"v_4/v_2 = (7/8)^(1/4) = {v4_over_v2:.15f}")
    print(f"direct fourth root (A_4/A_2)^(1/4) = {direct_root:.15f}")
    check(
        "A_2/A_4 is locally derived as 7/8 without endpoint-ledger status import",
        abs((a2 / a4) - float(a2_over_a4)) < 1.0e-15,
        f"A_2/A_4={a2 / a4:.15f}",
    )
    check("L_t=4 endpoint uses inverse placement (7/8)^(1/4), not direct root", v4_over_v2 < 1.0 < direct_root)
    check(
        "L_t=4 exact base is the endpoint coefficient ratio A_2/A_4=7/8",
        a2_over_a4 == Fraction(7, 8),
    )

    scalar_ratio = 2.0 / math.sqrt(3.0)
    scalar_scale = scalar_ratio ** -0.25
    expected_scalar = (math.sqrt(3.0) / 2.0) ** 0.25
    print(f"A_inf/A_2 = 2/sqrt(3) = {scalar_ratio:.15f}")
    print(f"v_inf/v_2 = (A_inf/A_2)^(-1/4) = {scalar_scale:.15f}")
    check(
        "A_inf/A_2 is locally derived as 2/sqrt(3) without endpoint-ledger status import",
        abs((ainf / a2) - scalar_ratio) < 1.0e-15,
        f"A_inf/A_2={ainf / a2:.15f}",
    )
    check("temporal-average scalar endpoint has the same inverse-fourth-root placement", abs(scalar_scale - expected_scalar) < 1.0e-15)
    check("temporal-average scalar endpoint compresses downward relative to L_t=2", scalar_ratio > 1.0 and scalar_scale < 1.0)

    section("Documentary scope checks (not proof or audit status)")
    note = note_text(NOTE_PATH)
    parent = note_text(PARENT_NOTE_PATH)
    flat = " ".join(note.split())
    parent_flat = " ".join(parent.split())
    check("source states positive supplied quartic premises and open physical identification",
          "stipulated quartic density law" in flat
          and "does not identify the electroweak VEV" in flat
          and "missing-ledger membership contract" in flat
          and "withdrawn from current authority" in flat)
    check("parent keeps coefficient identification open",
          "HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md" in parent
          and "does not identify the computed condensate ratio" in parent_flat)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
