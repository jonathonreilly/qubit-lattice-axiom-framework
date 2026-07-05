#!/usr/bin/env python3
"""Verifier for D17/full-cell source-carrier separability support.

The runner checks that a supplied full-cell source carrier can separate from
the fixed D17 weak-isospin singlet normalization, while direct product unit
normalization remains the wrong class for the lepton 1/256 lane.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
FULL_CELL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md"
TENSOR_FIREWALL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
SIMPLEX = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
D17 = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
SOURCE_ACTION = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
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
    audit.check("D17/full-cell separability note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        NOTE,
        FULL_CELL,
        TENSOR_FIREWALL,
        SIMPLEX,
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
        "D17 Full-Cell Separability Support",
        "H_unit^lep = (1/sqrt(2))",
        "Z_lep^2 = N_c N_iso = 1 * 2 = 2",
        "A_cell = M_2(C)^tensor4",
        "|C| = 256",
        "S_lift[J]",
        "coefficient(alpha,c) = (1/sqrt(2)) * (1/256)",
        "does not force a unit vector over `512` product",
        "direct unit vector over `2 * 256` components",
        "arbitrary product weights `u_{alpha,c}`",
        "SU(2)-triplet carrier insertion",
        "source-coupled local-action route marker",
        "Open PR Alignment",
        "#4925",
        "#4932",
        "#4934",
        "No-Go Discipline Gate",
        "broad T2/T3 closure fails; narrowed D17 full-cell",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("D17/source-carrier separability arithmetic")
    d17_components = 2
    carrier_dim = 4**4
    d17_component = 1.0 / math.sqrt(d17_components)
    d17_norm_sq = d17_components * d17_component * d17_component
    uniform_weight = Fraction(1, carrier_dim)
    separated_coeff = d17_component * float(uniform_weight)
    direct_unit_coeff = 1.0 / math.sqrt(d17_components * carrier_dim)
    free_source_weights = carrier_dim
    arbitrary_product_weights = d17_components * carrier_dim

    audit.check("D17 block has two weak-isospin components", d17_components == 2)
    audit.check("D17 vector is unit-normalized", abs(d17_norm_sq - 1.0) < 1e-15, f"norm_sq={d17_norm_sq:.12f}")
    audit.check("full-cell source carrier has 256 coordinates", carrier_dim == 256)
    audit.check("separable source has 256 free source weights", free_source_weights == 256)
    audit.check("arbitrary product weights would have 512 free coefficients", arbitrary_product_weights == 512)
    audit.check("uniform source weight is exact 1/256", uniform_weight == Fraction(1, 256))
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
        "direct product unit coefficient is 16 times separated source-density coefficient",
        abs(direct_unit_coeff / separated_coeff - 16.0) < 1e-12,
        f"ratio={direct_unit_coeff / separated_coeff:.1f}",
    )

    section("Authority boundary checks")
    full_cell = read(FULL_CELL)
    tensor_firewall = read(TENSOR_FIREWALL)
    simplex = read(SIMPLEX)
    d17 = read(D17)
    source_action = read(SOURCE_ACTION)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    source_action_flat = flat(source_action).lower()
    minimal_flat = flat(minimal).lower()

    audit.check("full-cell support names full-cell source locality as residual", "full OS0-cell source locality" in full_cell)
    audit.check("tensor firewall names D17 compatibility", "T3 D17 compatibility" in tensor_firewall)
    audit.check("simplex support does not provide D17 attachment", "not prove that the charged-lepton source" in simplex)
    audit.check("D17 source note names scalar singlet", "unique color-singlet, SU(2)-singlet" in d17)
    audit.check("D17 source note names 1/sqrt2", "unit coefficient is `1/sqrt(2)`" in d17)
    audit.check("D17 source note does not assign retained status", "does not assign retained status" in d17)
    audit.check("D17 non-claims exclude mass prediction", "lepton mass or Yukawa-value prediction" in d17)
    audit.check("source-action note is open_gate", "claim_type: open_gate" in source_action)
    audit.check("source-action convention remains admitted", "source-coupling convention remains admitted" in source_action_flat)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal_flat and "outside axiom content" in minimal_flat)
    audit.check("kinetic primitive excludes readout bridge", "readout bridge" in kinetic)
    audit.check("scale primitive excludes dimensionless physics", "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    audit.check(
        "registry names approved premise nodes",
        all(name in registry for name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of A1 closure from D17.",
        "No derivation of charged-lepton full OS0-cell source locality.",
        "No derivation of the source-coupled local-action convention.",
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
        "This note proves D17 closes A1",
        "D17 derives the electron mass",
        "This note proves charged-lepton full OS0-cell source locality",
        "A2 source-density readout is derived",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
