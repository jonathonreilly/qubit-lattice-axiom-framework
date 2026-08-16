#!/usr/bin/env python3
"""Exact stabilizer of the tied occupancy kernels on finite G+.

G+ is the 24 proper cube rotations, acting in the 3-vector representation.
The theorem reports Stab(n) at the two positive two-ball sites and whether
a stabilizer element swaps the tied ±x slots. Stab is displayed, not adopted.
"""

from __future__ import annotations

import ast
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/TIED_KERNEL_STABILIZER_FORBIDS_EQUIVARIANT_FIRE_"
    "BOUNDED_THEOREM_NOTE_2026-08-15.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TIED_KERNEL_STABILIZER_FORBIDS_EQUIVARIANT_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Vector = tuple[Fraction, Fraction, Fraction]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]
PLUS_X: Vector = (Fraction(1), Fraction(0), Fraction(0))
MINUS_X: Vector = (Fraction(-1), Fraction(0), Fraction(0))
N1: Vector = (Fraction(0), Fraction(1, 3), Fraction(-1, 3))
N2: Vector = (Fraction(0), Fraction(-1, 3), Fraction(1, 3))
SLOTS: tuple[Vector, ...] = (
    PLUS_X,
    MINUS_X,
    (Fraction(0), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(-1), Fraction(0)),
    (Fraction(0), Fraction(0), Fraction(1)),
    (Fraction(0), Fraction(0), Fraction(-1)),
)
SLOT_NAMES = {
    PLUS_X: "+x",
    MINUS_X: "-x",
    (Fraction(0), Fraction(1), Fraction(0)): "+y",
    (Fraction(0), Fraction(-1), Fraction(0)): "-y",
    (Fraction(0), Fraction(0), Fraction(1)): "+z",
    (Fraction(0), Fraction(0), Fraction(-1)): "-z",
}


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


G_PLUS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Vector) -> Vector:
    permutation, signs = rotation
    result = [Fraction(0), Fraction(0), Fraction(0)]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return (result[0], result[1], result[2])


def stabilizer(kernel: Vector) -> tuple[Rotation, ...]:
    return tuple(
        rotation
        for rotation in G_PLUS
        if rotate_vector(rotation, kernel) == kernel
    )


def swaps_tied_slots(rotation: Rotation) -> bool:
    return rotate_vector(rotation, PLUS_X) == MINUS_X


def identity_rotation() -> Rotation:
    return ((0, 1, 2), (1, 1, 1))


def letters() -> tuple[str, str]:
    return ("+", "-")


def opposite_x_labelings() -> tuple[dict[Vector, str], ...]:
    plus, minus = letters()
    other = [slot for slot in SLOTS if slot not in (PLUS_X, MINUS_X)]
    out: list[dict[Vector, str]] = []
    for plus_letter, minus_letter in ((plus, minus), (minus, plus)):
        for assignment in product(letters(), repeat=len(other)):
            labeling = {PLUS_X: plus_letter, MINUS_X: minus_letter}
            labeling.update(dict(zip(other, assignment, strict=True)))
            out.append(labeling)
    return tuple(out)


def all_labelings() -> tuple[dict[Vector, str], ...]:
    return tuple(
        dict(zip(SLOTS, assignment, strict=True))
        for assignment in product(letters(), repeat=len(SLOTS))
    )


def labeling_is_stab_invariant(
    labeling: dict[Vector, str], stab: tuple[Rotation, ...]
) -> bool:
    return all(
        labeling[rotate_vector(rotation, slot)] == labeling[slot]
        for rotation in stab
        for slot in SLOTS
    )


def parse_audit_input_paths(source: str) -> object:
    tree = ast.parse(source)
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS":
                return ast.literal_eval(node.value)
    raise AssertionError("AUDIT_INPUT_PATHS assignment is missing")


