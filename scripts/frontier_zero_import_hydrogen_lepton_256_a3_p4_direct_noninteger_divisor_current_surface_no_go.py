#!/usr/bin/env python3
"""Verifier for the A3 P4 direct noninteger-divisor current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply the direct theorem needed to replace exact 256 by
N_A3 = 256.082435... without comparator input. It preserves P4 as an open
route and does not derive C_A3, m_e, alpha(0), or hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PLACEMENT_DISCRIMINATOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
PRECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
ROUTE_TRIAGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
OS0_GEOMETRY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md"
M2_TENSOR = ROOT / "docs" / "M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md"
LEPTON_YUKAWA = ROOT / "docs" / "LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md"
MW_OPEN = ROOT / "docs" / "LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md"
P1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P3_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2

P4_INPUTS = {
    "P4_DIRECT_NONINTEGER_DIVISOR_TEXT_LOCK",
    "EXACT_256_SCAFFOLD_STATUS",
    "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED",
    "P4_PLACEMENT_SELECTED",
    "NO_SOURCE_FRONT_KOIDE_DOUBLE_COUNT",
    "NO_LEPTON_MASS_OR_MW_COMPARATOR_PROOF_INPUT",
    "NO_RYDBERG_OR_ALPHA_PROOF_INPUT",
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


def closes_p4(inputs: set[str]) -> bool:
    return P4_INPUTS <= inputs


def a_lepton_squared() -> float:
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        A3_PLACEMENT,
        PLACEMENT_DISCRIMINATOR,
        PRECISION,
        ROUTE_TRIAGE,
        OS0_GEOMETRY,
        M2_TENSOR,
        LEPTON_YUKAWA,
        MW_OPEN,
        P1_NO_GO,
        P2_NO_GO,
        P3_NO_GO,
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
        "A3 P4 Direct Noninteger Divisor Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not derive `C_A3`",
        "does not ratify P4 direct noninteger divisor",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
        "P4_DIRECT_NONINTEGER_DIVISOR_TEXT_LOCK",
        "EXACT_256_SCAFFOLD_STATUS",
        "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED",
        "P4_PLACEMENT_SELECTED",
        "NO_SOURCE_FRONT_KOIDE_DOUBLE_COUNT",
        "NO_LEPTON_MASS_OR_MW_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_OR_ALPHA_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "S_0 = 1/256 = 0.00390625",
        "S_P4 = 1/N_A3 = 0.003904992543192026",
        "Delta N = N_A3 - 256",
        "direct_noninteger_divisor_primitive",
        "a3_direct_divisor_primitive",
        "source_geometry_noninteger_divisor_primitive",
        "a3_correction_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad P4 no-go fails; narrowed current-surface non-supply claim passes",
        "It is not P4",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("P4 direct-divisor predicate checks")
    full_inputs = set(P4_INPUTS)
    audit.check("full P4 direct-divisor contract accepts retained handoff", closes_p4(full_inputs))
    for missing in sorted(P4_INPUTS):
        reduced = set(P4_INPUTS)
        reduced.remove(missing)
        audit.check(f"P4 direct-divisor handoff fails without {missing}", not closes_p4(reduced))
    accepted_subsets = [subset for subset in all_subsets(P4_INPUTS) if closes_p4(subset)]
    audit.check("only full P4 subset closes direct divisor", accepted_subsets == [full_inputs])
    current_surface = {
        "P4_DIRECT_NONINTEGER_DIVISOR_TEXT_LOCK",
        "EXACT_256_SCAFFOLD_STATUS",
        "P4_PLACEMENT_SELECTED",
        "NO_SOURCE_FRONT_KOIDE_DOUBLE_COUNT",
        "NO_LEPTON_MASS_OR_MW_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_OR_ALPHA_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check(
        "current surface without direct noninteger-divisor theorem does not close P4",
        not closes_p4(current_surface),
    )

    section("Target arithmetic checks")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    s0 = 1.0 / 256.0
    s_p4 = 1.0 / n_a3
    delta_n = n_a3 - 256.0
    front = 1.0 / math.sqrt(2.0)
    r0 = 1.0
    product_p4 = front * s_p4 * r0
    product_p1 = front * (c_a3 * s0) * r0
    base_product = front * s0 * r0

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 empirical divisor reproduced", abs(n_a3 - 256.08243522600384) < 1e-10)
    audit.check("C_A3 target reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("exact source singleton is 1/256", abs(s0 - 0.00390625) < 1e-18)
    audit.check("P4 singleton reproduced", abs(s_p4 - 0.003904992543192026) < 1e-18)
    audit.check("P4 divisor offset reproduced", abs(delta_n - 0.08243522600384) < 1e-10)
    audit.check("P4 direct product equals corrected exact-256 product", abs(product_p4 - product_p1) < 1e-20)
    audit.check("P4 correction ratio is C_A3", abs(product_p4 / base_product - c_a3) < 1e-15)
    audit.check("direct P4 singleton is less than exact singleton", s_p4 < s0)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    a3_placement = read(A3_PLACEMENT)
    placement = read(PLACEMENT_DISCRIMINATOR)
    placement_flat = flat(placement)
    precision = read(PRECISION)
    route_triage = read(ROUTE_TRIAGE)
    os0_geometry = read(OS0_GEOMETRY)
    m2_tensor = read(M2_TENSOR)
    lepton_yukawa = read(LEPTON_YUKAWA)
    mw_open = read(MW_OPEN)
    p1_no_go = read(P1_NO_GO)
    p2_no_go = read(P2_NO_GO)
    p3_no_go = read(P3_NO_GO)
    minimal = flat(read(MINIMAL))
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]

    audit.check("goal packet references P4 current-surface no-go", NOTE.name in goal and "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in goal)
    audit.check("K4 packet references P4 current-surface no-go", NOTE.name in k4_packet and "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in k4_packet)
    audit.check("A3 packet keeps P4 theorem open", "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in a3_placement and "P4 direct noninteger divisor" in a3_placement)
    audit.check("placement discriminator keeps P4 open", "P4 direct noninteger divisor" in placement and "OPEN. Current direct-divisor surfaces do not supply" in placement_flat)
    audit.check(
        "precision firewall names direct route",
        "direct-noninteger divisor" in precision and "derive the physical divisor `N = 256.082435...` directly" in precision,
    )
    audit.check("route triage names direct divisor route", "derive the noninteger divisor directly" in route_triage)
    audit.check("OS0 geometry keeps noninteger precision separate", "No derivation of the `256.08` precision correction." in os0_geometry)
    audit.check("M2 tensor is exact 256 only", "4^4 = 256" in m2_tensor and "does not connect `1/256` to the lepton empirical open gate" in m2_tensor)
    audit.check("Lepton Yukawa probe preserves noninteger residual", "empirical N     = m_W / a²  = 256.0824" in lepton_yukawa and "not exact" in lepton_yukawa.lower())
    audit.check("mW open gate remains empirical only", "empirical open gate" in mw_open.lower() and "does **not** prove a lepton mass theorem" in mw_open)
    audit.check("P1 no-go remains alternate route only", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in p1_no_go and "It is not P4" in note)
    audit.check("P2 no-go remains alternate route only", "CHARGED_LEPTON_FRONT_MATCHING_RETAINED" in p2_no_go and "It is not P4" in note)
    audit.check("P3 no-go remains alternate route only", "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in p3_no_go and "It is not P4" in note)
    audit.check("minimal axioms keep downstream structure outside axiom content", "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration" in minimal)
    audit.check("scale primitive excludes dimensionless correction", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector and empirical fit", "selector" in kinetic and "empirical fit" in kinetic)
    audit.check("realized primitive excludes state-contingent content", "state-contingent content" in realized and "normalization rule" in realized)

    for node_name in [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
    for absent in [
        "direct_noninteger_divisor_primitive",
        "a3_direct_divisor_primitive",
        "source_geometry_noninteger_divisor_primitive",
        "a3_correction_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)

    section("Open PR and non-claim boundaries")
    latest_pr_markers = [
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", marker in note)

    explicit_non_claims = [
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of `N_A3 = 256.082435...`.",
        "No derivation or ratification of `P4_DIRECT_NONINTEGER_DIVISOR_RETAINED`.",
        "No derivation of `DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED`.",
        "No derivation of a determinant, volume, trace, or source-geometry theorem",
        "No use of observed `m_W`, observed charged-lepton masses, observed `m_e`,",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `C_A3`",
        "This note derives `N_A3`",
        "P4 direct noninteger divisor is retained",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED is supplied",
        "direct noninteger-divisor theorem is retained",
        "This note claims hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
