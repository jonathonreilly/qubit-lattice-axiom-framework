#!/usr/bin/env python3
"""Verifier for the K4 absolute charged-lepton scale current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply the K4 scale assembly consumed by the physical electron
mass lane. It preserves the positive K4 contract and does not derive m_e,
alpha(0), Rydberg, or hydrogen.
"""

from __future__ import annotations

import json
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
ELECTRON_MASS_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ELECTRON_MASS_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K4_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
WEAK_FRONT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_P2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
P1_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P3_KOIDE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P4_DIRECT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
PRECISION_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


K4_INPUTS = {
    "K4_SCALE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "WEAK_FRONT_BASE_RETAINED",
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "A3_PRECISION_PLACEMENT_RETAINED",
    "NO_SOURCE_A3_DOUBLE_COUNT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PHYSICAL_ELECTRON_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
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


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def closes_physical_electron(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        ELECTRON_MASS_PACKET,
        ELECTRON_MASS_NO_GO,
        K4_DECISION,
        WEAK_FRONT_DECISION,
        WEAK_FRONT_NO_GO,
        SOURCE_DECISION,
        EXACT_SOURCE_NO_GO,
        A3_DECISION,
        A3_NO_GO,
        A3_P2,
        P1_SOURCE_NO_GO,
        P2_FRONT_NO_GO,
        P3_KOIDE_NO_GO,
        P4_DIRECT_NO_GO,
        LEPTON_SCALE,
        PRECISION_FIREWALL,
        REGISTRY,
        TIER_A_REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "Absolute Charged-Lepton Scale Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify the absolute",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "K4_SCALE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "WEAK_FRONT_BASE_RETAINED",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "y_scale = g_2 * (1/sqrt(2)) * S_l",
        "S_0 = 1/256",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "S_l = C_A3 * S_0 = 1/N_A3",
        "P1: F_0 * (C_A3 * S_0) * R_0",
        "P2: (C_A3 * F_0) * S_0 * R_0",
        "P3: F_0 * S_0 * (C_A3 * R_0)",
        "P4: F_0 * (1/N_A3) * R_0",
        "C_A3^2",
        "absolute_charged_lepton_scale_primitive",
        "weak_front_base_primitive",
        "exact_source_singleton_primitive",
        "a3_precision_placement_primitive",
        "charged_lepton_scale_primitive",
        "electron_mass_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad K4 no-go fails; narrowed current-surface non-supply claim passes",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("K4 predicate checks")
    full_inputs = set(K4_INPUTS)
    audit.check("full K4 contract accepts retained handoff", closes_k4(full_inputs))
    for missing in sorted(K4_INPUTS):
        reduced = set(K4_INPUTS)
        reduced.remove(missing)
        audit.check(f"K4 handoff fails without {missing}", not closes_k4(reduced))
    accepted_subsets = [subset for subset in all_subsets(K4_INPUTS) if closes_k4(subset)]
    audit.check("only full K4 subset closes handoff", accepted_subsets == [full_inputs])
    current_surface = {
        "K4_SCALE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check(
        "current surface without weak/source/A3 inputs does not close K4",
        not closes_k4(current_surface),
    )
    audit.check(
        "retained K4 alone does not close physical electron",
        not closes_physical_electron({"ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED"}),
    )
    audit.check(
        "full physical electron predicate still needs K4 plus other inputs",
        closes_physical_electron(set(PHYSICAL_ELECTRON_INPUTS)),
    )

    section("Finite K4 target checks")
    getcontext().prec = 60
    s0 = Fraction(1, 256)
    audit.check("exact source scaffold is 1/256", s0 == Fraction(1, 256))
    n_a3 = Decimal("256.08243522600384")
    c_a3 = Decimal(256) / n_a3
    audit.check("A3 correction target reproduced", abs(c_a3 - Decimal("0.9996780910571587")) < Decimal("1e-16"), str(c_a3))
    direct = Decimal(1) / n_a3
    audit.check("C_A3 times exact singleton equals 1/N_A3", abs(c_a3 * Decimal(s0.numerator) / Decimal(s0.denominator) - direct) < Decimal("1e-40"))
    f0 = Decimal("0.459")
    r0 = Decimal("0.001628115093")
    s0_dec = Decimal(s0.numerator) / Decimal(s0.denominator)
    p1 = f0 * (c_a3 * s0_dec) * r0
    p2 = (c_a3 * f0) * s0_dec * r0
    p3 = f0 * s0_dec * (c_a3 * r0)
    p4 = f0 * direct * r0
    base = f0 * s0_dec * r0
    double_count = f0 * (c_a3 * s0_dec) * (c_a3 * r0)
    audit.check("P1 product equals P2 product", abs(p1 - p2) < Decimal("1e-40"))
    audit.check("P1 product equals P3 product", abs(p1 - p3) < Decimal("1e-40"))
    audit.check("P1 product equals P4 product", abs(p1 - p4) < Decimal("1e-40"))
    audit.check("one placement is C_A3 times base", abs(p1 / base - c_a3) < Decimal("1e-40"))
    audit.check("double-counted correction differs from one-correction product", abs(double_count - p1) > Decimal("1e-10"))
    audit.check("double-counted correction is C_A3 squared times base", abs(double_count / base - c_a3 * c_a3) < Decimal("1e-40"))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    electron_mass_packet = read(ELECTRON_MASS_PACKET)
    electron_mass_no_go = read(ELECTRON_MASS_NO_GO)
    k4_decision = read(K4_DECISION)
    weak_front_decision = read(WEAK_FRONT_DECISION)
    weak_front_no_go = read(WEAK_FRONT_NO_GO)
    source_decision = read(SOURCE_DECISION)
    exact_source_no_go = read(EXACT_SOURCE_NO_GO)
    a3_decision = read(A3_DECISION)
    a3_no_go = read(A3_NO_GO)
    a3_p2 = read(A3_P2)
    p1_source_no_go = read(P1_SOURCE_NO_GO)
    p2_front_no_go = read(P2_FRONT_NO_GO)
    p3_koide_no_go = read(P3_KOIDE_NO_GO)
    p4_direct_no_go = read(P4_DIRECT_NO_GO)
    lepton_scale = read(LEPTON_SCALE)
    precision_firewall = read(PRECISION_FIREWALL)
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    tier_a = read(TIER_A_REGISTRY)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    audit.check("goal packet references K4 no-go", NOTE.name in goal and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in goal)
    audit.check("Koide firewall references K4 no-go", NOTE.name in koide_firewall and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in koide_firewall)
    audit.check("physical electron packet references K4 no-go", NOTE.name in electron_mass_packet and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in electron_mass_packet)
    audit.check("physical electron no-go already keeps K4 open", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in electron_mass_no_go and "current retained, primitive, and open-PR surfaces do not supply" in electron_mass_no_go)
    audit.check("K4 decision remains decision-only", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_decision and "does not ratify the absolute charged-lepton scale" in flat(k4_decision))
    audit.check("weak-front decision remains base only", "WEAK_FRONT_BASE_RETAINED" in weak_front_decision and "does not derive the A3 correction" in weak_front_decision)
    audit.check("weak-front no-go keeps base unsupplied", "WEAK_FRONT_BASE_RETAINED" in weak_front_no_go and "current retained, primitive, and open-PR surfaces do not supply" in weak_front_no_go)
    audit.check("source decision remains source-side only", "EXACT_SOURCE_SINGLETON_RETAINED" in source_decision and "This is source-side only" in source_decision and "does not derive" in source_decision)
    audit.check("exact-source no-go keeps source singleton unsupplied", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_source_no_go and "current retained, primitive, and open-PR surfaces do not supply" in exact_source_no_go)
    audit.check("A3 decision remains placement only", "A3_PRECISION_PLACEMENT_RETAINED" in a3_decision and "does not by itself derive `C_A3`" in a3_decision)
    audit.check("A3 no-go keeps placement unsupplied", "A3_PRECISION_PLACEMENT_RETAINED" in a3_no_go and "current retained, primitive, and open-PR surfaces do not supply" in a3_no_go)
    audit.check("P1 no-go keeps source correction open", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in p1_source_no_go and "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED" in p1_source_no_go)
    audit.check("P2 target names weak-front matching", "F_phys = C_A3 * g_2 * (1/sqrt(2))" in a3_p2 and "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in a3_p2)
    audit.check("P2 no-go keeps front matching open", "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_front_no_go and "MATCHING_THEOREM_RETAINED" in p2_front_no_go)
    audit.check("P3 no-go keeps Koide correction open", "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in p3_koide_no_go and "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED" in p3_koide_no_go)
    audit.check("P4 no-go keeps direct divisor open", "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in p4_direct_no_go and "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in p4_direct_no_go)
    audit.check("lepton-scale probe carries K4 factorization", "y_scale := a_lepton" in lepton_scale and "1/256" in lepton_scale)
    audit.check("precision firewall does not derive correction", "No derivation of `C_A3 = 0.999678091...`" in precision_firewall)
    audit.check("minimal axioms exclude downstream physical observables", "physical-observable identification" in minimal)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "absolute_charged_lepton_scale_primitive",
        "weak_front_base_primitive",
        "exact_source_singleton_primitive",
        "a3_precision_placement_primitive",
        "charged_lepton_scale_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered K4 shortcut: {absent}", absent not in registry_text)
    audit.check("scale primitive excludes dimensionless scale assembly", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes values and normalization", "normalization rule" in realized and "or value is supplied" in realized)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.",
        "No derivation or ratification of `WEAK_FRONT_BASE_RETAINED`.",
        "No derivation or ratification of `EXACT_SOURCE_SINGLETON_RETAINED`.",
        "No derivation or ratification of `A3_PRECISION_PLACEMENT_RETAINED`.",
        "No derivation of `C_A3 = 0.999678091...` or `N_A3 = 256.082435...`.",
        "No derivation or ratification of any P1/P2/P3/P4 placement theorem.",
        "No derivation of `a_l^2`, `m_e`, `alpha(0)`, static-source Rydberg, or",
        "No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies the absolute charged-lepton scale",
        "absolute charged-lepton scale is retained",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED is supplied",
        "weak-front base is retained",
        "exact source singleton is retained",
        "A3 precision placement is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
