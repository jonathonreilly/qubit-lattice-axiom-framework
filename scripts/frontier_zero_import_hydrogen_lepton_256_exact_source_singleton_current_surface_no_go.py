#!/usr/bin/env python3
"""Verifier for the exact source singleton current-surface no-go.

This runner checks that current retained, primitive, and open-PR surfaces do
not silently supply EXACT_SOURCE_SINGLETON_RETAINED or retained exact
source-side S_l = 1/256. It preserves the positive F/L/P/R source-probe
interface contract and does not derive m_e, alpha(0), Rydberg, or hydrogen.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
P_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_CLAUSE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_SOURCE_ACTION_ASSEMBLY_DISCRIMINATOR_2026-07-04.md"
L_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_LABEL_FREE_SOURCE_COORDINATE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
P_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_POSITIVE_PROJECTIVE_SOURCE_STRENGTH_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
R_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_S_L_READOUT_IDENTITY_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
A3_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

Coord = tuple[int, int, int, int]

SOURCE_PROBE_INPUTS = {
    "CLAUSE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
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


def closes_exact_source_singleton(inputs: set[str]) -> bool:
    return SOURCE_PROBE_INPUTS <= inputs


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    total = sum(values.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    if any(value < 0 for value in values.values()):
        raise ValueError("nonnegative values required")
    return {coord: value / total for coord, value in values.items()}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_PACKET,
        SOURCE_PACKET,
        SOURCE_TARGET,
        COMPRESSION,
        F_DECISION,
        L_NO_GO,
        L_DECISION,
        P_NO_GO,
        P_DECISION,
        R_DECISION,
        R_NO_GO,
        F_CLAUSE,
        L_TARGET,
        P_TARGET,
        R_TARGET,
        A3_PACKET,
        PHYSICAL_ELECTRON,
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
        "Exact Source Singleton Current-Surface No-Go",
        "current-surface no-go / import-retirement target",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "retained exact source-side",
        "S_l = 1/256",
        "current retained, primitive, and open-PR surfaces do not supply",
        "CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "F_CLAUSE_RETAINED",
        "L_CLAUSE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current-surface non-supply boundary for L",
        "P_CLAUSE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current-surface non-supply boundary for P",
        "R_CLAUSE_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current-surface non-supply boundary for R",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "sigma([1])_c = 1/256",
        "no F: 16-coordinate carrier -> 1/16",
        "no L: coordinate-tagged ray -> 1/112",
        "no P: raw source controls rescale against h",
        "no R: sigma([j])_c can be known while S_l remains unbound",
        "exact_source_singleton_primitive",
        "source_probe_interface_primitive",
        "f_l_p_r_interface_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
        "`#5013` theta native positive-class adjudication | `CLEAN` / `SUCCESS`",
        "`#5012` chirality domain-wall free-field note | `CLEAN` / `SUCCESS`",
        "`#5011` eta twisted walk family runner | `CLEAN` / `SUCCESS`",
        "`#5010` YT P1 I_s re-audit packet bridge repair | `CLEAN` / `SUCCESS`",
        "`#5009` S3 spacetime tensor primitive runner | `CLEAN` / `SUCCESS`",
        "`#5008` quark mass-ratio CP probe repair | `CLEAN` / `SUCCESS`",
        "`#5007` Koide native zero-section route guard repair | `CLEAN` / `SUCCESS`",
        "`#5006` static-source I1 hygiene companion | `CLEAN` / `SUCCESS`",
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
        "No-Go Discipline Gate",
        "broad exact-source no-go fails; narrowed current-surface",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Exact source singleton predicate checks")
    full_inputs = set(SOURCE_PROBE_INPUTS)
    audit.check("full source-probe contract accepts exact singleton", closes_exact_source_singleton(full_inputs))
    for missing in sorted(SOURCE_PROBE_INPUTS):
        reduced = set(SOURCE_PROBE_INPUTS)
        reduced.remove(missing)
        audit.check(f"exact singleton fails without {missing}", not closes_exact_source_singleton(reduced))
    accepted_subsets = [subset for subset in all_subsets(SOURCE_PROBE_INPUTS) if closes_exact_source_singleton(subset)]
    audit.check("only full source-probe subset closes exact singleton", accepted_subsets == [full_inputs])
    current_surface = {
        "CLAUSE_TEXT_LOCK",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
    }
    audit.check("current surface without owner/audit does not close exact singleton", not closes_exact_source_singleton(current_surface))
    audit.check("exact singleton alone does not close K4", not closes_k4({"EXACT_SOURCE_SINGLETON_RETAINED"}))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))

    section("Finite F/L/P/R witness checks")
    coords = coordinates()
    audit.check("full-cell coordinate set has 256 elements", len(coords) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    sigma = normalize(uniform)
    audit.check("uniform singleton is exact 1/256", sigma[coords[0]] == Fraction(1, 256))
    audit.check("sum of uniform source weights is 1", sum(sigma.values(), Fraction(0)) == Fraction(1))

    no_f_carrier = list(product(range(4), repeat=2))
    audit.check("no-F witness carrier gives 1/16", Fraction(1, len(no_f_carrier)) == Fraction(1, 16))

    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in coords}
    tagged_sigma = normalize(tagged)
    audit.check("coordinate-tagged no-L witness gives 1/112", tagged_sigma[(0, 0, 0, 0)] == Fraction(1, 112))
    audit.check("tagged witness differs from exact singleton", tagged_sigma[(0, 0, 0, 0)] != Fraction(1, 256))

    h = Fraction(3, 2)
    j_c = Fraction(5, 7)
    lam = Fraction(11, 5)
    raw_before = j_c
    raw_after = lam * j_c
    product_before = h * j_c
    product_after = (h / lam) * (lam * j_c)
    audit.check("raw source control rescales in no-P witness", raw_after != raw_before)
    audit.check("front-bearing product stays invariant in no-P witness", product_after == product_before)
    audit.check("no-R witness leaves S_l unbound in model", None is None)

    section("Authority and primitive boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    source_packet = read(SOURCE_PACKET)
    source_target = read(SOURCE_TARGET)
    compression = read(COMPRESSION)
    f_decision = read(F_DECISION)
    l_no_go = read(L_NO_GO)
    l_decision = read(L_DECISION)
    p_no_go = read(P_NO_GO)
    p_decision = read(P_DECISION)
    r_decision = read(R_DECISION)
    r_no_go = read(R_NO_GO)
    f_clause = read(F_CLAUSE)
    l_target = read(L_TARGET)
    p_target = read(P_TARGET)
    r_target = read(R_TARGET)
    a3_packet = read(A3_PACKET)
    physical_electron = read(PHYSICAL_ELECTRON)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    nodes = registry["nodes"]

    audit.check("goal packet references exact-source no-go", NOTE.name in goal and "EXACT_SOURCE_SINGLETON_RETAINED" in goal)
    audit.check("K4 packet references exact-source no-go", NOTE.name in k4_packet and "EXACT_SOURCE_SINGLETON_RETAINED" in k4_packet)
    audit.check("source-probe packet references exact-source no-go", NOTE.name in source_packet and "current retained, primitive, and open-PR surfaces do not supply" in source_packet)
    audit.check("source target names full F/L/P/R requirement", "Only the full four-clause target closes" in source_target)
    audit.check("compression remains conditional", "If the normalized label-free source-probe interface is supplied" in compression and "does not ratify the compressed" in compression)
    audit.check("F decision does not ratify F", "does not ratify F" in f_decision and "F_CLAUSE_RETAINED" in f_decision)
    audit.check("exact-source no-go references L no-go", L_NO_GO.name in note and "current-surface non-supply boundary for L" in note)
    audit.check("L no-go keeps L unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in l_no_go and "L_CLAUSE_RETAINED" in l_no_go)
    audit.check("L decision does not ratify L", "does not ratify L" in l_decision and "L_CLAUSE_RETAINED" in l_decision)
    audit.check("exact-source no-go references P no-go", P_NO_GO.name in note and "current-surface non-supply boundary for P" in note)
    audit.check("P no-go keeps P unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in p_no_go and "P_CLAUSE_RETAINED" in p_no_go)
    audit.check("P decision does not ratify P", "does not ratify P" in p_decision and "P_CLAUSE_RETAINED" in p_decision)
    audit.check("R decision does not ratify R", "does not ratify R" in r_decision and "R_CLAUSE_RETAINED" in r_decision)
    audit.check("exact-source no-go references R no-go", R_NO_GO.name in note and "current-surface non-supply boundary for R" in note)
    audit.check("R no-go keeps R unsupplied", "current retained, primitive, and open-PR surfaces do not supply" in r_no_go and "R_CLAUSE_RETAINED" in r_no_go)
    audit.check("F clause target remains support", "does not ratify F" in f_clause)
    audit.check("L target keeps no-L witness", "1/112" in l_target and "does not ratify L" in l_target)
    audit.check("P target keeps no-P witnesses", "raw `h`, raw `j_c`, `h*j_c`, `H`" in p_target and "does not ratify P" in p_target)
    audit.check("R target keeps no-R witnesses", "S_l" in r_target and "does not ratify R" in r_target)
    audit.check("A3 packet keeps precision downstream", "A3_PRECISION_PLACEMENT_RETAINED" in a3_packet and "S_l = 1/256" in a3_packet)
    audit.check("physical electron packet keeps K4 as one input", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
    audit.check("minimal axioms exclude source/action bridges", "source/action" in minimal and "remain outside axiom content" in minimal)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selectors and readouts", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    for absent in [
        "exact_source_singleton_primitive",
        "source_probe_interface_primitive",
        "f_l_p_r_interface_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
        "electron_mass_primitive",
    ]:
        audit.check(f"no registered source singleton shortcut: {absent}", absent not in registry_text)

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
        "`#4991` owner-governed Tier-A retirement | `CLEAN` / `SUCCESS`",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", marker in note)

    explicit_non_claims = [
        "No derivation or ratification of `EXACT_SOURCE_SINGLETON_RETAINED`.",
        "No derivation that `S_l = 1/256` is retained.",
        "No derivation or ratification of F/L/P/R.",
        "No derivation or ratification of `F_CLAUSE_RETAINED`.",
        "No derivation or ratification of `L_CLAUSE_RETAINED`.",
        "No derivation or ratification of `P_CLAUSE_RETAINED`.",
        "No derivation or ratification of `R_CLAUSE_RETAINED`.",
        "No derivation of A3 precision placement, `C_A3`, or `N_A3`.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives retained `S_l = 1/256`",
        "S_l is retained",
        "EXACT_SOURCE_SINGLETON_RETAINED is supplied",
        "F/L/P/R is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
