#!/usr/bin/env python3
"""Verifier for the lepton-1/256 Schur two-scale firewall.

This runner checks exact arithmetic and source-boundary discipline. It does
not derive a charged-lepton mass, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md"

G2_V_BOUNDED = 0.6480
G_WEAK_CYCLE12 = 0.653
M_W = 80369.2
G_F = 1.1663787e-5


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
    audit.check("two-scale firewall note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/G_WEAK_FROM_FRAMEWORK_NOTE_2026-05-03.md",
        "docs/DM_NEUTRINO_SCHUR_SUPPRESSION_NAMED_ADMISSIONS_BOUNDED_THEOREM_NOTE_2026-06-07.md",
        "docs/DM_NEUTRINO_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md",
        "scripts/frontier_neutrino_schur_suppression_named_admissions.py",
        "scripts/frontier_neutrino_vsel_curvature_transport_obstruction.py",
        "docs/LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "y_scale(v) = g_2(v) * (1/sqrt(2)) * S_l",
        "S_l        = 1/256",
        "(g/sqrt(2))^2 / 32 = g^2 / 64",
        "g_2^2 |_lattice / 64 = 1/256",
        "mixed-scale split",
        "B1",
        "B2",
        "B3",
        "B4",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "C_A3 = 0.999678091",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed two-scale firewall passes",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Exact Schur and lattice arithmetic")
    g = 1.2345
    schur_left = (g / math.sqrt(2.0)) ** 2 / 32.0
    schur_right = g * g / 64.0
    audit.check(
        "Schur identity (g/sqrt2)^2/32 = g^2/64",
        abs(schur_left - schur_right) < 1e-15,
        f"diff={schur_left - schur_right:.3e}",
    )

    g2_lattice_sq = Fraction(1, 4)
    s_lattice = g2_lattice_sq / Fraction(64)
    target = Fraction(1, 256)
    audit.check("lattice suppressor is exact 1/256", s_lattice == target, str(s_lattice))
    audit.check("squared lattice suppressor is exact 1/65536", s_lattice * s_lattice == Fraction(1, 65536))

    section("Two-scale substitution tests")
    target_float = float(target)
    s_bounded_v = G2_V_BOUNDED * G2_V_BOUNDED / 64.0
    ratio_bounded = s_bounded_v / target_float
    s_cycle12 = G_WEAK_CYCLE12 * G_WEAK_CYCLE12 / 64.0
    ratio_cycle12 = s_cycle12 / target_float

    audit.check(
        "bounded weak-scale Schur suppressor overshoots 1/256 by about 68 percent",
        1.65 < ratio_bounded < 1.72,
        f"ratio={ratio_bounded:.6f}, overshoot={(ratio_bounded - 1.0) * 100:.2f}%",
    )
    audit.check(
        "cycle-12 weak benchmark suppressor overshoots 1/256 by about 71 percent",
        1.68 < ratio_cycle12 < 1.73,
        f"ratio={ratio_cycle12:.6f}, overshoot={(ratio_cycle12 - 1.0) * 100:.2f}%",
    )

    y_target_mixed = G2_V_BOUNDED / math.sqrt(2.0) * target_float
    y_all_weak = G2_V_BOUNDED / math.sqrt(2.0) * s_bounded_v
    y_all_lattice = 0.5 / math.sqrt(2.0) * target_float
    audit.check(
        "all-weak y_scale is too high by the same suppressor ratio",
        abs((y_all_weak / y_target_mixed) - ratio_bounded) < 1e-12,
        f"ratio={y_all_weak / y_target_mixed:.6f}",
    )
    audit.check(
        "all-lattice front factor undershoots target mixed-scale front",
        0.75 < (y_all_lattice / y_target_mixed) < 0.79,
        f"ratio={y_all_lattice / y_target_mixed:.6f}",
    )

    v_gev = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5
    g2_from_mw = 2.0 * (M_W / 1000.0) / v_gev
    s_from_mw = g2_from_mw * g2_from_mw / 64.0
    ratio_from_mw = s_from_mw / target_float
    audit.check(
        "m_W/v inferred weak-scale suppressor is also far above 1/256",
        ratio_from_mw > 1.65,
        f"g2={g2_from_mw:.6f}, ratio={ratio_from_mw:.6f}",
    )

    section("Named wall and non-claim boundary")
    for phrase in [
        "B1 | Charged-lepton Schur carrier",
        "B2 | Denominator/readout",
        "B3 | Sector identity",
        "B4 | Two-scale split",
        "derive a small correction from exact `256` to the empirical `256.08`",
    ]:
        audit.check(f"wall/repair target present: {phrase}", phrase in note)

    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of a charged-lepton Schur carrier.",
        "No proof that `S_l = y_nu^eff` or `S_l = y_0_lattice`.",
        "No derivation of the two-scale split.",
        "No derivation of the `256.08` correction.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "charged-lepton Schur carrier is retained",
        "two-scale split is derived",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "S_l = y_nu^eff is proven",
        "S_l = y_0_lattice is proven",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
