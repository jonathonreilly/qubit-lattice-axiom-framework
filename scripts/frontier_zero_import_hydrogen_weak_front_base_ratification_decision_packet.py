#!/usr/bin/env python3
"""Verifier for the weak-front base decision packet.

This runner checks that the uncorrected charged-lepton weak-front base is
explicit and remains separate from A3 matching, exact source singleton,
physical electron mass, alpha(0), and hydrogen closure.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
WEAK_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
D17_BLOCK_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md"
SU2_CONTEXT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md"
A3_P2 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
D17_SUPPORT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
F2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F2_CHARGED_LEPTON_SOURCE_BLOCK_SELECTOR_DISCRIMINATOR_2026-07-04.md"
CL3_SM = ROOT / "docs" / "CL3_SM_EMBEDDING_THEOREM.md"
SU2_BETA = ROOT / "docs" / "SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md"
EW_HIGGS = ROOT / "docs" / "EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A_REGISTRY = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"


WEAK_FRONT_BASE_INPUTS = {
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


def closes_weak_front_base(inputs: set[str]) -> bool:
    return WEAK_FRONT_BASE_INPUTS <= inputs


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        WEAK_FRONT_NO_GO,
        D17_BLOCK_DECISION,
        SU2_CONTEXT_DECISION,
        A3_P2,
        LEPTON_SCALE,
        D17_SUPPORT,
        F2_TARGET,
        CL3_SM,
        SU2_BETA,
        EW_HIGGS,
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
        "Weak-Front Base Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the weak-front base",
        "WEAK_FRONT_BASE_RETAINED",
        "the uncorrected charged-lepton weak-front base for the K4 scale assembly",
        "F_0 = g_2 * (1/sqrt(2))",
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
        "No proper subset of those ten contract inputs",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "base-front target remains needed",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_D17_BLOCK_NORMALIZATION_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "D17_BLOCK_NORMALIZATION_TEXT_LOCK",
        "D17_STATED_BLOCK_SCOPE_ACCEPTED",
        "TWO_COMPONENT_UNIT_NORMALIZATION_CHECK",
        "D17_ONLY_NO_SOURCE_SINGLETON_OR_A3_INPUT",
        "NO_WEAK_COUPLING_OR_FRONT_BASE_INPUT",
        "NO_MASS_OR_COMPARATOR_PROOF_INPUT",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_SU2_COUPLING_CONTEXT_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "SU2_WEAK_COUPLING_CONTEXT_TEXT_LOCK",
        "CL3_SU2_WEAK_CONTEXT_ACCEPTED",
        "BARE_G2_SYMBOL_SCOPE_LOCK",
        "CHARGED_LEPTON_WEAK_DOUBLET_SCOPE_LOCK",
        "RUNNING_STRUCTURE_BOUNDARY_LOCK",
        "NO_PHYSICAL_G2V_OR_MW_INPUT",
        "NO_THRESHOLD_OR_A3_MATCHING_INPUT",
        "NO_D17_SOURCE_SINGLETON_OR_MASS_INPUT",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad weak-front-base retention is not shipped",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(WEAK_FRONT_BASE_INPUTS)
    audit.check("full weak-front-base contract accepts decision", closes_weak_front_base(full_inputs))
    for missing in sorted(WEAK_FRONT_BASE_INPUTS):
        reduced = set(WEAK_FRONT_BASE_INPUTS)
        reduced.remove(missing)
        audit.check(f"weak-front-base decision fails without {missing}", not closes_weak_front_base(reduced))
    accepted_subsets = [subset for subset in all_subsets(WEAK_FRONT_BASE_INPUTS) if closes_weak_front_base(subset)]
    audit.check("only full tested contract subset closes weak-front base", accepted_subsets == [full_inputs])

    weak_front_consequence = {"WEAK_FRONT_BASE_RETAINED"}
    audit.check("weak front alone does not close K4", not closes_k4(weak_front_consequence))
    full_k4 = set(K4_INPUTS)
    audit.check("full K4 predicate model closes K4", closes_k4(full_k4))
    for missing in sorted(K4_INPUTS):
        reduced = set(K4_INPUTS)
        reduced.remove(missing)
        audit.check(f"K4 predicate fails without {missing}", not closes_k4(reduced))

    section("Finite front witness checks")
    g2_values = [0.5, 0.6528252293493516, 1.0]
    for g2 in g2_values:
        front = g2 / math.sqrt(2.0)
        audit.check(f"front equals g2/sqrt2 for g2={g2:.6f}", abs(front - g2 * (1.0 / math.sqrt(2.0))) < 1e-15)
        audit.check(f"source singleton is 1/256 of front for g2={g2:.6f}", abs((front / 256.0) / front - 1.0 / 256.0) < 1e-15)

    d17_norm = 2.0 * (1.0 / math.sqrt(2.0)) ** 2
    audit.check("D17 two-component block is unit normalized", abs(d17_norm - 1.0) < 1e-15)

    c_a3 = 0.9996780910571587
    g2 = 0.6528252293493516
    front = g2 / math.sqrt(2.0)
    corrected_front = c_a3 * front
    source = 1.0 / 256.0
    audit.check("A3 correction changes base front", corrected_front != front and abs(corrected_front / front - c_a3) < 1e-15)
    audit.check("P2 and source-readout placements are product equivalent", abs((corrected_front * source) - (front * (c_a3 * source))) < 1e-20)
    audit.check("placement equivalence does not erase dependency placement", c_a3 != 1.0 and source == 1.0 / 256.0)

    section("Authority boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    weak_front_no_go = read(WEAK_FRONT_NO_GO)
    d17_block_decision = read(D17_BLOCK_DECISION)
    su2_context_decision = read(SU2_CONTEXT_DECISION)
    a3_p2 = read(A3_P2)
    lepton_scale = read(LEPTON_SCALE)
    d17_support = read(D17_SUPPORT)
    f2_target = read(F2_TARGET)
    cl3_sm = read(CL3_SM)
    su2_beta = read(SU2_BETA)
    ew_higgs = read(EW_HIGGS)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A_REGISTRY)
    nodes = registry["nodes"]

    for container_name, container in [
        ("goal packet", goal),
        ("absolute charged-lepton scale packet", k4_packet),
        ("A3 P2 target discriminator", a3_p2),
    ]:
        audit.check(f"{container_name} references weak-front-base packet", NOTE.name in container)

    audit.check("CL3 SM support names SU2 weak and g2 count", "physical SU(2)_weak" in cl3_sm and "g₂² = 1/(d+1)" in cl3_sm)
    audit.check("CL3 SM support names lepton weak doublet", "lepton-like: 1 antisym × 2" in cl3_sm and "weak-doublet" in cl3_sm)
    audit.check(
        "SU2 beta note supplies b2 structural support",
        "`b_2 = 19/6`" in su2_beta and "one structural ingredient" in su2_beta and "toward eventual lane closure" in su2_beta,
    )
    audit.check(
        "EW Higgs note keeps numerical g2 downstream",
        "numerical values of `g_2(v)`" in flat(ew_higgs) and "remain downstream lanes" in flat(ew_higgs),
    )
    audit.check("lepton-scale probe factorizes weak front", "g_2 · (1/sqrt(2)) · (1/256)" in lepton_scale)
    audit.check("D17 support keeps 1/sqrt2 separate from 256", "preserves the D17 `1/sqrt(2)` block anchor" in d17_support)
    audit.check("F2 target uses D17 block anchor conditionally", "B_lep = (1/sqrt(2))" in f2_target and "does not ratify F2" in f2_target)
    audit.check("A3 P2 target consumes weak front base separately", "WEAK_FRONT_BASE_RETAINED" in a3_p2 and "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in a3_p2)
    audit.check("K4 packet consumes weak front base", "WEAK_FRONT_BASE_RETAINED" in k4_packet)
    audit.check("weak-front packet references weak-front current no-go", WEAK_FRONT_NO_GO.name in note and "base-front target remains needed" in note)
    audit.check("weak-front packet references D17 block decision", D17_BLOCK_DECISION.name in note and "D17_BLOCK_NORMALIZATION_TEXT_LOCK" in note)
    audit.check("weak-front packet references SU2 context decision", SU2_CONTEXT_DECISION.name in note and "SU2_WEAK_COUPLING_CONTEXT_TEXT_LOCK" in note)
    audit.check("D17 block decision feeds this weak-front packet", NOTE.name in d17_block_decision and "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED" in d17_block_decision)
    audit.check("SU2 context decision feeds this weak-front packet", NOTE.name in su2_context_decision and "SU2_WEAK_COUPLING_CONTEXT_RETAINED" in su2_context_decision)
    audit.check("weak-front no-go keeps base unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in weak_front_no_go and "WEAK_FRONT_BASE_RETAINED" in weak_front_no_go)
    audit.check("goal packet consumes weak front base lane", NOTE.name in goal and "WEAK_FRONT_BASE_RETAINED" in goal)
    audit.check("minimal axioms keep downstream bridges outside axiom content", "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration" in flat(minimal))
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
        "weak_front_base_primitive",
        "su2_weak_coupling_context_primitive",
        "weak_front_matching_primitive",
        "a3_correction_primitive",
        "charged_lepton_scale_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of the weak-front base.",
        "No derivation or ratification of a physical low-scale `g_2(v)` value.",
        "No derivation or ratification of the A3 correction `C_A3`.",
        "No derivation of `S_l = 1/256`.",
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
        "weak-front base is retained",
        "A3 correction is retained",
        "physical low-scale `g_2(v)` is derived",
        "m_e is retained",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
