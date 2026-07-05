#!/usr/bin/env python3
"""Verifier for the lepton-1/256 L1 source-norm discriminator.

This support runner checks that the target 1/256 belongs to the L1
algebra-coordinate density class, while uniform L2/Hilbert-Schmidt/Fisher
source-unit normalization over the same 256 coordinates gives 1/16.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
READOUT_DISC = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
TENSOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
SIMPLEX = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md"
SIMPLEX_UNIFORMITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
HIERARCHY_D4 = ROOT / "docs" / "HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md"
DM_SCHUR = ROOT / "docs" / "DM_WILSON_DIRECT_DESCENDANT_LOCAL_SCHUR_SOURCE_FAMILY_THEOREM_NOTE_2026-04-18.md"
BASIS_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"


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
    audit.check("L1 source-norm discriminator note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "docs/SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md",
        "docs/HIERARCHY_D4_DENSITY_SCALE_READOUT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-16.md",
        "docs/DM_WILSON_DIRECT_DESCENDANT_LOCAL_SCHUR_SOURCE_FAMILY_THEOREM_NOTE_2026-04-18.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "A2 source-norm discriminator",
        "L1 algebra-coordinate density",
        "L2 / Hilbert-Schmidt / Fisher unit",
        "dim_C M_2(C) = 4",
        "(1/4)^4 = 1/256",
        "(1/2)^4 = 1/16",
        "uniform L1 density vector has coefficient `1/256` and L2 norm `1/16`",
        "uniform L2 unit vector has coefficient `1/16` and L1 mass `16`",
        "RN-cocycle / P-cal source unit",
        "source-action simplex transfer",
        "linear action simplex average gives `1/256`",
        "source-action simplex uniformity",
        "uniquely `1/256` if local coordinate relabeling symmetry is physical",
        "matrix-unit basis/source frame",
        "basis/source-frame selector",
        "D4 fixed-density scale bridge",
        "determinant / Schur source-family route",
        "#4928",
        "#4923",
        "#4927",
        "#4922",
        "#4924",
        "A2.2 norm-domain selector",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed L1 source-norm discriminator",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("L1 versus L2 arithmetic")
    slot_dim = 4
    slots = 4
    total_dim = slot_dim**slots
    l1_slot = Fraction(1, slot_dim)
    l2_slot = Fraction(1, 2)  # 1/sqrt(4)
    l1_total = l1_slot**slots
    l2_total = l2_slot**slots
    l1_vector_l2_norm_sq = total_dim * l1_total * l1_total
    l2_vector_l1_mass = total_dim * l2_total
    audit.check("one M_2(C) algebra slot has four coordinates", slot_dim == 4)
    audit.check("four OS0 algebra slots give 256 coordinates", total_dim == 256)
    audit.check("one-slot L1 density is 1/4", l1_slot == Fraction(1, 4))
    audit.check("one-slot L2 unit coefficient is 1/2", l2_slot == Fraction(1, 2))
    audit.check("four-slot L1 density is exact 1/256", l1_total == Fraction(1, 256))
    audit.check("four-slot L2 unit coefficient is exact 1/16", l2_total == Fraction(1, 16))
    audit.check("L2 coefficient is 16 times the L1 coefficient", l2_total / l1_total == 16)
    audit.check("uniform L1 density vector has L2 norm 1/16", l1_vector_l2_norm_sq == Fraction(1, 256))
    audit.check("uniform L2 unit vector over 256 channels has L1 mass 16", l2_vector_l1_mass == 16)
    audit.check("target S_l belongs to L1 class, not L2 class", l1_total == Fraction(1, 256) and l2_total != Fraction(1, 256))

    section("Source transfer boundary checks")
    readout_disc = read(READOUT_DISC)
    tensor = read(TENSOR)
    source_measure = read(SOURCE_MEASURE)
    simplex = read(SIMPLEX)
    simplex_uniformity = read(SIMPLEX_UNIFORMITY)
    hierarchy = read(HIERARCHY_D4)
    dm_schur = read(DM_SCHUR)
    basis_selector = read(BASIS_SELECTOR)
    minimal = flat(read(MINIMAL)).lower()
    registry = read(REGISTRY)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    scale = flat(read(SCALE)).lower()

    audit.check(
        "readout discriminator names coefficient density and projection contrast",
        "algebra-basis coefficient density" in readout_disc and "projection/Born trace" in readout_disc,
    )
    audit.check(
        "tensor firewall keeps A1 carrier and A2 readout separate",
        "A1 tensor lift" in tensor and "A2 readout rule" in tensor and "(1/sqrt(2))*(1/16)" in tensor,
    )
    audit.check(
        "source-measure theorem is Fisher-unit / lambda-sensitive",
        "Fisher norm `lambda^2`" in source_measure
        and "lambda = 1" in source_measure
        and "1/sqrt(6)" in source_measure,
    )
    audit.check(
        "source-action simplex discriminator splits primitive unit from simplex average",
        "primitive source-unit" in simplex
        and "linear action simplex average" in simplex
        and "1/sqrt(256) = 1/16" in simplex,
    )
    audit.check(
        "source-action simplex uniformity support proves transitive coefficient",
        "transitivity forces" in simplex_uniformity
        and "w_* = 1/256" in simplex_uniformity
        and "35 orbits" in simplex_uniformity,
    )
    audit.check(
        "hierarchy D4 bridge is fixed-density-to-scale, not lepton source density",
        "rho_* = A(L) v(L)^4" in hierarchy
        and "fourth root" in hierarchy
        and "does not identify the electroweak VEV" in hierarchy,
    )
    audit.check(
        "DM Schur source-family theorem is conditional on supplied charged block",
        "once a charged microscopic block" in dm_schur
        and "does **not** derive the" in dm_schur
        and "charged microscopic block or the charged support" in dm_schur,
    )
    audit.check(
        "basis-selector discriminator makes fixed matrix-unit frame explicit",
        "1/256  ->  1/16" in basis_selector
        and "basis/source-frame selector" in basis_selector
        and "fixed-coordinate density fact" in basis_selector,
    )
    audit.check(
        "minimal axioms exclude source/action and normalization bridges",
        "source/action" in minimal and "born weights" in minimal and "probability" in minimal,
    )
    audit.check("primitive registry names approved primitive nodes", all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    audit.check("kinetic primitive excludes selector and readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes measure and normalization", "measure" in realized and "normalization rule" in realized)
    audit.check("scale primitive excludes dimensionless physics", "dimensionless" in scale and "mass ratio" in scale)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar source uses L1 algebra-density",
        "No derivation of uniformity over the 256 algebra coordinates.",
        "No derivation of the charged-lepton tensor lift.",
        "No derivation of a determinant, Schur, or volume-density theorem.",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note proves the charged-lepton scalar source uses L1 algebra-density",
        "uniformity over the 256 algebra coordinates is derived",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
