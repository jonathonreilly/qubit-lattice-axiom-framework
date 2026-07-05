#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide native zero-section #5007 discriminator.

This is a support runner. It verifies that the #5007 route-guard repair is kept
separate from a retained physical electron-mass readout.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
SOURCE_DECISION_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ROUTE_TRIAGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
GOAL_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
A3_DISCRIMINATOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
KOIDE_ROUTE_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_CLOSURE_ROUTE_NOTE_2026-04-24.md"
KOIDE_ROUTE_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_closure_route.py"
KOIDE_REVIEW_NOTE = ROOT / "docs" / "KOIDE_NATIVE_ZERO_SECTION_NATURE_REVIEW_NOTE_2026-04-24.md"
KOIDE_REVIEW_RUNNER = ROOT / "scripts" / "frontier_koide_native_zero_section_nature_review.py"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
SCALE_PRIMITIVE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_PRIMITIVE = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED_PRIMITIVE = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


class Audit:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            prefix = "PASS"
        else:
            self.fail_count += 1
            prefix = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{prefix}: {label}{suffix}")

    def summary(self) -> None:
        print(f"\nSUMMARY: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def brannen_root_ratio(k: int, delta: float) -> float:
    return 1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * k / 3.0)


def root_ratios(delta: float) -> list[float]:
    return [brannen_root_ratio(k, delta) for k in range(3)]


def koide_q(delta: float) -> float:
    xs = root_ratios(delta)
    return sum(x * x for x in xs) / (sum(xs) ** 2)


def electron_factor(delta: float) -> float:
    return min(x * x for x in root_ratios(delta))


NATIVE_ROUTE_BRIDGES = {
    "ZERO_SOURCE_READOUT",
    "REAL_PRIMITIVE_BRANNEN_ENDPOINT",
    "BASED_DETERMINANT_LINE_READOUT",
}

PHYSICAL_ELECTRON_INPUTS = NATIVE_ROUTE_BRIDGES | {
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE",
    "SCALE_SUPPLIED",
}


def closes_native_route_bridge(inputs: set[str]) -> bool:
    return NATIVE_ROUTE_BRIDGES <= inputs


