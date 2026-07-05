#!/usr/bin/env python3
"""Verifier for the physical electron species-bridge current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply the K3 species-bridge handoff consumed by the physical
electron mass lane. It preserves the positive owner/audit route and does not
derive m_e, alpha(0), Rydberg, or hydrogen.
"""

from __future__ import annotations

import json
import unicodedata
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_CURRENT_SURFACE_NO_GO_2026-07-05.md"
NATIVE_BRIDGE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRIDGE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
K4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
BRANCH_MASS_MAP_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SPECIES_MINIMUM = ROOT / "docs" / "SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md"
SPECIES_RATIFICATION = ROOT / "docs" / "SPECIES_BRIDGE_RESIDUAL_IS_RATIFICATION_CLASS_GRADE_SCOPED_BOUNDED_NOTE_2026-07-02.md"
SPECIES_REALIZED = ROOT / "docs" / "ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md"
SPECIES_RUNNER = ROOT / "scripts" / "frontier_species_bridge_ratification_class_2026_07_02.py"
CHIRALITY_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_CHIRALITY_DOMAIN_WALL_PR5017_5018_IMPACT_DISCRIMINATOR_2026-07-05.md"
W4C_IMPACT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_W4C_PR5028_IMPACT_DISCRIMINATOR_2026-07-05.md"
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
    "KOIDE_BRANCH_MASS_MAP_RETAINED",
    "SCALE_REFERENCE_PRIMITIVE_CHAIN_SATISFIED",
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


Matrix = tuple[tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction]]


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


def closes_k3(inputs: set[str]) -> bool:
    return K3_DECISION_INPUTS <= inputs


