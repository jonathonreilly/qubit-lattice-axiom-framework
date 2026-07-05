#!/usr/bin/env python3
"""Verify the hydrogen impact discriminator for PR #4991 Tier-A retirement."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


AC_STATUS_INPUTS = {
    "OWNER_ADOPTION_PR4991",
    "AC_OCCUPANCY_GRAIN_PREMISE",
    "AC_RETA_H_UNIT_READOUT_LICENSE",
}

ELECTRON_READOUT_EXTRA_INPUTS = {
    "C3_SPECIES_BRIDGE_OWNER_RATIFIED",
    "ZERO_SOURCE_READOUT",
    "REAL_PRIMITIVE_BRANNEN_ENDPOINT",
    "BASED_DETERMINANT_LINE_READOUT",
}

ELECTRON_SCALE_INPUTS = {
    "ABSOLUTE_CHARGED_LEPTON_SCALE",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def closes_old_ac_tier_a_status(inputs: set[str]) -> bool:
    """#4991 closes the old AC Tier-A status only when all AC atoms are adopted."""
    return AC_STATUS_INPUTS <= inputs


def closes_retained_electron_mass(inputs: set[str]) -> bool:
    """Electron mass needs AC status, native readout bridge atoms, and scale."""
    return (
        closes_old_ac_tier_a_status(inputs)
        and ELECTRON_READOUT_EXTRA_INPUTS <= inputs
        and ELECTRON_SCALE_INPUTS <= inputs
    )


def closes_hydrogen(inputs: set[str]) -> bool:
    """Hydrogen additionally needs alpha/atomic bridge inputs."""
    return closes_retained_electron_mass(inputs) and {
        "RETAINED_ALPHA_ZERO",
        "RETAINED_ATOMIC_BRIDGE",
    } <= inputs


def require(condition: bool, label: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS {label}")
    else:
        print(f"FAIL {label}")
        failures.append(label)


def require_text(text: str, needle: str, failures: list[str]) -> None:
    text_compact = " ".join(text.split())
    needle_compact = " ".join(needle.split())
    require(
        needle in text or needle_compact in text_compact,
        f"note contains {needle!r}",
        failures,
    )


def main() -> int:
    failures: list[str] = []
    note = read(NOTE)
    tier_a = json.loads(read(TIER_A_REGISTRY))
    primitive_registry = read(PRIMITIVE_REGISTRY)

    required_phrases = [
        "Tier-A Owner-Retirement PR #4991 Impact Discriminator",
        "#4991",
        "owner-governed Tier-A retirement",
        "genuine_admitted_input_count = 0",
        "retired_derivation_targets",
        "owner_governed_premise_nodes.json",
        "AC_phi_lambda",
        "theta",
        "Owner-governed residual premises chain-satisfy without Tier-A bounding",
        "not theorem closure",
        "not an axiom",
        "not an approved primitive",
        "not an audit verdict",
        "ac_orbit_occupancy_statistical_grain_premise",
        "ac_reta_hclass_hunit_readout_premise",
        "theta_gauge_sector_phase_source_premise",
        "theta_mass_determinant_channel_w2_premise",
        "supplies no value of `r`, `delta`, charged-lepton mass",
        "above-C3 taste/Dirac/chirality content",
        "#5010 | CLEAN",
        "#5009 | CLEAN",
        "#5008 | CLEAN",
        "#5007 | CLEAN",
        "#4991 | CLEAN",
        "#4990 | CLEAN",
        "#4989 | CLEAN",
        "Current main has not adopted #4991",
        "The live current-main Tier-A registry still contains `AC_phi_lambda`",
        "K1 counting/occupancy",
        "K2 R-eta readout license",
        "K3 species bridge",
        "K4 absolute scale",
        "Z1 zero-source readout",
        "Z2 real-primitive Brannen endpoint",
        "Z3 based determinant-line readout",
        "F/L/P/R source-side selector",
        "`m_e = a_l^2 * rho_e(delta)`",
        "source-probe selector F/L/P/R must ratify `S_l = 1/256`",
        "Koide-native electron readout must close Z1/Z2/Z3 without imports",
        "physical electron mass must get an absolute scale",
        "`alpha(0)` must be derived or admitted by an approved retained primitive",
        "N1 alternative routes checked",
        "N2 wall-independence audit",
        "N3 hidden-wall scan",
        "N4 residual matching",
        "N5 rhetoric audit",
        "N6 partial-closure path",
        "N7 steelman",
        "N8 cross-cycle echo",
        "Non-Claims",
    ]
    for phrase in required_phrases:
        require_text(note, phrase, failures)

    forbidden_overclaims = [
        "hydrogen is derived",
        "retained hydrogen calculation is complete",
        "zero-import electron mass is derived",
        "AC_phi_lambda retained theorem",
        "theta retained theorem",
        "PR #4991 derives alpha",
        "PR #4991 derives hydrogen",
    ]
    for phrase in forbidden_overclaims:
        require(phrase not in note, f"note avoids overclaim {phrase!r}", failures)

    live_targets = tier_a.get("derivation_targets", {})
    require(
        any(target.get("label") == "AC_phi_lambda" for target in live_targets.values()),
        "current-main Tier-A registry still has AC_phi_lambda live before #4991 adoption",
        failures,
    )
    require(
        tier_a.get("genuine_admitted_input_count", 0) > 0,
        "current-main Tier-A registry is not already #4991-retired",
        failures,
    )
    require(
        "owner_governed_premise_nodes" not in primitive_registry,
        "primitive registry does not absorb owner-governed premise nodes",
        failures,
    )

    pr4991_inputs = {
        "OWNER_ADOPTION_PR4991",
        "AC_OCCUPANCY_GRAIN_PREMISE",
        "AC_RETA_H_UNIT_READOUT_LICENSE",
    }
    require(
        closes_old_ac_tier_a_status(pr4991_inputs),
        "#4991 inputs close old AC Tier-A status class",
        failures,
    )
    require(
        not closes_retained_electron_mass(pr4991_inputs),
        "#4991 inputs alone do not close retained electron mass",
        failures,
    )
    require(
        not closes_hydrogen(pr4991_inputs),
        "#4991 inputs alone do not close hydrogen",
        failures,
    )

    with_native_readout = pr4991_inputs | ELECTRON_READOUT_EXTRA_INPUTS
    require(
        not closes_retained_electron_mass(with_native_readout),
        "native readout without scale still does not close electron mass",
        failures,
    )
    with_scale = with_native_readout | ELECTRON_SCALE_INPUTS
    require(
        closes_retained_electron_mass(with_scale),
        "electron mass predicate requires AC status, native readout atoms, and scale",
        failures,
    )
    require(
        not closes_hydrogen(with_scale),
        "electron mass without alpha/atomic bridge still does not close hydrogen",
        failures,
    )

    print(f"SUMMARY failures={len(failures)}")
    if failures:
        for failure in failures:
            print(f"FAILED {failure}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