def normalize(text: str) -> str:
    return " ".join(text.split())


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'}: {label} {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note_path = ROOT / NOTE_REL
    axiom_path = ROOT / AXIOM_REL
    note = note_path.read_text(encoding="utf-8")
    axiom = axiom_path.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)
    self_source = Path(__file__).read_text(encoding="utf-8")
    literal_paths = parse_audit_input_paths(self_source)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current minimal_axioms Lattice covariance clause")
    print("declared_math: finite G+ in the 3-vector representation; tied kernels n1, n2")

    checks.check(
        "audit-input-paths",
        AUDIT_INPUT_PATHS
        == (
            "docs/TIED_KERNEL_STABILIZER_FORBIDS_EQUIVARIANT_FIRE_BOUNDED_THEOREM_NOTE_2026-08-15.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and literal_paths == AUDIT_INPUT_PATHS
        and all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and AUDIT_TIMEOUT_SEC == 120,
        "AUDIT_INPUT_PATHS is the required static two-string literal tuple",
    )
    checks.check(
        "g-plus-order",
        len(G_PLUS) == 24 and len(set(G_PLUS)) == 24,
        "finite G+ is exactly the 24 proper cube rotations",
    )
    checks.check(
        "declared-kernels",
        N1 == (Fraction(0), Fraction(1, 3), Fraction(-1, 3))
        and N2 == (Fraction(0), Fraction(-1, 3), Fraction(1, 3))
        and N2 == tuple(-component for component in N1),
        "n1 and n2 are the declared tied occupancy kernels",
    )

    stab1 = stabilizer(N1)
    stab2 = stabilizer(N2)
    swap1 = tuple(rotation for rotation in stab1 if swaps_tied_slots(rotation))
    swap2 = tuple(rotation for rotation in stab2 if swaps_tied_slots(rotation))

    print(f"stab_n1_order: {len(stab1)}")
    print(f"stab_n2_order: {len(stab2)}")
    print(f"stab_n1_has_tied_swap: {bool(swap1)}")
    print(f"stab_n2_has_tied_swap: {bool(swap2)}")

    checks.check(
        "theorem-1-stab-orders",
        len(stab1) == 2 and len(stab2) == 2,
        "|Stab(n1)| = |Stab(n2)| = 2",
    )
    checks.check(
        "theorem-1-tied-swap",
        len(swap1) == 1
        and len(swap2) == 1
        and swap1 == swap2
        and identity_rotation() in stab1
        and identity_rotation() in stab2
        and not swaps_tied_slots(identity_rotation()),
        "exactly one non-identity stabilizer element swaps +x with -x at both sites",
    )
    swapper = swap1[0]
    checks.check(
        "swapper-action",
        rotate_vector(swapper, N1) == N1
        and rotate_vector(swapper, N2) == N2
        and rotate_vector(swapper, PLUS_X) == MINUS_X
        and rotate_vector(swapper, MINUS_X) == PLUS_X
        and rotate_vector(swapper, (Fraction(0), Fraction(1), Fraction(0)))
        == (Fraction(0), Fraction(0), Fraction(-1))
        and rotate_vector(swapper, (Fraction(0), Fraction(0), Fraction(1)))
        == (Fraction(0), Fraction(-1), Fraction(0)),
        "the common swapper is x -> -x, y -> -z, z -> -y",
    )

    opposite = opposite_x_labelings()
    invariant1 = [
        labeling
        for labeling in all_labelings()
        if labeling_is_stab_invariant(labeling, stab1)
    ]
    invariant2 = [
        labeling
        for labeling in all_labelings()
        if labeling_is_stab_invariant(labeling, stab2)
    ]
    firing_invariant1 = [
        labeling
        for labeling in opposite
        if labeling_is_stab_invariant(labeling, stab1)
    ]
    firing_invariant2 = [
        labeling
        for labeling in opposite
        if labeling_is_stab_invariant(labeling, stab2)
    ]
    checks.check(
        "theorem-2-same-letter",
        all(labeling[PLUS_X] == labeling[MINUS_X] for labeling in invariant1)
        and all(labeling[PLUS_X] == labeling[MINUS_X] for labeling in invariant2)
        and len(invariant1) == 8
        and len(invariant2) == 8
        and len(opposite) == 32
        and firing_invariant1 == []
        and firing_invariant2 == [],
        "every Stab-invariant labeling gives +x and -x the same letter, so none fire",
    )
    slot_odd = {slot: ("+" if slot == PLUS_X else "-") for slot in SLOTS}
    slot_odd[MINUS_X] = "-"
    checks.check(
        "slot-odd-not-equivariant",
        slot_odd[PLUS_X] != slot_odd[MINUS_X]
        and not labeling_is_stab_invariant(slot_odd, stab1)
        and not labeling_is_stab_invariant(slot_odd, stab2),
        "a slot-odd opposite-x labeling fires and is not stabilizer-invariant",
    )
    checks.check(
        "lattice-clause",
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
        in axiom
        and "proper cubic rotations about each site" in axiom_flat
        and "proper cubic rotations about each site" in note_flat,
        "the current Lattice wording supplies finite proper cubic rotations",
    )
    checks.check(
        "admissibility-unedited",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat
        and "Do not write Stab into Admissibility" in note
        and "Stab(" not in axiom
        and "stabilizer" not in axiom.lower(),
        "Stab is displayed and is not written into Admissibility",
    )
    checks.check(
        "displayed-not-adopted",
        "Displayed, not adopted" in note
        and "Do not attach L1" in note
        and "leftover-char" in note
        and "not leftover-char of slotn" in note_flat
        and "finite G+ = 24 only" in note_flat.replace("`", ""),
        "the note reports the stabilizer obstruction without adopting it or attaching L1",
    )
    forbidden = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")
    script_body = self_source.split("forbidden = ", 1)[0]
    checks.check(
        "forbidden-phrases",
        all(phrase not in note for phrase in forbidden)
        and all(phrase not in script_body for phrase in forbidden),
        "the forbidden rhetoric strings are absent from the note and runner",
    )
    checks.check(
        "claim-scope",
        'claim_scope: "Whether the G+ stabilizer of the tied occupancy kernels at the two positive two-ball sites contains an element swapping the tied slots, and whether that forbids every cube-equivariant firing labeling, is reported. Displayed, not adopted."'
        in note
        and "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "hypothetical_axiom_status: no edit" in note,
        "claim_scope and machine status match the displayed-not-adopted residual",
    )
    checks.check(
        "no-axiom-edit",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "no axiom edit" in note_flat.lower()
        and "cache_write: false" in self_source,
        "the only axiom authority is the current memo; no cache or axiom rewrite",
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
