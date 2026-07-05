#!/usr/bin/env python3
"""Verifier for the lepton-1/256 matrix-unit basis-selector discriminator.

This support runner checks that fixed-basis matrix-unit coefficient density
can display 1/256, while full inner-automorphism covariance moves the same
projection to the tracial/projection class 1/16. It does not derive S_l,
an electron mass, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md"
READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
L1 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
TRACIAL = ROOT / "docs" / "PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md"
MAXSYM = ROOT / "docs" / "PRE_RECORD_REFERENCE_STATE_MAXIMAL_SYMMETRY_OPEN_GATE_NOTE_2026-06-05.md"
NOETHER = ROOT / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md"
LOCAL_DENSITY = ROOT / "docs" / "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
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


def coeff_average_sum_entries(entries: list[list[Fraction]]) -> Fraction:
    n = len(entries)
    return sum(sum(row, Fraction(0)) for row in entries) / (n * n)


def l1_mass(entries: list[list[Fraction]]) -> Fraction:
    return sum(sum(abs(x) for x in row) for row in entries)


def trace(entries: list[list[Fraction]]) -> Fraction:
    return sum(entries[i][i] for i in range(len(entries)))


def normalized_trace(entries: list[list[Fraction]]) -> Fraction:
    return trace(entries) / len(entries)


def hs_norm_squared_projection(entries: list[list[Fraction]]) -> Fraction:
    # The examples are real symmetric projections, so Tr(P^dag P)=sum_ij P_ij^2.
    return sum(sum(x * x for x in row) for row in entries)


def e00(n: int) -> list[list[Fraction]]:
    return [[Fraction(1 if i == 0 and j == 0 else 0) for j in range(n)] for i in range(n)]


def flat_projection(n: int) -> list[list[Fraction]]:
    return [[Fraction(1, n) for _ in range(n)] for _ in range(n)]


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("basis-selector discriminator note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md",
        "docs/PRE_RECORD_REFERENCE_STATE_MAXIMAL_SYMMETRY_OPEN_GATE_NOTE_2026-06-05.md",
        "docs/AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md",
        "docs/STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md",
        "docs/SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "A2 basis/covariance discriminator",
        "basis/source-frame selector",
        "A = M_2(C)^tensor4 ~= M_16(C)",
        "complex algebra dimension dim_C(A) = n^2 = 256",
        "fixed-basis coefficient avg",
        "1/256  ->  1/16",
        "(1/4)^4 = 1/256",
        "(1/2)^4 = 1/16",
        "MINIMAL_AXIOMS_2026-06-29.md",
        "PRE_RECORD_REFERENCE_STATE_MAXIMAL_SYMMETRY_OPEN_GATE_NOTE_2026-06-05.md",
        "AXIOM_FIRST_LATTICE_NOETHER_ABSTRACT_BILINEAR_CONTINUITY_NARROW_THEOREM_NOTE_2026-06-06.md",
        "STAGGERED_DIRAC_LOCAL_DENSITY_READOUT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-17.md",
        "#4922",
        "#4923",
        "#4927",
        "#4928",
        "#4929",
        "A2.3 basis/source-frame selector",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed matrix-unit basis-selector",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Exact covariance arithmetic")
    for n, label in [(2, "one-slot"), (16, "four-slot")]:
        e = e00(n)
        p = flat_projection(n)
        audit.check(f"{label}: E00 normalized trace is 1/{n}", normalized_trace(e) == Fraction(1, n))
        audit.check(f"{label}: flat projection normalized trace is 1/{n}", normalized_trace(p) == Fraction(1, n))
        audit.check(f"{label}: E00 fixed-basis coefficient average is 1/n^2", coeff_average_sum_entries(e) == Fraction(1, n * n))
        audit.check(f"{label}: flat projection fixed-basis coefficient average is 1/n", coeff_average_sum_entries(p) == Fraction(1, n))
        audit.check(f"{label}: E00 L1 coordinate mass is 1", l1_mass(e) == 1)
        audit.check(f"{label}: flat projection L1 coordinate mass is n", l1_mass(p) == n)
        audit.check(f"{label}: E00 Hilbert-Schmidt norm squared is 1", hs_norm_squared_projection(e) == 1)
        audit.check(f"{label}: flat projection Hilbert-Schmidt norm squared is 1", hs_norm_squared_projection(p) == 1)
        audit.check(
            f"{label}: fixed-basis coefficient average is not inner-automorphism invariant",
            coeff_average_sum_entries(e) != coeff_average_sum_entries(p),
            f"{coeff_average_sum_entries(e)} -> {coeff_average_sum_entries(p)}",
        )

    n = 16
    audit.check("four-slot fixed-coordinate value is exact 1/256", coeff_average_sum_entries(e00(n)) == Fraction(1, 256))
    audit.check("four-slot flat conjugate value is exact 1/16", coeff_average_sum_entries(flat_projection(n)) == Fraction(1, 16))
    audit.check("four-slot conjugation shifts coefficient average by factor 16", coeff_average_sum_entries(flat_projection(n)) / coeff_average_sum_entries(e00(n)) == 16)
    audit.check("projection/tracial value stays 1/16", normalized_trace(e00(n)) == normalized_trace(flat_projection(n)) == Fraction(1, 16))

    section("Source-authority boundary checks")
    readout = read(READOUT)
    l1 = read(L1)
    minimal = flat(read(MINIMAL)).lower()
    tracial = read(TRACIAL)
    maxsym = read(MAXSYM)
    noether = flat(read(NOETHER))
    local_density = read(LOCAL_DENSITY)
    source_measure = read(SOURCE_MEASURE)
    registry = read(REGISTRY)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    scale = flat(read(SCALE)).lower()

    audit.check(
        "readout discriminator names matrix-unit coefficient density",
        "matrix-unit coordinate" in readout and "1/256" in readout and "1/16" in readout,
    )
    audit.check(
        "L1 discriminator names L1 target and L2 contrast",
        "L1 algebra-coordinate density" in l1 and "L2 / Hilbert-Schmidt / Fisher" in l1,
    )
    audit.check(
        "minimal axioms provide no privileged possibility or source/action bridge",
        "no possibility is privileged" in minimal and "source/action" in minimal and "physical-observable identification" in minimal,
    )
    audit.check(
        "tracial derivation is inner-automorphism invariant state route",
        "inner-automorphism invariance" in tracial and "normalized trace" in tracial,
    )
    audit.check(
        "maximal-symmetry note treats no-preferred-basis as extra premise",
        "No preferred basis" in maxsym and "one premise" in maxsym and "record-absence does not entail" in maxsym,
    )
    audit.check(
        "Noether theorem supplies matrix-unit continuity, not source density",
        "matrix-unit Lie algebra" in noether and "support envelope" in noether and "does not use" in noether,
    )
    audit.check(
        "local density bridge supplies local projection identity",
        "n_x := a_x^dag a_x" in local_density and "positive local projection" in local_density,
    )
    audit.check(
        "RN source-measure theorem is Fisher-unit route",
        "Fisher norm `lambda^2`" in source_measure and "primitive source coordinate" in source_measure,
    )
    audit.check("primitive registry names approved primitive nodes", all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    audit.check("kinetic primitive excludes source frame/readout selector", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes measure and normalization", "measure" in realized and "normalization rule" in realized)
    audit.check("scale primitive excludes dimensionless physics", "dimensionless" in scale and "mass ratio" in scale)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar source uses the fixed",
        "No derivation of uniform L1 density over the 256 algebra coordinates.",
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
        "This note proves the charged-lepton scalar source uses the fixed",
        "uniform L1 density over the 256 algebra coordinates is derived",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