def closes_physical_electron_readout(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        KOIDE_FIREWALL,
        SOURCE_DECISION_PACKET,
        ROUTE_TRIAGE,
        GOAL_PACKET,
        A3_DISCRIMINATOR,
        KOIDE_ROUTE_NOTE,
        KOIDE_ROUTE_RUNNER,
        KOIDE_REVIEW_NOTE,
        KOIDE_REVIEW_RUNNER,
        PRIMITIVE_REGISTRY,
        TIER_A_REGISTRY,
        SCALE_PRIMITIVE,
        KINETIC_PRIMITIVE,
        REALIZED_PRIMITIVE,
        MINIMAL_AXIOMS,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = " ".join(note.split())
    koide_firewall = read(KOIDE_FIREWALL)
    koide_route_note = read(KOIDE_ROUTE_NOTE)
    koide_route_runner = read(KOIDE_ROUTE_RUNNER)
    primitive_registry = read(PRIMITIVE_REGISTRY)
    primitive_sources = "\n".join(
        [
            primitive_registry,
            read(SCALE_PRIMITIVE),
            read(KINETIC_PRIMITIVE),
            read(REALIZED_PRIMITIVE),
            read(MINIMAL_AXIOMS),
        ]
    )
    tier_a_registry = read(TIER_A_REGISTRY)

    section("Required note content")
    required_phrases = [
        "Zero-Import Hydrogen: Koide Native Zero-Section PR5007 Impact Discriminator",
        "#5007",
        "source-preserving repair",
        "PASSED: 7/12",
        "PASSED: 12/12",
        "PASSED: 18/18",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
        "not a retained electron readout",
        "zero-source readout",
        "real-primitive Brannen endpoint",
        "based determinant-line readout",
        "physical electron species bridge",
        "absolute charged-lepton scale",
        "m_e = a_l^2 * rho_e(delta)",
        "rho_e(delta) = min_k [1 + sqrt(2) cos(delta + 2 pi k / 3)]^2",
        "Q = sum_k m_k / (sum_k sqrt(m_k))^2 = 2/3",
        "`#5010` | `CLEAN`",
        "`#5009` | `CLEAN`",
        "`#5008` | `CLEAN`",
        "`#5007` | `CLEAN`",
        "`#5006` | `CLEAN`",
        "`#5005` | `CLEAN`",
        "Merge-state labels are moving review metadata",
        "Keep Lane 6 source-side work primary",
        "Promote Koide native zero-section follow-up",
        "Do not spend `#5007` as `m_e`",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed `#5007` hydrogen-impact discriminator passes",
    ]
    for phrase in required_phrases:
        audit.check(f"required note phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Koide source-boundary checks")
    for phrase in [
        "physical Koide closure",
        "No physical charged-lepton zero-source readout is derived.",
        "No physical Brannen endpoint identification is derived.",
        "No physical determinant-line based readout is derived.",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
    ]:
        audit.check(f"route note preserves boundary: {phrase}", phrase in koide_route_note)

    for phrase in [
        "Need physical proof of zero-source readout, real-primitive Brannen endpoint, and unit-preserving determinant-line readout.",
        "No physical Brannen endpoint, determinant-line unit, or charged-lepton zero-source identification is derived here.",
        "KOIDE_NATIVE_ZERO_SECTION_DEFINED_ROUTE_ALGEBRA=TRUE",
    ]:
        audit.check(f"route runner preserves boundary: {phrase}", phrase in koide_route_runner)

    for phrase in [
        "K1 | Counting-measure bit",
        "K2 | Radian/readout identification",
        "K3 | Species/electron branch",
        "K4 | Absolute scale",
        "Q=2/3` is a shape-surface condition, not yet an electron eigenvalue",
    ]:
        audit.check(f"hydrogen Koide firewall boundary present: {phrase}", phrase in koide_firewall)

    section("Closure predicate checks")
    audit.check(
        "Z1-Z3 exactly close the native route bridge predicate",
        closes_native_route_bridge(set(NATIVE_ROUTE_BRIDGES)),
    )
    for missing in sorted(NATIVE_ROUTE_BRIDGES):
        reduced = set(NATIVE_ROUTE_BRIDGES)
        reduced.remove(missing)
        audit.check(
            f"native route bridge fails without {missing}",
            not closes_native_route_bridge(reduced),
        )
    audit.check(
        "Z1-Z3 alone do not close physical electron readout",
        not closes_physical_electron_readout(set(NATIVE_ROUTE_BRIDGES)),
    )
    audit.check(
        "all Z1-Z3/K3/K4 inputs close physical electron readout predicate",
        closes_physical_electron_readout(set(PHYSICAL_ELECTRON_INPUTS)),
    )
    for missing in sorted(PHYSICAL_ELECTRON_INPUTS):
        reduced = set(PHYSICAL_ELECTRON_INPUTS)
        reduced.remove(missing)
        audit.check(
            f"physical electron readout fails without {missing}",
            not closes_physical_electron_readout(reduced),
        )

    section("Phase-blind arithmetic")
    delta = 2.0 / 9.0
    rho_delta = electron_factor(delta)
    rho_zero = electron_factor(0.0)
    audit.check("Q remains 2/3 at delta=2/9", abs(koide_q(delta) - 2.0 / 3.0) < 1e-14)
    audit.check("Q remains 2/3 at delta=0", abs(koide_q(0.0) - 2.0 / 3.0) < 1e-14)
    audit.check(
        "delta=2/9 electron factor matches comparator band",
        0.00162 < rho_delta < 0.00164,
        f"rho={rho_delta:.15f}",
    )
    audit.check(
        "delta=0 keeps same Q with more than 50x electron-like factor",
        rho_zero / rho_delta > 50.0,
        f"ratio={rho_zero / rho_delta:.2f}",
    )

    section("Registry boundary")
    for primitive in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"primitive registry names {primitive}", primitive in primitive_registry)
    audit.check("AC_phi_lambda remains a Tier-A registry row", "AC_phi_lambda" in tier_a_registry)
    audit.check("AC_phi_lambda is not a primitive registry node", "AC_phi_lambda" not in primitive_registry)
    for phrase in [
        "dimensionless quantity",
        "selector",
        "readout bridge",
        "normalization rule",
        "empirical fit",
    ]:
        audit.check(f"primitive source boundary excludes automatic {phrase}", phrase in primitive_sources)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `m_e`.",
        "No derivation that `#5007` is retained or merged.",
        "No retirement of `AC_phi_lambda`.",
        "No derivation of zero-source readout, real-primitive Brannen endpoint, or",
        "No derivation of the physical electron species bridge.",
        "No derivation of `a_l^2`, `S_l`, `C_A3`, `alpha(0)`, or hydrogen spectroscopy.",
        "No new axiom, primitive, or admitted import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `m_e`",
        "This note derives hydrogen",
        "#5007 derives the electron mass",
        "#5007 closes hydrogen",
        "zero-source readout is derived",
        "real-primitive Brannen endpoint is derived",
        "based determinant-line readout is derived",
        "physical electron species bridge is derived",
        "S_l is retained",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
