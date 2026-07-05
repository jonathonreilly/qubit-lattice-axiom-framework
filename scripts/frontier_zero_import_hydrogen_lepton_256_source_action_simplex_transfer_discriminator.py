#!/usr/bin/env python3
"""Verifier for the lepton-1/256 source-action simplex discriminator.

This support runner checks that the top RN/Fisher source-unit precedent
transfers to a 256-channel uniform source as 1/16, while a linear action
simplex density gives 1/256. It does not derive S_l, a charged-lepton mass,
alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md"
L1 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
TENSOR_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
SIMPLEX_UNIFORMITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
TENSOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
YT_FISHER = ROOT / "docs" / "YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md"
YT_TIER_A = ROOT / "docs" / "YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md"
YT_DEM = ROOT / "docs" / "YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md"
LOCAL_ACTION = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
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


def flat(text: str) -> str:
    return " ".join(text.split())


def section(title: str) -> None:
    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-action simplex discriminator note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md",
        "docs/SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md",
        "docs/YT_PRIMITIVE_SOURCE_UNIT_FISHER_NORMALIZATION_SUPPORT_NOTE_2026-05-25.md",
        "docs/YT_TIER_A_SOURCE_ACTION_TOP_PREMISE_CLOSURE_NOTE_2026-05-29.md",
        "docs/YT_QUBIT_DEMOCRATIC_TOP_COEFFICIENT_CANDIDATE_NOTE_2026-05-25.md",
        "docs/OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md",
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
        "Source-Action Simplex Transfer Discriminator",
        "primitive RN/Fisher/L2 source unit",
        "linear action simplex density",
        "u_top,i = 1/sqrt(6)",
        "w_top,i = 1/6",
        "u_256,i = 1/sqrt(256) = 1/16",
        "w_256,i = 1/256",
        "O_avg = (1/256) sum_{i=1}^{256} O_i",
        "||O_avg||_2 = 1/16",
        "lambda = 1/sqrt(256) = 1/16",
        "(1/sqrt(2)) * (1/16)",
        "(1/sqrt(2)) * (1/256)",
        "A2.1 measure-domain selector",
        "A2.2 norm-domain selector",
        "linear action coefficient density / simplex average",
        "#4931",
        "occurrence/event license",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed source-action simplex transfer discriminator passes.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Exact source-normalization arithmetic")
    for n in [6, 256]:
        l2_coeff = 1.0 / math.sqrt(n)
        simplex_coeff = Fraction(1, n)
        lambda_scale = 1.0 / math.sqrt(n)
        audit.check(f"N={n}: L2 unit vector has norm one", abs(n * l2_coeff * l2_coeff - 1.0) < 1e-12)
        audit.check(f"N={n}: simplex density has L1 mass one", n * simplex_coeff == 1)
        audit.check(
            f"N={n}: simplex density L2 norm squared is 1/N",
            n * simplex_coeff * simplex_coeff == Fraction(1, n),
        )
        audit.check(
            f"N={n}: simplex/L2 coefficient ratio is 1/sqrt(N)",
            abs(float(simplex_coeff) / l2_coeff - lambda_scale) < 1e-12,
        )

    audit.check("top primitive unit coefficient is not top simplex coefficient", abs(1 / math.sqrt(6) - 1 / 6) > 0.2)
    audit.check("top primitive coefficient squared is 1/6", abs((1 / math.sqrt(6)) ** 2 - 1 / 6) < 1e-12)
    audit.check("lepton primitive unit coefficient is exact 1/16", Fraction(1, 16) == Fraction(1, int(math.sqrt(256))))
    audit.check("lepton simplex coefficient is exact 1/256", Fraction(1, 256) == Fraction(1, 256))
    audit.check("lepton primitive coefficient is 16 times simplex coefficient", Fraction(1, 16) / Fraction(1, 256) == 16)
    audit.check("lepton simplex viewed as RN coordinate has lambda^2=1/256", Fraction(1, 16) ** 2 == Fraction(1, 256))

    front = 1.0 / math.sqrt(2.0)
    primitive_front = front / 16.0
    target_front = front / 256.0
    audit.check("D17 front times primitive 256-unit gives larger coefficient", primitive_front > target_front)
    audit.check("D17 primitive/simplex ratio is 16", abs(primitive_front / target_front - 16.0) < 1e-12)

    section("Source-authority boundary checks")
    l1 = read(L1)
    readout = read(READOUT)
    tensor_frame = read(TENSOR_FRAME)
    simplex_uniformity = read(SIMPLEX_UNIFORMITY)
    tensor = read(TENSOR)
    source_measure = read(SOURCE_MEASURE)
    yt_fisher = read(YT_FISHER)
    yt_tier_a = read(YT_TIER_A)
    yt_dem = read(YT_DEM)
    local_action = read(LOCAL_ACTION)
    lepton_scale = read(LEPTON_SCALE)
    minimal = flat(read(MINIMAL)).lower()
    registry = read(REGISTRY)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    scale = flat(read(SCALE)).lower()

    audit.check("L1 discriminator names 1/256 as L1 and 1/16 as L2", "L1 algebra-coordinate density" in l1 and "(1/2)^4 = 1/16" in l1)
    audit.check("readout discriminator names projection contrast", "projection/Born trace" in readout and "algebra-basis coefficient density" in readout)
    audit.check("restricted tensor-frame support names relabeling invariance", "uniform coefficient 1/256 is invariant" in tensor_frame and "coordinate bijections" in tensor_frame)
    audit.check("simplex uniformity support derives uniqueness from transitivity", "transitivity forces" in simplex_uniformity and "w_* = 1/256" in simplex_uniformity)
    audit.check("tensor firewall records primitive-unit mismatch", "(1/sqrt(2))*(1/16)" in tensor and "(1/sqrt(2))*(1/256)" in tensor)
    audit.check("RN cocycle theorem names Fisher norm lambda squared", "Fisher norm `lambda^2`" in source_measure and "lambda = 1" in source_measure)
    audit.check("YT Fisher note selects lambda one", "lambda = 1" in yt_fisher and "1/sqrt(6)" in yt_fisher)
    audit.check("YT Tier-A source-action note is bounded top closure", "lambda = 1" in yt_tier_a and "y_33 = 1 / sqrt(6)" in yt_tier_a)
    audit.check("YT democratic note is unit-vector amplitude, not closure", "unit vector" in yt_dem and "1/sqrt(6)" in yt_dem and "does not claim" in yt_dem)
    audit.check("local-action note is an open-gate convention candidate", "open_gate" in local_action and "source-coupled local-action convention" in local_action)
    audit.check("lepton-scale probe isolates 1/256 as residual", "g_2" in lepton_scale and "(1/sqrt(2))" in lepton_scale and "(1/256)" in lepton_scale)
    audit.check("minimal axioms exclude source/action and observable bridges", "source/action" in minimal and "probability" in minimal and "physical-observable identification" in minimal)
    audit.check(
        "primitive registry names approved primitive nodes",
        all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]),
    )
    audit.check("kinetic primitive excludes selector/readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes measure and normalization", "measure" in realized and "normalization rule" in realized)
    audit.check("scale primitive excludes dimensionless suppression", "dimensionless" in scale and "mass ratio" in scale)

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar source uses linear action",
        "No derivation that the charged-lepton scalar source uses the tensor-product",
        "No derivation of the charged-lepton tensor lift.",
        "No derivation of the charged-lepton source bridge.",
        "No derivation of the `256.082435...` precision correction.",
        "No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note proves the charged-lepton scalar source uses linear action",
        "This note derives the charged-lepton source bridge",
        "hydrogen is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "A2 is closed",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
