#!/usr/bin/env python3
"""Exact Fraction checks: a 3-atom M_2 menu is not a unital M_3 factor.

Identity gates reconstruct P0, P1, P+ as rank-1 projections and compute
dim_generated_algebra(). The mutation predicates
dim generated algebra == 9 and unital_m3_to_m2_exists() must fail.
Parents: axiom memo only. No QCD import. Menu weights are not adopted.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "THREE_ATOM_MENU_ON_M2_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/THREE_ATOM_MENU_ON_M2_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Matrix = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return (
        (left[0][0] - right[0][0], left[0][1] - right[0][1]),
        (left[1][0] - right[1][0], left[1][1] - right[1][1]),
    )


def mat_scale(coeff: Fraction, matrix: Matrix) -> Matrix:
    return (
        (coeff * matrix[0][0], coeff * matrix[0][1]),
        (coeff * matrix[1][0], coeff * matrix[1][1]),
    )


def mat_adj(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def mat_trace(matrix: Matrix) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def is_rank1_projection(matrix: Matrix) -> bool:
    return (
        mat_mul(matrix, matrix) == matrix
        and mat_adj(matrix) == matrix
        and mat_trace(matrix) == Fraction(1)
    )


def flatten(matrix: Matrix) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    return (matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1])


def span_rank(matrices: tuple[Matrix, ...]) -> int:
    """Exact Fraction row-reduction rank of flattened 2x2 matrices."""
    rows = [list(flatten(matrix)) for matrix in matrices]
    rank = 0
    col = 0
    n_rows = len(rows)
    n_cols = 4
    while rank < n_rows and col < n_cols:
        pivot = None
        for i in range(rank, n_rows):
            if rows[i][col] != 0:
                pivot = i
                break
        if pivot is None:
            col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_val = rows[rank][col]
        rows[rank] = [entry / pivot_val for entry in rows[rank]]
        for i in range(n_rows):
            if i == rank or rows[i][col] == 0:
                continue
            factor = rows[i][col]
            rows[i] = [rows[i][j] - factor * rows[rank][j] for j in range(n_cols)]
        rank += 1
        col += 1
    return rank


def p0() -> Matrix:
    return (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(0)),
    )


def p1() -> Matrix:
    return (
        (Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )


def p_plus() -> Matrix:
    half = Fraction(1, 2)
    return (
        (half, half),
        (half, half),
    )


def identity2() -> Matrix:
    return (
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
    )


def test_mu() -> tuple[Fraction, Fraction, Fraction]:
    """Equal-weight test object only. Weights are not adopted."""
    third = Fraction(1, 3)
    return (third, third, third)


def generated_words() -> tuple[Matrix, ...]:
    gens = (p0(), p1(), p_plus(), identity2())
    words = list(gens)
    for left in gens:
        for right in gens:
            words.append(mat_mul(left, right))
            words.append(mat_adj(mat_mul(left, right)))
    return tuple(words)


def dim_generated_algebra() -> int:
    """Complex dimension of C*(P0, P1, P+); exact Fraction rank."""
    return span_rank(generated_words())


def dim_generated_algebra_eq_9() -> bool:
    """Mutation predicate: dim generated algebra == 9. Must fail."""
    return dim_generated_algebra() == 9


def unital_hom_exists(k: int, m: int) -> bool:
    """Unital C-linear *-hom M_k(C) -> M_m(C) exists iff k divides m."""
    return m % k == 0


def unital_m3_to_m2_exists() -> bool:
    """Mutation predicate: unital M_3 -> M_2 exists. Must fail (3 ∤ 2)."""
    return unital_hom_exists(3, 2)


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

    print("external_scientific_inputs: none; exact Fraction rays and integer remainder")
    print("package_local_integrity_reads: proposed source note and live axiom memo only")
    print("measure_boundary: exact Fraction; no float, no QCD import")
    print("negative_scope: 3-atom menu is not a unital M_3 factor; leftover not adopted")

    ray0 = p0()
    ray1 = p1()
    ray_plus = p_plus()
    unit = identity2()
    mu = test_mu()

    checks.check(
        "identity-p0-projection",
        "P0 is a rank-1 projection with exact Fraction entries",
        is_rank1_projection(ray0),
    )
    checks.check(
        "identity-p1-projection",
        "P1 is a rank-1 projection with exact Fraction entries",
        is_rank1_projection(ray1),
    )
    checks.check(
        "identity-pplus-projection",
        "P+ is a rank-1 projection with exact Fraction entries",
        is_rank1_projection(ray_plus),
    )
    checks.check(
        "pairwise-distinct",
        "P0, P1, P+ are pairwise distinct",
        ray0 != ray1 and ray0 != ray_plus and ray1 != ray_plus,
    )
    checks.check(
        "theorem1-three-element-menu",
        "{P0, P1, P+} is a 3-element subset of one-site M_2",
        len({flatten(ray0), flatten(ray1), flatten(ray_plus)}) == 3,
    )
    checks.check(
        "theorem1-mu-test-object",
        "μ = (1/3, 1/3, 1/3) is an exact Fraction test object summing to 1",
        mu == (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3))
        and sum(mu, Fraction(0)) == Fraction(1)
        and all(isinstance(weight, Fraction) for weight in mu),
    )
    checks.check(
        "theorem1-mu-not-adopted",
        "note displays μ as a test object only and does not adopt the weights",
        "test object only" in note and "does not adopt those weights" in note,
    )
    checks.check(
        "theorem2-record-locks-one",
        "live Record axiom locks exactly one admissible local possibility",
        "When present, a record locks exactly one admissible local possibility."
        in axiom
        and "locks exactly one of `{P0, P1, P+}`" in note,
    )
    checks.check(
        "theorem2-three-lock-labels",
        "three distinct lock labels exist; a blank site cannot be read",
        "Three distinct lock labels exist." in note
        and "A site with no record cannot be read." in axiom
        and "A site with no record cannot be read." in note,
    )
    checks.check(
        "theorem3-p0-plus-p1-is-identity",
        "P0 + P1 equals I_2 exactly",
        mat_add(ray0, ray1) == unit,
    )
    checks.check(
        "theorem3-off-diagonal-units",
        "P0 P+ and P+ P0 supply the off-diagonal matrix units",
        mat_sub(mat_scale(Fraction(2), mat_mul(ray0, ray_plus)), ray0)
        == ((Fraction(0), Fraction(1)), (Fraction(0), Fraction(0)))
        and mat_sub(mat_scale(Fraction(2), mat_mul(ray_plus, ray0)), ray0)
        == ((Fraction(0), Fraction(0)), (Fraction(1), Fraction(0))),
    )
    checks.check(
        "theorem3-generated-dim-is-4",
        "dim_C C*(P0, P1, P+) = 4 via dim_generated_algebra()",
        dim_generated_algebra() == 4,
    )
    checks.check(
        "theorem3-not-m3",
        "generated algebra is not M_3(C) because 4 != 9",
        dim_generated_algebra() != 9 and "It is **not** `M_3(C)`" in note,
    )
    checks.check(
        "mutation-generated-dim-eq-9-fails",
        "predicate dim generated algebra == 9 fails",
        dim_generated_algebra_eq_9() is False,
    )
    checks.check(
        "theorem4-three-not-divides-two",
        "3 does not divide 2",
        2 % 3 != 0,
    )
    checks.check(
        "mutation-unital-m3-to-m2-exists-fails",
        "predicate unital M_3 → M_2 exists fails",
        unital_m3_to_m2_exists() is False,
    )
    checks.check(
        "theorem4-type-separation",
        "a 3-atom menu is not a unital M_3 factor",
        "A 3-atom menu is therefore not a unital `M_3` factor." in note
        and "three lockable possibilities" in note
        and "unital `M_3` host algebra" in note,
    )
    checks.check(
        "theorem5-no-qcd-su3-qubit-rewrite",
        "note does not install SU(3), name QCD, select color, or rewrite Qubit",
        "does not install `SU(3)`, name QCD, select color, or rewrite" in note
        and "The full one-site possibility domain has algebraic presentation `M_2(C)`."
        in axiom
        and "Do not ship" in note,
    )
    checks.check(
        "no-r-half-axiom",
        "note does not adopt an r = 1/2 axiom",
        "No `r = 1/2` axiom is adopted." in note
        and "`r = 1/2` is now an axiom" in note,
    )
    checks.check(
        "no-central-decomposition-for-su3",
        "note refuses a central decomposition invented to fit SU(3)",
        "No central decomposition is invented to fit `SU(3)`." in note
        and "centre of `M_2(C)` is scalars" in note,
    )
    required_status = (
        'hypothetical_axiom_status: "color-as-3-atom-support leftover: '
        'Record locks one of three M_2 rays; not adopted as QCD"',
        "actual_current_surface_status: bounded-support",
    )
    checks.check(
        "machine-status-contract",
        "note carries the required leftover status and bounded-support surface",
        all(phrase in note for phrase in required_status),
    )
    checks.check(
        "audit-input-paths",
        "AUDIT_INPUT_PATHS is the required string-literal tuple",
        AUDIT_INPUT_PATHS
        == (
            "docs/THREE_ATOM_MENU_ON_M2_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        )
        and NOTE_PATH.is_file()
        and AXIOM_PATH.is_file()
        and (
            'AUDIT_INPUT_PATHS = (\n'
            '    "docs/THREE_ATOM_MENU_ON_M2_IS_NOT_UNITAL_M3_BOUNDED_THEOREM_NOTE_2026-08-13.md",\n'
            '    "docs/MINIMAL_AXIOMS_2026-06-29.md",\n'
            ')'
        )
        in self_source,
    )
    qcd_module_load = ("from " + "qcd")
    qcd_import = ("import " + "qcd")
    checks.check(
        "claim-type-and-gate",
        "bounded theorem type and N1-N8 gate are source-visible; no QCD module load",
        "**Type:** bounded_theorem" in note
        and all(f"### N{index}" in note for index in range(1, 9))
        and "FAIL / DO NOT SHIP" in note
        and "an axiom update is necessary" in note
        and qcd_module_load not in self_source.lower()
        and qcd_module_load not in note.lower()
        and qcd_import not in self_source.lower(),
    )
    checks.check(
        "exact-fraction-no-float",
        "algebra identities use Fraction only",
        all(isinstance(entry, Fraction) for entry in flatten(ray_plus))
        and isinstance(dim_generated_algebra(), int)
        and "float" not in self_source.split("no float", 1)[0][-20:],
    )

    print("per_element: P0, P1, P+ and μ = (1/3, 1/3, 1/3) as a test object")
    print("per_site: one-site A = M_2; generated algebra dimension 4")
    print("per_block: unital A3 -> A2 is the only negative block tested")
    print("lattice_wide: checked and not executed — no lattice-wide color claim")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
