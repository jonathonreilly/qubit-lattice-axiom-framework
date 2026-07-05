#!/usr/bin/env python3
"""Verifier for restricted tensor-frame support of the lepton 1/256 route.

This support runner checks a conditional finite-set theorem: if a physical
tensor-product matrix-unit source frame and L1 density semantics are supplied,
the uniform 1/256 density is invariant under tensor-frame relabelings. It does
not derive S_l, a charged-lepton mass, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
MATRIX = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md"
L1 = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md"
READOUT = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"


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


Coord = tuple[int, int, int, int]
Density = dict[Coord, Fraction]


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


def uniform_density(coords: list[Coord]) -> Density:
    return {coord: Fraction(1, len(coords)) for coord in coords}


def pushforward(mu: Density, mapping: dict[Coord, Coord]) -> Density:
    out = {coord: Fraction(0) for coord in mu}
    for coord, mass in mu.items():
        out[mapping[coord]] += mass
    return out


def is_uniform(mu: Density, value: Fraction) -> bool:
    return all(mass == value for mass in mu.values())


def slot_permutation_mapping(coords: list[Coord], perm: tuple[int, int, int, int]) -> dict[Coord, Coord]:
    return {coord: tuple(coord[i] for i in perm) for coord in coords}


def local_relabel_mapping(
    coords: list[Coord],
    relabels: tuple[tuple[int, int, int, int], tuple[int, int, int, int], tuple[int, int, int, int], tuple[int, int, int, int]],
) -> dict[Coord, Coord]:
    return {coord: tuple(relabels[slot][coord[slot]] for slot in range(4)) for coord in coords}


def index_to_coord(index: int) -> Coord:
    return (
        (index // 64) % 4,
        (index // 16) % 4,
        (index // 4) % 4,
        index % 4,
    )


def coord_to_index(coord: Coord) -> int:
    return coord[0] * 64 + coord[1] * 16 + coord[2] * 4 + coord[3]


def affine_coordinate_bijection(coords: list[Coord]) -> dict[Coord, Coord]:
    # Odd multiplier is coprime to 256, so this is a bijection of coordinate labels.
    return {coord: index_to_coord((73 * coord_to_index(coord) + 19) % 256) for coord in coords}


def marginal(mu: Density, slot: int) -> dict[int, Fraction]:
    out = {local: Fraction(0) for local in range(4)}
    for coord, mass in mu.items():
        out[coord[slot]] += mass
    return out


def coeff_average_sum_entries(entries: list[list[Fraction]]) -> Fraction:
    n = len(entries)
    return sum(sum(row, Fraction(0)) for row in entries) / (n * n)


def normalized_trace(entries: list[list[Fraction]]) -> Fraction:
    return sum(entries[i][i] for i in range(len(entries))) / len(entries)


def e00(n: int) -> list[list[Fraction]]:
    return [[Fraction(1 if i == 0 and j == 0 else 0) for j in range(n)] for i in range(n)]


def flat_projection(n: int) -> list[list[Fraction]]:
    return [[Fraction(1, n) for _ in range(n)] for _ in range(n)]


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("restricted tensor-frame support note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md",
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
        "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
        "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
        "docs/audit/data/axiom_premise_nodes.json",
    ]
    for rel in source_paths:
        audit.check(f"source path exists: {rel}", (ROOT / rel).exists())

    section("Required note content")
    required_phrases = [
        "Restricted Tensor-Frame Invariance Support",
        "supplied physical tensor-product matrix-unit source frame",
        "A = M_2(C)^tensor4 ~= M_16(C)",
        "C = {0,1,2,3}^4",
        "|C| = 4^4 = 256",
        "mu(c) = 1/256",
        "one-slot marginal",
        "slot permutations",
        "independent local relabelings",
        "S_4^4 semidirect S_4",
        "24^5 = 7,962,624",
        "arbitrary coordinate bijection",
        "not full `U(16)` covariance",
        "E_00 fixed-coordinate average",
        "flat conjugate fixed-coordinate avg",
        "A2.4 coefficient uniformity",
        "conditionall",
        "A2.3 physical tensor-frame selector: still missing",
        "A2.2 L1 source semantics: still missing",
        "No-Go Discipline Gate",
        "broad no-go fails; restricted tensor-frame support passes.",
    ]
    # The "conditionall" fragment deliberately catches conditionally/conditional wording.
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite tensor-frame arithmetic")
    coords = coordinates()
    mu = uniform_density(coords)
    expected = Fraction(1, 256)

    audit.check("coordinate set has 4^4 = 256 labels", len(coords) == 4**4 == 256)
    audit.check("uniform density assigns exact 1/256", is_uniform(mu, expected))
    audit.check("uniform density sums to one", sum(mu.values(), Fraction(0)) == 1)
    audit.check("product factor (1/4)^4 is exact 1/256", Fraction(1, 4) ** 4 == expected)

    for slot in range(4):
        m = marginal(mu, slot)
        audit.check(f"slot {slot} has four marginal labels", set(m) == {0, 1, 2, 3})
        audit.check(f"slot {slot} marginal is uniform 1/4", all(value == Fraction(1, 4) for value in m.values()))

    slot_perm = (2, 0, 3, 1)
    slot_push = pushforward(mu, slot_permutation_mapping(coords, slot_perm))
    audit.check("nontrivial slot permutation preserves support size", len(slot_push) == 256)
    audit.check("nontrivial slot permutation preserves uniform 1/256", is_uniform(slot_push, expected))

    relabels = (
        (1, 2, 3, 0),
        (0, 2, 1, 3),
        (3, 0, 1, 2),
        (2, 3, 0, 1),
    )
    local_push = pushforward(mu, local_relabel_mapping(coords, relabels))
    audit.check("independent local relabeling preserves support size", len(local_push) == 256)
    audit.check("independent local relabeling preserves uniform 1/256", is_uniform(local_push, expected))

    affine_map = affine_coordinate_bijection(coords)
    audit.check("affine coordinate map is bijective on 256 labels", len(set(affine_map.values())) == 256)
    affine_push = pushforward(mu, affine_map)
    audit.check("arbitrary coordinate bijection preserves support size", len(affine_push) == 256)
    audit.check("arbitrary coordinate bijection preserves uniform 1/256", is_uniform(affine_push, expected))

    audit.check("tensor-frame relabeling group size is 24^5", math.factorial(4) ** 5 == 7_962_624)

    section("Full U(16) boundary contrast")
    n = 16
    fixed = coeff_average_sum_entries(e00(n))
    flat_avg = coeff_average_sum_entries(flat_projection(n))
    fixed_trace = normalized_trace(e00(n))
    flat_trace = normalized_trace(flat_projection(n))
    audit.check("E00 fixed-coordinate average is 1/256", fixed == Fraction(1, 256))
    audit.check("flat conjugate fixed-coordinate average is 1/16", flat_avg == Fraction(1, 16))
    audit.check("normalized traces remain 1/16", fixed_trace == flat_trace == Fraction(1, 16))
    audit.check("full unitary mixing changes fixed-coordinate density", fixed != flat_avg)

    section("Source-authority boundary checks")
    matrix = read(MATRIX)
    l1 = read(L1)
    readout = read(READOUT)
    minimal = flat(read(MINIMAL)).lower()
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    scale = flat(read(SCALE)).lower()
    registry = read(REGISTRY)

    audit.check("basis-selector discriminator names full inner-automorphism firewall", "full inner-automorphism" in matrix and "basis/source-frame selector" in matrix)
    audit.check("L1 discriminator names L1 and L2 split", "L1 algebra-coordinate density" in l1 and "L2 / Hilbert-Schmidt / Fisher" in l1)
    audit.check("readout discriminator names projection and matrix-unit alternatives", "projection/Born trace" in readout and "matrix-unit coordinate" in readout)
    audit.check("minimal axioms exclude privileged possibility", "no possibility is privileged" in minimal and "source/action" in minimal)
    audit.check("kinetic primitive excludes selector/readout bridge", "selector" in kinetic and "readout bridge" in kinetic)
    audit.check("realized primitive excludes measure and normalization", "measure" in realized and "normalization rule" in realized)
    audit.check("scale primitive excludes dimensionless suppression", "dimensionless" in scale and "mass ratio" in scale)
    audit.check(
        "primitive registry names approved primitive nodes",
        all(p in registry for p in ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]),
    )

    section("Non-claim boundary")
    explicit_non_claims = [
        "No derivation of `S_l = 1/256`.",
        "No derivation that the charged-lepton scalar source uses this tensor-product",
        "No derivation that the source/action coefficient uses L1 density semantics.",
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
        "This note proves the charged-lepton scalar source uses this tensor-product",
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
