#!/usr/bin/env python3
"""Verifier for the static-source one-body/Hartree decision packet.

This runner checks that the one-body NR physical-unit and Hartree mapping
handoff is explicit, that atomic shape support is not over-spent as a retained
physical spectrum, and that downstream hydrogen claims remain blocked.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
THREE_GATE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md"
READOUT_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
READOUT_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_READOUT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
NR_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
NR_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
NR_CURRENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md"
RYDBERG = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
RYDBERG_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
PHYSICAL_UNIT = ROOT / "docs" / "ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md"
PHYSICAL_UNIT_RUNNER = ROOT / "scripts" / "frontier_atomic_lane2_physical_unit_limit_boundary.py"
KINETIC_REPAIR = ROOT / "docs" / "HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md"
GREEN_KERNEL = ROOT / "docs" / "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md"
ATOMIC_PROBE = ROOT / "docs" / "ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md"
ATOMIC_COMPANION = ROOT / "scripts" / "frontier_atomic_hydrogen_lattice_companion.py"
RYDBERG_FIREWALL = ROOT / "docs" / "ATOMIC_RYDBERG_DEPENDENCY_FIREWALL_NOTE_2026-04-27.md"
ELECTRON_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


ONE_BODY_HARTREE_INPUTS = {
    "STATIC_SOURCE_ONE_BODY_HARTREE_TEXT_LOCK",
    "SCALAR_OPERATOR_SURFACE_CONSUMED",
    "STATIC_COULOMB_KERNEL_CONSUMED",
    "LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF",
    "DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF",
    "NO_TEXTBOOK_SCHRODINGER_IMPORT",
    "HARTREE_MAPPING_TEXT_LOCK",
    "RETAINED_ELECTRON_MASS_INPUT_CONSUMED",
    "RETAINED_ALPHA0_INPUT_CONSUMED",
    "UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0",
    "PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

THREE_GATE_INPUTS = {
    "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
    "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
    "HARTREE_SCALE_MAPPING_RATIFIED",
}

NR_COULOMB_INPUTS = {
    "STATIC_SOURCE_NR_COULOMB_TEXT_LOCK",
    "SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED",
    "COULOMB_KERNEL_ASYMPTOTIC_RATIFIED",
    "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
    "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
    "HARTREE_SCALE_MAPPING_RATIFIED",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

STATIC_SOURCE_RYDBERG_INPUTS = {
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


def closes_one_body_hartree(inputs: set[str]) -> bool:
    return ONE_BODY_HARTREE_INPUTS <= inputs


def closes_three_gate(inputs: set[str]) -> bool:
    return THREE_GATE_INPUTS <= inputs


def closes_nr_coulomb(inputs: set[str]) -> bool:
    return NR_COULOMB_INPUTS <= inputs


def closes_static_rydberg(inputs: set[str]) -> bool:
    return STATIC_SOURCE_RYDBERG_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        CURRENT,
        GOAL,
        THREE_GATE,
        READOUT_PACKET,
        READOUT_CURRENT,
        NR_PACKET,
        NR_ASSEMBLY,
        NR_CURRENT,
        RYDBERG,
        RYDBERG_ASSEMBLY,
        PHYSICAL_UNIT,
        PHYSICAL_UNIT_RUNNER,
        KINETIC_REPAIR,
        GREEN_KERNEL,
        ATOMIC_PROBE,
        ATOMIC_COMPANION,
        RYDBERG_FIREWALL,
        ELECTRON_PACKET,
        ALPHA_PACKET,
        REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    current = read(CURRENT)
    note_flat = flat(note)
    current_flat = flat(current)

    section("Required decision and no-go content")
    required_note_phrases = [
        "Static-Source One-Body Hartree Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
        "HARTREE_SCALE_MAPPING_RATIFIED",
        "STATIC_SOURCE_ONE_BODY_HARTREE_TEXT_LOCK",
        "SCALAR_OPERATOR_SURFACE_CONSUMED",
        "STATIC_COULOMB_KERNEL_CONSUMED",
        "LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF",
        "DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF",
        "NO_TEXTBOOK_SCHRODINGER_IMPORT",
        "HARTREE_MAPPING_TEXT_LOCK",
        "RETAINED_ELECTRON_MASS_INPUT_CONSUMED",
        "RETAINED_ALPHA0_INPUT_CONSUMED",
        "UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0",
        "PHYSICAL_UNIT_SCALE_FORMULA_HANDOFF",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those fourteen contract inputs",
        "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
        "STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_ONE_BODY_HARTREE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md",
        "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
        "ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md",
        "frontier_atomic_hydrogen_lattice_companion.py",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_ALPHA0_TRANSPORT_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` finite multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5006` static-source I1 hygiene companion | open, clean",
        "Primitive Registry Check",
        "one_body_schrodinger_primitive",
        "one_body_nr_primitive",
        "hartree_scale_mapping_primitive",
        "unit_source_coefficient_primitive",
        "electron_mass_primitive",
        "alpha0_primitive",
        "static_source_rydberg_primitive",
        "hydrogen_primitive",
        "Distance To Hydrogen",
        "Explicit Non-Claims",
    ]
    for phrase in required_note_phrases:
        audit.check(f"decision phrase present: {phrase}", flat(phrase) in note_flat)

    required_current_phrases = [
        "Static-Source One-Body Hartree Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "the current retained, primitive, and open-PR surfaces do not supply",
        "fourteen-input one-body/Hartree handoff",
        "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
        "HARTREE_SCALE_MAPPING_RATIFIED",
        "STATIC_SOURCE_ONE_BODY_HARTREE_TEXT_LOCK",
        "LOW_ENERGY_ONE_PARTICLE_REDUCTION_HANDOFF",
        "DIMENSIONLESS_COULOMB_SPECTRUM_HANDOFF",
        "UNIT_SOURCE_COEFFICIENT_MATCHED_TO_ALPHA0",
        "No-Go Discipline Gate",
        "OPEN POSITIVE ROUTE",
        "Gate result",
        "Explicit Non-Claims",
    ]
    for phrase in required_current_phrases:
        audit.check(f"current-surface phrase present: {phrase}", flat(phrase) in current_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in current)

    section("Decision predicate checks")
    full_contract = set(ONE_BODY_HARTREE_INPUTS)
    audit.check("full one-body/Hartree contract accepts handoff", closes_one_body_hartree(full_contract))
    for missing in sorted(ONE_BODY_HARTREE_INPUTS):
        reduced = set(ONE_BODY_HARTREE_INPUTS)
        reduced.remove(missing)
        audit.check(f"one-body/Hartree handoff fails without {missing}", not closes_one_body_hartree(reduced))
    accepted_subsets = [subset for subset in all_subsets(ONE_BODY_HARTREE_INPUTS) if closes_one_body_hartree(subset)]
    audit.check("only full one-body/Hartree subset closes handoff", accepted_subsets == [full_contract])
    audit.check(
        "one-body/Hartree consequences without readout do not close three-gate target",
        not closes_three_gate({"ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED", "HARTREE_SCALE_MAPPING_RATIFIED"}),
    )
    audit.check("full three-gate model predicate closes", closes_three_gate(set(THREE_GATE_INPUTS)))
    audit.check(
        "one-body/Hartree handoff alone does not close parent NR Coulomb",
        not closes_nr_coulomb({"ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED", "HARTREE_SCALE_MAPPING_RATIFIED"}),
    )
    audit.check(
        "static-source Rydberg still needs retained NR Coulomb plus physical inputs",
        not closes_static_rydberg({"ATOMIC_OPERATOR_HARNESS_VERIFIED", "NO_RYDBERG_COMPARATOR_PROOF_INPUT"}),
    )
    audit.check("full static-source Rydberg predicate closes model target", closes_static_rydberg(set(STATIC_SOURCE_RYDBERG_INPUTS)))

    section("Finite atomic and Hartree arithmetic checks")
    eps = {n: Fraction(-1, 2 * n * n) for n in range(1, 6)}
    audit.check("dimensionless E1 is -1/2", eps[1] == Fraction(-1, 2))
    for n in range(1, 6):
        audit.check(f"dimensionless ratio n={n} is 1/n^2", eps[n] / eps[1] == Fraction(1, n * n))

    hartree_scales = [Fraction(1, 1), Fraction(3, 1), Fraction(27, 1)]
    spectra = [[scale * eps[n] for n in range(1, 4)] for scale in hartree_scales]
    audit.check("all Hartree choices preserve E2/E1 = 1/4", all(row[1] / row[0] == Fraction(1, 4) for row in spectra))
    audit.check("all Hartree choices preserve E3/E1 = 1/9", all(row[2] / row[0] == Fraction(1, 9) for row in spectra))
    audit.check("different Hartree choices give different E1 values", len({row[0] for row in spectra}) == len(spectra))

    alpha0 = 1.0 / 137.035999084
    electron_mass_ev = 510998.950
    hartree_ev = electron_mass_ev * alpha0 * alpha0
    rydberg_ev = hartree_ev / 2.0
    audit.check("Hartree comparator is in known eV band", 27.21 < hartree_ev < 27.22, f"H={hartree_ev:.12f}")
    audit.check("Rydberg comparator is half Hartree", abs(2.0 * rydberg_ev - hartree_ev) < 1e-12)
    for g_value in [0.25, 1.0, 3.0]:
        for r_value in [2.0, 10.0, 100.0]:
            green = 1.0 / (4.0 * math.pi * r_value)
            v_lat = -4.0 * math.pi * g_value * green
            audit.check(
                f"Green kernel gives -g/r for g={g_value} r={r_value}",
                abs(v_lat + g_value / r_value) < 1e-12,
            )
    unit_coeff = 1.0
    color_casimir = 4.0 / 3.0
    audit.check("unit-source and color-Casimir coefficients are distinct", unit_coeff != color_casimir)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    three_gate = read(THREE_GATE)
    nr_packet = read(NR_PACKET)
    nr_assembly = read(NR_ASSEMBLY)
    nr_current = read(NR_CURRENT)
    rydberg = read(RYDBERG)
    rydberg_assembly = read(RYDBERG_ASSEMBLY)
    physical_unit = read(PHYSICAL_UNIT)
    physical_unit_runner = read(PHYSICAL_UNIT_RUNNER)
    kinetic_repair = read(KINETIC_REPAIR)
    green_kernel = read(GREEN_KERNEL)
    atomic_probe = read(ATOMIC_PROBE)
    atomic_companion = read(ATOMIC_COMPANION)
    rydberg_firewall = read(RYDBERG_FIREWALL)

    for label, text in [
        ("goal packet", goal),
        ("three-gate target bundle", three_gate),
        ("NR Coulomb parent packet", nr_packet),
        ("NR Coulomb assembly", nr_assembly),
        ("NR Coulomb current no-go", nr_current),
        ("static-source Rydberg discriminator", rydberg),
        ("static-source Rydberg assembly", rydberg_assembly),
    ]:
        audit.check(f"{label} references one-body/Hartree decision packet", NOTE.name in text)
        audit.check(f"{label} references one-body/Hartree current no-go", CURRENT.name in text)

    audit.check("three-gate target keeps readout separate", "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED" in three_gate)
    audit.check("readout packet is sibling support only", READOUT_PACKET.name in three_gate)
    audit.check("readout current no-go is sibling support only", READOUT_CURRENT.name in three_gate)
    audit.check("physical-unit boundary names Hartree missing scale", "E_H = m_e alpha(0)^2" in physical_unit and "Rydberg = E_H / 2" in physical_unit)
    audit.check("physical-unit runner checks scale degeneracy", "Different Hartree scales give different E1 values" in physical_unit_runner)
    audit.check("kinetic repair refuses absolute eV predictions", "absolute-eV" in kinetic_repair or "absolute eV" in kinetic_repair)
    audit.check("green kernel names framework-local coefficient", "1 / (4 pi |r|)" in green_kernel or "1/(4 pi |x|)" in green_kernel)
    audit.check("atomic probe is textbook scaffold only", "standard QM" in atomic_probe or "textbook" in atomic_probe)
    audit.check("lattice companion is coupling-relative only", "coupling-relative" in atomic_companion or "no physical eV scale" in atomic_companion)
    audit.check("Rydberg firewall blocks direct substitution", "Rydberg" in rydberg_firewall and "firewall" in rydberg_firewall.lower())

    registry = json.loads(read(REGISTRY))
    for node in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]:
        audit.check(f"registry node present: {node}", node in registry["nodes"])
        audit.check(f"registry current_path for {node}", "current_path" in registry["nodes"][node])

    minimal = read(MINIMAL)
    scale = read(SCALE)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    audit.check("minimal axioms exclude source/action bridges", "source/action" in minimal and "physical-observable identification" in minimal)
    audit.check("scale primitive excludes dimensionless quantities", "carries zero dimensionless" in scale and "does not supply any dimensionless quantity" in scale)
    audit.check("kinetic primitive excludes dynamics/couplings", "no mass ratio" in kinetic and "coupling" in kinetic)
    audit.check("realized primitive excludes values and state-selection", "does not supply a state" in realized and "state-contingent value" in realized)

    absent_shortcuts = [
        "one_body_schrodinger_primitive",
        "one_body_nr_primitive",
        "hartree_scale_mapping_primitive",
        "unit_source_coefficient_primitive",
        "electron_mass_primitive",
        "alpha0_primitive",
        "static_source_rydberg_primitive",
        "hydrogen_primitive",
    ]
    for shortcut in absent_shortcuts:
        audit.check(f"no registered one-body/Hartree shortcut: {shortcut}", shortcut not in registry["nodes"])

    section("Non-claim boundary")
    non_claims = [
        "No derivation or ratification of `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`.",
        "No derivation or ratification of `HARTREE_SCALE_MAPPING_RATIFIED`.",
        "No derivation or ratification of `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.",
        "No derivation or ratification of `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`.",
        "No derivation or ratification of `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.",
        "No derivation of `m_e`.",
        "No derivation of `alpha(0)`.",
        "No static-source Rydberg retained claim.",
        "No retained hydrogen calculation.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in non_claims:
        audit.check(f"decision explicit non-claim present: {phrase}", phrase in note)
        audit.check(f"current explicit non-claim present: {phrase}", phrase in current)

    forbidden = [
        "This packet ratifies the one-body NR",
        "This packet ratifies Hartree mapping",
        "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED is supplied",
        "HARTREE_SCALE_MAPPING_RATIFIED is supplied",
        "This note ratifies the one-body NR",
        "This note ratifies Hartree mapping",
        "This packet derives `m_e`",
        "This packet derives `alpha(0)`",
        "This packet claims hydrogen is retained",
        "observed Rydberg is used as proof",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent from decision: {phrase}", phrase not in note)
        audit.check(f"forbidden overclaim absent from current no-go: {phrase}", phrase not in current)

    audit.summary()


if __name__ == "__main__":
    main()
