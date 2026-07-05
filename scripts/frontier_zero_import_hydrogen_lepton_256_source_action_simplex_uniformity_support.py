#!/usr/bin/env python3
"""Verifier for source-action simplex uniformity support in the lepton 1/256 lane.

This support runner checks the finite theorem: a simplex-normalized linear
action coefficient over the 256 tensor-frame coordinates, invariant under
local coordinate relabelings, is uniquely 1/256. It does not derive S_l,
a charged-lepton mass, alpha(0), or hydrogen spectroscopy.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md"
TRANSFER = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md"
TENSOR_FRAME = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md"
BASIS = ROOT / "docs" / "ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md"
SOURCE_MEASURE = ROOT / "docs" / "SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md"
LOCAL_ACTION = ROOT / "docs" / "OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md"
MINIMAL = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
KINETIC = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
REALIZED = ROOT / "docs" / "REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SCALE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"


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


def swap_local(coord: Coord, slot: int, a: int, b: int) -> Coord:
    items = list(coord)
    if items[slot] == a:
        items[slot] = b
    elif items[slot] == b:
        items[slot] = a
    return tuple(items)  # type: ignore[return-value]


def swap_slots(coord: Coord, i: int, j: int) -> Coord:
    items = list(coord)
    items[i], items[j] = items[j], items[i]
    return tuple(items)  # type: ignore[return-value]


def orbit_count(coords: list[Coord], generators: list[dict[Coord, Coord]]) -> int:
    parent = {coord: coord for coord in coords}

    def find(coord: Coord) -> Coord:
        while parent[coord] != coord:
            parent[coord] = parent[parent[coord]]
            coord = parent[coord]
        return coord

    def union(a: Coord, b: Coord) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for generator in generators:
        for coord, image in generator.items():
            union(coord, image)

    return len({find(coord) for coord in coords})


def local_swap_generators(coords: list[Coord]) -> list[dict[Coord, Coord]]:
    return [
        {coord: swap_local(coord, slot, a, b) for coord in coords}
        for slot in range(4)
        for a, b in [(0, 1), (1, 2), (2, 3)]
    ]


def slot_swap_generators(coords: list[Coord]) -> list[dict[Coord, Coord]]:
    return [
        {coord: swap_slots(coord, i, j) for coord in coords}
        for i, j in [(0, 1), (1, 2), (2, 3)]
    ]


def local_permutation_sending(source: Coord, target: Coord) -> tuple[tuple[int, int, int, int], ...]:
    perms: list[tuple[int, int, int, int]] = []
    for src_value, dst_value in zip(source, target):
        perm = list(range(4))
        perm[src_value], perm[dst_value] = perm[dst_value], perm[src_value]
        perms.append(tuple(perm))
    return tuple(perms)


def apply_local_permutation(coord: Coord, perms: tuple[tuple[int, int, int, int], ...]) -> Coord:
    return tuple(perms[slot][coord[slot]] for slot in range(4))  # type: ignore[return-value]


def slot_permutation_orbit_representatives(coords: list[Coord]) -> set[Coord]:
    return {tuple(sorted(coord)) for coord in coords}  # type: ignore[return-value]


def main() -> None:
    audit = Audit()

    section("File and source-surface checks")
    audit.check("source-action simplex uniformity note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    note = read(NOTE)
    note_flat = flat(note)

    source_paths = [
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md",
        "docs/ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md",
        "docs/SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md",
        "docs/OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md",
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
        "Source-Action Simplex Uniformity Support",
        "S_src = h * sum_{c in C} w_c O_c",
        "w_c >= 0",
        "sum_{c in C} w_c = 1",
        "G = S_4^4",
        "transitively on `C`",
        "w_* = 1/256",
        "slot permutations only `S_4`",
        "35 orbits",
        "local coordinate relabeling symmetry",
        "A2.4 coefficient uniformity",
        "#4932",
        "No-Go Discipline Gate",
        "broad no-go fails; narrowed source-action simplex uniformity support passes.",
    ]
    for phrase in required_phrases:
        audit.check(f"required phrase present: {phrase}", phrase in note_flat)

    for marker in ["N1 -", "N2 -", "N3 -", "N4 -", "N5 -", "N6 -", "N7 -", "N8 -"]:
        audit.check(f"no-go discipline marker present: {marker}", marker in note)

    section("Finite transitivity and orbit checks")
    coords = coordinates()
    audit.check("coordinate set has 4^4 = 256 labels", len(coords) == 256)

    local_generators = local_swap_generators(coords)
    slot_generators = slot_swap_generators(coords)
    audit.check("local relabeling generators collapse to one orbit", orbit_count(coords, local_generators) == 1)
    audit.check("tensor-frame relabeling generators collapse to one orbit", orbit_count(coords, local_generators + slot_generators) == 1)
    audit.check("slot-only generators do not collapse to one orbit", orbit_count(coords, slot_generators) == 35)
    audit.check("slot-only orbit representatives match combinations with repetition", len(slot_permutation_orbit_representatives(coords)) == len(list(combinations_with_replacement(range(4), 4))) == 35)

    examples = [((0, 0, 0, 0), (3, 2, 1, 0)), ((1, 2, 3, 0), (0, 0, 0, 0)), ((3, 1, 0, 2), (2, 3, 1, 1))]
    for source, target in examples:
        perms = local_permutation_sending(source, target)
        audit.check(f"local permutations send {source} to {target}", apply_local_permutation(source, perms) == target)

    section("Simplex coefficient arithmetic")
    coefficient = Fraction(1, len(coords))
    audit.check("single-orbit simplex coefficient is exact 1/256", coefficient == Fraction(1, 256))
    audit.check("256 copies of 1/256 sum to one", len(coords) * coefficient == 1)
    audit.check("L2/RN invariant unit coefficient is 1/16", Fraction(1, 16) * Fraction(1, 16) * len(coords) == 1)
    audit.check("L2/RN coefficient is 16 times simplex coefficient", Fraction(1, 16) / coefficient == 16)

    distinguished = (0, 0, 0, 0)
    counter_weights = defaultdict(lambda: Fraction(1, 510))
    counter_weights[distinguished] = Fraction(1, 2)
    counter_sum = sum(counter_weights[coord] for coord in coords)
    audit.check("without transitivity, nonuniform normalized weights exist", counter_sum == 1 and counter_weights[distinguished] != coefficient)

    section("Source-authority boundary checks")
    transfer = read(TRANSFER)
    tensor_frame = read(TENSOR_FRAME)
    basis = read(BASIS)
    source_measure = read(SOURCE_MEASURE)
    local_action = read(LOCAL_ACTION)
    minimal = flat(read(MINIMAL)).lower()
    registry = read(REGISTRY)
    kinetic = read(KINETIC)
    realized = read(REALIZED)
    scale = flat(read(SCALE)).lower()

    audit.check("transfer discriminator names simplex versus source unit", "linear action simplex density" in transfer and "1/sqrt(256) = 1/16" in transfer)
    audit.check("tensor-frame note names relabeling support", "uniform coefficient 1/256 is invariant" in tensor_frame and "coordinate bijections" in tensor_frame)
    audit.check("basis selector keeps full U(16) firewall", "full inner automorphism" in basis or "full inner-automorphism" in basis)
    audit.check("RN source-measure theorem names Fisher norm lambda squared", "Fisher norm `lambda^2`" in source_measure)
    audit.check("local-action note is open-gate convention candidate", "open_gate" in local_action and "source-coupled local-action convention" in local_action)
    audit.check("minimal axioms exclude source/action and observable bridges", "source/action" in minimal and "physical-observable identification" in minimal and "probability" in minimal)
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
        "No derivation that local coordinate relabeling symmetry is physically",
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
