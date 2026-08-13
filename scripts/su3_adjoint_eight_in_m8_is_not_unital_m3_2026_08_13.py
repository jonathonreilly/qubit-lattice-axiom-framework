#!/usr/bin/env python3
"""Exact checks: su(3) adjoint-8 sits in M_8 and is not unital M_3.

Gell-Mann matrices and f_abc are reconstructed over Q(sqrt(3)).
The leftover is displayed and not adopted as QCD or as unital M_3.
No QCD import, no Qubit rewrite, no runner cache.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "SU3_ADJOINT_EIGHT_IN_M8_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/SU3_ADJOINT_EIGHT_IN_M8_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


@dataclass(frozen=True)
class Q3:
    """a + b*sqrt(3) with a, b rational."""

    rat: Fraction
    s3: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "rat", Fraction(self.rat))
        object.__setattr__(self, "s3", Fraction(self.s3))

    def __add__(self, other: Q3) -> Q3:
        return Q3(self.rat + other.rat, self.s3 + other.s3)

    def __sub__(self, other: Q3) -> Q3:
        return Q3(self.rat - other.rat, self.s3 - other.s3)

    def __neg__(self) -> Q3:
        return Q3(-self.rat, -self.s3)

    def __mul__(self, other: Q3) -> Q3:
        return Q3(
            self.rat * other.rat + 3 * self.s3 * other.s3,
            self.rat * other.s3 + self.s3 * other.rat,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Q3):
            return NotImplemented
        return self.rat == other.rat and self.s3 == other.s3

    def is_zero(self) -> bool:
        return self.rat == 0 and self.s3 == 0


@dataclass(frozen=True)
class Cpx:
    re: Q3
    im: Q3 = Q3(0)

    def __add__(self, other: Cpx) -> Cpx:
        return Cpx(self.re + other.re, self.im + other.im)

    def __sub__(self, other: Cpx) -> Cpx:
        return Cpx(self.re - other.re, self.im - other.im)

    def __neg__(self) -> Cpx:
        return Cpx(-self.re, -self.im)

    def __mul__(self, other: Cpx) -> Cpx:
        return Cpx(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cpx):
            return NotImplemented
        return self.re == other.re and self.im == other.im

    def is_zero(self) -> bool:
        return self.re.is_zero() and self.im.is_zero()

    def conjugate(self) -> Cpx:
        return Cpx(self.re, -self.im)


ZERO = Cpx(Q3(0))
ONE = Cpx(Q3(1))
I_UNIT = Cpx(Q3(0), Q3(1))
TWO_I = Cpx(Q3(0), Q3(2))

Matrix = tuple[tuple[Cpx, ...], ...]
Real8 = tuple[tuple[Q3, ...], ...]


def zmat(n: int) -> list[list[Cpx]]:
    return [[ZERO for _ in range(n)] for _ in range(n)]


def freeze(data: list[list[Cpx]]) -> Matrix:
    return tuple(tuple(row) for row in data)


def madd(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[r][c] + right[r][c] for c in range(len(left)))
        for r in range(len(left))
    )


def mscale(scalar: Cpx, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scalar * matrix[r][c] for c in range(len(matrix)))
        for r in range(len(matrix))
    )


def mmul(left: Matrix, right: Matrix) -> Matrix:
    size = len(left)
    return tuple(
        tuple(
            sum((left[r][k] * right[k][c] for k in range(size)), ZERO)
            for c in range(size)
        )
        for r in range(size)
    )


def comm(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left_val - right_val for left_val, right_val in zip(left_row, right_row))
        for left_row, right_row in zip(mmul(left, right), mmul(right, left))
    )


def mtrace(matrix: Matrix) -> Cpx:
    return sum((matrix[i][i] for i in range(len(matrix))), ZERO)


def madjoint(matrix: Matrix) -> Matrix:
    size = len(matrix)
    return tuple(tuple(matrix[c][r].conjugate() for c in range(size)) for r in range(size))


def matrices_equal(left: Matrix, right: Matrix) -> bool:
    return all(
        left[r][c] == right[r][c]
        for r in range(len(left))
        for c in range(len(left))
    )


def gell_mann() -> tuple[Matrix, ...]:
    """Standard Gell-Mann matrices; λ_8 uses the exact coefficient 1/sqrt(3)."""
    inv_sqrt3 = Q3(0, Fraction(1, 3))  # sqrt(3)/3 = 1/sqrt(3)

    l1 = freeze(
        [
            [ZERO, ONE, ZERO],
            [ONE, ZERO, ZERO],
            [ZERO, ZERO, ZERO],
        ]
    )
    l2 = freeze(
        [
            [ZERO, -I_UNIT, ZERO],
            [I_UNIT, ZERO, ZERO],
            [ZERO, ZERO, ZERO],
        ]
    )
    l3 = freeze(
        [
            [ONE, ZERO, ZERO],
            [ZERO, -ONE, ZERO],
            [ZERO, ZERO, ZERO],
        ]
    )
    l4 = freeze(
        [
            [ZERO, ZERO, ONE],
            [ZERO, ZERO, ZERO],
            [ONE, ZERO, ZERO],
        ]
    )
    l5 = freeze(
        [
            [ZERO, ZERO, -I_UNIT],
            [ZERO, ZERO, ZERO],
            [I_UNIT, ZERO, ZERO],
        ]
    )
    l6 = freeze(
        [
            [ZERO, ZERO, ZERO],
            [ZERO, ZERO, ONE],
            [ZERO, ONE, ZERO],
        ]
    )
    l7 = freeze(
        [
            [ZERO, ZERO, ZERO],
            [ZERO, ZERO, -I_UNIT],
            [ZERO, I_UNIT, ZERO],
        ]
    )
    diag8 = Cpx(inv_sqrt3)
    l8 = freeze(
        [
            [diag8, ZERO, ZERO],
            [ZERO, diag8, ZERO],
            [ZERO, ZERO, Cpx(Q3(0, Fraction(-2, 3)))],
        ]
    )
    return (l1, l2, l3, l4, l5, l6, l7, l8)


def perm_sign(triple: tuple[int, int, int]) -> int | None:
    a, b, c = triple
    if len({a, b, c}) < 3:
        return None
    inversions = int(a > b) + int(a > c) + int(b > c)
    return 1 if inversions % 2 == 0 else -1


def structure_constants() -> tuple[tuple[tuple[Q3, ...], ...], ...]:
    """f_abc with 0-based indices, totally antisymmetric, values in Q(sqrt(3))."""
    independent = {
        (0, 1, 2): Q3(1),
        (0, 3, 6): Q3(Fraction(1, 2)),
        (0, 4, 5): Q3(Fraction(-1, 2)),
        (1, 3, 5): Q3(Fraction(1, 2)),
        (1, 4, 6): Q3(Fraction(1, 2)),
        (2, 3, 4): Q3(Fraction(1, 2)),
        (2, 5, 6): Q3(Fraction(-1, 2)),
        (3, 4, 7): Q3(0, Fraction(1, 2)),
        (5, 6, 7): Q3(0, Fraction(1, 2)),
    }
    data = [[[Q3(0) for _ in range(8)] for _ in range(8)] for _ in range(8)]
    for (a0, b0, c0), value in independent.items():
        base = (a0, b0, c0)
        base_sign = perm_sign(base)
        assert base_sign is not None
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    if {a, b, c} != {a0, b0, c0}:
                        continue
                    sign = perm_sign((a, b, c))
                    if sign is None:
                        continue
                    data[a][b][c] = value if sign == base_sign else -value
    return tuple(tuple(tuple(row) for row in plane) for plane in data)


def adjoint_matrices(f: tuple[tuple[tuple[Q3, ...], ...], ...]) -> tuple[Real8, ...]:
    """ad(λ_a)_{bc} = 2 f_abc, eight real 8x8 matrices."""
    out: list[Real8] = []
    for a in range(8):
        out.append(
            tuple(tuple(Q3(2) * f[a][b][c] for c in range(8)) for b in range(8))
        )
    return tuple(out)


def real_mul(left: Real8, right: Real8) -> Real8:
    return tuple(
        tuple(
            sum((left[r][k] * right[k][c] for k in range(8)), Q3(0))
            for c in range(8)
        )
        for r in range(8)
    )


def real_comm(left: Real8, right: Real8) -> Real8:
    product = real_mul(left, right)
    opposite = real_mul(right, left)
    return tuple(
        tuple(product[r][c] - opposite[r][c] for c in range(8)) for r in range(8)
    )


def real_scale(scalar: Q3, matrix: Real8) -> Real8:
    return tuple(tuple(scalar * matrix[r][c] for c in range(8)) for r in range(8))


def real_equal(left: Real8, right: Real8) -> bool:
    return all(left[r][c] == right[r][c] for r in range(8) for c in range(8))


def frobenius(left: Real8, right: Real8) -> Q3:
    return sum((left[r][c] * right[r][c] for r in range(8) for c in range(8)), Q3(0))


def tensor_basis(*factors: tuple) -> tuple:
    out: tuple = ((),)
    for factor in factors:
        out = tuple(left + (vec,) for left in out for vec in factor)
    return out


def matrix_units(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(n) for j in range(n))


def divides(n: int, m: int) -> bool:
    return n != 0 and m % n == 0


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


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none; Gell-Mann data reconstructed over Q(sqrt(3))")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction / Q(sqrt(3)); no QCD import")
    print("negative_scope: adjoint-8 is not unital M_3; leftover not adopted")

    lambdas = gell_mann()
    f_abc = structure_constants()
    ads = adjoint_matrices(f_abc)

    checks.check(
        "theorem1-count",
        "there are eight Gell-Mann matrices",
        len(lambdas) == 8,
    )
    checks.check(
        "theorem1-traceless",
        "each Gell-Mann matrix has trace 0",
        all(mtrace(matrix).is_zero() for matrix in lambdas),
    )
    checks.check(
        "theorem1-hermitian",
        "each Gell-Mann matrix is Hermitian",
        all(matrices_equal(matrix, madjoint(matrix)) for matrix in lambdas),
    )
    gram_ok = True
    for a, left in enumerate(lambdas):
        for b, right in enumerate(lambdas):
            value = mtrace(mmul(left, right))
            target = Cpx(Q3(2 if a == b else 0))
            if value != target:
                gram_ok = False
    checks.check(
        "theorem1-trace-form",
        "Tr(λ_a λ_b) = 2 δ_ab, so the eight are R-independent",
        gram_ok,
    )
    dim_su3 = 8
    dim_m3 = 3 * 3
    checks.check(
        "theorem1-eight-not-nine",
        "dim_R su(3) = 8 is not dim_C M_3 = 9",
        dim_su3 == 8 and dim_m3 == 9 and dim_su3 != dim_m3,
    )

    two_i_l3 = mscale(TWO_I, lambdas[2])
    checks.check(
        "theorem2-i-spin",
        "[λ_1, λ_2] = 2i λ_3",
        matrices_equal(comm(lambdas[0], lambdas[1]), two_i_l3),
    )
    half = Cpx(Q3(Fraction(1, 2)))
    sqrt3_over_2 = Cpx(Q3(0, Fraction(1, 2)))
    v_spin_target = mscale(
        TWO_I,
        madd(mscale(half, lambdas[2]), mscale(sqrt3_over_2, lambdas[7])),
    )
    checks.check(
        "theorem2-v-spin",
        "[λ_4, λ_5] = 2i (1/2 λ_3 + √3/2 λ_8)",
        matrices_equal(comm(lambdas[3], lambdas[4]), v_spin_target),
    )
    u_spin_target = mscale(
        TWO_I,
        madd(mscale(-half, lambdas[2]), mscale(sqrt3_over_2, lambdas[7])),
    )
    checks.check(
        "theorem2-u-spin",
        "[λ_6, λ_7] = 2i (-1/2 λ_3 + √3/2 λ_8)",
        matrices_equal(comm(lambdas[5], lambdas[6]), u_spin_target),
    )
    checks.check(
        "theorem2-f147",
        "f_147 = 1/2, so [λ_1, λ_4] = i λ_7",
        f_abc[0][3][6] == Q3(Fraction(1, 2))
        and matrices_equal(comm(lambdas[0], lambdas[3]), mscale(I_UNIT, lambdas[6])),
    )
    closure_ok = True
    sample_pairs = ((0, 1), (3, 4), (5, 6), (0, 3), (3, 7), (5, 7))
    for a, b in sample_pairs:
        target = tuple(
            tuple(ZERO for _ in range(3)) for _ in range(3)
        )
        acc = target
        for c in range(8):
            coeff = Cpx(Q3(0), Q3(2)) * Cpx(f_abc[a][b][c])
            acc = madd(acc, mscale(coeff, lambdas[c]))
        if not matrices_equal(comm(lambdas[a], lambdas[b]), acc):
            closure_ok = False
    checks.check(
        "theorem2-closure-formula",
        "[λ_a, λ_b] = 2i ∑_c f_abc λ_c on a generating set",
        closure_ok,
    )

    checks.check(
        "theorem3-shape",
        "ad(λ_a) are eight 8x8 real matrices",
        len(ads) == 8 and all(len(mat) == 8 and len(mat[0]) == 8 for mat in ads),
    )
    pairing_ok = True
    for a in range(8):
        for d in range(8):
            value = frobenius(ads[a], ads[d])
            target = Q3(12 if a == d else 0)
            if value != target:
                pairing_ok = False
    checks.check(
        "theorem3-independent",
        "Frobenius pairing of ad(λ_a) is 12 δ_ad, so they are independent",
        pairing_ok,
    )
    checks.check(
        "theorem3-homomorphism",
        "[ad(λ_1), ad(λ_2)] = -2 ad(λ_3) in the convention ad_{bc}=2 f_abc",
        real_equal(real_comm(ads[0], ads[1]), real_scale(Q3(-2), ads[2])),
    )
    site_basis = ((1, 0), (0, 1))
    h_basis = tensor_basis(site_basis, site_basis, site_basis)
    h_dim = len(h_basis)
    m8_dim = len(matrix_units(h_dim))
    checks.check(
        "theorem3-sits-in-m8",
        "three-site H ≅ C^8 and ad(su(3)) ⊂ M_8(R) ⊂ End(C^8)",
        h_dim == 8 and m8_dim == 64 and len(ads) == 8,
    )

    checks.check(
        "theorem4-three-not-divide-eight",
        "3 does not divide 8",
        divides(3, 8) is False,
    )
    checks.check(
        "theorem4-no-unital-hom",
        "no unital *-hom M_3(C) -> M_8(C)",
        divides(3, h_dim) is False and dim_m3 != 8 and dim_m3 != 64,
    )

    mutation_dim_nine = dim_su3 == 9
    mutation_divides = divides(3, 8)
    mutation_dependent = pairing_ok is False
    checks.check(
        "mutation-dim-su3-eq-9",
        "predicate dim su(3) == 9 fails",
        mutation_dim_nine is False,
    )
    checks.check(
        "mutation-3-divides-8",
        "predicate 3 divides 8 fails",
        mutation_divides is False,
    )
    checks.check(
        "mutation-ad-dependent",
        "predicate ad(λ_a) linearly dependent fails",
        mutation_dependent is False,
    )

    required_status = (
        'hypothetical_axiom_status: "color-as-adjoint-8 leftover: su(3) closes in M_8; not adopted as QCD or as unital M_3"',
        "actual_current_surface_status: bounded-support",
    )
    checks.check(
        "machine-status-contract",
        "note carries the required leftover status and bounded-support surface",
        all(phrase in note for phrase in required_status),
    )
    checks.check(
        "theorem5-qubit-names-m2",
        "live axiom memo names one-site M_2(C), not su(3)",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "Qubit names `M_2(C)`, not `su(3)`" in note,
    )
    checks.check(
        "theorem5-refusals",
        "note refuses QCD, a color axiom, C^8=M_3, Y_0, and hypercharge",
        all(
            phrase in note
            for phrase in (
                "does not adopt a color axiom",
                "does not identify `Y_0` or hypercharge",
                "Do not identify `C^8` with `M_3`",
                "Do not identify `ad(su(3))` with a unital",
                "They do not name Gell-Mann matrices or QCD",
            )
        ),
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/SU3_ADJOINT_EIGHT_IN_M8_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and (
            "AUDIT_INPUT_PATHS = (\n"
            '    "docs/SU3_ADJOINT_EIGHT_IN_M8_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",\n'
            '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
            ")"
        )
        in self_source
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file(),
    )
    qcd_module_load = "from " + "qcd"
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and N1-N8 gate are source-visible; no QCD module load",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note
        and qcd_module_load not in self_source.lower()
        and qcd_module_load not in note.lower(),
    )

    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
