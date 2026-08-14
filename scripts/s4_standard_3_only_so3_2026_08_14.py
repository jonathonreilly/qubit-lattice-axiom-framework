#!/usr/bin/env python3
"""Exact checks that only the standard 3 of S4 lands in SO(3).

G is 3x3 signed permutation matrices of determinant +1. The twist
3' = 3 ⊗ sgn is evaluated on a displayed 90° axis rotation. No cache
write, no float inputs, no axiom edit.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "S4_STANDARD_3_ONLY_SO3_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/S4_STANDARD_3_ONLY_SO3_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, ...], ...]
Vec = tuple[Fraction, ...]


def F(value: int) -> Fraction:
    return Fraction(value)


def mat(*rows: tuple[int, int, int]) -> Matrix:
    return tuple(tuple(F(entry) for entry in row) for row in rows)


def vec(*coords: int) -> Vec:
    return tuple(F(entry) for entry in coords)


def apply(matrix: Matrix, vector: Vec) -> Vec:
    return tuple(
        sum((matrix[row][col] * vector[col] for col in range(3)), F(0))
        for row in range(3)
    )


def scale(scalar: Fraction, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scalar * matrix[row][col] for col in range(3)) for row in range(3)
    )


def det3(matrix: Matrix) -> Fraction:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def is_signed_permutation(matrix: Matrix) -> bool:
    allowed = {F(-1), F(0), F(1)}
    if any(entry not in allowed for row in matrix for entry in row):
        return False
    row_counts = [sum(1 for entry in row if entry != 0) for row in matrix]
    col_counts = [
        sum(1 for row in range(3) if matrix[row][col] != 0) for col in range(3)
    ]
    return row_counts == [1, 1, 1] and col_counts == [1, 1, 1]


def canon_line(vector: Vec) -> Vec:
    for entry in vector:
        if entry != 0:
            return vector if entry > 0 else tuple(-coord for coord in vector)
    raise ValueError("zero vector does not determine a line")


LINES: tuple[Vec, ...] = (
    vec(1, 1, 1),
    vec(1, 1, -1),
    vec(1, -1, 1),
    vec(1, -1, -1),
)


def line_index(vector: Vec) -> int:
    representative = canon_line(vector)
    return LINES.index(representative)


def phi(matrix: Matrix) -> tuple[int, ...]:
    return tuple(line_index(apply(matrix, line)) for line in LINES)


def cycle_lengths(images: tuple[int, ...]) -> tuple[int, ...]:
    seen = [False] * len(images)
    lengths: list[int] = []
    for start in range(len(images)):
        if seen[start]:
            continue
        length = 0
        index = start
        while not seen[index]:
            seen[index] = True
            index = images[index]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def perm_sign(images: tuple[int, ...]) -> int:
    sign = 1
    for length in cycle_lengths(images):
        if (length - 1) % 2 == 1:
            sign *= -1
    return sign


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; exact signed-permutation algebra only")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction coefficients; no floating-point inputs")
    print("claim_boundary: bounded algebraic result; no physical map is asserted")

    rotation = mat((1, 0, 0), (0, 0, -1), (0, 1, 0))
    vertex = mat((0, 0, 1), (1, 0, 0), (0, 1, 0))
    minus_rotation = scale(F(-1), rotation)
    phi_r = phi(rotation)
    phi_s = phi(vertex)
    sign_r = perm_sign(phi_r)
    sign_s = perm_sign(phi_s)
    twist_r = scale(F(sign_r), rotation)
    twist_s = scale(F(sign_s), vertex)

    images_r = tuple(apply(rotation, line) for line in LINES)
    expected_r = (LINES[2], LINES[0], LINES[3], LINES[1])
    images_s = tuple(canon_line(apply(vertex, line)) for line in LINES)
    expected_s = (LINES[0], LINES[3], LINES[1], LINES[2])

    checks.check(
        "thm1-signed-perm",
        "R is a 3x3 signed permutation matrix",
        is_signed_permutation(rotation),
    )
    checks.check("thm1-det-r", "det R = +1", det3(rotation) == F(1))
    checks.check(
        "thm1-in-g-and-so3",
        "R lies in G and in SO(3)",
        is_signed_permutation(rotation) and det3(rotation) == F(1),
    )

    checks.check(
        "thm2-line-images",
        "R sends (l0,l1,l2,l3) to (l2,l0,l3,l1)",
        images_r == expected_r,
    )
    checks.check(
        "thm2-four-cycle",
        "phi(R) is a 4-cycle",
        cycle_lengths(phi_r) == (4,) and len(set(phi_r)) == 4,
    )
    checks.check(
        "thm2-sign-odd",
        "sgn(phi(R)) = -1",
        sign_r == -1,
    )

    checks.check(
        "thm3-twist-is-minus-r",
        "3'(R) = sgn(phi(R)) R equals -R",
        twist_r == minus_rotation,
    )
    checks.check(
        "thm3-det-minus-r",
        "det(-R) = -1",
        det3(minus_rotation) == F(-1),
    )
    checks.check(
        "thm3-odd-dim-sign-identity",
        "det(-R) = (-1)^3 det R",
        det3(minus_rotation) == (F(-1) ** 3) * det3(rotation),
    )
    checks.check(
        "thm3-not-in-so3",
        "-R is outside SO(3)",
        det3(minus_rotation) != F(1),
    )
    checks.check(
        "thm4-standard-3-in-so3",
        "the standard inclusion sends R into SO(3)",
        det3(rotation) == F(1),
    )
    checks.check(
        "thm4-twist-not-hom-to-so3",
        "3' is not a homomorphism G -> SO(3)",
        det3(twist_r) != F(1),
    )

    checks.check(
        "thm5-s-in-g",
        "S is a signed permutation matrix of determinant +1",
        is_signed_permutation(vertex) and det3(vertex) == F(1),
    )
    checks.check(
        "thm5-line-images",
        "S sends (l0,l1,l2,l3) to (l0,l3,l1,l2)",
        images_s == expected_s,
    )
    checks.check(
        "thm5-three-cycle",
        "phi(S) is a 3-cycle with one fixed line",
        cycle_lengths(phi_s) == (3, 1),
    )
    checks.check(
        "thm5-sign-even",
        "sgn(phi(S)) = +1",
        sign_s == 1,
    )
    checks.check(
        "thm5-twist-agrees",
        "3'(S) equals the standard 3 on S",
        twist_s == vertex,
    )

    checks.check(
        "mutation-det-r-not-minus",
        "the det R = -1 mutation is rejected",
        det3(rotation) != F(-1),
    )
    checks.check(
        "mutation-phi-r-not-3-cycle",
        "the 3-cycle mutation of phi(R) is rejected",
        cycle_lengths(phi_r) != (3, 1),
    )
    checks.check(
        "mutation-det-minus-r-not-plus",
        "the det(-R) = +1 mutation is rejected",
        det3(minus_rotation) != F(1),
    )

    lattice_head = (
        "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"
    )
    lattice_tail = (
        "adjacency, standard translations, and proper cubic rotations about each site."
    )
    qubit_quote = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
    )
    forbidden = (
        "G_N",
        "1/r",
        "1/r^2",
        "Lattice-named",
        "not a TOE",
        "L_phys",
        "we adopt",
        "Codex",
    )
    allowed_retained = (
        "audit_required_before_effective_retained: true",
        "bare_retained_allowed: false",
    )
    other_retained = note
    for line in allowed_retained:
        other_retained = other_retained.replace(line, "")

    checks.check(
        "live-parent-quotes",
        "Lattice and Qubit sentences are quoted without rewrite",
        lattice_head in axiom
        and lattice_tail in axiom
        and lattice_head in note
        and lattice_tail in note
        and qubit_quote in axiom
        and qubit_quote in note,
    )
    checks.check(
        "target-name-only",
        "Aut(M_2) cong SO(3) is present as a name for the target",
        "Aut(M_2) ≅ SO(3)" in note
        and "name for the target" in note,
    )
    checks.check(
        "no-qubit-flip",
        "the note does not rewrite the Qubit sentence",
        "Qubit sentence is not rewritten" in note
        and qubit_quote in note,
    )
    checks.check(
        "machine-status-contract",
        "bounded status and uniqueness-repair trace are source-visible",
        "actual_current_surface_status: bounded-support" in note
        and "target_claim_type: bounded_theorem" in note
        and "trace_class: uniqueness_repair" in note
        and 'next_trace_action: "independent audit of the bounded algebraic claim"'
        in note,
    )
    checks.check(
        "import-boundary-contract",
        "the supplied group and absent physical bridge are disclosed",
        "## Inputs And Import Boundary" in note
        and "Explicit theorem-domain condition" in note
        and "External empirical or literature inputs:** none" in note
        and "Open physical bridge" in note,
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/S4_STANDARD_3_ONLY_SO3_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    checks.check(
        "forbidden-hygiene",
        "forbidden note substrings and adoption language are absent",
        all(token not in note for token in forbidden)
        and "we adopt" not in note.lower()
        and "Codex" not in note
        and "new axiom" not in note.lower()
        and "promoted" not in note.lower()
        and "retained" not in other_retained
        and all(line in note for line in allowed_retained)
        and ("import " + "qcd") not in self_source.lower()
        and ("from " + "qcd") not in self_source.lower(),
    )
    checks.check(
        "claim-type-and-scope",
        "the bounded type and SO(3) obstruction are source-visible",
        "**Type:** bounded_theorem" in note
        and "not a homomorphism `G → SO(3)`" in note
        and "only `3`, not `3'`" in note
        and "### N8" not in note
        and "FAIL / DO NOT SHIP" not in note,
    )

    print("per_element: R, -R, and the vertex companion S are checked by exact determinants")
    print("per_site: the four space-diagonal lines are the only evaluated orbit")
    print("per_mode: the odd 4-cycle and the even 3-cycle of S_4 are both resolved")
    print("per_block: only the 3 versus 3' landing question inside SO(3) is closed")
    print(
        "lattice_wide: checked and not executed — the claim asserts no lattice-wide lift"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
