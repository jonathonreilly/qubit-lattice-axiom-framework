#!/usr/bin/env python3
"""Verifier for the S_l source-readout identity bridge support note.

This runner checks the conditional symbol bridge:
if S_l denotes the normalized singleton source-strength multiplier, then
S_l = sigma([j])_c, and the prior uniform-ray chain gives 1/256.
It does not derive S_l, m_e, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md"
GOAL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_GOAL_PACKET_2026-07-04.md"
ROUTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md"
LEPTON_SCALE = ROOT / "docs" / "LEPTON_SCALE_FRONTIER_PROBE_2026-06-05.md"
D17_SEP = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_D17_FULL_CELL_SEPARABILITY_SUPPORT_2026-07-04.md"
SOURCE_COUPLED = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SHAPE_SELECTOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
PROJECTIVE_UNIFORM = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
INVARIANCE_BRIDGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
READOUT_DISCRIMINATOR = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
L1_NORM = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
PRECISION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


Coord = tuple[int, int, int, int]
Vector = dict[Coord, Fraction]


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


def coordinates() -> list[Coord]:
    return list(product(range(4), repeat=4))


def normalize(vector: Vector) -> Vector:
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in vector.items()}


def coefficient(front: Fraction, source_weight: Fraction) -> Fraction:
    return front * source_weight


def solve_s_l(front: Fraction, source_coeff: Fraction) -> Fraction:
    if front == 0:
        raise ValueError("nonzero front required")
    return source_coeff / front


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("S_l readout identity bridge note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        GOAL,
        ROUTE,
        LEPTON_SCALE,
        D17_SEP,
        SOURCE_COUPLED,
        SHAPE_SELECTOR,
        PROJECTIVE_SECTION,
        PROJECTIVE_UNIFORM,
        INVARIANCE_BRIDGE,
        SOURCE_MEASURE,
        READOUT_DISCRIMINATOR,
        L1_NORM,
        PRECISION,
        MINIMAL,
        KINETIC,
        SCALE,
        REALIZED,
        REGISTRY,
    ]
    for path in source_paths:
        audit.check(f"source path exists: {path.relative_to(ROOT)}", path.exists())

    section("Required note content")
    required_phrases = [
        "S_l Readout Identity Bridge Support",
        "S_l readout identity",
        "y_scale = g_2 * (1/sqrt(2)) * S_l",
        "source-readout convention",
        "normalized singleton source-strength multiplier",
        "S_l = sigma([j])_c",
        "sigma([j])_c = 1/256",
        "source-strength multiplier",
        "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "sigma([j])_c = (h*j_c)/H",
        "W6 candidate selector",
        "W6",
        "256.082435",
        "No-Go Discipline Gate",
        "broad `S_l` closure fails; narrowed source-readout identity bridge support passes.",
        "Gate result: `PASS` for the narrowed `S_l` source-readout identity bridge",
        "Open PR Alignment",
        "#4938",
        "MERGED",
        "#4945",
        "#4946",
        "#4947",
        "#4950",
        "#4952",
        "#4955",
        "#4956",
        "#4957",
        "#4958",
        "#4959",
        "#4960",
        "Phi = S_sum = 2/3",
        "Phi = Tr L_3^+ = 2/3",
        "minimal positive K-breaking",
        "dynamic helper dependency audit-packet repair",
        "hypercharge downstream trace scope quarantine",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("S_l source-readout identity arithmetic")
    coords = coordinates()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)

    uniform = {coord: Fraction(5, 1) for coord in coords}
    uniform_weights = normalize(uniform)
    source_weight = uniform_weights[coords[0]]
    audit.check("uniform projective source singleton is 1/256", source_weight == Fraction(1, 256))

    front = Fraction(7, 11)
    source_coeff = coefficient(front, source_weight)
    audit.check("source coefficient has front times source weight", source_coeff == front * Fraction(1, 256))
    audit.check("nonzero front cancellation recovers S_l source weight", solve_s_l(front, source_coeff) == source_weight)

    scaled_uniform = {coord: Fraction(25, 1) for coord in coords}
    audit.check("positive rescaling keeps normalized source weight", normalize(scaled_uniform)[coords[0]] == source_weight)

    nonuniform = {coord: Fraction(4 if coord[0] == 0 else 1, 1) for coord in coords}
    nonuniform_weights = normalize(nonuniform)
    audit.check("nonuniform normalized source ray still sums to one", sum(nonuniform_weights.values(), Fraction(0)) == 1)
    audit.check("nonuniform singleton is not 1/256", nonuniform_weights[coords[0]] != Fraction(1, 256))

    rn_amplitude = Fraction(1, 16)
    audit.check("RN/Fisher uniform 256-channel amplitude is 1/16", len(coords) * rn_amplitude * rn_amplitude == 1)
    audit.check("RN/Fisher amplitude differs from S_l source singleton", rn_amplitude != Fraction(1, 256))

    exact_divisor = Fraction(256, 1)
    comparator_micro = Fraction(256_082_435, 1_000_000)
    correction = exact_divisor / comparator_micro
    audit.check("precision correction remains below one", correction < 1)
    audit.check("precision correction is close to 0.999678", Fraction(9996, 10000) < correction < Fraction(1, 1))

    section("Authority boundary checks")
    lepton_scale = read(LEPTON_SCALE)
    d17_sep = read(D17_SEP)
    source_coupled = read(SOURCE_COUPLED)
    shape_selector = read(SHAPE_SELECTOR)
    projective_section = read(PROJECTIVE_SECTION)
    projective_uniform = read(PROJECTIVE_UNIFORM)
    invariance_bridge = read(INVARIANCE_BRIDGE)
    source_measure = read(SOURCE_MEASURE)
    readout_discriminator = read(READOUT_DISCRIMINATOR)
    l1_norm = read(L1_NORM)
    precision = read(PRECISION)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("lepton scale probe names y_scale factorization", "y_scale := a_lepton" in lepton_scale and "(1/sqrt(2))" in lepton_scale and "(1/256)" in lepton_scale)
    audit.check("D17 separability names D17 and 1/sqrt(2)", "D17" in d17_sep and "1/sqrt(2)" in d17_sep)
    audit.check("source-coupled note names derivative attachment", "dS_lep/dj_c = h * B_lep * O_c" in source_coupled)
    audit.check("shape selector names Q1-Q4 and sigma candidate", "Q1-Q4" in shape_selector and "(h*j_c)/H" in shape_selector)
    audit.check("projective-section note names sigma", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("uniform-ray note names W6 as S_l residual", "W6" in projective_uniform and "S_l" in projective_uniform)
    audit.check("invariance bridge names source-family naturality", "source-family naturality" in invariance_bridge)
    audit.check("source-measure theorem names Fisher source unit", "Fisher" in source_measure and "source unit" in source_measure)
    audit.check("readout discriminator contrasts projection/Born trace and 1/16", "projection/Born trace" in readout_discriminator and "1/16" in readout_discriminator)
    audit.check("L1 norm discriminator names L1 algebra-coordinate density", "L1 algebra-coordinate density" in l1_norm)
    audit.check("precision firewall names comparator divisor", "256.082435" in precision)
    audit.check("minimal axioms exclude source/action and weights", "source/action" in minimal_flat and "weights" in minimal_flat)
    audit.check("kinetic primitive excludes selector and readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("scale primitive excludes dimensionless quantity", "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    audit.check(
        "registry names approved premise nodes",
        all(name in registry for name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that `S_l` is physically the normalized singleton",
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is a full-cell",
        "No derivation that source controls are nonnegative source strengths.",
        "No derivation that charged-lepton source strength is physically the",
        "No unconditional derivation that source-family naturality is physically",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, Koide/electron species readout, `alpha(0)`, or",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives hydrogen",
        "This note proves W6",
        "W6 is now retained",
        "S_l is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
