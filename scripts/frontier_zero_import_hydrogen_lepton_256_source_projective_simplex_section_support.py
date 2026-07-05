#!/usr/bin/env python3
"""Verifier for the projective-simplex section support note.

This runner checks the finite theorem that a nonzero nonnegative source ray has
a well-defined L1 simplex representative, and that the uniform 256-coordinate
ray gives singleton weight 1/256. It does not derive S_l, m_e, alpha(0), or
hydrogen spectroscopy.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md"
NORMALIZATION_GAUGE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md"
SOURCE_CONTROL = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md"
SOURCE_STRENGTH = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md"
UNIFORMITY = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
RESTRICTED_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
TRANSFER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md"
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
        raise ValueError("projective simplex section needs positive total")
    return {coord: value / total for coord, value in vector.items()}


def measure(weights: Vector, subset: set[Coord]) -> Fraction:
    return sum((weights.get(coord, Fraction(0)) for coord in subset), Fraction(0))


def permute_slots(coord: Coord) -> Coord:
    return (coord[1], coord[0], coord[3], coord[2])


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("projective-simplex section support note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        NOTE,
        NORMALIZATION_GAUGE,
        SOURCE_CONTROL,
        SOURCE_STRENGTH,
        UNIFORMITY,
        RESTRICTED_FRAME,
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
        "Source Projective-Simplex Section Support",
        "P_+(C) = (R_{\\ge 0}^C \\ {0}) / R_{>0}",
        "sigma([j])_c = j_c / sum_d j_d",
        "sum_c sigma([j])_c = 1",
        "mu_[j](C) = 1",
        "sigma([1])_c = 1/256",
        "projective positive source ray",
        "L1 simplex section",
        "gauge section",
        "uniform ray",
        "positive-rescaling gauge obstruction",
        "S_l reads",
        "Open PR Alignment",
        "#4938",
        "#4939",
        "#4940",
        "#4941",
        "#4942",
        "#4943",
        "#4944",
        "matter-action/statistics no-go",
        "statistical-grain shortcut",
        "No-Go Discipline Gate",
        "broad A2/S_l closure fails; narrowed projective-simplex section support passes.",
        "Gate result: `PASS` for the narrowed projective-simplex section support",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", " ".join(phrase.split()) in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Projective simplex arithmetic")
    coords = coordinates()
    n = len(coords)
    audit.check("source coordinate set has 4^4 = 256 labels", n == 256)

    uniform = {coord: Fraction(3, 5) for coord in coords}
    uniform_weights = normalize(uniform)
    audit.check("uniform ray normalizes to total one", sum(uniform_weights.values(), Fraction(0)) == 1)
    audit.check("uniform ray singleton weight is 1/256", uniform_weights[coords[0]] == Fraction(1, 256))

    lam = Fraction(17, 3)
    rescaled_uniform = {coord: lam * value for coord, value in uniform.items()}
    audit.check("L1 section is invariant under positive source-control rescaling", normalize(rescaled_uniform) == uniform_weights)

    h = Fraction(11, 1)
    audit.check(
        "source term coefficient is invariant when h rescales inversely",
        h * uniform[coords[0]] == (h / lam) * rescaled_uniform[coords[0]],
    )

    nonuniform: Vector = {}
    for coord in coords[:128]:
        nonuniform[coord] = Fraction(2, 1)
    for coord in coords[128:]:
        nonuniform[coord] = Fraction(1, 1)
    nonuniform_weights = normalize(nonuniform)
    audit.check("nonuniform positive ray has total raw strength 384", sum(nonuniform.values(), Fraction(0)) == 384)
    audit.check("nonuniform ray normalizes to total one", sum(nonuniform_weights.values(), Fraction(0)) == 1)
    audit.check("nonuniform ray does not force singleton 1/256", nonuniform_weights[coords[0]] != Fraction(1, 256))
    audit.check("first nonuniform normalized weight is 1/192", nonuniform_weights[coords[0]] == Fraction(1, 192))
    audit.check("last nonuniform normalized weight is 1/384", nonuniform_weights[coords[-1]] == Fraction(1, 384))

    first_block = set(coords[:64])
    second_block = set(coords[64:128])
    audit.check("test blocks are disjoint", first_block.isdisjoint(second_block))
    audit.check(
        "normalized weights are finitely additive on disjoint blocks",
        measure(nonuniform_weights, first_block | second_block)
        == measure(nonuniform_weights, first_block) + measure(nonuniform_weights, second_block),
    )
    audit.check("uniform 64-coordinate block has source strength 1/4", measure(uniform_weights, first_block) == Fraction(1, 4))

    permuted_uniform = {permute_slots(coord): value for coord, value in uniform.items()}
    audit.check("uniform ray is fixed by slot permutation after normalization", normalize(permuted_uniform) == uniform_weights)

    signed = dict(uniform)
    signed[coords[0]] = Fraction(-1, 1)
    audit.check("signed control vector is outside nonnegative source-strength cone", any(value < 0 for value in signed.values()))

    zero = {coord: Fraction(0) for coord in coords}
    try:
        normalize(zero)
        zero_rejected = False
    except ValueError:
        zero_rejected = True
    audit.check("zero vector has no projective simplex section", zero_rejected)

    l2_uniform = Fraction(1, 16)
    audit.check("uniform 256-channel L2/RN source-unit coefficient is 1/16", n * l2_uniform * l2_uniform == 1)
    audit.check("L2/RN coefficient differs from projective L1 singleton", l2_uniform != Fraction(1, 256))

    section("Authority boundary checks")
    normalization_gauge = read(NORMALIZATION_GAUGE)
    source_control = read(SOURCE_CONTROL)
    source_strength = read(SOURCE_STRENGTH)
    uniformity = read(UNIFORMITY)
    restricted_frame = read(RESTRICTED_FRAME)
    transfer = read(TRANSFER)
    source_measure = read(SOURCE_MEASURE)
    minimal = read(MINIMAL)
    kinetic = read(KINETIC)
    scale = read(SCALE)
    realized = read(REALIZED)
    registry = read(REGISTRY)
    minimal_flat = flat(minimal).lower()

    audit.check("normalization gauge firewall names positive rescaling", "(h, j) -> (h/lambda, lambda j)" in normalization_gauge)
    audit.check("source-control support names linearity", "J(j_A + j_B) = J(j_A) + J(j_B)" in source_control)
    audit.check("source-strength support names mu(C)=1 and 1/256", "mu(C) = 1" in source_strength and "mu({c}) = 1/256" in source_strength)
    audit.check("uniformity support names simplex normalization and transitivity", "simplex normalization" in uniformity and "transitivity" in uniformity)
    audit.check("restricted frame support names tensor-frame relabelings", "tensor-frame relabelings" in restricted_frame)
    audit.check("transfer discriminator keeps RN/Fisher at 1/16", "1/sqrt(256) = 1/16" in transfer)
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
        "No derivation that tensor-frame symmetry forces the uniform source ray.",
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
        "`1/256` is now derived for `S_l`",
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
