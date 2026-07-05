#!/usr/bin/env python3
"""Verifier for the source-strength normalization gauge firewall.

This runner checks the finite rescaling freedom between source controls and
the source-coupling amplitude. It does not derive S_l, a charged-lepton mass,
alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md"
SOURCE_CONTROL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
SOURCE_STRENGTH = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
ATTACHMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
TRANSFER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


Coord = tuple[int, int, int, int]


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


def normalize(values: dict[Coord, Fraction]) -> dict[Coord, Fraction]:
    total = sum(values.values(), Fraction(0))
    return {coord: value / total for coord, value in values.items()}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-strength normalization gauge firewall note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        SOURCE_CONTROL,
        SOURCE_STRENGTH,
        ATTACHMENT,
        SOURCE_SLOT,
        TRANSFER,
        SOURCE_MEASURE,
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
        "Source-Strength Normalization Gauge Firewall",
        "S_src[j] = h * B_lep * J(j)",
        "(h, j) -> (h/lambda, lambda j)",
        "h * J(j)",
        "mu(C) = 1",
        "total-strength section",
        "positive source vector",
        "w_c = j_c / sum_d j_d",
        "1/256",
        "1/16",
        "source control magnitude and source-coupling amplitude",
        "normalization gauge",
        "Record-Additivity Firewall",
        "Open PR Alignment",
        "Merge-state labels are moving review metadata",
        "#4938",
        "#4939",
        "#4940",
        "#4941",
        "#4942",
        "#4943",
        "#4944",
        "mode-set / corner-transfer",
        "stale-green runner-cache repair sweep",
        "matter-action/statistics no-go",
        "statistical-grain selector",
        "`DIRTY`",
        "UNSTABLE",
        "CLEAN",
        "No-Go Discipline Gate",
        "broad A2/S_l closure fails; narrowed source-strength normalization gauge firewall passes.",
        "Gate result: `PASS` for the narrowed firewall",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite normalization-gauge arithmetic")
    coords = coordinates()
    n = len(coords)
    audit.check("source coordinate set has 4^4 = 256 labels", n == 256)

    a = Fraction(3, 5)
    h = Fraction(7, 1)
    uniform_controls = {coord: a for coord in coords}
    total_strength = sum(uniform_controls.values(), Fraction(0))
    normalized = normalize(uniform_controls)
    audit.check("uniform unnormalized total strength is 256a", total_strength == 256 * a, f"total={total_strength}")
    audit.check("normalizing uniform positive controls gives total one", sum(normalized.values(), Fraction(0)) == 1)
    audit.check("uniform normalized singleton weight is exact 1/256", normalized[coords[0]] == Fraction(1, 256))

    big_h = n * a * h
    audit.check("overall source amplitude absorbs unnormalized total strength", big_h * Fraction(1, n) == h * a)
    audit.check("h*a differs from normalized singleton when h and a are not fixed", h * a != Fraction(1, n))

    lam = Fraction(11, 1)
    rescaled_h = h / lam
    rescaled_a = lam * a
    audit.check("positive rescaling leaves h*j coefficient invariant", rescaled_h * rescaled_a == h * a)

    lam_16 = Fraction(16, 1)
    audit.check(
        "lambda=16 maps 1/256 controls to 1/16 controls with inverse h rescale",
        h * Fraction(1, 256) == (h / lam_16) * Fraction(1, 16),
    )

    nonuniform_controls = {}
    for coord in coords[:128]:
        nonuniform_controls[coord] = Fraction(2, 1)
    for coord in coords[128:]:
        nonuniform_controls[coord] = Fraction(1, 1)
    nonuniform_norm = normalize(nonuniform_controls)
    audit.check("nonuniform positive vector has total strength 384", sum(nonuniform_controls.values(), Fraction(0)) == 384)
    audit.check("normalization alone gives a simplex point", sum(nonuniform_norm.values(), Fraction(0)) == 1)
    audit.check("normalization alone does not imply uniformity", nonuniform_norm[coords[0]] != nonuniform_norm[coords[-1]])
    audit.check("first nonuniform normalized weight is 1/192", nonuniform_norm[coords[0]] == Fraction(1, 192))
    audit.check("last nonuniform normalized weight is 1/384", nonuniform_norm[coords[-1]] == Fraction(1, 384))

    l2_uniform = Fraction(1, 16)
    audit.check("uniform 256-channel L2/RN source-unit coefficient is 1/16", n * l2_uniform * l2_uniform == 1)
    audit.check("L2/RN coefficient is 16 times the L1 singleton weight", l2_uniform / Fraction(1, 256) == 16)

    section("Authority boundary checks")
    source_control = read(SOURCE_CONTROL)
    source_strength = read(SOURCE_STRENGTH)
    attachment = read(ATTACHMENT)
    source_slot = read(SOURCE_SLOT)
    transfer = read(TRANSFER)
    source_measure = read(SOURCE_MEASURE)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("source-control note names J linearity", "J(j_A + j_B) = J(j_A) + J(j_B)" in source_control)
    audit.check("source-control note leaves total normalization open", "total normalization `mu(C) = 1`" in source_control)
    audit.check("source-strength note proves 1/256 only after mu(C)=1", "mu(C) = 1" in source_strength and "mu({c}) = 1/256" in source_strength)
    audit.check("attachment support names derivative insertion", "dS_lep/dj_c = h * B_lep * O_c" in attachment)
    audit.check("source-slot support names source map", "J(j) = sum_{c in C} j_c O_c" in source_slot)
    audit.check("transfer discriminator contrasts 1/16 and 1/256", "1/sqrt(256) = 1/16" in transfer and "1/256" in transfer)
    audit.check("RN theorem names Fisher norm and source unit", "Fisher norm" in source_measure and "source unit" in source_measure)
    audit.check("minimal axioms provide Record formation and exclude source/action", "Records form" in minimal and "source/action" in minimal_flat)
    audit.check("kinetic primitive excludes normalization and selector", "normalization" in kinetic and "selector" in kinetic)
    audit.check("scale primitive excludes dimensionless quantity", "does not supply any dimensionless quantity" in scale)
    audit.check("realized primitive excludes weighting and normalization", "weighting" in realized and "normalization rule" in realized)
    audit.check(
        "registry names approved premise nodes",
        all(name in registry for name in ["minimal_axioms", "kinetic_isotropy_primitive", "scale_reference_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is a full-cell",
        "No derivation that source controls are positive source strengths.",
        "No derivation of total normalization `mu(C) = 1`.",
        "No derivation that `S_l` reads normalized source weight.",
        "No derivation of tensor-frame relabeling symmetry as a physical source",
        "No derivation of the `256.08` precision correction.",
        "No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.",
        "No audit status change for any cited row.",
        "No new axiom, primitive, or admitted import.",
    ]
    for phrase in explicit_non_claims:
        audit.check(f"explicit non-claim present: {phrase}", phrase in note)

    forbidden_overclaims = [
        "This note derives `S_l = 1/256`",
        "This note derives hydrogen",
        "This note proves A2 closure",
        "source-control linearity closes A2/source normalization",
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
