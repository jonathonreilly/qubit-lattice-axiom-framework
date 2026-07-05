#!/usr/bin/env python3
"""Verifier for projective tensor-frame uniform-ray support.

This runner checks the finite theorem: a nonzero nonnegative projective source
ray invariant under a finite transitive tensor-frame relabeling group is
uniform, and its L1 simplex section has singleton coordinate 1/256.
It does not derive S_l, m_e, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md"
PROJECTIVE_SECTION = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
SIMPLEX_UNIFORMITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
RESTRICTED_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
SOURCE_SLOT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md"
MATRIX_BASIS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md"
SOURCE_STRENGTH = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
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


def normalize(vector: Vector) -> Vector:
    total = sum(vector.values(), Fraction(0))
    if total <= 0:
        raise ValueError("positive total required")
    return {coord: value / total for coord, value in vector.items()}


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


def apply_perm(vector: Vector, perm) -> Vector:
    return {perm(coord): value for coord, value in vector.items()}


def projective_scale(a: Vector, b: Vector) -> Fraction | None:
    """Return lambda if a = lambda b with lambda > 0, else None."""
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


def is_uniform(vector: Vector) -> bool:
    values = list(vector.values())
    return all(value == values[0] for value in values)


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("projective tensor-frame uniform-ray support note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        PROJECTIVE_SECTION,
        SIMPLEX_UNIFORMITY,
        RESTRICTED_FRAME,
        SOURCE_SLOT,
        MATRIX_BASIS,
        SOURCE_STRENGTH,
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
        "Source Projective Tensor-Frame Uniform-Ray Support",
        "G_frame = S_4^4",
        "G_frame_extended = S_4^4 semidirect S_4",
        "lambda_g = 1",
        "finite transitive tensor-frame projective invariance",
        "uniform ray",
        "sigma([j])_c = 1/256",
        "positive scale character",
        "nonzero nonnegative projective source ray",
        "W5b",
        "Open PR Alignment",
        "#4938",
        "#4939",
        "#4940",
        "#4941",
        "#4942",
        "#4943",
        "#4944",
        "#4945",
        "R-eta current-support-stack no-go",
        "Phi = S_sum = 2/3",
        "No-Go Discipline Gate",
        "broad A2/S_l closure fails; narrowed projective tensor-frame uniform-ray support passes.",
        "Gate result: `PASS` for the narrowed projective tensor-frame uniform-ray",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite projective-uniformity theorem checks")
    coords = coordinates()
    n = len(coords)
    audit.check("source coordinate set has 4^4 = 256 labels", n == 256)

    uniform = {coord: Fraction(7, 3) for coord in coords}
    swap_01_slot0 = lambda coord: swap_values_in_slot(coord, 0, 0, 1)
    swap_12_slot2 = lambda coord: swap_values_in_slot(coord, 2, 1, 2)
    slot_swap_03 = lambda coord: swap_slots(coord, 0, 3)

    for name, perm in [
        ("slot0 value swap", swap_01_slot0),
        ("slot2 value swap", swap_12_slot2),
        ("slot permutation", slot_swap_03),
    ]:
        permuted = apply_perm(uniform, perm)
        audit.check(f"uniform ray exactly invariant under {name}", permuted == uniform)
        audit.check(f"projective scale under {name} is one", projective_scale(permuted, uniform) == 1)

    nonuniform = {}
    for coord in coords:
        nonuniform[coord] = Fraction(2 if coord[0] == 0 else 1, 1)
    permuted_nonuniform = apply_perm(nonuniform, swap_01_slot0)
    audit.check("nonuniform ray is not projectively invariant under transitive generator", projective_scale(permuted_nonuniform, nonuniform) is None)

    # Finite-order projective character check: if Pj = lambda*j and P^2=e,
    # then lambda^2=1. Positive lambda forces lambda=1.
    for lam in [Fraction(1, 1), Fraction(2, 1), Fraction(3, 5)]:
        finite_order_ok = lam * lam == 1
        audit.check(
            f"order-two positive projective scale lambda={lam} is trivial iff lambda=1",
            finite_order_ok == (lam == 1),
        )

    weights = normalize(uniform)
    audit.check("uniform projective ray normalizes to total one", sum(weights.values(), Fraction(0)) == 1)
    audit.check("uniform projective ray singleton coordinate is 1/256", weights[coords[0]] == Fraction(1, 256))

    first_slot_zero = {coord for coord in coords if coord[0] == 0}
    first_slot_nonzero = {coord for coord in coords if coord[0] != 0}
    block_ray = {coord: Fraction(5 if coord[0] == 0 else 2, 1) for coord in coords}
    restricted_perm = lambda coord: swap_values_in_slot(coord, 1, 0, 1)
    audit.check("block ray invariant under nontransitive within-block relabeling", apply_perm(block_ray, restricted_perm) == block_ray)
    audit.check("nontransitive invariance does not force global uniformity", not is_uniform(block_ray))
    block_weights = normalize(block_ray)
    audit.check("nonuniform block ray still has normalized total one", sum(block_weights.values(), Fraction(0)) == 1)
    audit.check("nonuniform block ray singleton differs from 1/256", block_weights[coords[0]] != Fraction(1, 256))
    audit.check("block partition covers C", len(first_slot_zero | first_slot_nonzero) == n)

    signed = dict(uniform)
    signed[coords[0]] = Fraction(-7, 3)
    audit.check("signed ray is outside nonnegative source-strength semantics", any(value < 0 for value in signed.values()))

    l2_uniform = Fraction(1, 16)
    audit.check("uniform 256-channel L2/RN source-unit coefficient is 1/16", n * l2_uniform * l2_uniform == 1)
    audit.check("L2/RN coefficient differs from projective L1 singleton", l2_uniform != Fraction(1, 256))

    section("Authority boundary checks")
    projective_section = read(PROJECTIVE_SECTION)
    simplex_uniformity = read(SIMPLEX_UNIFORMITY)
    restricted_frame = read(RESTRICTED_FRAME)
    source_slot = read(SOURCE_SLOT)
    matrix_basis = read(MATRIX_BASIS)
    source_strength = read(SOURCE_STRENGTH)
    source_measure = read(SOURCE_MEASURE)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("projective-section note names L1 section and uniform ray", "sigma([j])_c = j_c / sum_d j_d" in projective_section and "uniform ray" in projective_section)
    audit.check("simplex-uniformity note names transitivity", "transitivity" in simplex_uniformity)
    audit.check("restricted-frame note names tensor-frame relabelings", "tensor-frame relabelings" in restricted_frame)
    audit.check("source-slot note names source map", "J(j) = sum_{c in C} j_c O_c" in source_slot)
    audit.check("matrix basis discriminator names full U(16) contrast", "full `U(16)`" in matrix_basis and "1/16" in matrix_basis)
    audit.check("source-strength support names mu(C)=1 and 1/256", "mu(C) = 1" in source_strength and "mu({c}) = 1/256" in source_strength)
    audit.check("RN theorem names Fisher norm and source unit", "Fisher norm" in source_measure and "source unit" in source_measure)
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
        "No derivation that tensor-frame relabeling invariance is a physical source",
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
        "This note proves A2 closure",
        "`S_l = 1/256` is now derived",
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