def closes_physical_electron(inputs: set[str]) -> bool:
    return PHYSICAL_ELECTRON_INPUTS <= inputs


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
        KOIDE_FIREWALL,
        SPECIES_DECISION,
        PHYSICAL_ELECTRON_PACKET,
        PHYSICAL_ELECTRON_NO_GO,
        NATIVE_BRIDGE_NO_GO,
        BRIDGE_DECISION,
        K4_NO_GO,
        BRANCH_MASS_MAP_NO_GO,
        SPECIES_MINIMUM,
        SPECIES_RATIFICATION,
        SPECIES_REALIZED,
        SPECIES_RUNNER,
        CHIRALITY_IMPACT,
        W4C_IMPACT,
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
        "Physical Electron Species-Bridge Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not ratify the physical electron species bridge",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED",
        "current retained, primitive, merged-PR, and open-PR surfaces do not supply",
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
        "PR4929_OWNER_ADOPTION",
        "single C3 orbit on three labels",
        "orbit average of `diag(0,3,6)`",
        "two regular C3 carriers with a unitary intertwiner",
        "nondegenerate registered pattern in a supplied context",
        "physical_electron_species_bridge_primitive",
        "physical_electron_species_primitive",
        "species_bridge_primitive",
        "c3_species_bridge_primitive",
        "electron_species_bridge_primitive",
        "electron_mass_primitive",
        "ZERO_IMPORT_HYDROGEN_CHIRALITY_DOMAIN_WALL_PR5017_5018_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_KOIDE_W4C_PR5028_IMPACT_DISCRIMINATOR_2026-07-05.md",
        "`#5028` W4c labeling/species repairs | merged after open lane-relevant refresh",
        "`#5018` domain-wall edge content vs SM chiral fermions map | `CLEAN` / `SUCCESS`",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | `CLEAN` / `SUCCESS`",
        "`#5014` record-formation front/domain-wall chirality | `CLEAN` / `SUCCESS`",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "`#4929` species-bridge partial-retirement | `CLEAN` / `SUCCESS`",
        "`#4897` species universal-floor reclassification | `DIRTY` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad species-bridge no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("K3 predicate checks")
    full_inputs = set(K3_DECISION_INPUTS)
    audit.check("full K3 contract accepts retained handoff", closes_k3(full_inputs))
    for missing in sorted(K3_DECISION_INPUTS):
        reduced = set(K3_DECISION_INPUTS)
        reduced.remove(missing)
        audit.check(f"K3 handoff fails without {missing}", not closes_k3(reduced))
    accepted_subsets = [subset for subset in all_subsets(K3_DECISION_INPUTS) if closes_k3(subset)]
    audit.check("only full K3 subset closes handoff", accepted_subsets == [full_inputs])
    current_surface = {
        "K3_SPECIES_BRIDGE_TEXT_LOCK",
        "C3_GRADE_SCOPE_LOCK",
        "MINIMUM_DECOMPOSITION_RETAINED",
        "RATIFICATION_CLASS_BOUNDARY_RETAINED",
        "NO_ABOVE_C3_CONTENT_INPUT",
        "NO_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
    }
    audit.check("current surface without adoption/owner/audit does not close K3", not closes_k3(current_surface))
    audit.check(
        "retained K3 alone does not close physical electron",
        not closes_physical_electron({"PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED"}),
    )
    audit.check(
        "full physical electron predicate still needs K3 plus other inputs",
        closes_physical_electron(set(PHYSICAL_ELECTRON_INPUTS)),
    )

    section("Finite C3 witness checks")
    orbit = []
    x = 0
    cycle = {0: 1, 1: 2, 2: 0}
    for _ in range(3):
        orbit.append(x)
        x = cycle[x]
    audit.check("C3 action has one transitive orbit on three labels", set(orbit) == {0, 1, 2} and x == 0)

    f0 = Fraction(0)
    f1 = Fraction(1)
    i3: Matrix = ((f1, f0, f0), (f0, f1, f0), (f0, f0, f1))
    c3: Matrix = ((f0, f0, f1), (f1, f0, f0), (f0, f1, f0))
    c3_sq = matmul(c3, c3)
    h = diagm(Fraction(0), Fraction(3), Fraction(6))
    d_h = diag_of(h)
    spread_h = max(d_h) - min(d_h)
    h_avg = add(
        add(scal(Fraction(1, 3), h), scal(Fraction(1, 3), matmul(matmul(c3, h), transpose(c3)))),
        scal(Fraction(1, 3), matmul(matmul(c3_sq, h), transpose(c3_sq))),
    )
    d_avg = diag_of(h_avg)
    audit.check("generic corner weights have spread 6", spread_h == Fraction(6))
    audit.check("C3 orbit average collapses spread to 0", max(d_avg) - min(d_avg) == 0)
    audit.check("C3 orbit average is 3I", h_avg == scal(Fraction(3), i3))

    e: Matrix = ((f1, f0, f0), (f0, f0, f1), (f0, f1, f0))
    broken = c3
    audit.check("two regular C3 carriers are distinct", c3 != c3_sq)
    audit.check("intertwiner is unitary", matmul(transpose(e), e) == i3 and e != i3)
    audit.check("intertwiner satisfies E*C1 = C2*E", matmul(e, c3) == matmul(c3_sq, e))
    audit.check("broken shift fails the intertwiner equation", matmul(broken, c3) != matmul(c3_sq, broken))

    registered = ("electron-pattern", "muon-pattern", "tau-pattern")
    record_assignment = {0: registered[0], 1: registered[1], 2: registered[2]}
    assignments = []
    for perm in permutations(registered):
        candidate = {0: perm[0], 1: perm[1], 2: perm[2]}
        if candidate == record_assignment:
            assignments.append(candidate)
    audit.check("nondegenerate supplied records leave exactly one sector assignment", len(assignments) == 1)
    audit.check("sixfold naming orbit remains visible", len(list(permutations(registered))) == 6)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    koide_firewall = read(KOIDE_FIREWALL)
    species_decision = read(SPECIES_DECISION)
    physical_packet = read(PHYSICAL_ELECTRON_PACKET)
    physical_no_go = read(PHYSICAL_ELECTRON_NO_GO)
    native_bridge_no_go = read(NATIVE_BRIDGE_NO_GO)
    bridge_decision = read(BRIDGE_DECISION)
    k4_no_go = read(K4_NO_GO)
    branch_no_go = read(BRANCH_MASS_MAP_NO_GO)
    chirality_impact = read(CHIRALITY_IMPACT)
    w4c_impact = read(W4C_IMPACT)
    species_minimum = canon(read(SPECIES_MINIMUM))
    species_ratification = canon(read(SPECIES_RATIFICATION))
    species_realized = canon(read(SPECIES_REALIZED)).lower()
    species_runner = canon(read(SPECIES_RUNNER))
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry_text = read(REGISTRY)
    registry = json.loads(registry_text)
    tier_a = json.loads(read(TIER_A_REGISTRY))
    nodes = registry["nodes"]

    audit.check("goal packet references species no-go", NOTE.name in goal and "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in goal)
    audit.check("Koide firewall references species no-go", NOTE.name in koide_firewall and "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in koide_firewall)
    audit.check("species decision references species no-go", NOTE.name in species_decision and "species bridge target remains needed" in species_decision)
    audit.check("physical electron packet references species no-go", NOTE.name in physical_packet and "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in physical_packet)
    audit.check("physical electron no-go references species no-go", NOTE.name in physical_no_go and "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in physical_no_go)
    audit.check(
        "species no-go references chirality impact note",
        CHIRALITY_IMPACT.name in note and "#5018" in note and "#5017" in note,
    )
    audit.check(
        "species no-go references #5028 impact note",
        W4C_IMPACT.name in note and "#5028" in note,
    )
    audit.check(
        "chirality impact keeps K3 separate",
        "above-C3 chirality/domain-wall content" in chirality_impact
        and "No derivation or ratification of `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`." in chirality_impact,
    )
    audit.check(
        "W4c impact keeps K3 separate",
        "labeling/species dependency-surface readiness" in w4c_impact
        and "No derivation or ratification of `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`." in w4c_impact,
    )
    audit.check(
        "native bridge no-go keeps K3 separate",
        "physical electron species bridge" in native_bridge_no_go
        and "No derivation or ratification of the physical electron species bridge." in native_bridge_no_go,
    )
    audit.check("bridge decision keeps species bridge downstream", "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED" in bridge_decision)
    audit.check("K4 no-go keeps species independent", "physical electron species bridge" in k4_no_go and "independent" in k4_no_go)
    branch_no_go_flat = flat(branch_no_go)
    audit.check("branch mass-map no-go does not supply species", "physical species identity" in branch_no_go_flat and "not derived in this note" in branch_no_go_flat)

    for phrase in [
        "carrying no tested C3-grade number, selector, ordering, or weight",
        "two provably-vacuous",
        "within-triplet naming",
        "carrier-triplet choice",
        "It remains an interpretive bridge",
    ]:
        audit.check(f"species minimum source phrase present: {phrase}", phrase in species_minimum)
    for phrase in [
        "owner decision",
        "nothing adopted",
        "fails",
        "path-extension",
        "second relatum is external nature",
        "taste/Dirac/chirality",
    ]:
        audit.check(f"species ratification source phrase present: {phrase}", phrase in species_ratification)
    for phrase in [
        "no admitted content beyond named, already-tracked items survives",
        "does **not** edit the tier-a registry",
        "does **not** derive the carrier locus",
        "does **not** select `r=1/2`",
        "does **not** derive",
    ]:
        audit.check(f"realized species source phrase present: {phrase}", phrase in species_realized)
    audit.check("species runner encodes positive condition failure", "POSITIVE_CONDITION" in species_runner and "FAILS" in species_runner)

    ac_targets = [target for target in tier_a["derivation_targets"].values() if target.get("label") == "AC_phi_lambda"]
    audit.check("current-main Tier-A registry has AC_phi_lambda target", len(ac_targets) == 1)
    if ac_targets:
        audit.check("current-main AC_phi_lambda minimum still contains species_bridge", "species_bridge" in ac_targets[0].get("minimum_decomposition", []))
    audit.check("AC_phi_lambda is not a primitive registry node", "AC_phi_lambda" not in nodes)
    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "physical_electron_species_bridge_primitive",
        "physical_electron_species_primitive",
        "species_bridge_primitive",
        "c3_species_bridge_primitive",
        "electron_species_bridge_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered species shortcut: {absent}", absent not in registry_text)
    audit.check("minimal axioms keep downstream gates outside axiom content", "remain outside axiom content" in minimal and "AC_phi_lambda" in minimal)
    audit.check("scale primitive excludes dimensionless Koide content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes state selection and values", "state-selection rule" in realized and "or value is supplied" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5028` W4c labeling/species repairs | merged after open lane-relevant refresh",
        "`#5018` domain-wall edge content vs SM chiral fermions map | `CLEAN` / `SUCCESS`",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | `CLEAN` / `SUCCESS`",
        "`#5014` record-formation front/domain-wall chirality | `CLEAN` / `SUCCESS`",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "`#4929` species-bridge partial-retirement | `CLEAN` / `SUCCESS`",
        "`#4897` species universal-floor reclassification | `DIRTY` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_nonclaims = [
        "No derivation or ratification of `PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED`.",
        "No current-main removal of `species_bridge` from the Tier-A registry.",
        "No derivation or ratification of `PR4929_OWNER_ADOPTION`.",
        "No derivation of K1 occupancy/counting or K2 R-eta/phase readout.",
        "No derivation or ratification of Z1/Z2/Z3 native bridge clauses.",
        "No derivation or ratification of the Koide branch mass-map.",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No spending of PR `#5017` or PR `#5018` as K3 species-bridge closure.",
        "No spending of PR `#5028` as K3 species-bridge closure.",
        "No derivation of `a_l^2`, `S_l`, `C_A3`, `m_e`, `alpha(0)`, or hydrogen",
        "No above-C3 taste, Dirac, chirality, CKM/PMNS, or carrier-selection closure.",
        "No use of observed lepton masses, observed `m_W`, fitted `a_l`, fitted",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
        "No audit status change for any cited row.",
    ]
    for phrase in explicit_nonclaims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden = [
        "This note ratifies the physical electron species bridge",
        "physical electron species bridge is retained",
        "PHYSICAL_ELECTRON_SPECIES_BRIDGE_RETAINED is supplied",
        "PR4929_OWNER_ADOPTION is supplied",
        "species_bridge is removed from the Tier-A registry",
        "m_e is derived",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
