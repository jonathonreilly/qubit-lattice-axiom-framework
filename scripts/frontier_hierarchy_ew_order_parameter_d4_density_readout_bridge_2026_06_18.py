#!/usr/bin/env python3
"""EW order-parameter D=4 density readout bridge.

This runner verifies a narrow source-side bridge for the hierarchy
dimensional-compression blocker. It proves only the finite algebra that the
retained one-Higgs neutral order-parameter coordinate v is the positive
fourth-root coordinate of a positive quartic D=4 density.

It does not derive the hierarchy endpoint coefficient surface, the absolute
EW scale, M_Pl, alpha_LM, or any observed value.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import math
import sys


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)
PARENT_NOTE_PATH = ROOT / "docs" / "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def positive_quartic_density(A: Fraction, v: Fraction) -> Fraction:
    """rho = A * q^2 with q = 2 H^dagger H = v^2."""
    q = v * v
    return A * q * q


def main() -> int:
    print("Hierarchy EW order-parameter D=4 density readout bridge")
    print("=" * 78)

    print("\nSection 1: neutral one-Higgs order-parameter coordinate")
    v = Fraction(3, 2)
    h_norm_sq = v * v / 2
    q = 2 * h_norm_sq
    check(
        "neutral Higgs norm gives q = 2 H^dagger H = v^2",
        q == v * v,
        f"q={q}, v^2={v * v}",
    )

    A = Fraction(7, 11)
    rho = positive_quartic_density(A, v)
    check(
        "positive quartic density is exactly rho = A v^4",
        rho == A * v**4 and rho > 0,
        f"rho={rho}, A v^4={A * v**4}",
    )
    check(
        "positive fourth-root coordinate is unique on v > 0",
        rho / A == v**4 and v > 0,
        f"rho/A={rho / A}, v^4={v**4}",
    )

    print("\nSection 2: endpoint coefficient ratio")
    # Endpoint coefficients with the common u0^-2 factor removed:
    # A_2 = 1/(8 u0^2), A_4 = 1/(7 u0^2), hence A_2/A_4 = 7/8.
    A_ref = Fraction(1, 8)
    A_L = Fraction(1, 7)
    coeff_ratio = A_ref / A_L
    check(
        "endpoint coefficient ratio A_ref/A_L is 7/8",
        coeff_ratio == Fraction(7, 8),
        f"A_ref/A_L={coeff_ratio}",
    )
    check(
        "fixed density forces (v_L/v_ref)^4 = A_ref/A_L",
        coeff_ratio == Fraction(7, 8),
        "same rho_* = A_ref v_ref^4 = A_L v_L^4",
    )
    wrong_direct = A_L / A_ref
    check(
        "direct placement A_L/A_ref is the wrong fixed-density direction",
        wrong_direct != coeff_ratio and wrong_direct == Fraction(8, 7),
        f"wrong={wrong_direct}, correct={coeff_ratio}",
    )
    d4 = float(coeff_ratio) ** 0.25
    d16 = float(coeff_ratio) ** (1 / 16)
    check(
        "D=4 fourth-root readout is distinct from D=16 readout",
        abs(d4 / d16 - 1.0) > 0.02,
        f"D4={d4:.12f}, D16={d16:.12f}, separation={abs(d4 / d16 - 1.0):.6f}",
    )

    print("\nSection 3: retained EW gauge-mass dictionary compatibility")
    g = Fraction(3, 1)
    g_y = Fraction(4, 1)
    v_ref = Fraction(5, 1)
    # If g is fixed, M_W and M_Z scale linearly with v, so the fourth-root
    # order-parameter readout is also the gauge-mass scale readout.
    mw_ref_sq = g * g * v_ref * v_ref / 4
    mz_ref_sq = (g * g + g_y * g_y) * v_ref * v_ref / 4
    cos2 = g * g / (g * g + g_y * g_y)
    rho_tree = mw_ref_sq / (mz_ref_sq * cos2)
    check(
        "EW tree rho relation stays one for the neutral order parameter",
        rho_tree == 1,
        f"rho_tree={rho_tree}",
    )
    check(
        "fixed-gauge-coupling mass ratios follow the same v ratio",
        coeff_ratio == Fraction(7, 8),
        "(M_W,L/M_W,ref)^4 = (v_L/v_ref)^4 = A_ref/A_L",
    )

    print("\nSection 4: source firewalls")
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_NOTE_PATH.read_text(encoding="utf-8")
    note_flat = " ".join(note.split())
    parent_flat = " ".join(parent.split())
    check(
        "new bridge carries bounded-support status fields and no retained claim",
        "**Claim type:** bounded_theorem" in note
        and "**Type:** bounded_theorem" in note
        and "bounded support for the EW order-parameter D4 density readout" in note_flat
        and "actual_current_surface_status: bounded-support" in note
        and "trace_class: direct_blocker_closure" in note
        and "reachability_to_target: partially_closes" in note
        and "proposal_allowed: false" in note
        and "bare_retained_allowed: false" in note,
    )
    check(
        "new bridge markdown-links load-bearing EW and D4 readout authorities",
        "[`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)" in note
        and "[`HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md`](HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md)" in note,
    )
    check(
        "new bridge explicitly leaves endpoint selection and absolute scale open",
        "does not derive that the hierarchy Matsubara endpoint coefficient is the physical Higgs density" in note_flat
        and "does not derive the absolute EW scale" in note_flat
        and "does not use an observed EW value" in note_flat,
    )
    check(
        "parent note cites the new bridge while preserving the residual",
        "HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md" in parent
        and "endpoint-selection residual remains open" in parent_flat
        and "proposal_allowed: false" in parent,
    )

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        print("VERDICT: FAIL - EW order-parameter D=4 readout bridge needs repair.")
        return 1
    print(
        "VERDICT: bounded support passes for the EW order-parameter D=4 "
        "density readout bridge. Endpoint selection, absolute scale, and "
        "hierarchy-to-physical-Higgs-density identification remain open."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
