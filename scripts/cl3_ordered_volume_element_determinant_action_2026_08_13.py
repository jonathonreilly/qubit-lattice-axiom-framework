#!/usr/bin/env python3
"""Exact integer checks: Cl(3,0) volume elements +ω and −ω are not axiom-selected.

Identity gates call volume() and volume_opp(). The predicates
ω' ≠ −ω and ω² ≠ (−ω)² are required to fail.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]

AUDIT_INPUT_PATHS = (
    "docs/CL3_VOLUME_ELEMENTS_PLUS_MINUS_NOT_AXIOM_SELECTED_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / AUDIT_INPUT_PATHS[0]
PARENT_PATH = ROOT / AUDIT_INPUT_PATHS[1]
AXIOM_PATH = ROOT / AUDIT_INPUT_PATHS[2]


class Cl3:
    """Integer span of Cl(3,0) in the ordered basis 1, e1, e2, e3, e12, e13, e23, e123."""

    __slots__ = ("c",)

    def __init__(self, coeffs: tuple[int, ...] | list[int]) -> None:
        values = tuple(int(value) for value in coeffs)
        if len(values) != 8:
            raise ValueError("Cl(3,0) vectors have eight integer coefficients")
        self.c = values

    def __add__(self, other: "Cl3") -> "Cl3":
        return Cl3(tuple(a + b for a, b in zip(self.c, other.c)))

    def __sub__(self, other: "Cl3") -> "Cl3":
        return Cl3(tuple(a - b for a, b in zip(self.c, other.c)))

    def __neg__(self) -> "Cl3":
        return Cl3(tuple(-value for value in self.c))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Cl3) and self.c == other.c

    def __mul__(self, other: "Cl3") -> "Cl3":
        acc = [0, 0, 0, 0, 0, 0, 0, 0]
        for mask_a, coeff_a in enumerate(self.c):
            if coeff_a == 0:
                continue
            for mask_b, coeff_b in enumerate(other.c):
                if coeff_b == 0:
                    continue
                sign, mask = _blade_mul(mask_a, mask_b)
                acc[mask] += sign * coeff_a * coeff_b
        return Cl3(tuple(acc))

    def grade_parity(self) -> int | None:
        parities = {
            bin(mask).count("1") % 2
            for mask, coeff in enumerate(self.c)
            if coeff
        }
        if len(parities) != 1:
            return None
        return next(iter(parities))

    def is_scalar(self, value: int) -> bool:
        return self.c == (value, 0, 0, 0, 0, 0, 0, 0)


def _blade_mul(mask_a: int, mask_b: int) -> tuple[int, int]:
    """Euclidean Cl(3,0) product of two basis blades. Returns (sign, mask)."""
    sign = 1
    mask = mask_a
    for index in range(3):
        if ((mask_b >> index) & 1) == 0:
            continue
        higher = 0
        for other in range(index + 1, 3):
            if (mask >> other) & 1:
                higher += 1
        if higher % 2:
            sign = -sign
        mask ^= 1 << index
    return sign, mask


def basis(mask: int) -> Cl3:
    coeffs = [0] * 8
    coeffs[mask] = 1
    return Cl3(tuple(coeffs))


SCALAR = basis(0)
E1 = basis(1)
E2 = basis(2)
E3 = basis(4)
GENERATORS = (E1, E2, E3)


def volume() -> Cl3:
    return E1 * E2 * E3


def volume_opp() -> Cl3:
    return E3 * E2 * E1


def identity_opposite_is_minus() -> bool:
    return volume_opp() == -volume()


def identity_squares_equal() -> bool:
    return (volume() * volume()) == (volume_opp() * volume_opp())


def mutation_opp_neq_minus() -> bool:
    """Predicate ω' ≠ −ω. Must fail on the live algebra."""
    return volume_opp() != -volume()


def mutation_squares_unequal() -> bool:
    """Predicate ω² ≠ (−ω)². Must fail on the live algebra."""
    minus = -volume()
    return (volume() * volume()) != (minus * minus)


