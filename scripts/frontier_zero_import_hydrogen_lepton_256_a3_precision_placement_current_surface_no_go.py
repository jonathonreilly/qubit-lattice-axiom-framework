#!/usr/bin/env python3
"""Verifier for the A3 precision-placement current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply A3_PRECISION_PLACEMENT_RETAINED. It preserves the positive
P1/P2/P3/P4 placement routes and keeps K4, m_e, alpha(0), Rydberg, and hydrogen
downstream.
"""

from __future__ import annotations

from decimal import Decimal, getcontext
from itertools import combinations
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_NO_DOUBLE_COUNT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PRECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
P1_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
P2_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_FRONT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_RATIFICATION_DECISION_PACKET_2026-07-05.md"
P3_KOIDE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P4_DIRECT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KOIDE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

A3_INPUTS = {
    "A3_PLACEMENT_TEXT_LOCK",
    "EXACT_SOURCE_SCAFFOLD_STATUS",
    "ONE_PLACEMENT_SELECTED",
    "PLACEMENT_THEOREM_RETAINED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PLACEMENTS = {
    "P1_SOURCE_READOUT_CORRECTION_RETAINED",
    "P2_WEAK_FRONT_MATCHING_RETAINED",
    "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
    "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
}

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


def closes_a3(inputs: set[str], placements: set[str]) -> bool:
    return A3_INPUTS <= inputs and len(PLACEMENTS & placements) == 1


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        A3_DECISION,
        A3_NO_DOUBLE_COUNT,
        SOURCE_DECISION,
        EXACT_SOURCE_NO_GO,
        WEAK_FRONT_NO_GO,
        PRECISION,
        PLACEMENT,
        P1_SOURCE_NO_GO,
        P2_TARGET,
        P2_FRONT_NO_GO,
        P2_FRONT_DECISION,
        P3_KOIDE_NO_GO,
        P4_DIRECT_NO_GO,
        KOIDE,
        PHYSICAL_ELECTRON,
        ALPHA,
        STATIC_TARGET,
        MINIMAL,
        REGISTRY,
        TIER_A_REGISTRY,
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
        "A3 Precision-Placement Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "current retained, primitive, and open-PR surfaces do not supply",
        "A3_PLACEMENT_TEXT_LOCK",
        "EXACT_SOURCE_SCAFFOLD_STATUS",
        "ONE_PLACEMENT_SELECTED",
        "PLACEMENT_THEOREM_RETAINED",
        "NO_SOURCE_DOUBLE_COUNT",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED",
        "P2_WEAK_FRONT_MATCHING_RETAINED",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "P1: F_0 * (C_A3 * S_0) * R_0",
        "P2: (C_A3 * F_0) * S_0 * R_0",
        "P3: F_0 * S_0 * (C_A3 * R_0)",
        "P4: F_0 * (1/N_A3) * R_0",
        "C_A3^2",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_NO_DOUBLE_COUNT_COMPOSITION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "NO_SOURCE_DOUBLE_COUNT",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "MATCHING_THEOREM_RETAINED",
        "positive P2 front-matching owner/audit handoff",
        "P2 front-matching route has an explicit ten-input packet but is still unaccepted",
        "a3_precision_placement_primitive",
        "a3_correction_primitive",
        "a3_placement_selector_primitive",
        "weak_front_matching_primitive",
        "koide_electron_a3_correction_primitive",
        "direct_noninteger_divisor_primitive",
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
        "broad A3 no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("A3 predicate checks")
    full_inputs = set(A3_INPUTS)
    audit.check("full A3 contract plus one placement accepts decision", closes_a3(full_inputs, {"P2_WEAK_FRONT_MATCHING_RETAINED"}))
    for missing in sorted(A3_INPUTS):
        reduced = set(A3_INPUTS)
        reduced.remove(missing)
        audit.check(f"A3 decision fails without {missing}", not closes_a3(reduced, {"P2_WEAK_FRONT_MATCHING_RETAINED"}))
    audit.check("A3 decision fails with no placement", not closes_a3(full_inputs, set()))
    for placement in sorted(PLACEMENTS):
        audit.check(f"single placement accepts: {placement}", closes_a3(full_inputs, {placement}))
    for subset in all_subsets(PLACEMENTS):
        if len(subset) != 1:
            audit.check(f"non-singleton placement rejected: {sorted(subset)}", not closes_a3(full_inputs, subset))
    audit.check("A3 alone does not close K4", not closes_k4({"A3_PRECISION_PLACEMENT_RETAINED"}))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))

    section("Finite placement witness checks")
    getcontext().prec = 50
    n_a3 = Decimal("256.08243522600384")
    c_a3 = Decimal(256) / n_a3
    s0 = Decimal(1) / Decimal(256)
    f0 = Decimal("0.461616")
    r0 = Decimal("1.375")
    p1 = f0 * (c_a3 * s0) * r0
    p2 = (c_a3 * f0) * s0 * r0
    p3 = f0 * s0 * (c_a3 * r0)
    p4 = f0 * (Decimal(1) / n_a3) * r0
    base = f0 * s0 * r0
    double_count = (c_a3 * f0) * (c_a3 * s0) * r0
    audit.check("A3 correction target reproduced", abs(c_a3 - Decimal("0.9996780910571587")) < Decimal("1e-16"), str(c_a3))
    audit.check("exact source scaffold is 1/256", s0 == Decimal("0.00390625"))
    audit.check("P1 product equals P2 product", abs(p1 - p2) < Decimal("1e-45"))
    audit.check("P1 product equals P3 product", abs(p1 - p3) < Decimal("1e-45"))
    audit.check("P1 product equals P4 product", abs(p1 - p4) < Decimal("1e-45"))
    audit.check("placement product is C_A3 times base", abs(p1 / base - c_a3) < Decimal("1e-45"))
    audit.check("double-counted correction differs from one-correction product", abs(double_count - p1) > Decimal("1e-9"))
    audit.check("double-counted correction is C_A3 squared times base", abs(double_count / base - c_a3 * c_a3) < Decimal("1e-45"))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    a3_decision = read(A3_DECISION)
    a3_no_double_count = read(A3_NO_DOUBLE_COUNT)
    source_decision = read(SOURCE_DECISION)
    exact_source_no_go = read(EXACT_SOURCE_NO_GO)
    weak_front_no_go = read(WEAK_FRONT_NO_GO)
    precision = read(PRECISION)
    placement = read(PLACEMENT)
    p1_source_no_go = read(P1_SOURCE_NO_GO)
    p2_target = read(P2_TARGET)
    p2_front_no_go = read(P2_FRONT_NO_GO)
    p2_front_decision = read(P2_FRONT_DECISION)
    p3_koide_no_go = read(P3_KOIDE_NO_GO)
    p4_direct_no_go = read(P4_DIRECT_NO_GO)
    koide = read(KOIDE)
    physical_electron = read(PHYSICAL_ELECTRON)
    alpha = read(ALPHA)
    static_target = read(STATIC_TARGET)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    tier_a = read(TIER_A_REGISTRY)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    audit.check("goal packet references A3 no-go", NOTE.name in goal)
    audit.check("K4 packet references A3 no-go", NOTE.name in k4_packet)
    audit.check("A3 decision references A3 no-go", NOTE.name in a3_decision)
    audit.check("A3 no-go references no-double-count packet", A3_NO_DOUBLE_COUNT.name in note)
    audit.check("no-double-count packet does not close A3", "NO_SOURCE_DOUBLE_COUNT" in a3_no_double_count and "does not supply `A3_PRECISION_PLACEMENT_RETAINED`" in a3_no_double_count)
    audit.check("source decision keeps A3 downstream", "does not place the `256.082435...` precision" in source_decision)
    audit.check("exact-source no-go keeps exact source unsupplied", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_source_no_go and "current retained, primitive, and open-PR surfaces do not supply" in exact_source_no_go)
    audit.check("weak-front no-go keeps front unsupplied", "WEAK_FRONT_BASE_RETAINED" in weak_front_no_go and "current retained, primitive, and open-PR surfaces do not supply" in weak_front_no_go)
    audit.check("precision firewall does not derive C_A3", "No derivation of `C_A3 = 0.999678091...`" in precision)
    audit.check("placement discriminator lists P1-P5", all(token in placement for token in ["P1 source-readout", "P2 front-factor", "P3 Koide", "P4 direct", "P5 empirical"]))
    audit.check("P1 no-go keeps P1 unsupplied", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in p1_source_no_go and "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED" in p1_source_no_go)
    audit.check("P2 target names weak-front theorem", "F_phys = C_A3 * g_2 * (1/sqrt(2))" in p2_target and "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_target)
    audit.check("P2 no-go keeps P2 unsupplied", "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_front_no_go and "MATCHING_THEOREM_RETAINED" in p2_front_no_go)
    audit.check("P2 decision opens positive handoff", "P2_MATCHING_TEXT_LOCK" in p2_front_decision and "P2_WEAK_FRONT_MATCHING_RETAINED" in p2_front_decision)
    audit.check("P3 no-go keeps P3 unsupplied", "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in p3_koide_no_go and "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED" in p3_koide_no_go)
    audit.check("P4 no-go keeps P4 unsupplied", "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in p4_direct_no_go and "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in p4_direct_no_go)
    audit.check("K4 consumes A3 placement", "A3_PRECISION_PLACEMENT_RETAINED" in k4_packet and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_packet)
    audit.check("Koide remains downstream", "No derivation of `m_e`" in koide)
    audit.check("physical electron remains downstream", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron)
    audit.check("alpha target remains downstream", "No derivation of `alpha(0)`" in alpha)
    audit.check("static target remains downstream", "STATIC_SOURCE_RYDBERG" in static_target or "static-source Rydberg" in static_target)
    audit.check("minimal axioms exclude physical-observable identification", "physical-observable identification" in minimal)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "a3_precision_placement_primitive",
        "a3_correction_primitive",
        "a3_placement_selector_primitive",
        "weak_front_matching_primitive",
        "koide_electron_a3_correction_primitive",
        "direct_noninteger_divisor_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered A3 shortcut: {absent}", absent not in registry_text)
    audit.check("scale primitive excludes dimensionless corrections", "zero dimensionless content" in scale and "mass ratio" in scale)
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

    explicit_non_claims = [
        "No derivation or ratification of A3 precision placement.",
        "No derivation or ratification of any P1/P2/P3/P4 placement theorem.",
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of `N_A3 = 256.082435...`.",
        "No derivation of corrected `S_l = 1/N_A3`.",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note ratifies A3",
        "A3 precision placement is retained",
        "A3_PRECISION_PLACEMENT_RETAINED is supplied",
        "C_A3 is retained",
        "N_A3 is retained",
        "corrected S_l is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
