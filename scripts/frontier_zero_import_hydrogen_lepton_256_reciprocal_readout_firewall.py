#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen lepton-1/256 reciprocal-readout firewall.

This support runner checks the arithmetic and source boundaries behind A2:
`1/dim_C(M_2(C)^tensor4)` is the target readout, but the readout rule itself
is not derived here.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
D17 = ROOT / "docs" / "LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
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


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("reciprocal-readout firewall note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md",
        "docs/LEPTON_BLOCK_SCALAR_SINGLET_COMPOSITE_UNIQUENESS_D17_PRIME_THEOREM_NOTE_2026-05-10.md",
        "docs/M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_note_phrases = [
        "A2 | Reciprocal readout",
        "dim_C(M_2(C)^tensor4) = 4^4 = 256",
        "y_scale = g_2 * (1/sqrt(2)) * S_l",
        "S_l     = 1/256",
        "H_unit^lep = (1/sqrt(2))",
        "Z_lep^2 = N_c * N_iso = 1 * 2 = 2",
        "1/sqrt(N) = 1/16",
        "1/N = 1/256",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "projection/Born trace",
        "algebra-basis coefficient density",
        "matrix-unit coordinates",
        "minimal_axioms",
        "kinetic_isotropy_primitive",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "(1/sqrt(2))*(1/16)",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "256.082435",
        "Open PR Alignment",
        "#4922",
        "#4924",
        "#4927",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed reciprocal-readout firewall",
    ]
    for phrase in required_note_phrases:
        audit.check(f"required note phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Readout arithmetic")
    dim_m2 = 4
    slots = 4
    n_modes = dim_m2**slots
    density_readout = Fraction(1, n_modes)
    amplitude_readout = 1.0 / math.sqrt(n_modes)
    block_norm = 1.0 / math.sqrt(2.0)
    audit.check("four-slot M_2(C) count is N=256", n_modes == 256)
    audit.check("volume/density reciprocal is exact 1/256", density_readout == Fraction(1, 256))
    audit.check("unit-amplitude normalization is 1/16", abs(amplitude_readout - 1.0 / 16.0) < 1e-15)
    audit.check(
        "amplitude readout overshoots density target by factor 16",
        abs(amplitude_readout / float(density_readout) - 16.0) < 1e-12,
        f"ratio={amplitude_readout / float(density_readout):.1f}",
    )
    audit.check("D17-prime block normalization is 1/sqrt2, not 1/256", abs(block_norm - 1.0 / math.sqrt(2.0)) < 1e-15 and abs(block_norm - 1.0 / 256.0) > 0.7)
    audit.check("block-only anchor divided by target-suppressed anchor differs by 256", Fraction(1, 1) / density_readout == 256)

    section("Source boundary checks")
    d17 = read(D17)
    lepton_scale = read(LEPTON_SCALE)
    minimal = read(MINIMAL)
    registry = read(REGISTRY)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    scale = read(SCALE)
    minimal_flat = flat(minimal).lower()
    scale_flat = flat(scale).lower()

    d17_phrases = [
        "H_unit^lep = (1/sqrt(2))",
        "Z_lep^2 = N_c N_iso = 1 * 2 = 2",
        "unit coefficient is `1/sqrt(2)`",
    ]
    for phrase in d17_phrases:
        audit.check(f"D17 boundary phrase present: {phrase}", phrase in d17)

    audit.check(
        "lepton-scale boundary names the exact g2, block, and 1/256 factorization",
        "y_scale :=" in lepton_scale
        and "g_2" in lepton_scale
        and "(1/sqrt(2))" in lepton_scale
        and "(1/256)" in lepton_scale,
    )
    for phrase in [
        "the factor `1/256 = 1/(dim_C M_2(C))^4`",
        "No derivation of `1/256`; it is the open gate.",
    ]:
        audit.check(f"lepton-scale boundary phrase present: {phrase}", phrase in lepton_scale)

    audit.check(
        "minimal axioms exclude weight/probability/source-observable bridges",
        "with what weight" in minimal_flat
        and "probability" in minimal_flat
        and "source/action" in minimal_flat
        and "physical-observable identification" in minimal_flat,
    )
    audit.check(
        "registry summary excludes downstream normalization rules",
        "weighting, normalization" in registry,
    )
    audit.check("primitive registry names approved primitive nodes", all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    audit.check("kinetic primitive excludes readout bridge and empirical fit", "readout bridge" in kinetic and "empirical fit" in kinetic)
    audit.check("realized-state primitive excludes normalization rule", "normalization rule" in realized)
    audit.check(
        "scale-reference primitive excludes dimensionless content",
        "dimensionless" in scale_flat and "mass ratio" in scale_flat,
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that reciprocal dimension is a Yukawa suppression.",
        "No derivation of the charged-lepton tensor lift.",
        "No derivation of a determinant, density, or volume readout theorem.",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "reciprocal dimension is retained as a Yukawa suppression",
        "determinant readout is derived",
        "density readout is derived",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