class Gauss:
    __slots__ = ("re", "im")

    def __init__(self, re: int, im: int = 0) -> None:
        self.re = int(re)
        self.im = int(im)

    def __add__(self, other: "Gauss") -> "Gauss":
        return Gauss(self.re + other.re, self.im + other.im)

    def __neg__(self) -> "Gauss":
        return Gauss(-self.re, -self.im)

    def __mul__(self, other: "Gauss") -> "Gauss":
        return Gauss(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Gauss) and self.re == other.re and self.im == other.im


class Mat2:
    """2×2 matrices over Z[i], used only for the Pauli exhibit."""

    __slots__ = ("a",)

    def __init__(self, entries: tuple[tuple[Gauss, Gauss], tuple[Gauss, Gauss]]) -> None:
        self.a = entries

    def __neg__(self) -> "Mat2":
        return Mat2(tuple(tuple(-entry for entry in row) for row in self.a))  # type: ignore[arg-type]

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Mat2) and self.a == other.a

    def __mul__(self, other: "Mat2") -> "Mat2":
        out = []
        for row in range(2):
            out_row = []
            for col in range(2):
                acc = Gauss(0)
                for mid in range(2):
                    acc = acc + self.a[row][mid] * other.a[mid][col]
                out_row.append(acc)
            out.append(tuple(out_row))
        return Mat2((out[0], out[1]))


ZERO_G = Gauss(0)
ONE_G = Gauss(1)
I_G = Gauss(0, 1)
SIGMA1 = Mat2(((ZERO_G, ONE_G), (ONE_G, ZERO_G)))
SIGMA2 = Mat2(((ZERO_G, Gauss(0, -1)), (I_G, ZERO_G)))
SIGMA3 = Mat2(((ONE_G, ZERO_G), (ZERO_G, Gauss(-1))))
PAULI_I = Mat2(((ONE_G, ZERO_G), (ZERO_G, ONE_G)))


def pauli_volume() -> Mat2:
    return volume_from(SIGMA1, SIGMA2, SIGMA3)


def pauli_volume_opp() -> Mat2:
    return volume_opp_from(SIGMA1, SIGMA2, SIGMA3)


def volume_from(e1, e2, e3):
    return e1 * e2 * e3


def volume_opp_from(e1, e2, e3):
    return e3 * e2 * e1


def apply_linear(matrix: tuple[tuple[int, ...], ...], vectors: tuple[Cl3, Cl3, Cl3]) -> tuple[Cl3, Cl3, Cl3]:
    images = []
    for col in range(3):
        acc = Cl3((0, 0, 0, 0, 0, 0, 0, 0))
        for row in range(3):
            coeff = matrix[row][col]
            if coeff == 1:
                acc = acc + vectors[row]
            elif coeff == -1:
                acc = acc - vectors[row]
        images.append(acc)
    return images[0], images[1], images[2]


def permutation_sign(perm: tuple[int, ...]) -> int:
    sign = 1
    values = list(perm)
    for i in range(3):
        for j in range(i + 1, 3):
            if values[i] > values[j]:
                sign = -sign
    return sign


