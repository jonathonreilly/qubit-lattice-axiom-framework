#!/usr/bin/env python3
"""Verifier for the Koide R-eta h-class current-surface no-go."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_UNIT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_UNIT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
R_ETA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
AC_R_ETA_CLUSTER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md"
R_ETA_NARROWING = ROOT / "docs" / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
R_ETA_W2 = ROOT / "docs" / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
FIXED_LOCUS = ROOT / "docs" / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
FLAVOR_ASYMMETRY = ROOT / "docs" / "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md"
OPERATOR_DENSITY = ROOT / "docs" / "FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md"
AMBIENT_FACE = ROOT / "docs" / "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md"
K_EVEN_PATTERN = ROOT / "docs" / "ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


H_CLASS_INPUTS = {
    "R_ETA_H_CLASS_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "SUPPLIED_CONTEXT_REGISTRABILITY_ACCEPTED",
    "AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = {
    "R_ETA_H_CLASS_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "SUPPLIED_CONTEXT_REGISTRABILITY_ACCEPTED",
    "AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_ACCEPTED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

R_ETA_INPUTS = {
    "R_ETA_RETIREMENT_TEXT_LOCK",
    "FORM_LAYER_AND_K_ORBIT_AUTHORITY_ACCEPTED",
    "FINITE_FIXED_LOCUS_ARITHMETIC_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_RETAINED",
    "R_ETA_H_CLASS_RETAINED",
    "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
    "NO_R_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

TWO_NINTHS_INPUTS = {
    "TWO_NINTHS_READOUT_TEXT_LOCK",
    "FINITE_TWO_NINTHS_DENSITY_CONTEXT_ACCEPTED",
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
    "FOLD_AND_BRANCH_DOMAIN_LOCK",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K2_INPUTS = {
    "K2_EXACTNESS_TEXT_LOCK",
    "REGISTERED_PHI_VALUE_FACE_ACCEPTED",
    "DISTINGUISHED_TWO_NINTHS_THEOREM_RETAINED",
    "RADIAN_READOUT_LICENSE_RETAINED",
    "FOLD_AND_BRANCH_DOMAIN_LOCK",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

ELECTRON_MASS_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
}

HYDROGEN_INPUTS = ELECTRON_MASS_INPUTS | {
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
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


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


def closes_two_ninths(inputs: set[str]) -> bool:
    return TWO_NINTHS_INPUTS <= inputs


def closes_k2(inputs: set[str]) -> bool:
    return K2_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        H_CLASS_TARGET,
        H_CLASS_DECISION,
        H_UNIT_CURRENT,
        H_UNIT_DECISION,
        R_ETA_CURRENT,
        R_ETA_TARGET,
        R_ETA_DECISION,
        K2_TARGET,
        TWO_NINTHS_TARGET,
        PHYSICAL_ELECTRON,
        PR5019_IMPACT,
        PR5020_IMPACT,
        PR5022_IMPACT,
        AC_R_ETA_CLUSTER,
        R_ETA_NARROWING,
        R_ETA_W2,
        FIXED_LOCUS,
        FLAVOR_ASYMMETRY,
        OPERATOR_DENSITY,
        AMBIENT_FACE,
        K_EVEN_PATTERN,
        PRIMITIVE_REGISTRY,
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
        "Koide R-Eta H-Class Fixed-Locus Current-Surface No-Go",
        "current-surface no-go / import-retirement subtarget",
        "does not ratify `R_ETA_H_CLASS_RETAINED`",
        "current retained, primitive, merged-PR, and open-PR surfaces do not",
        "R_ETA_H_CLASS_RETAINED",
        "R_ETA_H_CLASS_TEXT_LOCK",
        "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
        "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
        "SUPPLIED_CONTEXT_REGISTRABILITY_ACCEPTED",
        "AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_ACCEPTED",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
        "NO_H_UNIT_OR_RADIAN_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "L3(1,2) = 2/9",
        "AB/Lefschetz fixed-locus",
        "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
        "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md",
        "FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md",
        "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md",
        "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md",
        "ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md",
        "merged `#5020` Koide R-eta value-face registered-angle/exactness relocation",
        "merged `#5022` delta-eta chain R-eta supplied-premise audit repair",
        "merged `#5019` Koide `AC_phi_lambda` axiom-surface rebase",
        "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
        "`#4986` AC R-eta h-class stretch no-go",
        "`#4984` AC R-eta direct-license no-go",
        "`#4981` AC R-eta C3 ratification non-supply",
        "merged `#5023` Koide W4 audit-readiness repairs",
        "merged `#5024` Koide W4 gate-note premise minimization and substep1 rebase",
        "#5023/#5024 W4 gate route",
        "`#5021` primitive-retirement review draft",
        "no primitive retirement and no registry edit",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad h-class current-surface no-go fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    full_inputs = set(H_CLASS_INPUTS)
    audit.check("full h-class contract accepts handoff", closes_h_class(full_inputs))
    for missing in sorted(H_CLASS_INPUTS):
        reduced = set(H_CLASS_INPUTS)
        reduced.remove(missing)
        audit.check(f"h-class handoff fails without {missing}", not closes_h_class(reduced))
    accepted_subsets = [subset for subset in all_subsets(H_CLASS_INPUTS) if closes_h_class(subset)]
    audit.check("only full h-class subset closes handoff", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close h-class", not closes_h_class(set(CURRENT_SURFACE_INPUTS)))

    consequence = {"R_ETA_H_CLASS_RETAINED"}
    audit.check("h-class consequence alone does not close R-eta retirement", not closes_r_eta(consequence))
    audit.check("h-class consequence alone does not close two-ninths subgate", not closes_two_ninths(consequence))
    audit.check("h-class consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("h-class consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("h-class consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    h_class_target = read(H_CLASS_TARGET)
    h_class_decision = read(H_CLASS_DECISION)
    h_unit_current = read(H_UNIT_CURRENT)
    h_unit_decision = read(H_UNIT_DECISION)
    r_eta_current = read(R_ETA_CURRENT)
    r_eta_target = read(R_ETA_TARGET)
    r_eta_decision = read(R_ETA_DECISION)
    k2_target = read(K2_TARGET)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    physical_electron = read(PHYSICAL_ELECTRON)
    pr5019 = read(PR5019_IMPACT)
    pr5020 = read(PR5020_IMPACT)
    pr5022 = read(PR5022_IMPACT)
    ac_r_eta_cluster = read(AC_R_ETA_CLUSTER)
    narrowing = read(R_ETA_NARROWING)
    w2 = read(R_ETA_W2)
    fixed_locus = read(FIXED_LOCUS)
    flavor_asymmetry = read(FLAVOR_ASYMMETRY)
    operator_density = read(OPERATOR_DENSITY)
    ambient = read(AMBIENT_FACE)
    k_even = read(K_EVEN_PATTERN)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("R-eta current no-go", r_eta_current),
        ("h-class target", h_class_target),
        ("h-class decision packet", h_class_decision),
    ]:
        audit.check(
            f"{label} references h-class current no-go",
            NOTE.name in container and "R_ETA_H_CLASS_RETAINED" in container,
        )

    audit.check("h-class target names same thirteen-input contract", H_CLASS_INPUTS <= set(h_class_target.split()))
    audit.check("h-class decision names same thirteen-input contract", H_CLASS_INPUTS <= set(h_class_decision.split()))
    audit.check("h-unit current no-go stays independent", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit_current and "R_ETA_H_CLASS_RETAINED" in h_unit_current)
    audit.check("h-unit decision stays independent", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit_decision and "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`." in h_unit_decision)
    audit.check("R-eta target consumes h-class as one subinput", "R_ETA_H_CLASS_RETAINED" in r_eta_target)
    audit.check("R-eta decision consumes h-class as one subinput", "R_ETA_H_CLASS_RETAINED" in r_eta_decision)
    audit.check(
        "R-eta current no-go keeps h-class open",
        "R_ETA_H_CLASS_RETAINED" in r_eta_current
        and NOTE.name in r_eta_current
        and "current-surface non-supply boundary" in r_eta_current,
    )
    audit.check("two-ninths target remains downstream", "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths_target)
    audit.check("K2 target remains downstream", "K2_R_ETA_EXACTNESS_RETAINED" in k2_target)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)

    audit.check("R-eta narrowing splits h-class and h-unit", "A_R-eta" in narrowing and "h-class" in narrowing and "h-unit" in narrowing)
    audit.check("W2 bridge closes supplied context only", "closes only piece 1" in w2 and "physical charged-lepton carrier must be shown" in w2)
    audit.check("fixed-locus source forces unique trace-free pair", "unique trace-free pair" in fixed_locus and "2/9" in fixed_locus)
    audit.check("fixed-locus source excludes physical readout", "physical single-summand readout" in fixed_locus)
    audit.check("flavor asymmetry source keeps physical readout open", "Physical readout is the one remaining gate" in flavor_asymmetry)
    audit.check("operator-density source keeps physical readout bridge open", "physical readout bridge" in operator_density and "single fixed-point local" in operator_density)
    audit.check("ambient face supplies no physical normalization", "No physical-normalization selection is supplied" in ambient)
    audit.check("registered-pattern note keeps value as registered data", "realized-state registered data" in k_even and "not deriving `delta = 2/9`" in k_even)
    audit.check("#5019 impact remains premise hygiene", "premise-hygiene" in pr5019 or "premise hygiene" in pr5019)
    audit.check("#5020 impact keeps exactness residual open", "exactness remains open" in pr5020)
    audit.check("#5022 impact keeps R-eta supplied, not derived", "supplied" in pr5022 and "no retained R-eta derivation" in pr5022)
    audit.check(
        "AC R-eta cluster keeps h-class open",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`." in ac_r_eta_cluster
        and "No spending of `#4982`-`#4986` landed-main notes as retained K2 closure." in ac_r_eta_cluster,
    )
    audit.check("Tier-A registry still names R-eta admission", "R-eta" in tier_a and "density-read-as-angle" in tier_a)
    audit.check("realized primitive supplies no value", "no state" in realized_text and "or value is supplied" in flat(realized_text))

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "r_eta_h_class_primitive",
        "single_fixed_point_readout_primitive",
        "physical_carrier_context_primitive",
        "fixed_locus_readout_primitive",
        "r_eta_h_unit_identity_radian_primitive",
        "r_eta_readout_identification_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["mass ratio", "selector", "readout bridge", "normalization", "value", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5022` delta-eta chain R-eta supplied-premise audit repair | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, dirty",
        "`#4986` AC R-eta h-class stretch no-go | landed-main science commit after PR close",
        "`#4984` AC R-eta direct-license no-go | landed-main science commit after PR close",
        "`#4981` AC R-eta C3 ratification non-supply | open and lane-relevant",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | merged, audit success",
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | merged",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged",
        "`#5018`/`#5017` chirality/domain-wall stack | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation of physical carrier realization for the charged-lepton",
        "No derivation of a single fixed-point physical readout theorem.",
        "No derivation of R-eta from the current retained inventory alone.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "landed-main `#4984`/`#4986` supplies h-class fixed-locus retirement",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies h-class",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "physical carrier realization is derived",
        "single fixed-point readout theorem is derived",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
