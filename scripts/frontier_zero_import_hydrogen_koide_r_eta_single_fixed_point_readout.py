#!/usr/bin/env python3
"""Verifier for the Koide R-eta single fixed-point readout lane."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SINGLE_FIXED_POINT_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SINGLE_FIXED_POINT_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SINGLE_FIXED_POINT_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
H_CLASS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_TARGET_DISCRIMINATOR_2026-07-05.md"
H_CLASS_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_RATIFICATION_DECISION_PACKET_2026-07-05.md"
H_CLASS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_CARRIER_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_PHYSICAL_CARRIER_CONTEXT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
R_ETA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_UNIT_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
TWO_NINTHS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_TWO_NINTHS_RADIAN_READOUT_TARGET_DISCRIMINATOR_2026-07-05.md"
K2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_TARGET_DISCRIMINATOR_2026-07-05.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PR5030_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
FIXED_LOCUS = ROOT / "docs" / "KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md"
FLAVOR_ASYMMETRY = ROOT / "docs" / "FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31.md"
OPERATOR_DENSITY = ROOT / "docs" / "FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md"
LOCAL_CAR = ROOT / "docs" / "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md"
GATE_COLLAPSE = ROOT / "docs" / "FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31.md"
AMBIENT_FACE = ROOT / "docs" / "ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md"
K_EVEN_PATTERN = ROOT / "docs" / "ACPHILAMBDA_K_EVEN_REGISTRATION_CORRECTION_REGISTERED_PATTERN_2026-07-02.md"
W2 = ROOT / "docs" / "ACPHILAMBDA_R_ETA_W2_REGISTRABILITY_CONTEXT_BRIDGE_NOTE_2026-06-18.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


READOUT_INPUTS = {
    "SINGLE_FIXED_POINT_READOUT_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "LOCAL_CAR_DENSITY_READOUT_BRIDGE_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_BOUNDARY_ACCOUNTED",
    "GLOBAL_ETA_EQUIVARIANT_ZERO_EXCLUDED_AS_READOUT",
    "EXTENSIVE_SUM_READOUT_EXCLUDED",
    "OTHER_K_EVEN_FUNCTIONAL_EXCLUDED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = {
    "SINGLE_FIXED_POINT_READOUT_TEXT_LOCK",
    "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
    "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
    "LOCAL_CAR_DENSITY_READOUT_BRIDGE_ACCEPTED",
    "PHYSICAL_CARRIER_CONTEXT_BOUNDARY_ACCOUNTED",
    "NO_H_UNIT_OR_RADIAN_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
}

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


def closes_readout(inputs: set[str]) -> bool:
    return READOUT_INPUTS <= inputs


def closes_h_class(inputs: set[str]) -> bool:
    return H_CLASS_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


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
        TARGET,
        DECISION,
        CURRENT,
        GOAL,
        KOIDE_FIREWALL,
        H_CLASS_TARGET,
        H_CLASS_DECISION,
        H_CLASS_CURRENT,
        PHYSICAL_CARRIER_TARGET,
        R_ETA_TARGET,
        R_ETA_DECISION,
        R_ETA_CURRENT,
        H_UNIT_TARGET,
        TWO_NINTHS_TARGET,
        K2_TARGET,
        PHYSICAL_ELECTRON,
        PR5030_IMPACT,
        FIXED_LOCUS,
        FLAVOR_ASYMMETRY,
        OPERATOR_DENSITY,
        LOCAL_CAR,
        GATE_COLLAPSE,
        AMBIENT_FACE,
        K_EVEN_PATTERN,
        W2,
        PRIMITIVE_REGISTRY,
        TIER_A_REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    target = read(TARGET)
    decision = read(DECISION)
    current = read(CURRENT)
    packet = "\n".join([target, decision, current])
    packet_flat = flat(packet)

    section("Required packet content")
    required_phrases = [
        "Koide R-Eta Single Fixed-Point Readout Target Discriminator",
        "Koide R-Eta Single Fixed-Point Readout Ratification Decision Packet",
        "Koide R-Eta Single Fixed-Point Readout Current-Surface No-Go",
        "target discriminator / Koide R-eta h-class readout-selection handoff",
        "decision packet / Koide R-eta h-class readout-selection handoff",
        "current-surface no-go / Koide R-eta h-class readout-selection handoff",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED",
        "SINGLE_FIXED_POINT_READOUT_TEXT_LOCK",
        "FIXED_LOCUS_WEIGHT_DENSITY_ACCEPTED",
        "FINITE_KS_LOCAL_DENSITY_OPERATOR_FACE_ACCEPTED",
        "LOCAL_CAR_DENSITY_READOUT_BRIDGE_ACCEPTED",
        "PHYSICAL_CARRIER_CONTEXT_BOUNDARY_ACCOUNTED",
        "GLOBAL_ETA_EQUIVARIANT_ZERO_EXCLUDED_AS_READOUT",
        "EXTENSIVE_SUM_READOUT_EXCLUDED",
        "OTHER_K_EVEN_FUNCTIONAL_EXCLUDED",
        "NO_H_UNIT_OR_RADIAN_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset",
        "The primitive registry was checked",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply",
        "broad single-fixed-point-readout claim fails; narrowed target",
        "broad single-fixed-point-readout retained claim fails",
        "broad single-fixed-point-readout current-surface no-go fails",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker repeated in packet: {marker}", packet.count(marker) >= 3)

    section("Predicate checks")
    full_inputs = set(READOUT_INPUTS)
    audit.check("full readout contract accepts handoff", closes_readout(full_inputs))
    for missing in sorted(READOUT_INPUTS):
        reduced = set(READOUT_INPUTS)
        reduced.remove(missing)
        audit.check(f"readout handoff fails without {missing}", not closes_readout(reduced))
    accepted_subsets = [subset for subset in all_subsets(READOUT_INPUTS) if closes_readout(subset)]
    audit.check("only full readout subset closes handoff", accepted_subsets == [full_inputs])
    audit.check("current surface inputs do not close readout", not closes_readout(set(CURRENT_SURFACE_INPUTS)))

    consequence = {"SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED"}
    audit.check("readout consequence alone does not close h-class", not closes_h_class(consequence))
    audit.check("readout plus carrier context still does not close h-class", not closes_h_class(consequence | {"PHYSICAL_CARRIER_CONTEXT_RETAINED"}))
    audit.check("readout consequence alone does not close R-eta", not closes_r_eta(consequence))
    audit.check("readout consequence alone does not close K2 exactness", not closes_k2(consequence))
    audit.check("readout consequence alone does not close electron mass", not closes_electron_mass(consequence))
    audit.check("readout consequence alone does not close hydrogen", not closes_hydrogen(consequence))

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    h_class_target = read(H_CLASS_TARGET)
    h_class_decision = read(H_CLASS_DECISION)
    h_class_current = read(H_CLASS_CURRENT)
    physical_carrier_target = read(PHYSICAL_CARRIER_TARGET)
    r_eta_target = read(R_ETA_TARGET)
    r_eta_decision = read(R_ETA_DECISION)
    r_eta_current = read(R_ETA_CURRENT)
    h_unit = read(H_UNIT_TARGET)
    two_ninths = read(TWO_NINTHS_TARGET)
    k2 = read(K2_TARGET)
    physical_electron = read(PHYSICAL_ELECTRON)
    pr5030 = read(PR5030_IMPACT)
    fixed_locus = read(FIXED_LOCUS)
    flavor_asymmetry = read(FLAVOR_ASYMMETRY)
    operator_density = read(OPERATOR_DENSITY)
    local_car = read(LOCAL_CAR)
    gate_collapse = read(GATE_COLLAPSE)
    ambient = read(AMBIENT_FACE)
    k_even = read(K_EVEN_PATTERN)
    w2 = read(W2)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    tier_a = read(TIER_A_REGISTRY)
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    realized = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("h-class target", h_class_target),
        ("h-class decision", h_class_decision),
        ("h-class current no-go", h_class_current),
    ]:
        audit.check(
            f"{label} references readout lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED" in container,
        )

    audit.check("physical carrier target keeps readout separate", "NO_SINGLE_FIXED_POINT_READOUT_INPUT" in physical_carrier_target)
    audit.check("R-eta target consumes h-class, not readout directly", "R_ETA_H_CLASS_RETAINED" in r_eta_target)
    audit.check("R-eta decision remains downstream", "R_ETA_READOUT_IDENTIFICATION_RETAINED" in r_eta_decision)
    audit.check("R-eta current no-go keeps h-class open", "R_ETA_H_CLASS_RETAINED" in r_eta_current)
    audit.check("h-unit target remains independent", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit)
    audit.check("two-ninths target remains downstream", "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED" in two_ninths)
    audit.check("K2 target remains downstream", "K2_R_ETA_EXACTNESS_RETAINED" in k2)
    audit.check("physical electron packet remains downstream", "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT" in physical_electron)
    audit.check("PR5030 impact excludes readout theorem", "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`." in pr5030)

    audit.check("fixed-locus source forces local density", "local density `2/9`" in fixed_locus and "unique trace-free pair" in fixed_locus)
    audit.check("fixed-locus source excludes physical readout", "physical single-summand readout" in fixed_locus)
    audit.check("flavor asymmetry keeps physical readout open", "Physical readout is the one remaining gate" in flavor_asymmetry)
    audit.check("operator-density source keeps physical bridge open", "physical readout bridge" in operator_density and "single fixed-point local" in operator_density)
    audit.check("local CAR bridge is one-mode only", "finite local density/readout bridge for the one-mode" in local_car and "does not derive the full Kawamoto-Smit" in local_car)
    audit.check("gate-collapse row is open gate", "open_gate" in gate_collapse and "Axiom 2 locality is genuinely silent" in gate_collapse)
    audit.check("gate-collapse row admits intensive and extensive", "admits **both** intensive densities" in gate_collapse and "extensive quasi-local sums" in gate_collapse)
    audit.check("ambient face supplies no physical normalization", "No physical-normalization selection is supplied" in ambient)
    audit.check("K-even pattern keeps value as registered data", "value is realized-state registered data" in k_even and "not deriving `delta = 2/9`" in k_even)
    audit.check("W2 bridge leaves physical carrier open", "physical charged-lepton carrier must be shown" in w2)
    audit.check("Tier-A registry still names R-eta admission", "R-eta" in tier_a and "density-read-as-angle" in tier_a)
    audit.check("realized primitive supplies no value", "no state" in realized and "or value is supplied" in flat(realized))

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "single_fixed_point_readout_primitive",
        "readout_selector_primitive",
        "r_eta_h_class_primitive",
        "physical_carrier_context_primitive",
        "r_eta_h_unit_identity_radian_primitive",
        "r_eta_readout_identification_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "normalization", "value", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open PR and non-claim boundaries")
    current_flat = flat(current)
    open_markers = [
        "`#5030` multisite Pauli finite-carrier provenance | open, audit success at refresh",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, dirty, audit success",
        "`#5022` delta-eta chain R-eta supplied-premise audit repair | merged, audit success",
        "`#5020` Koide R-eta value-face registered-angle/exactness relocation | merged",
        "`#5017`/`#5018` chirality/domain-wall stack | open, audit success",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in open_markers:
        audit.check(f"open PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_CARRIER_CONTEXT_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies single fixed-point readout",
        "This packet ratifies single fixed-point readout",
        "SINGLE_FIXED_POINT_READOUT_THEOREM_RETAINED is supplied",
        "PHYSICAL_CARRIER_CONTEXT_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "hydrogen retained theorem",
        "This note claims hydrogen is retained",
        "**Status:** retained",
        "**Status:** proposed_retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in packet)

    audit.summary()


if __name__ == "__main__":
    main()
