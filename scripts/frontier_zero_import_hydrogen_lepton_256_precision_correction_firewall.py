#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen lepton-1/256 precision firewall.

This support runner checks A3: exact 256 is not the same as the empirical
open-gate divisor 256.082435..., and a retained precision theorem remains
needed. It does not derive a charged-lepton mass or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2
M_W_ERR = 13.3
G_F = 1.1663787e-5
ALPHA0_INV = 137.035999084


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


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("precision-correction firewall note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_OS0_M2_TENSOR_GEOMETRY_REPAIR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SCHUR_TWO_SCALE_FIREWALL_2026-07-04.md",
        "docs/LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md",
        "docs/LEPTON_MASS_SCALE_MW_OVER_256_EMPIRICAL_OPEN_GATE_NOTE_2026-05-26.md",
        "docs/M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_note_phrases = [
        "A3 | Precision correction",
        "empirical divisor 256.08 versus",
        "a_lepton^2      = 313.8411267023086 MeV",
        "empirical N     = m_W / a_lepton^2 = 256.08243522600384",
        "C_A3 = 256 / N = 0.9996780910571587",
        "m_W(exact 256) = 256 * a_lepton^2 = 80343.328435791 MeV",
        "Candidate Correction Classes",
        "correction-on-exact-256",
        "direct-noninteger divisor",
        "Open PR Alignment",
        "#4926",
        "#4925",
        "#4922",
        "#4924",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed precision-correction firewall",
    ]
    for phrase in required_note_phrases:
        audit.check(f"required note phrase present: {phrase}", phrase in note)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Precision arithmetic")
    a2 = a_lepton_squared()
    n_empirical = M_W / a2
    epsilon = n_empirical / 256.0 - 1.0
    correction = 256.0 / n_empirical
    m_w_exact_256 = 256.0 * a2
    delta_m_w = M_W - m_w_exact_256
    n_lo = (M_W - M_W_ERR) / a2
    n_hi = (M_W + M_W_ERR) / a2
    sigma = abs(n_empirical - 256.0) / (256.0 * (M_W_ERR / M_W))

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10, f"a2={a2:.13f}")
    audit.check("repo m_W/256 comparator reproduced", abs(M_W / 256.0 - 313.9421875) < 1e-12)
    audit.check("empirical divisor is 256.082435", abs(n_empirical - 256.08243522600384) < 1e-10, f"N={n_empirical:.12f}")
    audit.check("relative offset is +0.032201 percent", abs(epsilon - 0.0003220126015774927) < 1e-15, f"epsilon={epsilon:.15f}")
    audit.check("required multiplicative correction is 0.999678091", abs(correction - 0.9996780910571587) < 1e-15)
    audit.check("exact-256 m_W value is about 80343.328 MeV", abs(m_w_exact_256 - 80343.328435791) < 1e-9)
    audit.check("repo m_W minus exact-256 m_W is about 25.872 MeV", abs(delta_m_w - 25.87156420899555) < 1e-9)
    audit.check("integer 256 excluded by m_W uncertainty window", n_lo > 256.0 or n_hi < 256.0, f"N window=[{n_lo:.3f},{n_hi:.3f}]")
    audit.check("integer 256 is about 1.945 sigma_mW away", 1.90 < sigma < 2.00, f"sigma={sigma:.6f}")

    section("Candidate correction scale comparisons")
    alpha0 = 1.0 / ALPHA0_INV
    v_gev = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5
    v_mev = v_gev * 1000.0
    g2_v = 2.0 * M_W / v_mev
    y_tau = M_TAU * math.sqrt(2.0) / v_mev
    required = epsilon
    comparisons = {
        "alpha0_over_pi": alpha0 / math.pi,
        "alpha0_over_8pi": alpha0 / (8.0 * math.pi),
        "g2sq_over_16pisq": g2_v * g2_v / (16.0 * math.pi * math.pi),
        "g2sq_over_64pisq": g2_v * g2_v / (64.0 * math.pi * math.pi),
        "ytau_sq_over_16pisq": y_tau * y_tau / (16.0 * math.pi * math.pi),
        "me_over_mmu": M_E / M_MU,
        "mmu_over_mtau": M_MU / M_TAU,
    }
    audit.check("alpha0/pi is about 7x too large", 6.5 < comparisons["alpha0_over_pi"] / required < 7.5)
    audit.check("alpha0/(8pi) is nearby but not equal", 0.85 < comparisons["alpha0_over_8pi"] / required < 0.95)
    audit.check("g2^2/(16pi^2) is about 8x too large", 8.0 < comparisons["g2sq_over_16pisq"] / required < 8.8)
    audit.check("g2^2/(64pi^2) is about 2x too large", 1.9 < comparisons["g2sq_over_64pisq"] / required < 2.2)
    audit.check("ytau^2/(16pi^2) is far too small", comparisons["ytau_sq_over_16pisq"] / required < 0.01)
    audit.check("simple lepton mass ratios are too large", comparisons["me_over_mmu"] / required > 10 and comparisons["mmu_over_mtau"] / required > 100)

    section("Primitive and non-claim boundary")
    registry = read(REGISTRY)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    audit.check("primitive registry names approved nodes", all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    audit.check("scale primitive excludes dimensionless physics", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selector/readout/empirical fit", "selector" in kinetic and "readout bridge" in kinetic and "empirical fit" in kinetic)
    audit.check(
        "realized-state primitive excludes values and normalization rules",
        "normalization rule" in realized and "or value is supplied" in realized,
    )

    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of a direct `N = 256.082435...` theorem.",
        "No derivation of a lepton scale-running or threshold correction.",
        "No derivation of `m_W`, `a_lepton`, `m_e`, `alpha(0)`, or hydrogen",
        "No use of observed charged-lepton masses or `m_W` as proof inputs.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives `C_A3`",
        "This note derives hydrogen",
        "precision correction is retained",
        "m_W is derived",
        "a_lepton is derived",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
