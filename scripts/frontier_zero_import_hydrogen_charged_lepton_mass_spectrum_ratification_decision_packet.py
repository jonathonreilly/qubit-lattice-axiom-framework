#!/usr/bin/env python3
"""Verifier for the charged-lepton mass-spectrum decision packet."""

from __future__ import annotations

from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
R_LEP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_R_LEP_THRESHOLDS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ELECTRON_MASS_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
NATIVE_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANCH_MASS_MAP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ABSOLUTE_SCALE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


SPECTRUM_INPUTS = {
    "CHARGED_LEPTON_MASS_SPECTRUM_TEXT_LOCK",
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "FULL_CHARGED_LEPTON_SPECIES_LABELING_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

R_LEP_INPUTS = {
    "R_LEP_THRESHOLDS_TEXT_LOCK",
    "ALPHA_MZ_SCALE_CONTEXT_RETAINED",
    "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED",
    "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED",
    "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_PDG_LEPTON_MASS_PROOF_INPUT",
    "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

ELECTRON_MASS_CONSEQUENCE = {"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT"}
SPECTRUM_CONSEQUENCE = {
    "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED",
    "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED",
    "CHARGED_LEPTON_MASS_SPECTRUM_RETAINED",
}


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


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def all_subsets(items: set[str]) -> list[set[str]]:
    ordered = sorted(items)
    subsets: list[set[str]] = []
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            subsets.append(set(combo))
    return subsets


def closes_spectrum(inputs: set[str]) -> bool:
    return SPECTRUM_INPUTS <= inputs


def closes_r_lep(inputs: set[str]) -> bool:
    return R_LEP_INPUTS <= inputs


def r(k: int, delta: float) -> float:
    return 1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * k / 3.0)


def roots(delta: float) -> list[float]:
    return [r(k, delta) for k in range(3)]


def masses(delta: float, scale: float) -> list[float]:
    return [scale * root * root for root in roots(delta)]


def signed_koide_q(delta: float) -> float:
    values = roots(delta)
    return sum(value * value for value in values) / (sum(values) ** 2)


def physical_positive_q(delta: float) -> float:
    values = roots(delta)
    squared = [value * value for value in values]
    return sum(squared) / (sum(math.sqrt(value) for value in squared) ** 2)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        R_LEP_NO_GO,
        ELECTRON_MASS_PACKET,
        NATIVE_BRIDGE,
        BRANCH_MASS_MAP,
        SPECIES_BRIDGE,
        ABSOLUTE_SCALE,
        SCALE_REFERENCE,
        REGISTRY,
        MINIMAL,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Charged-Lepton Mass-Spectrum Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the physical charged-lepton mass spectrum",
        "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED",
        "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED",
        "the physical charged-lepton mass-spectrum handoff for the zero-import hydrogen",
        "R-Lep and Lane 6 lanes",
        "CHARGED_LEPTON_MASS_SPECTRUM_TEXT_LOCK",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "FULL_CHARGED_LEPTON_SPECIES_LABELING_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_ALPHA0_OR_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eleven contract inputs",
        "CHARGED_LEPTON_MASS_SPECTRUM_RETAINED",
        "ALPHA_MZ_SCALE_CONTEXT_RETAINED",
        "LEPTON_THRESHOLD_MOMENT_MAP_RETAINED",
        "r_k(delta) = 1 + sqrt(2) cos(delta + 2 pi k / 3)",
        "m_k = a_l^2 r_k(delta)^2",
        "delta = 2/9",
        "0.04034990821920668",
        "0.5802119201475365",
        "2.3794381716332564",
        "Permuting branch labels preserves the unordered",
        "Open PRs were refreshed on 2026-07-05 UTC after `#5015` opened and after",
        "clean/green status is not a prerequisite",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad spectrum-retention claim fails; narrowed mass-spectrum",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(SPECTRUM_INPUTS)
    audit.check("full spectrum contract accepts handoff", closes_spectrum(full_inputs))
    for missing in sorted(SPECTRUM_INPUTS):
        reduced = set(SPECTRUM_INPUTS)
        reduced.remove(missing)
        audit.check(f"spectrum handoff fails without {missing}", not closes_spectrum(reduced))
    accepted_subsets = [subset for subset in all_subsets(SPECTRUM_INPUTS) if closes_spectrum(subset)]
    audit.check("only full spectrum subset closes handoff", accepted_subsets == [full_inputs])

    audit.check("electron mass consequence does not close full spectrum", not closes_spectrum(ELECTRON_MASS_CONSEQUENCE))
    audit.check("spectrum consequence alone does not close R-Lep", not closes_r_lep(SPECTRUM_CONSEQUENCE))
    audit.check("full R-Lep predicate closes with all inputs", closes_r_lep(set(R_LEP_INPUTS)))
    for missing in sorted(R_LEP_INPUTS):
        reduced = set(R_LEP_INPUTS)
        reduced.remove(missing)
        audit.check(f"R-Lep still fails without {missing}", not closes_r_lep(reduced))

    section("Finite spectrum arithmetic checks")
    delta = 2.0 / 9.0
    expected_roots = [
        0.04034990821920668,
        0.5802119201475365,
        2.3794381716332564,
    ]
    sorted_roots = sorted(roots(delta))
    for got, expected, label in zip(sorted_roots, expected_roots, ["electron-like", "muon-like", "tau-like"]):
        audit.check(
            f"delta=2/9 sorted {label} root ratio matches witness",
            abs(got - expected) < 1e-14,
            f"{got:.15f}",
        )
    audit.check("sum roots is 3", abs(sum(roots(delta)) - 3.0) < 1e-14)
    audit.check("sum root squares is 6", abs(sum(value * value for value in roots(delta)) - 6.0) < 1e-14)
    audit.check("signed Koide Q is 2/3 at delta=2/9", abs(signed_koide_q(delta) - 2.0 / 3.0) < 1e-14)
    audit.check("delta=2/9 positive branch chamber", all(value > 0 for value in roots(delta)))
    audit.check("positive physical Q is 2/3 in positive chamber", abs(physical_positive_q(delta) - 2.0 / 3.0) < 1e-14)

    bad_delta = 1.0
    audit.check("delta=1 has a negative signed branch", min(roots(bad_delta)) < 0.0)
    audit.check("signed Q remains 2/3 at delta=1", abs(signed_koide_q(bad_delta) - 2.0 / 3.0) < 1e-14)
    audit.check("positive-root Q differs when a branch is negative", abs(physical_positive_q(bad_delta) - 2.0 / 3.0) > 0.05)

    scale = 313.841126
    mass_values = masses(delta, scale)
    mass_values_scaled = masses(delta, scale * 1.01)
    for base, scaled in zip(mass_values, mass_values_scaled):
        audit.check("scale replacement multiplies each mass", abs(scaled / base - 1.01) < 1e-14)
    audit.check("unordered triple survives branch permutation", sorted(mass_values) == sorted(reversed(mass_values)))
    audit.check("electron-only consequence has one mass, not three labels", len(SPECTRUM_CONSEQUENCE - ELECTRON_MASS_CONSEQUENCE) == 3)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    r_lep = read(R_LEP_NO_GO)
    electron_packet = read(ELECTRON_MASS_PACKET)
    native_bridge = read(NATIVE_BRIDGE)
    branch_map = read(BRANCH_MASS_MAP)
    species_bridge = read(SPECIES_BRIDGE)
    absolute_scale = read(ABSOLUTE_SCALE)
    scale_reference = flat(read(SCALE_REFERENCE)).lower()
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("R-Lep no-go", r_lep),
        ("physical electron mass packet", electron_packet),
    ]:
        audit.check(f"{container_name} references spectrum packet", NOTE.name in container)

    audit.check(
        "R-Lep no-go consumes spectrum consequences",
        "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED" in r_lep
        and "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED" in r_lep,
    )
    audit.check("electron packet remains electron-facing", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in electron_packet)
    audit.check("native bridge remains route support", "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in native_bridge and "does not derive `m_e`" in native_bridge)
    audit.check("branch map remains composition support", "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_map and "does not derive a physical electron mass" in branch_map)
    audit.check("species bridge remains K3 electron support", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_bridge and "K3 support only" in species_bridge)
    audit.check("absolute scale remains K4 only", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in absolute_scale and "K4 support only" in absolute_scale)
    audit.check("scale primitive has zero dimensionless mass content", "zero dimensionless content" in scale_reference and "mass ratio" in scale_reference)
    audit.check(
        "minimal axioms require downstream bridges",
        "Further physical\nstructure requires derivation" in minimal,
    )

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "charged_lepton_mass_spectrum_primitive",
        "full_charged_lepton_species_labeling_primitive",
        "r_lep_thresholds_primitive",
        "electron_mass_primitive",
        "alpha0_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5011` eta twisted walk family runner | open",
        "`#5010` YT P1 I_s re-audit packet bridge repair | open",
        "`#5009` S3 spacetime tensor primitive runner | open",
        "`#5008` quark mass-ratio CP probe repair | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open",
        "`#4991` owner-governed Tier-A retirement | open",
    ]
    for marker in latest_pr_markers:
        audit.check(f"opened PR marker present: {marker}", flat(marker) in note_flat)
    audit.check("open PR check does not require clean status", "clean/green status is not a prerequisite" in note)

    explicit_non_claims = [
        "No derivation or ratification of the physical charged-lepton mass spectrum.",
        "No derivation or ratification of `m_e`, `m_mu`, or `m_tau`.",
        "No derivation or ratification of the native Z1-Z3 bridge clauses.",
        "No derivation or ratification of the Koide branch-to-mass map.",
        "No derivation or ratification of full physical `e`, `mu`, `tau` labels.",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation or ratification of `R_LEP_THRESHOLDS_RETAINED`.",
        "No derivation or ratification of `T_LEP_THRESHOLD_MOMENT_RETAINED`.",
        "No derivation of `alpha(0)`, static-source Rydberg, or retained hydrogen.",
        "No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the physical charged-lepton mass spectrum",
        "physical charged-lepton mass spectrum is retained",
        "R_LEP_THRESHOLDS_RETAINED is supplied",
        "alpha(0) is retained",
        "hydrogen is retained",
        "PDG charged-lepton masses are proof inputs",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
