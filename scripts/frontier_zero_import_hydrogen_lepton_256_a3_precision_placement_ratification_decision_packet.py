#!/usr/bin/env python3
"""Verifier for the A3 precision-placement ratification decision packet.

This runner checks that A3 is packaged as a one-placement/no-double-count
decision surface. It does not ratify A3, derive C_A3, m_e, alpha(0), or
hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
SOURCE_PROBE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PRECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
A3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P1_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
P2_FRONT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P3_KOIDE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P4_DIRECT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KOIDE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
ALPHA = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2
G_F = 1.1663787e-5

A3_DECISION_INPUTS = {
    "A3_PLACEMENT_TEXT_LOCK",
    "EXACT_SOURCE_SCAFFOLD_STATUS",
    "ONE_PLACEMENT_SELECTED",
    "PLACEMENT_THEOREM_RETAINED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

PLACEMENT_THEOREMS = {
    "P1_SOURCE_READOUT_CORRECTION_RETAINED",
    "P2_WEAK_FRONT_MATCHING_RETAINED",
    "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
    "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
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


def accepts_a3_decision(inputs: set[str], placements: set[str]) -> bool:
    return A3_DECISION_INPUTS <= inputs and len(PLACEMENT_THEOREMS & placements) == 1


def a_lepton_squared() -> float:
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def weak_front_factor() -> float:
    v_mev = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5 * 1000.0
    g2 = 2.0 * M_W / v_mev
    return g2 / math.sqrt(2.0)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        SOURCE_PROBE_DECISION,
        PRECISION,
        PLACEMENT,
        A3_NO_GO,
        P1_SOURCE_NO_GO,
        P2_TARGET,
        P2_FRONT_NO_GO,
        P3_KOIDE_NO_GO,
        P4_DIRECT_NO_GO,
        KOIDE,
        ALPHA,
        MINIMAL,
        REGISTRY,
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
        "A3 Precision-Placement Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify A3",
        "the charged-lepton A3 precision-placement decision",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED",
        "P2_WEAK_FRONT_MATCHING_RETAINED",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current surfaces do not supply `P1_SOURCE_READOUT_CORRECTION_RETAINED`",
        "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current surfaces do not supply `P2_WEAK_FRONT_MATCHING_RETAINED`",
        "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current surfaces do not supply `P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED`",
        "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current surfaces do not supply `P4_DIRECT_NONINTEGER_DIVISOR_RETAINED`",
        "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED",
        "empirical-splice class P5 is not an admissible zero-import decision route",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "A3 placement target remains needed",
        "A3_PLACEMENT_TEXT_LOCK",
        "EXACT_SOURCE_SCAFFOLD_STATUS",
        "ONE_PLACEMENT_SELECTED",
        "PLACEMENT_THEOREM_RETAINED",
        "NO_SOURCE_DOUBLE_COUNT",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those nine contract inputs is a retained A3 placement decision",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "F_0 * (C * S_0) * R_0",
        "(C * F_0) * S_0 * R_0",
        "F_0 * S_0 * (C * R_0)",
        "F_0 * (1/N_A3) * R_0",
        "#5011",
        "#5010",
        "#5009",
        "#5008",
        "#5007",
        "#5006",
        "audit_pipeline",
        "SUCCESS",
        "Merge-state labels are moving review metadata",
        "The primitive registry was checked",
        "No-Go Discipline Gate",
        "decision-ready ratification contract",
        "broad A3-retention claim fails; narrowed precision-placement",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(A3_DECISION_INPUTS)
    audit.check(
        "full contract plus one placement accepts A3 decision",
        accepts_a3_decision(full_inputs, {"P2_WEAK_FRONT_MATCHING_RETAINED"}),
    )
    for missing in sorted(A3_DECISION_INPUTS):
        reduced = set(A3_DECISION_INPUTS)
        reduced.remove(missing)
        audit.check(
            f"A3 decision fails without contract input {missing}",
            not accepts_a3_decision(reduced, {"P2_WEAK_FRONT_MATCHING_RETAINED"}),
        )
    audit.check("A3 decision fails with no placement theorem", not accepts_a3_decision(full_inputs, set()))
    for placement in sorted(PLACEMENT_THEOREMS):
        audit.check(f"single placement accepts: {placement}", accepts_a3_decision(full_inputs, {placement}))
    for subset in all_subsets(PLACEMENT_THEOREMS):
        if len(subset) != 1:
            audit.check(f"non-singleton placement set rejected: {sorted(subset)}", not accepts_a3_decision(full_inputs, subset))

    section("Finite product-degeneracy witness")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    s0 = 1.0 / 256.0
    front = weak_front_factor()
    r0 = 1.0
    product_p1 = front * (c_a3 * s0) * r0
    product_p2 = (c_a3 * front) * s0 * r0
    product_p3 = front * s0 * (c_a3 * r0)
    product_p4 = front * (1.0 / n_a3) * r0
    base_product = front * s0 * r0
    double_count = (c_a3 * front) * (c_a3 * s0) * r0

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 empirical divisor reproduced", abs(n_a3 - 256.08243522600384) < 1e-10)
    audit.check("A3 correction reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("exact source scaffold is 1/256", abs(s0 - 0.00390625) < 1e-18)
    audit.check("P1 product equals P2 product", abs(product_p1 - product_p2) < 1e-20)
    audit.check("P1 product equals P3 product", abs(product_p1 - product_p3) < 1e-20)
    audit.check("P1 product equals P4 product", abs(product_p1 - product_p4) < 1e-20)
    audit.check("placement product is C_A3 times base", abs(product_p1 / base_product - c_a3) < 1e-15)
    audit.check("double-counted correction is distinguishable", abs(double_count - product_p1) > 1e-7)
    audit.check("double-counted correction is C_A3 squared times base", abs(double_count / base_product - c_a3 * c_a3) < 1e-15)

    section("Authority boundary checks")
    goal = read(GOAL)
    route = read(ROUTE)
    source_probe = read(SOURCE_PROBE_DECISION)
    precision = read(PRECISION)
    placement = read(PLACEMENT)
    a3_no_go = read(A3_NO_GO)
    p1_source_no_go = read(P1_SOURCE_NO_GO)
    p2_target = read(P2_TARGET)
    p3_koide_no_go = read(P3_KOIDE_NO_GO)
    p4_direct_no_go = read(P4_DIRECT_NO_GO)
    koide = read(KOIDE)
    alpha = read(ALPHA)
    minimal = read(MINIMAL)
    registry = json.loads(read(REGISTRY))
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    nodes = registry["nodes"]

    audit.check("goal packet references A3 decision packet", NOTE.name in goal)
    audit.check("route triage references A3 decision packet", NOTE.name in route)
    audit.check(
        "source-probe decision remains exact source scaffold only",
        "S_l = 1/256" in source_probe and "does not place the `256.082435...` precision" in source_probe,
    )
    audit.check("precision firewall does not derive C_A3", "No derivation of `C_A3 = 0.999678091...`" in precision)
    audit.check("A3 placement discriminator lists source/front/Koide/direct placements", all(p in placement for p in ["P1 source-readout correction", "P2 front-factor/threshold correction", "P3 Koide/electron-readout correction", "P4 direct noninteger divisor"]))
    audit.check("A3 decision references A3 current-surface no-go", A3_NO_GO.name in note and "A3 placement target remains needed" in note)
    audit.check("A3 current-surface no-go keeps A3 placement unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in a3_no_go and "A3_PRECISION_PLACEMENT_RETAINED" in a3_no_go)
    audit.check("P1 current-surface no-go keeps source correction open", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in p1_source_no_go and "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED" in p1_source_no_go)
    audit.check("P2 target names weak-front theorem", "F_phys = C_A3 * g_2 * (1/sqrt(2))" in p2_target and "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_target)
    audit.check("P3 current-surface no-go keeps Koide readout correction open", "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in p3_koide_no_go and "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED" in p3_koide_no_go)
    audit.check("P4 current-surface no-go keeps direct divisor open", "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in p4_direct_no_go and "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in p4_direct_no_go)
    audit.check("Koide firewall leaves electron readout open", "No derivation of `m_e`" in koide and "physical electron species bridge" in koide)
    audit.check("alpha target remains downstream", "No derivation of `alpha(0)`" in alpha and "R-Lep" in alpha)
    audit.check("minimal axioms exclude physical-observable identification", "physical-observable identification" in minimal)
    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("no A3 correction primitive registered", "a3_correction_primitive" not in nodes and "a3_precision_placement_primitive" not in nodes)
    audit.check("scale primitive excludes dimensionless corrections", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes values and normalization", "normalization rule" in realized and "or value is supplied" in realized)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5011` eta twisted walk family runner | `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of A3.",
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of `N_A3 = 256.082435...`.",
        "No derivation of corrected `S_l = 1/N_A3`.",
        "No derivation of a charged-lepton weak-front threshold correction.",
        "No derivation of a Koide/electron readout correction.",
        "No derivation of a direct noninteger-divisor theorem.",
        "No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`, or",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies A3",
        "A3 is retained",
        "C_A3 is retained",
        "N_A3 is retained",
        "corrected S_l is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
