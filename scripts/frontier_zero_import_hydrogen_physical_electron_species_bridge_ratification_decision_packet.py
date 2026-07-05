#!/usr/bin/env python3
"""Verifier for the physical electron species-bridge decision packet.

This runner checks that the K3 species-bridge decision contract is explicit
and remains separate from native Koide bridge closure, absolute scale,
alpha(0), and hydrogen closure.
"""

from __future__ import annotations

import json
import unicodedata
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE_TRIAGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRIDGE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md"
PR4991_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_TIER_A_OWNER_RETIREMENT_PR4991_IMPACT_DISCRIMINATOR_2026-07-04.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SPECIES_MINIMUM = ROOT / "docs" / "SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
SPECIES_RATIFICATION = ROOT / "docs" / "SPECIES_BRIDGE_RESIDUAL_IS_RATIFICATION_CLASS_GRADE_SCOPED_BOUNDED_NOTE_2026-07-02.md"
SPECIES_REALIZED = ROOT / "docs" / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md"
SPECIES_RUNNER = ROOT / "scripts" / "frontier_species_bridge_ratification_class_2026_07_02.py"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


K3_DECISION_INPUTS = {
    "K3_SPECIES_BRIDGE_TEXT_LOCK",
    "C3_GRADE_SCOPE_LOCK",
    "MINIMUM_DECOMPOSITION_RETAINED",
    "RATIFICATION_CLASS_BOUNDARY_RETAINED",
    "PR4929_OWNER_ADOPTION",
    "NO_ABOVE_C3_CONTENT_INPUT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PHYSICAL_ELECTRON_INPUTS = {
    "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
    "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
    "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
}

