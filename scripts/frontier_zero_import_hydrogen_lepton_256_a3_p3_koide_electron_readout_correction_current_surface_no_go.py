#!/usr/bin/env python3
"""Verifier for the A3 P3 Koide/electron-readout correction current-surface no-go.

This runner checks that current Koide/electron surfaces do not silently supply
the P3 theorem needed to place C_A3 in the electron readout factor. It
preserves P3 as an open route and does not derive C_A3, m_e, alpha(0), or
hydrogen.
"""

from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
A3_PLACEMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PLACEMENT_DISCRIMINATOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
P1_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P2_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md"
KOIDE_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md"
PR5007 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_PR5007_IMPACT_DISCRIMINATOR_2026-07-04.md"
NATIVE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_TARGET_DISCRIMINATOR_2026-07-04.md"
NATIVE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_NATIVE_ZERO_SECTION_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SPECIES_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_SPECIES_BRIDGE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
BRANCH_MAP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_KOIDE_BRANCH_MASS_MAP_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ELECTRON_MASS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
TIER_A = ROOT / "docs" / "audit" / "data" / "tier_a_admissions.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2

P3_INPUTS = {
    "P3_KOIDE_ELECTRON_READOUT_TEXT_LOCK",
    "KOIDE_ELECTRON_READOUT_CONTEXT_RETAINED",
    "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED",
    "P3_PLACEMENT_SELECTED",
    "NO_SOURCE_OR_FRONT_DOUBLE_COUNT",
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


def closes_p3(inputs: set[str]) -> bool:
    return P3_INPUTS <= inputs


def a_lepton_squared() -> float:
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def rho(delta: float, branch: int = 0) -> float:
    return (1.0 + math.sqrt(2.0) * math.cos(delta + 2.0 * math.pi * branch / 3.0)) ** 2


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        A3_PLACEMENT,
        PLACEMENT_DISCRIMINATOR,
        P1_NO_GO,
        P2_NO_GO,
        KOIDE_FIREWALL,
        PR5007,
        NATIVE_TARGET,
        NATIVE_DECISION,
        SPECIES_DECISION,
        BRANCH_MAP,
        ELECTRON_MASS,
        REGISTRY,
        TIER_A,
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
        "A3 P3 Koide/Electron-Readout Correction Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "does not derive `C_A3`",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
        "P3_KOIDE_ELECTRON_READOUT_TEXT_LOCK",
        "KOIDE_ELECTRON_READOUT_CONTEXT_RETAINED",
        "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED",
        "P3_PLACEMENT_SELECTED",
        "NO_SOURCE_OR_FRONT_DOUBLE_COUNT",
        "NO_LEPTON_MASS_OR_MW_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_OR_ALPHA_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "S_0 = 1/256 = 0.00390625",
        "R_P3 = C_A3 * R_0",
        "koide_electron_a3_correction_primitive",
        "koide_readout_correction_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad P3 no-go fails; narrowed current-surface non-supply claim passes",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("P3 correction predicate checks")
    full_inputs = set(P3_INPUTS)
    audit.check("full P3 correction contract accepts readout correction", closes_p3(full_inputs))
    for missing in sorted(P3_INPUTS):
        reduced = set(P3_INPUTS)
        reduced.remove(missing)
        audit.check(f"P3 correction fails without {missing}", not closes_p3(reduced))
    accepted_subsets = [subset for subset in all_subsets(P3_INPUTS) if closes_p3(subset)]
    audit.check("only full P3 subset closes readout correction", accepted_subsets == [full_inputs])
    current_surface = {
        "KOIDE_ELECTRON_READOUT_CONTEXT_RETAINED",
        "P3_PLACEMENT_SELECTED",
        "NO_SOURCE_OR_FRONT_DOUBLE_COUNT",
        "NO_LEPTON_MASS_OR_MW_COMPARATOR_PROOF_INPUT",
        "NO_RYDBERG_OR_ALPHA_PROOF_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
    }
    audit.check("current surface without Koide/electron A3 theorem does not close P3", not closes_p3(current_surface))

    section("Target arithmetic checks")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    front = 1.0 / math.sqrt(2.0)
    s0 = 1.0 / 256.0
    r0 = 1.0
    product_p3 = front * s0 * (c_a3 * r0)
    product_p1 = front * (c_a3 * s0) * r0
    base_product = front * s0 * r0
    rho_delta = rho(2.0 / 9.0, branch=1)
    rho_zero = rho(0.0, branch=1)

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 empirical divisor reproduced", abs(n_a3 - 256.08243522600384) < 1e-10)
    audit.check("C_A3 target reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("exact source singleton is 1/256", abs(s0 - 0.00390625) < 1e-18)
    audit.check("P3 readout placement equals P1 product after common correction", abs(product_p3 - product_p1) < 1e-20)
    audit.check("P3 correction ratio is C_A3", abs(product_p3 / base_product - c_a3) < 1e-15)
    audit.check("Koide phase-blind comparator residue remains large", rho_zero / rho_delta > 50.0)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    a3_placement = read(A3_PLACEMENT)
    placement = read(PLACEMENT_DISCRIMINATOR)
    placement_flat = flat(placement)
    p1_no_go = read(P1_NO_GO)
    p2_no_go = read(P2_NO_GO)
    koide_firewall = read(KOIDE_FIREWALL)
    pr5007 = read(PR5007)
    native_target = read(NATIVE_TARGET)
    native_decision = read(NATIVE_DECISION)
    species_decision = read(SPECIES_DECISION)
    branch_map = read(BRANCH_MAP)
    electron_mass = read(ELECTRON_MASS)
    minimal = flat(read(MINIMAL))
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    tier_a = read(TIER_A)
    nodes = registry["nodes"]

    audit.check("goal packet references P3 current-surface no-go", NOTE.name in goal and "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in goal)
    audit.check("K4 packet references P3 current-surface no-go", NOTE.name in k4_packet and "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED" in k4_packet)
    audit.check("A3 packet keeps P3 theorem open", "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED" in a3_placement and "P3 Koide/electron readout" in a3_placement)
    audit.check("placement discriminator keeps P3 open", "P3 Koide/electron-readout correction" in placement and "OPEN. Current Koide/electron surfaces do not supply" in placement_flat)
    audit.check("P1 no-go remains alternate route only", "P1_SOURCE_READOUT_CORRECTION_RETAINED" in p1_no_go and "It is not P3" in note)
    audit.check("P2 no-go remains alternate route only", "P2_WEAK_FRONT_MATCHING_RETAINED" in p2_no_go and "It is not P3" in note)
    audit.check("Koide firewall keeps K4 and m_e separate", "A3 precision placement" in koide_firewall and "No derivation of `m_e`." in koide_firewall)
    audit.check("PR5007 impact does not close A3 placement", "A3 precision route" in pr5007 and "cannot be inferred from `#5007`" in pr5007)
    audit.check("native bridge target is not electron readout", "prevents Z1-Z3 from closing `m_e`" in native_target)
    audit.check("native bridge decision keeps K4 downstream", "source-probe F/L/P/R and A3 decisions" in native_decision and "K4 scale side after bridge" in native_decision)
    audit.check("species decision keeps K4 scale-side separate", "source-probe F/L/P/R and A3 decisions" in species_decision and "K4 scale side, not K3" in species_decision)
    audit.check("branch mass map excludes fitted A3 precision", "fitted A3 precision" in branch_map and "excluded as proof inputs" in branch_map)
    audit.check("electron mass packet is downstream consumer", "m_e = a_l^2 * rho_e(delta)" in electron_mass and "does not derive" in electron_mass)
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
        "koide_electron_a3_correction_primitive",
        "koide_readout_correction_primitive",
        "a3_correction_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered primitive shortcut: {absent}", absent not in nodes)
    audit.check("AC_phi_lambda remains Tier-A, not primitive", "AC_phi_lambda" in tier_a and "AC_phi_lambda" not in nodes)

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
        "No derivation or ratification of `P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED`.",
        "No derivation of `KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED`.",
        "No derivation of native zero-section bridge, physical electron species",
        "No use of observed `m_W`, observed charged-lepton masses, observed `m_e`,",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `C_A3`",
        "P3 Koide/electron-readout correction is retained",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED is supplied",
        "Koide/electron readout correction is retained",
        "This note claims hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
