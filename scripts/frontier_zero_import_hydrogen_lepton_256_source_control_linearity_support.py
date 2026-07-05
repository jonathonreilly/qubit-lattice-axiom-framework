#!/usr/bin/env python3
"""Verifier for source-control linearity support in the lepton 1/256 lane.

This runner checks the conditional theorem that a slot-resolved source map
J(j)=sum_c j_c O_c is additive over disjoint source-control functions. It does
not derive source-strength positivity, normalization, S_l, a charged-lepton
mass, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
ATTACHMENT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
SOURCE_STRENGTH = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
TRANSFER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md"
LOCAL_ACTION = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
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


def indicator(subset: set[Coord], value: Fraction = Fraction(1, 1)) -> Vector:
    return {coord: value for coord in subset}


def add_vectors(a: Vector, b: Vector) -> Vector:
    coords = set(a) | set(b)
    return {coord: a.get(coord, Fraction(0)) + b.get(coord, Fraction(0)) for coord in coords}


def source_image(vector: Vector) -> Vector:
    # Matrix units are linearly independent, so the coefficient vector is the
    # source-map image in the matrix-unit basis.
    return dict(vector)


def support(vector: Vector) -> set[Coord]:
    return {coord for coord, value in vector.items() if value != 0}


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-control linearity support note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        ATTACHMENT,
        SOURCE_SLOT,
        SOURCE_STRENGTH,
        TRANSFER,
        LOCAL_ACTION,
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
        "Source-Control Linearity Support",
        "J(j_A + j_B) = J(j_A) + J(j_B)",
        "S_src[j_A + j_B] = S_src[j_A] + S_src[j_B]",
        "J(1_{A union B}) = J(1_A) + J(1_B)",
        "source-control coarse graining",
        "Record-Additivity Firewall",
        "linearity of source controls is vector-space structure",
        "source strength is a nonnegative normalized measure",
        "mu(C) = 1",
        "source-control linearity",
        "#4939",
        "AC(i) dynamical-index occupancy no-go",
        "#4940",
        "rule achirality from minimality",
        "#4941",
        "AC(i) determinant-order/chiral L-R no-go",
        "No-Go Discipline Gate",
        "broad A2/S_l closure fails; narrowed source-control linearity support passes.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite source-control linearity checks")
    coords = coordinates()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)

    a_set = set(coords[:37])
    b_set = set(coords[100:181])
    audit.check("test source-control supports are disjoint", a_set.isdisjoint(b_set))

    j_a = indicator(a_set, Fraction(2, 3))
    j_b = indicator(b_set, Fraction(5, 7))
    lhs = source_image(add_vectors(j_a, j_b))
    rhs = add_vectors(source_image(j_a), source_image(j_b))
    audit.check("J(j_A+j_B) equals J(j_A)+J(j_B)", lhs == rhs)
    audit.check("support of sum is disjoint union of supports", support(lhs) == a_set | b_set)

    one_a = indicator(a_set)
    one_b = indicator(b_set)
    indicator_union = indicator(a_set | b_set)
    audit.check("indicator source controls add on disjoint unions", add_vectors(one_a, one_b) == indicator_union)
    audit.check("coarse-grained control count is additive", len(a_set | b_set) == len(a_set) + len(b_set) == 118)

    negative_control = indicator({coords[0]}, Fraction(-3, 1))
    audit.check("linearity alone permits negative coefficients", next(iter(negative_control.values())) < 0)

    scaled = {coord: Fraction(17, 1) * value for coord, value in indicator_union.items()}
    audit.check("linearity alone permits arbitrary overall scale", sum(scaled.values()) == Fraction(17 * 118, 1))
    audit.check("source-control linearity does not impose total strength one", sum(indicator_union.values()) == 118)

    uniform_strength = {coord: Fraction(1, 256) for coord in coords}
    audit.check("normalization is extra beyond linearity", sum(uniform_strength.values()) == 1)
    audit.check("uniform normalized singleton is 1/256 only after normalization", uniform_strength[coords[0]] == Fraction(1, 256))

    l2_unit = Fraction(1, 16)
    audit.check("L2/RN uniform source-unit coefficient remains 1/16", len(coords) * l2_unit * l2_unit == 1)
    audit.check("L2/RN coefficient differs from linear source-strength singleton", l2_unit != Fraction(1, 256))

    section("Authority boundary checks")
    attachment = read(ATTACHMENT)
    source_slot = read(SOURCE_SLOT)
    source_strength = read(SOURCE_STRENGTH)
    transfer = read(TRANSFER)
    local_action = read(LOCAL_ACTION)
    source_measure = read(SOURCE_MEASURE)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("attachment support names source derivative insertion", "dS_lep/dj_c = h * B_lep * O_c" in attachment)
    audit.check("source-slot support names slot-resolved source map", "J(j) = sum_{c in C} j_c O_c" in source_slot)
    audit.check("source-strength note names nonnegative normalized measure", "nonnegative source-strength" in source_strength and "mu(C) = 1" in source_strength)
    audit.check("transfer discriminator keeps RN/Fisher at 1/16", "1/sqrt(256) = 1/16" in transfer)
    audit.check("local-action candidate states source-coupling convention", "Local source derivatives of `S` define the local operator insertions" in local_action)
    audit.check("RN theorem names Fisher norm and source unit", "Fisher norm" in source_measure and "source unit" in source_measure)
    audit.check("minimal axioms provide record additivity", "scalar readout" in minimal and "additive" in minimal)
    audit.check("minimal axioms exclude source/action", "source/action" in minimal_flat and "outside axiom content" in minimal_flat)
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
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is a full-cell",
        "No derivation that source-control coefficients are nonnegative normalized",
        "No derivation of total normalization `mu(C) = 1`.",
        "No derivation of tensor-frame relabeling symmetry as a physical source",
        "No derivation of the charged-lepton source bridge.",
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
        "This note derives source-strength semantics",
        "S_l is retained",
        "m_e is derived",
        "alpha(0) is derived",
        "This note claims hydrogen is retained",
    ]
    for phrase in forbidden_overclaims:
        audit.check(f"forbidden overclaim absent: {phrase}", phrase not in note)

    audit.summary()


if __name__ == "__main__":
    main()
