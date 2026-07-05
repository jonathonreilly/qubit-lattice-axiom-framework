#!/usr/bin/env python3
"""Verifier for the exact source singleton assembly ladder review packet.

This runner checks that the source-side F/L/P/R -> source-probe -> exact
singleton -> K4-consumer ladder is review-compressed without ratifying the
source singleton, K4, physical electron mass, alpha(0), or hydrogen.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
K4_ASSEMBLY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_K4_SCALE_ASSEMBLY_LADDER_REVIEW_PACKET_2026-07-05.md"
K4_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
K4_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
SOURCE_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
SOURCE_TARGET = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md"
SOURCE_COMPRESSION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md"
EXACT_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_RATIFICATION_DECISION_PACKET_2026-07-05.md"
EXACT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md"
F_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
L_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
P_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
R_DECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md"
F_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
L_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
R_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md"
PR5030 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_MULTISITE_PAULI_PR5030_CARRIER_PROVENANCE_IMPACT_DISCRIMINATOR_2026-07-05.md"
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


CLAUSE_TOKENS = {
    "F_CLAUSE_RETAINED",
    "L_CLAUSE_RETAINED",
    "P_CLAUSE_RETAINED",
    "R_CLAUSE_RETAINED",
}

SOURCE_PROBE_INPUTS = {
    "CLAUSE_TEXT_LOCK",
    "CHARGED_LEPTON_SCOPE_LOCK",
    "NO_NEW_PRIMITIVE_OR_AXIOM",
    "NO_EMPIRICAL_COMPARATOR_INPUT",
    "OWNER_RATIFICATION",
    "AUDIT_ACCEPTANCE",
}

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

HYDROGEN_INPUTS = {
    "RETAINED_ELECTRON_MASS_PHYSICAL_UNIT",
    "RETAINED_ALPHA0_LOW_ENERGY_COULOMB",
    "RETAINED_STATIC_SOURCE_NR_COULOMB_LIMIT",
    "ATOMIC_OPERATOR_HARNESS_VERIFIED",
    "NO_RYDBERG_COMPARATOR_PROOF_INPUT",
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


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    total = sum(values.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    if any(value < 0 for value in values.values()):
        raise ValueError("nonnegative values required")
    return {coord: value / total for coord, value in values.items()}


def closes_source_probe(inputs: set[str], clauses: set[str]) -> bool:
    return SOURCE_PROBE_INPUTS <= inputs and CLAUSE_TOKENS <= clauses


def closes_exact_source(inputs: set[str]) -> bool:
    return EXACT_SOURCE_INPUTS <= inputs


def closes_k4(inputs: set[str]) -> bool:
    return K4_INPUTS <= inputs


def closes_hydrogen(inputs: set[str]) -> bool:
    return HYDROGEN_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    source_paths = [
        NOTE,
        GOAL,
        K4_ASSEMBLY,
        K4_DECISION,
        K4_NO_GO,
        SOURCE_DECISION,
        SOURCE_TARGET,
        SOURCE_COMPRESSION,
        EXACT_DECISION,
        EXACT_NO_GO,
        F_DECISION,
        L_DECISION,
        P_DECISION,
        R_DECISION,
        F_NO_GO,
        L_NO_GO,
        P_NO_GO,
        R_NO_GO,
        PR5030,
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

    section("Required packet content")
    required_phrases = [
        "Exact Source Singleton Assembly Ladder Review Packet",
        "support / review-compression packet",
        "This packet does not ratify F/L/P/R",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "F_CLAUSE_RETAINED",
        "L_CLAUSE_RETAINED",
        "P_CLAUSE_RETAINED",
        "R_CLAUSE_RETAINED",
        "SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED",
        "FULL_CELL_SOURCE_CARRIER_CHECK",
        "PROJECTIVE_UNIFORM_RAY_CHECK",
        "S_L_READOUT_IDENTITY_BOUND",
        "WEAK_FRONT_BASE_RETAINED",
        "A3_PRECISION_PLACEMENT_RETAINED",
        "NO_SOURCE_A3_DOUBLE_COUNT",
        "CLAUSE_TEXT_LOCK",
        "NO_NEW_PRIMITIVE_OR_AXIOM",
        "NO_EMPIRICAL_COMPARATOR_INPUT",
        "OWNER_RATIFICATION",
        "AUDIT_ACCEPTANCE",
        "No proper subset of the six source-probe contract inputs",
        "No proper subset of the eleven exact-source contract inputs",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_F_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_R_CLAUSE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_INTERFACE_COMPRESSION_SUPPORT_2026-07-04.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_EXACT_SOURCE_SINGLETON_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "ZERO_IMPORT_HYDROGEN_ABSOLUTE_CHARGED_LEPTON_SCALE_RATIFICATION_DECISION_PACKET_2026-07-04.md",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "sigma([1])_c = 1/256",
        "a reduced two-slot carrier gives `1/16`",
        "a coordinate-tagged ray can give `1/112`",
        "`#5033` RP two-step runner scope cleanup | open, clean",
        "`#5030` multisite Pauli carrier provenance | open, clean",
        "`#5021` primitive-retirement review | open draft, dirty",
        "`#5018` domain-wall edge content vs SM chiral fermions map | open",
        "`#5017` domain-wall edge anomaly inflow via spectral flow | open",
        "`#5016` zero-import hydrogen retained lane bundle | open",
        "`#5015` wave-collapse-block01 measurement-collapse gate | open draft",
        "`#5014` record-formation front/domain-wall chirality | open",
        "`#5012` chirality domain-wall free-field note | open",
        "`#5007` Koide native zero-section route guard repair | open",
        "`#5006` static-source I1 hygiene companion | open",
        "`#4991` owner-governed Tier-A retirement | open",
        "The primitive registry was checked",
        "f_l_p_r_interface_primitive",
        "source_probe_interface_primitive",
        "exact_source_singleton_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
        "absolute_charged_lepton_scale_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
        "Distance To Hydrogen",
        "No-Go Discipline Gate",
        "Gate result",
        "Explicit Non-Claims",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Contract predicate checks")
    full_source_inputs = set(SOURCE_PROBE_INPUTS)
    full_clauses = set(CLAUSE_TOKENS)
    audit.check("full source-probe ladder closes interface", closes_source_probe(full_source_inputs, full_clauses))
    for missing in sorted(SOURCE_PROBE_INPUTS):
        reduced = set(SOURCE_PROBE_INPUTS)
        reduced.remove(missing)
        audit.check(f"source-probe fails without {missing}", not closes_source_probe(reduced, full_clauses))
    for missing in sorted(CLAUSE_TOKENS):
        reduced_clauses = set(CLAUSE_TOKENS)
        reduced_clauses.remove(missing)
        audit.check(f"source-probe fails without {missing}", not closes_source_probe(full_source_inputs, reduced_clauses))
    source_accepting = [
        (inputs, clauses)
        for inputs in all_subsets(SOURCE_PROBE_INPUTS)
        for clauses in all_subsets(CLAUSE_TOKENS)
        if closes_source_probe(inputs, clauses)
    ]
    audit.check("only full source-probe subset closes", source_accepting == [(full_source_inputs, full_clauses)])

    full_exact_inputs = set(EXACT_SOURCE_INPUTS)
    audit.check("full exact-source contract closes singleton", closes_exact_source(full_exact_inputs))
    for missing in sorted(EXACT_SOURCE_INPUTS):
        reduced = set(EXACT_SOURCE_INPUTS)
        reduced.remove(missing)
        audit.check(f"exact-source fails without {missing}", not closes_exact_source(reduced))
    exact_accepting = [subset for subset in all_subsets(EXACT_SOURCE_INPUTS) if closes_exact_source(subset)]
    audit.check("only full exact-source subset closes", exact_accepting == [full_exact_inputs])

    audit.check("F/L/P/R clauses alone do not close exact source", not closes_exact_source(set(CLAUSE_TOKENS)))
    audit.check(
        "source-probe acceptance alone does not close exact source",
        not closes_exact_source({"SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED"}),
    )
    audit.check("exact-source consequence alone does not close K4", not closes_k4({"EXACT_SOURCE_SINGLETON_RETAINED"}))
    audit.check("full K4 predicate model closes K4", closes_k4(set(K4_INPUTS)))
    audit.check("K4 consequence alone does not close hydrogen", not closes_hydrogen({"ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED"}))
    audit.check("full hydrogen predicate model closes hydrogen", closes_hydrogen(set(HYDROGEN_INPUTS)))

    section("Finite witness checks")
    coords = coordinates()
    audit.check("full-cell coordinate set has 256 elements", len(coords) == 256)
    uniform = {coord: Fraction(1) for coord in coords}
    sigma = normalize(uniform)
    audit.check("uniform singleton is exact 1/256", sigma[coords[0]] == Fraction(1, 256))
    audit.check("uniform source weights sum to one", sum(sigma.values(), Fraction(0)) == Fraction(1))
    no_full_cell = list(product(range(4), repeat=2))
    audit.check("reduced no-F witness gives 1/16", Fraction(1, len(no_full_cell)) == Fraction(1, 16))
    tagged = {coord: Fraction(4 if coord[0] == 0 else 1) for coord in coords}
    tagged_sigma = normalize(tagged)
    audit.check("coordinate-tagged no-L witness gives 1/112", tagged_sigma[(0, 0, 0, 0)] == Fraction(1, 112))
    audit.check("tagged witness differs from exact singleton", tagged_sigma[(0, 0, 0, 0)] != Fraction(1, 256))
    h = Fraction(3, 2)
    j_c = Fraction(5, 7)
    lam = Fraction(11, 5)
    raw = h * j_c
    raw_rescaled = (h / lam) * (lam * j_c)
    audit.check("raw h*j_c is invariant under source gauge rescale", raw == raw_rescaled)
    audit.check("raw j_c alone changes under source gauge rescale", j_c != lam * j_c)

    section("Authority boundary checks")
    goal = read(GOAL)
    k4_assembly = read(K4_ASSEMBLY)
    k4_decision = read(K4_DECISION)
    k4_no_go = read(K4_NO_GO)
    source_decision = read(SOURCE_DECISION)
    source_target = read(SOURCE_TARGET)
    compression = read(SOURCE_COMPRESSION)
    exact_decision = read(EXACT_DECISION)
    exact_no_go = read(EXACT_NO_GO)
    f_decision = read(F_DECISION)
    l_decision = read(L_DECISION)
    p_decision = read(P_DECISION)
    r_decision = read(R_DECISION)
    f_no_go = read(F_NO_GO)
    l_no_go = read(L_NO_GO)
    p_no_go = read(P_NO_GO)
    r_no_go = read(R_NO_GO)
    pr5030 = read(PR5030)
    a3_decision = read(A3_DECISION)
    physical_electron = read(PHYSICAL_ELECTRON)
    alpha_target = read(ALPHA_TARGET)
    static_target = read(STATIC_TARGET)

    audit.check("goal packet references source assembly ladder", NOTE.name in goal)
    audit.check("K4 assembly references source assembly ladder", NOTE.name in k4_assembly)
    audit.check("K4 decision references source assembly ladder", NOTE.name in k4_decision)
    audit.check("K4 no-go keeps K4 unsupplied", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in k4_no_go and "do not supply" in k4_no_go)
    audit.check("source decision remains support-only", "does not ratify F/L/P/R" in source_decision and "S_l = 1/256" in source_decision)
    audit.check("source target names one-clause witnesses", "no F" in source_target and "1/16" in source_target and "1/112" in source_target)
    audit.check("compression remains conditional", "If the normalized label-free source-probe interface is supplied" in compression)
    audit.check("exact decision remains below K4", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_decision and "No derivation or ratification of K4 scale assembly" in exact_decision)
    audit.check("exact no-go keeps singleton unsupplied", "EXACT_SOURCE_SINGLETON_RETAINED" in exact_no_go and "do not supply" in exact_no_go)
    audit.check("F decision packages F token", "F_CLAUSE_RETAINED" in f_decision and "does not ratify F" in f_decision)
    audit.check("L decision packages L token", "L_CLAUSE_RETAINED" in l_decision and "does not ratify L" in l_decision)
    audit.check("P decision packages P token", "P_CLAUSE_RETAINED" in p_decision and "does not ratify P" in p_decision)
    audit.check("R decision packages R token", "R_CLAUSE_RETAINED" in r_decision and "does not ratify R" in r_decision)
    audit.check("F no-go keeps F unsupplied", "F_CLAUSE_RETAINED" in f_no_go and "do not supply" in f_no_go)
    audit.check("L no-go keeps L unsupplied", "L_CLAUSE_RETAINED" in l_no_go and "do not supply" in l_no_go)
    audit.check("P no-go keeps P unsupplied", "P_CLAUSE_RETAINED" in p_no_go and "do not supply" in p_no_go)
    audit.check("R no-go keeps R unsupplied", "R_CLAUSE_RETAINED" in r_no_go and "do not supply" in r_no_go)
    audit.check("PR5030 remains finite carrier support only", "finite algebraic carrier support only" in pr5030)
    audit.check("A3 decision remains downstream", "A3_PRECISION_PLACEMENT_RETAINED" in a3_decision and "does not by itself derive `C_A3`" in a3_decision)
    audit.check("physical electron decision depends on K4", "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED" in physical_electron)
    audit.check("alpha target remains downstream", "No derivation of `alpha(0)`" in alpha_target)
    audit.check("static target remains downstream", "STATIC_SOURCE_RYDBERG" in static_target or "static-source Rydberg" in static_target)

    section("Primitive registry checks")
    registry = json.loads(read(REGISTRY))
    nodes = registry["nodes"]
    expected_nodes = {
        "minimal_axioms": "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "scale_reference_primitive": "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "kinetic_isotropy_primitive": "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "realized_state_primitive": "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    }
    for node, path in expected_nodes.items():
        audit.check(f"registry node present: {node}", node in nodes)
        audit.check(f"registry path matches for {node}", nodes[node]["current_path"] == path)

    minimal = read(MINIMAL)
    scale = flat(read(SCALE)).lower()
    kinetic = flat(read(KINETIC)).lower()
    realized = flat(read(REALIZED)).lower()
    audit.check("minimal axioms keep downstream derivation outside axiom content", "remain outside axiom content" in minimal)
    audit.check("scale primitive excludes dimensionless content", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes readout bridge", "readout bridge" in kinetic and "mass ratio" in kinetic)
    audit.check("realized primitive excludes state-selection values", "state-selection rule" in realized and "or value is supplied" in realized)
    for forbidden in [
        "f_l_p_r_interface_primitive",
        "source_probe_interface_primitive",
        "exact_source_singleton_primitive",
        "source_strength_normalization_primitive",
        "s_l_readout_primitive",
        "absolute_charged_lepton_scale_primitive",
        "electron_mass_primitive",
        "hydrogen_primitive",
    ]:
        audit.check(f"no shortcut primitive registered: {forbidden}", forbidden not in nodes)

    section("Non-claim checks")
    explicit_non_claims = [
        "No derivation or ratification of `F_CLAUSE_RETAINED`.",
        "No derivation or ratification of `L_CLAUSE_RETAINED`.",
        "No derivation or ratification of `P_CLAUSE_RETAINED`.",
        "No derivation or ratification of `R_CLAUSE_RETAINED`.",
        "No derivation or ratification of `SOURCE_PROBE_INTERFACE_CONTRACT_ACCEPTED`.",
        "No derivation or ratification of `EXACT_SOURCE_SINGLETON_RETAINED`.",
        "No retained status claim for exact source-side `S_l = 1/256`.",
        "No derivation or ratification of `ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED`.",
        "No derivation of `m_e`, `alpha(0)`, static-source Rydberg closure, or",
        "No new axiom, primitive, Tier-A admission, empirical import, or audit status",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This packet ratifies the exact source singleton",
        "This packet ratifies K4",
        "EXACT_SOURCE_SINGLETON_RETAINED is retained",
        "S_l = 1/256 is retained",
        "ABSOLUTE_CHARGED_LEPTON_SCALE_RETAINED is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This packet claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
