#!/usr/bin/env python3
"""Exact negative boundary for the hierarchy fixed-density selector route.

The runner verifies that the D=4 fixed-density coefficient-to-scale map
determines endpoint ratios but cannot, by itself, select the physical endpoint
coefficient surface or absolute electroweak scale. It writes no audit result.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "HIERARCHY_FIXED_DENSITY_PHYSICAL_SELECTOR_NO_GO_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md"
BRIDGE = ROOT / "docs" / "HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
EW_BRIDGE = (
    ROOT
    / "docs"
    / "HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def flat(text: str) -> str:
    return " ".join(text.split())


def endpoint_coefficients(u0: float = 1.0) -> dict[str, float]:
    return {
        "A2": 1.0 / (8.0 * u0 * u0),
        "A4": 1.0 / (7.0 * u0 * u0),
        "Ainf": 1.0 / (4.0 * math.sqrt(3.0) * u0 * u0),
    }


def scale_for_fixed_density(rho_star: float, coefficient: float) -> float:
    return (rho_star / coefficient) ** 0.25


def main() -> None:
    print("Hierarchy fixed-density physical selector no-go")
    print("=" * 78)

    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    bridge_text = BRIDGE.read_text(encoding="utf-8")
    ew_bridge_text = EW_BRIDGE.read_text(encoding="utf-8")
    note_flat = flat(note_text)
    parent_flat = flat(parent_text)
    bridge_flat = flat(bridge_text)
    ew_bridge_flat = flat(ew_bridge_text)

    check("no-go note declares source-side negative route pruning", "**Claim type:** no_go / negative_route_pruning" in note_text)
    check("no-go note forbids new axiom/status/readout injection", "No new axiom, observed value, fitted selector, audit verdict, or physical VEV" in note_flat)
    check(
        "fixed-density bridge supplies map but not endpoint selection",
        "rho_* = A(L) v(L)^4" in bridge_text
        and "identifies the relevant `A(L)` surface" in bridge_flat,
    )
    check(
        "EW coordinate bridge supplies coordinate but leaves endpoint selection open",
        "EW order-parameter coordinate `v`" in ew_bridge_flat
        and "It does not close the endpoint-selection half" in ew_bridge_text
        and "does not derive the absolute EW scale" in ew_bridge_flat,
    )
    check(
        "parent note still names endpoint-selection residual as open",
        "endpoint-selection residual remains open" in parent_flat
        and "endpoint coefficient-to-physical-Higgs-density selection" in parent_flat,
    )

    coeffs = endpoint_coefficients()
    A2, A4, Ainf = coeffs["A2"], coeffs["A4"], coeffs["Ainf"]
    check("endpoint coefficients are positive", all(value > 0.0 for value in coeffs.values()), str(coeffs))
    check("A2/A4 endpoint ratio equals 7/8", abs((A2 / A4) - (7.0 / 8.0)) < 1e-14, f"A2/A4={A2/A4:.12f}")
    check("Ainf/A2 endpoint ratio equals 2/sqrt(3)", abs((Ainf / A2) - (2.0 / math.sqrt(3.0))) < 1e-14, f"Ainf/A2={Ainf/A2:.12f}")

    rho = 11.0
    scales = {name: scale_for_fixed_density(rho, coeff) for name, coeff in coeffs.items()}
    check(
        "fixed-density bridge reproduces v4/v2=(A2/A4)^(1/4)",
        abs((scales["A4"] / scales["A2"]) - ((A2 / A4) ** 0.25)) < 1e-14,
        f"v4/v2={scales['A4']/scales['A2']:.12f}",
    )
    check(
        "fixed-density bridge reproduces vinf/v2=(A2/Ainf)^(1/4)",
        abs((scales["Ainf"] / scales["A2"]) - ((A2 / Ainf) ** 0.25)) < 1e-14,
        f"vinf/v2={scales['Ainf']/scales['A2']:.12f}",
    )

    lam = 3.7
    scaled_rho = (lam**4) * rho
    scaled_scales = {name: scale_for_fixed_density(scaled_rho, coeff) for name, coeff in coeffs.items()}
    check(
        "absolute-density scaling rescales all v_i by lambda",
        all(abs(scaled_scales[name] / scales[name] - lam) < 1e-12 for name in coeffs),
        ", ".join(f"{name}:{scaled_scales[name]/scales[name]:.12f}" for name in coeffs),
    )
    check(
        "absolute-density scaling leaves all endpoint ratios unchanged",
        abs((scaled_scales["A4"] / scaled_scales["A2"]) - (scales["A4"] / scales["A2"])) < 1e-14
        and abs((scaled_scales["Ainf"] / scaled_scales["A2"]) - (scales["Ainf"] / scales["A2"])) < 1e-14,
    )

    selector_readouts = {}
    for selected_name, selected_coeff in coeffs.items():
        selected_scale = 1.0
        selected_rho = selected_coeff * selected_scale**4
        selector_readouts[selected_name] = {
            name: scale_for_fixed_density(selected_rho, coeff)
            for name, coeff in coeffs.items()
        }
    check(
        "each endpoint can be normalized as reference without violating fixed-density algebra",
        all(abs(readouts[name] - 1.0) < 1e-14 for name, readouts in selector_readouts.items()),
        ", ".join(f"{name}->v_ref={selector_readouts[name][name]:.1f}" for name in selector_readouts),
    )
    nonidentical_refs = {
        name: tuple(round(readouts[key], 12) for key in ("A2", "A4", "Ainf"))
        for name, readouts in selector_readouts.items()
    }
    check(
        "different endpoint references give distinct compatible readout triples",
        len(set(nonidentical_refs.values())) == 3,
        str(nonidentical_refs),
    )

    forbidden_numeric_selectors = ["C_obs", "246.22"]
    check(
        "no-go runner uses no observed electroweak target selector",
        all(token not in note_text for token in forbidden_numeric_selectors)
        and all(token not in __doc__ for token in forbidden_numeric_selectors)
        and "Fitting to `v_obs`, PDG data" in note_flat
        and "explicitly forbids" in note_flat,
    )
    check(
        "no-go note preserves future positive physical-selector routes",
        "does not prune future positive routes" in note_flat
        and "independent physical selector theorem" in note_flat,
    )
    check(
        "no-go note targets the exact hierarchy audit blocker",
        "hierarchy endpoint coefficient surface and absolute scale are still not selected" in note_flat
        and "physical Higgs density surface or fix the absolute electroweak scale" in note_flat,
    )
    check(
        "no-go discipline N1-N8 gate is visible",
        "## No-Go Discipline Gate" in note_text
        and "N1, alternative routes tested" in note_text
        and "N8, cross-cycle echo" in note_text,
    )

    print(f"\nSUMMARY: HIERARCHY FIXED-DENSITY SELECTOR NO-GO PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
