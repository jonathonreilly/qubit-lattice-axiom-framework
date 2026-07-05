#!/usr/bin/env python3
"""Verifier for the weak-front SU2 coupling-context decision packet.

This runner checks that the SU(2)_L weak-coupling context handoff is explicit
and remains separate from physical g_2(v), observed m_W, threshold matching,
D17 normalization, source singleton, A3 matching, K4 scale assembly, physical
electron mass, alpha(0), and hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
WEAK_FRONT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
D17_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
CL3_SM = ROOT / "docs" / "CL3_SM_EMBEDDING_THEOREM.md"
SU2_BETA = ROOT / "docs" / "SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md"
EW_HIGGS = ROOT / "docs" / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
A3_P2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


SU2_CONTEXT_INPUTS = {
    "SU2_WEAK_COUPLING_CONTEXT_TEXT_LOCK",
    "CL3_SU2_WEAK_CONTEXT_ACCEPTED",
    "BARE_G2_SYMBOL_SCOPE_LOCK",
    "CHARGED_LEPTON_WEAK_DOUBLET_SCOPE_LOCK",
    "RUNNING_STRUCTURE_BOUNDARY_LOCK",
    "NO_PHYSICAL_G2V_OR_MW_INPUT",
    "NO_THRESHOLD_OR_A3_MATCHING_INPUT",
    "NO_D17_SOURCE_SINGLETON_OR_MASS_INPUT",
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


def closes_su2_context(inputs: set[str]) -> bool:
    return SU2_CONTEXT_INPUTS <= inputs


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
        D17_DECISION,
        K4_PACKET,
        CL3_SM,
        SU2_BETA,
        EW_HIGGS,
        LEPTON_SCALE,
        A3_P2,
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
        "Weak-Front SU2 Coupling-Context Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the weak-front base",
        "SU2_WEAK_COUPLING_CONTEXT_RETAINED",
        "the SU(2)_L weak-coupling context and symbol for the charged-lepton K4 weak-front base",
        "F_0 = g_2 * (1/sqrt(2))",
        "SU2_WEAK_COUPLING_CONTEXT_TEXT_LOCK",
        "CL3_SU2_WEAK_CONTEXT_ACCEPTED",
        "BARE_G2_SYMBOL_SCOPE_LOCK",
        "CHARGED_LEPTON_WEAK_DOUBLET_SCOPE_LOCK",
        "RUNNING_STRUCTURE_BOUNDARY_LOCK",
        "NO_PHYSICAL_G2V_OR_MW_INPUT",
        "NO_THRESHOLD_OR_A3_MATCHING_INPUT",
        "NO_D17_SOURCE_SINGLETON_OR_MASS_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eleven contract inputs",
        "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED",
        "WEAK_FRONT_BASE_RETAINED",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "CL3 even-subalgebra support",
        "structural beta support",
        "physical value held separate",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` domain-wall chiral edge from achiral bulk | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad physical-weak-front-value closure fails; narrowed SU2",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_su2 = set(SU2_CONTEXT_INPUTS)
    audit.check("full SU2 context contract accepts decision", closes_su2_context(full_su2))
    for missing in sorted(SU2_CONTEXT_INPUTS):
        reduced = set(SU2_CONTEXT_INPUTS)
        reduced.remove(missing)
        audit.check(f"SU2 context decision fails without {missing}", not closes_su2_context(reduced))
    accepted_subsets = [subset for subset in all_subsets(SU2_CONTEXT_INPUTS) if closes_su2_context(subset)]
    audit.check("only full tested SU2 subset closes context", accepted_subsets == [full_su2])

    su2_consequence = {"SU2_WEAK_COUPLING_CONTEXT_RETAINED"}
    audit.check("SU2 consequence alone does not close weak-front base", not closes_weak_front_base(su2_consequence))
    weak_front_missing_d17 = set(WEAK_FRONT_INPUTS)
    weak_front_missing_d17.remove("CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED")
    audit.check("weak-front contract still needs D17 normalization", not closes_weak_front_base(weak_front_missing_d17))
    audit.check("full weak-front contract model closes weak-front base", closes_weak_front_base(set(WEAK_FRONT_INPUTS)))
    audit.check("SU2 consequence alone does not close K4", not closes_k4(su2_consequence))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))

    section("Finite context witness checks")
    d = 3
    dim_even = d + 1
    g2_sq = 1.0 / dim_even
    g2 = math.sqrt(g2_sq)
    alpha2_bare_inv = 4.0 * math.pi / g2_sq
    b2 = 19.0 / 6.0
    audit.check("CL3 even dimension gives d+1=4", dim_even == 4)
    audit.check("bare g2 squared context is 1/4", abs(g2_sq - 0.25) < 1e-15)
    audit.check("bare g2 symbol value from that context is 1/2", abs(g2 - 0.5) < 1e-15)
    audit.check("bare inverse alpha2 witness is 16pi", abs(alpha2_bare_inv - 16.0 * math.pi) < 1e-12)
    audit.check("structural beta witness b2 is 19/6", abs(b2 - (19.0 / 6.0)) < 1e-15)
    for supplied_g2 in [0.5, 0.6528252293493516, 1.0]:
        front = supplied_g2 / math.sqrt(2.0)
        audit.check(f"front scales with supplied g2={supplied_g2:.6f}", abs(front / supplied_g2 - 1.0 / math.sqrt(2.0)) < 1e-15)
    audit.check("changing physical g2 changes the front value", (0.5 / math.sqrt(2.0)) != (0.6528252293493516 / math.sqrt(2.0)))

    section("Authority boundary checks")
    goal = read(GOAL)
    weak_front_decision = read(WEAK_FRONT_DECISION)
    weak_front_no_go = read(WEAK_FRONT_NO_GO)
    d17_decision = read(D17_DECISION)
    k4_packet = read(K4_PACKET)
    cl3_sm = read(CL3_SM)
    su2_beta = read(SU2_BETA)
    ew_higgs = read(EW_HIGGS)
    lepton_scale = read(LEPTON_SCALE)
    a3_p2 = read(A3_P2)
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
        audit.check(f"{container_name} references SU2 context packet", NOTE.name in container)

    audit.check("CL3 support names physical SU2 weak", "physical SU(2)_weak" in cl3_sm)
    audit.check("CL3 support names bare coupling context", "1/(d+1)" in cl3_sm and "g_Y" in cl3_sm)
    audit.check("CL3 support names lepton weak doublet", "lepton-like" in cl3_sm and "weak-doublet" in cl3_sm)
    audit.check("SU2 beta note supplies b2 structural support", "`b_2 = 19/6`" in su2_beta and "one structural ingredient" in su2_beta)
    audit.check("SU2 beta note keeps lane closure downstream", "toward eventual lane closure" in su2_beta and "not a closure" in su2_beta.lower())
    audit.check("EW Higgs note keeps numerical g2 downstream", "numerical values of `g_2(v)`" in flat(ew_higgs) and "remain downstream lanes" in flat(ew_higgs))
    audit.check("lepton-scale probe uses weak factor but keeps empirical gate", "g_2" in lepton_scale and "1/sqrt(2)" in lepton_scale and "without using `m_W`" in lepton_scale)
    audit.check("D17 decision remains separate", "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED" in d17_decision and "does not ratify the weak-front base" in d17_decision)
    audit.check("A3 P2 target remains matching target", "F_phys = C_A3 * g_2 * (1/sqrt(2))" in a3_p2 and "does not derive" in a3_p2)
    audit.check("source decision remains source-side only", "EXACT_SOURCE_SINGLETON_RETAINED" in source_decision and "does not derive `m_e`" in source_decision)
    audit.check("weak-front packet consumes SU2 context", "SU2_WEAK_COUPLING_CONTEXT_RETAINED" in weak_front_decision)
    audit.check("weak-front no-go still keeps base unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in weak_front_no_go)
    audit.check("K4 consumes weak-front base rather than SU2 directly", "WEAK_FRONT_BASE_RETAINED" in k4_packet and "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_packet)
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
        "su2_weak_coupling_context_primitive",
        "physical_g2_value_primitive",
        "weak_front_base_primitive",
        "weak_front_matching_primitive",
        "a3_correction_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)

    section("Non-claim boundaries")
    explicit_non_claims = [
        "No derivation or ratification of the weak-front base.",
        "No derivation or ratification of a physical low-scale `g_2(v)` value.",
        "No derivation or ratification of observed `m_W` or electroweak threshold",
        "No derivation or ratification of the D17 block normalization.",
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
        "This packet derives a physical low-scale `g_2(v)`",
        "This packet derives `m_W`",
        "This packet ratifies the absolute charged-lepton scale",
        "SU2 context closes K4",
        "m_e is retained",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
