#!/usr/bin/env python3
"""Finite scalar examples of a restricted quartic-law non-identification result.

Positive numerical density fixes the scales. Only unspecified density permits
rescaling; an endpoint tag absent from these equations is not determined by them.
No physical-selector impossibility or route-exhaustion claim is established.
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

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ['docs/HIERARCHY_FIXED_DENSITY_PHYSICAL_SELECTOR_NO_GO_NOTE_2026-06-18.md', 'docs/HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md', 'docs/HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md', 'docs/HIERARCHY_EW_ORDER_PARAMETER_D4_DENSITY_READOUT_BRIDGE_BOUNDED_SUPPORT_NOTE_2026-06-18.md']

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
    print("Restricted fixed-density scalar-law examples")
    print("=" * 78)

    note_text = NOTE.read_text(encoding="utf-8")
    parent_text = PARENT.read_text(encoding="utf-8")
    bridge_text = BRIDGE.read_text(encoding="utf-8")
    ew_bridge_text = EW_BRIDGE.read_text(encoding="utf-8")
    note_flat = flat(note_text)
    parent_flat = flat(parent_text)
    bridge_flat = flat(bridge_text)
    ew_bridge_flat = flat(ew_bridge_text)

    check("documentary boundary states restricted algebra and missing physical no-go",
          "restricted algebraic non-identification" in note_flat
          and "physical no-go unestablished" in note_flat)
    check("source distinguishes specified density from a free density parameter",
          "specified numerical" in note_flat
          and "different** densities" in note_flat
          and "not multiple solutions" in note_flat)
    check("coefficient bridge supplies quartic premises, not physical identification",
          "stipulated quartic density law" in bridge_flat
          and "does not identify the electroweak VEV" in bridge_flat)
    check("EW bridge leaves the physical interpretation open",
          "does not derive the absolute EW scale" in ew_bridge_flat
          and "does not derive that the hierarchy Matsubara endpoint coefficient is the physical Higgs density" in ew_bridge_flat)
    check("parent retains open coefficient identification",
          "does not identify the computed condensate ratio" in parent_flat
          and "endpoint-selection residual remains open" in parent_flat)

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

    check("documentary boundary excludes an observed target or replacement ledger",
          "No observed EW target" in note_flat
          and "replacement ledger" in note_flat)
    check("source preserves future positive physical-selector routes",
          "does not prune future positive routes" in note_flat
          and "independent selector relation remains a positive route" in note_flat)
    check("normalization examples explicitly change density",
          "changes `rho`" in note_flat and "different** densities" in note_flat)
    check("N1-N8 limitations are visible without a route-exhaustion PASS claim",
          "## No-Go Discipline Gate" in note_text
          and "N1, alternative routes tested" in note_text
          and "N8, cross-cycle echo" in note_text
          and "physical no-go packet remains incomplete" in note_flat)

    # Unscored granularity inventory; no pseudo-PASS for unexecuted resolutions.
    print("per_element: checked and not executed — no matrix-element carrier is instantiated; only supplied scalar coefficient equations are evaluated.")
    print("per_site: checked and not executed — fixtures contain no site-indexed fields or site-wise dynamics; no site obstruction is claimed.")
    print("per_mode: checked and not executed — Ainf is a supplied angular-average formula, not an executed spectrum or momentum-mode limit.")
    print("lattice_wide: checked and not executed — no lattice-size sequence or infinite-volume limit is computed; broader physical selector exclusion remains unproved.")
    print(f"per_block: supplied A2={A2:.12f}, A4={A4:.12f}; ratio={A2/A4:.12f}.")
    print(f"angular-average formula: Ainf={Ainf:.12f}; no lattice or continuum executed.")
    print(f"reference normalization yields {len(set(nonidentical_refs.values()))} triples at different densities.")
    print("Physical selector routes are not exhausted; the broader no-go packet is incomplete.")

    print(f"\nSUMMARY: RESTRICTED QUARTIC-LAW CHECKS PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
