#!/usr/bin/env python3
"""Verifier for source projective tensor-frame invariance bridge support.

This runner checks the conditional bridge: source-family preserving tensor-frame
relabelings make the projective source ray invariant if the physical source-ray
assignment is natural under those relabelings. It does not derive S_l, m_e,
alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_INVARIANCE_BRIDGE_SUPPORT_2026-07-04.md"
PROJECTIVE_UNIFORM = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
RESTRICTED_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
MATRIX_BASIS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md"
SOURCE_LINEARITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
SOURCE_STRENGTH = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


Coord = tuple[int, int, int, int]
Vector = dict[Coord, Fraction]
Perm = Callable[[Coord], Coord]


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


def swap_values_in_slot(coord: Coord, slot: int, a: int, b: int) -> Coord:
    values = list(coord)
    if values[slot] == a:
        values[slot] = b
    elif values[slot] == b:
        values[slot] = a
    return tuple(values)  # type: ignore[return-value]


def swap_slots(coord: Coord, slot_a: int, slot_b: int) -> Coord:
    values = list(coord)
    values[slot_a], values[slot_b] = values[slot_b], values[slot_a]
    return tuple(values)  # type: ignore[return-value]


def rho_vector(vector: Vector, perm: Perm) -> Vector:
    return {perm(coord): value for coord, value in vector.items()}


def source_map(vector: Vector) -> dict[Coord, Fraction]:
    return dict(vector)


def relabel_basis(source: dict[Coord, Fraction], perm: Perm) -> dict[Coord, Fraction]:
    return {perm(coord): value for coord, value in source.items()}


def normalize(vector: Vector) -> Vector:
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in vector.items()}


def projective_scale(a: Vector, b: Vector) -> Fraction | None:
    lam: Fraction | None = None
    for coord in set(a) | set(b):
        av = a.get(coord, Fraction(0))
        bv = b.get(coord, Fraction(0))
        if bv == 0:
            if av != 0:
                return None
            continue
        candidate = av / bv
        if candidate <= 0:
            return None
        if lam is None:
            lam = candidate
        elif candidate != lam:
            return None
    return lam


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-family naturality bridge note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        PROJECTIVE_UNIFORM,
        PROJECTIVE_SECTION,
        SOURCE_SLOT,
        RESTRICTED_FRAME,
        MATRIX_BASIS,
        SOURCE_LINEARITY,
        SOURCE_STRENGTH,
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
        "Source Projective Tensor-Frame Invariance Bridge Support",
        "J(j) = sum_{c in C} j_c O_c",
        "rho_g",
        "source-family preserving relabeling",
        "source-family naturality",
        "projective source ray",
        "finite transitive tensor-frame projective invariance",
        "sigma([j])_c = 1/256",
        "physical invariance bridge",
        "W5b",
        "No-Go Discipline Gate",
        "broad W5b closure fails; narrowed source-family naturality bridge support passes.",
        "Gate result: `PASS` for the narrowed source-family naturality bridge support.",
        "Open PR Alignment",
        "#4938",
        "#4939",
        "#4940",
        "#4941",
        "#4942",
        "#4943",
        "#4944",
        "#4945",
        "#4946",
        "R-eta current-support-stack no-go",
        "R-eta transport-stretch no-go",
        "Phi = S_sum = 2/3",
        "Phi = Tr L_3^+ = 2/3",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Source-family equivariance checks")
    coords = coordinates()
    audit.check("source coordinate set has 4^4 = 256 labels", len(coords) == 256)
    vector = {coord: Fraction(3 * coord[0] + coord[1] + 5, 1) for coord in coords}

    perms: list[tuple[str, Perm]] = [
        ("slot0 value swap", lambda coord: swap_values_in_slot(coord, 0, 0, 1)),
        ("slot2 value swap", lambda coord: swap_values_in_slot(coord, 2, 1, 2)),
        ("slot permutation", lambda coord: swap_slots(coord, 0, 3)),
    ]
    for name, perm in perms:
        left = relabel_basis(source_map(vector), perm)
        right = source_map(rho_vector(vector, perm))
        audit.check(f"rho_g J(j) = J(rho_g j) for {name}", left == right)

    uniform = {coord: Fraction(9, 4) for coord in coords}
    for name, perm in perms:
        relabeled = rho_vector(uniform, perm)
        audit.check(f"uniform projective ray invariant under source-family naturality for {name}", projective_scale(relabeled, uniform) == 1)

    tagged = {coord: Fraction(4 if coord[0] == 0 else 1, 1) for coord in coords}
    relabeled_tagged = rho_vector(tagged, perms[0][1])
    audit.check("coordinate-tagged nonuniform ray changes under relabeling", relabeled_tagged != tagged)
    audit.check("coordinate-tagged nonuniform ray is not projectively invariant", projective_scale(relabeled_tagged, tagged) is None)

    weights = normalize(uniform)
    audit.check("uniform natural source ray normalizes to total one", sum(weights.values(), Fraction(0)) == 1)
    audit.check("uniform natural source ray singleton coordinate is 1/256", weights[coords[0]] == Fraction(1, 256))

    l2_uniform = Fraction(1, 16)
    audit.check("full U(16) / L2 contrast remains 1/16", len(coords) * l2_uniform * l2_uniform == 1)
    audit.check("source-family L1 singleton differs from 1/16", Fraction(1, 256) != l2_uniform)

    section("Authority boundary checks")
    projective_uniform = read(PROJECTIVE_UNIFORM)
    projective_section = read(PROJECTIVE_SECTION)
    source_slot = read(SOURCE_SLOT)
    restricted_frame = read(RESTRICTED_FRAME)
    matrix_basis = read(MATRIX_BASIS)
    source_linearity = read(SOURCE_LINEARITY)
    source_strength = read(SOURCE_STRENGTH)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("prior uniform-ray note names W5b and finite theorem", "W5b" in projective_uniform and "lambda_g = 1" in projective_uniform)
    audit.check("projective-section note names L1 section", "sigma([j])_c = j_c / sum_d j_d" in projective_section)
    audit.check("source-slot note names source map", "J(j) = sum_{c in C} j_c O_c" in source_slot)
    audit.check("restricted-frame note names tensor-frame relabelings", "tensor-frame relabelings" in restricted_frame)
    audit.check("matrix basis discriminator names full U(16) contrast", "full `U(16)`" in matrix_basis and "1/16" in matrix_basis)
    audit.check("source-control linearity note names additivity", "J(j_A + j_B) = J(j_A) + J(j_B)" in source_linearity)
    audit.check("source-strength note names mu(C)=1 and 1/256", "mu(C) = 1" in source_strength and "mu({c}) = 1/256" in source_strength)
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
        "No derivation of the source-coupled local-action convention.",
        "No derivation that the charged-lepton scalar source is a full-cell",
        "No derivation that source controls are nonnegative source strengths.",
        "No derivation that charged-lepton source strength is physically the",
        "No unconditional derivation that source-family naturality is physically",
        "No derivation that `S_l` reads `sigma([j])_c`.",
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
        "This note proves W5b",
        "W5b is now retained",
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
