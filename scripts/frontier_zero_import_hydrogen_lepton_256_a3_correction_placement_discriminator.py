#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen lepton-1/256 A3 placement note.

This support runner checks that the A3 correction is treated as a placement
problem, not as a free empirical multiplier. It does not derive a charged
lepton mass or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md"
P1_SOURCE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P3_KOIDE_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md"
P4_DIRECT_NO_GO = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
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


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def a_lepton_squared() -> float:
    a = (math.sqrt(M_E) + math.sqrt(M_MU) + math.sqrt(M_TAU)) / 3.0
    return a * a


def weak_front_factor() -> float:
    v_mev = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5 * 1000.0
    g2 = 2.0 * M_W / v_mev
    return g2 / math.sqrt(2.0)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("A3 placement discriminator note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md",
        "docs/LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "A3 Correction-Placement Discriminator",
        "N_A3   = 256.08243522600384",
        "C_A3   = 256 / N_A3 = 0.9996780910571587",
        "1/N_A3 = C_A3 * (1/256) = 0.003904992543192026",
        "Placement Algebra",
        "(C_A3 F_0) * S_0",
        "F_0        * (C_A3 S_0)",
        "F_0        * S_0       * (C_A3 R_0)",
        "Placement Classes",
        "P1 source-readout correction",
        "P2 front-factor/threshold correction",
        "P3 Koide/electron-readout correction",
        "P4 direct noninteger divisor",
        "P5 empirical splice",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "P1_SOURCE_READOUT_CORRECTION_RETAINED",
        "CORRECTED_SOURCE_READOUT_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED",
        "KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED",
        "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED",
        "OPEN. Current direct-divisor surfaces do not supply",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md",
        "F_phys = C_A3 * g_2 * (1/sqrt(2))",
        "ell_A3 ~= 0.03768480771",
        "charged-lepton front/matching theorem",
        "Relation To The Current Source Chain",
        "source-family naturality",
        "sigma([j])_c = 1/256",
        "Open PR Alignment",
        "#5011",
        "CLEAN",
        "#4893",
        "#4898",
        "#4902",
        "#4905",
        "#4906",
        "#4938",
        "Merged into `main` at 2026-07-04T15:14:57Z",
        "#4940",
        "Currently `CLEAN`",
        "#4943",
        "Currently `DIRTY`",
        "#4947",
        "Currently `CLEAN`",
        "#4948",
        "Currently `CLEAN` after earlier moving labels",
        "#4949",
        "Currently `UNSTABLE` after earlier moving labels",
        "#4950",
        "additive-even premise relocation",
        "global exact-branch shortcut `n=dA`",
        "closed-nonexact sector",
        "minimal positive K-breaking / inhomogeneous C3 transport",
        "Primitive Boundary",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed correction-placement",
    ]
    for phrase in required_phrases:
        audit.check(f"required note phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("A3 correction arithmetic")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    s0 = 1.0 / 256.0
    s_corrected = c_a3 * s0
    s_direct = 1.0 / n_a3
    delta_s = s0 - s_direct
    relative_source_shift = s_direct / s0 - 1.0
    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 empirical divisor reproduced", abs(n_a3 - 256.08243522600384) < 1e-10, f"N={n_a3:.12f}")
    audit.check("A3 correction reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("exact source singleton is 1/256", abs(s0 - 0.00390625) < 1e-18)
    audit.check("corrected source singleton is 1/N_A3", abs(s_corrected - s_direct) < 1e-18)
    audit.check("corrected singleton value reproduced", abs(s_direct - 0.003904992543192026) < 1e-18)
    audit.check("A3 shifts source by about -0.03219 percent", -0.00033 < relative_source_shift < -0.00031)
    audit.check("absolute singleton correction is nonzero", delta_s > 1e-6)

    section("Placement degeneracy")
    front = weak_front_factor()
    r0 = 1.0
    product_source = front * (c_a3 * s0) * r0
    product_front = (c_a3 * front) * s0 * r0
    product_readout = front * s0 * (c_a3 * r0)
    product_direct = front * s_direct * r0
    base_product = front * s0 * r0
    audit.check("base product is shifted by C_A3", abs(product_source / base_product - c_a3) < 1e-15)
    audit.check("source placement equals front-factor placement", abs(product_source - product_front) < 1e-18)
    audit.check("source placement equals Koide/readout placement", abs(product_source - product_readout) < 1e-18)
    audit.check("source placement equals direct divisor placement", abs(product_source - product_direct) < 1e-18)
    audit.check("placement algebra is numerically degenerate", len({round(product_source, 18), round(product_front, 18), round(product_readout, 18), round(product_direct, 18)}) == 1)
    audit.check("placement correction is small but not zero", 0.999 < product_source / base_product < 1.0)

    section("Primitive and non-claim boundary")
    registry = read(REGISTRY)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    audit.check("primitive registry names approved nodes", all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    p4_direct_no_go = read(P4_DIRECT_NO_GO)
    audit.check("P4 current-surface no-go keeps direct divisor open", "P4_DIRECT_NONINTEGER_DIVISOR_RETAINED" in p4_direct_no_go and "DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED" in p4_direct_no_go)
    audit.check("scale primitive excludes dimensionless corrections", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selectors and empirical fit", "selector" in kinetic and "empirical fit" in kinetic and "readout bridge" in kinetic)
    audit.check("realized-state primitive excludes state content and normalization", "state-contingent content" in realized and "normalization rule" in realized)

    explicit_non_claims = [
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of `N_A3 = 256.082435...`.",
        "No derivation of corrected `S_l = 1/N_A3`.",
        "No derivation of a weak/lepton threshold correction.",
        "No derivation of a Koide/electron readout correction.",
        "No derivation of a direct noninteger divisor theorem.",
        "No use of observed charged-lepton masses or `m_W` as proof inputs.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `C_A3`",
        "This note derives `N_A3`",
        "This note derives corrected `S_l`",
        "threshold correction is retained",
        "Koide/electron readout correction is retained",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
