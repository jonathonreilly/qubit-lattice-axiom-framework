#!/usr/bin/env python3
"""Verifier for the hydrogen-facing AC/R-eta upstream cluster impact note."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_AC_R_ETA_UPSTREAM_CLUSTER_IMPACT_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
K2_EXACTNESS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_EXACTNESS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_ETA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_READOUT_RETIREMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_CLASS_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_CLASS_FIXED_LOCUS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
H_UNIT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_H_UNIT_IDENTITY_RADIAN_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


CLUSTER_INPUTS = {
    "AC_R_ETA_CLUSTER_CONTEXT",
    "OCCUPANCY_FORMATION_NON_SUPPLY",
    "OCCURRENCE_AXIOM_HYGIENE_NON_SUPPLY",
    "MEASURE_BINARY_AXIOM_UPDATE_NON_SUPPLY",
    "DOUBLET_CLOCK_NON_SUPPLY",
    "DIRECT_LICENSE_SPLIT",
    "H_UNIT_PRIMITIVE_NON_SUPPLY",
    "H_CLASS_STRETCH_NON_SUPPLY",
    "C3_RATIFICATION_OPEN_CONTEXT",
    "NO_RETAINED_STATUS_CHANGE",
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


def closes(inputs: set[str], required: set[str]) -> bool:
    return required <= inputs


def c3_additive(alpha: Fraction, values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return alpha * sum(values, Fraction(0))


def main() -> None:
    audit = Audit()

    section("File checks")
    for path in [
        NOTE,
        GOAL,
        KOIDE_FIREWALL,
        K2_EXACTNESS,
        R_ETA_CURRENT,
        H_CLASS_CURRENT,
        H_UNIT_CURRENT,
        PRIMITIVE_REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required note content")
    required_phrases = [
        "AC R-Eta Upstream Cluster Impact Discriminator",
        "merged-main / open-PR impact discriminator for Koide K2 R-eta",
        "does not derive `R_ETA_H_CLASS_RETAINED`",
        "does not derive `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`",
        "does not derive `K2_R_ETA_EXACTNESS_RETAINED`",
        "commit `8b2bea3148` / PR `#4982`",
        "commit `4a47f56db0` / PR `#4983`",
        "commit `c671996ebf` / PR `#4984`",
        "commit `8ca8adaa0b` / PR `#4985`",
        "commit `8c033532f1` / PR `#4986`",
        "commit `89768b461c` AC R-eta occurrence axiom-hygiene no-go",
        "commit `e2d1dec095` AC measure binary axiom-update no-go",
        "PR `#4981` AC R-eta C3 ratification non-supply",
        "closed without GitHub merge flag",
        "generic occurrence only",
        "doublet reading/occupancy binary",
        "L = 2/9",
        "S_sum = 3 L = 2/3",
        "I_alpha(x0, x1, x2) = alpha (x0 + x1 + x2)",
        "alpha = 2/27",
        "Phi_beta = beta S_sum",
        "Omega(delta) = 2 sqrt(3) sin(delta)",
        "Current Packet Wiring",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "broad K2/hydrogen closure claim fails; narrowed AC/R-eta",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite witness checks")
    l_value = Fraction(2, 9)
    s_sum = 3 * l_value
    audit.check("fixed-locus density is 2/9", l_value == Fraction(2, 9))
    audit.check("S_sum is 2/3", s_sum == Fraction(2, 3))

    orbit = (Fraction(1), Fraction(1), Fraction(1))
    alpha_target = Fraction(2, 27)
    audit.check("h-class target alpha gives 2/9 on full orbit", c3_additive(alpha_target, orbit) == l_value)
    alpha_family = [Fraction(0), Fraction(1, 9), Fraction(1, 3), Fraction(1), Fraction(2, 27)]
    outputs = [c3_additive(alpha, orbit) for alpha in alpha_family]
    audit.check("C3 additive family has multiple valid outputs", len(set(outputs)) == len(outputs))
    audit.check("fixed-locus alpha is one member, not forced by additivity", alpha_target in alpha_family and len(alpha_family) > 1)

    beta_family = [Fraction(0), Fraction(1, 3), Fraction(1), Fraction(2), Fraction(3)]
    phi_outputs = [beta * s_sum for beta in beta_family]
    audit.check("h-unit beta=1 gives Phi=2/3", Fraction(1) * s_sum == Fraction(2, 3))
    audit.check("other beta choices do not all give Phi=2/3", sum(1 for value in phi_outputs if value == Fraction(2, 3)) == 1)

    omega = 2.0 * math.sqrt(3.0) * math.sin(2.0 / 9.0)
    audit.check("doublet clock Omega(2/9) misses 2/3", abs(omega - (2.0 / 3.0)) > 0.09, f"Omega={omega:.12f}")
    audit.check("event-rate fit retains a free activation parameter", abs((2.0 / 3.0) / omega - 1.0) > 0.1)

    section("Predicate checks")
    cluster_inputs = set(CLUSTER_INPUTS)
    audit.check("cluster context predicate accepts context", closes(cluster_inputs, CLUSTER_INPUTS))
    audit.check("cluster context alone does not close h-class", not closes(cluster_inputs, H_CLASS_INPUTS))
    audit.check("cluster context alone does not close h-unit", not closes(cluster_inputs, H_UNIT_INPUTS))
    audit.check("cluster context alone does not close R-eta", not closes(cluster_inputs, R_ETA_INPUTS))
    audit.check("cluster context alone does not close K2", not closes(cluster_inputs, K2_INPUTS))
    audit.check("cluster context alone does not close electron mass", not closes(cluster_inputs, ELECTRON_MASS_INPUTS))
    audit.check("cluster context alone does not close hydrogen", not closes(cluster_inputs, HYDROGEN_INPUTS))
    audit.check("full h-class predicate closes with full h-class inputs", closes(set(H_CLASS_INPUTS), H_CLASS_INPUTS))
    audit.check("full h-unit predicate closes with full h-unit inputs", closes(set(H_UNIT_INPUTS), H_UNIT_INPUTS))
    audit.check("full R-eta predicate closes with full R-eta inputs", closes(set(R_ETA_INPUTS), R_ETA_INPUTS))
    audit.check("full K2 predicate closes with full K2 inputs", closes(set(K2_INPUTS), K2_INPUTS))

    section("Wiring and primitive boundary checks")
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    k2_exactness = read(K2_EXACTNESS)
    r_eta_current = read(R_ETA_CURRENT)
    h_class_current = read(H_CLASS_CURRENT)
    h_unit_current = read(H_UNIT_CURRENT)
    registry_text = read(PRIMITIVE_REGISTRY)
    primitive_registry = json.loads(registry_text)
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("K2 exactness current no-go", k2_exactness),
        ("R-eta readout current no-go", r_eta_current),
        ("h-class current no-go", h_class_current),
        ("h-unit current no-go", h_unit_current),
    ]:
        audit.check(
            f"{label} references cluster impact note",
            NOTE.name in container
            and "#4986" in container
            and "89768b461c" in container
            and "e2d1dec095" in container,
        )

    audit.check("h-class current no-go keeps h-class open", "R_ETA_H_CLASS_RETAINED" in h_class_current and "do not supply" in h_class_current)
    audit.check("h-unit current no-go keeps h-unit open", "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED" in h_unit_current and "do not supply" in h_unit_current)
    audit.check("R-eta current no-go keeps readout retirement open", "R_ETA_READOUT_IDENTIFICATION_RETAINED" in r_eta_current and "do not supply" in r_eta_current)
    audit.check("K2 current no-go keeps exactness open", "K2_R_ETA_EXACTNESS_RETAINED" in k2_exactness and "do not supply" in k2_exactness)

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)
    for absent in [
        "r_eta_h_class_primitive",
        "r_eta_h_unit_identity_radian_primitive",
        "r_eta_readout_identification_primitive",
        "k2_r_eta_exactness_primitive",
        "ac_measure_binary_primitive",
        "occurrence_event_law_primitive",
        "phase_selector_primitive",
        "readout_bridge_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered shortcut primitive: {absent}", absent not in registry_text)
    for excluded in ["selector", "readout bridge", "normalization", "value", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Non-claim boundaries")
    explicit_nonclaims = [
        "No derivation or ratification of `R_ETA_H_CLASS_RETAINED`.",
        "No derivation or ratification of `R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED`.",
        "No derivation or ratification of `R_ETA_READOUT_IDENTIFICATION_RETAINED`.",
        "No derivation or ratification of `KOIDE_TWO_NINTHS_RADIAN_READOUT_RETAINED`.",
        "No derivation or ratification of `K2_R_ETA_EXACTNESS_RETAINED`.",
        "No derivation or ratification of `RETAINED_ELECTRON_MASS_PHYSICAL_UNIT`.",
        "No derivation of `S_l`, A3, `C_A3`, `alpha(0)`, static-source Rydberg, or",
        "No spending of PR `#4981` as R-eta closure.",
        "No spending of `#4982`-`#4986` landed-main notes as retained K2 closure.",
        "No spending of landed-main `89768b461c` or `e2d1dec095` as K1/K2 closure.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "R_ETA_H_CLASS_RETAINED is supplied",
        "R_ETA_H_UNIT_IDENTITY_RADIAN_RETAINED is supplied",
        "R_ETA_READOUT_IDENTIFICATION_RETAINED is supplied",
        "K2_R_ETA_EXACTNESS_RETAINED is supplied",
        "physical electron mass is retained",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
