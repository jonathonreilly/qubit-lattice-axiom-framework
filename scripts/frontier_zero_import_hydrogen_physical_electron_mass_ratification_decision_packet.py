#!/usr/bin/env python3
"""Verifier for the physical electron mass decision packet.

This runner checks that the Lane 6 electron-mass handoff is explicit and
remains separate from alpha(0), static-source Rydberg closure, and comparator
data. It does not derive m_e or hydrogen spectroscopy.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
NATIVE_BRIDGE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SCALE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRANCH_MASS_MAP_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANCH_MASS_MAP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md"
ELECTRON_MASS_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
MASS_SPECTRUM_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
CHIRALITY_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHIRALITY_DOMAIN_WALL_PR5017_5018_IMPACT_DISCRIMINATOR_2026-07-05.md"
KOIDE_OPEN_CERT = ROOT / "docs" / "CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md"
BRANNEN_OPEN_GATE = ROOT / "docs" / "LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"


ELECTRON_MASS_INPUTS = {
    "PHYSICAL_ELECTRON_MASS_TEXT_LOCK",
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
    "NO_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

STATIC_SOURCE_REQUIRED = {
    "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "AUDIT_ACCEPTANCE",
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


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_static_source_rydberg(inputs: set[str]) -> bool:
    return STATIC_SOURCE_REQUIRED <= inputs


def brannen_root_ratio(k: int, delta: float) -> float:
    return 1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * k / 3.0)


def root_ratios(delta: float) -> list[float]:
    return [brannen_root_ratio(k, delta) for k in range(3)]


def koide_q(delta: float) -> float:
    xs = root_ratios(delta)
    return sum(x * x for x in xs) / (sum(xs) ** 2)


def rho_e(delta: float) -> float:
    return min(x * x for x in root_ratios(delta))


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        STATIC_TARGET,
        KOIDE_FIREWALL,
        BRIDGE_DECISION,
        NATIVE_BRIDGE_NO_GO,
        SPECIES_DECISION,
        SPECIES_NO_GO,
        SCALE_DECISION,
        SCALE_NO_GO,
        BRANCH_MASS_MAP_DECISION,
        BRANCH_MASS_MAP_NO_GO,
        ELECTRON_MASS_NO_GO,
        MASS_SPECTRUM_PACKET,
        PR5020_IMPACT,
        PR5019_IMPACT,
        CHIRALITY_IMPACT,
        KOIDE_OPEN_CERT,
        BRANNEN_OPEN_GATE,
        LEPTON_SCALE,
        SCALE_REFERENCE,
        REGISTRY,
        TIER_A_REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Physical Electron Mass Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the physical electron mass",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "the physical electron mass readout for the hydrogen static-source Rydberg lane",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "native bridge target remains needed",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "species bridge target remains needed",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "K4 scale target remains needed",
        "KOIDE_BRANCH_MASS_MAP_RETAINED",
        "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current Koide algebra, primitive, and open-PR surfaces do not",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "ZERO_IMPORT_HYDROGEN_CHARGED_LEPTON_MASS_SPECTRUM_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "mass-spectrum target remains needed",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "native bridge, physical species",
        "KOIDE_BRANCH_MASS_MAP_TEXT_LOCK",
        "BRANNEN_CIRCULANT_BRANCH_FORM_RETAINED",
        "SQUARE_ROOT_MASS_READOUT_RETAINED",
        "POSITIVE_CHAMBER_OR_SIGN_RULE_RETAINED",
        "SCALE_PARAMETER_COMPOSITION_RETAINED",
        "PHASE_SCALE_SPECIES_SCOPE_LOCK",
        "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
        "NO_LEPTON_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eleven contract inputs",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "m_e = a_l^2 * rho_e(delta)",
        "Q = 2/3",
        "rho_e(delta) = 0.001628115093",
        "Open PR Alignment",
        "Open PRs were refreshed on 2026-07-05 UTC after `#5015` opened and after",
        "clean/green status is not a prerequisite",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open",
        "K2 value-face progress",
        "exactness residual remains open",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | open",
        "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "premise-hygiene and audit-readiness context",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "ZERO_IMPORT_HYDROGEN_CHIRALITY_DOMAIN_WALL_PR5017_5018_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "above-C3 chiral-content map",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad electron-mass-retention claim fails; narrowed physical",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(ELECTRON_MASS_INPUTS)
    audit.check("full electron-mass contract accepts decision", closes_electron_mass(full_inputs))
    for missing in sorted(ELECTRON_MASS_INPUTS):
        reduced = set(ELECTRON_MASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"electron-mass decision fails without {missing}", not closes_electron_mass(reduced))
    accepted_subsets = [subset for subset in all_subsets(ELECTRON_MASS_INPUTS) if closes_electron_mass(subset)]
    audit.check("only full tested contract subset closes electron mass", accepted_subsets == [full_inputs])

    electron_consequence = {"RETAINED_ELECTRON_MASS_PHYSICAL_UNIT"}
    audit.check("electron mass alone does not close static-source Rydberg", not closes_static_source_rydberg(electron_consequence))
    alpha_consequence = {"RETAINED_ALPHA0_LOW_ENERGY_COULOMB"}
    audit.check("alpha(0) alone does not close static-source Rydberg", not closes_static_source_rydberg(alpha_consequence))
    full_static = set(STATIC_SOURCE_REQUIRED)
    audit.check("full static-source predicate model closes Rydberg", closes_static_source_rydberg(full_static))
    for missing in sorted(STATIC_SOURCE_REQUIRED):
        reduced = set(STATIC_SOURCE_REQUIRED)
        reduced.remove(missing)
        audit.check(f"static-source Rydberg fails without {missing}", not closes_static_source_rydberg(reduced))

    section("Finite branch arithmetic checks")
    expected_delta = 2.0 / 9.0
    expected_sorted = [
        0.04034990821920668,
        0.5802119201475365,
        2.3794381716332564,
    ]
    sorted_delta = sorted(root_ratios(expected_delta))
    for got, expected, label in zip(sorted_delta, expected_sorted, ["electron-like", "muon-like", "tau-like"]):
        audit.check(
            f"delta=2/9 sorted {label} root ratio matches comparator",
            abs(got - expected) < 1e-14,
            f"{got:.15f}",
        )

    for delta in [expected_delta, 0.0, 0.5, 1.0, 3.0 * math.pi / 4.0]:
        audit.check(
            f"Koide Q remains 2/3 at delta={delta:.6f}",
            abs(koide_q(delta) - 2.0 / 3.0) < 1e-14,
            f"Q={koide_q(delta):.15f}",
        )

    rho_delta = rho_e(expected_delta)
    rho_zero = rho_e(0.0)
    rho_zero_branch = rho_e(3.0 * math.pi / 4.0)
    audit.check(
        "delta=2/9 electron factor is the sharp comparator value",
        abs(rho_delta - expected_sorted[0] ** 2) < 1e-16 and 0.00162 < rho_delta < 0.00164,
        f"rho={rho_delta:.15f}",
    )
    audit.check("delta=0 has same Q but larger electron-like factor", rho_zero > 0.08, f"rho={rho_zero:.15f}")
    audit.check(
        "delta=0 electron-like factor is more than 50x delta=2/9",
        rho_zero / rho_delta > 50.0,
        f"ratio={rho_zero / rho_delta:.2f}",
    )
    audit.check(
        "delta=3*pi/4 can make one branch zero while preserving Q",
        rho_zero_branch < 1e-28,
        f"rho={rho_zero_branch:.3e}",
    )

    scale_a = 313.841126
    scale_b = scale_a * 1.01
    mass_a = scale_a * rho_delta
    mass_b = scale_b * rho_delta
    mass_wrong_phase = scale_a * rho_zero
    audit.check("same branch factor with different scale changes mass", abs(mass_b / mass_a - 1.01) < 1e-14)
    audit.check("same scale with different phase changes mass", mass_wrong_phase / mass_a > 50.0)
    audit.check("product identity m_e = a_l^2 * rho_e(delta) is finite arithmetic", abs(mass_a - scale_a * rho_delta) < 1e-15)

    section("Authority boundary checks")
    goal = read(GOAL)
    static_target = read(STATIC_TARGET)
    koide_firewall = read(KOIDE_FIREWALL)
    bridge_decision = read(BRIDGE_DECISION)
    native_bridge_no_go = read(NATIVE_BRIDGE_NO_GO)
    species_decision = read(SPECIES_DECISION)
    species_no_go = read(SPECIES_NO_GO)
    scale_decision = read(SCALE_DECISION)
    scale_no_go = read(SCALE_NO_GO)
    branch_mass_map_decision = read(BRANCH_MASS_MAP_DECISION)
    branch_mass_map_no_go = read(BRANCH_MASS_MAP_NO_GO)
    electron_mass_no_go = read(ELECTRON_MASS_NO_GO)
    mass_spectrum_packet = read(MASS_SPECTRUM_PACKET)
    pr5020_impact = read(PR5020_IMPACT)
    chirality_impact = read(CHIRALITY_IMPACT)
    koide_open_cert = read(KOIDE_OPEN_CERT)
    brannen_open_gate = read(BRANNEN_OPEN_GATE)
    lepton_scale = read(LEPTON_SCALE)
    scale_reference = flat(read(SCALE_REFERENCE)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("static-source Rydberg discriminator", static_target),
        ("Koide electron-readout firewall", koide_firewall),
    ]:
        audit.check(f"{container_name} references electron-mass packet", NOTE.name in container)

    audit.check("Koide firewall still names K1-K4 separation", all(token in koide_firewall for token in ["K1 |", "K2 |", "K3 |", "K4 |"]))
    audit.check("Koide firewall does not derive m_e", "No derivation of `m_e`." in koide_firewall)
    audit.check("native bridge packet remains bridge only", "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in bridge_decision and "does not derive `m_e`" in bridge_decision)
    audit.check("electron-mass packet references native no-go", NATIVE_BRIDGE_NO_GO.name in note and "native bridge target remains needed" in note)
    audit.check(
        "native no-go keeps bridge open",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED" in native_bridge_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in native_bridge_no_go,
    )
    audit.check("species packet remains K3 only", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_decision and "K3 support only" in species_decision)
    audit.check(
        "electron-mass packet references chirality impact note",
        CHIRALITY_IMPACT.name in note and "#5018" in note and "#5017" in note,
    )
    audit.check(
        "chirality impact remains non-mass context",
        "above-C3 chirality/domain-wall content" in chirality_impact
        and "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`." in chirality_impact,
    )
    audit.check("electron-mass packet references species no-go", SPECIES_NO_GO.name in note and "species bridge target remains needed" in note)
    audit.check(
        "species no-go keeps K3 open",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_no_go
        and "current retained, primitive, merged-PR, and open-PR surfaces do not supply" in species_no_go,
    )
    audit.check("scale packet remains K4 only", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in scale_decision and "K4 support only" in scale_decision)
    audit.check("electron-mass packet references K4 no-go", SCALE_NO_GO.name in note and "K4 scale target remains needed" in note)
    audit.check("K4 no-go keeps absolute scale open", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in scale_no_go and "current retained, primitive, and open-PR surfaces do not supply" in scale_no_go)
    audit.check(
        "branch mass-map packet remains map only",
        "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_mass_map_decision and "does not derive a physical electron mass" in branch_mass_map_decision,
    )
    audit.check(
        "branch mass-map no-go keeps map open",
        "KOIDE_BRANCH_MASS_MAP_RETAINED" in branch_mass_map_no_go and "SQUARE_ROOT_MASS_READOUT_RETAINED" in branch_mass_map_no_go,
    )
    audit.check(
        "electron mass no-go keeps physical m_e open",
        "PHYSICAL_ELECTRON_READOUT_RETAINED" in electron_mass_no_go and "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in electron_mass_no_go,
    )
    audit.check("electron-mass packet references full mass-spectrum sibling", MASS_SPECTRUM_PACKET.name in note and "mass-spectrum target remains needed" in note)
    audit.check(
        "mass-spectrum sibling keeps full triple separate",
        "PHYSICAL_CHARGED_LEPTON_MASS_TRIPLE_RETAINED" in mass_spectrum_packet
        and "PHYSICAL_CHARGED_LEPTON_SPECIES_LABELS_RETAINED" in mass_spectrum_packet,
    )
    audit.check(
        "electron-mass packet references #5020 impact note",
        PR5020_IMPACT.name in note and "#5020" in note,
    )
    audit.check(
        "#5020 impact remains K2 value-face progress only",
        "K2 value-face progress" in pr5020_impact
        and "No derivation of `delta = 2/9`." in pr5020_impact
        and "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`." in pr5020_impact,
    )
    audit.check("Koide open certificate keeps physical mass spectrum open", "not a derivation of the physical charged-lepton" in koide_open_cert)
    audit.check("Koide open certificate excludes mass-spectrum theorem", "physical charged-lepton mass-spectrum theorem" in koide_open_cert)
    audit.check("Brannen open gate excludes phase and scale derivation", "does not derive the Brannen phase" in brannen_open_gate and "dimensionful mass scale" in brannen_open_gate)
    audit.check("Brannen open gate excludes absolute predictions", "absolute predictions of `m_e`, `m_mu`, or `m_tau`" in brannen_open_gate)
    audit.check("lepton-scale probe names scale factorization", "y_scale := a_lepton" in lepton_scale and "1/256" in lepton_scale)
    audit.check("lepton-scale probe keeps 1/256 open", "No derivation of `1/256`; it is the open gate." in lepton_scale)
    audit.check("scale-reference primitive is units-only", "zero dimensionless content" in scale_reference and "units conversion" in scale_reference)
    audit.check("static target consumes retained electron mass", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in static_target)
    audit.check("static target still needs alpha0", "RETAINED_ALPHA0_LOW_ENERGY_COULOMB" in static_target)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "electron_mass_primitive",
        "koide_branch_mass_map_primitive",
        "charged_lepton_phase_primitive",
        "physical_electron_species_primitive",
        "absolute_charged_lepton_scale_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | open",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | open",
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
    audit.check("open PR check does not require clean status", "clean/green status is not a prerequisite" in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of the physical electron mass.",
        "No derivation or ratification of the native Z1-Z3 bridge clauses.",
        "No derivation or ratification of the physical electron species bridge.",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation or ratification of the Koide branch-to-mass map.",
        "No derivation of `Q=2/3`, `delta = 2/9`, `rho_e(delta)`, or `a_l^2`.",
        "No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted",
        "No derivation of `alpha(0)`, static-source Rydberg, or full hydrogen",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the physical electron mass",
        "physical electron mass is retained",
        "m_e is retained",
        "This packet derives `m_e`",
        "delta = 2/9 is derived",
        "a_l^2 is derived",
        "static-source Rydberg hydrogen is retained",
        "full precision hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
