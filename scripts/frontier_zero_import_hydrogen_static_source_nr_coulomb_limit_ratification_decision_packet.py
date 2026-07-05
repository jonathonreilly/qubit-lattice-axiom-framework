#!/usr/bin/env python3
"""Verifier for the static-source NR Coulomb limit decision packet.

This runner checks that the static-source one-body Coulomb limit is packaged
as an explicit owner/audit decision contract and kept separate from electron
mass, alpha0 transport, and final hydrogen closure.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_LIMIT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
STATIC_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PHYSICAL_UNIT_BOUNDARY = ROOT / "docs" / "ATOMIC_LANE2_PHYSICAL_UNIT_LIMIT_BOUNDARY_NOTE_2026-04-29.md"
PHYSICAL_UNIT_RUNNER = ROOT / "scripts" / "frontier_atomic_lane2_physical_unit_limit_boundary.py"
KINETIC_REPAIR = ROOT / "docs" / "HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md"
KINETIC_REPAIR_RUNNER = ROOT / "scripts" / "frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py"
GREEN_KERNEL = ROOT / "docs" / "LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md"
GREEN_KERNEL_RUNNER = ROOT / "scripts" / "lattice_greens_z3_asymptotic_normalization_certificate.py"
I1_BRIDGE = ROOT / "docs" / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27.md"
I1_HYGIENE = ROOT / "docs" / "STATIC_SOURCE_READOUT_I1_ACCEPTED_PREMISE_BRIDGE_DEP_RESOLUTION_HYGIENE_COMPANION_NOTE_2026-06-04.md"
I1_RUNNER = ROOT / "scripts" / "static_source_readout_i1_accepted_premise_runner.py"
I1_HYGIENE_RUNNER = ROOT / "scripts" / "audit_companion_static_source_readout_i1_dep_resolution_2026_06_04.py"
ATOMIC_PROBE = ROOT / "docs" / "ATOMIC_HYDROGEN_HELIUM_PROBE_NOTE.md"
LATTICE_COMPANION = ROOT / "scripts" / "frontier_atomic_hydrogen_lattice_companion.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E_EV_COMPARATOR = 510_998.95
ALPHA0_INV_COMPARATOR = 137.035999084

NR_COULOMB_DECISION_INPUTS = {
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


def closes_nr_coulomb_decision(inputs: set[str]) -> bool:
    return NR_COULOMB_DECISION_INPUTS <= inputs


def closes_static_source_rydberg(inputs: set[str]) -> bool:
    return STATIC_SOURCE_RYDBERG_INPUTS <= inputs


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
        STATIC_TARGET,
        STATIC_NO_GO,
        PHYSICAL_UNIT_BOUNDARY,
        PHYSICAL_UNIT_RUNNER,
        KINETIC_REPAIR,
        KINETIC_REPAIR_RUNNER,
        GREEN_KERNEL,
        GREEN_KERNEL_RUNNER,
        I1_BRIDGE,
        I1_HYGIENE,
        I1_RUNNER,
        I1_HYGIENE_RUNNER,
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

    section("Required note content")
    required_phrases = [
        "Static-Source NR Coulomb Limit Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the static-source",
        "the zero-import static-source nonrelativistic Coulomb limit package",
        "SNR.1",
        "SNR.2",
        "SNR.3",
        "SNR.4",
        "SNR.5",
        "SNR.6",
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
        "No proper subset of those eleven contract inputs",
        "STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED",
        "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_NR_COULOMB_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply",
        "STATIC_SOURCE_LINEAR_RESPONSE_READOUT_RATIFIED",
        "ONE_BODY_NR_PHYSICAL_UNIT_LIMIT_RATIFIED",
        "HARTREE_SCALE_MAPPING_RATIFIED",
        "support, not the retained physical-unit one-body theorem",
        "epsilon_n = -1 / (2 n^2)",
        "E_H = m_e alpha(0)^2",
        "Rydberg = E_H / 2",
        "V_lat(r) = -4 pi g G(r) -> -g/|r|",
        "V(r) = -C g_bare^2 G(r)",
        "alpha := g_bare^2/(4 pi)",
        "Open PRs were refreshed on 2026-07-05 UTC",
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "the static-source NR Coulomb limit is packaged as a decision-ready",
        "broad no-go fails; narrowed static-source NR Coulomb decision",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(NR_COULOMB_DECISION_INPUTS)
    audit.check("full NR Coulomb contract accepts decision", closes_nr_coulomb_decision(full_inputs))
    for missing in sorted(NR_COULOMB_DECISION_INPUTS):
        reduced = set(NR_COULOMB_DECISION_INPUTS)
        reduced.remove(missing)
        audit.check(f"NR Coulomb decision fails without {missing}", not closes_nr_coulomb_decision(reduced))
    accepted_subsets = [subset for subset in all_subsets(NR_COULOMB_DECISION_INPUTS) if closes_nr_coulomb_decision(subset)]
    audit.check("only full tested contract subset closes NR Coulomb decision", accepted_subsets == [full_inputs])

    nr_limit_only = {"RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT"}
    with_me_alpha = {
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    }
    audit.check("NR Coulomb limit alone does not close static-source Rydberg", not closes_static_source_rydberg(nr_limit_only))
    audit.check("m_e plus alpha0 alone do not close static-source Rydberg", not closes_static_source_rydberg(with_me_alpha))
    audit.check("full static-source predicate closes model Rydberg target", closes_static_source_rydberg(set(STATIC_SOURCE_RYDBERG_INPUTS)))
    for missing in sorted(STATIC_SOURCE_RYDBERG_INPUTS):
        reduced = set(STATIC_SOURCE_RYDBERG_INPUTS)
        reduced.remove(missing)
        audit.check(f"static-source Rydberg predicate fails without {missing}", not closes_static_source_rydberg(reduced))

    section("Finite Coulomb and Hartree arithmetic")
    levels = {n: dimensionless_level(n) for n in range(1, 6)}
    audit.check("dimensionless E1 is -1/2", levels[1] == Fraction(-1, 2))
    for n, level in levels.items():
        ratio = level / levels[1]
        audit.check(f"dimensionless ratio n={n} is 1/n^2", ratio == Fraction(1, n * n))

    hartree_scales = [
        Fraction(20, 1),
        Fraction(27_211_386, 1_000_000),
        Fraction(40, 1),
    ]
    spectra = [[physical_level(n, scale) for n in (1, 2, 3)] for scale in hartree_scales]
    audit.check("all Hartree choices preserve E2/E1 = 1/4", all(row[1] / row[0] == Fraction(1, 4) for row in spectra))
    audit.check("all Hartree choices preserve E3/E1 = 1/9", all(row[2] / row[0] == Fraction(1, 9) for row in spectra))
    audit.check("different Hartree choices give different E1 values", len({row[0] for row in spectra}) == len(spectra))

    alpha0 = 1.0 / ALPHA0_INV_COMPARATOR
    hartree_ev = M_E_EV_COMPARATOR * alpha0 * alpha0
    rydberg_ev = 0.5 * hartree_ev
    audit.check("Hartree comparator is in known eV band", 27.21 < hartree_ev < 27.22, f"H={hartree_ev:.12f}")
    audit.check("Rydberg comparator is half Hartree", abs(2.0 * rydberg_ev - hartree_ev) < 1e-12)
    audit.check("Rydberg comparator is in known static-source band", 13.60 < rydberg_ev < 13.61, f"R={rydberg_ev:.12f}")

    for g in [0.25, 1.0, 3.0]:
        for r in [2.0, 10.0, 100.0]:
            lhs = -4.0 * math.pi * g * (1.0 / (4.0 * math.pi * r))
            rhs = -g / r
            audit.check(f"Green kernel gives -g/r for g={g} r={r}", abs(lhs - rhs) < 1e-15)

    for c_value in [1.0, 4.0 / 3.0]:
        for g_bare in [0.5, 1.0, 2.0]:
            alpha = g_bare * g_bare / (4.0 * math.pi)
            r = 7.0
            v_direct = -c_value * g_bare * g_bare / (4.0 * math.pi * r)
            v_alpha = -c_value * alpha / r
            audit.check(f"static-source readout alpha substitution C={c_value} g={g_bare}", abs(v_direct - v_alpha) < 1e-15)
    unit_alpha = 1.0 / (4.0 * math.pi)
    audit.check("unit-source coefficient gives -alpha/r", abs((-1.0 * unit_alpha / 5.0) - (-(1.0 / (4.0 * math.pi)) / 5.0)) < 1e-16)
    audit.check("color Casimir coefficient is not unit-source coefficient", abs((4.0 / 3.0) - 1.0) > 0.1)

    section("Authority boundary checks")
    goal = read(GOAL)
    static_target = read(STATIC_TARGET)
    static_no_go = read(STATIC_NO_GO)
    physical_unit_boundary = read(PHYSICAL_UNIT_BOUNDARY)
    physical_unit_runner = read(PHYSICAL_UNIT_RUNNER)
    kinetic_repair = read(KINETIC_REPAIR)
    green_kernel = read(GREEN_KERNEL)
    i1_bridge = read(I1_BRIDGE)
    i1_hygiene = read(I1_HYGIENE)
    atomic_probe = read(ATOMIC_PROBE)
    lattice_companion = read(LATTICE_COMPANION)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("static-source target", static_target),
    ]:
        audit.check(f"{container_name} references NR Coulomb decision packet", NOTE.name in container)

    audit.check("static packet references current-surface no-go", STATIC_NO_GO.name in note and "current retained, primitive, and open-PR surfaces do not supply" in note)
    audit.check("static no-go names retained handoff", "STATIC_SOURCE_NR_COULOMB_LIMIT_RETAINED" in static_no_go and "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT" in static_no_go)
    audit.check("static-source target keeps NR Coulomb limit downstream", "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT" in static_target)
    audit.check("physical-unit boundary names Hartree missing scale", "E_H = m_e alpha(0)^2" in physical_unit_boundary and "Rydberg = E_H / 2" in physical_unit_boundary)
    audit.check("physical-unit runner checks scale degeneracy", "Different Hartree scales give different E1 values" in physical_unit_runner)
    audit.check("kinetic repair refuses unique Cl3 kinetic derivation", "No such derivation is claimed here" in kinetic_repair)
    audit.check("kinetic repair refuses absolute eV predictions", "absolute-eV predictions" in kinetic_repair)
    audit.check("green kernel names framework-local 1/(4 pi r)", "framework-local large-separation normalization" in green_kernel and "1 / (4 pi |r|)" in green_kernel)
    audit.check("green kernel keeps references non-load-bearing", "not the load-bearing import" in green_kernel)
    audit.check("I1 bridge registers accepted-premise packet", "accepted-premise packet entry" in i1_bridge and "not derived in this bridge" in i1_bridge)
    audit.check("I1 bridge does not close downstream physical theorem", "This bridge does not close:" in i1_bridge)
    audit.check("I1 hygiene is meta and no status promotion", "substance-vs-grade separation" in i1_hygiene and "does not promote status" in i1_hygiene)
    audit.check("atomic probe is textbook scaffold only", "textbook inputs" in atomic_probe and "No `Cl(3)` on `Z^3` framework input" in atomic_probe)
    audit.check("atomic probe names Schrodinger gap", "single-particle Schrodinger" in atomic_probe and "not currently a retained" in atomic_probe)
    audit.check("lattice companion is coupling-relative only", "coupling-relative" in lattice_companion and "Absolute scale requires m_e" in lattice_companion)

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
        "static_source_nr_coulomb_primitive",
        "one_body_schrodinger_primitive",
        "static_source_readout_primitive",
        "electron_mass_primitive",
        "alpha0_primitive",
        "hydrogen_spectrum_primitive",
    ]:
        audit.check(f"no registered static-source shortcut: {absent}", absent not in registry_text)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of the static-source NR Coulomb limit.",
        "No derivation or ratification of the scalar lattice-operator atomic surface.",
        "No derivation or ratification of the static-source linear-response readout",
        "No derivation of the physical-unit one-body Schrodinger reduction.",
        "No derivation of `m_e`.",
        "No derivation of `alpha(0)`.",
        "No retained hydrogen calculation.",
        "No full precision hydrogen spectroscopy.",
        "No use of observed Rydberg, observed hydrogen lines, PDG `m_e`, observed",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the static-source NR Coulomb limit",
        "static-source NR Coulomb limit is retained",
        "This packet derives `m_e`",
        "This packet derives `alpha(0)`",
        "This packet claims hydrogen is retained",
        "full precision hydrogen is retained",
        "observed Rydberg is used as proof",
        "P1 is derived from the framework",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
