#!/usr/bin/env python3
"""Verifier for the Koide R-eta h-unit current-surface no-go."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
H_UNIT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_RATIFICATION_DECISION_PACKET_2026-07-05.md"
R_ETA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5019_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ACPHILAMBDA_PR5019_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5020_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_VALUE_FACE_PR5020_IMPACT_DISCRIMINATOR_2026-07-05.md"
PR5022_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_DELTA_ETA_PR5022_IMPACT_DISCRIMINATOR_2026-07-05.md"
AC_R_ETA_CLUSTER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md"
DEFECT_UNIT = ROOT / "docs" / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
CYCLE_HOLONOMY = ROOT / "docs" / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
A1_RADIAN = ROOT / "docs" / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
Z3_RADIAN = ROOT / "docs" / "KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md"
BRANNEN_CONVENTION = ROOT / "docs" / "BRANNEN_DELTA_SPECTRAL_ASYMMETRY_CONVENTION_ISOLATION_NOTE_2026-05-31.md"
PHASE_UNIT = ROOT / "docs" / "PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


H_UNIT_INPUTS = {
    "R_ETA_H_UNIT_TEXT_LOCK",
    "DEFECT_IDENTITY_UNIT_NORMAL_FORM_ACCEPTED",
    "ANGLE_SIDE_RIGIDITY_ACCEPTED",
    "TYPE_B_TO_RADIAN_RESIDUAL_ALIGNMENT_ACCEPTED",
    "IDENTITY_UNIT_SELECTION_THEOREM_RETAINED",
    "NO_COUNT_NORMALIZATION_SHORTCUT",
    "NO_H_CLASS_CARRIER_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = {
    "R_ETA_H_UNIT_TEXT_LOCK",
    "DEFECT_IDENTITY_UNIT_NORMAL_FORM_ACCEPTED",
    "ANGLE_SIDE_RIGIDITY_ACCEPTED",
    "TYPE_B_TO_RADIAN_RESIDUAL_ALIGNMENT_ACCEPTED",
    "NO_COUNT_NORMALIZATION_SHORTCUT",
    "NO_H_CLASS_CARRIER_OR_MASS_INPUT",
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


def closes_h_unit(inputs: set[str]) -> bool:
    return H_UNIT_INPUTS <= inputs


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
        H_UNIT_TARGET,
        H_UNIT_DECISION,
        R_ETA_CURRENT,
        R_ETA_TARGET,
        R_ETA_DECISION,
        H_CLASS_TARGET,
        H_CLASS_DECISION,
        K2_TARGET,
        TWO_NINTHS_TARGET,
        PHYSICAL_ELECTRON,
        PR5019_IMPACT,
        PR5020_IMPACT,
        PR5022_IMPACT,
        AC_R_ETA_CLUSTER,
        DEFECT_UNIT,
        CYCLE_HOLONOMY,
        A1_RADIAN,
        Z3_RADIAN,
        BRANNEN_CONVENTION,
        PHASE_UNIT,
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
        "Koide R-Eta H-Unit Identity-Radian Current-Surface No-Go",
        "current-surface no-go / import-retirement subtarget",
        "does not ratify `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`",
        "current retained, primitive, merged-PR, and open-PR surfaces do not",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED",
        "R_ETA_H_UNIT_TEXT_LOCK",
        "DEFECT_IDENTITY_UNIT_NORMAL_FORM_ACCEPTED",
        "ANGLE_SIDE_RIGIDITY_ACCEPTED",
        "TYPE_B_TO_RADIAN_RESIDUAL_ALIGNMENT_ACCEPTED",
        "IDENTITY_UNIT_SELECTION_THEOREM_RETAINED",
        "NO_COUNT_NORMALIZATION_SHORTCUT",
        "NO_H_CLASS_CARRIER_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "I_c(R) = c * |R| * L",
        "c = 1",
        "Phi = 2/3",
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md",
        "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md",
        "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md",
        "BRANNEN_DELTA_SPECTRAL_ASYMMETRY_CONVENTION_ISOLATION_NOTE_2026-05-31.md",
        "PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md",
        "merged `#5020` Koide R-eta value-face registered-angle/exactness relocation",
        "merged `#5022` delta-eta chain R-eta supplied-premise audit repair",
        "merged `#5019` Koide `AC_phi_lambda` axiom-surface rebase",
        "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ACPHILAMBDA_R_ETA_HUNIT_APPROVED_PRIMITIVE_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md",
        "ACPHILAMBDA_R_ETA_DOUBLET_CLOCK_RATE_NORMALIZATION_NO_GO_NOTE_2026-07-04.md",
        "`#4985` AC R-eta h-unit primitive no-go",
        "`#4984` AC R-eta direct-license no-go",
        "`#4983` AC R-eta doublet-clock no-go",
        "`#4981` AC R-eta C3 ratification non-supply",
        "`#5021` primitive-retirement review draft",
        "no primitive retirement and no registry edit",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad h-unit current-surface no-go fails; narrowed",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    full_inputs = set(H_UNIT_INPUTS)
    audit.check("full h-unit contract accepts handoff", closes_h_unit(full_inputs))
    for missing in sorted(H_UNIT_INPUTS):
        reduced = set(H_UNIT_INPUTS)
        reduced.remove(missing)
        audit.check(f"h-unit handoff fails without {missing}", not closes_h_unit(reduced))
    accepted_subsets = [subset for subset in all_subsets(H_UNIT_INPUTS) if closes_h_unit(subset)]
    audit.check("only full h-unit subset closes handoff", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close h-unit", not closes_h_unit(set(CURRENT_SURFACE_INPUTS)))

    consequence = {"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}
    audit.check("h-unit consequence alone does not close R-eta retirement", not closes_r_eta(consequence))
    audit.check("h-unit consequence alone does not close two-ninths subgate", not closes_two_ninths(consequence))
    audit.check("h-unit consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("h-unit consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("h-unit consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    h_unit_target = read(H_UNIT_TARGET)
    h_unit_decision = read(H_UNIT_DECISION)
    r_eta_current = read(R_ETA_CURRENT)
    r_eta_target = read(R_ETA_TARGET)
    r_eta_decision = read(R_ETA_DECISION)
    h_class_target = read(H_CLASS_TARGET)
    h_class_decision = read(H_CLASS_DECISION)
    k2_target = read(K2_TARGET)
    two_ninths_target = read(TWO_NINTHS_TARGET)
    physical_electron = read(PHYSICAL_ELECTRON)
    pr5019 = read(PR5019_IMPACT)
    pr5020 = read(PR5020_IMPACT)
    pr5022 = read(PR5022_IMPACT)
    ac_r_eta_cluster = read(AC_R_ETA_CLUSTER)
    defect_unit = read(DEFECT_UNIT)
    cycle = read(CYCLE_HOLONOMY)
    a1_radian = read(A1_RADIAN)
    z3_radian = read(Z3_RADIAN)
    brannen = read(BRANNEN_CONVENTION)
    phase_unit = read(PHASE_UNIT)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("R-eta current no-go", r_eta_current),
        ("h-unit target", h_unit_target),
        ("h-unit decision packet", h_unit_decision),
    ]:
        audit.check(
            f"{label} references h-unit current no-go",
            NOTE.name in container and "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in container,
        )

    audit.check("h-unit target names same eleven-input contract", H_UNIT_INPUTS <= set(h_unit_target.split()))
    audit.check("h-unit decision names same eleven-input contract", H_UNIT_INPUTS <= set(h_unit_decision.split()))
    audit.check("R-eta target consumes h-unit as one subinput", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in r_eta_target)
    audit.check("R-eta decision consumes h-unit as one subinput", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in r_eta_decision)
    audit.check("h-class target stays independent", "R_ETA_H_CLASS_RETAINED" in h_class_target and "does not supply `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`" in h_class_target)
    audit.check(
        "h-class decision stays independent",
        "R_ETA_H_CLASS_RETAINED" in h_class_decision
        and "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_class_decision
        and "h-class <-> h-unit" in h_class_decision,
    )
    audit.check("two-ninths target remains downstream", "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths_target)
    audit.check("K2 target remains downstream", "K2_R_ETA_EXACTNESS_RETAINED" in k2_target)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)

    audit.check("defect-unit note derives normal form", "I_c(R) = c * |R| * L" in defect_unit)
    audit.check(
        "defect-unit note blocks homogeneous c=1 route",
        "no derivation drawn from this scanned surface can single out" in flat(defect_unit),
    )
    audit.check("defect-unit note says count pins wrong member", "c = u / L = 1 / (2/9) = 9/2" in defect_unit)
    audit.check("cycle holonomy note states equivalent coordinate", "c = 1  <=>  Phi = S_sum = 2/3" in cycle)
    audit.check("cycle holonomy note does not derive value", "No derivation is supplied for `Phi = 2/3`." in cycle)
    audit.check("A1 radian bridge keeps Type-B primitive open", "TYPE_B_TO_RADIAN_IDENTIFICATION_REMAINS_PRIMITIVE=TRUE" in a1_radian)
    audit.check("Z3 radian bridge source is present", "KOIDE_Z3_QUBIT_RADIAN_BRIDGE" in Z3_RADIAN.name and len(z3_radian) > 0)
    audit.check("Brannen convention source is present", "2/9" in brannen and len(brannen) > 0)
    audit.check("phase-unit source is present", "U(1)" in phase_unit or "phase" in phase_unit)
    audit.check("#5019 impact remains premise hygiene", "premise-hygiene" in pr5019 or "premise hygiene" in pr5019)
    audit.check("#5020 impact keeps exactness residual open", "exactness remains open" in pr5020)
    audit.check("#5022 impact keeps R-eta supplied, not derived", "supplied" in pr5022 and "no retained R-eta derivation" in pr5022)
    audit.check(
        "AC R-eta cluster keeps h-unit open",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`." in ac_r_eta_cluster
        and "No spending of landed-main `89768b461c` or `e2d1dec095` as K1/K2 closure." in ac_r_eta_cluster,
    )
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in primitive_nodes)
    audit.check("realized primitive supplies no value", "no state" in realized_text and "or value is supplied" in flat(realized_text))

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "r_eta_h_unit_primitive",
        "r_eta_h_unit_identity_radian_primitive",
        "identity_radian_primitive",
        "phase_selector_primitive",
        "readout_bridge_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["mass ratio", "phase", "selector", "readout bridge", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    open_markers = [
        "`#5022` delta-eta chain R-eta supplied-premise audit repair | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, dirty",
        "`#4985` AC R-eta h-unit primitive no-go | landed-main science commit after PR close",
        "`#4984` AC R-eta direct-license no-go | landed-main science commit after PR close",
        "`#4983` AC R-eta doublet-clock no-go | landed-main science commit after PR close",
        "`#4981` AC R-eta C3 ratification non-supply | open and lane-relevant",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | merged",
        "`#5019` Koide `AC_phi_lambda` axiom-surface rebase | merged",
        "`#5018`/`#5017` chirality/domain-wall stack | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation of `c = 1` from Record additivity, count normalization, or",
        "No derivation of `Phi = 2/3`.",
        "No derivation of R-eta from the current retained inventory alone.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "landed-main `#4983`/`#4984`/`#4985` supplies",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies h-unit",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "Phi = 2/3 is derived",
        "c = 1 is derived",
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
