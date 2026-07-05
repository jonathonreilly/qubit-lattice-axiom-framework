#!/usr/bin/env python3
"""Verifier for the exact source singleton decision packet.

This runner checks that the K4 source-side EXACT_SOURCE_SINGLETON_RETAINED
handoff is explicit, finite, and separate from F/L/P/R ratification status,
A3 placement, K4 scale assembly, physical electron mass, alpha(0), and
hydrogen.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_RATIFICATION_DECISION_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
EXACT_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SOURCE_PACKET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
A3_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_PRECISION_PLACEMENT_RATIFICATION_DECISION_PACKET_2026-07-04.md"
PHYSICAL_ELECTRON = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_PHYSICAL_ELECTRON_MASS_RATIFICATION_DECISION_PACKET_2026-07-04.md"
ALPHA_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ALPHA_QED_LOOP_KERNEL_TARGET_DISCRIMINATOR_2026-07-04.md"
STATIC_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_STATIC_SOURCE_RYDBERG_CLOSURE_DISCRIMINATOR_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

Coord = tuple[int, int, int, int]


EXACT_SOURCE_INPUTS = {
    "EXACT_SOURCE_SINGLETON_TEXT_LOCK",
    "SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED",
    "FULL_CELL_SOURCE_CARRIER_CHECK",
    "PROJECTIVE_UNIFORM_RAY_CHECK",
    "S_L_READOUT_IDENTITY_BOUND",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_A3_OR_K4_OR_MASS_INPUT",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
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


def closes_exact_source(inputs: set[str]) -> bool:
    return EXACT_SOURCE_INPUTS <= inputs


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
        EXACT_SOURCE_NO_GO,
        SOURCE_PACKET,
        SOURCE_TARGET,
        COMPRESSION,
        F_DECISION,
        L_DECISION,
        P_DECISION,
        R_DECISION,
        F_NO_GO,
        L_NO_GO,
        P_NO_GO,
        R_NO_GO,
        A3_DECISION,
        PHYSICAL_ELECTRON,
        ALPHA_TARGET,
        STATIC_TARGET,
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
        "Exact Source Singleton Ratification Decision Packet",
        "decision packet / import-retirement handoff",
        "does not ratify the exact source singleton",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "the exact charged-lepton source-side singleton S_l = 1/256 as the K4 source",
        "EXACT_SOURCE_SINGLETON_TEXT_LOCK",
        "SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED",
        "FULL_CELL_SOURCE_CARRIER_CHECK",
        "PROJECTIVE_UNIFORM_RAY_CHECK",
        "S_L_READOUT_IDENTITY_BOUND",
        "CHARGED_LEPTON_SCOPE_LOCK",
        "NO_A3_OR_K4_OR_MASS_INPUT",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of those eleven contract inputs",
        "S_l = 1/256",
        "WEAK_FRONT_BASE_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED",
        "PHYSICAL_ELECTRON_READOUT_RETAINED",
        "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
        "STATIC_SOURCE_RYDBERG_RETAINED",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "sigma([1])_c = 1/256",
        "no charged-lepton source singleton",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "exact_source_singleton_primitive",
        "source_probe_interface_primitive",
        "f_l_p_r_interface_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
        "What This Moves",
        "No-Go Discipline Gate",
        "decision-ready ratification",
        "broad exact-source retention is not shipped",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Decision predicate checks")
    full_inputs = set(EXACT_SOURCE_INPUTS)
    audit.check("full exact-source contract accepts decision", closes_exact_source(full_inputs))
    for missing in sorted(EXACT_SOURCE_INPUTS):
        reduced = set(EXACT_SOURCE_INPUTS)
        reduced.remove(missing)
        audit.check(f"exact-source decision fails without {missing}", not closes_exact_source(reduced))
    accepted_subsets = [subset for subset in all_subsets(EXACT_SOURCE_INPUTS) if closes_exact_source(subset)]
    audit.check("only full tested exact-source subset closes decision", accepted_subsets == [full_inputs])
    audit.check("exact source alone does not close K4", not closes_k4({"EXACT_SOURCE_SINGLETON_RETAINED"}))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))

    section("Finite source witness checks")
    coords = coordinates()
    audit.check("full-cell coordinate set has 256 elements", len(coords) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    sigma = normalize(uniform)
    audit.check("uniform singleton is exact 1/256", sigma[coords[0]] == Fraction(1, 256))
    audit.check("uniform source weights sum to one", sum(sigma.values(), Fraction(0)) == Fraction(1))
    no_full_cell = list(product(range(4), repeat=2))
    audit.check("reduced no-carrier witness gives 1/16", Fraction(1, len(no_full_cell)) == Fraction(1, 16))
    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in coords}
    tagged_sigma = normalize(tagged)
    audit.check("coordinate-tagged no-L witness gives 1/112", tagged_sigma[(0, 0, 0, 0)] == Fraction(1, 112))
    audit.check("tagged witness differs from exact singleton", tagged_sigma[(0, 0, 0, 0)] != Fraction(1, 256))
    h = Fraction(3, 2)
    j_c = Fraction(5, 7)
    lam = Fraction(11, 5)
    audit.check("raw source control rescales in no-P witness", lam * j_c != j_c)
    audit.check("front-bearing product stays invariant in no-P witness", (h / lam) * (lam * j_c) == h * j_c)

    section("Authority boundary checks")
    goal = read(GOAL)
    k4_packet = read(K4_PACKET)
    exact_no_go = read(EXACT_SOURCE_NO_GO)
    source_packet = read(SOURCE_PACKET)
    source_target = read(SOURCE_TARGET)
    compression = read(COMPRESSION)
    f_decision = read(F_DECISION)
    l_decision = read(L_DECISION)
    p_decision = read(P_DECISION)
    r_decision = read(R_DECISION)
    f_no_go = read(F_NO_GO)
    l_no_go = read(L_NO_GO)
    p_no_go = read(P_NO_GO)
    r_no_go = read(R_NO_GO)
    a3_decision = read(A3_DECISION)
    physical_electron = read(PHYSICAL_ELECTRON)
    alpha_target = read(ALPHA_TARGET)
    static_target = read(STATIC_TARGET)
    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    registry = json.loads(read(REGISTRY))
    registry_text = read(REGISTRY)
    nodes = registry["nodes"]

    audit.check("goal packet references exact-source decision", NOTE.name in goal and "EXACT_SOURCE_SINGLETON_RETAINED" in goal)
    audit.check("K4 packet references exact-source decision", NOTE.name in k4_packet and "EXACT_SOURCE_SINGLETON_RETAINED" in k4_packet)
    audit.check("exact-source no-go references exact-source decision", NOTE.name in exact_no_go and "positive handoff" in exact_no_go)
    audit.check("source packet remains source-probe handoff", "the normalized label-free charged-lepton full-cell source-probe interface" in source_packet)
    audit.check("source packet does not ratify F/L/P/R", "does not ratify F/L/P/R" in source_packet)
    audit.check("source target names full F/L/P/R interface", "full F/L/P/R interface" in source_target)
    audit.check("compression supplies conditional exact S_l", "S_l = 1/256" in compression and "does not ratify" in compression)
    audit.check("F decision remains below source singleton", "F_CLAUSE_RETAINED" in f_decision and "does not ratify F" in f_decision)
    audit.check("L decision remains below source singleton", "L_CLAUSE_RETAINED" in l_decision and "does not ratify L" in l_decision)
    audit.check("P decision remains below source singleton", "P_CLAUSE_RETAINED" in p_decision and "does not ratify P" in p_decision)
    audit.check("R decision remains below source singleton", "R_CLAUSE_RETAINED" in r_decision and "does not ratify R" in r_decision)
    audit.check("F no-go keeps F unsupplied", "F_CLAUSE_RETAINED" in f_no_go and "current retained, primitive, and open-PR surfaces do not supply" in f_no_go)
    audit.check("L no-go keeps L unsupplied", "L_CLAUSE_RETAINED" in l_no_go and "current retained, primitive, and open-PR surfaces do not supply" in l_no_go)
    audit.check("P no-go keeps P unsupplied", "P_CLAUSE_RETAINED" in p_no_go and "current retained, primitive, and open-PR surfaces do not supply" in p_no_go)
    audit.check("R no-go keeps R unsupplied", "R_CLAUSE_RETAINED" in r_no_go and "current retained, primitive, and open-PR surfaces do not supply" in r_no_go)
    audit.check("A3 decision remains downstream", "A3_PRECISION_PLACEMENT_RETAINED" in a3_decision and "does not by itself derive `C_A3`" in a3_decision)
    audit.check("physical electron remains downstream", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron)
    audit.check("alpha target remains downstream", "No derivation of `alpha(0)`" in alpha_target)
    audit.check("static target remains downstream", "STATIC_SOURCE_RYDBERG" in static_target or "static-source Rydberg" in static_target)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal and "remain outside axiom content" in minimal)
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)

    for node_name, path in [
        ("minimal_axioms", "docs/MINIMAL_AXIOMS_2026-06-29.md"),
        ("scale_reference_primitive", "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"),
        ("kinetic_isotropy_primitive", "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"),
        ("realized_state_primitive", "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"),
    ]:
        audit.check(f"registry node present: {node_name}", node_name in nodes)
        audit.check(f"registry current_path for {node_name}", nodes[node_name]["current_path"] == path)
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
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open",
        "`#4991` owner-governed Tier-A retirement | open",
    ]
    for marker in latest_pr_markers:
        audit.check(f"latest PR marker present: {marker}", flat(marker) in note_flat)

    explicit_non_claims = [
        "No derivation or ratification of `EXACT_SOURCE_SINGLETON_RETAINED`.",
        "No derivation that `S_l = 1/256` is retained.",
        "No derivation or ratification of F/L/P/R.",
        "No derivation or ratification of `F_CLAUSE_RETAINED`,",
        "No derivation or ratification of A3 precision placement, `C_A3`, or",
        "No derivation or ratification of K4 scale assembly.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg, or hydrogen.",
        "No use of observed `m_W`, observed charged-lepton masses, fitted `a_l`,",
        "No audit status change for any cited row.",
        "No new axiom, primitive, Tier-A admission, or empirical import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the exact source singleton",
        "exact source singleton is retained",
        "EXACT_SOURCE_SINGLETON_RETAINED is supplied",
        "F/L/P/R is retained",
        "A3 precision placement is retained",
        "K4 scale assembly is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
