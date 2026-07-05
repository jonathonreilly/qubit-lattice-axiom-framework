#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen lepton-1/256 readout discriminator.

This support runner checks the finite-algebra arithmetic behind the A2
readout-measure split. It does not derive a charged-lepton mass or hydrogen.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
RECIPROCAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md"
TENSOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
FLAVOR_FORM = ROOT / "docs" / "FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md"
FLAVOR_EIN = ROOT / "scripts" / "flavor_einselection_2sector_modulo_kreality_2026_06_02.py"
PRE_RECORD_TRACE = ROOT / "docs" / "PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
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


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def flat(text: str) -> str:
    return " ".join(text.split())


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("readout-measure discriminator note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md",
        "scripts/flavor_einselection_2sector_modulo_kreality_2026_06_02.py",
        "docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md",
        "docs/LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md",
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
        "A2 | Readout rule",
        "A = M_2(C)^tensor4 ~= M_16(C)",
        "d_H       = 16",
        "dim_C(A)  = d_H^2 = 256",
        "projection trace / Born frame",
        "rank-one projection on `C^16`",
        "algebra-basis coefficient density",
        "one matrix-unit coordinate among `16^2` coordinates",
        "(1/sqrt(2))*(1/16)",
        "(1/sqrt(2))*(1/256)",
        "A2.1 measure-domain selector",
        "A2.2 norm-domain selector",
        "A2.3 basis/source-frame selector",
        "A2.4 coefficient uniformity",
        "A2.5 charged-lepton source bridge",
        "A2.6 precision interface",
        "#4922",
        "#4924",
        "#4928",
        "#4923",
        "#4927",
        "record-comparability block02",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed readout-measure discriminator",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Projection versus coefficient arithmetic")
    hilbert_dim = 16
    algebra_dim = hilbert_dim * hilbert_dim
    projection_weight = Fraction(1, hilbert_dim)
    coefficient_weight = Fraction(1, algebra_dim)
    unit_amplitude = 1.0 / math.sqrt(algebra_dim)
    block_norm = 1.0 / math.sqrt(2.0)
    audit.check("M_2(C)^tensor4 Hilbert dimension is 16", hilbert_dim == 2**4)
    audit.check("M_16(C) complex algebra dimension is 256", algebra_dim == 256)
    audit.check("rank-one projection trace weight is 1/16", projection_weight == Fraction(1, 16))
    audit.check("uniform matrix-unit coefficient weight is 1/256", coefficient_weight == Fraction(1, 256))
    audit.check("projection trace is 16 times the coefficient density", projection_weight / coefficient_weight == 16)
    audit.check("unit-amplitude normalization over 256 modes is 1/16", abs(unit_amplitude - 1.0 / 16.0) < 1e-15)
    audit.check(
        "D17 attached projection class is larger by factor 16",
        abs((block_norm * float(projection_weight)) / (block_norm * float(coefficient_weight)) - 16.0) < 1e-12,
    )
    audit.check(
        "coefficient density gives the lepton-scale target class",
        coefficient_weight == Fraction(1, 256) and abs(block_norm * float(coefficient_weight) - (1.0 / math.sqrt(2.0)) / 256.0) < 1e-15,
    )

    section("Source boundary checks")
    reciprocal = read(RECIPROCAL)
    tensor = read(TENSOR)
    flavor_form = read(FLAVOR_FORM)
    flavor_ein = read(FLAVOR_EIN)
    pre_record = read(PRE_RECORD_TRACE)
    basis_selector = read(BASIS_SELECTOR)
    lepton_scale = read(LEPTON_SCALE)
    minimal = flat(read(MINIMAL)).lower()
    registry = read(REGISTRY)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    scale = flat(read(SCALE)).lower()

    audit.check("reciprocal firewall distinguishes 1/sqrt(N) from 1/N", "1/sqrt(N) = 1/16" in reciprocal and "1/N = 1/256" in reciprocal)
    audit.check("tensor firewall records direct-product unit-normalization mismatch", "(1/sqrt(2))*(1/16)" in tensor and "(1/sqrt(2))*(1/256)" in tensor)
    audit.check(
        "flavor form/weight note excludes Record-supplied weights",
        "form/weight separation" in flavor_form
        and "Born weights" in flavor_form
        and "block-count" in flavor_form,
    )
    audit.check(
        "flavor einselection script separates Born dimension weights from block-counting",
        "Born/tracial max-entropy" in flavor_ein
        and "weights blocks by DIMENSION" in flavor_ein
        and "equal-power-per-block" in flavor_ein,
    )
    audit.check(
        "pre-record trace note contains matrix-unit normalized trace proof",
        "matrix-unit proof" in pre_record and "1/n" in pre_record and "Tr(A)" in pre_record,
    )
    audit.check(
        "lepton-scale probe names algebra-dimension target",
        "1/(dim_C M_2(C))^4" in lepton_scale and "1/256" in lepton_scale,
    )
    audit.check(
        "L1 source-norm discriminator cross-link is present",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md" in note
        and "L1 algebra-coordinate density" in note
        and "L2 / Hilbert-Schmidt / Fisher-unit" in note,
    )
    audit.check(
        "basis-selector discriminator cross-link is present",
        "basis/source-frame selector" in note
        and "1/256  ->  1/16" in basis_selector,
    )
    audit.check(
        "minimal axioms exclude weighting and source-observable bridges",
        "weights" in minimal
        and "source/action" in minimal
        and "physical-observable identification" in minimal,
    )
    audit.check("primitive registry names approved primitive nodes", all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    audit.check("kinetic primitive excludes readout bridge", "readout bridge" in kinetic and "selector" in kinetic and "empirical fit" in kinetic)
    audit.check("realized-state primitive excludes measure and weighting", "measure" in realized and "weighting" in realized and "normalization rule" in realized)
    audit.check("scale primitive excludes dimensionless physics", "dimensionless" in scale and "mass ratio" in scale)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar coefficient uses the",
        "No derivation of uniform coefficient density over the 256 matrix units.",
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
        "the charged-lepton scalar coefficient uses the algebra-basis source measure",
        "uniform coefficient density over the 256 matrix units is derived",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
