#!/usr/bin/env python3
"""Verifier for the zero-import hydrogen A3 P2 weak-front target note.

This support runner checks the P2 front-factor/threshold target arithmetic. It
does not derive C_A3, a charged-lepton mass, alpha(0), or hydrogen.
"""

from __future__ import annotations

import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md"
PRIMITIVE_REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"

M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86
M_W = 80369.2
G_F = 1.1663787e-5
B2 = 19.0 / 6.0

P2_REQUIRED_INPUTS = {
    "EXACT_SOURCE_SINGLETON_RETAINED",
    "WEAK_FRONT_BASE_RETAINED",
    "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
    "NO_SOURCE_DOUBLE_COUNT",
    "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
    "AUDIT_ACCEPTANCE",
}


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


def weak_front_components() -> tuple[float, float, float, float]:
    v_mev = (1.0 / (math.sqrt(2.0) * G_F)) ** 0.5 * 1000.0
    g2 = 2.0 * M_W / v_mev
    front = g2 / math.sqrt(2.0)
    alpha2 = g2 * g2 / (4.0 * math.pi)
    return v_mev, g2, front, alpha2


def closes_p2(inputs: set[str]) -> bool:
    return P2_REQUIRED_INPUTS <= inputs


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("A3 P2 weak-front discriminator note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_CORRECTION_PLACEMENT_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "docs/LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md",
        "docs/LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md",
        "docs/SU2_WEAK_BETA_COEFFICIENT_STRUCTURAL_CLOSED_FORM_THEOREM_NOTE_2026-04-26.md",
        "docs/audit/data/axiom_premise_nodes.json",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "A3 P2 Weak-Front Threshold Target Discriminator",
        "P2 front-factor/threshold correction",
        "F_phys = C_A3 * g_2 * (1/sqrt(2))",
        "S_l = 1/256",
        "N_A3 = 256.08243522600384",
        "C_A3 = 256 / N_A3 = 0.9996780910571587",
        "delta_front = C_A3 - 1 = -0.0003219089428413424",
        "1/alpha_2_phys = (1/C_A3^2) * 1/alpha_2_0",
        "Delta(1/alpha_2) ~= 0.01899279085",
        "b_2 = 19/6",
        "ell_A3",
        "exp(ell_A3) ~= 1.038403884",
        "Required P2 Closure Inputs",
        "ZERO_IMPORT_HYDROGEN_WEAK_FRONT_BASE_RATIFICATION_DECISION_PACKET_2026-07-05.md",
        "WEAK_FRONT_BASE_TEXT_LOCK",
        "SU2_WEAK_COUPLING_CONTEXT_RETAINED",
        "CHARGED_LEPTON_D17_BLOCK_NORMALIZATION_RETAINED",
        "UNCORRECTED_FRONT_SCOPE_LOCK",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_CHARGED_LEPTON_FRONT_MATCHING_CURRENT_SURFACE_NO_GO_2026-07-05.md",
        "current retained, primitive, and open-PR surfaces do not supply `CHARGED_LEPTON_FRONT_MATCHING_RETAINED`",
        "EXACT_SOURCE_SINGLETON_RETAINED",
        "WEAK_FRONT_BASE_RETAINED",
        "CHARGED_LEPTON_FRONT_MATCHING_RETAINED",
        "NO_SOURCE_DOUBLE_COUNT",
        "NO_MW_OR_LEPTON_COMPARATOR_PROOF_INPUT",
        "AUDIT_ACCEPTANCE",
        "Open PR Alignment",
        "#5011",
        "CLEAN",
        "#5010",
        "CLEAN",
        "#5009",
        "#5008",
        "#5007",
        "#5006",
        "No-Go Discipline Gate",
        "broad P2 no-go fails; narrowed weak-front threshold target",
    ]
    for phrase in required_phrases:
        audit.check(f"required note phrase present: {phrase}", flat(phrase) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("P2 target arithmetic")
    a2 = a_lepton_squared()
    n_a3 = M_W / a2
    c_a3 = 256.0 / n_a3
    delta_front = c_a3 - 1.0
    v_mev, g2, front, alpha2 = weak_front_components()
    inv_alpha2 = 1.0 / alpha2
    inv_rel_shift = 1.0 / (c_a3 * c_a3) - 1.0
    delta_inv_alpha2 = inv_alpha2 * inv_rel_shift
    ell_a3 = delta_inv_alpha2 * (2.0 * math.pi) / B2
    scale_ratio = math.exp(ell_a3)
    exact_source = 1.0 / 256.0
    base_product = front * exact_source
    p2_product = c_a3 * front * exact_source
    p1_product = front * (c_a3 * exact_source)

    audit.check("repo a_lepton^2 comparator reproduced", abs(a2 - 313.8411267023086) < 1e-10)
    audit.check("A3 empirical divisor reproduced", abs(n_a3 - 256.08243522600384) < 1e-10)
    audit.check("A3 correction reproduced", abs(c_a3 - 0.9996780910571587) < 1e-15)
    audit.check("front correction is the expected -0.03219 percent", -0.00033 < delta_front < -0.00031, f"delta={delta_front:.15f}")
    audit.check("weak g2 comparator reproduced", abs(g2 - 0.6528252293493516) < 1e-14)
    audit.check("weak front comparator reproduced", abs(front - 0.4616171466025896) < 1e-14)
    audit.check("inverse alpha2 comparator reproduced", abs(inv_alpha2 - 29.48600969791912) < 1e-12)
    audit.check("inverse alpha2 shift reproduced", abs(delta_inv_alpha2 - 0.018992790852657246) < 1e-15)
    audit.check("one-loop equivalent log reproduced", abs(ell_a3 - 0.03768480771402659) < 1e-15)
    audit.check("one-loop equivalent scale ratio reproduced", abs(scale_ratio - 1.0384038843982628) < 1e-15)
    audit.check("P2 product equals P1 product numerically", abs(p2_product - p1_product) < 1e-20)
    audit.check("P2 product is C_A3 times base product", abs(p2_product / base_product - c_a3) < 1e-15)
    audit.check("P2 correction is small but nonzero", 0.999 < p2_product / base_product < 1.0)

    section("P2 closure predicate")
    empty_inputs: set[str] = set()
    source_only = {"EXACT_SOURCE_SINGLETON_RETAINED"}
    front_only = {"WEAK_FRONT_BASE_RETAINED"}
    no_matching = P2_REQUIRED_INPUTS - {"CHARGED_LEPTON_FRONT_MATCHING_RETAINED"}
    full = set(P2_REQUIRED_INPUTS)
    audit.check("empty inputs do not close P2", not closes_p2(empty_inputs))
    audit.check("source singleton alone does not close P2", not closes_p2(source_only))
    audit.check("weak front alone does not close P2", not closes_p2(front_only))
    audit.check("all but matching theorem does not close P2", not closes_p2(no_matching))
    audit.check("full P2 predicate closes P2", closes_p2(full))

    section("Primitive and non-claim boundary")
    registry = read(PRIMITIVE_REGISTRY)
    scale = flat(read(SCALE)).lower()
    kinetic = read(KINETIC)
    realized = flat(read(REALIZED)).lower()
    audit.check("primitive registry names approved nodes", all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]))
    audit.check("no A3 correction primitive is registered", "a3_correction_primitive" not in registry and "weak_front_matching_primitive" not in registry)
    audit.check("scale primitive excludes dimensionless corrections", "zero dimensionless content" in scale and "mass ratio" in scale)
    audit.check("kinetic primitive excludes selectors and empirical fit", "selector" in kinetic and "empirical fit" in kinetic and "readout bridge" in kinetic)
    audit.check("realized-state primitive excludes normalization", "normalization rule" in realized and "state-contingent content" in realized)

    explicit_non_claims = [
        "No derivation of `C_A3 = 0.999678091...`.",
        "No derivation of a charged-lepton weak-front threshold correction.",
        "No derivation of a finite matching or scheme correction.",
        "No derivation of corrected `S_l`.",
        "No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.",
        "No use of observed charged-lepton masses, observed `m_W`, fitted `a_l`, or",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `C_A3`",
        "weak-front threshold correction is retained",
        "finite matching correction is retained",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
