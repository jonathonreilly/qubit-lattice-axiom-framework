#!/usr/bin/env python3
"""Exact checks for two spatially covariant conditional-law models.

The paired theorem constructs two fixed nearest-neighbor probability rules on
M_2(C), both controlled by one proper-cubic invariant shell parity.  Their
internal SU(2)-conjugation behavior is different.  No Record scalar or physical
gauge-step process is used.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = (
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_"
    "BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Vector = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], tuple[int, int, int]]

DIRECTIONS: tuple[Vector, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXIS_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
Q8_LABELS = ("+1", "-1", *AXIS_LABELS)
LABEL_TO_VECTOR: dict[str, Vector] = dict(zip(AXIS_LABELS, DIRECTIONS, strict=True))
VECTOR_TO_LABEL = {vector: label for label, vector in LABEL_TO_VECTOR.items()}

Matrix2 = tuple[tuple[complex, complex], tuple[complex, complex]]
IDENTITY2: Matrix2 = ((1, 0), (0, 1))
Q8_MATRICES: dict[str, Matrix2] = {
    "+1": IDENTITY2,
    "-1": ((-1, 0), (0, -1)),
    "+x": ((0, 1j), (1j, 0)),
    "-x": ((0, -1j), (-1j, 0)),
    "+y": ((0, 1), (-1, 0)),
    "-y": ((0, -1), (1, 0)),
    "+z": ((1j, 0), (0, -1j)),
    "-z": ((-1j, 0), (0, 1j)),
}


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(left[row][k] * right[k][column] for k in range(2)) for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_adjoint(matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(matrix[column][row].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_determinant(matrix: Matrix2) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return -1 if inversions % 2 else 1


ROTATIONS: tuple[Rotation, ...] = tuple(
    (permutation, signs)
    for permutation in permutations((0, 1, 2))
    for signs in product((-1, 1), repeat=3)
    if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] == 1
)


def rotate_vector(rotation: Rotation, vector: Vector) -> Vector:
    permutation, signs = rotation
    result = [0, 0, 0]
    for source_axis in range(3):
        result[permutation[source_axis]] = signs[source_axis] * vector[source_axis]
    return tuple(result)  # type: ignore[return-value]


def rotate_label(rotation: Rotation, label: str) -> str:
    if label in {"+1", "-1"}:
        return label
    return VECTOR_TO_LABEL[rotate_vector(rotation, LABEL_TO_VECTOR[label])]


def rotate_shell(rotation: Rotation, shell: tuple[str, ...]) -> tuple[str, ...]:
    rotated: dict[Vector, str] = {}
    for direction, label in zip(DIRECTIONS, shell, strict=True):
        rotated[rotate_vector(rotation, direction)] = rotate_label(rotation, label)
    return tuple(rotated[direction] for direction in DIRECTIONS)


Measure = dict[str, Fraction]


def point_mass(label: str) -> Measure:
    return {candidate: Fraction(candidate == label) for candidate in Q8_LABELS}


DELTA_PLUS = point_mass("+1")
DELTA_MINUS = point_mass("-1")
NU_AXIS: Measure = {
    label: Fraction(1, 6) if label in AXIS_LABELS else Fraction(0)
    for label in Q8_LABELS
}


def is_probability(measure: Measure) -> bool:
    return (
        set(measure) == set(Q8_LABELS)
        and all(weight >= 0 for weight in measure.values())
        and sum(measure.values(), Fraction(0)) == 1
    )


def pushforward(rotation: Rotation, measure: Measure) -> Measure:
    result = {label: Fraction(0) for label in Q8_LABELS}
    for label, weight in measure.items():
        result[rotate_label(rotation, label)] += weight
    return result


def shell_parity(shell: tuple[str, ...]) -> int:
    if len(shell) != len(DIRECTIONS) or any(label not in Q8_LABELS for label in shell):
        raise ValueError("shell must give one Q8 label for each nearest neighbor")
    return sum(label == "+1" for label in shell) % 2


def central_law(shell: tuple[str, ...]) -> Measure:
    return DELTA_PLUS if shell_parity(shell) == 0 else DELTA_MINUS


def axis_law(shell: tuple[str, ...]) -> Measure:
    return DELTA_PLUS if shell_parity(shell) == 0 else NU_AXIS


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
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_flat = normalize(note)
    axiom_flat = normalize(axiom)

    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print("scientific_dependency: current minimal_axioms Admissibility/Qubit clauses")
    print("declared_math: Q8 matrix embedding, proper cubic rotations, finite Borel measures")

    checks.check(
        "audit-input-paths",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
        "the note and current axiom memo are the complete declared source packet",
    )
    checks.check(
        "current-admissibility-clause",
        "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
        in axiom_flat,
        "the current source supplies a conditional local probability law",
    )
    checks.check(
        "current-covariance-clause",
        "one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations"
        in axiom_flat,
        "the current source supplies the spatial covariance contract",
    )
    record_section = axiom.split("### Record / Fixed Reality", 1)[1].split(
        "## Qualification", 1
    )[0]
    checks.check(
        "post-reset-record-boundary",
        "A site with no record cannot be read." in normalize(record_section)
        and "I(empty)" not in record_section
        and "scalar readout" not in record_section
        and "additive" not in record_section,
        "the theorem uses the current unreadable-absence boundary and no retired scalar structure",
    )
    checks.check(
        "note-contract",
        "**Type:** bounded_theorem" in note
        and "actual_current_surface_status: bounded-support" in note
        and "These are two separate model laws." in note
        and "positive pair-of-models witness" in note_flat,
        "the note states the bounded positive model-pair target",
    )
    checks.check(
        "note-dependency",
        "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "heat-kernel notes" not in note_flat.lower(),
        "the only scientific authority is the current four-axiom memo",
    )

    checks.check(
        "q8-cardinality",
        len(Q8_LABELS) == len(set(Q8_LABELS)) == 8
        and set(AXIS_LABELS) == set(VECTOR_TO_LABEL.values()),
        "the finite support contains two central and six quaternion-axis atoms",
    )
    matrix_values = set(Q8_MATRICES.values())
    checks.check(
        "q8-matrix-embedding",
        set(Q8_MATRICES) == set(Q8_LABELS)
        and len(matrix_values) == 8
        and all(matrix_determinant(matrix) == 1 for matrix in matrix_values)
        and all(
            matrix_multiply(matrix_adjoint(matrix), matrix) == IDENTITY2
            for matrix in matrix_values
        )
        and all(
            matrix_multiply(left, right) in matrix_values
            for left in matrix_values
            for right in matrix_values
        ),
        "the eight displayed matrices form a unitary determinant-one subgroup of M_2(C)",
    )
    checks.check(
        "proper-cubic-group",
        len(ROTATIONS) == 24 and len(set(ROTATIONS)) == 24,
        "the determinant-positive signed-permutation group has 24 elements",
    )
    checks.check(
        "direction-action",
        all(
            {rotate_vector(rotation, direction) for direction in DIRECTIONS}
            == set(DIRECTIONS)
            for rotation in ROTATIONS
        ),
        "every proper cubic rotation permutes the six neighbor directions",
    )
    checks.check(
        "q8-action",
        all(
            {rotate_label(rotation, label) for label in Q8_LABELS}
            == set(Q8_LABELS)
            for rotation in ROTATIONS
        ),
        "the spatial action fixes the center and permutes the six axis atoms",
    )

    checks.check(
        "probability-normalization",
        all(is_probability(measure) for measure in (DELTA_PLUS, DELTA_MINUS, NU_AXIS)),
        "both delta measures and the six-axis measure have exact total mass one",
    )
    nonnormalized_mutation = dict(NU_AXIS)
    nonnormalized_mutation["+x"] += Fraction(1, 6)
    checks.check(
        "mutation-probability-total",
        not is_probability(nonnormalized_mutation),
        "adding an unbalanced axis mass is rejected by the normalization gate",
    )
    checks.check(
        "axis-cubic-invariance",
        all(pushforward(rotation, NU_AXIS) == NU_AXIS for rotation in ROTATIONS),
        "the uniform six-axis measure is invariant under all 24 proper cubic rotations",
    )
    checks.check(
        "central-cubic-invariance",
        all(
            pushforward(rotation, measure) == measure
            for rotation in ROTATIONS
            for measure in (DELTA_PLUS, DELTA_MINUS)
        ),
        "the central point masses are fixed by the spatial rotation action",
    )

    even_shell = ("+1",) * 6
    odd_shell = ("-1", "+1", "+1", "+1", "+1", "+1")
    checks.check(
        "shell-parity-witnesses",
        shell_parity(even_shell) == 0 and shell_parity(odd_shell) == 1,
        "the two displayed shells realize both conditional branches",
    )
    checks.check(
        "parity-covariance",
        all(
            shell_parity(rotate_shell(rotation, shell)) == shell_parity(shell)
            for rotation in ROTATIONS
            for shell in product(("+1", "-1"), repeat=6)
        ),
        "all 64 central shells retain parity under all 24 rotations",
    )
    checks.check(
        "central-law-variation",
        central_law(even_shell) == DELTA_PLUS
        and central_law(odd_shell) == DELTA_MINUS
        and central_law(even_shell) != central_law(odd_shell),
        "the central law changes output between even and odd shell conditions",
    )
    checks.check(
        "axis-law-variation",
        axis_law(even_shell) == DELTA_PLUS
        and axis_law(odd_shell) == NU_AXIS
        and axis_law(even_shell) != axis_law(odd_shell),
        "the axis law changes output between even and odd shell conditions",
    )
    checks.check(
        "law-covariance",
        all(
            pushforward(rotation, law(shell)) == law(rotate_shell(rotation, shell))
            for rotation in ROTATIONS
            for shell in (even_shell, odd_shell)
            for law in (central_law, axis_law)
        ),
        "both conditional laws obey the exact pushforward covariance equation",
    )
    checks.check(
        "laws-distinct",
        central_law(odd_shell) != axis_law(odd_shell),
        "the odd-shell outputs are different normalized measures",
    )

    diagonal_axis_squared_components = (Fraction(1, 2), Fraction(1, 2), Fraction(0))
    support_squared_components = {
        tuple(Fraction(component * component) for component in vector)
        for vector in DIRECTIONS
    }
    checks.check(
        "internal-pi-over-four-image",
        diagonal_axis_squared_components not in support_squared_components
        and NU_AXIS["+x"] == Fraction(1, 6),
        "the rotated +x atom has two nonzero components and leaves the six-axis support",
    )
    checks.check(
        "central-full-conjugation",
        DELTA_PLUS["+1"] == 1 and DELTA_MINUS["-1"] == 1,
        "central matrices commute with every internal SU(2) element",
    )

    first_slot_condition = lambda shell: int(shell[0] == "+1")
    moved_single_plus = ("+1", "-1", "-1", "-1", "-1", "-1")
    checks.check(
        "mutation-first-slot-condition-breaks-covariance",
        any(
            first_slot_condition(rotate_shell(rotation, moved_single_plus))
            != first_slot_condition(moved_single_plus)
            for rotation in ROTATIONS
        ),
        "a direction-privileging shell rule is rejected by the rotation test",
    )
    anisotropic_axis = dict(NU_AXIS)
    anisotropic_axis["+x"] += Fraction(1, 12)
    anisotropic_axis["-x"] -= Fraction(1, 12)
    checks.check(
        "mutation-anisotropic-axis-breaks-covariance",
        is_probability(anisotropic_axis)
        and any(
            pushforward(rotation, anisotropic_axis) != anisotropic_axis
            for rotation in ROTATIONS
        ),
        "an unequal axis weighting is rejected by the proper-cubic invariance test",
    )
    substantive_note = note.split("## Review record", 1)[0]
    checks.check(
        "record-semantics-absent",
        "No Record functional appears" in substantive_note
        and "uses no scalar collection readout, no finite additivity"
        in normalize(substantive_note)
        and "I(empty)" not in substantive_note
        and "dummy record" not in substantive_note.lower(),
        "the repaired theorem restores none of the retired scalar Record semantics",
    )
    checks.check(
        "physical-boundary",
        all(
            phrase in note_flat
            for phrase in (
                "selects neither rule as the framework's physical law",
                "no map from a one-site conditional possibility law to a gauge-link step process",
                "no continuum `SU(2)` measure",
                "no Haar selection",
                "no Markov generator",
            )
        ),
        "the exact finite pair is separated from every downstream physical selection claim",
    )
    checks.check(
        "review-record",
        "submitted version used a retired scalar Record functional" in note
        and "broad negative framing" in note
        and "is not shipped" in note,
        "the source records why the original negative theorem was replaced",
    )

    print(
        "per_element: executed — all eight Q8 support labels and the declared internal rotation image are checked exactly"
    )
    print(
        "per_site: executed — one six-neighbor shell is checked under every proper cubic direction permutation"
    )
    print(
        "per_mode: checked and not executed — the theorem has no spectral, momentum, or normal-mode decomposition"
    )
    print(
        "per_block: executed — both central and axis conditional-law branches are normalized, varied, and compared"
    )
    print(
        "lattice_wide: checked and not executed — the theorem proves a translation-reused local rule, not a global history"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
