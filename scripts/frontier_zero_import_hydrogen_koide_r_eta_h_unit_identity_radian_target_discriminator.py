#!/usr/bin/env python3
"""Verifier for the hydrogen-facing Koide R-eta h-unit target."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
R_ETA_RETIREMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_TARGET_DISCRIMINATOR_2026-07-05.md"
R_ETA_NARROWING = ROOT / "docs" / "ACPHILAMBDA_R_ETA_READOUT_IDENTIFICATION_NARROWING_BOUNDED_THEOREM_NOTE_2026-06-11.md"
DEFECT_UNIT = ROOT / "docs" / "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md"
A1_RADIAN = ROOT / "docs" / "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md"
Z3_RADIAN = ROOT / "docs" / "KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md"
BRANNEN_CONVENTION = ROOT / "docs" / "BRANNEN_DELTA_SPECTRAL_ASYMMETRY_CONVENTION_ISOLATION_NOTE_2026-05-31.md"
PHASE_UNIT = ROOT / "docs" / "PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md"
CYCLE_HOLONOMY = ROOT / "docs" / "ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01.md"
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

R_ETA_RETIREMENT_INPUTS = {
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

TWO_NINTHS_SUBGATE_INPUTS = {
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

K2_EXACTNESS_INPUTS = {
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


def closes_r_eta_retirement(inputs: set[str]) -> bool:
    return R_ETA_RETIREMENT_INPUTS <= inputs


def closes_two_ninths_subgate(inputs: set[str]) -> bool:
    return TWO_NINTHS_SUBGATE_INPUTS <= inputs


def closes_k2_exactness(inputs: set[str]) -> bool:
    return K2_EXACTNESS_INPUTS <= inputs


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
        R_ETA_RETIREMENT,
        R_ETA_NARROWING,
        DEFECT_UNIT,
        A1_RADIAN,
        Z3_RADIAN,
        BRANNEN_CONVENTION,
        PHASE_UNIT,
        CYCLE_HOLONOMY,
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
        "Koide R-Eta H-Unit Identity-Radian Target Discriminator",
        "target discriminator / Koide R-eta h-unit import-retirement handoff",
        "does not ratify `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`",
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
        "ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01.md",
        "KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md",
        "KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md",
        "BRANNEN_DELTA_SPECTRAL_ASYMMETRY_CONVENTION_ISOLATION_NOTE_2026-05-31.md",
        "PLANCK_TARGET3_PHASE_UNIT_EDGE_STATISTICS_BOUNDARY_NOTE_2026-04-25.md",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad h-unit-retained claim fails; narrowed identity-radian",
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
    audit.check(
        "h-unit supplies one proper input to R-eta retirement",
        {"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"} < R_ETA_RETIREMENT_INPUTS,
    )
    audit.check(
        "h-unit handoff alone does not close R-eta retirement",
        not closes_r_eta_retirement({"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}),
    )
    audit.check(
        "h-unit handoff alone does not close two-ninths subgate",
        not closes_two_ninths_subgate({"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}),
    )
    audit.check(
        "h-unit handoff alone does not close K2 exactness",
        not closes_k2_exactness({"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}),
    )
    audit.check(
        "h-unit handoff alone does not close electron mass",
        not closes_electron_mass({"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}),
    )
    audit.check(
        "h-unit handoff alone does not close hydrogen",
        not closes_hydrogen({"R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED"}),
    )

    section("Authority and source-boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    r_eta_retirement = read(R_ETA_RETIREMENT)
    r_eta_narrowing = read(R_ETA_NARROWING)
    defect_unit = read(DEFECT_UNIT)
    a1_radian = read(A1_RADIAN)
    z3_radian = read(Z3_RADIAN)
    brannen = read(BRANNEN_CONVENTION)
    phase_unit = read(PHASE_UNIT)
    cycle_holonomy = read(CYCLE_HOLONOMY)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])
    tier_a_text = read(TIER_A_REGISTRY)
    realized_text = read(REALIZED)

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", koide_firewall),
        ("R-eta retirement target", r_eta_retirement),
    ]:
        audit.check(
            f"{label} references h-unit target",
            NOTE.name in container and "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in container,
        )

    audit.check("R-eta narrowing splits h-class and h-unit", "h-class" in r_eta_narrowing and "h-unit" in r_eta_narrowing)
    audit.check("R-eta narrowing keeps h-unit admitted", "h-unit" in r_eta_narrowing and "neither derived here" in r_eta_narrowing)
    audit.check("defect unit defines identity-unit wall", "W_defect_identity_unit" in defect_unit and "identity-unit member is `c=1`" in defect_unit)
    audit.check(
        "defect unit proves rescale obstruction",
        "rescale-invariant" in defect_unit
        and "no derivation drawn from this scanned surface can single out the identity-unit member `c = 1`"
        in flat(defect_unit),
    )
    audit.check("defect unit count pins wrong member", "c = u / L = 1 / (2/9) = 9/2  !=  1" in defect_unit)
    audit.check("defect unit localizes junction to R-eta", "R-eta sub-admission" in defect_unit and "density-to-angle junction" in defect_unit)
    audit.check("A1 audit keeps Type-B-to-radian primitive", "TYPE_B_TO_RADIAN_IDENTIFICATION_REMAINS_PRIMITIVE=TRUE" in a1_radian)
    audit.check("A1 audit sharpens period convention", "period-`1 rad` convention" in a1_radian and "canonical period-`2" in a1_radian)
    audit.check("Z3 no-go keeps pure-rational radian bridge missing", "Every retained radian" in z3_radian and "No such bridge is retained" in z3_radian)
    audit.check(
        "Brannen convention note does not adopt period-1 normalization",
        "does not adopt a period-1-radian normalization" in flat(brannen),
    )
    audit.check("phase-unit note supplies native U(1) but not selected value", "`U(1)` phase unit" in phase_unit and "does not derive" in phase_unit)
    audit.check("cycle holonomy identifies same junction wall", "W_cycle_holonomy_value == W_defect_identity_unit == R-eta junction coefficient" in cycle_holonomy)
    audit.check("Tier-A registry names R-eta sub-admission", "delta readout identification R-eta" in tier_a_text)
    audit.check("realized-state primitive supplies no value", "no state" in realized_text and "or value is supplied" in flat(realized_text))

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in primitive_nodes)
    for absent in [
        "r_eta_h_unit_identity_radian_primitive",
        "r_eta_h_class_primitive",
        "r_eta_readout_identification_primitive",
        "type_b_to_radian_primitive",
        "delta_exactness_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in primitive_nodes)
    for excluded in ["phase", "selector", "readout bridge", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation of R-eta from the current retained inventory alone.",
        "No derivation of `delta = 2/9` as a retained physical phase.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No use of observed lepton masses, fitted `Phi_PDG`, fitted `delta`, observed",
        "No derivation of K1 occupancy/counting, K3 physical species bridge, K4",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note derives R-eta",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "period-1-radian normalization is adopted",
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
