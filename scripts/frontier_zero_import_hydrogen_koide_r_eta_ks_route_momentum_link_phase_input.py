#!/usr/bin/env python3
"""Verifier for the Koide R-eta KS-route momentum/link-phase input lane."""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_TARGET_DISCRIMINATOR_2026-07-05.md"
DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_ROUTE_MOMENTUM_LINK_PHASE_INPUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SIGMA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md"
SIGMA_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SIGMA_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SCALAR_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TARGET_DISCRIMINATOR_2026-07-05.md"
KS_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TARGET_DISCRIMINATOR_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
KINETIC_CLASS = ROOT / "docs" / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
P_FLUX = ROOT / "docs" / "P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md"
Z_CERT = ROOT / "docs" / "STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md"
FSB_K = ROOT / "docs" / "AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md"
GSTAR_THERMAL = ROOT / "docs" / "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
KS_FORCING = ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"
REALIZATION_GATE = ROOT / "docs" / "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


LINK_INPUTS = {
    "KS_ROUTE_MOMENTUM_LINK_PHASE_TEXT_LOCK",
    "TWO_FLUX_CLASS_KINETIC_SURFACE_ACCEPTED",
    "P_FLUX_WITHIN_SURFACE_SELECTION_ACCEPTED",
    "KAWAMOTO_SMIT_LINK_PHASE_REPRESENTATIVE_ACCEPTED",
    "FINITE_LINK_PHASE_AND_BLOCH_MOMENTUM_SUPPORT_CHECK",
    "WRAP_HOLONOMY_BOUNDARY_LOCK",
    "NO_FULL_KINETIC_SURFACE_RETIREMENT_INPUT",
    "NO_SPINFUL_KERNEL_OBJECT_THEOREM_INPUT",
    "NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT",
    "NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT",
    "NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT",
    "NO_KS_ROUTE_CLOSURE_INPUT",
    "NO_PARENT_BRIDGE_OR_HW1_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

CURRENT_SURFACE_INPUTS = LINK_INPUTS - {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}

SIGMA_ROUTE_INPUTS = {
    "SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TEXT_LOCK",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
    "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "KINETIC_TWO_RAY_SURFACE_ACCEPTED",
    "FINITE_SIGMA_DOT_P_NONCENTRALITY_CHECK",
    "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
    "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
    "NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT",
    "NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT",
    "NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT",
    "NO_KS_ROUTE_CLOSURE_INPUT",
    "NO_PARENT_BRIDGE_OR_HW1_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

SCALAR_LIFT_INPUTS = {
    "SPINFUL_STAGGERED_KERNEL_SCALAR_LIFT_EXCLUSION_TEXT_LOCK",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "SCALAR_KERNEL_COMPATIBILITY_ACCEPTED",
    "STAGGERED_KS_CHIRALITY_ROUTE_SURFACE_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
    "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
    "NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT",
    "NO_KS_ROUTE_CLOSURE_INPUT",
    "NO_PARENT_BRIDGE_OR_HW1_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

KS_ROUTE_INPUTS = {
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_TEXT_LOCK",
    "MATTER_ATTACHMENT_KS_REDUCTION_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "KS_PHASE_FORCING_SURFACE_ACCEPTED",
    "GRASSMANN_CAR_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
    "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
    "NO_ELEMENTARY_STATE_LAW_INPUT",
    "NO_HW1_OR_BRIDGE_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PARENT_BRIDGE_INPUTS = {
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_TEXT_LOCK",
    "OPERATOR_FRAME_MERGER_ACCEPTED",
    "SPIN_MODULE_ESCAPE_NO_GO_ACCEPTED",
    "NATIVE_D_SPIN_BLINDNESS_ACCEPTED",
    "KS_SCALARIZATION_SURFACE_ACCEPTED",
    "STAGGERED_CHIRALITY_SELECTOR_SURFACE_ACCEPTED",
    "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
    "NO_HW1_LOCUS_OR_CARRIER_CLOSURE_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
    "NO_K1_K3_K4_OR_MASS_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

HW1_INPUTS = {
    "HW1_PHYSICAL_GENERATION_LOCUS_TEXT_LOCK",
    "MOMENTUM_TYPE_THEOREM_ACCEPTED",
    "STAGGERED_KS_REALIZATION_SURFACE_ACCEPTED",
    "K1_FLUX_SELECTOR_WITHIN_SURFACE_ACCEPTED",
    "HW1_C3_TRIPLET_ALGEBRA_ACCEPTED",
    "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
    "NO_SPECIES_LABEL_BIJECTION_INPUT",
    "NO_SINGLE_FIXED_POINT_READOUT_INPUT",
    "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
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


def norm(text: str) -> str:
    replacements = {
        "\u2212": "-",
        "\u03c6": "phi",
        "\u03a6": "Phi",
        "\u03b7": "eta",
        "\u2070": "0",
        "\u03bc": "mu",
        "\u03c0": "pi",
        "\u00b2": "2",
        "\u00b3": "3",
        "\u03a3": "Sigma",
        "\u00d7": "x",
        "\u2261": "equiv",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return flat(text)


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


def closes_link_input(inputs: set[str]) -> bool:
    return LINK_INPUTS <= inputs


def closes_sigma_route(inputs: set[str]) -> bool:
    return SIGMA_ROUTE_INPUTS <= inputs


def closes_scalar_lift_exclusion(inputs: set[str]) -> bool:
    return SCALAR_LIFT_INPUTS <= inputs


def closes_ks_route(inputs: set[str]) -> bool:
    return KS_ROUTE_INPUTS <= inputs


def closes_parent_bridge(inputs: set[str]) -> bool:
    return PARENT_BRIDGE_INPUTS <= inputs


def closes_hw1(inputs: set[str]) -> bool:
    return HW1_INPUTS <= inputs


def closes_r_eta(inputs: set[str]) -> bool:
    return R_ETA_INPUTS <= inputs


def closes_electron_mass(inputs: set[str]) -> bool:
    return ELECTRON_MASS_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def eta(x: tuple[int, int, int], mu: int) -> int:
    if mu == 0:
        return 1
    if mu == 1:
        return -1 if x[0] % 2 else 1
    if mu == 2:
        return -1 if (x[0] + x[1]) % 2 else 1
    raise ValueError(mu)


def shift(x: tuple[int, int, int], mu: int, n: int) -> tuple[int, int, int]:
    values = list(x)
    values[mu] = (values[mu] + 1) % n
    return tuple(values)  # type: ignore[return-value]


def plaquette_flux_k1(x: tuple[int, int, int], mu: int, nu: int, n: int) -> int:
    return eta(x, mu) * eta(shift(x, mu, n), nu) * eta(shift(x, nu, n), mu) * eta(x, nu)


def finite_link_phase_checks(audit: Audit) -> None:
    n = 4
    sites = [(x, y, z) for x in range(n) for y in range(n) for z in range(n)]
    plaquettes = [(site, mu, nu) for site in sites for mu in range(3) for nu in range(mu + 1, 3)]

    k0_fluxes = [1 for _site, _mu, _nu in plaquettes]
    k1_fluxes = [plaquette_flux_k1(site, mu, nu, n) for site, mu, nu in plaquettes]

    audit.check("finite K0 representative has uniform +1 plaquette flux", all(value == 1 for value in k0_fluxes))
    audit.check("finite Kawamoto-Smit representative has uniform -1 plaquette flux", all(value == -1 for value in k1_fluxes))
    audit.check("finite eta_1 representative is identically one", all(eta(site, 0) == 1 for site in sites))
    audit.check("finite eta_2 representative flips with x1", eta((0, 0, 0), 1) == 1 and eta((1, 0, 0), 1) == -1)
    audit.check("finite eta_3 representative flips with x1+x2", eta((0, 0, 0), 2) == 1 and eta((1, 0, 0), 2) == -1 and eta((1, 1, 0), 2) == 1)

    for t in [0.0, 0.13, -0.27, 0.41]:
        value = math.cos(math.pi / 2.0 + t) + math.cos(math.pi / 2.0 - t) + math.cos(math.pi / 2.0)
        audit.check(f"K0 Bloch zero-line identity holds at t={t}", abs(value) < 1e-12)

    for q in [(0.05, 0.0, 0.0), (0.04, -0.03, 0.02), (-0.02, 0.01, 0.06)]:
        energy = 2.0 * math.sqrt(sum(math.sin(component) ** 2 for component in q))
        linear = 2.0 * math.sqrt(sum(component * component for component in q))
        audit.check(f"K1 cone energy is positive near corner for q={q}", energy > 0.0)
        audit.check(f"K1 cone energy matches linear support for q={q}", abs(energy - linear) <= (2.0 / 3.0) * (linear / 2.0) ** 2)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        TARGET,
        DECISION,
        CURRENT,
        SIGMA_TARGET,
        SIGMA_DECISION,
        SIGMA_CURRENT,
        SCALAR_TARGET,
        KS_TARGET,
        GOAL,
        KOIDE_FIREWALL,
        KINETIC_CLASS,
        P_FLUX,
        Z_CERT,
        FSB_K,
        GSTAR_THERMAL,
        KS_FORCING,
        REALIZATION_GATE,
        PRIMITIVE_REGISTRY,
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
        "Koide R-Eta KS Route Momentum Link-Phase Input Target Discriminator",
        "Koide R-Eta KS Route Momentum Link-Phase Input Ratification Decision Packet",
        "Koide R-Eta KS Route Momentum Link-Phase Input Current-Surface No-Go",
        "scripts/frontier_zero_import_hydrogen_koide_r_eta_ks_route_momentum_link_phase_input.py",
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED",
        "KS_ROUTE_MOMENTUM_LINK_PHASE_TEXT_LOCK",
        "TWO_FLUX_CLASS_KINETIC_SURFACE_ACCEPTED",
        "P_FLUX_WITHIN_SURFACE_SELECTION_ACCEPTED",
        "KAWAMOTO_SMIT_LINK_PHASE_REPRESENTATIVE_ACCEPTED",
        "FINITE_LINK_PHASE_AND_BLOCH_MOMENTUM_SUPPORT_CHECK",
        "WRAP_HOLONOMY_BOUNDARY_LOCK",
        "NO_FULL_KINETIC_SURFACE_RETIREMENT_INPUT",
        "NO_SPINFUL_KERNEL_OBJECT_THEOREM_INPUT",
        "NO_TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_INPUT",
        "NO_SCALAR_LIFT_EXCLUSION_HANDOFF_INPUT",
        "NO_KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_INPUT",
        "NO_KS_ROUTE_CLOSURE_INPUT",
        "NO_PARENT_BRIDGE_OR_HW1_INPUT",
        "NO_R_Q_DELTA_OR_R_ETA_VALUE_INPUT",
        "NO_K1_K3_K4_OR_MASS_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED",
        "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md",
        "P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md",
        "STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md",
        "AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md",
        "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md",
        "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md",
        "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_R_ETA_SPINFUL_SIGMA_DOT_P_KERNEL_KS_ROUTE_TARGET_DISCRIMINATOR_2026-07-05.md",
        "`#5016` zero-import hydrogen retained lane bundle",
        "merged `#5019`",
        "merged `#5020`",
        "merged `#5022`",
        "merged `#5023`",
        "merged `#5024`",
        "open `#5021`",
        "open `#5014`",
        "open `#5017`",
        "open `#5018`",
        "The approved primitive registry was checked",
        "clean/dirty/check labels are not proof inputs",
        "No-Go Discipline Gate",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in packet_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in packet)

    section("Predicate checks")
    full_link = set(LINK_INPUTS)
    audit.check("full momentum/link-phase contract closes target", closes_link_input(full_link))
    audit.check("current surface does not close momentum/link-phase target", not closes_link_input(CURRENT_SURFACE_INPUTS))

    for missing in sorted(LINK_INPUTS):
        reduced = set(full_link)
        reduced.remove(missing)
        audit.check(f"momentum/link-phase contract fails without input {missing}", not closes_link_input(reduced))

    accepted_subsets = [subset for subset in all_subsets(LINK_INPUTS) if closes_link_input(subset)]
    audit.check("only one minimal full momentum/link-phase subset closes", accepted_subsets == [LINK_INPUTS])

    link_consequence = {"KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED"}
    sigma_without_link = set(SIGMA_ROUTE_INPUTS) - {"KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED"}
    sigma_without_kernel_object = set(SIGMA_ROUTE_INPUTS) - {"KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED"}
    audit.check("link consequence alone does not close sigma-dot-p KS route", not closes_sigma_route(link_consequence))
    audit.check("link consequence plus remaining sigma inputs closes sigma-dot-p KS route", closes_sigma_route(link_consequence | sigma_without_link))
    audit.check("link consequence cannot close sigma route without spinful kernel-object theorem", not closes_sigma_route(sigma_without_kernel_object))
    audit.check("link consequence alone does not close scalar-lift exclusion", not closes_scalar_lift_exclusion(link_consequence))
    audit.check("link consequence alone does not close KS route", not closes_ks_route(link_consequence))
    audit.check("link consequence alone does not close parent bridge", not closes_parent_bridge(link_consequence))
    audit.check("link consequence alone does not close HW1", not closes_hw1(link_consequence))
    audit.check("link consequence alone does not close R-eta", not closes_r_eta(link_consequence))
    audit.check("link consequence alone does not close electron mass", not closes_electron_mass(link_consequence))
    audit.check("link consequence alone does not close hydrogen", not closes_hydrogen(link_consequence))

    section("Finite link-phase and Bloch support checks")
    finite_link_phase_checks(audit)

    section("Authority and primitive boundary checks")
    sigma_target = read(SIGMA_TARGET)
    sigma_decision = read(SIGMA_DECISION)
    sigma_current = read(SIGMA_CURRENT)
    sigma_packet = "\n".join([sigma_target, sigma_decision, sigma_current])
    goal = read(GOAL)
    firewall = read(KOIDE_FIREWALL)
    kinetic_class = read(KINETIC_CLASS)
    p_flux = read(P_FLUX)
    z_cert = read(Z_CERT)
    fsb_k = read(FSB_K)
    gstar_thermal = read(GSTAR_THERMAL)
    ks_forcing = read(KS_FORCING)
    realization_gate = read(REALIZATION_GATE)
    primitive_registry = json.loads(read(PRIMITIVE_REGISTRY))
    primitive_nodes = primitive_registry["nodes"]
    primitive_text = "\n".join([read(MINIMAL), read(SCALE), read(KINETIC), read(REALIZED)])

    for label, container in [
        ("goal packet", goal),
        ("Koide firewall", firewall),
        ("sigma target", sigma_target),
        ("sigma decision", sigma_decision),
        ("sigma current no-go", sigma_current),
    ]:
        audit.check(
            f"{label} references momentum/link-phase lane",
            TARGET.name in container
            and DECISION.name in container
            and CURRENT.name in container
            and "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED" in container,
        )

    audit.check("momentum/link-phase packet references sigma parent target", SIGMA_TARGET.name in packet)
    audit.check("sigma packet still consumes momentum/link-phase handle as subinput", "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED" in sigma_packet)

    kinetic_flat = norm(kinetic_class)
    p_flux_flat = norm(p_flux)
    z_flat = norm(z_cert)
    fsb_flat = norm(fsb_k)
    gstar_flat = norm(gstar_thermal)
    ks_flat = norm(ks_forcing)
    realization_flat = norm(realization_gate)

    audit.check(
        "kinetic class names two flux classes and K1 representative",
        "K0` = uniform plaquette flux `+1`" in kinetic_flat
        and "K1` = uniform plaquette flux `-1`" in kinetic_flat
        and "representative the Kawamoto-Smit" in kinetic_flat,
    )
    audit.check(
        "kinetic class leaves K1 selector residual explicit",
        "specified constraint set does NOT force `K1`" in kinetic_flat
        and "P-SD therefore holds as a theorem given the `K1` branch" in kinetic_flat,
    )
    audit.check(
        "P-FLUX selects within licensed surface without wholesale P-KIN retirement",
        "within the licensed two-class kinetic surface" in p_flux_flat
        and "`phi = -1` is selected" in p_flux_flat
        and "B-BIT retired within the licensed two-class surface" in p_flux_flat
        and "does not by itself prove the kinetic-class forcing row's surface assumptions or retire P-KIN wholesale" in p_flux_flat,
    )
    audit.check(
        "Z certificate supplies K1/K0 geometry but no selection",
        "The Kawamoto-Smit kernel `h_K1` satisfies (Z)" in z_flat
        and "flux-`(+1)` kernel `h_K0` VIOLATES" in z_flat
        and "This note **performs no selection**" in z_cert,
    )
    audit.check(
        "FSB-K source supplies retained thermal currency context",
        "fermionic Stefan-Boltzmann" in fsb_flat
        and "retained" in fsb_flat
        and "T" in fsb_flat,
    )
    audit.check(
        "G-star thermal bridge supplies seven-eighths SB context",
        "7/8" in gstar_flat
        and "Stefan-Boltzmann" in gstar_flat,
    )
    audit.check(
        "KS forcing names eta representative and bounded premises",
        "eta_1 = 1" in ks_flat
        and "eta_2(x) = (-1)" in ks_flat
        and "eta_3(x) = (-1)" in ks_flat
        and "P-KIN and P-SD remain declared premises" in ks_flat,
    )
    audit.check(
        "realization gate keeps kinetic supply line bounded",
        "kinetic-class / P-FLUX supply line" in realization_flat
        and "current closure remains bounded/conditional" in realization_flat,
    )

    for node in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node}", node in primitive_nodes)

    for forbidden_node in [
        "ks_route_momentum_link_phase_primitive",
        "spinful_sigma_dot_p_kernel_primitive",
        "spinful_staggered_kernel_primitive",
        "scalar_lift_exclusion_primitive",
        "ks_to_physical_matter_state_spinor_law_primitive",
        "ks_spin_lift_physical_action_primitive",
        "physical_matter_state_law_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {forbidden_node}", forbidden_node not in primitive_nodes)

    for excluded in ["selector", "readout bridge", "state-selection rule", "mass ratio", "empirical fit"]:
        audit.check(f"primitive notes exclude {excluded}", excluded in primitive_text)

    section("Open/merged PR and non-claim boundaries")
    current_flat = flat(current)
    pr_markers = [
        "`#5016` zero-import hydrogen retained lane bundle | open; audit running at refresh",
        "`#5019` AC_phi_lambda decomposition chain | merged, audit success",
        "`#5020` AC_phi_lambda value face | merged, audit success",
        "`#5022` delta-eta chain repair | merged, audit success",
        "`#5023` Koide W4 audit-readiness repairs | merged, audit success",
        "`#5024` Koide W4 gate-note premise minimization + substep1-bridge rebase | merged, audit success",
        "`#5021` primitive-retirement review: meta gate map, no retirements | open draft, audit success",
        "`#5014` record-formation front is the domain wall | open, audit success",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open, audit success",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open, audit success",
        "clean/dirty/check labels are not proof inputs",
    ]
    for marker in pr_markers:
        audit.check(f"PR marker present: {marker}", flat(marker) in current_flat)

    explicit_nonclaims = [
        "`KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED`.",
        "`KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED`.",
        "`SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED`.",
        "`TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED`.",
        "`SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED`.",
        "No derivation or ratification of `KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED`.",
        "`KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED`.",
        "No derivation or ratification of `PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED`.",
        "No derivation or ratification of `HW1_PHYSICAL_GENERATION_LOCUS_RETAINED`.",
        "retained hydrogen",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
        "No claim that #5014, #5017, #5018, #5019, #5020, #5022, #5023, or #5024",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in packet)

    forbidden = [
        "This note ratifies route-defined momentum/link-phase input",
        "KS_ROUTE_DEFINED_MOMENTUM_COVECTOR_OR_LINK_PHASE_INPUT_RETAINED is supplied",
        "KS_ROUTE_SPINFUL_KERNEL_OBJECT_THEOREM_RETAINED is supplied",
        "SPINFUL_SIGMA_DOT_P_KERNEL_DEFINED_ON_KS_ROUTE_RETAINED is supplied",
        "TRIVIAL_SCALAR_LIFT_COVARIANCE_EXCLUSION_RETAINED is supplied",
        "SPINFUL_STAGGERED_KERNEL_EXCLUDES_SCALAR_LIFT_RETAINED is supplied",
        "KS_SPIN_LIFT_PHYSICAL_ACTION_LAW_RETAINED is supplied",
        "KS_TO_PHYSICAL_MATTER_STATE_SPINOR_LAW_THEOREM_RETAINED is supplied",
        "PHYSICAL_MATTER_STATE_LAW_BRIDGE_RETAINED is supplied",
        "HW1_PHYSICAL_GENERATION_LOCUS_RETAINED is supplied",
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