HYDROGEN_INPUTS = PHYSICAL_ELECTRON_INPUTS | {
    "ALPHA0_RETAINED",
    "STATIC_SOURCE_RYDBERG_RETAINED",
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


def canon(text: str) -> str:
    return flat(unicodedata.normalize("NFKC", text))


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


def closes_k3_decision(inputs: set[str]) -> bool:
    return K3_DECISION_INPUTS <= inputs


def closes_physical_electron(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


Matrix = tuple[tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction]]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def scal(c: Fraction, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def diagm(a: Fraction, b: Fraction, c: Fraction) -> Matrix:
    z = Fraction(0)
    return ((a, z, z), (z, b, z), (z, z, c))


def diag_of(a: Matrix) -> list[Fraction]:
    return [a[i][i] for i in range(3)]


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ROUTE_TRIAGE,
        KOIDE_FIREWALL,
        BRIDGE_DECISION,
        BRIDGE_TARGET,
        PR4991_IMPACT,
        SOURCE_DECISION,
        A3_DECISION,
        SPECIES_NO_GO,
        SPECIES_MINIMUM,
        SPECIES_RATIFICATION,
        SPECIES_REALIZED,
        SPECIES_RUNNER,
        REGISTRY,
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
        "Physical Electron Species-Bridge Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the physical electron species bridge",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "the C3-grade physical electron species bridge for the charged-lepton Koide",
        "K3_SPECIES_BRIDGE_TEXT_LOCK",
        "C3_GRADE_SCOPE_LOCK",
        "MINIMUM_DECOMPOSITION_RETAINED",
        "RATIFICATION_CLASS_BOUNDARY_RETAINED",
        "PR4929_OWNER_ADOPTION",
        "NO_ABOVE_C3_CONTENT_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those ten contract inputs",
        "NATIVE_ZERO_SECTION_BRIDGE_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "ALPHA0_RETAINED",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "species bridge target remains needed",
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#4929` species-bridge partial-retirement | `SUCCESS`",
        "`#4897` species universal-floor reclassification | `SUCCESS`",
        "The current-main Tier-A registry still contains `species_bridge`",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad K3-retention claim fails; narrowed physical electron",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(K3_DECISION_INPUTS)
    audit.check("full K3 contract accepts decision", closes_k3_decision(full_inputs))
    for missing in sorted(K3_DECISION_INPUTS):
        reduced = set(K3_DECISION_INPUTS)
        reduced.remove(missing)
        audit.check(f"K3 decision fails without {missing}", not closes_k3_decision(reduced))
    accepted_subsets = [subset for subset in all_subsets(K3_DECISION_INPUTS) if closes_k3_decision(subset)]
    audit.check("only full tested contract subset closes K3 decision", accepted_subsets == [full_inputs])

    k3_consequence = {"PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED"}
    audit.check("K3 alone does not close physical electron", not closes_physical_electron(k3_consequence))
    audit.check("full physical electron predicate closes electron", closes_physical_electron(set(PHYSICAL_ELECTRON_INPUTS)))
    for missing in sorted(PHYSICAL_ELECTRON_INPUTS):
        reduced = set(PHYSICAL_ELECTRON_INPUTS)
        reduced.remove(missing)
        audit.check(f"physical electron predicate fails without {missing}", not closes_physical_electron(reduced))
    audit.check("physical electron alone does not close hydrogen", not closes_hydrogen(set(PHYSICAL_ELECTRON_INPUTS)))
    audit.check("full hydrogen predicate model closes hydrogen", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Finite C3 witness checks")
    orbit = []
    x = 0
    p = {0: 1, 1: 2, 2: 0}
    for _ in range(3):
        orbit.append(x)
        x = p[x]
    audit.check("C3 action has one transitive orbit on three labels", set(orbit) == {0, 1, 2} and x == 0)

    f0 = Fraction(0)
    f1 = Fraction(1)
    i3: Matrix = ((f1, f0, f0), (f0, f1, f0), (f0, f0, f1))
    c3: Matrix = ((f0, f0, f1), (f1, f0, f0), (f0, f1, f0))
    c3_sq = matmul(c3, c3)
    h = diagm(Fraction(0), Fraction(3), Fraction(6))
    d_h = diag_of(h)
    spread_h = max(d_h) - min(d_h)
    h_avg = add(add(scal(Fraction(1, 3), h), scal(Fraction(1, 3), matmul(matmul(c3, h), transpose(c3)))), scal(Fraction(1, 3), matmul(matmul(c3_sq, h), transpose(c3_sq))))
    d_avg = diag_of(h_avg)
    audit.check("generic corner weights have spread 6", spread_h == Fraction(6))
    audit.check("C3 orbit average collapses spread to 0", max(d_avg) - min(d_avg) == 0)
    audit.check("C3 orbit average is 3I", h_avg == scal(Fraction(3), i3))

    c1 = c3
    c2 = c3_sq
    e: Matrix = ((f1, f0, f0), (f0, f0, f1), (f0, f1, f0))
    e_broken = c1
    audit.check("two regular C3 carriers are distinct", c1 != c2)
    audit.check("intertwiner is unitary", matmul(transpose(e), e) == i3 and e != i3)
    audit.check("intertwiner satisfies E*C1 = C2*E", matmul(e, c1) == matmul(c2, e))
    audit.check("broken shift fails the intertwiner equation", matmul(e_broken, c1) != matmul(c2, e_broken))

    registered = ("electron-pattern", "muon-pattern", "tau-pattern")
    record_assignment = {0: registered[0], 1: registered[1], 2: registered[2]}
    assignments = []
    for perm in permutations(registered):
        candidate = {0: perm[0], 1: perm[1], 2: perm[2]}
        if candidate == record_assignment:
            assignments.append(candidate)
    audit.check("nondegenerate supplied records leave exactly one sector assignment", len(assignments) == 1)
    audit.check("sixfold naming orbit remains visible", len(list(permutations(registered))) == 6)

    section("Authority boundary checks")
    goal = read(GOAL)
    route_triage = read(ROUTE_TRIAGE)
    koide_firewall = read(KOIDE_FIREWALL)
    bridge_decision = read(BRIDGE_DECISION)
    bridge_target = read(BRIDGE_TARGET)
    pr4991 = read(PR4991_IMPACT)
    source_decision = read(SOURCE_DECISION)
    a3_decision = read(A3_DECISION)
    species_no_go = read(SPECIES_NO_GO)
    species_minimum = canon(read(SPECIES_MINIMUM))
    species_ratification = canon(read(SPECIES_RATIFICATION))
    species_realized = canon(read(SPECIES_REALIZED)).lower()
    species_runner = canon(read(SPECIES_RUNNER))
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = json.loads(read(TIER_A_REGISTRY))
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("route triage", route_triage),
        ("Koide firewall", koide_firewall),
    ]:
        audit.check(f"{container_name} references species decision packet", NOTE.name in container)

    audit.check("bridge decision keeps species bridge downstream", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in bridge_decision)
    audit.check("bridge target keeps species bridge downstream", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in bridge_target)
    audit.check("PR4991 impact keeps K3 limited", "K3 species bridge" in pr4991 and "No above-C3 taste/Dirac/chirality content" in pr4991)
    audit.check("source decision remains K4 scale-side support", "S_l = 1/256" in source_decision and "does not derive `m_e`" in source_decision)
    audit.check("A3 decision remains precision placement only", "does not ratify A3" in a3_decision and "does not derive" in a3_decision and "`C_A3`" in a3_decision)
    audit.check("species decision references species no-go", SPECIES_NO_GO.name in note and "species bridge target remains needed" in note)
    audit.check(
        "species no-go keeps K3 open",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in species_no_go
        and "current retained, primitive, and open-PR surfaces do not supply" in species_no_go,
    )

    source_requirements = [
        "carrying no tested C3-grade number, selector, ordering, or weight",
        "two provably-vacuous",
        "within-triplet naming",
        "carrier-triplet choice",
        "It remains an interpretive bridge",
    ]
    for phrase in source_requirements:
        audit.check(f"species minimum source phrase present: {phrase}", phrase in species_minimum)

    ratification_requirements = [
        "owner decision",
        "nothing adopted",
        "fails",
        "path-extension",
        "second relatum is external nature",
        "taste/Dirac/chirality",
    ]
    for phrase in ratification_requirements:
        audit.check(f"species ratification source phrase present: {phrase}", phrase in species_ratification)

    realized_requirements = [
        "no admitted content beyond named, already-tracked items survives",
        "does **not** edit the tier-a registry",
        "does **not** derive the carrier locus",
        "does **not** select `r=1/2`",
        "does **not** derive",
    ]
    for phrase in realized_requirements:
        audit.check(f"realized species source phrase present: {phrase}", phrase in species_realized)

    audit.check("species runner encodes positive condition failure", "POSITIVE_CONDITION" in species_runner and "FAILS" in species_runner)

    ac_targets = [target for target in tier_a["derivation_targets"].values() if target.get("label") == "AC_phi_lambda"]
    audit.check("current-main Tier-A registry has AC_phi_lambda target", len(ac_targets) == 1)
    if ac_targets:
        audit.check("current-main AC_phi_lambda minimum still contains species_bridge", "species_bridge" in ac_targets[0].get("minimum_decomposition", []))
    audit.check("AC_phi_lambda is not a primitive registry node", "AC_phi_lambda" not in nodes)
    audit.check("no species bridge primitive registered", "physical_electron_species_bridge_primitive" not in nodes)
    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms keep downstream gates outside axiom content", "remain outside axiom content" in minimal and "AC_phi_lambda" in minimal)
    audit.check("scale primitive excludes dimensionless Koide content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes state selection and values", "state-selection rule" in realized and "or value is supplied" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5012` chirality domain-wall free-field note | `SUCCESS`",
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `SUCCESS`",
        "`#4929` species-bridge partial-retirement | `SUCCESS`",
        "`#4897` species universal-floor reclassification | `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of the physical electron species bridge.",
        "No current-main removal of `species_bridge` from the Tier-A registry.",
        "No derivation of K1 occupancy/counting or K2 R-eta/phase readout.",
        "No derivation or ratification of Z1/Z2/Z3 native bridge clauses.",
        "No derivation of `a_l^2`, `S_l`, `C_A3`, `m_e`, `alpha(0)`, or hydrogen",
        "No above-C3 taste, Dirac, chirality, CKM/PMNS, or carrier-selection closure.",
        "No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the physical electron species bridge",
        "physical electron species bridge is retained",
        "K1 is derived",
        "K2 is derived",
        "Z1 is derived",
        "Z2 is derived",
        "Z3 is derived",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