def proper_cubic_rotations() -> list[tuple[tuple[int, ...], ...]]:
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            det = permutation_sign(perm) * signs[0] * signs[1] * signs[2]
            if det != 1:
                continue
            matrix = []
            for row in range(3):
                row_entries = []
                for col in range(3):
                    row_entries.append(signs[row] if perm[row] == col else 0)
                matrix.append(tuple(row_entries))
            rotations.append(tuple(matrix))
    return rotations


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_n = normalize(note)
    parent_n = normalize(parent)
    axiom_n = normalize(axiom)

    print("external_scientific_inputs: none; exact Cl(3,0) anticommutators and the declared axiom/parent wording")
    print("audit_input_paths: " + ", ".join(AUDIT_INPUT_PATHS))

    checks.check(
        "audit-inputs-exist",
        "declared note, May 10 parent, and axiom memo are readable",
        NOTE_PATH.is_file() and PARENT_PATH.is_file() and AXIOM_PATH.is_file(),
    )

    car_ok = True
    for i, ei in enumerate(GENERATORS):
        for j, ej in enumerate(GENERATORS):
            anti = ei * ej + ej * ei
            expected = SCALAR + SCALAR if i == j else Cl3((0, 0, 0, 0, 0, 0, 0, 0))
            car_ok = car_ok and anti == expected
    checks.check("car", "{ei, ej} = 2 δ_ij I on the integer generators", car_ok)

    checks.check(
        "identity-opp-minus",
        "volume_opp() equals -volume()",
        identity_opposite_is_minus(),
    )
    checks.check(
        "identity-squares",
        "volume()^2 equals volume_opp()^2",
        identity_squares_equal(),
    )
    checks.check(
        "mutation-opp-neq-minus",
        "the predicate ω' ≠ −ω fails",
        mutation_opp_neq_minus() is False,
    )
    checks.check(
        "mutation-squares-unequal",
        "the predicate ω² ≠ (−ω)² fails",
        mutation_squares_unequal() is False,
    )

    omega = volume()
    omega_opp = volume_opp()
    checks.check("odd-grade", "both volume elements are grade-odd", omega.grade_parity() == 1 and omega_opp.grade_parity() == 1)
    central = all(omega * gen == gen * omega and omega_opp * gen == gen * omega_opp for gen in GENERATORS)
    checks.check("central", "n=3 odd: ω and ω' commute with every generator", central)
    checks.check("square-minus-one", "ω² = (−ω)² = −I", (omega * omega).is_scalar(-1) and ((-omega) * (-omega)).is_scalar(-1))

    pauli_w = pauli_volume()
    pauli_w_opp = pauli_volume_opp()
    i_times_id = Mat2(((I_G, ZERO_G), (ZERO_G, I_G)))
    checks.check(
        "pauli-volume",
        "σ1 σ2 σ3 = i I and the opposite product is −i I",
        pauli_w == i_times_id and pauli_w_opp == -i_times_id,
    )
    checks.check(
        "pauli-squares",
        "(σ1 σ2 σ3)² = (−σ1 σ2 σ3)² = −I",
        pauli_w * pauli_w == -PAULI_I and pauli_w_opp * pauli_w_opp == -PAULI_I,
    )

    rotations = proper_cubic_rotations()
    gens = (E1, E2, E3)
    preserve = True
    for matrix in rotations:
        images = apply_linear(matrix, gens)
        rotated = volume_from(*images)
        rotated_opp = volume_opp_from(*images)
        if rotated != omega or rotated_opp != omega_opp:
            preserve = False
            break
    checks.check(
        "proper-rotations-preserve-both",
        "all 24 proper cubic rotations preserve ω and −ω",
        len(rotations) == 24 and preserve,
    )

    reflection = ((-1, 0, 0), (0, 1, 0), (0, 0, 1))
    reflected = volume_from(*apply_linear(reflection, gens))
    checks.check(
        "improper-flips",
        "the sample det=−1 map exchanges the two volume signs",
        reflected == -omega,
    )

    qubit_quote = (
        "A `Cl(3,0)`-compatible real-algebra presentation may be used equivalently and "
        "adds no further primitive structure."
    )
    checks.check(
        "source-qubit",
        "axiom memo carries the Qubit Cl(3,0) equivalence sentence",
        normalize(qubit_quote) in axiom_n,
    )
    checks.check(
        "source-lattice",
        "axiom memo names proper cubic rotations",
        "proper cubic rotations about each site" in axiom_n,
    )
    checks.check(
        "source-parent-odd-central",
        "May 10 parent states the odd-n centrality rule",
        "If `n` is odd, `omega` **commutes** with every generator" in parent
        or "If n is odd, omega commutes with every generator" in parent_n,
    )
    checks.check(
        "source-note-missing-input",
        "this note displays s in {+1, −1} and does not add a chirality axiom",
        "s ∈ {+1, −1}" in note and "does not add a chirality axiom" in note_n,
    )
    checks.check(
        "source-note-no-identifications",
        "this note refuses hypercharge, gravity-orientation, and fifth-axiom identifications",
        "weak hypercharge" in note_n and "gravity orientation" in note_n and "fifth framework axiom" in note_n,
    )
    checks.check(
        "source-note-no-reopen-dt",
        "this note does not reopen d_t",
        "does not reopen `d_t`" in note or "does not reopen d_t" in note_n,
    )
    checks.check(
        "source-note-hygiene",
        "this note avoids we-adopt / new-axiom / Codex language",
        "we adopt" not in note_n.lower()
        and "new axiom" not in note_n.lower()
        and "codex" not in note_n.lower(),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
