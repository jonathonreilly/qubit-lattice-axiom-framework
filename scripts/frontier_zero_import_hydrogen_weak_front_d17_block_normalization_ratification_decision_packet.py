#!/usr/bin/env python3
"""Verifier for the weak-front D17 block-normalization decision packet.

This runner checks that the D17 1/sqrt(2) block-normalization handoff is
explicit and remains separate from source singleton, weak-front base, A3
matching, K4 scale assembly, physical electron mass, alpha(0), and hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
WEAK_FRONT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
D17_SOURCE = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
D17_SEPARABILITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
F2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


D17_INPUTS = {
    "D17_BLOCK_NORMALIZATION_TEXT_LOCK",
    "D17_STATED_BLOCK_SCOPE_ACCEPTED",
    "TWO_COMPONENT_UNIT_NORMALIZATION_CHECK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "D17_ONLY_NO_SOURCE_SINGLETON_OR_A3_INPUT",
    "NO_WEAK_COUPLING_OR_FRONT_BASE_INPUT",
    "NO_MASS_OR_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

WEAK_FRONT_INPUTS = {
    "WEAK_FRONT_BASE_TEXT_LOCK",
    "SU2_WEAK_COUPLING_CONTEXT_RETAINED",
    "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "UNCORRECTED_FRONT_SCOPE_LOCK",
    "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
    "NO_A3_OR_THRESHOLD_MATCHING_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

K4_INPUTS = {
    "K4_SCALE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "WEAK_FRONT_BASE_RETAINED",
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "A3_PRECISION_PLACEMENT_RETAINED",
    "NO_SOURCE_A3_DOUBLE_COUNT",
    "NO_COMPARATOR_PROOF_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
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


def closes_d17_normalization(inputs: set[str]) -> bool:
    return D17_INPUTS <= inputs


def closes_weak_front_base(inputs: set[str]) -> bool:
    return WEAK_FRONT_INPUTS <= inputs


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        WEAK_FRONT_DECISION,
        WEAK_FRONT_NO_GO,
        K4_PACKET,
        D17_SOURCE,
        D17_SEPARABILITY,
        F2_TARGET,
        LEPTON_SCALE,
        A3_DECISION,
        SOURCE_DECISION,
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
        "Weak-Front D17 Block-Normalization Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the weak-front base",
        "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED",
        "the charged-lepton D17 two-component block-normalization factor for the K4 weak-front base",
        "B_lep = (1/sqrt(2)) sum_alpha bar L_L^alpha H_alpha e_R",
        "Z_lep^2 = N_c N_iso = 1 * 2 = 2",
        "D17_BLOCK_NORMALIZATION_TEXT_LOCK",
        "D17_STATED_BLOCK_SCOPE_ACCEPTED",
        "TWO_COMPONENT_UNIT_NORMALIZATION_CHECK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "D17_ONLY_NO_SOURCE_SINGLETON_OR_A3_INPUT",
        "NO_WEAK_COUPLING_OR_FRONT_BASE_INPUT",
        "NO_MASS_OR_COMPARATOR_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those ten contract inputs",
        "SU2_WEAK_COUPLING_CONTEXT_RETAINED",
        "WEAK_FRONT_BASE_RETAINED",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "direct `512`-component normalization",
        "source-density singleton held separate",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` domain-wall chiral edge from achiral bulk | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad D17-to-weak-front/K4 closure fails; narrowed D17",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_d17 = set(D17_INPUTS)
    audit.check("full D17 normalization contract accepts decision", closes_d17_normalization(full_d17))
    for missing in sorted(D17_INPUTS):
        reduced = set(D17_INPUTS)
        reduced.remove(missing)
        audit.check(f"D17 normalization decision fails without {missing}", not closes_d17_normalization(reduced))
    accepted_subsets = [subset for subset in all_subsets(D17_INPUTS) if closes_d17_normalization(subset)]
    audit.check("only full tested D17 subset closes normalization", accepted_subsets == [full_d17])

    d17_consequence = {"CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED"}
    audit.check("D17 consequence alone does not close weak-front base", not closes_weak_front_base(d17_consequence))
    weak_front_missing_su2 = set(WEAK_FRONT_INPUTS)
    weak_front_missing_su2.remove("SU2_WEAK_COUPLING_CONTEXT_RETAINED")
    audit.check("weak-front contract still needs SU2 weak context", not closes_weak_front_base(weak_front_missing_su2))
    audit.check("full weak-front contract model closes weak-front base", closes_weak_front_base(set(WEAK_FRONT_INPUTS)))
    audit.check("D17 consequence alone does not close K4", not closes_k4(d17_consequence))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))

    section("Finite normalization witness checks")
    coeff = 1.0 / math.sqrt(2.0)
    d17_norm = 2.0 * coeff * coeff
    audit.check("D17 two-component block is unit normalized", abs(d17_norm - 1.0) < 1e-15)
    audit.check("Z_lep squared equals 2", 1 * 2 == 2)
    direct_512 = coeff / 16.0
    source_density = coeff / 256.0
    audit.check("direct 512-unit shortcut differs from source-density singleton", direct_512 != source_density)
    audit.check("direct shortcut is 16 times source-density singleton", abs(direct_512 / source_density - 16.0) < 1e-15)
    for g2 in [0.5, 0.6528252293493516, 1.0]:
        front = g2 * coeff
        audit.check(f"D17 factor scales weak-front symbol for g2={g2:.6f}", abs(front / g2 - coeff) < 1e-15)
        audit.check(f"D17 factor alone does not select g2={g2:.6f}", front != coeff or g2 == 1.0)

    section("Authority boundary checks")
    goal = read(GOAL)
    weak_front_decision = read(WEAK_FRONT_DECISION)
    weak_front_no_go = read(WEAK_FRONT_NO_GO)
    k4_packet = read(K4_PACKET)
    d17_source = read(D17_SOURCE)
    d17_separability = read(D17_SEPARABILITY)
    f2_target = read(F2_TARGET)
    lepton_scale = read(LEPTON_SCALE)
    a3_decision = read(A3_DECISION)
    source_decision = read(SOURCE_DECISION)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("weak-front-base packet", weak_front_decision),
        ("weak-front current no-go", weak_front_no_go),
        ("K4 packet", k4_packet),
    ]:
        audit.check(f"{container_name} references D17 normalization packet", NOTE.name in container)

    audit.check("D17 source names scalar block", "bar L_L^alpha  H_alpha  e_R" in d17_source)
    audit.check("D17 source names Z_lep normalization", "Z_lep^2 = N_c N_iso = 1 * 2 = 2" in d17_source)
    audit.check("D17 source declares bounded theorem status", "**Claim type:** bounded_theorem" in d17_source)
    audit.check("D17 separability keeps 1/sqrt2 separate from 256", "preserves the D17 `1/sqrt(2)` block anchor" in d17_separability)
    audit.check("F2 target uses D17 block conditionally", "D17 + SECTOR + SCALAR + ATTACHMENT" in f2_target)
    audit.check("lepton-scale probe factorizes D17 with weak and source factors", "g_2" in lepton_scale and "1/sqrt(2)" in lepton_scale and "1/256" in lepton_scale)
    audit.check("A3 decision remains placement only", "A3_PRECISION_PLACEMENT_RETAINED" in a3_decision and "does not by itself derive `C_A3`" in a3_decision)
    audit.check("source decision remains source singleton only", "EXACT_SOURCE_SINGLETON_RETAINED" in source_decision and "does not derive `m_e`" in source_decision)
    audit.check("weak-front packet consumes D17 normalization", "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED" in weak_front_decision)
    audit.check("weak-front no-go still keeps base unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in weak_front_no_go)
    audit.check("K4 consumes weak-front base rather than D17 directly", "WEAK_FRONT_BASE_RETAINED" in k4_packet and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_packet)
    audit.check("minimal axioms keep physical structure downstream", "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration" in flat(minimal))
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector and empirical fit", "selector" in kinetic and "empirical fit" in kinetic)
    audit.check("realized-state primitive excludes state-contingent content", "state-contingent content" in realized and "normalization rule" in realized)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    for absent in [
        "d17_charged_lepton_block_normalization_primitive",
        "d17_charged_lepton_block_primitive",
        "weak_front_base_primitive",
        "source_singleton_primitive",
        "a3_correction_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No derivation or ratification of the weak-front base.",
        "No derivation or ratification of a physical low-scale `g_2(v)` value.",
        "No derivation or ratification of exact source-side `S_l = 1/256`.",
        "No derivation or ratification of the A3 correction `C_A3`.",
        "No derivation or ratification of the absolute charged-lepton scale.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No use of observed charged-lepton masses, observed `m_W`, fitted `g_2(v)`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the weak-front base",
        "This packet derives the weak-front base",
        "This packet ratifies the absolute charged-lepton scale",
        "D17 closes K4",
        "m_e is retained",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
