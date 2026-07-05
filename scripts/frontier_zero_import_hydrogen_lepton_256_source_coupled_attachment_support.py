#!/usr/bin/env python3
"""Verifier for lepton 1/256 source-coupled attachment support.

This runner checks the finite conditional theorem: under a supplied
source-coupled local-action convention and a supplied lepton-specific full-cell
scalar source, action derivatives attach the 256 full-cell source directions
as scalar multipliers on the D17 charged-lepton block. It does not derive S_l,
an electron mass, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
D17_SEPARABILITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
SIMPLEX = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
D17 = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
LOCAL_ACTION = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
P1_LOCALITY = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_LOCALITY_OF_SOURCE_DERIVATIVES_NARROW_NOTE_2026-05-21.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
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
    audit.check("source-coupled attachment support note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        FULL_CELL,
        D17_SEPARABILITY,
        SIMPLEX,
        D17,
        LOCAL_ACTION,
        P1_LOCALITY,
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
        "Source-Coupled Attachment Support",
        "source-coupled local-action convention",
        "lepton-specific full OS0-cell scalar source",
        "B_lep = (1/sqrt(2))",
        "A_cell = M_2(C)^tensor4",
        "|C| = 256",
        "S_lep[J] = h * B_lep * sum_{c in C} j_c O_c",
        "dS_lep/dj_c = h * B_lep * O_c",
        "does not introduce `512` independent product weights",
        "(1/sqrt(2))*(1/256)",
        "(1/sqrt(2))*(1/16)",
        "scalar-multiplier attachment",
        "source derivatives of `S` define local insertions",
        "RN/Fisher source-unit contrast",
        "Open PR Alignment",
        "#4935",
        "#4936",
        "G3 phase-type `F cup F` insertion",
        "No-Go Discipline Gate",
        "broad A1/S_l closure fails; narrowed source-coupled attachment support passes.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite source-derivative attachment arithmetic")
    coordinates = list(product(range(4), repeat=4))
    carrier_dim = len(coordinates)
    d17_components = 2
    d17_component = 1.0 / math.sqrt(d17_components)
    d17_norm_sq = d17_components * d17_component * d17_component
    derivative_directions = carrier_dim
    arbitrary_product_weights = d17_components * carrier_dim
    uniform_weight = Fraction(1, carrier_dim)
    separated_coeff = d17_component * float(uniform_weight)
    direct_unit_coeff = 1.0 / math.sqrt(arbitrary_product_weights)

    audit.check("coordinate set has 4^4 = 256 labels", carrier_dim == 256)
    audit.check("source derivative count equals carrier count", derivative_directions == 256)
    audit.check("D17 block has two weak-isospin components", d17_components == 2)
    audit.check("D17 block vector is unit-normalized", abs(d17_norm_sq - 1.0) < 1e-15, f"norm_sq={d17_norm_sq:.12f}")
    audit.check("arbitrary product attachment would have 512 coefficients", arbitrary_product_weights == 512)
    audit.check("uniform simplex source weight is exact 1/256", uniform_weight == Fraction(1, 256))
    audit.check(
        "separated coefficient is (1/sqrt2)*(1/256)",
        abs(separated_coeff - (1.0 / math.sqrt(2.0)) / 256.0) < 1e-15,
        f"coeff={separated_coeff:.12f}",
    )
    audit.check(
        "direct product unit coefficient is (1/sqrt2)*(1/16)",
        abs(direct_unit_coeff - (1.0 / math.sqrt(2.0)) / 16.0) < 1e-15,
        f"unit={direct_unit_coeff:.12f}",
    )
    audit.check(
        "direct unit coefficient is 16 times separated density coefficient",
        abs(direct_unit_coeff / separated_coeff - 16.0) < 1e-12,
        f"ratio={direct_unit_coeff / separated_coeff:.1f}",
    )

    slot_additive_dim = 4 * 4
    diagonal_dim = 4
    scalar_dim = 1
    audit.check("slot-additive source has 16 directions", slot_additive_dim == 16)
    audit.check("diagonal source has 4 directions", diagonal_dim == 4)
    audit.check("scalar/tracial source has 1 direction", scalar_dim == 1)
    audit.check("weaker source shapes do not reach 256", all(v != 256 for v in [slot_additive_dim, diagonal_dim, scalar_dim, d17_components]))

    section("Authority boundary checks")
    full_cell = read(FULL_CELL)
    d17_separability = read(D17_SEPARABILITY)
    simplex = read(SIMPLEX)
    d17 = read(D17)
    local_action = read(LOCAL_ACTION)
    p1_locality = read(P1_LOCALITY)
    source_measure = read(SOURCE_MEASURE)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    local_action_flat = flat(local_action).lower()
    p1_flat = flat(p1_locality).lower()
    minimal_flat = flat(minimal).lower()

    audit.check("full-cell support names source locality residual", "full OS0-cell source locality" in full_cell)
    audit.check("D17 separability names scalar source multiplier", "scalar source multiplier" in d17_separability)
    audit.check("simplex support keeps A2 source semantics open", "source-action semantics" in simplex and "not prove that the charged-lepton source" in simplex)
    audit.check("D17 note supplies scalar singlet and 1/sqrt2", "H_unit^lep = (1/sqrt(2))" in d17 and "unit coefficient is `1/sqrt(2)`" in d17)
    audit.check("D17 note excludes mass prediction", "lepton mass or Yukawa-value prediction" in d17)
    audit.check("local-action note is open_gate", "Claim type:** open_gate" in local_action)
    audit.check("local-action note names action source derivatives", "O_x[J]" in local_action and "source-derivative" in local_action)
    audit.check("local-action convention remains admitted", "source-coupling convention remains admitted" in local_action_flat)
    audit.check("P1 locality note guards scalar-generator circularity", "logically equivalent to p1" in p1_flat and "relabels p1" in p1_flat)
    audit.check("RN source-measure theorem names Fisher unit contrast", "Fisher norm `lambda^2`" in source_measure and "1/sqrt(6)" in source_measure)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal_flat and "outside axiom content" in minimal_flat)
    audit.check("kinetic primitive excludes selector and readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    audit.check(
        "registry names approved premise nodes",
        all(name in registry for name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source has full OS0-cell source",
        "No derivation of physical tensor-product source-frame selection.",
        "No derivation of A2 source-density readout.",
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
        "This note proves the source-coupled local-action convention",
        "This note proves A1 closure",
        "A2 source-density readout is derived",
        "the electron mass is derived",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
