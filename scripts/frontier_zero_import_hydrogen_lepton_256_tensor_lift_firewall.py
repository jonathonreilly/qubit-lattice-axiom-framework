#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen lepton-1/256 tensor-lift firewall.

This support runner checks the arithmetic and source boundaries behind A1:
the OS0 M_2(C)^tensor4 count is exact, but a theorem is still needed to attach
that carrier to the charged-lepton scalar coefficient.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
D17 = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
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
    audit.check("tensor-lift firewall note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md",
        "docs/LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md",
        "docs/M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_note_phrases = [
        "A1 | Tensor lift",
        "M_2(C) factor per OS0 regulator slot",
        "H_unit^lep = (1/sqrt(2))",
        "Z_lep^2 = N_c * N_iso = 1 * 2 = 2",
        "direct tensor product count = 2 * 256 = 512",
        "1/sqrt(512) = (1/sqrt(2)) * (1/16)",
        "(1/sqrt(2)) * (1/256)",
        "overshoots the needed suppressed coefficient by a factor of `16`",
        "T1 carrier attachment",
        "T2 sector specificity",
        "T3 D17 compatibility",
        "T4 readout compatibility",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md",
        "full OS0-cell linear source",
        "matrix-unit coordinates",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md",
        "D17 `1/sqrt(2)` normalization separates",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "C_A3 = 0.999678091",
        "Open PR Alignment",
        "#4925",
        "#4922",
        "#4924",
        "#4903",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed tensor-lift firewall passes",
    ]
    for phrase in required_note_phrases:
        audit.check(f"required note phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Tensor-count and normalization arithmetic")
    d17_count = 2
    dim_m2 = 4
    os0_slots = 4
    n_os0 = dim_m2**os0_slots
    direct_tensor_count = d17_count * n_os0
    d17_norm = 1.0 / math.sqrt(d17_count)
    os0_amplitude_norm = 1.0 / math.sqrt(n_os0)
    direct_unit_norm = 1.0 / math.sqrt(direct_tensor_count)
    target_density_norm = d17_norm * float(Fraction(1, n_os0))

    audit.check("D17 block count is 2", d17_count == 2)
    audit.check("D17 unit normalization is 1/sqrt2", abs(d17_norm - 1.0 / math.sqrt(2.0)) < 1e-15)
    audit.check("OS0 M_2(C)^tensor4 count is 256", n_os0 == 256)
    audit.check("direct D17 x OS0 tensor count is 512", direct_tensor_count == 512)
    audit.check(
        "direct unit normalization equals (1/sqrt2)*(1/16)",
        abs(direct_unit_norm - d17_norm * os0_amplitude_norm) < 1e-15
        and abs(os0_amplitude_norm - 1.0 / 16.0) < 1e-15,
        f"unit={direct_unit_norm:.12f}",
    )
    audit.check(
        "target separated normalization equals (1/sqrt2)*(1/256)",
        abs(target_density_norm - d17_norm / 256.0) < 1e-15,
        f"target={target_density_norm:.12f}",
    )
    audit.check(
        "ordinary direct-tensor unit normalization overshoots target by factor 16",
        abs(direct_unit_norm / target_density_norm - 16.0) < 1e-12,
        f"ratio={direct_unit_norm / target_density_norm:.1f}",
    )
    audit.check("reciprocal M_2(C)^tensor4 density is exact 1/256", Fraction(1, n_os0) == Fraction(1, 256))

    section("Source boundary checks")
    d17 = read(D17)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    for phrase in [
        "H_unit^lep = (1/sqrt(2))",
        "Z_lep^2 = N_c N_iso = 1 * 2 = 2",
        "unit coefficient is `1/sqrt(2)`",
    ]:
        audit.check(f"D17 boundary phrase present: {phrase}", phrase in d17)

    audit.check("minimal axioms supply one-site M_2(C)", "M_2(C)" in minimal)
    audit.check(
        "minimal axioms keep source/action and observable bridges outside axiom content",
        "source/action" in minimal_flat and "physical-observable identification" in minimal_flat,
    )
    audit.check(
        "minimal axioms exclude transition probabilities or weights",
        "transition probabilities or weights" in minimal_flat,
    )
    audit.check(
        "kinetic primitive supplies OS0 geometry but excludes readout bridge",
        "Z^3 x Z_tau" in kinetic and "readout bridge" in kinetic and "No mass ratio" in kinetic,
    )
    audit.check("registry names minimal axioms and kinetic primitive", "minimal_axioms" in registry and "kinetic_isotropy_primitive" in registry)
    audit.check(
        "registry excludes downstream normalization rules from primitives",
        "weighting, normalization" in registry,
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar block carries",
        "No derivation that ordinary tensor-product normalization is the lepton",
        "No derivation of a determinant, density, volume, Schur, or",
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
        "tensor lift is retained",
        "charged-lepton tensor lift is derived",
        "ordinary tensor-product normalization is retained as the lepton suppression",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
