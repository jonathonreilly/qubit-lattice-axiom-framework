#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen full-cell source-carrier support.

This runner checks the A1 finite theorem: a full OS0-cell linear source over
four local M_2(C) slots has a 256-coordinate matrix-unit carrier, while weaker
source shapes do not.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
TENSOR_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
OS0_REPAIR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md"
SIMPLEX = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
D17 = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
SOURCE_ACTION = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
D17_SEPARABILITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


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


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("full-cell source-carrier note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        NOTE,
        TENSOR_FIREWALL,
        OS0_REPAIR,
        SIMPLEX,
        D17_SEPARABILITY,
        D17,
        SOURCE_ACTION,
        MINIMAL,
        KINETIC,
        SCALE,
        REALIZED,
        REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    section("Required note content")
    required_phrases = [
        "Full-Cell Source-Carrier Support",
        "full OS0-cell linear source",
        "M_2(C)^tensor4",
        "S_src[J] = sum_{c in C} j_c O_c",
        "|C| = 4^4 = 256",
        "slot-additive source",
        "`4 * 4 = 16`",
        "diagonal slot-locked source",
        "scalar/tracial source",
        "D17 weak-isospin singlet alone",
        "source-coupled local-action candidate",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "D17's `1/sqrt(2)` block normalization",
        "`512`-component unit vector",
        "Open PR Alignment",
        "#4903",
        "#4925",
        "#4932",
        "#4933",
        "No-Go Discipline Gate",
        "broad A1 closure fails; narrowed full-cell carrier support",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite carrier arithmetic")
    slot_dim = 4
    slots = ("x", "y", "z", "tau")
    coordinates = list(product(range(slot_dim), repeat=len(slots)))
    full_cell_dim = slot_dim ** len(slots)
    slot_additive_dim = slot_dim * len(slots)
    diagonal_dim = slot_dim
    scalar_dim = 1
    d17_components = 2

    audit.check("four OS0 slots are present", len(slots) == 4)
    audit.check("one M_2(C) matrix-unit basis has four coordinates", slot_dim == 4)
    audit.check("full-cell tensor coordinate count is 4^4", len(coordinates) == full_cell_dim == 256)
    audit.check("tensor coordinates are unique", len(set(coordinates)) == 256)
    audit.check("slot-additive source has 16 coordinates", slot_additive_dim == 16)
    audit.check("diagonal slot-locked source has 4 coordinates", diagonal_dim == 4)
    audit.check("scalar/tracial source has 1 coordinate", scalar_dim == 1)
    audit.check("D17 weak-isospin block has 2 components", d17_components == 2)
    audit.check("only full-cell tensor source reaches 256", all(v != 256 for v in [slot_additive_dim, diagonal_dim, scalar_dim, d17_components]))

    section("Authority boundary checks")
    tensor_firewall = read(TENSOR_FIREWALL)
    os0_repair = read(OS0_REPAIR)
    simplex = read(SIMPLEX)
    d17 = read(D17)
    source_action = read(SOURCE_ACTION)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()
    source_action_flat = flat(source_action).lower()

    audit.check("tensor firewall names A1 carrier attachment", "T1 carrier attachment" in tensor_firewall)
    audit.check("OS0 repair supplies 4^4 geometry count", "4^4 = 256" in os0_repair and "A1" in os0_repair)
    audit.check("simplex support requires supplied source-action semantics", "source-action semantics" in simplex and "not prove that the charged-lepton source" in simplex)
    audit.check("D17 supplies 1/sqrt2 and not mass closure", "H_unit^lep = (1/sqrt(2))" in d17 and "lepton mass or Yukawa-value prediction" in d17)
    audit.check("source-action note is an open gate", "claim_type: open_gate" in source_action and "open_gate" in source_action)
    audit.check("source-action note admits convention rather than deriving it", "not a derivation closure" in source_action_flat and "source-coupling convention remains admitted" in source_action_flat)
    audit.check("minimal axioms supply M_2(C)", "M_2(C)" in minimal)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal_flat and "outside axiom content" in minimal_flat)
    audit.check("kinetic primitive supplies OS0 geometry", "Z^3 x Z_tau" in kinetic and "OS0" in kinetic)
    audit.check("kinetic primitive excludes selector and readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless" in scale and "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    audit.check(
        "registry names approved primitive nodes",
        all(name in registry for name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar source has full OS0-cell source",
        "No derivation of the source-coupled local-action convention.",
        "No derivation of charged-lepton sector specificity for the full-cell carrier.",
        "No derivation of A2 source-density readout.",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives hydrogen",
        "This note claims A1 closure",
        "the charged-lepton scalar source has full OS0-cell source locality",
        "the source-coupled local-action convention is derived",
        "A2 source-density readout is derived",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
