#!/usr/bin/env python3
"""Verifier for the static-source NR Coulomb three-gate target bundle.

This runner checks that the readout, one-body NR, and Hartree mapping child
gates are explicit review targets while preserving the support-only boundary.
It does not ratify any of the three gates or the parent NR Coulomb limit.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET_BUNDLE_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
STATIC_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
STATIC_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
STATIC_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md"
STATIC_RYDBERG = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
STATIC_RYDBERG_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
I1_BRIDGE = ROOT / "docs" / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
I1_HYGIENE = ROOT / "docs" / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
I1_NATIVE = ROOT / "docs" / "I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md"
I1_QUADRATIC = ROOT / "docs" / "I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md"
I1_RUNNER = ROOT / "scripts" / "static_source_readout_i1_accepted_premise_runner.py"
I1_HYGIENE_RUNNER = ROOT / "scripts" / "audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.py"
KINETIC_REPAIR = ROOT / "docs" / "HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md"
GREEN_KERNEL = ROOT / "docs" / "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md"
PHYSICAL_UNIT_BOUNDARY = ROOT / "docs" / "ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md"
PHYSICAL_UNIT_RUNNER = ROOT / "scripts" / "frontier_atomic_lane2_physical_unit_limit_boundary.py"
ATOMIC_PROBE = ROOT / "docs" / "ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md"
LATTICE_COMPANION = ROOT / "scripts" / "frontier_atomic_hydrogen_lattice_companion.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


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

STATIC_RYDBERG_INPUTS = {
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


def closes_three_gate(inputs: set[str]) -> bool:
    return THREE_GATE_INPUTS <= inputs


def closes_nr_coulomb(inputs: set[str]) -> bool:
    return NR_COULOMB_INPUTS <= inputs


def closes_static_rydberg(inputs: set[str]) -> bool:
    return STATIC_RYDBERG_INPUTS <= inputs


def dimensionless_level(n: int) -> Fraction:
    return Fraction(-1, 2 * n * n)


def physical_level(n: int, hartree_ev: Fraction) -> Fraction:
    return hartree_ev * dimensionless_level(n)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        STATIC_PACKET,
        STATIC_ASSEMBLY,
        STATIC_NO_GO,
        STATIC_RYDBERG,
        STATIC_RYDBERG_ASSEMBLY,
        I1_BRIDGE,
        I1_HYGIENE,
        I1_NATIVE,
        I1_QUADRATIC,
        I1_RUNNER,
        I1_HYGIENE_RUNNER,
        KINETIC_REPAIR,
        GREEN_KERNEL,
        PHYSICAL_UNIT_BOUNDARY,
        PHYSICAL_UNIT_RUNNER,
        ATOMIC_PROBE,
        LATTICE_COMPANION,
        REGISTRY,
        MINIMAL,
        SCALE,
        KINETIC,
        REALIZED,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    note = read(NOTE)
    note_flat = flat(note)

    section("Required target bundle content")
    required_phrases = [
        "Static-Source NR Coulomb Three-Gate Target Bundle",
        "target bundle / review-compression packet",
        "support-only",
        "STATIC_SOURCE_NR_COULOMB_THREE_GATE_TARGET",
        "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
        "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
        "HARTREE_SCALE_MAPPING_RATIFIED",
        "STATIC_SOURCE_READOUT_TEXT_LOCK",
        "NATIVE_STATIC_FIELD_INTEGRATION_HANDOFF",
        "SOURCE_NORMALIZED_QUADRATIC_ACTION_HANDOFF",
        "LINEAR_RESPONSE_ENERGY_READOUT_HANDOFF",
        "UNIT_ELECTROMAGNETIC_SOURCE_COEFFICIENT_HANDOFF",
        "NO_ACCEPTED_PREMISE_AS_RETAINED_THEOREM",
        "ONE_BODY_NR_TEXT_LOCK",
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
        "STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md",
        "I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md",
        "I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md",
        "HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md",
        "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md",
        "ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md",
        "frontier_atomic_hydrogen_lattice_companion.py",
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` finite multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall anomaly inflow spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5011` eta twisted walk family runner | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open, clean",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "static_source_readout_primitive",
        "one_body_schrodinger_primitive",
        "one_body_nr_primitive",
        "hartree_scale_mapping_primitive",
        "static_source_nr_coulomb_primitive",
        "static_source_rydberg_primitive",
        "hydrogen_primitive",
        "Distance To Hydrogen",
        "No-Go Discipline Gate",
        "Gate result",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Predicate checks")
    full_three_gate = set(THREE_GATE_INPUTS)
    audit.check("full three-gate target closes child target", closes_three_gate(full_three_gate))
    for missing in sorted(THREE_GATE_INPUTS):
        reduced = set(THREE_GATE_INPUTS)
        reduced.remove(missing)
        audit.check(f"three-gate target fails without {missing}", not closes_three_gate(reduced))
    accepted_child_subsets = [subset for subset in all_subsets(THREE_GATE_INPUTS) if closes_three_gate(subset)]
    audit.check("only full child subset closes three-gate target", accepted_child_subsets == [full_three_gate])

    base_parent_support = {
        "STATIC_SOURCE_NR_COULOMB_TEXT_LOCK",
        "SCALAR_LATTICE_OPERATOR_SURFACE_RATIFIED",
        "COULOMB_KERNEL_ASYMPTOTIC_RATIFIED",
        "ATOMIC_OPERATOR_HARNESS_VERIFIED",
        "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
    }
    audit.check(
        "three content gates alone do not close parent NR Coulomb",
        not closes_nr_coulomb(full_three_gate),
    )
    audit.check(
        "base support plus child gates still needs owner/audit for parent closure",
        not closes_nr_coulomb(base_parent_support | full_three_gate),
    )
    audit.check(
        "base support plus child gates plus owner/audit closes model parent",
        closes_nr_coulomb(base_parent_support | full_three_gate | {"OWNER_RATIFICATION", "AUDIT_ACCEPTANCE"}),
    )
    audit.check(
        "retained NR Coulomb alone does not close static-source Rydberg",
        not closes_static_rydberg({"RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT"}),
    )
    audit.check(
        "full static-source Rydberg predicate closes model target",
        closes_static_rydberg(set(STATIC_RYDBERG_INPUTS)),
    )

    section("Finite Coulomb and Hartree arithmetic")
    levels = {n: dimensionless_level(n) for n in range(1, 6)}
    audit.check("dimensionless E1 is -1/2", levels[1] == Fraction(-1, 2))
    for n, level in levels.items():
        audit.check(f"dimensionless ratio n={n} is 1/n^2", level / levels[1] == Fraction(1, n * n))

    hartree_scales = [Fraction(20, 1), Fraction(27_211_386, 1_000_000), Fraction(40, 1)]
    spectra = [[physical_level(n, scale) for n in (1, 2, 3)] for scale in hartree_scales]
    audit.check("all Hartree choices preserve E2/E1 = 1/4", all(row[1] / row[0] == Fraction(1, 4) for row in spectra))
    audit.check("all Hartree choices preserve E3/E1 = 1/9", all(row[2] / row[0] == Fraction(1, 9) for row in spectra))
    audit.check("different Hartree choices give different E1 values", len({row[0] for row in spectra}) == len(spectra))

    for g in [0.25, 1.0, 3.0]:
        for r in [2.0, 10.0, 100.0]:
            lhs = -4.0 * math.pi * g * (1.0 / (4.0 * math.pi * r))
            rhs = -g / r
            audit.check(f"Green kernel gives -g/r for g={g} r={r}", abs(lhs - rhs) < 1e-15)

    for c_value in [1.0, 4.0 / 3.0]:
        for g_bare in [0.5, 1.0, 2.0]:
            alpha = g_bare * g_bare / (4.0 * math.pi)
            r = 7.0
            direct = -c_value * g_bare * g_bare / (4.0 * math.pi * r)
            via_alpha = -c_value * alpha / r
            audit.check(f"static-source readout alpha substitution C={c_value} g={g_bare}", abs(direct - via_alpha) < 1e-15)
    audit.check("unit-source and color-Casimir coefficients are distinct", abs((4.0 / 3.0) - 1.0) > 0.1)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    static_packet = read(STATIC_PACKET)
    static_assembly = read(STATIC_ASSEMBLY)
    static_no_go = read(STATIC_NO_GO)
    static_rydberg = read(STATIC_RYDBERG)
    static_rydberg_assembly = read(STATIC_RYDBERG_ASSEMBLY)
    i1_bridge = read(I1_BRIDGE)
    i1_hygiene = read(I1_HYGIENE)
    i1_native = read(I1_NATIVE)
    i1_quadratic = read(I1_QUADRATIC)
    i1_runner = read(I1_RUNNER)
    i1_hygiene_runner = read(I1_HYGIENE_RUNNER)
    kinetic_repair = read(KINETIC_REPAIR)
    green_kernel = read(GREEN_KERNEL)
    physical_unit_boundary = read(PHYSICAL_UNIT_BOUNDARY)
    physical_unit_runner = read(PHYSICAL_UNIT_RUNNER)
    atomic_probe = read(ATOMIC_PROBE)
    lattice_companion = read(LATTICE_COMPANION)
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()

    for container_name, container in [
        ("goal packet", goal),
        ("parent static-source NR packet", static_packet),
        ("static-source NR assembly", static_assembly),
        ("static-source NR no-go", static_no_go),
        ("static-source Rydberg discriminator", static_rydberg),
        ("static-source Rydberg assembly", static_rydberg_assembly),
    ]:
        audit.check(f"{container_name} references three-gate bundle", NOTE.name in container)

    audit.check("parent static packet still names eleven inputs", all(item in static_packet for item in NR_COULOMB_INPUTS))
    audit.check("static assembly still support-only", "does not supply `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`" in flat(static_assembly))
    audit.check("static no-go keeps current-surface scope", "current retained, primitive, and open-PR surfaces do not supply" in static_no_go)
    audit.check("Rydberg discriminator keeps NR Coulomb downstream", "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT" in static_rydberg)
    audit.check("I1 bridge registers accepted-premise packet", "accepted-premise packet entry" in i1_bridge and "not derived in this bridge" in i1_bridge)
    audit.check("I1 bridge does not close downstream physical theorem", "This bridge does not close:" in i1_bridge)
    audit.check("I1 hygiene keeps no status promotion", "does not promote status" in i1_hygiene or "Audit-lane values are printed as metadata" in i1_hygiene_runner)
    audit.check("I1 native relocation keeps residuals explicit", "RELOCATES, does not eliminate" in i1_native and "general energy-readout bridge remains open" in i1_native)
    audit.check("I1 quadratic bridge keeps supplied-action boundary", "source-normalized leading quadratic action" in i1_quadratic and "does not derive the physical source-coupling normalization" in i1_quadratic)
    audit.check("I1 runner remains accepted-premise scoped", "accepted-premise" in i1_runner)
    audit.check("kinetic repair refuses absolute eV predictions", "absolute-eV predictions" in kinetic_repair)
    audit.check("green kernel names framework-local 1/(4 pi r)", "framework-local large-separation normalization" in green_kernel and "1 / (4 pi |r|)" in green_kernel)
    audit.check("physical-unit boundary names Hartree missing scale", "E_H = m_e alpha(0)^2" in physical_unit_boundary and "Rydberg = E_H / 2" in physical_unit_boundary)
    audit.check("physical-unit runner checks scale degeneracy", "Different Hartree scales give different E1 values" in physical_unit_runner)
    audit.check("atomic probe is textbook scaffold only", "textbook inputs" in atomic_probe and "No `Cl(3)` on `Z^3` framework input" in atomic_probe)
    audit.check("atomic probe names Schrodinger gap", "single-particle Schrodinger" in atomic_probe and "not currently a retained" in atomic_probe)
    audit.check("lattice companion is coupling-relative only", "coupling-relative" in lattice_companion and "Absolute scale requires m_e" in lattice_companion)

    nodes = registry["nodes"]
    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms exclude source/action bridges", "source/action" in minimal and "remain outside axiom content" in minimal)
    audit.check("scale primitive excludes dimensionless couplings", "zero dimensionless content" in scale and "coupling" in scale)
    audit.check("kinetic primitive excludes dynamics/couplings", "dynamics" in kinetic and "coupling" in kinetic)
    audit.check("realized primitive excludes state-selection and values", "state-selection rule" in realized and "or value is supplied" in realized)
    for absent in [
        "static_source_readout_primitive",
        "one_body_schrodinger_primitive",
        "one_body_nr_primitive",
        "hartree_scale_mapping_primitive",
        "static_source_nr_coulomb_primitive",
        "static_source_rydberg_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no registered three-gate shortcut: {absent}", absent not in registry_text)

    section("Open PR and non-claim boundaries")
    explicit_non_claims = [
        "No derivation or ratification of `STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED`.",
        "No derivation or ratification of `ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED`.",
        "No derivation or ratification of `HARTREE_SCALE_MAPPING_RATIFIED`.",
        "No derivation or ratification of `STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED`.",
        "No derivation or ratification of `RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT`.",
        "No derivation of `m_e`.",
        "No derivation of `alpha(0)`.",
        "No static-source Rydberg retained claim.",
        "No retained hydrogen calculation.",
        "No use of observed Rydberg, observed hydrogen lines, PDG `m_e`, observed",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the static-source readout",
        "This packet ratifies the one-body NR",
        "This packet ratifies the Hartree mapping",
        "This packet ratifies the static-source NR Coulomb limit",
        "STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED is supplied",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT is supplied",
        "This packet derives `m_e`",
        "This packet derives `alpha(0)`",
        "This packet claims hydrogen is retained",
        "observed Rydberg is used as proof",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
