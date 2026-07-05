#!/usr/bin/env python3
"""Verifier for the OS0 M_2(C)^tensor4 geometry repair note.

This is a support runner. It verifies finite dimension arithmetic and the
primitive boundary; it does not derive a charged-lepton mass or hydrogen.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md"
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


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("OS0 geometry repair note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md",
        "docs/LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "scripts/p2_euclidean_vs_lorentzian_fork_2026_06_05.py",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Finite dimension arithmetic")
    dim_m2 = 4
    spatial_slots = 3
    os0_slots = 4
    audit.check("dim_C M_2(C) = 4", dim_m2 == 4)
    audit.check("spatial-only count gives 4^3 = 64", dim_m2**spatial_slots == 64)
    audit.check("OS0 four-slot count gives 4^4 = 256", dim_m2**os0_slots == 256)
    audit.check("OS0/spatial count ratio is one M_2(C) factor = 4", (dim_m2**os0_slots) // (dim_m2**spatial_slots) == 4)
    audit.check("reciprocal four-slot value is exact 1/256", Fraction(1, dim_m2**os0_slots) == Fraction(1, 256))

    section("Primitive boundary")
    kinetic = read(KINETIC)
    registry = read(REGISTRY)
    required_kinetic_phrases = [
        "kinetic_isotropy_primitive",
        "Z^3 x Z_tau",
        "hypercubic-symmetric",
        "c_t = c_s",
        "No mass ratio",
        "selector",
        "readout bridge",
        "empirical fit",
    ]
    for phrase in required_kinetic_phrases:
        audit.check(f"kinetic primitive boundary phrase present: {phrase}", phrase in kinetic)

    audit.check("kinetic primitive registered in axiom premise registry", "kinetic_isotropy_primitive" in registry)
    audit.check("registry says primitives chain-satisfy without bounding downstream rows", "chain-satisfy without bounding downstream rows" in registry)

    section("Required note content")
    required_note_phrases = [
        "S_l = 1 / dim_C(M_2(C)^tensor4) = 1/256",
        "Z^3 x Z_tau, c_t = c_s",
        "four regulator slots",
        "A1 | Tensor lift",
        "A2 | Reciprocal readout",
        "A3 | Precision correction",
        "Follow-up A2 firewall",
        "Follow-up A1 firewall",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "Follow-up A3 firewall",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "256.082435",
        "1/sqrt(N) = 1/16",
        "geometry-slot premise only",
        "No-Go Discipline Gate",
        "broad closure fails; narrowed geometry repair passes",
    ]
    for phrase in required_note_phrases:
        audit.check(f"required note phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar block carries",
        "No derivation that reciprocal dimension is a Yukawa suppression.",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "charged-lepton scalar block carries M_2(C)^tensor4",
        "reciprocal dimension is the charged-lepton Yukawa suppression",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
