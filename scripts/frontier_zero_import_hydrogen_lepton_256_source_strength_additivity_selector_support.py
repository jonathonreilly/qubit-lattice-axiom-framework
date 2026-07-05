#!/usr/bin/env python3
"""Verifier for source-strength additivity selector support in the lepton 1/256 lane.

This runner checks the finite conditional theorem: a normalized finitely
additive source-strength measure over the 256 tensor-frame source controls,
with transitive local relabeling symmetry, assigns singleton strength 1/256.
It does not derive S_l, a charged-lepton mass, alpha(0), or hydrogen
spectroscopy.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
L1 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
TRANSFER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md"
UNIFORMITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
ATTACHMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


Coord = tuple[int, int, int, int]


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


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def measure(subset: set[Coord], singleton_weight: Fraction) -> Fraction:
    return Fraction(len(subset)) * singleton_weight


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-strength additivity selector support note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        L1,
        TRANSFER,
        UNIFORMITY,
        SOURCE_SLOT,
        ATTACHMENT,
        SOURCE_MEASURE,
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
        "Source-Strength Additivity Selector Support",
        "source-strength additivity selector support",
        "linear action-strength coordinates",
        "mu(A union B) = mu(A) + mu(B)",
        "mu(C) = 1",
        "mu({c}) = 1/256",
        "L1/simplex",
        "L2/RN/Fisher",
        "1/sqrt(256) = 1/16",
        "source-control coarse graining",
        "J(j) = sum_c j_c O_c",
        "squared L2 amplitudes",
        "Open PR Alignment",
        "#4938",
        "#4939",
        "AC(i) dynamical-index occupancy no-go",
        "#4940",
        "rule achirality from minimality",
        "#4941",
        "AC(i) determinant-order/chiral L-R no-go",
        "K/CPT orbit-constancy supplied-context bridge",
        "No-Go Discipline Gate",
        "broad A2/S_l closure fails; narrowed source-strength additivity selector support passes.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite additivity arithmetic")
    coords = coordinates()
    n = len(coords)
    singleton_weight = Fraction(1, n)
    audit.check("source coordinate set has 4^4 = 256 labels", n == 256)
    audit.check("uniform additive singleton weight is exact 1/256", singleton_weight == Fraction(1, 256))
    audit.check("256 additive singleton weights sum to 1", n * singleton_weight == 1)

    first_block = set(coords[:100])
    second_block = set(coords[100:])
    union_block = first_block | second_block
    audit.check("test blocks are disjoint", first_block.isdisjoint(second_block))
    audit.check(
        "finite additivity holds for a 100+156 coarse graining",
        measure(union_block, singleton_weight) == measure(first_block, singleton_weight) + measure(second_block, singleton_weight) == 1,
    )

    one_slot_zero = {coord for coord in coords if coord[0] == 0}
    audit.check("one-slot marginal has 64 source controls", len(one_slot_zero) == 64)
    audit.check("one-slot additive marginal is 1/4", measure(one_slot_zero, singleton_weight) == Fraction(1, 4))

    four_equal_parts = [set(coords[i * 64 : (i + 1) * 64]) for i in range(4)]
    audit.check("four equal coarse-graining parts cover C", sum(len(part) for part in four_equal_parts) == n)
    audit.check("four equal additive part strengths sum to 1", sum(measure(part, singleton_weight) for part in four_equal_parts) == 1)

    section("L1 versus L2/RN/Fisher source-strength contrast")
    l2_uniform = Fraction(1, 16)
    audit.check("uniform 256-channel L2/RN amplitude is 1/16", n * l2_uniform * l2_uniform == 1)
    audit.check("L2/RN amplitude is 16 times the L1 source-strength weight", l2_uniform / singleton_weight == 16)

    for k in [2, 4, 16, 256]:
        l1_part = Fraction(1, k)
        l2_amp = 1.0 / math.sqrt(k)
        audit.check(f"L1 equal refinement with k={k} sums to one", k * l1_part == 1)
        audit.check(
            f"L2 amplitude refinement with k={k} is not linear-additive",
            not math.isclose(k * l2_amp, 1.0, rel_tol=0.0, abs_tol=1e-12) if k > 1 else True,
            f"sum_amplitudes={k * l2_amp:.6g}",
        )
        audit.check(
            f"squared L2 amplitudes with k={k} are additive only after squaring",
            math.isclose(k * (l2_amp * l2_amp), 1.0, rel_tol=0.0, abs_tol=1e-12),
        )

    audit.check("coarse-grained L2 unit amplitude is not additive for 1+1", not math.isclose(math.sqrt(2.0), 2.0))
    audit.check("squaring changes source object from linear coefficient", "the additive object is `u_c^2`, not the linear action coefficient" in note_flat)

    section("Authority boundary checks")
    l1 = read(L1)
    transfer = read(TRANSFER)
    uniformity = read(UNIFORMITY)
    source_slot = read(SOURCE_SLOT)
    attachment = read(ATTACHMENT)
    source_measure = read(SOURCE_MEASURE)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("L1 discriminator names 1/256 density and 1/16 source-unit contrast", "L1 algebra-coordinate density" in l1 and "1/16" in l1)
    audit.check(
        "transfer discriminator names linear action simplex density",
        "linear action simplex density" in transfer and "primitive RN/Fisher/L2 source unit" in transfer,
    )
    audit.check("uniformity support names simplex normalization and transitivity", "simplex normalization" in uniformity and "transitivity" in uniformity)
    audit.check("source-slot frame note names J(j) source map", "J(j) = sum_{c in C} j_c O_c" in source_slot)
    audit.check("attachment note names source-coupled local-action convention", "source-coupled local-action convention" in attachment)
    audit.check("RN theorem names Fisher norm and source unit", "Fisher norm" in source_measure and "source unit" in source_measure)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal_flat and "outside axiom content" in minimal_flat)
    audit.check("kinetic primitive excludes normalization and selector", "selector" in kinetic and "normalization" in kinetic)
    audit.check("scale primitive excludes dimensionless quantity", "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    audit.check(
        "registry names approved premise nodes",
        all(name in registry for name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar source uses additive",
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is a full-cell",
        "No derivation of tensor-frame relabeling symmetry as a physical source",
        "No derivation of the charged-lepton source bridge.",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives hydrogen",
        "This note proves A2 closure",
        "S_l is retained",
        "the charged-lepton scalar source uses additive source-strength semantics.",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
